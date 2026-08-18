# Novel 连载 anti-slop 审计（2026-08-14 · 深度蒸馏门禁首跑）

> 依据: `skills/prism-qa/references/anti-slop-gate.md` + `human-voice-prose.md` §6 裁决表
> （novel 行：破折号允许但过度即删；感知修正式翻案腔逐处过「新区分」检验）
> 工具: `python3 scripts/check_human_voice.py <章节>`

## 结果总表

| 章节 | 破折号 | 感知修正翻案腔 | 其他硬禁令 | 结论 |
|---|---|---|---|---|
| fires-of-fate episode-001 | 0 | 4 处（灯光/鬼/烧别人/烧皮肤） | 硬停词 0 / 黑话 0 / 同构排比 1 处提醒 | canon passed · 发布前需按裁决人工判定 + 排比删减 |
| fires-of-fate episode-101 | 40 → **2**（保留 1 处核心揭示「不是尸体——是影子」） | 4 处（火不够/手机/灯坏了/收音机） | 叙述冒号 20 处已清；剩余 1 标题冒号 + 1 时间冒号（22:47）为结构位 | ✅ 硬失败清零（draft only） |
| fen-yuan-ren episode-001 | 28 → **4**（保留表盘→读数一组电影式转场，L26/L46） | 4 处（臭/动/敲/耳朵） | 叙述冒号 8 处已清；系统面板字段冒号（宿主/阶位/怨念值等）为 UI 固定位 | ✅ 硬失败清零（draft only） |

## 判定口径

- 破折号：源仓 kushi-narrative-zh 口径为「删过度破折号」；Prism 操作口径
  （human-voice-prose §6 novel 行）：单篇 >15 处或密度 >1 处/150 字视为过度。
- 翻案腔：novel 体裁中「不是X，是Y」若为人物感知修正的叙述动作（误解→认知变化）可保留，
  逐处过「新区分」检验；每篇 ≥5 处需删减。上表命中项均为感知修正式，待发布前人工过判别。
- 提示性冒号/叙述冒号：novel 正文中「引出原话」冒号合法（引用人物原话），非提示性用法。

## 处置

- 三章均为 draft only / 未发布；本审计不阻断 canon 状态（fires-of-fate 已 passed，
  fen-yuan-ren 为 review_required）
- ✅ 已修复（2026-08-14）：episode-101 破折号 40→2、fen-yuan-ren 28→4（保留项逐处说明），
  两章叙述冒号清零（仅标题/时间/系统 UI 结构位豁免）
- 发布路径（prism-release）前仍须完成：翻案腔逐处「新区分」判别记录（4+4 处均为
  感知修正式，按 novel 裁决行可保留）、episode-001 同构排比删减、fen-yuan-ren 保留
  破折号的人工复核，并把结果附回本审计
