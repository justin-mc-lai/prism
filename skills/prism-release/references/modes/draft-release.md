# Mode: draft-release

Draft handoff and human-gated publish/schedule

## When to use

- User intent matches human verb **发** / triggers: 发, 草稿, 发布, 定时, release, prism-release

## When not to use

- 无 QA 放行、静默公开发布、跳过人工批准、改母稿

## Procedure

1. Restate the `release` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-008 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `stop` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: bridge draft tools; defer vendor sync-ai pin; human approval always
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: draft-release
public_id: release
lane: standard|fast|canon
recommended_next_harness: stop
map_ids_considered: ['MAP-008']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Human approval gate

- `draft` actions may proceed with recorded intent.
- `publish` / `schedule` require explicit human confirmation in the card decision section.
- Read `skills/_internal/orchestration/publish-approval.md` before any public action.
