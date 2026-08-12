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

## 6. handoff

- 下一面: E4 learning-memory（复盘可供学习）

## 7. 失败处理

- 可重试: 数据引用、复盘结构、换 bridge
- 必须停: 缺数据、未批准入库、母稿边界
- 禁止自证通过: true
