---
name: oss-repo-read
description: |
  深度库拾读源码：从 oss-sync 镜像或 GitHub 只读拉取仓库，产出 repo-digest.md（核心模块、入口、调用关系）。
  供 selfmedia-writing 写 🗺️💎 段。仅 oss-pick-standard；日榜跳过。触发词：读 repo、源码解析、repo-digest、oss-repo-read。
allowed-tools:
  - Read
  - Write
  - Bash
metadata:
  pipeline_step: read-repo
  pipeline_order: after draft, before selfmedia-writing
  pairs_with: [selfmedia-writing, manage-oss-sync]
---

# 读开源仓库（oss-repo-read）

你是库拾的**源码导读员**。目标读者是**新手小白**——他们没读过这个仓库，你要帮后续成稿 skill 抓住「3～5 个核心模块/函数」和主流程，而不是堆目录树。

## 何时使用

- `pipeline: oss-pick-standard` 深度稿，在 `selfmedia-writing` **之前**
- `meta.yaml` 含 `source_repo` 或 `repo_url`
- 用户要求「看透代码」「架构主流程」「设计亮点要有依据」

**日榜 `oss-pick-daily` 不跑本 skill。**

## 输入

| 文件 | 用途 |
|------|------|
| `content/masters/{vertical}/{slug}/meta.yaml` | `source_repo`, `oss_sync_path`, `repo_url` |
| `content/sources/{vertical}/{slug}/notes.md` | 选题背景（可选） |
| `content/masters/{vertical}/{slug}/MASTER.md` | 已定稿方向（可选） |

## 输出

**权威落盘：** `content/sources/{vertical}/{slug}/repo-digest.md`

结构固定：

```markdown
# Repo Digest — {slug}

- repo: {owner/repo}
- digest_at: {ISO8601}
- mirror_path: {path or unknown}

## 顶层结构（≤15 行）

## 核心模块（3～5 个）

每个模块：名称、文件路径、一句话职责、谁调用谁（主动语态一句）

## 主流程（输入→输出）

极简列表或 5 步以内

## 值得写进 💎 的代码点（≥2）

文件路径 + 设计意图 + 好处（内存/并发/可维护…）

## 读源码时的坑 / 局限线索（供 ⚠️ 段）

## 未读 / 未确认（诚实标注）
```

## 执行步骤

### 1. 定位本地镜像（优先）

```bash
python3 ~/.codex/skills/manage-oss-sync/scripts/manage_oss_sync.py show owner/repo --json
```

从 JSON 取 `local_path` 或 `path`。若无镜像：

```bash
scripts/lib/oss-repo-digest.sh --slug {slug} --vertical oss-picks
```

脚本会尝试 oss-sync 索引 + 常见 `~/oss-sync` 路径；仍失败则 **只读** `git clone --depth 1` 到 `/tmp/oss-repo-read/{slug}`（用完可删）。

### 2. 读什么（剥冗余）

优先顺序：

1. `README.md` / `docs/` 索引页（建立地图，不当正文）
2. `package.json` / `pyproject.toml` / `go.mod` → 找 `main`、CLI 入口
3. `src/` 或包根下 **入口文件**（`index.ts`, `cli.ts`, `main.py`…）
4. 与 README「核心概念」对应的 **2～4 个实现文件**（各读前 80～120 行）
5. **不要**通读全仓；未读文件写入「未读 / 未确认」

### 3. 写 digest（小白可跟）

- 模块名用白话 + 括号附英文/路径
- 调用关系用主动语态：「CLI 解析参数后调用 `applyChange()`」
- 禁止编造未在文件中出现的函数名
- 每个 💎 线索必须带 **文件路径**

### 4. 证据

深度稿 humanize evidence 须含：

```json
{ "id": "read-repo", "skill": "oss-repo-read", "output_path": "content/sources/oss-picks/{slug}/repo-digest.md" }
```

## 禁止

- 日榜跑本 skill
- 无 digest 直接进入 `selfmedia-writing` 深度四段式
- 把 digest 整段粘贴进 `humanized.md`（只作写作依据）

## 示例

```text
/oss-repo-read openspec 深度库拾，产出 repo-digest.md
```
