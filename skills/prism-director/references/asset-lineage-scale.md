# 资产谱系与尺寸冻结（asset-lineage-scale）

> 内部参考：供 `prism-director` 在建资产卡与 evolution 链时执行。
> 上游方法论：onlyshot 7 段 identity block（`asset-prompt-templates.md`）+ 本仓三分法
> （`asset-consistency-gate.md` §1）；本文件新增 **LIN（谱系）** 与 **SCL（尺寸）** 两组规则，
> 执行契约见 `contracts/asset-consistency.contract.md` 判据 7–8（fail-closed）。
> 实例：`~/workspace/doomsday-l6-manju/analysis/资产卡_一致性冻结_v1.0.md`（L6 八阶段）。

## 1. 谱系标记（LIN）：进化不得丢失的身份证

每个资产在 `[IDENTITY]` 段声明 `lineage: <谱系名>`；有 evolution 链的资产另声明
`lineage markers: <M-1> / <M-2> / ...`。

**LIN-01（硬）**：任一 `evolution` 版本必须完整保留其 base 的全部 lineage markers。
少一个 marker = `asset_lineage_broken`，blocked。观众认不出"这是同一台/同一个人"，
进化即失败。

谱系标记的选取标准（按优先级）：
1. 全剧最高辨识度视觉元素（如 L6 的血红贯穿式星环灯）；
2. 贯穿各形态的材质/色彩基底（如哑光黑）；
3. 形态转换的残留痕迹（如车门变肩甲的接缝、轮胎纹）。

**LIN-02**：evolution 链命名 `<asset_id>__<form>`；base 永不覆盖；进化方向只增不减
（S7 不得长得像另一台车）。

## 2. 尺寸冻结（SCL）：体型不得悄悄膨胀

**SCL-01（硬）**：每个资产 `traits` 必须含**尺度锚**，二选一：
- 人物：`>N head units` 或等价身高（如 `height ~180cm`）；
- 载具/神兽/道具：物理尺寸（如 `length ~5.0m`）+ ref 图每格**人形剪影尺度条**
  （`human silhouette scale bar in each quadrant`，写进 `[LAYOUT]` 段）。

缺尺度锚 = `asset_scale_missing`，blocked。空泛词（"精致""巨大""很长"）不算锚点。

**SCL-02**：有 evolution 链的资产必须附**尺寸对照表**（阶段/形态/全长全高/尺度锚），
相邻阶段体型跃迁必须在变化记录（CON-04）中说明原因。S5 8 米 → S7 50 米这类跃迁
无记录 = 观众出戏，blocked。

## 3. 变体登记表（与 CON-04 对齐）

`variant`（换装/换状态）不新建身份，但必须登记一行：

| 资产 | 变体 ID | 变化（前态→后态） | 原因 | 生效范围 |
|---|---|---|---|---|

五要素对齐 CON-04（前态/后态/原因/范围/受影响 ID）。未登记的变体不得流入分镜（AST-05）。

## 4. 反模式

| 反模式 | 后果 |
|---|---|
| evolution 新形态丢失谱系标记 | 观众认不出是同一个，`asset_lineage_broken` |
| 只写"巨大化"不写尺寸 | S1→S7 体型比漂移，`asset_scale_missing` |
| 换装直接新建人物卡 | 身份爆炸，binding 失效 |
| ref 图无尺度条 | 模型自由发挥体型，跨镜必崩 |
| 把情绪写进 FACE 段 | 污染 ref，污染后无法做中性锚点 |
