---
name: selfmedia-agent-reach
description: |
  封装已安装的 Agent-Reach：全网平台搜索、热评与讨论汇聚，服务自媒体调研与成稿。
  上游 https://github.com/Panniantong/Agent-Reach ；本机 CLI `agent-reach`，skill 见 ~/.agents/skills/agent-reach。
  触发：Agent-Reach、全网调研、热评、多平台搜索、小红书/B站/X 讨论。
metadata:
  project: selfmedia-creator
  upstream: https://github.com/Panniantong/Agent-Reach
  local_skill: /Users/apple/.agents/skills/agent-reach/SKILL.md
  cli: agent-reach
  pairs_with: [selfmedia-topic-radar, selfmedia-last30days, selfmedia-humanize]
---

# selfmedia-agent-reach

## 做什么

对**已确定的话题**做多平台证据与热评收集，供成稿引用与对立观点。

## 怎么跑

1. **先读并遵循：** `/Users/apple/.agents/skills/agent-reach/SKILL.md`  
2. 开工前：`agent-reach doctor --json`（或 skill 要求的体检），声明使用的平台/后端。  
3. 自媒体默认组合：  
   - 网页/综搜（Exa 等 skill 内路由）  
   - 中文：小红书 + B站（doctor 显示可用时）  
   - 讨论：X/Twitter 或 Reddit（可用时）  
4. 输出：**事实要点 + 热评摘录 + 链接**；再交给 topic-radar / 成稿。

## 回传格式

```markdown
### [Agent-Reach] 平台 - 标题/账号
- 互动：
- 链接：
- 热评/观点：（各 1 句，注明情绪：赞同/反对/嘲讽）
- 可引用？（是/否，是否需改写）
```

落盘：`content/sources/radar/agent-reach-{topic-slug}-{YYYYMMDD}.md`

## 与 last30days 分工

| | last30days | Agent-Reach |
|---|---|---|
| 强项 | 近 30 天多源研究简报 | 实时多平台 + 中文社区 |
| 用法 | 广撒网定主题 | 定题后深挖评论与证据 |

## 边界

- 只读调研，不发帖不点赞  
- 按 doctor 路由，不发明命令  
- 热评要标注来源，禁止假造评论  
