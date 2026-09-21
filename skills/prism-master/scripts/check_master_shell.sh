#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }
S=skills/prism-master
test -f "$S/SKILL.md" || fail "SKILL.md"
test -f "$S/agents/openai.yaml" || fail "openai.yaml"
test -f "$S/references/skill-ir.md" || fail "skill-ir"
test -f "$S/references/modes/freeze-master.md" || fail "mode file"
test -f "$S/references/modes/extract-storyworld.md" || fail "extract-storyworld mode file"
test -f "$S/references/storyworld-extraction.md" || fail "storyworld-extraction ref"
for pat in 身份 变体 镜头瞬态 故事语义 interior exterior holder 未决 识别锚点 连续性锁 画面代称; do
  rg -q "$pat" "$S/references/storyworld-extraction.md" || fail "storyworld-extraction lacks $pat"
done
rg -q "extract-storyworld" "$S/SKILL.md" || fail "SKILL lacks extract-storyworld mode row"
rg -q "extract-storyworld" "$S/references/modes/INDEX.md" || fail "INDEX lacks extract-storyworld"
rg -q "extract-storyworld" "$S/references/skill-ir.md" || fail "skill-ir lacks extract-storyworld"
rg -q "scenes/" contracts/storyworld.schema.yaml || fail "storyworld schema lacks scenes/"
rg -q "props/" contracts/storyworld.schema.yaml || fail "storyworld schema lacks props/"
rg -q "\"scenes\"" content/pipelines/ai-manga-drama/storyboard-schema.json || fail "storyboard schema lacks scenes"
rg -q "\"props\"" content/pipelines/ai-manga-drama/storyboard-schema.json || fail "storyboard schema lacks props"
test -f "$S/evals/evals.json" || fail "evals"
test -f "$S/manifest.json" || fail "manifest"
rg -q "operating_mode: production" "$S/SKILL.md" || fail "production mode"
rg -q "public_id: \"master\"" "$S/SKILL.md" || fail "public_id"
rg -q "MAP-" "$S/references/adapter-migration-pointer.md" || fail "MAP pointer"
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL leak"
pass "prism-master production shell checks"
