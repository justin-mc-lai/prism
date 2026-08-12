# Form contract: thread（Lake D2 · X thread 快道/标准道）

> 形态契约。结构规则继承 `contracts/writing.contract.md`；QA 继承 `anti-slop-gate.md`。

## 1. identity

- form_id: thread
- 定位: X/微博式短链观点帖
- lane: fast|standard（fast 需显式 `fast_lane_skip` 标注；canon 禁用快道）
- bridge: writing-agent（缺失 → blocked）

## 2. 决策边界

- 能决定：倒金字塔结构、节奏、bridge 选择
- 不能决定：事实真伪、QA 判定、公开发布

## 3. intake

- 快道: 事实快照（选题 + 关键事实/引用）即可；intel/master/director 以 `fast_lane_skip` 标注跳过
- 标准道: 冻结母稿 + 可选 director treatment

拒绝：无事实快照/母稿；lane=canon 却要求 fast_lane_skip → blocked（illegal）

## 4. output

- 成稿: `content/presentations/{vertical}/{slug}/thread-{angle}.md`
- 证据: `.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-003.json`
- 头部: form_id + lane + fast_lane_skip（若快道）

## 5. gate（倒金字塔）

1. hook（第一句给结论/钩子）
2. 证据（具体事实/引用，weasel 归因禁止）
3. 观点（有态度，无空口号）
4. 行动/收尾（具体下一步；禁假深刻结尾）

每条命中 anti-slop-gate 模式必须 quote 原文行 + 修复建议 + 证据路径。

## 6. handoff

- 下一公开面: prism-qa（anti-slop-gate）→ release

## 7. 失败处理

- 可重试: 结构、节奏、换 bridge
- 必须停: 事实无源、发布、工具缺失（bridge_tool_missing）
- 禁止自证通过: true
