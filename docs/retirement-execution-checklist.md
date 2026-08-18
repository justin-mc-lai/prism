# 退役执行清单（Prism 替换 selfmedia-creator）

> 状态：待所有者决策（`docs/owner-license-decision.md`）后执行。
> 前置事实（已核）：蒸馏层无源仓可运行（`scripts/check_standalone_distill.sh` PASS）；
> 34 个 bridge 已装；license 评估已记录（matrix）。

## 分支 A：A1 MIT 声明（推荐 · 全链自足）

1. 所有者在 `docs/owner-license-decision.md` 勾选 A1 并填写授权日期。
2. 将 ATTRIBUTION 草稿落为 `docs/ATTRIBUTION-render-chain.md`。
3. pin 渲染脚本族 + templates 进 Prism（`scripts/` + `templates/`，随附 ATTRIBUTION）。
4. `registry/writing-adapters.yaml` / `publish-adapters.yaml` 渲染 bridge 改指向本地 pin。
5. `registry/source-capability-inventory.md` 退役条件 a) 标记完成。
6. 复跑全量门禁（7 个）+ 新增渲染样本（image-post 渲染后过 OCR 门）。
7. 源仓降级只读 archive（仓库归档/冻结标记，不删除）。
8. 移除 bridge 回源路径（install 脚本保留但标注 archive-only）。

## 分支 B：A2 自用私有许可（可 pin 不公开）

1. 勾选 A2；ATTRIBUTION 标注「自用私有许可，不对外再分发」。
2. 执行分支 A 第 2-6 步（公开发布仍走 bridge + 人工批准）。
3. 公开发布场景不承诺脱离源仓。

## 分支 C：A3 维持现状（bridge 永久化）

1. 勾选 A3；退役不执行，源仓保持读写。
2. 新增「bridge 状态页」：34 个 bridge + 凭证类 bridge 的可用性清单。
3. 每年复核 license 评估与 pin 候选变化。

## 共通收尾（三个分支都做）

- [ ] `README.md` 退役状态段落更新
- [ ] `registry/adapter-migration-matrix.md` 退役记录
- [ ] `.beacon` 版本收口记录（release 门）
- [ ] 人工确认（公开发布永远需要）
