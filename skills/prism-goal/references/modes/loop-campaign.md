# Mode: loop-campaign

Cross-surface Prism campaign / series / review orchestration.

## When to use

- User wants 连载、战役、长跑、全流程 across more than one public surface
- Need lane choice (`fast` | `standard` | `canon`) and evidence binding between stages
- Resume after a prior human-card handoff

## When not to use

- Single public-surface request (hand off immediately)
- Beacon engineering delivery (`beacon-goal`)
- Asking goal to write copy, freeze masters, or publish

## Lane selection

| Lane | Sequence | Guard |
|------|----------|-------|
| `standard` | intel → master → director → produce → qa → release | Default when unsure |
| `fast` | goal → produce → qa → release | Requires explicit `fast_lane_skip` annotation + risk allows |
| `canon` | goal → master → director → produce → qa → release → goal review | World/bible / positive canon at stake |

Read kernel when sequence is ambiguous:

- `skills/_internal/orchestration/skill-routing.md`
- `skills/_internal/orchestration/quality-gates.md`
- `skills/_internal/orchestration/creation-mode-map.md`
- `skills/_internal/orchestration/pipeline-contract.md`
- `skills/_internal/orchestration/publish-approval.md`

## State machine (governor only)

```text
idle
  → classify_lane
  → route_next_public_surface
  → await_surface_evidence
  → (repeat) | human_decision_required | release_gate
release_gate → human_confirmed → done | human_rejected → idle
```

Goal never executes maker/checker/release verdicts. It only routes and records.

## Turn procedure

1. Restate campaign intent in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Select lane; if `fast`, require skip annotation in machine face.
3. Name **one** `recommended_next_harness` from public registry ids.
4. List required evidence for that handoff (paths or missing).
5. Emit human card + machine face; stop.

For Lake C+ campaign work, prefer these dossier anchors when present:

- `content/distribution/campaigns/{campaign_id}.yaml`
- `content/distribution/bindings/{binding_id}.yaml`
- `content/storyworlds/{world_slug}/`
- `content/masters/{vertical}/{slug}/`

## Adapter policy

- Resolve producers via `registry/adapter-migration-matrix.md` strategies (`bridge` | `distill` | `vendor_pin` | `defer`).
- Prefer `bridge` / `distill` until Lake D opens `vendor_pin`.
- Human face: public surface verbs only. Machine face: optional `map_id`.

## Output extras for this mode

```yaml
mode_id: loop-campaign
lane: standard|fast|canon
fast_lane_skip: false
recommended_next_harness: intel|master|director|produce|qa|release|stop
map_ids_considered: []   # machine face only
deferred_lakes: [C, D, E, F]  # when relevant
```

## Nested refs (load on demand)

- `../human-card-handoff.md` — before emitting the card
- `../adapter-migration-pointer.md` — when choosing bridge vs distill vs defer
- Kernel files under `skills/_internal/orchestration/` — when routing conflicts
