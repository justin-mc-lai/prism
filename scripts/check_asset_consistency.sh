#!/usr/bin/env bash
# prism-manga-asset-gate-v1 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-MAG-001 distill reference in director refs
test -f skills/prism-director/references/asset-consistency-gate.md || fail "distill ref missing"
for pat in "身份" "变体" "镜头瞬态" "识别锚点" "CON-01" "CON-04" "AST-05" "画风统一" "lumenx" "drama-skills"; do
  rg -q "$pat" skills/prism-director/references/asset-consistency-gate.md || fail "distill lacks $pat"
done

# AC-MAG-002 gate contract seven sections + fail-closed codes
test -f contracts/asset-consistency.contract.md || fail "gate contract missing"
for pat in identity "决策边界" intake output gate handoff "失败处理" "asset_identity_missing" "禁止自证通过"; do
  rg -q "$pat" contracts/asset-consistency.contract.md || fail "gate contract lacks $pat"
done

# AC-MAG-003 manga_drama wiring (intake anchor + gate upgrade)
rg -q "asset-consistency.contract" contracts/form-manga-drama.contract.md || fail "manga contract lacks gate ref"
rg -q "识别锚点|未决项不得流入分镜" contracts/form-manga-drama.contract.md || fail "manga intake lacks anchor rule"

# AC-MAG-004 registry chain mentions the gate
rg -q "资产一致性门.*asset-consistency" registry/form-registry.yaml || fail "registry chain lacks gate step"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); m=[f for f in d['forms'] if f['form']=='manga_drama']; assert m and 'asset-consistency' in m[0]['producer_chain']" || fail "registry manga_drama chain invalid"

# AC-MAG-007 inventory A4 standing decision note
rg -q "MoneyPrinterTurbo.*defer-pin|defer-pin.*MoneyPrinterTurbo" registry/source-capability-inventory.md || fail "inventory lacks defer-pin decision"

# upstream runtime not pinned
test ! -d vendor/skills/lumenx || fail "lumenx runtime must not be pinned"
test ! -d vendor/skills/dramaclaw || fail "dramaclaw must not be pinned (Elastic-2.0)"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_asset_consistency: all prism-manga-asset-gate-v1 gates PASS"
