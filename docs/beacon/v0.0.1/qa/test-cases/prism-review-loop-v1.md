---
slug: prism-review-loop-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-review-loop-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-RVL-001 | AC-RVL-001 | `test -f contracts/review-loop.contract.md && rg -n "review_id|campaign_id|period|metrics_refs|findings|actions" contracts/review-loop.contract.md` | 复盘契约含核心字段 |
| TC-RVL-002 | AC-RVL-002 | `test -f registry/review-adapters.yaml && rg -n "bible|retro|findings" registry/review-adapters.yaml` | 复盘 bridge 登记 |
| TC-RVL-003 | AC-RVL-003 | `rg -n "人工|批准|确认" contracts/review-loop.contract.md` | 人工批准入库 |
| TC-RVL-004 | AC-RVL-004 | `rg -n "review-loop.contract" skills/_internal/orchestration/creation-mode-map.md` | 系列圣经路由引用 |
| TC-RVL-005 | AC-RVL-005 | `test -x scripts/check_review_loop.sh` | exec 脚本存在且可执行 |
| TC-RVL-006 | AC-RVL-005 | `bash scripts/check_review_loop.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-RVL-007 | AC-RVL-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/review-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=3 else 1)"` | ≥3 个复盘 bridge |
| TC-RVL-008 | AC-RVL-006 | `rg -n "metrics_refs|不空谈|blocked" contracts/review-loop.contract.md` | 数据驱动声明 |
| TC-RVL-009 | AC-RVL-007 | `rg -n "复盘段|母稿|正典|不改" contracts/review-loop.contract.md` | 圣经更新边界 |
| TC-RVL-010 | AC-RVL-008 | `rg -n "证据|evidence|maker|checker" contracts/review-loop.contract.md && test -f skills/prism-qa/references/anti-slop-gate.md` | maker≠checker 分离 |
| TC-RVL-011 | AC-RVL-009 | `rg -n "fail-closed|blocked|reason_code" contracts/review-loop.contract.md` | bridge fail-closed |
| TC-RVL-012 | AC-RVL-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md && rg -n "E4|Lake F" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md` | 分湖边界存在 |
| TC-RVL-013 | AC-RVL-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md` | illegal 转移覆盖 |
| TC-RVL-014 | AC-RVL-001 | `rg -n "US-RVL-001|复盘" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md` | 复盘旅程可追溯 |
| TC-RVL-015 | AC-RVL-006 | `rg -n "US-RVL-002|metrics_refs" docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md` | 无数据拒绝路径可追溯 |
