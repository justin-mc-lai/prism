# content/storyworlds

StoryWorld（世界圣经）根目录。世界圣经与 canon ledger **高于任何展示变体**；
变体只能转译，不得新增正典。

## 结构

```text
content/storyworlds/{world_slug}/
  world.yaml          # 必填：world_slug / title / canon_policy / default_lane
  bible.md            # 必填：世界设定正文
  canon-ledger.yaml   # 必填：正典条目账本（entries）
  characters/         # 必填：角色条目
  timeline/           # 必填：时间线
  episodes/           # 可选：分集（narrative-episode schema）
  scenes/             # 可选
  props/              # 可选
```

## 规则

- `default_lane` 必须是 `canon` 或 `standard`；`canon` 车道**禁用 fast-lane-skip**。
- `canon_policy` 走 fail-closed：正典未核完不得冻结。
- episode 未过正典门（`canon_gate_status=review_required|failed`）**不得进入 generated**。
- 落盘形状见 `contracts/storyworld.schema.yaml` 与 `contracts/narrative-episode.schema.yaml`。

## 示例

`_examples/demo-world/` 只用于校验 schema，**不是可发布内容**。

## 现有世界

| world_slug | 状态 |
|---|---|
| （暂无；novel 长跑题材启动时创建） | — |
