---
slug: prism-form-writing-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-writing-v1（qa/test-cases 镜像）

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-WRITE-001 | AC-WRITE-001 | `test -f contracts/writing.contract.md && rg -n "identity|决策边界|失败处理" contracts/writing.contract.md && rg -n "四段式|倒金字塔|emotional" contracts/writing.contract.md` | 写作契约存在且含七段与蒸馏规则 |
| TC-WRITE-002 | AC-WRITE-002 | `test -f skills/prism-qa/references/anti-slop-gate.md && rg -n "二元对比|清嗓|weasel|假深刻|总结复读" skills/prism-qa/references/anti-slop-gate.md && rg -n "证据|原文行" skills/prism-qa/references/anti-slop-gate.md` | 反 slop 门存在且覆盖模式与证据要求 |
| TC-WRITE-003 | AC-WRITE-003 | `test -f registry/writing-adapters.yaml && rg -n "humanizer-zh" registry/writing-adapters.yaml && rg -n "selfmedia-humanize" registry/writing-adapters.yaml && rg -n "fail-closed|blocked" registry/writing-adapters.yaml` | bridge 登记表存在 |
| TC-WRITE-004 | AC-WRITE-004 | `rg -n "MAP-005" skills/_internal/orchestration/creation-mode-map.md && rg -n "writing.contract|anti-slop-gate" skills/_internal/orchestration/creation-mode-map.md` | 路由引用契约与门禁 |
| TC-WRITE-005 | AC-WRITE-005 | `test -x scripts/check_writing_adapters.sh` | exec 校验脚本存在且可执行 |
| TC-WRITE-006 | AC-WRITE-005 | `bash scripts/check_writing_adapters.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-WRITE-007 | AC-WRITE-003 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/writing-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=8 else 1)"` | ≥8 个 bridge 条目 |
| TC-WRITE-008 | AC-WRITE-006 | `test ! -f skills/_internal/adapters/SKILL.md && test ! -f skills/prism-qa/references/SKILL.md && test ! -f skills/prism-produce/references/SKILL.md` | 无顶层 SKILL.md 泄漏 |
| TC-WRITE-009 | AC-WRITE-007 | `rg -n "fail-closed|blocked|reason_code" contracts/writing.contract.md` | bridge fail-closed 规则声明 |
| TC-WRITE-010 | AC-WRITE-008 | `test -f contracts/writing.contract.md && test -f skills/prism-qa/references/anti-slop-gate.md && rg -n "evidence|证据" skills/prism-qa/references/anti-slop-gate.md` | maker≠checker 分离且 qa 含证据 |
| TC-WRITE-011 | AC-WRITE-009 | `rg -n "不承诺|必过|占位" skills/prism-qa/references/anti-slop-gate.md` | 硬边界声明 |
| TC-WRITE-012 | AC-WRITE-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md && rg -n "D2|D3|D4|D5|D6" docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md` | 分湖边界存在 |
| TC-WRITE-013 | AC-WRITE-010 | `rg -n "Illegal|illegal|宣称 Lake D" docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-WRITE-014 | AC-WRITE-001 | `rg -n "US-PRISM-001|成稿" docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md && rg -n "writing.contract" contracts/writing.contract.md` | US-PRISM-001 成稿链可追溯 |
| TC-WRITE-015 | AC-WRITE-002 | `python3 -c "import re; t=open('skills/prism-qa/references/anti-slop-gate.md').read(); pats=re.findall(r'^[-*] ', t, re.M); raise SystemExit(0 if len(pats)>=15 else 1)"` | 模式与判据合计 ≥15 条 |
