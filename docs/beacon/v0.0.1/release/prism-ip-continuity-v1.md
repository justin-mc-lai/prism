# Release Brief — prism-ip-continuity-v1（Lake B · IP 级连续性 · L3）

- status: **released（人工批准）**
- feature: `prism-ip-continuity-v1`
- version: `v0.0.1`
- program: `prism-ip-model`（L3；L1 `prism-ip-schema-v1` 已发布）
- approved_by: 用户（对话指令：批准 + 写 brief + 推送 origin/main）
- approved_at: 2026-09-30（Asia/Shanghai）
- approved_action: push `main` → `origin/main` + 登记 release brief
- release_gate: → **human_confirmed**
- QA: TC 16/16 passed · AC 6/6 · release_ready=true
- truth: **R2 frozen**（R1 冻结 → R2 修 TC-IPC-014 `{R}` 未转义 → `rg -F`）
- research: `docs/beacon/v0.0.1/research/prism-ip-continuity-v1.md`

## Delivered

1. **演进链（AC-IPC-001）**：`content/ips/{ip_id}/revisions/{R}.yaml`（`revision`/`reason`/`affected_assets`）；
   从 R1 到当前 `canon_revision` 每跳缺记录即 `revision_chain_incomplete`。
2. **按 IP 视图（AC-IPC-002）**：`scripts/check_ip_continuity.sh view --ip <id>` 输出版本链 + 引用清单。
3. **漂移审计（AC-IPC-003）**：同一 IP 资产被多作品引用且 `resolved_revision` 不一致时报告
   `continuity_revision_drift`（warning，退出码 0，只审计不阻断）。
4. **season 门（AC-IPC-004）**：`content/ips/{ip_id}/seasons/{season_id}.yaml` 的 `campaign_refs`
   必须同属该 IP；否则 `season_ip_mismatch`。
5. **复用 campaign（AC-IPC-005）**：season = 按 IP 聚合的多 campaign；`contracts/ip.schema.yaml` 增补
   `seasons` 段；未新造 `series` 对象。
6. **校验脚本（AC-IPC-006）**：`scripts/check_ip_continuity.sh`（`--self-test` / `--invert` / `--expect`）。

变更：改 `contracts/ip.schema.yaml`（revisions/seasons 段）；新增 `scripts/check_ip_continuity.sh`、
`content/ips/_examples/ip-demo/revisions/R1.yaml` + `seasons/s1.yaml`。

## Still forbidden / deferred

- 新增生产链、修改 IP 正典（只读投影）、替 QA 下 verdict、发布自动化。
- 不得宣称海级 closure。
