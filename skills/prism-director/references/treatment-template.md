# Director Treatment Template（Prism 蒸馏版）

> Internal reference for `prism-director`. Not host-discoverable.
> 蒸馏自 selfmedia-creator `skills/selfmedia-director/references/director-treatment-template.md`（自研）。

## 使用时机

导演方案、多形态改编、视频概念、战役 treatment、或从选题/母稿产出生产就绪交接物时读取本模板。

Treatment 是第一个生产门：核心意图与观众承诺未连贯前，不得进入 beat sheet、分镜、视觉生成或发布建议。

## 规则

- 一次 treatment 只拥有一个核心意图；两个意图竞争 → 拆分变体或请用户选择。
- 观众承诺要具体：观众留下来得到什么？
- 声明作品拒绝做什么（non-goals），边界保护调性与生产成本。
- 证据支撑的事实与创意解读分开标注。
- 平台技巧服从意图。
- 素材不足时标记 `scaffold` 并附来源清单。

## 核心模板

```markdown
# Director Treatment

## Identity

- master_id:
- working_title:
- content_kind:
- presentation_scope:
- status: treatment | scaffold | needs-source | approved

## Core Intent

- one_sentence_intent:
- audience:
- audience_promise:
- desired_aftertaste:
- primary_action_after_viewing:

## Logline

一句话：特定受众遇到特定冲突，发现特定转折。

## Conflict

- surface_conflict:
- deeper_conflict:
- cognitive_tension:
- emotional_tension:
- stakes_if_ignored:

## Narrative World

- viewpoint:
- narrator_role:
- value_stance:
- tone:
- rhythm_personality:
- forbidden_drift:

## Emotional Curve

| Stage | Audience state | Story beat | Evidence/detail | Risk |
|---|---|---|---|---|
| Entry |  |  |  |  |
| Build |  |  |  |  |
| Turn |  |  |  |  |
| Proof |  |  |  |  |
| Release |  |  |  |  |

## Evidence And Claims

| Claim | Evidence/source | Can appear in master | Can appear in variant | Notes |
|---|---|---|---|---|
|  |  | yes/no | yes/no |  |

## Production Reality

- available_assets:
- missing_assets:
- rights_constraints:
- human_appearance:
- voiceover:
- ai_visuals_allowed:
- production_cost_risk:
- approval_needed_before_generation:

## Presentation Variants

| Variant | Form | Audience angle | Reusable platforms | New creative needed | Reason |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Non-Goals

- not_for:
- do_not_say:
- do_not_show:
- do_not_generate:

## Next Gate

- gate: treatment-approval
- decision_needed:
- if_approved_next:
- if_rejected_rework:
```

## 变体注意

- **blog/文章**：补证据密度、配图作用、段落节奏；观众承诺要「值得收藏/值得转发」。
- **vlog/口播**：补表演者角色、脸/屏幕/B-roll 配比、前 3 秒画面；logline 要「可演」不只是「可解释」。
- **轮播/thread**：补单元数、首卡/首帖承诺、每个单元凭什么赚到下一次滑动。
- **AI 视频**：补角色/场景/物件连续性风险；生成前是否需要资产批准。

## 验收清单（可进 beat sheet 的条件）

- [ ] 一句话核心意图已陈述
- [ ] 受众与观众承诺具体
- [ ] 冲突是真实的，不只是话题标签
- [ ] 视角与语气稳定
- [ ] 事实与创意解读分离
- [ ] 视觉/声音世界服务同一意图
- [ ] 生产现实明确
- [ ] non-goals 防止漂移
- [ ] 下一个批准门可见
