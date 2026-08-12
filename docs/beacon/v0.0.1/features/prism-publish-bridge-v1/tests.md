---
slug: prism-publish-bridge-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-publish-bridge-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-PUB-001 | AC-PUB-001 | `test -f contracts/publish-bridge.contract.md && rg -n "publish-content|schedule-post|x-publish|manage-media" contracts/publish-bridge.contract.md` | 发布桥契约含路由 |
| TC-PUB-002 | AC-PUB-002 | `test -f registry/publish-adapters.yaml && rg -n "publish-content" registry/publish-adapters.yaml && rg -n "schedule-post" registry/publish-adapters.yaml` | adapter 登记存在 |
| TC-PUB-003 | AC-PUB-003 | `rg -n "草稿|人工|二次批准|公开" contracts/publish-bridge.contract.md` | 草稿-only + 人工门 |
| TC-PUB-004 | AC-PUB-004 | `rg -n "superseded-misrouted|do_not_publish|误" contracts/publish-bridge.contract.md` | 误路由守卫 |
| TC-PUB-005 | AC-PUB-005 | `test -x scripts/check_publish_bridge.sh` | exec 脚本存在且可执行 |
| TC-PUB-006 | AC-PUB-005 | `bash scripts/check_publish_bridge.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-PUB-007 | AC-PUB-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/publish-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=4 else 1)"` | ≥4 个 bridge 条目 |
| TC-PUB-008 | AC-PUB-006 | `rg -n "publish-bridge.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由引用发布桥 |
| TC-PUB-009 | AC-PUB-007 | `rg -n "fail-closed|blocked|reason_code" contracts/publish-bridge.contract.md` | bridge fail-closed |
| TC-PUB-010 | AC-PUB-008 | `rg -n "凭证|密钥|secrets|\.env|禁止入库" contracts/publish-bridge.contract.md` | 凭证保护声明 |
| TC-PUB-011 | AC-PUB-009 | `rg -n "draft_id|URL|证据|evidence|已发布" contracts/publish-bridge.contract.md` | 发布证据要求 |
| TC-PUB-012 | AC-PUB-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md && rg -n "Lake E|Lake F|sync-ai" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md` | 分湖边界存在 |
| TC-PUB-013 | AC-PUB-010 | `rg -n "Illegal|illegal|无人工|宣称海" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-PUB-014 | AC-PUB-003 | `rg -n "US-PUB-001|草稿" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md` | 草稿旅程可追溯 |
| TC-PUB-015 | AC-PUB-004 | `rg -n "US-PUB-002|误传|do_not_publish" docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md` | 误路由旅程可追溯 |
