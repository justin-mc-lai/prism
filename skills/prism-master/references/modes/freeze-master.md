# Mode: freeze-master

Freeze FactMaster and/or StoryMaster with evidence

## When to use

- User intent matches human verb **定** / triggers: 定, 母稿, 正典, FactMaster, StoryMaster, 冻结, prism-master

## When not to use

- 选题调研、导演分镜、形态生产、QA 自证、公开发布

## Procedure

1. Restate the `master` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-004 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `director` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: distill MASTER freeze rules; content data may bridge until Prism content/ exists
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: freeze-master
public_id: master
lane: standard|fast|canon
recommended_next_harness: director
map_ids_considered: ['MAP-004']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- Kernel under `skills/_internal/orchestration/` when routing conflicts
