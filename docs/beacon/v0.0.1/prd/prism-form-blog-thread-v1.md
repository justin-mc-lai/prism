---
slug: prism-form-blog-thread-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md
---

# PRD — prism-form-blog-thread-v1（Lake D2）

## 问题

D1 有了写作地基，但没有具体形态的生产者契约：blog 长文与 X thread 谁写、按什么结构、
走什么道（标准/快道）、产出与证据落在哪里，都没有文件级规范。

## 目标

`registry/form-registry.yaml` 注册 blog/thread；`contracts/form-blog.contract.md` 与
`contracts/form-thread.contract.md` 定义输入/结构/输出/证据/fail-closed；creation-mode-map
路由引用；`scripts/check_blog_thread_forms.sh` exec 校验。

## 边界

- 能做：form 注册、两个生产者契约、路由、校验脚本。
- 不能做：D3–D6 形态；vendor_pin；metrics；平台 API；自动公开发布。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；freeze → implement → QA → release 人工门。
