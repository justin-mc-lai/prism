# 第三方规范运用审计 — humanized.md（anydoc blog-beginner）

> 审计对象: `humanized.md`
> 规范来源: selfmedia-creator 第三方/自研 skill
> - 写稿: selfmedia-writing（prose-core / oss-depth-beginner-archetype / checklist / content-pipeline）
> - 人话: selfmedia-humanize（ai-tells-checklist / human-voice-techniques）、humanizer-zh
> - 创作: kushi-narrative-zh（6 原则）
> 审计时间: 2026-08-12

## 结论

**未完整运用。** 结构骨架（四段式/MVP/由简入深/亮点/坑点/行动）基本达标，但完整规范存在
7 项缺口 + 1 项硬门未满足；按 fail-closed 原则，当前 QA 结论应为 **needs_fix**（原 pass 不成立）。

## 对照矩阵

| # | 规范项 | 要求（来源） | 实际 | 判定 |
|---|--------|--------------|------|------|
| 1 | repo-digest | 深度稿必须先有 `repo-digest.md`（archetype：无 digest → 停止） | 未生成，只用 README+API | ❌ |
| 2 | 🚀 小白 MVP | 环境前提一行 + 命令块 + 跑通清单 + 口诀三句 | 命令✅ 清单✅ 口诀✅ 环境前提❌ | ⚠️ |
| 3 | 📖 由简入深 | 阅读路径**表格**（3/10/进阶 ≥3 行）+ 引导句 | 用小节替代表格；无“先跑 MVP 再回来看 🗺️” | ❌ |
| 4 | 截图/图说 | 深度稿 ≥2 张 assets 截图（enrich 后） | 0 张 | ❌ |
| 5 | 🗺️ 进阶 | “先懂”白话✅ + 进阶**模块表**（3–5 模块） | 进阶为散文，无模块表 | ⚠️ |
| 6 | ⚠️ 坑点 | 工业短板 + **不适合列表** | 短板✅ 无“不适合”列表 | ⚠️ |
| 7 | 术语 inline | 术语首次出现白话解释（kushi 6 原则 / checklist） | “绑定”“Agent Skill”未解释；WASM 已解释 | ⚠️ |
| 8 | 人味层 bridge | writing.contract 硬门：每稿必须走至少一轮人味层（selfmedia-humanize / humanizer-zh 等） | **未实际运行**，QA 仅静态模式扫描 | ❌ 硬门 |
| 9 | humanizer-zh 全清单 | 夸大意义/知名度/-ing 浅析/宣传语/模糊归因/AI 词汇/系动词回避/否定排比/连接短语 | 仅扫部分模式；词表扫描结果 0 命中✅，但全清单未逐条跑 | ⚠️ |
| 10 | 口语转折密度 | 约 800 字 3–6 处（human-voice-techniques） | 全文仅 1 处（“更烦的是”） | ❌ |
| 11 | 朗读检查 | prose-core：写完后朗读改别扭句 | 未执行（无证据） | ❌ |
| 12 | 主动语态 | 禁“被发布/被调用”类 | 全文仅 1 处比喻“像被洗衣机搅过”，可接受 | ✅ |
| 13 | 禁翻译腔/禁词 | 综上所述/值得注意的是/不仅…而且… 等 | 全部 0 命中 | ✅ |
| 14 | 场景开场 ≥80 字 | archetype/checklist | 154 字 | ✅ |
| 15 | 长度 1500–2800 字 | archetype | 约 2001 字（不含代码块空白） | ✅ |
| 16 | 四段 H2 emoji | 🎯🗺️💎⚠️ 固定 | 全部存在 | ✅ |
| 17 | 对比表 ≤1 张 | prose-core | 0 张 | ✅ |
| 18 | meta.yaml R11 | 深度稿完成后加 `content_spec: r11` | 只有 `humanize_gate: required`，无 content_spec | ❌ |
| 19 | 个人经历/细节 | 真素材→可核对公开事实→占位 | 使用可核对公开事实（命令/数字）✅，无虚假经历 | ✅ |
| 20 | 情感起伏/有边界 | 有态度、有适合/不适合 | 有态度✅；边界在坑点但不完整 | ⚠️ |

## 硬门判定

- `writing.contract` 第 5 节：**“每稿必须走至少一轮人味层（bridge：selfmedia-humanize / humanizer-zh / qu-ai-wei / shuorenhua 等）”** —— 本稿未执行 ❌
- 因此按 fail-closed，本稿不得进入 release_candidate；应先补人味层 + 缺项后重跑 QA。

## 修复清单（建议顺序）

1. 生成 `repo-digest.md`（oss-repo-read 规范：仓库速览/主流程/模块/坑点线索）
2. 实际执行一轮人味层 bridge（selfmedia-humanize 或 humanizer-zh，记录证据）
3. 补口语转折 3–6 处/800 字、朗读自检（记录改动）
4. 由简入深改表格（3 分钟/10 分钟/进阶 + 引导句）
5. 补术语解释（绑定、Agent Skill）；坑点补“不适合”列表；🗺️ 补进阶模块表
6. 配图：加 0–2 张截图占位或 enrich（说明来源）
7. meta.yaml 加 `content_spec: r11`
