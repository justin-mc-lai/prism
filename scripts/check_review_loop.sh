#!/usr/bin/env bash
# Lake E3 review-loop exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-RVL-001 contract fields
test -f contracts/review-loop.contract.md || fail "review-loop.contract missing"
for pat in review_id campaign_id period metrics_refs findings actions; do
  rg -q "$pat" contracts/review-loop.contract.md || fail "contract lacks $pat"
done

# AC-RVL-002 registry
test -f registry/review-adapters.yaml || fail "review-adapters.yaml missing"
rg -q "bible|retro|findings" registry/review-adapters.yaml || fail "adapter entries missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/review-adapters.yaml')); assert len(d['adapters'])>=3, 'adapters <3'" || fail "adapters <3"

# AC-RVL-003 human approval
for pat in 人工 批准 确认; do
  rg -q "$pat" contracts/review-loop.contract.md || fail "contract lacks approval $pat"
done

# AC-RVL-004 routing
rg -q "review-loop.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-RVL-006 data driven
for pat in metrics_refs 不空谈 blocked; do
  rg -q "$pat" contracts/review-loop.contract.md || fail "contract lacks data-driven $pat"
done

# AC-RVL-007 bible boundary
for pat in 复盘段 母稿 正典 不改; do
  rg -q "$pat" contracts/review-loop.contract.md || fail "contract lacks bible boundary $pat"
done

# AC-RVL-008 maker != checker
rg -q "证据|evidence|maker|checker" contracts/review-loop.contract.md || fail "contract lacks separation"

# AC-RVL-009 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/review-loop.contract.md || fail "fail-closed missing"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_review_loop: all Lake E3 gates PASS"
