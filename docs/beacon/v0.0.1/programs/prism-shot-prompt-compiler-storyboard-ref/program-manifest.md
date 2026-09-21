---
program_slug: prism-shot-prompt-compiler-storyboard-ref
version: v0.0.1
plan_mode: interactive
plan_mode_reason: one_question_round_completed_2026_09_21
scope_mode: phased_lake
lake_or_ocean: 海
this_lake: Lake B′（提示词编译器 + 渲染交接去兜底）
sea_promise: full_selfmedia_creation_capability
extract_to: independent_prism_repo
beacon_alignment: design_philosophy_only
public_id: goal
repos:
  - prism（本仓）
  - selfmedia-creator（源仓，只读 archive）
  - beacon（设计理念对照；advisory only）
intent_one_liner: Prism 产出全部前置文本提示词与 provider 请求包；渲染交下游 provider；无凭证 fail-closed，不做本地兜底
created_at: "2026-09-21"
plan_revision: PPC-plan
current_lake_feature: prism-prompt-compiler-v1
prior_lake_features:
  - prism-manga-asset-gate-v1
  - prism-asset-gate-rollout-v1
  - prism-form-novel-v1
  - prism-form-av-v1
source_freeze: selfmedia-creator prism-canon-v1@R3
decisions_2026_09_21:
  assemble: 改为只拼接 provider 真实片段（缺片段 fail-closed）
  voice: edge-tts 一并删除，语音交下游 provider
  frozen_contract_change: 新 feature + change 记录 + refreeze form-manga-drama
---

# Program Manifest

User utterance: 实现 prism 提示词编译器与渲染交接：蒸馏剧本模板、shot-prompt-compiler、storyboard ref_image 字段、asset-render 契约与适配器；取消 FFmpeg kenburns 兜底，无凭证 fail-closed 终止；Prism 产出全部前置文本提示词，文生图/图生视频/文生视频交给下游 provider

## Intent

Prism 是 agent skill：**先把前置文本全部生成出来**（剧本 / 分镜 / 资产 ref 提示词 / 每镜图片与视频提示词 /
字幕 / provider 请求包），画面与音视频的生成交给下游 provider 模型。本轮同时拆除本地兜底
（FFmpeg kenburns、edge-tts），无凭证直接终止。

## Lanes

- Lane 1（本湖）：提示词编译器 + ref_image + asset-render 契约 + 去兜底（`prism-prompt-compiler-v1`）
- Lane 2（后续海）：provider 执行器（真实 T2I/I2V/T2V/TTS 调用 + 凭证管理），不在本湖
- Lane 3（后续海）：novel / live_drama 复用 asset-render 契约
