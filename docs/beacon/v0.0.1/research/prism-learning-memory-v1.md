---
slug: prism-learning-memory-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：开始 Lake E；E4 学习记忆"
user_decision: promoted
---

# Research: prism-learning-memory-v1

## 背景

E1–E3 完成发布证据、指标快照、复盘。E4 收口：可回放学习记忆。

## 源/本仓证据

- Beacon 学习边界：可回放、可审计、可裁剪；learning 不定义 truth/gate
- E3 `review-loop.contract.md`：复盘发现可作为学习来源

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 学习契约 | `contracts/learning-memory.contract.md` | memory_id + source_ref + confidence + applicability |
| 边界 | advisory only | 不写 truth、不给 verdict |
| bridge | `registry/learning-adapters.yaml` | memory-store / recall / prune |

## 明确不做（本子湖）

- Lake F、平台 API、learning 写入 truth、海 closure 宣称
