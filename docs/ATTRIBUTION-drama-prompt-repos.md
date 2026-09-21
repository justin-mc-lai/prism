# ATTRIBUTION — 短剧/漫剧提示词语料（vendor 四源）

## 来源

| vendor 路径 | 上游仓库 | 作者 | License | 核实日期 |
|---|---|---|---|---|
| `vendor/skills/short-drama-skills` | https://github.com/YvonneMovingon/short-drama-skills | YvonneMovingon（LuxReal） | MIT | 2026-09-17 |
| `vendor/skills/onlyshot` | https://github.com/A-cat-with-carrots/OnlyShot | A-cat-with-carrots（神仙鱼） | MIT | 2026-09-17 |
| `vendor/skills/su-ai-short-drama` | https://github.com/doublesq97-ui/su-ai-short-drama | doublesq97-ui | MIT | 2026-09-17 |
| `vendor/skills/shuohao-skills` | https://github.com/eternityspring/shuohao-skills | eternityspring | Apache-2.0 | 2026-09-17 |

核实项：仓库存在、LICENSE 文件在位、README 功能描述与实测内容一致。

## 补充来源 — 分镜连续性七律（未 vendor，仅蒸馏）

| 上游仓库 | 文件 | License | 核实日期 |
|---|---|---|---|
| https://github.com/HBAI-Ltd/Toonflow-app | `data/skills/production_skills/storyboard_table_techniques.md`（七律原始出处）；另参考同目录 `production_agent_supervision.md`、`production_execution_storyboard_table.md` | Apache-2.0 | 2026-09-21 |
| https://github.com/neilalexanderlee/ai-comic-studio | `src/lib/ai/prompts/storyboard-supervision.ts`（七律再诠释 + 导演前置四问） | Apache-2.0 | 2026-09-21 |

- 取用：`skills/prism-director/references/continuity-seven-laws.md`（七律 / 片段过渡四法 / 拆分粒度 / 两版分歧）。
- **未 vendor 原件**，只蒸馏判断框架与阈值；不含上游运行时或样例数据。
- 两版**节拍密度阈值方向相反**（Toonflow 上限 / ai-comic-studio 下限），各自对应不同失败模式，
  非可互换常数；引用须带来源与适用条件，换模型/形态须重测。

## 本仓使用了什么

1. **蒸馏**（判断框架与阈值，不复制运行时）→
   - `skills/prism-director/references/prompt-syntax-table.md`
   - `contracts/prompt-syntax.contract.md`
   - 取用明细：
     - short-drama-skills → 字段定式（05）、时长公式/切镜阈值（01）、动作语法（03）、对话权力博弈（02）
     - onlyshot → 分镜图 8 段定式、ref 6 段 identity block、失败模式与敏感词四类、字符数/并发实测阈值
     - su-ai-short-drama → 景别/机位/连续性的选择理由（用于字段规则）
     - shuohao-skills → 切分→校验→出图的接力顺序（用于 §0 三层分离）

2. **资产提示词 + 剧本模板蒸馏**（2026-09-21，prism-asset-prompt-templates-v1 / prism-prompt-compiler-v1）→
   - `skills/prism-director/references/asset-prompt-templates.md`
     （执行门 `scripts/check_asset_prompt_templates.sh`）
   - `skills/prism-director/references/script-templates.md`
     （执行门 `scripts/check_prompt_compiler.sh` + `scripts/check_render_handoff.sh`）
   - 取用明细：
     - onlyshot `references/ref-prompt-industrial.md` → **7 段 identity block** 骨架、
       三条铁律（ref 中性平光 / 一致性靠参考图锚定 / 身份块逐字复用）、
       前 200 token 权重、NOT 词 ≤5、四视图水印陷阱、拟物化真假陷阱、候选数成本
     - onlyshot `assets/templates/05_角色圣经.md` → **人物卡**（4 宫格 + 服装表 + 视觉母题）
     - onlyshot `assets/templates/06_场景圣经.md` → **场景卡**（四宫格：全景/入口/陈设/对位）
     - onlyshot `assets/templates/07_道具圣经.md` → **道具卡**（4 宫格白底产品图）
     - onlyshot `assets/templates/03_完整剧本.md` + `剧本.md` + `镜头清单.md` + `分镜.json`
       → **完整剧本 / 分集剧本 / 镜头清单三模板** + storyboard 字段映射（本仓 8-12 镜 / 60-90s 收缩）
     - 本仓新增（无上游对应）：**神兽卡**（creature + evolution 链）、**群像卡**（数量/密度约束）、
       **风格正交**（资产串常量 × 风格串可换，接 `lumenx-style-presets.json` ⊕ `registry/style-presets.yaml`）、
       **确定性编译器** `scripts/prompt_compiler.py`
   - 上游模板原件**保留在 `vendor/skills/onlyshot/`**（蒸馏 ≠ 搬走），本仓版本为 Prism 改写。
3. **vendor 原件**：四仓完整复制到 `vendor/skills/`（剔除 `.git`）。为控制仓库体积，
   剔除上游大体积演示媒体（`su-ai-short-drama/docs/media/*.gif|*.mp4`、
   `short-drama-skills/script-*.png`、`shuohao-skills/assets/reelbench-first-screen.png`）；
   这些媒体仅用于上游 README 演示，不含语法信息，需要时按上方仓库地址取回。
4. **未使用**：上游 CLI/脚本运行时（`scripts/`、`tools/`）不接入主链；上游样例 JSON/MD
   （如 `shuohao-skills/skills/novel-characters/examples/渡口-*.json`）仅作格式参考，不作为本项目母稿。
5. **明确未 vendor**（授权链不清，只作外部参考）：
   `fenggeliaoai/AIPrompts` — GPL-3.0 且作者注明「部分提示词非原创，原作者【道格】，切勿商业使用」，
   与本仓闭源商用冲突，**不复制任何内容**。

## 使用边界

- 上游 MIT / Apache-2.0 内容商用须保留本声明与随附 LICENSE。
- onlyshot 的字符数上限、ref 权重、一致性百分比均来自其单项目 N=36 实测（即梦 5.0，
  2026-05-16，中英 ~7:3）。**不是模型官方物理常数**；换模型 / 换语言比例 / 换时间窗须重测。
  引用时带来源与测试条件；未重测即引用视为无证据（见 `contracts/prompt-syntax.contract.md` §5）。
- su-ai-short-drama 的「女频/男频」是内容市场创作配置，非对性别的心理判断；本项目只取其
  岗位分工与景别机位规则，不搬运受众假设。
- 上游提示词涉及具体平台（红果/抖音/即梦）的节奏与合规结论，本项目不据此声称任何平台过审
 或流量结果；《微短剧发展管理办法》AI 标识义务仍由 `form-manga-drama.contract.md` §5 强制。
