# 把 Word/PDF/PPT 一键变成干净 Markdown：anydoc 三分钟上手

> 库拾一句话：一个 3 周涨到约 1.5 万星的 Rust 小工具，把办公文档变成 AI 和编辑器都能读懂的 Markdown。

信息更新于 2026-08-12（star 数为检索时刻快照）。项目地址：github.com/firecrawl/anydoc。

## 先讲个真实痛点

你可能经历过：客户或同事发来一个 Word 文档，你把内容复制进笔记/编辑器，标题变乱码、表格散架、
图片失踪，排版像被洗衣机搅过。更烦的是，想把文档喂给 AI 让它总结，AI 也读不懂一堆碎片格式。

大部分人的解法是手动整理，一份文档花二十分钟。GitHub 上一个叫 **anydoc** 的新项目，想把这件
事变成一条命令。

## 🚀 小白 MVP：先跑通再说

不需要安装任何东西，直接在你的终端里执行：

```bash
npx @firecrawl/anydoc 你的文档.docx
```

它会输出一份干净 Markdown。想存成文件：

```bash
npx @firecrawl/anydoc slides.pptx -o slides.md
```

跑通检查清单：

- 终端输出了 Markdown 文本（不再是乱格式）
- `-o` 生成了文件
- 表格和标题结构还在

三句口诀：

1. 文档进、Markdown 出。
2. 先 npx 试，常用再全局装。
3. 装不上就换 Node 或 Python 的方式。

## 📖 由简入深：三种打开方式

**3 分钟：命令行**（上面已经跑通）

想随时用，装全局命令：

```bash
npm install -g @firecrawl/anydoc
```

**10 分钟：Node.js 或 Python 接进自己的脚本**

Node：

```bash
npm install @firecrawl/anydoc
```

```js
import { toMarkdown } from '@firecrawl/anydoc';
const markdown = await toMarkdown('report.docx');
```

Python：

```bash
pip install firecrawl-anydoc
```

```python
import anydoc
markdown = anydoc.to_markdown("report.docx")
```

**进阶：让 AI 助手直接读文档**

anydoc 以 Agent Skill 的形式分发：

```bash
npx skills add firecrawl/anydoc
```

装完后，你的 AI 助手可以直接把一份 Word/PDF 转成 Markdown 再处理。另外它提供浏览器（WebAssembly）
版本，官方 demo 页在浏览器里本地转换文件，文件不会离开你的电脑。

## 🎯 一句话看透本质

anydoc 是一个**格式无关的“文档 → Markdown”转换层**：无论进来的是 Word、PPT、Excel 还是
PDF/EPUB/CSV，出去的都是同一种干净、统一的 Markdown。

这也是它对 AI 有用的原因：大模型不擅长读二进制办公格式，但非常擅长读 Markdown。

## 🗺️ 核心架构与主流程

先懂白话版：

1. 你丢给它一个文件路径或文件内容。
2. Rust 写成的核心负责解析并转换成 Markdown。
3. 你拿到统一格式的输出（Node、Python、浏览器三种入口任选）。

再进一档：同一内核有 Node.js、Python、WASM 三套绑定；官方还把它用在了自家的 Firecrawl Parse
托管 API 上（anydoc 本体不读扫描版 PDF，OCR 由托管 API 负责）。

## 💎 绝妙的设计亮点

1. **输出稳定**：不同格式进、同一种 Markdown 出，下游不用为每种格式写适配。
2. **浏览器本地转换**：WASM 版在本地跑，适合处理敏感文件。
3. **Agent Skill 一条命令**：`npx skills add firecrawl/anydoc`，AI 助手立刻会读文档。

## ⚠️ 潜在坑点与局限性

- **扫描版 PDF 转不了**：anydoc 本体不做 OCR，扫描页需要官方托管 API（要钱或额度）。
- **“单数字毫秒”是官方声明**：README 宣称的速度我没有独立测过，超大文件请以实测为准。
- **npx 首次会下载二进制**：第一次执行稍慢是正常的。
- **数据会变**：截至 2026-08-12 约 14,888 stars / 792 forks，数字会随时间变化。

## 接下来你可以

1. 拿一份手边的 `.docx` 或 `.pdf` 跑一次 `npx @firecrawl/anydoc 文件`。
2. 想给 AI 助手加能力：`npx skills add firecrawl/anydoc`。
3. 需要批量处理再研究 Node/Python 绑定；敏感文件优先用浏览器 WASM demo。

---

*本文基于 anydoc 官方仓库 README 与 GitHub 公开元数据（检索时刻 2026-08-12）整理；未经独立性能测试。*
