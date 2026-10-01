# Release Brief — prism-shot-iteration-budget-v1（生成预算与收敛红线）

- status: **released（人工批准）**
- feature: `prism-shot-iteration-budget-v1`
- version: `v0.0.1`
- approved_by: 用户（对话指令：批准 + 写 brief + 推送 origin/main）
- approved_at: 2026-09-30（Asia/Shanghai）
- approved_action: push `main` → `origin/main` + 登记 release brief
- release_gate: `release_gate` → **human_confirmed**
- QA: 19/19 TC passed · AC 7/7 · release_ready=true
- truth: **R3 frozen**（R1 冻结 → R2 ux_required 修正 → R3 implementation-first-reconciliation）
- reconciliation: completed（`implementation_first_reconciliation_completed`，current=R3）
- research: `docs/beacon/v0.0.1/research/prism-shot-iteration-budget-v1.md`
- provenance: Jarvis Muse 漫剧六步法
  （`https://x.com/jarvis11x/status/2104397648438476868`）蒸馏

## Delivered

1. **迭代预算（AC-ITB-001）**：`storyboard-schema.json` 新增 `iteration_budget`/`attempts`；
   `attempts > iteration_budget` 且无降级 → `iteration_budget_exceeded`。
2. **超限降级（AC-ITB-002）**：`convergence ∈ {simplified, redesigned}` + `downgrades ≤ max_downgrades`，
   超过即 `shot_aborted`（防无限降级）。
3. **禁后期配音兜底（AC-ITB-003）**：`dialogue_source=post_dub` → `post_dub_fallback_forbidden`
   （对白失败只能改镜头设计，与 assemble no-fallback 总则一致）。
4. **画面肯定式（AC-ITB-004）**：补进 `contracts/prompt-syntax.contract.md` §9；
   命中否定式 → `image_negation_not_affirmative`（字幕/音频否定除外）。
5. **能力域前置门（AC-ITB-005）**：`provider`/`model`/`reachable` 白名单；
   动作/对白不可达 → `action_outside_model_domain` / `dialogue_outside_model_domain`，设计期退回。
6. **校验脚本（AC-ITB-006）**：`scripts/check_shot_iteration_budget.sh`
   （`--self-test` / `--invert` / `--expect`）。
7. **阈值来源义务（AC-ITB-007）**：`threshold_source`（来源 + 测试条件：题材 + 模型），
   缺失 → `threshold_source_missing`。

变更：`storyboard-schema.json`（+25）、`contracts/prompt-syntax.contract.md`（新增 §9–12）、
新增 `scripts/check_shot_iteration_budget.sh`。

## Still forbidden / deferred

- provider 计费/成本账单对接（未做，YAGNI）。
- 自动降级策略学习（归 Lake E 学习面）。
- 视频生成/渲染/拼接链不变（Lake D 已交付）。
- 不得宣称海级 closure。
