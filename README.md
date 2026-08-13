# Prism（棱镜）

独立内容营销创作 agent skill 仓。与 Beacon 设计理念对齐；能力来自 selfmedia-creator 提取编排。

> Lake B 立项仓 · 源映射见 Source Skill Inventory（selfmedia-creator v0.0.6 prism-canon-v1 R3）

## Lake B 交付物（v0.0.1）

- 公开面：`skills/prism-{goal,intel,master,director,produce,qa,release}/SKILL.md`
- 注册表：`registry/public-surface.yaml` · `registry/adapter-index.yaml`
- 契约：`contracts/skill-contract-7seg.tpl.md` · `contracts/human-card.md`
- 编排内核：`skills/_internal/orchestration/`
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
