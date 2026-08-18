# Mode: treatment-director

Director treatment / presentation map from frozen masters

## When to use

- User intent matches human verb **导** / triggers: 导, 导演, treatment, 分镜, 节拍, prism-director

## When not to use

- 改写母稿事实、直接成片、自证 QA、跳过母稿冻结

## Procedure

1. Restate the `director` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-002 strategy in `registry/adapter-migration-matrix.md`.
3. Read `../director-philosophy.md`（意图第一性 + 叙事系统）before acting.
4. Produce treatment per `../treatment-template.md`; score per `../qc-scorecard.md`.
5. Execute only this surface; write/read evidence paths explicitly.
6. Default `recommended_next_harness`: `produce` unless blocked.
7. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: distill treatment/QC norms; defer heavy generators to Lake D
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: treatment-director
public_id: director
lane: standard|fast|canon
recommended_next_harness: produce
map_ids_considered: ['MAP-002']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../director-philosophy.md` — 顶层公理/叙事系统/自媒体适配
- `../treatment-template.md` — treatment 核心模板 + 验收清单
- `../qc-scorecard.md` — 13 维评分卡 + 生产门 + 自动阻断
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Director 侧硬门（Lake B′ 蒸馏后）

1. 无一句话核心意图 + 目标受众 → 不产出完整 treatment，一次只问一个关键问题。
2. 事实/创意解读必须分栏标注；无源主张不得进入变体。
3. 产出必带 treatment 验收清单自评 + QC 评分；<45 分不得交接 produce。
