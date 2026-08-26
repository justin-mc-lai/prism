# LumenX 蒸馏（2026-08-25）

上游：https://github.com/alibaba/lumenx （MIT）— AI 短漫剧一站式生产平台。
本地镜像：`oss-sync/automation/auto/lumenx/`（完整克隆，199M，不入本仓 git）。

## 蒸馏范围

只蒸馏能增强本仓 `ai-manga-drama` 管线的能力；不引入其 FastAPI 后端 / Next.js 前端 / Atelier 画布运行时。

| LumenX 能力 | 蒸馏产物 | 本仓接入点 |
|------|------|------|
| 风格预设库（15 预设 × positive/negative prompt × best_for/avoid_for） | `lumenx-style-presets.json`（原样拷贝） | 分镜资产生成时选风格；打斗类用 `fashion_battle_anime`，武侠用 `chinese_ink_fantasy` |
| 结构化 prompt 组装顺序（prompt_assembly.py） | 见下「组装契约」 | 每镜 asset 生成与 R2V 视频提示词 |
| 运镜词表 MOVEMENT_MAP（14 种主运镜 + 副运镜 + 速度） | 见下「运镜词表」 | storyboard shot 的 camera 字段 |
| `[characterN:name]` R2V 引用标签 | 见下「引用标签」 | Seedance/HappyHorse 类参考生视频请求 |
| 台词口型注入（张嘴说话 cue） | 见下「口型 cue」 | 有对白镜头的视频提示词 |
| 模型目录认知（Seedance/Kling V3/Vidu Q3/Wan/GPT-Image-2/CosyVoice） | 无代码，仅知识 | `request` 选 provider 时参考 |

源码索引（镜像内）：`src/apps/comic_gen/{pipeline,storyboard,prompt_assembly}.py`、`style_presets.json`、`config/model_catalog/`。

## 组装契约（每镜提示词优先级）

```text
视觉描述(核心叙事) → 光照补充 → 运镜 → 景别/角度(未覆盖时) → 角色外观关键词
```

- 各段以「。」连接，去尾部重复标点。
- 角色外观 = 姓名+年龄+性别+服装（无服装则取描述前 60 字）。
- 负面词从所选风格预设的 `negative_prompt` 取。

## 运镜词表

static 固定机位 / push_in 推镜头 / pull_out 拉镜头 / pan_left 左摇 / pan_right 右摇 / tilt_up 上摇 / tilt_down 下摇 / orbit 环绕 / follow 跟随 / crane_up 升镜 / crane_down 降镜 / handheld 手持 / zoom_in 变焦推 / zoom_out 变焦拉。速度：slow 缓慢、fast 快速；副运镜写作「主运镜，同时副运镜」。

打斗镜头推荐组合：快速 push_in（重击特写）、handheld（混战）、orbit（对峙环拍）、follow（追逐）、crane_up（胜负定格收尾）。

## 引用标签（R2V）

参考生视频把参考图当通用槽位：`[characterN:name]` 按角色在前、场景在后编号（character1=第一张参考图）。提示词中角色名出现处就地注入 `{name}[character{n}:{name}]`。本仓 `request` 生成的 segments.references.images 顺序即槽位顺序。

## 口型 cue

有台词的镜头，在视频提示词尾部追加：`{说话人}张嘴说话，表情{情绪}，台词：「{line}」`——作为视觉叙事的一部分，不是独立元数据段。

## 使用方式

写 `storyboard.json` 时：先从 `lumenx-style-presets.json` 选定 preset（记入 episode README），再按组装契约逐镜写 description 与运镜；生成静帧用 preset.positive_prompt 作为风格后缀、negative_prompt 作负面词。其余校验/QA/合成仍走 `scripts/ai_manga_drama.py`，本文件不改六阶段契约。
