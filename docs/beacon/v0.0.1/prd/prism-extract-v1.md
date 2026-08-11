---
slug: prism-extract-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
domain_required: true
ux_required: false
parser_contract: beacon-feature-package-v2
materials_status: current
package_maturity: filled
truth_source_model: intent_first
program_ref: docs/beacon/v0.0.1/programs/prism-canon/program-manifest.md
canonical_refs:
  prd: docs/beacon/v0.0.1/features/prism-extract-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-extract-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-extract-v1/tests.md
provenance:
  - ac_id: AC-EXTRACT-001
    source_type: user_intent
    source_ref: "utterance 2026-08-11: 开始 Lake B，并确保在新的库立项"
  - ac_id: AC-EXTRACT-002
    source_type: migrated_truth
    source_ref: "selfmedia-creator docs/beacon/v0.0.6/features/prism-canon-v1 R3 · DL-001/DL-008"
  - ac_id: AC-EXTRACT-003
    source_type: user_intent
    source_ref: "utterance: 把当前的冻结的需求迁移进行实现，通过 beacon-goal v0.0.1"
---

# Requirement Truth: prism-extract-v1（v0.0.1 · Lake B）

## 人话

把 `selfmedia-creator` 里已冻结的 Prism 宪法与 Source Skill Inventory，落到**独立新仓 Prism**：建仓立项、迁入宪法、装上 1+6 公开面 SKILL 壳、契约模板、编排内核和 adapter 索引。本湖只做提取落地，不做八形态生产链，也不宣称全海创作能力已交付。

- 能做：独立仓 + 宪法迁入 + 七个公开面壳 + 注册表 + 七段契约模板 + 人类卡 + 编排内核迁入 + adapter 索引
- 不能做：不实现 form producer chains（Lake D）；不落 campaign schema（Lake C）；不改 Beacon 编码能力；不自动公开发布
- 怎样算完：四件套填满；AC 全有 TC；公开面与注册表可被命令验证；QA 通过；release 等人确认

## User Intent

开始 Lake B：新库立项；迁移已冻结需求并实现；用 beacon-goal / v0.0.1 顺序交付到可验收。

## User Intent Snapshot

