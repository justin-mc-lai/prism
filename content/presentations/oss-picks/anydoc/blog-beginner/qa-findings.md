# QA Findings — anydoc blog-beginner

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-005']
- 检查对象: `content/presentations/oss-picks/anydoc/blog-beginner/humanized.md`

## 1. anti-slop / 人话门

按 `skills/prism-qa/references/anti-slop-gate.md` 扫描：

| 模式 | 结果 | 证据 |
------|------|------|
| 二元对比（不是X而是Y） | 未命中 | `rg "不是.*而是" humanized.md` → 0 |
| 清嗓开场（说实话/值得注意的是） | 未命中 | `rg "说实话\|值得注意的是"` → 0 |
| 总结复读（综上所述/最后总体） | 未命中 | `rg "综上所述"` → 0 |
| 空话词（赋能/闭环） | 未命中 | `rg "赋能\|闭环"` → 0 |
| 机械排比/三段式法则 | 未命中 | 通读：短段节奏有变化，无强制三连 |
| 假深刻结尾 | 未命中 | 结尾为具体行动项，非金句 |

人话判据：句式长短交错 ✅；口语转折为点缀 ✅；细节具体（命令/数字/路径）✅；结尾可行动 ✅。

## 2. 事实核对（vs FactMaster）

| 成稿声明 | 母稿来源 | 结论 |
|---------|----------|------|
| 约 14,888 stars / 792 forks（2026-08-12） | MASTER claim 4 | ✅ 一致并标注检索时刻 |
| 支持 Word/PPT/Excel/ODT/RTF/EPUB/CSV/PDF | claim 1 | ✅ |
| 输出 GitHub-Flavored Markdown | claim 2 | ✅ |
| Rust + Node/Python/WASM 绑定 | claim 3 | ✅ |
| MIT | claim 5 | ✅ |
| “单数字毫秒”标注为官方声明 | claim 6 | ✅ 未夸大 |
| 浏览器 WASM 本地转换不上传 | claim 7 | ✅ |
| 扫描 PDF OCR 由托管 API 负责 | claim 8 | ✅ |
| `npx skills add firecrawl/anydoc` | claim 9 | ✅ |
| CLI/Node/Python 安装命令 | claim 10–12 | ✅ |

## 3. 门禁结论

- anti-slop：pass（无命中模式）
- 事实对齐：pass（全部声明可回源 FactMaster）
- 证据路径：`content/masters/oss-picks/anydoc/MASTER.md` + `repo-digest.md` + GitHub API 快照

## 4. 修复记录（2026-08-13，第三方规范审计后）

| 原缺口 | 修复 | 验证 |
|--------|------|------|
| repo-digest 缺失 | 新增 `repo-digest.md` | ✅ 存在 |
| 由简入深表格/引导句 | 改为 3 行表格 + “先跑 MVP，再回来看 🗺️” | ✅ |
| 截图 0 张 | 新增“先带你看一眼”2 处显式占位 | ✅ 占位（enrich 待补） |
| 进阶模块表 | 🗺️ 新增 5 模块表（CLI/Node/Python/WASM/Agent Skill） | ✅ |
| 不适合列表 | ⚠️ 新增“真正不适合它的场景”3 条 | ✅ |
| 术语解释 | “绑定（bindings）”“Agent Skill”inline 解释 | ✅ |
| 口语转折密度 | 增至 7 处 / 约 2364 字 | ✅ |
| 朗读自检 | 执行并记录于 `humanize-pass-evidence.md` | ✅ |
| 人味层硬门 | 实际改写一轮，证据可回放 | ✅ |
| meta R11 | `content_spec: r11` 已加 | ✅ |

## 5. 深度蒸馏复核（2026-08-14）

| 检查项 | 结果 | 证据 |
|--------|------|------|
| `check_human_voice.py` 硬禁令 | 失败清零（硬停词/破折号/叙述冒号/黑话/翻案腔 全 0） | 复核记录见 `humanize-pass-evidence.md` |
| 结构性冒号仲裁 | 28 处全部为体裁固定位，逐条归位豁免 | 同证据文件 |
| 口语转折密度 | 5 处 / 约 2300 字（修复 2 处硬停词后），点缀非灌满 | 同证据文件 |

## 5. 最终门禁结论

- anti-slop：pass
- 事实对齐：pass
- 人味层：pass（实际执行 + 证据）
- 放行至 release（草稿阶段）；**公开发布需人工二次批准**
- 显式 deferral：真实截图 enrich（当前为占位）、独立性能基准（保持“官方声明”标注）
