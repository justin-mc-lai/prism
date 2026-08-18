# 节气养生垂直领域 · 导演 Treatment 模板（Prism 蒸馏版 v1）

> Internal reference for `prism-director`. Not host-discoverable.
> 蒸馏自 selfmedia-creator `skills/selfmedia-director/references/jieqi-yangsheng-treatment-template.md`（自研）。
> 适用：`jieqi-yangsheng` 垂直长跑题材——一年 24 个节气 + 三伏/三九等节点，每节点一篇。
> 账号绑定走配置（registry/account profile），本模板不硬编码账号名。

## 0. 内部边界（永远不进公开产物）

- 内部定位、目标人群标签、运营公式、变现词：只写 registry / account contract / 本模板。
- 公开品牌与公开产物禁止出现以上内容。

## 1. 每篇 treatment 必填字段

```yaml
series: jieqi-yangsheng
episode: <节气名>-<年份>-<序号>        # 例：liqiu-2026-01
node: <节气/节点>                       # 例：立秋（2026-08-07）
days_to_next_node: <天数>               # 例：距末伏 7 天
core_intent: <读者看完后的一个行动>       # 例：照单买菜，把三样吃对
audience_promise: <一句话承诺，受众视角>
conflict: <节气带来的具体矛盾>           # 例：立秋≠凉快，暑湿还在
calendar_facts:                         # 必须 lunar-python 核算
  - <日期/农历/干支/节气/三伏等>
keywords: [扶阳, 祛湿, 健脾, ...]       # 功效关键词（内部参考）
formula_blocks:                         # 爆款公式（内部参考，不进公开产物）
  - 俗语开头
  - 节气节点
  - 功效关键词
  - 数字菜品
  - 古籍引文 + 白话
  - 当日日历 + 宜忌
  - 应时活动
```

## 2. 标准卡组（8 卡）

| seq | 卡 | 必带 |
| --- | --- | --- |
| 01 | cover_card | 俗语 + 数字承诺 |
| 02 | calendar_card | 日期/节气/农历/干支/距下节点；宜 3 + 忌 3 |
| 03 | principle_card | 节气古训；古籍引文 + 白话 |
| 04-06 | ingredient_card ×3 | 食材—克数—做法—注意；古籍引文 + 白话 |
| 07 | seasonal_card | 古典人物应时活动（文生图）；宜动忌懒；引文 + 白话 |
| 08 | takeaway_card | 清单 + 三不边界 + 免责 |

## 3. 资产连续性契约

- 视觉 DNA：水墨/工笔、宣纸底 `#f7f2e6`、朱砂印章；底图无文字。
- 字体：标题 Songti 系，正文宋体/黑体混排；正文要点 ≥ 30px，白话 ≥ 27px。
- 背景池：`content/series/jieqi-yangsheng/assets/bg/`，每节气新增 1-2 张。
- 古籍引文库：`content/sources/tcm/`，原文逐字核对，禁转译当原文。
- 俗语库/食材库/宜忌库：系列圣经 `content/series/jieqi-yangsheng/bible.md`（Prism 内待长跑题材启动时创建）。

## 4. 生产门禁（导演 QC）

1. 受众视角复读：无内部定位/公式/运营词。
2. 古籍核对：引文原文逐字核对 + 白话准确。
3. 日历核对：lunar-python 核算日期/节气/农历/干支。
4. OCR：底图无文字、卡片无乱码、无截断。
5. 合同校验：1080×1440；页脚 public_brand；0 errors。

## 5. 多平台变体（同题材后续分发）

| 平台 | 变体 | 复用资产 |
| --- | --- | --- |
| 公众号 | 贴图 8 卡 → 长文（可选） | 卡组文字 + 引文 |
| 头条/百家号 | 文章版：引文原文段落化 | 卡组文字 |
| 知乎 | 问答/文章版：节气食养原则展开 | principle + 引文 |
| 小红书 | 图文 3-4 张：封面 + 宜忌 + 食谱 | 卡 02/04-06 |
| 抖音/视频号 | 短视频：口播 + 底图轮播 | seasonal_card + 卡组 |

平台账号与凭证状态见系列圣经「多平台矩阵」；未配置凭证的平台不强行发布。
