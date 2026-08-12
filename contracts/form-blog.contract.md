# Form contract: blog（Lake D2 · 深度长文）

> 形态契约。结构规则继承 `contracts/writing.contract.md`；QA 继承 `anti-slop-gate.md`。

## 1. identity

- form_id: blog
- 定位: 深度长文（开源科普/主题深度稿）
- lane: standard（禁用 fast_lane_skip）
- bridge: selfmedia-writing / humanizer-zh / selfmedia-humanize（缺一即 blocked）

## 2. 决策边界

- 能决定：结构选型（四段式）、文笔执行、bridge 选择
- 不能决定：母稿事实、QA 判定、公开发布

## 3. intake（必填）

- 冻结母稿引用（MASTER + meta.yaml）
- director treatment（presentation map / 角度）
- 读者层级

拒绝：无母稿 / 无 treatment / bridge 缺失 → blocked + reason_code

## 4. output

- 成稿: `content/presentations/{vertical}/{slug}/blog-{angle}/humanized.md`
- 证据: `.beacon/evidence/implement/prism-form-blog-thread-v1/AC-FORM-002.json`
- 头部: form_id + master_ref + treatment_ref + lane

## 5. gate（四段式结构清单）

1. 场景开场（痛点 ≥80 字）
2. 🚀 小白 MVP（可复制命令 + 跑通检查）
3. 📖 由简入深（3/10/进阶阅读路径）
4. 🎯 一句话看透本质
5. 🗺️ 核心架构与主流程（先白话闭环，再进阶模块）
6. 💎 绝妙设计亮点（≥2）
7. ⚠️ 潜在坑点与局限性
8. 接下来你可以（行动项）

文笔五原则 + 禁翻译腔见 writing.contract；QA 引用 anti-slop-gate。

## 6. handoff

- 下一公开面: prism-qa（anti-slop-gate + 事实核对）
- 禁止跳过: qa、human release

## 7. 失败处理

- 可重试: 结构缺段、人味不足、bridge 换工具
- 必须停: 事实/正典/发布/工具安装
- 禁止自证通过: true
