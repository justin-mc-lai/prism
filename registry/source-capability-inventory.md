# Source Capability Inventory（selfmedia-creator 全量盘点）

> 目标：让 Prism 对源仓每个创作能力都有明确策略（distill / bridge / vendor_pin / defer），
> 逐步替换过程中不留「未盘点即未决策」的灰色面。
> 盘点基线：selfmedia-creator `skills/` + `vendor/writing-skills/`（2026-08-14）。

## 全量表

| # | 源能力 | 上游 | 定位 | 策略 | Prism 落点 | 状态 |
|---|--------|------|------|------|-----------|------|
| 1 | selfmedia-production-pipeline | 自研 | 生产管线编排 | distill | `skills/_internal/orchestration/*` | 已蒸馏（MAP-001） |
| 2 | selfmedia-director | 自研 | 导演 treatment/QC 规范 | distill（体量中等） | `prism-director` + `_internal/adapters/director.contract.md` | ✅ 已蒸馏（MAP-002） |
| 3 | selfmedia-topic-radar | 自研 | 选题雷达 | bridge | `prism-intel` briefing schema | bridge（MAP-003） |
| 4 | selfmedia-newsnow | 自研 | 热点速报 | bridge | `prism-intel` | bridge（MAP-010） |
| 5 | selfmedia-last30days | 自研 | 30 天盘点 | bridge | `prism-intel` | bridge（MAP-010） |
| 6 | selfmedia-zhihu-hot | 自研 | 知乎热榜 | bridge | `prism-intel` | bridge（MAP-010） |
| 7 | selfmedia-tl1 | 自研 | 选题清单 | bridge | `prism-intel` | bridge（MAP-010） |
| 8 | selfmedia-writing | 自研 | 库拾成稿主入口（结构+文笔） | distill | `contracts/writing.contract.md` + `prism-produce/references/prose-core.md` | ✅ 已蒸馏（MAP-005） |
| 9 | selfmedia-humanize | 自研 | 自媒体口语/人味策略 | distill + bridge | `prism-produce/references/humanize-techniques.md` | ✅ 已蒸馏（MAP-005） |
| 10 | humanizer-zh | op7418/Humanizer-zh | 中文终检去痕 | bridge（词表可后 pin） | `prism-qa` anti-slop-gate | bridge（MAP-005） |
| 11 | qu-ai-wei | LifelongLazyLearner/qu-ai-wei | 中文去 AI 味（仲裁树） | bridge + distill 仲裁原则 | `prism-qa` anti-slop-gate（仲裁顺序） | 原则已蒸馏（MAP-005） |
| 12 | shuorenhua | MrGeDiao/shuorenhua | 中英去模板感（Tier/场景） | bridge + distill 场景档位 | `prism-qa` anti-slop-gate（场景档位） | 档位已蒸馏（MAP-005） |
| 13 | no-ai-slop | petergyang/no-ai-slop | 英文最小改写/检测 | bridge | `prism-qa` | bridge（MAP-005） |
| 14 | stop-slop | hardikpandya/stop-slop | 英文去 slop | bridge | `prism-qa` | bridge（MAP-005） |
| 15 | humanizer-en | blader/humanizer | 英文基础去味 | bridge | `prism-qa` | bridge（MAP-005） |
| 16 | de-ai-prompt-enhancer | OUBIGFA/… | 风格样本 + 写作增强 | bridge | `prism-produce` | bridge（MAP-011） |
| 17 | writing-agent | dongbeixiaohuo/writing-agent | 长流程选题→证据→审稿→导出 | bridge（大运行时） | `prism-produce` | bridge（MAP-005） |
| 18 | rnskill | Pluviobyte/rnskill | 洗稿/选题/封面/视频合集 | bridge | `prism-produce` | bridge（MAP-011） |
| 19 | kushi-narrative-zh | 自研 | MASTER → humanized 叙事 | bridge | `prism-produce` novel 子湖 | bridge（MAP-012） |
| 20 | kushi-visual-enrich | 自研 | 视觉 enrich | bridge | `prism-produce` | bridge（MAP-012） |
| 21 | oss-repo-read | 自研 | 仓库研究 | bridge | `prism-intel`/`prism-master` | bridge（MAP-013） |
| 22 | create-content | 自研 | 通用创作入口 | bridge | `prism-produce` | bridge（MAP-013） |
| 23 | analyze-data | 自研 | 数据分析 | bridge | `prism-intel` | bridge（MAP-013） |
| 24 | manage-media | 自研 | 媒体资产管理 | bridge | `prism-produce` | bridge（MAP-014） |
| 25 | character-illustrations | 自研 | 角色插图 | bridge | `prism-produce` AV/贴图 | bridge（MAP-014） |
| 26 | ian-xiaohei-illustrations | 自研 | 插画风格包 | bridge | `prism-produce` AV/贴图 | bridge（MAP-014） |
| 27 | comic-storyboard | 自研 | 漫画分镜 | bridge | `prism-produce` comic | bridge（MAP-007） |
| 28 | openmontage | vendor（AGPL-3.0） | 视频生产入口 | defer | `prism-produce` AV | defer（MAP-007） |
| 29 | selfmedia-account-pipeline | 自研 | 账号管线+贴图渲染 | pin 渲染链 + defer 账号管线 | `prism-produce`（`scripts/render_*.py` + `templates/`，A1 MIT） | ✅ 渲染链已 pin；账号管线 defer（MAP-006） |
| 30 | selfmedia-agent-reach | 自研 | 触达/分发 | bridge | `prism-release` | bridge（MAP-015） |
| 31 | publish-content | 自研 | 发布入口 | bridge | `prism-release` | bridge（MAP-008） |
| 32 | schedule-post | 自研 | 排期 | bridge | `prism-release` | bridge（MAP-008） |
| 33 | x-publish | 自研 | X 发布 | bridge | `prism-release` | bridge（MAP-015） |
| 34 | vendor/human-writing | KKKKhazix/human-writing（MIT） | 说人话层 + 检查脚本 | vendor_pin（脚本/词表） | `scripts/check_human_voice.py` + `human-voice-prose.md` | ✅ 已 pin（MAP-016） |
| 35 | vendor/Jellyfish | Forget-C/Jellyfish | 写作 monorepo | defer（license 评估后） | `vendor/` 候选 | defer（MAP-016） |
| 36 | vendor/OpenMontage | AGPL-3.0 | 视频 monorepo | defer | `vendor/` 候选 | defer（MAP-016） |
| 37 | vendor/book-video | Endless1936/book-video | 书籍视频 monorepo | defer | `vendor/` 候选 | defer（MAP-016） |
| 38 | vendor/writing-agent | dongbeixiaohuo/writing-agent | 长流程 monorepo | bridge | `prism-produce` | bridge（MAP-016） |
| 39 | vendor/rnskill | Pluviobyte/rnskill | 合集 monorepo | bridge | `prism-produce` | bridge（MAP-016） |

