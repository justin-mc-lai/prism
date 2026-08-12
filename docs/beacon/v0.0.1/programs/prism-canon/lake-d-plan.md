# Lake D Program Plan — 八形态生产链（pln-program）

- program: prism-canon · version: v0.0.1 · lake: D
- plan_mode: interactive · scope_mode: phased_lake
- 海承诺: full_selfmedia_creation_capability（Lake D = 完整创作能力主体，must）
- 来源: selfmedia-creator `prism-canon-v1@R3`（INT-P14 / DL-003）+ registry/adapter-migration-matrix.md MAP-002/005/006/007/008
- 生成日期: 2026-08-12

## Intent（一行）

把八形态内容生产链（blog / thread / 贴图包 / 小红书图文 / novel / comic / vlog / book_video）按
“先文本后视觉、先轻量后重资产、bridge 优先、distill 只收可复用规则”拆成子湖，逐个冻结与实现，
最终支撑 US-PRISM-001/002 主链（intel → master → director → produce → qa → release）。

## 源能力清单（selfmedia-creator → Prism）

| 簇 | 源 skills | 角色 | 策略 |
|---|---|---|---|
| 写作/叙事 | selfmedia-writing、kushi-narrative-zh、create-content、writing-agent、oss-repo-read | 成稿主链 | distill 自研规范（四段式/日榜/情绪长文）；bridge writing-agent 与 oss-repo-read |
| 人话/反 slop | selfmedia-humanize、humanizer-zh、qu-ai-wei、shuorenhua、no-ai-slop、stop-slop、humanizer-en、de-ai-prompt-enhancer | 人味改写/机检降痕 | distill 判据进 prism-qa（人话策略、slop 模式清单）；bridge 具体工具按名调用 |
| 导演 | selfmedia-director | treatment / presentation map / shot list | distill handoff 契约字段（MAP-002），主体已是 director 面 |
| 贴图/账号 | selfmedia-account-pipeline + render_wechat_article_pages / html_cards / image_cards | 账号产出包 | distill shot-list/caption 元数据规则；bridge 渲染脚本；清洗账号硬编码 |
| 小红书 | xhs-article-to-images（若已安装） | 小红书图文 | bridge + OCR 门 |
| 漫画 | comic-storyboard | 3:4 竖版漫画 | bridge（ChatGPT 网页流程）；distill 版式/文字可读性规则 |
| 视频 | openmontage（AGPL-3.0）、book-video、rnskill 视频族 | vlog/book_video | bridge 优先；vendor_pin 需 license review + ATTRIBUTION；distill director handoff 字段 |
| 发布 | publish-content、schedule-post、x-publish、manage-media | 草稿/排期 | bridge；公开仍人工批准（publish-approval 内核已具备） |

## 子湖拆分与顺序

| 子湖 | feature slug | 形态 | 交付物 | 策略 |
|---|---|---|---|---|
| D1 | prism-form-writing-v1 | 基础写作/人话/反 slop 链（地基） | writing.contract.md 正文、anti-slop-gate.md、人话判据、creation-mode-map 路由更新、check_writing_adapters.sh | distill + bridge |
| D2 | prism-form-blog-thread-v1 | blog 深度长文 + X thread | form 注册（blog/thread）、producer 契约（四段式/倒金字塔/快道）、bridge writing-agent | distill + bridge |
| D3 | prism-form-image-post-v1 | 贴图包（article-paper/短卡）+ 小红书图文 | shot-list/caption 规则、render bridge 路由、OCR 门、form 注册 | distill + bridge |
| D4 | prism-form-novel-v1 | novel 连载 | 长文本 producer、canon episode 钩子（接 Lake C）、bridge kushi-narrative-zh | bridge + distill |
| D5 | prism-form-av-v1 | comic + vlog + book_video | director handoff 字段、bridge 路由、license 注记 | bridge 优先 |
| D6 | prism-publish-bridge-v1 | 发布/排期桥 | publish/schedule 路由、草稿合同、人工批准集成 | bridge |

顺序理由：

1. D1 先做——所有形态都依赖写作、人话、反 slop 门，先把地基煮干。
2. D2 文本形态最轻、无外部重资产，能快速验证整条链。
3. D3 贴图依赖 D1 文案 + director shot list（MAP-006）。
4. D4 novel 依赖 Lake C 的 canon 门与长文本写作。
5. D5 AV 最重（外部运行时 + license），放后且 bridge 优先。
6. D6 发布桥跨形态收口。

## Bridge / Distill 规则

- **bridge**：live network、API keys、大运行时、外部 monorepo（writing-agent、humanizer 系列、xhs 工具、openmontage、comic-storyboard、publish/schedule）→ 按名调用已安装 skill/脚本；找不到必须 fail-closed，不假装生成。
- **distill**：只收通过 复用性/生成性/独特性/边界 扫描的规范与门禁——反 slop 模式清单、人话判据、四段式/倒金字塔结构、shot-list/caption 元数据、director handoff 字段、发布审批清单。
- **vendor_pin**：Lake D+ 才允许；必须 license allowlist + ATTRIBUTION；AGPL OpenMontage 默认不 pin，只 bridge。
- **defer**：metrics（E）、monetization（F）、selfmedia-sync-ai 分发 API、全量 vendor 树。

## 风险与门禁（pln-review 摘要）

- R1 外部 skill 依赖宿主安装路径：bridge 必须 fail-closed（缺路径 → 明确 blocked，不产出假文件）。
- R2 账号硬编码（kushi-gzh 等）必须清洗成 registry/配置，禁止进 Prism 正文。
- R3 AV vendor license：默认 bridge；pin 需人工批准 + ATTRIBUTION。
- R4 每子湖独立 feature 包，禁止 8 形态塞一个包（范围失控）。
- R5 exec-layer 测试必须带真实断言（吸取 Lake C `assertion_count_zero_pass` 教训）。
- R6 每个子湖走完整门：truth review → freeze → implement（worktree）→ QA → release 人工门；不得宣称 Lake D 全部完成直到 D1–D6 全过。

## Route

D1 → beacon-gen-truth → Truth Review Gate → freeze → implement → QA → 进入 D2（重复）。
全子湖完成前不得宣称海 closure；每个子湖 release 均需人工确认。
