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
scope_mode: phased_lake
feature: prism-manga-asset-gate-v1
version: v0.0.1
depends_on: prism-form-av-v1 / ai-manga-drama 源 truth R1
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-MAG01 | source | must | AC-MAG-001（蒸馏参考） | covered |
| INT-MAG02 | migrated | must | AC-MAG-002（门契约） | covered |
| INT-MAG03 | migrated | must | AC-MAG-003（manga 接线） | covered |
| INT-MAG04 | migrated | must | AC-MAG-004（registry 链） | covered |
| INT-MAG05 | migrated | must | AC-MAG-005（exec 脚本） | covered |
| INT-MAG06 | migrated | must | AC-MAG-006（上游不 pin） | covered |
| INT-MAG07 | source | must | AC-MAG-007（A4 常设决策） | covered |
| INT-MAG08 | sea | must | live_drama/comic rollout | deferred → prism-asset-gate-rollout-v1 |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-MAG-001 | 每个画面实体必须先归类身份/变体/镜头瞬态；禁止把每次出场变成新身份 |
| FP-MAG-002 | 识别锚点必须可见、可生成、可比较；空泛质量词不算锚点 |
| FP-MAG-003 | 相邻镜头边界差异必须有变化记录支撑（CON-01） |
| FP-MAG-004 | 未决项不得流入图片提示词或分镜（AST-05，fail-closed） |
| FP-MAG-005 | 全片引用同一风格锚点；换风格 = 新建版本并记录生效集数 |
| FP-MAG-006 | 本门是既有门的**加强**，不替代 refs-exist 与五类 QA 门 |
| FP-MAG-007 | 只取判断框架，不复制上游运行时；受 license 约束的仓库不整包 pin |
| FP-MAG-008 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-MAG-001：用户要漫剧。director 出分镜 JSON（角色卡 + asset_ref）→
produce 前过资产一致性门（三分法 / binding / 边界匹配 / 变化记录 / 画风统一）→
五类 QA 门 → release 停人工。

US-MAG-002：分镜里有未决资产。资产门 fail-closed，未决项不得流入分镜或图片提示词。

US-MAG-003：相邻镜头状态不一致且无变化记录。资产门判失败，要求补变化记录或重出分镜。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| AssetConsistencyGate | asset-consistency | 六判据门契约 |
| AssetIdentity | identity | 换一个就不再是同一实体 |
| AssetVariant | variant | 身份不变，状态改变 |
| ShotTransient | transient | 姿势/机位等，归分镜层 |
| ChangeRecord | CON-04 | 前态/后态/原因/范围/受影响 ID |
| StyleAnchor | lookdev | 全片风格锚点帧 |
| MangaContract | form-manga-drama | 接线点 |
| UpstreamDistill | drama-skills / lumenx | 判断框架来源 |

## Domain FSM（D 落地）

状态：gate_planned → distill_landed → contract_landed → manga_wired → registry_updated → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| distill_landed | gate_planned | 蒸馏参考含三分法/锚点/边界/画风 |
| contract_landed | distill_landed | asset-consistency.contract 七节 |
| manga_wired | contract_landed | manga 契约 intake 锚点 + gate#2 升级 |
| registry_updated | manga_wired | producer_chain 含门步骤 |
| indexed | registry_updated | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- 未决资产项流入图片提示词或分镜 → illegal
- 相邻镜头边界差异无变化记录支撑仍通过 → illegal
- 宣称本门可替代正典门 / QA SCORECARD → illegal
- 把每次出场都变成新身份 → illegal
- pin lumenx/dramaclaw/MPT/openstory 运行时 → illegal
- 复制上游正文超过判断框架所需的短引 → illegal
- 宣称海 closure → illegal

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| gate_planned | land_distill | framework keywords present | distill_landed | write asset-consistency-gate.md |
| distill_landed | land_contract | seven sections + fail-closed code | contract_landed | write asset-consistency.contract |
| contract_landed | wire_manga | intake anchor + gate#2 ref | manga_wired | update form-manga-drama.contract |
| manga_wired | update_registry | chain carries gate step | registry_updated | update form-registry |
| registry_updated | index | exec script + no leak | indexed | write check_asset_consistency.sh |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 蒸馏参考落地（AC-MAG-001）
2. 门契约七节（AC-MAG-002）
3. manga_drama 契约接线（AC-MAG-003）
4. registry 生产链更新（AC-MAG-004）
5. exec 校验脚本（AC-MAG-005）
6. 上游运行时不 pin（AC-MAG-006）
7. MPT/openstory A4 常设决策入册（AC-MAG-007）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-MAG01 | live_drama / comic rollout | accepted | 拆到 prism-asset-gate-rollout-v1 |
| DL-MAG02 | lumenx / dramaclaw 运行时 pin | accepted | 只 distill；dramaclaw 受 Elastic-2.0 约束 |
| DL-MAG03 | MPT / openstory pin | accepted | 按 A4 逐次决策 |
| DL-MAG04 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-MAG-001 | 进入 `distill_landed`：`skills/prism-director/references/asset-consistency-gate.md` 含三分法、识别锚点、CON-01 边界匹配、CON-04 变化记录、AST-05 binding、画风统一、lumenx 三件套映射，标注双上游出处 |
| AC-MAG-002 | 进入 `contract_landed`：`contracts/asset-consistency.contract.md` 含 identity/决策边界/intake/output/gate/handoff/失败处理；fail-closed 码 `asset_identity_missing`；六判据叠加不替代既有门 |
| AC-MAG-003 | 进入 `manga_wired`：form-manga-drama.contract.md intake 要求识别锚点（未决项不得流入分镜），gate 第 2 条升级引用 asset-consistency 契约 |
| AC-MAG-004 | 进入 `registry_updated`：manga_drama producer_chain 在 storyboard 校验后插入资产一致性门步骤且 YAML 可解析 |
| AC-MAG-005 | 进入 `indexed`：`scripts/check_asset_consistency.sh` 可执行且 PASS |
| AC-MAG-006 | 上游边界：vendor/skills 下不得出现 lumenx、dramaclaw 目录（distill only，不 pin 运行时） |
| AC-MAG-007 | source-capability-inventory 记录 defer-pin 维持 + 触发条件 + 届时按 A4 逐次 pin |

## Non-goals

- 不 pin lumenx/dramaclaw/MoneyPrinterTurbo/openstory 任何运行时或整包
- 不复制 drama-skills/lumenx 正文超过判断框架所需的短引
- 不改变 manga_drama FSM 与五类 QA 门语义（本门为 gate#2 加强项）
- 不做 live_drama/comic 接入实现（仅声明适用面）；不做发布自动化

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
