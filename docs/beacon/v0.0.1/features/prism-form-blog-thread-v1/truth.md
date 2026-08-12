---
slug: prism-form-blog-thread-v1
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
  prd: docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-blog-thread-v1/tests.md
provenance:
  - ac_id: AC-FORM-001
    source_type: migrated_truth
    source_ref: "Lake A FP-PRISM-007 新增形态只改 registry + form contract + 路由表"
  - ac_id: AC-FORM-002
    source_type: source_evidence
    source_ref: "selfmedia-writing 四段式 / US-PRISM-001 / US-PRISM-005"
---

# Requirement Truth: prism-form-blog-thread-v1（v0.0.1 · Lake D2）

## 人话

D1 已经把写作/人话/反 slop 地基煮干。D2 落地前两个**文本形态的生产者契约**：
blog 深度长文（四段式）和 X thread（倒金字塔 + 快道）。每个形态登记进 form registry，
规定“吃什么输入、按什么结构写、产出放哪、证据怎么写、哪些走法非法”，并桥接现有写作工具。
具体写手工具仍是 bridge（selfmedia-writing / writing-agent），判断规则是 Prism 自己的。

- 能做：`registry/form-registry.yaml`（blog/thread 注册）；`contracts/form-blog.contract.md`；
  `contracts/form-thread.contract.md`；creation-mode-map 路由引用；exec 校验脚本。
- 不能做：贴图/xhs（D3）、novel（D4）、comic/vlog/book_video（D5）、发布桥（D6）；
  不 vendor_pin；不做 metrics；不接平台 API。
- 怎样算完：四件套填满；AC 全有 TC；exec 脚本 PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake D：先落 blog + thread 两个最轻文本形态，验证“form 注册 + 生产者契约 + bridge”的闭环。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D2（blog/thread forms）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-form-blog-thread-v1
version: v0.0.1
depends_on: prism-form-writing-v1（D1）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-F01 | migrated | must | AC-FORM-001 | covered |
| INT-F02 | migrated | must | AC-FORM-002 | covered |
| INT-F03 | migrated | must | AC-FORM-003 | covered |
| INT-F04 | migrated | must | AC-FORM-004 | covered |
| INT-F05 | migrated | must | AC-FORM-005 | covered |
| INT-F06 | migrated | must | AC-FORM-006 | covered |
| INT-F07 | migrated | must | AC-FORM-007 | covered |
| INT-F08 | migrated | must | AC-FORM-008 | covered |
| INT-F09 | migrated | must | AC-FORM-009 | covered |
| INT-F10 | migrated | must | AC-FORM-010 | covered |
| INT-F11 | sea | must | D3–D6 其余形态 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-FORM-001 | 新增形态只改 registry + form contract + 路由表（FP-PRISM-007），不动主链与导演骨架 |
| FP-FORM-002 | 形态契约依赖 D1：结构规则引 writing.contract；QA 引 anti-slop-gate |
| FP-FORM-003 | 无冻结母稿（或快道事实快照）不得产出 |
| FP-FORM-004 | lane=canon 禁用 fast_lane_skip；快道必须显式标注 |
| FP-FORM-005 | bridge 缺工具 fail-closed，不产出假文件 |
| FP-FORM-006 | 继承 FP-PRISM-002/004/013：母稿权威；不自证；不得宣称海 closure |

## 用户旅程 / 故事

US-FORM-001（= US-PRISM-001）：用户要一篇 blog。intel 定角度 → master 冻结 FactMaster →
director 出 treatment → prism-produce 按 `form-blog.contract`（四段式）成稿 →
qa 过 anti-slop-gate + 事实核对 → release。

US-FORM-002（= US-PRISM-005）：快道 thread。用户只调 prism-goal；lane=fast；
intel/master/director 以 `fast_lane_skip` 标注跳过 → produce 按 `form-thread.contract`
（倒金字塔）→ qa → release。

US-FORM-003：维护者加新形态。只加 registry 条目 + form contract + 路由行；主链不动。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| FormRegistry | form | 形态 → 契约 + lane + 生产链 |
| BlogFormContract | form-blog | 四段式；标准道 |
| ThreadFormContract | form-thread | 倒金字塔；快道/标准道 |
| RouteEntry | form | creation-mode-map 中 blog/thread 行 |

