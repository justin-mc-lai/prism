# Skill Routing（Prism 原生版）

> 本文件为 Prism 路由真值（MAP-009 distill 后的 Prism-native 重写，2026-08-14）。
> 源仓账号默认（kushi-gzh 等）已移除；账号一律走配置（registry/account profile），禁止硬编码。
> bridge 按名调用已安装 skill；缺失 fail-closed（安装通道：`scripts/install_bridges.sh`）。
> 27 个 skill 已 pin 进 `vendor/skills/`（A4 · 2026-08-15，ATTRIBUTION 见
> `docs/ATTRIBUTION-bridges.md`）；仅 rnskill / de-ai-prompt-enhancer /
> ian-xiaohei-illustrations 资产保持 bridge。

## Routing Table

| Need | Primary skill/tool | Output | Gate |
| --- | --- | --- | --- |
| 选题、热点、信息差、近 30 天变化 | `qi_dev.sh intel-radar`（bridge） | `briefing.md`, saved IntelRadar file | evidence gate |
| Creative direction, narrative, presentation map | `prism-director` | treatment, beat sheet, asset continuity, director QC | director gate |
| WeChat 贴图 Tab package | `form-image-post.contract` + `vendor/skills/character-illustrations` 等 | caption, shot list, PNG assets, image-post draft evidence | visual/platform gate |
| Chinese long article / blog | `prism-produce`（writing.contract + prose-core）→ `vendor/skills/humanizer-zh` 等 | `humanized.md` or `body.md` | anti-slop gate |
| Vlog / short video | `prism-director` + `form-av.contract`（vlog 路由） | `script.md`, `storyboard.md`, `edit-plan.md`, 成片占位 | video QA gate |
| Talking-head cut | `AI剪口播`、`ra-local-talking-head-cut`（外部 bridge） | cut plan, subtitles, final video | video QA gate |
| Comic / story visual | `vendor/skills/comic-storyboard`（A4 pin） | comic storyboard/assets | visual continuity gate |
| Cover / editorial visual | `$qi-dev-gemini-image-gen` 无字底图 + `scripts/kushi_cover_text_overlay.py`（✅ 本地 pin，A1） | cover art, poster, editorial key visual | platform visual gate |
| 深度微信贴图（整文纸面分页） | `form-image-post.contract` + `scripts/render_wechat_article_pages.py`（✅ 本地 pin，A1） | warm-paper 1080×1440 pages, caption, presentation | visual/platform gate |
| Image/media upload | `vendor/skills/manage-media`（A4 pin） | media IDs/URLs | platform gate |
| Rendering | render scripts（✅ 本地 pin，`scripts/render_*.py` + `templates/`） | markdown/html/mp4 last-mile files | render gate |
| Draft/publish handoff | `vendor/skills/publish-content`、平台 publish bridge | draft ID, URL, publication record | human approval gate |
| Scheduling | `vendor/skills/schedule-post`（A4 pin） | scheduled job | human approval gate |

## Dynamic Routing Algorithm

1. Read the campaign intent and target account/platform family.
2. Resolve `vertical`, `account`, `pipeline`, and default visual skill from `content/registry.yaml`（配置，无硬编码账号）。
3. If the task starts from topic discovery, route to `qi_dev.sh intel-radar` before director planning.
4. Always route multi-format or visual/video work through `prism-director`.
5. Select one producer path per presentation form（creation-mode-map 路由表）。
6. Route article-paper cover requests to `$qi-dev-gemini-image-gen` 无字底图 + `scripts/kushi_cover_text_overlay.py`（本地 pin）；正文内部视觉路由到对应插画 bridge。
7. Run maker outputs into independent QA（prism-qa），then supervisor review.
8. Route to publish only after `publish-approval.md` allows the requested action（人工二次批准）。

## WeChat 贴图 Tab + 深度整文纸面分页

默认走 Prism 产链（账号配置驱动，无账号默认）：

```text
orchestration kernel（prism-goal 编排）
  → source verify（README / package / setup / 关键命令文件，prism-master）
  → prism-director treatment（可选但推荐）
  → prism-produce（writing.contract + prose-core + human-voice-prose）
  → $qi-dev-gemini-image-gen 无字底图 → scripts/kushi_cover_text_overlay.py（本地 pin，3:4 cover_card）
  → scripts/render_wechat_article_pages.py（本地 pin）
  → caption-short.md + manifest + value-gate / visual QA（prism-qa）
  → supervisor review
  → human approval
  → publish bridge（草稿-only + 人工二次批准）
```

## Vlog Package

```text
orchestration kernel
  → qi_dev.sh intel-radar briefing if needed
  → prism-director（treatment + presentation map + shot list）
  → prism-produce（form-av.contract · script.md + edit-list.md）
  → openmontage / video bridge（AGPL，默认 bridge 不 pin）
  → subtitle/audio/render QA
  → supervisor review
  → human approval
  → platform draft or scheduled publish
```

## Blog / Article Package

```text
orchestration kernel
  → source/briefing（prism-intel → prism-master）
  → prism-director if the angle or multi-platform plan matters
  → prism-produce（writing.contract 体裁选型 + prose-core）
  → humanize 层（human-voice-prose + humanize-techniques + bridge humanizer 族）
  → check_human_voice.py（失败清零，提醒项按裁决表）
  → prism-qa（anti-slop-gate + 事实核对）
  → human approval
  → publish
```

For high-risk topics such as health, legal, finance, or current policy, source verification is a blocking gate.
