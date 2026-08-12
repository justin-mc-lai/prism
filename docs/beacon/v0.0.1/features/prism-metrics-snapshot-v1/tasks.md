---
slug: prism-metrics-snapshot-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-metrics-snapshot-v1

## Task Ledger

- [ ] TASK-001 Implement AC-MSNAP-001: 进入 `contract_landed`：`contracts/metrics-snapshot.contract.md` 定义 snap... · ac=AC-MSNAP-001 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-001.json`
- [ ] TASK-002 Implement AC-MSNAP-002: 进入 `registry_landed`：`registry/metrics-adapters.yaml` 含 ≥2 个快照采集 brid... · ac=AC-MSNAP-002 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-002.json`
- [ ] TASK-003 Implement AC-MSNAP-003: measured 守卫：无 publication_ref 不得生成快照（引用 E1 发布事件） · ac=AC-MSNAP-003 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-003.json`
- [ ] TASK-004 Implement AC-MSNAP-004: 进入 `routing_landed`：creation-mode-map 快照/measured 引用 metrics-snapshot... · ac=AC-MSNAP-004 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-004.json`
- [ ] TASK-005 Implement AC-MSNAP-005: 进入 `indexed`：`scripts/check_metrics_snapshot.sh` exec-layer 校验 PASS · ac=AC-MSNAP-005 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-005.json`
- [ ] TASK-006 Implement AC-MSNAP-006: 空快照/不编造：缺数据用显式空快照，禁止猜测 · ac=AC-MSNAP-006 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-006.json`
- [ ] TASK-007 Implement AC-MSNAP-007: 凭证保护：平台凭证/密钥禁止入库 · ac=AC-MSNAP-007 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-007.json`
- [ ] TASK-008 Implement AC-MSNAP-008: bridge fail-closed：统计工具缺失 → blocked + reason_code · ac=AC-MSNAP-008 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-008.json`
- [ ] TASK-009 Implement AC-MSNAP-009: 证据要求：快照必须带 collected_at 与来源，缺证据不算采集 · ac=AC-MSNAP-009 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-009.json`
- [ ] TASK-010 Implement AC-MSNAP-010: Non-goals：E3/E4、平台 API 全量显式排除；不得宣称海 closure · ac=AC-MSNAP-010 · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-metrics-snapshot-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
