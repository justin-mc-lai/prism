# 分层 SoT 决策：Prism × selfmedia-creator 双仓关系（Layered Source of Truth）

> 状态：**已决策 · 生效中**（decided_by: human，2026-08-21）
> 背景：`selfmedia-creator/ARCHIVED.md` 于 2026-08-14 宣布源仓只读、能力全量蒸馏进 Prism；
> 但 2026-08-21 源仓仍冻结了 `v0.0.5/features/ai-manga-drama` R1 truth——归档声明与实际行为
> 已发生冲突。若不裁决，将出现第三套流程与内容树漂移。本文件是唯一裁决记录。

## 决策

### D1 · 撤销源仓只读归档

`selfmedia-creator` 复活为「统一创作运营台」，承接账号矩阵、环境隔离、渲染执行、发布传输、
发布证据与指标采集。归档结论中"创作规范层已由 Prism 接管"的部分继续成立。

### D2 · 分层唯一写入口（SoT 归属表）

| 层 | 对象 | 唯一写入口 |
|---|---|---|
| L1 规范 | 宪法、7 公开面、QA 门禁 | **Prism** |
| L2 形态 | `registry/form-registry.yaml`、`contracts/form-*.contract.md`、路由 | **Prism**（FP-PRISM-007） |
| L3 创作实例 | briefings / masters / presentations / renders / storyworlds / writing-style | **Prism**（门禁脚本在此侧） |
| L4 运营 | accounts 矩阵、account-contract、环境合同（浏览器/IP）、publish-api / sync-ai / douyin 传输、publications 证据 | **selfmedia-creator** |
| L5 反馈 | metrics / review-loop / learning-memory 的契约 | **Prism**；数据采集在源仓执行 |

同一对象类型禁止两侧同时可写；同名 master slug 双仓并存视为违规。

### D3 · 桥接单向 + fail-closed

- Prism → 源仓：发布/排期经既有 bridge（`install_bridges.sh` 先例），缺桥即阻断生产。
- 源仓 → Prism：仅限 metrics 数据按 E1/E2 契约回传，走确定性脚本，禁止人工双向自由写。
- 凭证永不入任一仓库（沿用 `credentials_never_in_repo`）。

### D4 · 新形态一律走 Prism 注册表

短剧、漫剧等一切新形态按 FP-PRISM-007 进入 `form-registry.yaml` + form contract + 路由，
不得在源仓另立 pipeline 规范。已在源仓冻结的形态 truth（如 ai-manga-drama R1）降级为
research 输入，由本仓重新冻结后转正。

## 生效动作清单

- [x] 本决策文件落库
- [x] `contracts/form-manga-drama.contract.md`（registered，2026-08-21 human 指令转正）
- [x] `registry/form-registry.yaml` `manga_drama` entry（status: registered）
- [x] 源仓漫剧 worktree 已合入 main@07aed5f；CLI + pipeline 目录已 A4 pin 进 Prism 并 validate 通过
- [x] 改 `selfmedia-creator/ARCHIVED.md` 为「部分解档：L4 运营层恢复写入」并指向本文件
- [x] 两仓 AGENTS.md 各加一行 SoT 指针（指向本文件）
- [x] 互斥校验脚本：同名 master slug 双仓可写检测（fail-closed）——`workspace/check_content_mutex.py` + `check_pin_drift.py`，入口 `make -C workspace check`

## 信号与转向

- 生效信号：新形态从注册到首条草稿周期缩短；truth 冻结只出现在 Prism；运营对象只在源仓生长。
- 失效信号：出现第三处母稿目录；fail-closed 桥接拦截被人工绕过；源仓再生长 L1–L3 规范文件。
- **转向条件**：两周内 fail-closed 桥接两次阻断真实生产 ⇒ 放弃跨仓协作，改为物理合并
  （Prism 单仓，账号资产整体搬迁），本表转为迁移清单。

## 记录

- decided_by: human（指令「先落那一页决策文档 + 漫剧 form contract 的迁移稿」，2026-08-21）
- decided_at: 2026-08-21
- 关联：`docs/owner-license-decision.md`（A1/A4/A5 pin 授权继续有效）、
  `selfmedia-creator/docs/beacon/v0.0.5/features/ai-manga-drama/truth.md@R1`
