---
slug: prism-form-image-post-v1
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
  prd: docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md
  user_story: docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md
  test_case: docs/beacon/v0.0.1/features/prism-form-image-post-v1/tests.md
provenance:
  - ac_id: AC-IMG-001
    source_type: migrated_truth
    source_ref: "Lake A MAP-006 · selfmedia-account-pipeline"
  - ac_id: AC-IMG-002
    source_type: source_evidence
    source_ref: "selfmedia-account-pipeline title/caption/1-9/cover rules"
---

# Requirement Truth: prism-form-image-post-v1（v0.0.1 · Lake D3）

## 人话

D3 落地两个**图像形态**的生产者契约：公众号贴图包（image-post）和小红书图文（xhs）。
贴图包规则从源仓 `selfmedia-account-pipeline` 蒸馏：标题 ≤20 字且不带账号前缀、caption 独立、
图片 1–9 张（超 9 拆条）、封面必须无文字底图 + 本地排版、QA 查乱码/图序/尺寸/图文分离。
渲染脚本与 xhs 工具一律 bridge（缺失即 blocked），账号硬编码必须清洗成配置。

- 能做：form-registry 注册 image-post/xhs；`contracts/form-image-post.contract.md`；
  `contracts/form-xhs.contract.md`；creation-mode-map 路由；exec 校验脚本。
- 不能做：novel（D4）、comic/vlog/book_video（D5）、发布桥（D6）；不 vendor_pin；不做 metrics。
- 怎样算完：四件套填满；AC 全有 TC；exec PASS；truth review + freeze；implement → QA → release 人工门。

## User Intent

继续 Lake D：落贴图包 + 小红书图文形态，验证“图像形态契约 + bridge 渲染 + OCR 门”闭环。

## User Intent Snapshot

```yaml
lake_or_ocean: 海
this_lake: Lake D3（image-post / xhs forms）
user_decision: promoted
scope_mode: phased_lake
sea_promise: full_selfmedia_creation_capability
delivery: sub-lakes D1..D6
source_deferral: DL-003 / INT-P14
feature: prism-form-image-post-v1
version: v0.0.1
depends_on: prism-form-writing-v1（D1）· prism-form-blog-thread-v1（D2 form registry）
```

## Intent Coverage Matrix

| intent_id | source | strength | landing | status |
|-----------|--------|----------|---------|--------|
| INT-I01 | migrated | must | AC-IMG-001 | covered |
| INT-I02 | migrated | must | AC-IMG-002 | covered |
| INT-I03 | migrated | must | AC-IMG-003 | covered |
| INT-I04 | migrated | must | AC-IMG-004 | covered |
| INT-I05 | migrated | must | AC-IMG-005 | covered |
| INT-I06 | migrated | must | AC-IMG-006 | covered |
| INT-I07 | migrated | must | AC-IMG-007 | covered |
| INT-I08 | migrated | must | AC-IMG-008 | covered |
| INT-I09 | migrated | must | AC-IMG-009 | covered |
| INT-I10 | migrated | must | AC-IMG-010 | covered |
| INT-I11 | sea | must | D4–D6 其余形态 | deferred |

## First principles（域）

| ID | Constraint |
|----|------------|
| FP-IMG-001 | title/caption/图片/封面四分离；title ≤20 字、不带账号前缀 |
| FP-IMG-002 | 图片 1–9 张；超 9 拆条；图序与尺寸必须 QA 核验 |
| FP-IMG-003 | 封面只允许无文字底图 + 本地标题排版；模型不得画正文文字 |
| FP-IMG-004 | render 脚本与 xhs 工具 bridge；缺失 fail-closed，不产出假文件 |
| FP-IMG-005 | 账号硬编码（kushi-gzh 等）禁止进 Prism 契约，一律配置化 |
| FP-IMG-006 | 只创建草稿；公开发布必须人工二次批准；误传文章 Tab → superseded-misrouted + do_not_publish |
| FP-IMG-007 | 继承 FP-PRISM-002/004/013 |

## 用户旅程 / 故事

US-IMG-001：战役负责人要贴图包。director 出 shot list（visual_carrier）→ produce 按
`form-image-post.contract` 生成 1–9 张图 + caption + 封面 → QA 按 OCR/图序/尺寸/图文分离核验 →
release 创建草稿（不自动公开）。

US-IMG-002：用户要小红书图文。produce 按 `form-xhs.contract` bridge xhs-article-to-images →
OCR 门 → release；工具缺失时明确 blocked。

US-IMG-003：新账号接入。只改账号配置/registry，不改契约；禁止把账号名写死进正文。

## Domain Model

| Entity | Key | Notes |
|--------|-----|-------|
| ImagePostFormContract | form-image-post | 贴图包：title/caption/图/封面四分离 |
| XhsFormContract | form-xhs | 小红书图文 bridge |
| ShotList | shot list | director → produce 的视觉载体 |
| AssetBundle | images/caption/cover | 1–9 张 + 独立 caption + 本地排版封面 |

## Domain FSM（D3 落地）

