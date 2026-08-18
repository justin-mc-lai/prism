# anydoc 线程稿（X 短链 · 倒金字塔）

> form_id: thread · lane: standard · master_ref: content/masters/oss-picks/anydoc/MASTER.md
> 检索时刻 2026-08-12 · star/forks 为快照

1/ 处理文档最烦的是格式。Word 复制进编辑器，标题乱码、表格散架、图片失踪。把文档喂给 AI 总结，AI 也读不懂一堆碎片。这个月 GitHub 出现一个 Rust 小工具，九天涨到约 1.5 万星，专治这种破事，把办公格式变成干净 Markdown。

2/ 它叫 anydoc（github.com/firecrawl/anydoc，MIT）。支持 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF 八种格式，输出统一的 GitHub 风格 Markdown。官方宣称速度是单数字毫秒级。这是官方声明，我没独立测过。

3/ 最实用的是三条入口。CLI 一条命令 `npx @firecrawl/anydoc 你的文档.docx`；Node 和 Python 各有 `toMarkdown` 系列 API，适合写脚本批量转；浏览器 WASM 版在本地转，敏感文件不用上传。

4/ 如果你在乎隐私，重点看浏览器版。它用 WebAssembly 在本地转换，文件不上传。CLI 首次 npx 会联网拉二进制，但转换本身在本地跑。

5/ 说个诚实边界。扫描版 PDF 它转不了，anydoc 本体不做 OCR，扫描页要走官方托管 API（Firecrawl Parse）。手写稿、拍照页不归它管。

6/ 我的判断很简单。如果你的场景是“把文档变成 AI 能读的 Markdown”，现在不用等，直接 `npx @firecrawl/anydoc 文件.docx` 试一次。想批量处理再看 Node/Python 绑定，敏感文件优先 WASM。

7/ 数据会变。截至检索时刻约 14,888 stars / 792 forks。工具 08-03 创建，08-12 检索时就是这个数，九天长了这么多星，说明踩过同一坑的人不少。

8/ 想试的话，拿一份手边的 `.docx` 或 `.pdf` 跑一次，三分钟就知道值不值。
