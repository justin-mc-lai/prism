---
slug: prism-campaign-schema-v1
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
  prd: docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-campaign-schema-v1/tests.md
provenance:
  - ac_id: AC-SCHEMA-001
    source_type: migrated_truth
    source_ref: "Lake A DL-002 / AC-PRISM-008 campaign 机制级定义"
  - ac_id: AC-SCHEMA-003
    source_type: migrated_truth
    source_ref: "Lake A AC-PRISM-009 正典门禁；FP-PRISM-003 OOC fail-closed"
  - ac_id: AC-SCHEMA-009
    source_type: user_intent
    source_ref: "utterance 2026-08-11: 同意继续 Lake C freeze package"
---

# Requirement Truth: prism-campaign-schema-v1（v0.0.1 · Lake C）

## 人话

Lake B 已把 Prism 独立仓、公开面壳和 adapter 索引搭好；本湖要把 **campaign / storyworld / master 内容 schema** 落成可验证的文件契约与目录布局，支撑 US-PRISM-002 连载旅程与 canon 车道。只做正典/连载容器与 schema 注册，不实现八形态生产链，不做指标回流，不宣称海 closure。

- 能做：schema 注册表；`content/masters/`、`content/storyworlds/`、`content/distribution/campaigns|bindings/` 布局契约；Campaign / StoryWorld / NarrativeEpisode / MasterContent 字段规范；canon gate 钩子；加深 MAP-004 master 冻结清单；示例 scaffold + 校验脚本
- 不能做：form producer chains（Lake D）；metrics/learning loop（Lake E）；monetization（Lake F）；全量 vendor 搬迁；分发 API 自动化；把 schema 冻结宣称为完整创作能力已交付
- 怎样算完：四件套填满；AC 全有 TC；schema 可被命令验证；truth review + freeze 通过；再进入 implement → QA → release

## User Intent

继续 Lake C：在独立 Prism 仓落地 campaign / storyworld schema（DL-002），深化 MAP-004，为连载/正典容器提供文件级真值。

## User Intent Snapshot

