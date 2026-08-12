---
slug: prism-metrics-publication-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-metrics-publication-v1

## Task Ledger

- [ ] TASK-001 Implement AC-MPUB-001: 进入 `contract_landed`：`contracts/metrics-publication.contract.md` 定义发布... · ac=AC-MPUB-001 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-001.json`
- [ ] TASK-002 Implement AC-MPUB-002: 进入 `registry_landed`：`registry/metrics-adapters.yaml` 登记 ≥3 个统计 bridg... · ac=AC-MPUB-002 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-002.json`
- [ ] TASK-003 Implement AC-MPUB-003: measured 守卫：契约声明无 publication 记录不得进入 measured（引用 Lake A FSM） · ac=AC-MPUB-003 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-003.json`
- [ ] TASK-004 Implement AC-MPUB-004: 进入 `routing_landed`：creation-mode-map 发布/回流引用 metrics-publication.con... · ac=AC-MPUB-004 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-004.json`
- [ ] TASK-005 Implement AC-MPUB-005: 进入 `indexed`：`scripts/check_metrics_publication.sh` exec-layer 校验 PASS · ac=AC-MPUB-005 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-005.json`
- [ ] TASK-006 Implement AC-MPUB-006: 不编造指标：契约声明缺数据用显式空快照，禁止猜测趋势 · ac=AC-MPUB-006 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-006.json`
- [ ] TASK-007 Implement AC-MPUB-007: 凭证保护：平台凭证/密钥禁止入库 · ac=AC-MPUB-007 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-007.json`
- [ ] TASK-008 Implement AC-MPUB-008: bridge fail-closed：统计工具缺失 → blocked + reason_code · ac=AC-MPUB-008 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-008.json`
- [ ] TASK-009 Implement AC-MPUB-009: 证据要求：事件必须带 publication_id/url/时间，缺证据不算回流 · ac=AC-MPUB-009 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-009.json`
- [ ] TASK-010 Implement AC-MPUB-010: Non-goals：E2–E4、平台 API 全量、vendor sync-ai 显式排除；不得宣称海 closure · ac=AC-MPUB-010 · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-metrics-publication-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
