---
slug: prism-learning-memory-v1
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
  prd: docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-learning-memory-v1/tests.md
provenance:
  - ac_id: AC-LMEM-001
    source_type: migrated_truth
    source_ref: "Lake A INT-P15 学习闭环 · Beacon learning 边界（可回放/可审计/可裁剪）"
  - ac_id: AC-LMEM-002
    source_type: user_intent
    source_ref: "utterance 2026-08-12：开始 Lake E；E4 学习记忆"
---

# Requirement Truth: prism-learning-memory-v1（v0.0.1 · Lake E4）

## 人话

Lake E 的收口子湖：把复盘后的**学习记忆**落成可回放、可审计、可裁剪的记录。学习只辅助判断
（影响排序/风险 framing），**不定义 truth、不通过 gate、不给 QA/release verdict**；每一条记忆带
来源、时间、置信度、适用边界与回放路径；冲突或过时记忆显式标记并可剪枝。

- 能做：`contracts/learning-memory.contract.md`；`registry/learning-adapters.yaml`；
  creation-mode-map 学习引用；exec 校验脚本。
- 不能做：Lake F monetization；平台 API；learning 写入 requirement truth。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

完成 Lake E：落可回放学习记忆，让复盘结果可持续改善判断，但不越界。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake E4（learning memory）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes E1..E4
source_deferral: DL-004 / INT-P15
feature: prism-learning-memory-v1
version: v0.0.1
depends_on: prism-review-loop-v1（E3）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-LM01 | migrated | must | AC-LMEM-001 | covered |
| INT-LM02 | migrated | must | AC-LMEM-002 | covered |
| INT-LM03 | migrated | must | AC-LMEM-003 | covered |
| INT-LM04 | migrated | must | AC-LMEM-004 | covered |
| INT-LM05 | migrated | must | AC-LMEM-005 | covered |
| INT-LM06 | migrated | must | AC-LMEM-006 | covered |
| INT-LM07 | migrated | must | AC-LMEM-007 | covered |
| INT-LM08 | migrated | must | AC-LMEM-008 | covered |
| INT-LM09 | migrated | must | AC-LMEM-009 | covered |
| INT-LM10 | migrated | must | AC-LMEM-010 | covered |
| INT-LM11 | sea | optional | Lake F monetization | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-LMEM-001 | learning 只辅助判断：不定义 truth、不通 gate、不给 QA/release verdict |
| FP-LMEM-002 | 每条记忆可回放：source_ref + 时间 + 证据路径 |
| FP-LMEM-003 | 可审计：能说明哪些 learning 影响本轮判断 |
| FP-LMEM-004 | 可裁剪：冲突/过时记忆显式标记并可 prune |
| FP-LMEM-005 | bridge 缺工具 fail-closed |
| FP-LMEM-006 | 继承 FP-PRISM-006/013 |

## 用户旅程 / 故事

US-LMEM-001：E3 复盘产出发现 → 按 `learning-memory.contract` 写入记忆（来源/时间/置信度/适用边界）
→ 后续 intel/plan 可回放引用（advisory）。

US-LMEM-002：冲突记忆。两条记忆互相矛盾 → 显式 conflict 标记，不静默合并。

US-LMEM-003：记忆过期/无用 → prune 规则裁剪，保留审计痕迹。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| LearningMemory | memory_id | source_ref + claim + confidence + applicability |
| RecallRef | ref | 回放路径（证据） |
| PruneRecord | prune_id | 裁剪痕迹 |

## Domain FSM（E4 落地）

状态：lmem_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | lmem_planned | learning-memory.contract present |
| registry_landed | contract_landed | learning-adapters.yaml ≥3 |
| routing_landed | registry_landed | creation-mode-map 学习引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- lmem_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- learning 写入 requirement truth / 给出 gate verdict
- 记忆无 source_ref/时间
- 冲突记忆静默合并
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| lmem_planned | land_contract | contract present | contract_landed | write learning-memory.contract |
| contract_landed | register_adapters | ≥3 entries | registry_landed | write learning-adapters.yaml |
| registry_landed | wire_routing | refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 学习记忆契约（AC-LMEM-001）
2. adapter 登记（AC-LMEM-002）
3. advisory-only 边界（AC-LMEM-003）
4. 路由引用（AC-LMEM-004）
5. exec 脚本（AC-LMEM-005）
6. 可回放/可审计（AC-LMEM-006）
7. 可裁剪/冲突标记（AC-LMEM-007）
8. 不替代 QA/release（AC-LMEM-008）
9. bridge fail-closed（AC-LMEM-009）
10. Non-goals / deferral（AC-LMEM-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-LM01 | monetization | accepted | Lake F |
| DL-LM02 | 平台 API 全量 | accepted | 跨仓/凭证门 |
| DL-LM03 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-LMEM-001 | 进入 `contract_landed`：`contracts/learning-memory.contract.md` 定义 memory_id/source_ref/claim/confidence/applicability/evidence |
| AC-LMEM-002 | 进入 `registry_landed`：`registry/learning-adapters.yaml` 登记 ≥3 个学习工具 bridge（memory-store / recall / prune） |
| AC-LMEM-003 | advisory-only：契约声明 learning 不定义 truth、不通 gate、不给 QA/release verdict |
| AC-LMEM-004 | 进入 `routing_landed`：creation-mode-map 学习引用 learning-memory.contract |
| AC-LMEM-005 | 进入 `indexed`：`scripts/check_learning_memory.sh` exec-layer 校验 PASS |
| AC-LMEM-006 | 可回放/可审计：每条记忆带 source_ref + 时间 + 回放路径 |
| AC-LMEM-007 | 可裁剪：冲突/过时记忆显式标记，prune 保留审计痕迹 |
| AC-LMEM-008 | 边界：learning 不替代 QA/release 判定 |
| AC-LMEM-009 | bridge fail-closed：工具缺失 → blocked + reason_code |
| AC-LMEM-010 | Non-goals：Lake F、平台 API 显式排除；不得宣称海 closure |

## Non-goals

- 不变现/改编合同（Lake F）
- 不接平台 API 全量
- learning 不写入 requirement truth；不替代 QA/release
- 不把 E1–E4 宣称为海级完整能力已交付（Lake F 未做）

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
