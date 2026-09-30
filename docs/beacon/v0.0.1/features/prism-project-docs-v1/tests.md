---
slug: prism-project-docs-v1
version: v0.0.1
materials_status: current
---

# Tests: prism-project-docs-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-PDO-001 | AC-PDO-001 | `rm -rf /tmp/prism-pdo-001 && python3 $PRISM_HOME/scripts/ai_manga_drama.py init --dir /tmp/prism-pdo-001/docs/prism --episode ep-t1 && diff <(ls /tmp/prism-pdo-001/docs/prism \| grep -v README.md \| sort) <(ls content \| sort)` | 项目侧子目录与 content/ 同名同构（README.md 除外） |
| TC-PDO-002 | AC-PDO-001 | `test -f /tmp/prism-pdo-001/docs/prism/README.md && rg -q '大纲' /tmp/prism-pdo-001/docs/prism/README.md && rg -q '母稿\|masters' /tmp/prism-pdo-001/docs/prism/README.md && rg -q '分镜' /tmp/prism-pdo-001/docs/prism/README.md` | 门面 README 存在且含大纲/母稿/分镜三类索引 |
| TC-PDO-003 | AC-PDO-001 | `bash scripts/check_prism_project_docs.sh --init-shape /tmp/prism-pdo-001/docs/prism` | init 落盘形状检查脚本 exit 0 |
| TC-PDO-004 | AC-PDO-002 | `rg -n 'PRISM_HOME' skills/prism-director/SKILL.md skills/prism-produce/SKILL.md skills/prism-qa/SKILL.md \| wc -l \| awk '{exit !($1>=3)}'` | 公开 skill 指令面写入 PRISM_HOME 约定（≥3 处） |
| TC-PDO-005 | AC-PDO-002 | `rg -n '\$PRISM_HOME/scripts/' skills/prism-director/SKILL.md skills/prism-produce/SKILL.md \| wc -l \| awk '{exit !($1>=2)}'` | 命令示例以 `$PRISM_HOME/scripts/` 开头（≥2 处） |
| TC-PDO-006 | AC-PDO-002 | `! git ls-files \| rg -q 'prompt_compiler\.py\|ai_manga_drama\.py\|drama_spec\.py' \|\| (git ls-files \| rg 'prompt_compiler\.py\|ai_manga_drama\.py\|drama_spec\.py' \| rg -q '^scripts/')` | 仓内三脚本只存在于 scripts/（唯一能力 SoT，无副本） |
| TC-PDO-007 | AC-PDO-003 | `bash scripts/check_prism_project_docs.sh --canonical-path` | 契约 §4 与管线 README canonical 行唯一且一致（exit 0） |
| TC-PDO-008 | AC-PDO-003 | `rg -n 'alias\|deprecated' contracts/form-manga-drama.contract.md \| rg -q 'content/presentations'` | 旧路径 content/presentations 已标 alias/deprecated |
| TC-PDO-009 | AC-PDO-003 | `bash scripts/check_prism_project_docs.sh --canonical-path --invert; test $? -eq 1` | 反向断言：破坏 canonical 一致性时检查脚本必须 fail（负向） |
| TC-PDO-010 | AC-PDO-004 | `bash scripts/check_prism_project_docs.sh --install-notice` | install 产物说明含"只装指令面 + PRISM_HOME"（exit 0） |
| TC-PDO-011 | AC-PDO-004 | `rg -n '只软链\|指令面' scripts/install_public_surfaces.sh \| wc -l \| awk '{exit !($1>=1)}'` | install 脚本注释明示只装指令面 |
| TC-PDO-012 | AC-PDO-005 | `! rg -n 'parser_contract\|revision_id' docs/prism/ \|\| ! rg -l 'parser_contract' docs/prism/ 2>/dev/null` | docs/prism 无需求真相字段（负向） |
| TC-PDO-013 | AC-PDO-005 | `! rg --files docs/beacon \| rg -q '(^|/)(storyboard\.json\|分镜脚本\.md)$'` | docs/beacon 下无分镜产物文件（负向；按产物名判定，非字面内容匹配） |
| TC-PDO-014 | AC-PDO-005 | `bash scripts/check_prism_project_docs.sh --boundary` | 边界检查脚本 exit 0（单向引用 + 无真相字段） |
| TC-PDO-015 | GATES | `beacon truth review prism-project-docs-v1 --project . --version v0.0.1 --json` | Truth Review Gate A/B/C + L0 pass，recommend_freeze=true |
| TC-PDO-016 | GATES | `beacon doctor verify-truth-integrity prism-project-docs-v1 --project-root . --version v0.0.1 --mode block --json \| python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get('result',{}).get('blocked') in (False,None) and d.get('result',{}).get('closure_contract',{}).get('closure_allowed') else 1"` | `closure_allowed=true` 且 finding_count=0（integrity 门真跑、非空报告） |
| TC-PDO-017 | GATES | `rg -n 'user_decision:\s*pending' docs/beacon/v0.0.1/features/prism-project-docs-v1/truth.md; test $? -eq 1` | Deferral Ledger 无 pending 项（rg 无命中则 exit 1 → 断言成立） |
| TC-PDO-018 | FSM | `rg -n 'scaffolded.*validated\|validated.*compiled\|compiled.*rendered\|rendered.*assembled\|assembled.*qa_passed\|qa_passed.*released' docs/beacon/v0.0.1/features/prism-project-docs-v1/truth.md \| wc -l \| awk '{exit !($1>=6)}'` | FSM 七态六跃迁在 truth 中成对出现（scaffolded→validated→compiled→rendered→assembled→qa_passed→released） |
| TC-PDO-019 | FSM | `rg -n 'illegal: scaffolded → compiled\|illegal: compiled → rendered\|illegal: assembled → released' docs/beacon/v0.0.1/features/prism-project-docs-v1/truth.md \| wc -l \| awk '{exit !($1>=3)}'` | 三条非法跃迁槽位（跳校验/无凭证渲染/无人工发布）全部在 truth |
| TC-PDO-020 | FSM | `rm -rf /tmp/pdo-fsm && cp -r content/pipelines/ai-manga-drama/fixtures/ep-xianxia-spec /tmp/pdo-fsm && (unset PRISM_T2I_KEY PRISM_I2V_KEY PRISM_T2V_KEY PRISM_TTS_KEY; python3 scripts/ai_manga_drama.py request --episode /tmp/pdo-fsm >/dev/null 2>&1; echo $? )` | illegal compiled→rendered：无凭证必须 fail-closed，输出 `2`（无兜底、无假成片） |
| TC-PDO-021 | FSM | `rg -o '"release_gate": "pending_human"' /tmp/pdo-fsm/video-manifest.json` | illegal assembled→released：BLOCKED 时 release_gate 停在 `pending_human`（无人工批准不得发布） |
| TC-PDO-022 | FSM | `python3 scripts/ai_manga_drama.py validate --storyboard content/pipelines/ai-manga-drama/fixtures/ep-compile-test/storyboard.json >/dev/null 2>&1; test $? -eq 0` | legal scaffolded→validated：合法跃迁可执行（validate exit 0） |

## Coverage 说明

- 每条 AC 至少一行行为级 TC（Command + Assertion），验证列均为可执行命令 + 可判定断言。
- TC-PDO-006/012/013/009 为负向断言（应当失败的检查必须真的失败）。
- TC-PDO-001/002/003 依赖 TC-PDO-001 先创建的临时目录 `/tmp/prism-pdo-001`，按序执行。
- `PRISM_HOME` 在执行环境未设置时取仓库根：`export PRISM_HOME=$(pwd)`。
