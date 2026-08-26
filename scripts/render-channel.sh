#!/usr/bin/env bash
# Render humanized master → channel-ready Markdown (R3)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

ACCOUNT=""
PLATFORM=""
VERTICAL=""
SLUG=""
SKIP_HUMANIZE_GATE=0

usage() {
  echo "Usage: render-channel.sh --account <id> --platform <id> --vertical <id> --slug <id>" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --account) ACCOUNT="$2"; shift 2 ;;
    --platform) PLATFORM="$2"; shift 2 ;;
    --vertical) VERTICAL="$2"; shift 2 ;;
    --slug) SLUG="$2"; shift 2 ;;
    --skip-humanize-gate) SKIP_HUMANIZE_GATE=1; shift ;;
    -h|--help) usage ;;
    *) echo "Unknown arg: $1" >&2; usage ;;
  esac
done

[[ -n "$ACCOUNT" && -n "$PLATFORM" && -n "$VERTICAL" && -n "$SLUG" ]] || usage

MASTER_DIR="$ROOT/content/masters/${VERTICAL}/${SLUG}"
HUMANIZED="$MASTER_DIR/humanized.md"
META="$MASTER_DIR/meta.yaml"
OUT_DIR="$ROOT/content/renders/${ACCOUNT}/${PLATFORM}"
OUT="$OUT_DIR/${SLUG}.md"

if [[ ! -f "$HUMANIZED" ]]; then
  echo "error: humanized.md required (fail-closed): $HUMANIZED" >&2
  exit 1
fi

CHANNEL_DIR="$ROOT/content/channels/${PLATFORM}"
ACCOUNT_CHANNEL="$ROOT/content/channels/_accounts/${ACCOUNT}/${PLATFORM}"
if [[ -d "$ACCOUNT_CHANNEL" && -f "$ACCOUNT_CHANNEL/template.yaml" ]]; then
  TEMPLATE="$ACCOUNT_CHANNEL/template.yaml"
else
  TEMPLATE="$CHANNEL_DIR/template.yaml"
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "error: channel template not found: $TEMPLATE" >&2
  exit 1
fi

meta_val() {
  local key="$1"
  local default="${2:-}"
  if [[ -f "$META" ]] && rg -q "^${key}:" "$META"; then
    sed -n "s/^${key}:[[:space:]]*//p" "$META" | head -1
  else
    echo "$default"
  fi
}

HUMANIZE_GATE="$(meta_val humanize_gate optional)"
PIPELINE="$(meta_val pipeline oss-pick-daily)"
CONTENT_SPEC="$(meta_val content_spec "")"
DEPTH_LINT_ARGS=()
if [[ "$PIPELINE" == "oss-pick-standard" && "$CONTENT_SPEC" == "r11" ]]; then
  DEPTH_LINT_ARGS=(--depth)
