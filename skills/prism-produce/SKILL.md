---
name: prism-produce
description: >
  Prism public produce surface. Human verb: 产. Beacon design alias: implement.
  Presentation production routed by form registry and adapter strategies. Triggers: 产, 成稿, 贴图, 视频稿, 展示变体, prism-produce.
  Hard gate: 只按已冻结母稿生产；不得新增事实/正典.
  Do not use for: 冻结母稿、独立验收自证、公开发布、无母稿开写. Adapters stay internal-only. Lake B′ production sample.
metadata:
  version: "v0.0.1"
  brand: Prism
  public_surface: true
  public_id: "produce"
  scheme: "A-1plus6"
  beacon_alias: "implement"
  lake: "B"
  operating_mode: production
  skill_ir: references/skill-ir.md
---

# prism-produce

**Public surface**: `produce` · **Brand**: Prism（棱镜） · **Human verb**: 产  
**Beacon design alias**: implement（不对人暴露为 Prism 公开面名）  
**Operating mode**: production sample (qi-dev-skill-creator)

## HARD GATE

只按已冻结母稿生产；不得新增事实/正典

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
| `form-produce` | `references/modes/form-produce.md` | Produce one presentation form from frozen master + director map |

Index: `references/modes/INDEX.md`  
Skill IR: `references/skill-ir.md`

## Workflow

1. Classify request → primary mode (or hand off if wrong surface).
2. Read migration strategy for MAP-005, MAP-006, MAP-007 in `registry/adapter-migration-matrix.md`.
3. Execute this surface's job only; bind evidence paths.
4. Recommend next public harness; never claim another harness's job done.

## Output contract (minimum)

- Human card: `## 这次做了什么` / `## 需要你决定` / `## 下一步`
- `mode_id` (required)
- `public_id`: `produce`
- `lane`: `fast` | `standard` | `canon` (inherit from campaign when present)
- `evidence_refs`
- `recommended_next_harness`: one of `goal|intel|master|director|produce|qa|release|stop`
- Machine face may cite `map_id`; human face must not name adapters

## Boundaries

- Strategy now: distill+bridge writing/人话; defer account/AV chains; never vendor-copy wholesale
- Do not implement deferred Lake D form producer bodies inside this shell.
- Do not vendor-copy third-party packs wholesale.
- Do not leak `_internal` adapter skill names on the human face.
- Do not approve public publish unless this is `release` **and** human confirmation is recorded.

## Verification

```bash
python3 /Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py skills/prism-produce
bash skills/prism-produce/scripts/check_produce_shell.sh
```

## Failure handling

See `references/skill-ir.md` failure table. Default: stop, emit human card with decision, keep evidence paths honest.

## Resources

- `references/skill-ir.md` — semantic contract
- `references/modes/` — mode progressive disclosure
- `references/human-card-handoff.md` — anti-leak card checklist
- `references/personal-style-layer.md` — 个人文风层（WRITING.md + 修改学习 + 作者信息密度）
- `references/adapter-migration-pointer.md` — MAP matrix pointer
- `evals/evals.json` — smoke / trigger evals
- `scripts/check_produce_shell.sh` — shell sanity
- `manifest.json` — maturity metadata
- `agents/openai.yaml` — Codex/OpenAI UI metadata
