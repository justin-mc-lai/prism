---
slug: prism-adaptation-contracts-v1
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
  prd: docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-adaptation-contracts-v1/tests.md
provenance:
  - ac_id: AC-ADP-001
    source_type: migrated_truth
    source_ref: "Lake A INT-P16 / DL-005 改编合同"
  - ac_id: AC-ADP-002
    source_type: user_intent
    source_ref: "utterance 2026-08-12：开始 Lake F 并跑完可交付"
---

# Requirement Truth: prism-adaptation-contracts-v1（v0.0.1 · Lake F2）

## 人话

Lake F 收口：**改编契约层**。把小说/漫画/视频等资产的改编授权（漫画、视频、游戏、书籍改编权）
落成文件级契约：adaptation_id、资产引用、授权范围、分成/版权条款、批准与证据。默认只登记契约、
不自动授权；license 边界与人工批准是硬门；敏感合同信息受管不入库。

- 能做：`contracts/adaptation.contract.md`；`registry/adaptation-adapters.yaml`；
  creation-mode-map 改编引用；exec 校验脚本。
- 不能做：平台授权 API；自动授权；自动公开。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

完成 Lake F：落改编契约，完成 A–F 全湖可交付。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake F2（adaptation contracts）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes F1..F2
source_deferral: DL-005 / INT-P16
feature: prism-adaptation-contracts-v1
version: v0.0.1
depends_on: prism-monetization-contracts-v1（F1）· StoryWorld/canon（C/D4）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-AD01 | migrated | must | AC-ADP-001 | covered |
| INT-AD02 | migrated | must | AC-ADP-002 | covered |
| INT-AD03 | migrated | must | AC-ADP-003 | covered |
| INT-AD04 | migrated | must | AC-ADP-004 | covered |
| INT-AD05 | migrated | must | AC-ADP-005 | covered |
| INT-AD06 | migrated | must | AC-ADP-006 | covered |
| INT-AD07 | migrated | must | AC-ADP-007 | covered |
| INT-AD08 | migrated | must | AC-ADP-008 | covered |
| INT-AD09 | migrated | must | AC-ADP-009 | covered |
| INT-AD10 | migrated | must | AC-ADP-010 | covered |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-ADP-001 | 改编授权必须人工批准 + evidence；默认只登记不授权 |
| FP-ADP-002 | 改编不得破坏母稿正典；授权范围/条款必须明确 |
| FP-ADP-003 | 不编造授权/分成；缺证据 blocked |
| FP-ADP-004 | license 边界：第三方 IP/风格改写安全，未获权不自动授权 |
| FP-ADP-005 | 合同敏感信息受管，禁止入库 |
| FP-ADP-006 | 继承 FP-PRISM-002/003/005/013 |

## 用户旅程 / 故事

US-ADP-001：小说/漫画资产收到改编意向 → 按 `adaptation.contract` 登记授权（范围/条款/分成）→
人工批准 → 才可谈改编。

US-ADP-002：未获权自动授权被拒。缺 approval/evidence → blocked，不自动授权。

US-ADP-003：合同信息。走受管 secrets，禁止入库。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| AdaptationDeal | adaptation_id | asset_ref + type + rights + royalty + approval |
| LicenseBoundary | license | 第三方 IP 边界 |
| RoyaltyTerm | royalty | 分成/版权条款 |

## Domain FSM（F2 落地）

状态：adp_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | adp_planned | adaptation.contract present |
| registry_landed | contract_landed | adaptation-adapters.yaml ≥3 |
| routing_landed | registry_landed | creation-mode-map 改编引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- adp_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 未人工批准自动授权
- 编造授权/分成
- 改编破坏母稿正典
- 合同信息入库
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| adp_planned | land_contract | contract present | contract_landed | write adaptation.contract |
| contract_landed | register_adapters | ≥3 entries | registry_landed | write adaptation-adapters.yaml |
| registry_landed | wire_routing | refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 改编契约（AC-ADP-001）
2. adapter 登记（AC-ADP-002）
3. 人工批准/默认不授权（AC-ADP-003）
4. 路由引用（AC-ADP-004）
5. exec 脚本（AC-ADP-005）
6. 不编造授权/分成（AC-ADP-006）
7. 正典保护（AC-ADP-007）
8. license 边界（AC-ADP-008）
9. 敏感信息保护（AC-ADP-009）
10. Non-goals / deferral（AC-ADP-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-AD01 | 平台授权 API | accepted | 跨仓/凭证门 |
| DL-AD02 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-ADP-001 | 进入 `contract_landed`：`contracts/adaptation.contract.md` 定义 adaptation_id/asset_ref/type/rights/royalty/approval/evidence 与 fail-closed |
| AC-ADP-002 | 进入 `registry_landed`：`registry/adaptation-adapters.yaml` 登记 ≥3 个改编工具 bridge（rights-record / royalty-calc / license-check） |
| AC-ADP-003 | 人工批准：改编授权必须 approval + evidence；默认只登记不授权 |
| AC-ADP-004 | 进入 `routing_landed`：creation-mode-map 改编引用 adaptation.contract |
| AC-ADP-005 | 进入 `indexed`：`scripts/check_adaptation.sh` exec-layer 校验 PASS |
| AC-ADP-006 | 不编造授权/分成：缺证据 blocked |
| AC-ADP-007 | 正典保护：改编不得破坏母稿正典（引用 canon ledger） |
| AC-ADP-008 | license 边界：第三方 IP 未获权不自动授权 |
| AC-ADP-009 | 敏感信息保护：合同信息受管，禁止入库 |
| AC-ADP-010 | Non-goals：平台授权 API 显式排除；不得宣称海 closure |

## Non-goals

- 不接平台授权 API
- 不自动授权；不自动公开
- 不把 F2 单独宣称为海 closure（全湖交付仍以版本级 release 确认为准）

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
