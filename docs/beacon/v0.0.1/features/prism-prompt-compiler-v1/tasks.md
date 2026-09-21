---
slug: prism-prompt-compiler-v1
version: v0.0.1
materials_status: current
task_source: acceptance_criteria
---

# Tasks: prism-prompt-compiler-v1

## Task Ledger

- [x] TASK-001 Implement AC-PPC-001: 蒸馏 `script-templates.md`（完整剧本 + 分镜表 + 镜头清单） · ac=AC-PPC-001 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-001.json`
- [x] TASK-002 Implement AC-PPC-002: `scripts/prompt_compiler.py` 确定性编译器 · ac=AC-PPC-002 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-002.json`
- [x] TASK-003 Implement AC-PPC-003: schema + CLI `ref_image` 字段与校验 · ac=AC-PPC-003 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-003.json`
- [x] TASK-004 Implement AC-PPC-004: `contracts/asset-render.contract.md` + `registry/render-adapters.yaml` · ac=AC-PPC-004 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-004.json`
- [x] TASK-005 Implement AC-PPC-005: CLI 去兜底（删 kenburns/edge-tts；assemble 只拼真实片段） · ac=AC-PPC-005 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-005.json`
- [x] TASK-006 Implement AC-PPC-006: 契约与路由同步（manga 契约/registry/README/creation-mode-map） · ac=AC-PPC-006 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-006.json`
- [x] TASK-007 Implement AC-PPC-007: 新增 exec 门禁 + 既有门禁零回归 · ac=AC-PPC-007 · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-007.json`
- [x] TASK-008 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/GATES.json`
- [x] TASK-009 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/prism-prompt-compiler-v1/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
