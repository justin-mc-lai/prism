---
name: selfmedia-zhihu-hot
description: |
  知乎今日热榜（经 TopHub 聚合页），看知乎当天在吵什么；服务自媒体选题与「知乎向」二创角度。
  入口 https://tophub.today/n/mproPpoq6O
  触发：知乎热榜、知乎今日热点、tophub 知乎。
metadata:
  project: selfmedia-creator
  urls:
    - https://tophub.today/n/mproPpoq6O
  pairs_with: [selfmedia-topic-radar, selfmedia-agent-reach]
---

# selfmedia-zhihu-hot

## 入口

- 热榜页：https://tophub.today/n/mproPpoq6O  
- 需要单条详情时：打开热榜中的知乎原链，或用 `selfmedia-agent-reach` / `curl https://r.jina.ai/{知乎url}` 读正文摘要  

## 抓取步骤

1. 拉取 TopHub 知乎榜（jina 阅读器或浏览器）。  
2. 提取排名、标题、热度值、链接。  
3. 输出 **Top 10** 卡片；标出 3 个「适合自媒体二创」的（有争议/有场景/有反常识）。  
4. 用户选定后：再读 1～2 篇高赞回答摘要（勿全文洗稿）。

## 输出卡片

```markdown
### [知乎热榜] #{n} 标题
- 热度：
- 链接：
- 一句话：讨论焦点
- 可写切口：你的角度（反对/补充/落地方法）
- 洗稿风险：高/中/低
```

落盘可选：`content/sources/radar/zhihu-hot-{YYYYMMDD}.md`

## 边界

- **禁止**搬运知乎原文当原创长文  
- 二创必须换结构、加经历/边界、用大道无形语气  
- 医疗情感等敏感热榜谨慎跟  
