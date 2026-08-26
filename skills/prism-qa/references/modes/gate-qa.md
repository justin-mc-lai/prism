# Mode: gate-qa

Independent multi-gate verification with evidence paths

## When to use

- User intent matches human verb **验** / triggers: 验, 验收, anti-slop, 事实核对, 视觉门, prism-qa

## When not to use

- 代写正文、代发、用生产结果自证、跳过证据

## Procedure

1. Restate the `qa` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-005 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `release` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: distill gate checklists; checker ≠ maker
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: gate-qa
public_id: qa
lane: standard|fast|canon
recommended_next_harness: release
map_ids_considered: ['MAP-005']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../anti-slop-gate.md` — slop 模式清单 + 场景档位 + 仲裁顺序（qa 主清单）
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Gate set (minimum)

- anti-slop / 人话 (distill checklist; bridge humanizer if installed)
- fact alignment vs frozen master
- visual/platform evidence when media present
- fail-closed if any required evidence path missing
