# Research Closure: prism-ip-model-v1

- version: `v0.0.1`
- feature: `prism-ip-model-v1`（program: `prism-ip-model`）
- 别名（用户词）：`project` / 项目 / IP（本文视三者同义：一个创作身份 + 它的正典资产库）
- diagram_types: none
- state_axes: ip-lifecycle (draft → active → paused → archived)；asset-revision (R1 → R2 → …)
- status: research closure（planner artifact，非 frozen truth）

## 人话（用户洞察，先摆正）

**IP 的本质不是"一个文件夹"，而是"一套可被别的项目引用的正典资产"。**

漫剧 / 短剧 / 小说 的创作原理都一样：
- **小说**：角色圣经、世界观设定反复用；系列作品共享人物。
- **漫剧 / 短剧**：Jarvis 那篇 Muse 六步法的核心纪律就是
  **"不锁定全部资产，一个镜头也不生成；人物描述词一旦冻结，每个分镜提示词里一字不许改"**。
- **联名**：两个 IP 的角色同台 —— 本质是"从两个资产库各取资产"。

所以真正被复用、被冻结、被引用的**原子单位是「资产」**（人物 / 场景 / 道具 / 风格），
不是"项目"、不是"目录"。

**IP = 把这些冻结资产集中起来、给稳定地址、允许被别的项目 import 的那个命名空间。**

> 一句话：**IP 是资产的"发行包"，项目是资产的"使用方"。**
> 冻一次，处处引用 —— 这才是 IP 的定义性能力。

## 用户洞察（本轮修正）

- 上一轮模型把原语放在"归属边 `ip_refs[]`"（谁属于谁）。**方向对，但抓错了重点。**
- 真正的原语是 **资产引用（asset import）**：
  「IP A 里生成的角色，能在 IP/项目 B 里被逐字引用」。
- 这解释了为什么"联名 / 连载 / 持续创作"是**同一件事**：

| 诉求 | 本质动作 |
|---|---|
| 持续创作 | IP 的正典资产库**随时间增长**（每集产出 → 沉淀为新资产） |
| **IP 联名** | 一个作品**同时 import ≥2 个 IP 的资产** |
| 长篇连载 | 后续每集**import 同一批冻结资产**（保证跨集不换脸） |

三者共用**一个机制**：引用冻结资产。这就是第一性原理的收敛点。

## 现状证据（Prism 已有 90% 机器，缺的只是"跨项目化"）

Prism 已经把资产当可复用常量了 —— **但只在一个项目内部**：

| 已有能力 | 证据 | 作用域 |
|---|---|---|
| 资产有稳定 id | `asset-prompt-templates.md:68` `[IDENTITY] <asset_id>, fixed design` | 项目内 |
| 身份块逐字复用是铁律 | 同文件铁律 3「identity block 逐字复用 = 常量」 | 项目内 |
| 资产谱系 | 同文件 L261-263 `base` / `variant`(`__`) / `evolution`(`__<form>`) | 项目内 |
| 分镜引用资产 | `storyboard-schema.json:79` `asset_ref`（**本地 string**） | 项目内 |
| 引用图 | `storyboard-schema.json:83` `ref_image`（**相对 episode 目录的路径**） | 项目内 |
| 跨镜一致性门 | `contracts/asset-consistency.contract.md`（六判据 fail-closed） | 项目内 |
| 资产宿主 | `storyworld/`（characters/scenes/props）+ `masters/.../assets/` | 项目内 |

**缺口精确到这里**：
1. **没有全局地址空间**：`asset_ref` / `ref_image` 是本地字符串/路径，换个项目就解析不到。
2. **没有 import 声明**：没有任何"从别的 IP 取资产"的语法（全仓 rg 无 cross-project/import）。
3. **没有跨 IP 权限与正典门**：引用别人的资产，谁授权？源 IP 未冻结怎么办？
4. **资产宿主分裂**：`storyworld/characters/` 和 `masters/.../assets/` 两处存资产，无统一登记。

## 第一性原理（三句话）

1. **可复用的原子 = 冻结资产**（identity block 逐字 + 引用图 + 稳定 `asset_id` + revision）。
   —— 现有资产机制已证明这一点，只是地址是本地的。
2. **IP = 资产的全局命名空间 + 生命周期 + 发布身份**。
   —— 解决 id 冲突、授权、版本、归属；让"另一个项目"能解析到它。
