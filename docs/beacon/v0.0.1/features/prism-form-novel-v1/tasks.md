---
slug: prism-form-novel-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-form-novel-v1

## Task Ledger

- [ ] TASK-001 Implement AC-NVL-001: 进入 `forms_registered`：form-registry 登记 novel，含 contract 引用与生产链 · ac=AC-NVL-001 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-001.json`
- [ ] TASK-002 Implement AC-NVL-002: 进入 `novel_contract_landed`：`contracts/form-novel.contract.md` 定义 Stor... · ac=AC-NVL-002 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-002.json`
- [ ] TASK-003 Implement AC-NVL-003: failed` 不得进入 generated；canon 禁用 fast_lane_skip · ac=AC-NVL-003 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-003.json`
- [ ] TASK-004 Implement AC-NVL-004: 进入 `routing_landed`：creation-mode-map 新增 novel 行，引用 form-novel.contra... · ac=AC-NVL-004 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-004.json`
- [ ] TASK-005 Implement AC-NVL-005: 进入 `indexed`：`scripts/check_novel_form.sh` exec-layer 校验 PASS · ac=AC-NVL-005 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-005.json`
- [ ] TASK-006 Implement AC-NVL-006: bridge fail-closed：kushi-narrative-zh 缺失 → blocked + reason_code · ac=AC-NVL-006 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-006.json`
- [ ] TASK-007 Implement AC-NVL-007: StoryWorld 引用：契约引用 `content/storyworlds/{world_slug}/`（bible/canon-le... · ac=AC-NVL-007 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-007.json`
- [ ] TASK-008 Implement AC-NVL-008: maker≠checker：novel 契约与 anti-slop-gate/正典 QA 分离，证据可引用 · ac=AC-NVL-008 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-008.json`
- [ ] TASK-009 Implement AC-NVL-009: OOC/连续性门：契约声明设定漂移/OOC 按事实错误 fail-closed · ac=AC-NVL-009 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-009.json`
- [ ] TASK-010 Implement AC-NVL-010: Non-goals：D5/D6、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure · ac=AC-NVL-010 · evidence=`.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-form-novel-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-form-novel-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
