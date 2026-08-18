---
name: kushi-visual-enrich
description: |
  库拾母版视觉充实：为 oss-pick 深度稿抓取官网/文档站/GitHub 截图，写入 assets/ 并在 humanized.md 中插入图说。
  优先一手页面截图，引导读者「先看图再读文」。与 kushi-narrative-zh、humanizer-zh 串联使用。
triggers:
  - pattern: "库拾截图|visual-enrich|充实配图"
  - pattern: "assets/manifest"
allowed-tools:
  - Read
  - Write
  - Edit
  - Shell
  - Grep
  - Glob
metadata:
  pipeline_step: enrich-visual
  pipeline_order: after kushi-narrative-zh, before humanizer-zh
  pairs_with: [kushi-narrative-zh, web-access]
  authority: content/masters/_template/MASTER-SPEC.md
---

# kushi-visual-enrich：母版视觉充实

## 何时使用

- `humanized.md` 叙事稿已写好，需要**截图 + 图说**降低阅读门槛
- 新建 `content/masters/{vertical}/{slug}/assets/` 素材
- 日榜通常只需封面；**深度稿（oss-pick-standard）必须做视觉充实**

## 管线位置

```text
kushi-narrative-zh → kushi-visual-enrich → humanizer-zh → render
```

## 截图来源优先级

1. **项目官方文档站**（如 `*.mintlify.app`、`docs.xxx.com`、README 里的 Documentation 链接）
2. **项目官网**（如 `primeradiant.com/superpowers`）
3. **GitHub 仓库页**（无独立文档/官网时）

同一项目可组合多张，但每张图要有** distinct 目的**（见下表）。

## 深度稿推荐截图清单

| 优先级 | 目标页面 | 文件名建议 | 图说作用 |
|--------|----------|------------|----------|
| P0 | GitHub 仓库顶栏（star、简介、目录） | `github-repo-header.png` | 建立信任：有多人 star、项目活跃 |
| P0 | 官方文档核心页（workflow / quickstart） | `docs-workflow.png` | 帮读者建立全局心智模型 |
| P1 | README 首屏（How it works 段） | `github-readme-intro.png` | 与作者原话对齐，减少误解 |
| P2 | 本机实操（安装后对话） | `workflow-screenshot.png` | 证明「装完真的会变」 |

**禁止**：长期只用 GitHub OG 社交预览图糊弄；`picsum` 占位不得进发布稿。

## 执行步骤

### 1. 解析链接

从 `meta.yaml`、`MASTER.md`、`notes.md`、上游 README 提取：

- `repo_url` / `source_repo`
- `homepage`、`documentation`（GitHub About 或 README）
- oss-sync 本地副本路径（可选）

### 2. 打开页面并截图

优先加载 **`web-access`** skill：

- 微信、需登录态：Chrome CDP（`check-deps.mjs` → Proxy `/new` → `/screenshot`）
- GitHub、Mintlify 文档：CDP 或 Cursor browser 均可
- 截图保存到 `content/masters/{vertical}/{slug}/assets/`
- 宽度建议 1200px 左右，PNG 格式

```bash
# 示例：web-access Proxy
curl -s "http://localhost:3456/new?url=https://github.com/owner/repo"
curl -s "http://localhost:3456/screenshot?target=ID&file=/path/to/assets/github-repo-header.png"
```

### 3. 更新 manifest.yaml

每个 slug 目录维护 `assets/manifest.yaml`：

```yaml
assets:
  - id: github-repo-header
    file: github-repo-header.png
    kind: screenshot
    source: https://github.com/owner/repo
    captured_at: "2026-06-18"
    alt: 仓库顶栏：star 数、简介与目录结构
```

### 4. 插入 humanized.md

**写法参考**（逛逛 GitHub 类公众号）：图放在**读者需要「停一下、建立画面」**的位置，不是堆在文末。

```markdown
## 先带你看一眼仓库

![Superpowers GitHub 仓库：23 万 star，skills 与多端插件目录一目了然](assets/github-repo-header.png)

上图能看到几件事：star 已经到 …；目录里有 `skills/` 和 `.claude-plugin`、`.codex-plugin`、`.cursor-plugin` 等——说明它从设计上就是多端插件，不是某个 IDE 专属。

![官方文档里的七步工作流总览](assets/docs-workflow.png)

文档站把流程画成一张图。后文按这个顺序讲，你对照图读会轻松很多。
```

图说必须**引导阅读**：告诉读者「从图里先看什么、再读哪一节」，而不是「截图如下」。

### 5. 自检

见 `references/checklist.md`。

## 与 kushi-narrative-zh 的分工

| | kushi-narrative-zh | kushi-visual-enrich |
|---|-------------------|---------------------|
| 输出 | 叙事 prose 结构 | assets/ + 图说插入 |
| 体裁参考 | 连贯科普文 | 逛逛 GitHub 类「场景 + 配图锚点」 |

## 参考样稿

- `content/masters/oss-picks/superpowers/humanized.md`
- `content/masters/oss-picks/superpowers/assets/manifest.yaml`
