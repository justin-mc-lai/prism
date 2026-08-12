# FactMaster: anydoc

> kind: fact · pipeline: oss-pick-standard · 检索时刻: 2026-08-12

## 一句话

anydoc 是一个把 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV 和 PDF 转换成干净
GitHub 风格 Markdown 的快速 Rust 库，带 Node.js、Python 与浏览器（WebAssembly）绑定。

## 来源（source_refs）

- 仓库: `https://github.com/firecrawl/anydoc`（default branch: main）
- 元数据: GitHub API `repos/firecrawl/anydoc`（检索时刻 2026-08-12）
- README: 仓库 README.md（268 行，检索时刻 2026-08-12）
- 文档站: `https://firecrawl.github.io/anydoc/`

## Canonical claims（每条带来源）

| # | 事实 | 来源 |
|---|------|------|
| 1 | 支持输入格式：Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, PDF | README 首段 |
| 2 | 输出为干净 GitHub-Flavored Markdown | README 首段 |
| 3 | 核心实现语言 Rust；含 Node.js / Python / WASM（浏览器）绑定 | README 首段 |
| 4 | 仓库创建于 2026-08-03，检索时刻 14,888 stars / 792 forks / 53 open issues | GitHub API |
| 5 | 协议 MIT | GitHub API license.spdx_id |
| 6 | 官方宣称转换速度“single-digit milliseconds”（单数字毫秒级） | README 首段（官方声明，非独立测试） |
| 7 | 浏览器 demo 以 WebAssembly 运行，文件本地转换、不上传 | README “Try it in your browser” |
| 8 | 支撑 Firecrawl Parse 托管 API；扫描页 OCR 由托管 API 提供（anydoc 本体不读扫描页） | README 首段 |
| 9 | 以 Agent Skill 分发：`npx skills add firecrawl/anydoc` | README Quick start |
| 10 | CLI 安装：`npx @firecrawl/anydoc <file>`；全局 `npm install -g @firecrawl/anydoc` | README Quick start |
| 11 | Node：`npm install @firecrawl/anydoc`，API `toMarkdown/toMarkdownBytes/toDocument` | README Node.js |
| 12 | Python：`pip install firecrawl-anydoc`，API `anydoc.to_markdown / to_markdown_bytes / to_document` | README Python |
| 13 | WASM：`npm install @firecrawl/anydoc-wasm` | README Browser (WebAssembly) |

## 不确定性标注

- “单数字毫秒级”为项目官方声明；未做独立基准测试。
- star/forks 为检索时刻快照，会随时间变化。
- 扫描版 PDF 的 OCR 不在 anydoc 本体能力内（由 Firecrawl Parse 托管 API 覆盖）。

## 禁止改写

- 不得把官方声明写成独立测试结论。
- 不得声称支持 anydoc 未列出的格式。
