# QA Findings — anydoc xhs-beginner

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-005', 'MAP-002']
- 检查对象: `content/presentations/oss-picks/anydoc/xhs-beginner/humanized.md`

## 1. anti-slop / 人话门

| 检查 | 结果 | 证据 |
|------|------|------|
| 翻案腔 7 变体 | 0 命中 | `check_human_voice.py` 0 |
| 清嗓开场/万能开场 | 0 命中 | 首段为具体场景 |
| 硬停词/黑话/借喻/抒情词 | 0 命中 | 脚本 0 |
| 叙述提示性冒号 | 0 命中（列表冒号已改逗号） | 修复记录见 `humanize-pass-evidence.md` |
| 破折号 | 0 命中 | 脚本 0 |
| 句长机械节奏 | 无警告（变异系数警告已消除） | 脚本 0 warning |
| 小红书平台适配 | 痛点开场/emoji 克制/分段短/标题兑现 | 通读 |
| 无源归因 | 0 命中 | 全部回源 MASTER |

结构性豁免（逐条归位）：元信息头部 3 处英文冒号；卡片标注 9 处（大字/副标/配文，form-xhs manifest 固定位）。

## 2. 事实核对（vs FactMaster）

| 成稿声明 | 母稿来源 | 结论 |
|---------|----------|------|
| 8 种格式 + 干净 Markdown | claim 1–2 | ✅ |
| Rust + Node/Python/WASM | claim 3 | ✅ |
| 9 天约 1.5 万星（08-03 创建，08-12 检索） | claim 4 | ✅ 日期推算已标注 |
| MIT | claim 5 | ✅ |
| WASM 本地转换不上传 | claim 7 | ✅ |
| 扫描 PDF 走托管 API | claim 8 | ✅ |
| CLI 命令 | claim 10 | ✅ |

## 3. OCR / 图片门

- 4 张卡均为显式【图片占位】（enrich 待补），无假截图；占位符合仓规
- 卡片配文与正文一致，无标题承诺落空

## 4. 门禁结论

- anti-slop：pass（脚本失败项清零，结构性豁免已归位）
- 事实对齐：pass（全部声明回源 FactMaster）
- 证据路径：`content/masters/oss-picks/anydoc/MASTER.md` + `humanize-pass-evidence.md`
- verdict: `release_candidate_draft_only`（图片 enrich 后仍须人工批准发布）
