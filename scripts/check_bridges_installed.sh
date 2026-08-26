#!/usr/bin/env bash
# Bridge/pin availability gate（真实断言）
# - 29 个 skill 全部 pin 进 vendor/skills/（A4+A5，2026-08-15），bridge 数量清零
# - rnskill 96M skills 子树为唯一 archive-only 回源引用（CC BY-NC 非商业合规）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }

# 1. pinned 29 个（vendor/skills/ 存在 + SKILL.md）
PINNED_COUNT=0
for d in vendor/skills/*/; do
  test -f "$d/SKILL.md" || fail "pinned skill missing SKILL.md: $d"
  PINNED_COUNT=$((PINNED_COUNT + 1))
done
test "$PINNED_COUNT" -ge 29 || fail "pinned skills <29 (got $PINNED_COUNT)"
echo "PASS: $PINNED_COUNT skills pinned in vendor/skills/"

# 2. 守卫文件齐备（rnskill 非商业 + de-ai NOTICE）
test -f vendor/skills/rnskill/NOTICE.md || fail "rnskill NOTICE missing"
rg -q "非商业" vendor/skills/rnskill/NOTICE.md || fail "rnskill non-commercial guard missing"
test -f vendor/skills/de-ai-prompt-enhancer/NOTICE.md || fail "de-ai NOTICE missing"

# 3. 各 skill root 不应再有指向源仓的 symlink（已全部 pin）
for root in "$HOME/.codex/skills" "$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.cursor/skills"; do
  stale=$(find "$root" -maxdepth 1 -type l -lname '*selfmedia-creator*' 2>/dev/null | wc -l | tr -d ' ')
  test "$stale" = "0" || fail "stale source symlinks in $root: $stale"
done
echo "PASS: no source-repo symlinks in skill roots"

echo "PASS: bridge availability gate (29 pinned, 0 bridged, 0 source symlinks)"
