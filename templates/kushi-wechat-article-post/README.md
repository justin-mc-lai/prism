# 库拾微信整文贴图模板

暖纸底长文 HTML → Playwright 分页截图（1080×1440）。  
这是 `kushi-gzh` 深度 OSS 贴图的默认视觉（`kushi-article-paper-portrait`）。

## 稳定入口（推荐）

```bash
scripts/kushi_wechat_article_image_post.sh \
  --slug <slug> \
  --version v1 \
  --markdown content/renders/kushi-gzh/wechat-gzh/<slug>.md \
  --title '二十字内标题' \
  --source-label github.com/org/repo \
  --cover punk-assets/punk-cover/<slug>-wechat-gzh-image-post-v1/cover.jpg \
  --diagrams content/presentations/oss-picks/<slug>/wechat-gzh-image-post-v1/diagrams.yaml
```

## 底层渲染

```bash
python3 scripts/render_wechat_article_pages.py \
  --markdown content/renders/kushi-gzh/wechat-gzh/<slug>.md \
  --output-dir content/renders/kushi-gzh/wechat-gzh/assets/<slug>-vN \
  --html-out content/presentations/.../html/article.html \
  --source-label github.com/org/repo \
  --diagrams content/presentations/.../diagrams.yaml \
  --diagrams-dir content/presentations/.../diagrams \
  --start-index 2 \
  --total-with-cover \
  --manifest .../assets/manifest.yaml
```

封面（punk 等）放到 `01-cover.jpg`。正文页从 `--start-index` 起编号。

## diagrams.yaml

可选。不提供则只排文字，不插入任何流程图。

```yaml
injections:
  - id: sprint-flow
    match_all: ["/office-hours"]
    file: sprint-flow.svg
    title: "Sprint 主链"
  - id: usage-loop
    match_any: ["真浏览器"]
    file: usage-loop.svg
    title: "装载到行动"
    append_if_unmatched: true
```

SVG 先查 presentation 的 `diagrams/`，再回退到本模板 `diagrams/`。

## 分页硬规则

- 用整页 `full_page` 截图再按块边界裁切，禁止仅靠 `scrollY` 视口截图（末页会钳制重叠）。
- 块边界优先不切断段落 / figure。
- 页脚写 source-label 与 `n/N`（含封面时用 `--total-with-cover`）。

## 代码块

Markdown 里用 ``` ```bash ``` 围栏的代码会渲染成独立 `.code-block`（暖纸底、左侧橙色边线、`bash` 语言标签、整块不跨页）。行内 `code` 保留浅底圆角样式。

## 正文组件（callout / stat / compare）

渲染器支持三种组件块，语法与代码块一样是显式围栏，整块不跨页：

```text
:::callout warning Windows 注意
Windows 还要 Node.js；无 Dev Mode 时每次 git pull 后必须重跑 ./setup。
:::

:::stat 59
SKILL.md 数量
克隆里数到 59 个；README 营销口径写 23 个专家角色。
:::

:::compare
| 营销口径 | 克隆核对 |
| --- | --- |
| 23 个专家角色 | 59 个 SKILL.md |
| 只能 Claude Code | 10+ host，./setup --host codex |
:::
```

- `callout` 类型：note / warning / danger / ok / tip；第一行 `:::callout <type> <标题>`。
- `stat`：第一行 `:::stat <大数字>`，第二行标签，其余为说明。
- `compare`：两列表格，第一行为表头，支持 `| --- |` 分隔行。

## 文件

- `css/article.css` — 暖纸底、衬线正文、行距
- `diagrams/*.svg` — 可复用图元；选题专用图放 presentation `diagrams/`
