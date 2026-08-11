---
slug: prism-campaign-schema-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md
---

# PRD — prism-campaign-schema-v1（Lake C）

## 问题

Lake B 已交付独立仓、公开面壳与 adapter 索引，但 campaign / storyworld / master 内容对象只有
Lake A 的机制级定义（AC-PRISM-008/009、DL-002），没有文件级 schema 与目录契约，连载与 canon
车道缺少可验证的容器真值。

## 目标

落地 `registry/content-schema.yaml` 注册表 + 5 个内容对象契约
（master-content / storyworld / campaign / narrative-episode / distribution-binding）、
`content/` 目录 scaffold 与示例、canon gate 钩子、MAP-004 master 冻结清单，
以及 `scripts/check_content_schema.sh` 校验脚本，使 schema 可被命令验证。

## 边界

- 能做：schema 注册表、契约、scaffold、canon 钩子、MAP-004 加深、校验脚本。
- 不能做：form producer chains（Lake D）、metrics/learning loop（Lake E）、monetization（Lake F）、
  vendor_pin 全量搬迁、分发 API 自动化、自动公开发布。
- 怎样算完：四件套填满；AC 全有 TC；schema 校验脚本 PASS；Truth Review Gate + freeze 通过；
  implement → QA → release 人工门。

## 验收摘要

AC-SCHEMA-001…010（见 truth.md）；TC-SCHEMA-001…015（含 4 条 exec-layer）。
