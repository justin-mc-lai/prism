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
- Kernel under `skills/_internal/orchestration/` when routing conflicts
