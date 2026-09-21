# Skill IR — prism-master

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Own content-truth freeze for FactMaster/StoryMaster; block freeze when facts/canon incomplete.
Own asset extraction from novel/script/outline into the reusable roster (characters/scenes/props) that feeds StoryWorld and storyboard.

## Triggers

- 定, 母稿, 正典, FactMaster, StoryMaster, 冻结, prism-master
- 提取人物, 提取场景, 提取道具, 拆角色, 拆场景, 拆道具, 小说资产

## Should not trigger

- 选题调研、导演分镜、形态生产、QA 自证、公开发布

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `prism-goal` | Multi-surface campaign loop only |
| Other `prism-*` | Different verb / stage; do not absorb |
| `beacon-*` | Engineering track, not content truth |

## Inputs

- User intent for `定`
- Upstream evidence / frozen refs when required by HARD GATE
- Constitution + registries + migration matrix

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: master`, `evidence_refs`, `recommended_next_harness`
- Artifacts under agreed content/evidence paths when produced

## Workflow (summary)

1. Confirm this is the correct public surface.
2. Load `freeze-master` or `extract-storyworld` mode file.
3. Apply MAP strategy: distill MASTER freeze rules; content data may bridge until Prism content/ exists
4. Do only `master` work; emit card + next harness.

## Failure modes

| Failure | Response |
|---------|----------|
| Wrong public surface | Hand off; do not stretch |
| Missing required evidence | Stop; list missing refs |
| Adapter name on human face | Rewrite human card |
| Unresolved fact conflicts | Do not freeze; list conflicts and required sources |
| Request to freeze from produce output alone | Refuse; master precedes produce |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure |
| `references/human-card-handoff.md` | Anti-leak |
| `references/adapter-migration-pointer.md` | MAP policy |
| `scripts/check_master_shell.sh` | Deterministic shell sanity |
| `evals/evals.json` | Trigger smoke |
| `manifest.json` | Maturity metadata |

## Trust / permission boundary

- No silent publish; no credential harvesting
- Bridge commands only when runtime exists; never invent results
- MAP ids MAP-004 only on machine face

## Eval plan

- Smoke: quick_validate + shell script
- Trigger positives/negatives in evals.json
- Graded with-skill vs baseline: **missing evidence**

## Promotion evidence

- Structure gates: quick_validate + check_master_shell
- Graded eval loop: **missing evidence**
