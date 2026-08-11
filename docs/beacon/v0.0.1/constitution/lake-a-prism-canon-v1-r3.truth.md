---
slug: prism-canon-v1
version: v0.0.6
status: frozen
revision_id: R3
language: zh
domain_required: true
ux_required: false
parser_contract: beacon-feature-package-v2
materials_status: current
package_maturity: filled
truth_source_model: intent_first
program_ref: docs/beacon/v0.0.6/programs/prism-canon/program-manifest.md
canonical_refs:
  prd: docs/beacon/v0.0.6/features/prism-canon-v1/truth.md
  user_story: docs/beacon/v0.0.6/features/prism-canon-v1/truth.md
  test_case: docs/beacon/v0.0.6/features/prism-canon-v1/tests.md
provenance:
  - ac_id: AC-PRISM-001
    source_type: user_intent
    source_ref: "utterance: 以上整合成与 beacon 并行的新 agent skill 项目，beacon 管编码规范，这个管内容营销创作规范"
  - ac_id: AC-PRISM-002
    source_type: user_intent
    source_ref: "utterance: 先 $beacon:beacon-truth v0.0.6 进行湖海拆分并冻结"
  - ac_id: AC-PRISM-003
    source_type: design_confirmed
    source_ref: "conversation 2026-08-11: 双母稿模型（FactMaster / StoryMaster）与对象模型确认"
  - ac_id: AC-PRISM-010
    source_type: user_intent
    source_ref: "utterance: 湖海拆分并冻结；Deferral 无未决项"
  - ac_id: AC-PRISM-013
    source_type: user_intent
    source_ref: "utterance: 直接走 beacon change prism-canon-v1 做 R2 refreeze，把 1+6 公开面 + 人类卡契约 + 子 skill 不可见 写进 truth"
  - ac_id: AC-PRISM-016
    source_type: design_confirmed
    source_ref: "conversation 2026-08-11: 两套生命周期与三车道分析确认"
  - ac_id: AC-PRISM-017
    source_type: user_intent
    source_ref: "utterance 2026-08-11: 完整能力是海级承诺、分湖交付"
  - ac_id: AC-PRISM-018
    source_type: user_intent
    source_ref: "utterance 2026-08-11: 从自媒体创作项目提取 skill 统一编排；提取方式独立新仓 Prism"
  - ac_id: AC-PRISM-019
    source_type: user_intent
    source_ref: "utterance 2026-08-11: skill 设计理念对齐 Beacon；能力是完整自媒体内容创作，有导演、编排等"
---

# Requirement Truth: prism-canon-v1（v0.0.6 · R3）

## 人话

从本仓 `selfmedia-creator` 抽出已有内容创作 skill（导演、编排、写作、人话、贴图、视频、漫画、发布等），统一编排进与 Beacon **设计理念对齐**的新 agent skill 项目 **Prism**（棱镜），落地为**独立新仓**。Beacon 管编码规范与工程 truth；Prism 管内容营销创作规范与内容 truth。对齐的是 1+6 公开面、契约、门禁、人类卡、anti-leak——不是 Beacon 的编码能力。

海级承诺：完整的自媒体内容创作能力（选题→母稿→导演→生产→QA→发布→回流）。交付方式：分湖。本湖（Lake A）只冻宪法与提取映射；独立仓与公开面壳在 Lake B；形态生产链在 Lake D；本湖不得宣称海 closure（不宣称本湖 = 全海完工）。

R3 纠正：产品不是「写完宪法文档就算 Prism」；产品是「从本仓提取并编排成可安装的 Prism 内容创作 agent skill」，宪法是 Lake A 的煮干面。

- 能做：冻结 Prism 身份与双轨；冻结双母稿与主链/门禁；冻结 1+6 / 人类卡 / anti-leak / 三车道；冻结本仓 Source Skill Inventory→公开面映射；登记海级完整能力的分湖交付；澄清命名与快道 FSM
- 不能做：本湖不建 Prism 仓、不搬 skill 文件、不实现八形态生产链、不改 Beacon 编码 gate、不吞分发 API
- 怎样算完：四件套填满；Gate A–D 过；R3 refreeze 成功；Deferral 无未决项

## User Intent

