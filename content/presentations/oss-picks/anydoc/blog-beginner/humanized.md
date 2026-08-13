# 把 Word/PDF/PPT 一键变成干净 Markdown：anydoc 三分钟上手

> 库拾一句话：一个 3 周涨到约 1.5 万星的 Rust 小工具，把办公文档变成 AI 和编辑器都能读懂的 Markdown。

信息更新于 2026-08-12（star 数为检索时刻快照）。项目地址：github.com/firecrawl/anydoc · 协议 MIT · 核心 Rust。

## 先说你可能遇到过的事

你可能经历过：同事发来一个 Word 文档，你把内容复制进笔记或编辑器，标题变乱码、表格散架、图片失踪，排版像被洗衣机搅过。更难受的是，你想把文档喂给 AI 让它总结，AI 也读不懂一堆碎片格式。

大部分人的解法是手动整理，一份文档花二十分钟。GitHub 上一个叫 **anydoc** 的新项目想把这件破事变成一条命令。说白了，它就是个“文档翻译器”：办公格式进，干净 Markdown 出。问题是，光靠复制粘贴，格式永远救不回来。

## 🚀 小白 MVP：先跑通再说

环境前提：有 Node.js 就行（npx 自带），不用先装 anydoc。

直接在你的终端执行：

```bash
npx @firecrawl/anydoc 你的文档.docx
```

想存成文件：

```bash
npx @firecrawl/anydoc slides.pptx -o slides.md
```

跑通检查清单：

- 终端输出了 Markdown 文本（不再是乱格式）
- 用 `-o` 生成了 `.md` 文件
- 表格、标题结构还在

三句口诀：

1. 文档进，Markdown 出。
2. 先 npx 试，常用再全局装。
3. 装不上就换 Node 或 Python。

说真的，第一次看到一行命令就能出干净 Markdown，是有点惊喜的。

## 📖 这篇怎么读（由简入深）

先跑 MVP，再回来看 🗺️。想快点，看 3 分钟行；想接进自己的脚本，看 10 分钟行。

| 时间 | 读哪几节 | 得到什么 |
|------|----------|----------|
| 3 分钟 | 🚀 MVP + 接下来你可以 | 能跑通一条命令 |
| 10 分钟 | Node / Python 示例 | 能写脚本批量转文档 |
| 进阶 | 🗺️ 模块表 + WASM + Agent Skill | 知道三种接法怎么选 |

## 先带你看一眼

【截图占位 1：README 顶部 —— 支持格式列表与 badges（来源：firecrawl/anydoc README）】

【截图占位 2：浏览器 demo 页 —— WebAssembly 本地转换（来源：firecrawl.github.io/anydoc）】

图说：上面是仓库门面，下面是浏览器本地 demo；两张图都指向“文档进、Markdown 出”这条主线。（真实截图待 enrich 步骤补齐，当前为显式占位。）

## 🎯 一句话看透本质

anydoc 是一个格式无关的“文档 → Markdown”转换层：无论进来的是 Word、PPT、Excel 还是 PDF、EPUB、CSV，出去的都是同一种干净、统一的 Markdown。

这也是它对 AI 有用的原因：大模型不擅长读二进制办公格式，但非常擅长读 Markdown。其实它背后就三步：读文件、转格式、输出文本。

## 🗺️ 核心架构与主流程

先懂白话版：

1. 你丢给它一个文件路径或文件内容。
2. Rust 写成的核心负责解析并转换成 Markdown。
3. 你拿到统一格式的输出（Node、Python、浏览器三种入口任选）。

进阶：同一内核有三条绑定（bindings，就是让其他语言或环境能调用 Rust 核心的接口）：

| 模块 | 入口 | 适合谁 |
|------|------|--------|
| CLI | `npx @firecrawl/anydoc` | 只想手动转文件 |
| Node.js | `toMarkdown / toMarkdownBytes / toDocument` | 写脚本或服务 |
| Python | `anydoc.to_markdown / to_markdown_bytes / to_document` | 数据与自动化 |
| WASM | `@firecrawl/anydoc-wasm` | 浏览器本地转换 |
| Agent Skill | `npx skills add firecrawl/anydoc` | 让 AI 助手直接读文档 |

另外官方把它用在了自家的 Firecrawl Parse 托管 API 上；anydoc 本体不读扫描版 PDF，OCR 由托管 API 负责。

## 💎 绝妙的设计亮点

1. 输出稳定：不同格式进、同一种 Markdown 出，下游不用为每种格式写适配。
2. 浏览器本地转换：WASM 版在本地跑，敏感文件不用上传。
3. Agent Skill 一条命令装好：`npx skills add firecrawl/anydoc`，AI 助手立刻会读文档。

Agent Skill 说白了就是一个“教 AI 助手用工具的安装包”；装上之后，你让它总结一份 PDF，它知道先转成 Markdown 再读。

## ⚠️ 潜在坑点与局限性

- 扫描版 PDF 转不了：anydoc 本体不做 OCR，扫描页要走官方托管 API（要钱或额度）。
- “单数字毫秒”是官方声明：README 宣称的速度我没有独立测过，超大文件请以实测为准。
- npx 首次会下载二进制，第一次执行稍慢。
- 数据会变：截至 2026-08-12 约 14,888 stars / 792 forks，数字会随时间变化。

话说回来，这些坑大多能绕开。真正不适合它的场景：

- 手写稿、拍照页：需要 OCR，那不是 anydoc 的活。
- 要保真版式还原（比如打印稿）：它输出 Markdown，不是 PDF 编辑器。
- 敏感文件又想完全离线：WASM demo 本地跑，但 CLI 首次 npx 会联网拉二进制。

## 接下来你可以

1. 拿一份手边的 `.docx` 或 `.pdf` 跑一次 `npx @firecrawl/anydoc 文件`。
2. 想给 AI 助手加能力：`npx skills add firecrawl/anydoc`。
3. 要批量处理再看 Node / Python 绑定；敏感文件优先用浏览器 WASM demo。

---

*本文基于 anydoc 官方仓库 README 与 GitHub 公开元数据（检索时刻 2026-08-12）整理；未经独立性能测试。*
