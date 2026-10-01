---
slug: prism-ip-import-gate-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-ip-import-gate-v1

## Task Ledger

- [ ] TASK-001 Implement AC-IPG-001: 新增 `crossovers` 内容对象：`registry/content-schema.yaml` 含 `schema_id: cro... · ac=AC-IPG-001 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-001.json`
- [ ] TASK-002 Implement AC-IPG-002: 当作品 `imports[]` 涉及的 `from` 去重后项数 ≥ 2 时，必须存在 `content/crossovers/{cros... · ac=AC-IPG-002 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-002.json`
- [ ] TASK-003 Implement AC-IPG-003: 联名记录须含非空 `disclosure_note`；缺失即 blocked，reason_code 为 `crossover_discl... · ac=AC-IPG-003 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-003.json`
- [ ] TASK-004 Implement AC-IPG-004: 联名记录声明分成时，`royalty_split` 各项占比合计等于 100%；当 `non_royalty` 显式声明为 true 时豁... · ac=AC-IPG-004 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-004.json`
- [ ] TASK-005 Implement AC-IPG-005: 联名须逐个校验参与 IP 正典冻结状态：`participant_ips` 中任一项不满足 `status=active` 且正典冻结，即... · ac=AC-IPG-005 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-005.json`
- [ ] TASK-006 Implement AC-IPG-006: 确定性校验脚本 `scripts/check_ip_import_gate.sh` 对给定作品与联名记录判定合规；违规时非零退出并打印对应... · ac=AC-IPG-006 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-006.json`
- [ ] TASK-007 Implement AC-IPG-007: 与 F1/F2 叠加：联名涉变现时，`contracts/monetization.contract.md` 披露门同时适用；涉改编时，`... · ac=AC-IPG-007 · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/AC-IPG-007.json`
- [ ] TASK-008 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/GATES.json`
- [ ] TASK-009 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-ip-import-gate-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
