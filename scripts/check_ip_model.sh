#!/usr/bin/env bash
# prism-ip-schema-v1 acceptance checker (AC-IPM-006).
#
# Validates the IP model: registry registration, ip.yaml required fields, status enum,
# import resolution (ip_id / asset_id exist), asset_id uniqueness within an IP.
# Violations print a reason_code and cause a non-zero exit.
#
# Modes:
#   (no args)                          validate content/ips in this repo
#   --fixtures <dir>                   validate the {ip_id}/ip.yaml set under <dir>
#   --expect pass|fail                 assert no violations (pass) or violations present (fail)
#   --invert                           flip the exit code (negative self-test); supersedes --expect
#   --self-test                        run internal good/bad fixtures, exit 0 when the check behaves
#   --work <dir>                       optional work-side dir to scan for imports[] resolution
#
# Root = this script's parent dir (works as $PRISM_HOME/scripts/<this> in projects too).
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIXTURES=""
WORK=""
EXPECT="pass"
INVERT=0
SELF_TEST=0

while [ $# -gt 0 ]; do
  case "$1" in
    --fixtures) FIXTURES="${2:-}"; shift ;;
    --work) WORK="${2:-}"; shift ;;
    --expect) EXPECT="${2:-pass}"; shift ;;
    --invert) INVERT=1 ;;
    --self-test) SELF_TEST=1 ;;
    *) : ;;
  esac
  shift
done

validate() {
  # $1 = IP dir containing {ip_id}/ip.yaml ; $2 = optional work dir ; $3 = exclude _examples
  python3 - "$1" "$2" "${3:-0}" <<'PY'
import sys, os, glob, re
try:
    import yaml
except Exception as exc:  # pragma: no cover
    print("pyyaml_missing: %s" % exc)
    sys.exit(1)

ip_dir = sys.argv[1]
work_dir = sys.argv[2] if len(sys.argv) > 2 else ""
skip_examples = (sys.argv[3] if len(sys.argv) > 3 else "0") == "1"
ip_files = sorted(glob.glob(os.path.join(ip_dir, "*", "ip.yaml")))
if skip_examples:
    ip_files = [f for f in ip_files if not os.path.basename(os.path.dirname(f)).startswith("_")]
if not ip_files:
    print("ip_model: no IP registered under %s (vacuous pass)" % ip_dir)
    sys.exit(0)

REQUIRED = ["ip_id", "title", "kind", "status", "canon_revision", "publish_identity_ref"]
STATUSES = {"draft", "active", "paused", "archived"}
KINDS = {"fact", "story", "brand"}
ASSET_CLASSES = ["characters", "scenes", "props", "styles"]

violations = []
registry = {}

for f in ip_files:
    with open(f, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        violations.append("ip_not_found: %s not a mapping" % f)
        continue
    for key in REQUIRED:
        if data.get(key) in (None, ""):
            violations.append("ip_missing_field:%s:%s" % (os.path.basename(os.path.dirname(f)), key))
    if data.get("status") not in STATUSES:
        violations.append("ip_bad_status:%s:%s" % (data.get("ip_id"), data.get("status")))
    if data.get("kind") not in KINDS:
        violations.append("ip_bad_kind:%s:%s" % (data.get("ip_id"), data.get("kind")))
    ip_id = str(data.get("ip_id") or "")
    base = os.path.dirname(f)
    if not os.path.isdir(os.path.join(base, "assets")):
        violations.append("asset_missing:%s:assets/" % ip_id)
    seen = {}
    for cls in ASSET_CLASSES:
        for entry in sorted(glob.glob(os.path.join(base, "assets", cls, "*"))):
            aid = os.path.basename(entry.rstrip("/"))
            if aid in seen:
                violations.append("asset_id_duplicate:%s:%s" % (ip_id, aid))
            seen[aid] = cls
    if ip_id:
        registry[ip_id] = {
            "status": data.get("status"),
            "canon_revision": str(data.get("canon_revision") or ""),
            "assets": set(seen.keys()),
        }

# import resolution on the work side (optional)
work_ips = []
if work_dir and os.path.isdir(work_dir):
    for f in sorted(glob.glob(os.path.join(work_dir, "**", "*.yaml"), recursive=True)):
        try:
            with open(f, encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        imports = data.get("imports")
        if not isinstance(imports, list):
            continue
        srcs = set()
        for item in imports:
            if not isinstance(item, dict):
                continue
            src = str(item.get("from") or "")
            asset = str(item.get("asset") or "")
            rev = item.get("revision")
            if src:
                srcs.add(src)
            if not src:
                violations.append("import_missing_from:%s" % os.path.relpath(f, work_dir))
                continue
            if src not in registry:
                violations.append("ip_not_found:%s" % src)
                continue
            meta = registry[src]
            if meta["status"] not in ("active",):
                violations.append("ip_unfrozen:%s:%s" % (src, meta["status"]))
            aid = asset.split("/")[-1] if asset else ""
            if aid and aid not in meta["assets"]:
                violations.append("asset_missing:%s:%s" % (src, aid))
            if rev and str(rev) != meta["canon_revision"]:
                violations.append("revision_mismatch:%s:%s!=%s" % (src, rev, meta["canon_revision"]))
        if len([s for s in srcs if s]) >= 2:
            work_ips.append(sorted(srcs))
            for src in srcs:
                meta = registry.get(src)
                if not meta or meta["status"] != "active":
                    violations.append("crossover_canon_unmet:%s" % src)

for v in violations:
    print(v)
sys.exit(1 if violations else 0)
PY
}

run() {
  validate "$1" "$2" "${3:-0}"
}

if [ "$SELF_TEST" = "1" ]; then
  TMP="$(mktemp -d)"
  mkdir -p "$TMP/good/ip-a/assets/characters/hero"
  cat > "$TMP/good/ip-a/ip.yaml" <<'Y'
ip_id: ip-a
title: Good IP
kind: story
status: active
canon_revision: R1
publish_identity_ref: brand:a
Y
  if ! run "$TMP/good" "" >/dev/null 2>&1; then
    echo "self-test failed: good fixture was rejected"; rm -rf "$TMP"; exit 1
  fi
  mkdir -p "$TMP/bad/ip-b/assets"
  cat > "$TMP/bad/ip-b/ip.yaml" <<'Y'
ip_id: ip-b
title: Bad IP
kind: story
status: bogus
Y
  if run "$TMP/bad" "" >/dev/null 2>&1; then
    echo "self-test failed: bad fixture was accepted"; rm -rf "$TMP"; exit 1
  fi
  rm -rf "$TMP"
  echo "check_ip_model: self-test pass"
  exit 0
fi

TARGET="${FIXTURES:-$ROOT/content/ips}"
WORKDIR="${WORK:-$ROOT/content}"
EXCLUDE_EXAMPLES=0
if [ -z "$FIXTURES" ]; then EXCLUDE_EXAMPLES=1; fi

OUT="$(run "$TARGET" "$WORKDIR" "$EXCLUDE_EXAMPLES" 2>&1)"
RC=$?
if [ -n "$OUT" ]; then printf '%s\n' "$OUT"; fi

if [ "$INVERT" = "1" ]; then
  exit $(( 1 - RC ))
fi
case "$EXPECT" in
  fail) exit $(( RC == 0 ? 1 : 0 )) ;;
  pass|*) exit $RC ;;
esac
