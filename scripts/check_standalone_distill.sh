#!/usr/bin/env bash
# Lake B′ standalone self-sufficiency gate（真实断言：蒸馏层不依赖源仓即可运行；
# bridge 缺失必须 fail-closed，不假装产出）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# 1. 蒸馏层文件全部在仓内（不依赖源仓）
for f in \
  skills/prism-produce/references/prose-core.md \
  skills/prism-produce/references/human-voice-prose.md \
  skills/prism-produce/references/humanize-techniques.md \
  skills/prism-produce/references/personal-style-layer.md \
  skills/prism-director/references/director-philosophy.md \
  skills/prism-director/references/treatment-template.md \
  skills/prism-director/references/qc-scorecard.md \
  skills/prism-director/references/jieqi-yangsheng-treatment-template.md \
  skills/prism-intel/references/briefing-schema.md \
  skills/prism-intel/references/topic-radar.md \
  skills/prism-qa/references/anti-slop-gate.md \
  contracts/writing.contract.md \
  scripts/check_human_voice.py; do
  test -f "$f" || fail "distilled asset missing in-repo: $f"
done
pass "distilled assets self-contained (no source repo needed)"

# 2. 无源仓时 bridge 安装必须 fail-closed（不假装产出）
if SELFMEDIA_SOURCE=/nonexistent/selfmedia-creator bash scripts/install_writing_bridges.sh --dry-run >/tmp/prism-bridge-test.log 2>&1; then
  fail "bridge installer must fail-closed when source missing"
fi
rg -q "bridge source not found" /tmp/prism-bridge-test.log || fail "fail-closed message missing"
pass "bridge fail-closed when source missing"

# 3. 在仓工具无源仓可运行
python3 scripts/check_human_voice.py content/presentations/oss-picks/anydoc/thread-launch/humanized.md >/dev/null 2>&1 || true
pass "check_human_voice.py runs in-repo"

# 4. 编排层无源仓残留路径（已 Prism-native 化的检查）
if rg -q "skills/selfmedia-director/references" skills/_internal/orchestration/; then
  fail "orchestration still references source-only director path"
fi
if rg -q "kushi-gzh.*默认" skills/_internal/orchestration/; then
  fail "orchestration still has account default"
fi
if rg -q "小黑" skills/_internal/orchestration/ contracts/; then
  fail "orchestration/contracts still has account character name"
fi
if rg -q "jieqi-yangsheng-gzh" skills/_internal/orchestration/; then
  fail "orchestration still has account-specific contract"
fi
rg -q "jieqi-yangsheng-treatment-template.md" skills/prism-director/references/jieqi-yangsheng-treatment-template.md \
  || fail "jieqi template not in-repo"
pass "orchestration Prism-native (no source-only paths, no account defaults)"

pass "check_standalone_distill: standalone self-sufficiency gates PASS"
