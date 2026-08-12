#!/usr/bin/env bash
# Lake E2 metrics-snapshot exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-MSNAP-001 contract fields
test -f contracts/metrics-snapshot.contract.md || fail "metrics-snapshot.contract missing"
for pat in snapshot_id publication_ref collected_at 来源; do
  rg -q "$pat" contracts/metrics-snapshot.contract.md || fail "contract lacks $pat"
done

# AC-MSNAP-002 registry snapshot entries
test -f registry/metrics-adapters.yaml || fail "metrics-adapters.yaml missing"
rg -q "snapshot" registry/metrics-adapters.yaml || fail "snapshot entries missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/metrics-adapters.yaml')); rs=[a for a in d['adapters'] if 'snapshot' in a['name']]; assert len(rs)>=2, 'snapshot adapters <2'" || fail "snapshot adapters <2"

# AC-MSNAP-003 measured guard
for pat in publication_ref "无 publication" measured; do
  rg -q "$pat" contracts/metrics-snapshot.contract.md || fail "contract lacks measured guard $pat"
done

# AC-MSNAP-004 routing
rg -q "metrics-snapshot.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-MSNAP-006 empty snapshot
for pat in 空快照 禁止 不编造 猜; do
  rg -q "$pat" contracts/metrics-snapshot.contract.md || fail "contract lacks empty-snapshot $pat"
done

# AC-MSNAP-007 credentials
for pat in 凭证 密钥 secrets 禁止入库; do
  rg -q "$pat" contracts/metrics-snapshot.contract.md || fail "contract lacks credential guard $pat"
done

# AC-MSNAP-008 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/metrics-snapshot.contract.md || fail "fail-closed missing"

# AC-MSNAP-009 evidence
for pat in collected_at 来源 缺证据; do
  rg -q "$pat" contracts/metrics-snapshot.contract.md || fail "contract lacks evidence $pat"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_metrics_snapshot: all Lake E2 gates PASS"
