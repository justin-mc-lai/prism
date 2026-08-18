---
name: selfmedia-humanize
description: |
  自媒体人味改写 / 降 AI 套路。把选题、提纲或 AI 初稿改成更像真人表达的稿件，
  降低腾讯朱雀等 AI 内容检测常见的「模板感」（句长均匀、空总结、机械排比）。
  触发：selfmedia-humanize、过朱雀、降 AI 味、查重、口语化改写、人味润色、机检。
  与 humanizer-zh 关系：humanizer-zh 偏终检去痕；本 skill 偏成稿/二创时的句式与口语策略，可串联使用。
  Use when rewriting social content to sound more human and less template-AI for detectors like Tencent Zhuque.
metadata:
  pipeline_step: humanize
  pairs_with: [selfmedia-writing, humanizer-zh, qu-ai-wei, shuorenhua, create-content, kushi-narrative-zh]
  project: selfmedia-creator
---

# selfmedia-humanize（人味 · 降套路）

## 定位

本 skill 属于 **selfmedia-creator 项目**内的成稿/二创助手。

目标：打破 AI 生成的套路化模式，补齐人类表达习惯与个性化特征，使文稿读起来像具体某个人在说话。

**不是**「保证过朱雀」的对抗工具；检测模型会变，只能**降低可识别 AI 模板感**。

### 硬边界

- 不承诺必过朱雀 / 任意 AI 检测分数  
- 不教批量刷检测、伪造账号或恶意规避平台规则  
- 不编造个人经历、数据、截图；无素材用 `【经历占位：…】`  
- 与 `selfmedia-writing` 串联时：先成稿结构，再本 skill 人味，再 `humanizer-zh` 终检（若走库拾管线）

## 何时用

- 公众号 / 小红书 / 口播 / 视频号文案要「像人」
- 用户提到：朱雀、AI 味、查重、机检、口语化
- 已有大模型初稿，需要打散套路二改
- `create-content` 或 `selfmedia-writing` 产出后需要额外人味层

## 工作流

### 1. 收输入

| 项 | 说明 |
|---|---|
| 平台 | 小红书 / 公号 / 口播 / 其他 |
| 目标 | 种草 / 科普 / 观点 / 获客 |
| 素材 | 事实、观点、**真实**经历 |
| 禁忌 | 不能说的、品牌调性 |
| 篇幅 | 字数或口播秒数 |

有初稿 → **改写模式**；无初稿 → 先写再自检。

### 2. 扫 AI 套路

按 `references/ai-tells-checklist.md` 扫描后再动笔。

### 3. 强制人味手法（本 skill 核心）

写作/改写时**同时**做到（细则：`references/human-voice-techniques.md`）：

1. **句式长短交错**  
   长句 + 短句 + 反问 + 感叹；打破「句句差不多长、结构对称」。
2. **转折与口语连接（点缀）**  
   其实 / 说实话 / 讲道理 / 话说回来 / 我倒觉得 / 先说结论  
   禁止每句「说实话」。
3. **个人经历与细节**  
   真素材优先；越具体越好（时间、场景、结果）；无则占位，禁止假履历。
4. **情感起伏**  
   有态度、犹豫、取舍；不要只有正确废话。
5. **反模板**  
   少机械排比；少「综上所述 / 值得注意的是 / 赋能 / 闭环」；结尾少空口号。

### 4. 输出格式

```markdown
## 成稿
（可直接用或进 humanizer-zh）

## 可选标题（3）
…

## 人味自检
- 句式交错：
- 口语转折：
- 具体细节：
- 仍偏 AI 处：（若有）

## 给其他模型的提示词（可选）
见 references/prompt-rewrite.md，需要时粘贴，勿当正文。
```

平台壳：`references/platform-notes.md`。

### 5. 与项目内其他 skill

```text
create-content / selfmedia-writing
  → selfmedia-humanize   # 本 skill：句式与口语策略
  → humanizer-zh         # 终检：去痕与词表
  → publish / schedule
```

库拾深度稿：以 `selfmedia-writing` 管线为准；本 skill 可在 humanizer 前做一轮「口语交错」补强。

## 质量条

- 读起来像**具体的人**，不是百科 + 演讲稿  
- 口语连接是调味，不是灌满  
- 有信息增量，不是纯语气词  
- 通读出声不别扭  

## 禁止

- 「保证 0% AI / 必过朱雀」  
- 无中生有的经历与数据  
- 为降 AI 味变成不可读碎碎念  

## 参考（按需）

| 文件 | 何时 |
|---|---|
| `references/ai-tells-checklist.md` | 改稿前 |
| `references/human-voice-techniques.md` | 手法 |
| `references/prompt-rewrite.md` | 用户要提示词 |
| `references/platform-notes.md` | 指定平台 |
