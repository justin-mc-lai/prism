# Beacon Feature Change Projection

- feature: `prism-release-av-gate-v1`
- feature_slug: `prism-release-av-gate-v1`
- version: `v0.0.1`
- artifact_role: `release-facing projection/read model`
- truth_source: `false`

## Scope
- Lake B′：把 `contracts/asset-render.contract.md` §6（AI 标识强制）与 §7（handoff /
  `release_gate=pending_human`）接进 `prism-release` 公开面。
- 此前 release 面对 AV 交接**零引用**——agent 走到「发」时看不见 AV 终态与法定义务。

## Added
- docs/beacon/v0.0.1/features/prism-release-av-gate-v1/{truth,tasks,tests,evidence}.md
- docs/beacon/v0.0.1/change/prism-release-av-gate-v1.md

## Removed
- （无）

## Fixed
- `skills/prism-release/references/modes/draft-release.md`：Procedure 增 AV/manga 交接三判据
  （`release_gate == pending_human` / AI 标识在场 / 无自动发布路径）+ nested refs
- `skills/prism-release/SKILL.md`：HARD GATE 与 Boundaries 补 AI 标识义务与 `pending_human` 终态
- `skills/prism-release/scripts/check_release_shell.sh`：增 AV gate 断言

## Refreeze
- （无；本湖只做接线，不改任何既有契约语义）
