# QA Findings — anydoc image-post-beginner

- mode_id: gate-qa
- public_id: qa
- lane: standard
- recommended_next_harness: release
- map_ids_considered: ['MAP-006']
- 检查对象: `manifest.yaml` + `title.md` + `caption-short.md` + `director-shot-list.md`

## 1. 四分离检查

| 项 | 结果 | 证据 |
|---|---|---|
| title ≤20 字、无账号前缀 | ✅「把 Word/PDF 变成干净 Markdown」（12 字） | `title.md` |
| caption 独立短说明 | ✅ 一句话 + 边界提示，不退化为标题/正文 | `caption-short.md` |
| 图片 1–9 | ✅ 6 张 | `manifest.yaml` image_count |
| 图序明确 + cover_card 声明 | ✅ 第 1 张 cover_card | manifest |
| 封面无文字底图 + 本地排版 | ✅ 占位注明「无文字底图，本地排版标题」 | manifest card 1 |
| 尺寸 1080x1440 | ✅ | manifest image_dimension |
| 无账号硬编码 | ✅ 无 kushi-gzh 等账号名 | 通读 |

## 2. 文案门（anti-slop）

- 全部 caption 无翻案腔/硬停词/黑话/叙述冒号（caption 文案逐条人工过 anti-slop-gate 清单）
- 事实全部回源 MASTER：格式 claim 1–2 / 三入口 claim 3, 11–13 / star 快照 claim 4 /
  WASM 不上传 claim 7 / OCR 边界 claim 8 / CLI claim 10
- 「9 天」= 创建 08-03 → 检索 08-12 日期推算，已标注快照时刻

## 3. OCR / 渲染门（pending）

- ✅ 已渲染（2026-08-14）：`scripts/render_wechat_html_cards.py`（A1 MIT pin）产出
  `rendered/01-cover.png … 06-action.png`，1080×1440，图序与 manifest 一致
- ✅ OCR 门：macOS Vision 框架逐卡核验，文字可读、无乱码、无随机文字；
  小字号 OCR 伪影（MIIT / CLl / frecrawl）已对照 HTML 源文本确认是 OCR 误读非渲染错误
- 封面为 HTML 本地排版（非无文字底图 + 叠加管线）；如需 Gemini 无字底图封面，
  走 `scripts/kushi_cover_text_overlay.py` 分支（同样已 pin）

## 4. 门禁结论

- 四分离：pass；文案：pass；事实对齐：pass；渲染 + OCR：pass
- verdict: `release_candidate_draft_only`（人工批准后才可发布）
