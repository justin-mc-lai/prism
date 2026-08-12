---
slug: prism-monetization-contracts-v1
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
  prd: docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-monetization-contracts-v1/tests.md
provenance:
  - ac_id: AC-MON-001
    source_type: migrated_truth
    source_ref: "Lake A INT-P16 / DL-005 变现合同"
  - ac_id: AC-MON-002
    source_type: user_intent
    source_ref: "utterance 2026-08-12：开始 Lake F 并跑完可交付"
---

# Requirement Truth: prism-monetization-contracts-v1（v0.0.1 · Lake F1）

## 人话

Lake F 第一块：**变现契约层**。把品牌合作、广告位、付费内容、带货等变现方式落成文件级契约：
每条 deal 带 deal_id、类型、条款、披露义务与证据；变现承诺必须人工批准；health/legal/finance
风险内容变现前必须过合规门；不编造收入/合作；收款与合同敏感信息受管不入库。

- 能做：`contracts/monetization.contract.md`；`registry/monetization-adapters.yaml`；
  creation-mode-map 变现引用；exec 校验脚本。
- 不能做：改编契约（F2）；平台支付 API；自动承诺合作；自动公开。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

开始 Lake F：先落变现契约，再改编契约，完成 A–F 全湖。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake F1（monetization contracts）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes F1..F2
source_deferral: DL-005 / INT-P16
feature: prism-monetization-contracts-v1
version: v0.0.1
depends_on: B/C/D/E 内容与发布链
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-MO01 | migrated | must | AC-MON-001 | covered |
| INT-MO02 | migrated | must | AC-MON-002 | covered |
| INT-MO03 | migrated | must | AC-MON-003 | covered |
| INT-MO04 | migrated | must | AC-MON-004 | covered |
| INT-MO05 | migrated | must | AC-MON-005 | covered |
| INT-MO06 | migrated | must | AC-MON-006 | covered |
| INT-MO07 | migrated | must | AC-MON-007 | covered |
| INT-MO08 | migrated | must | AC-MON-008 | covered |
| INT-MO09 | migrated | must | AC-MON-009 | covered |
| INT-MO10 | migrated | must | AC-MON-010 | covered |
| INT-MO11 | sea | optional | F2 改编契约 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-MON-001 | 变现承诺必须人工批准 + evidence（approval_recorded） |
| FP-MON-002 | 不编造收入/合作；缺证据 blocked |
| FP-MON-003 | 广告/赞助必须披露标注（内容合规） |
| FP-MON-004 | health/legal/finance 风险内容：变现前必须过合规门 |
| FP-MON-005 | 收款/合同敏感信息受管，禁止入库 |
| FP-MON-006 | 继承 FP-PRISM-002/005/013 |

## 用户旅程 / 故事

US-MON-001：品牌合作意向 → 按 `monetization.contract` 登记 deal（类型/条款/披露）→
人工批准 → 内容标注广告/赞助 → 发布。

US-MON-002：风险内容变现被拒。health/legal/finance 未过合规门 → blocked，不承诺。

US-MON-003：收款信息。走受管 secrets，禁止入库。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| MonetizationDeal | deal_id | type + terms + disclosure + evidence |
| ComplianceGate | gate | 风险内容变现合规门 |
| DisclosureNote | note | 广告/赞助标注 |

## Domain FSM（F1 落地）

状态：mon_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | mon_planned | monetization.contract present |
| registry_landed | contract_landed | monetization-adapters.yaml ≥3 |
| routing_landed | registry_landed | creation-mode-map 变现引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- mon_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 未人工批准承诺变现
- 编造收入/合作
- 风险内容未过合规门仍变现
- 收款/合同信息入库
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| mon_planned | land_contract | contract present | contract_landed | write monetization.contract |
| contract_landed | register_adapters | ≥3 entries | registry_landed | write monetization-adapters.yaml |
| registry_landed | wire_routing | refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 变现契约（AC-MON-001）
2. adapter 登记（AC-MON-002）
3. 人工批准（AC-MON-003）
4. 路由引用（AC-MON-004）
5. exec 脚本（AC-MON-005）
6. 不编造收入（AC-MON-006）
7. 披露义务（AC-MON-007）
8. 风险合规门（AC-MON-008）
9. 敏感信息保护（AC-MON-009）
10. Non-goals / deferral（AC-MON-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-MO01 | 改编契约 | accepted | F2 |
| DL-MO02 | 平台支付 API | accepted | 跨仓/凭证门 |
| DL-MO03 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-MON-001 | 进入 `contract_landed`：`contracts/monetization.contract.md` 定义 deal_id/type/terms/disclosure/evidence 与 fail-closed |
| AC-MON-002 | 进入 `registry_landed`：`registry/monetization-adapters.yaml` 登记 ≥3 个变现工具 bridge（deal-record / compliance-check / disclosure-template） |
| AC-MON-003 | 人工批准：变现承诺必须 human approval + evidence 才生效 |
| AC-MON-004 | 进入 `routing_landed`：creation-mode-map 变现引用 monetization.contract |
| AC-MON-005 | 进入 `indexed`：`scripts/check_monetization.sh` exec-layer 校验 PASS |
| AC-MON-006 | 不编造收入/合作：缺证据 blocked |
| AC-MON-007 | 披露义务：广告/赞助必须标注 |
| AC-MON-008 | 风险合规门：health/legal/finance 未过合规不得变现 |
| AC-MON-009 | 敏感信息保护：收款/合同信息受管，禁止入库 |
| AC-MON-010 | Non-goals：改编契约、平台支付 API 显式排除；不得宣称海 closure |

## Non-goals

- 不做改编契约（F2）
- 不接平台支付 API
- 不自动承诺合作；不自动公开
- 不把 F1 宣称为变现闭环完成（F2 未做）

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
