---
slug: prism-review-loop-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md
---

# User Stories — prism-review-loop-v1（Lake E3）

## US-RVL-001 战役复盘

周期结束 → 收集 E1/E2 数据 → 按 `review-loop.contract` 生成复盘 → 人工批准 →
写回系列圣经复盘段 → goal 复盘 loop 关闭。

## US-RVL-002 无数据被拒

缺 metrics_refs → blocked，不空谈。

## US-RVL-003 圣经边界

复盘只写 bible 复盘段；母稿事实/正典不动。
