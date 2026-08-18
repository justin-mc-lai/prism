---
name: kushi-narrative-zh
description: |
  库拾母版叙事规范：把 MASTER.md 改写成连贯、有人味的中文科普稿（humanized.md）。
  适用于 oss-pick-standard 深度库拾与 oss-pick-daily 日榜。
  在 humanizer-zh 之前执行。触发：润色 humanized、库拾母版、日榜/深度稿去清单化。
triggers:
  - pattern: "库拾叙事|科普叙事|kushi-narrative"
  - pattern: "humanized.*母版"
allowed-tools:
  - Read
  - Write
  - Edit
metadata:
  pipeline_step: narrate
  pipeline_order: before humanizer-zh
  trigger: MASTER.md → humanized.md 叙事润色
  pairs_with: [humanizer-zh, kushi-visual-enrich]
  authority: content/masters/_template/MASTER-SPEC.md
  gold_samples:
    - content/masters/oss-picks/superpowers/humanized.md
    - content/masters/oss-picks/daily-2026-06-17/humanized.md
---

# 库拾叙事科普（kushi-narrative-zh）

> **成稿主入口为 `selfmedia-writing`**（新手小白 + 深度四段式 + 编排 humanizer）。本 skill 保留为**体裁与 anti-patterns 参考库**；新稿请优先 `/selfmedia-writing`。

你是库拾的母版编辑。任务不是「压缩信息」，而是**写给人读的科普文章**：有场景、有顺序、有判断，术语自然嵌进段落，而不是标语和表格堆砌。

本 skill 负责**叙事层**；去 AI 痕交给 `humanizer-zh`（pipeline 里两步串联，先 narrative 后 humanizer）。

## 何时使用

- `content/masters/**/MASTER.md` 已完成，需要产出 `humanized.md`
- 现有 `humanized.md` 读起来像清单、模板、口号（「30 秒看懂」「没设计不准写码」）
- 日榜或深度稿需要统一「库拾文风」

## 两种体裁

| 体裁 | pipeline | 参考样稿 |
|------|----------|----------|
| **深度库拾** | `oss-pick-standard` | `content/masters/oss-picks/superpowers/humanized.md` |
| **日榜** | `oss-pick-daily` | `content/masters/oss-picks/daily-YYYY-MM-DD/humanized.md` |

详细结构见 `references/archetypes.md`；禁止写法见 `references/anti-patterns.md`。配图规范见 `skills/kushi-visual-enrich/`；公众号节奏参考见其 `references/wechat-style-notes.md`。

## 核心原则（6 条）

1. **场景先行** — 用读者熟悉的处境开场（被 AI 乱改代码、刷 Trending 不知道点哪个），再引出项目。
2. **顺序叙事** — 按「是什么 → 怎么工作 → 怎么用 → 局限 → 下一步」推进；流程类内容按**时间顺序**讲，不要跳步。
3. **段落为主** — 一节至少 2～3 句完整 prose；表格只用于对比、安装命令、日榜数据，不替代正文。
4. **配图锚点** — 深度稿在「建立信任 / 建立全局模型」处插入截图 + 图说（见 kushi-visual-enrich）
5. **术语 inline** — 专业词首次出现时解释；禁止整页名词表
6. **有人味** — 允许具体感受与判断；禁止 AI 腔（见 humanizer-zh）

### Step 1：读 MASTER + meta.yaml

提取：仓库链接、star 快照、one_line_conclusion、目标读者、可操作步骤（安装/试用）。

### Step 2：选体裁 archetype

- 深度 → `references/archetypes.md#深度库拾`
- 日榜 → `references/archetypes.md#日榜`

### Step 3：写 humanized.md

- H1 保留 meta 标题方向，**禁止**字面「总（」「分（」作 H2
- 小节标题用自然语言（「先说你可能遇到过的事」「今天 GitHub 上什么在涨星」）
- 全中文；英文仅保留：仓库名、命令、skill 文件名、协议名（首次带中文解释）
- 深度稿：Claude Code / Codex 安装方式优先，Cursor 仅作库拾验证示例
- 保留 `assets/` 图片引用路径

### Step 4：自检（30 秒）

见 `references/archetypes.md` 末尾自检 + `skills/kushi-visual-enrich/references/checklist.md`（若已配图）。

### Step 5：视觉充实（深度稿）

交 `kushi-visual-enrich` 抓取文档站/GitHub 截图并写图说；日榜可跳过或仅封面。

### Step 6：交给 humanizer-zh

对 `humanized.md` 再跑一遍去 AI 痕，重点删：三段式排比、过度破折号、空洞金句。

## 与 MASTER-SPEC 的关系

- `MASTER-SPEC.md`：字段、四端渲染、assets 约束（authority）
- **本 skill**：humanized 层的叙事方法与体裁模板（method）
- **humanizer-zh**：语言自然化与反 AI 腔（polish）

## 禁止

- 把 `qi-dev-llm-plain-summary` 的输出模板（「一句话结论」「名词大白话」整节）原样贴进正文
- 在读者稿里写内部工具链（ao compose、agency-agents 安装路径等），除非文章主题就是库拾工作流
- 用 star 数代替价值判断，不解释项目解决什么问题

## 示例调用

```text
/kushi-narrative-zh 把 content/masters/oss-picks/foo/MASTER.md 润色为 humanized.md，深度库拾体裁
```

```text
/kushi-narrative-zh 重写 daily-2026-06-17 humanized.md，日榜体裁，表格保留
```
