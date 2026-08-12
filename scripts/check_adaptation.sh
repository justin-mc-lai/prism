#!/usr/bin/env bash
# Lake F2 adaptation exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-ADP-001 contract fields
test -f contracts/adaptation.contract.md || fail "adaptation.contract missing"
for pat in adaptation_id asset_ref type rights royalty approval; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks $pat"
done

# AC-ADP-002 registry
test -f registry/adaptation-adapters.yaml || fail "adaptation-adapters.yaml missing"
rg -q "rights-record|royalty|license" registry/adaptation-adapters.yaml || fail "adapter entries missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/adaptation-adapters.yaml')); assert len(d['adapters'])>=3, 'adapters <3'" || fail "adapters <3"

# AC-ADP-003 approval / default no grant
for pat in 人工 批准 不授权 默认; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks approval $pat"
done

# AC-ADP-004 routing
rg -q "adaptation.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-ADP-006 no fabrication
for pat in 不编造 缺证据 blocked; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks no-fabrication $pat"
done

# AC-ADP-007 canon protection
for pat in 正典 canon 母稿; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks canon $pat"
done

# AC-ADP-008 license boundary
for pat in license 第三方 未获权 不自动授权; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks license $pat"
done

# AC-ADP-009 sensitive info
for pat in 合同 敏感 secrets 禁止入库; do
  rg -q "$pat" contracts/adaptation.contract.md || fail "contract lacks sensitive guard $pat"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_adaptation: all Lake F2 gates PASS"
