---
slug: prism-title-lab-v1
version: v0.0.1
status: frozen
language: zh
domain_required: true
package_maturity: filled
parser_contract: beacon-feature-package-v2
materials_status: current
truth_source_model: intent_first
canonical_refs:
  prd: docs/beacon/v0.0.1/features/prism-title-lab-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-title-lab-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-title-lab-v1/tests.md
provenance:
  - ac_id: AC-001
    source_type: user_intent
    source_ref: "utterance_sentence_1: 补齐 Prism 标题能力：title-lab 参考层（7 公式 8 模板蒸馏）"
  - ac_id: AC-002
    source_type: user_intent
    source_ref: "utterance_sentence_2: intel briefing 增标题公式建议"
  - ac_id: AC-003
    source_type: user_intent
    source_ref: "utterance_sentence_3: anti-slop 与 quality-gates 增标题门"
  - ac_id: AC-004
    source_type: user_intent
    source_ref: "utterance_sentence_4: ATTRIBUTION-corpora+LICENSE+title-corpus 语料署名"
  - ac_id: AC-005
    source_type: user_intent
    source_ref: "utterance_sentence_5: metrics/review 命中率闭环，发布人工门"
---

# Requirement Truth: prism-title-lab-v1 (v0.0.1)

## 人话

给 Prism 补一块「会起标题」的蒸馏能力：把已核实的外部开源 Skill（bigpeng-hot-gzh，MIT）
的 7 种标题公式与 8 个选题模板，改写成 Prism 自己的参考层，并接进现有选题、成稿、验收、复盘四个环节。

- 能做：新增 `title-lab.md` 参考层（路径 A 出 6 条候选标题覆盖 ≥6 种公式 + 1 首选；路径 B 出 4 个选题方向，
  模板不重复）；`prism-intel` briefing 在选题角度后给出公式化标题建议；`prism-qa` 与编排门禁对候选标题
  做质量检查；语料样本与 MIT 署名落到 Prism 文档；指标与复盘字段记录「标题公式 ↔ 命中结果」。
- 不能做：不训练或微调任何模型权重；不承诺「必爆 / 必命中」；不把上游样本当 Prism 原创；
  不整段搬运上游 100 篇爆文原文；不新增发布通道，公开发布仍走人工门。
- 怎样算完：5 个 AC 全部有落盘产物；每个 AC 有可执行 TC（Command + Assertion）；verify-closure 通过；
  Truth Review Gate 通过后 freeze，再进入实现。

## User Intent

> 补齐 Prism 标题能力：title-lab 参考层（7 公式 8 模板蒸馏）；intel briefing 增标题公式建议；
> anti-slop 与 quality-gates 增标题门；ATTRIBUTION-corpora+LICENSE+title-corpus 语料署名；
> metrics/review 命中率闭环，发布人工门。

## User Intent Snapshot

- lake_or_ocean: lake
- 承诺面：Prism 内部 skill / 契约 / 文档层（references + contracts + docs + registry），不承诺平台流量结果。
- 命中语义：由「可执行标题门 + 发布后 4 周基线对比」定义，不是绝对值承诺。

## Domain Model

| Entity | Key | Precedence / Requires |
|--------|-----|------------------------|
| TitleLabel | label_id | 标题实验室实体；引用选题角度/母稿；输出候选标题集 |
| TitleCandidate | candidate_id | 属于 TitleLabel；携带公式 id、字数、兑现点、首选标记 |
| TitleGateReport | report_id | 引用候选集；banned 命中清单；gate verdict（pass/fix） |
| PublicationMetric | metric_id | 引用候选标的最终标题；title_formula / is_preferred / 平台指标 |
| ReviewBaseline | baseline_id | 4 周窗口的公式命中对照；只能由已发布指标聚合 |

## 用户旅程

US-TITLE-001：创作者拿到选题或草稿 → produce 调 title-lab 出候选标题集（路径 A/B）→
prism-qa 跑标题门 → 用户选定/首选锁定 → 随文章/贴图发布 → E1 记录 title_formula 与是否首选 →
E3 每 4 周对比基线沉淀记忆。

## Alignment Surface（本 revision 必煮干）

| 对齐项 | 承诺 | 边界 |
|---|---|---|
| title-lab 参考层 | produce 侧新增 title-lab.md：7 公式 + 8 模板 + 硬规则 + 样本校准引用 | 只做标题与选题方向，不生成正文 |
| intel 公式建议 | briefing-schema 增「选题角度 + 标题公式建议」小节 | 不改变六段式主体，不削弱不编造门 |
| 标题门 | anti-slop-gate + quality-gates Gate 4 增标题检查项 | 检查规则可 grep/脚本化，不要求模型评分 |
| 语料署名 | ATTRIBUTION-corpora.md + LICENSE + title-corpus 校准层 | 只收录已公开 45 条样本与公式规则；不追索上游未公开语料 |
| 命中率闭环 | metrics-publication 增 title_formula/is_preferred；review-loop 增 4 周基线对比 | 字段先落，对比数据依赖真实发布回流后验 |

## Phased Backlog（明确不在本包 closure）

