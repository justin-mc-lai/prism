# 视觉充实（visual-enrich · Prism 蒸馏版）

> Internal reference for `prism-produce`. Not host-discoverable.
> 蒸馏自 selfmedia-creator `skills/kushi-visual-enrich/`（自研）。
> 定位：深度稿（oss-pick-standard）必须做视觉充实；日榜通常只需封面。

## 管线位置

```text
叙事稿 → visual-enrich（截图 + 图说）→ humanize 终检 → render
```

## 截图来源优先级

1. **项目官方文档站**（`docs.xxx.com`、README 里的 Documentation 链接）
2. **项目官网**
3. **GitHub 仓库页**（无独立文档/官网时）

同一项目可组合多张，但每张图要有 **distinct 目的**。

## 深度稿推荐截图清单

| 优先级 | 目标页面 | 图说作用 |
|--------|----------|----------|
| P0 | GitHub 仓库顶栏（star、简介、目录） | 建立信任：有多人 star、项目活跃 |
| P0 | 官方文档核心页（workflow / quickstart） | 帮读者建立全局心智模型 |
| P1 | README 首屏（How it works 段） | 与作者原话对齐，减少误解 |
| P2 | 本机实操（安装后运行效果） | 证明「装完真的会变」 |

**禁止**：长期只用 GitHub OG 社交预览图糊弄；`picsum` 占位不得进发布稿（占位必须显式标注「待 enrich」）。

## 执行步骤

1. **解析链接**：从 `meta.yaml` / `MASTER.md` / `notes.md` 提取 `repo_url`、`homepage`、`documentation`。
2. **截图**：保存到 `content/masters/{vertical}/{slug}/assets/`；宽度约 1200px，PNG。
3. **更新 manifest**：

```yaml
assets:
  - id: github-repo-header
    file: github-repo-header.png
    kind: screenshot
    source: https://github.com/owner/repo
    captured_at: "YYYY-MM-DD"
    alt: 仓库顶栏：star 数、简介与目录结构
```

4. **插入 humanized.md**：图放在读者需要「停一下、建立画面」的位置，不是堆在文末；
   图说必须**引导阅读**（「从图里先看什么、再读哪一节」），不写「截图如下」。

## 自检

- [ ] 深度稿 ≥2 张一手截图（仓库顶栏 + 文档核心页优先）
- [ ] 每张图有 distinct 目的，图说引导阅读
- [ ] manifest 含 source + captured_at + alt
- [ ] 无 OG 糊弄、无 picsum、无未标注占位
