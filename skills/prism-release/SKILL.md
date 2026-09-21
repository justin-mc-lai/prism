---
name: prism-release
description: >
  Prism public release surface. Human verb: 发. Beacon design alias: release.
  Draft/publish handoff; public actions require human approval. Triggers: 发, 草稿, 发布, 定时, release, prism-release.
  Hard gate: 公开必须人工二次批准；草稿≠公开发布.
  Do not use for: 无 QA 放行、静默公开发布、跳过人工批准、改母稿. Adapters stay internal-only. Lake B′ production sample.
metadata:
  version: "v0.0.1"
  brand: Prism
  public_surface: true
  public_id: "release"
  scheme: "A-1plus6"
  beacon_alias: "release"
  lake: "B"
  operating_mode: production
  skill_ir: references/skill-ir.md
---

# prism-release

**Public surface**: `release` · **Brand**: Prism（棱镜） · **Human verb**: 发  
**Beacon design alias**: release（不对人暴露为 Prism 公开面名）  
**Operating mode**: production sample (qi-dev-skill-creator)

## HARD GATE

公开必须人工二次批准；草稿≠公开发布

AV / manga 附加：成片终态 = `release_gate: pending_human`；成片必须带 **AI 提示标识**
（总局令第 16 号）；仓库内**无自动公开发布路径**（见 `contracts/asset-render.contract.md` §6/§7）。

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
| `draft-release` | `references/modes/draft-release.md` | Draft handoff and human-gated publish/schedule |

Index: `references/modes/INDEX.md`  
Skill IR: `references/skill-ir.md`

## Workflow

1. Classify request → primary mode (or hand off if wrong surface).
2. Read migration strategy for MAP-008 in `registry/adapter-migration-matrix.md`.
3. Execute this surface's job only; bind evidence paths.
4. Recommend next public harness; never claim another harness's job done.

## Output contract (minimum)

- Human card: `## 这次做了什么` / `## 需要你决定` / `## 下一步`
- `mode_id` (required)
- `public_id`: `release`
- `lane`: `fast` | `standard` | `canon` (inherit from campaign when present)
- `evidence_refs`
- `recommended_next_harness`: one of `goal|intel|master|director|produce|qa|release|stop`
- Machine face may cite `map_id`; human face must not name adapters

## Boundaries

- Strategy now: bridge draft tools; defer vendor sync-ai pin; human approval always
- Do not implement deferred Lake D form producer bodies inside this shell.
- Do not vendor-copy third-party packs wholesale.
- Do not leak `_internal` adapter skill names on the human face.
- Do not approve public publish unless this is `release` **and** human confirmation is recorded.
- **AV / manga**：不得放行无 AI 标识的成片；不得在 `release_gate != pending_human` 时公开；
  **不得新增任何自动发布路径**（`publish` 一律人工二次批准并留痕）。

## Verification

```bash
python3 /Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py skills/prism-release
bash skills/prism-release/scripts/check_release_shell.sh
```

## Failure handling

See `references/skill-ir.md` failure table. Default: stop, emit human card with decision, keep evidence paths honest.

## Resources

- `references/skill-ir.md` — semantic contract
- `references/modes/` — mode progressive disclosure
- `references/human-card-handoff.md` — anti-leak card checklist
- `references/adapter-migration-pointer.md` — MAP matrix pointer
- `evals/evals.json` — smoke / trigger evals
- `scripts/check_release_shell.sh` — shell sanity
- `manifest.json` — maturity metadata
- `agents/openai.yaml` — Codex/OpenAI UI metadata
