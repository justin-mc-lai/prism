---
name: prism-master
description: >
  Prism public master surface. Human verb: 定. Beacon design alias: truth.
  FactMaster/StoryMaster freeze authority for content truth. Triggers: 定, 母稿, 正典, FactMaster, StoryMaster, 冻结, prism-master.
  资产提取支线：提取人物, 提取场景, 提取道具, 拆角色, 拆场景, 拆道具, 小说资产.
  Hard gate: 事实或正典未核完不冻结；展示变体不得新增事实/正典.
  Do not use for: 选题调研、导演分镜、形态生产、QA 自证、公开发布. Adapters stay internal-only. Lake B′ production sample.
metadata:
  version: "v0.0.1"
  brand: Prism
  public_surface: true
  public_id: "master"
  scheme: "A-1plus6"
  beacon_alias: "truth"
  lake: "B"
  operating_mode: production
  skill_ir: references/skill-ir.md
---

# prism-master

**Public surface**: `master` · **Brand**: Prism（棱镜） · **Human verb**: 定  
**Beacon design alias**: truth（不对人暴露为 Prism 公开面名）  
**Operating mode**: production sample (qi-dev-skill-creator)

## HARD GATE

事实或正典未核完不冻结；展示变体不得新增事实/正典

Shared preamble:

1. Lake vs sea — boil lakes; split/defer seas.
2. Search before invent — constitution, registry, evidence first.
3. User sovereignty on publish and freeze.
4. No fake delivery (placeholder, docs-only, zero assertions).
5. Harness boundaries — maker ≠ checker; release always human gate.

## Canonical workspace

- Constitution: `docs/beacon/v0.0.1/constitution/prism-constitution.md`
- Public registry: `registry/public-surface.yaml`
- Adapter index: `registry/adapter-index.yaml`
- Migration matrix: `registry/adapter-migration-matrix.md`
- Orchestration kernel: `skills/_internal/orchestration/`
- Human card: `contracts/human-card.md`
- Seven-seg template: `contracts/skill-contract-7seg.tpl.md`
- Adapter stubs: `skills/_internal/adapters/` (internal only)

## Mandatory progressive load

1. Select **exactly one** primary `mode_id` from the table.
2. **Read the mode file completely** before acting.
3. Open nested refs only when the mode file links them.
4. Emit output contract + human card + `recommended_next_harness`.
5. Stop at harness boundary; route to another public core instead of stretching this one.

| mode_id | Load file | Purpose |
|---------|-----------|---------|
| `freeze-master` | `references/modes/freeze-master.md` | Freeze FactMaster and/or StoryMaster with evidence |
| `extract-storyworld` | `references/modes/extract-storyworld.md` | Extract reusable asset roster (characters/scenes/props) from novel/script/outline |

Index: `references/modes/INDEX.md`  
Skill IR: `references/skill-ir.md`

## Workflow

1. Classify request → primary mode (or hand off if wrong surface).
2. Read migration strategy for MAP-004 in `registry/adapter-migration-matrix.md`.
3. Execute this surface's job only; bind evidence paths.
4. Recommend next public harness; never claim another harness's job done.

## Output contract (minimum)

- Human card: `## 这次做了什么` / `## 需要你决定` / `## 下一步`
- `mode_id` (required)
- `public_id`: `master`
- `lane`: `fast` | `standard` | `canon` (inherit from campaign when present)
- `evidence_refs`
- `recommended_next_harness`: one of `goal|intel|master|director|produce|qa|release|stop`
- Machine face may cite `map_id`; human face must not name adapters

## Boundaries

- Strategy now: distill MASTER freeze rules; content data may bridge until Prism content/ exists
- Do not implement deferred Lake D form producer bodies inside this shell.
- Do not vendor-copy third-party packs wholesale.
- Do not leak `_internal` adapter skill names on the human face.
- Do not approve public publish unless this is `release` **and** human confirmation is recorded.

## Verification

```bash
python3 /Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py skills/prism-master
bash skills/prism-master/scripts/check_master_shell.sh
```

## Failure handling

See `references/skill-ir.md` failure table. Default: stop, emit human card with decision, keep evidence paths honest.

## Resources

- `references/skill-ir.md` — semantic contract
- `references/modes/` — mode progressive disclosure
- `references/human-card-handoff.md` — anti-leak card checklist
- `references/adapter-migration-pointer.md` — MAP matrix pointer
- `evals/evals.json` — smoke / trigger evals
- `scripts/check_master_shell.sh` — shell sanity
- `manifest.json` — maturity metadata
- `agents/openai.yaml` — Codex/OpenAI UI metadata
