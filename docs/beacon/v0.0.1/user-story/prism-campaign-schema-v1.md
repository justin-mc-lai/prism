---
slug: prism-campaign-schema-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md
---

# User Stories — prism-campaign-schema-v1（Lake C）

本文件是 Lake C 的用户旅程冻结面；AC 与 TC 的权威落在 feature package truth/tests。

## US-SCHEMA-001（= US-PRISM-002）连载旅程

用户要连载小说或漫画。`prism-goal` / campaign 定连载计划 → `prism-master` 冻结 StoryMaster →
`prism-director` 出 episode 大纲或分镜 → `prism-produce` 产章节 → `prism-qa` 过正典/连续性门 →
`prism-release` → 连载发布。本湖只冻 schema 与路径，不执行生产链。

验收映射：AC-SCHEMA-001 / 004 / 005 / 007 / 009。

## US-SCHEMA-002 Master / StoryWorld 维护旅程

维护者为 FactMaster 与 StoryMaster 在 `content/masters/` 建立统一 `meta.yaml` + `MASTER.md` 契约；
StoryWorld 在 `content/storyworlds/` 挂接 `world.yaml`、`bible.md`、`canon-ledger.yaml`、
`characters/`、`timeline/`。kind=story 的 master 必须引用 world 或 canon 锚点。

验收映射：AC-SCHEMA-002 / 003 / 008。

## US-SCHEMA-003 Campaign / Binding 登记旅程

战役负责人在 `content/distribution/campaigns/` 登记 `campaign_id`、`lane`、`objective`、
`master_refs`、可选 `world_slug` 与 `schedule_intent`；bindings 在
`content/distribution/bindings/` 连接 presentation × endpoint。

验收映射：AC-SCHEMA-004 / 006 / 010。

## 验收与发布旅程

QA 以 `scripts/check_content_schema.sh` 与 15 条 TC 验证 schema 可被命令校验；release 必须人工确认，
不得宣称海 closure。

验收映射：AC-SCHEMA-001…010 + TC-SCHEMA-001…015。
