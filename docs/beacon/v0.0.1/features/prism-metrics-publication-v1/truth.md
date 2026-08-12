---
slug: prism-metrics-publication-v1
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
  prd: docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-metrics-publication-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-metrics-publication-v1/tests.md
provenance:
  - ac_id: AC-MPUB-001
    source_type: migrated_truth
    source_ref: "Lake A FSM published→measured / FP-PRISM-006 / INT-P15"
  - ac_id: AC-MPUB-002
    source_type: user_intent
    source_ref: "utterance 2026-08-12：开始 Lake E（指标/学习回流）"
---

# Requirement Truth: prism-metrics-publication-v1（v0.0.1 · Lake E1）

## 人话

Lake E 的第一块地基：把 D6 发布桥产生的**发布证据**（draft_id / URL / 平台 / 时间）回流成结构化
事件，作为指标基座。没有发布记录就没有指标（FSM `published → measured` 的守卫）。指标只是投影
（FP-PRISM-006），不编造、不猜。平台统计工具（analyze-data 等）只做 bridge，凭证不入库。

- 能做：`contracts/metrics-publication.contract.md`；`registry/metrics-adapters.yaml`；
  creation-mode-map 回流引用；exec 校验脚本。
- 不能做：指标快照采集（E2）、复盘/圣经更新（E3）、学习记忆（E4）；不编造指标；不吞平台 API 凭证。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

开始 Lake E：先落发布证据回流，再逐步指标快照、复盘、学习。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake E1（publication evidence feedback）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes E1..E4
source_deferral: DL-004 / INT-P15
feature: prism-metrics-publication-v1
version: v0.0.1
depends_on: prism-publish-bridge-v1（D6）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-MP01 | migrated | must | AC-MPUB-001 | covered |
| INT-MP02 | migrated | must | AC-MPUB-002 | covered |
| INT-MP03 | migrated | must | AC-MPUB-003 | covered |
| INT-MP04 | migrated | must | AC-MPUB-004 | covered |
| INT-MP05 | migrated | must | AC-MPUB-005 | covered |
| INT-MP06 | migrated | must | AC-MPUB-006 | covered |
| INT-MP07 | migrated | must | AC-MPUB-007 | covered |
| INT-MP08 | migrated | must | AC-MPUB-008 | covered |
| INT-MP09 | migrated | must | AC-MPUB-009 | covered |
| INT-MP10 | migrated | must | AC-MPUB-010 | covered |
| INT-MP11 | sea | should | E2–E4 回流面 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-MPUB-001 | 无 publication 记录不得进入 measured（FSM 非法转移） |
| FP-MPUB-002 | 指标是投影不是 canonical；发布记录才是回流基座 |
| FP-MPUB-003 | 不编造指标/趋势；缺数据用显式空快照 |
| FP-MPUB-004 | 平台凭证/密钥禁止入库（protected path） |
| FP-MPUB-005 | bridge 缺工具 fail-closed |
| FP-MPUB-006 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-MPUB-001：D6 发布桥创建草稿并获 draft_id → 人工二次批准后平台返回 URL/publication_id →
prism-release 按 `metrics-publication.contract` 写入发布事件 → E2 才能采指标。

US-MPUB-002：无发布记录。任何“指标回流”请求必须 blocked（publication_record_missing），
不猜数据。

US-MPUB-003：新平台接入。只加 metrics-adapters bridge 登记；凭证走受管 secrets。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| PublicationEvent | publication_id | 平台真实发布结果（基座） |
| MetricsAdapterMap | map | 平台统计工具 bridge |
| ArtifactRef | artifact_ref | 关联成稿/战役路径 |

## Domain FSM（E1 落地）

状态：mpub_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | mpub_planned | metrics-publication.contract present |
| registry_landed | contract_landed | metrics-adapters.yaml ≥3 bridge |
| routing_landed | registry_landed | creation-mode-map 回流引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- mpub_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 无 publication 记录进入 measured
- 编造指标/趋势
- 凭证入库
- bridge 缺失仍“回流”
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| mpub_planned | land_contract | contract present | contract_landed | write metrics-publication.contract |
| contract_landed | register_adapters | ≥3 bridges | registry_landed | write metrics-adapters.yaml |
| registry_landed | wire_routing | refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 发布事件契约（AC-MPUB-001）
2. adapter 登记（AC-MPUB-002）
3. FSM measured 守卫（AC-MPUB-003）
4. 路由引用（AC-MPUB-004）
5. exec 脚本（AC-MPUB-005）
6. 不编造指标（AC-MPUB-006）
7. 凭证保护（AC-MPUB-007）
8. bridge fail-closed（AC-MPUB-008）
9. 证据要求（AC-MPUB-009）
10. Non-goals / deferral（AC-MPUB-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-MP01 | 指标快照采集 | accepted | E2 |
| DL-MP02 | 战役复盘/圣经更新 | accepted | E3 |
| DL-MP03 | 学习记忆 | accepted | E4 |
| DL-MP04 | 平台 API 全量自动化 | accepted | 跨仓/凭证门 |
| DL-MP05 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-MPUB-001 | 进入 `contract_landed`：`contracts/metrics-publication.contract.md` 定义发布事件字段（publication_id/platform/url/published_at/artifact_ref/evidence）与 fail-closed |
| AC-MPUB-002 | 进入 `registry_landed`：`registry/metrics-adapters.yaml` 登记 ≥3 个统计 bridge（analyze-data / 平台 stats / 报表工具） |
| AC-MPUB-003 | measured 守卫：契约声明无 publication 记录不得进入 measured（引用 Lake A FSM） |
| AC-MPUB-004 | 进入 `routing_landed`：creation-mode-map 发布/回流引用 metrics-publication.contract |
| AC-MPUB-005 | 进入 `indexed`：`scripts/check_metrics_publication.sh` exec-layer 校验 PASS |
| AC-MPUB-006 | 不编造指标：契约声明缺数据用显式空快照，禁止猜测趋势 |
| AC-MPUB-007 | 凭证保护：平台凭证/密钥禁止入库 |
| AC-MPUB-008 | bridge fail-closed：统计工具缺失 → blocked + reason_code |
| AC-MPUB-009 | 证据要求：事件必须带 publication_id/url/时间，缺证据不算回流 |
| AC-MPUB-010 | Non-goals：E2–E4、平台 API 全量、vendor sync-ai 显式排除；不得宣称海 closure |

## Non-goals

- 不做指标快照采集（E2）、复盘/圣经更新（E3）、学习记忆（E4）
- 不 vendor 平台 API 全量自动化
- 不编造指标；不做 monetization（F）
- 不把 E1 宣称为完整回流闭环已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
