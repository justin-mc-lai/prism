---
slug: prism-publish-bridge-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md
---

# PRD — prism-publish-bridge-v1（Lake D6）

## 问题

D1–D5 产出没有统一的发布边界：谁建草稿、谁可公开、凭证怎么保护、误路由怎么处理，缺文件级契约。

## 目标

`contracts/publish-bridge.contract.md`（bridge 路由 + 草稿-only + 人工二次批准 + 误路由守卫 +
证据记录 + 凭证保护）；`registry/publish-adapters.yaml`（≥4 bridge）；路由引用；exec 校验脚本。

## 边界

- 能做：发布桥契约、登记、路由、校验。
- 不能做：metrics（E）、monetization（F）、vendor sync-ai、自动公开。
