# Intel Briefing Schema（Prism 蒸馏版）

> Internal reference for `prism-intel`. Not host-discoverable.
> 蒸馏自 selfmedia-creator 选题雷达族（MAP-003/010 distill）：`selfmedia-topic-radar` /
> `selfmedia-newsnow` / `selfmedia-last30days` / `selfmedia-zhihu-hot` / `selfmedia-tl1`。
> 样本依据：`content/briefings/anydoc-hotspot.md`（2026-08-12 真实产出）。

## 产出位置

- `content/briefings/{slug}-hotspot.md`（单篇）或 `content/briefings/{campaign_id}/{period}.md`（战役期）
- 证据：`.beacon/evidence/implement/prism-intel/`（可选，证据行内亦可）

## 必填字段

```yaml
mode_id: brief-intel
public_id: intel
lane: standard|fast|canon
recommended_next_harness: master
map_ids_considered: ['MAP-003', 'MAP-010']
```

## 正文结构（六段）

1. **来源与检索时刻**：数据源（GitHub API / 平台接口 / 爬取快照）、检索时间；快照类数据必须标注「检索时刻」。
2. **热点结论**：一屏内给出「谁、多快、多少」的可核验结论（示例：firecrawl/anydoc 为本周新建仓库 star 增速第一梯队）。
3. **选题角度**：1–3 个候选角度；每个角度给「受众 + 信息差」（大多数人不知道什么）。
4. **证据**：可复核链接/路径 + 检索时刻 + 风险提示（star 会变、官方声明非实测等）。
5. **不编造门**：趋势与指标只来自检索结果；无来源的「趋势判断」必须显式标注为推测。
6. **下一步**：`recommended_next_harness: master`（冻结事实）或直接给快照路径。

## 选题角度 + 标题公式建议（衔接 title-lab）

每个「选题角度」后附一行标题方向，帮助 plan 阶段兑现「定角度、受众、风险、爆款公式」：

```yaml
title_hint:
  angle: <一句话角度>
  audience: <身份词，如 独立开发者 / 上班族>
  formula_candidates: [数字清单, 速成教程]   # 2 个以内，具体公式见 title-lab.md
  produce_handoff: title-lab 出候选标题（路径 A/B）
```

规则：

- intel 只给公式/方向建议，不产出最终标题；最终候选由 `prism-produce` 的
  `skills/prism-produce/references/title-lab.md` 生成并过标题门。
- 建议公式必须落在 title-lab 七型公式内；拿不准时省略，不硬凑。
- 公式建议不豁免不编造门：标题要素（数字/社会证明）仍是后续检索事实，不是编造素材。

## 硬边界

- 不编造趋势与指标（public-surface hard gate）。
- 数据快照必须带检索时刻；变化型数据（star/榜单）禁止写成恒久事实。
- 选题角度可以多给，但每个角度必须落到「能查证的事实面」，不许空转。
- bridge 缺失（qi_dev.sh 不可用）时输出 missing-evidence 标签并停止，不虚构雷达结果。

## 多源聚合（MAP-010）

「不知道写什么」时按序聚合：

1. `qi_dev.sh intel-radar deep-plan "<topic>" --save`（第一性原理 briefing）
2. 中文讨论热度：`selfmedia-zhihu-hot`（bridge）
3. 中文圈传播：`selfmedia-tl1`（bridge）
4. 新闻由头：`selfmedia-newsnow`（bridge）
5. 有明确话题再深挖：`selfmedia-last30days` + `selfmedia-agent-reach`（bridge）

默认收敛口径：中文区、可评论、近 7 日热、不限垂类；平台/方向未给时不再追问超过 2 问。

跨期自我进化闭环（学→做→反、事件级去重、人工管配置、表现反哺选题）见
`references/topic-radar.md`；本 schema 只负责单次快照。
