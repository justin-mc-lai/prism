# Project adapter · selfmedia-creator

本 skill 落在仓库内，便于不同 vertical 共用同一小黑视觉 DNA，且不依赖全局 `~/.codex/skills` 是否安装。

## 路径

- 权威 skill：`skills/ian-xiaohei-illustrations/SKILL.md`
- Codex 项目镜像：`.codex/skills/ian-xiaohei-illustrations/`（与上同步）
- 产出默认：`content/masters/{vertical}/{slug}/assets/{slug}-illustrations/`

## 生图后端（本机实测 2026-07-22）

| 后端 | 状态 | 说明 |
|------|------|------|
| `agnes-image-2.1-flash` | **可用** | `qi_dev.sh agnes-image-gen`；当前默认 |
| `grok-4.5` | **不可用** | 文本模型；网关明确不支持 `/v1/images/*` |
| `grok-imagine-image` / `grok-imagine-image-quality` | 接口存在，**账号无资格** | 返回 `grok_media_no_eligible_account` |
| Tuzki `gpt-image-*` | **无兼容账号** | `No available compatible accounts` |

Agent 在本项目执行小黑配图时：

1. 先读本目录 `SKILL.md` + `references/*`
2. 出 shot list
3. 默认用 Agnes 文生图；若用户明确要求 Grok 生图，先探测 media 资格，失败则回退 Agnes 并说明原因
4. **不要**把 Grok 4.5 对话模型当作 image generator

## 绑定 vertical

见 `content/registry.yaml` 中 `visual_skill: ian-xiaohei-illustrations`。
