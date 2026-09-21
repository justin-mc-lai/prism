---
slug: prism-prompt-compiler-v1
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
program_ref: docs/beacon/v0.0.1/programs/prism-shot-prompt-compiler-storyboard-ref/program-manifest.md
canonical_refs:
  prd: docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/tests.md
provenance:
  - ac_id: AC-PPC-001
    source_type: source_evidence
    source_ref: "vendor/skills/onlyshot/assets/templates/{03_完整剧本,剧本,镜头清单}.md + 分镜.json（MIT，A-cat-with-carrots/OnlyShot）；授权见 docs/ATTRIBUTION-drama-prompt-repos.md"
  - ac_id: AC-PPC-002
    source_type: migrated_truth
    source_ref: "contracts/prompt-syntax.contract.md §4 输出路径 + §5 八判据；skills/prism-director/references/{prompt-syntax-table,asset-prompt-templates,script-templates}.md"
  - ac_id: AC-PPC-003
    source_type: source_evidence
    source_ref: "content/pipelines/ai-manga-drama/storyboard-schema.json（三类资产）；skills/prism-director/references/asset-consistency-gate.md §2 识别锚点（lumenx 三件套）"
  - ac_id: AC-PPC-005
    source_type: migrated_truth
    source_ref: "contracts/form-manga-drama.contract.md §1（源 truth R1 kenburns 降级）→ 本次 refreeze 取消兜底"
  - ac_id: AC-PPC-005
    source_type: user_decision
    source_ref: "2026-09-21 用户决策：取消 FFmpeg kenburns 兜底；edge-tts 一并删除；无凭证直接终止；Prism 只产前置文本提示词"
---

# Requirement Truth: prism-prompt-compiler-v1（v0.0.1 · Lake B′ 提示词编译器 + 渲染交接）

## 人话

Prism 是 agent skill，它的活是**把前置文本全部产出来**：从已冻结分镜 + 选定风格，
编译出资产 ref 提示词、每镜图片提示词、每镜视频提示词、字幕，以及给下游 provider 的请求包。
**画面、视频、语音的生成不在 Prism 里做**——文生图、图生视频、文生视频都是后续 provider 模型的事。

本轮同时**拆掉本地兜底**：不再用 FFmpeg 缩放运镜"假装"出片，也不再本地跑 edge-tts 配音。
无凭证就**直接终止**（fail-closed），绝不产出假成片。`assemble` 退化为"只拼接 provider 真实片段"。

- 能做：蒸馏剧本/分镜表/镜头清单模板；写确定性提示词编译器；分镜 schema 登记资产身份参考图
  （ref_image）；定 asset-render 契约与 provider 适配器登记；CLI 去兜底改造。
- 不能做：实现任何 provider 的 HTTP/SDK 调用；管凭证；本地生成画面或音频；自动发布。
- 怎样算完：AC 全有 TC；exec 门禁 PASS；既有门禁零回归；implement → QA → release 人工门。

## User Intent

让 Prism 产出**全部前置文本提示词与 provider 请求包**；渲染（T2I/I2V/T2V/TTS）交下游 provider；
取消 FFmpeg kenburns 与本地 edge-tts 兜底，无凭证 fail-closed 终止。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake B′（提示词编译器 + 渲染交接去兜底）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes PPC-1..PPC-4
feature: prism-prompt-compiler-v1
version: v0.0.1
depends_on: prism-manga-asset-gate-v1 / prism-asset-gate-rollout-v1
decisions_2026_09_21:
  assemble: 改为只拼接 provider 真实片段（缺片段 fail-closed）
  voice: edge-tts 一并删除，语音交下游 provider
  frozen_contract_change: 新 feature + change 记录 + refreeze form-manga-drama
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-P01 | user | must | AC-PPC-001（剧本模板） | covered |
| INT-P02 | user | must | AC-PPC-002（提示词编译器） | covered |
| INT-P03 | user | must | AC-PPC-003（ref_image 字段） | covered |
| INT-P04 | user | must | AC-PPC-004（asset-render 契约 + 适配器） | covered |
| INT-P05 | user | must | AC-PPC-005（去兜底 provider-only） | covered |
| INT-P06 | user | must | AC-PPC-006（契约与路由同步） | covered |
| INT-P07 | user | must | AC-PPC-007（exec 门禁 + 零回归） | covered |
| INT-P08 | sea | must | provider 执行器（真实 T2I/I2V/T2V/TTS 调用 + 凭证管理） | deferred |
| INT-P09 | sea | must | novel / live_drama 复用 asset-render | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-PPC-001 | Prism 产出文本与请求包；像素与音频由 provider 产出（职责边界不可越） |
| FP-PPC-002 | 无凭证 fail-closed；**不存在任何本地兜底路径**（FP-PRISM-004 不假交付） |
| FP-PPC-003 | 编译器必须确定性：同 storyboard + 同风格 → 逐字节一致 |
| FP-PPC-004 | 一致性靠参考图锚定（ref_image）+ 身份块逐字复用；风格串可换、身份串不动 |
| FP-PPC-005 | 未过编译器不得进 assemble（非法跃迁） |
| FP-PPC-006 | 片段规格不符拒绝拼接，**不偷偷缩放**；缺片段不合成替代品 |
| FP-PPC-007 | 凭证永不入库；Prism 不发起任何网络调用 |
| FP-PPC-008 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-PPC-001：用户要漫剧。prism-master 冻结 StoryMaster → director 按 `script-templates.md`
落剧本/分镜（storyboard.json + `ref_image`）→ 过资产一致性门与镜头语法门 →
`prompt_compiler.py` 编译资产/图片/视频提示词 + srt → `request` 出 provider 请求包 →
provider 渲染资产图与 `clips/{shot_id}.mp4` → `assemble` 拼真实片段 + 烧 AI 标识 → QA → release。

