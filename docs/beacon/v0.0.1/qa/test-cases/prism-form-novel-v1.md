---
slug: prism-form-novel-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-novel-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-NVL-001 | AC-NVL-001 | `test -f registry/form-registry.yaml && rg -n "novel" registry/form-registry.yaml && rg -n "form-novel.contract" registry/form-registry.yaml` | form registry 注册 novel |
| TC-NVL-002 | AC-NVL-002 | `test -f contracts/form-novel.contract.md && rg -n "StoryMaster|episode|content/storyworlds|证据|evidence" contracts/form-novel.contract.md` | novel 契约含输入/结构/输出/证据 |
| TC-NVL-003 | AC-NVL-003 | `rg -n "canon_gate_status|review_required|failed|generated|fast_lane_skip" contracts/form-novel.contract.md` | canon 钩子声明 |
| TC-NVL-004 | AC-NVL-004 | `rg -n "novel|form-novel.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由含 novel 行 |
| TC-NVL-005 | AC-NVL-005 | `test -x scripts/check_novel_form.sh` | exec 脚本存在且可执行 |
| TC-NVL-006 | AC-NVL-005 | `bash scripts/check_novel_form.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-NVL-007 | AC-NVL-001 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; raise SystemExit(0 if 'novel' in fs else 1)"` | registry 含 novel |
| TC-NVL-008 | AC-NVL-006 | `rg -n "kushi-narrative-zh|fail-closed|blocked|reason_code" contracts/form-novel.contract.md` | bridge fail-closed |
| TC-NVL-009 | AC-NVL-007 | `rg -n "content/storyworlds|bible|canon-ledger" contracts/form-novel.contract.md` | StoryWorld 路径引用 |
| TC-NVL-010 | AC-NVL-008 | `test -f skills/prism-qa/references/anti-slop-gate.md && rg -n "证据|原文行" skills/prism-qa/references/anti-slop-gate.md` | maker≠checker 证据 |
| TC-NVL-011 | AC-NVL-009 | `rg -n "OOC|设定漂移|fail-closed|事实错误" contracts/form-novel.contract.md` | OOC/连续性门 |
| TC-NVL-012 | AC-NVL-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md && rg -n "D5|D6" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md` | 分湖边界存在 |
| TC-NVL-013 | AC-NVL-010 | `rg -n "Illegal|illegal|宣称 Lake D" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md` | illegal 转移覆盖 |
| TC-NVL-014 | AC-NVL-002 | `rg -n "US-PRISM-002|连载" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md` | 连载旅程可追溯 |
| TC-NVL-015 | AC-NVL-003 | `rg -n "US-NVL-002|canon_gate_status" docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md` | canon 拒绝路径可追溯 |
