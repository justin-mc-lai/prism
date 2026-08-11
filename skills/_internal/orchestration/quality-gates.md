# Quality Gates

Use this reference for release readiness and supervisor review.

## Gate 0: Evidence / Topic Gate

Pass when:

- Topic source, draft path, or Intel Radar briefing exists.
- Current facts include concrete dates and source trace.
- Intel Radar output separates 现象, 不变量, 变量/噪声, 信息差, 可行动, 不确定.

Block when:

- Claims rely on “网上都说 / 有人反馈 / 数据显示” without a named source.
- The topic is current, legal, visa/travel, medical, or financial and sources were not verified.
- The briefing fabricates comments, metrics, platform posts, or trend strength.

## Gate 1: Director Gate

Pass when:

- Core intent, target audience, narrative viewpoint, conflict, and emotional curve are explicit.
- Presentation map states which outputs are blog/vlog/article/thread/carousel/comic.
- Beat sheet or shot list is executable.
- Asset continuity marks available, missing, generated, and forbidden assets.
- Director QC has pass/fix/block status.

Block when:

- The plan is a list of formats without a unifying audience effect.
- Video/visual work assumes unavailable footage, rights, or characters.
- Platform adaptation changes the factual claim.

## Gate 2: Text Anti-Slop Gate

Pass when:

- The draft sounds like a specific account/person, not a generic AI explainer.
- `no-ai-slop`, `selfmedia-humanize`, or `humanizer-zh` has been applied or consciously skipped with reason.
- Empty summaries, fake-profound endings, throat-clearing, generic “信息差” bragging, and fake expertise are removed.
- Personal details are real or marked as placeholders.

Block when:

- The draft invents experience, numbers, sources, or user stories.
- The draft promises “必过 / 必涨 / 必会”.
- The draft reads like a template with uniform sentence rhythm and decorative formatting.

## Gate 3: Visual / Image Gate

Pass when:

- Aspect ratio and canvas match the platform.
- Visual IP is stable: for 小黑, black body, white-dot eyes, thin legs, blank serious expression, and not a cute mascot.
- The character participates in the core action, not as decoration.
- Any visible Chinese text is short, readable, and semantically correct.
- OCR/manual inspection finds no乱码, duplicate labels, accidental “小黑” label, random English, misspellings, or unrelated text.
- Arrows, labels, and state boxes match the shot list.
- The image is not a PPT slide, dense flowchart, copied old composition, screenshot-looking UI, or overfilled canvas.

Block when:

- Text is unreadable or wrong in a way readers will notice.
- The generated image contains unintended labels like “小黑”.
- The character scale/style changes enough to look like a different IP.
- The image contradicts the article.

## Gate 4: Platform / Render Gate

Pass when:

- Title, subtitle, cover, excerpt, tags, image dimensions, video aspect ratio, and file format satisfy the target platform profile.
- For WeChat image_post, title is short and separate from caption; caption is not a title rewrite; uploaded image count matches the manifest/shot list.
- Rendered markdown/html/mp4 exists at the expected path.
- Platform-specific overrides do not alter facts.
- Draft upload inputs are complete.

Block when:

- Required cover, title, summary, media IDs, or render file is missing.
- WeChat image_post title is empty, caption is a title rewrite, or uploaded image count does not match the manifest/shot list.
- Render output has broken images, invalid relative paths, or mismatched assets.
- Account/platform endpoint is ambiguous.

## Gate 5: Supervisor Review

The supervisor must review as an independent checker.

Required verdict:

```yaml
verdict: pass | needs_fix | block
reviewed_at:
reviewer: supervisor
scope:
  master_id:
  presentation_id:
  endpoints: []
checks:
  evidence:
  director:
  text:
  visual:
  platform:
  compliance:
blockers: []
fixes: []
publish_allowed: false
```

Pass only when all blocking gates have passed. `publish_allowed` remains false until human approval is recorded.

## Gate 6: Human Approval Gate

Pass when:

- The user has reviewed the release candidate or platform draft preview.
- Approval names the action: draft upload, schedule, or public publish.
- Approval names the scope: exact presentation and endpoints.

Block when:

- The user gave general intent such as “继续” but did not approve public publish.
- The artifact changed after approval.
- The platform preview has not been checked after browser-plugin upload.

## Gate 7: Publication Record Gate

Pass when:

- Draft ID, platform post ID, URL, schedule time, or failure reason is recorded.
- Publication links back to `master_id`, `presentation_id`, `endpoint_id`, and `binding_id`.
- Metrics snapshot plan exists for follow-up.

Block when:

- The publish step failed silently.
- A platform draft is reported as published.
- No URL/ID/failure reason is captured.
