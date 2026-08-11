# Adapter contract: intel

> Internal only. Not host-discoverable. Seven-segment per contracts/skill-contract-7seg.tpl.md

## 1. identity
- skill_id: adapter-intel
- public_or_adapter: adapter
- one_liner: Lake B indexed adapter stub for intel; body extraction deepens in Lake D

## 2. 决策边界
- 能决定：按公开面 handoff 执行局部变换
- 不能决定：不改母稿事实/正典；不自证 QA；不公开发布
- 必须上抛：缺证据、跨公开面路由、人工批准点

## 3. intake
- 必填输入：上游公开面输出路径 + 冻结母稿引用（若适用）
- 拒绝条件：无冻结母稿却要求 produce；无证据却要求放行

## 4. output contract
- 人类面产出：不直接对人暴露本 adapter 名
- 机器面产出：artifact paths + evidence refs
- 路径约定：content/ 或 .beacon/evidence/（后续湖落地）

## 5. gate
- 通过条件：产出文件存在且满足上游 gate 声明
- fail-closed：缺证据 / 正典漂移 / 公开未批准
- 证据路径：.beacon/evidence/

## 6. handoff
- 下一公开面：由 registry/public-surface.yaml + orchestration routing 决定
- 禁止跳过：qa 与 human release 批准

## 7. 失败处理
- 可重试：生成类可修复失败
- 必须停并等人：发布/正典/合规
- 禁止自证通过：true
