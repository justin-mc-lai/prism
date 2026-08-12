#!/usr/bin/env bash
# Lake E1 metrics-publication exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-MPUB-001 contract fields
test -f contracts/metrics-publication.contract.md || fail "metrics-publication.contract missing"
for pat in publication_id platform url published_at artifact_ref; do
  rg -q "$pat" contracts/metrics-publication.contract.md || fail "contract lacks $pat"
done

# AC-MPUB-002 registry
test -f registry/metrics-adapters.yaml || fail "metrics-adapters.yaml missing"
rg -q "analyze-data" registry/metrics-adapters.yaml || fail "adapter analyze-data missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/metrics-adapters.yaml')); assert len(d['adapters'])>=3, 'adapters <3'" || fail "adapters <3"

# AC-MPUB-003 measured guard
for pat in measured publication_record "无 publication"; do
  rg -q "$pat" contracts/metrics-publication.contract.md || fail "contract lacks measured guard $pat"
done

# AC-MPUB-004 routing
rg -q "metrics-publication.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-MPUB-006 no fabrication
for pat in 空快照 禁止 不编造 猜; do
  rg -q "$pat" contracts/metrics-publication.contract.md || fail "contract lacks no-fabrication $pat"
done

# AC-MPUB-007 credentials
for pat in 凭证 密钥 secrets 禁止入库; do
  rg -q "$pat" contracts/metrics-publication.contract.md || fail "contract lacks credential guard $pat"
done

# AC-MPUB-008 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/metrics-publication.contract.md || fail "fail-closed missing"

# AC-MPUB-009 evidence
for pat in publication_id url 时间 缺证据; do
  rg -q "$pat" contracts/metrics-publication.contract.md || fail "contract lacks evidence $pat"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_metrics_publication: all Lake E1 gates PASS"
