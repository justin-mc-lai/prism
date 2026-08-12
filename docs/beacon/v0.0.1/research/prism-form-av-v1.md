---
slug: prism-form-av-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：Lake D 逐个形态冻结实现；D5 AV"
user_decision: promoted
---

# Research: prism-form-av-v1

## 背景

D1–D4 完成写作/文本/图像/连载形态。D5 落地 AV 三形态（comic/vlog/book_video），bridge 优先。

## 源仓证据

- `openmontage`：AGPL-3.0，Remotion/FFmpeg 成片；bridge 优先
- `comic-storyboard`：3:4 竖版、文字可读性规则、ChatGPT 网页生成流程
- `book-video` / `rnskill`：书籍/剧集视频与合集
- creation-mode-map：已有 vlog 行；无 comic/book_video 行
- MAP-007：defer generators / bridge 已装工具；director handoff 字段蒸馏

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| AV 契约 | `contracts/form-av.contract.md` | 三形态路由 + 交接字段 + license |
| 策略 | bridge 优先 | 不复制 AGPL 大栈 |
| pin | 人工批准 + ATTRIBUTION | license 门 |
| QA | 乱码/版权/分镜/anti-slop | 与 maker 分离 |

## 明确不做（本子湖）

- D6、vendor_pin 全量、metrics、平台 API、海 closure 宣称
