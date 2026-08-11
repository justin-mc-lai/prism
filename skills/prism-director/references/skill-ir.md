# Skill IR — prism-director

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Turn frozen masters into treatment/storyboard/rhythm plans without inventing new facts.

## Triggers

- 导, 导演, treatment, 分镜, 节拍, prism-director

## Should not trigger

- 改写母稿事实、直接成片、自证 QA、跳过母稿冻结

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `prism-goal` | Multi-surface campaign loop only |
| Other `prism-*` | Different verb / stage; do not absorb |
| `beacon-*` | Engineering track, not content truth |

## Inputs

- User intent for `导`
- Upstream evidence / frozen refs when required by HARD GATE
- Constitution + registries + migration matrix

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: director`, `evidence_refs`, `recommended_next_harness`
- Artifacts under agreed content/evidence paths when produced

## Workflow (summary)

1. Confirm this is the correct public surface.
2. Load `treatment-director` mode file.
3. Apply MAP strategy: distill treatment/QC norms; defer heavy generators to Lake D
4. Do only `director` work; emit card + next harness.

## Failure modes

| Failure | Response |
|---------|----------|
| Wrong public surface | Hand off; do not stretch |
| Missing required evidence | Stop; list missing refs |
| Adapter name on human face | Rewrite human card |
| No frozen master ref | Stop; recommend prism-master |
| User wants final video now | Hand off produce after treatment accepted; do not generate AV here in Lake B′ |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure |
| `references/human-card-handoff.md` | Anti-leak |
| `references/adapter-migration-pointer.md` | MAP policy |
| `scripts/check_director_shell.sh` | Deterministic shell sanity |
| `evals/evals.json` | Trigger smoke |
| `manifest.json` | Maturity metadata |

## Trust / permission boundary

- No silent publish; no credential harvesting
- Bridge commands only when runtime exists; never invent results
- MAP ids MAP-002 only on machine face

## Eval plan

- Smoke: quick_validate + shell script
- Trigger positives/negatives in evals.json
- Graded with-skill vs baseline: **missing evidence**

## Promotion evidence

- Structure gates: quick_validate + check_director_shell
- Graded eval loop: **missing evidence**
