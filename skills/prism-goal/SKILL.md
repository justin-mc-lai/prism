---
name: prism-goal
description: >
  Prism public goal surface for long-run content campaigns and series.
  Use when the user wants 做/连载/战役/长跑/全流程 across Prism public surfaces
  (intel→master→director→produce→qa→release) with lane choice and evidence binding.
  Triggers: 做, 连载, 战役, prism-goal, campaign loop, multi-surface sequencing.
  Do not use for single-step 选题/定稿/导/产/验/发 alone, Beacon engineering goal,
  or claiming full sea-level creation capability. Adapters stay internal-only.
metadata:
  version: "v0.0.1"
  brand: Prism
  public_surface: true
  public_id: "goal"
  scheme: "A-1plus6"
  beacon_alias: "goal"
  lake: "B"
  operating_mode: production
  skill_ir: references/skill-ir.md
---

# prism-goal

**Public surface**: `goal` · **Brand**: Prism（棱镜） · **Human verb**: 做/连载  
**Beacon design alias**: goal（不对人暴露为 Prism 公开面名）  
**Operating mode**: production sample (qi-dev-skill-creator)

## HARD GATE

Orchestrate content campaign loops only. Complete needs verifier evidence. Release always human gate. Long-run only on goal. Goal does not count as a 7th content harness.

Shared preamble:

1. Lake vs sea — boil lakes; split/defer seas.
2. Search before invent — constitution, registry, evidence first.
3. User sovereignty on publish and freeze.
4. No fake delivery (placeholder, docs-only, zero assertions).
5. Harness boundaries — maker ≠ checker; goal never issues QA/release verdicts.

## Canonical workspace

- Constitution: `docs/beacon/v0.0.1/constitution/prism-constitution.md`
- Public registry: `registry/public-surface.yaml`
- Adapter index: `registry/adapter-index.yaml`
- Migration matrix: `registry/adapter-migration-matrix.md`
- Orchestration kernel: `skills/_internal/orchestration/`
- Human card: `contracts/human-card.md`
- Seven-seg template: `contracts/skill-contract-7seg.tpl.md`

## Mandatory progressive load

1. Select **exactly one** primary `mode_id` from the table.
2. **Read the mode file completely** before acting.
3. Open nested refs only when the mode file links them.
4. Emit output contract + human card + `recommended_next_harness`.
5. Stop at harness boundary; route to another public core instead of stretching goal.

| mode_id | Load file | Purpose |
|---------|-----------|---------|
| `loop-campaign` | `references/modes/loop-campaign.md` | Cross-surface campaign / series orchestration |
| `marketing-engineer` | `references/modes/marketing-engineer.md` | Post-release loop: 出圈 + measured→review→learn→下一轮 |

Index: `references/modes/INDEX.md`  
Skill IR: `references/skill-ir.md`

## Workflow

1. Classify request → primary mode (or hand off to a single public surface).
2. Choose `lane`: `fast` | `standard` | `canon` (see mode file).
3. Read constitution + registries when routing is ambiguous.
4. Produce orchestration artifacts for this turn only.
5. Recommend next public harness; never claim another harness’s job done.

## Content lanes (summary)

```text
fast:     goal → produce → qa → release   (requires fast_lane_skip annotation)
standard: intel → master → director → produce → qa → release
canon:    goal → master → director → produce → qa → release → goal review
```

## Output contract (minimum)

- Human card: `## 这次做了什么` / `## 需要你决定` / `## 下一步`
- `mode_id` (required)
- `public_id`: `goal`
- `lane`: `fast` | `standard` | `canon`
- `evidence_refs`
- `recommended_next_harness`: one of `goal|intel|master|director|produce|qa|release|stop`
- Machine face may cite `map_id`; human face must not name adapters

## Boundaries

- Do not implement form producer chains (Lake D).
- Do not vendor-copy third-party packs from selfmedia-creator in this skill.
- Do not invent intel metrics/trends; route to `prism-intel` / bridge.
- Do not approve public publish; only `prism-release` + human confirmation.
- Do not leak `_internal` adapter skill names on the human face.

## Verification

```bash
python3 /Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py skills/prism-goal
bash skills/prism-goal/scripts/check_goal_shell.sh
# all 1+6 public surfaces:
bash scripts/check_all_public_surfaces.sh
```

## Failure handling

See `references/skill-ir.md` failure table. Default: stop, emit human card with decision, keep evidence paths honest.

## Resources

- `references/skill-ir.md` — semantic contract
- `references/modes/` — mode progressive disclosure
- `references/human-card-handoff.md` — anti-leak card checklist
- `references/adapter-migration-pointer.md` — MAP matrix pointer
- `evals/evals.json` — smoke / trigger evals
- `scripts/check_goal_shell.sh` — shell sanity
- `manifest.json` — maturity metadata
- `agents/openai.yaml` — Codex/OpenAI UI metadata
