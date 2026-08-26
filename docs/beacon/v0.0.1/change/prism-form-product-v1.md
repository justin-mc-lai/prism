# Beacon Feature Change Projection

- feature: `prism-form-product-v1`
- feature_slug: `prism-form-product-v1`
- version: `v0.0.1`
- artifact_role: `release-facing projection/read model`
- truth_source: `false`

## Scope
- Lake D2 扩展：product（电商商品）形态契约 + 注册 + 路由；编排内核新增 classify_form
  自动识别步骤并接进 prism-goal 状态机；外部参考库蒸馏批次入册（5 库）；
  drama-skills（MIT）整包 vendor pin + ATTRIBUTION。

## Added
- contracts/form-product.contract.md
- skills/_internal/orchestration/form-autodetect.md
- scripts/check_product_form.sh
- registry/form-registry.yaml product 条目
- creation-mode-map 电商商品行 + classify_form 提示
- loop-campaign 状态机 classify_lane → classify_form 接线
- source-capability-inventory.md §外部参考库蒸馏批次
- vendor/skills/drama-skills/（MIT，LICENSE 随附）
- docs/ATTRIBUTION-bridges.md drama-skills 行

## Removed
- （无）

## Fixed
- （无）

## Non-goals
- lumenx/MoneyPrinterTurbo/openstory 运行时不 pin；dramaclaw Elastic-2.0 只 distill；
  不做平台发布 API。
