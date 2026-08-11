# Skill IR — prism-goal

Mode: `production` · Maturity: `production-sample` · Owner: Prism Lake B′

## Owned job

Cross-cutting long-run orchestration for Prism campaigns/series/reviews: choose lane, sequence public surfaces, bind evidence, stop at harness boundaries. Does not produce content, freeze masters, or publish.

## Triggers

- 做 / 连载 / 战役 / 长跑 / 全流程 / prism-goal / campaign loop
- Multi-surface sequencing when user wants more than one public harness

## Should not trigger

- Single-step 选题 → `prism-intel`
- 只定母稿 → `prism-master`
- 只导方案 → `prism-director`
- 只产形态 → `prism-produce`
- 只验收 → `prism-qa`
- 只发草稿/公开 → `prism-release`
- Beacon 工程交付 goal（`beacon-goal`）— 不同产品轨

## Near neighbors

| Neighbor | Boundary |
|----------|----------|
| `beacon-goal` | 工程 truth / 编码交付；Prism 是内容 truth |
| `prism-intel` | 单次选题/briefing，无跨面编排 |
| Lake D form producers | goal 只路由；不内嵌 producer 实现 |

## Inputs

- User campaign intent (topic / series / review)
- Optional: frozen master refs, prior evidence paths
- Constitution + registries always readable

## Outputs

- Human card (`contracts/human-card.md`)
- Machine face: `mode_id`, `lane`, `public_id: goal`, `evidence_refs`, `recommended_next_harness`
- Never leak adapter / internal skill names on the human face

## Workflow (summary)

1. Qualify lake vs sea; refuse sea-closure claims on Lake B/B′.
2. Select exactly one `mode_id` from `references/modes/INDEX.md`.
3. Load mode file; open nested refs only when linked.
4. Route to next public surface; do not stretch goal into maker/checker/release verdicts.
5. Emit output contract + human card.

## Failure modes

| Failure | Response |
|---------|----------|
| Ambiguous single-surface ask | Recommend the owning public surface; do not force loop |
| Missing evidence for advance | Stop; list missing refs |
| User asks to skip QA/publish approval | Refuse; cite HARD GATE |
| Adapter name on human face | Rewrite human card; keep map_id on machine face only |
| Request to vendor-copy all third parties now | Point to `registry/adapter-migration-matrix.md`; defer Lake D pins |

## Resources (why they earn weight)

| Path | Why |
|------|-----|
| `references/modes/*` | Progressive disclosure for orchestration variants |
| `references/human-card-handoff.md` | Anti-leak + card checklist |
| `references/adapter-migration-pointer.md` | Points to canonical MAP matrix |
| `scripts/check_goal_shell.sh` | Deterministic production-shell sanity |
| `evals/evals.json` | Trigger + boundary smoke |
| `manifest.json` | Maturity / owner / platforms |

## Trust / permission boundary

- No credentials, no publish APIs, no vendor install by default
- May read constitution, registry, orchestration, evidence paths
- Bridge commands (e.g. `qi_dev.sh intel-radar`) only when routing intel and user/runtime already has them — never invent scan results

## Eval plan

- Smoke: structure validate + shell script
- Trigger positives/negatives in `evals/evals.json`
- Missing: with-skill vs baseline graded runs (label: missing evidence until transcript runs exist)

## Promotion evidence

- Lake B extract QA passed for repo shells (separate feature evidence)
- This package: `quick_validate.py` pass + `scripts/check_goal_shell.sh` pass
- Graded eval loop: **missing evidence**