```yaml
lake_or_ocean: 湖
this_lake: Lake B
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: lakes
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
source_repo: selfmedia-creator
source_feature: prism-canon-v1@R3
feature: prism-extract-v1
version: v0.0.1
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-B01 | prompt | must | AC-EXTRACT-001 | covered |
| INT-B02 | migrated | must | AC-EXTRACT-002 | covered |
| INT-B03 | migrated | must | AC-EXTRACT-003 | covered |
| INT-B04 | migrated | must | AC-EXTRACT-004 | covered |
| INT-B05 | migrated | must | AC-EXTRACT-005 | covered |
| INT-B06 | migrated | must | AC-EXTRACT-006 | covered |
| INT-B07 | migrated | must | AC-EXTRACT-007 | covered |
| INT-B08 | migrated | must | AC-EXTRACT-008 | covered |
| INT-B09 | prompt | must | AC-EXTRACT-009 | covered |
| INT-B10 | migrated | must | AC-EXTRACT-010 | covered |
| INT-B11 | sea | must | Lake D form chains | deferred |
| INT-B12 | sea | should | Lake C campaign schema | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-EXTRACT-001 | Prism 仓独立于 selfmedia-creator；源仓只作提取源 |
| FP-EXTRACT-002 | 公开面严格 1+6；adapter 不可见 |
| FP-EXTRACT-003 | Lake B 交付提取壳与索引，不假装生产链已完成 |
| FP-EXTRACT-004 | 继承 Lake A FP-PRISM-001…013；冲突时以本仓 constitution 投影 + change 为准 |
| FP-EXTRACT-005 | 公开发布仍须人工批准 |

## 用户旅程 / 故事

US-EXTRACT-001：维护者开独立 Prism 仓，用 beacon init v0.0.1 立项。  
US-EXTRACT-002：迁入 Lake A 宪法与 Inventory，写成 constitution + adapter-index。  
US-EXTRACT-003：安装 7 个公开面 SKILL.md，人对人只见 prism-*。  
US-EXTRACT-004：编排内核从 production-pipeline references 迁入 `_internal/orchestration`。  
US-EXTRACT-005：QA 用文件存在性与注册表一致性验证；release 等人确认。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| PrismRepo | repo_root | 独立 git 仓 |
| PublicSurface | public_id | goal+六能力 |
| AdapterMap | map_id | 源 skill → 落点 |
| SkillContract | contract_id | 七段模板 |
| HumanCard | card_id | 人类面+机器面 |

## Domain FSM（提取落地）

状态：planned → repo_bootstrapped → constitution_migrated → surfaces_installed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| repo_bootstrapped | planned | git_repo_and_beacon_v001 |
| constitution_migrated | repo_bootstrapped | constitution_files_present |
| surfaces_installed | constitution_migrated | seven_public_skills_present |
| indexed | surfaces_installed | registry_and_adapters_present |
| qa_pass | indexed | all_tc_pass |
| release_candidate | qa_pass | evidence_complete |
| human_accepted | release_candidate | human_confirmed |

## Illegal transitions

- planned → surfaces_installed（跳过建仓）
- indexed → human_accepted（跳过 QA）
- 宣称 Lake D 完成
- adapter 顶层暴露为公开 skill

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| planned | bootstrap | git+beacon init | repo_bootstrapped | write README/AGENTS |
| repo_bootstrapped | migrate | constitution copied | constitution_migrated | write constitution |
| constitution_migrated | install_surfaces | 7 SKILL.md | surfaces_installed | write public shells |
| surfaces_installed | index | registries present | indexed | write adapter index |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 独立仓立项（AC-EXTRACT-001）
2. 宪法迁入（AC-EXTRACT-002）
3. 1+6 公开面壳（AC-EXTRACT-003）
4. 注册表（AC-EXTRACT-004）
5. 七段契约模板（AC-EXTRACT-005）
6. 人类卡（AC-EXTRACT-006）
7. 编排内核（AC-EXTRACT-007）
8. Adapter 索引（AC-EXTRACT-008）
9. 源溯源（AC-EXTRACT-009）
10. Non-goals / 分湖边界（AC-EXTRACT-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-B01 | form producer chains | accepted | Lake D |
| DL-B02 | campaign/storyworld schema | accepted | Lake C |
| DL-B03 | metrics/learning loop | accepted | Lake E |
| DL-B04 | monetization contracts | accepted | Lake F |
| DL-B05 | 全量 skill 正文搬迁 | accepted | Lake D 加深；本湖索引+壳 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-EXTRACT-001 | PrismRepo 独立 git 仓 create 完成并进入 `repo_bootstrapped`；含 README/AGENTS；路径不在 selfmedia-creator 内 |
| AC-EXTRACT-002 | 进入 `constitution_migrated`：`docs/beacon/v0.0.1/constitution/prism-constitution.md` 与 Lake A truth 快照存在 |
| AC-EXTRACT-003 | 进入 `surfaces_installed`：恰好 7 个公开面 `skills/prism-*/SKILL.md`（goal+intel+master+director+produce+qa+release） |
| AC-EXTRACT-004 | PublicSurface 注册表 `registry/public-surface.yaml` 声明 Scheme A，且 `max_public_harnesses: 6`（支撑 `surfaces_installed`） |
| AC-EXTRACT-005 | SkillContract 七段模板 `contracts/skill-contract-7seg.tpl.md` 存在（支撑 `indexed`） |
| AC-EXTRACT-006 | HumanCard `contracts/human-card.md` 含人类面三节与机器面（支撑 `indexed`） |
| AC-EXTRACT-007 | 进入 `indexed` 前编排内核就绪：`_internal/orchestration` 含 skill-routing / quality-gates / creation-mode-map / pipeline-contract |
| AC-EXTRACT-008 | AdapterMap `registry/adapter-index.yaml` 覆盖 MAP-001…009 且 adapters 无顶层 SKILL.md；illegal：adapter 顶层暴露为公开 skill |
| AC-EXTRACT-009 | 溯源指向 selfmedia-creator `prism-canon-v1` R3 / program-manifest（`constitution_migrated` 证据） |
| AC-EXTRACT-010 | Non-goals 排除 Lake C/D；illegal：宣称 Lake D 完成 / 跳过 `qa_pass` 直接 `human_accepted`；不得宣称海 closure |

## Non-goals

- 不实现八形态生产链脚本
- 不落 campaign/storyworld schema
- 不复制 Beacon 编码能力
- 不自动公开发布
- 不把 Lake B 宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
