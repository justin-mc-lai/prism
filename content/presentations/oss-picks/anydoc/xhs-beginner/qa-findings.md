# QA Findings — anydoc · xhs-beginner（样例）

> maker ≠ checker：本文件由 QA 面产出。

## 判据与结论

| # | 判据 | 方法 | 结论 |
|---|---|---|---|
| 1 | 合同 | `form_id: xhs` 头在场 | pass |
| 2 | 图位 | 显式 `【图片占位 …】` 5 处 | pass |
| 3 | 人味门 | 翻案腔变形 0 / 硬停词 0 / 黑话 0 | pass |
| 4 | 可读性 | `check_readability.py`（非 depth） | pass |
| 5 | 事实纪律 | 样例标注 scaffold | pass |

## 未决项

- 真实母稿（scaffold）
- 公开发布：`release_gate: pending_human`

## 结论

结构层 pass；**不构成发布许可**。
