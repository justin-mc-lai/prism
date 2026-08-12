#!/usr/bin/env bash
# Lake D6 publish bridge exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-PUB-001 contract + routes
test -f contracts/publish-bridge.contract.md || fail "publish-bridge.contract missing"
for pat in publish-content schedule-post x-publish manage-media; do
  rg -q "$pat" contracts/publish-bridge.contract.md || fail "contract lacks $pat"
done

# AC-PUB-002 registry
test -f registry/publish-adapters.yaml || fail "publish-adapters.yaml missing"
rg -q "publish-content" registry/publish-adapters.yaml || fail "adapter publish-content missing"
rg -q "schedule-post" registry/publish-adapters.yaml || fail "adapter schedule-post missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/publish-adapters.yaml')); assert len(d['adapters'])>=4, 'adapters <4'" || fail "adapters <4"

# AC-PUB-003 draft-only + human gate
for pat in 草稿 人工 二次批准 公开; do
  rg -q "$pat" contracts/publish-bridge.contract.md || fail "contract lacks $pat"
done

# AC-PUB-004 misroute guard
for pat in superseded-misrouted do_not_publish 误; do
  rg -q "$pat" contracts/publish-bridge.contract.md || fail "contract lacks $pat"
done

# AC-PUB-006 routing
rg -q "publish-bridge.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-PUB-007 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/publish-bridge.contract.md || fail "fail-closed missing"

# AC-PUB-008 credentials protection
for pat in 凭证 密钥 secrets 禁止入库; do
  rg -q "$pat" contracts/publish-bridge.contract.md || fail "contract lacks credential guard $pat"
done

# AC-PUB-009 evidence
for pat in draft_id URL 证据 已发布; do
  rg -q "$pat" contracts/publish-bridge.contract.md || fail "contract lacks evidence $pat"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_publish_bridge: all Lake D6 gates PASS"
