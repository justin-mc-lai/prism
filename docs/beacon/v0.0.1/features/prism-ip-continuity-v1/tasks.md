---
slug: prism-ip-continuity-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-ip-continuity-v1

## Task Ledger

- [ ] TASK-001 Implement AC-IPC-001: IP 每次 `canon_revision` 跳变须有 `content/ips/{ip_id}/revisions/{R}.yaml`，... · ac=AC-IPC-001 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-001.json`
- [ ] TASK-002 Implement AC-IPC-002: 确定性脚本 `scripts/check_ip_continuity.sh view --ip {ip_id}` 输出该 IP 的版本链（... · ac=AC-IPC-002 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-002.json`
- [ ] TASK-003 Implement AC-IPC-003: 连续性审计：同一 IP 资产被多于一个作品引用、且各自 `resolved_revision` 不一致、且不存在对应演进记录时，报告 `c... · ac=AC-IPC-003 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-003.json`
- [ ] TASK-004 Implement AC-IPC-004: `content/ips/{ip_id}/seasons/{season_id}.yaml` 含 `season_id` 与 `campa... · ac=AC-IPC-004 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-004.json`
- [ ] TASK-005 Implement AC-IPC-005: season 复用现有 `campaign` 对象（一个 IP 对应多个 campaign），不新增 series 对象；`contrac... · ac=AC-IPC-005 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-005.json`
- [ ] TASK-006 Implement AC-IPC-006: 确定性脚本 `scripts/check_ip_continuity.sh` 校验演进链与 season；违规时非零退出并打印 reaso... · ac=AC-IPC-006 · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/AC-IPC-006.json`
- [ ] TASK-007 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/GATES.json`
- [ ] TASK-008 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-ip-continuity-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
