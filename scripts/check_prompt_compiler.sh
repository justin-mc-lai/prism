#!/usr/bin/env bash
# prism-prompt-compiler-v1 · 编译器确定性门（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

COMPILER=scripts/prompt_compiler.py
FX=content/pipelines/ai-manga-drama/fixtures/ep-compile-test
OVERLAY=registry/style-presets.yaml
BASE=content/pipelines/ai-manga-drama/lumenx-style-presets.json

# AC-PPC-002a 编译器在位 + 关键结构
test -f "$COMPILER" || fail "$COMPILER missing"
for pat in "load_presets" "ref_safe_style" "asset_prompt" "image_prompt" "video_prompt" "build_srt" "DRAMA_LIGHT_TOKENS" "CLASS_LAYOUT"; do
  rg -q "$pat" "$COMPILER" || fail "compiler lacks $pat"
done

# AC-PPC-002b fixture 在位
test -f "$FX/storyboard.json" || fail "fixture storyboard missing"
test -f "$FX/assets/char-01-lin.png" || fail "fixture ref image missing"

# AC-PPC-002c 风格合并：base + overlay 无冲突，且 29 预设可枚举
python3 - << 'PYEOF' || fail "style merge invalid"
import json, yaml
base = json.load(open("content/pipelines/ai-manga-drama/lumenx-style-presets.json"))
ov = yaml.safe_load(open("registry/style-presets.yaml"))
bids = {p["id"] for p in base["presets"]}
oids = {p["id"] for p in ov["presets"]}
assert not (bids & oids), f"id collision: {bids & oids}"
assert len(bids | oids) == 29, f"expected 29 presets, got {len(bids|oids)}"
PYEOF
n="$(python3 "$COMPILER" --episode "$FX" --style x --list-styles | wc -l | tr -d ' ')"
test "$n" = "29" || fail "expected 29 listable styles, got $n"

# AC-PPC-002d 编译成功 + 四产物齐备
python3 "$COMPILER" --episode "$FX" --style gongbi_heavy_color > /dev/null
for f in 资产提示词.md 图片提示词.md 视频提示词.md ep-compile-test.srt; do
  test -s "$FX/$f" || fail "compiler output missing/empty: $f"
done

# AC-PPC-002e 确定性：两次编译逐字节一致
TMP="$(mktemp -d)"
for f in 资产提示词.md 图片提示词.md 视频提示词.md ep-compile-test.srt; do cp "$FX/$f" "$TMP/"; done
python3 "$COMPILER" --episode "$FX" --style gongbi_heavy_color > /dev/null
for f in 资产提示词.md 图片提示词.md 视频提示词.md ep-compile-test.srt; do
  cmp -s "$TMP/$f" "$FX/$f" || fail "compiler not deterministic: $f"
done
rm -rf "$TMP"

# AC-PPC-002f 产物内容：7 段 identity block + ref-safe（无戏剧光污染）
for tag in '\[IDENTITY\]' '\[BODY\]' '\[LAYOUT\]' '\[STYLE\]' '\[NEGATIVE\]'; do
  rg -q -- "$tag" "$FX/资产提示词.md" || fail "asset prompt lacks segment $tag"
done
rg -q "neutral studio lighting flat even" "$FX/资产提示词.md" || fail "asset prompt lacks neutral flat lighting"
rg -qi "cinematic lighting|lens flare|chiaroscuro" "$FX/资产提示词.md" && fail "asset prompt leaked drama-light token"
# 每镜图片提示词 8 段
for tag in '\[CHARACTER\]' '\[BACKGROUND\]' '\[ACTION\]' '\[SCENE\]' '\[LIGHT\]' '\[TEXT\]'; do
  rg -q -- "$tag" "$FX/图片提示词.md" || fail "image prompt lacks segment $tag"
done
rg -q "这里还有人吗" "$FX/图片提示词.md" || fail "image prompt lost dialogue (must be verbatim)"
rg -q "这里还有人吗" "$FX/ep-compile-test.srt" || fail "srt lost dialogue"
rg -q "SHOT" "$FX/视频提示词.md" || fail "video prompt lacks SHOT"

# AC-PPC-002g 未知风格 fail-closed
python3 "$COMPILER" --episode "$FX" --style no_such_style > /dev/null 2>&1 && fail "unknown style did not fail closed"

pass "check_prompt_compiler: all prism-prompt-compiler-v1 compiler gates PASS"
