---
name: selfmedia-writing
description: |
  库拾自媒体成稿：面向新手小白的 GitHub 开源库科普解读。深度稿四段式（🎯🗺️💎⚠️）+ 日榜倒金字塔。
  另含情绪观点长文体裁（emotional-essay，X 长文/公众号贴图深度稿）。
  文笔层 = prose-core + 说人话层（ra-人话 / 活人感写作完整蒸馏）。
  整合 oss-repo-read 依据、自媒体文笔、humanizer-zh 终检。触发：selfmedia-writing、自媒体成稿、humanized 润色。
allowed-tools:
  - Read
  - Write
  - Edit
metadata:
  pipeline_step: narrate
  pipeline_order: after oss-repo-read → before kushi-visual-enrich → humanizer-zh
  pairs_with: [oss-repo-read, kushi-narrative-zh, kushi-visual-enrich, humanizer-zh]
  authority: content/masters/_template/MASTER-SPEC.md
  content_pipeline: skills/selfmedia-writing/references/content-pipeline.md
  reader_tier: beginner
  gold_samples:
    - content/masters/oss-picks/openspec/humanized.md
    - content/masters/oss-picks/daily-2026-06-22/humanized.md
---

# 自媒体成稿（selfmedia-writing）

你是一位**精通底层架构的资深软件架构师**，但写出来的话要让**新手小白**能跟住——像带徒弟，自信、笃定、接地气。

目标：把 GitHub 开源库讲清楚，让人**愿意读完**，而不是看完标题就关。

## 何时使用

- `MASTER.md` +（深度）`repo-digest.md` → `humanized.md`
- 读者层级：**新手小白**（假设会点鼠标、能跟命令，不假设读过源码）
- 日榜 `daily-YYYY-MM-DD` 或深度 `oss-pick-standard`

## 深度管线（固定顺序）

```text
MASTER.md + repo-digest.md
  → ① 叙事与四段结构（本 skill）
  → ② 自媒体文笔（references/prose-core.md）
  → ③ kushi-visual-enrich
  → ④ humanizer-zh
  → humanized.md
```

日榜无 `read-repo`；见 `references/oss-daily-archetype.md`。

R10 门禁：`readability-lint.py --depth`；`record-humanize-evidence.py --pipeline oss-pick-standard`。

---

## ① 深度稿结构（oss-pick-standard）

读：`MASTER.md`、`meta.yaml`、`repo-digest.md`（**必读**）、`notes.md`。  
权威顺序见 `references/content-pipeline.md`。

**开篇：**

1. H1 + `> 库拾一句话` + 元信息
2. **场景开场**（痛点，≥80 字）

**小白层（四段之前，必填）：**

3. **🚀 小白 MVP** — 环境前提、可复制命令、跑通检查清单、三句口诀
4. **📖 由简入深怎么读** — 时间表（3 分钟 / 10 分钟 / 全文）

**配图：** 先带你看一眼（≥2 图，enrich 插入）

**四段核心（H2 固定 emoji）：**

| H2 | 内容 |
|----|------|
| **🎯 一句话看透本质** | 痛点 + 底层逻辑；不罗列功能 |
| **🗺️ 核心架构与主流程** | **先**白话闭环（H3「先懂…」）→ **再**进阶模块表（依据 repo-digest） |
| **💎 绝妙的设计亮点** | ≥2 点；可写「看不懂可先跳过」 |
| **⚠️ 潜在坑点与局限性** | 不适合场景 |

**收尾：** 对比表（可选）+ 接下来你可以

细则：`references/oss-depth-beginner-archetype.md` · 样稿：`openspec/humanized.md`

## 体裁选型

| 体裁 | 何时用 | 权威参考 |
|------|--------|----------|
| oss-pick-standard（深度四段式） | 开源库科普，读者新手小白 | `references/oss-depth-beginner-archetype.md` |
| oss-pick-daily（日榜倒金字塔） | 每日 GitHub 涨星榜 | `references/oss-daily-archetype.md` |
| emotional-essay（情绪观点长文） | 亲密关系/情绪/欲望等「无名体验」长文；X 长文、公众号贴图深度稿、小红书图文 | `references/emotional-essay-archetype.md` |

**emotional-essay 的 humanizer 覆盖：** 终检按 archetype「覆盖表」执行——否定定义壳、短节拍段、收尾金句是本体裁的合法引擎，禁止按通用 AI 痕迹清单抹平；真伪分界用 archetype 的「判别开关」（否定是否带新区分、短段是否具体、金句是否被机制铺垫）。

---

## ② 自媒体文笔（必做）

朗读一遍；拗口就改。见 `references/prose-core.md`。

| # | 原则 |
|---|------|
| 1 | 像说话一样写 |
| 2 | 一句一意 |
| 3 | 倒金字塔 |
| 4 | **主动语态**（禁「被发布」「被调用」） |
| 5 | 正面表述 |

**输出风格（硬规则）：**

- 禁翻译腔：「正如我们所见」「被广泛使用」「基于…的原因」
- 术语首次出现用白话括号解释
- 短句为主；专业词 **加粗** 一次即可

**说人话层（必做，所有公开成稿）：** 见 `references/human-voice-prose.md`（ra-人话 + 活人感写作 1.1 完整蒸馏；活人感写作钉死副本在 `vendor/writing-skills/human-writing/`，交付环合同见 `DELIVERY-RING-CONTRACT.md`）。

- 现实稿先过材料门（≥5 件具体材料，不足则研究/追问/缩短，禁止注水）
- 找说话位置再动笔；翻案腔按「动作」查，不按字面查
- 成稿跑 `python3 scripts/check-human-voice.py <稿>`：失败项清零，提醒项人工裁决
- emotional-essay 体裁按该参考「体裁裁决表」执行（否定壳走「新区分」检验，检查脚本命中作提醒）

---

## ③ 视觉充实

深度稿：`kushi-visual-enrich`。日榜：Trending 截图。

---

## ④ humanizer-zh 终检

humanizer **不负责降维**；小白层须在 ①② 完成。

---

## 自检

见 `references/checklist.md`。深度稿额外：

- [ ] 四段 H2 齐全（🎯🗺️💎⚠️）
- [ ] 🚀 MVP + 📖 由简入深 节齐全
- [ ] 🗺️💎 有 repo-digest 依据
- [ ] `readability-lint.py --depth` 通过

---

## 与子 skill 关系

| Skill | 角色 |
|-------|------|
| **oss-repo-read** | 深度稿读 repo → `repo-digest.md` |
| **selfmedia-writing**（本 skill） | 成稿主入口 |
| kushi-narrative-zh | 体裁参考库 |
| kushi-visual-enrich | 配图 |
| humanizer-zh | 终检 |

## 示例

```text
/selfmedia-writing openspec 深度成稿，读者新手小白，四段式
```

```text
/selfmedia-writing daily-2026-06-22 日榜，倒金字塔
```

## 禁止

- 深度稿无 repo-digest 写 🗺️💎
- dev 脚本直写生产 humanized
- 跳过 humanizer-zh
