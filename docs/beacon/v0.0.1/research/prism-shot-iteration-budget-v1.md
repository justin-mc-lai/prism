# Research Closure: prism-shot-iteration-budget-v1

- version: `v0.0.1`
- feature: `prism-shot-iteration-budget-v1`
- 别名：镜头迭代预算 / 收敛红线 / 生成预算门
- diagram_types: none
- state_axes: shot-generation (prompted → attempted<N → converged | simplified | aborted)
- status: research closure（planner artifact，非 frozen truth）

## 人话

漫剧/短剧实操里有三条硬纪律，Prism 现在**一条都没落成门**：

1. **每镜有生成预算，超了就简化，不许无限抽卡。**
   推文原话："一个分镜平均 3–4 次生成换 1 条可用，一集 18 镜，50–70 次生成是常态"；
   红线："一镜 10–15 次迭代不收敛就简化镜头，不许烧生成次数"。
2. **原生对白做不出来就改镜头设计，永远不走后期配音。**
   推文原话："原生对白做不出来就改镜头设计，永远不走后期配音"。Prism 有"无本地兜底"铁律，
   但**没有**"配音兜底"这条具体禁令与检测。
3. **画面里的"不要"无效，必须改肯定式表达。**
   推文原话："否定约束只对字幕和音频有效，画面上想'不要'什么，得用肯定式表达"。
   Prism 的 `prompt-syntax-table.md §9` 只有"禁抽象质量词"，**没有**这条。
4. （同族）**能力域前置**：定分镜前先问"这个模型做得到吗"。
   推文："做漫剧不是实现导演意图，而是在模型可达域内找最优解"。
   `drama-storyboard-spec.contract.md` 已有"阈值单题材+单模型，换模型须重测"的意识，但没成为前置门。

**为什么值得单独冻**：这是从"能产"到"可控产"的分界线。没有预算与收敛红线，
生产会退化成无限抽卡——成本不可控、交付不确定。

## 现状证据

| 项 | 现状 | 缺口 |
|---|---|---|
| 生成尝试计数 | `scripts/ai_manga_drama.py` 只有 `init/validate/request/assemble/qa/manifest`；`request` 产 `render-request.json` | **无 attempt/revision 计数、无预算** |
| 收敛判定 | 无 | **无"超预算 → 强制简化镜头"规则** |
| 对白兜底 | `assemble` "stitches provider clips only; no synthesis, no fallback"（README/脚本注释） | 有"无合成兜底"总则，**无"对白失败必须改镜头设计、禁后期配音"专项判据与检测** |
| 画面否定 | `prompt-syntax-table.md §9` 禁抽象质量词/禁字幕/禁空表情 | **无"画面类否定无效→改肯定式"** |
| 能力域前置 | `drama-storyboard-spec.contract.md` 声明阈值可迁移性 | **非前置门**，无"选定 provider/模型 → 探测可达动作白名单"步骤 |
| 成本/预算模型 | 无 | **全仓无** |

## 第一性原理（三句话）

1. **模型有硬边界**（10s 时长、对白发音、画面否定无效）。工作流若假装边界不存在，产出必崩。
   → 约束必须**前置到设计期**（分镜规划），而不是在生成期反复抽卡修补。
2. **抽卡次数 = 成本**。成本必须**有预算、可观测、超限触发降级**（简化镜头），而不是无限重试。
3. **"降级"只能向"改设计"方向**（简化镜头 / 改对白为画面叙事），**不能向"后期合成"方向**
   （配音/对口型/本地合成）。后者是违反"无本地兜底"的假交付。

## Business Flow（produce 侧闭环）

```text
director 交分镜（含每镜 actions/dialogue）
  → 能力域前置门（canonical: provider 能力白名单）
      对白 >模型可达 → 直接退回改镜头设计（不进生成）
  → produce 逐镜生成，每镜 attempt 计数
      收敛（达标）→ 记录 attempts → 下一镜
      达预算上限仍未收敛 → 触发「简化镜头」（拆/并/降复杂度）→ 重规划该镜
      对白失败 → 改镜头设计（禁后期配音兜底）
  → 证据：每镜 attempts / cost / 收敛方式（native|simplified|redesigned）
  → QA 复核预算与收敛记录（超预算无降级 = fail）
```

## State Machine

- `planned` → `prompted`（提示词就绪）→ `attempting(n)`（第 n 次生成，n≤budget）
  → `converged`（达标）| `simplified`（超限降级后达标）| `redesigned`（对白失败改设计后达标）| `aborted`（不可达，停）。
