# Adapter migration matrix — MAP-001…009
#
# Authority: Lake A Source Skill Inventory → Lake B index → Lake B′ migration policy
# Companion: registry/adapter-index.yaml
# Consumer: skills/prism-goal (and later public surfaces)
#
# Strategies:
#   bridge     — call stable external/local command or skill path; do not copy
#   distill    — extract reusable norms/checklists/scripts into Prism internals
#   vendor_pin — copy/pin under vendor/ with ATTRIBUTION (Lake D+, license gate)
#   defer      — explicitly out of current lake

| map_id | source (selfmedia-creator) | prism landing | strategy now (B′) | deepen lake | distill target (if any) | bridge surface (if any) | vendor_pin (if any) | status |
|--------|----------------------------|---------------|-------------------|-------------|-------------------------|-------------------------|---------------------|--------|
| MAP-001 | `skills/selfmedia-production-pipeline` | `prism-goal` + orchestration kernel | **distill** (kernel already extracted) | B′ polish | `skills/_internal/orchestration/*` | — | — | extracted_kernel |
| MAP-002 | `skills/selfmedia-director` | `prism-director` | **distill** treatment/QC norms; body later | D | `skills/_internal/adapters/director.*` refs | optional read-only path to source skill until distill lands | — | indexed → distill_next |
| MAP-003 | `selfmedia-topic-radar` / `newsnow` / `last30days` / `$qi-dev-intel-radar` | `prism-intel` | **bridge** primary to `qi_dev.sh intel-radar`; distill briefing schema only | C/D | briefing schema + evidence gate checklist | `qi_dev.sh intel-radar doctor\|deep-plan` | do not vendor radar runtimes | indexed → bridge |
| MAP-004 | `content/masters/**` + MASTER 规范 | `prism-master` | **distill** MASTER freeze rules; content stays data | C | master freeze checklist + Fact/Story split | path bridge to source masters until Prism `content/` exists | — | distilled_schema |
| MAP-005 | `selfmedia-writing` / `humanize` / `humanizer-zh` / `no-ai-slop` | `prism-produce` + `prism-qa` | **distill** anti-slop + 人话判据; **bridge** heavy humanizer until distill complete | D | `writing` + `qa` adapter refs (gates, not full models) | source skill paths / local humanizer installs | optional later pin of wordlists only | indexed → distill+bridge |
| MAP-006 | `selfmedia-account-pipeline` + 贴图渲染脚本 | `prism-produce` | **defer** full chain; distill naming/1-9 limits only if needed for routing | D | shot-list / caption metadata rules | source account-pipeline | render scripts pin under license review | indexed → defer |
| MAP-007 | `openmontage` / `comic-storyboard` / rnskill 视频族 | `prism-produce` | **defer** generators; **bridge** when user already has skills installed | D | director handoff fields only | installed local skills by name via routing table | large AV stacks: pin only with ATTRIBUTION | indexed → defer/bridge |
| MAP-008 | `publish-content` / `schedule-post` / sync-ai 桥 | `prism-release` | **bridge** draft tools; **defer** vendor sync-ai pin; human approval always | D/E | publish-approval checklist (kernel has start) | local publish skills; extension path documented not copied | `vendor/selfmedia-sync-ai` only after license+need | indexed → bridge/defer |
| MAP-009 | pipeline refs `creation-mode-map` / `skill-routing` / `quality-gates` | orchestration / routing truth | **distill** (already in kernel); scrub selfmedia-only account paths over time | B′ | same kernel files; Prism-native routing rewrite | — | — | extracted_kernel |

## Decision rules

1. **Default to bridge** for anything with live network, API keys, or large runtimes (`intel-radar`, video gen, publish extensions).
2. **Distill** only what passes recurrence / generativity / distinctiveness / boundary (qi-dev bounded scan). Prefer checklists, gates, schemas, small scripts.
3. **vendor_pin** requires: Lake ≥ D, ATTRIBUTION entry, license allowlist, and a Prism adapter contract that does not become host-visible.
4. **defer** is a first-class status — not a soft TODO. Goal must not pretend deferred producers exist.
5. **anti-leak**: migration work never adds top-level `SKILL.md` under `skills/_internal/adapters/`.

## Lake mapping

| Lake | Migration focus |
|------|-----------------|
| B | Index + shells + kernel extract |
| B′ (this doc) | qi-dev production sample on `prism-goal`; matrix + bridge/distill policy |
| C | campaign/master schema; deepen MAP-004 distill |
| D | form producers; selective vendor_pin + MAP-002/005/006/007 bodies |
| E | metrics / feedback adapters |
| F | monetization optional |

## What not to copy from selfmedia-creator

- Beacon branding / engineering lifecycle as Prism public names
- WiseFlow web UI / logos
- Unverified crawl stacks
- Account-specific hardcodes (`kushi-gzh` paths) without Prism registry rewrite
- Full `vendor/` tree “just in case”

## Verification hooks

```bash
rg -n "MAP-00" registry/adapter-migration-matrix.md registry/adapter-index.yaml
bash skills/prism-goal/scripts/check_goal_shell.sh
```

## Missing evidence (labeled)

- Graded transcript proving agents follow strategy column under ambiguity
- License review tickets for any future vendor_pin rows
- Prism-native rewrite of `skill-routing.md` removing selfmedia-only account defaults
