---
program_slug: prism-canon
version: v0.0.1
plan_mode: interactive
scope_mode: phased_lake
lake_or_ocean: 湖
this_lake: Lake F
sea_promise: full_selfmedia_creation_capability
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
public_id: goal
repos:
  - prism（本仓）
  - selfmedia-creator（源仓）
  - beacon（设计理念对照；advisory only）
intent_one_liner: Lake F — 变现/改编契约（F1 变现 → F2 改编；海承诺最后一湖）
created_at: "2026-08-11"
plan_revision: F1-plan
journey_freeze: US-SCHEMA-001..003
prior_lake_features:
  - prism-extract-v1
  - prism-campaign-schema-v1
  - prism-form-writing-v1
  - prism-form-blog-thread-v1
  - prism-form-image-post-v1
  - prism-form-novel-v1
  - prism-form-av-v1
  - prism-publish-bridge-v1
  - prism-metrics-publication-v1
  - prism-metrics-snapshot-v1
  - prism-review-loop-v1
  - prism-learning-memory-v1
current_lake_feature: prism-monetization-contracts-v1
source_freeze: selfmedia-creator prism-canon-v1@R3
source_deferral: DL-005
---

# Program Manifest — prism-canon（Prism 仓 · Lake D）

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

- status: qa_passed_release_candidate
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

## Lake C 交付状态（2026-08-11 晚）

- truth：R5 frozen（含实现证据 reconciliation；baseline `sha256:75836a09…`）
- implement：15/15 TC pass（`scripts/check_content_schema.sh` exec-layer PASS）
- QA：`run-20260811T232406916560` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- release：人工门待确认（不自动公开发布）

## Lake D（2026-08-12 规划）

pln-program 已完成八形态拆分：D1 writing 基础链 → D2 blog/thread → D3 贴图/xhs → D4 novel →
D5 comic/vlog/book_video → D6 publish bridge。详见 `programs/prism-canon/lake-d-plan.md`。
当前进入 D1（`prism-form-writing-v1`）truth → freeze → implement → QA。

## Lake D1 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_writing_adapters.sh` exec PASS）
- QA：`run-20260812T084228065759` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：D2（`prism-form-blog-thread-v1`）待启动；release 人工门待确认

## Lake D2 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_blog_thread_forms.sh` exec PASS）
- QA：`run-20260812T084947791269` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：D3（`prism-form-image-post-v1`）待启动

## Lake D3 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_image_post_forms.sh` exec PASS）
- QA：`run-20260812T085444996257` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：D4（`prism-form-novel-v1`）待启动

## Lake D4 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_novel_form.sh` exec PASS）
- QA：`run-20260812T085911329188` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：D5（`prism-form-av-v1`）待启动

## Lake D5 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_av_forms.sh` exec PASS）
- QA：`run-20260812T090408217552` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：D6（`prism-publish-bridge-v1`）待启动

## Lake D6 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_publish_bridge.sh` exec PASS）
- QA：`run-20260812T090820139073` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`

## Lake D 总状态（2026-08-12）

- D1–D6 全部 truth→freeze→implement→QA 完成，`release_ready=true`（各 release 人工门待确认）
- 八形态生产链契约已注册：blog / thread / image-post / xhs / novel / comic / vlog / book_video + publish bridge
- 仍未做：Lake E metrics 回流、Lake F monetization、vendor sync-ai、公开发布人工确认
- 不得宣称海 closure

## 版本级 Release（2026-08-12 人工确认）

- `release_accepted`：12 features（B/C/D1–D6/E1–E4）全部 QA 通过并合入 main
- 证据：`docs/beacon/v0.0.1/release/v0.0.1-release-confirmation.md` + `beacon release scorecard v0.0.1`（release_ready=true）
- 平台公开发布仍逐内容人工门；Lake F（可选）未做，不得宣称海 closure

## Lake E（2026-08-12 规划）

pln-program 拆分完成：E1 发布证据回流 → E2 MetricsSnapshot 指标快照 → E3 战役复盘/圣经更新 →
E4 可回放学习记忆。详见 `programs/prism-canon/lake-e-plan.md`。当前进入 E1（`prism-metrics-publication-v1`）。

## Lake E1 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_metrics_publication.sh` exec PASS）
- QA：`run-20260812T183252827530` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：E2（`prism-metrics-snapshot-v1`）待启动

## Lake E2 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_metrics_snapshot.sh` exec PASS）
- QA：`run-20260812T183837779955` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：E3（`prism-review-loop-v1`）待启动

## Lake E3 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_review_loop.sh` exec PASS）
- QA：`run-20260812T184310318974` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`
- 下一子湖：E4（`prism-learning-memory-v1`）待启动

## Lake E4 交付状态（2026-08-12）

- truth：R1 frozen · implement：15/15 TC pass（`scripts/check_learning_memory.sh` exec PASS）
- QA：`run-20260812T184654601157` · 10/10 AC · 15/15 scenario · release_confidence 1.0 · `release_ready=true`

## Lake E 总状态（2026-08-12）

- E1–E4 全部 truth→freeze→implement→QA 完成，`release_ready=true`（各 release 人工门待确认）
- 回流闭环已文件化：发布事件 → 指标快照 → 复盘/圣经 → 学习记忆（advisory only）
- 仍未做：Lake F（monetization，可选）、公开发布人工确认；不得宣称海 closure
