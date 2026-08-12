---
slug: prism-adaptation-contracts-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-adaptation-contracts-v1

## Task Ledger

- [ ] TASK-001 Implement AC-ADP-001: 进入 `contract_landed`：`contracts/adaptation.contract.md` 定义 adaptation... · ac=AC-ADP-001 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-001.json`
- [ ] TASK-002 Implement AC-ADP-002: 进入 `registry_landed`：`registry/adaptation-adapters.yaml` 登记 ≥3 个改编工具 ... · ac=AC-ADP-002 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-002.json`
- [ ] TASK-003 Implement AC-ADP-003: 人工批准：改编授权必须 approval + evidence；默认只登记不授权 · ac=AC-ADP-003 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-003.json`
- [ ] TASK-004 Implement AC-ADP-004: 进入 `routing_landed`：creation-mode-map 改编引用 adaptation.contract · ac=AC-ADP-004 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-004.json`
- [ ] TASK-005 Implement AC-ADP-005: 进入 `indexed`：`scripts/check_adaptation.sh` exec-layer 校验 PASS · ac=AC-ADP-005 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-005.json`
- [ ] TASK-006 Implement AC-ADP-006: 不编造授权/分成：缺证据 blocked · ac=AC-ADP-006 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-006.json`
- [ ] TASK-007 Implement AC-ADP-007: 正典保护：改编不得破坏母稿正典（引用 canon ledger） · ac=AC-ADP-007 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-007.json`
- [ ] TASK-008 Implement AC-ADP-008: license 边界：第三方 IP 未获权不自动授权 · ac=AC-ADP-008 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-008.json`
- [ ] TASK-009 Implement AC-ADP-009: 敏感信息保护：合同信息受管，禁止入库 · ac=AC-ADP-009 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-009.json`
- [ ] TASK-010 Implement AC-ADP-010: Non-goals：平台授权 API 显式排除；不得宣称海 closure · ac=AC-ADP-010 · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-adaptation-contracts-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
