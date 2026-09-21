#!/usr/bin/env bash
# Production-shell sanity for prism-goal (qi-dev production sample).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

test -f skills/prism-goal/SKILL.md || fail "SKILL.md missing"
test -f skills/prism-goal/agents/openai.yaml || fail "agents/openai.yaml missing"
test -f skills/prism-goal/references/skill-ir.md || fail "skill-ir.md missing"
test -f skills/prism-goal/references/modes/loop-campaign.md || fail "loop-campaign.md missing"
test -f skills/prism-goal/references/modes/marketing-engineer.md || fail "marketing-engineer.md missing"
test -f skills/prism-goal/references/marketing-engineer/first-principles.md || fail "marketing-engineer first-principles.md missing"
rg -q "marketing-engineer" skills/prism-goal/references/modes/INDEX.md || fail "marketing-engineer not in modes INDEX"
rg -q "marketing-engineer" skills/prism-goal/SKILL.md || fail "marketing-engineer not in SKILL.md mode table"
test -f skills/prism-goal/evals/evals.json || fail "evals.json missing"
test -f skills/prism-goal/manifest.json || fail "manifest.json missing"

test -f registry/public-surface.yaml || fail "public-surface.yaml missing"
test -f registry/adapter-index.yaml || fail "adapter-index.yaml missing"
test -f registry/adapter-migration-matrix.md || fail "adapter-migration-matrix.md missing"
test -f contracts/human-card.md || fail "human-card.md missing"
test -f docs/beacon/v0.0.1/constitution/prism-constitution.md || fail "constitution missing"

rg -q "public_id: goal" registry/public-surface.yaml || fail "goal not in public-surface"
rg -q "scheme: A-1plus6" registry/public-surface.yaml || fail "scheme missing"
rg -q "max_public_harnesses: 6" registry/public-surface.yaml || fail "harness cap missing"
rg -q "MAP-001" registry/adapter-migration-matrix.md || fail "MAP-001 missing in matrix"
rg -q "MAP-009" registry/adapter-migration-matrix.md || fail "MAP-009 missing in matrix"
rg -q "operating_mode: production" skills/prism-goal/SKILL.md || fail "production mode not declared"

# Anti-leak: top-level adapters must not ship SKILL.md
if test -f skills/_internal/adapters/SKILL.md; then
  fail "adapters must not be host-discoverable (SKILL.md present)"
fi

# Exactly 7 public prism shells
count="$(find skills -maxdepth 2 -path 'skills/prism-*/SKILL.md' ! -path 'skills/prism-kernel/*' | wc -l | tr -d ' ')"
test "$count" = "7" || fail "expected 7 public prism SKILL.md, got $count"

pass "prism-goal production shell checks"
