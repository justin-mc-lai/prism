# Form contract: av（Lake D5 · comic / vlog / book_video）

> 形态契约。AV 大栈 bridge 优先；license 敏感，vendor_pin 需人工批准 + ATTRIBUTION。

## 1. identity

- form_id: av（comic / vlog / book_video 三路由）
- lane: standard
- bridge 路由:
  - comic → comic-storyboard（3:4 竖版；文字 ≥48px/可读；ChatGPT 网页流程）
  - vlog → openmontage（Remotion/FFmpeg；AGPL-3.0，默认 bridge 不 pin）
  - book_video → book-video / rnskill 视频族

## 2. 决策边界

- 能决定：路由选择、交接字段执行、bridge 选择
- 不能决定：母稿事实、QA 判定、公开发布、vendor_pin（需人工）

## 3. intake（director handoff 必填）

- treatment（核心意图/情绪曲线）
- presentation map（镜头/页面 × 受众效果）
- shot list 或 storyboard（分镜/分页）；comic 多集路由下引用须解析到资产身份条目，
  过**资产一致性门** `contracts/asset-consistency.contract.md`
  （三分法/边界匹配/画风统一；未决项不得流入分页）

拒绝：缺任一交接字段 / bridge 缺失 → blocked + reason_code

## 4. output

- comic: `content/presentations/{vertical}/{slug}/comic-{angle}/pages/`
- vlog: `content/presentations/{vertical}/{slug}/vlog-{angle}/`（脚本 + 成片 + 剪辑清单）
- book_video: `content/presentations/{vertical}/{slug}/book-video-{angle}/`
- 证据: `.beacon/evidence/implement/prism-form-av-v1/AC-AV-002.json`

## 5. gate（QA 门）

- 字幕/画面文字无乱码、无随机文字
- 版权安全（角色/风格改写为描述性特征；受版权保护角色拒绝）
- 分镜/图序/分页一致；漫画 3:4 竖版、文字可读
- comic 多集路由：过资产一致性门（`contracts/asset-consistency.contract.md`）；
  vlog / book_video 单集口播不接入
- 文案过 anti-slop-gate；每项结论引用原文/素材行 + 证据路径

## 6. license 注记

- OpenMontage: AGPL-3.0 → 默认 bridge；vendor_pin 需 license review + ATTRIBUTION + 人工批准
- 其他大栈（rnskill/book-video 等）同规则；未过 license 门一律不 pin

## 7. handoff / 失败处理

- 下一公开面: prism-qa → prism-release（草稿；公开需人工二次批准）
- 可重试: 渲染、分镜、换 bridge
- 必须停: bridge 缺失（av_bridge_missing）、license 未过、事实/正典、发布
- 禁止自证通过: true
