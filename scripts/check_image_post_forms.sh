#!/usr/bin/env bash
# Lake D3 image-post/xhs form exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# AC-IMG-001 registry
test -f registry/form-registry.yaml || fail "form-registry.yaml missing"
rg -q "image-post" registry/form-registry.yaml || fail "image-post missing in registry"
rg -q "xhs" registry/form-registry.yaml || fail "xhs missing in registry"
python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; assert {'image-post','xhs'} <= fs, 'forms missing'" || fail "registry forms invalid"

# AC-IMG-002 image-post contract
test -f contracts/form-image-post.contract.md || fail "form-image-post.contract missing"
for pat in "20 字" "caption" "1–9" "封面" "乱码" "图序" "尺寸"; do
  rg -q "$pat" contracts/form-image-post.contract.md || fail "image contract lacks $pat"
done
rg -q "证据|evidence" contracts/form-image-post.contract.md || fail "image contract lacks evidence"
rg -q "配置|禁止.*硬编码|kushi" contracts/form-image-post.contract.md || fail "image contract lacks account config rule"

# AC-IMG-003 xhs contract
test -f contracts/form-xhs.contract.md || fail "form-xhs.contract missing"
for pat in "xhs-article-to-images" "OCR" "fail-closed" "blocked"; do
  rg -q "$pat" contracts/form-xhs.contract.md || fail "xhs contract lacks $pat"
done

# AC-IMG-004 routing
rg -q "form-image-post.contract|form-xhs.contract" skills/_internal/orchestration/creation-mode-map.md || fail "route refs missing"

# AC-IMG-007 fail-closed
rg -q "fail-closed|blocked|reason_code" contracts/form-image-post.contract.md contracts/form-xhs.contract.md || fail "fail-closed missing"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_image_post_forms: all Lake D3 gates PASS"
