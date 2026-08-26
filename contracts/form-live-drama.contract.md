# Form contract: live_drama（真人微短剧 · Lake D）

> 状态：**registered**（2026-08-21 human 冻结指令；truth R1）。
> 所有者确认：**持有《广播电视节目制作经营许可证》**（decided_by: human，2026-08-21）。
> 选题证据：`content/briefings/live-drama-hotspot.md`（检索时刻 2026-08-21）。
> 监管基线：《微短剧发展管理办法》（广电总局令第 16 号，2026-09-01 施行）；
> 持证机构可按需走一类/二类备案，本契约默认仍按三类平台自审出草稿，一类/二类题材
> 送审材料由 prism-release 人工批准后整理。

## 1. identity

- form_id: live_drama（真人实拍微短剧；与 manga_drama（AI 漫剧）互斥不混路由）
- lane: standard
- 分工：Prism 自动化=剧本/分集/分镜/剪辑清单/合规门；人工交付=实拍素材；bridge=openmontage 剪辑
- 合规定位：默认按**三类微短剧**（低投资一般题材）走播出平台自审；一类/二类题材直接 blocked

## 2. 决策边界

- 能决定：分集结构、剧本执行、剪辑参数、合规检查单生成
- 不能决定：正典事实、实拍执行、QA 判定、平台送审动作、公开发布

## 3. intake（必填）

- StoryMaster / 剧集 bible（world_slug，canon ledger）
- director 分集大纲（每集 hook / 冲突 / 翻转点）+ 单集成片剧本（场景表 + 台词）
- **拍摄素材 ingest（人工交付物）**：素材清单 manifest（文件名 × 场景 × 时长），缺清单 → blocked
- 演员授权记录（肖像/表演权同意）；缺失 → blocked（`live_actor_consent_missing`）

拒绝：缺任一 → blocked + reason_code。

## 4. output

- 剧本包：`content/presentations/{world_slug}/{slug}/live-drama-{ep}/`
  （script.md、shot-list.md、edit-list.md、ingest-manifest.json）
- 成片草稿：同目录 `draft/ep-{slug}.mp4`（openmontage 剪辑产物）
- 合规附件：compliance-checklist.md（三类自审材料核对单 + 节目编号标注位）

## 5. gate（任一失败 exit 非 0）

1. 剧本/口播文案过 anti-slop-gate 与 check_human_voice.py
2. 素材引用完整：edit-list 每一镜对应 ingest-manifest 存在项
3. **AI 镜头标识检查**：混用 AI 生成镜头的成片，每集明显位置须有提示标识（总局令第 16 号义务）
4. 演员授权齐备
5. 题材红线：政治/军事/外交/国家安全等特殊题材 → 一类路径 → 走持证机构备案流程，
   本管线只产出送审材料包（样片/字幕表/备案表），不自动送审

## 6. license / 凭证注记

- openmontage AGPL：维持 bridge 不 pin
- 平台凭证不入仓；送审材料由 prism-release 在人工批准后整理导出

## 7. handoff / 失败处理

- 下一公开面：prism-qa（含合规门）→ prism-release（停人工审片；送审/发布需人工二次批准）
- 可重试：剧本、剪辑、换镜重拍建议单
- 必须停：无素材清单、无授权、特殊题材、任何自动发布
- 禁止自证通过：true

## Non-goals（本形态明确不做）

数字人替身主演；一类/二类备案代理；付费投流与投放优化；多季排播调度。
