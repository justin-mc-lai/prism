---
slug: prism-form-product-v1
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
  prd: docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-product-v1/tests.md
provenance:
  - ac_id: AC-PRD-001
    source_type: migrated_truth
    source_ref: "Lake D2 FP-PRISM-007 form registry 惯例 · planner review 2026-08-26 P1"
  - ac_id: AC-PRD-004
    source_type: source_evidence
    source_ref: "zenstory-ai/drama-skills 路由入口同构 + dramaclaw 形态覆盖声明（planner review 2026-08-26）"
---

# Requirement Truth: prism-form-product-v1（v0.0.1 · Lake D2 扩展）

## 人话

给 Prism 补上**电商商品形态**和**形态自动识别**：用户说「帮我做这个商品的好物图文」时，
goal 能自动判定该走 product form；product 契约强制商品事实有源、广告法极限词 fail-closed。
同一批把 5 个开源参考库盘点入册，并把 MIT 的 drama-skills 整包 pin 进 vendor。

- 能做：form-registry 注册 product；`contracts/form-product.contract.md`；
  `form-autodetect.md` classify_form 步骤并接进 goal 状态机；creation-mode-map 电商行；
  inventory 增补 5 库；drama-skills vendor pin + ATTRIBUTION；exec 校验脚本。
- 不能做：pin lumenx/dramaclaw/MoneyPrinterTurbo/openstory 运行时；dramaclaw 整包复制
  （Elastic-2.0）；平台 API；发布自动化。
- 怎样算完：AC 全有 TC；exec PASS；全量门禁绿；implement → QA → release 人工门。

## User Intent

分析后确认的批次更新：新增 classify_form 自动识别 + 电商商品 form + 5 库 inventory +
drama-skills vendor pin，确保验收通过可交付。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D2 扩展（product form）+ 编排内核（classify_form）+ 参考库盘点
user_decision: promoted
scope_mode: phased_lake
feature: prism-form-product-v1
version: v0.0.1
depends_on: prism-form-blog-thread-v1 / prism-form-image-post-v1（form registry 惯例）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-PRD01 | migrated | must | AC-PRD-001（product 注册） | covered |
| INT-PRD02 | migrated | must | AC-PRD-002（契约七节） | covered |
| INT-PRD03 | migrated | must | AC-PRD-003（事实门+极限词门） | covered |
| INT-PRD04 | source | must | AC-PRD-004（classify_form） | covered |
| INT-PRD05 | migrated | must | AC-PRD-005（路由表） | covered |
| INT-PRD06 | migrated | must | AC-PRD-006（exec 脚本） | covered |
| INT-PRD07 | source | must | AC-PRD-007（drama-skills pin） | covered |
| INT-PRD08 | source | must | AC-PRD-008（5 库入册） | covered |
| INT-PRD09 | migrated | must | AC-PRD-009（分湖边界） | covered |
| INT-PRD10 | sea | must | 其余形态扩展 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-PRD-001 | 商品事实必须有源（规格/价格/参数）；无源不得产出成稿 |
| FP-PRD-002 | 广告法极限词 fail-closed，并给替代表达 |
| FP-PRD-003 | 未跑 classify_form 且无显式 form 指定，不得路由 produce |
| FP-PRD-004 | 形态识别多命中/零命中 fail-closed 交人，不猜 |
| FP-PRD-005 | 受 Elastic-2.0 约束的仓库只蒸馏判断框架，禁止整包复制 |
| FP-PRD-006 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-PRD-001：用户说「帮我做这个商品的好物图文」。goal 先跑 classify_form，
判定 form=product → 路由 product 契约 → produce 前过商品事实门与极限词门 → QA → release。

US-PRD-002：商品资料不全。product 契约 blocked（`product_fact_missing`），
不产出成稿，要求补资料。

US-PRD-003：文案含极限词。极限词门 fail-closed，给出替代表达后再进 QA。

US-PRD-004：形态识别多命中。classify_form fail-closed 交人，不自动路由。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| ProductFormContract | form-product | 七节契约 + 输出路径 |
| FormAutodetect | classify_form | 11 形态关键词映射 |
| ProductFactGate | product_fact_missing | 商品事实有源门 |
| AdLawGate | 极限词 | 广告法合规门 |
| VendorPin | drama-skills | MIT 整包 pin |
| ReferenceInventory | source-capability-inventory | 外部参考库入册 |

## Domain FSM（D2 扩展落地）

