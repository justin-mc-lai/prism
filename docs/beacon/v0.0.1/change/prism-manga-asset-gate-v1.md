# Beacon Feature Change Projection

- feature: `prism-manga-asset-gate-v1`
- feature_slug: `prism-manga-asset-gate-v1`
- version: `v0.0.1`
- artifact_role: `release-facing projection/read model`
- truth_source: `false`

## Scope
- Lake D：manga_drama 资产一致性门（蒸馏 drama-skills + lumenx 判断框架，MAP-017）：
  三分法/识别锚点/CON-01 边界匹配/CON-04 变化记录/AST-05 binding/画风统一；
  契约 + manga 接线 + registry 链更新 + exec 门禁；MPT/openstory A4 defer-pin 常设决策入册。

## Added
- skills/prism-director/references/asset-consistency-gate.md
- contracts/asset-consistency.contract.md
- scripts/check_asset_consistency.sh
- source-capability-inventory §A4 常设决策

## Removed
- （无）

## Fixed
- form-manga-drama.contract.md intake 补识别锚点要求；gate#2 由 refs 存在升级为一致性门引用
- registry/form-registry.yaml manga_drama producer_chain 插入门步骤
