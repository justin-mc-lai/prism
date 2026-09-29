# AI 漫剧管线（ai-manga-drama）

从「故事」到「480p 草稿」的漫剧流水线。需求真源：
`docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/truth.md`（R1 frozen）。
交接契约：`contracts/asset-render.contract.md`。

> **2026-09-21 refreeze（prism-prompt-compiler-v1）**：取消全部本地兜底。
> Prism 只产出**前置文本提示词与 provider 请求包**；画面/视频/语音由下游 provider 生成。
> 无凭证直接终止；FFmpeg kenburns 合成与本地 edge-tts 已删除。

## 六阶段契约

```text
story → storyboard JSON → prompt_compiler（资产/图片/视频提示词 + srt + 分镜脚本）
      → provider 渲染（T2I 建资产 → I2V|T2V 出 clips）→ assemble（拼真实片段 + AI 标识）
      → QA → ReadyForReview
```

> **分镜填写规范（manju-drama）**：分镜声明 `"spec": "manju-drama"` 时启用神魔修仙漫剧规范
> （分镜 15s ⊃ 子镜 3-5s / 在位站位锁定 / 音效必填 / 字秒预算 / 特写配比）：
> 参考 `skills/prism-director/references/drama-storyboard-spec.md`（MJ-* 86 条），
> 门 `contracts/drama-storyboard-spec.contract.md`，实现 `scripts/drama_spec.py`，
> 检查 `scripts/check_drama_storyboard_spec.sh`；编译器额外产出 `分镜脚本.md` + `drama-spec.json`。
> 不声明 `spec` 时为原行为（向后兼容）。

## 目录契约

| 内容 | 路径 |
|------|------|
| 管线契约/schema/检查单 | `content/pipelines/ai-manga-drama/` |
| episode 母稿（storyboard/资产/片段/台账/编译产物） | `content/masters/ai-manga-drama/{slug}/` |
| 成片草稿 | `content/renders/ai-manga-drama/draft/{slug}-480p.mp4` |
| 实现证据 | `.beacon/evidence/implement/prism-prompt-compiler-v1/` |
| QA 证据 | `.beacon/evidence/qa/ai-manga-drama/` |
| drama spec 证据 | `.beacon/evidence/qa/drama-storyboard-spec/` |

> episode 目录由 `init --dir <parent> --episode <slug>` 决定：编译产物（资产/图片/视频提示词、
> `{ep}.srt`、`分镜脚本.md`、`drama-spec.json`、`render-request.json`、`video-manifest.json`、
> `cost-ledger.json`）全部落在该 episode 目录内；成片落在 `content/renders/`。
> （契约 `contracts/form-manga-drama.contract.md` §4 写作 `content/presentations/{vertical}/{slug}/`，
> 属迁移期口径，实际以 `--dir` 为准。）

## 命令索引

```bash
# 1. 建骨架（含 assets/ 与 clips/）
python3 scripts/ai_manga_drama.py init --episode ep-xxx --dir <parent>

# 2. 校验 storyboard（含 ref_image 解析 + drama spec 门，fail-closed）
python3 scripts/ai_manga_drama.py validate --storyboard <episode>/storyboard.json

# 2b. 单独跑分镜规范门（spec: manju-drama；MJ-* 规则）
python3 scripts/drama_spec.py --storyboard <episode>/storyboard.json --json

# 3. 编译前置文本提示词（确定性；风格见 registry/style-presets.yaml）
python3 scripts/prompt_compiler.py --episode <episode> --style cinematic_realism
python3 scripts/prompt_compiler.py --episode <episode> --style x --list-styles

# 4. 出 provider 请求包（无凭证 exit 2，不产假成片）
python3 scripts/ai_manga_drama.py request --episode <episode>

# 5. provider 按提示词渲染：资产图回填 ref_image，片段落 clips/{shot_id}.mp4（480x854）

# 6. 拼真实片段 + 烧 AI 标识（缺片段/规格不符即终止）
python3 scripts/ai_manga_drama.py assemble --episode <episode>

# 7. QA 七类判据
python3 scripts/ai_manga_drama.py qa --episode <episode>
python3 scripts/ai_manga_drama.py manifest --episode <episode>
```

## 渲染策略（provider-only，无兜底）

- **Prism 的产出**：`资产提示词.md` / `图片提示词.md` / `视频提示词.md` / `{ep}.srt` / `render-request.json`
- **provider 的产出**：资产参考图（回填 `ref_image`）、`clips/{shot_id}.mp4`（480x854）、音轨
- **凭证**：环境变量名见 `registry/render-adapters.yaml`（`PRISM_T2I_KEY` / `PRISM_I2V_KEY` /
  `PRISM_T2V_KEY` / `PRISM_TTS_KEY`；视频阶段兼容 `FAL_KEY` / `REPLICATE_API_TOKEN` /
  `SILICONFLOW_API_KEY`）；凭证永不入库
- **无凭证 → `BLOCKED:missing_credential` exit 2，直接终止**
- **缺片段或规格不符 → 拒绝拼接，不偷偷缩放**（`no_local_fallback`）
- 每一集必须保留 `cost-ledger.json`，QA 会读取并校验

## QA 判据（七类）

1. storyboard 通过 schema 校验（含 `ref_image` 解析 + `spec: manju-drama` 时的 drama spec 门）；
2. 每个镜头的 `asset_ref` 真实存在；
3. 编译器三件产物齐备（`资产提示词.md` / `图片提示词.md` / `视频提示词.md`）；
4. 成片存在且非空；
5. ffprobe 时长 60-90 秒、分辨率 480x854；
6. cost-ledger 与 video-manifest 完整；
7. **无本地兜底**：`video-manifest.mode == provider-only`，不得声称 kenburns/edge-tts。

## 发布边界

本管线不发任何平台。成片终态 `release_gate: pending_human`；公开发布必须另走人工审片与发布流程。

## Fixture

`content/pipelines/ai-manga-drama/fixtures/ep-compile-test/` 是编译器确定性回归样本
（8 镜 / 64s / 含 ref_image），供 `scripts/check_prompt_compiler.sh` 使用。

`content/pipelines/ai-manga-drama/fixtures/ep-xianxia-spec/` 是 **manju-drama 分镜规范样本**
（`spec: manju-drama`，4 分镜 × 15s × 5 子镜，含在位站位/音效/特效），
供 `scripts/check_drama_storyboard_spec.sh` 使用（含 11 类负向断言 + 确定性）。
