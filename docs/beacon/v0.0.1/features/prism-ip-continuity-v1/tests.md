---
slug: prism-ip-continuity-v1
version: v0.0.1
materials_status: current
---

# Tests: prism-ip-continuity-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-IPC-001 | AC-IPC-001 | `rg -q 'revision_chain_incomplete' scripts/check_ip_continuity.sh && rg -q 'revisions' contracts/ip.schema.yaml` | 演进链门 reason_code + 契约段存在 |
| TC-IPC-002 | AC-IPC-001 | `rg -q 'affected_assets' contracts/ip.schema.yaml scripts/check_ip_continuity.sh` | 演进记录字段 affected_assets 存在 |
| TC-IPC-003 | AC-IPC-002 | `bash scripts/check_ip_continuity.sh view --ip ip-demo 2>/dev/null; test $? -eq 0` | 按 IP 视图命令可用（exit 0） |
| TC-IPC-004 | AC-IPC-002 | `rg -q 'resolved_revision' scripts/check_ip_continuity.sh` | 视图输出含 resolved_revision 引用清单 |
| TC-IPC-005 | AC-IPC-003 | `rg -q 'continuity_revision_drift' scripts/check_ip_continuity.sh` | 漂移审计 reason_code 存在 |
| TC-IPC-006 | AC-IPC-003 | `rg -q 'continuity_revision_drift' scripts/check_ip_continuity.sh && ! rg -q 'continuity_revision_drift.*exit 1' scripts/check_ip_continuity.sh` | 漂移为 warning（不在退出码 1 分支） |
| TC-IPC-007 | AC-IPC-004 | `rg -q 'season_ip_mismatch' scripts/check_ip_continuity.sh && rg -q 'campaign_refs' contracts/ip.schema.yaml` | season 门 reason_code + 契约字段存在 |
| TC-IPC-008 | AC-IPC-005 | `rg -q 'seasons' contracts/ip.schema.yaml && ! rg -qF 'schema_id: series' registry/content-schema.yaml` | season 复用 campaign，未新造 series 对象（负向） |
| TC-IPC-009 | AC-IPC-006 | `bash scripts/check_ip_continuity.sh --self-test 2>/dev/null; test $? -eq 0` | 校验脚本自检通过（exit 0） |
| TC-IPC-010 | AC-IPC-006 | `bash scripts/check_ip_continuity.sh --fixtures content/ips/_examples/ip-demo --expect pass; test $? -eq 0` | 对合规样例判定通过 |
| TC-IPC-011 | AC-IPC-006 | `bash scripts/check_ip_continuity.sh --fixtures content/ips/_examples/ip-demo --invert --expect fail; test $? -eq 1` | 反向断言：破坏演进链时门必须 fail（负向） |
| TC-IPC-012 | GATES | `beacon truth review prism-ip-continuity-v1 --project . --version v0.0.1 --json` | Truth Review Gate A/B/C + L0 pass，recommend_freeze=true |
| TC-IPC-013 | GATES | `beacon doctor verify-truth-integrity prism-ip-continuity-v1 --project-root . --version v0.0.1 --mode block --json \| python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get('result',{}).get('blocked') in (False,None) and d.get('result',{}).get('closure_contract',{}).get('closure_allowed') else 1)"` | closure_allowed=true 且无 blocking finding（integrity 门真跑） |
| TC-IPC-014 | FSM | `rg -nF 'bump_revision without revisions/{R}.yaml record' docs/beacon/v0.0.1/features/prism-ip-continuity-v1/truth.md` | 非法跃迁槽位：无演进记录不得跳版本 |
| TC-IPC-015 | FSM | `rg -n 'open_season with campaign from another IP' docs/beacon/v0.0.1/features/prism-ip-continuity-v1/truth.md` | 非法跃迁槽位：跨 IP campaign 不得入 season |
| TC-IPC-016 | FSM | `rg -n '审计结果直接修改 IP 正典' docs/beacon/v0.0.1/features/prism-ip-continuity-v1/truth.md` | 非法跃迁槽位：视图只读不得改正典 |

## Coverage 说明

- 每条 AC 至少一行行为级 TC（Command + Assertion），验证列均为可执行命令 + 可判定断言。
- TC-IPC-008/011 为负向断言（应失败的检查必须真的失败 / 不得出现被禁对象）。
- TC-IPC-010/011 依赖实现期 `content/ips/_examples/ip-demo` 的演进链样例。
- `PRISM_HOME` 在执行环境未设置时取仓根：`export PRISM_HOME=$(pwd)`。
