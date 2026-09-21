---
slug: prism-release-av-gate-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
domain_required: true
ux_required: false
parser_contract: beacon-feature-package-v2
materials_status: current
package_maturity: filled
truth_source_model: intent_first
program_ref: docs/beacon/v0.0.1/programs/prism-release-av-manga-release-gate/program-manifest.md
canonical_refs:
  prd: docs/beacon/v0.0.1/features/prism-release-av-gate-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-release-av-gate-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-release-av-gate-v1/tests.md
provenance:
  - ac_id: AC-RAV-001
    source_type: migrated_truth
    source_ref: "contracts/asset-render.contract.md §6（AI 标识强制）/ §7（handoff：release_gate=pending_human）；contracts/form-manga-drama.contract.md §5 附加门"
  - ac_id: AC-RAV-002
    source_type: user_decision
    source_ref: "2026-09-21 用户决策：补齐 prism-release 对 AV 交接的引用（最后一处缺口）"
  - ac_id: AC-RAV-003
    source_type: migrated_truth
    source_ref: "registry/form-registry.yaml manga_drama producer_chain「release 停 pending_human」；skills/prism-release/references/modes/draft-release.md Human approval gate"
---

# Requirement Truth: prism-release-av-gate-v1（v0.0.1 · release 面 AV 交接门）

## 人话

漫剧/漫画成片停在 `release_gate: pending_human`，而且要带 AI 提示标识。
但 **release 面此前完全不知道这两件事**——没有任何引用，agent 走到「发」这一步时
看不见 AV 的终态与法定义务。

本湖只做一件事：把 `contracts/asset-render.contract.md` 的 §6（AI 标识强制）与
§7（handoff / `pending_human`）接进 `prism-release`，并加 exec 断言。

- 能做：`draft-release.md` 增 AV/manga 交接核验；`SKILL.md` 硬门与 boundaries 补该义务；
  扩展 `check_release_shell.sh` 断言。
- 不能做：自动发布；改 asset-render / form-manga-drama 契约语义；实现平台发布 API；
  替代 QA 判定。
- 怎样算完：AC 全有 TC；exec PASS；全量门禁零回归；implement → QA → release 人工门。

## User Intent

补齐 `prism-release` 对 AV/manga 渲染交接（`release_gate=pending_human` + AI 标识）的引用与核验。

## User Intent Snapshot

```yaml
lake_or_ocean: 湖
this_lake: Lake B′（release 面 AV 交接门 · 最后一处接线缺口）
user_decision: promoted
scope_mode: phased_lake
feature: prism-release-av-gate-v1
version: v0.0.1
depends_on: prism-prompt-compiler-v1（asset-render 契约与 provider-only 链路）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-RAV01 | user | must | AC-RAV-001（mode 增 AV 交接核验） | covered |
| INT-RAV02 | user | must | AC-RAV-002（SKILL 硬门 + boundaries） | covered |
| INT-RAV03 | user | must | AC-RAV-003（exec 断言扩展） | covered |
| INT-RAV04 | sea | must | 平台发布 API / 自动发布 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-RAV-001 | AV/manga 成片终态 = `release_gate: pending_human`；**仓库内无自动发布路径** |
| FP-RAV-002 | AI 提示标识为法定义务（总局令第 16 号）；成片无标识即不得进入发布交接 |
| FP-RAV-003 | 草稿 ≠ 公开发布；公开发布须人工二次批准并留痕 |
| FP-RAV-004 | release 不判定 QA；无 QA 放行不得进入发布交接 |
| FP-RAV-005 | release 面不改母稿/正典，不改 asset-render 契约语义 |
| FP-RAV-006 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-RAV-001：用户要发漫剧草稿。QA 放行后进 release → release 核 `video-manifest.json`
的 `release_gate == pending_human` 且成片带 AI 标识 → 产出草稿交接卡 → **停**，等人工批准。

US-RAV-002：成片无 AI 标识。release 明确阻断（`release_ai_label_missing`），不放行。

US-RAV-003：用户要求直接公开发布。release 拒绝静默发布，要求人工二次批准并留痕。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| ReleaseSurface | prism-release | 公开面（发） |
| AssetRenderContract | asset-render | §6 AI 标识 / §7 handoff |
| ReleaseManifest | video-manifest.json | `release_gate` / `mode` 来源 |
| HumanApprovalGate | pending_human | 仓库内无自动发布路径 |
| AiLabelObligation | 总局令第16号 | 成片强制标识 |

## Domain FSM（RAV 落地）

状态：rav_planned → mode_wired → skill_gate_wired → shell_check_extended → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| mode_wired | rav_planned | draft-release.md 含 AV 交接核验 |
| skill_gate_wired | mode_wired | SKILL.md 硬门/boundaries 含 AI 标识与 pending_human |
| shell_check_extended | skill_gate_wired | check_release_shell.sh 含 AV 断言 |
| indexed | shell_check_extended | exec + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- AV 成片无 AI 标识仍进入发布交接 → illegal
- `release_gate != pending_human` 仍放行公开 → illegal
- 未过 QA 进入 release → illegal
- 仓库内出现自动公开发布路径 → illegal
- release 面改写 asset-render / form-manga-drama 契约语义 → illegal
- 静默公开发布（无人工二次批准留痕）→ illegal
- 宣称海 closure → illegal

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| rav_planned | wire_mode | AV handoff checks present | mode_wired | update draft-release.md |
| mode_wired | wire_skill_gate | AI label + pending_human in gates | skill_gate_wired | update SKILL.md |
| skill_gate_wired | extend_check | AV assertions present | shell_check_extended | extend check_release_shell.sh |
| shell_check_extended | index | exec pass + no leak | indexed | run check_all_public_surfaces.sh |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. mode 增 AV 交接核验（AC-RAV-001）
2. SKILL 硬门 + boundaries（AC-RAV-002）
3. exec 断言扩展（AC-RAV-003）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-RAV01 | 平台发布 API / 自动发布 | accepted | 属后续海；仓库内无自动发布 |
| DL-RAV02 | 改 asset-render 契约语义 | rejected | 本湖只做接线 |
| DL-RAV03 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-RAV-001 | 进入 `mode_wired`：`references/modes/draft-release.md` 增 AV/manga 交接核验三判据（`release_gate == pending_human` / AI 标识在场 / 无自动发布路径）+ nested refs 指向 `contracts/asset-render.contract.md` 与 `registry/render-adapters.yaml` |
| AC-RAV-002 | 进入 `skill_gate_wired`：`SKILL.md` 的 HARD GATE 与 Boundaries 明确 AI 标识义务与 `pending_human` 终态；不得出现自动公开发布路径 |
| AC-RAV-003 | 进入 `shell_check_extended`：`skills/prism-release/scripts/check_release_shell.sh` 增 AV gate 断言并 PASS；`bash scripts/check_all_public_surfaces.sh` 保持 PASS |

## Non-goals

- 不实现任何平台发布 API 或自动发布路径；仓库内 `release_gate: pending_human` 为终态
- 不改 `contracts/asset-render.contract.md` / `contracts/form-manga-drama.contract.md` 语义
- 不改 QA 判定；release 不接受未过 QA 的产物
- 不把本湖宣称为海 closure

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
