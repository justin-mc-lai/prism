---
slug: prism-learning-memory-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md
---

# User Stories — prism-learning-memory-v1（Lake E4）

## US-LMEM-001 学习记忆

E3 复盘发现 → 按 `learning-memory.contract` 写入记忆（来源/时间/置信度/适用边界）→
intel/plan 可回放引用（advisory）。

## US-LMEM-002 冲突记忆

两条记忆矛盾 → 显式 conflict 标记，不静默合并。

## US-LMEM-003 裁剪

过期/无用记忆 → prune 规则裁剪，保留审计痕迹。
