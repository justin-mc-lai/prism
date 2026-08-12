#!/usr/bin/env bash
# Lake D2 blog/thread form exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-FORM-001 registry
test -f registry/form-registry.yaml || fail "form-registry.yaml missing"
rg -q "blog" registry/form-registry.yaml || fail "blog missing in registry"
rg -q "thread" registry/form-registry.yaml || fail "thread missing in registry"
rg -q "form-blog.contract|form-thread.contract" registry/form-registry.yaml || fail "contract refs missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert {'blog','thread'} <= fs, 'forms missing'" || fail "registry forms invalid"

# AC-FORM-002 blog contract
test -f contracts/form-blog.contract.md || fail "form-blog.contract missing"
for pat in 四段式 母稿 director humanized.md; do
  rg -q "$pat" contracts/form-blog.contract.md || fail "blog contract lacks $pat"
done
rg -q "证据|evidence" contracts/form-blog.contract.md || fail "blog contract lacks evidence"

# AC-FORM-003 thread contract
test -f contracts/form-thread.contract.md || fail "form-thread.contract missing"
for pat in 倒金字塔 fast_lane_skip canon writing-agent; do
  rg -q "$pat" contracts/form-thread.contract.md || fail "thread contract lacks $pat"
done
rg -q "illegal|禁止" contracts/form-thread.contract.md || fail "thread contract lacks illegal guard"

# AC-FORM-004 routing
rg -q "form-blog.contract|form-thread.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route refs missing"

# AC-FORM-006 no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

# AC-FORM-008 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/form-blog.contract.md contracts/form-thread.contract.md || fail "fail-closed missing"

pass "check_blog_thread_forms: all Lake D2 gates PASS"
