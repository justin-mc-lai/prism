---
name: selfmedia-newsnow
description: |
  封装 NewsNow：优雅汇聚实时热门新闻，作自媒体由头与选题。
  上游 https://github.com/ourongxing/newsnow
  触发：NewsNow、实时热闻、今日新闻选题。
metadata:
  project: selfmedia-creator
  upstream: https://github.com/ourongxing/newsnow
  pairs_with: [selfmedia-topic-radar, selfmedia-agent-reach]
---

# selfmedia-newsnow

## 做什么

从 NewsNow 类「多源热门新闻」界面收集**实时**头条，压缩为选题卡片。

## 怎么用

1. 打开用户或默认的 NewsNow 实例（自托管 / 公开演示页；以仓库 README 当前推荐为准）：  
   https://github.com/ourongxing/newsnow  
2. 用浏览器或 `https://r.jina.ai/{实例URL}` 提取可读列表。  
3. 若本地已 docker/部署 NewsNow：优先读本地实例。  
4. 按频道（若有：科技/财经/综合）各取 Top 若干。  
5. 失败时：用 `selfmedia-agent-reach` 或 WebSearch「今日 科技 热点」兜底，并注明非 NewsNow 源。

## 输出卡片

```markdown
### [NewsNow] 标题
- 源站/频道：
- 链接：
- 一句话：
- 可写切口：解读 / 影响 / 普通人怎么办
- 时效：小时级 / 日级
```

落盘：`content/sources/radar/newsnow-{YYYYMMDD}.md`

## 边界

- 新闻事实以源站为准；不确定就链出去  
- 突发敏感新闻默认只做「发生了什么 + 信息来源」，不做阴谋推断  
