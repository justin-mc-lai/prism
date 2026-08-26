# QA Findings — anydoc vlog-beginner

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-007']
- 检查对象: `script.md` + `edit-list.md` + `director-treatment.md`

## 1. 口播稿门（anti-slop + 体裁）

| 检查 | 结果 | 证据 |
|------|------|------|
| 翻案腔/硬停词/黑话 | 0 命中 | `check_human_voice.py` 0 |
| 叙述提示性冒号 | 0 命中（3 处已改陈述） | `humanize-pass-evidence.md` |
| 破折号（含 en dash） | 0 命中（镜头区间改 `~`） | 同证据 |
| 前 3 秒钩子 | ✅ 开场即场景 | script 0~3s 段 |
| 气口断句/口播词 | ✅ 短句按气口，无「进行/以及/从而」 | 通读 |
| 句长节奏 | ✅ 变异系数警告清零 | 脚本 0 warning |
| 字幕不逐字复读 | ✅ edit-list 字幕要点为结构化 | `edit-list.md` |

## 2. 事实核对（vs FactMaster）

| 成稿声明 | 母稿来源 | 结论 |
|---------|----------|------|
| 九天约 1.5 万星（08-03→08-12） | claim 4 | ✅ 标注快照 |
| 办公格式 → 干净 Markdown | claim 1–2 | ✅ |
| 三入口（CLI/Node·Python/WASM） | claim 3, 10–13 | ✅ |
| WASM 本地转换不上传 | claim 7 | ✅ |
| 扫描 PDF 走托管 API | claim 8 | ✅ |
| MIT | claim 5 | ✅ |

## 3. AV 门（pending 项）

- 分镜/图序/分页一致：✅ 6 镜头与 presentation map、edit list 三处一致
- 字幕/画面文字无乱码：N/A（素材为显式占位，无假图）
- 版权安全：✅ 无受版权保护角色；工具截图占位待 enrich 时核
- openmontage bridge：deferred（AGPL，不 pin）→ 成片 `【成片占位】`，不假装产出

## 4. 门禁结论

- 文案：pass；事实对齐：pass；AV 交接字段：pass（成片待 bridge）
- verdict: `release_candidate_draft_only`（成片渲染 + 人工批准后才可发布）
