#!/usr/bin/env bash
# prism-form-product-v1 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-PRD-001 registry
test -f registry/form-registry.yaml || fail "form-registry.yaml missing"
rg -q "product" registry/form-registry.yaml || fail "product missing in registry"
rg -q "form-product.contract" registry/form-registry.yaml || fail "product contract ref missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert 'product' in fs, 'product missing'" || fail "registry product invalid"

# AC-PRD-002 contract intake/output/evidence
test -f contracts/form-product.contract.md || fail "form-product.contract missing"
for pat in intake output "content/presentations" "证据|evidence" "reason_code"; do
  rg -q "$pat" contracts/form-product.contract.md || fail "product contract lacks $pat"
done

# AC-PRD-003 fact + compliance gates
for pat in "product_fact_missing" "规格|价格" "极限词|广告法" "fail-closed"; do
  rg -q "$pat" contracts/form-product.contract.md || fail "product contract lacks gate $pat"
done

# AC-PRD-004 classify_form kernel + goal wiring
test -f skills/_internal/orchestration/form-autodetect.md || fail "form-autodetect.md missing"
for pat in product novel vlog manga_drama live_drama "禁止静默猜测|禁止.*猜测" form_detected; do
  rg -q "$pat" skills/_internal/orchestration/form-autodetect.md || fail "autodetect lacks $pat"
done
rg -q "classify_form" skills/prism-goal/references/modes/loop-campaign.md || fail "goal state machine lacks classify_form"

# AC-PRD-005 routing row
rg -q "电商商品|form-product.contract" skills/_internal/orchestration/creation-mode-map.md || fail "mode-map lacks product row"

# AC-PRD-007 drama-skills pin + attribution
test -d vendor/skills/drama-skills/skills || fail "drama-skills not pinned under vendor/skills/"
test -f vendor/skills/drama-skills/LICENSE || fail "drama-skills LICENSE missing"
rg -q "drama-skills" docs/ATTRIBUTION-bridges.md || fail "ATTRIBUTION lacks drama-skills"

# AC-PRD-008 inventory batch
rg -q "alibaba/lumenx|lumenx" registry/source-capability-inventory.md || fail "inventory lacks lumenx"
for repo in dramaclaw MoneyPrinterTurbo openstory drama-skills; do
  rg -q "$repo" registry/source-capability-inventory.md || fail "inventory lacks $repo"
done

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_product_form: all prism-form-product-v1 gates PASS"
