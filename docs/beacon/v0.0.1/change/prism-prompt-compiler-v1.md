# Beacon Feature Change Projection

- feature: `prism-prompt-compiler-v1`
- feature_slug: `prism-prompt-compiler-v1`
- version: `v0.0.1`
- artifact_role: `release-facing projection/read model`
- truth_source: `false`

## Scope
- Lake B′：Prism 作为 agent skill 产出**全部前置文本提示词 + provider 请求包**；
  渲染（T2I/I2V/T2V/TTS）交下游 provider。
- 去兜底：取消 FFmpeg kenburns 合成与本地 edge-tts 配音；无凭证 fail-closed 终止，不产假成片。
- 四件套：剧本模板蒸馏 · 确定性提示词编译器 · 分镜 ref_image 字段 · asset-render 契约与适配器登记。

## Added
- docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/{truth,tasks,tests,evidence}.md
- skills/prism-director/references/script-templates.md
- scripts/prompt_compiler.py
- contracts/asset-render.contract.md
- registry/render-adapters.yaml
- scripts/check_prompt_compiler.sh
- scripts/check_render_handoff.sh

## Removed
- `scripts/ai_manga_drama.py`：kenburns 合成路径（`cmd_assemble` 的 ffmpeg zoompan 段）
- `scripts/ai_manga_drama.py`：本地 TTS 链（`VOICE_PROVIDERS` / `resolve_edge_tts` / `synth_voice` /
  `EDGE_TTS_CANDIDATES` / `DEFAULT_VOICE_ID` / `--voice` / `--voice-id`）
- `scripts/ai_manga_drama.py`：音频 mux 与 `--allow-audio-overflow`；`SUBTITLE_MODES`/`--subtitles` 本地链
- 契约层 kenburns 降级表述（`form-manga-drama.contract.md` §1/§5/§6）

## Fixed
- `content/pipelines/ai-manga-drama/storyboard-schema.json`：characters/scenes/props/shots 支持 `ref_image`
- `scripts/ai_manga_drama.py`：`assemble` 改为只拼接 episode `clips/` 下 provider 真实片段 + 烧 AI 标识；
  缺任一片段 fail-closed
- `registry/form-registry.yaml`：manga_drama producer_chain 插入 compile 步骤、渲染来源改为 provider-only
- `content/pipelines/ai-manga-drama/README.md` + `skills/_internal/orchestration/creation-mode-map.md`：去兜底同步
- `scripts/check_asset_consistency.sh`：移除已删符号（`VOICE_PROVIDERS`/`synth_voice`/`allow-audio-overflow` 等）断言

## Refreeze
- `contracts/form-manga-drama.contract.md` 由「源 truth R1 kenburns 降级」refreeze 为「provider-only，无兜底」；
  冻结依据：用户 2026-09-21 决策（见 truth.md provenance AC-PPC-005）。
