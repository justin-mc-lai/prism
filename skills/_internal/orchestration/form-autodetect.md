# Form Auto-Detect（classify_form 操作表）

> 确定性关键词 → form 映射。在 goal `classify_lane` 之后、`route_next_public_surface` 之前执行。
> 结果记入 machine face `form_detected`。表只增不改语义；新形态 = form registry + 本表各加一行。

## 映射表

| 触发词（命中即候选） | form |
|---|---|
| 小说, 连载, 章节, episode, 正文更新 | novel |
| vlog, 口播, 出镜, 视频稿 | vlog |
| 博客, 长文, 深度文章, 公众号文章 | blog |
| thread, 推文, 推特串, X 连发 | thread |
| 小红书, 种草图文, xhs | xhs |
| 贴图, 配图, image post, 图文集 | image-post |
| 漫画, comic | comic |
| 漫剧, 动态漫, manga drama | manga_drama |
| 短剧, 真人短剧, 分集剧本实拍, live drama | live_drama |
| 书籍视频, 讲书, book video, 书单视频 | book_video |
| 商品, 产品, 带货, 电商, 好物, 测评, 开箱 | product |

## 裁决规则

1. 显式指定优先：campaign 已声明 form 或用户点名形态 → 直接用，不跑本表。
2. 命中唯一 → 该 form。
3. 命中多个或零个 → human card 列候选请用户定，**禁止静默猜测**（fail-closed）。
4. 判定结果必须写入 machine face：

```yaml
mode_id: loop-campaign
form_detected: product
form_detect_source: explicit|keyword|human
```

## 边界

- classify_form 只选形态路由，不改变 lane（fast/standard/canon）语义。
- 不新增公开面；本表属 `_internal/orchestration/`，不对人暴露名字。
