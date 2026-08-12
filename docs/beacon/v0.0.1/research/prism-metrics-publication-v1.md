---
slug: prism-metrics-publication-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：开始 Lake E；E1 发布证据回流"
user_decision: promoted
---

# Research: prism-metrics-publication-v1

## 背景

Lake E = 指标/学习回流（DL-004 / INT-P15）。E1 先落发布证据回流，作为指标基座。

## 源/本仓证据

- Lake A FSM：`published → measured` 守卫 `publication_record_exists`
- Lake A FP-PRISM-006：指标是投影不是 canonical
- D6 `publish-bridge.contract.md`：draft_id/URL/人工批准
- `analyze-data`：多平台统计（wechat/xhs/douyin）

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 发布事件 | `contracts/metrics-publication.contract.md` | 结构化回流基座 |
| bridge | `registry/metrics-adapters.yaml` | 平台统计工具按名调用 |
| 凭证 | 受管 secrets | protected path |

## 明确不做（本子湖）

- E2–E4、平台 API 全量、编造指标、海 closure 宣称
