---
slug: prism-publish-bridge-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：Lake D 逐个形态冻结实现；D6 publish bridge"
user_decision: promoted
---

# Research: prism-publish-bridge-v1

## 背景

D1–D5 完成八形态生产链。D6 收口发布/排期桥：草稿-only、人工二次批准、凭证保护、误路由守卫。

## 源仓证据

- `publish-content`：平台路由表（wechat/juejin/zhihu/toutiao/douyin/x）
- `schedule-post`：日历/批量排期
- `x-publish` / `manage-media`：X 发布与媒体管理
- MAP-008：bridge 草稿工具；vendor sync-ai 延后；人工批准始终
- Lake A FP-PRISM-005：公开发布必须人工批准

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 发布契约 | `contracts/publish-bridge.contract.md` | 草稿边界 + 人工门 + 证据 |
| 登记 | `registry/publish-adapters.yaml` | 机器可校验 |
| 凭证 | 禁止入库 | protected path |
| sync-ai | 不吞 | 跨仓延后 |

## 明确不做（本子湖）

- metrics（E）、monetization（F）、vendor sync-ai、自动公开、海 closure 宣称
