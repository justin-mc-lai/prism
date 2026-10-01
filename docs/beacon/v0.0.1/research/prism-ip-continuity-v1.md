# Research Closure: prism-ip-continuity-v1（L3）

- version: `v0.0.1`
- feature: `prism-ip-continuity-v1`
- program: `prism-ip-model`（L3）
- depends_on: `prism-ip-schema-v1`（L1，已 released）
- status: research closure（planner artifact，非冻结 truth）

## 人话

一个 IP 会**持续创作、长篇连载**：第 1 集用了角色 A 的 R1 版，第 10 集 IP 演进到 R4，
角色 A 换了新形态。这时要能回答三个问题：

1. **连续性**：这个 IP 的历史作品里，同一资产用了哪些版本？跨集有没有莫名换脸？
2. **演进**：IP 的正典从 R1→R2→…→Rn 改了什么？谁在什么时间改的？
3. **按 IP 收敛**：选题/定稿/导演（intel/master/director）能不能"只看这个 IP"？
   season（一季 = 多个 campaign）怎么按 IP 组织？

L1 给了 IP + 资产 + import；L2 管联名授权。L3 管**时间轴**：IP 的生命周期与版本演进，
以及按 IP 的视图收敛。

## 现状证据

| 已有 | 位置 | 缺什么 |
|---|---|---|
| IP `canon_revision` + `status` | `contracts/ip.schema.yaml`（L1） | 无 revision 历史/演进记录 |
| import `resolved_revision` 落盘 | L1 | 无"跨集汇总"视图 |
| campaign 作"serial dossier" | `contracts/campaign.schema.yaml` | 无"season = 按 IP 聚合的多 campaign" |
| 按 IP 过滤能力 | 无 | intel/master/director 面无 IP 视图 |

## 第一性原理

**连载的本质是"同一身份在时间上的连续"。** 所以要能：
- 记录身份的**演进链**（revision + 变更原因），而不是只有一个当前值；
- 对任何历史产物，**可回指**它当时用的 revision（L1 的 `resolved_revision` 已是种子）；
- 提供**按 IP 的聚合视图**（历史作品、版本时间线、season）。

判定：**湖**，单 feature，依赖 L1（已 released）。纯投影/视图层，不新增生产链。

## 模型形状

```text
content/ips/{ip_id}/revisions/         # L3 新增：IP 版本演进链
  R1.yaml ... Rn.yaml                  # 每次 canon_revision 的变更记录（原因/时间/影响资产）
content/ips/{ip_id}/seasons/           # L3 新增（可选）：season = 按 IP 聚合的 campaign 组
  {season_id}.yaml                     # 引用多个 campaign_id，同一 IP
```

投影/门：
- **演进链完整**：IP 的 `canon_revision` 每跳须有 `revisions/{R}.yaml`（原因 + 影响资产）；缺 → `revision_chain_incomplete`。
- **连续性**：同一 IP 的资产被多个作品 import 时，记录各自 `resolved_revision`；跨集出现"同资产不同 revision 且无演进记录支撑"→ `continuity_revision_drift`（warning，不阻断；用于审计）。
- **season 聚合**：`seasons/{id}.yaml` 的 campaign 必须同属一个 IP；否则 `season_ip_mismatch`。
- **按 IP 视图**：提供确定性命令/脚本 `scripts/check_ip_continuity.sh` 输出某 IP 的版本链 + 作品引用清单（供 intel/master/director 消费）。

## Decision Priority

1. 契约 > 本地约定。
2. 演进必须有记录（fail-closed）；连续性漂移记为 warning（审计，不阻断生产）。
3. 复用 campaign 表达 season，不新造对象。
4. 视图层只读，不改 truth / 不产内容。
5. 最懒可用：复用 L1 的 `canon_revision`/`resolved_revision`，只新增 revisions/ 与 seasons/。

## Promotion Notes（truth AC 候选）

- AC-IPC-001：IP 每次 `canon_revision` 跳变须有 `content/ips/{ip_id}/revisions/{R}.yaml`（`revision`、`reason`、`affected_assets`）；缺失 → `revision_chain_incomplete`。
- AC-IPC-002：`scripts/check_ip_continuity.sh` 可输出某 IP 的版本链（R1→…→Rn）与作品引用清单（确定性）。
- AC-IPC-003：连续性审计：同 IP 资产被多作品引用时，`resolved_revision` 不一致且无对应演进记录 → 报告 `continuity_revision_drift`（warning，exit 0 但列出）。
- AC-IPC-004：`content/ips/{ip_id}/seasons/{season_id}.yaml` 引用的 campaign 必须同属该 IP；否则 `season_ip_mismatch`。
- AC-IPC-005：season 复用现有 `campaign` 对象（一个 IP 多个 campaign），不新造 series 对象；契约 `contracts/ip.schema.yaml` 增补 seasons 段。
- AC-IPC-006：校验脚本 `scripts/check_ip_continuity.sh` 合规通过、违规非零退出 + reason_code；含 `--self-test`。

## Promotion Log

- 2026-09-30：L1 released 后，按 program `prism-ip-model` 推进 L3（defer 项提前，因 L1 已就绪）。
  promoted → freeze `prism-ip-continuity-v1`（AC-IPC-001..006）。
