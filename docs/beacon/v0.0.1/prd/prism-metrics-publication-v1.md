---
slug: prism-metrics-publication-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md
---

# PRD — prism-metrics-publication-v1（Lake E1）

## 问题

发布后没有结构化发布事件，指标无基座；FSM `published → measured` 守卫没有契约支撑。

## 目标

`contracts/metrics-publication.contract.md`（发布事件字段 + measured 守卫 + 不编造 + 凭证保护 +
证据要求）；`registry/metrics-adapters.yaml`（≥3 bridge）；路由回流引用；exec 校验脚本。

## 边界

- 能做：发布事件契约、登记、路由、校验。
- 不能做：E2–E4；平台 API 全量；编造指标；自动公开。
