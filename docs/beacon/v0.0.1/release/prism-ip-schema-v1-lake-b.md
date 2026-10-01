# Release Brief — prism-ip-schema-v1（Lake B · IP 轴）

- status: **released（人工批准）**
- feature: `prism-ip-schema-v1`
- version: `v0.0.1`
- approved_by: 用户（对话指令：批准 + 写 brief + 推送 origin/main）
- approved_at: 2026-09-30（Asia/Shanghai）
- approved_action: push `main` → `origin/main` + 登记 release brief
- release_gate: `release_gate` → **human_confirmed**
- QA: 24/24 TC passed · AC 8/8 · release_ready=true
- truth: **R3 frozen**（R1 冻结 → R2 ux_required 修正 → R3 implementation-first-reconciliation）
- reconciliation: completed（`implementation_first_reconciliation_completed`，current=R3）
- research: `docs/beacon/v0.0.1/research/prism-ip-model-v1.md`
- program: `prism-ip-model`（L1）

## Delivered

1. **IP 对象（AC-IPM-001）**：`contracts/ip.schema.yaml` + `registry/content-schema.yaml` 注册
   `schema_id: ip`，根 `content/ips/{ip_id}/`；`ip.yaml` 必填 `ip_id`/`title`/`kind`/`status`/
   `canon_revision`/`publish_identity_ref`；生命周期 `draft→active→paused→archived`。
2. **IP 资产（AC-IPM-002）**：`assets/{characters,scenes,props,styles}/<asset_id>/`，
   冻结 identity block（7 段）+ 引用图 + 谱系；`asset_id` 同 IP 内唯一；跨 IP 引用带 `from`。
3. **import 声明（AC-IPM-003）**：`master-content`/`storyworld`/`campaign`/`narrative-episode`
   四契约新增可选 `imports[]:{from,asset,track,revision}`，`default_track: latest`；旧内容不回填。
4. **解析与 fail-closed（AC-IPM-004）**：逐字注入源 identity block；`track: latest` 落盘
   `resolved_revision`；四类 fail-closed（`ip_not_found`/`ip_unfrozen`/`asset_missing`/`revision_mismatch`）；
   禁止静默本地重描述。
5. **联名正典门（AC-IPM-005）**：多源 import（≥2 IP）聚合正典门 AND，`crossover_canon_unmet`。
6. **校验脚本（AC-IPM-006）**：`scripts/check_ip_model.sh`（注册/必填/引用解析/asset_id 唯一；
   `--self-test` / `--invert` / `--expect`）。
7. **docs/prism 同构（AC-IPM-007）**：`check_prism_project_docs.sh --init-shape` 纳入 `ips/`。
8. **存量资产收敛（AC-IPM-008）**：`scripts/migrate_assets_to_ip.sh`（storyworld/master → IP；
   幂等 + 不丢资产 + alias manifest）。

变更：18 文件 +670（新增 `contracts/ip.schema.yaml`、两个脚本、`content/ips/`，改 4 契约 + 2 registry/check）。

## Still forbidden / deferred

- L2 `prism-ip-import-gate-v1`（import 解析门执行层 + 跨 IP 授权/披露钩子，接 F1/F2）未冻。
- L3 `prism-ip-continuity-v1`（IP 级连续性/season 投影）defer。
- 发布自动化、平台对接不变；不得宣称海级 closure。
