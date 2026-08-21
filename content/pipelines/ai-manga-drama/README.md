# AI 漫剧管线（ai-manga-drama）

第一版从「故事」到「480p 草稿」的漫剧流水线。需求真源：`docs/beacon/v0.0.5/features/ai-manga-drama/truth.md`（R1 frozen）。

## 六阶段契约

```text
story → storyboard JSON → assets（角色/场景静帧）→ video（Seedance 2.5 / 降级）→ voice/subtitle（本版文本先行）→ assemble + QA → ReadyForReview
```

## 目录契约

| 内容 | 路径 |
|------|------|
| 管线契约/schema/检查单 | `content/pipelines/ai-manga-drama/` |
| episode 母稿（storyboard/角色/资产/台账） | `content/masters/ai-manga-drama/{slug}/` |
| 成片草稿 | `content/renders/ai-manga-drama/draft/{slug}-480p.mp4` |
| 实现证据 | `.beacon/evidence/implement/ai-manga-drama/` |
| QA 证据 | `.beacon/evidence/qa/ai-manga-drama/` |

## 命令索引

```bash
python3 scripts/ai_manga_drama.py init --episode ep-xxx --dir <parent>
python3 scripts/ai_manga_drama.py validate --storyboard content/masters/ai-manga-drama/ep-001-escape/storyboard.json
python3 scripts/ai_manga_drama.py request --episode content/masters/ai-manga-drama/ep-001-escape
python3 scripts/ai_manga_drama.py assemble --episode content/masters/ai-manga-drama/ep-001-escape --mode kenburns
python3 scripts/ai_manga_drama.py qa --episode content/masters/ai-manga-drama/ep-001-escape
python3 scripts/ai_manga_drama.py manifest --episode content/masters/ai-manga-drama/ep-001-escape
```

## 视频生成策略

- 优先：Seedance 2.5（环境变量 `FAL_KEY` / `REPLICATE_API_TOKEN` / `SILICONFLOW_API_KEY` 任一存在时构建 30s 参考链请求）。
- 降级：无视频凭证时 `request` 写 `video-manifest.json` 为 `BLOCKED:missing_credential` 并 exit 2（fail-closed，不产生假视频）；`assemble --mode kenburns` 用分镜静帧 + 缩放运镜合成 480x854 草稿。
- 每一集必须保留 `cost-ledger.json`，QA 会读取并校验。

## QA 判据（五类）

1. storyboard 通过 schema 校验；
2. 每个镜头的 `asset_ref` 真实存在；
3. 成片存在且非空；
4. ffprobe 时长 60-90 秒、分辨率 480x854；
5. cost-ledger 与 video-manifest 完整。

## 发布边界

本管线不发任何平台。成片终态 `release_gate: pending_human`；公开发布必须另走人工审片与发布流程。
