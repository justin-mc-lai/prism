#!/usr/bin/env bash
# prism-manga-asset-gate-v1 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-MAG-001 distill reference in director refs
test -f skills/prism-director/references/asset-consistency-gate.md || fail "distill ref missing"
for pat in "身份" "变体" "镜头瞬态" "识别锚点" "CON-01" "CON-04" "AST-05" "画风统一" "lumenx" "drama-skills"; do
  rg -q "$pat" skills/prism-director/references/asset-consistency-gate.md || fail "distill lacks $pat"
done

# AC-MAG-002 gate contract seven sections + fail-closed codes
test -f contracts/asset-consistency.contract.md || fail "gate contract missing"
for pat in identity "决策边界" intake output gate handoff "失败处理" "asset_identity_missing" "禁止自证通过"; do
  rg -q "$pat" contracts/asset-consistency.contract.md || fail "gate contract lacks $pat"
done

# AC-MAG-003 manga_drama wiring (intake anchor + gate upgrade)
rg -q "asset-consistency.contract" contracts/form-manga-drama.contract.md || fail "manga contract lacks gate ref"
rg -q "识别锚点|未决项不得流入分镜" contracts/form-manga-drama.contract.md || fail "manga intake lacks anchor rule"

# AC-MAG-004 registry chain mentions the gate
rg -q "资产一致性门.*asset-consistency" registry/form-registry.yaml || fail "registry chain lacks gate step"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); m=[f for f in d['forms'] if f['form']=='manga_drama']; assert m and 'asset-consistency' in m[0]['producer_chain']" || fail "registry manga_drama chain invalid"

# AC-MAG-007 inventory A4 standing decision note
rg -q "MoneyPrinterTurbo.*defer-pin|defer-pin.*MoneyPrinterTurbo" registry/source-capability-inventory.md || fail "inventory lacks defer-pin decision"

# upstream runtime not pinned
test ! -d vendor/skills/lumenx || fail "lumenx runtime must not be pinned"
test ! -d vendor/skills/dramaclaw || fail "dramaclaw must not be pinned (Elastic-2.0)"

# AC-RLO-001..003 rollout wiring (prism-asset-gate-rollout-v1)
rg -q "资产一致性门" contracts/form-live-drama.contract.md || fail "live_drama contract lacks gate ref"
rg -q "asset-consistency.contract" contracts/form-live-drama.contract.md || fail "live_drama contract lacks gate path"
rg -q "资产一致性|asset-consistency" contracts/form-av.contract.md || fail "form-av comic lacks gate ref"
python3 - << 'PYEOF' || fail "registry rollout chains invalid"
import yaml
d = yaml.safe_load(open("registry/form-registry.yaml"))
c = {f["form"]: f["producer_chain"] for f in d["forms"]}
assert "asset-consistency" in c["live_drama"], "live_drama chain"
assert "asset-consistency" in c["comic"], "comic chain"
# vlog / book_video must NOT be wired (Non-goal boundary)
assert "asset-consistency" not in c["vlog"], "vlog must stay unwired"
assert "asset-consistency" not in c["book_video"], "book_video must stay unwired"
PYEOF

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

# AC-MAG-008..010 资产三类（characters/scenes/props）+ 声音链（prism-manga-asset-three-class-v1）
SCHEMA=content/pipelines/ai-manga-drama/storyboard-schema.json
CLI=scripts/ai_manga_drama.py
test -f "$SCHEMA" || fail "storyboard-schema missing"
for pat in '"characters"' '"scenes"' '"props"' '"interior"' '"exterior"' '"holder"' 'scene_ref' 'prop_refs'; do
  rg -q -- "$pat" "$SCHEMA" || fail "storyboard-schema lacks $pat"
done
# 三类字段在 CLI 校验里真实生效（不是只写进 schema）
for pat in "_validate_entities" "not in characters" "not in scenes" "not in props" "kind must be interior|exterior"; do
  rg -q -- "$pat" "$CLI" || fail "CLI validate lacks $pat"
done
# 渲染链：provider-only + 无兜底（prism-prompt-compiler-v1，2026-09-21 refreeze）
for pat in "RENDER_STAGE_ENVS" "resolve_stage_credential" "required_clip_paths" "no_local_fallback" "provider-only" "TARGET_RESOLUTION" "missing_credential"; do
  rg -q -- "$pat" "$CLI" || fail "CLI render chain lacks $pat"
done
# 本地兜底符号必须已删除（真反断言：不是注释，是标识符）
for pat in VOICE_PROVIDERS resolve_edge_tts synth_voice EDGE_TTS_CANDIDATES DEFAULT_VOICE_ID SUBTITLE_MODES zoompan allow_audio_overflow DRAFT_KENBURNS build_srt has_audio_stream; do
  rg -q -- "$pat" "$CLI" && fail "CLI still contains removed local-fallback symbol: $pat"
done
# ref_image 字段接线（schema + CLI 双向）
rg -q '"ref_image"' "$SCHEMA" || fail "schema lacks ref_image"
rg -q "ref_image" "$CLI" || fail "CLI lacks ref_image validation"
rg -q "_check_ref_image" "$CLI" || fail "CLI lacks _check_ref_image"
# storyworld schema 三类落盘目录
rg -q "characters/" contracts/storyworld.schema.yaml || fail "storyworld lacks characters/"
rg -q "scenes/" contracts/storyworld.schema.yaml || fail "storyworld lacks scenes/"
rg -q "props/" contracts/storyworld.schema.yaml || fail "storyworld lacks props/"
# 提取 mode 接线
for f in skills/prism-master/SKILL.md skills/prism-master/references/modes/INDEX.md skills/prism-master/references/skill-ir.md; do
  rg -q "extract-storyworld" "$f" || fail "master extract wiring lacks extract-storyworld in $f"
done
rg -q "storyworld-extraction" skills/prism-master/references/modes/extract-storyworld.md || fail "mode lacks storyworld-extraction ref"
rg -q "未决" skills/prism-master/references/storyworld-extraction.md || fail "extraction ref lacks 未决 rule"

pass "check_asset_consistency: all prism-manga-asset-gate-v1 gates PASS"
