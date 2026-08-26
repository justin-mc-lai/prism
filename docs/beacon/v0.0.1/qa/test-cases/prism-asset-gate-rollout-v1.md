---
slug: prism-asset-gate-rollout-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-asset-gate-rollout-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-RLO-001 | AC-RLO-001 | `rg -n "资产一致性门" contracts/form-live-drama.contract.md && rg -n "asset-consistency.contract" contracts/form-live-drama.contract.md` | live_drama 契约接线 |
| TC-RLO-002 | AC-RLO-002 | `rg -n "资产一致性\|asset-consistency" contracts/form-av.contract.md` | comic 路由接线 |
| TC-RLO-003 | AC-RLO-003 | `python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); c={f['form']:f['producer_chain'] for f in d['forms']}; assert 'asset-consistency' in c['live_drama'] and 'asset-consistency' in c['comic']"` | 两链含门步骤 |
| TC-RLO-004 | AC-RLO-004 | `bash scripts/check_asset_consistency.sh` | exec-layer 校验 PASS |
