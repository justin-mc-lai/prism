# Gate contract: asset-render（渲染交接门 · provider-only）

> 执行契约。Prism 只产出**前置文本提示词与 provider 请求包**；画面/视频/语音的实际生成
> 交下游 provider。判断框架见 `skills/prism-director/references/{asset-prompt-templates,script-templates,prompt-syntax-table}.md`。
> 适配器登记见 `registry/render-adapters.yaml`。

## 1. identity

- gate_id: asset-render
- 适用形态: manga_drama（首批）、comic / vlog / book_video / live_drama（后续复用）
- 定位: **交接门**——Prism 交出提示词与请求包，provider 交出像素；无凭证即终止，**无任何本地兜底**
- 编译器: `scripts/prompt_compiler.py`（确定性，同输入同输出）
- 管线: `scripts/ai_manga_drama.py`（init / validate / request / assemble / qa / manifest）

## 2. 决策边界

- 能决定：提示词编译、风格预设选择、阶段凭证是否齐备、请求包结构、片段规格判定
- 不能决定：母稿事实与正典、QA 最终 verdict、公开发布、**任何 provider 的实际调用**
- **不做**：本地合成画面（禁 FFmpeg 缩放运镜）、本地 TTS、任何"降级/兜底"路径

## 3. intake（必填）

- 已冻结 `storyboard.json`（过 `storyboard-schema.json`；`ref_image` 声明即须解析到真实文件）
- 资产身份参考图已回填（`characters[].ref_image` / `scenes[].ref_image` / `props[].ref_image`）
- 选定风格预设 id（`registry/style-presets.yaml` ⊕ `lumenx-style-presets.json`，按 id 合并）
- `cost-ledger.json` 已初始化（每次 provider 尝试必记 provider/status/retries/cost 或 n/a）

拒绝：storyboard 不合法 / ref_image 未解析 / 风格预设未知 / 未过编译器 →
blocked + reason_code（`render_storyboard_invalid` / `render_ref_unresolved` / `render_style_unknown` /
`render_compile_missing`）

## 4. output

- 编译产物（episode 目录内）：
  - `资产提示词.md` — 资产 ref 提示词（T2I，一实体一条，中性平光）
  - `图片提示词.md` — 每镜图片提示词（I2I/T2I，8 段）
  - `视频提示词.md` — 每镜视频提示词（I2V/T2V）
  - `{episode}.srt` — 字幕 sidecar（由台词 + 镜时长派生，纯文本）
- provider 请求包：`render-request.json`（`stages[]` 四阶段状态 + `segments[]` + `references.images`）
- 成片：`content/renders/ai-manga-drama/draft/{episode}-480p.mp4`（由 provider 片段拼接而成）
- 证据：`.beacon/evidence/qa/prism-prompt-compiler-v1/SCORECARD.json`

**FSM（沿用）**：Outlined → Storyboarded → AssetsReady → Drafting → DraftReady → Finalized；
Rejected 仅可 revise 回 Drafting。非法跃迁禁止（含 **未过编译器 → assemble**）。

## 5. gate（六判据，任一失败 fail-closed）

1. **编译产物齐备**：`资产提示词.md` / `图片提示词.md` / `视频提示词.md` 三者存在（`prompt_artifacts`）
2. **确定性**：同 storyboard + 同风格两次编译**逐字节一致**（无时间戳/随机进正文）
3. **资产引用**：全部 `asset_ref` 存在；声明 `ref_image` 的条目均已解析（并过资产一致性门
   `contracts/asset-consistency.contract.md`）
4. **凭证齐备**：`t2i` 与（`i2v` 或 `t2v`）阶段凭证在场；缺任一 → `BLOCKED:missing_credential` exit 2
5. **片段规格**：`clips/{shot_id}.mp4` 逐个存在且为 480x854；缺片段或规格不符 →
   **拒绝拼接，不偷偷缩放**（`no_local_fallback`）
6. **AI 提示标识**：成片明显位置带 AI 标识（《微短剧发展管理办法》总局令第 16 号义务）

附加门：`prompt-syntax.contract.md` 八判据（镜头提示词语法）在编译阶段叠加；
文案过 anti-slop-gate；localization-checklist 四类检查点被 episode README 引用。

## 6. license / 凭证注记

- 凭证**永不入库**（`credentials_never_in_repo`）；环境变量名见 `registry/render-adapters.yaml`
- 上游 MIT / Apache-2.0 提示词工艺（onlyshot、lumenx）商用须保留
  `docs/ATTRIBUTION-drama-prompt-repos.md` 声明与随附 LICENSE
- 本形态不接任何平台发布通道；`release_gate: pending_human` 为终态

## 7. handoff / 失败处理

- 下一公开面：prism-qa → prism-release（草稿审片；公开发布需人工二次批准）
- 可重试：`compile`（换风格/改 storyboard）、`request`（换 provider）、`assemble`（片段补齐后重拼）
- 必须停：**无凭证**（不降级）、片段缺失（不合成）、规格不符（不缩放）、事实/正典问题、任何发布动作
- 禁止自证通过：true

## Non-goals

- 不实现任何 provider 的 HTTP/SDK 调用；不管理凭证；不写 `.env`
- 不本地生成画面、视频或音频；**不保留任何降级路径**（kenburns / edge-tts 已删除）
- 不做 Content ID 自动匹配（仅人工检查单）；不做多语种 TTS（文本先行）
