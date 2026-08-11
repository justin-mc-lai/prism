# Skill IR — prism-intel

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Produce an evidence-backed intel briefing for a topic/angle; never invent metrics or trends.

## Triggers

- 选, 选题, 信息差, 热点, briefing, prism-intel

## Should not trigger

- 全流程战役编排(用 prism-goal)、定母稿、导方案、产文、验收、发布

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `prism-goal` | Multi-surface campaign loop only |
| Other `prism-*` | Different verb / stage; do not absorb |
| `beacon-*` | Engineering track, not content truth |

## Inputs

- User intent for `选`
- Upstream evidence / frozen refs when required by HARD GATE
- Constitution + registries + migration matrix

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: intel`, `evidence_refs`, `recommended_next_harness`
- Artifacts under agreed content/evidence paths when produced

## Workflow (summary)

1. Confirm this is the correct public surface.
2. Load `brief-intel` mode file.
3. Apply MAP strategy: bridge primary to qi_dev.sh intel-radar; distill briefing schema only
4. Do only `intel` work; emit card + next harness.

## Failure modes

| Failure | Response |
|---------|----------|
| Wrong public surface | Hand off; do not stretch |
| Missing required evidence | Stop; list missing refs |
| Adapter name on human face | Rewrite human card |
| Radar/bridge unavailable | Stop; label missing runtime; do not fabricate signals |
| User asks for guaranteed hotness scores | Refuse; provide qualitative evidence paths only |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure |
| `references/human-card-handoff.md` | Anti-leak |
| `references/adapter-migration-pointer.md` | MAP policy |
| `scripts/check_intel_shell.sh` | Deterministic shell sanity |
| `evals/evals.json` | Trigger smoke |
| `manifest.json` | Maturity metadata |

## Trust / permission boundary

- No silent publish; no credential harvesting
- Bridge commands only when runtime exists; never invent results
- MAP ids MAP-003 only on machine face

## Eval plan

- Smoke: quick_validate + shell script
- Trigger positives/negatives in evals.json
- Graded with-skill vs baseline: **missing evidence**

## Promotion evidence

- Structure gates: quick_validate + check_intel_shell
- Graded eval loop: **missing evidence**
