#!/usr/bin/env bash
# Validate all Prism 1+6 public surfaces (Lake B′ production samples).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
VALIDATE="${VALIDATE:-/Users/apple/Developer/Personal/oss-sync/core-skills/openai-skills/skills/.system/skill-creator/scripts/quick_validate.py}"

surfaces=(goal intel master director produce qa release)
for s in "${surfaces[@]}"; do
  echo "=== prism-$s ==="
  python3 "$VALIDATE" "skills/prism-$s"
  bash "skills/prism-$s/scripts/check_${s}_shell.sh"
done

count="$(find skills -maxdepth 2 -path 'skills/prism-*/SKILL.md' ! -path 'skills/prism-kernel/*' | wc -l | tr -d ' ')"
test "$count" = "7" || { echo "FAIL: expected 7 public shells, got $count" >&2; exit 1; }
test ! -f skills/_internal/adapters/SKILL.md || { echo "FAIL: adapter host leak" >&2; exit 1; }
rg -q "MAP-009" registry/adapter-migration-matrix.md

echo "PASS: all 7 Prism public surfaces production-sample gates"