## Domain FSM（D2 落地）

状态：blog_thread_planned → forms_registered → blog_contract_landed → thread_contract_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| forms_registered | blog_thread_planned | `registry/form-registry.yaml` 含 blog+thread |
| blog_contract_landed | forms_registered | `contracts/form-blog.contract.md` present |
| thread_contract_landed | blog_contract_landed | `contracts/form-thread.contract.md` present |
| routing_landed | thread_contract_landed | creation-mode-map 引用 form contracts |
| indexed | routing_landed | exec 脚本 + 无 SKILL.md 泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- blog_thread_planned → routing_landed（跳过注册与契约）
- indexed → human_accepted（跳过 QA）
- lane=canon 使用 fast_lane_skip
- 无母稿/事实快照仍产出
- bridge 缺失仍产出（假交付）
- 宣称 Lake D 全部完成

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| blog_thread_planned | register_forms | blog+thread in registry | forms_registered | write form-registry.yaml |
| forms_registered | land_blog_contract | blog contract present | blog_contract_landed | write form-blog.contract |
| blog_contract_landed | land_thread_contract | thread contract present | thread_contract_landed | write form-thread.contract |
| thread_contract_landed | wire_routing | route refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. form registry 注册 blog/thread（AC-FORM-001）
2. blog producer 契约（AC-FORM-002）
3. thread producer 契约（AC-FORM-003）
4. creation-mode-map 路由（AC-FORM-004）
5. exec 校验脚本（AC-FORM-005）
6. 形态扩展只动 registry+contract+routing（AC-FORM-006）
7. 快道/canon 门禁（AC-FORM-007）
8. bridge fail-closed（AC-FORM-008）
9. maker≠checker（AC-FORM-009）
10. Non-goals / deferral（AC-FORM-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-F01 | 贴图/xhs 形态本体 | accepted | D3 |
| DL-F02 | novel 形态本体 | accepted | D4 |
| DL-F03 | comic/vlog/book_video 本体 | accepted | D5 |
| DL-F04 | publish/schedule 桥 | accepted | D6 |
| DL-F05 | vendor_pin 外部大栈 | accepted | license review + ATTRIBUTION |
| DL-F06 | metrics/learning loop | accepted | Lake E |
| DL-F07 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-FORM-001 | 进入 `forms_registered`：`registry/form-registry.yaml` 登记 blog 与 thread，各含 contract 引用、lane 与生产链 |
| AC-FORM-002 | 进入 `blog_contract_landed`：`contracts/form-blog.contract.md` 定义输入（冻结母稿 + director treatment）、四段式结构、输出路径（content/presentations/…/humanized.md）、证据与 fail-closed |
| AC-FORM-003 | 进入 `thread_contract_landed`：`contracts/form-thread.contract.md` 定义倒金字塔结构、fast_lane_skip 标注、canon 禁用快道、bridge writing-agent |
| AC-FORM-004 | 进入 `routing_landed`：creation-mode-map 的 blog/thread 行引用 form-blog.contract / form-thread.contract |
| AC-FORM-005 | 进入 `indexed`：`scripts/check_blog_thread_forms.sh` exec-layer 校验 PASS |
| AC-FORM-006 | 形态扩展规则声明：新增形态只改 registry + form contract + 路由表，不改主链 |
| AC-FORM-007 | 快道门禁：thread 契约声明 lane=canon 禁用 fast_lane_skip；快道必须显式标注 |
| AC-FORM-008 | bridge fail-closed：writing-agent 等缺失 → blocked + reason_code，不产出假文件 |
| AC-FORM-009 | maker≠checker：form 契约与 anti-slop-gate 分离；QA 证据引用原文行 |
| AC-FORM-010 | Non-goals：D3–D6 形态、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure |

## Non-goals

- 不实现贴图/xhs（D3）、novel（D4）、comic/vlog/book_video（D5）、发布桥（D6）
- 不 vendor_pin 外部写作工具
- 不做 metrics（E）/ monetization（F）
- 不接平台 API
- 不把 D1+D2 宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
