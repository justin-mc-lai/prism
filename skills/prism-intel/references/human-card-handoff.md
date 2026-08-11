# Human card handoff checklist — prism-intel

Canonical template: `contracts/human-card.md`

## Before emit

1. Use public verb **选** only on the human face.
2. Strip `_internal`, `adapter-*`, `selfmedia-*`, vendor package names from human text.
3. Put `map_id` / bridge commands only on machine face.
4. List `evidence_refs` or explicit missing list.

## Machine face minimum

```yaml
mode_id: brief-intel
lane: standard
public_id: intel
evidence_refs: []
recommended_next_harness: master
```
