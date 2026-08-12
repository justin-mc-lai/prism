---
slug: prism-form-image-post-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-form-image-post-v1

## Task Ledger

- [ ] TASK-001 Implement AC-IMG-001: 进入 `forms_registered`：form-registry 登记 image-post 与 xhs，各含 contract 引... · ac=AC-IMG-001 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-001.json`
- [ ] TASK-002 Implement AC-IMG-002: 进入 `image_contract_landed`：`contracts/form-image-post.contract.md` 声明... · ac=AC-IMG-002 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-002.json`
- [ ] TASK-003 Implement AC-IMG-003: 进入 `xhs_contract_landed`：`contracts/form-xhs.contract.md` 声明 bridge x... · ac=AC-IMG-003 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-003.json`
- [ ] TASK-004 Implement AC-IMG-004: 进入 `routing_landed`：creation-mode-map 贴图包/xhs 行引用 form contracts · ac=AC-IMG-004 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-004.json`
- [ ] TASK-005 Implement AC-IMG-005: 进入 `indexed`：`scripts/check_image_post_forms.sh` exec-layer 校验 PASS · ac=AC-IMG-005 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-005.json`
- [ ] TASK-006 Implement AC-IMG-006: 账号硬编码清洗：契约声明账号/平台走配置，禁止 kushi-gzh 等硬编码进正文 · ac=AC-IMG-006 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-006.json`
- [ ] TASK-007 Implement AC-IMG-007: render bridge fail-closed：渲染脚本/xhs 工具缺失 → blocked + reason_code · ac=AC-IMG-007 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-007.json`
- [ ] TASK-008 Implement AC-IMG-008: OCR/QA 门：QA 检查无乱码/随机文字、图序、尺寸、caption/title 分离、价值门，证据可引用 · ac=AC-IMG-008 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-008.json`
- [ ] TASK-009 Implement AC-IMG-009: maker≠checker：form 契约与 anti-slop-gate/OCR 检查分离 · ac=AC-IMG-009 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-009.json`
- [ ] TASK-010 Implement AC-IMG-010: Non-goals：D4–D6、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure · ac=AC-IMG-010 · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-010.json`
- [ ] TASK-011 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/GATES.json`
- [ ] TASK-012 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-form-image-post-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
