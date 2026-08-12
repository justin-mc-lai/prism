#!/usr/bin/env bash
# Lake F1 monetization exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-MON-001 contract fields
test -f contracts/monetization.contract.md || fail "monetization.contract missing"
for pat in deal_id type terms disclosure evidence; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks $pat"
done

# AC-MON-002 registry
test -f registry/monetization-adapters.yaml || fail "monetization-adapters.yaml missing"
rg -q "deal-record|compliance|disclosure" registry/monetization-adapters.yaml || fail "adapter entries missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/monetization-adapters.yaml')); assert len(d['adapters'])>=3, 'adapters <3'" || fail "adapters <3"

# AC-MON-003 human approval
for pat in 人工 批准 approval; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks approval $pat"
done

# AC-MON-004 routing
rg -q "monetization.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-MON-006 no fabrication
for pat in 不编造 缺证据 blocked; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks no-fabrication $pat"
done

# AC-MON-007 disclosure
for pat in 披露 广告 赞助 标注; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks disclosure $pat"
done

# AC-MON-008 risk compliance
for pat in health legal finance 合规; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks compliance $pat"
done

# AC-MON-009 sensitive info
for pat in 收款 敏感 secrets 禁止入库; do
  rg -q "$pat" contracts/monetization.contract.md || fail "contract lacks sensitive guard $pat"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_monetization: all Lake F1 gates PASS"
