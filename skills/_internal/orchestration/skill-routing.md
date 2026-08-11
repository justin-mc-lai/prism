# Skill Routing

Use this reference when selecting specialist skills for a campaign.

## Routing Table

| Need | Primary skill/tool | Output | Gate |
| --- | --- | --- | --- |
| 选题、热点、信息差、近 30 天变化 | `$qi-dev-intel-radar` | `briefing.md`, saved IntelRadar file | evidence gate |
| Creative direction, narrative, presentation map | `selfmedia-director` | treatment, beat sheet, asset continuity, director QC | director gate |
| WeChat 贴图 Tab package with 小黑 illustrations | `selfmedia-account-pipeline` + `ian-xiaohei-illustrations` | caption, shot list, PNG assets, image-post draft evidence | visual/platform gate |
| Chinese long article / blog | `selfmedia-writing`, `selfmedia-humanize`, `humanizer-zh`, `no-ai-slop` | `humanized.md` or `body.md` | anti-slop gate |
| Vlog / short video | `ra-video-production-director`, `openmontage`, video skills | `script.md`, `storyboard.md`, `edit-plan.md`, mp4 | video QA gate |
| Talking-head cut | `AI剪口播`, `ra-local-talking-head-cut`, `ra-audio-to-subtitles` | cut plan, subtitles, final video | video QA gate |
| Comic / story visual | `comic-storyboard` | comic storyboard/assets | visual continuity gate |
| Cover / editorial visual | article-paper 默认 `$qi-dev-gemini-image-gen` 无字底图 + `scripts/kushi_cover_text_overlay.py`；`punk-cover` 仅显式备选 | cover art, poster, editorial key visual | platform visual gate |
| 库拾深度微信贴图（整文纸面分页） | `selfmedia-account-pipeline` + `scripts/kushi_wechat_article_image_post.sh` | warm-paper 1080×1440 pages, caption, presentation | visual/platform gate |
| Image/media upload | `manage-media` | media IDs/URLs | platform gate |
| Rendering | render scripts / platform renderer | markdown/html/mp4 last-mile files | render gate |
| Draft/publish handoff | `publish-content`, platform publish skills, `publish-sync-ai`, publish API | draft ID, URL, publication record | human approval gate |
| Scheduling | `schedule-post` | scheduled job | human approval gate |

## Dynamic Routing Algorithm

1. Read the campaign intent and target account/platform family.
2. Resolve `vertical`, `account`, `pipeline`, and default visual skill from `content/registry.yaml`.
3. If the task starts from topic discovery, route to `$qi-dev-intel-radar` before director planning.
4. Always route multi-format or visual/video work through `selfmedia-director`.
5. Select one producer path per presentation form.
6. Route article-paper cover requests to `$qi-dev-gemini-image-gen` 无字底图 + `scripts/kushi_cover_text_overlay.py`；只有显式指定时走 `punk-cover`；正文内部视觉路由到对应插画 skill。
7. Run maker outputs into independent QA, then supervisor review.
8. Route to publish only after `release-approval.md` allows the requested action.

## WeChat Official Account 贴图 Tab + 库拾整文纸面分页（默认深度稿）

`kushi-gzh` 深度 OSS 核对默认走这条（`pm-skills` v4 已验收固化）：

```text
selfmedia-production-pipeline
  → source verify (README / package / setup / 关键命令文件)
  → selfmedia-director treatment（可选但推荐）
  → skills/human-writing → renders/.../{slug}.md
  → $qi-dev-gemini-image-gen 无字底图 → scripts/kushi_cover_text_overlay.py（3:4 cover_card）
  → scripts/kushi_wechat_article_image_post.sh
       （render_wechat_article_pages.py + diagrams.yaml 可选）
  → caption-short.md + presentation.yaml + value-gate / visual QA
  → supervisor review
  → human approval
  → publish-sync-ai.sh --media image（贴图 Tab）
```

日榜短卡或明确要白底信息图时，才改走 `kushi-oss-portrait-white-infographic`。

## WeChat Official Account 贴图 Tab + 小黑 Package

Use this package for WeChat Official Account 草稿箱「贴图」Tab content like the EVUS example:

```text
selfmedia-production-pipeline
  → qi-dev-intel-radar briefing if topic/research is needed
  → selfmedia-director treatment + presentation map
  → selfmedia-account-pipeline shot list
  → punk-cover for cover if the package needs a cover/hero visual
  → ian-xiaohei-illustrations image generation
  → visual QA / OCR / no乱码 check
  → supervisor review
  → human approval
  → sync-ai image-post draft upload (`--media image` / `--kind image`)
```

The account adapter owns the shot-list, asset naming convention, 1-9 image limit, short title, caption, and the “title/caption are metadata, not content” rule. The production pipeline owns the gates and publish boundary. Do not route “上传贴图” to a generic WeChat article draft unless the user explicitly asks for a long-form article draft.

## Vlog Package

```text
selfmedia-production-pipeline
  → qi-dev-intel-radar briefing if needed
  → selfmedia-director or ra-video-production-director
  → script.md + storyboard.md + edit-plan.md
  → openmontage / video generator / cut skill
  → subtitle/audio/render QA
  → supervisor review
  → human approval
  → platform draft or scheduled publish
```

The director decides the audiovisual treatment. Video generators execute; they do not change the content claim.

## Blog / Article Package

```text
selfmedia-production-pipeline
  → source/briefing
  → selfmedia-director if the angle or multi-platform plan matters
  → selfmedia-writing or writing-agent
  → selfmedia-humanize / humanizer-zh
  → no-ai-slop detect/edit
  → render
  → supervisor review
  → human approval
  → publish
```

For high-risk topics such as visa, legal, medical, finance, or current policy, source verification is a blocking gate.
