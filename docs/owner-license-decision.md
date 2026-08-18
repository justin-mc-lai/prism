# 所有者 License 决策模板（Prism 退役前置项）

> 状态：**待所有者决策**（2026-08-14）
> 用途：源仓 `selfmedia-creator` 无 LICENSE 文件。Prism 退役（源仓降级只读、移除 bridge
> 回源路径）前，所有者需对以下自研资产给出明确的 license 声明。勾选即视为决定，记录在本文件。

## 决策项 A：渲染/证据脚本族 + templates

涉及：

- `scripts/render_wechat_html_cards.py`、`scripts/kushi_cover_text_overlay.py`、
  `scripts/kushi_wechat_article_image_post.sh`、`scripts/render_spec_kit_wechat_cards.py`、
  `scripts/render_superpowers_wechat_cards.py`、`scripts/render-channel.sh`
- `scripts/lib/readability-lint.py`、`scripts/lib/record-humanize-evidence.py`、`scripts/lib/kit_render.py` 等 lib
- `templates/`（96K：jieqi-yangsheng-classical / kushi-wechat-article-post / kushi-wechat-image-post / wechat-card-kit）

选项：

- [ ] **A1 · MIT 声明**：上述自研脚本与模板以 MIT 许可授权 Prism 使用与再分发。
  后果：Prism 可按 MAP-006 vendor_pin，贴图渲染链解除对源仓依赖（可直接退役渲染桥）。
- [ ] **A2 · 自用私有许可**：仅授权 Prism 仓（同一所有者）内部使用，不对外再分发。
  后果：Prism 可 pin 但不对外公开发布；公开发布仍需 bridge + 人工批准。
- [ ] **A3 · 维持现状**：不声明。后果：保持 bridge + 显式占位，退役条件 a) 不满足。

## 决策项 B：AV 大栈

- OpenMontage（AGPL-3.0）：bridge 使用合规；**不 pin**（避免 AGPL 传染分发面）。
  - [ ] B1 · 确认维持 bridge（推荐，无需额外动作）
  - [ ] B2 · 要求 license review 后 pin（需人工批准 + ATTRIBUTION + 完整 AGPL 义务评估）
- rnskill（CC BY-NC 4.0）：商业场景禁止 pin/复制。
  - [ ] B3 · 确认仅 bridge 引用（推荐）

## 记录

- decided_by: human（用户指令「选 A1」，2026-08-14）
- decided_at: 2026-08-14
- decisions: A1（渲染脚本族 + templates 以 MIT 授权 Prism 使用与再分发）/ B1（OpenMontage 维持 bridge）

## 追加决策 A4（2026-08-15 · human 指令「把可 pin 的（MIT 类的上游 + 自研脚本）也 pin 进仓」）

- decided_by: human
- decided_at: 2026-08-15
- decisions:
  - A4-1：源仓自研 skill 逻辑（17 个 `selfmedia-*` / `kushi-*` / `oss-repo-read` /
    `analyze-data` / `create-content` / `manage-media` / `publish-content` /
    `schedule-post` / `x-publish` / `selfmedia-agent-reach` + `ian-xiaohei-illustrations`
    逻辑部分）以 MIT 授权 Prism 使用与再分发。
  - A4-2：MIT 上游 skill（humanizer-zh / qu-ai-wei / shuorenhua / no-ai-slop /
    stop-slop / humanizer-en / writing-agent / comic-storyboard /
    character-illustrations）按各自 LICENSE 以 ATTRIBUTION 随附方式 pin。
  - A4-3：保持 bridge（license 不允许或不明）：`rnskill`（CC BY-NC 4.0 非商业）、
    `de-ai-prompt-enhancer`（无 LICENSE 声明）、`ian-xiaohei-illustrations/assets`
    （13M 示例资产，逻辑已 pin）。

## 追加决策 A5（2026-08-15 · human 指令「rnskill、de-ai-prompt-enhancer、ian-xiaohei 一起」）

- decided_by: human
- decided_at: 2026-08-15
- decisions:
  - A5-1：`ian-xiaohei-illustrations` 整包（含 13M assets，自研）MIT 授权 pin。
  - A5-2：`de-ai-prompt-enhancer` 完整 pin，随附 NOTICE 标注 license 缺失风险；
    公开发布前须向上游确认 LICENSE。
  - A5-3：`rnskill` 以 CC BY-NC 4.0 合规方式 pin（仅合规层：SKILL/LICENSE/CREDITS/
    README/VERSION + NOTICE 非商业守卫）；96M skills 子树保持 archive-only 回源引用。
- 结果：29 个 bridge 全部 pin 或守卫化，**bridge 数量清零**。

## A1 落地包（预置 · 勾选 A1 后直接执行）

预置 ATTRIBUTION 草稿（MIT 路径 pin 时随附，路径以源仓为准）：

```text
Prism 贴图渲染链 · MIT ATTRIBUTION
----------------------------------
以下脚本与模板由 Prism 所有者（selfmedia-creator 源仓）以 MIT 许可授权本仓再分发：
- scripts/render_wechat_html_cards.py            （源仓 scripts/render_wechat_html_cards.py）
- scripts/kushi_cover_text_overlay.py            （源仓 scripts/kushi_cover_text_overlay.py）
- scripts/kushi_wechat_article_image_post.sh     （源仓 scripts/kushi_wechat_article_image_post.sh）
- scripts/render_spec_kit_wechat_cards.py        （源仓 scripts/render_spec_kit_wechat_cards.py）
- scripts/render_superpowers_wechat_cards.py     （源仓 scripts/render_superpowers_wechat_cards.py）
- scripts/lib/readability-lint.py                （仅参考；Prism 已用原生 check_readability.py 替代）
- templates/（jieqi-yangsheng-classical / kushi-wechat-article-post /
  kushi-wechat-image-post / wechat-card-kit）
授权日期：____（勾选 A1 时填写）
```

勾选 A1 后执行路径：`docs/retirement-execution-checklist.md` 分支 A。
