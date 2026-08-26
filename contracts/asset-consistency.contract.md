# Gate contract: asset-consistency（Lake D · 资产一致性门）

> 执行契约。判断框架蒸馏见 `skills/prism-director/references/asset-consistency-gate.md`
> （MAP-017）；适用 manga_drama 及后续多集 AV 形态。

## 1. identity

- gate_id: asset-consistency
- 适用形态: manga_drama（首批）、live_drama 分镜阶段、comic 多集
- 上游蒸馏: drama-skills/short-drama-assets（MIT）+ alibaba/lumenx（MIT，仅框架）

## 2. 决策边界

- 能决定：身份/变体/瞬态归类、binding 解析判定、边界匹配结论、stale 标记
- 不能决定：母稿事实与正典、QA 最终 verdict、公开发布

## 3. intake

- 已冻结 storyboard.json（含角色卡 + asset_ref）+ assets/ 目录（身份条目 + 风格锚点帧）

拒绝：assets/ 缺身份条目或风格锚点帧 → blocked + `reason_code=asset_identity_missing`

## 4. output

- 审计记录: `content/presentations/{vertical}/{slug}/manga-drama-{ep}/asset-consistency.json`
  （每镜头 boundary-match 结果 + 每条变化 CON-04 五要素 + binding 表）
- 证据: `.beacon/evidence/implement/prism-manga-asset-gate-v1/AC-MAG-003.json`

## 5. gate（六判据，任一失败 fail-closed）

1. 三分法完整：每个 asset_ref 归类身份/变体/瞬态，无未决流入分镜（AST-05）
2. 识别锚点：身份条目含可见/可生成/可比对锚点，无空泛质量词
3. 边界匹配（CON-01）：相邻镜头 end→start 逐字段一致或有变化记录支撑
4. 变化记录（CON-04）：前态/后态/原因/范围/受影响 ID 五要素齐全
5. 画风统一：全部镜头引用同一风格锚点版本；换版有生效记录
6. 与既有门叠加：`asset_refs_exist` 仍必须通过；本门是加强不是替代

## 6. handoff

- 位于 director → produce 交接与 prism-qa 复核两处执行；结论供 QA SCORECARD 引用

## 7. 失败处理

- 可重试：补身份条目、补变化记录、重出分镜
- 必须停：正典冲突、未决项伪造已确认、发布动作
- 禁止自证通过: true
