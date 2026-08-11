# Publish Approval

Read this before using browser automation, sync-ai, publish API, platform skills, or scheduling.

## Approval States

```text
not-ready
  → release-candidate
  → approved-for-draft | approved-for-image-draft
  → draft-created | image-draft-created
  → approved-for-publish
  → scheduled | published | failed
```

Meanings:

- `not-ready`: any upstream gate failed or assets are incomplete.
- `release-candidate`: supervisor says the package is ready for human review.
- `approved-for-draft`: human approved creating/uploading a platform draft only.
- `approved-for-image-draft`: human approved creating/uploading a WeChat Official Account image-post/贴图 draft only.
- `draft-created`: browser extension/API created a draft and returned evidence.
- `image-draft-created`: browser extension/API created a WeChat Official Account 「贴图」Tab draft and returned evidence.
- `approved-for-publish`: human approved public publish or scheduling for exact endpoints.
- `scheduled`: scheduled job exists.
- `published`: public URL/post ID exists.
- `failed`: failure reason is recorded.

## Human Approval Requirements

Valid approval must include:

- artifact scope: master/presentation or exact file path;
- endpoint scope: account and platform;
- action scope: draft, schedule, or publish;
- timing scope if scheduling;
- acknowledgement of visible preview when public publish is requested.

Ambiguous phrases such as “继续”, “可以了”, or “发一下” are enough for draft upload only if the current task context clearly says draft upload. They are not enough for public publish when multiple endpoints or artifact versions exist.

## Browser Extension / sync-ai Boundary

The external browser plugin is a distribution executor.

It may:

- check connection and login state;
- upload rendered content and media;
- create platform drafts;
- return screenshots, draft IDs, platform metadata, and errors;
- schedule or publish only after explicit approval.

It must not:

- rewrite claims, titles, body, captions, or image text;
- choose new endpoints not in the approval scope;
- click final publish without approval;
- treat preview success as public publish;
- hide platform warnings or content-risk prompts.

### WeChat Official Account Image Post Boundary

When the user says “微信公众号贴图”, “贴图内容”, “小黑贴图”, or “上传贴图”, treat the target as the WeChat draft box 「贴图」Tab:

- use `media_type: image` / `kind: image_post`;
- command path: `scripts/publish-sync-ai.sh --media image` or CLI `--kind image`;
- approval action: `image_draft`, not generic article draft;
- title must be generated separately and kept within 20 Chinese-visible characters;
- caption must be a short image-post description, not the full long-form body;
- capture uploaded image count and file list;
- success evidence must say `草稿·贴图` or instruct checking the 「贴图」Tab.

Do not upload a WeChat image-post package as an article draft unless the user explicitly asks for “文章草稿 / 长文 / 图文文章”. If this happens by mistake, mark the article draft as `superseded-misrouted` and block it from release.

## sync-ai Preflight

Before draft upload:

- Confirm fork extension is loaded from `vendor/selfmedia-sync-ai/packages/extension/dist/` or the source repo.
- Confirm MCP bridge uses `ws://localhost:9528`.
- Confirm the extension service worker is actually connected (`connected: true` / `MCP_STATUS` OK); Chrome being open is not enough.
- If `timeout:no_extension`, `connected:false`, or the bridge stays on `mode: primary`, reload the extension, reopen the MCP settings page in the same Chrome Profile, and reconnect before retrying.
- Confirm token in `.env` matches extension settings.
- Confirm the target platform is logged in within the same Chrome Profile.
- Prefer platform draft mode for WeChat official account and image notes.

## Evidence to Capture

For every draft/publish attempt, capture:

```yaml
job_id:
binding_id:
master_id:
presentation_id:
endpoint_id:
action: draft | image_draft | schedule | publish
status: draft-created | image-draft-created | scheduled | published | failed
artifact_paths: []
platform_draft_id:
platform_post_id:
url:
scheduled_at:
evidence_paths: []
error:
created_at:
```

If the platform returns warnings, validation errors, sensitive-word prompts, failed media upload, or captcha/login prompts, stop and preserve the visible evidence for human decision.
