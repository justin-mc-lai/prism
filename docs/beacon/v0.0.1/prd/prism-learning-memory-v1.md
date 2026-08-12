---
slug: prism-learning-memory-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md
---

# PRD — prism-learning-memory-v1（Lake E4）

## 问题

复盘产出没有持久化：判断改善依赖即时上下文，记忆不可回放、不可审计、不可裁剪。

## 目标

`contracts/learning-memory.contract.md`（memory_id/source_ref/claim/confidence/applicability +
advisory-only + 可回放/可裁剪）；`registry/learning-adapters.yaml`（≥3）；路由引用；exec 校验脚本。

## 边界

- 能做：学习记忆契约、登记、路由、校验。
- 不能做：Lake F；平台 API；learning 写入 truth/替代 QA。
