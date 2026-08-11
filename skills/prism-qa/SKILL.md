---
name: prism-qa
description: >
  Prism public qa surface. Human verb: 验. Beacon design alias: qa.
  Independent gates: anti-slop, facts, visual, platform evidence. Triggers: 验, 验收, anti-slop, 事实核对, 视觉门, prism-qa.
  Hard gate: maker 不自证；缺证据不过；不得改写母稿正典来“修过”.
  Do not use for: 代写正文、代发、用生产结果自证、跳过证据. Adapters stay internal-only. Lake B′ production sample.
metadata:
  version: "v0.0.1"
  brand: Prism
  public_surface: true
  public_id: "qa"
  scheme: "A-1plus6"
  beacon_alias: "qa"
  lake: "B"
  operating_mode: production
  skill_ir: references/skill-ir.md
---

# prism-qa

**Public surface**: `qa` · **Brand**: Prism（棱镜） · **Human verb**: 验  
**Beacon design alias**: qa（不对人暴露为 Prism 公开面名）  
**Operating mode**: production sample (qi-dev-skill-creator)

## HARD GATE

maker 不自证；缺证据不过；不得改写母稿正典来“修过”

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
| `gate-qa` | `references/modes/gate-qa.md` | Independent multi-gate verification with evidence paths |

Index: `references/modes/INDEX.md`  
Skill IR: `references/skill-ir.md`

## Workflow

1. Classify request → primary mode (or hand off if wrong surface).
2. Read migration strategy for MAP-005 in `registry/adapter-migration-matrix.md`.
3. Execute this surface's job only; bind evidence paths.
4. Recommend next public harness; never claim another harness's job done.

## Output contract (minimum)

- Human card: `## 这次做了什么` / `## 需要你决定` / `## 下一步`
- `mode_id` (required)
- `public_id`: `qa`
- `lane`: `fast` | `standard` | `canon` (inherit from campaign when present)
- `evidence_refs`
- `recommended_next_harness`: one of `goal|intel|master|director|produce|qa|release|stop`
- Machine face may cite `map_id`; human face must not name adapters

## Boundaries

- Strategy now: distill gate checklists; checker ≠ maker
- Do not implement deferred Lake D form producer bodies inside this shell.
- Do not vendor-copy third-party packs wholesale.
- Do not leak `_internal` adapter skill names on the human face.
- Do not approve public publish unless this is `release` **and** human confirmation is recorded.

## Verification

```bash
python3 /Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py skills/prism-qa
bash skills/prism-qa/scripts/check_qa_shell.sh
```

## Failure handling

See `references/skill-ir.md` failure table. Default: stop, emit human card with decision, keep evidence paths honest.

## Resources

- `references/skill-ir.md` — semantic contract
- `references/modes/` — mode progressive disclosure
- `references/human-card-handoff.md` — anti-leak card checklist
- `references/adapter-migration-pointer.md` — MAP matrix pointer
- `evals/evals.json` — smoke / trigger evals
- `scripts/check_qa_shell.sh` — shell sanity
- `manifest.json` — maturity metadata
- `agents/openai.yaml` — Codex/OpenAI UI metadata
