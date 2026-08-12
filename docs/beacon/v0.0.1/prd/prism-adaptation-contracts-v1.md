---
slug: prism-adaptation-contracts-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md
---

# PRD — prism-adaptation-contracts-v1（Lake F2）

## 问题

资产改编无契约：授权范围、分成、license 边界、正典保护缺文件级规范。

## 目标

`contracts/adaptation.contract.md`（adaptation_id/asset_ref/rights/royalty/approval +
默认不授权 + 正典保护 + license 边界）；`registry/adaptation-adapters.yaml`（≥3）；路由引用；exec 校验脚本。

## 边界

- 能做：改编契约、登记、路由、校验。
- 不能做：平台授权 API；自动授权；自动公开。
