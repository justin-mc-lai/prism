# Director Treatment — anydoc · thread-launch（样例）

```yaml
mode_id: treatment-director
creation_type: thread
form_id: thread
presentation_id: anydoc-thread-launch
hard_gate: "只出方案，不写正文、不渲染、不发布"
recommended_next_harness: produce
```

## Core Intent

一句话核心意图：让读者用一条 thread 看懂「内容与版式分离」这一个点。

- audience：经常把同一份内容铺到多个平台的人
- audience_promise：读完知道这条路能不能省事
- desired_aftertaste：这事不难，我也能试
- primary_action_after_viewing：去看一眼官方文档

## Logline

一份内容要发三个地方的人，遇到「改一处、三处都要改」的重复劳动，发现可以把版式交给模板。

## Conflict

- surface_conflict：同一份内容要手抄三遍
- deeper_conflict：内容和版式被绑死，改一个牵动另一个
- emotional_tension：明知道重复，却停不下来
- stakes_if_ignored：内容越多，重复成本越高

## Narrative World

- viewpoint：第二人称，对着读者说
- narrator_role：先试过的人，回头讲一句
- tone：平实，不推销
- rhythm_personality：短句推进，一条一个点
- forbidden_drift：不吹效果、不编数据

## Emotional Curve

| Stage | Audience state | Story beat | Evidence/detail | Risk |
|---|---|---|---|---|
| Entry | 被说中 | 改一处三处都要改 | 日常重复劳动 | 变成抱怨 |
| Build | 好奇 | 内容单独放一份 | 单一内容源 | 太抽象 |
| Turn | 明白 | 版式交给模板 | 模板决定版式 | 需要例子 |
| Proof | 认可 | 改一个不牵动另一个 | 分离带来的好处 | 过度承诺 |
| Release | 想试 | 代价也说清楚 | 前期要拆结构 | 变成软文 |

## Evidence And Claims

| Claim | Evidence/source | Can appear in master | Can appear in variant | Notes |
|---|---|---|---|---|
| 一份源文件生成多种格式 | 样例，无真实来源 | no | yes（标注 scaffold） | 不声称真实效果 |

## Production Reality

- available_assets：母稿引用位、版式模板
- missing_assets：真实母稿与来源核对（标注 scaffold）
- rights_constraints：样例，无第三方 IP
- human_appearance：无
- voiceover：无
- ai_visuals_allowed：否
- production_cost_risk：低
- approval_needed_before_generation：否（样例）

## Non-Goals

- not_for：真实项目背书
- do_not_say：不编造指标、不写平台效果
- do_not_show：无
- do_not_generate：无

## Next Gate

- gate: treatment-approval
- decision_needed：样例是否保留
- if_approved_next：produce
- if_rejected_rework：补真实母稿
