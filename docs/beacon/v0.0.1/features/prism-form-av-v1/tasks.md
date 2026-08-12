---
slug: prism-form-av-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-form-av-v1

## Task Ledger

- [ ] TASK-001 Implement AC-AV-001: 进入 `forms_registered`：form-registry 登记 comic、vlog、book_video · ac=AC-AV-001 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-001.json`
- [ ] TASK-002 Implement AC-AV-002: 进入 `av_contract_landed`：`contracts/form-av.contract.md` 定义三形态 bridge ... · ac=AC-AV-002 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-002.json`
- [ ] TASK-003 Implement AC-AV-003: director handoff：契约要求 treatment / presentation map / shot list / stor... · ac=AC-AV-003 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-003.json`
- [ ] TASK-004 Implement AC-AV-004: 进入 `routing_landed`：creation-mode-map 的 vlog 行引用 form-av.contract，并新增... · ac=AC-AV-004 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-004.json`
- [ ] TASK-005 Implement AC-AV-005: 进入 `indexed`：`scripts/check_av_forms.sh` exec-layer 校验 PASS · ac=AC-AV-005 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-005.json`
- [ ] TASK-006 Implement AC-AV-006: license 注记：契约声明 AGPL-3.0 等 license 边界；默认 bridge；pin 需人工批准 + ATTRIBUTION · ac=AC-AV-006 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-006.json`
- [ ] TASK-007 Implement AC-AV-007: bridge fail-closed：工具缺失 → blocked + reason_code · ac=AC-AV-007 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-007.json`
- [ ] TASK-008 Implement AC-AV-008: QA 门：字幕/文字无乱码、版权安全、分镜/图序一致、anti-slop-gate 文案证据 · ac=AC-AV-008 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-008.json`
- [ ] TASK-009 Implement AC-AV-009: maker≠checker：form-av 契约与 QA 门分离 · ac=AC-AV-009 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-009.json`
- [ ] TASK-010 Implement AC-AV-010: Non-goals：D6、vendor_pin 全量、metrics、平台 API 显式排除；不得宣称海 closure · ac=AC-AV-010 · evidence=`.beacon/evidence/implement/prism-form-av-v1/AC-AV-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-form-av-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-form-av-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
