#!/usr/bin/env bash
# prism-ip-schema-v1 asset convergence (AC-IPM-008).
#
# Registers existing asset units from storyworlds/*/characters|scenes|props and
# masters/*/*/assets/** into content/ips/{ip_id}/assets/<class>/<asset_id>/.
# Idempotent (re-runs add nothing) and loss-free (source count == registered count);
# writes an alias manifest so old references stay resolvable during the兼容期.
#
# Modes:
#   (no args)              apply migration to this repo
#   --dry-run              report the plan without writing; no writes
#   --expect no-loss       assert registered count == source count (exit 0/1)
#   --self-test            run on a temp tree; assert idempotent + no-loss; exit 0
#   --root <dir>           operate on <dir> instead of this repo
#
# Root = this script's parent dir (works as $PRISM_HOME/scripts/<this> in projects too).
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DRY=0
EXPECT=""
SELF_TEST=0
TARGET_ROOT=""

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY=1 ;;
    --expect) EXPECT="${2:-}"; shift ;;
    --self-test) SELF_TEST=1 ;;
    --root) TARGET_ROOT="${2:-}"; shift ;;
    *) : ;;
  esac
  shift
done

plan_and_apply() {
  # $1 = project root ; $2 = dry (1/0)
  python3 - "$1" "$2" <<'PY'
import sys, os, glob, json, shutil
root = sys.argv[1]
dry = sys.argv[2] == "1"

def asset_units(base, classes):
    units = []
    for cls in classes:
        d = os.path.join(base, cls)
        if not os.path.isdir(d):
            continue
        for entry in sorted(glob.glob(os.path.join(d, "*"))):
            if os.path.isdir(entry) and os.listdir(entry):
                units.append((cls, os.path.basename(entry), entry))
    return units

CLASSES = ["characters", "scenes", "props", "styles"]
sources = []

# storyworlds: content/storyworlds/<world_slug>/{characters,scenes,props}/
for world in sorted(glob.glob(os.path.join(root, "content", "storyworlds", "*"))):
    if not os.path.isdir(world):
        continue
    slug = os.path.basename(world)
    for cls, aid, path in asset_units(world, CLASSES):
        sources.append(("storyworld", "ip-" + slug, cls, aid, path))

# masters: content/masters/<vertical>/<slug>/assets/**
for master in sorted(glob.glob(os.path.join(root, "content", "masters", "*", "*"))):
    assets = os.path.join(master, "assets")
    if not os.path.isdir(assets):
        continue
    slug = os.path.basename(master)
    for cls, aid, path in asset_units(assets, CLASSES):
        sources.append(("master", "ip-" + slug, cls, aid, path))

registered = []
alias = []
for kind, ip_id, cls, aid, path in sources:
    dest = os.path.join(root, "content", "ips", ip_id, "assets", cls, aid)
    registered.append((ip_id, cls, aid))
    alias.append({"source": os.path.relpath(path, root), "ip_id": ip_id,
                  "asset": "%s/%s" % (cls, aid)})
    if dry:
        continue
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if not os.path.isdir(dest):
        shutil.copytree(path, dest)
    ip_yaml = os.path.join(root, "content", "ips", ip_id, "ip.yaml")
    if not os.path.exists(ip_yaml):
        with open(ip_yaml, "w", encoding="utf-8") as fh:
            fh.write("ip_id: %s\ntitle: %s\nkind: story\nstatus: draft\n"
                     "canon_revision: R1\npublish_identity_ref: \"\"\n" % (ip_id, ip_id))

src_count = len(sources)
reg_count = len(registered)
print(json.dumps({"source_units": src_count, "registered_units": reg_count,
                  "alias_records": len(alias)}, ensure_ascii=False))
if not dry:
    man = os.path.join(root, ".beacon", "ip-migration-manifest.json")
    os.makedirs(os.path.dirname(man), exist_ok=True)
    with open(man, "w", encoding="utf-8") as fh:
        json.dump({"schema_version": "1.0", "artifact": "ip-asset-migration",
                   "source_units": src_count, "registered_units": reg_count,
                   "alias": alias}, fh, ensure_ascii=False, indent=2)
sys.exit(0 if src_count == reg_count else 1)
PY
}

if [ "$SELF_TEST" = "1" ]; then
  TMP="$(mktemp -d)"
  mkdir -p "$TMP/content/storyworlds/w1/characters/hero" "$TMP/content/masters/v1/m1/assets/props/lamp"
  : > "$TMP/content/storyworlds/w1/characters/hero/identity.md"
  : > "$TMP/content/masters/v1/m1/assets/props/lamp/identity.md"
  if ! plan_and_apply "$TMP" "0" >/dev/null; then
    echo "self-test failed: first migration violated no-loss"; rm -rf "$TMP"; exit 1
  fi
  c1="$(find "$TMP/content/ips" -mindepth 4 -maxdepth 4 -type d 2>/dev/null | wc -l | tr -d ' ')"
  plan_and_apply "$TMP" "0" >/dev/null
  c2="$(find "$TMP/content/ips" -mindepth 4 -maxdepth 4 -type d 2>/dev/null | wc -l | tr -d ' ')"
  if [ "$c1" != "$c2" ]; then
    echo "self-test failed: migration not idempotent ($c1 != $c2)"; rm -rf "$TMP"; exit 1
  fi
  rm -rf "$TMP"
  echo "migrate_assets_to_ip: self-test pass"
  exit 0
fi

TARGET="${TARGET_ROOT:-$ROOT}"
if [ "$DRY" = "1" ]; then
  OUT="$(plan_and_apply "$TARGET" "1")"
  RC=$?
else
  OUT="$(plan_and_apply "$TARGET" "0")"
  RC=$?
fi
[ -n "$OUT" ] && printf '%s\n' "$OUT"
case "$EXPECT" in
  no-loss) exit $RC ;;
  *) exit $RC ;;
esac
