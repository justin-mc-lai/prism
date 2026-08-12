# Adapter contract: monetization（Lake F1 · 变现契约）

> 变现契约层。承诺需人工批准；披露与合规是硬门；不编造收入。

## 1. identity

- skill_id: adapter-monetization
- public_or_adapter: adapter
- one_liner: 品牌合作/广告/付费/带货 deal 登记与批准

## 2. 决策边界

- 能决定：deal 结构、类型归类、披露文本、合规检查
- 不能决定：承诺合作/收入、公开、QA 判定

## 3. intake（必填）

- deal_id + type（brand/ad/paid/goods）+ terms + disclosure + evidence

拒绝：缺 evidence → blocked + reason_code=deal_evidence_missing；不编造收入/合作

## 4. output

- 记录: `content/deals/{deal_id}.yaml`（批准后）
- 证据: `.beacon/evidence/implement/prism-monetization-contracts-v1/AC-MON-001.json`

## 5. gate

- 人工批准：变现承诺必须 approval_recorded 才生效
- 披露义务：广告/赞助内容必须标注（disclosure note）
- 风险合规门：health/legal/finance 内容未过合规不得变现
- 敏感信息保护：收款/合同信息走受管 secrets，禁止入库

## 6. handoff

- 下一面: F2 adaptation-contracts（改编契约）

## 7. 失败处理

- 可重试: 条款补全、披露文本、合规补检
- 必须停: 未批准、缺证据、合规未过、敏感信息入库
- 禁止自证通过: true
