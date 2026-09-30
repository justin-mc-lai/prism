# Release Brief — prism-project-docs-v1（Lake B）

- status: **released（人工批准）**
- feature: `prism-project-docs-v1`
- version: `v0.0.1`
- approved_by: 用户（对话指令：批准 + 写 brief + 推送 origin/main）
- approved_at: 2026-09-30（Asia/Shanghai）
- approved_action: `check_release_gate(human_confirmed=True)` → done + push `main` → `origin/main`
- release_gate: `release_gate` → **human_confirmed**
- QA: `run-20260930T115906965349` · **22/22 TC passed** · AC 7/7 · release_confidence 1.0
- truth: **R5 frozen**（baseline `sha256:7680b00dc667…`）
- reconciliation: **completed**（`change_reason=implementation-first-reconciliation`，R4→R5）
- release scorecard: **release_ready=true**
- loop-goal run: `lg-cc1c678c67c8` → stage `done`

## Delivered

1. **项目内作品目录（AC-PDO-001）**
   - `scripts/ai_manga_drama.py init --dir <project>/docs/prism`：在任意项目建 `docs/prism/`，
     子目录与 Prism 仓 `content/` 同名同构（README.md 除外），并生成门面 `README.md`
     三类索引（大纲 / 母稿 / 分镜剧本）。
2. **PRISM_HOME 零副本约定（AC-PDO-002）**
   - `skills/prism-director|produce|qa/SKILL.md` 写入 `PRISM_HOME` 指令面（3 面共 11 处），
     命令统一写成 `$PRISM_HOME/scripts/...`；项目内不拷贝任何脚本。
3. **路径契约唯一化（AC-PDO-003）**
   - `contracts/form-manga-drama.contract.md §4` 与 `content/pipelines/ai-manga-drama/README.md`
     收敛为唯一 canonical 路径，旧路径标 alias/deprecated。
4. **可执行检查门（AC-PDO-004）**
   - `scripts/check_prism_project_docs.sh`：断言目录同构、README 门面、PRISM_HOME 指令面、
     路径正典无回潮；`--help`/位置参数可用，CI 友好。
5. **与 docs/beacon 边界（AC-PDO-005）**
   - 明确 `docs/beacon/` 管需求真相、`docs/prism/` 管作品产物，单向引用、互不越界写入。

变更文件（8 个，+166/−5）：`scripts/ai_manga_drama.py`、`scripts/check_prism_project_docs.sh`、
`scripts/install_public_surfaces.sh`、`contracts/form-manga-drama.contract.md`、
`content/pipelines/ai-manga-drama/README.md`、`skills/prism-{director,produce,qa}/SKILL.md`。

## Known runtime caveat（非本 feature 引入）

- 版本级 `beacon release check v0.0.1` 仍报 `coverage artifact ready` fail：版本聚合
  `.beacon/coverage-summary.json` 的 `coverage_rate=0.0`（`feature=""` 聚合口径，tested_ac=0）。
  该现象在既往各 lake 发布中同样存在，属版本级聚合口径问题，非本 feature QA 缺口；
  权威 `beacon release scorecard v0.0.1` 判定 `release_ready=true`，QA 层证据链已闭合。

## Still forbidden / deferred

- `prism-drama-spec-v1`（manju 86 规则分镜规范，代码已落盘）另行建包冻结，不在本 feature 内。
- 公开发布内容创作能力的其它湖（C/D/E/F）不因本 feature 解锁。
- 不得宣称海级 closure。