fi
if [[ "$SKIP_HUMANIZE_GATE" -eq 0 && "$HUMANIZE_GATE" == "required" ]]; then
  if [[ ${#DEPTH_LINT_ARGS[@]} -gt 0 ]]; then
    python3 "$ROOT/scripts/lib/readability-lint.py" "$HUMANIZED" "${DEPTH_LINT_ARGS[@]}" || {
      echo "error: readability lint failed (humanize_gate=required): $SLUG" >&2
      exit 1
    }
  else
    python3 "$ROOT/scripts/lib/readability-lint.py" "$HUMANIZED" || {
      echo "error: readability lint failed (humanize_gate=required): $SLUG" >&2
      exit 1
    }
  fi
  python3 "$ROOT/scripts/lib/verify-humanize-evidence.py" --slug "$SLUG" --vertical "$VERTICAL" || {
    echo "error: humanize evidence missing or invalid: $SLUG" >&2
    exit 1
  }
fi

TITLE="$(meta_val title "")"
COVER="$(meta_val cover "")"
SOURCE_URL="$(meta_val source_url "$(meta_val source_repo "")")"
AUTHOR="库拾"
NEED_COMMENT="true"
TITLE_PREFIX=""

if rg -q '^title_prefix:' "$TEMPLATE" 2>/dev/null; then
  TITLE_PREFIX="$(sed -n 's/^title_prefix:[[:space:]]*//p' "$TEMPLATE" | head -1 | sed 's/^"\(.*\)"$/\1/' | tr -d '"')"
fi

if rg -q '^  author:' "$TEMPLATE" 2>/dev/null; then
  AUTHOR="$(sed -n 's/^  author:[[:space:]]*//p' "$TEMPLATE" | head -1)"
fi

if [[ -z "$TITLE" ]]; then
  TITLE="$(sed -n 's/^# //p' "$HUMANIZED" | head -1)"
fi

# meta 深度稿标题常用「库拾」包裹；各端 template 另有 title_prefix，先剥掉避免双品牌
strip_canonical_brand_wrap() {
  local t="$1"
  while [[ "$t" == 「库拾」* || "$t" == 【库拾】* ]]; do
    if [[ "$t" == 「库拾」* ]]; then
      t="${t#「库拾」}"
    elif [[ "$t" == 【库拾】* ]]; then
      t="${t#【库拾】}"
    fi
  done
  echo "$t"
}

if [[ -n "$TITLE_PREFIX" ]]; then
  if [[ "$TITLE" == ${TITLE_PREFIX}* ]]; then
    : # 已有渠道前缀（如微信「库拾」）
  else
    TITLE="$(strip_canonical_brand_wrap "$TITLE")"
    TITLE="${TITLE_PREFIX}${TITLE}"
  fi
fi

if [[ -z "$COVER" ]]; then
  if [[ -f "$MASTER_DIR/assets/github-og.png" ]]; then
    COVER="assets/github-og.png"
  else
    COVER="https://picsum.photos/seed/kushi-${SLUG}/900/383"
  fi
fi

BODY="$(awk 'BEGIN{p=0} /^## /{p=1} p{print}' "$HUMANIZED")"
if [[ -z "$BODY" ]]; then
  BODY="$(tail -n +2 "$HUMANIZED")"
fi

mkdir -p "$OUT_DIR"

# Per-slug asset isolation: assets/{slug}/… avoids cross-article filename collisions
# (e.g. many depth picks share github-repo-header.png).
ASSETS_SRC="$MASTER_DIR/assets"
ASSETS_DEST="$OUT_DIR/assets/$SLUG"

daily_trending_basename() {
  if [[ "$SLUG" =~ ^daily-(.+)$ ]]; then
    echo "github-trending-${BASH_REMATCH[1]}.png"
  else
    echo "github-trending.png"
  fi
}

sync_render_assets() {
  [[ -d "$ASSETS_SRC" ]] || return 0
  mkdir -p "$ASSETS_DEST"
  local f base dest_name dated
  dated="$(daily_trending_basename)"
  for f in "$ASSETS_SRC"/*; do
    [[ -f "$f" ]] || continue
    base="$(basename "$f")"
    [[ "$base" == "manifest.yaml" ]] && continue
    dest_name="$base"
    if [[ "$base" == "github-trending.png" || "$base" == "$dated" ]]; then
      dest_name="$dated"
      if [[ -f "$ASSETS_SRC/$dated" ]]; then
        cp -f "$ASSETS_SRC/$dated" "$ASSETS_DEST/$dest_name"
      else
        cp -f "$f" "$ASSETS_DEST/$dest_name"
      fi
      continue
    fi
    cp -f "$f" "$ASSETS_DEST/$dest_name"
  done
}

rewrite_asset_ref() {
  local rel="$1"
  if [[ "$rel" == assets/"$SLUG"/* ]]; then
    echo "$rel"
    return
  fi
  if [[ "$rel" == assets/* ]]; then
    local rest="${rel#assets/}"
    if [[ "$rest" == "github-trending.png" && "$SLUG" =~ ^daily-(.+)$ ]]; then
      rest="github-trending-${BASH_REMATCH[1]}.png"
    fi
    echo "assets/${SLUG}/${rest}"
    return
  fi
  echo "$rel"
}

COVER="$(rewrite_asset_ref "$COVER")"
sync_render_assets

BODY="$(printf '%s' "$BODY" | python3 "$ROOT/scripts/lib/rewrite-render-asset-refs.py" "$SLUG")"

{
  echo "---"
  echo "title: ${TITLE}"
  echo "cover: ${COVER}"
  echo "author: ${AUTHOR}"
  echo "source_url: ${SOURCE_URL}"
  echo "need_open_comment: ${NEED_COMMENT}"
  echo "---"
  echo ""
  echo "$BODY"
  if [[ -n "$SOURCE_URL" ]]; then
    echo ""
    echo "## 原文"
    echo ""
    echo "${SOURCE_URL}"
  fi
} > "$OUT"

echo "rendered: $OUT"