3. **跨项目复用 = import（引用冻结资产，不改写）**。
   —— 不是复制粘贴（复制 = 两份正典 = 漂移）。**引用边，零副本**，与上一版
   `prism-project-docs-v1` 的 `PRISM_HOME` 零副本铁律同构。

**联名因此不需要新机制**：联名 = 一个作品的 `imports[]` 指向 ≥2 个 IP。天然 N:N。

## 模型形状（最小正确）

```text
content/ips/{ip_id}/                     # 新对象：IP = 正典资产命名空间
  ip.yaml                                #   ip_id, title, kind(fact|story|brand),
                                         #   status(draft|active|paused|archived),
                                         #   default_lane, publish_identity_ref,
                                         #   canon_revision(R)
  assets/
    characters/<asset_id>/               #   identity block(7段) + ref 图 + 谱系(base/variant/evolution)
    scenes/<asset_id>/
    props/<asset_id>/
    styles/<asset_id>/
```

作品侧（storyboard / episode / campaign / master）新增**可选 import 声明**：

```yaml
imports:
  - from: ip_lin                     # 源 IP
    asset: characters/lin            # 资产路径
    revision: R2                     # 钉版本（或不写=跟最新，须显式）
```

解析规则（execution + gate 共用）：
- 解析：默认 `track: latest` → 取源 IP 的**当前最新冻结** identity block，**逐字注入**提示词（复用 `asset-prompt-templates` + `prompt_compiler`）。
- **落盘即钉**：解析时刻的源 IP `canon_revision` 写入作品侧（`resolved_revision`），保证产物**可复现、可追溯**；"跟最新"是**生产时**的行为，不是"产物随时漂"。
- **fail-closed**：源 IP 不存在 / 未冻结 / 资产缺失 / 已钉 revision 与源不符 → blocked + reason_code，**绝不静默降级为本地重描述**（那正是"换脸"的根因）。
- **联名聚合门**：`imports` 涉及 ≥2 个 IP 时，**所有**源 IP 的正典状态须为 frozen（AND），任一未过 → blocked。
- **命名空间**：`asset_id` 在 IP 内唯一；跨 IP 引用一律带 `from`，杜绝冲突。

## 三个诉求 → 一套机制（收敛表）

| 诉求 | 用这套模型怎么做 |
|---|---|
| 持续创作 | IP 资产库随生产增长；每次沉淀出新资产 → IP `canon_revision` +1；已产作品记录 `resolved_revision`，可复现 |
| IP 联名 | 作品 `imports[]` 指向 2 个 IP → 聚合正典门 → 两库资产同台逐字复用 |
| 长篇连载 | 默认 `track: latest`：每集解析到源 IP 当前最新冻结资产 → 跨集同脸；campaign 复用现有对象分组多集 |

## 决策点（用户已拍板 2026-09-30，freeze 的输入）

- **D1 命名**：✅ 采用 **`ip`**，路径 `content/ips/{ip_id}/`（人话"项目/IP"）。
- **D2 原语**：✅ 跨项目复用 = **import 引用（零副本）**，**不做** `content/projects/` 目录根、**不做**资产复制。
- **D3 地址空间**：✅ 资产在 IP 内以 `asset_id` 寻址；跨 IP 引用必须带 `from`；作品侧 `imports[]` 可选、不强制回填旧内容。
- **D4 版本**：✅ **默认 `track: latest`**（跟最新）；解析时刻**落盘记录 `resolved_revision`** 以保证产物可复现；
  已钉 `revision` 者按钉的解析。连载"中途换脸"风险由**源 IP 冻结态 + 落盘 revision 可追溯**兜底，不靠人工钉版本。
- **D5 联名正典门**：✅ 多源 import 时**所有**源 IP 须 frozen（AND, fail-closed）。
- **D6 资产宿主归一**：✅ **存量资产收敛进 IP**：`storyworld/characters|scenes|props/` 与 `masters/.../assets/`
  的资产条目**登记/迁移**为 IP 资产（`content/ips/{ip_id}/assets/...`），storyworld/master 通过 import 引用；
  旧引用走 alias 兼容期。以迁移脚本 + 校验断言保证不丢资产。

## 湖海拆分

判定：**湖**（只动内容模型 / 契约 / 校验，不实现生产链、不做发布自动化）。program `prism-ip-model`：

