# Lake E Program Plan — 指标/学习回流（pln-program）

- program: prism-canon · version: v0.0.1 · lake: E
- plan_mode: interactive · scope_mode: phased_lake
- 来源: Lake A INT-P15 / DL-004 / FP-PRISM-006 / FSM published→measured / US-PRISM-001/002
- 生成日期: 2026-08-12

## Intent（一行）

把发布后的**证据回流**变成可验证闭环：发布记录 → 指标快照 → 战役复盘/圣经更新 → 可回放学习记忆；
指标只是投影（FP-PRISM-006），不编造指标（intel 硬门），learning 只辅助判断、不定义 truth。

## 源能力清单

| 簇 | 来源 | 角色 | 策略 |
|---|---|---|---|
| 发布证据 | D6 publish-bridge（draft_id/URL） | 回流基座 | distill 事件 schema |
| 指标采集 | analyze-data（wechat/xhs/douyin stats）、平台 API | 聚合分析 | bridge；凭证不入库 |
| 复盘 | creation-mode-map 系列圣经（bible 复盘段）、US-PRISM-002 goal 复盘 | 战役/连载复盘 | distill 复盘判据 |
| 学习 | Beacon learning 边界（可回放/可审计/可裁剪） | 记忆 | distill 存储 schema；advisory only |

## 子湖拆分与顺序

| 子湖 | feature slug | 交付物 | 策略 |
|---|---|---|---|
| E1 | prism-metrics-publication-v1 | 发布事件契约（publication_id/platform/url/published_at/artifact_ref）+ metrics-adapters 登记 | distill + bridge |
| E2 | prism-metrics-snapshot-v1 | MetricsSnapshot 契约（snapshot_id/指标字段/时间/来源证据）+ FSM published→measured 钩子 | distill + bridge |
| E3 | prism-review-loop-v1 | 战役复盘契约 + 系列圣经更新规则（人工批准入库） | distill |
| E4 | prism-learning-memory-v1 | 可回放学习记忆契约（advisory only、可审计、可裁剪） | distill |

顺序理由：先有发布证据（E1）→ 才有指标快照（E2）→ 才能复盘（E3）→ 才有可回放学习（E4）。

## Bridge / Distill 规则

- bridge：平台统计 API / analyze-data；凭证走受管 secrets，禁止入库
- distill：发布事件 schema、MetricsSnapshot schema、复盘判据、学习记录 schema
- 硬边界：不编造指标与趋势；learning 不定义 truth/gate；指标是投影不是 canonical

## 风险与门禁

- R1 平台 API 凭证：受管 secrets + protected path
- R2 指标真实性：缺 publication 记录不得产生 measured（FSM 非法转移）
- R3 learning 边界：只做可回放 advisory，不写入 requirement truth
- R4 每个子湖独立 feature 包，完整走 truth→freeze→implement→QA→release 人工门

## Route

E1 → E2 → E3 → E4；全子湖完成前不得宣称海 closure；Lake F 仍未做。
