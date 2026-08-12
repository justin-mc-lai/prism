---
slug: prism-form-image-post-v1
version: v0.0.1
status: promoted
promotion_ref: "utterance 2026-08-12：Lake D 逐个形态冻结实现；D3 贴图/xhs"
user_decision: promoted
---

# Research: prism-form-image-post-v1

## 背景

D1/D2 完成写作地基与文本形态。D3 落地贴图包 + 小红书图文两个图像形态。

## 源仓证据

- `selfmedia-account-pipeline`：title ≤20 字无前缀、caption 独立、1–9 张/超9拆条、
  封面无文字底图 + 本地排版（`kushi_cover_text_overlay.py`）、QA（乱码/图序/尺寸/分离）、只建草稿
- creation-mode-map：贴图包 article-paper/短卡、小红书图文行
- MAP-006：distill shot-list/caption 规则；render 脚本 bridge；账号硬编码清洗

## 落点决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 贴图契约 | `contracts/form-image-post.contract.md` | 四分离 + 1–9 + 本地封面 |
| xhs 契约 | `contracts/form-xhs.contract.md` | bridge xhs-article-to-images + OCR 门 |
| 渲染 | bridge 源仓脚本（render_wechat_*） | 不复制大栈；缺失 blocked |
| 账号 | 配置化 | 禁止 kushi-gzh 硬编码 |

## 明确不做（本子湖）

- D4–D6、vendor_pin、metrics、平台 API、海 closure 宣称
