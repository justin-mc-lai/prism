---
name: create-content
description: |
  AI 驱动的自媒体内容创作 Skill。支持图文、短视频生成，覆盖微信公众号、小红书、抖音等平台。
  可根据选题自动研究、撰写、配图、生成视频。
  
  触发方式：
  - Hermes: "创作一篇关于{topic}的{platform}文章"
  - Codex: "/create-content --topic {topic} --platform {platform}"
  - Claude: "帮我创作一篇{platform}内容，主题是{topic}"
triggers:
  - pattern: "创作.*关于(.+)的(.+)"
    platforms: [wechat-gzh, xiaohongshu, douyin, twitter]
  - pattern: "/create-content"
    args: [topic, platform, style]
  - pattern: "帮我创作.*"
    args: [topic, platform]
---

# Create Content Skill

## When to Use

Use this skill when:

- 用户需要创作自媒体内容（文章、笔记、短视频）
- 用户提供了主题/选题，需要 AI 生成完整内容
- 用户需要为特定平台（微信公众号、小红书等）定制内容
- 用户需要配图或视频素材

## Workflow

### Step 1: 解析创作需求

从用户输入中提取：
- **topic**: 内容主题/选题
- **platform**: 目标平台（wechat-gzh, xiaohongshu, douyin, twitter）
- **style**: 风格（optional: 专业/轻松/故事/清单）
- **length**: 长度（optional: 短/中/长）

### Step 2: 选题研究（可选）

如果用户只提供了模糊主题，调用 `researchTopic` 进行：
- 热点分析
- 竞品内容调研
- 关键词提取

### Step 3: 内容生成

调用 `generateContent` 生成：
- 标题（3 个备选）
- 正文内容
- 摘要/导语
- 标签/关键词

### Step 4: 媒体生成（可选）

根据平台需求调用：
- `generateImage` - 生成封面图/配图
- `generateVideo` - 生成短视频

### Step 5: 保存母版（库拾 · 固化流水线）

权威文档：`skills/selfmedia-writing/references/content-pipeline.md`

**深度（`oss-pick-standard`）：**

1. `content/sources/{vertical}/{slug}/notes.md` — 选题
2. `MASTER.md` — 按 `oss-picks-depth.tpl.md`（含 MVP + 由简入深提纲）
3. `oss-repo-read` → `repo-digest.md`
4. `selfmedia-writing` → `humanized.md`（🚀📖🎯🗺️💎⚠️）
5. `kushi-visual-enrich` → `assets/`
6. `humanizer-zh` → 终检
7. `readability-lint.py --depth` + `record-humanize-evidence.py --pipeline oss-pick-standard`
8. `render-channel.sh` → `renders/`

**日榜（`oss-pick-daily`）：** 无 read-repo；`selfmedia-writing` 日榜体裁；evidence 三步。

注册表：`content/registry.yaml` · `content/pipelines/*.yaml`

### Step 6: 保存草稿（legacy）

调用 `createDraft` 保存到草稿箱，返回草稿 ID。

## Examples

### Example 1: 微信公众号文章

**User**: "创作一篇关于 AI 编程助手的微信公众号文章"

```
1. parseRequest:
   topic: "AI 编程助手"
   platform: "wechat-gzh"
   style: "专业"

2. generateContent:
   platform: "wechat-gzh"
   topic: "AI 编程助手"
   style: "professional"
   length: "medium"

3. generateImage:
   prompt: "AI programming assistant, futuristic, clean design, code background"
   size: "900x383"  # 公众号封面尺寸

4. createDraft:
   title: "AI 编程助手：开发效率的 10 倍提升"
   content: "..."
   coverImage: "..."
   platform: "wechat-gzh"

5. Return draft ID and preview link
```

### Example 2: 小红书笔记

**User**: "帮我写一篇关于上海咖啡探店的小红书笔记"

```
1. parseRequest:
   topic: "上海咖啡探店"
   platform: "xiaohongshu"
   style: "轻松"

2. generateContent:
   platform: "xiaohongshu"
   topic: "上海咖啡探店"
   style: "casual"
   length: "short"

3. generateImage:
   prompt: "Shanghai coffee shop, aesthetic, warm lighting, latte art"
   size: "1080x1440"  # 小红书图片尺寸

4. createDraft:
   title: "上海探店｜这 5 家咖啡馆值得打卡"
   content: "..."
   images: [...]
   platform: "xiaohongshu"
   tags: ["上海探店", "咖啡", "周末去哪儿"]
```

## Platform Specifications

| 平台 | 内容类型 | 标题长度 | 正文长度 | 图片尺寸 | 特殊要求 |
|------|----------|----------|----------|----------|----------|
| wechat-gzh | 图文 | ≤64 字 | 无限制 | 900×383 封面 | 需要摘要 |
| xiaohongshu | 笔记 | ≤20 字 | ≤1000 字 | 1080×1440 | 需要标签 |
| douyin | 短视频 | ≤55 字 | ≤500 字 | 1080×1920 | 竖版视频 |
| twitter | 推文 | ≤280 字 | - | 1200×675 | 支持线程 |

## Important Notes

- 生成内容需符合平台规范，避免敏感词
- 图片生成需考虑版权，优先使用 AI 生成
- 视频生成时间较长（约 10 分钟/分钟视频），需异步处理
- 草稿生成后需用户确认方可发布
