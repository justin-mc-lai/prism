---
slug: prism-form-novel-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md
---

# PRD — prism-form-novel-v1（Lake D4）

## 问题

连载小说没有生产者契约：episode 结构与正典门未接，StoryWorld/canon ledger 只存在于 schema，
没有“谁产出、怎么过正典门、产出落哪”的文件级规范。

## 目标

form-registry 注册 novel；`contracts/form-novel.contract.md`（StoryMaster 输入、episode 结构、
canon_gate_status 门、StoryWorld 路径、OOC fail-closed、bridge kushi-narrative-zh）；
creation-mode-map novel 行；`scripts/check_novel_form.sh` exec 校验。

## 边界

- 能做：novel 契约、canon 钩子、路由、校验。
- 不能做：D5/D6；vendor_pin；metrics；平台 API；自动公开。
