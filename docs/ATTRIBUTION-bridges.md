# ATTRIBUTION — bridge skills pin（A4 · 2026-08-15）

> 授权依据：`docs/owner-license-decision.md` A4（human 指令 2026-08-15）。
> pin 落点：`vendor/skills/<name>/`（非 skill root，不对人发现；按路径引用）。

## MIT 上游（各随附 LICENSE 文件）

| skill | 上游 | 版权 | 体积 |
|---|---|---|---|
| humanizer-zh | op7418/Humanizer-zh | 歸藏 | 36K |
| qu-ai-wei | LifelongLazyLearner/qu-ai-wei | （LICENSE 随附） | 1.2M |
| shuorenhua | MrGeDiao/shuorenhua | MrGeDiao | 2.2M |
| no-ai-slop | petergyang/no-ai-slop | Peter Yang | 372K |
| stop-slop | hardikpandya/stop-slop | Hardik Pandya | 32K |
| humanizer-en | blader/humanizer | Siqi Chen | 72K |
| writing-agent | dongbeixiaohuo/writing-agent | Dante.sun | 292K |
| comic-storyboard | Comic Workflow Codex Skill contributors | 同上 | 1.4M |
| character-illustrations | moxordo（Andy Kim） | 同上 | 672K |

## 自研（所有者 A4-1 MIT 授权）

| skill | 说明 |
|---|---|
| selfmedia-humanize / selfmedia-writing | 成稿/人味（判断已蒸馏，脚本随附） |
| selfmedia-topic-radar / newsnow / last30days / zhihu-hot / tl1 | 选题雷达族 |
| oss-repo-read / analyze-data / create-content | 研究/素材支持 |
| kushi-narrative-zh / kushi-visual-enrich | novel 叙事 / 视觉充实 |
| manage-media / publish-content / schedule-post / x-publish / selfmedia-agent-reach | 媒体/发布/排期/触达 |
| ian-xiaohei-illustrations（逻辑部分） | 插画包逻辑；13M 示例资产保持 bridge |

## 受限 pin（A5 · 2026-08-15，随附守卫）

| skill | 处理 | 守卫 |
|---|---|---|
| rnskill | 合规层 pin（SKILL/LICENSE/CREDITS/README/VERSION + NOTICE） | CC BY-NC 4.0 非商业；96M skills 子树 archive-only 回源引用（`vendor/skills/rnskill/NOTICE.md`） |
| de-ai-prompt-enhancer | 完整 pin + NOTICE | 无独立 LICENSE；衍生自 MIT Humanizer-zh；公开发布前须向上游确认（`vendor/skills/de-ai-prompt-enhancer/NOTICE.md`） |
| ian-xiaohei-illustrations | 整包 pin（含 13M assets，自研 A5-1） | 所有者 MIT 授权 |

> 29 个 bridge 全部 pin/守卫化（2026-08-15），bridge 数量清零；
> rnskill 子树为唯一 archive-only 回源引用（非商业合规）。
