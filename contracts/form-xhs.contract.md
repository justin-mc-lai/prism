# Form contract: xhs（Lake D3 · 小红书图文）

> 形态契约。bridge 优先；工具缺失 fail-closed。

## 1. identity

- form_id: xhs
- 定位: 小红书图文（emotional-essay 或种草向）
- lane: standard
- bridge: xhs-article-to-images（本地已安装时按名调用）

## 2. 决策边界

- 能决定：文案结构（emotional-essay 选型）、配图文案、桥接选择
- 不能决定：母稿事实、QA 判定、公开发布

## 3. intake

- 冻结母稿/事实快照 + 平台版式意图

拒绝：无母稿 / xhs-article-to-images 缺失 → blocked + reason_code=bridge_tool_missing

## 4. output

- 成稿: `content/presentations/{vertical}/{slug}/xhs-{angle}/`（文案 + 图片 + manifest）
- 证据: `.beacon/evidence/implement/prism-form-image-post-v1/AC-IMG-003.json`

## 5. gate（OCR 门）

- 图片文字 OCR 核验：无乱码、无随机文字、文字可读、版权安全
- caption/title 分离；anti-slop-gate 过
- 每项结论带证据引用

## 6. handoff

- 下一公开面: prism-qa → prism-release（只建草稿；公开需人工二次批准）

## 7. 失败处理

- 可重试: 文案、图片生成、换 bridge
- 必须停: 工具缺失、事实无源、发布批准
- 禁止自证通过: true