## 策略口径

- **distill**：只蒸馏「判断框架/门禁/清单/小脚本」，不进大体量运行时。
- **bridge**：按名调用已安装 skill/脚本，缺失 fail-closed；安装通道见 `scripts/install_bridges.sh`。
- **vendor_pin**：MIT 类小脚本/词表可 pin 进 Prism（带 ATTRIBUTION）；AGPL/大模型权重只 pin 引用不复制。
- **defer**：显式延后，不是软 TODO；goal 不得假装 deferred 能力已存在。

## A4+A5 pin 状态（2026-08-15）

- ✅ **29 个 skill 全部 pin** 进 `vendor/skills/`（20M，A4+A5 · 所有者授权）：
  - 9 个 MIT 上游（humanizer-zh / qu-ai-wei / shuorenhua / no-ai-slop / stop-slop /
    humanizer-en / writing-agent / comic-storyboard / character-illustrations，各随附 LICENSE）
  - 18 个自研逻辑（selfmedia-* / kushi-* / oss-repo-read / analyze-data / create-content /
    manage-media / publish-content / schedule-post / x-publish / selfmedia-agent-reach /
    ian-xiaohei-illustrations 整包含 13M assets）
  - 2 个受限 pin（rnskill 合规层 + 非商业 NOTICE；de-ai-prompt-enhancer + license NOTICE）
