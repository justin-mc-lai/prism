# Adapter contract: publish bridge（Lake D6）

> Release 侧桥。Prism 只建草稿/排期；公开发布必须人工二次批准。

## 1. identity

- skill_id: adapter-publish-bridge
- public_or_adapter: adapter
- one_liner: 发布/排期桥（MAP-008）——草稿-only、人工门、误路由守卫、证据记录
- bridge 路由: publish-content / schedule-post / x-publish / manage-media

## 2. 决策边界

- 能决定：平台路由、草稿创建、排期意图、证据记录
- 不能决定：公开发布（必须人工二次批准）、母稿事实、QA 判定

## 3. intake

- 成稿/成品引用（content/presentations 路径）+ 目标平台 + 账号配置
- 排期意图（可选：时间 + 日历）

拒绝：无成稿引用 / bridge 缺失 → blocked + reason_code（publish_bridge_missing）

## 4. output（草稿/排期，不公开）

- 草稿: 平台草稿 ID（draft_id）+ 预览 URL
- 排期: schedule 记录（平台 + 时间 + 草稿引用）
- 证据: `.beacon/evidence/implement/prism-publish-bridge-v1/AC-PUB-001.json`

## 5. gate（发布边界）

- **草稿-only**：Prism 只能创建草稿/排期意图；`published` 必须人工二次批准后由平台真实结果写入
- **误路由守卫**：草稿进入错误 tab/平台 → `superseded-misrouted` + `do_not_publish: true`，重走正确通道
- **凭证保护**：平台凭证/密钥/`.env`/secrets 禁止入库；走环境变量或受管 secrets
- **证据**：无 draft_id/URL 不算已发布；无证据默认不过

## 6. handoff

- 下一公开面: 人工平台预览 → 人工二次批准 → 真发布（记录 publication_id）
- 禁止跳过: 人工批准；禁止自动公开

## 7. 失败处理

- 可重试: 平台选择、排期、bridge 换工具
- 必须停: 工具缺失、凭证缺失、未批准公开、误路由未标记
- 禁止自证通过: true
