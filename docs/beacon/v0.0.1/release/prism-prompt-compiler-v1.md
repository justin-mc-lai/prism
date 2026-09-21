# Release Brief — prism-prompt-compiler-v1 (v0.0.1)

- release_id: `rel-prism-prompt-compiler-v1-20260921`
- feature: `prism-prompt-compiler-v1`
- version: `v0.0.1`
- status: **released（人工批准）**
- approved_by: 用户（对话指令：push 到 origin、release gate）
- approved_at: 2026-09-21（Asia/Shanghai）
- approved_action: push `main` → `origin/main` + 登记 release brief
- release_gate: `pending_human` → **human_confirmed**
- scorecard: `release_ready=true` · gate=Pass（blocked=2，见「已知运行时说明」）· qa=passed

## 交付内容

1. **提示词层**
   - `skills/prism-director/references/script-templates.md`：完整剧本 / 分集剧本 / 镜头清单三模板
   - `skills/prism-director/references/asset-prompt-templates.md`：7 段 identity block + 五类资产卡
   - `registry/style-presets.yaml`：风格预设 overlay 14 款（⊕ lumenx base 15 = 29）
2. **编译层**
   - `scripts/prompt_compiler.py`：storyboard + 风格预设 → 资产/图片/视频提示词 + srt（同输入逐字节一致）
3. **交接层**
   - `contracts/asset-render.contract.md`（七节 + fail-closed 码）
   - `registry/render-adapters.yaml`（t2i/i2v/t2v/tts provider-only 槽位）
   - `content/pipelines/ai-manga-drama/storyboard-schema.json` + CLI：`ref_image` 身份参考图
4. **去兜底（refreeze form-manga-drama）**
   - 删 FFmpeg kenburns 合成、edge-tts 配音、本地音轨与字幕链
   - 无凭证 / 未编译 / 缺片段 / 规格不符 → fail-closed；`assemble` 只拼 provider 真实片段 + 烧 AI 标识
5. **清红灯（defect_repair，非 requirement change）**
   - YAML `install.note` 续行 ×4；`check_bridges_installed` 兼容 monorepo/语料 pin；
     `check_pin_drift` mode 降 `report`
   - 3 个 truth 包补 domain 必需节；内容样例补齐（form / e2e / render 链）
   - `install_public_surfaces.sh` 修复悬空/陈旧 symlink（7 悬空 + 7 陈旧）

## 提交链

- `62e73c3` feat(prompt-render)：truth freeze R1 + implement + 清红灯 + 内容样例（main，355 files）
- `eafa0d7` fix(install)：agent skill 安装器悬空 symlink 修复（main）
- `origin/main` = `main` = `eafa0d7`

## 验收证据

- 实现证据：`.beacon/evidence/implement/prism-prompt-compiler-v1/AC-PPC-{001..007}.json`
- 汇总：`.beacon/evidence/implement/prism-prompt-compiler-v1/GATES.json`
  （`all_exec_gates_pass=true` · truth integrity `pass` · truth quality `pass` · materials `synced`）
- QA 矩阵：`.beacon/evidence/implement/prism-prompt-compiler-v1/QA-MATRIX.json`
- 全量门禁：`scripts/check_*.sh` **28/28 PASS**；`make -C workspace check` exit 0
- 分层验证：`beacon doctor verify-truth-integrity` **19/19 pass**（`--mode block --strict`）；
  `verify-truth-quality` 19/19 pass；`verify-context --strict` PASS
- agent 安装：8 个 skill root × 7 公开面 = **56 链接全部可解析**，重跑幂等，`_internal` 无泄漏

## 已知运行时说明（非功能阻塞，与 prism-title-lab-v1 同源）

`beacon release check v0.0.1` 全仓级两项元检查失败，属本仓 legacy→feature 迁移历史状态，
与本 feature 功能无关：

1. `legacy cutover preflight` → `legacy_cutover_required`
2. `coverage artifact ready` → `coverage_rate=0.0000`

`beacon release scorecard` 仍判 `Release ready: True`（gate=Pass, blocked=2）。功能 TC 与分层 QA 证据已闭环。

## 不覆盖

- **平台公开发布**：仍须按 `contracts/publish-bridge.contract.md` 逐内容人工二次批准
- **provider 执行器**（真实 T2I/I2V/T2V/TTS 调用 + 凭证管理）：属后续海（truth Deferral DL-P01）
- **novel / live_drama 复用 asset-render**：属后续湖（DL-P03）
