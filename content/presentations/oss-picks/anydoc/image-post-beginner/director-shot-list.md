# Director Shot List — anydoc · image-post-beginner（样例）

> 样例产物，用于 form_samples 结构校验；不承载可发布主张。
> 上游：`content/masters/oss-picks/anydoc/MASTER.md`（本样例无真实母稿，标注 scaffold）。

```yaml
mode_id: design-carousel
creation_type: image-post
form_id: image-post
presentation_id: anydoc-image-post-beginner
visual_carrier: image-post
hard_gate: "只出方案，不写正文、不渲染、不发布"
recommended_next_harness: produce
```

## 核心意图

一张卡一个意思，六张卡讲完"内容与版式分离"这一件事。

## 观众承诺

看完六张卡，能自己跑通一次贴图渲染。

## 卡片节拍

| seq | role | 这一张干什么 | 凭什么让人看下一张 |
|---|---|---|---|
| 1 | cover | 给结论：一份内容，三种格式 | 承诺有可复制的做法 |
| 2 | pain | 抓痛点：同一份内容改三遍 | 引出"能不能只写一遍" |
| 3 | idea | 给思路：内容与版式分离 | 引出"具体怎么落" |
| 4 | how | 给步骤：三步跑通 | 引出"哪里会翻车" |
| 5 | pitfall | 给坑点：三个常见错误 | 引出"现在就能试" |
| 6 | action | 给动作：命令 + 提醒 | — |

## 视觉载体

- 版式：`templates/kushi-wechat-image-post`（竖版 1080×1440）
- 视觉档位：`kushi-oss-portrait-white-infographic`
- 每卡一色，cover 用蓝，痛点用橙，坑点用红

## 生产现实

- available_assets：模板 CSS、渲染脚本
- missing_assets：真实母稿与来源核对（本样例标注 scaffold）
- ai_visuals_allowed：否（本形态为版式渲染，非 AI 生图）
- approval_needed_before_generation：否（样例）

## Non-Goals

- 不做真实项目背书；不写来源主张
- 不发布

## Next Gate

- gate: treatment-approval
- if_approved_next: produce（渲染）
