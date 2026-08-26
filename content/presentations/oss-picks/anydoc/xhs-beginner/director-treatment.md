# Director Treatment — anydoc xhs（小红书图文）

- mode_id: treatment-director
- public_id: director
- lane: standard
- recommended_next_harness: produce
- map_ids_considered: ['MAP-002']
- master_ref: content/masters/oss-picks/anydoc/MASTER.md

## Core Intent

- one_sentence_intent: 让被文档格式折磨的职场/内容人知道：办公文档转干净 Markdown 一条命令搞定，浏览器本地转不上传。
- audience: 经常处理 Word/PDF、要给 AI 喂文档的普通用户（非程序员也跟得上）。
- audience_promise: 30 秒读懂是什么，收藏后能照着命令试一次。
- primary_action_after_viewing: 收藏并拿手边文档跑一次 `npx @firecrawl/anydoc`。

## Logline

复制粘贴毁格式的日常，被一个九天涨到 1.5 万星的开源小工具终结，而且敏感文件可以在浏览器本地转。

## Conflict

- surface_conflict: 手动整理一份文档二十分钟 vs 一条命令出干净 Markdown。
- deeper_conflict: 工具方便但「要不要把文件传上去」的隐私顾虑。
- stakes_if_ignored: 继续忍受乱码表格，AI 也读不懂。

## Narrative World

- viewpoint: 第一人称使用者视角。
- tone: 种草但不夸张；有态度、有边界。
- forbidden_drift: 不承诺必过检测；不把官方速度声明当实测。

## Emotional Curve

| Stage | Audience state | Story beat |
|---|---|---|
| Entry | 痛点共鸣 | 复制粘贴毁格式 |
| Turn | 好奇 | 9 天 1.5 万星 |
| Proof | 信服 | 一条命令 + WASM 本地转 |
| Release | 行动 | 收藏 + 试一次 |

## Evidence And Claims

| Claim | Evidence/source | Notes |
|---|---|---|
| 9 天涨到约 1.5 万星 | MASTER claim 4 | 日期推算，标注快照 |
| 8 种格式 + GFM 输出 | claim 1–2 | 不超卖 |
| Node/Python/WASM 三入口 | claim 3, 11–13 | |
| WASM 本地转换不上传 | claim 7 | 隐私重点 |
| OCR 边界 | claim 8 | 诚实边界 |

## Presentation Variants

| Variant | Form | 说明 |
|---|---|---|
| 正文 | 种草图文 | 首图 + 4 内容卡（标题/正文兑现） |
| 封面卡 | 标题大字 | 【图片占位】待 enrich |

## Non-Goals

- not_for: 安装排错、扫描 PDF 方案、与竞品对比。
- do_not_say: 「人手必备」「效率神器」式空口号。
- do_not_show: 未验证的速度数字。

## Next Gate

- gate: treatment-approval（样本自审通过，QC 自评 55/65）
- if_approved_next: produce xhs 成稿（文案 + 配图文案 + manifest）