- 🔗 **bridge 数量清零**：skill roots 无任何指向源仓的 symlink；
  唯一 archive-only 回源引用 = rnskill 96M skills 子树（CC BY-NC 非商业合规）。
- ATTRIBUTION：`docs/ATTRIBUTION-bridges.md`；守卫：`vendor/skills/{rnskill,de-ai-prompt-enhancer}/NOTICE.md`。

## 替换路线（逐步替换 selfmedia-creator）

1. **D1 写作/人话深蒸馏**（✅ 2026-08-14 完成）：prose-core + human-voice-prose +
   humanize-techniques 进 Prism；`check_human_voice.py` pin 进 `scripts/`；
   写作 bridge 已安装（10 个 × 4 roots）；anydoc 样本已过新门禁复核。
2. **D2–D6 形态**（✅ 2026-08-14：thread / xhs / image-post / vlog 端到端样本 +
   novel 反 slop 审计全部落地，门禁 `scripts/check_form_samples.sh`）；
   剩余：贴图渲染、comic/book_video 成片（bridge deferred，占位明确不假装产出）。
3. **MAP-002**（✅ 2026-08-14 完成）：selfmedia-director treatment/QC 规范已蒸馏进
   `prism-director/references/`。
4. **E/F 支持面**（✅ 2026-08-14）：注册表 `install:` 通道补齐；源仓类 bridge
   （publish/intel/visual/writing 四品类 34 个）已装进 4 个 skill roots，
   门禁 `scripts/check_bridges_installed.sh`；凭证类 bridge 缺失 fail-closed。
5. **License 评估**（✅ 2026-08-14 记录于 migration matrix）：源仓无 LICENSE 文件，
   自研脚本/模板一律不 pin（bridge + 占位）；check-human-voice.py 因上游 MIT 已 pin。
6. **自足性硬化**（✅ 2026-08-14）：`skill-routing.md` Prism-native 重写（移除账号默认）；
   节气养生模板蒸馏进仓（`prism-director/references/jieqi-yangsheng-treatment-template.md`）；
   intel briefing schema 蒸馏进仓（`prism-intel/references/briefing-schema.md`）；
   编排内核账号引用清零（小黑角色 IP / jieqi 账号合同 → 配置驱动）；
   readability 规则蒸馏 + Prism 原生实现（`scripts/check_readability.py`，不 pin 源仓无 license 脚本）；
   门禁 `scripts/check_standalone_distill.sh` 证明蒸馏层无源仓可运行 + bridge 缺失 fail-closed。
   体裁原型全量蒸馏（✅ 2026-08-14）：emotional-essay（7 拍 + 8 硬规则 + 判别开关）、
   oss-daily（倒金字塔）、visual-enrich（截图充实）、reader-tier（新手小白写法）全部进仓，
   `contracts/writing.contract.md` 体裁选型表已接线。
7. **退役（待所有者决策）**：源仓降级为只读 archive、移除 bridge 回源路径，需满足——
   a) ✅ 已完成（2026-08-14）：所有者勾选 A1，渲染脚本族 + templates 以 MIT pin 进
      `scripts/` + `templates/`（ATTRIBUTION：`docs/ATTRIBUTION-render-chain.md`），
      门禁 `scripts/check_render_pin.sh` PASS，image-post 样本已真实渲染 + OCR 核验；
   b) ✅ AV 大栈维持 bridge（B1，OpenMontage AGPL 不 pin）；
   c) ✅ 蒸馏层无源仓可运行（standalone 门禁）；bridge 运行时以归档源仓为宿主（只读）。
   源仓归档标记：`selfmedia-creator/ARCHIVED.md`（2026-08-14）。
