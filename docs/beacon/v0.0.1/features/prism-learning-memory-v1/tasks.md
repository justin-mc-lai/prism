---
slug: prism-learning-memory-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-learning-memory-v1

## Task Ledger

- [ ] TASK-001 Implement AC-LMEM-001: 进入 `contract_landed`：`contracts/learning-memory.contract.md` 定义 memor... · ac=AC-LMEM-001 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-001.json`
- [ ] TASK-002 Implement AC-LMEM-002: 进入 `registry_landed`：`registry/learning-adapters.yaml` 登记 ≥3 个学习工具 br... · ac=AC-LMEM-002 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-002.json`
- [ ] TASK-003 Implement AC-LMEM-003: advisory-only：契约声明 learning 不定义 truth、不通 gate、不给 QA/release verdict · ac=AC-LMEM-003 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-003.json`
- [ ] TASK-004 Implement AC-LMEM-004: 进入 `routing_landed`：creation-mode-map 学习引用 learning-memory.contract · ac=AC-LMEM-004 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-004.json`
- [ ] TASK-005 Implement AC-LMEM-005: 进入 `indexed`：`scripts/check_learning_memory.sh` exec-layer 校验 PASS · ac=AC-LMEM-005 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-005.json`
- [ ] TASK-006 Implement AC-LMEM-006: 可回放/可审计：每条记忆带 source_ref + 时间 + 回放路径 · ac=AC-LMEM-006 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-006.json`
- [ ] TASK-007 Implement AC-LMEM-007: 可裁剪：冲突/过时记忆显式标记，prune 保留审计痕迹 · ac=AC-LMEM-007 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-007.json`
- [ ] TASK-008 Implement AC-LMEM-008: 边界：learning 不替代 QA/release 判定 · ac=AC-LMEM-008 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-008.json`
- [ ] TASK-009 Implement AC-LMEM-009: bridge fail-closed：工具缺失 → blocked + reason_code · ac=AC-LMEM-009 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-009.json`
- [ ] TASK-010 Implement AC-LMEM-010: Non-goals：Lake F、平台 API 显式排除；不得宣称海 closure · ac=AC-LMEM-010 · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-learning-memory-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
