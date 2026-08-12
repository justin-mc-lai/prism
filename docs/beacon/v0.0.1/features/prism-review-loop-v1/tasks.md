---
slug: prism-review-loop-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-review-loop-v1

## Task Ledger

- [ ] TASK-001 Implement AC-RVL-001: 进入 `contract_landed`：`contracts/review-loop.contract.md` 定义 review_id... · ac=AC-RVL-001 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-001.json`
- [ ] TASK-002 Implement AC-RVL-002: 进入 `registry_landed`：`registry/review-adapters.yaml` 登记 ≥3 个复盘工具 brid... · ac=AC-RVL-002 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-002.json`
- [ ] TASK-003 Implement AC-RVL-003: 人工批准：复盘结论/圣经更新必须人工确认后才写入 · ac=AC-RVL-003 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-003.json`
- [ ] TASK-004 Implement AC-RVL-004: 进入 `routing_landed`：creation-mode-map 系列圣经复盘段引用 review-loop.contract · ac=AC-RVL-004 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-004.json`
- [ ] TASK-005 Implement AC-RVL-005: 进入 `indexed`：`scripts/check_review_loop.sh` exec-layer 校验 PASS · ac=AC-RVL-005 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-005.json`
- [ ] TASK-006 Implement AC-RVL-006: 数据驱动：无 metrics_refs 的复盘 blocked，不空谈 · ac=AC-RVL-006 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-006.json`
- [ ] TASK-007 Implement AC-RVL-007: 圣经更新边界：只更新 bible 复盘段，不改已冻结母稿事实 · ac=AC-RVL-007 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-007.json`
- [ ] TASK-008 Implement AC-RVL-008: maker≠checker：复盘记录与 QA 分离，证据引用 · ac=AC-RVL-008 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-008.json`
- [ ] TASK-009 Implement AC-RVL-009: bridge fail-closed：工具缺失 → blocked + reason_code · ac=AC-RVL-009 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-009.json`
- [ ] TASK-010 Implement AC-RVL-010: Non-goals：E4、monetization 显式排除；不得宣称海 closure · ac=AC-RVL-010 · evidence=`.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-review-loop-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-review-loop-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
