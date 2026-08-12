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
- 证据路径：`content/masters/oss-picks/anydoc/MASTER.md` + GitHub API 快照
- 放行至 release（草稿阶段）；**公开发布需人工二次批准**
