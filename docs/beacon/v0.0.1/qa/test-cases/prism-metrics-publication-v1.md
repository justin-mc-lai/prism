---
slug: prism-metrics-publication-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-metrics-publication-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-MPUB-001 | AC-MPUB-001 | `test -f contracts/metrics-publication.contract.md && rg -n "publication_id|platform|url|published_at|artifact_ref" contracts/metrics-publication.contract.md` | 发布事件契约含核心字段 |
| TC-MPUB-002 | AC-MPUB-002 | `test -f registry/metrics-adapters.yaml && rg -n "analyze-data" registry/metrics-adapters.yaml` | 统计 bridge 登记存在 |
| TC-MPUB-003 | AC-MPUB-003 | `rg -n "measured|publication_record|无 publication" contracts/metrics-publication.contract.md` | measured 守卫声明 |
| TC-MPUB-004 | AC-MPUB-004 | `rg -n "metrics-publication.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由回流引用 |
| TC-MPUB-005 | AC-MPUB-005 | `test -x scripts/check_metrics_publication.sh` | exec 脚本存在且可执行 |
| TC-MPUB-006 | AC-MPUB-005 | `bash scripts/check_metrics_publication.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-MPUB-007 | AC-MPUB-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/metrics-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=3 else 1)"` | ≥3 个 bridge 条目 |
| TC-MPUB-008 | AC-MPUB-006 | `rg -n "空快照|禁止|不编造|猜" contracts/metrics-publication.contract.md` | 不编造指标声明 |
| TC-MPUB-009 | AC-MPUB-007 | `rg -n "凭证|密钥|secrets|禁止入库" contracts/metrics-publication.contract.md` | 凭证保护 |
| TC-MPUB-010 | AC-MPUB-008 | `rg -n "fail-closed|blocked|reason_code" contracts/metrics-publication.contract.md` | bridge fail-closed |
| TC-MPUB-011 | AC-MPUB-009 | `rg -n "publication_id|url|时间|缺证据" contracts/metrics-publication.contract.md` | 证据要求 |
| TC-MPUB-012 | AC-MPUB-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md && rg -n "E2|E3|E4" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md` | 分湖边界存在 |
| TC-MPUB-013 | AC-MPUB-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md` | illegal 转移覆盖 |
| TC-MPUB-014 | AC-MPUB-001 | `rg -n "US-MPUB-001|发布事件" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md` | 回流旅程可追溯 |
| TC-MPUB-015 | AC-MPUB-003 | `rg -n "US-MPUB-002|publication_record_missing" docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md` | 无记录拒绝路径可追溯 |
