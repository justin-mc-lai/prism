---
slug: prism-metrics-snapshot-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md
---

# PRD — prism-metrics-snapshot-v1（Lake E2）

## 问题

有发布证据但无指标快照契约：采集什么字段、绑定哪个发布、什么时间、证据在哪，没有文件级规范。

## 目标

`contracts/metrics-snapshot.contract.md`（snapshot_id/publication_ref/指标字段/collected_at/来源 +
measured 守卫 + 空快照 + 凭证保护）；registry 快照条目；路由引用；exec 校验脚本。

## 边界

- 能做：快照契约、登记、路由、校验。
- 不能做：E3/E4；平台 API 全量；编造指标。
