# Adapter contract: learning-memory（Lake E4 · 可回放学习记忆）

> 学习契约。advisory only：不定义 truth、不通 gate、不给 QA/release verdict。

## 1. identity

- skill_id: adapter-learning-memory
- public_or_adapter: adapter
- one_liner: 把复盘发现沉淀为可回放、可审计、可裁剪的记忆
- depends_on: contracts/review-loop.contract.md（E3）

## 2. 决策边界

- 能决定：记忆结构、置信度、适用边界、prune 建议
- 不能决定：requirement truth、gate 判定、QA/release verdict

## 3. intake（必填）

- source_ref（E3 复盘/数据来源）+ claim + confidence + applicability + 时间

拒绝：无 source_ref/时间 → blocked + reason_code=learning_source_missing

## 4. output

- 记忆: `.beacon/memory/prism-learning/{memory_id}.yaml`（或受管 memory 存储）
- 字段: memory_id / source_ref / claim / confidence / applicability / created_at / evidence
- 证据: `.beacon/evidence/implement/prism-learning-memory-v1/AC-LMEM-001.json`

## 5. gate（边界）

- advisory only：learning 不定义 truth、不通 gate、不给 QA/release verdict
- 可回放：每条记忆带 source_ref + 时间 + 回放路径（evidence）
- 可裁剪：冲突/过时记忆显式 conflict/prune 标记，裁剪保留审计痕迹
- 不静默合并冲突记忆

## 6. handoff

- 下一面: intel/plan 可回放引用（advisory），不替代任何 gate

## 7. 失败处理

- 可重试: 字段补全、置信度校准、换 bridge
- 必须停: 来源缺失、越界写入 truth、冲突未标记
- 禁止自证通过: true
