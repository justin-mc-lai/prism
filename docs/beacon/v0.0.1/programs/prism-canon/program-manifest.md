---
program_slug: prism-canon
version: v0.0.1
plan_mode: interactive
scope_mode: phased_lake
lake_or_ocean: 湖
this_lake: Lake C
sea_promise: full_selfmedia_creation_capability
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
public_id: goal
repos:
  - prism（本仓）
  - selfmedia-creator（源仓）
  - beacon（设计理念对照；advisory only）
intent_one_liner: Lake C — campaign / storyworld / master content schema 落地
created_at: "2026-08-11"
plan_revision: R1-rebuild
journey_freeze: US-SCHEMA-001..003
prior_lake_feature: prism-extract-v1
current_lake_feature: prism-campaign-schema-v1
source_freeze: selfmedia-creator prism-canon-v1@R3
source_deferral: DL-002
---

# Program Manifest — prism-canon（Prism 仓 · Lake C）

## Intent

在 Lake B 独立仓基础上，落地 campaign / storyworld / master 内容 schema 文件契约与目录布局，支撑 US-PRISM-002 连载与 canon 车道；深化 MAP-004。

## In（Lake C）

1. `registry/content-schema.yaml` 注册表
2. `contracts/*.schema.yaml` 五类内容对象契约
3. `content/masters/`、`content/storyworlds/`、`content/distribution/` scaffold
4. Canon gate 钩子与 illegal transitions
5. MAP-004 master-freeze-checklist
6. `scripts/check_content_schema.sh` 校验

## Out

- Lake D form producer chains
- Lake E metrics / learning loop
- Lake F monetization
- vendor_pin 全量搬迁

## Lake B status（已完成）

- **release_accepted** @ v0.0.1 / prism-extract-v1 R1

## Lake C delivery

- status: re_plan_done_then_freeze
- feature: prism-campaign-schema-v1 @ v0.0.1 R1
- worktree: .beacon/worktrees/v0.0.1/prism-campaign-schema-v1
- branch: beacon/v0.0.1/prism-campaign-schema-v1

## Lake C 重拆（pln-program · 2026-08-11）

planner-review 发现 main 树四件套被占位草稿覆盖、machine 投影与磁盘哈希全部 DRIFT，且 plan 层
`plan_journey_decomposition_incomplete`。本次按用户批准的顺序重做：

1. **意图重拆**：Lake C 只落 campaign / storyworld / master 内容 schema 与路径契约，支撑
   US-PRISM-002 连载旅程与 canon 车道；不实现生产链（DL-C01）、metrics（DL-C02）、monetization（DL-C03）。
2. **旅程冻结**：`docs/beacon/v0.0.1/user-story/prism-campaign-schema-v1.md` 冻结
   US-SCHEMA-001（连载旅程）、US-SCHEMA-002（master/storyworld 维护）、US-SCHEMA-003（campaign/binding 登记）。
3. **四件套重建**：从 delivery worktree 的权威全量包（truth/tests/tasks/evidence）回写 main，
   替换占位草稿；truth 含 INT-C01…13、FSM 五元组、illegal、DL-C01…07。
4. **后续门**：Truth Review Gate → freeze → implement（worktree 已有实现，补齐证据）→ QA → release 人工门。
