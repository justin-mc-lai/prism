#!/usr/bin/env bash
# Lake D5 AV form exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-AV-001 registry
test -f registry/form-registry.yaml || fail "form-registry.yaml missing"
for f in comic vlog book_video; do
  rg -q "$f" registry/form-registry.yaml || fail "$f missing in registry"
done
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert {'comic','vlog','book_video'} <= fs, 'AV forms missing'" || fail "registry AV forms invalid"

# AC-AV-002 contract + routes
test -f contracts/form-av.contract.md || fail "form-av.contract missing"
for pat in comic-storyboard openmontage book_video rnskill; do
  rg -q "$pat" contracts/form-av.contract.md || fail "av contract lacks $pat"
done

# AC-AV-003 director handoff
for pat in treatment "presentation map" "shot list" storyboard; do
  rg -q "$pat" contracts/form-av.contract.md || fail "av contract lacks handoff $pat"
done

# AC-AV-004 routing
rg -q "form-av.contract" skills/_internal/orchestration/creation-mode-map.md || fail "av route ref missing"
rg -q "comic|book_video" skills/_internal/orchestration/creation-mode-map.md || fail "comic/book_video rows missing"

# AC-AV-006 license
rg -q "AGPL|license|ATTRIBUTION|vendor_pin|批准" contracts/form-av.contract.md || fail "license note missing"

# AC-AV-007 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/form-av.contract.md || fail "fail-closed missing"

# AC-AV-008 QA gate
for pat in 乱码 版权 分镜 图序 anti-slop; do
  rg -q "$pat" contracts/form-av.contract.md || fail "av QA gate lacks $pat"
done
rg -q "证据|evidence" contracts/form-av.contract.md || fail "av QA evidence missing"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_av_forms: all Lake D5 gates PASS"
