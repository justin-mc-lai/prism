# Adapter migration matrix — MAP-001…009
#
# Authority: Lake A Source Skill Inventory → Lake B index → Lake B′ migration policy
# Companion: registry/adapter-index.yaml
# Consumer: skills/prism-goal (and later public surfaces)
#
# Strategies:
#   bridge     — call stable external/local command or skill path; do not copy
#   distill    — extract reusable norms/checklists/scripts into Prism internals
#   vendor_pin — copy/pin under vendor/ with ATTRIBUTION (Lake D+, license gate)
#   defer      — explicitly out of current lake

| map_id | source (selfmedia-creator) | prism landing | strategy now (B′) | deepen lake | distill target (if any) | bridge surface (if any) | vendor_pin (if any) | status |
|--------|----------------------------|---------------|-------------------|-------------|-------------------------|-------------------------|---------------------|--------|
| MAP-001 | `skills/selfmedia-production-pipeline` | `prism-goal` + orchestration kernel | **distill** (kernel already extracted) | B′ polish | `skills/_internal/orchestration/*` | — | — | extracted_kernel |
| MAP-002 | `skills/selfmedia-director` | `prism-director` | **distill** treatment/QC norms; body later | D | `skills/prism-director/references/{director-philosophy,treatment-template,qc-scorecard}.md` + `_internal/adapters/director.contract.md` | — | — | ✅ distilled（2026-08-14） |
| MAP-003 | `selfmedia-topic-radar` / `newsnow` / `last30days` / `$qi-dev-intel-radar` | `prism-intel` | **bridge** primary to `qi_dev.sh intel-radar`; distill briefing schema only | C/D | briefing schema + evidence gate checklist | `qi_dev.sh intel-radar doctor\|deep-plan` | do not vendor radar runtimes | indexed → bridge |
| MAP-004 | `content/masters/**` + MASTER 规范 | `prism-master` | **distill** MASTER freeze rules; content stays data | C | master freeze checklist + Fact/Story split | path bridge to source masters until Prism `content/` exists | — | distilled_schema |
| MAP-005 | `selfmedia-writing` / `humanize` / `humanizer-zh` / `no-ai-slop` | `prism-produce` + `prism-qa` | **distill** anti-slop + 人话判据; **bridge** heavy humanizer until distill complete | D | `writing` + `qa` adapter refs (gates, not full models) | source skill paths / local humanizer installs | optional later pin of wordlists only | indexed → distill+bridge |
| MAP-006 | `selfmedia-account-pipeline` + 贴图渲染脚本 | `prism-produce` | **pin** render 脚本族 + templates（A1 MIT，2026-08-14）；account 管线其余 defer | D | shot-list / caption metadata rules（form-image-post.contract）+ 本地 pin 脚本 | 渲染脚本本地 pin（`scripts/render_*.py` + `templates/`） | ✅ pinned（ATTRIBUTION: docs/ATTRIBUTION-render-chain.md） |
| MAP-007 | `openmontage` / `comic-storyboard` / rnskill 视频族 | `prism-produce` | **defer** generators; **bridge** when user already has skills installed | D | director handoff fields only | installed local skills by name via routing table | large AV stacks: pin only with ATTRIBUTION | indexed → defer/bridge |
| MAP-008 | `publish-content` / `schedule-post` / sync-ai 桥 | `prism-release` | **bridge** draft tools; **defer** vendor sync-ai pin; human approval always | D/E | publish-approval checklist (kernel has start) | local publish skills; extension path documented not copied | `vendor/selfmedia-sync-ai` only after license+need | indexed → bridge/defer |
| MAP-009 | pipeline refs `creation-mode-map` / `skill-routing` / `quality-gates` | orchestration / routing truth | **distill** (already in kernel); scrub selfmedia-only account paths over time | B′ | same kernel files; Prism-native routing rewrite | — | — | extracted_kernel |
| MAP-010 | `selfmedia-topic-radar` / `selfmedia-newsnow` / `selfmedia-last30days` / `selfmedia-zhihu-hot` / `selfmedia-tl1` | `prism-intel` | **bridge** primary to radar runtimes; distill briefing schema only | C/D | briefing schema + evidence gate checklist (in kernel) | `qi_dev.sh intel-radar` + source skill paths | do not vendor radar runtimes | indexed → bridge |
| MAP-011 | `de-ai-prompt-enhancer` / `rnskill`（写作集合） | `prism-produce` | **bridge** by name; distill style-transfer essentials only if recurrency passes | D | 风格迁移触发规则（可选） | `skill:de-ai-prompt-enhancer` / `skill:rnskill` | vendor sub-trees under license review | indexed → bridge |
| MAP-012 | `kushi-narrative-zh` / `kushi-visual-enrich` | `prism-produce`（novel 子湖 D4） | **bridge** novel 叙事 + 视觉 enrich | D | episode 结构已进 form-novel.contract | `skill:kushi-narrative-zh` / `skill:kushi-visual-enrich` | — | indexed → bridge |
| MAP-013 | `oss-repo-read` / `create-content` / `analyze-data` | `prism-intel` + `prism-master`（研究支持） | **bridge** 研究/素材工具；不复制运行时 | C/D | 来源核对清单已进 master freeze | source skill paths | — | indexed → bridge |
| MAP-014 | `character-illustrations` / `ian-xiaohei-illustrations` / `manage-media` | `prism-produce`（AV/贴图） | **bridge** 插图与媒体管理 | D | 分镜/角色设定字段（director handoff） | installed local skills by name | 大模型权重只 pin 不复制 | indexed → bridge |
| MAP-015 | `publish-content` / `x-publish` / `selfmedia-agent-reach` / `schedule-post` | `prism-release` | **bridge** 发布/排期/触达；凭证保护 + 人工批准不变 | D/E | publish-approval checklist | local publish skills; extension path documented | `vendor/selfmedia-sync-ai` only after license+need | indexed → bridge/defer |
| MAP-016 | vendor monorepos（`human-writing` / `Jellyfish` / `OpenMontage` / `book-video` / `rnskill` / `writing-agent`） | `skills/_internal` + `vendor/` | **vendor_pin** 只 pin 蒸馏脚本与词表（MIT 类），大体量运行时 **defer** | D | `scripts/check_human_voice.py`（已 pin，MIT ATTRIBUTION） | skill paths for monorepo entries | 按 license allowlist 逐项评估 | indexed → pin/defer |

