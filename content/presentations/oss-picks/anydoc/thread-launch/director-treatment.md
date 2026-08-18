# Director Treatment — anydoc thread（X 短链观点帖）

- mode_id: treatment-director
- public_id: director
- lane: standard
- recommended_next_harness: produce
- map_ids_considered: ['MAP-002']
- master_ref: content/masters/oss-picks/anydoc/MASTER.md

## Core Intent

- one_sentence_intent: 让写工具稿/喂 AI 的人知道：办公文档转 Markdown 已经可以一条命令搞定，且浏览器本地转、不上传。
- audience: 经常处理 Word/PDF、想把文档喂给 AI 或编辑器的内容创作者与开发者。
- audience_promise: 30 秒看完，知道三个入口选哪个，且能自己跑通第一条命令。
- primary_action_after_viewing: 拿一份手边文档跑 `npx @firecrawl/anydoc`。

## Logline

被文档格式折磨的人，遇到一个九天涨到约 1.5 万星的 Rust 小工具（08-03 创建，08-12 检索）：办公格式进、干净 Markdown 出，浏览器本地转不传文件。

## Conflict

- surface_conflict: 复制粘贴毁格式 vs 一条命令保结构。
- deeper_conflict: “方便”与“隐私”的取舍——CLI 联网 vs WASM 本地。
- stakes_if_ignored: 继续手动整理，一份文档二十分钟。

## Narrative World

- viewpoint: 第一人称工具使用者视角。
- tone: 直接、有态度、不吹。
- forbidden_drift: 不写成官方宣传稿；不把官方速度声明当实测。

## Emotional Curve

| Stage | Audience state | Story beat |
|---|---|---|
| Entry | 痛点共鸣 | 复制粘贴毁格式 |
| Turn | 好奇 | 9 天 1.5 万星的新工具 |
| Proof | 信服 | 一条命令 + 三入口 + WASM 不上传 |
| Release | 行动 | 拿手边文档试一次 |

## Evidence And Claims

| Claim | Evidence/source | Notes |
|---|---|---|
| 9 天涨到约 1.5 万星（08-03 创建 → 08-12 检索） | MASTER claim 4 | 标注检索时刻与日期推算 |
| 支持 8 种格式 | MASTER claim 1 | 不超卖 |
| 单数字毫秒为官方声明 | MASTER claim 6 | 必须标注 |
| WASM 本地转换不上传 | MASTER claim 7 | 关键卖点 |

## Non-Goals

- not_for: 评测对比、安装排错教程、扫描 PDF OCR 方案。
- do_not_say: “性能第一”“革命性”。
- do_not_show: 未验证的速度数字。

## Next Gate

- gate: treatment-approval（样本自审通过，QC 自评 56/65）
- if_approved_next: produce thread 成稿
