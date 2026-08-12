# Adapter contract: writing（Lake D1 · distilled）

> Internal only. Not host-discoverable. Seven-segment per contracts/skill-contract-7seg.tpl.md
> Source: selfmedia-creator `selfmedia-writing` / `selfmedia-humanize` / `humanizer-zh` / `no-ai-slop`（MAP-005 distill+bridge）
> Landing: contracts/writing.contract.md（Prism 成稿层权威；形态本体 D2–D6）

## 1. identity

- skill_id: adapter-writing
- public_or_adapter: adapter
- one_liner: Prism 成稿层地基——写作结构选型、文笔规则、人味策略与 bridge 通道；形态本体在 D2–D6
- map_id: MAP-005 · strategy: distill + bridge

## 2. 决策边界

- 能决定：体裁选型（四段式 / 日榜倒金字塔 / emotional-essay）、文笔执行、bridge 工具选择
- 不能决定：不改母稿事实/正典；不自证 QA；不公开发布；不承诺必过机检
- 必须上抛：bridge 工具缺失、缺冻结母稿、证据缺失、人工批准点

## 3. intake

- 必填输入：冻结母稿引用（MASTER 路径）+ 创作类型（blog/thread/贴图/…）+ 读者层级
- 拒绝条件：无冻结母稿却要求 produce；bridge 缺失却要求产出；无证据却要求放行

## 4. output contract

- 人类面产出：成稿路径 + 下一公开面（qa），不暴露 adapter 名
- 机器面产出：`content/presentations/{vertical}/{slug}/{presentation_slug}/` 或 `.beacon/evidence/` 产物 + evidence refs
- 路径约定：成稿写入 content 层；证据写入 `.beacon/evidence/implement/prism-form-writing-v1/`

## 5. gate

### 体裁选型（蒸馏自 selfmedia-writing）

| 体裁 | 何时用 | 结构 |
|------|--------|------|
| oss-pick-standard（深度四段式） | 开源科普、新手小白 | 场景开场 → 🚀 MVP → 📖 由简入深 → 🎯 本质 → 🗺️ 架构 → 💎 亮点 → ⚠️ 坑点 → 行动 |
| oss-pick-daily（日榜倒金字塔） | 每日榜单 | 结论先行、倒金字塔，无四段 emoji |
| emotional-essay（情绪观点长文） | X 长文/公众号贴图深度稿/小红书 | 否定定义壳 + 短节拍 + 收尾金句（按 archetype 判别开关，不按通用 AI 痕迹抹平） |

### 文笔五原则（蒸馏自 prose-core）

1. 像说话一样写
2. 一句一意
3. 倒金字塔（结论先行）
4. 主动语态（禁「被发布」「被调用」）
5. 正面表述

### 硬规则

- 禁翻译腔：「正如我们所见」「被广泛使用」「基于…的原因」
- 术语首次出现用白话括号解释
- 禁假数据/假经历/假截图；无素材用 `【经历占位：…】`
- 每稿必须走至少一轮人味层（bridge：selfmedia-humanize / humanizer-zh / qu-ai-wei / shuorenhua 等）

### fail-closed（bridge）

- bridge 工具缺失 → `blocked` + `reason_code=bridge_tool_missing`，**不产出假文件**
- 缺冻结母稿 → `blocked` + `reason_code=frozen_master_missing`
- 产出必须带 evidence 路径，否则视为未完成

## 6. handoff

- 下一公开面：prism-qa（按 `skills/prism-qa/references/anti-slop-gate.md` 核验）
- 禁止跳过：qa、human release 批准
- 跨形态路由：`skills/_internal/orchestration/creation-mode-map.md`

## 7. 失败处理

- 可重试：生成类修复、换 bridge、补素材
- 必须停并等人：发布/正典/合规/工具安装
- 禁止自证通过：true
