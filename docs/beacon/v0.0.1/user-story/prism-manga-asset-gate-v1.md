---
slug: prism-manga-asset-gate-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md
---

# User Stories — prism-manga-asset-gate-v1（Lake D）

## US-MAG-001 一致性门拦截漂移

director 出 storyboard.json → produce 前跑资产一致性门：asset_ref 解析到身份条目、
相邻镜头 end→start 匹配、画风同锚点；任一失败 → blocked + reason_code，human card 列修复项。

## US-MAG-002 未决项不流入

分镜引用了一个未确认的新道具 → AST-05 fail-closed（`asset_identity_missing`），
不得为让生成继续而猜一个 ID。

## US-MAG-003 换装是变体不是新角色

第 3 集主角换礼服 → 资产层记录变体（基底+变化+原因+生效集数），身份不变；
分镜只拥有瞬态（姿势/站位）。

## US-MAG-004 参考库按需取用

做漫剧时 director 可对照 `vendor/skills/drama-skills/skills/short-drama-assets` 的
连续性/审查清单细化判断；lumenx 只作框架参考（本地镜像），运行时不进仓。
