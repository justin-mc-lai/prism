---
slug: prism-publish-bridge-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-publish-bridge-v1

## Task Ledger

- [ ] TASK-001 Implement AC-PUB-001: 进入 `contract_landed`：`contracts/publish-bridge.contract.md` 定义 bridge... · ac=AC-PUB-001 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-001.json`
- [ ] TASK-002 Implement AC-PUB-002: 进入 `registry_landed`：`registry/publish-adapters.yaml` 登记 ≥4 个 bridge（... · ac=AC-PUB-002 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-002.json`
- [ ] TASK-003 Implement AC-PUB-003: 草稿-only：契约声明只创建草稿/排期意图；公开必须人工二次批准 · ac=AC-PUB-003 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-003.json`
- [ ] TASK-004 Implement AC-PUB-004: 误路由守卫：误传目标 → superseded-misrouted + do_not_publish · ac=AC-PUB-004 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-004.json`
- [ ] TASK-005 Implement AC-PUB-005: 进入 `indexed`：`scripts/check_publish_bridge.sh` exec-layer 校验 PASS · ac=AC-PUB-005 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-005.json`
- [ ] TASK-006 Implement AC-PUB-006: 进入 `routing_landed`：creation-mode-map 引用 publish-bridge.contract · ac=AC-PUB-006 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-006.json`
- [ ] TASK-007 Implement AC-PUB-007: bridge fail-closed：工具缺失 → blocked + reason_code，不假装发布 · ac=AC-PUB-007 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-007.json`
- [ ] TASK-008 Implement AC-PUB-008: 凭证保护：契约声明平台凭证/密钥禁止入库（protected path） · ac=AC-PUB-008 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-008.json`
- [ ] TASK-009 Implement AC-PUB-009: 发布证据：draft_id/URL 必须记录；无证据不算已发布 · ac=AC-PUB-009 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-009.json`
- [ ] TASK-010 Implement AC-PUB-010: Non-goals：metrics、monetization、vendor sync-ai 显式排除；不得宣称海 closure · ac=AC-PUB-010 · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-publish-bridge-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
