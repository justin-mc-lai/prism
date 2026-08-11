# Skill IR — prism-produce

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Produce presentation variants strictly from frozen masters and accepted director maps.

## Triggers

- 产, 成稿, 贴图, 视频稿, 展示变体, prism-produce

## Should not trigger

- 冻结母稿、独立验收自证、公开发布、无母稿开写

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `prism-goal` | Multi-surface campaign loop only |
| Other `prism-*` | Different verb / stage; do not absorb |
| `beacon-*` | Engineering track, not content truth |

## Inputs

- User intent for `产`
- Upstream evidence / frozen refs when required by HARD GATE
- Constitution + registries + migration matrix

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: produce`, `evidence_refs`, `recommended_next_harness`
- Artifacts under agreed content/evidence paths when produced

## Workflow (summary)

1. Confirm this is the correct public surface.
2. Load `form-produce` mode file.
3. Apply MAP strategy: distill+bridge writing/人话; defer account/AV chains; never vendor-copy wholesale
4. Do only `produce` work; emit card + next harness.

## Failure modes

| Failure | Response |
|---------|----------|
| Wrong public surface | Hand off; do not stretch |
| Missing required evidence | Stop; list missing refs |
| Adapter name on human face | Rewrite human card |
| Missing master freeze | Stop; recommend prism-master |
| Form producer deferred (MAP-006/007) | Label defer; offer bridge if installed, else stop |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure |
| `references/human-card-handoff.md` | Anti-leak |
| `references/adapter-migration-pointer.md` | MAP policy |
| `scripts/check_produce_shell.sh` | Deterministic shell sanity |
| `evals/evals.json` | Trigger smoke |
| `manifest.json` | Maturity metadata |

## Trust / permission boundary

- No silent publish; no credential harvesting
- Bridge commands only when runtime exists; never invent results
- MAP ids MAP-005, MAP-006, MAP-007 only on machine face

## Eval plan

- Smoke: quick_validate + shell script
- Trigger positives/negatives in evals.json
- Graded with-skill vs baseline: **missing evidence**

## Promotion evidence

- Structure gates: quick_validate + check_produce_shell
- Graded eval loop: **missing evidence**
