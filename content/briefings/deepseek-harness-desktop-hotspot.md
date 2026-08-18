# Intel Briefing — deepseek-harness-desktop（2026-08-16）

- mode_id: brief-intel
- public_id: intel
- lane: standard
- recommended_next_harness: master
- map_ids_considered: ['MAP-003']
- 来源: GitHub Search API（created > 2026-07-25 · sort=stars · 检索时间 2026-08-16）

## 热点结论

`anywhere-labs/deepseek-harness-desktop` 为 2026-08-13 新建仓库，检索时刻 **6,593 stars /
289 forks / 88 open issues**，TypeScript 实现，MIT 协议。
定位：把官方 DeepSeek Harness（DSH）的本地 Web UI 装进 macOS / Windows 原生桌面应用，
自动启动和管理本地 Harness 服务，普通用户无需安装 Node.js 或执行命令。

## 选题角度

面向新手小白与内容创作者的科普角度：**“不装 Node.js、不敲命令，装个 App 就用上 DeepSeek Harness”**。
信息差点：大多数人不知道 DSH 还有桌面封装；README 明确标注插件市场、手机远程、Channels
仍为路线图，成稿必须区分“已交付”和“规划中”。

## 证据

- `https://api.github.com/repos/anywhere-labs/deepseek-harness-desktop`（元数据，检索时刻 2026-08-16）
- README.md（主要功能 / 插件生态 / 与官方关系，158 行）
- docs/user-guide.md（安装 / 首次启动 / profile / 插件管理 / 更新）
- docs/architecture.md（Electron 宿主 + Host + loopback carrier）
- docs/why-desktop.md（定位与刻意不做什么）
- releases API（v2.0.0，2026-08-15）
- 风险提示：star 数会随时间变化，成稿须标注“检索时刻”；未做本地安装实测。
