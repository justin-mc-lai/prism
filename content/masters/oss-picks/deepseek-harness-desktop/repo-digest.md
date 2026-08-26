# repo-digest: anywhere-labs/deepseek-harness-desktop

> 检索时刻: 2026-08-16 · 来源: GitHub API + README.md + docs/ + dsh-plugin-desktop/README.md

## 仓库速览

- 仓库: https://github.com/anywhere-labs/deepseek-harness-desktop（default branch: master）
- 创建: 2026-08-13 · 检索时刻: 6,593 stars / 289 forks / 88 open issues
- 语言: TypeScript · 协议: MIT · 官网: dshdesktop.cn（README 主下载入口 deepseekdesktop.com）
- 定位: 把官方 DeepSeek Harness 的本地 Web UI 打包成 macOS / Windows 原生桌面应用

## 主流程

1. 用户安装并打开 DSH Desktop，Electron 获取单实例锁并读取当前 profile。
2. Launcher 准备激活的 profile，启动官方 DSH Host（Electron main 进程内）。
3. Host 绑定 127.0.0.1 的 HTTP/WebSocket，官方 Web carrier 组合 dsh-base 与 dsh-web-app。
4. Electron BrowserWindow 加载同源沙箱页面；Web surface 加载成功后才创建托盘并提交
   last-known-good profile 状态。
5. 关闭窗口只隐藏；托盘退出才结束应用与 Host 进程。profile/模式切换通过有序重启生效。

## 核心模块

| 模块 | 入口 | 说明 |
|------|------|------|
| Electron 宿主 | `dsh-plugin-desktop` 可执行文件 | 窗口、托盘、单实例、关闭即隐藏生命周期 |
| Launcher / profile | `desktop-profiles` | 激活与切换 profile，切换先记 pending 再重启 |
| 官方 DSH Host | 上游 deepseek-harness | agent、模型、工具、会话、Web 服务 |
| desktopProfiles 服务 | `dsh-plugin-desktop/profile-service` | 第三方插件的公开 contract：查看/切换 profile |
| desktopPnpm 服务 | `dsh-plugin-desktop/pnpm` | 第三方插件的公开 contract：安装/更新/移除插件 |
| desktop-terminal / desktop-updates | `desktop-shell` 子 row | 内置终端与后台版本检查 |

## 坑/局限线索

- Linux 仅兼容模式，不提供高级模式（README 模式节）
- 插件市场、手机远程、Channels 为路线图，非当前版本功能
- 插件变更后需要重启应用，bundle 才会进入 Loader 组合
- 第三方插件不能直接控制 BrowserWindow、托盘、Electron IPC 或安装器私有路径
- 未做本地安装实测，行为描述以 README 与官方文档为准

## 可写进 💎 的点

- 公开接口收敛为两个 service，插件边界清晰，升级排错更稳
- profile 切换 last-known-good 回滚，启动失败回到上一次可用配置
- 私有 PATH shim 只作用于 Desktop 终端，不污染系统 shell 配置
