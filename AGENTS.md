<!-- BEACON:START -->
<!-- BEACON:VERSION:v1.6.12 -->
<!-- BEACON:DOCS_VERSION:v0.0.1 -->
# AGENTS.md

This file is Beacon-managed agent operation guidance.

## Agent behavior
- Keep scope tight and implement the smallest correct change.
- Verify diagnostics/tests before claiming completion.
- Preserve user-authored sections outside Beacon managed blocks.

## Beacon requirement-material usage
- Runtime target version: `v1.6.12`
- Docs target version: `v0.0.1`
- Use `docs/beacon/global-boundaries.md` as the canonical Beacon-wide global constraint source.
- Use `docs/beacon/<version>/` as the canonical delivery tree.
- Read progressively in this order:
  1. `docs/beacon/global-boundaries.md`
  2. `docs/beacon/<version>/SUMMARY.md`
  3. `docs/beacon/<version>/execution/index.md`
  4. `docs/beacon/<version>/execution/architecture-blueprint.md`
  5. `docs/beacon/<version>/prd/`, `user-story/`, `qa/test-cases/`
  6. `docs/beacon/<version>/.machine/`
- For greenfield projects: start with architecture blueprint, then enter think → user-story → prd.
- For takeover projects: document current-state architecture, service map, constraints, and version timeline before new implementation.
- If context blocks are missing/corrupted, run:
  - `beacon doctor setup-context --project-root .`
  - `beacon doctor verify-context --project-root . --strict`
- After runtime/version upgrades on a real project, sync machine requirement materials before QA:
  - `beacon doctor sync-materials --project-root . --version <version> --all-features`
<!-- BEACON:END -->


## Prism 项目规则（Lake B）

- 本仓是独立 Prism（棱镜）内容创作 agent skill 仓。
- 公开面只有 `prism-goal` + 六个能力面；`skills/_internal/**` 不对人发现。
- 源仓提取自 `/Users/apple/Developer/Personal/products/selfmedia-creator`；完整生产链属后续湖。
- 公开发布必须人工批准。
- 双仓分层 SoT 唯一裁决：`docs/sot-layering-decision.md`——本仓拥有 L1–L3 写入口，
  源仓仅 L4 运营层；跨仓改动后跑 `make -C workspace check`。
