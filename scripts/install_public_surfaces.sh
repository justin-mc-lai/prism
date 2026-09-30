#!/bin/bash
# Prism public-surface installer for agent skill roots.
#
# 只软链指令面：本脚本只装 7 个公开 SKILL.md（指令面），能力面（scripts/、
# content/pipelines/ 等）不随装、项目内零脚本副本；项目侧一律经 PRISM_HOME
# （= Prism 仓根）调用：$PRISM_HOME/scripts/<tool>。
#
# Links the 7 public surfaces (skills/prism-{goal,intel,master,director,produce,qa,release})
# into agent skill dirs so Codex / Claude / generic agents / Cursor can discover them.
# `skills/_internal` is never exposed (repo rule: 不对人发现).
#
# Idempotent. Options: --dry-run | --uninstall
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/skills"

DRY_RUN=0
UNINSTALL=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --uninstall) UNINSTALL=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

# Public surface ids from the registry, in canonical order.
PUBLIC_IDS=(goal intel master director produce qa release)

ROOTS=(
  "$HOME/.codex/skills"
  "$HOME/.claude/skills"
  "$HOME/.agents/skills"
  "$HOME/.cursor/skills"
  "$HOME/.gemini/config/skills"
  "$ROOT/.agents/skills"
  "$ROOT/../.agents/skills"
  "$ROOT/.cursor/skills"
)

mode=install
[ "$UNINSTALL" = "1" ] && mode=uninstall
echo "prism public-surface $mode (dry-run=$DRY_RUN)"
echo "  source: $SRC"

do_link() {
  local name="$1" target="$2" src_path="$SRC/$name"
  # Repo-local roots use portable relative links; home roots use absolute links.
  case "$target" in
    "$ROOT"/*) src_path="$(python3 -c "import os,sys; print(os.path.relpath('$SRC/$name','$(dirname "$target")'))")" ;;
  esac
  if [ "$UNINSTALL" = "1" ]; then
    if [ -L "$target" ]; then
      echo "  rm $target"
      if [ "$DRY_RUN" = "0" ]; then rm "$target"; fi
    elif [ -e "$target" ]; then
      echo "  skip $target (not a symlink; not touching)"
    fi
    return
  fi
  # 分类：悬空 symlink / 指向他处的陈旧 symlink / 已正确的 symlink / 非 symlink / 不存在
  local action="link" actual=""
  if [ -L "$target" ]; then
    actual="$(readlink "$target")"
    if [ ! -e "$target" ]; then
      action="relink-dangling"
    elif [ "$actual" != "$src_path" ]; then
      action="relink-stale"
    else
      action="skip"
    fi
  elif [ -e "$target" ]; then
    echo "  skip $target (not a symlink; not touching)"
    return
  fi
  case "$action" in
    skip)
      echo "  exists $target (skip)"
      ;;
    link)
      if [ "$DRY_RUN" = "0" ]; then mkdir -p "$(dirname "$target")"; fi
      echo "  link $name -> $target ($src_path)"
      if [ "$DRY_RUN" = "0" ]; then ln -s "$src_path" "$target"; fi
      ;;
    *)
      echo "  $action $target (was -> $actual)"
      if [ "$DRY_RUN" = "0" ]; then rm "$target"; mkdir -p "$(dirname "$target")"; ln -s "$src_path" "$target"; fi
      ;;
  esac
}

for id in "${PUBLIC_IDS[@]}"; do
  name="prism-$id"
  [ -f "$SRC/$name/SKILL.md" ] || { echo "missing SKILL.md for $name" >&2; exit 1; }
  for root in "${ROOTS[@]}"; do
    do_link "$name" "$root/$name"
  done
done

echo "done. New links take effect on the agent's next session/reload."
