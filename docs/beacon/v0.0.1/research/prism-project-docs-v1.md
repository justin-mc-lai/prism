# Research Closure: prism-project-docs-v1

- version: `v0.0.1`
- feature: `prism-project-docs-v1`
- diagram_types: none
- state_axes: episode-lifecycle (planned → validated → compiled → rendered → assembled → qa-passed)
- status: research closure (planner artifact，非 frozen truth)

## Architecture

三个物理位置，三个不同性质的 SoT，必须先分清再谈目录：

| 位置 | 放什么 | 性质 |
|---|---|---|
| prism 仓 `skills/` + `scripts/` + `contracts/` + `content/pipelines/*.schema.json` | 指令面 + 执行体 + 判据 | **能力 SoT**（唯一，不复制） |
| 项目仓 `docs/prism/`（本 feature 要新建） | 大纲、母稿、分镜剧本、提示词、srt、manifest、成片索引 | **内容 SoT**（项目的作品资产，归项目 git 管） |
| prism 仓 `content/` | `_examples`、`fixtures/`、dogfood 样例 | 样例，**不是**任何项目的内容 SoT |

关键洞察（第一性）：**prism 仓的 `content/` 就是 prism 自己这个项目里的 `docs/prism/`**。
两者应当**同构**（同一套子目录名），而不是发明第二套心智模型。缺的从来不是新 schema，
而是「把同一布局引导到任意项目」的**投影机制** + 路径契约唯一化。

canonical write path：
- 能力演进 → 只写 prism 仓（`scripts/`、`contracts/`、`storyboard-schema.json`）。
- 内容产出 → 只写项目 `docs/prism/`（由 `--dir` / `PRISM_OUT` 参数决定）。
- 读侧投影：7 个公开 skill 的 SKILL.md（软链）、`分镜脚本.md` / `drama-spec.json` / `{ep}.srt`（编译产物）。

## Business Flow

触发：项目里的人/agent 调用某个 prism 公开面（选 → 定 → 导 → 产 → 验 → 发）。

1. **发现**：agent 通过软链的 `SKILL.md` 找到指令面。
2. **定位能力**：指令面必须告知执行体在哪（当前缺口：只讲怎么做，不讲脚本在哪 → 见 Open Questions Q1）。
3. **建包**：`ai_manga_drama.py init --dir <project>/docs/prism --episode <slug>` → 落 `docs/prism/pipelines/ai-manga-drama/<slug>/storyboard.json`。
4. **校验/编译/渲染/拼接/QA**：同一条命令链，产物全部落 `--dir` 下；凭证缺失 fail-closed，无本地兜底（沿用现有铁律）。
5. **终端态**：`qa-passed` + release 人工批准；`docs/prism/` 里留下可 review 的文本证据（分镜脚本.md、srt、drama-spec.json、SCORECARD）。

分支点：无凭证（exit 2，终止）／spec 门失败（reason_code，回 director）／QA 不过（回 produce，不改母稿）。
actor handoff：master 冻结后内容 SoT 变更只能走 refreeze，produce/qa 不得反向改 `docs/prism/` 里的母稿。

## State Machine

- 稳定态：`draft`（storyboard 可编辑）→ `validated` → `compiled`（提示词+srt 已产）→ `rendered`（clips 齐）→ `assembled`（成片+AI 标识）→ `qa-passed` → `released`（人工批准）。
- 合法迁移：只进不退；`released` 不可回。
- 阻断迁移：`compiled` 之前无 ref_image 不得进 `rendered`；无 `qa-passed` 不得进 `released`；任何态不得静默改已冻结母稿。
- 恢复：`rendered` 失败可重跑 provider 调用（幂等 by shot_id），不回退已成片段。
- `docs/prism/` 与 `docs/beacon/` 无状态耦合：beacon 管需求真相状态，prism 管内容产线状态。

## Decision Priority

冲突时的裁决顺序（实现与 QA 必须按此序评估）：

