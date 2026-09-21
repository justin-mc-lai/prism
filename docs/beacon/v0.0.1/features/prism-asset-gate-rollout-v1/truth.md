---
slug: prism-asset-gate-rollout-v1
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
  prd: docs/beacon/v0.0.1/features/prism-asset-gate-rollout-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-asset-gate-rollout-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-asset-gate-rollout-v1/tests.md
provenance:
  - ac_id: AC-RLO-001
    source_type: migrated_truth
    source_ref: "prism-manga-asset-gate-v1 R1 §1 适用面声明（live_drama 分镜阶段、comic 多集）；form-live-drama.contract.md / form-av.contract.md 现行结构"
---

# Requirement Truth: prism-asset-gate-rollout-v1（v0.0.1 · 资产一致性门推广）

## 人话

把 manga_drama 已上线的资产一致性门按其适用面声明推到 **live_drama（分镜阶段）** 和
**comic（多集路由）**：实拍短剧的分镜/剪辑清单引用必须能解析到资产条目，多集漫画的
角色/场景跨页一致。规则不变，只是接入面扩大。

- 能做：两个契约 intake+gate 接线；registry 两条 producer_chain 插入门步骤；
  exec 校验脚本扩展断言；truth 四件套。
- 不能做：改两形态既有 FSM/gate 语义；给 vlog/book_video 接入（单集口播，无多镜资产
  连续性问题，超出适用面声明）；上游运行时 pin；发布自动化。
- 怎样算完：AC 全有 TC；exec PASS；make check 绿；implement → QA → release 人工门。

## User Intent

live_drama/comic 接入同一资产一致性门（契约已声明适用面）。

## User Intent Snapshot

```yaml
lake_or_ocean: 湖
this_lake: Lake D 资产一致性门 rollout（2 形态接线）
user_decision: promoted
scope_mode: phased_lake
feature: prism-asset-gate-rollout-v1
version: v0.0.1
depends_on: prism-manga-asset-gate-v1（门契约与判断框架）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-R01 | migrated | must | AC-RLO-001（live_drama 接线） | covered |
| INT-R02 | migrated | must | AC-RLO-002（comic 接线） | covered |
| INT-R03 | migrated | must | AC-RLO-003（registry 两链） | covered |
| INT-R04 | migrated | must | AC-RLO-004（exec 扩展） | covered |
| INT-R05 | sea | must | vlog/book_video 接入 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-RLO-001 | 只扩**适用面**，不改门的判断框架（FP-MAG 系列原样继承） |
| FP-RLO-002 | 分镜引用必须可解析到资产条目；未决项不得流入剪辑/生成（fail-closed） |
| FP-RLO-003 | vlog / book_video 不接入：单集口播无多镜资产连续性问题 |
| FP-RLO-004 | 不改两形态既有 FSM 与既有五类/合规门语义 |
| FP-RLO-005 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-RLO-001：用户要真人短剧。director 出分集剧本 + 分镜/剪辑清单 →
produce 前过资产一致性门（引用可解析 + 边界匹配）→ 合规门 → release。

US-RLO-002：用户要多集漫画。director 出 storyboard + 角色/场景设定 →
comic 多集路由过资产一致性门（三分法 / 边界匹配 / 画风统一）→ QA → release。

US-RLO-003：用户要 vlog。单集口播，无多镜资产连续性问题 → **不接入本门**（显式 Non-goal）。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| AssetConsistencyGate | asset-consistency | 判断框架（继承，不改） |
| LiveDramaContract | form-live-drama | intake + gate 接线点 |
| ComicRoute | form-av（comic） | 多集路由接线点 |
| ProducerChain | form | registry 中的门步骤 |
| RolloutScope | scope | 适用面声明（live_drama / comic） |

## Domain FSM（rollout 落地）

状态：rollout_planned → live_wired → comic_wired → registry_updated → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| live_wired | rollout_planned | form-live-drama 含门引用 |
| comic_wired | live_wired | form-av 含门引用 |
| registry_updated | comic_wired | 两链各含 asset-consistency 步骤 |
| indexed | registry_updated | exec 脚本扩展 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- 分镜引用无法解析到资产条目仍进入剪辑/生成 → illegal
- 宣称本 rollout 改变了门的判断框架 → illegal（只扩适用面）
- 给 vlog / book_video 接入本门 → illegal（超出适用面声明）
- 改两形态既有 FSM 或既有门语义 → illegal
- 上游运行时 pin / 发布自动化 → illegal
- 宣称海 closure → illegal

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| rollout_planned | wire_live | live contract refs present | live_wired | update form-live-drama.contract |
| live_wired | wire_comic | comic route refs present | comic_wired | update form-av.contract |
| comic_wired | update_registry | both chains carry gate step | registry_updated | update form-registry |
| registry_updated | index | exec script + no leak | indexed | extend check_asset_consistency.sh |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. live_drama 契约接线（AC-RLO-001）
2. comic 路由接线（AC-RLO-002）
3. registry 两条 producer_chain（AC-RLO-003）
4. exec 校验扩展（AC-RLO-004）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-R01 | vlog / book_video 接入 | accepted | 单集口播无多镜资产连续性问题 |
| DL-R02 | 改门判断框架 | rejected | 本 rollout 只扩适用面 |
| DL-R03 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-RLO-001 | form-live-drama.contract.md intake 要求分镜交付含资产身份条目引用；gate 新增资产一致性判据（引用可解析 + 边界匹配），fail-closed |
| AC-RLO-002 | form-av.contract.md（comic 路由）intake 要求 storyboard/shot list 带 asset_ref 解析；gate 对多集路由新增资产一致性判据 |
| AC-RLO-003 | live_drama 与 comic 的 producer_chain 各插入资产一致性门步骤；registry YAML 可解析 |
| AC-RLO-004 | `scripts/check_asset_consistency.sh` 增加 rollout 断言且整体 PASS |

## Non-goals

- vlog / book_video 不接入（超出 asset-consistency.contract §1 适用面声明）
- 不修改 manga_drama 已冻结接线；不改两形态 FSM 与既有五类/合规门语义
- 不 pin 任何上游运行时；不做发布自动化

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
