---
slug: prism-adaptation-contracts-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-adaptation-contracts-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-ADP-001 | AC-ADP-001 | `test -f contracts/adaptation.contract.md && rg -n "adaptation_id|asset_ref|type|rights|royalty|approval" contracts/adaptation.contract.md` | 改编契约含核心字段 |
| TC-ADP-002 | AC-ADP-002 | `test -f registry/adaptation-adapters.yaml && rg -n "rights-record|royalty|license" registry/adaptation-adapters.yaml` | 改编 bridge 登记 |
| TC-ADP-003 | AC-ADP-003 | `rg -n "人工|批准|不授权|默认" contracts/adaptation.contract.md` | 人工批准/默认不授权 |
| TC-ADP-004 | AC-ADP-004 | `rg -n "adaptation.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由改编引用 |
| TC-ADP-005 | AC-ADP-005 | `test -x scripts/check_adaptation.sh` | exec 脚本存在且可执行 |
| TC-ADP-006 | AC-ADP-005 | `bash scripts/check_adaptation.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-ADP-007 | AC-ADP-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/adaptation-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=3 else 1)"` | ≥3 个改编 bridge |
| TC-ADP-008 | AC-ADP-006 | `rg -n "不编造|缺证据|blocked" contracts/adaptation.contract.md` | 不编造授权/分成 |
| TC-ADP-009 | AC-ADP-007 | `rg -n "正典|canon|母稿" contracts/adaptation.contract.md` | 正典保护 |
| TC-ADP-010 | AC-ADP-008 | `rg -n "license|第三方|未获权|不自动授权" contracts/adaptation.contract.md` | license 边界 |
| TC-ADP-011 | AC-ADP-009 | `rg -n "合同|敏感|secrets|禁止入库" contracts/adaptation.contract.md` | 敏感信息保护 |
| TC-ADP-012 | AC-ADP-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md && rg -n "授权 API" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md` | 分湖边界存在 |
| TC-ADP-013 | AC-ADP-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md` | illegal 转移覆盖 |
| TC-ADP-014 | AC-ADP-001 | `rg -n "US-ADP-001|改编" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md` | 改编旅程可追溯 |
| TC-ADP-015 | AC-ADP-003 | `rg -n "US-ADP-002|不自动授权" docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md` | 未授权拒绝路径可追溯 |
