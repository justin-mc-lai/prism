# Human card handoff checklist — prism-qa

Canonical template: `contracts/human-card.md`

## Before emit

1. Use public verb **验** only on the human face.
2. Strip `_internal`, `adapter-*`, `selfmedia-*`, vendor package names from human text.
3. Put `map_id` / bridge commands only on machine face.
4. List `evidence_refs` or explicit missing list.

## Machine face minimum

```yaml
mode_id: gate-qa
lane: standard
public_id: qa
evidence_refs: []
recommended_next_harness: release
```
