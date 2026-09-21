# 营销工程师系统 · 第一性原理拆解（Prism 版）

> 落点：`prism-goal` 的 `marketing-engineer` 模式设计依据。
> 外部来源：Shann³ @shannholmberg《How to Become a Marketing Engineer》
> （原文 https://x.com/shannholmberg/status/2098004743536750869 ；中译情报快照见
> `~/Documents/IntelRadar/20260915T143749-vibe-marketing-营销工程师方法论.md`）。
> 边界：本文件是 Prism 的解读与映射，不新增内容 truth；external 主张一律标注来源，不升级为 Prism 事实。

## 0. 问题陈述

现状缺口不是「没有创作能力」，是**闭环没合上**：项目停在 vibe coding（本地能跑、能生成），
从未走完 `Publication → Metrics → Retrospective → Learning → 下一轮`。

对应到 Prism：**编排面（goal）的车道止于 `release`**。`measured` 态与 E1–E4 契约都在宪法与
adapter 里，但没有一个公开面模式去驱动它们。所以「跑不出去见世面」= 对象链的后半段没有编排入口。

## 1. Prism 创作工作流的第一性拆解

### 1.1 最小对象链（不可再分）

来自 `skills/_internal/orchestration/pipeline-contract.md`：

```text
SourceSignal → MasterContent → PresentationVariant → DistributionBinding
             → DistributionJob → Publication → MetricsSnapshot / Retrospective
```

这不是流程，是**七种存在**：每个对象都有独立的失败面，任一缺失，闭环就断。

### 1.2 从对象链导出的不变量

每条不变量 = 某个对象「为什么必须存在」。删掉对象，不变量立刻破。

| # | 不变量 | 由哪个对象保证 | 宪法锚点 |
|---|--------|----------------|----------|
| I1 | 信号先于内容：无来料不得成稿 | SourceSignal | `briefed` 守卫 `source_material_present` |
| I2 | 真值先于投影：展示只转译，不新增事实/正典 | MasterContent | FP-PRISM-002 / -003 |
| I3 | 绑定先于动作：无 `presentation×endpoint` 不得建 job | DistributionBinding | `content/distribution/bindings/` |
| I4 | 动作必须被记录：发布是基座，指标只是投影 | DistributionJob → Publication | FP-PRISM-006 |
| I5 | 结果先于结论：无发布记录不得 `measured` | Publication | FSM 守卫 `publication_record_exists` |
| I6 | 独立检验：生成方不得自证合格 | （跨对象） | FP-PRISM-004 |
| I7 | 不可逆点人批：公开发布只能人批 | （跨对象） | FP-PRISM-005 |
| I8 | 投影不是真值：渲染/发布记录/指标都可重算 | MetricsSnapshot | FP-PRISM-006 |

### 1.3 Prism 七面 = 对象链的职责切分

| 公开面 | 拥有对象 | 唯一职责 | 不碰 |
|--------|----------|----------|------|
| goal | Campaign（编排） | 选道、排序、绑证据、停在边界 | 不产、不定、不批 |
| intel | SourceSignal | 有证据的来料 | 不编趋势 |
| master | MasterContent / StoryWorld | 冻结事实与正典 | 不定呈现 |
| director | （方案） | 意图→treatment/分镜 | 不写正文 |
| produce | PresentationVariant | 按母稿生产 | 不自证 |
| qa | （证据） | 独立过门禁 | 不改事实放行 |
| release | DistributionJob / Publication | 草稿-only + 人批 | 不自动公开 |

### 1.4 闭环断点（诊断结论）

按 1.2 的不变量逐条对照，当前 Prism 的断点集中在 I4/I5 之后的编排缺失：

| 断点 | 不变量 | 现状 | 缺口 |
|------|--------|------|------|
| D-1 | I4/I5 | E1 `metrics-publication` + E2 `metrics-snapshot` 契约、Gate 7 都在 | goal 车道到 release 就停；无模式驱动 measured 段 |
| D-2 | I6 | `asset-consistency` 门只管 AV 形态内部一致 | 无 **campaign 级多渠道整体一致性**（广告承诺 vs 落地页 vs 邮件） |
| D-3 | I1 | intel 单次选题强 | 无「周期性拉新信号」（cron/重复任务）编排 |
| D-4 | I2 | master 单 slug 事实强、series bible 有 | 缺 **company 级知识层**（受众/卖点/定位/声音）跨 campaign 复用 |
| D-5 | I6/I7 | 人批在 release 有 | 无 bot/常驻入口承接「团队派活 + 定时」 |

