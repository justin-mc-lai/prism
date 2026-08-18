# 库拾内容创作流水线（权威）

> **Authority：** 与 `content/masters/_template/MASTER-SPEC.md` 互为引用。  
> **Gold 深度样稿：** `content/masters/oss-picks/openspec/humanized.md`  
> **Gold 日榜样稿：** `content/masters/oss-picks/daily-2026-06-22/humanized.md`

## 1. 两条管线

| Pipeline | 读者 | 读 repo | 成稿结构 |
|----------|------|---------|----------|
| `oss-pick-standard` | 新手小白 | **必须** `repo-digest.md` | MVP + 由简入深 + 四段式 |
| `oss-pick-daily` | 新手小白 | 跳过 | 日榜倒金字塔（无四段 emoji） |

注册：`content/registry.yaml`、`content/pipelines/*.yaml`。

## 2. 深度管线步骤（oss-pick-standard）

```text
notes.md
  → create-content 起草 MASTER.md
  → oss-repo-read → sources/{vertical}/{slug}/repo-digest.md
  → selfmedia-writing → humanized.md（初稿）
  → kushi-visual-enrich → assets/ + 图说
  → humanizer-zh → humanized.md（终稿）
  → render-channel.sh → renders/
  → publish-content → published-track
```

| Step | Skill / 脚本 | 产出 |
|------|----------------|------|
| source | oss-pick / notes | `content/sources/.../notes.md` |
| draft | create-content | `MASTER.md` + `meta.yaml` |
| read-repo | oss-repo-read | `repo-digest.md` |
| narrate | selfmedia-writing | `humanized.md` |
| enrich-visual | kushi-visual-enrich | `assets/*.png` + manifest |
| humanize | humanizer-zh | `humanized.md` 终检 |
| render | render-channel.sh | `renders/{account}/{platform}/{slug}.md` |

**禁止：** `humanize_oss_pick_batch.py` 等 dev 脚本直写生产 `humanized.md`。

## 3. 深度 humanized.md 章节顺序（固定）

1. H1 + `> 库拾一句话` + 元信息行
2. **场景开场**（痛点，≥80 字）
3. **🚀 小白 MVP** — 可复制命令 + 跑通检查清单 + 三句口诀
4. **📖 由简入深怎么读** — 3 分钟 / 10 分钟 / 进阶 / 选型 阅读表
5. **先带你看一眼** — ≥2 张截图 + 图说（enrich 后插入）
6. **🎯 一句话看透本质**
7. **🗺️ 核心架构与主流程** — 先「小白层」白话三步，再「进阶」模块表（依据 repo-digest）
8. **💎 绝妙的设计亮点** — ≥2 点；段首注明「看不懂可先跳过」
9. **⚠️ 潜在坑点与局限性** — 含不适合场景
10. **对比 / 选型**（可选一张表）
11. **接下来你可以** — 行动项

细则：`oss-depth-beginner-archetype.md`。

## 4. MASTER.md 编辑提纲（深度）

母版是 humanize 输入，须包含：

- 速览（slug、pipeline、读者）
- **小白 MVP 要点**（安装命令、slash/示例、跑通标志）
- **由简入深阅读路径**（表格）
- 主体要点（供展开四段式）
- 对比与收尾要点

模板：`content/masters/_template/oss-picks-depth.tpl.md`。

## 5. 门禁（`humanize_gate: required` + `content_spec: r11`）

深度 slug 在 `meta.yaml` 声明 `humanize_gate: required` 时：

1. `readability-lint.py humanized.md --depth`（四段 + MVP + 由简入深）
2. `verify-humanize-evidence.py`（四步：read-repo / narrate / enrich / humanize）
3. `render-channel.sh` 自动对 `pipeline: oss-pick-standard` 加 `--depth`

Evidence 路径：`.beacon/evidence/selfmedia-creator-v001/humanize/{slug}.json`

## 6. Agent 调用速查

```text
/oss-repo-read {slug}
/selfmedia-writing {slug} 深度成稿，新手小白
/kushi-visual-enrich {slug}
/humanizer-zh content/masters/oss-picks/{slug}/humanized.md
python3 scripts/lib/readability-lint.py .../humanized.md --depth
python3 scripts/lib/record-humanize-evidence.py --slug {slug} --pipeline oss-pick-standard --lint-passed
```
