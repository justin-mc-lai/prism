---
slug: prism-form-av-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md
---

# PRD — prism-form-av-v1（Lake D5）

## 问题

comic/vlog/book_video 没有生产者路由与交接契约：导演输出什么、桥接哪个工具、license 边界在哪，
都没有文件级规范；AV 大栈 vendor_pin 风险未收口。

## 目标

form-registry 注册 comic/vlog/book_video；`contracts/form-av.contract.md`（三形态 bridge 路由、
director handoff 字段、license 注记、QA 门、fail-closed）；creation-mode-map 路由；exec 校验脚本。

## 边界

- 能做：AV 路由契约、license 注记、QA 门、校验。
- 不能做：D6；vendor_pin 全量；metrics；平台 API；自动公开。
