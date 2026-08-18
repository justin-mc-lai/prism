# 深度稿：新手小白（MVP + 由简入深 + 四段式）

> **Gold：** `content/masters/oss-picks/openspec/humanized.md`  
> **流水线：** `content-pipeline.md`

## 与 repo-digest 的关系

| 段落 | digest 字段 |
|------|-------------|
| 🚀 MVP | MASTER「小白 MVP」+ README 安装/首个命令 |
| 🎯 | 综合 digest + MASTER 一句话 |
| 🗺️ 进阶层 | 「主流程」+「核心模块」 |
| 💎 | 「值得写进 💎 的代码点」 |
| ⚠️ | 「坑/局限线索」+ MASTER 边界 |

无 digest 或 scaffold only → **停止**，先跑 `oss-repo-read`。

## humanized.md 章节顺序（固定）

```markdown
# H1
> 库拾一句话
元信息行
## 先说你可能遇到过的事
## 🚀 小白 MVP：…（H2 须含「小白 MVP」）
## 📖 这篇怎么读（由简入深）（H2 须含「由简入深」）
## 先带你看一眼（可选，深度稿 ≥2 图）
## 🎯 一句话看透本质
## 🗺️ 核心架构与主流程
### 先懂…（小白层，白话）
### 进阶：…（模块表，可选 H3）
## 💎 绝妙的设计亮点
## ⚠️ 潜在坑点与局限性
## 接下来你可以（或对比表 + 收尾）
```

## 🚀 小白 MVP（必填）

- **位置：** 场景开场之后、四段式之前
- **内容：**
  - 环境前提（Node 版本等）一行
  - 可复制 `bash` 块（install + init）
  - 可复制 AI slash / 命令示例
  - **跑通检查清单**（3～5 条：目录/文件是否出现）
  - **口诀** 三句（如 propose → apply → archive）
- **原则：** 读者不读后文也能先动手试一次

## 📖 由简入深（必填）

- **位置：** MVP 之后
- **形式：** 表格 — 时间 | 读哪几节 | 得到什么
- 至少 3 行：3 分钟 / 10 分钟 / 全文或进阶
- 一句引导：「先跑 MVP，再回来看 🗺️」

## 四段 H2（emoji 固定）

```markdown
## 🎯 一句话看透本质
## 🗺️ 核心架构与主流程
## 💎 绝妙的设计亮点
## ⚠️ 潜在坑点与局限性
```

### 🎯

- 2～4 句；痛点 + 底层逻辑；不罗列功能

### 🗺️

- **两层：** 先白话闭环（无路径表），再「进阶」模块表（3～5 模块 + 路径）
- 调用关系主动语态一句

### 💎

- ≥2 点；段首可加「看不懂可先跳过」
- 路径 + 设计意图 + 好处

### ⚠️

- 工业短板 + **不适合** 列表

## 输出风格

见 `prose-core.md`：禁翻译腔、禁被动「被调用/被发布」。

长度：1500～2800 字（含表与代码块）。

## meta.yaml（R11 固化稿）

深度稿完成 humanize 后，在 `meta.yaml` 增加：

```yaml
content_spec: r11
humanize_gate: required
```

`render-channel.sh` 仅在 `content_spec: r11` 时对 `humanize_gate: required` 跑 `--depth` lint。存量旧稿未 backfill 前勿加 `content_spec: r11`。
