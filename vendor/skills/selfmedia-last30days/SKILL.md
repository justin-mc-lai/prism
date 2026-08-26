---
name: selfmedia-last30days
description: |
  封装 last30days：抓取近 30 天 X/油管/Reddit 等热门讨论，服务自媒体热点选题。
  上游 https://github.com/mvanhorn/last30days-skill ；本机通常已装在 ~/.codex/skills/last30days。
  触发：last30days、近30天热点、油管热议、X 热帖研究。
metadata:
  project: selfmedia-creator
  upstream: https://github.com/mvanhorn/last30days-skill
  local_skill: /Users/apple/.codex/skills/last30days/SKILL.md
  pairs_with: [selfmedia-topic-radar, selfmedia-agent-reach]
---

# selfmedia-last30days

## 做什么

按主题检索**近约 30 天**多平台讨论，输出带引用的研究简报，供选题与成稿。

## 怎么跑

1. **优先加载上游 skill 全文并严格按其流程执行：**  
   `/Users/apple/.codex/skills/last30days/SKILL.md`  
   （若存在 `~/.codex/skills/last30days/skills/last30days/SKILL.md` 符号链接，同内容。）
2. 上游要求的 first-run / API key（如 `SCRAPECREATORS_API_KEY`、可选 X 的 AUTH_TOKEN/CT0）按其文档处理。  
3. 自媒体场景默认参数建议：  
   - 主题：用户给出的方向；没有则用中文区近期科技/AI/效率工具  
   - 输出：中文摘要 + 英文源保留链接  

## 回传给 topic-radar 的格式

每条热点压缩为：

```markdown
### [last30days] 话题名
- 平台：X / YouTube / Reddit / …
- 热度信号：赞/评/播放（有则写）
- 链接：
- 一句话：
- 可写切口：
```

完整 briefing 可落盘到项目：

`content/sources/radar/last30days-{topic-slug}-{YYYYMMDD}.md`

## 边界

- 需要 Node/Python 与上游配置；未配置时明确告知缺什么，不要假装搜过  
- 引用必须可点开；禁止编造帖文  
