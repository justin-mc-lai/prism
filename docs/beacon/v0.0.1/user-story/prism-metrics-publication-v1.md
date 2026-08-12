---
slug: prism-metrics-publication-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md
---

# User Stories — prism-metrics-publication-v1（Lake E1）

## US-MPUB-001 发布事件回流

D6 发布桥创建草稿 → 人工二次批准 → 平台返回 URL/publication_id → 按
`metrics-publication.contract` 写入发布事件 → E2 才能采指标。

## US-MPUB-002 无记录拒绝

无 publication 记录时指标回流 blocked（publication_record_missing），不猜数据。

## US-MPUB-003 新平台接入

只加 metrics-adapters bridge 登记；凭证走受管 secrets。
