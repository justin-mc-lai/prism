# Prism 人类卡契约

> 来源：Lake A AC-PRISM-014。每次公开面调用结束必须输出。

## 人类面（给人看）

### 这次做了什么

- 状态：
- 产出路径：
- 关键结果（一句话）：

### 需要你决定

- 决策点：
- 选项：
- 默认建议：

### 下一步

- 谁接（公开面 id / 人）：
- 建议动作：

## 机器面（给编排）

```yaml
mode_id:
lane: fast|standard|canon
public_id:
evidence_refs: []
fsm_transition:
transaction_ref:
```

规则：

- 人类面不出现内部 adapter / 子 skill 名（anti-leak）
- 机器面可引用 adapter map_id，不对人展示
