# Form contract: novel（Lake D4 · 连载）

> 形态契约。正典规则继承 Lake A FP-PRISM-003 / Lake C narrative-episode schema。

## 1. identity

- form_id: novel
- 定位: 连载小说/漫画脚本（episode 制）
- lane: canon|standard（canon 禁用 fast_lane_skip）
- bridge: `vendor/skills/kushi-narrative-zh`（A4 pin · 缺失 → blocked）

## 2. 决策边界

- 能决定：episode 结构、叙事执行、bridge 选择
- 不能决定：正典事实、canon_gate 判定、QA 判定、公开发布

## 3. intake（必填）

- StoryMaster（world bible + canon ledger，`content/storyworlds/{world_slug}/`）
- director episode outline（sequence + 冲突 + 节奏）

拒绝：无 StoryMaster / 无 outline / `vendor/skills/kushi-narrative-zh` 缺失 → blocked + reason_code

## 4. output

- 章节: `content/storyworlds/{world_slug}/episodes/{episode_id}.yaml` + 正文草稿
- 证据: `.beacon/evidence/implement/prism-form-novel-v1/AC-NVL-002.json`
- 头部: episode_id + world_slug + master_id + sequence + canon_gate_status

## 5. gate（正典门）

- `canon_gate_status` 三态：review_required / passed / failed
- `review_required` 或 `failed` → **不得进入 generated**（illegal）
- OOC / 设定漂移 → 按事实错误 fail-closed（引用 canon ledger 证据）
- bible/canon ledger 高于展示变体；变体不得新增正典
- QA 每项结论引用原文行 + 证据路径

## 6. handoff

- 下一公开面: prism-qa（正典/连续性/anti-slop-gate）→ prism-release

## 7. 失败处理

- 可重试: 叙事稿、episode 结构、换 bridge
- 必须停: 正典未过（canon_gate_status≠passed）、事实无源、发布批准
- 禁止自证通过: true
