# Human card handoff checklist

Canonical template: `contracts/human-card.md`

## Before emit

1. Fill human sections with public verbs only (`选/定/导/产/验/发/做`).
2. Strip any `_internal`, `adapter-*`, `selfmedia-*`, vendor package names from human text.
3. Put `map_id` / bridge command only in machine face if needed.
4. Every advance lists concrete `evidence_refs` or an explicit missing list.

## Machine face minimum

```yaml
mode_id: loop-campaign
lane: standard
public_id: goal
evidence_refs: []
recommended_next_harness: intel
fsm_transition: idle->route_next_public_surface
transaction_ref: ""
```

## Anti-leak test

If a non-operator reader can see an internal skill path in the human card, rewrite before delivery.
