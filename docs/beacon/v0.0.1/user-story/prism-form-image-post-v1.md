---
slug: prism-form-image-post-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md
---

# User Stories — prism-form-image-post-v1（Lake D3）

## US-IMG-001 贴图包

director 出 shot list → produce 按 `form-image-post.contract` 生成 1–9 张图 + caption + 本地排版封面
→ QA（OCR/图序/尺寸/图文分离）→ release 创建草稿（不自动公开）。

## US-IMG-002 小红书图文

produce 按 `form-xhs.contract` bridge xhs-article-to-images → OCR 门 → release；工具缺失 blocked。

## US-IMG-003 新账号接入

只改账号配置/registry；禁止账号硬编码进契约。