状态：product_planned → product_registered → product_contract_landed → autodetect_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| product_registered | product_planned | form-registry 含 product |
| product_contract_landed | product_registered | form-product.contract present |
| autodetect_landed | product_contract_landed | form-autodetect.md + goal 接线 |
| routing_landed | autodetect_landed | creation-mode-map 电商行 present |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- 商品事实无源仍产出成稿 → illegal
- 极限词未消除即进入 QA → illegal
- 未跑 classify_form 且无显式 form 指定就路由 produce → illegal
- 形态识别多命中/零命中仍自动路由（不交人）→ illegal
- dramaclaw 整包复制进 vendor（Elastic-2.0）→ illegal
- 宣称海 closure（覆盖全部自媒体创作能力）→ illegal

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| product_planned | register_form | product in registry | product_registered | update form-registry |
| product_registered | land_contract | form-product.contract present | product_contract_landed | write contract |
| product_contract_landed | land_autodetect | autodetect + goal wiring | autodetect_landed | write form-autodetect.md |
| autodetect_landed | wire_routing | ecommerce row present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check_product_form.sh |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. product 形态注册（AC-PRD-001）
2. product 契约落地（AC-PRD-002）
3. 商品事实门 + 极限词门（AC-PRD-003）
4. classify_form 自动识别（AC-PRD-004）
5. 路由表更新（AC-PRD-005）
6. exec 校验脚本（AC-PRD-006）
7. drama-skills vendor pin（AC-PRD-007）
8. 外部参考库入册（AC-PRD-008）
9. Non-goals 分湖边界（AC-PRD-009）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-PRD01 | lumenx / MoneyPrinterTurbo / openstory 运行时 pin | accepted | 只 distill；需要时按 A4 单独决策 |
| DL-PRD02 | dramaclaw 整包复制 | rejected | Elastic-2.0 约束 |
| DL-PRD03 | 电商平台 / 社媒发布 API | accepted | 属后续湖 |
| DL-PRD04 | 其余形态扩展 | accepted | 本湖只做 product |
| DL-PRD05 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-PRD-001 | 进入 `product_registered`：form-registry.yaml 登记 `product`，含 `contracts/form-product.contract.md` 引用与完整 producer_chain；YAML 可解析 |
| AC-PRD-002 | 进入 `product_contract_landed`：契约定义 identity/决策边界/intake/output/gate/handoff/失败处理 七节；输出路径 `content/presentations/{vertical}/{slug}/product-{angle}/`；证据路径指向本 feature evidence |
| AC-PRD-003 | 商品事实门：intake 强制商品事实有源，无源 → blocked `reason_code=product_fact_missing`；极限词（最/第一/顶级等广告法词）fail-closed 并给替代表达 |
| AC-PRD-004 | 进入 `autodetect_landed`：`skills/_internal/orchestration/form-autodetect.md` 提供 11 形态确定性关键词映射；显式指定优先；多命中/零命中 fail-closed 交人；结果记 machine face `form_detected`；prism-goal loop-campaign 状态机接线 `classify_lane → classify_form → route_next_public_surface` |
| AC-PRD-005 | 进入 `routing_landed`：creation-mode-map 新增电商商品行并引用 form-product.contract；标注 classify_form 入口提示 |
| AC-PRD-006 | 进入 `indexed`：`scripts/check_product_form.sh` 可执行且 PASS（真实断言，缺一即 FAIL） |
| AC-PRD-007 | drama-skills vendor pin：`vendor/skills/drama-skills/` 整包（去 .git），LICENSE 随附；ATTRIBUTION 登记 MIT 行 |
| AC-PRD-008 | source-capability-inventory.md 新增「外部参考库蒸馏批次」：lumenx/dramaclaw/drama-skills/MoneyPrinterTurbo/openstory 五库各含 license/策略/落点/状态 |
| AC-PRD-009 | 分湖边界：不 pin 四个平台型仓库运行时；不做 dramaclaw 整包复制（Elastic-2.0）；不做平台发布 API；不得宣称海 closure |

## Non-goals

- lumenx / MoneyPrinterTurbo / openstory 运行时不 pin（只 distill，需要时按 A4 单独决策）
- dramaclaw 受 Elastic-2.0 约束：只蒸馏判断框架，禁止整包复制进 vendor
- 不做电商平台/社媒发布 API 与自动化发布
- 不改六个公开面的 HARD GATE 与 human card 结构

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
