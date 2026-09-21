# Director Treatment — watermarks-remover · blog-beginner（样例）

```yaml
mode_id: treatment-director
creation_type: blog
form_id: blog
presentation_id: watermarks-remover-blog-beginner
hard_gate: "只出方案，不写正文、不渲染、不发布"
recommended_next_harness: produce
```

## Core Intent

一句话核心意图：让读者先分清"谁的素材"，再决定要不要用这类工具。

- audience：处理自己图片素材的普通创作者
- audience_promise：读完能自己判断一个场景合不合规
- desired_aftertaste：这事有边界，我知道边界在哪
- primary_action_after_viewing：先确认素材归属，再动手

## Logline

一个想清理自己图片素材的人，遇到"工具能用但不敢用"的犹豫，
发现判断标准其实只有一条：素材归谁。

## Conflict

- surface_conflict：工具能用，但不知道能不能用
- deeper_conflict：技术可行与合规可行是两回事
- cognitive_tension：边界不在工具，在使用者
- stakes_if_ignored：踩到他人权利或平台规则

## Narrative World

- viewpoint：第二人称，对读者说话
- narrator_role：先把边界讲清楚的人
- value_stance：不鼓励越界，也不吓唬人
- tone：平实，就事论事
- rhythm_personality：先给判断标准，再展开
- forbidden_drift：不写操作步骤、不写规避方法、不编数据

## Emotional Curve

| Stage | Audience state | Story beat | Evidence/detail | Risk |
|---|---|---|---|---|
| Entry | 被说中 | 能用但不敢用 | 常见犹豫 | 变说教 |
| Build | 明白 | 只问素材归谁 | 一句实话 | 太简化 |
| Turn | 理解 | 三步都不复杂 | 定位/重建/合成 | 变成教程 |
| Proof | 认可 | 坑在元数据与过度相信 | 三层坑点 | 过度技术 |
| Release | 有边界感 | 不提供规避方法 | 明确拒绝 | 显得回避 |

## Evidence And Claims

| Claim | Evidence/source | Can appear in master | Can appear in variant | Notes |
|---|---|---|---|---|
| 工具分三步 | 简报（样例） | yes | yes | 不写步骤细节 |
| 去除他人版权标识高风险 | 简报（样例） | yes | yes | — |
| 合规前提是自有素材 | 简报（样例） | yes | yes | — |

## Production Reality

- available_assets：母稿引用位
- missing_assets：真实来源核对（样例未做）
- rights_constraints：涉及第三方版权话题，须保守表述
- human_appearance：无
- voiceover：无
- ai_visuals_allowed：否
- production_cost_risk：低
- approval_needed_before_generation：是（合规敏感）

## Non-Goals

- not_for：教人去除他人水印
- do_not_say：不写操作步骤、不写平台规避方法
- do_not_show：无
- do_not_generate：无

## Next Gate

- gate: treatment-approval
- decision_needed：合规表述是否足够保守
- if_approved_next: produce
- if_rejected_rework：收窄到"自有素材处理"
