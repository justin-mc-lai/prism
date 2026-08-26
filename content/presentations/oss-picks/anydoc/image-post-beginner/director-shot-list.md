# Director Shot List — anydoc 贴图包（公众号 image-post）

- mode_id: treatment-director
- public_id: director
- lane: standard
- recommended_next_harness: produce
- map_ids_considered: ['MAP-002', 'MAP-006']
- master_ref: content/masters/oss-picks/anydoc/MASTER.md

## Core Intent

- one_sentence_intent: 6 张图讲完「文档转 Markdown 一条命令 + 三入口 + 隐私重点」，收藏即可照着用。
- audience: 被文档格式折磨的内容人/职场人，不假设会写代码。
- audience_promise: 看图就能判断「我该用哪个入口」。
- primary_action_after_viewing: 收藏，拿手边文档试一次。

## Emotional Curve

| 图序 | Audience state | Story beat |
|---|---|---|
| 1 cover | 痛点共鸣 | 复制粘贴毁格式 |
| 2 | 好奇 | 9 天 1.5 万星的开源工具 |
| 3 | 认知 | 一件事：办公格式进、Markdown 出 |
| 4 | 选择 | 三条入口怎么选 |
| 5 | 信任 | 隐私重点：WASM 本地转不上传 |
| 6 | 行动 | 诚实边界 + 试一次 |

## Visual Carrier（每张图的视觉承载体）

| 图序 | 类型 | 视觉承载体 | 配文要点 |
|---|---|---|---|
| 1 | cover_card | 无文字底图（本地排版标题） | 标题：把 Word/PDF 变成干净 Markdown |
| 2 | 内容图 | 乱码/散架对比示意 | 痛点场景 |
| 3 | 内容图 | 格式→Markdown 流程示意 | 一件事说清 |
| 4 | 内容图 | CLI/脚本/浏览器三入口分栏 | 怎么选 |
| 5 | 内容图 | 浏览器本地转示意 | WASM 不上传 |
| 6 | 内容图 | 行动步骤 3 行 | 试一次 |

## Non-Goals

- not_for: 长文替代、竞品对比、安装排错。
- do_not_show: 未验证速度数字、假截图。

## Next Gate

- gate: treatment-approval（QC 自评 55/65）→ produce image-post
