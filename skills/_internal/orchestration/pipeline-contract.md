# Pipeline Contract

Use this contract when creating or auditing a self-media campaign dossier.

## First-Principles Object Model

```text
SourceSignal
  → MasterContent
  → PresentationVariant
  → DistributionBinding
  → DistributionJob
  → Publication
  → MetricsSnapshot / Retrospective
```

Definitions:

- `SourceSignal`: trend, source article, document, video, user draft, or Intel Radar briefing.
- `MasterContent`: factual and narrative authority for a slug.
- `PresentationVariant`: blog/article/vlog/short-video/thread/carousel/comic translation of the master.
- `DistributionBinding`: connects one presentation to one account/platform endpoint.
- `DistributionJob`: one attempt to draft, schedule, publish, retry, or fail.
- `Publication`: real platform outcome with draft ID, post ID, URL, failure reason, and metrics.

## Recommended Dossier Layout

```text
content/masters/{vertical}/{slug}/
  meta.yaml
  briefing.md
  MASTER.md
  humanized.md
  assets/

content/presentations/{vertical}/{slug}/{presentation_slug}/
  presentation.yaml
  body.md
  script.md
  storyboard.md
  edit-plan.md
  shot-list.md
  assets/
  qa/
    director-qc.md
    anti-slop.md
    visual-qa.md
    supervisor-review.md
    release-approval.md

content/distribution/campaigns/{campaign_id}.yaml
content/distribution/bindings/{binding_id}.yaml
content/storyworlds/{world_slug}/
  world.yaml
  bible.md
  canon-ledger.yaml
  characters/
  timeline/
  episodes/{episode_id}.yaml
content/publications/{platform}/{account}/{slug}/{publication_id}.yaml
```

Only create files that match the requested output forms. For a WeChat 贴图 Tab package（账号角色 IP 走配置，如 shot-list 角色卡）, `shot-list.md`, `assets/`, `visual-qa.md`, `supervisor-review.md`, and `release-approval.md` are more important than video files. Keep `body.md` only if there is a companion article or source text. For a vlog, `script.md`, `storyboard.md`, `edit-plan.md`, subtitles, and render evidence are required.

## State Machine

```text
idea
  → briefed
  → directed
  → generated
  → qa-needs-fix | qa-pass
  → supervisor-needs-fix | release-candidate
  → human-approved-draft | human-approved-image-draft | human-approved-publish
  → draft-created | scheduled | published | failed
```

Rules:

- `idea → briefed` requires source material or Intel Radar briefing.
- `briefed → directed` requires a director treatment or a labeled reason for skipping director.
- `directed → generated` requires a presentation map and asset assumptions.
- `generated → qa-pass` requires evidence for text, visual, platform, and source checks.
- `generated → qa-pass` for story episodes also requires `canon_gate_status=passed`.
- `qa-pass → release-candidate` requires supervisor review.
- `release-candidate → human-approved-*` requires explicit human approval.
- `human-approved-draft` permits draft upload only.
- `human-approved-image-draft` permits WeChat Official Account 「贴图」Tab draft upload only. It must use `media_type: image` / `kind: image_post`; generic article draft upload is not allowed for this state.
- `human-approved-publish` permits public publish or scheduling within the approved scope.
- `lane=canon` disables `fast_lane_skip`.
- It is illegal for a StoryMaster episode with `canon_gate_status=review_required` or `failed` to enter `generated`.

## Minimal `presentation.yaml`

```yaml
schema_version: "1"
presentation_id: "{vertical}/{slug}:{form}:{angle}:v1"
master_id: "{vertical}/{slug}"
form: blog_article | wechat_article | short_video_vlog | talking_head_video | thread | carousel | comic_story
language: zh-CN
target_profiles: []

director:
  core_intent: ""
  audience: ""
  narrative_viewpoint: ""
  conflict: ""
  emotional_curve: []

outputs:
  primary: body.md
  assets_dir: assets/
  renderable: false

constraints:
  max_new_claims: 0
  source_trace_required: true
  human_approval_required: true
```

## Minimal `release-approval.md`

```yaml
status: pending # pending | approved | rejected
approved_by:
approved_at:
scope:
  presentations: []
  endpoints: []
  allowed_actions: [] # draft | image_draft | schedule | publish
notes:
```
