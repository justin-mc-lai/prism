# Adapter contract: adaptation（Lake F2 · 改编契约）

> 改编授权契约层。默认只登记不授权；人工批准 + 正典保护是硬门。

## 1. identity

- skill_id: adapter-adaptation
- public_or_adapter: adapter
- one_liner: 小说/漫画/视频资产改编授权登记与批准
- depends_on: contracts/monetization.contract.md（F1）

## 2. 决策边界

- 能决定：授权结构、类型归类、条款/分成整理、license 检查
- 不能决定：授权生效（必须人工批准）、母稿正典、公开

## 3. intake（必填）

- adaptation_id + asset_ref（母稿/正典引用）+ type（comic/video/game/book）+ rights + royalty

拒绝：缺 asset_ref / approval / evidence → blocked + reason_code=adaptation_evidence_missing

## 4. output

- 记录: `content/adaptations/{adaptation_id}.yaml`（批准后）
- 证据: `.beacon/evidence/implement/prism-adaptation-contracts-v1/AC-ADP-001.json`

## 5. gate

- 默认只登记不授权：必须 approval_recorded 才可谈改编
- 正典保护：改编不得破坏母稿正典（引用 canon ledger）
- license 边界：第三方 IP 未获权不自动授权；风格改写安全描述
- 不编造授权/分成：缺证据 blocked
- 合同敏感信息走受管 secrets，禁止入库

## 6. handoff

- 下一面: 人类批准 → 改编项目启动（不在本湖）

## 7. 失败处理

- 可重试: 条款补全、royalty 校准、license 补检
- 必须停: 未批准、缺证据、正典冲突、敏感信息入库
- 禁止自证通过: true
