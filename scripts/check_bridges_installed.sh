#!/usr/bin/env bash
# Bridge/pin availability gate（真实断言）
# - 29 个 skill 全部 pin 进 vendor/skills/（A4+A5，2026-08-15），bridge 数量清零
# - rnskill 96M skills 子树为唯一 archive-only 回源引用（CC BY-NC 非商业合规）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }

# 1. pinned 条目完整性
# 三种合法 pin 形状：
#   a) 扁平 skill：顶层 SKILL.md
#   b) monorepo skill：子树含 SKILL.md（如 drama-skills / shuohao-skills / su-ai-short-drama）
#   c) 提示词语料 pin：无 SKILL.md，但有 prompt.md / README.md（如 short-drama-skills）
SKILL_PINS=0
CORPUS_PINS=0
for d in vendor/skills/*/; do
  if test -f "${d}SKILL.md" || find "$d" -maxdepth 3 -name SKILL.md -print -quit 2>/dev/null | grep -q .; then
    SKILL_PINS=$((SKILL_PINS + 1))
  elif find "$d" -maxdepth 4 \( -name 'prompt.md' -o -name 'README.md' \) -print -quit 2>/dev/null | grep -q .; then
    CORPUS_PINS=$((CORPUS_PINS + 1))
  else
    fail "pinned entry has neither SKILL.md nor corpus docs: $d"
  fi
done
test "$SKILL_PINS" -ge 29 || fail "skill pins <29 (got $SKILL_PINS)"
echo "PASS: $SKILL_PINS skill pins + $CORPUS_PINS corpus pins in vendor/skills/"

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
