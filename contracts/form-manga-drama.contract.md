# Form contract: manga_drama（Lake D）

> 状态：**registered**（2026-08-21 human 指令转正）。
> 源真相：`selfmedia-creator/docs/beacon/v0.0.5/features/ai-manga-drama/truth.md@R1`
> （frozen 2026-08-21），按 sot-layering-decision.md D4 迁移，源 truth 降级为 research 输入。
> 实现已 pin：`scripts/ai_manga_drama.py`（A4 MIT）+ `content/pipelines/ai-manga-drama/`；
> 首集 ep-001-escape QA SCORECARD pass（87.6s / 480x854 / cost-ledger 12 条），实例暂留源仓作
> v0.0.5 证据绑定（历史例外），新实例一律落 Prism。
> 一句话：英文小故事 → 9:16、60–90s、480p 成片草稿；Seedance 2.5 有凭证走视频链，
> 无凭证 FFmpeg kenburns 降级；两路证据格式完全一致；终态停在人工审片门。

## 1. identity

- form_id: manga_drama
- lane: standard
- bridge 路由（**provider-only，无兜底**；2026-09-21 refreeze）:
  - 编译 → `scripts/prompt_compiler.py` 产出 `资产提示词.md` / `图片提示词.md` / `视频提示词.md` / `{ep}.srt`
    （确定性，同输入同输出）
  - 渲染 → 下游 provider only：T2I 建资产参考图 → I2V（或 T2V）出 `clips/{shot_id}.mp4`
  - **凭证缺失 → 显式 `BLOCKED:missing_credential` exit 2，直接终止；不做任何本地合成兜底**
    （FFmpeg kenburns 与本地 edge-tts 已于 prism-prompt-compiler-v1 删除）
- 交接契约: `contracts/asset-render.contract.md`（六判据 + provider 槽位登记见 `registry/render-adapters.yaml`）
- CLI: `scripts/ai_manga_drama.py`（init / validate / request / assemble / qa / manifest；已 pin，
  schema 位于 `content/pipelines/ai-manga-drama/storyboard-schema.json`）

## 2. 决策边界

- 能决定：provider/fallback 选择、episode 骨架、合成参数、重试与换 provider
- 不能决定：母稿事实与正典、QA 判定、公开发布（release_gate 终态 = `pending_human`）、凭证管理

## 3. intake（director handoff 必填）

- story：故事文档已落盘（`story_documented`）
- storyboard.json：8–12 镜头、9:16、目标 60–90 秒、台词文本先行、含角色卡（character sheet）
  与 asset_ref，通过 `storyboard-schema.json` 校验（`schema_valid`）；asset_ref 须解析到
  assets/ 身份条目并带识别锚点（未决项不得流入分镜）
- 资产三类（`storyboard-schema.json`）：`characters[]` 必填；`scenes[]`（`kind` ∈
  `interior`/`exterior`）与 `props[]`（`holder` 指向 `characters[].id`）可选，声明后
  镜头的 `scene_ref` / `prop_refs` 必须逐个解析（fail-closed）
- cost-ledger.json 已初始化（每次生成尝试必记 provider/status/retries/cost 或 n/a，禁止空壳兜底）

拒绝：缺任一交接字段 → blocked + reason_code（`manga_story_missing` / `manga_storyboard_invalid` /
`manga_ledger_missing`）。

## 4. output

- episode：`content/presentations/{vertical}/{slug}/manga-drama-{ep}/`
  （storyboard.json、assets/、video-request.json、video-manifest.json、cost-ledger.json、README）
- 成片：同目录 `draft/ep-{slug}-480p.mp4`（480x854、60–90 秒，ffprobe 可验）
- 声音链（**交下游 provider**，`assemble` 不再本地合成）：配音与字幕状态写进 `video-manifest.json`；
  `{ep}.srt` 由编译器作为**纯文本产物**产出（台词 + 镜时长派生），不做本地 TTS 与音频 mux
- 证据：`.beacon/evidence/qa/prism-form-manga-drama-v1/SCORECARD.json`

FSM（沿用源 R1）：Outlined → Storyboarded → AssetsReady → Drafting → DraftReady → Finalized，
Rejected 仅可 revise 回 Drafting；非法跃迁禁止：Storyboarded→Finalized、Outlined→Drafting、
DraftReady→Storyboarded、Finalized→Rejected、Rejected→Finalized。

## 5. gate（六类判据，任一失败 exit 非 0）

1. schema：storyboard.json 过 JSON Schema 校验
2. 资产引用：全部 asset_ref 存在（`asset_refs_exist`）；声明的 `ref_image` 均已解析
   （`render_ref_unresolved`）；并过**资产一致性门**
   `contracts/asset-consistency.contract.md`（三分法归类 / binding 解析 AST-05 /
   边界匹配 CON-01 / 变化记录 CON-04 / 画风统一；蒸馏依据
   `skills/prism-director/references/asset-consistency-gate.md` MAP-017）
3. 编译产物：`资产提示词.md` / `图片提示词.md` / `视频提示词.md` 三者齐备（`prompt_artifacts`）
4. 成片存在且非空
5. 时长/分辨率：ffprobe 实测 60–90s、480x854
6. 台账完整：cost-ledger 覆盖全部 provider 尝试
7. **无本地兜底**：`video-manifest.json` 的 `mode` 必须为 `provider-only`，且不得声称
   `ffmpeg-kenburns` / `edge-tts`（`no_local_fallback`）；片段规格不符或缺失一律终止，
   **拒绝拼接与缩放**（`contracts/asset-render.contract.md` §5）

附加门：localization-checklist 四类检查点（台词重构 / 敏感题材 / 价值观 / 平台版权规则）
被 episode README 引用；文案过 anti-slop-gate；
**AI 提示标识**：本形态为 AI 生成内容，每集成片明显位置必须带 AI 提示标识
（《微短剧发展管理办法》总局令第 16 号义务，2026-09-01 施行）。

## 6. license / 凭证注记

- **无凭证直接终止**（`BLOCKED:missing_credential` exit 2），**不做任何降级或兜底**
  （2026-09-21 refreeze；原 kenburns 降级路径已删除）；凭证环境变量名见
  `registry/render-adapters.yaml`，凭证不入仓（`credentials_never_in_repo`）
- **AI 提示标识由 CLI 强制烧录**（assemble 内置，缺中文字体即 fail-closed）；本形态不接任何平台
  发布通道；`release_gate: pending_human` 为终态，仓库内无自动发布命令

## 7. handoff / 失败处理

- 下一公开面：prism-qa → prism-release（草稿审片；公开发布需人工二次批准——当前版本无此路径）
- 可重试：`compile`（换风格/改 storyboard）、`request`（换 provider）、`assemble`（片段补齐后重拼）、
  revise（Rejected → Drafting）
- 必须停：**无凭证**（不降级）、**片段缺失或规格不符**（不合成、不缩放）、CLI bridge 缺失、
  事实/正典问题、任何发布动作
- 禁止自证通过：true

## Non-goals（继承源 R1，2026-09-21 refreeze 增补）

真人短剧 / 数字人；多集批量调度与队列；模型训练微调与本地权重；多语种 TTS 接入
（文本先行）；Content ID 自动匹配（仅人工检查单）。
**新增**：任何本地兜底合成（FFmpeg kenburns / edge-tts / 本地音轨）；provider SDK 实现与凭证管理
（Prism 只出提示词与请求包）。
