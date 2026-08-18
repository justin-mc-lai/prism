# Form contract: image-post（Lake D3 · 公众号贴图包）

> 形态契约。源规则蒸馏自 `selfmedia-account-pipeline`（MAP-006）。

## 1. identity

- form_id: image-post
- 定位: 公众号「贴图」Tab 图像产出包（非长文草稿）
- lane: standard
- render: 本地 pin（A1 · MIT）：`scripts/render_wechat_article_pages.py` /
  `render_wechat_html_cards.py` / `render_wechat_image_cards.py` + `scripts/kushi_cover_text_overlay.py` +
  `templates/`；ATTRIBUTION 见 `docs/ATTRIBUTION-render-chain.md`

## 2. 决策边界

- 能决定：图序、caption 文案、封面排版、桥接选择
- 不能决定：母稿事实、QA 判定、公开/上传发布

## 3. intake（必填）

- director shot list（visual_carrier）+ 冻结母稿/快照
- 账号 profile（走配置，禁止硬编码 kushi-gzh 等账号名）

拒绝：无 shot list / 无母稿 / bridge 缺失 → blocked + reason_code

## 4. output（四分离）

- `title`：≤20 字短题，不带账号前缀
- `caption`：独立短说明（caption-short.md / manifest 字段），不退化为标题或正文
- 图片：1-9 张（1–9），超 9 拆条；图序明确（第 1 张可声明为 cover_card）
- 封面：无文字底图（生成模型只做底图）+ 本地标题排版（`scripts/kushi_cover_text_overlay.py`），
  封面不混入正文图；尺寸默认 1080x1440
- 证据：`.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-002.json`

## 5. gate（QA 清单）

- 无乱码、无随机文字、无账号角色名/标签误写
- 图序正确、尺寸合规、图片数 1–9
- title/caption/图片/封面分离成立
- 价值门通过；contract-check 通过
- 每项结论带证据引用

## 6. handoff

- 下一公开面: prism-qa（OCR/图序/尺寸/分离）→ prism-release（只建草稿）
- 误传文章 Tab → `superseded-misrouted` + `do_not_publish: true`
- 公开发布必须人工二次批准

## 7. 失败处理

- 可重试: 渲染、caption、图序、换 bridge
- 必须停: 工具缺失（render_tool_missing）、事实/正典、发布批准
- 禁止自证通过: true