状态：image_planned → forms_registered → image_contract_landed → xhs_contract_landed → routing_landed → indexed → qa_pass → release_candidate → human_accepted

| State | From | Guard |
|-------|------|-------|
| forms_registered | image_planned | form-registry 含 image-post+xhs |
| image_contract_landed | forms_registered | form-image-post.contract present |
| xhs_contract_landed | image_contract_landed | form-xhs.contract present |
| routing_landed | xhs_contract_landed | creation-mode-map 引用 form contracts |
| indexed | routing_landed | exec 脚本 + 无泄漏 |
| qa_pass | indexed | all TC pass |
| release_candidate | qa_pass | evidence complete |
| human_accepted | release_candidate | human confirmed |

## Illegal transitions

- image_planned → routing_landed（跳过注册/契约）
- indexed → human_accepted（跳过 QA）
- 模型生成带文字图片充当封面/正文
- 图片 >9 张仍单包
- bridge 缺失仍产出
- 未人工批准进入发布
- 宣称 Lake D 全部完成

## FSM 五元组

| State | Event | Guard | To | Action |
|-------|-------|-------|-----|--------|
| image_planned | register_forms | image-post+xhs in registry | forms_registered | update form-registry |
| forms_registered | land_image_contract | image contract present | image_contract_landed | write form-image-post.contract |
| image_contract_landed | land_xhs_contract | xhs contract present | xhs_contract_landed | write form-xhs.contract |
| xhs_contract_landed | wire_routing | route refs present | routing_landed | update creation-mode-map |
| routing_landed | index | exec script + no leak | indexed | write check script |
| indexed | qa | TCs pass | qa_pass | write evidence |
| qa_pass | package | evidence complete | release_candidate | release brief |
| release_candidate | human_ok | human confirmed | human_accepted | release |

## Alignment Surface

1. form registry image-post/xhs（AC-IMG-001）
2. image-post 契约（AC-IMG-002）
3. xhs 契约（AC-IMG-003）
4. 路由引用（AC-IMG-004）
5. exec 脚本（AC-IMG-005）
6. 账号硬编码清洗（AC-IMG-006）
7. bridge fail-closed（AC-IMG-007）
8. OCR/QA 门（AC-IMG-008）
9. maker≠checker（AC-IMG-009）
10. Non-goals / deferral（AC-IMG-010）

## Deferral Ledger

| deferral_id | item | user_decision | reason |
|-------------|------|---------------|--------|
| DL-I01 | novel 形态本体 | accepted | D4 |
| DL-I02 | comic/vlog/book_video 本体 | accepted | D5 |
| DL-I03 | publish/schedule 桥 | accepted | D6 |
| DL-I04 | vendor_pin 渲染/图像大栈 | accepted | license review + ATTRIBUTION |
| DL-I05 | metrics/learning loop | accepted | Lake E |
| DL-I06 | 本子湖宣称海 closure | rejected | FP-PRISM-013 |

## Acceptance Criteria

| AC ID | Description |
|-------|-------------|
| AC-IMG-001 | 进入 `forms_registered`：form-registry 登记 image-post 与 xhs，各含 contract 引用与生产链 |
| AC-IMG-002 | 进入 `image_contract_landed`：`contracts/form-image-post.contract.md` 声明 title≤20 无前缀、caption 独立、1–9 张/超9拆条、封面本地排版、QA 清单（乱码/图序/尺寸/分离）与 fail-closed |
| AC-IMG-003 | 进入 `xhs_contract_landed`：`contracts/form-xhs.contract.md` 声明 bridge xhs-article-to-images、OCR 门、fail-closed |
| AC-IMG-004 | 进入 `routing_landed`：creation-mode-map 贴图包/xhs 行引用 form contracts |
| AC-IMG-005 | 进入 `indexed`：`scripts/check_image_post_forms.sh` exec-layer 校验 PASS |
| AC-IMG-006 | 账号硬编码清洗：契约声明账号/平台走配置，禁止 kushi-gzh 等硬编码进正文 |
| AC-IMG-007 | render bridge fail-closed：渲染脚本/xhs 工具缺失 → blocked + reason_code |
| AC-IMG-008 | OCR/QA 门：QA 检查无乱码/随机文字、图序、尺寸、caption/title 分离、价值门，证据可引用 |
| AC-IMG-009 | maker≠checker：form 契约与 anti-slop-gate/OCR 检查分离 |
| AC-IMG-010 | Non-goals：D4–D6、vendor_pin、metrics、平台 API 显式排除；不得宣称海 closure |

## Non-goals

- 不实现 novel（D4）、comic/vlog/book_video（D5）、发布桥（D6）
- 不 vendor_pin 图像/渲染大栈
- 不做 metrics（E）/ monetization（F）
- 不接平台 API；不自动公开
- 不把 D1–D3 宣称为完整创作能力已交付

## Freeze readiness

- [x] L0 人话
- [x] Intent Coverage Matrix
- [x] Domain FSM
- [x] tests.md 覆盖全部 AC
- [x] Deferral 无未决项
