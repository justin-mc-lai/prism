#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }
S=skills/prism-release
test -f "$S/SKILL.md" || fail "SKILL.md"
test -f "$S/agents/openai.yaml" || fail "openai.yaml"
test -f "$S/references/skill-ir.md" || fail "skill-ir"
test -f "$S/references/modes/draft-release.md" || fail "mode file"
test -f "$S/evals/evals.json" || fail "evals"
test -f "$S/manifest.json" || fail "manifest"
rg -q "operating_mode: production" "$S/SKILL.md" || fail "production mode"
rg -q "public_id: \"release\"" "$S/SKILL.md" || fail "public_id"
rg -q "MAP-" "$S/references/adapter-migration-pointer.md" || fail "MAP pointer"
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL leak"

# AC-RAV-001/002/003 AV/manga 交接门（prism-release-av-gate-v1）
M="$S/references/modes/draft-release.md"
for pat in "pending_human" "AI 标识" "自动.{0,6}发布"; do
  rg -q "$pat" "$M" || fail "draft-release lacks AV handoff: $pat"
done
rg -q "asset-render.contract" "$M" || fail "draft-release lacks asset-render ref"
rg -q "render-adapters" "$M" || fail "draft-release lacks render-adapters ref"
rg -q "release_ai_label_missing" "$M" || fail "draft-release lacks ai-label fail code"
rg -q "AI 提示标识" "$S/SKILL.md" || fail "SKILL lacks AI label obligation"
rg -q "pending_human" "$S/SKILL.md" || fail "SKILL lacks pending_human terminal state"
# 反断言：release 面不得出现自动发布路径
rg -q "自动发布路径" "$S/SKILL.md" || fail "SKILL lacks auto-publish prohibition"
rg -qi --glob '!**/check_release_shell.sh' -- "auto-publish|publish --auto|auto_publish[[:space:]]*[:=][[:space:]]*true" "$S" && fail "release surface exposes auto-publish path"

pass "prism-release production shell checks"
