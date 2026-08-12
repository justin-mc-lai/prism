---
slug: prism-form-blog-thread-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：Lake D 逐个形态冻结实现；D2 blog/thread"
user_decision: promoted
---

# Research: prism-form-blog-thread-v1

## 背景

D1（prism-form-writing-v1）已交付写作/人话/反 slop 地基。D2 落地两个最轻文本形态：
blog 深度长文与 X thread。

## 源仓证据

- US-PRISM-001 blog 链：intel → master → director → produce(writing/humanize) → qa → release
- US-PRISM-005 thread 快道：goal → produce → qa → release，`fast_lane_skip` 标注
- selfmedia-writing：四段式/日榜倒金字塔/emotional-essay 选型
- creation-mode-map：blog/thread 行（已引 writing.contract / anti-slop-gate）
- FP-PRISM-007：新增形态只改 registry + form contract + 路由表

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| form 注册 | `registry/form-registry.yaml` | 机器可校验；与 registry 模式一致 |
| blog 契约 | `contracts/form-blog.contract.md` | 四段式；标准道 |
| thread 契约 | `contracts/form-thread.contract.md` | 倒金字塔；快道/标准道；canon 禁用快道 |
| 工具 | bridge writing-agent / selfmedia-writing | 不复制大运行时 |

## 明确不做（本子湖）

- D3–D6 形态、vendor_pin、metrics、平台 API、海 closure 宣称
