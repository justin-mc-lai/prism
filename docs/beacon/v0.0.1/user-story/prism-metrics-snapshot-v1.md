---
slug: prism-metrics-snapshot-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md
---

# User Stories — prism-metrics-snapshot-v1（Lake E2）

## US-MSNAP-001 指标快照

E1 发布事件存在 → 按 `metrics-snapshot.contract` 采集时间点指标 →
`content/publications/.../metrics/` 快照 → E3 复盘。

## US-MSNAP-002 无数据

无发布记录或平台无数据 → 显式空快照或 blocked，不猜。

## US-MSNAP-003 新指标源

只加 metrics-adapters 登记；凭证走受管 secrets。
