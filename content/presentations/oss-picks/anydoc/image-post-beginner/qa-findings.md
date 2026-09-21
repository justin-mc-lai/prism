# QA Findings — anydoc · image-post-beginner（样例）

> maker ≠ checker：本文件由 QA 面产出，不由生产面自证。

## 判据与结论

| # | 判据 | 方法 | 结论 |
|---|---|---|---|
| 1 | 合同 | `manifest.form_id == image-post` 且 `1 <= image_count <= 9` | pass（6） |
| 2 | 结构 | 六卡 role 齐备（cover/pain/idea/how/pitfall/action） | pass |
| 3 | 文字可读 | 渲染后逐卡 OCR 复核，无截断/乱码/遮挡 | pass（`ocr_gate: pass`） |
| 4 | 版式一致 | 六卡同模板、同尺寸 1080×1440 | pass |
| 5 | 文案 | 过 anti-slop-gate（样例文案短，无套路词） | pass |
| 6 | 来源 | 样例标注 scaffold，**无可发布主张** | pass（不发布） |

## 未决项

- 真实母稿与来源核对：本样例缺失，标注 scaffold。
- 公开发布：`release_gate: pending_human`。

## 结论

结构层 pass；**不构成发布许可**。公开发布必须走 prism-release 人工二次批准。
