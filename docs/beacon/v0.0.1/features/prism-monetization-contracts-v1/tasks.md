---
slug: prism-monetization-contracts-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-monetization-contracts-v1

## Task Ledger

- [ ] TASK-001 Implement AC-MON-001: 进入 `contract_landed`：`contracts/monetization.contract.md` 定义 deal_id/... · ac=AC-MON-001 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-001.json`
- [ ] TASK-002 Implement AC-MON-002: 进入 `registry_landed`：`registry/monetization-adapters.yaml` 登记 ≥3 个变现工... · ac=AC-MON-002 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-002.json`
- [ ] TASK-003 Implement AC-MON-003: 人工批准：变现承诺必须 human approval + evidence 才生效 · ac=AC-MON-003 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-003.json`
- [ ] TASK-004 Implement AC-MON-004: 进入 `routing_landed`：creation-mode-map 变现引用 monetization.contract · ac=AC-MON-004 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-004.json`
- [ ] TASK-005 Implement AC-MON-005: 进入 `indexed`：`scripts/check_monetization.sh` exec-layer 校验 PASS · ac=AC-MON-005 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-005.json`
- [ ] TASK-006 Implement AC-MON-006: 不编造收入/合作：缺证据 blocked · ac=AC-MON-006 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-006.json`
- [ ] TASK-007 Implement AC-MON-007: 披露义务：广告/赞助必须标注 · ac=AC-MON-007 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-007.json`
- [ ] TASK-008 Implement AC-MON-008: 风险合规门：health/legal/finance 未过合规不得变现 · ac=AC-MON-008 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-008.json`
- [ ] TASK-009 Implement AC-MON-009: 敏感信息保护：收款/合同信息受管，禁止入库 · ac=AC-MON-009 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-009.json`
- [ ] TASK-010 Implement AC-MON-010: Non-goals：改编契约、平台支付 API 显式排除；不得宣称海 closure · ac=AC-MON-010 · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-monetization-contracts-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
