# repo-digest: firecrawl/anydoc

> 检索时刻: 2026-08-12 · 来源: GitHub API + README.md（268 行）

## 仓库速览

- 仓库: https://github.com/firecrawl/anydoc（default branch: main）
- 创建: 2026-08-03 · 检索时刻: 14,888 stars / 792 forks / 53 open issues
- 语言: Rust · 协议: MIT · 文档站: https://firecrawl.github.io/anydoc/
- 定位: 把 Word/PowerPoint/Excel/OpenDocument/RTF/EPUB/CSV/PDF 转成干净 GitHub-Flavored Markdown

## 主流程

1. 输入文件路径或内容（CLI / Node / Python / WASM）
2. Rust 核心解析并转换（官方宣称单数字毫秒级）
3. 输出统一 GitHub-Flavored Markdown（或 Document 中间模型）

## 核心模块

| 模块 | 入口 | 说明 |
|------|------|------|
| CLI | `npx @firecrawl/anydoc` | 手动转文件；`-o` 输出文件；stdin 支持 `--format csv` |
| Node.js | `@firecrawl/anydoc` | `toMarkdown / toMarkdownBytes / toDocument` |
| Python | `firecrawl-anydoc` | `anydoc.to_markdown / to_markdown_bytes / to_document` |
| WASM | `@firecrawl/anydoc-wasm` | 浏览器本地转换 demo |
| Agent Skill | `npx skills add firecrawl/anydoc` | 让 AI 助手直接读文档 |
| 托管 API | Firecrawl Parse | anydoc 转换 + OCR（扫描页） |

## 坑/局限线索

- 扫描版 PDF 需要 OCR（托管 API），anydoc 本体不处理
- “single-digit milliseconds”为官方声明，无独立基准
- npx 首次使用需下载预编译二进制

## 可写进 💎 的点

- 格式无关、输出统一
- WASM 浏览器本地转换（文件不上传）
- Agent Skill 分发（一条命令让 agent 会读文档）
