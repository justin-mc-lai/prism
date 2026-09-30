---
slug: prism-ip-schema-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-ip-schema-v1

## Task Ledger

- [ ] TASK-001 Implement AC-IPM-001: 注册 `ip` 内容对象：`registry/content-schema.yaml` 含 `schema_id: ip`，`root: ... · ac=AC-IPM-001 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-001.json`
- [ ] TASK-002 Implement AC-IPM-002: IP 资产条目位于 `content/ips/{ip_id}/assets/{characters,scenes,props,styles... · ac=AC-IPM-002 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-002.json`
- [ ] TASK-003 Implement AC-IPM-003: 作品侧契约（`master-content`、`storyworld`、`campaign`、`narrative-episode`）各含... · ac=AC-IPM-003 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-003.json`
- [ ] TASK-004 Implement AC-IPM-004: import 解析逐字注入源 IP 冻结 identity block；`track: latest` 解析时将源 IP 当时的 `can... · ac=AC-IPM-004 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-004.json`
- [ ] TASK-005 Implement AC-IPM-005: 当一个作品的 `imports[]` 指向两个及以上 IP 时，要求全部被引用 IP 的 `status=active` 且正典已冻结；任... · ac=AC-IPM-005 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-005.json`
- [ ] TASK-006 Implement AC-IPM-006: 校验脚本 `scripts/check_ip_model.sh` 可验证：IP 已注册；`ip.yaml` 必填字段齐全；`imports... · ac=AC-IPM-006 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-006.json`
- [ ] TASK-007 Implement AC-IPM-007: `check_prism_project_docs.sh --init-shape` 对 `docs/prism` 的同构断言包含 `ip... · ac=AC-IPM-007 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-007.json`
- [ ] TASK-008 Implement AC-IPM-008: scenes · ac=AC-IPM-008 · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/AC-IPM-008.json`
- [ ] TASK-009 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/GATES.json`
- [ ] TASK-010 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-ip-schema-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
