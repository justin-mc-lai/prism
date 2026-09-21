#!/usr/bin/env bash
# prism-prompt-compiler-v1 · 渲染交接去兜底门（真实断言 + 负例执行：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

CON=contracts/asset-render.contract.md
REG=registry/render-adapters.yaml
CLI=scripts/ai_manga_drama.py
FX=content/pipelines/ai-manga-drama/fixtures/ep-compile-test

# ── 1. asset-render 契约七节 + fail-closed 码 ────────────────────────────
test -f "$CON" || fail "$CON missing"
for pat in identity 决策边界 intake output gate handoff 失败处理 gate_id "asset-render" "fail-closed" "禁止自证通过" provider-only; do
  rg -q "$pat" "$CON" || fail "asset-render.contract lacks $pat"
done
for pat in render_storyboard_invalid render_ref_unresolved render_style_unknown render_compile_missing; do
  rg -q "$pat" "$CON" || fail "asset-render.contract lacks reason_code $pat"
done
rg -q "credentials_never_in_repo" "$CON" || fail "asset-render.contract lacks credential guard"

# ── 2. render-adapters 登记：四阶段 + 守卫 ───────────────────────────────
test -f "$REG" || fail "$REG missing"
python3 - << 'PYEOF' || fail "render-adapters structure invalid"
import yaml
d = yaml.safe_load(open("registry/render-adapters.yaml"))
stages = [a["stage"] for a in d["adapters"]]
assert stages == ["t2i", "i2v", "t2v", "tts"], f"stages: {stages}"
for a in d["adapters"]:
    assert a["strategy"] == "provider_only", f"{a['stage']} not provider_only"
    assert a["credential_env"].startswith("PRISM_"), f"{a['stage']} credential_env"
    assert a["fail_closed"] is True, f"{a['stage']} not fail_closed"
g = d["guards"]
for k in ("credentials_never_in_repo", "no_local_fallback", "missing_credential_terminates",
          "missing_clip_terminates", "provider_only_manifest"):
    assert g.get(k) is True, f"guard {k} missing"
assert g["clip_spec_enforced"] == "480x854"
PYEOF

# ── 3. 契约/路由同步 ─────────────────────────────────────────────────────
rg -q "asset-render.contract" contracts/form-manga-drama.contract.md || fail "manga contract lacks asset-render ref"
rg -q "无兜底|不做任何降级|无本地兜底" contracts/form-manga-drama.contract.md || fail "manga contract lacks no-fallback clause"
python3 - << 'PYEOF' || fail "registry manga_drama chain not synced"
import yaml
d = yaml.safe_load(open("registry/form-registry.yaml"))
m = [f for f in d["forms"] if f["form"] == "manga_drama"][0]
c = m["producer_chain"]
assert "prompt_compiler" in c, "chain lacks compile step"
assert "asset-render" in c, "chain lacks asset-render gate"
assert "provider-only" in c, "chain lacks provider-only"
assert "kenburns" not in c, "chain still mentions kenburns"
assert "asset_render" in d["shared_gates"], "shared_gates lacks asset_render"
PYEOF
rg -q "provider-only" content/pipelines/ai-manga-drama/README.md || fail "pipeline README lacks provider-only"
rg -qi "kenburns 降级|assemble --mode kenburns" content/pipelines/ai-manga-drama/README.md && fail "pipeline README still documents kenburns fallback"
rg -q "manga_drama 漫剧" skills/_internal/orchestration/creation-mode-map.md || fail "creation-mode-map lacks manga_drama row"
rg -q "provider-only" skills/_internal/orchestration/creation-mode-map.md || fail "creation-mode-map lacks provider-only"

# ── 4. CLI 反断言：本地兜底符号已删 ──────────────────────────────────────
for pat in VOICE_PROVIDERS resolve_edge_tts synth_voice EDGE_TTS_CANDIDATES SUBTITLE_MODES zoompan allow_audio_overflow DRAFT_KENBURNS build_srt has_audio_stream; do
  if rg -q -- "$pat" "$CLI"; then fail "CLI still contains removed local-fallback symbol: $pat"; fi
done

# ── 5. 负例执行：无凭证 / 未编译 / 缺片段 都必须终止 ─────────────────────
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cp "$FX/storyboard.json" "$TMP/"
cp -r "$FX/assets" "$TMP/"

# 5a. 无凭证 → request 必须 exit≠0，且不得产出成片
if env -u PRISM_T2I_KEY -u PRISM_I2V_KEY -u PRISM_T2V_KEY -u PRISM_TTS_KEY \
       -u FAL_KEY -u REPLICATE_API_TOKEN -u SILICONFLOW_API_KEY \
       python3 "$CLI" request --episode "$TMP" > /dev/null 2>&1; then
  fail "request succeeded without credential (must fail closed)"
fi
if rg -q '"status": "READY"' "$TMP/video-manifest.json" 2>/dev/null; then
  fail "manifest claims READY without credential"
fi

# 5b. 未过编译器 → assemble 必须 exit≠0
if python3 "$CLI" assemble --episode "$TMP" > /dev/null 2>&1; then
  fail "assemble ran without compiler artifacts (illegal transition)"
fi

# 5c. 编译后但缺 provider 片段 → assemble 必须 exit≠0，且不得产出成片
python3 scripts/prompt_compiler.py --episode "$TMP" --style cinematic_realism > /dev/null
if python3 "$CLI" assemble --episode "$TMP" > /dev/null 2>&1; then
  fail "assemble synthesized without provider clips (fallback regression)"
fi
test ! -f "content/renders/ai-manga-drama/draft/$(python3 -c "import json;print(json.load(open('$TMP/storyboard.json'))['episode'])")-480p.mp4" \
  || fail "a fake render was produced without provider clips"

pass "check_render_handoff: all provider-only / no-fallback gates PASS"
