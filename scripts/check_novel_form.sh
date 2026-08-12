#!/usr/bin/env bash
# Lake D4 novel form exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-NVL-001 registry
test -f registry/form-registry.yaml || fail "form-registry.yaml missing"
rg -q "novel" registry/form-registry.yaml || fail "novel missing in registry"
rg -q "form-novel.contract" registry/form-registry.yaml || fail "novel contract ref missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert 'novel' in fs, 'novel missing'" || fail "registry novel invalid"

# AC-NVL-002 contract
test -f contracts/form-novel.contract.md || fail "form-novel.contract missing"
for pat in StoryMaster episode "content/storyworlds" "证据|evidence"; do
  rg -q "$pat" contracts/form-novel.contract.md || fail "novel contract lacks $pat"
done

# AC-NVL-003 canon hook
for pat in canon_gate_status review_required failed generated fast_lane_skip; do
  rg -q "$pat" contracts/form-novel.contract.md || fail "novel contract lacks canon hook $pat"
done

# AC-NVL-004 routing
rg -q "novel|form-novel.contract" skills/_internal/orchestration/creation-mode-map.md || fail "novel route missing"

# AC-NVL-006 bridge fail-closed
rg -q "kushi-narrative-zh|fail-closed|blocked|reason_code" contracts/form-novel.contract.md || fail "bridge fail-closed missing"

# AC-NVL-007 storyworld path
rg -q "content/storyworlds|bible|canon-ledger" contracts/form-novel.contract.md || fail "storyworld refs missing"

# AC-NVL-009 OOC gate
rg -q "OOC|设定漂移|fail-closed|事实错误" contracts/form-novel.contract.md || fail "OOC gate missing"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_novel_form: all Lake D4 gates PASS"
