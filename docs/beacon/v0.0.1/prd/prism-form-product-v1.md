---
slug: prism-form-product-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-product-v1/truth.md
---

# PRD — prism-form-product-v1（Lake D2 扩展）

## 问题

用户清单里的「电商商品」形态在 Prism 无 form contract、无注册路由；goal 只有 lane 分类没有
form 自动识别，入口靠人工查表；2026-08 评估的 5 个开源热门创作仓库（lumenx/dramaclaw/
drama-skills/MoneyPrinterTurbo/openstory）未入盘点册，其中与 Prism 同构的 drama-skills
（MIT）未 pin。

## 目标

1. `registry/form-registry.yaml` 注册 product；`contracts/form-product.contract.md`
   定义商品事实门 + 广告法极限词门（均 fail-closed）。
2. `skills/_internal/orchestration/form-autodetect.md`：11 形态关键词映射 classify_form，
   接进 prism-goal loop-campaign 状态机；显式指定优先，多命中/零命中交人。
3. creation-mode-map 增电商商品行。
4. source-capability-inventory 增补五库批次（license/策略/落点/状态）。
5. drama-skills 整包 pin 进 `vendor/skills/drama-skills/` + ATTRIBUTION。
6. `scripts/check_product_form.sh` exec 门禁。

## 边界

- 能做：product 契约/注册/路由/自动识别/盘点/pin/exec 校验。
- 不能做：四平台仓库运行时 pin；dramaclaw 整包复制（Elastic-2.0）；平台发布 API；
  公开发布自动化。

## 成功判据

TC-PRD-001..010 全 PASS；`bash scripts/check_product_form.sh` PASS；
`make -C workspace check` PASS；受影响 skill quick_validate PASS。

## 参考

- planner review（pln-review · 2026-08-26）：P1 form-autodetect / P1 ecommerce-form /
  P2 inventory-refresh / P2 asset-consistency
- 上游证据：zenstory-ai/drama-skills README（MIT）、dramaclaw README（Elastic-2.0）、
  alibaba/lumenx README（MIT，本地镜像 oss-sync/automation/auto/lumenx）
