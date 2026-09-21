---
program_slug: prism-release-av-manga-release-gate
version: v0.0.1
plan_mode: interactive
plan_mode_reason: governance_precheck_pass_2026_09_21
scope_mode: phased_lake
lake_or_ocean: 湖
this_lake: Lake B′（release 面 AV 交接门 · 最后一处接线缺口）
sea_promise: full_selfmedia_creation_capability
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
public_id: goal
repos:
  - prism（本仓）
  - selfmedia-creator（源仓，只读参考）
  - beacon（设计理念对照；advisory only）
intent_one_liner: 把 asset-render 契约的 §6（AI 标识）/ §7（pending_human handoff）接进 prism-release 公开面
created_at: "2026-09-21"
plan_revision: RAV-plan
current_lake_feature: prism-release-av-gate-v1
prior_lake_features:
  - prism-prompt-compiler-v1
  - prism-manga-asset-gate-v1
  - prism-asset-gate-rollout-v1
source_freeze: selfmedia-creator prism-canon-v1@R3
---

# Program Manifest

User utterance: prism-release 对接 AV/manga 渲染交接：识别 release_gate=pending_human 终态、强制 AI 提示标识门、禁止静默公开发布；补齐 release 面对 asset-render 契约的引用与核验步骤

## Intent

`prism-release` 此前对 AV/manga 交接**零引用**。本湖只做接线：让「发」这一步看得见
AV 成片的终态（`pending_human`）与法定义务（AI 标识），并加 exec 断言。

## Lanes

- Lane 1（本湖）：release 面 AV 交接接线（`prism-release-av-gate-v1`）
- Lane 2（后续海）：平台发布 API / 自动发布，不在本湖
- Lane 3（后续海）：`prism-intel` 侧的形态感知（当前无需，选题面不涉渲染）
