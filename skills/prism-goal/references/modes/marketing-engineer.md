# Mode: marketing-engineer

把「已做完的东西」推到见世面：定位 → 冻结 → 派生 → 草稿 → 人批公开 → 回流 → 复盘 → 学习 → 下一轮。
这是 `loop-campaign` 的**回环延伸**：车道不再止于 `release`。

设计依据：`../marketing-engineer/first-principles.md`（对象链不变量 + 断点诊断 + 出圈阶梯）。
外部方法论参考：Shann³《How to Become a Marketing Engineer》（来源见依据文件，不升级为 Prism 事实）。

## When to use

- 用户说：跑不出去 / 没见世面 / 只有本地能跑 / 想发布但没闭环 / 发完没人看 / 有数据但不复盘
- 已有可发布对象（产品/母稿/成稿），要的是**发布与回流**，不是从零选题
- 要串多轮：本轮结果决定下一轮（战役/连载/周期报告）

## When not to use

- 只有单步创作（选题/定稿/成稿/验收）→ 直接交对应公开面
- 只建草稿或只公开发布一次 → `prism-release`
- 纯编码/工程交付 → `beacon-goal`（FP-PRISM-001 分轨）
- 无任何可发布对象、连母稿都没有 → 先回 `prism-intel` / `prism-master`

## 与 loop-campaign 的差异

| | loop-campaign | marketing-engineer |
|---|---|---|
| 终点 | `release`（草稿/发布） | `release → measured → review → learn → 下一轮` |
| 触发 | 多面创作编排 | 已有对象要出圈 + 回环 |
| 缺证据 | 停止并列缺 | 同 + 缺 `publication_ref` 不得进 measured |
| 新增门 | — | campaign 整体一致性门（D-2）+ 回流入库人批 |

## Lane 与回环段

```text
fast:     goal → produce → qa → release                          → measure?
standard: intel → master → director → produce → qa → release     → measure → review → learn
canon:    goal → master → director → produce → qa(正典) → release → goal 复盘(含 measured 段)
```

- 回环段（`measure/review/learn`）**只读结果、只写复盘/记忆**，不产生新内容 truth。
- `measure` 可缺工具 → 显式空快照（`status=empty`），**不编造指标**（E2 守卫）。
- 无发布记录 → `blocked`，`reason_code=publication_record_missing`。

## 出圈阶梯（把用户位置对齐到台阶）

先判定用户在第几阶，只推下一阶，**不一次吃十个台阶**：

| 阶 | 状态 | 下一步该调谁 | 门 |
|---|---|---|---|
| 0 | 本地能跑 | （若纯工程）`beacon-goal`；若内容 → 1 | — |
| 1 定位 | 无受众/卖点/定位 | 建 `shared-knowledge`（受众/卖点/定位/声音）→ `prism-master` | 无来源不写定位 |
| 2 冻结 | 无母稿 | `prism-master` | 事实/正典未核完不冻结 |
| 3 派生 | 无形态 | `prism-director` + `form-autodetect` → `prism-produce` | 无核心意图不出方案 |
| 4 草稿 | 无草稿 | `prism-release`（草稿-only） | 无成稿引用 blocked |
| 5 人批公开 | 只有草稿 | 人工二次批准 → 记 `publication_id` | FP-PRISM-005 |
| 6 回流 | 无发布记录/指标 | E1 → E2（tools 缺失走空快照） | 无 publication_ref 不得 measured |
| 7 复盘 | 有计划无复盘 | E3 `review-loop`（`metrics_refs` 必填） | 无数据不空谈；入库人批 |
| 8 学习 | 复盘没沉淀 | E4 `learning-memory`（advisory only） | 可回放、冲突需标记 |
| 9 下一轮 | 结果没回简报 | `prism-intel` 下一份简报引用结果 + 人的解释 | 结果与解释一起进上下文 |

## Campaign 级编排（贯穿整场）

`loop-campaign` 已有：车道、form 识别、证据绑定。本模式追加三件事：

1. **共享上下文**：一份 campaign brief（受众/卖点/目标/排期）+ 一套视觉参考，所有渠道引用同一份。
   视觉参考与渠道产出的绑定见 `contracts/asset-consistency.contract.md`（形态内）；
   campaign 级统一目录锚点：`content/distribution/campaigns/{campaign_id}.yaml`。
2. **工单与并行**：把战役拆成可点名的工单（交付物 + 引用上下文 + 进审前必须过的检查 + 依赖 + 产出链接）。
   可并行的：竞品调研 / 历史复盘 / 潜客调研。不可并行的：最终文案（需已定卖点）、广告（需落地页）、
   跟进邮件（需与注册动作一致）。
3. **整体一致性门（D-2，本模式新增）**：单件都过门禁 ≠ 彼此不打架。发前必须复核：
   广告承诺 vs 落地页兑现 / 邮件 vs 母稿卖点 / 日期、链接、主张是否一致。
   任一不一致 → `blocked`，退回修改，**不进入公开发布**。

> 工单不是新对象 truth；它是 `DistributionJob` 的编排视图，落位由 release/adapter 侧记录。

## 周期任务与常驻 Bot（D-3 / D-5）

只有工作流**可靠跑通后**才允许加周期（cron）或常驻 bot。规则：

- 先跑通一次：定义它能访问什么、应产出什么、怎么检查、失败怎么办。
- **调度救不了没跑通的工作流**。数据更新失败必须显式报错，不得静默拿旧数据写一份笃定的报告。
- 权限分级：出报告 / 建草稿 / 改预算，需要的批准不同。默认只给「出报告 + 建草稿」，不给公开发布。
- Bot 只是消息或时间表触发的同一工作流；不新增 truth、不绕过人工门。

## 硬门（fail-closed）

- 无 `publication_ref` 不得 `measured`（FP-PRISM-006）
- 指标只出投影/空快照，**不编造趋势**（FP-PRISM-006）
- 复盘无 `metrics_refs` → `blocked`（E3）
- 学习记忆 advisory only，不写 truth、不通门（E4）
- 公开/排期/发布永远人工二次批准（FP-PRISM-005）
- campaign 整体一致性未过 → 不进入公开发布
- 凭据永不入仓（`credentials_never_in_repo`）

## Turn procedure

1. 一句话复述意图；判定用户在第几阶（上表）。
2. 选 lane；显式指定优先，多命中/零命中的形态交人（复用 `form-autodetect.md`）。
3. 只推**下一阶**，给一个 `recommended_next_harness`（公开面 id）。
4. 列出该交接需要的证据（路径或 missing）；缺证据写明，不跳过。
5. 若进入回环段：先查发布记录 → 再快照 → 再复盘 → 再学习；每步标注人批点。
6. 输出人类卡 + 机器面，停。

## Output extras

```yaml
mode_id: marketing-engineer
lane: standard|fast|canon
stage: 0|1|2|3|4|5|6|7|8|9
form_detected: ""            # classify_form 结果
publication_ref: null        # 回环段必填，缺失即 blocked
recommended_next_harness: intel|master|director|produce|qa|release|stop
campaign_consistency: none|pending|pass|blocked
```

## Nested refs（按需加载）

- `../marketing-engineer/first-principles.md` — 设计依据、断点诊断、Shann ↔ Prism 映射
- `contracts/metrics-publication.contract.md`（E1）· `contracts/metrics-snapshot.contract.md`（E2）
- `contracts/review-loop.contract.md`（E3）· `contracts/learning-memory.contract.md`（E4）
- `contracts/publish-bridge.contract.md` · `contracts/asset-consistency.contract.md`
- `skills/_internal/orchestration/publish-approval.md`、`quality-gates.md`（Gate 7）
