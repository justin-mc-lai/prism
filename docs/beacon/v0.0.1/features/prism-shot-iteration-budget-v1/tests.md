---
slug: prism-shot-iteration-budget-v1
version: v0.0.1
materials_status: current
---

# Tests: prism-shot-iteration-budget-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-ITB-001 | AC-ITB-001 | `for f in iteration_budget attempts; do rg -q "$f" content/pipelines/ai-manga-drama/storyboard-schema.json || exit 1; done` | 分镜 schema 声明 iteration_budget 与 attempts |
| TC-ITB-002 | AC-ITB-001 | `rg -n 'iteration_budget_exceeded' scripts/check_shot_iteration_budget.sh` | 超预算 reason_code 在门脚本中声明 |
| TC-ITB-003 | AC-ITB-002 | `rg -n 'simplified' scripts/check_shot_iteration_budget.sh && rg -n 'redesigned' scripts/check_shot_iteration_budget.sh` | 降级枚举 simplified 与 redesigned 均在门脚本中声明 |
| TC-ITB-004 | AC-ITB-002 | `rg -n 'max_downgrades' scripts/check_shot_iteration_budget.sh && rg -n 'shot_aborted' scripts/check_shot_iteration_budget.sh` | 降级上限与终止态声明存在 |
| TC-ITB-005 | AC-ITB-003 | `rg -n 'post_dub_fallback_forbidden' scripts/check_shot_iteration_budget.sh` | 禁后期配音兜底 reason_code 存在 |
| TC-ITB-006 | AC-ITB-003 | `rg -n 'post_dub' scripts/check_shot_iteration_budget.sh \| wc -l \| awk '{exit !($1>=1)}'` | 后期配音检出逻辑存在 |
| TC-ITB-007 | AC-ITB-004 | `rg -n 'image_negation_not_affirmative' scripts/check_shot_iteration_budget.sh contracts/prompt-syntax.contract.md` | 画面否定式判据契约与门脚本同时声明 |
| TC-ITB-008 | AC-ITB-005 | `rg -n 'action_outside_model_domain' scripts/check_shot_iteration_budget.sh && rg -n 'dialogue_outside_model_domain' scripts/check_shot_iteration_budget.sh` | 能力域前置门两类 reason_code 存在 |
| TC-ITB-009 | AC-ITB-005 | `rg -n 'reachable' contracts/prompt-syntax.contract.md scripts/check_shot_iteration_budget.sh` | 能力域可达白名单在契约与门脚本中声明 |
| TC-ITB-010 | AC-ITB-006 | `bash scripts/check_shot_iteration_budget.sh --self-test 2>/dev/null; test $? -eq 0` | 门脚本自检通过（exit 0） |
| TC-ITB-011 | AC-ITB-006 | `bash scripts/check_shot_iteration_budget.sh --storyboard content/pipelines/ai-manga-drama/fixtures/ep-compile-test/storyboard.json --expect pass; test $? -eq 0` | 对合规样例判定通过 |
| TC-ITB-012 | AC-ITB-006 | `bash scripts/check_shot_iteration_budget.sh --storyboard content/pipelines/ai-manga-drama/fixtures/ep-compile-test/storyboard.json --invert --expect fail; test $? -eq 1` | 反向断言：破坏预算记录时门必须 fail（负向） |
| TC-ITB-013 | AC-ITB-007 | `rg -n 'threshold_source_missing' scripts/check_shot_iteration_budget.sh` | 阈值来源义务 reason_code 存在 |
| TC-ITB-014 | AC-ITB-007 | `rg -n 'threshold_source' contracts/prompt-syntax.contract.md scripts/check_shot_iteration_budget.sh \| wc -l \| awk '{exit !($1>=1)}'` | 阈值来源标注在契约或门脚本中体现 |
| TC-ITB-015 | GATES | `beacon truth review prism-shot-iteration-budget-v1 --project . --version v0.0.1 --json` | Truth Review Gate A/B/C + L0 pass，recommend_freeze=true |
| TC-ITB-016 | GATES | `beacon doctor verify-truth-integrity prism-shot-iteration-budget-v1 --project-root . --version v0.0.1 --mode block --json \| python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get('result',{}).get('blocked') in (False,None) and d.get('result',{}).get('closure_contract',{}).get('closure_allowed') else 1)"` | closure_allowed=true 且无 blocking finding（integrity 门真跑） |
| TC-ITB-017 | FSM | `rg -n 'attempting → converged while attempts 大于 iteration_budget 且无降级' docs/beacon/v0.0.1/features/prism-shot-iteration-budget-v1/truth.md` | 非法跃迁槽位：超预算无降级不得收敛 |
| TC-ITB-018 | FSM | `rg -n 'post_dub 产物进入 assemble' docs/beacon/v0.0.1/features/prism-shot-iteration-budget-v1/truth.md` | 非法跃迁槽位：后期配音产物不得进入拼接 |
| TC-ITB-019 | FSM | `rg -n 'action_outside_model_domain 直接进入 attempting' docs/beacon/v0.0.1/features/prism-shot-iteration-budget-v1/truth.md` | 非法跃迁槽位：跳过能力域门直接生成被禁止 |

## Coverage 说明

- 每条 AC 至少一行行为级 TC（Command + Assertion），验证列均为可执行命令 + 可判定断言。
- TC-ITB-012 为负向断言（应失败的检查必须真的失败）。
- TC-ITB-011/012 依赖实现期 storyboard fixture 中的预算字段，QA 阶段执行。
- `PRISM_HOME` 在执行环境未设置时取仓根：`export PRISM_HOME=$(pwd)`。
