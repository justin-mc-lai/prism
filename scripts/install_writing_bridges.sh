#!/usr/bin/env bash
# Prism writing/humanize bridge installer.
#
# Links the writing/humanize bridge skills declared in registry/writing-adapters.yaml
# from the selfmedia-creator source repo into agent skill roots, so prism-produce /
# prism-qa fail-closed bridges resolve at runtime.
#
# Source repo may be overridden with SELFMEDIA_SOURCE. The source repo stays the
# canonical bridge host until replacement (see registry/source-capability-inventory.md).
#
# Idempotent. Options: --dry-run | --uninstall
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="${SELFMEDIA_SOURCE:-/Users/apple/Developer/Personal/products/selfmedia-creator}"

DRY_RUN=0
UNINSTALL=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --uninstall) UNINSTALL=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

# Bridge skills from registry/writing-adapters.yaml (canonical order).
# NOTE: 写作产链 10 个 skill 已于 2026-08-15 全部 pin 进 vendor/skills/（A4），
# 本脚本保留为 archive-only 兼容入口，实际不再需要安装。
BRIDGE_IDS=()

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
echo "prism writing-bridge $mode (dry-run=$DRY_RUN)"
echo "  source: $SOURCE/skills"

for id in "${BRIDGE_IDS[@]}"; do
  src_path="$SOURCE/skills/$id"
  if [ "$UNINSTALL" != "1" ] && [ ! -f "$src_path/SKILL.md" ]; then
    echo "  skip $id (SKILL.md missing in source)" >&2
    continue
  fi
  for root in "${ROOTS[@]}"; do
    target="$root/$id"
    if [ "$UNINSTALL" = "1" ]; then
      if [ -L "$target" ]; then
        echo "  rm $target"
        if [ "$DRY_RUN" = "0" ]; then rm "$target"; fi
      elif [ -e "$target" ]; then
        echo "  skip $target (not a symlink; not touching)"
      fi
      continue
    fi
    if [ -e "$target" ] || [ -L "$target" ]; then
      echo "  exists $target (skip)"
    else
      echo "  link $id -> $target"
      if [ "$DRY_RUN" = "0" ]; then ln -s "$src_path" "$target"; fi
    fi
  done
done

echo "done. New links take effect on the agent's next session/reload."
