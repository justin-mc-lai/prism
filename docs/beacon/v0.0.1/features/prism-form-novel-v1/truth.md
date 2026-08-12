---
slug: prism-form-novel-v1
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
  prd: docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-novel-v1/tests.md
provenance:
  - ac_id: AC-NVL-001
    source_type: migrated_truth
    source_ref: "Lake A FP-PRISM-003 / AC-PRISM-009 · Lake C narrative-episode contract"
  - ac_id: AC-NVL-002
    source_type: source_evidence
    source_ref: "kushi-narrative-zh / US-PRISM-002 连载旅程"
---

# Requirement Truth: prism-form-novel-v1（v0.0.1 · Lake D4）

## 人话

D4 落地 **novel 连载**形态的生产者契约：长文本按 StoryWorld + canon ledger 组织成 episode，
每集必须过正典门（`canon_gate_status`）才能进入 produced/generated；世界圣经与 canon ledger
高于任何展示变体；OOC/设定漂移按事实错误 fail-closed。长文本叙事桥接 `kushi-narrative-zh`，
正典/连续性判断是 Prism 自己的规则。

- 能做：form-registry 注册 novel；`contracts/form-novel.contract.md`；creation-mode-map novel 行；
  exec 校验脚本。
- 不能做：comic/vlog/book_video（D5）、发布桥（D6）；不 vendor_pin；不做 metrics。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake D：落 novel 连载形态，把 Lake C 的正典门接进生产者契约。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D4（novel form）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-form-novel-v1
version: v0.0.1
depends_on: prism-campaign-schema-v1（Lake C canon/StoryWorld schema）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-N01 | migrated | must | AC-NVL-001 | covered |
| INT-N02 | migrated | must | AC-NVL-002 | covered |
| INT-N03 | migrated | must | AC-NVL-003 | covered |
| INT-N04 | migrated | must | AC-NVL-004 | covered |
| INT-N05 | migrated | must | AC-NVL-005 | covered |
| INT-N06 | migrated | must | AC-NVL-006 | covered |
| INT-N07 | migrated | must | AC-NVL-007 | covered |
| INT-N08 | migrated | must | AC-NVL-008 | covered |
| INT-N09 | migrated | must | AC-NVL-009 | covered |
| INT-N10 | migrated | must | AC-NVL-010 | covered |
| INT-N11 | sea | must | D5/D6 其余形态 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-NVL-001 | StoryMaster 的正典即 truth；OOC/设定漂移按事实错误 fail-closed（FP-PRISM-003） |
| FP-NVL-002 | episode 未过 canon gate（review_required/failed）不得进入 generated |
| FP-NVL-003 | world bible 与 canon ledger 高于展示变体；变体只能转译，不得新增正典 |
| FP-NVL-004 | lane=canon 禁用 fast_lane_skip |
| FP-NVL-005 | bridge kushi-narrative-zh 缺失 fail-closed，不产出假文件 |
| FP-NVL-006 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-NVL-001（= US-PRISM-002）：用户要连载小说。prism-goal/campaign 定连载计划 →
prism-master 冻结 StoryMaster（world bible + canon ledger）→ director 出 episode 大纲 →
produce 按 `form-novel.contract` 产章节（写入 `content/storyworlds/{world}/episodes/`）→
qa 过正典/连续性门（canon_gate_status=passed）→ release。

US-NVL-002：episode 正典未过。produce/qa 明确 blocked（canon_gate_status=review_required/failed），
不进入 generated。

US-NVL-003：新增世界/章节。只加 storyworld/episodes 数据 + registry 注册，不改主链。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| NovelFormContract | form-novel | episode 生产者契约 |
| StoryWorld | world_slug | bible / canon ledger（Lake C 路径） |
| NarrativeEpisode | episode_id | canon_gate_status 门禁 |
| EpisodeDraft | draft | 产出 + 正典证据 |

## Domain FSM（D4 落地）

状态：novel_planned → forms_registered → novel_contract_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| forms_registered | novel_planned | form-registry 含 novel |
| novel_contract_landed | forms_registered | form-novel.contract present |
| routing_landed | novel_contract_landed | creation-mode-map novel 行 present |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- novel_planned → routing_landed（跳过注册/契约）
- indexed → human_accepted（跳过 QA）
- episode `canon_gate_status=review_required|failed` → generated
- lane=canon 使用 fast_lane_skip
- OOC/设定漂移仍放行
- bridge 缺失仍产出
- 宣称 Lake D 全部完成

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| novel_planned | register_form | novel in registry | forms_registered | update form-registry |
| forms_registered | land_contract | novel contract present | novel_contract_landed | write form-novel.contract |
| novel_contract_landed | wire_routing | novel row present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. form registry novel（AC-NVL-001）
2. novel 契约（AC-NVL-002）
3. canon 钩子（AC-NVL-003）
4. 路由引用（AC-NVL-004）
5. exec 脚本（AC-NVL-005）
6. bridge fail-closed（AC-NVL-006）
7. StoryWorld/canon ledger 引用（AC-NVL-007）
8. maker≠checker（AC-NVL-008）
9. OOC/连续性门（AC-NVL-009）
10. Non-goals / deferral（AC-NVL-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-N01 | comic/vlog/book_video 本体 | accepted | D5 |
| DL-N02 | publish/schedule 桥 | accepted | D6 |
| DL-N03 | vendor_pin 外部大栈 | accepted | license review + ATTRIBUTION |
| DL-N04 | metrics/learning loop | accepted | Lake E |
| DL-N05 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-NVL-001 | 进入 `forms_registered`：form-registry 登记 novel，含 contract 引用与生产链 |
| AC-NVL-002 | 进入 `novel_contract_landed`：`contracts/form-novel.contract.md` 定义 StoryMaster 输入、episode 结构、输出路径（content/storyworlds/{world}/episodes/）、证据与 fail-closed |
| AC-NVL-003 | canon 钩子：契约声明 episode `canon_gate_status=review_required|failed` 不得进入 generated；canon 禁用 fast_lane_skip |
| AC-NVL-004 | 进入 `routing_landed`：creation-mode-map 新增 novel 行，引用 form-novel.contract 与 canon 门 |
| AC-NVL-005 | 进入 `indexed`：`scripts/check_novel_form.sh` exec-layer 校验 PASS |
| AC-NVL-006 | bridge fail-closed：kushi-narrative-zh 缺失 → blocked + reason_code |
| AC-NVL-007 | StoryWorld 引用：契约引用 `content/storyworlds/{world_slug}/`（bible/canon-ledger）路径 |
| AC-NVL-008 | maker≠checker：novel 契约与 anti-slop-gate/正典 QA 分离，证据可引用 |
| AC-NVL-009 | OOC/连续性门：契约声明设定漂移/OOC 按事实错误 fail-closed |
| AC-NVL-010 | Non-goals：D5/D6、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure |

## Non-goals

- 不实现 comic/vlog/book_video（D5）、发布桥（D6）
- 不 vendor_pin 外部叙事/写作大栈
- 不做 metrics（E）/ monetization（F）
- 不接平台 API
- 不把 D1–D4 宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
