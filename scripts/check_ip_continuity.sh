#!/usr/bin/env bash
# prism-ip-continuity-v1 acceptance checker (AC-IPC-001..006).
#
# IP-level continuity: the revision evolution chain, a by-IP view (version chain + work refs),
# a drift audit (warning only), and season grouping (a season = campaigns of one IP).
#
# Modes:
#   view --ip <ip_id>      print the IP's revision chain + work reference list (exit 0)
#   --fixtures <ip_dir>    validate one IP dir (revisions chain + seasons)
#   --work <dir>           optional work side dir used for the drift audit
#   --ip-root <dir>        where IPs live (default: <root>/content/ips)
#   --expect pass|fail     assert violations absent (pass) / present (fail)
#   --invert               flip the exit code (negative self-test); supersedes --expect
#   --self-test            run internal good/bad fixtures; exit 0 when the check behaves
#
# Root = this script's parent dir.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIXTURES=""
WORK=""
IP_ROOT=""
VIEW_IP=""
EXPECT="pass"
INVERT=0
SELF_TEST=0

while [ $# -gt 0 ]; do
  case "$1" in
    view) : ;;
    --ip) VIEW_IP="${2:-}"; shift ;;
    --fixtures) FIXTURES="${2:-}"; shift ;;
    --work) WORK="${2:-}"; shift ;;
    --ip-root) IP_ROOT="${2:-}"; shift ;;
    --expect) EXPECT="${2:-pass}"; shift ;;
    --invert) INVERT=1 ;;
    --self-test) SELF_TEST=1 ;;
    *) : ;;
  esac
  shift
done

validate() {
  python3 - "$1" "$2" <<'PY'
import sys, os, glob, re
try:
    import yaml
except Exception as exc:
    print("pyyaml_missing: %s" % exc)
    sys.exit(1)

ip_dir = sys.argv[1]
work_dir = sys.argv[2] if len(sys.argv) > 2 else ""
ip_yaml = os.path.join(ip_dir, "ip.yaml")
if not os.path.isfile(ip_yaml):
    print("ip_not_found: %s" % ip_dir)
    sys.exit(1)
data = yaml.safe_load(open(ip_yaml, encoding="utf-8")) or {}
ip_id = str(data.get("ip_id") or "")
cur = str(data.get("canon_revision") or "")
violations = []

# AC-IPC-001 revision chain: R1..Rn each need revisions/{R}.yaml
m = re.match(r"^R(\d+)$", cur)
if m:
    n = int(m.group(1))
    for i in range(1, n + 1):
        rf = os.path.join(ip_dir, "revisions", "R%d.yaml" % i)
        if not os.path.isfile(rf):
            violations.append("revision_chain_incomplete:%s:R%d" % (ip_id, i))
            continue
        rd = yaml.safe_load(open(rf, encoding="utf-8")) or {}
        if not isinstance(rd, dict) or not rd.get("reason") or "affected_assets" not in rd:
            violations.append("revision_chain_incomplete:%s:R%d:fields" % (ip_id, i))

# AC-IPC-004 seasons: every campaign_ref belongs to this IP
for sf in sorted(glob.glob(os.path.join(ip_dir, "seasons", "*.yaml"))):
    sd = yaml.safe_load(open(sf, encoding="utf-8")) or {}
    if not isinstance(sd, dict):
        continue
    refs = sd.get("campaign_refs") or []
    if not isinstance(refs, list) or not refs:
        violations.append("season_ip_mismatch:%s:empty" % os.path.basename(sf))
        continue
    for item in refs:
        if not isinstance(item, dict):
            violations.append("season_ip_mismatch:%s:bad_entry" % os.path.basename(sf))
            continue
        if str(item.get("ip") or "") != ip_id:
            violations.append("season_ip_mismatch:%s:%s" % (os.path.basename(sf), item.get("ip")))

# AC-IPC-003 drift audit (warning only, never blocks)
drift = []
if work_dir and os.path.isdir(work_dir):
    seen = {}
    for wf in sorted(glob.glob(os.path.join(work_dir, "**", "*.yaml"), recursive=True)):
        try:
            wd = yaml.safe_load(open(wf, encoding="utf-8")) or {}
        except Exception:
            continue
        if not isinstance(wd, dict):
            continue
        for item in (wd.get("imports") or []):
            if isinstance(item, dict) and str(item.get("from") or "") == ip_id:
                aid = str(item.get("asset") or "")
                rev = str(item.get("resolved_revision") or "")
                seen.setdefault(aid, set()).add(rev)
    for aid, revs in seen.items():
        if len(revs) > 1:
            drift.append("continuity_revision_drift:%s:%s" % (aid, ",".join(sorted(revs))))

for d in drift:
    print(d)  # warning: audit only, exit code stays 0

for v in violations:
    print(v)
sys.exit(1 if violations else 0)
PY
}

