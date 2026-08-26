# FactMaster: deepseek-harness-desktop

> kind: fact · pipeline: oss-pick-standard · 检索时刻: 2026-08-16

## 一句话

DeepSeek Harness Desktop（DSH Desktop）是一个把官方 DeepSeek Harness 的本地 Web UI
装进 macOS / Windows 原生桌面应用的社区项目。应用自动启动并管理本地 Harness 服务，
集成系统托盘与桌面窗口，普通用户不需要安装 Node.js 或执行命令。

## 来源（source_refs）

- 仓库: `https://github.com/anywhere-labs/deepseek-harness-desktop`（default branch: master）
- 元数据: GitHub API `repos/anywhere-labs/deepseek-harness-desktop`（检索时刻 2026-08-16）
- README: 仓库 README.md（158 行，检索时刻 2026-08-16）
- 文档: docs/why-desktop.md、docs/user-guide.md、docs/architecture.md（检索时刻 2026-08-16）
- 插件包: dsh-plugin-desktop/README.md（检索时刻 2026-08-16）
- Releases: GitHub API `releases`（v2.0.0，2026-08-15）

## Canonical claims（每条带来源）

| # | 事实 | 来源 |
|---|------|------|
| 1 | 定位：为 DeepSeek Harness 生态打造的现代桌面端体验，把官方 DSH 的本地 Web UI 带到原生桌面 | README 主要功能 Desktop |
| 2 | 应用自动启动和管理本地 Harness 服务，集成系统托盘与桌面窗口，用户无需安装 Node.js 或执行命令 | README 主要功能 Desktop |
| 3 | 支持平台：macOS 与 Windows（README badges；Linux 仅兼容模式，见用户指南模式节） | README 徽标 + docs/user-guide.md |
| 4 | 基于 deepseek-ai/deepseek-harness 构建；agent、模型、工具、会话、Web UI 和插件生态来自上游项目 | README 与官方项目的关系 |
| 5 | 是社区桌面版，不是 DeepSeek 官方产品 | README License 免责声明 |
| 6 | 仓库创建于 2026-08-13，检索时刻 6,593 stars / 289 forks / 88 open issues | GitHub API |
| 7 | 语言 TypeScript，协议 MIT | GitHub API license.spdx_id |
| 8 | 两个公开插件接口：desktopProfiles（查看/切换 profile）与 desktopPnpm（安装/更新/移除插件） | README 插件生态 |
| 9 | 兼容模式保留官方默认 Web client 与 profile 自己的布局；高级模式加入桌面自有 frame、布局、Mica/vibrancy 与原生拖动区域 | docs/user-guide.md 兼容模式与高级模式 |
| 10 | 首次启动准备默认 profile，并在本机启动官方 DSH Web surface；关闭窗口通常只隐藏，托盘退出才结束应用和 Host 进程 | docs/user-guide.md 安装与首次启动 |
| 11 | 插件管理沿用官方 CLI：`dsh plugin --profile desktop add/remove/update`；插件变更后需重启应用 | docs/user-guide.md 插件管理 |
| 12 | 托盘打开 DSH 终端时，应用在 user-data 目录生成 dsh/pnpm/node 私有 shim，只对该终端进程设置 PATH，不修改系统 PATH | docs/user-guide.md 打开终端 |
| 13 | 插件市场、手机远程控制、Channels 在 README 中标注“即将推出”，不属于当前安装包已交付功能 | README 主要功能表 + 插件生态 |
| 14 | 最新 release v2.0.0 发布于 2026-08-15 | GitHub releases API |
| 15 | 更新检查：后台请求 dshdesktop.cn/api/desktop/version；仅当服务端版本严格更高时才询问下载，用户确认后才请求固定下载地址 | docs/user-guide.md 更新 |
| 16 | 架构：Electron main 进程启动官方 DSH Host，Host 通过 loopback HTTP/WebSocket 提供 Web UI；页面不直接调用 Electron API | docs/architecture.md 总览 |

## 不确定性标注

- star/forks 为检索时刻快照（2026-08-16），会随时间变化。
- 未在本机安装实测；安装、profile、插件行为均来自 README 与官方文档描述。
- 插件市场、手机远程、Channels 为路线图功能，成稿不得写成已交付。
- “无需安装 Node.js”指普通用户日常使用；插件管理仍使用 `dsh` 命令（应用内置终端）。

## 禁止改写

- 不得把社区桌面版写成 DeepSeek 官方产品。
- 不得把路线图功能（插件市场、手机远程、Channels）写成当前版本已提供。
- 不得声称“完全不需要命令行”；应用内置终端与 dsh 命令仍是插件管理入口。
- 不得把 README 徽标中的“即将推出”状态写成已发布。
