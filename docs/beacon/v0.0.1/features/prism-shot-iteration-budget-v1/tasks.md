---
slug: prism-shot-iteration-budget-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-shot-iteration-budget-v1

## Task Ledger

- [ ] TASK-001 Implement AC-ITB-001: 分镜/镜头 schema 含 `iteration_budget`（每镜生成上限，正整数）与 `attempts`（实际尝试次数）；当 `... · ac=AC-ITB-001 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-001.json`
- [ ] TASK-002 Implement AC-ITB-002: 超预算的镜头必须附降级记录：`convergence` 取值限定在枚举 `simplified`（简化镜头）、`redesigned`（改... · ac=AC-ITB-002 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-002.json`
- [ ] TASK-003 Implement AC-ITB-003: 证据链中出现"对白由后期合成（TTS / 配音）产生"即 fail-closed，reason_code 为 `post_dub_fall... · ac=AC-ITB-003 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-003.json`
- [ ] TASK-004 Implement AC-ITB-004: `prompt-syntax` 判定新增：画面元素描述若使用否定式（形如 `no <元素>` 、`不要 <元素>` 描述画面内容）即 bl... · ac=AC-ITB-004 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-004.json`
- [ ] TASK-005 Implement AC-ITB-005: 能力域前置门：produce 前须声明目标 provider 与模型，并校验分镜动作与对白在该模型的 `reachable` 白名单内；动... · ac=AC-ITB-005 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-005.json`
- [ ] TASK-006 Implement AC-ITB-006: 确定性校验脚本 `scripts/check_shot_iteration_budget.sh` 可对给定 storyboard 与证据判... · ac=AC-ITB-006 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-006.json`
- [ ] TASK-007 Implement AC-ITB-007: 阈值来源义务：`iteration_budget`、`max_downgrades`、以及能力域 `reachable` 白名单必须标注来... · ac=AC-ITB-007 · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/AC-ITB-007.json`
- [ ] TASK-008 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/GATES.json`
- [ ] TASK-009 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-shot-iteration-budget-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