从自媒体创作项目提取 skill，统一编排，成立与 Beacon 编码 agent skill 类似的 Prism 内容创作 agent skill；设计理念对齐；能力完整（含导演、编排）；海级承诺、分湖交付；提取进独立新仓。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: 湖
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: lakes
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
source_repo: selfmedia-creator
first_lake: prism-canon-v1
revision: R3
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-P01 | prompt | must | AC-PRISM-001 | covered |
| INT-P02 | prompt | must | AC-PRISM-002 | covered |
| INT-P03 | design | must | AC-PRISM-003 | covered |
| INT-P04 | design | must | AC-PRISM-004, AC-PRISM-021 | covered |
| INT-P05 | design | must | AC-PRISM-005 | covered |
| INT-P06 | design | must | AC-PRISM-006 | covered |
| INT-P07 | design | must | AC-PRISM-007 | covered |
| INT-P08 | design | must | AC-PRISM-008 | covered |
| INT-P09 | design | must | AC-PRISM-009 | covered |
| INT-P10 | prompt | must | AC-PRISM-010 | covered |
| INT-P11 | prompt | must | AC-PRISM-011, AC-PRISM-012 | covered |
| INT-P12 | prompt | must | Lake B: 独立 Prism 仓 + 公开面壳 + 提取落地 | deferred |
| INT-P13 | design | should | Lake C: campaign / storyworld schema 落地 | deferred |
| INT-P14 | prompt | must | Lake D: form producer chains（完整创作能力主体） | deferred |
| INT-P15 | design | should | Lake E: 指标/学习闭环与系列圣经更新 | deferred |
| INT-P16 | vision | optional | Lake F: 变现/改编合同 | deferred |
| INT-P17 | prompt | must | AC-PRISM-013 | covered |
| INT-P18 | prompt | must | AC-PRISM-014 | covered |
| INT-P19 | prompt | must | AC-PRISM-015 | covered |
| INT-P20 | design | must | AC-PRISM-016, AC-PRISM-022 | covered |
| INT-P21 | prompt | must | Lake B: 公开面 SKILL.md 壳与注册表文件 | deferred |
| INT-P22 | prompt | must | AC-PRISM-017 | covered |
| INT-P23 | prompt | must | AC-PRISM-018, AC-PRISM-020 | covered |
| INT-P24 | prompt | must | AC-PRISM-019 | covered |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-PRISM-001 | 内容 truth 与工程 truth 分轨：Prism 不写编码规范，Beacon 不写内容营销规范；交叉问题只能出 advisory，不互相改 truth |
| FP-PRISM-002 | 母稿是语义/正典权威；展示变体只能转译，不得新增事实或正典 |
| FP-PRISM-003 | StoryMaster 的正典即 truth；OOC 或设定漂移按事实错误处理，fail-closed |
| FP-PRISM-004 | maker 与 checker 分离；生成方不得自证合格 |
| FP-PRISM-005 | 公开发布前必须人工批准；skill 只能创建草稿 |
| FP-PRISM-006 | 单真值多投影：canonical 是内容对象与 skill 契约；renders、发布记录、指标是投影 |
| FP-PRISM-007 | 新增形态只改 registry + form contract + 路由表，不改主链与导演骨架 |
| FP-PRISM-008 | 两套生命周期：内容对象走轻量风险分流（快/标准/正典），能力（skill）走严谨版本闭环；Beacon 1+6 是造能力的元流程，不是每篇内容的必走流程 |
| FP-PRISM-009 | 人类面是意图入口，不是流程入口：人只说做什么/要什么，车道与 mode 由 prism-goal 分类，复杂度留在机器面 |
| FP-PRISM-010 | 公开面固定为 1 横切 + 6 能力；子 skill 不带顶层 SKILL.md，只作 adapter，禁止向人暴露内部编排名 |
| FP-PRISM-011 | Prism 能力来自本仓 skill 提取与统一编排，不是从零发明第二套内容管线；提取目标是独立 Prism 仓 |
| FP-PRISM-012 | 与 Beacon 对齐的是设计理念与调用形状；明确不对齐编码/工程能力复制 |
| FP-PRISM-013 | 海级完整创作能力是承诺；分湖是交付节奏；不得把 Lake A 文档冻结伪装成全海能力已交付 |

## 用户旅程 / 故事

US-PRISM-001：用户要一篇 blog。prism-intel 定角度 → prism-master 冻结 FactMaster → prism-director 出 treatment → prism-produce 走 writing/humanize/render → prism-qa 过反 slop 与事实核对 → prism-release 监制 + 人工批准 → 发布 → 指标回流。

