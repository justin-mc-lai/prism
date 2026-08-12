---
slug: prism-form-writing-v1
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
  prd: docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-writing-v1/tests.md
provenance:
  - ac_id: AC-WRITE-001
    source_type: migrated_truth
    source_ref: "Lake A INT-P14 / DL-003 · MAP-005 distill+bridge"
  - ac_id: AC-WRITE-002
    source_type: source_evidence
    source_ref: "selfmedia-creator skills/no-ai-slop + humanizer-zh + selfmedia-humanize"
---

# Requirement Truth: prism-form-writing-v1（v0.0.1 · Lake D1）

## 人话

Lake D 的第一块地基：把写作、人味改写、反 AI 味门禁从 `selfmedia-creator` 蒸馏成 Prism 自己的
produce 契约与 qa 门，并把现成人味/改写工具登记成 bridge 适配器。本子湖**不实现任何具体形态**
（blog/thread/贴图等本体在 D2–D6），只把“成稿层”的规则、门禁和路由煮干，让后面每个形态都有同一套
写作与反 slop 标准可依赖。

- 能做：writing.contract（七段 + 蒸馏写作规则）；anti-slop-gate（slop 模式 + 人话判据 + 证据要求）；
  writing-adapters bridge 登记表；creation-mode-map 路由更新；exec 校验脚本。
- 不能做：不写 blog/thread/贴图/novel/comic/vlog/book_video 的具体生产者（D2–D6）；
  不 vendor_pin 外部大栈（license 门）；不做 metrics（E）；不接平台 API（跨仓）。
- 怎样算完：四件套填满；AC 全有 TC；exec 脚本 PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

开始 Lake D：先煮干写作/人话/反 slop 地基（MAP-005 distill+bridge），再逐个形态落地。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D1（writing base）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-form-writing-v1
version: v0.0.1
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-W01 | migrated | must | AC-WRITE-001 | covered |
| INT-W02 | migrated | must | AC-WRITE-002 | covered |
| INT-W03 | migrated | must | AC-WRITE-003 | covered |
| INT-W04 | migrated | must | AC-WRITE-004 | covered |
| INT-W05 | migrated | must | AC-WRITE-005 | covered |
| INT-W06 | migrated | must | AC-WRITE-006 | covered |
| INT-W07 | migrated | must | AC-WRITE-007 | covered |
| INT-W08 | migrated | must | AC-WRITE-008 | covered |
| INT-W09 | migrated | must | AC-WRITE-009 | covered |
| INT-W10 | migrated | must | AC-WRITE-010 | covered |
| INT-W11 | sea | must | D2 blog/thread 形态本体 | deferred |
| INT-W12 | sea | must | D3–D6 其余形态与发布桥 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-WRITE-001 | 写作规则与反 slop 门是 Prism 自己的蒸馏规范；bridge 只是工具通道，不外包判断 |
| FP-WRITE-002 | maker ≠ checker：produce 侧 writing.contract 与 qa 侧 anti-slop-gate 分离 |
| FP-WRITE-003 | 不承诺“必过机检/0% AI”；只降低可识别模板感 |
| FP-WRITE-004 | 不编造个人经历、数据、截图；无素材用显式占位 |
| FP-WRITE-005 | bridge 缺工具必须 fail-closed（blocked + reason_code），不产出假文件 |
| FP-WRITE-006 | 继承 FP-PRISM-002/004/013：母稿权威；不自证 QA；不得宣称海 closure |

## 用户旅程 / 故事

US-WRITE-001（= US-PRISM-001 的成稿段）：prism-produce 拿到冻结母稿 → 按 writing.contract
（四段式/倒金字塔/情绪长文选型）成稿 → 走人话层（selfmedia-humanize / humanizer-zh 等 bridge）→
prism-qa 按 anti-slop-gate 逐条核验并引用证据行 → 交给 release。

US-WRITE-002：维护者新增一个人味工具。只改 `registry/writing-adapters.yaml` 登记 bridge 命令，
不改主链与写作规则。

US-WRITE-003：bridge 工具缺失时。produce/qa 明确返回 blocked + reason_code，不假装产出；
人类决定安装工具或换 bridge。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| WritingContract | contract_id | produce 侧七段契约 + 蒸馏写作规则 |
| AntiSlopGate | gate_id | qa 侧 slop 模式/人话判据/证据要求 |
| WritingAdapterMap | map_id | 源工具 → bridge 命令（MAP-005 深化） |
| RouteEntry | form | creation-mode-map 中的成稿路由 |

## Domain FSM（D1 落地）