1. **global-boundaries / 现行契约**（`contracts/*.contract.md`）——契约赢过一切本地约定。
2. **路径唯一化裁决**：同一产物只允许一条 canonical 路径；另一处标注 `alias/deprecated`，不得两处都写"应当"。（当前冲突点：`form-manga-drama.contract.md §4 = content/presentations/{vertical}/{slug}/manga-drama-{ep}/` vs 管线 README = `content/masters/ai-manga-drama/{slug}/`。）
3. **SoT 归属**：项目内容归项目仓，能力归 prism 仓；任何"把 scripts 复制进项目"的方案默认低优先（复制=第二份能力 SoT=漂移）。
4. **凭证与兜底**：无凭证 fail-closed > 一切便利性；kenburns/本地兜底已由用户决策取消，不再讨论。
5. **最懒可用**：能用"参数/环境变量 + 现有 --dir"解决的，不新增分发机制。

## Decisions（2026-09-29 用户已拍板，freeze 的输入）

- **D1 = Q1 采纳 A**：`PRISM_HOME` 约定；skill 指令面写明，全部命令 `$PRISM_HOME/scripts/...`，项目零能力副本。
- **D2 = Q3+Q4 采纳同构方案**：项目 `docs/prism/{briefings,storyworlds,masters,pipelines,produced,distribution}/README.md` 与 prism `content/` 同构；`form-manga-drama.contract.md §4` 改为单一 canonical（项目侧 `docs/prism/pipelines/...`，prism 仓 `content/` 为 dogfood），旧路径标 alias/deprecated 并加 `check_*` 断言防回潮。
- **D3 = Q5 采纳切分**：manju 蒸馏单独成 `prism-drama-spec-v1`；本 feature 不含 86 规则/门/fixture 的实现内容（它们已落盘未 commit，归属另一 feature package 冻结）。

## Open Questions

无。全部 open question 已在上方 `Decisions` 关闭（D1/D2/D3，2026-09-29 用户拍板）。

## Promotion Notes

accepted 后进 truth 冻结，建议 AC 切分（可验收、可机器/证据判定）：

1. `AC: 项目侧 init 落盘形状` —— 在空项目跑 `init --dir <p>/docs/prism` 后，目录树与 `content/` 同构，README 索引存在。
2. `AC: 路径契约唯一化` —— `form-manga-drama.contract.md` 与管线 README 只剩一条 canonical 路径，另一处为 alias 标注；`check_*` 断言两处文本一致。
3. `AC: 能力可达性` —— 按 SKILL.md 指引（含 PRISM_HOME 约定）在项目内跑通 `validate` 与 `compile`，产物全部落在 `--dir` 下，prism 仓无新增写入。
4. `AC: 不复制能力` —— 项目仓内不存在 `scripts/` 副本；断言 `git ls-files` 无 prompt_compiler 副本。
5. `AC: 与 docs/beacon/ 边界` —— docs/prism 不写需求真相字段，docs/beacon 不写分镜产物；交叉引用只允许单向（prism 产物引用 beacon feature slug）。

上游输入（freeze 前）：`truth.define → truth.acceptance → truth.coverage`。
兼容映射：`prd → user-story → test-case → requirement_clarity → freeze`。

## Support Findings

### Brainstorm

#### Round 2026-09-29T15:25:09.511051+00:00

- source_skill: `beacon-brainstorm`
- round_id: `2026-09-29T15:25:09.511051+00:00`
- material_effect: `read_only_route_only`
- adoption_status: `route_only`
- route_decision: beacon-brainstorm
- finding_summary: Converge missing or ambiguous requirement points into explicit questions and candidate decisions before editing frozen truth.
- source_refs: `docs/beacon/global-boundaries.md`, `docs/beacon/v0.0.1/SUMMARY.md`, `docs/beacon/v0.0.1/execution/index.md`, `docs/beacon/v0.0.1/execution/architecture-blueprint.md`, `contracts/form-manga-drama.contract.md`, `content/pipelines/ai-manga-drama/README.md`, `scripts/install_public_surfaces.sh`, `docs/sot-layering-decision.md`
