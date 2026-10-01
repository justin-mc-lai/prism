#!/usr/bin/env bash
# Lake B′ director deep-distillation exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# 1. director-philosophy 蒸馏
test -f skills/prism-director/references/director-philosophy.md || fail "director-philosophy.md missing"
for pat in 意图第一性 叙事世界一致性 展示优于说教 注意力稀缺 冲突是动力 钩子类型 文本三层 结局; do
  rg -q "$pat" skills/prism-director/references/director-philosophy.md || fail "director-philosophy lacks $pat"
done

# 2. treatment-template 蒸馏
test -f skills/prism-director/references/treatment-template.md || fail "treatment-template.md missing"
for pat in Core Intent Logline Conflict Narrative World Emotional Curve Production Reality Presentation Variants Non-Goals Next Gate 验收清单; do
  rg -q "$pat" skills/prism-director/references/treatment-template.md || fail "treatment-template lacks $pat"
done

# 3. qc-scorecard 蒸馏
test -f skills/prism-director/references/qc-scorecard.md || fail "qc-scorecard.md missing"
for pat in 生产门 treatment-approval 评分卡 满分 70 通过规则 自动阻断 失败响应 分镜颗粒度; do
  rg -q "$pat" skills/prism-director/references/qc-scorecard.md || fail "qc-scorecard lacks $pat"
done

# 4. adapter contract 非 stub
test -f skills/_internal/adapters/director.contract.md || fail "director.contract.md missing"
rg -q "MAP-002" skills/_internal/adapters/director.contract.md || fail "director.contract lacks MAP-002"
rg -q "意图第一性" skills/_internal/adapters/director.contract.md || fail "director.contract lacks distilled content"
rg -q "stub" skills/_internal/adapters/director.contract.md && fail "director.contract still stub"

# 5. mode 接线
rg -q "director-philosophy" skills/prism-director/references/modes/treatment-director.md || fail "mode lacks philosophy ref"
rg -q "qc-scorecard" skills/prism-director/references/modes/treatment-director.md || fail "mode lacks qc ref"
rg -q "45 分" skills/prism-director/references/modes/treatment-director.md || fail "mode lacks QC threshold"

# 6. 矩阵状态
rg -q "MAP-002.*distilled" registry/adapter-migration-matrix.md || fail "matrix MAP-002 not marked distilled"

# 7. 无泄漏
test ! -f skills/prism-director/references/SKILL.md || fail "director reference SKILL.md leak"

# 8. continuity-seven-laws 蒸馏（Toonflow 七律 + ai-comic-studio 再诠释）
test -f skills/prism-director/references/continuity-seven-laws.md || fail "continuity-seven-laws.md missing"
for pat in 动作连续性 景别递进法则 视轴守恒 朝向空间逻辑 信息控制意识 节拍密度约束 头尾安全区; do
  rg -q "$pat" skills/prism-director/references/continuity-seven-laws.md || fail "continuity-seven-laws lacks $pat"
done
rg -q "Toonflow-app" skills/prism-director/references/continuity-seven-laws.md || fail "continuity-seven-laws lacks Toonflow source"
rg -q "方向相反" skills/prism-director/references/continuity-seven-laws.md || fail "continuity-seven-laws lacks divergence note"
rg -q "continuity-seven-laws" skills/prism-director/references/modes/treatment-director.md || fail "mode lacks continuity ref"
rg -q "continuity-seven-laws" docs/ATTRIBUTION-drama-prompt-repos.md || fail "ATTRIBUTION lacks continuity-seven-laws"

# 9. 剧本/分镜模板蒸馏（onlyshot 03_完整剧本 / 剧本 / 镜头清单 / 分镜.json）
test -f skills/prism-director/references/script-templates.md || fail "script-templates.md missing"
for pat in 完整剧本 分集剧本 镜头清单 世界观 钩子 卡点 连戏检查 景别分布; do
  rg -q "$pat" skills/prism-director/references/script-templates.md || fail "script-templates lacks $pat"
done
rg -q "onlyshot" skills/prism-director/references/script-templates.md || fail "script-templates lacks upstream attribution"
rg -q "script-templates" skills/prism-director/references/modes/treatment-director.md || fail "mode lacks script-templates ref"
rg -q "script-templates" docs/ATTRIBUTION-drama-prompt-repos.md || fail "ATTRIBUTION lacks script-templates"
rg -q "不手写" skills/prism-director/references/script-templates.md || fail "script-templates lacks no-handwritten-prompt rule"

pass "check_director_distill: all Lake B′ director distillation gates PASS"
