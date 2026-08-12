---
slug: prism-form-novel-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-novel-v1/truth.md
---

# User Stories — prism-form-novel-v1（Lake D4）

## US-NVL-001 连载

prism-goal 定连载计划 → master 冻结 StoryMaster（bible + canon ledger）→ director 出 episode 大纲
→ produce 按 `form-novel.contract` 产章节（`content/storyworlds/{world}/episodes/`）→
qa 过正典/连续性门 → release。

## US-NVL-002 正典未过

episode `canon_gate_status=review_required|failed` → blocked，不进入 generated。

## US-NVL-003 新增世界/章节

只加 storyworld/episodes 数据与 registry 注册；不改主链。
