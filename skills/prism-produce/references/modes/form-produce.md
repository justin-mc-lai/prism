# Mode: form-produce

Produce one presentation form from frozen master + director map

## When to use

- User intent matches human verb **产** / triggers: 产, 成稿, 贴图, 视频稿, 展示变体, prism-produce

## When not to use

- 冻结母稿、独立验收自证、公开发布、无母稿开写

## Procedure

1. Restate the `produce` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-005, MAP-006, MAP-007 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `qa` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: distill+bridge writing/人话; defer account/AV chains; never vendor-copy wholesale
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: form-produce
public_id: produce
lane: standard|fast|canon
recommended_next_harness: qa
map_ids_considered: ['MAP-005', 'MAP-006', 'MAP-007']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../prose-core.md` — 文笔五原则执行版（成稿底线）
- `../human-voice-prose.md` — 说人话层三道门（材料/位置/禁令）+ 裁决表 + 改稿七遍
- `../humanize-techniques.md` — 人味手法 + 平台差异 + 降套路提示词
- `../personal-style-layer.md` — 个人文风层（WRITING.md + 修改学习 + 作者信息密度）
- `../emotional-essay-archetype.md` — 情绪观点长文体裁（7 拍 + 8 硬规则 + 判别开关）
- `../oss-daily-archetype.md` — 日榜体裁（倒金字塔，禁四段式）
- `../visual-enrich.md` — 深度稿截图充实（来源优先级 + 图说引导 + manifest）
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Produce 侧硬门（Lake B′ 深蒸馏后）

1. 现实稿 ≥1200 字：先过材料门（≥5 件可溯源材料），不足只能研究/追问/缩题。
2. 动笔前过说话位置五问；答案留后台，不展示给读者。
3. 成稿后跑 `python3 scripts/check_human_voice.py <稿>`：失败项清零，提醒项按
   `human-voice-prose.md` §6 裁决表人工处理，豁免项逐条记入 humanize 证据。
4. 人味层 bridge 命中缺失时 `blocked` + `reason_code=bridge_tool_missing`
   （安装通道：`bash scripts/install_writing_bridges.sh`）。
5. 有 `content/writing-style.md` 或单篇 style.md 时，成稿须过个人文风层
   （`../personal-style-layer.md`）；无 style 文件不阻断，但要在 human card 写明
   「个人文风层未启用」。
