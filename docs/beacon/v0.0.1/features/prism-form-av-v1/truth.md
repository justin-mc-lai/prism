---
slug: prism-form-av-v1
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
program_ref: docs/beacon/v0.0.1/programs/prism-canon/program-manifest.md
canonical_refs:
  prd: docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-av-v1/tests.md
provenance:
  - ac_id: AC-AV-001
    source_type: migrated_truth
    source_ref: "Lake A MAP-007 · openmontage/comic-storyboard/rnskill"
  - ac_id: AC-AV-002
    source_type: source_evidence
    source_ref: "openmontage AGPL-3.0 / comic-storyboard 3:4 竖版规则"
---

# Requirement Truth: prism-form-av-v1（v0.0.1 · Lake D5）

## 人话

D5 落地三个**视听形态**的生产者路由：comic（漫画）、vlog（口播视频）、book_video（书籍/剧集向视频）。
策略是 **bridge 优先**：直接调用已安装的外部工具（openmontage / comic-storyboard / book_video /
rnskill 视频族），Prism 只蒸馏“导演交接字段”和 QA 门，不整包复制。AV 大栈 license 敏感
（如 OpenMontage AGPL-3.0），默认不 pin；要 pin 必须人工批准 + ATTRIBUTION。

- 能做：form-registry 注册 comic/vlog/book_video；`contracts/form-av.contract.md`；
  creation-mode-map 路由；exec 校验脚本。
- 不能做：发布桥（D6）；vendor_pin 全量；metrics；平台 API。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake D：落地 AV 形态 bridge 路由与 license 边界，完成八形态中的最后三个生产者面。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D5（comic/vlog/book_video）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-form-av-v1
version: v0.0.1
depends_on: prism-form-writing-v1（D1）· director 面
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-A01 | migrated | must | AC-AV-001 | covered |
| INT-A02 | migrated | must | AC-AV-002 | covered |
| INT-A03 | migrated | must | AC-AV-003 | covered |
| INT-A04 | migrated | must | AC-AV-004 | covered |
| INT-A05 | migrated | must | AC-AV-005 | covered |
| INT-A06 | migrated | must | AC-AV-006 | covered |
| INT-A07 | migrated | must | AC-AV-007 | covered |
| INT-A08 | migrated | must | AC-AV-008 | covered |
| INT-A09 | migrated | must | AC-AV-009 | covered |
| INT-A10 | migrated | must | AC-AV-010 | covered |
| INT-A11 | sea | must | D6 publish 桥 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-AV-001 | AV 形态 bridge 优先；外部大栈不整包复制 |
| FP-AV-002 | vendor_pin 需 license allowlist + ATTRIBUTION + 人工批准（AGPL 默认不 pin） |
| FP-AV-003 | 导演交接字段必填：treatment / presentation map / shot list / storyboard |
| FP-AV-004 | QA 门：字幕/文字无乱码、版权安全、分镜/图序一致、anti-slop-gate 文案 |
| FP-AV-005 | bridge 缺失 fail-closed，不产出假文件 |
| FP-AV-006 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-AV-001：用户要漫画。director 出分镜 + 角色/场景设定 → produce 按 `form-av.contract`（comic 路由）
bridge comic-storyboard（3:4 竖版、文字可读）→ QA（无乱码、分页一致）→ release。

US-AV-002：用户要 vlog。director 出口播脚本/分镜 → bridge openmontage → 成片 QA → release。

US-AV-003：用户要 book_video。bridge book-video 管线；license 未过时不 vendor_pin，只 bridge。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| AvFormContract | form-av | comic/vlog/book_video 路由 + 交接字段 |
| DirectorHandoff | treatment/map/shotlist | 必填输入 |
| BridgeRoute | form | 工具名 + 调用方式 + fail-closed |
| LicenseNote | license | AGPL 等；pin 需批准 |

## Domain FSM（D5 落地）

状态：av_planned → forms_registered → av_contract_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| forms_registered | av_planned | form-registry 含 comic/vlog/book_video |
| av_contract_landed | forms_registered | form-av.contract present |
| routing_landed | av_contract_landed | creation-mode-map 引用 form-av.contract |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- av_planned → routing_landed（跳过注册/契约）
- indexed → human_accepted（跳过 QA）
- 无 director handoff 仍产出
- bridge 缺失仍产出
- 未过 license 门仍 vendor_pin
- 宣称 Lake D 全部完成

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| av_planned | register_forms | comic/vlog/book_video in registry | forms_registered | update form-registry |
| forms_registered | land_contract | form-av.contract present | av_contract_landed | write form-av.contract |
| av_contract_landed | wire_routing | route refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. form registry AV 三形态（AC-AV-001）
2. form-av 契约（AC-AV-002）
3. director handoff 字段（AC-AV-003）
4. 路由引用（AC-AV-004）
5. exec 脚本（AC-AV-005）
6. license 注记（AC-AV-006）
7. bridge fail-closed（AC-AV-007）
8. QA 门（AC-AV-008）
9. maker≠checker（AC-AV-009）
10. Non-goals / deferral（AC-AV-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-A01 | publish/schedule 桥 | accepted | D6 |
| DL-A02 | vendor_pin 全量 AV 大栈 | accepted | license review + ATTRIBUTION 后才允许 |
| DL-A03 | metrics/learning loop | accepted | Lake E |
| DL-A04 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-AV-001 | 进入 `forms_registered`：form-registry 登记 comic、vlog、book_video |
| AC-AV-002 | 进入 `av_contract_landed`：`contracts/form-av.contract.md` 定义三形态 bridge 路由（comic-storyboard / openmontage / book_video / rnskill）与 fail-closed |
| AC-AV-003 | director handoff：契约要求 treatment / presentation map / shot list / storyboard 作为必填输入 |
| AC-AV-004 | 进入 `routing_landed`：creation-mode-map 的 vlog 行引用 form-av.contract，并新增 comic / book_video 行 |
| AC-AV-005 | 进入 `indexed`：`scripts/check_av_forms.sh` exec-layer 校验 PASS |
| AC-AV-006 | license 注记：契约声明 AGPL-3.0 等 license 边界；默认 bridge；pin 需人工批准 + ATTRIBUTION |
| AC-AV-007 | bridge fail-closed：工具缺失 → blocked + reason_code |
| AC-AV-008 | QA 门：字幕/文字无乱码、版权安全、分镜/图序一致、anti-slop-gate 文案证据 |
| AC-AV-009 | maker≠checker：form-av 契约与 QA 门分离 |
| AC-AV-010 | Non-goals：D6、vendor_pin 全量、metrics、平台 API 显式排除；不得宣称海 closure |

## Non-goals

- 不实现发布桥（D6）
- 不 vendor_pin AV 大栈（license 门）
- 不做 metrics（E）/ monetization（F）
- 不接平台 API
- 不把 D1–D5 宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
