#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }
S=skills/prism-produce
test -f "$S/SKILL.md" || fail "SKILL.md"
test -f "$S/agents/openai.yaml" || fail "openai.yaml"
test -f "$S/references/skill-ir.md" || fail "skill-ir"
test -f "$S/references/modes/form-produce.md" || fail "mode file"
test -f "$S/evals/evals.json" || fail "evals"
test -f "$S/manifest.json" || fail "manifest"
rg -q "operating_mode: production" "$S/SKILL.md" || fail "production mode"
rg -q "public_id: \"produce\"" "$S/SKILL.md" || fail "public_id"
rg -q "MAP-" "$S/references/adapter-migration-pointer.md" || fail "MAP pointer"
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL leak"
pass "prism-produce production shell checks"
