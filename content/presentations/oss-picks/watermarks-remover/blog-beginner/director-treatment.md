# Director Treatment — watermarks-remover 科普文

- mode_id: treatment-director
- public_id: director
- lane: standard
- recommended_next_harness: produce
- map_ids_considered: ['MAP-002']
- master_ref: content/masters/oss-picks/watermarks-remover/MASTER.md

## Core Intent

- one_sentence_intent: 让 AI 重度用户知道「AI 会在文件里留多层溯源痕迹、怎么查、怎么按需清、边界在哪」。
- audience: 内容创作者、AI 工具重度用户（不假设会写代码）。
- audience_promise: 看完能用一条命令检查自己的文件，并分清「自己的内容」与「不该动的内容」。
- primary_action_after_viewing: 拿一份自己的文档跑 `inspect_file.py` 看一眼有没有隐藏痕迹。

## Logline

AI 写的字、生成的图，会悄悄带着几层溯源水印；一个 4 天涨到 8.5 千星的开源工具，
能查出来、按需清掉——但官方把边界写得很清楚：只对你拥有的内容动手。

## Conflict

- surface_conflict: 看不见的痕迹 vs 看得见的清理命令。
- deeper_conflict: 「清理自己的水印」与「伪装 AI 内容」只有一线之隔——工具怎么守住这条线。
- stakes_if_ignored: 你的文档/图片在不知情时携带厂商溯源信息。

## Emotional Curve

| Stage | Audience state | Story beat |
|---|---|---|
| Entry | 意外 | AI 文件里藏着看不见的痕迹 |
| Turn | 好奇 | 4 天 8.5 千星 + 三层处理结构 |
| Proof | 信服 | inspect 一条命令能查出来 |
| Release | 行动 + 边界 | 只清自己的内容；两个 harness 从不发布 |

## Evidence And Claims

| Claim | Evidence/source | Notes |
|---|---|---|
| 4 天涨到约 8.5 千星 | MASTER claim 6（08-11 创建，08-15 检索） | 日期推算，标注快照 |
| 三层处理 + 格式清单 | claim 2–3 | 不超卖 |
| 纯 stdlib Python | claim 5 | 关键卖点 |
| 两个 harness 从不发布 | claim 12 | 伦理边界事实 |
| content you own 定位 | claim 1 | 全文必须保持 |

## Non-Goals

- not_for: 教人规避平台检测、伪造内容来源、批量刷水印检测。
- do_not_say: 「一键清除所有 AI 痕迹」「必过检测」。
- do_not_show: 未验证的清除率/检测率。

## Next Gate

- gate: treatment-approval（QC 自评 56/65）→ produce blog
