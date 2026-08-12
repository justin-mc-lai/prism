---
slug: prism-form-writing-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：做 Lake D，先 pln-program 拆八形态，再逐个冻结实现"
user_decision: promoted
---

# Research: prism-form-writing-v1

## 背景

Lake D = 八形态生产链（海承诺主体）。pln-program 已产出 `programs/prism-canon/lake-d-plan.md`：
先做 D1 写作/人话/反 slop 地基（MAP-005 distill+bridge），再 D2 blog/thread → D3 贴图/xhs →
D4 novel → D5 comic/vlog/book_video → D6 publish bridge。

## 源仓证据

- `selfmedia-writing`：四段式（🎯🗺️💎⚠️）、日榜倒金字塔、emotional-essay、文笔五原则
- `selfmedia-humanize`：人味五手法（句式交错/口语转折/细节/情感起伏/反模板）、硬边界
- `humanizer-zh`：五原则（删填充/破公式/变节奏/信读者/删金句）
- `no-ai-slop`：16+ 可引用 slop 模式（二元对比/清嗓/伪洞察/weasel 归因/假深刻结尾等）
- adapter-index MAP-005：writing/humanize → prism-produce/prism-qa，distill+bridge

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 规则权威 | `contracts/writing.contract.md` | 与 Lake C 契约模式一致 |
| QA 门 | `skills/prism-qa/references/anti-slop-gate.md` | maker≠checker 分离 |
| bridge 登记 | `registry/writing-adapters.yaml` | 与 registry 模式一致；机器可校验 |
| 策略 | distill 判据 + bridge 工具 | 不 vendor_pin、不外包判断 |

## 明确不做（本子湖）

- D2–D6 形态本体
- vendor_pin 外部大栈
- metrics（Lake E）/ monetization（Lake F）
- 平台发布 API
- 海 closure 宣称
