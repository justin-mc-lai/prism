# Release Brief — prism-ip-import-gate-v1（Lake B · 联名执行门 · L2）

- status: **released（人工批准）**
- feature: `prism-ip-import-gate-v1`
- version: `v0.0.1`
- program: `prism-ip-model`（L2；L1 `prism-ip-schema-v1` 已发布）
- approved_by: 用户（对话指令：批准 + 写 brief + 推送 origin/main）
- approved_at: 2026-09-30（Asia/Shanghai）
- approved_action: push `main` → `origin/main` + 登记 release brief
- release_gate: → **human_confirmed**
- QA: TC 15/15 passed · AC 7/7 · release_ready=true
- truth: **R1 frozen**
- research: `docs/beacon/v0.0.1/research/prism-ip-import-gate-v1.md`

## Delivered

1. **联名授权对象（AC-IPG-001）**：`contracts/crossover.schema.yaml` + `registry/content-schema.yaml`
   注册 `schema_id: crossovers`，根 `content/crossovers/{crossover_id}.yaml`；必填
   `crossover_id`/`participant_ips`(≥2)/`work_ref`/`authorization`/`attribution`。
2. **授权门（AC-IPG-002）**：作品 `imports[]` 去重后 ≥2 个 IP 时，须有 `authorization.status=approved`
   的联名记录；否则 `crossover_authorization_missing`。
3. **披露门（AC-IPG-003）**：`disclosure_note` 非空；否则 `crossover_disclosure_missing`。
4. **分成门（AC-IPG-004）**：`royalty_split` 占比合计 100%，或 `non_royalty: true` 豁免；
   否则 `crossover_royalty_unrecorded`。
5. **正典聚合门（AC-IPG-005）**：参与 IP 须 `active` 且正典冻结；否则 `crossover_canon_unmet`（复用 L1 口径）。
6. **校验脚本（AC-IPG-006）**：`scripts/check_ip_import_gate.sh`（`--self-test` / `--invert` / `--expect`；
   含作品侧 ≥2 IP 联动判定）。
7. **F1/F2 叠加（AC-IPG-007）**：联名涉变现/改编时，F1 披露门与 F2 授权门经 hook 叠加，不替代。

变更：新增 `contracts/crossover.schema.yaml`、`scripts/check_ip_import_gate.sh`、`content/crossovers/`
（README + `_examples/cx-demo` + `ip-guest` 样例）；改 `registry/content-schema.yaml`。

## Still forbidden / deferred

- 代写正文、替 F1/F2 下变现/改编结论、发布自动化。
- 不得宣称海级 closure。
