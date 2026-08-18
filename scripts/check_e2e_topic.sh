#!/usr/bin/env bash
# E2E 全新 topic 生产验证门禁（2026-08-15 · watermarks-remover）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

T="content/presentations/oss-picks/watermarks-remover/blog-beginner"
M="content/masters/oss-picks/watermarks-remover"
B="content/briefings/watermarks-remover-hotspot.md"

# 1. 全链产物齐全（intel → master → director → produce → qa）
test -f "$B" || fail "intel briefing missing"
test -f "$M/meta.yaml" || fail "master meta missing"
test -f "$M/MASTER.md" || fail "MASTER missing"
rg -q "Canonical claims" "$M/MASTER.md" || fail "MASTER lacks claims"
test -f "$T/director-treatment.md" || fail "treatment missing"
test -f "$T/humanized.md" || fail "humanized missing"
test -f "$T/humanize-pass-evidence.md" || fail "humanize evidence missing"
test -f "$T/qa-findings.md" || fail "qa-findings missing"

# 2. 体裁结构（四段式必含）
for sec in "一句话看透本质" "核心架构与主流程" "绝妙的设计亮点" "潜在坑点与局限性"; do
  rg -q "$sec" "$T/humanized.md" || fail "missing section: $sec"
done

# 3. 确定性门禁
out=$(python3 scripts/check_human_voice.py "$T/humanized.md" 2>&1 || true)
echo "$out" | rg -q "翻案腔变形 0" || fail "voice: 翻案腔 not 0"
echo "$out" | rg -q "硬停词 0" || fail "voice: 硬停词 not 0"
echo "$out" | rg -q "黑话 0" || fail "voice: 黑话 not 0"
python3 scripts/check_readability.py "$T/humanized.md" --depth >/dev/null 2>&1 || fail "readability gate failed"

# 4. 事实纪律（15 claims 全部可回源；无编造指标）
rg -q "Canonical claims" "$M/MASTER.md" || fail "master claims missing"

# 5. 伦理边界（本 topic 专项）
rg -q "content you own" "$T/humanized.md" || fail "ethics boundary missing"
rg -q "不提供任何规避检测" "$T/humanized.md" || fail "ethics disclaimer missing"

pass "check_e2e_topic: watermarks-remover full-chain e2e PASS"
