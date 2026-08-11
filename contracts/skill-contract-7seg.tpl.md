# Prism Skill Contract（七段）· Template

> 来源：Lake A AC-PRISM-006。公开面与 adapter 均须填满；adapter 不对外发现。

## 1. identity

- skill_id:
- public_or_adapter: public | adapter
- public_id: (if public)
- human_verb:
- one_liner:

## 2. 决策边界

- 能决定：
- 不能决定：
- 必须上抛给人 / 上游公开面：

## 3. intake

- 必填输入：
- 可选输入：
- 拒绝条件：

## 4. output contract

- 人类面产出：
- 机器面产出（mode_id / lane / evidence）：
- 路径约定：

## 5. gate

- 通过条件：
- fail-closed 条件：
- 证据路径：

## 6. handoff

- 下一公开面：
- 交接物：
- 禁止跳过：

## 7. 失败处理

- 可重试：
- 必须停并等人：
- 禁止自证通过：
