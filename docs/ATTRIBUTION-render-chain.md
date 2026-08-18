# ATTRIBUTION — 贴图渲染链（MIT · A1 授权）

> 授权依据：`docs/owner-license-decision.md`（2026-08-14 · human 勾选 A1）。
> 以下脚本与模板由 Prism 所有者（selfmedia-creator 源仓，无独立 LICENSE 文件）以 MIT
> 许可授权本仓再分发。源仓保持只读 archive 状态。

## Pinned scripts（源仓 → Prism）

| 源仓路径 | Prism 落点 |
|---|---|
| `scripts/render_wechat_html_cards.py` | `scripts/render_wechat_html_cards.py` |
| `scripts/render_wechat_image_cards.py` | `scripts/render_wechat_image_cards.py` |
| `scripts/render_wechat_article_pages.py` | `scripts/render_wechat_article_pages.py` |
| `scripts/render_spec_kit_wechat_cards.py` | `scripts/render_spec_kit_wechat_cards.py` |
| `scripts/render_superpowers_wechat_cards.py` | `scripts/render_superpowers_wechat_cards.py` |
| `scripts/kushi_cover_text_overlay.py` | `scripts/kushi_cover_text_overlay.py` |
| `scripts/render_xhs_cover.py` | `scripts/render_xhs_cover.py` |
| `scripts/render-channel.sh` | `scripts/render-channel.sh` |
| `scripts/lib/kit_render.py` | `scripts/lib/kit_render.py` |
| `scripts/lib/rewrite-render-asset-refs.py` | `scripts/lib/rewrite-render-asset-refs.py` |

## Pinned templates（源仓 → Prism）

| 源仓路径 | Prism 落点 |
|---|---|
| `templates/kushi-wechat-image-post/` | `templates/kushi-wechat-image-post/` |
| `templates/kushi-wechat-article-post/` | `templates/kushi-wechat-article-post/` |
| `templates/wechat-card-kit/` | `templates/wechat-card-kit/` |
| `templates/jieqi-yangsheng-classical/` | `templates/jieqi-yangsheng-classical/` |

## 未 pin（说明）

- `scripts/lib/readability-lint.py`：仅参考；Prism 已用原生 `scripts/check_readability.py` 替代。
- `scripts/lib/record-humanize-evidence.py`、`publish-*.sh`、`sync-ai*` 等：凭证/发布链路，
  不在 A1 范围，维持 bridge 或 defer。

## 义务

- 本文件随 pin 产物保留；修改 pin 产物时保留本 ATTRIBUTION 头。
- 第三方依赖（Playwright、字体、图片生成服务、媒体素材）不因本授权自动覆盖。
