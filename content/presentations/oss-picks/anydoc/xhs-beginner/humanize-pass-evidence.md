# 人味层执行证据（xhs · 2026-08-14）

> 对象: `humanized.md` · 依据: `skills/prism-produce/references/humanize-techniques.md`（平台差异：
> 小红书开头抓痛点、emoji 克制、分段短、标题有正文兑现）+ `human-voice-prose.md` +
> `scripts/check_human_voice.py`

## 实际执行的改写操作

1. **痛点开场**：首段直接写「同事发来 Word，复制进笔记，标题变乱码…」场景，无问候/铺垫。
2. **标题兑现**：标题承诺「一键变干净 Markdown + 9 天涨 1.5 万星」，正文两处兑现（怎么用、star 快照）。
3. **emoji 克制**：0 个 emoji（小红书 4 卡文案不用 emoji 撑节奏）。
4. **分段短**：一段一意，最长段 3 行。
5. **硬禁令清零**：翻案腔/硬停词/黑话/破折号/叙述冒号全部 0；「一句话能说清：」改为陈述句。
6. **句长打散**：首段加长句（排版像被洗衣机搅过）与短句（二十分钟没了）交错，脚本变异系数警告清零。
7. **诚实边界**：OCR 局限、star 快照、官方速度声明未夸大，全部标注。

## 确定性检查（check_human_voice.py）

- 翻案句 0 / 同构排比 0 / 名词化 0 / 黑话 0 / 硬停词 0 / 模型路标 0 / 洞察路标 0
- 剩余冒号全部为结构固定位：元信息头部 3 处（`form_id:`/`lane:`/`master_ref:`）；
  卡片标注 9 处（`【封面卡…】大字：`/`副标：`/`配文：`，form-xhs 卡片 manifest 固定位）

## 事实约束

- 全部数据只引用 MASTER claims（格式 claim 1–2 / 三入口 claim 3, 11–13 / star 快照 claim 4 /
  MIT claim 5 / WASM 不上传 claim 7 / OCR 边界 claim 8 / CLI claim 10）
- 「9 天」= 创建 08-03 → 检索 08-12 的算术推算，已标注日期
