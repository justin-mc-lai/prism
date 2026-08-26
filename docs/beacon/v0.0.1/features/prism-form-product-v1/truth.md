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
```

## Acceptance Criteria

### AC-PRD-001 product 形态注册
form-registry.yaml 登记 `product`：含 `contracts/form-product.contract.md` 引用与完整
producer_chain；YAML 可解析。
- 验证：registry 解析 + rg 断言（TC-PRD-001/007）

### AC-PRD-002 product 契约落地
契约定义 identity/决策边界/intake/output/gate/handoff/失败处理 七节；输出路径
`content/presentations/{vertical}/{slug}/product-{angle}/`；证据路径指向本 feature evidence。
- 验证：rg 断言七节关键词（TC-PRD-002）

### AC-PRD-003 商品事实门 + 极限词门
intake 强制商品事实有源（资料/抓取留档/人工确认），无源 → blocked
`reason_code=product_fact_missing`；极限词（最/第一/顶级等广告法词）fail-closed 并给替代表达。
- 验证：rg 断言 gate 关键词（TC-PRD-003）

### AC-PRD-004 classify_form 自动识别
`skills/_internal/orchestration/form-autodetect.md` 提供 11 形态确定性关键词映射；
显式指定优先；多命中/零命中 fail-closed 交人；结果记 machine face `form_detected`；
prism-goal loop-campaign 状态机接线 `classify_lane → classify_form → route_next_public_surface`。
- 验证：文件存在 + 映射覆盖 novel/vlog/product/manga_drama/live_drama + goal 接线断言（TC-PRD-004）

### AC-PRD-005 路由表更新
creation-mode-map 新增电商商品行并引用 form-product.contract；标注 classify_form 入口提示。
- 验证：rg 断言（TC-PRD-005）

### AC-PRD-006 exec 校验脚本
`scripts/check_product_form.sh` 可执行且 PASS（真实断言，缺一即 FAIL）。
- 验证：执行脚本（TC-PRD-006）

### AC-PRD-007 drama-skills vendor pin
`vendor/skills/drama-skills/` 整包（去 .git），LICENSE 随附；ATTRIBUTION 登记 MIT 行。
- 验证：目录/LICENSE/ATTRIBUTION 断言（TC-PRD-008）

### AC-PRD-008 外部参考库入册
source-capability-inventory.md 新增「外部参考库蒸馏批次」：lumenx/dramaclaw/
drama-skills/MoneyPrinterTurbo/openstory 五库各含 license/策略/落点/状态。
- 验证：rg 断言五库名（TC-PRD-009）

### AC-PRD-009 Non-goals（分湖边界）
不 pin 四个平台型仓库运行时；不做 daramlaw 整包复制（Elastic-2.0）；不做平台发布 API；
不得宣称海 closure。
- 验证：truth Non-goals 节断言（TC-PRD-010）

## Non-goals

- lumenx / MoneyPrinterTurbo / openstory 运行时不 pin（只 distill，需要时按 A4 单独决策）
- dramaclaw 受 Elastic-2.0 约束：只蒸馏判断框架，禁止整包复制进 vendor
- 不做电商平台/社媒发布 API 与自动化发布
- 不改六个公开面的 HARD GATE 与 human card 结构

## Illegal transitions

- 商品事实无源仍产出成稿 → illegal
- 极限词未消除即进入 QA → illegal
- 未跑 classify_form 且无显式 form 指定就路由 produce → illegal
- 宣称海 closure（覆盖全部自媒体创作能力）→ illegal
