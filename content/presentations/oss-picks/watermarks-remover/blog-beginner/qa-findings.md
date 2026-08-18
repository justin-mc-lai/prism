# QA Findings — watermarks-remover blog-beginner

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-005', 'MAP-002']
- 检查对象: `content/presentations/oss-picks/watermarks-remover/blog-beginner/humanized.md`

## 1. anti-slop / 人话门

按 `skills/prism-qa/references/anti-slop-gate.md`（30+ 模式 + 场景档位 + 仲裁顺序）扫描：

| 检查 | 结果 | 证据 |
|------|------|------|
| 翻案腔 7 变体 | 0 命中 | `check_human_voice.py` 0 |
| 清嗓开场/万能开场 | 0 命中 | 首段为具体场景 |
| 硬停词/黑话/借喻/抒情词 | 0 命中 | 脚本 0 |
| 叙述提示性冒号 | 0 命中（4 处已改） | `humanize-pass-evidence.md` |
| 破折号（含 en dash） | 0 命中（占位符 2 处已改） | 同证据 |
| 无源归因（weasel） | 0 命中 | 全部回源 MASTER 15 条 claims |
| 结构固定位冒号 | 24 处逐条归位豁免 | 同证据 |
| 英文泄漏 | 0（代码块已跳过） | `check_readability.py` ok |

## 2. 事实核对（vs FactMaster）

| 成稿声明 | 母稿来源 | 结论 |
|---------|----------|------|
| 4 天约 8.5 千星 / 876 forks（08-11 创建，08-15 检索） | claim 6 | ✅ 日期推算 + 快照标注 |
| 三层处理（Unicode/统计/C2PA 等元数据） | claim 2 | ✅ |
| 格式清单（PNG/JPEG/WebP/SVG/PDF/DOCX/ODT/HTML/MD） | claim 3 | ✅ |
| 纯 Python 3.10+ 标准库 | claim 5 | ✅ |
| 文本工具拒绝二进制输入 | claim 9 | ✅ |
| API key 只走环境变量 + 远程默认关 | claim 11 | ✅ |
| 两个 harness 从不发布（license 原因） | claim 12 | ✅ 未夸大为已发布 |
| MIT | claim 7 | ✅ |
| content you own 定位 | claim 1 | ✅ 全文保持 |

## 3. 伦理/合规门（本 topic 专项）

- ✅ 未提供规避检测/伪造来源方法；结尾显式声明
- ✅ 「从不发布的 harness」按事实写，未写成可用能力
- ✅ 未承诺检测率/清除率；无假数据

## 4. 门禁结论

- anti-slop：pass（硬禁令清零，结构性豁免已归位）
- 事实对齐：pass（全部声明回源 FactMaster）
- 伦理门：pass
- 证据路径：`content/masters/oss-picks/watermarks-remover/MASTER.md` +
  `humanize-pass-evidence.md` + `content/briefings/watermarks-remover-hotspot.md`
- verdict: `release_candidate_draft_only`（截图 enrich 待补；发布仍需人工批准）
