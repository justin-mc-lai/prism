---
slug: prism-metrics-snapshot-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：开始 Lake E；E2 指标快照"
user_decision: promoted
---

# Research: prism-metrics-snapshot-v1

## 背景

E1 发布证据回流完成。E2 定义 MetricsSnapshot 指标快照契约。

## 源/本仓证据

- Lake A：MetricsSnapshot entity、FSM published→measured（publication_record_exists）
- E1 `metrics-publication.contract.md`：publication_id/url/时间
- `analyze-data`：views/interactions/followers 聚合

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 快照契约 | `contracts/metrics-snapshot.contract.md` | snapshot_id + publication_ref + collected_at |
| 空数据 | 显式空快照 | 不编造指标 |
| 凭证 | 受管 secrets | protected path |

## 明确不做（本子湖）

- E3/E4、平台 API 全量、编造指标、海 closure 宣称
