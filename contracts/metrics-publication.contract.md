# Adapter contract: metrics-publication（Lake E1 · 发布证据回流）

> 回流基座契约。指标是投影（FP-PRISM-006）；无发布记录不得进入 measured。

## 1. identity

- skill_id: adapter-metrics-publication
- public_or_adapter: adapter
- one_liner: 把 D6 发布桥结果结构化回流为发布事件
- depends_on: contracts/publish-bridge.contract.md（D6）

## 2. 决策边界

- 能决定：事件字段校验、平台归类、证据记录
- 不能决定：编造指标/趋势；公开发布；QA 判定

## 3. intake（必填）

- publication_id（平台真实 ID）+ platform + url + published_at + artifact_ref
- 标题跟踪（title-lab 产出时）：title_formula（最终标题所用公式 slug）+ is_preferred（是否首选/用户选定）

拒绝：缺任一字段 → blocked + reason_code=publication_record_missing；不猜数据

## 4. output

- 事件: `content/publications/{platform}/{account}/{slug}/`（publication.yaml）
- 事件字段：平台指标按 E2 快照采集；标题字段 `title_formula` / `is_preferred` 随发布记录一并回流（无 title-lab 产出的历史发布显式 `null`，不补造）
- 证据: `.beacon/evidence/implement/prism-metrics-publication-v1/AC-MPUB-001.json`
- 时间: 发布事件时间（published_at）必须真实记录；缺证据（时间/URL）不算回流

## 5. gate（measured 守卫）

- 无 publication 记录不得进入 measured（Lake A FSM illegal：published→measured 无记录）
- 指标是投影不是 canonical；发布记录是回流基座
- 缺数据用显式空快照；不编造指标/趋势（禁止猜测）
- 凭证保护：平台凭证/密钥/.env/secrets 禁止入库，走受管 secrets

## 6. handoff

- 下一面: E2 metrics-snapshot（指标快照采集）

## 7. 失败处理

- 可重试: 字段补全、平台归类、换 bridge
- 必须停: 凭证缺失、无发布记录、数据缺失
- 禁止自证通过: true
