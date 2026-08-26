---
slug: prism-asset-gate-rollout-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-asset-gate-rollout-v1/truth.md
---

# PRD — prism-asset-gate-rollout-v1（资产一致性门推广）

## 问题

asset-consistency 契约 §1 已声明适用 live_drama 分镜阶段与 comic 多集，但两形态契约
与 registry 生产链未接线——门声明了却没人执行。

## 目标

1. form-live-drama.contract.md：intake 分镜交付含资产身份条目引用；gate 新增一致性判据。
2. form-av.contract.md：intake storyboard 带 asset_ref 解析要求；comic 多集 gate 判据。
3. registry live_drama/comic producer_chain 各插入门步骤。
4. check_asset_consistency.sh 扩展 rollout 断言。

## 边界

- 能做：两契约接线、registry 链更新、exec 扩展。
- 不能做：vlog/book_video 接入；改 manga 冻结接线；改既有 FSM/gate 语义；上游 pin。

## 成功判据

TC-RLO-001..004 全 PASS；`make -C workspace check` PASS。
