# Form contract: product（Lake D2 · 电商商品）

> 形态契约。商品事实门 + 广告合规门优先于一切文案产出。
> 参考蒸馏：dramaclaw 电商视频管线判断框架（distill only，Elastic-2.0 不复制运行时）。

## 1. identity

- form_id: product
- 定位: 电商商品内容（种草图文 / 商品短视频脚本 / 好物测评 / 开箱）
- lane: standard
- bridge: 按名调用已装 skill/脚本（如 `vendor/skills/rnskill` 封面、`scripts/render_xhs_cover.py`）；缺失 → blocked

## 2. 决策边界

- 能决定：卖点排序、文案结构、桥接选择、版式
- 不能决定：商品事实（规格/价格/功能/资质）、QA 判定、公开发布

## 3. intake（必填）

- 冻结母稿/事实快照，其中商品事实必须有源：
  - 用户提供的商品资料（详情页/规格书），或
  - 商品链接抓取留档，或
  - 人工逐项确认记录
- 平台与版式意图（图文 / 视频脚本）

拒绝：无母稿 / 商品事实无源 → blocked + `reason_code=product_fact_missing`
拒绝：bridge 缺失 → blocked + `reason_code=bridge_tool_missing`

## 4. output

- 成稿: `content/presentations/{vertical}/{slug}/product-{angle}/`（文案 + 素材清单 + manifest）
- 证据: `.beacon/evidence/implement/prism-form-product-v1/AC-PRD-002.json`

## 5. gate（事实门 + 合规门）

- 商品事实门：规格/价格/功能/资质逐项对源；无源项删除或标注待确认，禁止编造参数
- 极限词门（广告法）：最/第一/顶级/绝对/国家级 等极限词 → fail-closed；给出合规替代表达
- anti-slop-gate 过；图片文字 OCR 核验（无乱码、文字可读）
- 每项结论带证据引用；maker ≠ checker

## 6. handoff

- 下一公开面: prism-qa（事实/合规/anti-slop-gate）→ prism-release（只建草稿；公开需人工二次批准）

## 7. 失败处理

- 可重试: 卖点结构、文案、素材、换 bridge
- 必须停: 商品事实无源、极限词无法消除、发布批准
- 禁止自证通过: true