## Decision rules

1. **Default to bridge** for anything with live network, API keys, or large runtimes (`intel-radar`, video gen, publish extensions).
2. **Distill** only what passes recurrence / generativity / distinctiveness / boundary (qi-dev bounded scan). Prefer checklists, gates, schemas, small scripts.
3. **vendor_pin** requires: Lake ≥ D, ATTRIBUTION entry, license allowlist, and a Prism adapter contract that does not become host-visible.
4. **defer** is a first-class status — not a soft TODO. Goal must not pretend deferred producers exist.
5. **anti-leak**: migration work never adds top-level `SKILL.md` under `skills/_internal/adapters/`.

## Lake mapping

| Lake | Migration focus |
|------|-----------------|
| B | Index + shells + kernel extract |
| B′ (this doc) | qi-dev production sample on `prism-goal`; matrix + bridge/distill policy |
| C | campaign/master schema; deepen MAP-004 distill |
| D | form producers; selective vendor_pin + MAP-002/005/006/007 bodies |
| E | metrics / feedback adapters |
| F | monetization optional |

## What not to copy from selfmedia-creator

- Beacon branding / engineering lifecycle as Prism public names
- WiseFlow web UI / logos
- Unverified crawl stacks
- Account-specific hardcodes (`kushi-gzh` paths) without Prism registry rewrite
- Full `vendor/` tree “just in case”

## Verification hooks

```bash
rg -n "MAP-00" registry/adapter-migration-matrix.md registry/adapter-index.yaml
bash skills/prism-goal/scripts/check_goal_shell.sh
```

## Missing evidence (labeled)

- Graded transcript proving agents follow strategy column under ambiguity
- License review tickets for any future vendor_pin rows
- ✅ 2026-08-14：`skill-routing.md` 已 Prism-native 重写（移除 kushi-gzh 账号默认；
  路由指向 prism-* 公开面 + bridge 名；门禁 `scripts/check_standalone_distill.sh`）

## License 评估（2026-08-14 · MAP-006/016 相关）

| 候选 | 来源 | License 状态 | 结论 |
|---|---|---|---|
| `scripts/check_human_voice.py` | 上游 human-writing（MIT） | ✅ MIT 归属保留 | 已 pin（MAP-016） |
| `scripts/lib/readability-lint.py` | 源仓自研 | 源仓无 LICENSE 文件 | 不 pin；bridge 引用 + 缺失 fail-closed；待所有者 license 声明 |
| `scripts/lib/record-humanize-evidence.py` | 源仓自研 | 同上 | 不 pin；bridge 引用 |
| render 脚本族（render_wechat_* / kushi_cover_text_overlay / render-channel）+ `templates/`（96K） | 源仓自研 | ✅ A1 MIT（2026-08-14 所有者授权） | **已 pin**：`scripts/render_*.py` + `templates/`；ATTRIBUTION 见 `docs/ATTRIBUTION-render-chain.md`；门禁 `scripts/check_render_pin.sh` PASS |
| `vendor/OpenMontage` | AGPL-3.0 | ✅ 已核（2026-08-14） | bridge 使用（不复制/不分发）合规；vendor_pin 会把 AGPL 传染进 Prism 分发面 → 默认不 pin，需 license review + ATTRIBUTION + 人工批准 |
| `vendor/book-video` | Apache-2.0（prototech/endless） | ✅ 已核 | pin 候选（permissive），需 ATTRIBUTION + license 文件随附；第三方工具/字体/模型不自动覆盖 |
| `vendor/Jellyfish` | Apache-2.0 | ✅ 已核 | pin 候选（permissive），需 ATTRIBUTION |
| `vendor/rnskill` | CC BY-NC 4.0 | ✅ 已核（2026-08-14） | **非商业许可** → 商业场景禁止 pin/复制；仅 bridge 引用 + 许可证边界提示 |
| `vendor/writing-agent` | MIT | ✅ 已核 | pin 候选（permissive），需 ATTRIBUTION |
| `vendor/human-writing` | MIT | ✅ 已核 | 已 pin（check_human_voice.py + 规则蒸馏） |

**结论**：源仓自研脚本/模板在所有者未给出 license 声明前一律不 pin（bridge + 占位），
与 Prism 规则「vendor_pin 需要 license allowlist」一致；check-human-voice 例外因上游 MIT 已成立。
