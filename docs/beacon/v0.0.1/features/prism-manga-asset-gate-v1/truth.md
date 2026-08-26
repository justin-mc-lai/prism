---
slug: prism-manga-asset-gate-v1
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
  prd: docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/tests.md
provenance:
  - ac_id: AC-MAG-001
    source_type: source_evidence
    source_ref: "vendor/skills/drama-skills/skills/short-drama-assets（MIT）SKILL.md + references/{continuity-delta,asset-review-checklist}.md；alibaba/lumenx README 核心能力（本地镜像 oss-sync/automation/auto/lumenx）"
  - ac_id: AC-MAG-004
    source_type: migrated_truth
    source_ref: "registry/form-registry.yaml manga_drama producer_chain（FP-PRISM-007 / ai-manga-drama R1）"
---

# Requirement Truth: prism-manga-asset-gate-v1（v0.0.1 · Lake D 资产一致性门）

## 人话

漫剧分镜里"角色突然换了衣服没人记录""上一镜结束在雨天下一镜悄悄变晴天"这类漂移，
现在有硬门拦：每个画面实体必须归类**身份/变体/镜头瞬态**，引用必须解析到资产条目，
相邻镜头首尾状态逐字段对得上，画风全片锁同一锚点。判断框架从 drama-skills（MIT）
和 lumenx（MIT）蒸馏，只取规则不复制运行时。

- 能做：蒸馏参考落 prism-director/references；`contracts/asset-consistency.contract.md`
  门契约；manga_drama 契约与 registry 生产链接线；exec 校验脚本；MPT/openstory A4 常设决策入册。
- 不能做：pin lumenx/dramaclaw/MPT/openstory 运行时；复制上游正文；替代五类 QA 门
  （本门是加强）；公开发布。
- 怎样算完：AC 全有 TC；exec PASS；make check 绿；implement → QA → release 人工门。

## User Intent

用 lumenx/drama-skills 蒸馏升级 manga_drama producer_chain 的资产一致性门；
MoneyPrinterTurbo/openstory 需要 pin 时按 A4 单独决策。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D（manga_drama 资产一致性门 + 蒸馏层）
user_decision: promoted
```

## Acceptance Criteria

### AC-MAG-001 蒸馏参考落地
`skills/prism-director/references/asset-consistency-gate.md`：三分法、识别锚点、CON-01
边界匹配、CON-04 变化记录、AST-05 binding、画风统一、lumenx 三件套映射，标注双上游出处。
- 验证：rg 断言关键词（TC-MAG-001）

### AC-MAG-002 门契约七节
`contracts/asset-consistency.contract.md` 含 identity/决策边界/intake/output/gate/handoff/
失败处理；fail-closed 码 `asset_identity_missing`；六判据叠加不替代既有门。
- 验证：rg 断言（TC-MAG-002）

### AC-MAG-003 manga_drama 契约接线
form-manga-drama.contract.md intake 要求识别锚点（未决项不得流入分镜），gate 第 2 条升级
引用 asset-consistency 契约。
- 验证：rg 断言（TC-MAG-003）

### AC-MAG-004 registry 生产链更新
manga_drama producer_chain 在 storyboard 校验后插入资产一致性门步骤且 YAML 可解析。
- 验证：python yaml 断言（TC-MAG-004）

### AC-MAG-005 exec 校验脚本
`scripts/check_asset_consistency.sh` 可执行且 PASS。
- 验证：执行（TC-MAG-005）

### AC-MAG-006 上游运行时不 pin
vendor/skills 下不得出现 lumenx、dramaclaw 目录（distill only 边界）。
- 验证：test 反断言（TC-MAG-006）

### AC-MAG-007 MPT/openstory A4 常设决策入册
source-capability-inventory 记录 defer-pin 维持 + 触发条件 + 届时按 A4 逐次 pin。
- 验证：rg 断言（TC-MAG-007）

## Non-goals

- 不 pin lumenx/dramaclaw/MoneyPrinterTurbo/openstory 任何运行时或整包
- 不复制 drama-skills/lumenx 正文超过判断框架所需的短引
- 不改变 manga_drama FSM 与五类 QA 门语义（本门为 gate#2 加强项）
- 不做 live_drama/comic 接入实现（仅声明适用面）；不做发布自动化

## Illegal transitions

- 未决资产项流入图片提示词或分镜 → illegal
- 相邻镜头边界差异无变化记录支撑仍通过 → illegal
- 宣称本门可替代正典门/QA SCORECARD → illegal
