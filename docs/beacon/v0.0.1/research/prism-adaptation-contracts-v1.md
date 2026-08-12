---
slug: prism-adaptation-contracts-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：开始 Lake F；F2 改编契约"
user_decision: promoted
---

# Research: prism-adaptation-contracts-v1

## 背景

Lake F 收口：改编授权契约。F1 变现契约已完成。

## 源/本仓证据

- Lake A：INT-P16 / DL-005 改编合同
- Lake C/D4：StoryWorld/canon ledger（改编不得破坏正典）
- F1 `monetization.contract.md`：人工批准/敏感信息模式复用

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 改编契约 | `contracts/adaptation.contract.md` | adaptation_id + rights + royalty + approval |
| 默认 | 只登记不授权 | 人工批准硬门 |
| bridge | `registry/adaptation-adapters.yaml` | rights-record / royalty-calc / license-check |

## 明确不做（本子湖）

- 平台授权 API、自动授权、自动公开、海 closure 宣称
