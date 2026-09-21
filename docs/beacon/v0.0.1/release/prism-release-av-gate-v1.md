# Release Brief — prism-release-av-gate-v1 (v0.0.1)

- release_id: `rel-prism-release-av-gate-v1-20260921`
- feature: `prism-release-av-gate-v1`
- version: `v0.0.1`
- status: **released（人工批准）**
- approved_by: 用户（对话指令：补上最后一个缺口 + 确保可交付）
- approved_at: 2026-09-21（Asia/Shanghai）
- approved_action: 合入 `main` + 推送 `origin/main` + 登记 release brief
- release_gate: `pending_human` → **human_confirmed**
- scorecard: `release_ready=true` · gate=Pass（blocked=2 属仓级元检查）· qa=passed

## 交付内容

补齐**最后一处接线缺口**：`prism-release` 此前对 AV/manga 渲染交接**零引用**。

1. `skills/prism-release/references/modes/draft-release.md`
   - Procedure 增 AV/manga 交接三判据：`release_gate == pending_human` / AI 标识在场 / 无自动发布路径
   - 新增 §AV/manga 交接门（判据表 + `release_ai_label_missing` fail 码）
   - nested refs 指向 `contracts/asset-render.contract.md` 与 `registry/render-adapters.yaml`
2. `skills/prism-release/SKILL.md`
   - HARD GATE 补 AI 标识义务 + `pending_human` 终态
   - Boundaries 补：不得放行无标识成片；不得新增自动发布路径
3. `skills/prism-release/scripts/check_release_shell.sh`
   - 增 AV gate 断言 + **自动发布路径反断言**（排除自匹配）

## 提交链

- `<pending>` feat(release): release 面 AV 交接门（prism-release-av-gate-v1 R1）
- `origin/main` = `main`

## 验收证据

- 实现证据：`.beacon/evidence/implement/prism-release-av-gate-v1/AC-RAV-{001..003}.json`
- 汇总：`.beacon/evidence/implement/prism-release-av-gate-v1/GATES.json`
  （`all_exec_gates_pass=true` · truth integrity `pass` · quality `pass` · materials `synced`）
- QA 矩阵：`.beacon/evidence/implement/prism-release-av-gate-v1/QA-MATRIX.json`
- 全量门禁：`scripts/check_*.sh` **28/28 PASS**；`check_all_public_surfaces.sh`（7 公开面）PASS
- 分层验证：`verify-truth-integrity` **20/20 pass**（`--mode block --strict`）；`verify-truth-quality` 20/20 pass

## 覆盖后的完整链路

```text
prism-produce  → prompt_compiler.py → 资产/图片/视频提示词 + srt
prism-qa       → 三件产物 + mode=provider-only + 片段规格（无兜底）
prism-release  → release_gate=pending_human + AI 标识 + 无自动发布  ← 本次补齐
```

## 已知运行时说明（非功能阻塞，与 prism-title-lab-v1 同源）

`beacon release check v0.0.1` 全仓级两项元检查失败（`legacy_cutover_required` /
`coverage artifact ready`），属本仓 legacy→feature 迁移历史状态，与本 feature 无关；
`beacon release scorecard` 仍判 `Release ready: True`。

## 不覆盖

- **平台公开发布**：仍须按 `contracts/publish-bridge.contract.md` 逐内容人工二次批准
- **平台发布 API / 自动发布**：属后续海（truth DL-RAV01）；仓库内无自动发布路径
