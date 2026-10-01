# Research Closure: prism-ip-import-gate-v1（L2）

- version: `v0.0.1`
- feature: `prism-ip-import-gate-v1`
- program: `prism-ip-model`（L2）
- depends_on: `prism-ip-schema-v1`（L1，已 released）
- status: research closure（planner artifact，非 frozen truth）

## 人话

L1 让"一个作品可以引用别的 IP 的资产"这件事**能被声明**了。
L2 要让它**能被把关**：联名（一个作品的 imports 指向 ≥2 个 IP）不是随便就能出的——

它是**两个创作主体的合作**，所以必须：
1. **授权**：两个 IP 的主体同意这次联名（谁跟谁、能用到什么程度）。
2. **披露**：对外要标明这是联名/品牌合作（接 F1 披露义务）。
3. **署名/分成**：谁挂名、收益怎么分（接 F1 变现 / F2 改编条款）。
4. **正典不打架**：两个 IP 的世界观/人设不能互相破坏。

L1 的 `check_ip_model.sh` 已经做了**静态**解析（引用能不能解析、源 IP 是否冻结、`crossover_canon_unmet`）。
L2 补的是**执行层 + 授权/披露层**：把"能解析"升级成"被授权、有披露、有署名记录"才放行。

## 现状证据（L1 + F1/F2）

| 已有 | 位置 | 缺什么 |
|---|---|---|
| import 声明 + 解析 + fail-closed | `contracts/ip.schema.yaml`、`scripts/check_ip_model.sh`（L1） | 无授权/披露/署名维度 |
| 多源联名正典门（AND） | `check_ip_model.sh` `crossover_canon_unmet` | 只判正典，不判授权/披露 |
| 变现 deal 登记 + 披露义务 | `contracts/monetization.contract.md`（F1） | 无"联名"这一 deal 类型钩子 |
| 改编授权登记 + 分成 | `contracts/adaptation.contract.md`（F2） | 无 IP 级联名授权记录 |

## 第一性原理

**联名 = 多个独立权利主体的合作行为。** 只要"多个主体"出现，就必须有：
同意（授权）→ 告知受众（披露）→ 分配（署名/分成）。这三件事不是可选项，是合作的定义性条件。
L1 解决"技术上能不能引用"，L2 解决"法律/关系上能不能出"。

判定：**湖**，单 feature，依赖 L1（已 released）。

## 模型形状

```text
content/ips/{ip_id}/ip.yaml            # L1 已有：publish_identity_ref（发布身份）
content/crossovers/{crossover_id}.yaml # L2 新增：联名授权记录
  - crossover_id, participant_ips[]   # 参与 IP（≥2）
  - work_ref                            # 联名作品（master/episode/campaign 路径）
  - authorization: { status, approved_by, approved_at, scope }
  - disclosure_note                     # 对外披露文本
  - attribution[]                       # 署名分配
  - royalty_split[]                     # 收益分成（接 F1/F2；可为空=不分账）
  - canon_refs[]                        # 各方正典引用（用于保护性校验）
```

门（execution + QA 两处）：
- `imports[]` 涉及 ≥2 IP → 必须有对应 `content/crossovers/{id}.yaml` 且 `authorization.status=approved`；
  否则 blocked + `crossover_authorization_missing`。
- 联名作品发布前必须有 `disclosure_note` 非空；否则 `crossover_disclosure_missing`。
- 声明分成时须 `royalty_split` 完整（各项合计=100% 或显式 non_royalty）；否则 `crossover_royalty_unrecorded`。
- 联名不得破坏任一参与 IP 的正典（复用 L1 `crossover_canon_unmet` + 各方 `canon_refs`）。
- 与 F1/F2 的关系：F1 管"变现承诺披露"，F2 管"改编授权"；L2 的联名授权若同时是变现/改编，
  **叠加** F1/F2 门（不替代）。

## Decision Priority

1. 契约 > 本地约定。
2. 多主体即需授权 + 披露（fail-closed）；不编造授权/分成（承 F1/F2）。
3. 与既有门叠加，不替代 F1/F2。
4. 正典保护优先：任一参与 IP 正典未过即阻断。
5. 最懒可用：复用 L1 解析 + F1/F2 记录，只新增"联名授权记录"一个对象。

## Promotion Notes（truth AC 候选）

- AC-IPG-001：新增 `crossovers` 对象 `content/crossovers/{crossover_id}.yaml` 契约 `contracts/crossover.schema.yaml`；必填 `crossover_id`、`participant_ips`（≥2）、`work_ref`、`authorization`、`attribution`。
- AC-IPG-002：`imports` 涉及 ≥2 IP 的作品，必须有 `authorization.status=approved` 的联名记录；否则 blocked + `crossover_authorization_missing`。
- AC-IPG-003：联名作品须有非空 `disclosure_note`；否则 `crossover_disclosure_missing`。
- AC-IPG-004：声明分成时 `royalty_split` 完整（合计 100% 或显式 `non_royalty`）；否则 `crossover_royalty_unrecorded`。
- AC-IPG-005：联名须逐个校验参与 IP 正典冻结（复用 L1），任一未过 → `crossover_canon_unmet`。
- AC-IPG-006：校验脚本 `scripts/check_ip_import_gate.sh` 对作品 + 联名记录判定；合规通过、违规非零退出 + reason_code。
- AC-IPG-007：与 F1/F2 叠加——联名涉变现/改编时，F1 披露门与 F2 授权门同时适用（记录 hook，不替代）。

## Promotion Log

- 2026-09-30：L1 released 后，按 program `prism-ip-model` 推进 L2。
  promoted → freeze `prism-ip-import-gate-v1`（AC-IPG-001..007）。
