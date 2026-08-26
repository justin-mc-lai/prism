---
slug: prism-form-product-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-product-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-PRD-001 | AC-PRD-001 | `test -f registry/form-registry.yaml && rg -n "product" registry/form-registry.yaml && rg -n "form-product.contract" registry/form-registry.yaml` | form registry 注册 product |
| TC-PRD-002 | AC-PRD-002 | `test -f contracts/form-product.contract.md && rg -c "identity|决策边界|intake|output|gate|handoff|失败处理" contracts/form-product.contract.md` | 契约七节齐全 |
| TC-PRD-003 | AC-PRD-003 | `rg -n "product_fact_missing|极限词\|广告法\|fail-closed\|规格\|价格" contracts/form-product.contract.md` | 事实门+合规门声明 |
| TC-PRD-004 | AC-PRD-004 | `test -f skills/_internal/orchestration/form-autodetect.md && rg -n "novel\|vlog\|manga_drama\|live_drama\|product" skills/_internal/orchestration/form-autodetect.md && rg -n "classify_form" skills/prism-goal/references/modes/loop-campaign.md` | classify_form 落地+goal 接线 |
| TC-PRD-005 | AC-PRD-005 | `rg -n "电商商品\|form-product.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由含电商行 |
| TC-PRD-006 | AC-PRD-006 | `bash scripts/check_product_form.sh` | exec-layer 校验 PASS（合法路径） |
| TC-PRD-007 | AC-PRD-001 | `python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert 'product' in fs"` | registry YAML 含 product |
| TC-PRD-008 | AC-PRD-007 | `test -d vendor/skills/drama-skills/skills && test -f vendor/skills/drama-skills/LICENSE && rg -n "drama-skills" docs/ATTRIBUTION-bridges.md` | drama-skills pin+ATTRIBUTION |
| TC-PRD-009 | AC-PRD-008 | `rg -n "lumenx\|dramaclaw\|MoneyPrinterTurbo\|openstory\|drama-skills" registry/source-capability-inventory.md` | inventory 五库入册 |
| TC-PRD-010 | AC-PRD-009 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md && rg -n "Elastic-2.0\|海 closure" docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md` | 分湖边界存在 |