US-PRISM-002：用户要连载小说或漫画。prism-goal/campaign 定连载计划 → prism-master 冻结 StoryMaster → prism-director 出 episode 大纲或分镜 → prism-produce 产章节或页面 → prism-qa 过正典/连续性/文字门 → prism-release → 连载发布 → 追读指标回流。

US-PRISM-003：新增形态。只改 registry、form contract、路由表，主链与导演骨架不动。

US-PRISM-004：Beacon 与 Prism 混用。编码/工程问题路由 Beacon，内容创作问题路由 Prism；交叉问题各自 advisory，不互改 truth。

US-PRISM-005：快道内容（日榜/thread）。人只调 prism-goal；lane=fast；intel/master/director 以 `fast_lane_skip` 标注跳过；走 produce → qa → release。

US-PRISM-006：公开面调用。人只说意图；输出人类卡；子 skill 名不出现。

US-PRISM-007：成立 Prism 仓。按本湖 Source Skill Inventory，从 selfmedia-creator 提取编排层与 adapter，装进独立 Prism 仓的 1+6 公开面（Lake B 执行）。

## Prism 公开面注册表（1+6）

对齐 Beacon Scheme A **调用形状**：1 个横切 goal + 恰好 6 个公开能力，禁止第 7 个公开 harness。公开面带顶层 SKILL.md，内部面全部不可见。

| Public id | 人类动词 | 触发 | Beacon 设计别名 | 硬门禁 |
|-----------|----------|------|-----------------|--------|
| prism-goal（横切） | 做/连载 | 长跑战役、系列、复盘 | goal | 长跑才进；不算第 7 面 |
| prism-intel | 选 | 选题/角度/调研 | plan | 不编造趋势与指标 |
| prism-master | 定 | 母稿/正典冻结 | truth | 事实或正典未核完不冻结 |
| prism-director | 导 | treatment/分镜/节奏 | design | 无核心意图不出方案 |
| prism-produce | 产 | 成稿/页面/成片 | implement | 只按已冻结母稿生产 |
| prism-qa | 验 | 检查/过门禁 | qa | maker 不自证；缺证据不过 |
| prism-release | 发 | 草稿/发布 | release | 公开必须人工二次批准 |

## 命名映射（R3）

- **内容人类面真名**：`prism-*`（上表）。
- **Beacon 名**（plan/truth/design/implement/qa/release）：设计别名，用于对照 Beacon 理念与能力生命周期；不对人暴露为 Prism 公开面。
- **对象主链**：SourceSignal → Master → Presentation → Binding → Job → Publication → Metrics。
- 禁止把「写完宪法文档」说成「Prism 已具备完整创作能力」。

## Source Skill Inventory（本仓 → Prism，登记级）

| 本仓来源 | Prism 落点 | 角色 |
|----------|------------|------|
| `skills/selfmedia-production-pipeline` | prism-goal / 编排内核 | 总控编排提取源 |
| `skills/selfmedia-director` | prism-director | 导演 |
| `skills/selfmedia-topic-radar` / `selfmedia-newsnow` / `selfmedia-last30days` / `$qi-dev-intel-radar` | prism-intel adapters | 选题/信息差 |
| `content/masters/**` + MASTER 规范 | prism-master | 母稿/正典 |
| `skills/selfmedia-writing` / `selfmedia-humanize` / `humanizer-zh` / `no-ai-slop` | prism-produce / prism-qa adapters | 写作与人话 |
| `skills/selfmedia-account-pipeline` / 贴图渲染脚本 | prism-produce adapters | 账号落地/贴图 |
| `skills/openmontage` / `comic-storyboard` / rnskill 视频族 | prism-produce adapters | 视频/漫画 |
| `skills/publish-content` / `schedule-post` / sync-ai 桥 | prism-release adapters | 草稿/发布（公开仍要人批） |
| `skills/selfmedia-production-pipeline/references/{creation-mode-map,skill-routing,quality-gates}.md` | 路由表 / 门禁真值 | 编排合同 |

本湖只冻结映射；搬仓与 SKILL.md 壳在 Lake B。

## 两套生命周期与三车道