- 合法：只增 n，不无限；`attempting(n>budget)` **非法**，必须先进 `simplified`/`redesigned`。
- 阻断：`converged` 前禁止进入 `assemble`；发现有后期配音产物 → fail-closed。
- 恢复：`simplified`/`redesigned` 后重置该镜预算（有上限次数，防无限降级循环）。

## Decision Priority（冲突裁决）

1. 现行契约（`prompt-syntax` / `drama-storyboard-spec` / `form-manga-drama`）> 本地约定。
2. **无兜底** > 便利：禁后期配音/合成，哪怕画面"差一点"。
3. **设计期约束 > 生成期修补**：能在分镜阶段避免的，不许推到抽卡。
4. 预算硬上限 > 完美主义：到顶必须降级，不许"再来一版"。
5. 阈值可迁移性：预算数字（如 10–15）来自**单题材+单模型**观测（推文/Seedance），
   换模型须重测并记录——**引用必须带来源与条件**，否则视为无证据。

## 湖海拆分

判定：**湖**，且**单 feature**（三条同族纪律 + 预算，一个门集）。program 归到生产纪律侧。

| 湖 | feature | 交付 |
|---|---|---|
| （本） | `prism-shot-iteration-budget-v1` | 预算/收敛门 + 禁后期配音判据 + 画面否定→肯定式判据 + 能力域前置门 + 校验脚本 + 证据 schema |

后续（defer，不在本包）：跨镜成本聚合报表 / provider 计费对接 / 自动降级策略学习（归 Lake E 学习面）。

## Promotion Notes（转 truth 的 AC 候选）

- AC-ITB-001：分镜/镜头 schema 增加 `iteration_budget`（每镜生成上限）与 `attempts`（实际次数）；`attempts > iteration_budget` 且无降级记录 → blocked + `reason_code=iteration_budget_exceeded`。
- AC-ITB-002：超预算必须有**降级记录**（`convergence: simplified|redesigned` + 具体动作），否则不得进入下一镜；降级次数有上限（防无限降级）。
- AC-ITB-003：**禁后期配音兜底**——证据链中若检出"对白由后期 TTS/配音合成"（而非 provider 原生对白或改设计后无对白）→ fail-closed + `reason_code=post_dub_fallback_forbidden`。
- AC-ITB-004：**画面否定式判据**——`prompt-syntax` 增加判定：画面描述的否定式（`no X` / `不要 X` 描述画面元素）须改为肯定式；命中即 blocked + `reason_code=image_negation_not_affirmative`（字幕/音频类否定除外）。
- AC-ITB-005：**能力域前置门**——produce 前须声明目标 provider/模型，并校验分镜动作/对白在该模型的**可达白名单**内；不可达项**在设计期**退回改镜头，不进生成（`reason_code=action_outside_model_domain` / `dialogue_outside_model_domain`）。
- AC-ITB-006：校验脚本（如 `scripts/check_shot_iteration_budget.sh`）可对给定 storyboard/证据判定：预算未超 或 有合规降级；含否定式画面描述即失败；含后期配音兜底即失败。
- AC-ITB-007：阈值来源义务——预算上限与可达白名单必须带来源与测试条件（题材+模型）；未标注来源的阈值视为无证据，门报 `threshold_source_missing`。

## Decision Priority 附：与既有门的关系

- `prompt-syntax.contract.md`：AC-ITB-004 是**新增判据**（不替代现有 8 判据）。
- `drama-storyboard-spec.contract.md`：AC-ITB-005 把其"阈值可迁移性"声明升级为**前置门**。
- `form-manga-drama.contract.md` §5 / `assemble` 的 no-fallback：AC-ITB-003 是其**对白专项化**。
- `asset-consistency`：无重叠（管跨镜一致性，不管预算）。

## 待确认（本轮用户已裁决）

- ✅ 用户："2 需要做" + "都冻、并行" → 本 feature 与 `prism-ip-schema-v1` **一起冻结、并行推进**。

## Promotion Log

- 2026-09-30：planner brainstorm（provenance: Jarvis Muse 漫剧六步法推文
  `https://x.com/jarvis11x/status/2104397648438476868`）产出本 research closure（非冻结真相）。
- 2026-09-30（裁决）：**promoted → freeze `prism-shot-iteration-budget-v1`**（AC-ITB-001..007），
  与 `prism-ip-schema-v1` 并行。
