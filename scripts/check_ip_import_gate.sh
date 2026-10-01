#!/usr/bin/env bash
# prism-ip-import-gate-v1 acceptance checker (AC-IPG-002..005).
#
# A work whose imports[] references two or more IPs is a crossover and must be authorized,
# disclosed, attributed, canon-clean, and (if split) royalty-complete.
#
# Modes:
#   --fixtures <dir>       validate a directory of crossover records (content/crossovers/*.yaml)
#   --work <dir>           also scan works for imports>=2 and require an approved crossover
#   --ip-root <dir>        where participant IPs live (default: <root>/content/ips)
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
EXPECT="pass"
INVERT=0
SELF_TEST=0

while [ $# -gt 0 ]; do
  case "$1" in
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
  python3 - "$1" "$2" "$3" <<'PY'
import sys, os, glob, json
try:
    import yaml
except Exception as exc:
    print("pyyaml_missing: %s" % exc)
    sys.exit(1)

cov_dir = sys.argv[1]
work_dir = sys.argv[2] if len(sys.argv) > 2 else ""
ip_root = sys.argv[3] if len(sys.argv) > 3 else ""
violations = []

# load participant IP status
ip_status = {}
if ip_root and os.path.isdir(ip_root):
    for f in glob.glob(os.path.join(ip_root, "**", "ip.yaml"), recursive=True):
        try:
            d = yaml.safe_load(open(f, encoding="utf-8")) or {}
        except Exception:
            continue
        if isinstance(d, dict) and d.get("ip_id"):
            ip_status[str(d["ip_id"])] = str(d.get("status") or "")

crossovers = []
if cov_dir and os.path.isdir(cov_dir):
    for f in sorted(glob.glob(os.path.join(cov_dir, "**", "*.yaml"), recursive=True)):
        try:
            d = yaml.safe_load(open(f, encoding="utf-8")) or {}
        except Exception:
            continue
        if isinstance(d, dict) and d.get("crossover_id"):
            crossovers.append((f, d))

def check_record(f, d):
    cid = str(d.get("crossover_id") or "")
    parts = d.get("participant_ips") or []
    if not isinstance(parts, list) or len(parts) < 2:
        violations.append("crossover_authorization_missing:%s:participants<2" % cid)
    auth = d.get("authorization") if isinstance(d.get("authorization"), dict) else {}
    if str(auth.get("status") or "") != "approved":
        violations.append("crossover_authorization_missing:%s" % cid)
    if not str(d.get("disclosure_note") or "").strip():
        violations.append("crossover_disclosure_missing:%s" % cid)
    rs = d.get("royalty_split")
    if rs:
        if not d.get("non_royalty"):
            total = 0.0
            ok = True
            for item in rs:
                if not isinstance(item, dict) or "percent" not in item:
                    ok = False
                    continue
                try:
                    total += float(item.get("percent"))
                except Exception:
                    ok = False
            if not ok or abs(total - 100.0) > 1e-6:
                violations.append("crossover_royalty_unrecorded:%s:sum=%s" % (cid, total))
    for pid in parts:
        st = ip_status.get(str(pid))
        if st is None:
            violations.append("crossover_canon_unmet:%s:unknown" % pid)
        elif st != "active":
            violations.append("crossover_canon_unmet:%s:%s" % (pid, st))

for f, d in crossovers:
    check_record(f, d)

# work-side: any work with imports of >=2 distinct IPs needs an approved crossover covering it
if work_dir and os.path.isdir(work_dir):
    approved = []
    for f, d in crossovers:
        parts = set(str(p) for p in (d.get("participant_ips") or []))
        if str((d.get("authorization") or {}).get("status") or "") == "approved":
            approved.append(parts)
    for wf in sorted(glob.glob(os.path.join(work_dir, "**", "*.yaml"), recursive=True)):
        try:
            wd = yaml.safe_load(open(wf, encoding="utf-8")) or {}
        except Exception:
            continue
        if not isinstance(wd, dict):
            continue
        imports = wd.get("imports")
        if not isinstance(imports, list):
            continue
        srcs = set()
        for item in imports:
            if isinstance(item, dict) and item.get("from"):
                srcs.add(str(item["from"]))
        if len(srcs) >= 2:
            if not any(srcs.issubset(p) for p in approved):
                violations.append("crossover_authorization_missing:work:%s" % os.path.relpath(wf, work_dir))

for v in violations:
    print(v)
sys.exit(1 if violations else 0)
PY
}

if [ "$SELF_TEST" = "1" ]; then
  TMP="$(mktemp -d)"
  mkdir -p "$TMP/ips/ip-a" "$TMP/ips/ip-b" "$TMP/cov" "$TMP/work/masters/v/m"
  printf 'ip_id: ip-a\ntitle: A\nkind: story\nstatus: active\ncanon_revision: R1\npublish_identity_ref: b\n' > "$TMP/ips/ip-a/ip.yaml"
  printf 'ip_id: ip-b\ntitle: B\nkind: story\nstatus: active\ncanon_revision: R1\npublish_identity_ref: b\n' > "$TMP/ips/ip-b/ip.yaml"
  cat > "$TMP/cov/cx-1.yaml" <<'Y'
crossover_id: cx-1
participant_ips: [ip-a, ip-b]
work_ref: masters/v/m
authorization: {status: approved, approved_by: op, approved_at: "2026-09-30", scope: full}
disclosure_note: "A x B 联名"
attribution: [{ip: ip-a, credit: A}, {ip: ip-b, credit: B}]
royalty_split: [{ip: ip-a, percent: 60}, {ip: ip-b, percent: 40}]
Y
  if ! validate "$TMP/cov" "" "$TMP/ips" >/dev/null; then
    echo "self-test failed: good crossover was rejected"; rm -rf "$TMP"; exit 1
  fi
  cat > "$TMP/cov/cx-2.yaml" <<'Y'
crossover_id: cx-2
participant_ips: [ip-a, ip-b]
work_ref: masters/v/m
authorization: {status: draft}
attribution: []
Y
  if validate "$TMP/cov" "" "$TMP/ips" >/dev/null; then
    echo "self-test failed: bad crossover was accepted"; rm -rf "$TMP"; exit 1
  fi
  rm -rf "$TMP"
  echo "check_ip_import_gate: self-test pass"
  exit 0
fi

TARGET="${FIXTURES:-$ROOT/content/crossovers}"
IPR="${IP_ROOT:-$ROOT/content/ips}"
OUT="$(validate "$TARGET" "$WORK" "$IPR" 2>&1)"
RC=$?
[ -n "$OUT" ] && printf '%s\n' "$OUT"

if [ "$INVERT" = "1" ]; then
  exit $(( 1 - RC ))
fi
case "$EXPECT" in
  fail) exit $(( RC == 0 ? 1 : 0 )) ;;
  pass|*) exit $RC ;;
esac
