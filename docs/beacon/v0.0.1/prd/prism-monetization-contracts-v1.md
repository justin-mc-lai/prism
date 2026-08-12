---
slug: prism-monetization-contracts-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md
---

# PRD — prism-monetization-contracts-v1（Lake F1）

## 问题

变现无契约：品牌合作/广告/付费/带货的条款、披露、合规与批准边界缺文件级规范。

## 目标

`contracts/monetization.contract.md`（deal 字段 + 人工批准 + 披露 + 合规门 + 敏感信息保护）；
`registry/monetization-adapters.yaml`（≥3）；路由引用；exec 校验脚本。

## 边界

- 能做：变现契约、登记、路由、校验。
- 不能做：F2 改编；平台支付 API；自动承诺合作；自动公开。