US-PPC-002：无凭证。`request` 明确 `BLOCKED:missing_credential` exit 2；不降级、不产假成片。

US-PPC-003：片段缺失或规格不符。`assemble` 明确终止（`missing_clip` / spec mismatch），
拒绝拼接与缩放，不产出替代成片。

US-PPC-004：换导演视角。只改 `--style`（29 预设），身份块与 storyboard 不动，重编译即得新提示词。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| Storyboard | storyboard.json | 分镜正典；shots[] + 三类资产 + ref_image |
| PromptArtifacts | 资产/图片/视频提示词 + srt | 编译器确定性产物（前置文本） |
| RenderRequest | render-request.json | provider 请求包（四阶段状态 + segments） |
| StylePreset | style_id | registry/style-presets.yaml ⊕ lumenx base，按 id 合并 |
| RenderAdapter | stage | t2i/i2v/t2v/tts 四槽位 + 凭证环境变量名 |
| ProviderClip | clips/{shot_id}.mp4 | provider 产出的真实片段（480x854） |
| RenderManifest | video-manifest.json | mode=provider-only；release_gate=pending_human |

## Domain FSM（PPC 落地）

状态：ppc_planned → compiler_landed → schema_landed → render_contract_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| compiler_landed | ppc_planned | prompt_compiler.py 确定性 PASS |
| schema_landed | compiler_landed | storyboard-schema 含 ref_image 且 CLI 校验 |
| render_contract_landed | schema_landed | asset-render.contract + render-adapters present |
| routing_landed | render_contract_landed | form-registry/README/creation-mode-map 去兜底 |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- ppc_planned → routing_landed（跳过编译器与契约）
- indexed → human_accepted（跳过 QA）
- 无凭证时产出任何"假成片"或占位视频
- 用本地 ffmpeg 生成画面/音频充当 provider 产物
- 未过 `prompt_compiler` 直接进 `assemble`
- 片段缺失/规格不符仍拼接或缩放
- 凭证或密钥写入仓库任何文件
- 宣称本湖已交付 provider 执行器（属后续海）

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| ppc_planned | land_compiler | deterministic + unknown style fails closed | compiler_landed | write prompt_compiler.py + fixture |
| compiler_landed | land_schema | ref_image in schema + CLI validation | schema_landed | update storyboard-schema + CLI |
| schema_landed | land_render_contract | contract + adapters present | render_contract_landed | write asset-render.contract + render-adapters |
| render_contract_landed | wire_routing | registry/README/mode-map synced | routing_landed | remove kenburns/edge-tts; provider-only |
| routing_landed | index | exec script + no leak | indexed | write check scripts |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. 剧本模板蒸馏（AC-PPC-001）
2. 确定性编译器（AC-PPC-002）
3. ref_image 字段（AC-PPC-003）
4. asset-render 契约 + 适配器登记（AC-PPC-004）
5. 去兜底 provider-only（AC-PPC-005）
6. 契约与路由同步（AC-PPC-006）
7. exec 门禁 + 零回归（AC-PPC-007）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-P01 | provider 执行器（真实 HTTP/SDK 调用） | accepted | 属后续海；本湖只出提示词与请求包 |
| DL-P02 | 凭证管理 / .env 读写 | accepted | credentials_never_in_repo |
| DL-P03 | novel / live_drama 复用 asset-render | accepted | 后续湖接入 |
| DL-P04 | 多语种 TTS / Content ID 自动匹配 | accepted | 文本先行 / 仅人工检查单 |
| DL-P05 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-PPC-001 | `script-templates.md` 含完整剧本 / 分集剧本 / 镜头清单三模板 + onlyshot 上游出处与授权 |
| AC-PPC-002 | `scripts/prompt_compiler.py` 从 storyboard + 风格预设产出 `资产提示词.md`/`图片提示词.md`/`视频提示词.md`/`{ep}.srt`；同输入两次**逐字节一致**；未知风格 fail-closed |
| AC-PPC-003 | `storyboard-schema.json` 的 characters/scenes/props/shots 支持 `ref_image`；CLI 声明即须解析到真实文件（fail-closed） |
| AC-PPC-004 | `contracts/asset-render.contract.md` 七节 + fail-closed 码；`registry/render-adapters.yaml` 四阶段 provider 槽位 + 凭证守卫 |
| AC-PPC-005 | CLI 删除 kenburns/edge-tts/音频链；`assemble` 只拼 `clips/` 真实片段 + 烧 AI 标识；无凭证/缺片段/规格不符 → exit≠0，不产替代成片 |
| AC-PPC-006 | form-manga-drama 契约取消 kenburns 并指向 asset-render；form-registry 链含 compile + provider-only；README 与 creation-mode-map 同步 |
| AC-PPC-007 | 新增 `check_prompt_compiler.sh` / `check_render_handoff.sh` PASS；既有门禁零回归 |

## Non-goals

- 不实现任何 provider 的 HTTP/SDK 调用（OpenAI/即梦/Seedance/Kling/Veo/Flux/…）
- 不引入凭证管理或 .env 读写；凭证永不入库
- 不本地生成画面、视频或音频；不做任何"降级/兜底"路径
- 不自动发布；`release_gate: pending_human` 为终态
- 不改 manga_drama FSM 语义与 QA 判据数量（本轮只改渲染来源与产物）
- 不接入 novel / live_drama 的编译器（仅声明后续可复用 asset-render 契约）

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
