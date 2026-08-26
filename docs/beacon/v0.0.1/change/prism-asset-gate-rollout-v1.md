# Beacon Feature Change Projection

- feature: `prism-asset-gate-rollout-v1`
- feature_slug: `prism-asset-gate-rollout-v1`
- version: `v0.0.1`
- artifact_role: `release-facing projection/read model`
- truth_source: `false`

## Scope
- 资产一致性门按适用面声明推广：live_drama（分镜阶段）+ comic（多集路由）契约与
  registry 生产链接线；exec 校验扩展。判断框架零改动（复用 MAP-017）。

## Added
- （无新文件；全部为既有文件接线）

## Removed
- （无）

## Fixed
- form-live-drama.contract.md intake 分镜交付身份条目要求 + gate#6 一致性判据
- form-av.contract.md intake asset_ref 解析要求 + comic 多集 gate 判据
- registry live_drama/comic producer_chain 插入门步骤
- check_asset_consistency.sh 扩展 rollout 断言（含 vlog/book_video 不接线反断言）
