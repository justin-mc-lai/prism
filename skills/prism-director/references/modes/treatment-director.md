# Mode: treatment-director

Director treatment / presentation map from frozen masters

## When to use

- User intent matches human verb **导** / triggers: 导, 导演, treatment, 分镜, 节拍, prism-director

## When not to use

- 改写母稿事实、直接成片、自证 QA、跳过母稿冻结

## Procedure

1. Restate the `director` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-002 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `produce` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

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
- Kernel under `skills/_internal/orchestration/` when routing conflicts
