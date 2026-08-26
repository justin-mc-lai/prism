---
name: selfmedia-topic-radar
description: |
  自媒体选题雷达：最近不知道写什么时，从多源素材聚合器拉热点，再收敛选题并成稿。
  聚合源：last30days、TL1 中文热帖、知乎今日热榜(TopHub)、NewsNow 热门新闻、Agent-Reach 全网热评。
  触发：不知道写什么、选题枯竭、热点选题、素材聚合、topic radar、中文区爆款对标。
  Use when the user lacks topic ideas and needs multi-source trend aggregation then self-media drafts.
metadata:
  project: selfmedia-creator
  pairs_with:
    - selfmedia-last30days
    - selfmedia-tl1
    - selfmedia-zhihu-hot
    - selfmedia-newsnow
    - selfmedia-agent-reach
    - selfmedia-humanize
    - humanizer-zh
    - selfmedia-writing
    - create-content
---

# selfmedia-topic-radar（选题雷达）

## 定位

「不知道写什么」时的**产品侧入口 skill**。

跨项目稳定入口优先：`qi_dev.sh intel-radar`（`qi-dev-intel-radar`）做 doctor / deep-plan / 第一性原理 briefing；本 skill 负责自媒体选题收敛与大道无形成稿。  
先多源捞料 → 选题收敛 → 按 **大道无形** 文风出提纲/成稿 → 可选 `selfmedia-humanize` / `humanizer-zh`。

## 素材源（项目内子 skill）

| 源 | Skill | 用途 |
|---|---|---|
| last30days | `selfmedia-last30days` | 近 30 天 X/油管等热议 |
| TL1 | `selfmedia-tl1` | 中文圈高粉热帖 |
| 知乎热榜 | `selfmedia-zhihu-hot` | 知乎当日最火讨论 |
| NewsNow | `selfmedia-newsnow` | 实时热门新闻 |
| Agent-Reach | `selfmedia-agent-reach` | 全网搜索 + 热评汇聚 |

文风：`references/voice-dadao.md`（大道无形 · 浅白 · 偶有锋利）。

## 工作流

### Phase 0 — 澄清（最多 2 问）

- 平台：小红书 / 公号 / 口播 / 库拾 OSS  
- 方向：科技 / 职场 / 认知 / 不限  

无回答则默认：**中文区、可评论、近 7 日热、不限垂类**。

### Phase 1 — 并行捞料（按需加载子 skill）

默认组合（不知写什么）：

1. `selfmedia-zhihu-hot` — 中文讨论热度  
2. `selfmedia-tl1` — 推特中文圈传播  
3. `selfmedia-newsnow` — 新闻由头  
4. 若有明确话题 → 再开 `selfmedia-last30days` + `selfmedia-agent-reach` 深挖  

每个源输出压缩为统一卡片（见下），**不要**把整页 HTML 贴给用户。

### Phase 2 — 选题收敛

输出 **5 个可写选题**，每条：

| 字段 | 说明 |
|---|---|
| 标题草案 | 1 句 |
| 由头 | 来自哪 1～2 个源 |
| 角度 | 你的独特切口（非复述热榜） |
| 风险 | 时效/敏感/洗稿风险 |
| 推荐平台 | |

再标 **今日首选 1 条** 及理由（一句人话）。

### Phase 3 — 成稿（用户确认选题后，或用户说直接写）

1. 对首选选题跑 `selfmedia-agent-reach` 补热评/对立观点（若未跑）  
2. 按 `voice-dadao.md` 写正文  
3. 需要过朱雀/降 AI 味 → `selfmedia-humanize`  
4. 需要词表终检 → `humanizer-zh`  

### 统一素材卡片格式

```markdown
### [源名] 标题
- 热度/粉丝/互动：（有则写）
- 链接：
- 一句话：在吵什么
- 可写切口：
- 采集时间：
```

## 输出给用户的默认结构

```markdown
## 雷达扫描摘要
（各源各 3～5 条卡片压缩）

## 5 个可写选题
…

## 今日首选
…

## 若现在就写（可选成稿）
（用户要写才展开；文风=大道无形）
```

## 硬边界

- 热点只作**由头**，禁止通篇搬运热帖原文  
- 不编造数据与经历；引用注明来源链接  
- 不承诺流量；不碰违法敏感跟风  
- last30days / Agent-Reach 依赖本机已安装环境（见子 skill）  

## 参考

- `references/voice-dadao.md`  
- `references/source-matrix.md`  
