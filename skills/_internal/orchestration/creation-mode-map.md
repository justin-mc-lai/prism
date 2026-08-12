# Creation Mode Map（操作表）

执行时按「创作类型 → 六个 harness」路由。每一步交付必须带 `mode_id` 与 `recommended_next_harness`，禁止越界自证。

## 路由总表

> Lake D1（writing base）：成稿实现列统一引用 `contracts/writing.contract.md`（体裁选型 + 文笔五原则 +
> fail-closed bridge），QA 列统一引用 `skills/prism-qa/references/anti-slop-gate.md`（MAP-005 distill+bridge）。

| 创作类型 | plan | truth | design | implement | qa | release |
| --- | --- | --- | --- | --- | --- | --- |
| blog 深度长文 | intel-radar / 角度 | MASTER + 来源核对 | selfmedia-director treatment | form-blog.contract（writing.contract 四段式）+ bridge humanizer 族 | anti-slop-gate + 事实核对 | 人工批准 → 文章草稿 |
| 贴图包 article-paper | 选题/节点 | MASTER + 核对 | director + shot list（visual_carrier） | writing.contract + render_wechat_article_pages | anti-slop-gate + OCR + contract-check | publish-sync-ai --media image |
| 贴图包 短卡 | 热点雷达 | 快照 | director（可选） | writing.contract（倒金字塔）+ render_wechat_html_cards / image_cards | anti-slop-gate + OCR + 合同 | publish-sync-ai |
| vlog 口播 | 话题/受众 | 脚本事实清单 | ra-video-production-director | writing.contract 口播稿 + TTS/分镜/剪辑 | anti-slop-gate + 视频 QA | 视频草稿 |
| X thread | 选题 | 事实 | director（可选） | form-thread.contract（writing.contract 倒金字塔）+ bridge writing-agent | anti-slop-gate | sidepilot |
| 小红书图文 | 选题 | 事实 | director + 版式 | writing.contract emotional-essay + xhs-article-to-images | anti-slop-gate + OCR | xhs-content-ops |
| 节气养生长跑题材（jieqi-yangsheng） | 节气排期表 + 俗语/食材/引文库 | MASTER + 古籍原文逐字核对 + lunar-python 日历核算 | selfmedia-director 节气模板（8 卡）+ shot list | writing.contract + 文生图古典底图 + render_wechat_html_cards | anti-slop-gate + 受众复读 + 古籍/日历核对 + OCR + 合同 | 公众号贴图草稿；后续按平台矩阵派生文章/短视频 |

## mode 契约模板（每个产物头部）

```yaml
mode_id: design-carousel
creation_type: image-post
output_contract:
  - director-treatment.md
  - presentation-map.yaml
  - shot-list.md
hard_gate: "只出方案，不写正文、不渲染、不发布"
recommended_next_harness: implement
```

## 六个 harness 的职责边界

- plan：定角度、受众、风险、爆款公式；**不**冻结事实、**不**写稿。
- truth：冻结 MASTER 事实与来源；**不**代生成方决定呈现。
- design：导演 treatment / presentation map / shot list；**不**写正文。
- implement：写作/生成/渲染；**不**自证合格。
- qa：反 slop、OCR、合同、导演 QC、受众视角复读（逐卡以读者身份检查内部定位/公式/运营词泄漏）；**不**改写事实来放行。
- release：监制 + 人工批准 → 草稿；公开发布必须再次明确批准。

## 健康/合规类内容额外门

新号 `jieqi-yangsheng-gzh` 合同要求：免责声明、禁止疗效承诺、个体差异提示、知识库出处待核对。通用执行：风险类内容（health/legal/finance/current-news）在 truth 阶段必须过来源核对，否则 implement 不得开始。

## 长跑题材（Series）编排

节气养生是日历驱动的长跑题材：一年 24 个节气 + 三伏/三九等节点，每节点一篇，可持续导演编剧。库拾（oss-picks）是发现驱动的长跑题材：按 trending 仓库持续产出，可叠加日榜/深度/主题月。

长跑题材必须额外维护：

1. **系列圣经**：`content/series/{vertical}/bible.md`（排期、资产池、俗语/食材/引文库、多平台矩阵、复盘）。
2. **单篇战役**：仍走 master → treatment → shot list → render → qa → release；每篇在圣经里登记 episode 序号。
3. **资产连续性**：同一题材的视觉 DNA、字体、背景池、角色/意象跨期复用，禁止每篇重新发明风格。
4. **多平台派生**：公众号贴图为默认首发；文章/短视频/小红书变体在 release 前按矩阵派生，凭证未配置的平台不强行发布。

节气养生模板：`skills/selfmedia-director/references/jieqi-yangsheng-treatment-template.md`；圣经：`content/series/jieqi-yangsheng/bible.md`。
