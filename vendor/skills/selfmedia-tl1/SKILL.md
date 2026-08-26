---
name: selfmedia-tl1
description: |
  抓取 TL1 中文圈高粉热帖（历史热帖/maxFans 等），一眼看什么火、什么传得快；可作选题由头。
  默认入口 https://tl1.com/history/maxFans/10000
  触发：TL1、中文推特热帖、X 中文圈热点。
metadata:
  project: selfmedia-creator
  urls:
    - https://tl1.com/history/maxFans/10000
  pairs_with: [selfmedia-topic-radar, selfmedia-agent-reach]
---

# selfmedia-tl1

## 入口

| 场景 | URL |
|---|---|
| 高粉历史热帖（默认） | https://tl1.com/history/maxFans/10000 |
| 其他板块 | 以用户指定的 tl1.com 路径为准；可在站内切换时间/粉丝阈值 |

## 抓取步骤

1. 用浏览器或 `curl` / `https://r.jina.ai/{url}` 拉取页面正文（优先可读提取）。  
2. 解析列表：作者、粉丝档、正文摘要、互动、链接（若有）。  
3. 取 **Top 8～15** 压缩为雷达卡片。  
4. 若页面 5xx/结构变化：说明失败，改用 `selfmedia-agent-reach` 搜 X 中文热议兜底。

## 输出卡片

```markdown
### [TL1] 摘要标题
- 作者/粉丝档：
- 互动：
- 链接：（推文或 TL1 页）
- 一句话：在传什么
- 可写切口：（换角度，禁止原文搬）
```

落盘可选：`content/sources/radar/tl1-{YYYYMMDD}.md`

## 边界

- 只作选题与评论由头；**禁止**大段复制推文当自己的正文  
- 注意时效与敏感；涉政涉敏默认跳过  
