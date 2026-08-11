---
slug: prism-campaign-schema-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-11：同意继续 Lake C freeze package"
user_decision: promoted
---

# Research: prism-campaign-schema-v1

## 背景

Lake A（`prism-canon-v1` R3）在 AC-PRISM-008 冻结了 **campaign 机制级定义**，但明确 **不落 schema 文件**（DL-002 → Lake C）。Lake B（`prism-extract-v1`）已完成独立仓提取与编排内核迁入，`pipeline-contract.md` 已规划 `content/distribution/campaigns/` 路径，但 `content/storyworlds/` 与正式契约尚未落地。

## 源仓证据

- `selfmedia-creator/content/masters/{vertical}/{slug}/` 已有 FactMaster 实例：`meta.yaml` + `MASTER.md`（如 `oss-picks/wenyan`）
- `content/storyworlds/` 在源仓尚不存在 — Lake C 为 greenfield schema
- `registry/adapter-migration-matrix.md` MAP-004：`distill` master freeze rules； deepen lake = C

## Lake C 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| Schema 权威位置 | `registry/content-schema.yaml` + `contracts/*.schema.yaml` | 与 Lake B registry 模式一致；机器可校验 |
| Master 路径 | `content/masters/{vertical}/{slug}/` | 继承源仓与 pipeline-contract |
| StoryWorld 路径 | `content/storyworlds/{world_slug}/` | Lake A 实体模型；source-architecture 已规划 |
| Campaign 路径 | `content/distribution/campaigns/{campaign_id}.yaml` | pipeline-contract 已有 |
| Canon gate | episode `canon_gate_status` + truth illegal 列表 | AC-PRISM-009 / FP-PRISM-003 |
| 示例策略 | `_examples/` 下最小合法样本 | 不污染生产 vertical |

## 明确不做（本湖）

- 八形态 producer 脚本（Lake D）
- MetricsSnapshot 采集实现（Lake E）
- vendor_pin 搬迁
- 海 closure 宣称

## 下一步

1. truth review + freeze 本包
2. implement 契约文件 + scaffold + `check_content_schema.sh`
3. QA → release（独立湖闭环）