- 内容生命周期（轻）：快道 `goal → produce → qa → release`（跳过须 `fast_lane_skip` 标注）；标准道 `intel → master → director → produce → qa → release`；正典道 `goal → master → director → produce → qa(正典) → release → goal 复盘`。
- 能力生命周期（重）：Candidate → Contract（七段）→ Implement → Eval → Route → Monitor/Retire。Beacon 1+6 **设计理念**对齐在这里。
- fail-closed 只在不可逆点：事实/合规发布前、正典冻结前、人工批准公开前。

## 人类卡契约

每次公开面调用结束，输出两张面：

- 人类面：状态、产出路径、需要人决定什么、下一步谁接。
- 机器面：mode_id、lane、evidence refs、FSM 迁移、事务记录。

格式：`## 这次做了什么` / `## 需要你决定` / `## 下一步`。

## 子 skill 不可见（anti-leak）

- 只有 7 个公开面携带顶层 SKILL.md。
- 子 skill 是 adapter，只带七段契约，不对外发现。
- 路由表是唯一编排真值。

## Domain Model

| Entity | Key | Precedence / Requires |
|--------|-----|------------------------|
| Campaign | campaign_id | 营销/连载战役根对象；派生多个 Master |
| MasterContent | master_id | FactMaster / StoryMaster |
| StoryWorld | world_slug | bible / canon ledger / 角色 / 时间线 |
| NarrativeEpisode | episode_id | 属于 StoryWorld |
| PresentationVariant | presentation_id | 带 form |
| DistributionBinding | binding_id | presentation × endpoint |
| DistributionJob | job_id | 草稿/发布尝试 |
| Publication | publication_id | 平台真实结果 |
| MetricsSnapshot | snapshot_id | 指标回流 |
| SkillExtractionMap | map_id | 本仓 skill → Prism 公开面/adapter（本湖登记） |

## Domain FSM（内容对象生命周期）

状态轴：`content_state` × `lane`（fast | standard | canon）。

状态集：idea, briefed, directed, generated, qa-needs-fix, qa-pass, supervisor-needs-fix, release-candidate, human-approved-draft, human-approved-image-draft, human-approved-publish, draft-created, scheduled, published, failed, measured

| State | From | Guard |
|-------|------|-------|
| briefed | idea | source_material_present |
| directed | briefed | director_intake_ok |
| generated | directed | presentation_map_present |
| generated | idea | lane=fast AND fast_lane_skip_annotated AND risk_allows_fast |
| qa-pass | generated | gate_evidence_complete |
| qa-needs-fix | generated | gate_failed |
| release-candidate | qa-pass | supervisor_pass |
| supervisor-needs-fix | qa-pass | supervisor_blocked |
| human-approved-draft | release-candidate | approval_recorded |
| human-approved-image-draft | release-candidate | approval_recorded + media_type=image |
| human-approved-publish | release-candidate | approval_recorded |
| draft-created | human-approved-draft / human-approved-image-draft | platform_draft_id |
| scheduled | human-approved-publish | approval_scope_contains_schedule |
| published | human-approved-publish | platform_post_id |
| failed | 任意 job 态 | error_recorded |
| measured | published | publication_record_exists |

## Illegal transitions

- idea → generated（lane≠fast，或缺少 `fast_lane_skip` 标注）
- generated → release-candidate（无 supervisor）
- release-candidate → published（无 human-approved-publish）
- qa-pass → supervisor 自证（maker 兼任 checker）
- published → draft-created / scheduled
- draft-created → published（无新批准）
- published → measured（无 publication 记录）
- StoryMaster episode 未过 canon gate → generated
- 任何公开发布事件在 human-approved-publish 缺失时发生
- lane=canon 走 fast_lane_skip（canon 禁用快道 skip）

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| idea | briefed | source_material_present | briefed | save_briefing |
| idea | fast_lane_skip | lane=fast AND fast_lane_skip_annotated AND risk_allows_fast | generated | annotate_skip_and_route_producer |
| briefed | directed | director_intake_ok | directed | write_treatment |
| directed | generated | presentation_map_present | generated | route_producer |
| generated | qa-pass | gate_evidence_complete | qa-pass | save_gate_evidence |
| generated | qa-needs-fix | gate_failed | qa-needs-fix | attach_findings |
| qa-needs-fix | generated | fix_requested | generated | rework |
| qa-pass | release-candidate | supervisor_pass | release-candidate | write_supervisor_review |
| qa-pass | supervisor-needs-fix | supervisor_blocked | supervisor-needs-fix | attach_blockers |
| supervisor-needs-fix | generated | fix_requested | generated | rework |
| release-candidate | human-approved-draft | approval_recorded | human-approved-draft | create_draft |
| release-candidate | human-approved-image-draft | approval_recorded + media_type=image | human-approved-image-draft | create_image_draft |
| release-candidate | human-approved-publish | approval_recorded | human-approved-publish | schedule_or_publish |
| human-approved-draft | draft-created | platform_draft_id | draft-created | record_publication |
| human-approved-image-draft | draft-created | platform_draft_id | draft-created | record_image_publication |
| human-approved-publish | scheduled | approval_scope_contains_schedule | scheduled | record_job |
| human-approved-publish | published | platform_post_id | published | record_url |
| 任意 job 态 | attempt-failed | error_recorded | failed | record_error |
| published | measured | publication_record_exists | measured | capture_metrics |

