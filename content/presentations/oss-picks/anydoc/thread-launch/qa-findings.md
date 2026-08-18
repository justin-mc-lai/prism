# QA Findings — anydoc thread-launch

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-005', 'MAP-002']
- 检查对象: `content/presentations/oss-picks/anydoc/thread-launch/humanized.md`

## 1. anti-slop / 人话门

按 `skills/prism-qa/references/anti-slop-gate.md` 扫描（≥30 模式 + 场景档位 + 仲裁顺序）：

| 检查 | 结果 | 证据 |
|------|------|------|
| 翻案腔（不是A而是B 及 7 变体） | 0 命中 | `check_human_voice.py` → 翻案腔变形 0 |
| 清嗓开场/总结复读/空金句 | 0 命中 | 通读 + 脚本 0 |
| 硬停词（说白了/说穿了/先说结论） | 0 命中 | 脚本 0 |
| 黑话/借喻/抒情词抽象化 | 0 命中 | 脚本 0 |
| 叙述提示性冒号 | 0 命中（7 处已改为陈述句） | 修复记录见 `humanize-pass-evidence.md` |
| 破折号 | 0 命中 | 脚本 0 |
| 无源归因（weasel） | 0 命中 | 全部数据回源 MASTER |
| 短帖节奏 | 每帖一意、帖帖推进 | 通读：8 帖 = 痛点→工具→入口→隐私→边界→判断→数据→行动 |

场景档位：public-writing / standard ✅；无源引用模式：不适用（全有源）✅。

## 2. 事实核对（vs FactMaster）

| 成稿声明 | 母稿来源 | 结论 |
|---------|----------|------|
| 8 种格式 | claim 1 | ✅ |
| GitHub 风格 Markdown | claim 2 | ✅ |
| Rust + Node/Python/WASM | claim 3 | ✅ |
| 九天约 1.5 万星 / 792 forks（创建 08-03，检索 08-12） | claim 4 | ✅ 标注快照与日期推算 |
| MIT | claim 5 | ✅ |
| 单数字毫秒为官方声明 | claim 6 | ✅ 未夸大 |
| WASM 本地转换不上传 | claim 7 | ✅ |
| 扫描 PDF 走托管 API | claim 8 | ✅ |
| CLI 命令 | claim 10 | ✅ |

## 3. 门禁结论

- anti-slop：pass（脚本失败项清零，结构性豁免 3 处元信息冒号已归位）
- 事实对齐：pass（全部声明回源 FactMaster）
- 证据路径：`content/masters/oss-picks/anydoc/MASTER.md` + `humanize-pass-evidence.md`
- verdict: `release_candidate_draft_only`（发布仍需人工批准）
