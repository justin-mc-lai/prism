---
slug: prism-form-novel-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：Lake D 逐个形态冻结实现；D4 novel"
user_decision: promoted
---

# Research: prism-form-novel-v1

## 背景

D1–D3 完成写作地基、文本形态与图像形态。D4 落地 novel 连载，接入 Lake C 的 canon 门。

## 源仓/本仓证据

- Lake A：FP-PRISM-003（正典即 truth、OOC fail-closed）、US-PRISM-002（连载旅程）
- Lake C：`contracts/narrative-episode.schema.yaml`（canon_gate_status）、storyworld 路径
- `kushi-narrative-zh`：MASTER → humanized 长文本叙事桥
- creation-mode-map：现有行无 novel；需新增

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| novel 契约 | `contracts/form-novel.contract.md` | episode 结构 + canon 门 |
| 输出 | `content/storyworlds/{world}/episodes/` | 与 Lake C schema 对齐 |
| 正典门 | `canon_gate_status=passed` 才可 generated | AC-PRISM-009 |
| 叙事桥 | kushi-narrative-zh | bridge，不复制 |

## 明确不做（本子湖）

- D5/D6、vendor_pin、metrics、平台 API、海 closure 宣称
