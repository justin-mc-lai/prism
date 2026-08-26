---
name: x-publish
description: >
  人类面一键 X（Twitter）发布：把给定文案直接发布到 qi-share/X 账号（白名单直接发布，
  用户 2026-08-11 已拍板）。触发词：发X、发推、发帖到X、x publish、发布推文、X发帖。
  发布后自动留证据并给出推文 URL。公众号/YouTube 不在本 skill 范围（仍走草稿+人工批准）。
---

# X 发布（x-publish）

## 边界（先读）

- 只发 `qi-share` / X 账号；发布即公开，文案即最终内容。
- 当前走本机已登录 Chrome（chrome-cdp 运行时）；BrowseForge 隔离档位 + 独立 IP 为 P1，未落地前不假装已隔离。
- 单条不超过 X 字数限制（约 280 字符，中文按字符计）。
- 测试贴提醒：如发测试内容，发布后提醒用户删除。

## 用法

```bash
# 一键发布
bash /Users/apple/Developer/Personal/products/selfmedia-sync-ai/scripts/x-publish.sh --text "推文内容"

# 预检不发帖
bash /Users/apple/Developer/Personal/products/selfmedia-sync-ai/scripts/x-publish.sh --text "推文内容" --dry-run
```

## 调用后必做

1. 检查输出：`state: done` + `publication_ref.url`。
2. 用浏览器打开 URL 核对标题/文案（X 风控会挡 curl，可能返回 000，不算失败）。
3. 写发布记录：`content/publications/x/qi-share/{job_id}.md`（account/platform/url/published_at/note）。
4. 把 URL 告诉用户。

## 失败处理

- `X_AUTH_REQUIRED`：本机 Chrome 未登录 x.com，让用户登录后重试。
- 其他失败：把 `failure.message` 原样展示，不假装成功；可重试（job 幂等，重跑同一 job_id 不会重复发）。
