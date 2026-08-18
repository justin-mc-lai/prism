# Release Brief — prism-title-lab-v1 (v0.0.1)

- release_id: `rel-prism-title-lab-v1-20260818`
- feature: `prism-title-lab-v1`
- version: `v0.0.1`
- status: **released（人工批准）**
- approved_by: 用户（对话指令：批准合并 + 授权 B 方案原样提交存量改动）
- approved_at: 2026-08-18（Asia/Shanghai）
- approved_action: 合并 `beacon/v0.0.1/prism-title-lab-v1` → `main` + 登记 release

## 交付内容

1. `skills/prism-produce/references/title-lab.md`：标题实验室（7 公式 + 8 模板 + 路径 A/B + 硬规则）
2. `skills/prism-intel/references/briefing-schema.md`：「选题角度 + 标题公式建议」小节（title_hint）
3. `skills/prism-qa/references/anti-slop-gate.md` + `skills/_internal/orchestration/quality-gates.md`：标题门
4. `docs/ATTRIBUTION-corpora.md` + `skills/prism-produce/references/LICENSE-bigpeng-hot-gzh` + `title-corpus.md`：语料署名与校准层
5. `contracts/metrics-publication.contract.md` + `contracts/review-loop.contract.md`：title_formula/is_preferred + 4 周基线对比

## 提交链

- `09f0f8e` truth(freeze) R1（main）
- `b2468d6` implement（feature）
- `95cd77d` tasks tick + GATES（feature）
- `91b1296` QA 证据 + 对抗审查（feature）
- `f7d6b92` 存量 Lake B′ 工作区改动原样提交（main，用户授权 B）
- `017ee1e` merge `beacon/v0.0.1/prism-title-lab-v1` → main

## 验收证据

- QA 运行矩阵 7/7 TC pass：`.beacon/evidence/auto-test/run-20260818T143750172905/qa9/tc-execution-map.json`
- 实现证据：`.beacon/evidence/implement/prism-title-lab-v1/AC-{001..005,GATES,QA-MATRIX}.json`
- 对抗审查 5 项翻车点全部有防护与证据（见 QA-MATRIX.json）
- 合并后 main 复验：TC-001..TC-006 + TC-EXEC-001 全部 exit 0

## 已知运行时说明（非功能阻塞）

- `beacon release check` 全仓级 `legacy_cutover_required` 与 `coverage artifact ready` 两项元检查失败，
  属本仓 legacy→feature 迁移历史状态，与本 feature 功能无关；功能 TC 与分层 QA 证据已闭环。
- goal 状态机 plan→truth 门曾因运行态 `recommended_next.blocks_auto_tick_past_plan` 未回写而卡住，
  已按 `mark_journeys_frozen` 语义修复，管线现停在 release 人工门并已获人工批准。

## 后续

- 命中率绝对值依赖发布后 4 周真实数据（deferred 后验，DL-T01）。
