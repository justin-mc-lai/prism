# Skill IR — prism-qa

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Independently verify produce artifacts against masters and gates; fail closed without evidence.

## Triggers

- 验, 验收, anti-slop, 事实核对, 视觉门, prism-qa

## Should not trigger

- 代写正文、代发、用生产结果自证、跳过证据

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `prism-goal` | Multi-surface campaign loop only |
| Other `prism-*` | Different verb / stage; do not absorb |
| `beacon-*` | Engineering track, not content truth |

## Inputs

- User intent for `验`
- Upstream evidence / frozen refs when required by HARD GATE
- Constitution + registries + migration matrix

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: qa`, `evidence_refs`, `recommended_next_harness`
- Artifacts under agreed content/evidence paths when produced

## Workflow (summary)

1. Confirm this is the correct public surface.
2. Load `gate-qa` mode file.
3. Apply MAP strategy: distill gate checklists; checker ≠ maker
4. Do only `qa` work; emit card + next harness.

## Failure modes

| Failure | Response |
|---------|----------|
| Wrong public surface | Hand off; do not stretch |
| Missing required evidence | Stop; list missing refs |
| Adapter name on human face | Rewrite human card |
| Maker asks to self-certify | Refuse; require separate evidence |
| Missing gate evidence | status=fail; recommend produce repair or stop |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure |
| `references/human-card-handoff.md` | Anti-leak |
| `references/adapter-migration-pointer.md` | MAP policy |
| `scripts/check_qa_shell.sh` | Deterministic shell sanity |
| `evals/evals.json` | Trigger smoke |
| `manifest.json` | Maturity metadata |

## Trust / permission boundary

- No silent publish; no credential harvesting
- Bridge commands only when runtime exists; never invent results
- MAP ids MAP-005 only on machine face

## Eval plan

- Smoke: quick_validate + shell script
- Trigger positives/negatives in evals.json
- Graded with-skill vs baseline: **missing evidence**

## Promotion evidence

- Structure gates: quick_validate + check_qa_shell
- Graded eval loop: **missing evidence**