## 2. Shann 六层 ↔ Prism 落点

| Shann 层 | 一句话 | Prism 现有落点 | 状态 |
|----------|--------|----------------|------|
| 什么是营销工程师 | 搭系统而非写文案 | 宪法「角色」+ 七面职责表 | ✅ 已有（概念） |
| 工作空间 | 按职能分目录 + 共享知识 | `pipeline-contract.md` dossier 布局 + `docs/sot-layering-decision.md` L1–L5 | ✅ 已有（L3/L4 在源仓） |
| 连接工具与数据 | API/凭据/权限拆分 | `registry/*-adapters.yaml` + `credentials_never_in_repo` + fail-closed bridge | ✅ 已有 |
| 知识层 | 内部+外部知识，来源与日期，已批准 vs 随口 | `prism-master` canonical claims + source trace；`content/series/*/bible.md` | ◐ 部分（缺 company 层，D-4） |
| 数据层 | 数仓 + 定时刷新 + 不虚假归因 | E1 `metrics-publication` / E2 `metrics-snapshot` / Gate 7 | ✅ 契约已有（缺编排入口，D-1） |
| 第一条工作流 | 先规划再跑，用人审 | `loop-campaign` 车道 + `publish-approval.md` | ✅ 已有 |
| 贯穿整场战役 | 共享 brief + 视觉参考 + 工单 + 并行 + 整体复核 | campaign/binding schema + `asset-consistency`（部分） | ◐ 部分（缺 campaign 整体门，D-2） |
| 循环逼近目标 | 定义完成→检查→退回→通过才交人 | `quality-gates.md` + loop-campaign 状态机 | ✅ 已有 |
| 定时任务与自治 Bot | cron + Slack bot | 无 | ❌ 缺口（D-3/D-5） |

## 3. 蒸馏后的方法论

### 3.1 三条公理

1. **没被发布的东西不存在。** 本地能跑 ≠ 存在。只有 `Publication`（平台真实 ID/URL）才是存在证据。
2. **没被记录的发布不能度量。** 指标是投影；先有 `publication_ref`，才允许快照（E2 守卫）。
3. **没回流的结果不算经验。** 结果必须经复盘（E3）→ 学习记忆（E4，advisory）→ 回到下一轮信号。

### 3.2 出圈阶梯（vibe coding → 见世面）

```text
0 本地可跑（vibe coding）
1 定位：一句话受众 + 卖点 + 定位（company 知识层，D-4）
2 冻结：把产品事实/正典冻成 master（I2）
3 派生：一真值多投影，按渠道出形态（I3）
4 草稿：发布桥只建草稿（I7 前置）
5 人批公开：人工二次批准 → publication（I4/I7）
6 回流：发布记录 + 指标快照（I4/I5）
7 复盘：metrics_refs 必填的复盘（E3）
8 学习：可回放记忆（E4，advisory only）
9 下一轮：结果 + 人的解释一起进下一份简报（I1 回环）
```

**首个该做的阶梯永远不是 0→全部，而是「挑一个你最会判断好坏的任务，把 2→6 跑通一次」。**

### 3.3 车道回环扩展

现有车道只覆盖到 release，本模式在其后追加 measured 段：

```text
fast:     goal → produce → qa → release                         [+ measure?]
standard: intel → master → director → produce → qa → release    → measure → review → learn
canon:    goal → master → director → produce → qa(正典) → release → goal 复盘
```

规则：`measure/review/learn` 三段**不产生新内容 truth**，只写复盘/记忆（E3/E4，人工批准后）。

## 4. 硬边界（继承）

- 内容 truth 与工程 truth 分轨（FP-PRISM-001）：编码项目要走 Beacon 工程轨；Prism 只给内容/营销侧。
- 母稿权威（FP-PRISM-002）：营销派生不得新增事实。
- maker ≠ checker（FP-PRISM-004）。
- 公开发布必须人工批准（FP-PRISM-005）。
- 不编造指标/趋势；无发布记录不得 measured（FP-PRISM-006）。
- 不把本模式说成「全海能力已交付」（FP-PRISM-013）。