状态：writing_planned → contract_landed → gate_landed → registry_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| contract_landed | writing_planned | `contracts/writing.contract.md` present |
| gate_landed | contract_landed | `skills/prism-qa/references/anti-slop-gate.md` present |
| registry_landed | gate_landed | `registry/writing-adapters.yaml` ≥8 bridge |
| routing_landed | registry_landed | creation-mode-map 引用 contract+gate |
| indexed | routing_landed | exec 脚本 + internal 无 SKILL.md |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- writing_planned → routing_landed（跳过契约/门禁/登记）
- indexed → human_accepted（跳过 QA）
- bridge 缺失仍产出文件（假交付）
- 承诺必过机检 / 编造经历数据
- 宣称 Lake D 全部完成（D2–D6 未交付）

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| writing_planned | land_contract | contract present | contract_landed | write writing.contract |
| contract_landed | land_gate | anti-slop-gate present | gate_landed | distill qa gate |
| gate_landed | register_adapters | ≥8 bridge entries | registry_landed | write writing-adapters.yaml |
| registry_landed | wire_routing | route refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. writing.contract 七段 + 蒸馏写作规则（AC-WRITE-001）
2. anti-slop-gate slop 模式 + 人话判据 + 证据（AC-WRITE-002）
3. writing-adapters bridge 登记（AC-WRITE-003）
4. creation-mode-map 路由（AC-WRITE-004）
5. exec 校验脚本（AC-WRITE-005）
6. adapter internal 不可见（AC-WRITE-006）
7. bridge fail-closed（AC-WRITE-007）
8. maker≠checker（AC-WRITE-008）
9. 硬边界（AC-WRITE-009）
10. Non-goals / deferral（AC-WRITE-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-D01 | blog/thread 形态本体 | accepted | D2 |
| DL-D02 | 贴图/xhs 形态本体 | accepted | D3 |
| DL-D03 | novel 形态本体 | accepted | D4 |
| DL-D04 | comic/vlog/book_video 本体 | accepted | D5 |
| DL-D05 | publish/schedule 桥 | accepted | D6 |
| DL-D06 | vendor_pin 外部大栈 | accepted | license review + ATTRIBUTION 后才允许 |
| DL-D07 | metrics/learning loop | accepted | Lake E |
| DL-D08 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-WRITE-001 | 进入 `contract_landed`：`contracts/writing.contract.md` 存在，含七段契约 + 蒸馏写作规则（四段式 / 日榜倒金字塔 / emotional-essay 选型 + 文笔五原则 + 禁翻译腔） |
| AC-WRITE-002 | 进入 `gate_landed`：`skills/prism-qa/references/anti-slop-gate.md` 含 ≥10 条 slop 模式（含二元对比/清嗓开场/伪洞察/冒号揭晓/重要性吹捧/weasel 归因/假深刻结尾/总结复读等）、≥5 条人话判据、证据要求（引用原文行 + 修复建议） |
| AC-WRITE-003 | 进入 `registry_landed`：`registry/writing-adapters.yaml` 登记 ≥8 个 bridge（humanizer-zh / selfmedia-humanize / qu-ai-wei / shuorenhua / no-ai-slop / stop-slop / humanizer-en / writing-agent），每项含 bridge 命令与 fail-closed 说明 |
| AC-WRITE-004 | 进入 `routing_landed`：`skills/_internal/orchestration/creation-mode-map.md` 的 blog / 贴图 / thread 行引用 MAP-005 策略与 writing.contract / anti-slop-gate |
| AC-WRITE-005 | 进入 `indexed`：`scripts/check_writing_adapters.sh` exec-layer 校验 PASS（真实断言：文件存在、关键字段、≥8 bridge、路由引用、无顶层 SKILL.md） |
| AC-WRITE-006 | adapter 不可见：`skills/_internal/adapters/` 与 `skills/prism-qa/references/` 下无 SKILL.md |
| AC-WRITE-007 | bridge fail-closed 规则在 contract 中声明：缺工具 → blocked + reason_code，不产出假文件 |
| AC-WRITE-008 | maker≠checker：writing.contract 与 anti-slop-gate 为独立文件，qa 侧含证据路径要求 |
| AC-WRITE-009 | 硬边界在 anti-slop-gate 声明：不承诺必过机检；不编造经历/数据/截图；无素材用占位 |
| AC-WRITE-010 | Non-goals：D2–D6 形态本体、vendor_pin、metrics、平台 API 全部显式排除；不得宣称海 closure |

## Non-goals

- 不实现 blog/thread/贴图/xhs/novel/comic/vlog/book_video 的具体生产者（D2–D6）
- 不 vendor_pin 外部写作/人味大栈（license 门未过）
- 不做指标采集/学习回流（Lake E）
- 不接平台发布 API（跨仓 selfmedia-sync-ai）
- 不把 D1 地基宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
