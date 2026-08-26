# Prism（棱镜）

独立内容营销创作 agent skill 仓。与 Beacon 设计理念对齐；能力来自 selfmedia-creator 提取编排。

> Lake B 立项仓 · 源映射见 Source Skill Inventory（selfmedia-creator v0.0.6 prism-canon-v1 R3）

## Lake B 交付物（v0.0.1）

- 公开面：`skills/prism-{goal,intel,master,director,produce,qa,release}/SKILL.md`
- 注册表：`registry/public-surface.yaml` · `registry/adapter-index.yaml`
- 契约：`contracts/skill-contract-7seg.tpl.md` · `contracts/human-card.md`
- 编排内核：`skills/_internal/orchestration/`
- 选题雷达（intel 侧）：`skills/prism-intel/references/topic-radar.md`
  （跨期闭环，学→做→反；2026-08-19 蒸馏自 star23/content-os MIT）
- 宪法：`docs/beacon/v0.0.1/constitution/`
- 需求包：`docs/beacon/v0.0.1/features/prism-extract-v1/`

源冻结：`selfmedia-creator` · `prism-canon-v1` R3。形态生产链在 Lake D，不在本湖。

## 安装到 agent

把 7 个公开面软链到 Codex / Claude / agents / Cursor 的 skill 目录
（`skills/_internal/**` 永不暴露）：

```bash
bash scripts/install_public_surfaces.sh            # 安装（幂等）
bash scripts/install_public_surfaces.sh --dry-run  # 预演
bash scripts/install_public_surfaces.sh --uninstall # 卸载
```

新链接在 agent 下次会话 / reload 后生效。

## 写作 / 人话能力（Lake B′ 深蒸馏）

- 已蒸馏进仓：`skills/prism-produce/references/prose-core.md`（文笔底线）、
  `skills/prism-produce/references/human-voice-prose.md`（说人话层三道门）、
  `skills/prism-produce/references/humanize-techniques.md`（人味手法）、
  `skills/prism-produce/references/personal-style-layer.md`（个人文风层：WRITING.md + 修改学习 + 作者信息密度，2026-08-17 情报吸收）、
  `content/writing-style.md`（个人文风说明书冷启动草稿 draft v0.1，作者复核后转 canonical）、
  `skills/prism-qa/references/anti-slop-gate.md`（30+ 模式 + 场景档位 + 仲裁顺序）。
- 导演层（MAP-002 已蒸馏）：`skills/prism-director/references/director-philosophy.md`（意图第一性）、
  `treatment-template.md`（treatment 模板）、`qc-scorecard.md`（13 维评分卡）。
- 端到端样本（thread / xhs，复用冻结母稿）：`content/presentations/oss-picks/anydoc/{thread-launch,xhs-beginner}/`。
- 端到端样本（image-post 贴图包 / vlog 口播 / novel 审计）：
  `content/presentations/oss-picks/anydoc/{image-post-beginner,vlog-beginner}/` +
  `content/storyworlds/anti-slop-audit-2026-08-14.md`。
- 确定性检查：`python3 scripts/check_human_voice.py <稿>`（MIT 归属，见文件头）。
- 可读性检查（Prism 原生实现，规则蒸馏自源仓 readability-lint）：
  `python3 scripts/check_readability.py <稿> [--depth]`。
- 写作 bridge（10 个，fail-closed）安装：

```bash
bash scripts/install_writing_bridges.sh            # 从 selfmedia-creator 安装（幂等）
bash scripts/install_writing_bridges.sh --dry-run  # 预演
bash scripts/install_writing_bridges.sh --uninstall # 卸载
```

- bridge 已清零（29 个 skill 全部 pin 进 `vendor/skills/`）：

```bash
bash scripts/check_bridges_installed.sh            # 校验 29 pin + 零源仓链接
```

> 源仓已于 2026-08-14 归档为只读 archive（`selfmedia-creator/ARCHIVED.md`）；
> 渲染链已 A1 MIT pin 进本仓（`scripts/render_*.py` + `templates/`，见
> `docs/ATTRIBUTION-render-chain.md`）；29 个 skill 已 A4+A5 pin 进 `vendor/skills/`
> （`docs/ATTRIBUTION-bridges.md`），bridge 清零；唯一 archive-only 回源引用 =
> rnskill 96M skills 子树（CC BY-NC 非商业合规，见 `vendor/skills/rnskill/NOTICE.md`）。

- 源仓能力全量盘点与替换路线：`registry/source-capability-inventory.md`；
  迁移矩阵：`registry/adapter-migration-matrix.md`（MAP-001…016，含 license 评估表）；
  退役决策入口：`docs/owner-license-decision.md`。

## 库拾 OSS-picks 成稿流程

新增一篇库拾（GitHub 开源库科普）文章的现行流程：

1. 选题（intel）：写 `content/briefings/<slug>-hotspot.md`，只收录有 GitHub API /
   README / 官方文档证据的结论，并标注检索时刻。
2. 定母稿（master）：在 `content/masters/oss-picks/<slug>/` 写 `meta.yaml` +
   `MASTER.md`（Canonical claims 逐条带来源）+ `repo-digest.md`。
3. 成稿（produce）：按 `vendor/skills/selfmedia-writing` 深度稿结构产出
   `humanized.md`（场景开场 + 🚀 小白 MVP + 📖 由简入深 + 🎯🗺️💎⚠️ 四段）。
4. 验收（qa）：跑确定性门禁，失败项清零：

   ```bash
   python3 scripts/check_human_voice.py content/masters/oss-picks/<slug>/humanized.md
   python3 scripts/check_readability.py content/masters/oss-picks/<slug>/humanized.md --depth
   ```

5. 后续：`kushi-visual-enrich` 补截图 → `humanizer-zh` 终检 →
   `render-channel.sh` 渲染；公开发布走 `prism-release`，必须人工批准。

示例：`content/masters/oss-picks/deepseek-harness-desktop/`（2026-08-16 新增，draft）。
