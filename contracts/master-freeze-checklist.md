# Master Freeze Checklist

Lake C deepens `MAP-004` by making MASTER freeze rules explicit for Prism-native `content/masters/`.

## Required before freeze

- `meta.yaml` exists and names `vertical`, `slug`, `title`, and `kind`
- `MASTER.md` exists and is the canonical authority body
- `kind=fact` carries source trace or claim provenance
- `kind=story` references a `world_slug` or equivalent canon anchor
- human-facing title and one-line intent are stable

## Canon guards

- StoryMaster episode cannot move to generated content before canon gate passes
- World bible and canon ledger outrank presentation variants
- New presentation forms may translate the master but may not add canon

## MAP-004 outcome

- status: `distilled_schema`
- deepen_lake: `C`
- landing: `prism-master`
