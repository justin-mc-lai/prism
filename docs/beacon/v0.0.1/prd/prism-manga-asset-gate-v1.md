---
slug: prism-manga-asset-gate-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-manga-asset-gate-v1/truth.md
---

# PRD — prism-manga-asset-gate-v1（Lake D 资产一致性门）

## 问题

manga_drama 现有门只验 `asset_refs_exist`（引用存在），不拦：出场即新身份、含混指代硬猜、
相邻镜头状态无来源跳变、逐镜画风漂移。drama-skills（identity/variant/continuity 框架）
与 lumenx（资产三件套+画风统一）已可蒸馏出成熟判断框架，但未进 Prism 门禁。

## 目标

1. 蒸馏框架落 `skills/prism-director/references/asset-consistency-gate.md`（MAP-017）。
2. `contracts/asset-consistency.contract.md` 六判据门（三分法/锚点/CON-01/CON-04/
   AST-05 binding/画风统一），fail-closed。
3. manga_drama 契约 intake + gate#2 接线；registry producer_chain 插入门步骤。
4. `scripts/check_asset_consistency.sh` exec 门禁。
5. MoneyPrinterTurbo/openstory 记 A4 常设决策：维持 defer-pin，按需逐次 pin。

## 边界

- 能做：蒸馏参考、门契约、接线、校验脚本、决策记录。
- 不能做：上游运行时 pin；复制上游正文；替代正典门/QA SCORECARD；发布自动化。

## 成功判据

TC-MAG-001..007 全 PASS；`bash scripts/check_asset_consistency.sh` PASS；
`make -C workspace check` PASS；prism-director quick_validate PASS。
