---
slug: prism-review-loop-v1
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
  prd: docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-review-loop-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-review-loop-v1/tests.md
provenance:
  - ac_id: AC-RVL-001
    source_type: migrated_truth
    source_ref: "Lake A US-PRISM-002 goal 复盘 / INT-P15 系列圣经更新"
  - ac_id: AC-RVL-002
    source_type: source_evidence
    source_ref: "creation-mode-map 系列圣经（bible 复盘段）"
---

# Requirement Truth: prism-review-loop-v1（v0.0.1 · Lake E3）

## 人话

E1/E2 有了发布事件和指标快照。E3 定义**战役复盘闭环**：按周期把战役/连载的表现数据、发现、
下一步行动整理成复盘记录，经人工批准后写回系列圣经（bible 复盘段）。复盘必须引用数据
（不空谈），只更新 bible/复盘段，不改已冻结母稿事实。

- 能做：`contracts/review-loop.contract.md`；`registry/review-adapters.yaml`；creation-mode-map
  系列圣经引用；exec 校验脚本。
- 不能做：学习记忆（E4）；monetization（F）；自动改写母稿；自动公开。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake E：落战役复盘 + 系列圣经更新闭环。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake E3（review loop）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes E1..E4
source_deferral: DL-004 / INT-P15
feature: prism-review-loop-v1
version: v0.0.1
depends_on: prism-metrics-snapshot-v1（E2）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-RV01 | migrated | must | AC-RVL-001 | covered |
| INT-RV02 | migrated | must | AC-RVL-002 | covered |
| INT-RV03 | migrated | must | AC-RVL-003 | covered |
| INT-RV04 | migrated | must | AC-RVL-004 | covered |
| INT-RV05 | migrated | must | AC-RVL-005 | covered |
| INT-RV06 | migrated | must | AC-RVL-006 | covered |
| INT-RV07 | migrated | must | AC-RVL-007 | covered |
| INT-RV08 | migrated | must | AC-RVL-008 | covered |
| INT-RV09 | migrated | must | AC-RVL-009 | covered |
| INT-RV10 | migrated | must | AC-RVL-010 | covered |
| INT-RV11 | sea | should | E4 学习记忆 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-RVL-001 | 复盘必须引用发布事件/指标快照；不空谈 |
| FP-RVL-002 | 复盘结论/圣经更新必须人工批准后才写入 |
| FP-RVL-003 | 只更新 bible 复盘段；不改已冻结母稿事实/正典 |
| FP-RVL-004 | maker≠checker：复盘记录与 QA 分离 |
| FP-RVL-005 | bridge 缺工具 fail-closed |
| FP-RVL-006 | 继承 FP-PRISM-002/006/013 |

## 用户旅程 / 故事

US-RVL-001（= US-PRISM-002 复盘段）：连载周期结束 → 收集 E1/E2 数据 → 按
`review-loop.contract` 生成复盘（发现 + 行动）→ 人工批准 → 写回系列圣经复盘段 →
goal 复盘 loop 关闭。

US-RVL-002：无数据复盘被拒。缺 metrics_refs → blocked，不空谈。

US-RVL-003：圣经更新边界。复盘只写 bible 复盘段；母稿事实/正典不动。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| ReviewRecord | review_id | campaign_id + period + metrics_refs + findings + actions |
| SeriesBible | bible | 复盘段写入目标（人工批准后） |
| MetricRef | snapshot_id | 引用 E2 快照 |

## Domain FSM（E3 落地）

状态：rvl_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | rvl_planned | review-loop.contract present |
| registry_landed | contract_landed | review-adapters.yaml ≥3 |
| routing_landed | registry_landed | creation-mode-map 系列圣经引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- rvl_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 无 metrics_refs 仍写复盘
- 未经人工批准写回 bible
- 复盘改写母稿事实/正典
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| rvl_planned | land_contract | contract present | contract_landed | write review-loop.contract |
| contract_landed | register_adapters | ≥3 entries | registry_landed | write review-adapters.yaml |
| registry_landed | wire_routing | bible refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 复盘契约（AC-RVL-001）
2. adapter 登记（AC-RVL-002）
3. 人工批准入库（AC-RVL-003）
4. 系列圣经路由（AC-RVL-004）
5. exec 脚本（AC-RVL-005）
6. 数据驱动（AC-RVL-006）
7. 圣经更新边界（AC-RVL-007）
8. maker≠checker（AC-RVL-008）
9. bridge fail-closed（AC-RVL-009）
10. Non-goals / deferral（AC-RVL-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-RV01 | 学习记忆 | accepted | E4 |
| DL-RV02 | monetization | accepted | Lake F |
| DL-RV03 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-RVL-001 | 进入 `contract_landed`：`contracts/review-loop.contract.md` 定义 review_id/campaign_id/period/metrics_refs/findings/actions/evidence 与 fail-closed |
| AC-RVL-002 | 进入 `registry_landed`：`registry/review-adapters.yaml` 登记 ≥3 个复盘工具 bridge（bible updater / retro template / findings store） |
| AC-RVL-003 | 人工批准：复盘结论/圣经更新必须人工确认后才写入 |
| AC-RVL-004 | 进入 `routing_landed`：creation-mode-map 系列圣经复盘段引用 review-loop.contract |
| AC-RVL-005 | 进入 `indexed`：`scripts/check_review_loop.sh` exec-layer 校验 PASS |
| AC-RVL-006 | 数据驱动：无 metrics_refs 的复盘 blocked，不空谈 |
| AC-RVL-007 | 圣经更新边界：只更新 bible 复盘段，不改已冻结母稿事实 |
| AC-RVL-008 | maker≠checker：复盘记录与 QA 分离，证据引用 |
| AC-RVL-009 | bridge fail-closed：工具缺失 → blocked + reason_code |
| AC-RVL-010 | Non-goals：E4、monetization 显式排除；不得宣称海 closure |

## Non-goals

- 不做学习记忆（E4）
- 不变现/改编合同（Lake F）
- 不自动改写母稿事实/正典
- 不自动公开

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
