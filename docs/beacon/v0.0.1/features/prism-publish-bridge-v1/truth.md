---
slug: prism-publish-bridge-v1
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
  prd: docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-publish-bridge-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-publish-bridge-v1/tests.md
provenance:
  - ac_id: AC-PUB-001
    source_type: migrated_truth
    source_ref: "Lake A MAP-008 · publish-content/schedule-post/x-publish"
  - ac_id: AC-PUB-002
    source_type: user_intent
    source_ref: "utterance 2026-08-12：Lake D6 publish bridge；公开发布人工门"
---

# Requirement Truth: prism-publish-bridge-v1（v0.0.1 · Lake D6）

## 人话

D6 是 Lake D 的收口子湖：把**发布/排期桥**定下来。Prism 只负责草稿与排期意图，公开发布永远
必须人工二次批准；桥接现有发布工具（publish-content / schedule-post / x-publish / manage-media），
平台凭证与密钥禁止进仓库；误传目标（tab/平台）必须标记 `superseded-misrouted` +
`do_not_publish`。D1–D5 的产出从这里走向草稿，但绝不自动公开。

- 能做：`contracts/publish-bridge.contract.md`；`registry/publish-adapters.yaml`；路由引用；exec 校验脚本。
- 不能做：metrics（E）、monetization（F）、vendor sync-ai、自动公开。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

完成 Lake D：发布/排期桥 + 人工批准集成，让八形态产出可安全到达“草稿”，公开仍留人工门。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D6（publish bridge）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-publish-bridge-v1
version: v0.0.1
depends_on: D1–D5 形态产出
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-P01 | migrated | must | AC-PUB-001 | covered |
| INT-P02 | migrated | must | AC-PUB-002 | covered |
| INT-P03 | migrated | must | AC-PUB-003 | covered |
| INT-P04 | migrated | must | AC-PUB-004 | covered |
| INT-P05 | migrated | must | AC-PUB-005 | covered |
| INT-P06 | migrated | must | AC-PUB-006 | covered |
| INT-P07 | migrated | must | AC-PUB-007 | covered |
| INT-P08 | migrated | must | AC-PUB-008 | covered |
| INT-P09 | migrated | must | AC-PUB-009 | covered |
| INT-P10 | migrated | must | AC-PUB-010 | covered |
| INT-P11 | sea | should | Lake E metrics 回流 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-PUB-001 | Prism 只创建草稿/排期意图；公开发布必须人工二次批准（FP-PRISM-005） |
| FP-PUB-002 | 平台凭证/密钥禁止进仓库（protected path） |
| FP-PUB-003 | 误传目标必须标记 superseded-misrouted + do_not_publish |
| FP-PUB-004 | bridge 缺工具 fail-closed，不假装发布 |
| FP-PUB-005 | 发布证据（draft_id/URL）必须记录；无证据不算已发布 |
| FP-PUB-006 | 继承 FP-PRISM-002/004/013；不吞 vendor sync-ai |

## 用户旅程 / 故事

US-PUB-001：形态产出成稿 → prism-release 按 `publish-bridge.contract` 创建平台草稿 →
人类在平台预览 → 人工再次明确批准 → 才真正发布。

US-PUB-002：误传目标。检测到草稿进入错误 tab/平台 → 标记 superseded-misrouted +
do_not_publish，重新走正确通道。

US-PUB-003：排期。用户给时间 → bridge schedule-post 生成排期意图；公开仍人工确认。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| PublishBridgeContract | publish-bridge | 草稿/排期/发布边界 |
| PublishAdapterMap | map | 平台工具 bridge 登记 |
| DraftRecord | draft_id | 平台草稿证据 |
| PublicationRecord | publication_id | 真发布证据（人工批准后） |

## Domain FSM（D6 落地）

状态：publish_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | publish_planned | publish-bridge.contract present |
| registry_landed | contract_landed | publish-adapters.yaml ≥4 bridge |
| routing_landed | registry_landed | creation-mode-map 引用 publish-bridge |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- publish_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 无人工二次批准直接公开
- 凭证/密钥入库
- bridge 缺失仍“发布”
- 误传目标未标记 do_not_publish
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| publish_planned | land_contract | contract present | contract_landed | write publish-bridge.contract |
| contract_landed | register_adapters | ≥4 bridges | registry_landed | write publish-adapters.yaml |
| registry_landed | wire_routing | route refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. publish-bridge 契约（AC-PUB-001）
2. adapter 登记（AC-PUB-002）
3. 草稿-only + 人工门（AC-PUB-003）
4. 误路由守卫（AC-PUB-004）
5. exec 脚本（AC-PUB-005）
6. 路由引用（AC-PUB-006）
7. bridge fail-closed（AC-PUB-007）
8. 凭证保护（AC-PUB-008）
9. 发布证据（AC-PUB-009）
10. Non-goals / deferral（AC-PUB-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-P01 | metrics/learning loop | accepted | Lake E |
| DL-P02 | monetization/改编合同 | accepted | Lake F |
| DL-P03 | vendor sync-ai 分发 API 全量 | accepted | 跨仓；bridge 不吞 |
| DL-P04 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-PUB-001 | 进入 `contract_landed`：`contracts/publish-bridge.contract.md` 定义 bridge 路由、草稿-only 边界、人工二次批准、证据记录 |
| AC-PUB-002 | 进入 `registry_landed`：`registry/publish-adapters.yaml` 登记 ≥4 个 bridge（publish-content / schedule-post / x-publish / manage-media） |
| AC-PUB-003 | 草稿-only：契约声明只创建草稿/排期意图；公开必须人工二次批准 |
| AC-PUB-004 | 误路由守卫：误传目标 → superseded-misrouted + do_not_publish |
| AC-PUB-005 | 进入 `indexed`：`scripts/check_publish_bridge.sh` exec-layer 校验 PASS |
| AC-PUB-006 | 进入 `routing_landed`：creation-mode-map 引用 publish-bridge.contract |
| AC-PUB-007 | bridge fail-closed：工具缺失 → blocked + reason_code，不假装发布 |
| AC-PUB-008 | 凭证保护：契约声明平台凭证/密钥禁止入库（protected path） |
| AC-PUB-009 | 发布证据：draft_id/URL 必须记录；无证据不算已发布 |
| AC-PUB-010 | Non-goals：metrics、monetization、vendor sync-ai 显式排除；不得宣称海 closure |

## Non-goals

- 不做指标采集/学习回流（Lake E）
- 不变现/改编合同（Lake F）
- 不 vendor sync-ai 分发 API
- 不自动公开发布
- 不把 D1–D6 冻结宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
