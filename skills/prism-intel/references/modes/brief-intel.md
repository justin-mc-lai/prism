# Mode: brief-intel

Evidence-backed topic/angle briefing via bridge + schema

## When to use

- User intent matches human verb **选** / triggers: 选, 选题, 信息差, 热点, briefing, prism-intel

## When not to use

- 全流程战役编排(用 prism-goal)、定母稿、导方案、产文、验收、发布

## Procedure

1. Restate the `intel` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-003 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `master` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: bridge primary to qi_dev.sh intel-radar; distill briefing schema only
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: brief-intel
public_id: intel
lane: standard|fast|canon
recommended_next_harness: master
map_ids_considered: ['MAP-003']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Bridge recipe (when runtime available)

```bash
qi_dev.sh intel-radar doctor
qi_dev.sh intel-radar deep-plan "<topic>" --save
```

If bridge unavailable: stop with missing-evidence label; do not fabricate.
