# Adapter contract: metrics-snapshot（Lake E2 · MetricsSnapshot）

> 快照契约。指标是投影；无发布记录不得 measured（继承 E1 守卫）。

## 1. identity

- skill_id: adapter-metrics-snapshot
- public_or_adapter: adapter
- one_liner: 某发布内容在某个时间点的平台指标快照
- depends_on: contracts/metrics-publication.contract.md（E1）

## 2. 决策边界

- 能决定：指标字段、采集时间、bridge 选择
- 不能决定：编造指标/趋势；公开；QA 判定

## 3. intake（必填）

- publication_ref（E1 发布事件 ID）+ 平台 + 采集时间

拒绝：无 publication_ref → blocked + reason_code=publication_record_missing；不猜数据

## 4. output

- 快照: `content/publications/{platform}/{account}/{slug}/metrics/{snapshot_id}.yaml`
- 字段: snapshot_id / publication_ref / views / interactions / followers / collected_at / source（来源）
- 证据: `.beacon/evidence/implement/prism-metrics-snapshot-v1/AC-MSNAP-001.json`

## 5. gate

- 无 publication_ref 不得生成快照（FSM measured 守卫）
- 缺数据用显式空快照（字段=null/0 + status=empty），不编造指标/趋势
- 缺证据（collected_at/来源）不算采集
- 凭证保护：平台凭证/密钥/.env/secrets 禁止入库，走受管 secrets

## 6. handoff

- 下一面: E3 review-loop（战役复盘）

## 7. 失败处理

- 可重试: 采集重试、换 bridge、字段补全
- 必须停: 凭证缺失、无发布记录、数据缺失
- 禁止自证通过: true
