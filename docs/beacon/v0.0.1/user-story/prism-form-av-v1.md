---
slug: prism-form-av-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md
---

# User Stories — prism-form-av-v1（Lake D5）

## US-AV-001 漫画

director 出分镜 + 角色/场景设定 → produce 按 `form-av.contract`（comic 路由）bridge
comic-storyboard（3:4 竖版、文字可读）→ QA（无乱码、分页一致）→ release。

## US-AV-002 vlog

director 出口播脚本/分镜 → bridge openmontage → 成片 QA → release。

## US-AV-003 book_video

bridge book-video 管线；license 未过时不 vendor_pin，只 bridge。
