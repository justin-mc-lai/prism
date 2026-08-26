---
slug: prism-asset-gate-rollout-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-asset-gate-rollout-v1/truth.md
---

# User Stories — prism-asset-gate-rollout-v1

## US-RLO-001 实拍短剧资产可解析

director 交分集剧本+shot-list → 资产一致性门核对每镜引用解析到身份条目、相邻镜头
end→start 匹配 → 失败 blocked 列修复项，人工素材 ingest 照常并行。

## US-RLO-002 多集漫画跨页一致

comic 第 N 页角色服装/伤势与第 1 页设定冲突 → 门拦截，要求按变体记录（基底+变化+原因+生效页），
禁止静默漂移。
