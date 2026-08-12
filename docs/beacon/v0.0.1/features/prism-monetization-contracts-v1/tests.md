---
slug: prism-monetization-contracts-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-monetization-contracts-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-MON-001 | AC-MON-001 | `test -f contracts/monetization.contract.md && rg -n "deal_id|type|terms|disclosure|evidence" contracts/monetization.contract.md` | 变现契约含核心字段 |
| TC-MON-002 | AC-MON-002 | `test -f registry/monetization-adapters.yaml && rg -n "deal-record|compliance|disclosure" registry/monetization-adapters.yaml` | 变现 bridge 登记 |
| TC-MON-003 | AC-MON-003 | `rg -n "人工|批准|approval" contracts/monetization.contract.md` | 人工批准 |
| TC-MON-004 | AC-MON-004 | `rg -n "monetization.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由变现引用 |
| TC-MON-005 | AC-MON-005 | `test -x scripts/check_monetization.sh` | exec 脚本存在且可执行 |
| TC-MON-006 | AC-MON-005 | `bash scripts/check_monetization.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-MON-007 | AC-MON-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/monetization-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=3 else 1)"` | ≥3 个变现 bridge |
| TC-MON-008 | AC-MON-006 | `rg -n "不编造|缺证据|blocked" contracts/monetization.contract.md` | 不编造收入 |
| TC-MON-009 | AC-MON-007 | `rg -n "披露|广告|赞助|标注" contracts/monetization.contract.md` | 披露义务 |
| TC-MON-010 | AC-MON-008 | `rg -n "health|legal|finance|合规" contracts/monetization.contract.md` | 风险合规门 |
| TC-MON-011 | AC-MON-009 | `rg -n "收款|敏感|secrets|禁止入库" contracts/monetization.contract.md` | 敏感信息保护 |
| TC-MON-012 | AC-MON-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md && rg -n "F2" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md` | 分湖边界存在 |
| TC-MON-013 | AC-MON-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-MON-014 | AC-MON-001 | `rg -n "US-MON-001|变现" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md` | 变现旅程可追溯 |
| TC-MON-015 | AC-MON-008 | `rg -n "US-MON-002|合规" docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md` | 合规拒绝路径可追溯 |