**悬空检查：** idea 可走 briefed 或 fast_lane_skip；其余同 R2。

invalid：idea→generated 无快道标注；generated→release-candidate；release-candidate→published 无批准；draft-created→published；published→measured 无记录；canon 用 fast skip；canon gate 未过→generated

```mermaid
stateDiagram-v2
  [*] --> idea
  idea --> briefed: briefed
  idea --> generated: fast_lane_skip
  briefed --> directed: directed
  directed --> generated: generated
  generated --> qa-pass: qa-pass
  generated --> qa-needs-fix: qa-needs-fix
  qa-needs-fix --> generated: fix_requested
  qa-pass --> release-candidate: supervisor_pass
  qa-pass --> supervisor-needs-fix: supervisor_blocked
  supervisor-needs-fix --> generated: fix_requested
  release-candidate --> human-approved-draft: approval_recorded
  release-candidate --> human-approved-image-draft: approval_recorded
  release-candidate --> human-approved-publish: approval_recorded
  human-approved-draft --> draft-created: platform_draft_id
  human-approved-image-draft --> draft-created: platform_draft_id
  human-approved-publish --> scheduled: approval_scope
  human-approved-publish --> published: platform_post_id
  published --> measured: publication_record_exists
```

## Alignment Surface（本湖必煮干）

1. Prism 身份与双轨（AC-PRISM-001）
2. 湖海拆分（AC-PRISM-002, AC-PRISM-010）
3. 双母稿（AC-PRISM-003）
4. 主链与命名映射（AC-PRISM-004, AC-PRISM-021）
5. 七道门禁（AC-PRISM-005）
6. skill 契约七段（AC-PRISM-006）
7. form contract 八形态登记（AC-PRISM-007）
8. campaign 机制（AC-PRISM-008）
9. 正典门禁概念（AC-PRISM-009）
10. 包形状与 TC（AC-PRISM-011, AC-PRISM-012）
11. 1+6 / 人类卡 / anti-leak / 三车道（AC-PRISM-013–016）
12. 海级完整能力分湖承诺（AC-PRISM-017）
13. 独立仓提取方式 + Source Skill Inventory（AC-PRISM-018, AC-PRISM-020）
14. Beacon 仅设计理念对齐（AC-PRISM-019）
15. 快道 FSM 合法化（AC-PRISM-022）

## Phased Backlog（后续湖 · 海级承诺的分湖面）

