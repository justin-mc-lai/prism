---
slug: prism-form-blog-thread-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-form-blog-thread-v1

## Task Ledger

- [ ] TASK-001 Implement AC-FORM-001: 进入 `forms_registered`：`registry/form-registry.yaml` 登记 blog 与 thread，... · ac=AC-FORM-001 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-001.json`
- [ ] TASK-002 Implement AC-FORM-002: 进入 `blog_contract_landed`：`contracts/form-blog.contract.md` 定义输入（冻结母稿... · ac=AC-FORM-002 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-002.json`
- [ ] TASK-003 Implement AC-FORM-003: 进入 `thread_contract_landed`：`contracts/form-thread.contract.md` 定义倒金字... · ac=AC-FORM-003 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-003.json`
- [ ] TASK-004 Implement AC-FORM-004: 进入 `routing_landed`：creation-mode-map 的 blog/thread 行引用 form-blog.con... · ac=AC-FORM-004 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-004.json`
- [ ] TASK-005 Implement AC-FORM-005: 进入 `indexed`：`scripts/check_blog_thread_forms.sh` exec-layer 校验 PASS · ac=AC-FORM-005 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-005.json`
- [ ] TASK-006 Implement AC-FORM-006: 形态扩展规则声明：新增形态只改 registry + form contract + 路由表，不改主链 · ac=AC-FORM-006 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-006.json`
- [ ] TASK-007 Implement AC-FORM-007: 快道门禁：thread 契约声明 lane=canon 禁用 fast_lane_skip；快道必须显式标注 · ac=AC-FORM-007 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-007.json`
- [ ] TASK-008 Implement AC-FORM-008: bridge fail-closed：writing-agent 等缺失 → blocked + reason_code，不产出假文件 · ac=AC-FORM-008 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-008.json`
- [ ] TASK-009 Implement AC-FORM-009: maker≠checker：form 契约与 anti-slop-gate 分离；QA 证据引用原文行 · ac=AC-FORM-009 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-009.json`
- [ ] TASK-010 Implement AC-FORM-010: Non-goals：D3–D6 形态、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure · ac=AC-FORM-010 · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-form-blog-thread-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
