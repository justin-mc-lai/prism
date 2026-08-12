---
slug: prism-metrics-snapshot-v1
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
  prd: docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/tests.md
provenance:
  - ac_id: AC-MSNAP-001
    source_type: migrated_truth
    source_ref: "Lake A MetricsSnapshot / FSM published→measured"
  - ac_id: AC-MSNAP-002
    source_type: source_evidence
    source_ref: "analyze-data 平台统计（views/interactions/followers）"
---

# Requirement Truth: prism-metrics-snapshot-v1（v0.0.1 · Lake E2）

## 人话

E1 把发布证据回流成基座。E2 在其上定义**指标快照**（MetricsSnapshot）：某篇发布内容在某个时间点的
平台指标（阅读/互动/粉丝等），必须带 publication_ref、采集时间和来源证据。没有发布记录就没有快照
（FSM `published → measured` 守卫）；缺数据用显式空快照，不编造。

- 能做：`contracts/metrics-snapshot.contract.md`；`registry/metrics-adapters.yaml` 快照条目；
  creation-mode-map 快照引用；exec 校验脚本。
- 不能做：复盘/圣经更新（E3）、学习记忆（E4）；不编造指标；不吞凭证。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake E：落 MetricsSnapshot 指标快照契约与采集门。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake E2（metrics snapshot）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes E1..E4
source_deferral: DL-004 / INT-P15
feature: prism-metrics-snapshot-v1
version: v0.0.1
depends_on: prism-metrics-publication-v1（E1）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-MS01 | migrated | must | AC-MSNAP-001 | covered |
| INT-MS02 | migrated | must | AC-MSNAP-002 | covered |
| INT-MS03 | migrated | must | AC-MSNAP-003 | covered |
| INT-MS04 | migrated | must | AC-MSNAP-004 | covered |
| INT-MS05 | migrated | must | AC-MSNAP-005 | covered |
| INT-MS06 | migrated | must | AC-MSNAP-006 | covered |
| INT-MS07 | migrated | must | AC-MSNAP-007 | covered |
| INT-MS08 | migrated | must | AC-MSNAP-008 | covered |
| INT-MS09 | migrated | must | AC-MSNAP-009 | covered |
| INT-MS10 | migrated | must | AC-MSNAP-010 | covered |
| INT-MS11 | sea | should | E3/E4 回流面 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-MSNAP-001 | 快照必须绑定 publication_ref；无发布记录不得 measured |
| FP-MSNAP-002 | 指标是投影；快照带 collected_at 与来源证据 |
| FP-MSNAP-003 | 缺数据用显式空快照；不编造指标/趋势 |
| FP-MSNAP-004 | 凭证/密钥禁止入库 |
| FP-MSNAP-005 | bridge 缺工具 fail-closed |
| FP-MSNAP-006 | 继承 FP-PRISM-006/013 |

## 用户旅程 / 故事

US-MSNAP-001：E1 发布事件存在 → 按 `metrics-snapshot.contract` 采集某时间点指标 →
写入 `content/publications/.../metrics/` 快照 → E3 才能复盘。

US-MSNAP-002：无发布记录或平台无数据。返回显式空快照或 blocked，不猜。

US-MSNAP-003：新增指标源。只加 metrics-adapters 登记；凭证走受管 secrets。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| MetricsSnapshot | snapshot_id | publication_ref + collected_at + 指标字段 |
| PublicationRef | publication_id | 绑定 E1 发布事件 |
| MetricField | views/interactions/followers | 平台真实值或显式空 |

## Domain FSM（E2 落地）

状态：msnap_planned → contract_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | msnap_planned | metrics-snapshot.contract present |
| registry_landed | contract_landed | registry 含快照条目 |
| routing_landed | registry_landed | creation-mode-map 快照引用 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- msnap_planned → routing_landed（跳过契约/登记）
- indexed → human_accepted（跳过 QA）
- 无 publication_ref 生成快照
- 编造指标/趋势
- 凭证入库
- bridge 缺失仍“采集”
- 宣称海 closure

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| msnap_planned | land_contract | contract present | contract_landed | write metrics-snapshot.contract |
| contract_landed | register_adapters | snapshot entries | registry_landed | update metrics-adapters.yaml |
| registry_landed | wire_routing | refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 快照契约（AC-MSNAP-001）
2. adapter 登记（AC-MSNAP-002）
3. FSM measured 守卫（AC-MSNAP-003）
4. 路由引用（AC-MSNAP-004）
5. exec 脚本（AC-MSNAP-005）
6. 空快照/不编造（AC-MSNAP-006）
7. 凭证保护（AC-MSNAP-007）
8. bridge fail-closed（AC-MSNAP-008）
9. 证据要求（AC-MSNAP-009）
10. Non-goals / deferral（AC-MSNAP-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-MS01 | 战役复盘/圣经更新 | accepted | E3 |
| DL-MS02 | 学习记忆 | accepted | E4 |
| DL-MS03 | 平台 API 全量自动化 | accepted | 跨仓/凭证门 |
| DL-MS04 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-MSNAP-001 | 进入 `contract_landed`：`contracts/metrics-snapshot.contract.md` 定义 snapshot_id/publication_ref/指标字段/collected_at/来源证据 与 fail-closed |
| AC-MSNAP-002 | 进入 `registry_landed`：`registry/metrics-adapters.yaml` 含 ≥2 个快照采集 bridge 条目 |
| AC-MSNAP-003 | measured 守卫：无 publication_ref 不得生成快照（引用 E1 发布事件） |
| AC-MSNAP-004 | 进入 `routing_landed`：creation-mode-map 快照/measured 引用 metrics-snapshot.contract |
| AC-MSNAP-005 | 进入 `indexed`：`scripts/check_metrics_snapshot.sh` exec-layer 校验 PASS |
| AC-MSNAP-006 | 空快照/不编造：缺数据用显式空快照，禁止猜测 |
| AC-MSNAP-007 | 凭证保护：平台凭证/密钥禁止入库 |
| AC-MSNAP-008 | bridge fail-closed：统计工具缺失 → blocked + reason_code |
| AC-MSNAP-009 | 证据要求：快照必须带 collected_at 与来源，缺证据不算采集 |
| AC-MSNAP-010 | Non-goals：E3/E4、平台 API 全量显式排除；不得宣称海 closure |

## Non-goals

- 不做战役复盘/圣经更新（E3）、学习记忆（E4）
- 不 vendor 平台 API 全量自动化
- 不编造指标；不做 monetization（F）

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