view() {
  python3 - "$1" "$2" <<'PY'
import sys, os, glob
try:
    import yaml
except Exception as exc:
    print("pyyaml_missing: %s" % exc)
    sys.exit(1)
ip_root = sys.argv[1]
ip_id = sys.argv[2]
target = ""
for f in glob.glob(os.path.join(ip_root, "**", "ip.yaml"), recursive=True):
    d = yaml.safe_load(open(f, encoding="utf-8")) or {}
    if str(d.get("ip_id") or "") == ip_id:
        target = os.path.dirname(f)
        cur = str(d.get("canon_revision") or "")
        break
if not target:
    print("ip_not_found: %s" % ip_id)
    sys.exit(1)
print("ip: %s (revision %s)" % (ip_id, cur))
print("revision chain:")
for f in sorted(glob.glob(os.path.join(target, "revisions", "R*.yaml"))):
    d = yaml.safe_load(open(f, encoding="utf-8")) or {}
    print("  %s reason=%s assets=%s" % (d.get("revision"), d.get("reason"), len(d.get("affected_assets") or [])))
print("work refs (resolved_revision): none external index; scan via --work")
sys.exit(0)
PY
}

if [ "$SELF_TEST" = "1" ]; then
  TMP="$(mktemp -d)"
  mkdir -p "$TMP/ips/ip-a/revisions" "$TMP/ips/ip-a/assets"
  printf 'ip_id: ip-a\ntitle: A\nkind: story\nstatus: active\ncanon_revision: R2\npublish_identity_ref: b\n' > "$TMP/ips/ip-a/ip.yaml"
  printf 'revision: R1\nreason: init\naffected_assets: []\n' > "$TMP/ips/ip-a/revisions/R1.yaml"
  printf 'revision: R2\nreason: add hero\naffected_assets: [hero]\n' > "$TMP/ips/ip-a/revisions/R2.yaml"
  if ! validate "$TMP/ips/ip-a" "" >/dev/null; then
    echo "self-test failed: good chain was rejected"; rm -rf "$TMP"; exit 1
  fi
  rm -f "$TMP/ips/ip-a/revisions/R2.yaml"
  if validate "$TMP/ips/ip-a" "" >/dev/null; then
    echo "self-test failed: broken chain was accepted"; rm -rf "$TMP"; exit 1
  fi
  rm -rf "$TMP"
  echo "check_ip_continuity: self-test pass"
  exit 0
fi

if [ -n "$VIEW_IP" ]; then
  view "${IP_ROOT:-$ROOT/content/ips}" "$VIEW_IP"
  exit $?
fi

TARGET="${FIXTURES:-$ROOT/content/ips}"
OUT="$(validate "$TARGET" "$WORK" 2>&1)"
RC=$?
[ -n "$OUT" ] && printf '%s\n' "$OUT"

if [ "$INVERT" = "1" ]; then
  exit $(( 1 - RC ))
fi
case "$EXPECT" in
  fail) exit $(( RC == 0 ? 1 : 0 )) ;;
  pass|*) exit $RC ;;
esac
