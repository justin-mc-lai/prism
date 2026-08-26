# Project adapter · comic-storyboard (selfmedia-creator)

Based on [SyMind/codex-comic](https://github.com/SyMind/codex-comic) (MIT).  
Skill id in this repo: **`comic-storyboard`** (folder name). Upstream frontmatter may still say comic-workflow; prefer this PROJECT for routing.

## When to use

- **`qinggan-gzh` / `emotion-comic` / matrix `qinggan-comic`**
- 多格、条漫、分镜、竖版故事页
- **不要**用 `character-illustrations` 硬画多格漫画页

## Backend priority (this machine)

1. **baoyu-comic**（若 agent 环境已装 `~/.codex/skills/baoyu-comic`）— 知识/叙事分镜 + 串图  
2. **本 skill 工作流** — 脚本/bible/提示词；出图优先 ChatGPT 网页（需 Chrome 插件）  
3. **Agnes image** — 仅当 1/2 不可用时，用 `references/prompt-templates.md` 单页出图，比例尽量 3:4

## Isolation

- 输出目录必须在：  
  `content/masters/emotion-comic/{slug}/comic/`  
  （script / bible / pages / prompts）
- 禁止写入 `airline-info` / `oss-picks` assets
- 角色 bible 与 `character-illustrations/characters/qinggan-star.md` **分开**：  
  - 16:9 单图概念 → qinggan-star  
  - 连载页角色 → `comic/bible/characters.md`

## Registry

```yaml
comic_skill: comic-storyboard
# optional fallback
comic_skill_fallback: baoyu-comic
```
