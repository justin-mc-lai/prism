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
```

## Acceptance Criteria

### AC-RLO-001 live_drama 接线
form-live-drama.contract.md：intake director 分镜交付须含资产身份条目引用；
gate 新增资产一致性门判据（shot-list/edit-list 引用可解析 + 边界匹配），fail-closed。
- 验证：rg 断言（TC-RLO-001）

### AC-RLO-002 comic 接线
form-av.contract.md：intake storyboard/shot list 须带 asset_ref 解析要求；
gate 对 comic 多集路由新增资产一致性判据。
- 验证：rg 断言（TC-RLO-002）

### AC-RLO-003 registry 两链更新
live_drama 与 comic producer_chain 各插入资产一致性门步骤，YAML 可解析。
- 验证：python yaml 断言（TC-RLO-003）

### AC-RLO-004 exec 校验扩展
check_asset_consistency.sh 增加 rollout 断言且整体 PASS。
- 验证：执行（TC-RLO-004）

## Non-goals

- vlog / book_video 不接入（超出 asset-consistency.contract §1 适用面声明）
- 不修改 manga_drama 已冻结接线；不改两形态 FSM 与既有五类/合规门语义
- 不 pin 任何上游运行时；不做发布自动化

## Illegal transitions

- 分镜引用无法解析到资产条目仍进入剪辑/生成 → illegal
- 宣称本 rollout 改变了门的判断框架 → illegal（只扩适用面）