- P1：小红书 / 视频号 / B 站标题配方差异项——延后，需平台数据。
- P2：命中率统计面板与自动周报——延后，待 E1 数据积累。
- P3：上游 100 篇全量语料入库——延后，上游未公开。

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-001 | prompt | must | AC-001 | covered |
| INT-002 | prompt | must | AC-002 | covered |
| INT-003 | prompt | must | AC-003 | covered |
| INT-004 | prompt | must | AC-004 | covered |
| INT-005 | prompt | must | AC-005 | covered |

## Acceptance Criteria

| AC ID | Description | FSM 路径 |
|-------|-------------|---------|
| AC-001 | `skills/prism-produce/references/title-lab.md` 存在；含路径 A（6 条候选标题，覆盖 ≥6 种公式 + 1 首选）与路径 B（4 个选题方向，模板不重复）；含硬规则（空数字 / 震惊体 / 编造社会证明 / 同义改写禁止）与「正文兑现点」约束；出声口径为 Prism 自己的规则，不含整段上游原文。 | candidate_set → qa_pending |
| AC-002 | `skills/prism-intel/references/briefing-schema.md` 增补「选题角度 + 标题公式建议」小节：每个选题角度给出对应公式/模板候选，并注明由 produce 侧 title-lab 执行。 | candidate_set → qa_pending |
| AC-003 | `skills/prism-qa/references/anti-slop-gate.md` 增「标题门」：检查空数字、震惊体、无法兑现、同义改写；`skills/_internal/orchestration/quality-gates.md` Gate 4 增「标题门 pass」条件：公式覆盖 ≥6、标题 18–32 字、工具名前 16 字、附赠物有正文兑现。 | qa_pending → selected_pending；qa_pending → candidate_set（修） |
| AC-004 | `docs/ATTRIBUTION-corpora.md` 存在，含 MIT 许可声明、上游仓库地址与核实日期；标题语料样本以校准层落盘（`skills/prism-produce/references/title-corpus.md`），标注来源与检索日期；仓库 LICENSE 随附上游 MIT 文本。 | candidate_set → qa_pending（语料完整性前置） |
| AC-005 | `contracts/metrics-publication.contract.md` 增 `title_formula` 与 `is_preferred` 跟踪字段；`contracts/review-loop.contract.md` 增「每 4 周对比标题公式命中的基线」条目；发布仍须人工批准（release 人工门不变）。 | locked → published（人工批准） |

## Domain FSM（标题生命周期）

状态链：candidate_set → qa_pending → selected_pending → locked → published

| State | From | Guard |
|-------|------|-------|
| candidate_set | — | 路径 A/B 产物齐全 |
| qa_pending | candidate_set | 候选标题集已生成 |
| selected_pending | qa_pending | 标题门 pass |
| locked | selected_pending | 用户选定或首选明确 |
| published | locked | 人工批准 + 全 gate 过 |

## Illegal transitions

- candidate_set → locked（跳过标题门）
- qa_pending → published（未人工批准）
- locked → published（无 gate / 人工链记录）
- 标题门报告伪造 pass 或 maker 自证
- 宣称「必爆 / 必命中」为承诺

## FSM 五元组（标题生命周期业务状态机）

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| candidate_set | generate（路径 A/B） | 6 公式或 4 方向已生成 | qa_pending | 产出候选标题集 |
| qa_pending | run_title_gate | banned 模式 0；兑现点齐全 | selected_pending | 生成标题门报告 |
| qa_pending | run_title_gate | 任一 banned 命中 | candidate_set | 附修复项重生成 |
| selected_pending | user_select | 用户或首选明确 | locked | 锁定标题进入 produce/渲染 |
| locked | publish_approved | 人工批准 + gate 全过 | published | 写入发布记录与指标字段 |

### invalid / illegal（FSM 五元组）

- candidate_set → locked（跳过标题门）
- qa_pending → published（未人工批准）
- locked → published（无 gate / 人工链记录）

## Non-goals

- 不训练、微调或上传任何模型权重；不承诺爆款 / 命中率绝对值
- 不整段搬运上游 100 篇爆文与未公开语料
- 不改写已有 form 契约的正文 / 格式结构（只增标题相关字段）
- 不新增平台发布通道或绕过人工批准
- 不产出「必过朱雀 / 保证流量」类宣传

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-T01 | 命中率绝对值验证依赖发布后平台数据 | accepted | 字段与 4 周对比机制进包，数据后验 |
| DL-T02 | 小红书 / 视频号标题差异配方 | accepted | 延后到 E1 数据积累 |
| DL-T03 | 上游 100 篇全量语料 | accepted | 延后，上游未公开 |

## Provenance

Each AC traces to a confirmed user intent (see frontmatter provenance).

## Source Excerpt

```markdown
补齐 Prism 标题能力：title-lab 参考层（7 公式 8 模板蒸馏）；intel briefing 增标题公式建议；
anti-slop 与 quality-gates 增标题门；ATTRIBUTION-corpora+LICENSE+title-corpus 语料署名；
metrics/review 命中率闭环，发布人工门。
```