```yaml
lake_or_ocean: 湖
this_lake: Lake C
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: lakes
prior_lake: Lake B release_accepted
feature: prism-campaign-schema-v1
version: v0.0.1
source_deferral: DL-002
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-C01 | migrated | must | AC-SCHEMA-001 | covered |
| INT-C02 | migrated | must | AC-SCHEMA-002 | covered |
| INT-C03 | migrated | must | AC-SCHEMA-003 | covered |
| INT-C04 | migrated | must | AC-SCHEMA-004 | covered |
| INT-C05 | migrated | must | AC-SCHEMA-005 | covered |
| INT-C06 | migrated | must | AC-SCHEMA-006 | covered |
| INT-C07 | migrated | must | AC-SCHEMA-007 | covered |
| INT-C08 | migrated | must | AC-SCHEMA-008 | covered |
| INT-C09 | migrated | should | AC-SCHEMA-009 | covered |
| INT-C10 | migrated | must | AC-SCHEMA-010 | covered |
| INT-C11 | sea | must | Lake D form producers | deferred |
| INT-C12 | sea | should | Lake E metrics loop | deferred |
| INT-C13 | sea | optional | Lake F monetization | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-SCHEMA-001 | 继承 Lake A FP-PRISM-001…013；母稿是语义/正典权威，展示变体只能转译 |
| FP-SCHEMA-002 | Campaign 是营销/连载战役根对象，可派生多个 Master；不替代 Master 正典 |
| FP-SCHEMA-003 | StoryWorld 承载 bible / canon ledger / 角色 / 时间线；StoryMaster episode 未过 canon gate 不得进入 generated |
| FP-SCHEMA-004 | schema 文件是 canonical 内容对象真值；renders / publications / metrics 仍是投影 |
| FP-SCHEMA-005 | Lake C 只落契约与 scaffold，不实现 producer 脚本与平台 API |
| FP-SCHEMA-006 | 公开发布仍须人工批准；schema 不得绕过 human-approved-publish |

## 用户旅程 / 故事

US-SCHEMA-001（= US-PRISM-002）：用户要连载小说或漫画。prism-goal/campaign 定连载计划 → prism-master 冻结 StoryMaster → prism-director 出 episode 大纲或分镜 → prism-produce 产章节 → prism-qa 过正典/连续性门 → prism-release → 连载发布。（本湖只冻 schema 与路径，不执行生产链。）

US-SCHEMA-002：维护者为 FactMaster 与 StoryMaster 在 `content/masters/` 建立统一 meta + MASTER 契约，StoryWorld 在 `content/storyworlds/` 挂接 canon ledger。

US-SCHEMA-003：战役负责人在 `content/distribution/campaigns/` 登记 campaign_id、lane、master 列表与排期意图，bindings 连接 presentation × endpoint。

## Domain Model

| Entity | Key | Precedence / Requires |
|--------|-----|------------------------|
| Campaign | campaign_id | 营销/连载战役根；`lane`；`master_refs[]`；可选 `world_slug` |
| MasterContent | master_id | `kind: fact\|story`；路径 `content/masters/{vertical}/{slug}/` |
| StoryWorld | world_slug | bible / canon ledger / 角色 / 时间线 |
| NarrativeEpisode | episode_id | 属于 StoryWorld；引用 `master_id`；`canon_gate_status` |
| DistributionBinding | binding_id | campaign × presentation × endpoint |
| SchemaRegistry | schema_id | 本湖契约版本索引 |

## Domain FSM（schema 落地）

状态：schema_planned → registry_indexed → layout_contracts_written → scaffold_present → canon_hooks_bound → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| registry_indexed | schema_planned | `registry/content-schema.yaml` present |
| layout_contracts_written | registry_indexed | master/storyworld/campaign/episode/binding contracts |
| scaffold_present | layout_contracts_written | example dirs + README under `content/` |
| canon_hooks_bound | scaffold_present | canon gate fields + illegal transitions in contracts |
| indexed | canon_hooks_bound | MAP-004 deepen + source-architecture updated |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- schema_planned → scaffold_present（跳过 registry 与 contracts）
- canon_hooks_bound → qa_pass（跳过 indexed / MAP-004）
- StoryMaster episode `canon_gate_status: review_required` → content_state `generated`（illegal）
- lane=canon 使用 `fast_lane_skip`（illegal）
- indexed → human_accepted（跳过 QA）
- 宣称 Lake D 形态生产链已完成
- 宣称 metrics 回流系统已交付（Lake E）
- schema 冻结即海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| schema_planned | index_registry | registry yaml valid | registry_indexed | write content-schema.yaml |
| registry_indexed | write_contracts | all contract files | layout_contracts_written | write contracts/*.schema.yaml |
| layout_contracts_written | scaffold | examples present | scaffold_present | write content/**/README + samples |
| scaffold_present | bind_canon | canon fields in episode + storyworld | canon_hooks_bound | update contracts + orchestration refs |
| canon_hooks_bound | deepen_map004 | checklist + adapter index | indexed | update MAP-004 distill targets |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. Schema 注册表（AC-SCHEMA-001）
2. MasterContent 布局（AC-SCHEMA-002）
3. StoryWorld 布局（AC-SCHEMA-003）
4. Campaign 契约（AC-SCHEMA-004）
5. NarrativeEpisode 契约（AC-SCHEMA-005）
6. DistributionBinding 契约（AC-SCHEMA-006）
7. Canon FSM 钩子（AC-SCHEMA-007）
8. MAP-004 加深（AC-SCHEMA-008）
9. US-PRISM-002 / loop-campaign 路径对齐（AC-SCHEMA-009）
10. Non-goals / 分湖边界（AC-SCHEMA-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-C01 | form producer chains | accepted | Lake D |
| DL-C02 | metrics / learning loop | accepted | Lake E |
| DL-C03 | monetization contracts | accepted | Lake F |
| DL-C04 | vendor_pin 全量搬迁 | accepted | Lake D+ |
| DL-C05 | 分发 API / selfmedia-sync-ai | accepted | 跨仓 |
| DL-C06 | 三车道路由引擎实现 | accepted | Lake D |
| DL-C07 | 本湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-SCHEMA-001 | 进入 `registry_indexed`：`registry/content-schema.yaml` 登记 master / storyworld / campaign / episode / binding 五类契约及 `schema_version` |
| AC-SCHEMA-002 | 进入 `layout_contracts_written`：`contracts/master-content.schema.yaml` 定义 FactMaster / StoryMaster 的 `content/masters/{vertical}/{slug}/` 必填文件（meta.yaml、MASTER.md）与 `kind` 枚举 |
| AC-SCHEMA-003 | `contracts/storyworld.schema.yaml` 定义 `content/storyworlds/{world_slug}/`（world.yaml、bible.md、canon-ledger.yaml、characters/、timeline/） |
| AC-SCHEMA-004 | `contracts/campaign.schema.yaml` 定义 `content/distribution/campaigns/{campaign_id}.yaml`：campaign_id、lane、objective、master_refs、可选 world_slug、schedule_intent |
| AC-SCHEMA-005 | `contracts/narrative-episode.schema.yaml` 定义 episode_id、world_slug、master_id、sequence、canon_gate_status（`review_required` / `passed` / `failed`） |
| AC-SCHEMA-006 | `contracts/distribution-binding.schema.yaml` 定义 binding_id、campaign_id、presentation_id、endpoint_ref；与 pipeline-contract 路径一致 |
| AC-SCHEMA-007 | Canon 钩子：contracts 与 `skills/_internal/orchestration/pipeline-contract.md` 声明 illegal：episode 未过 canon gate → generated；canon lane 禁用 fast_lane_skip |
| AC-SCHEMA-008 | MAP-004 加深：`contracts/master-freeze-checklist.md` 存在；`registry/adapter-migration-matrix.md` MAP-004 行 status 更新为 `distilled_schema` |
| AC-SCHEMA-009 | US-PRISM-002 可追溯：truth 含连载旅程；`skills/prism-goal/references/modes/loop-campaign.md` 引用 `content/distribution/campaigns/` 与 storyworld 路径 |
| AC-SCHEMA-010 | Non-goals 排除 Lake D/E/F；illegal：宣称形态生产链完成 / metrics 系统已交付 / 跳过 qa_pass；不得宣称海 closure |

## Non-goals

- 不实现八形态生产链脚本（blog/vlog/comic/…）
- 不实现指标采集、复盘、系列圣经自动更新（Lake E）
- 不变现/改编合同（Lake F）
- 不 vendor_pin 写作/视频/发布大栈
- 不改 Beacon 编码能力；不自动公开发布
- 不把 Lake C schema 冻结宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
