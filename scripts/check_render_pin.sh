#!/usr/bin/env bash
# Render-chain pin gate（A1 MIT · 真实断言：pin 产物存在、可运行、可渲染）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# 1. ATTRIBUTION 与决策记录
test -f docs/ATTRIBUTION-render-chain.md || fail "ATTRIBUTION-render-chain.md missing"
rg -q "A1" docs/owner-license-decision.md || fail "owner decision A1 not recorded"

# 2. pin 脚本齐全且语法有效
for f in \
  scripts/render_wechat_html_cards.py scripts/render_wechat_image_cards.py \
  scripts/render_wechat_article_pages.py scripts/render_spec_kit_wechat_cards.py \
  scripts/render_superpowers_wechat_cards.py scripts/kushi_cover_text_overlay.py \
  scripts/render_xhs_cover.py scripts/render-channel.sh \
  scripts/lib/kit_render.py scripts/lib/rewrite-render-asset-refs.py; do
  test -f "$f" || fail "pinned script missing: $f"
done
for f in scripts/render_*.py scripts/kushi_cover_text_overlay.py scripts/lib/kit_render.py scripts/lib/rewrite-render-asset-refs.py; do
  python3 -m py_compile "$f" || fail "compile fail: $f"
done
bash -n scripts/render-channel.sh || fail "render-channel.sh syntax"

# 3. templates 齐全
for d in kushi-wechat-image-post kushi-wechat-article-post wechat-card-kit jieqi-yangsheng-classical; do
  test -d "templates/$d" || fail "template dir missing: $d"
done

# 4. 渲染 smoke：渲染 2 张卡到 /tmp，断言 PNG 产出且非空
SMOKE_OUT="/tmp/prism-render-smoke"
rm -rf "$SMOKE_OUT"
python3 scripts/render_wechat_html_cards.py \
  --cards content/presentations/oss-picks/anydoc/image-post-beginner/cards.yaml \
  --output-dir "$SMOKE_OUT" --html-dir "$SMOKE_OUT/html" --skip-cover-roles "" >/dev/null 2>&1 \
  || fail "render smoke failed"
test -f "$SMOKE_OUT/01-cover.png" || fail "smoke cover missing"
test -f "$SMOKE_OUT/06-action.png" || fail "smoke action card missing"
size=$(stat -f%z "$SMOKE_OUT/01-cover.png")
test "$size" -gt 50000 || fail "smoke cover suspiciously small ($size bytes)"

# 5. 样本已渲染 + OCR 记录
test -f content/presentations/oss-picks/anydoc/image-post-beginner/rendered/06-action.png \
  || fail "sample rendered card missing"
rg -q "ocr_gate: pass" content/presentations/oss-picks/anydoc/image-post-beginner/manifest.yaml \
  || fail "sample ocr_gate not recorded"

rm -rf "$SMOKE_OUT"
pass "check_render_pin: render-chain pin gates PASS"