| Lake | 内容 | 海承诺角色 |
|------|------|------------|
| Lake B | **独立 Prism 仓**：从本仓提取公开面壳、契约模板、编排内核、adapter 索引 | 提取落地（must） |
| Lake C | campaign / storyworld schema | 正典/连载容器 |
| Lake D | form producer chains（blog/贴图/vlog/thread/novel/comic/book_video） | 完整创作能力主体（must） |
| Lake E | 指标/学习闭环 | 回流增强 |
| Lake F | 变现/改编合同 | 可选边界 |

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-001 | 独立 Prism 仓落地（含提取搬迁） | accepted | 海 must；本湖冻映射；Lake B 执行 |
| DL-002 | campaign / storyworld schema 文件 | accepted | Lake C |
| DL-003 | form producer chains 实现 | accepted | 海 must；Lake D |
| DL-004 | 指标/学习闭环 | accepted | Lake E |
| DL-005 | 变现/改编合同 | accepted | Lake F |
| DL-006 | 分发自动化与多平台 API | accepted | 跨仓 selfmedia-sync-ai，不并入本湖 |
| DL-007 | 修改 Beacon 编码规范 / 复制编码能力 | rejected | 只对齐设计理念 |
| DL-008 | Prism 公开面 SKILL.md 壳与注册表文件 | accepted | Lake B |
| DL-009 | 三车道路由引擎实现 | accepted | Lake D |
| DL-010 | 本湖假装全海能力已交付 | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-PRISM-001 | 定义 Prism（棱镜）与 Beacon 并行；Beacon=编码/工程 truth，Prism=内容营销创作规范/内容 truth |
| AC-PRISM-002 | 本湖为海级整合 Lake A，只冻宪法与提取映射；Phased Backlog 列 Lake B–F；不宣称全海 closure |
| AC-PRISM-003 | 冻结双母稿：FactMaster 与 StoryMaster；共用 SourceSignal→…→Metrics 对象主链 |
| AC-PRISM-004 | 冻结内容主链六公开能力阶段：intel→master→director→produce→qa→release，后接 metrics；skill 为 adapter，不得新增主 stage |
| AC-PRISM-005 | 冻结七道门禁：证据、导演、反 slop、视觉、平台、监制、人工；缺证据默认不过 |
| AC-PRISM-006 | 冻结 skill 契约七段：identity / 决策边界 / intake / output contract / gate / handoff / 失败处理 |
| AC-PRISM-007 | 冻结 form contract 四问 + 八形态登记（登记≠实现） |
| AC-PRISM-008 | 冻结 campaign 机制级定义；本湖不落 schema |
| AC-PRISM-009 | 冻结正典门禁概念；OOC/设定漂移 fail-closed |
| AC-PRISM-010 | 湖海拆分文件化；research promoted；Deferral 无未决项 |
| AC-PRISM-011 | beacon-feature-package-v2 四件套 + L0 + Intent + 旅程 + FSM 五元组 + illegal + Non-goals |
| AC-PRISM-012 | 每 AC≥1 TC；含≥1 exec-layer TC；tasks 带 ac= 与 evidence= |
| AC-PRISM-013 | 冻结 1+6 公开面；禁止第 7 公开 harness |
| AC-PRISM-014 | 冻结人类卡契约（人类面+机器面） |
| AC-PRISM-015 | 冻结子 skill 不可见；路由表唯一编排真值 |
| AC-PRISM-016 | 冻结两套生命周期与三车道 |
| AC-PRISM-017 | 冻结海级承诺：完整自媒体内容创作能力；交付=分湖；本湖不得宣称海 closure |
| AC-PRISM-018 | 冻结提取方式：从 selfmedia-creator 提取/编排 skill，目标独立新仓 Prism；本湖不建仓 |
| AC-PRISM-019 | 冻结 Beacon 对齐范围：仅设计理念与调用形状；明确不对齐编码能力 |
| AC-PRISM-020 | 冻结 Source Skill Inventory（本仓→Prism 公开面/adapter）登记表 |
| AC-PRISM-021 | 冻结命名映射：人类面真名 prism-*；Beacon 名为设计别名 |
| AC-PRISM-022 | 冻结快道 FSM：`fast_lane_skip` 合法；未标注的 idea→generated 仍 illegal；canon 禁用快道 skip |

## Non-goals

- 本湖不创建 Prism git 仓库、不搬迁 skill 文件
- 本湖不实现八形态生产链脚本
- 本湖不落 campaign/storyworld schema 文件
- 本湖不改 Beacon 编码规范，不复制 Beacon 编码能力
- 本湖不改 selfmedia-sync-ai 分发实现
- 本湖不做指标采集/复盘系统、不变现合同
- 本湖不把文档冻结宣称为完整创作能力已交付

## Freeze readiness（文档层）

- [x] L0 人话（R3 按纠正意图重写）
- [x] Intent Coverage Matrix：must covered 或 deferred+accepted
- [x] Domain FSM：含快道轴与 fast_lane_skip
- [x] tests.md 覆盖 AC-PRISM-017–022（TC-PRISM-023–028）
- [x] Deferral Ledger 无未决项
- [x] Truth Review Gate（R3：`review_gate_pass=true`，A–D 全过）
- [x] R3：海级分湖、独立仓提取、设计理念对齐、Source Inventory、命名映射、快道 FSM
