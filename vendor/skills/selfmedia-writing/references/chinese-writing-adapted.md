# chinese-writing 精华（库拾适配）

**来源：** [miantiao-me/aigc-weekly — chinese-writing](https://github.com/miantiao-me/aigc-weekly/blob/master/agent/.opencode/skills/chinese-writing/SKILL.md)  
**许可：** 遵循上游仓库；本文件为摘要与库拾场景裁剪，非逐字拷贝。

## 采纳项

| 上游章节 | 库拾用法 |
|----------|----------|
| 简单 / 人性化 / 清晰 | 与 humanizer-zh、prose-core 五原则一致 |
| 2.1 基本原则（说话、一句一意、倒金字塔、主动、正面） | **prose-core.md 正文** |
| 去 AI 味六原则 | **humanizer-zh** 终检执行 |
| 4.2 简化词池 | 写入 readability-lint 与编辑自检 |
| 5.3 条目撰写（产品/开源结构） | 深度稿「是什么」小节 |
| 7.x AI 陷阱表 | humanizer 阶段对照 |
| 9. 快速检查清单 | `references/checklist.md` |

## 未采纳 / 裁剪

| 上游 | 原因 |
|------|------|
| 5. 周刊写作专项（15 字标题等） | 库拾标题由 `meta.yaml` + 渠道 template 生成，不单设周刊体 |
| 表情符号禁令 | 库拾已禁止营销 emoji 标题 |
| 纯评论煽情 | 库拾偏开源解读，重事实与可操作建议 |

## 安装上游（可选）

```bash
npx agent-skills-cli install @miantiao-me/chinese-writing
```

库拾 **不依赖** 上游安装；本仓库 `selfmedia-writing` 已内联必要条文。需要周刊体扩展时可只读上游 SKILL 作参考。
