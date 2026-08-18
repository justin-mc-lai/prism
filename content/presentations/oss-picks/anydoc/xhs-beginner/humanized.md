# 把 Word/PDF 一键变干净 Markdown，这个工具 9 天涨了 1.5 万星

> form_id: xhs · lane: standard · master_ref: content/masters/oss-picks/anydoc/MASTER.md
> 检索时刻 2026-08-12 · 图片为显式占位，enrich 待补

同事发来 Word，你把它复制进笔记或编辑器，标题变乱码、表格散架、图片失踪，排版像被洗衣机搅过。想喂给 AI 总结，AI 也读不懂一堆碎片。手动整理一份，二十分钟没了。

GitHub 上有个叫 anydoc 的开源小工具，专治这事。它 8 月 3 号创建，12 号检索时已经约 1.5 万星，MIT 协议。

它做的事一句话能说清。把 Word、PPT、Excel、PDF 这些办公格式，变成统一的干净 Markdown。

怎么用，三个入口任选。

1. CLI，一条命令 `npx @firecrawl/anydoc 你的文档.docx`
2. 脚本，Node 和 Python 各有 `toMarkdown` 系列 API，适合批量转
3. 浏览器，WASM 版本地转换，敏感文件不上传

在意隐私的看第 3 条。浏览器 demo 用 WebAssembly 在本地跑，文件不用传给别人。

说个诚实边界：扫描版 PDF 它转不了。anydoc 本体不做 OCR，扫描页要走官方托管 API。手写稿、拍照页不归它管。

想试的话，拿一份手边文档跑一次命令，三分钟知道值不值。数据会变，star 数是 08-12 的快照。

---

## 配图文案（4 卡 · 图片占位待 enrich）

【封面卡 · 图片占位】大字：把 Word/PDF 变成干净 Markdown｜副标：9 天涨 1.5 万星的开源工具

【卡 2 · 图片占位：复制粘贴后乱码的文档对比】配文：复制粘贴毁格式，手动整理一份二十分钟

【卡 3 · 图片占位：终端执行 npx 命令截图】配文：一条命令 `npx @firecrawl/anydoc 你的文档.docx`

【卡 4 · 图片占位：浏览器 WASM demo 页】配文：敏感文件用浏览器版，本地转换不上传
