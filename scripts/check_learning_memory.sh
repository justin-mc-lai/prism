#!/usr/bin/env bash
# Lake E4 learning-memory exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-LMEM-001 contract fields
test -f contracts/learning-memory.contract.md || fail "learning-memory.contract missing"
for pat in memory_id source_ref claim confidence applicability; do
  rg -q "$pat" contracts/learning-memory.contract.md || fail "contract lacks $pat"
done

# AC-LMEM-002 registry
test -f registry/learning-adapters.yaml || fail "learning-adapters.yaml missing"
rg -q "memory-store|recall|prune" registry/learning-adapters.yaml || fail "adapter entries missing"
python3 -c "import yaml; d=yaml.safe_load(open('registry/learning-adapters.yaml')); assert len(d['adapters'])>=3, 'adapters <3'" || fail "adapters <3"

# AC-LMEM-003 advisory only
for pat in "不定义 truth" "不通 gate" verdict advisory; do
  rg -q "$pat" contracts/learning-memory.contract.md || fail "contract lacks advisory $pat"
done

# AC-LMEM-004 routing
rg -q "learning-memory.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route ref missing"

# AC-LMEM-006 replayable
for pat in source_ref 时间 回放; do
  rg -q "$pat" contracts/learning-memory.contract.md || fail "contract lacks replay $pat"
done

# AC-LMEM-007 prune/conflict
for pat in 冲突 conflict prune 裁剪; do
  rg -q "$pat" contracts/learning-memory.contract.md || fail "contract lacks prune $pat"
done

# AC-LMEM-008 boundary
for pat in 不替代 QA release; do
  rg -q "$pat" contracts/learning-memory.contract.md || fail "contract lacks boundary $pat"
done

# AC-LMEM-009 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/learning-memory.contract.md || fail "fail-closed missing"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_learning_memory: all Lake E4 gates PASS"
