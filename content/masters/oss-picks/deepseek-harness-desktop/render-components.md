# Render components（渲染层专用，不进入 humanized.md）

供 `render-channel.sh` / `render_wechat_article_pages.py` 阶段插入，替代长表格与纯文本段。
以下 `:::` 组件含冒号语法，会被人话检查器标记，因此只放在渲染层。

```text
:::stat 6,593
3 天 star
8 月 13 日建仓，8 月 15 日发布 v2.0.0，检索时刻 6,593 stars / 289 forks。
:::

:::compare
| 场景 | 选谁 | 为什么 |
| --- | --- | --- |
| 想快速体验 DSH | 桌面版 | 不用 Node.js，双击即用 |
| 想写插件、深度定制 | 官方 CLI | 公开接口只有 desktopProfiles / desktopPnpm |
| 生产环境、重要工作 | 先别依赖社区版 | 更新快、边界未定、非官方 |
:::

:::callout warning 社区版边界
它是社区桌面版，不是 DeepSeek 官方产品。插件市场、手机远程、Channels 仍是路线图，安装包里还没有这些入口。
:::
```
