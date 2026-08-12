---
slug: prism-form-writing-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-form-writing-v1

## Task Ledger

- [ ] TASK-001 Implement AC-WRITE-001: 进入 `contract_landed`：`contracts/writing.contract.md` 存在，含七段契约 + 蒸馏写作规... · ac=AC-WRITE-001 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-001.json`
- [ ] TASK-002 Implement AC-WRITE-002: 进入 `gate_landed`：`skills/prism-qa/references/anti-slop-gate.md` 含 ≥10... · ac=AC-WRITE-002 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-002.json`
- [ ] TASK-003 Implement AC-WRITE-003: 进入 `registry_landed`：`registry/writing-adapters.yaml` 登记 ≥8 个 bridge（... · ac=AC-WRITE-003 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-003.json`
- [ ] TASK-004 Implement AC-WRITE-004: 进入 `routing_landed`：`skills/_internal/orchestration/creation-mode-map... · ac=AC-WRITE-004 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-004.json`
- [ ] TASK-005 Implement AC-WRITE-005: 进入 `indexed`：`scripts/check_writing_adapters.sh` exec-layer 校验 PASS（真... · ac=AC-WRITE-005 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-005.json`
- [ ] TASK-006 Implement AC-WRITE-006: adapter 不可见：`skills/_internal/adapters/` 与 `skills/prism-qa/reference... · ac=AC-WRITE-006 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-006.json`
- [ ] TASK-007 Implement AC-WRITE-007: bridge fail-closed 规则在 contract 中声明：缺工具 → blocked + reason_code，不产出假文件 · ac=AC-WRITE-007 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-007.json`
- [ ] TASK-008 Implement AC-WRITE-008: maker≠checker：writing.contract 与 anti-slop-gate 为独立文件，qa 侧含证据路径要求 · ac=AC-WRITE-008 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-008.json`
- [ ] TASK-009 Implement AC-WRITE-009: 硬边界在 anti-slop-gate 声明：不承诺必过机检；不编造经历/数据/截图；无素材用占位 · ac=AC-WRITE-009 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-009.json`
- [ ] TASK-010 Implement AC-WRITE-010: Non-goals：D2–D6 形态本体、vendor_pin、metrics、平台 API 全部显式排除；不得宣称海 closure · ac=AC-WRITE-010 · evidence=`.beacon/evidence/implement/prism-form-writing-v1/AC-WRITE-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-form-writing-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-form-writing-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
