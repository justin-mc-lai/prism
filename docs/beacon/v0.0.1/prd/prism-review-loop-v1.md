---
slug: prism-review-loop-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md
---

# PRD — prism-review-loop-v1（Lake E3）

## 问题

有指标快照但无复盘闭环：谁复盘、引用什么数据、怎么写入圣经、哪些边界，缺文件级规范。

## 目标

`contracts/review-loop.contract.md`（review_id/campaign_id/period/metrics_refs/findings/actions +
人工批准 + 圣经边界）；`registry/review-adapters.yaml`（≥3）；系列圣经路由引用；exec 校验脚本。

## 边界

- 能做：复盘契约、登记、路由、校验。
- 不能做：E4；Lake F；自动改写母稿；自动公开。