| 湖 | feature | 交付 | 依赖 |
|---|---|---|---|
| L1 | `prism-ip-schema-v1` | IP 对象 + 资产登记（asset_id/revision/identity block）+ `imports[]` 声明与解析契约 + 校验脚本 + 示例；`docs/prism` 同构自动带 `ips/` | 无（可先冻） |
| L2 | `prism-ip-import-gate-v1` | import 解析门 + 多源正典聚合门 + 跨 IP 授权/披露钩子（接 F1/F2 联名署名分成） | L1 |
| L3（defer） | `prism-ip-continuity-v1` | IP 级连续性投影：revision 演进、season 投影、intel/master/director 面按 IP 收敛 | L1 |

**L1 单独就交付"资产可跨项目地址化 + 可声明引用"**；L2 才让引用**可执行、可把关**。

## Promotion Notes（转 truth 的 AC 候选）

- AC-IPM-001：注册 `ip` 对象，路径 `content/ips/{ip_id}/`，契约 `contracts/ip.schema.yaml`；`ip.yaml` 含 identity/status/revision/publish_identity_ref。
- AC-IPM-002：IP 资产条目含稳定 `asset_id` + `revision` + 冻结 identity block(7段) + 引用图；跨 IP 寻址须带 `from`（命名空间不冲突）。
- AC-IPM-003：作品侧（storyboard/episode/campaign/master）支持**可选** `imports[]:{from,asset,track|revision}`，默认 `track: latest`；旧内容不强制回填。
- AC-IPM-004：import 解析逐字注入 identity block；`track: latest` 解析后把源 IP 当时的 `canon_revision` 落盘为 `resolved_revision`（可复现/可追溯）；源 IP 缺失/未冻结/资产缺失/已钉 revision 不符 → fail-closed + reason_code，**禁止静默本地重描述**。
- AC-IPM-005：多源 import（联名）时聚合正典门 = 所有源 IP frozen（AND, fail-closed）。
- AC-IPM-006：校验脚本可验证 IP 注册 + import 引用可解析 + 命名空间唯一。
- AC-IPM-007：`docs/prism` 同构断言自动包含 `ips/`（复用 `check_prism_project_docs.sh --init-shape`）。
- AC-IPM-008：存量资产收敛——`storyworld/characters|scenes|props/` 与 `masters/.../assets/` 的资产条目登记进 IP
  `content/ips/{ip_id}/assets/`，storyworld/master 经 import 引用；迁移脚本**幂等**且**不丢资产**（迁移前后资产计数/清单一致），旧引用 alias 兼容有校验断言。

## Decision Priority（冲突裁决）

1. 契约（`contracts/*.contract.md`）> 本地约定。
2. **资产引用一律走 import 边，禁止复制**（复制 = 双正典 = 漂移，同 `PRISM_HOME` 零副本精神）。
3. 向后兼容：新字段可选，不动已冻结 content/契约的必填面。
4. fail-closed：import/正典门遇缺即阻，绝不静默降级重描述。
5. 最懒可用：能复用 `asset_id`/`asset-prompt-templates`/`asset-consistency` 就不造新机制；
   能复用 campaign 就不造 series；能复用 `docs/prism` 同构就不手工建目录。

## 用户裁决（2026-09-30，本轮）

- 核心判断：**IP = 跨项目可引用的正典资产库（原语=资产引用，不是归属目录）** —— ✅ 与用户意图一致。
- **D1**：✅ 命名 `ip`。
- **D6**：✅ **存量资产收敛进 IP**（迁移登记，不保留双宿主）。
- **D4**：✅ imports **跟最新**（`track: latest`），解析时落盘 `resolved_revision` 保可复现。
- 裁决：**两条 feature 一起冻、并行推进**（`prism-ip-schema-v1` + `prism-shot-iteration-budget-v1`）。

## 附带：`prism-shot-iteration-budget-v1`（并行冻结）

独立 research：`docs/beacon/v0.0.1/research/prism-shot-iteration-budget-v1.md`
（同源推文暴露，与 IP 轴零依赖，本轮一起冻）。

## Promotion Log

- 2026-09-30（第一轮）：planner brainstorm 产出"归属边"模型（`ip_refs[]`）。
- 2026-09-30（第二轮修正）：用户指出 **IP = 跨项目资产引用**；原语从"归属边"修正为
  **"冻结资产的 import 引用"**；三诉求（持续创作/联名/连载）统一到一个机制。
- 2026-09-30（裁决）：D1/D4/D6 拍板；**promoted → freeze `prism-ip-schema-v1`**（输入 D1–D6 + AC-IPM-001..008），
  与 `prism-shot-iteration-budget-v1` 并行冻结。
