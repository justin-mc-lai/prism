---
slug: prism-form-blog-thread-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-blog-thread-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-FORM-001 | AC-FORM-001 | `test -f registry/form-registry.yaml && rg -n "blog" registry/form-registry.yaml && rg -n "thread" registry/form-registry.yaml && rg -n "form-blog.contract|form-thread.contract" registry/form-registry.yaml` | form registry 注册 blog/thread |
| TC-FORM-002 | AC-FORM-002 | `test -f contracts/form-blog.contract.md && rg -n "四段式|母稿|director|humanized.md" contracts/form-blog.contract.md && rg -n "证据|evidence" contracts/form-blog.contract.md` | blog 契约含输入/结构/输出/证据 |
| TC-FORM-003 | AC-FORM-003 | `test -f contracts/form-thread.contract.md && rg -n "倒金字塔|fast_lane_skip|canon|writing-agent" contracts/form-thread.contract.md` | thread 契约含快道与 canon 门禁 |
| TC-FORM-004 | AC-FORM-004 | `rg -n "form-blog.contract|form-thread.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由引用 form 契约 |
| TC-FORM-005 | AC-FORM-005 | `test -x scripts/check_blog_thread_forms.sh` | exec 脚本存在且可执行 |
| TC-FORM-006 | AC-FORM-005 | `bash scripts/check_blog_thread_forms.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-FORM-007 | AC-FORM-001 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; raise SystemExit(0 if {'blog','thread'}<=fs else 1)"` | registry 含 blog+thread 且字段合法 |
| TC-FORM-008 | AC-FORM-006 | `rg -n "registry|form contract|路由表|主链" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md && test ! -f skills/_internal/adapters/SKILL.md` | 扩展规则声明 + 无 SKILL.md 泄漏 |
| TC-FORM-009 | AC-FORM-007 | `rg -n "canon|fast_lane_skip" contracts/form-thread.contract.md && rg -n "illegal|禁止" contracts/form-thread.contract.md` | 快道/canon 门禁 |
| TC-FORM-010 | AC-FORM-008 | `rg -n "fail-closed|blocked|reason_code" contracts/form-blog.contract.md contracts/form-thread.contract.md` | bridge fail-closed 声明 |
| TC-FORM-011 | AC-FORM-009 | `test -f skills/prism-qa/references/anti-slop-gate.md && rg -n "证据|原文行" skills/prism-qa/references/anti-slop-gate.md` | maker≠checker 证据要求 |
| TC-FORM-012 | AC-FORM-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md && rg -n "D3|D4|D5|D6" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md` | 分湖边界存在 |
| TC-FORM-013 | AC-FORM-010 | `rg -n "Illegal|illegal|宣称 Lake D" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md` | illegal 转移覆盖 |
| TC-FORM-014 | AC-FORM-002 | `rg -n "US-PRISM-001|blog" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md` | US-PRISM-001 blog 链可追溯 |
| TC-FORM-015 | AC-FORM-003 | `rg -n "US-PRISM-005|thread|快道" docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md` | US-PRISM-005 thread 快道可追溯 |
