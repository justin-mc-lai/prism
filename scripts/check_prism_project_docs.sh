#!/bin/bash
# prism-project-docs-v1 acceptance checker (AC-PDO-001/003/004/005).
#
# Modes:
#   --init-shape <dir>    project docs/prism tree is content-isomorphic + facade index present
#   --canonical-path      one canonical episode path across contract + pipeline README,
#                         legacy content/presentations line carries a deprecated alias marker
#   --install-notice      installer declares instruction-surface-only + PRISM_HOME convention
#   --boundary            docs/prism carries no truth fields; docs/beacon carries no drama artifacts
#   [--invert]            flip the exit code (self-test: broken input must then exit 0)
#
# Root = this script's parent dir (works as $PRISM_HOME/scripts/<this> in projects too).
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:-}"
shift || true
INVERT=0
DIR=""
while [ $# -gt 0 ]; do
  case "$1" in
    --invert) INVERT=1 ;;
    --init-shape) MODE="init-shape"; if [ -n "${2:-}" ] && [ "${2#--}" = "${2}" ]; then DIR="$2"; shift; fi ;;
    *) case "$MODE" in init-shape|--init-shape) [ -z "$DIR" ] && DIR="$1" ;; esac ;;
  esac
  shift
done

fail=0
note() { printf '%s\n' "$*"; }
die() { note "FAIL: $*"; fail=1; }

finish() {
  if [ "$INVERT" = "1" ]; then
    if [ "$fail" = "0" ]; then exit 1; else exit 0; fi
  fi
  exit "$fail"
}

case "$MODE" in
  --canonical-path|canonical-path)
    CANON='content/masters/ai-manga-drama/{slug}/'
    CONTRACT="$ROOT/contracts/form-manga-drama.contract.md"
    README="$ROOT/content/pipelines/ai-manga-drama/README.md"
    [ -f "$CONTRACT" ] || die "missing $CONTRACT"
    [ -f "$README" ] || die "missing $README"
    grep -qF "$CANON" "$CONTRACT" || die "contract lacks canonical episode path: $CANON"
    grep -qF "$CANON" "$README" || die "pipeline README lacks canonical episode path: $CANON"
    canon_n=$(grep -oF "$CANON" "$CONTRACT" | wc -l | tr -d ' ')
    [ "$canon_n" = "1" ] || die "contract canonical path must appear exactly once (got $canon_n)"
    grep -n 'content/presentations' "$CONTRACT" | grep -qiE 'alias|deprecated' \
      || die "contract's content/presentations line must be marked alias/deprecated"
    note "OK: canonical episode path is single and consistent; legacy presentations line is alias-marked"
    ;;
  --install-notice|install-notice)
    HEADER="$ROOT/scripts/install_public_surfaces.sh"
    [ -f "$HEADER" ] || die "missing $HEADER"
    head -n 14 "$HEADER" | grep -q '指令面' || die "installer header must declare 指令面-only scope"
    head -n 14 "$HEADER" | grep -q 'PRISM_HOME' || die "installer header must declare PRISM_HOME capability route"
    note "OK: installer declares instruction-surface-only + PRISM_HOME"
    ;;
  --boundary|boundary)
    if [ -d "$ROOT/docs/beacon" ]; then
      if rg --files "$ROOT/docs/beacon" | rg -q '(^|/)(storyboard\.json|分镜脚本\.md|[^/]*-480p\.mp4)$'; then
        die "docs/beacon contains a drama artifact file (storyboard/分镜脚本/成片)"
      fi
    fi
    if [ -d "$ROOT/docs/prism" ]; then
      if rg -q 'parser_contract|revision_id' "$ROOT/docs/prism/"; then
        die "docs/prism contains requirement-truth fields (parser_contract/revision_id)"
      fi
    fi
    note "OK: docs/prism carries no truth fields; docs/beacon carries no drama artifacts"
    ;;
  --init-shape|init-shape)
    [ -n "$DIR" ] || { die "--init-shape requires a directory"; finish; }
    [ -d "$DIR" ] || { die "not a directory: $DIR"; finish; }
    [ -d "$ROOT/content" ] || { die "missing $ROOT/content"; finish; }
    if ! diff <(ls "$DIR" | grep -v '^README\.md$' | sort) <(ls "$ROOT/content" | sort) >/dev/null; then
      die "tree is not content-isomorphic: $(diff <(ls "$DIR" | grep -v '^README\.md$' | sort) <(ls "$ROOT/content" | sort) | head -5 | tr '\n' ' ')"
    fi
    FACADE="$DIR/README.md"
    [ -f "$FACADE" ] || { die "missing facade README: $FACADE"; finish; }
    grep -q '大纲' "$FACADE" || die "facade README lacks 大纲 index entry"
    grep -qE '母稿|masters' "$FACADE" || die "facade README lacks 母稿/masters index entry"
    grep -q '分镜' "$FACADE" || die "facade README lacks 分镜 index entry"
    note "OK: tree is content-isomorphic and facade index carries 大纲/母稿/分镜"
    ;;
  *)
    note "usage: check_prism_project_docs.sh --init-shape <dir> | --canonical-path | --install-notice | --boundary [--invert]"
    exit 2
    ;;
esac

finish
