---
slug: prism-ip-import-gate-v1
version: v0.0.1
materials_status: current
---

# Tests: prism-ip-import-gate-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-IPG-001 | AC-IPG-001 | `rg -qF 'schema_id: crossovers' registry/content-schema.yaml && rg -qF 'content/crossovers/{crossover_id}.yaml' registry/content-schema.yaml && test -f contracts/crossover.schema.yaml` | crossovers 对象注册且契约存在 |
| TC-IPG-002 | AC-IPG-001 | `for f in crossover_id participant_ips work_ref authorization attribution; do rg -q "$f" contracts/crossover.schema.yaml || exit 1; done` | 联名契约五个必填字段声明 |
| TC-IPG-003 | AC-IPG-002 | `rg -q 'crossover_authorization_missing' scripts/check_ip_import_gate.sh` | 授权门 reason_code 存在 |
| TC-IPG-004 | AC-IPG-003 | `rg -q 'crossover_disclosure_missing' scripts/check_ip_import_gate.sh && rg -q 'disclosure_note' contracts/crossover.schema.yaml` | 披露门 reason_code + 契约字段 |
| TC-IPG-005 | AC-IPG-004 | `rg -q 'crossover_royalty_unrecorded' scripts/check_ip_import_gate.sh && rg -q 'royalty_split' contracts/crossover.schema.yaml` | 分成门 reason_code + 契约字段 |
| TC-IPG-006 | AC-IPG-005 | `rg -q 'crossover_canon_unmet' scripts/check_ip_import_gate.sh` | 正典聚合门 reason_code 存在 |
| TC-IPG-007 | AC-IPG-006 | `bash scripts/check_ip_import_gate.sh --self-test 2>/dev/null; test $? -eq 0` | 门脚本自检通过（exit 0） |
| TC-IPG-008 | AC-IPG-006 | `bash scripts/check_ip_import_gate.sh --fixtures content/crossovers/_examples --expect pass; test $? -eq 0` | 对合规样例判定通过 |
| TC-IPG-009 | AC-IPG-006 | `bash scripts/check_ip_import_gate.sh --fixtures content/crossovers/_examples --invert --expect fail; test $? -eq 1` | 反向断言：破坏联名记录时门必须 fail（负向） |
| TC-IPG-010 | AC-IPG-007 | `rg -q 'monetization.contract' contracts/crossover.schema.yaml && rg -q 'adaptation.contract' contracts/crossover.schema.yaml` | 与 F1/F2 叠加 hook 在联名契约中引用 |
| TC-IPG-011 | GATES | `beacon truth review prism-ip-import-gate-v1 --project . --version v0.0.1 --json` | Truth Review Gate A/B/C + L0 pass，recommend_freeze=true |
| TC-IPG-012 | GATES | `beacon doctor verify-truth-integrity prism-ip-import-gate-v1 --project-root . --version v0.0.1 --mode block --json \| python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get('result',{}).get('blocked') in (False,None) and d.get('result',{}).get('closure_contract',{}).get('closure_allowed') else 1)"` | closure_allowed=true 且无 blocking finding（integrity 门真跑） |
| TC-IPG-013 | FSM | `rg -n 'draft → approved without authorization_recorded' docs/beacon/v0.0.1/features/prism-ip-import-gate-v1/truth.md` | 非法跃迁槽位：无授权不得直接批准 |
| TC-IPG-014 | FSM | `rg -n 'approved → 发布 while disclosure_note 为空' docs/beacon/v0.0.1/features/prism-ip-import-gate-v1/truth.md` | 非法跃迁槽位：无披露不得发布 |
| TC-IPG-015 | FSM | `rg -n '参与 IP 非 active 时提交 review' docs/beacon/v0.0.1/features/prism-ip-import-gate-v1/truth.md` | 非法跃迁槽位：参与 IP 非 active 不得提交 |

## Coverage 说明

- 每条 AC 至少一行行为级 TC（Command + Assertion），验证列均为可执行命令 + 可判定断言。
- TC-IPG-009 为负向断言（应失败的检查必须真的失败）。
- TC-IPG-008/009 依赖实现期 `content/crossovers/_examples` 样例。
- `PRISM_HOME` 在执行环境未设置时取仓根：`export PRISM_HOME=$(pwd)`。
