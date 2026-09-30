#!/usr/bin/env bash
# prism-shot-iteration-budget-v1 acceptance checker (AC-ITB-001..007).
#
# Validates shot generation discipline on a storyboard:
#   - iteration budget: shots[].attempts <= shots[].iteration_budget (AC-ITB-001)
#   - over-budget requires a downgrade record: convergence in {simplified, redesigned}
#     with downgrades <= max_downgrades, else shot_aborted (AC-ITB-002)
#   - no post-dub fallback: dialogue_source != post_dub (AC-ITB-003)
#   - image negation must be affirmative (AC-ITB-004)
#   - capability-domain precheck: action/dialogue inside reachable whitelist (AC-ITB-005)
#   - threshold source obligation (AC-ITB-007)
#
# Modes:
#   --storyboard <path>       validate a storyboard json (vacuous pass when no budget fields)
#   --expect pass|fail        assert violations absent (pass) / present (fail)
#   --invert                  flip the exit code (negative self-test); supersedes --expect
#   --self-test               run internal good/bad storyboards; exit 0 when the check behaves
#
# Root = this script's parent dir.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STORYBOARD=""
EXPECT="pass"
INVERT=0
SELF_TEST=0

while [ $# -gt 0 ]; do
  case "$1" in
    --storyboard) STORYBOARD="${2:-}"; shift ;;
    --expect) EXPECT="${2:-pass}"; shift ;;
    --invert) INVERT=1 ;;
    --self-test) SELF_TEST=1 ;;
    *) : ;;
  esac
  shift
done

validate() {
  python3 - "$1" <<'PY'
import sys, json, re
path = sys.argv[1]
try:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
except Exception as exc:
    print("storyboard_unreadable: %s" % exc)
    sys.exit(1)

shots = data.get("shots") if isinstance(data, dict) else None
shots = shots if isinstance(shots, list) else []
violations = []

DOWNS = {"simplified", "redesigned"}
has_budget = any(s.get("iteration_budget") is not None or s.get("max_downgrades") is not None for s in shots)

# AC-ITB-007 threshold source obligation
if has_budget and not data.get("threshold_source"):
    violations.append("threshold_source_missing")

# AC-ITB-005 capability domain
reachable = data.get("reachable") if isinstance(data.get("reachable"), dict) else None
if reachable is not None:
    if not data.get("provider") or not data.get("model"):
        violations.append("action_outside_model_domain:missing provider/model")
    allowed_actions = set(reachable.get("actions") or [])
    allowed_dialogue = set(reachable.get("dialogue") or [])
    for s in shots:
        act = s.get("action")
        if act and allowed_actions and act not in allowed_actions:
            violations.append("action_outside_model_domain:%s" % act)
        dlg = s.get("dialogue")
        if dlg and allowed_dialogue and dlg not in allowed_dialogue:
            violations.append("dialogue_outside_model_domain:%s" % dlg)

NEG = re.compile(r"(?:\bno\s+[a-z]|不要|(?<![a-z])not\s+[a-z])")

for s in shots:
    sid = s.get("shot_id", "?")
    budget = s.get("iteration_budget")
    attempts = s.get("attempts")
    conv = s.get("convergence")
    if budget is not None and attempts is not None and attempts > budget:
        if conv not in DOWNS:
            violations.append("iteration_budget_exceeded:%s" % sid)
    maxd = s.get("max_downgrades")
    dgs = s.get("downgrades")
    if conv in DOWNS and maxd is not None and dgs is not None and dgs > maxd:
        violations.append("shot_aborted:%s" % sid)
    if s.get("dialogue_source") == "post_dub":
        violations.append("post_dub_fallback_forbidden:%s" % sid)
    texts = [str(s.get("description", ""))]
    for b in (s.get("beats") or []):
        if isinstance(b, dict):
            texts.append(str(b.get("description", "")))
    for t in texts:
        if NEG.search(t):
            violations.append("image_negation_not_affirmative:%s" % sid)
            break

for v in violations:
    print(v)
sys.exit(1 if violations else 0)
PY
}

if [ "$SELF_TEST" = "1" ]; then
  TMP="$(mktemp -d)"
  cat > "$TMP/good.json" <<'J'
{"episode":"ep-x","threshold_source":{"iteration_budget":"demo: seedance-2.0"},
 "shots":[{"shot_id":"s1","iteration_budget":12,"attempts":4,"convergence":"native"}]}
J
  cat > "$TMP/bad.json" <<'J'
{"episode":"ep-x","threshold_source":{"iteration_budget":"demo"},
 "shots":[{"shot_id":"s1","iteration_budget":10,"attempts":14,"convergence":"native"},
          {"shot_id":"s2","dialogue_source":"post_dub"}]}
J
  if ! validate "$TMP/good.json" >/dev/null; then
    echo "self-test failed: good storyboard was rejected"; rm -rf "$TMP"; exit 1
  fi
  if validate "$TMP/bad.json" >/dev/null; then
    echo "self-test failed: bad storyboard was accepted"; rm -rf "$TMP"; exit 1
  fi
  rm -rf "$TMP"
  echo "check_shot_iteration_budget: self-test pass"
  exit 0
fi

TARGET="${STORYBOARD:-$ROOT/content/pipelines/ai-manga-drama/fixtures/ep-compile-test/storyboard.json}"
if [ ! -f "$TARGET" ]; then
  echo "storyboard_not_found: $TARGET"
  exit 1
fi

OUT="$(validate "$TARGET" 2>&1)"
RC=$?
[ -n "$OUT" ] && printf '%s\n' "$OUT"

if [ "$INVERT" = "1" ]; then
  exit $(( 1 - RC ))
fi
case "$EXPECT" in
  fail) exit $(( RC == 0 ? 1 : 0 )) ;;
  pass|*) exit $RC ;;
esac
