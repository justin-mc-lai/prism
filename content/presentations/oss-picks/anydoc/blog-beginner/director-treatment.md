# Director Treatment — anydoc 小白科普文

- mode_id: treatment-director
- public_id: director
- lane: standard
- recommended_next_harness: produce
- map_ids_considered: ['MAP-002']

## 核心意图

让新手 30 秒内能跑通“文档 → Markdown”，并知道这条工具链还能接进自己的 AI 助手。

## 受众效果

读完觉得“我能用上”，不觉得是营销软文；技术名词首次出现用白话括号解释。

## 情绪曲线

痛点（复制粘贴格式乱）→ 上手快感（一行命令出结果）→ 认知增量（同一内核三种接法 + Agent Skill）。

## 节拍

1. 场景开场：收文档、贴进工具、格式全乱
2. 🚀 MVP：`npx @firecrawl/anydoc 你的文档.docx` + 跑通检查
3. 📖 由简入深：3 分钟 CLI / 10 分钟 Node·Python / 进阶 WASM·Agent Skill
4. 🎯 本质：格式无关的“文档→Markdown”转换层
5. 🗺️ 架构：Rust 核心 + 三绑定 + 托管 Parse
6. 💎 亮点：输出统一 / 浏览器本地转换 / Agent Skill
7. ⚠️ 坑点：扫描 PDF 要 OCR、官方速度声明、npx 首次下载
8. 收尾行动：装 CLI 试一个文件 / 给 Agent 装 skill

## 硬约束

- 所有数字只引用 FactMaster 事实（标注检索时刻）。
- 不夸大：速度声明标注“官方宣称”。
