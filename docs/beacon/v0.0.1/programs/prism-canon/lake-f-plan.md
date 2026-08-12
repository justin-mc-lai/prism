# Lake F Program Plan — 变现/改编契约（pln-program）

- program: prism-canon · version: v0.0.1 · lake: F
- plan_mode: interactive · scope_mode: phased_lake
- 来源: Lake A INT-P16（vision optional）/ DL-005（accepted）/ Phased Backlog Lake F
- 生成日期: 2026-08-12

## Intent（一行）

把**变现与改编**落成文件级契约：变现（品牌合作/广告/付费/带货）与改编（漫画/视频/游戏/书籍改编权）
都要求人工批准、证据记录、披露与合规门；不编造收入/合作，不吞平台支付 API。

## 子湖拆分

| 子湖 | feature slug | 交付物 | 策略 |
|---|---|---|---|
| F1 | prism-monetization-contracts-v1 | 变现契约（deal_id/type/terms/disclosure/evidence + 人工批准 + 风险内容合规门） | distill + bridge |
| F2 | prism-adaptation-contracts-v1 | 改编契约（adaptation_id/rights/royalty/approval/evidence + license 边界） | distill + bridge |

顺序理由：先变现（与内容发布直接相关），后改编（资产积累后才谈改编）。

## Bridge / Distill 规则

- bridge：合同记录/合规检查/披露模板等本地工具；缺工具 fail-closed
- distill：变现记录 schema、披露义务清单、风险内容合规门、改编权/分成 schema
- 边界：收款/合同敏感信息受管；不编造收入；不自动承诺合作

## 风险与门禁

- R1 敏感信息（收款、合同）→ 受管 secrets / 不入库
- R2 变现承诺必须人工批准 + evidence
- R3 health/legal/finance 风险内容：变现前必须过合规门
- R4 改编 license 边界：默认登记契约，不自动授权

## Route

F1 → F2；完成后 A–F 全湖交付（平台公开发布仍逐内容人工门）。
