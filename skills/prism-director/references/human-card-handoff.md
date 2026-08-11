# Human card handoff checklist — prism-director

Canonical template: `contracts/human-card.md`

## Before emit

1. Use public verb **导** only on the human face.
2. Strip `_internal`, `adapter-*`, `selfmedia-*`, vendor package names from human text.
3. Put `map_id` / bridge commands only on machine face.
4. List `evidence_refs` or explicit missing list.

## Machine face minimum

```yaml
mode_id: treatment-director
lane: standard
public_id: director
evidence_refs: []
recommended_next_harness: produce
```
