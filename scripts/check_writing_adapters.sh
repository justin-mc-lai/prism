#!/usr/bin/env bash
# Lake D1 writing base exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-WRITE-001 writing.contract
test -f contracts/writing.contract.md || fail "writing.contract.md missing"
rg -q "identity" contracts/writing.contract.md || fail "contract lacks identity"
rg -q "决策边界" contracts/writing.contract.md || fail "contract lacks 决策边界"
rg -q "失败处理" contracts/writing.contract.md || fail "contract lacks 失败处理"
rg -q "四段式|倒金字塔|emotional" contracts/writing.contract.md || fail "contract lacks distilled form rules"
rg -q "fail-closed|blocked|reason_code" contracts/writing.contract.md || fail "contract lacks fail-closed"

# AC-WRITE-002 anti-slop-gate
test -f skills/prism-qa/references/anti-slop-gate.md || fail "anti-slop-gate missing"
for pat in 二元对比 清嗓 weasel 假深刻 总结复读; do
  rg -q "$pat" skills/prism-qa/references/anti-slop-gate.md || fail "gate lacks pattern: $pat"
done
rg -q "证据|原文行" skills/prism-qa/references/anti-slop-gate.md || fail "gate lacks evidence requirement"
rg -q "不承诺|必过|占位" skills/prism-qa/references/anti-slop-gate.md || fail "gate lacks hard boundaries"
count=$(grep -c '^- ' skills/prism-qa/references/anti-slop-gate.md || true)
test "$count" -ge 15 || fail "gate bullets <15 (got $count)"

# AC-WRITE-003 writing-adapters
test -f registry/writing-adapters.yaml || fail "writing-adapters.yaml missing"
rg -q "humanizer-zh" registry/writing-adapters.yaml || fail "adapter humanizer-zh missing"
rg -q "selfmedia-humanize" registry/writing-adapters.yaml || fail "adapter selfmedia-humanize missing"
rg -q "fail_closed" registry/writing-adapters.yaml || fail "adapter fail_closed missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/writing-adapters.yaml')); assert len(d['adapters'])>=8, 'adapters <8'" || fail "adapters <8"

# AC-WRITE-004 routing
rg -q "MAP-005" skills/_internal/orchestration/creation-mode-map.md || fail "route lacks MAP-005"
rg -q "writing.contract|anti-slop-gate" skills/_internal/orchestration/creation-mode-map.md || fail "route lacks contract/gate refs"

# AC-WRITE-006 no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"
test ! -f skills/prism-qa/references/SKILL.md || fail "qa reference SKILL.md leak"

pass "check_writing_adapters: all Lake D1 gates PASS"
