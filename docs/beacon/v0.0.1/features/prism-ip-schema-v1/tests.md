---
slug: prism-ip-schema-v1
version: v0.0.1
materials_status: current
---

# Tests: prism-ip-schema-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-IPM-001 | AC-IPM-001 | `rg -n 'schema_id:\s*ip' registry/content-schema.yaml && rg -n 'root:\s*content/ips/\{ip_id\}/' registry/content-schema.yaml && test -f contracts/ip.schema.yaml` | IP 对象已注册且契约文件存在 |
| TC-IPM-002 | AC-IPM-001 | `for f in ip_id title kind status canon_revision publish_identity_ref; do rg -q "$f" contracts/ip.schema.yaml || exit 1; done` | ip.yaml 六个必填字段在契约中声明 |
| TC-IPM-003 | AC-IPM-001 | `rg -n 'archived' contracts/ip.schema.yaml && rg -n 'paused' contracts/ip.schema.yaml` | 生命周期枚举含 paused / archived |
| TC-IPM-004 | AC-IPM-002 | `rg -n 'content/ips/\{ip_id\}/assets/\{characters,scenes,props,styles\}/<asset_id>/' contracts/ip.schema.yaml` | IP 资产路径模式在契约中声明 |
| TC-IPM-005 | AC-IPM-002 | `rg -n 'asset_id' contracts/ip.schema.yaml && rg -n 'identity block' contracts/ip.schema.yaml` | 资产条目含 asset_id 与冻结 identity block 要求 |
| TC-IPM-006 | AC-IPM-003 | `for c in master-content storyworld campaign narrative-episode; do rg -q 'imports' contracts/$c.schema.yaml || exit 1; done` | 四个作品侧契约均含 imports 字段 |
| TC-IPM-007 | AC-IPM-003 | `rg -n 'track' contracts/ip.schema.yaml && rg -n 'latest' contracts/ip.schema.yaml` | import 支持 track 且声明 latest 缺省语义 |
| TC-IPM-008 | AC-IPM-004 | `rg -n 'resolved_revision' contracts/ip.schema.yaml scripts/check_ip_model.sh` | 解析结果记录 resolved_revision（跨契约与脚本） |
| TC-IPM-009 | AC-IPM-004 | `for rc in ip_not_found ip_unfrozen asset_missing revision_mismatch; do rg -q "$rc" scripts/check_ip_model.sh || exit 1; done` | 四类 fail-closed reason_code 均在解析校验中声明 |
| TC-IPM-010 | AC-IPM-004 | `! rg -n 'fallback.*redescrib\|静默.*本地重描述' scripts/check_ip_model.sh \|\| rg -n '禁止' scripts/check_ip_model.sh` | 禁止静默本地重描述在脚本中显式声明（负向语义） |
| TC-IPM-011 | AC-IPM-005 | `rg -n 'crossover_canon_unmet' scripts/check_ip_model.sh` | 多源联名聚合正典门 reason_code 存在 |
| TC-IPM-012 | AC-IPM-005 | `rg -n 'crossover' contracts/ip.schema.yaml scripts/check_ip_model.sh \| wc -l \| awk '{exit !($1>=1)}'` | 联名语义在契约或校验中体现 |
| TC-IPM-013 | AC-IPM-006 | `bash scripts/check_ip_model.sh --self-test 2>/dev/null; test $? -eq 0` | 校验脚本自检通过（exit 0） |
| TC-IPM-014 | AC-IPM-006 | `bash scripts/check_ip_model.sh --fixtures content/ips/_examples --expect pass; test $? -eq 0` | 对合规样例判定通过 |
| TC-IPM-015 | AC-IPM-006 | `bash scripts/check_ip_model.sh --fixtures content/ips/_examples --invert --expect fail; test $? -eq 1` | 反向断言：破坏引用时校验必须 fail（负向） |
| TC-IPM-016 | AC-IPM-007 | `export PRISM_HOME=$(pwd); bash scripts/check_prism_project_docs.sh --init-shape /tmp/prism-ipm-shape-x 2>/dev/null; rg -n 'ips' scripts/check_prism_project_docs.sh` | 同构校验纳入 ips/（脚本含 ips 处理） |
| TC-IPM-017 | AC-IPM-008 | `rg -n 'storyworlds\|masters' scripts/migrate_assets_to_ip.sh` | 迁移脚本覆盖 storyworld 与 masters 两个资产来源 |
| TC-IPM-018 | AC-IPM-008 | `bash scripts/migrate_assets_to_ip.sh --self-test 2>/dev/null; test $? -eq 0` | 迁移脚本幂等自检通过（exit 0） |
| TC-IPM-019 | AC-IPM-008 | `bash scripts/migrate_assets_to_ip.sh --dry-run --expect no-loss 2>/dev/null; test $? -eq 0` | 迁移 dry-run 断言不丢资产（清单计数一致） |
| TC-IPM-020 | GATES | `beacon truth review prism-ip-schema-v1 --project . --version v0.0.1 --json` | Truth Review Gate A/B/C + L0 pass，recommend_freeze=true |
| TC-IPM-021 | GATES | `beacon doctor verify-truth-integrity prism-ip-schema-v1 --project-root . --version v0.0.1 --mode block --json \| python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get('result',{}).get('blocked') in (False,None) and d.get('result',{}).get('closure_contract',{}).get('closure_allowed') else 1)"` | closure_allowed=true 且无 blocking finding（integrity 门真跑） |
| TC-IPM-022 | FSM | `rg -n 'archived → active without human_approved' docs/beacon/v0.0.1/features/prism-ip-schema-v1/truth.md` | 非法跃迁槽位：archived 复活须人工批准 |
| TC-IPM-023 | FSM | `rg -n 'import 引用 .draft. 或 .archived. 状态的 IP' docs/beacon/v0.0.1/features/prism-ip-schema-v1/truth.md` | 非法跃迁槽位：引用非 active IP 被禁止 |
| TC-IPM-024 | FSM | `rg -n '已钉 revision 的 import 在源 revision 变更后静默改引用' docs/beacon/v0.0.1/features/prism-ip-schema-v1/truth.md` | 非法跃迁槽位：静默改钉版引用被禁止 |

## Coverage 说明

- 每条 AC 至少一行行为级 TC（Command + Assertion），验证列均为可执行命令 + 可判定断言。
- TC-IPM-015 为负向断言（应失败的检查必须真的失败）。
- TC-IPM-016/017 依赖实现期新增的 `ips` 处理与迁移脚本，QA 阶段执行。
- `PRISM_HOME` 在执行环境未设置时取仓根：`export PRISM_HOME=$(pwd)`。
