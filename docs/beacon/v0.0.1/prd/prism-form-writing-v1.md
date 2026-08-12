---
slug: prism-form-writing-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md
---

# PRD — prism-form-writing-v1（Lake D1）

## 问题

Lake B/C 只有 writing adapter stub 与通用反 slop 概念，没有 Prism 自己的成稿规则、人味判据与
工具桥；八形态生产链（D2–D6）没有统一写作/反 slop 地基可依赖。

## 目标

落地 `contracts/writing.contract.md`（七段 + 蒸馏写作规则）、
`skills/prism-qa/references/anti-slop-gate.md`（slop 模式 + 人话判据 + 证据要求）、
`registry/writing-adapters.yaml`（≥8 bridge）、creation-mode-map 路由引用与
`scripts/check_writing_adapters.sh` exec 校验。

## 边界

- 能做：成稿规则、反 slop 门、bridge 登记、路由、校验脚本。
- 不能做：D2–D6 形态本体；vendor_pin；metrics；平台 API；自动公开发布。
- 怎样算完：四件套填满；AC 全有 TC；exec 脚本 PASS；freeze → implement → QA → release 人工门。
