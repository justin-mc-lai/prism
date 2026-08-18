#!/usr/bin/env bash
# Prism generic bridge installer (source-repo bridges by category).
#
# Categories:
#   全部 29 个 bridge 已 pin 进 vendor/skills/（A4+A5 · 2026-08-15），bridge 清零。
#   本脚本保留为 archive-only 兼容入口；rnskill 96M skills 子树为非商业 archive 引用。
#
# Platform/credential bridges（platform:getWechatGzhStats 等）不在此安装：
# 需要受管 secrets，缺失时 fail-closed。
#
# Source repo may be overridden with SELFMEDIA_SOURCE.
# NOTE: 源仓已归档（ARCHIVED.md，2026-08-14）为只读 archive；本脚本保留作为
# archive-only 回源通道，直到 bridge 全部蒸馏/替换完成。
# Idempotent. Options: --dry-run | --uninstall | --category <name>（默认全部）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="${SELFMEDIA_SOURCE:-/Users/apple/Developer/Personal/products/selfmedia-creator}"

DRY_RUN=0
UNINSTALL=0
CATEGORY="all"
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --category) CATEGORY="__next__" ;;
    --category=*) CATEGORY="${arg#--category=}" ;;
    *)
      if [ "$CATEGORY" = "__next__" ]; then CATEGORY="$arg"; else echo "unknown arg: $arg" >&2; exit 2; fi
      ;;
  esac
done

category_ids() {
  case "$1" in
    writing) echo "" ;;
    intel) echo "" ;;
    visual) echo "" ;;
    publish) echo "" ;;
    *) echo "" ;;
  esac
}

ROOTS=(
  "$HOME/.codex/skills"
  "$HOME/.claude/skills"
  "$HOME/.agents/skills"
  "$HOME/.cursor/skills"
)

if [ ! -d "$SOURCE/skills" ]; then
  echo "bridge source not found: $SOURCE/skills (set SELFMEDIA_SOURCE to the selfmedia-creator repo)" >&2
  exit 1
fi

mode=install
[ "$UNINSTALL" = "1" ] && mode=uninstall
echo "prism bridges $mode (category=$CATEGORY dry-run=$DRY_RUN)"
echo "  source: $SOURCE/skills"

for cat in writing intel visual publish; do
  if [ "$CATEGORY" != "all" ] && [ "$CATEGORY" != "$cat" ]; then continue; fi
  if [ -z "$(category_ids "$cat")" ]; then
    echo "  category: $cat（已全部 pin 进 vendor/skills/，无 bridge 需安装）"
    continue
  fi
  echo "  category: $cat"
  for id in $(category_ids "$cat"); do
    src_path="$SOURCE/skills/$id"
    if [ "$UNINSTALL" != "1" ] && [ ! -f "$src_path/SKILL.md" ]; then
      echo "    skip $id (SKILL.md missing in source)" >&2
      continue
    fi
    for root in "${ROOTS[@]}"; do
      target="$root/$id"
      if [ "$UNINSTALL" = "1" ]; then
        if [ -L "$target" ]; then
          echo "    rm $target"
          [ "$DRY_RUN" = "0" ] && rm "$target"
        elif [ -e "$target" ]; then
          echo "    skip $target (not a symlink; not touching)"
        fi
        continue
      fi
      if [ -e "$target" ] || [ -L "$target" ]; then
        echo "    exists $target (skip)"
      else
        echo "    link $id -> $target"
        [ "$DRY_RUN" = "0" ] && ln -s "$src_path" "$target"
      fi
    done
  done
done

echo "done. New links take effect on the agent's next session/reload."
