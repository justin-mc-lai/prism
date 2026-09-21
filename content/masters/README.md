# content/masters

Master（母稿）根目录。母稿是**事实与正典的唯一权威**，任何展示变体不得新增母稿没有的事实。

## 结构

```text
content/masters/{vertical}/{slug}/
  meta.yaml      # 必填：vertical / slug / title / kind
  MASTER.md      # 必填：canonical authority body
  briefing.md    # 可选：选题/来源简报
  humanized.md   # 可选：成稿
  assets/        # 可选：配图/素材
```

## 规则

- `kind: fact` — 事实型母稿，必须带 `source_refs` + `canonical_claims` + 来源证据。
- `kind: story` — 叙事型母稿，必须引用 StoryWorld 或 canon ledger（`story_kind_requires_world_or_canon_ref`）。
- **无来源不得新增主张**（`no_new_claims_without_source_trace`）。
- 冻结规则见 `contracts/master-freeze-checklist.md`（Lake C 深化 MAP-004）。
- 落盘形状见 `contracts/master-content.schema.yaml`。

## 示例

`_examples/` 下的样例只用于校验 schema，**不是可发布内容**：
- `_examples/fact-sample/` — 事实型母稿最小形状
- `_examples/story-sample/` — 叙事型母稿最小形状（引用 StoryWorld）

## 现有母稿

| vertical | slug | kind | 状态 |
|---|---|---|---|
| ai-coding | ai-coding | fact | draft |

StoryWorld 见 `content/storyworlds/`；发行编排见 `content/distribution/`。
