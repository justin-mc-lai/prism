---
slug: prism-form-image-post-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md
---

# PRD — prism-form-image-post-v1（Lake D3）

## 问题

贴图包与小红书图文没有生产者契约：title/caption/图片/封面混用、张数无上限、封面文字靠模型、
渲染工具与账号配置没有 fail-closed 规则。

## 目标

`form-image-post.contract.md`（四分离 + 1–9 张 + 本地排版封面 + OCR/QA 门）、
`form-xhs.contract.md`（bridge + OCR 门）、form-registry 注册、路由引用与 exec 校验脚本。

## 边界

- 能做：两个图像形态契约、注册、路由、校验。
- 不能做：D4–D6；vendor_pin；metrics；平台 API；自动公开。
