---
name: publish-content
description: |
  多平台内容发布 Skill（v0.0.1 copy-first）。路由到 crews/selfmedia-operator 下各 platform skill 或 publish-api。
triggers:
  - pattern: "发布.*到(.+)"
    args: [draftId, platform]
  - pattern: "/publish"
    args: [draftId, platform, scheduleTime]
  - pattern: "帮我发布.*"
    args: [draftId, platform]
---

# Publish Content Skill

## Platform 路由表（v0.0.1）

| 平台 | 轨 | 入口 |
|------|-----|------|
| 微信公众号 wechat-gzh | A | `scripts/publish-wechat.sh`（R12 compose：wenyan render html → Wechatsync weixin） |
| 掘金 juejin | A | `crews/selfmedia-operator/skills/juejin-publish/` SKILL |
| 知乎 zhihu | A | `crews/selfmedia-operator/skills/zhihu-publish/` SKILL |
| 今日头条 toutiao | A | `crews/selfmedia-operator/skills/toutiao-publish/` SKILL |
| 抖音 douyin | A | `crews/selfmedia-operator/skills/douyin-publish/` |
| Twitter/X | A/B | skill 或 `vendor/aitoearn/channel/publishing/providers/twitter.service.ts` |
| B站 bilibili | B | `vendor/aitoearn/.../bilibili.service.ts` + `POST /publish` |
| 微信（HTTP） | B | `POST http://127.0.0.1:3000/publish` body: `{"platform":"wxGzh","markdownPath":"..."}` |

## Workflow

1. 读取 `content/masters/{vertical}/{slug}/humanized.md`（或先 render）
2. 按上表选择 A 轨 shell/skill 或 B 轨 publish-api
3. 微信：文颜排版 → 草稿箱 → `published-track/scripts/record.sh`
4. 返回 media_id / URL / platformPostId

## 发布记录（微信强制）

```bash
bash crews/selfmedia-operator/skills/published-track/scripts/record.sh \
  --platform wx_mp \
  --title "<标题>" \
  --content-type article \
  --source-folder "<markdown目录>" \
  --publish-date "$(date +%Y-%m-%d)"
```

## Examples

**User**: 微信单端双线闭环（日榜 + 深度稿）

```bash
pnpm run publish:wechat:dual
# 或指定 slug：
bash scripts/with-env.sh bash scripts/publish-wechat.sh daily-2026-06-17 superpowers
```

**User**: 发布单篇到微信公众号

```bash
bash scripts/with-env.sh bash scripts/publish-wechat.sh --slug wenyan
```

**User**: 用 API 发布同一篇

```bash
curl -X POST http://127.0.0.1:3000/publish \
  -H 'Content-Type: application/json' \
  -d '{"platform":"wxGzh","markdownPath":"content/renders/kushi-gzh/wechat-gzh/wenyan.md"}'
```
