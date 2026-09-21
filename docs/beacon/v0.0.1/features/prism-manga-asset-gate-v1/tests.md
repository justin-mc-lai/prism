---
slug: prism-manga-asset-gate-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-manga-asset-gate-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-MAG-001 | AC-MAG-001 | `test -f skills/prism-director/references/asset-consistency-gate.md && rg -n "身份\|变体\|镜头瞬态\|CON-01\|CON-04\|AST-05" skills/prism-director/references/asset-consistency-gate.md` | 蒸馏参考含框架关键词 |
| TC-MAG-002 | AC-MAG-002 | `test -f contracts/asset-consistency.contract.md && rg -c "identity\|决策边界\|intake\|output\|gate\|handoff\|失败处理" contracts/asset-consistency.contract.md && rg -n "asset_identity_missing" contracts/asset-consistency.contract.md` | 门契约七节+fail-closed 码 |
| TC-MAG-003 | AC-MAG-003 | `rg -n "asset-consistency.contract" contracts/form-manga-drama.contract.md && rg -n "识别锚点" contracts/form-manga-drama.contract.md` | manga 契约接线 |
| TC-MAG-004 | AC-MAG-004 | `python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); m=[f for f in d['forms'] if f['form']=='manga_drama'][0]; assert 'asset-consistency' in m['producer_chain']"` | registry 链含门步骤 |
| TC-MAG-005 | AC-MAG-005 | `bash scripts/check_asset_consistency.sh` | exec-layer 校验 PASS |
| TC-MAG-006 | AC-MAG-006 | `test ! -d vendor/skills/lumenx && test ! -d vendor/skills/dramaclaw` | 上游运行时未 pin |
| TC-MAG-007 | AC-MAG-007 | `rg -n "defer-pin\|A4" registry/source-capability-inventory.md` | A4 常设决策入册 |
| TC-MAG-008 | AC-MAG-002 | `rg -n "Illegal transitions" docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md && rg -n "未决资产项流入图片提示词或分镜|无变化记录支撑仍通过|宣称本门可替代正典门" docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
