# Adapter contract: review-loop（Lake E3 · 战役复盘/圣经更新）

> 复盘闭环契约。数据驱动、人工批准入库、不改母稿事实。

## 1. identity

- skill_id: adapter-review-loop
- public_or_adapter: adapter
- one_liner: 战役/连载周期复盘 → 人工批准 → 系列圣经复盘段
- depends_on: contracts/metrics-snapshot.contract.md（E2）

## 2. 决策边界

- 能决定：复盘结构、发现/行动整理、圣经复盘段写入（批准后）
- 不能决定：母稿事实/正典、QA 判定、公开发布

## 3. intake（必填）

- campaign_id + period + metrics_refs（≥1 个 E2 快照引用）

拒绝：无 metrics_refs → blocked + reason_code=metrics_refs_missing；不空谈

## 4. output

- 复盘: `content/series/{vertical}/bible.md` 复盘段（人工批准后）
- 记录: `content/reviews/{campaign_id}/{period}.md`（review_id + findings + actions）
- 证据: `.beacon/evidence/implement/prism-review-loop-v1/AC-RVL-001.json`

## 5. gate

- 无 metrics_refs 的复盘 blocked（数据驱动）
- 复盘结论/圣经更新必须人工批准确认后才写入（approval_recorded）
- 只更新 bible 复盘段；不改已冻结母稿事实/正典
- maker≠checker：复盘记录与 QA 分离，证据引用

## 5.1 标题命中复盘（title-lab 配套 · 每 4 周）

- 周期：每 4 周至少 1 次（对齐 E2 快照窗口），按 `title_formula` 分组聚合。
- 对比基线：本周期各公式均值 vs 前 4 周基线；样本 <5 条标注「样本不足，不下结论」。
- 产出：`content/reviews/{campaign_id}/{period}.md` 增「标题命中」段：公式表现排序 + 首选命中率 +
  下一周期建议（保留/淘汰/换身份词）；人工批准后写入 bible 复盘段。
- 禁止：单篇高曝光直接当公式命中；无 title_formula 数据时跳过该段，不编造归因。

## 6. handoff

- 下一面: E4 learning-memory（复盘可供学习）

## 7. 失败处理

- 可重试: 数据引用、复盘结构、换 bridge
- 必须停: 缺数据、未批准入库、母稿边界
- 禁止自证通过: true
