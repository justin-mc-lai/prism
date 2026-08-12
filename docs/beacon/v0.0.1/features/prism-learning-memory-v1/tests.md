---
slug: prism-learning-memory-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-learning-memory-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-LMEM-001 | AC-LMEM-001 | `test -f contracts/learning-memory.contract.md && rg -n "memory_id|source_ref|claim|confidence|applicability" contracts/learning-memory.contract.md` | 学习契约含核心字段 |
| TC-LMEM-002 | AC-LMEM-002 | `test -f registry/learning-adapters.yaml && rg -n "memory-store|recall|prune" registry/learning-adapters.yaml` | 学习 bridge 登记 |
| TC-LMEM-003 | AC-LMEM-003 | `rg -n "不定义 truth|不通 gate|verdict|advisory" contracts/learning-memory.contract.md` | advisory-only 边界 |
| TC-LMEM-004 | AC-LMEM-004 | `rg -n "learning-memory.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由学习引用 |
| TC-LMEM-005 | AC-LMEM-005 | `test -x scripts/check_learning_memory.sh` | exec 脚本存在且可执行 |
| TC-LMEM-006 | AC-LMEM-005 | `bash scripts/check_learning_memory.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-LMEM-007 | AC-LMEM-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/learning-adapters.yaml')); raise SystemExit(0 if len(d.get('adapters',[]))>=3 else 1)"` | ≥3 个学习 bridge |
| TC-LMEM-008 | AC-LMEM-006 | `rg -n "source_ref|时间|回放" contracts/learning-memory.contract.md` | 可回放/可审计 |
| TC-LMEM-009 | AC-LMEM-007 | `rg -n "冲突|conflict|prune|裁剪" contracts/learning-memory.contract.md` | 可裁剪/冲突标记 |
| TC-LMEM-010 | AC-LMEM-008 | `rg -n "不替代|QA|release" contracts/learning-memory.contract.md` | 边界声明 |
| TC-LMEM-011 | AC-LMEM-009 | `rg -n "fail-closed|blocked|reason_code" contracts/learning-memory.contract.md` | bridge fail-closed |
| TC-LMEM-012 | AC-LMEM-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md && rg -n "Lake F" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md` | 分湖边界存在 |
| TC-LMEM-013 | AC-LMEM-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-LMEM-014 | AC-LMEM-001 | `rg -n "US-LMEM-001|学习记忆" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md` | 学习旅程可追溯 |
| TC-LMEM-015 | AC-LMEM-007 | `rg -n "US-LMEM-002|冲突" docs/beacon/v0.0.1/features/prism-learning-memory-v1/truth.md` | 冲突路径可追溯 |
