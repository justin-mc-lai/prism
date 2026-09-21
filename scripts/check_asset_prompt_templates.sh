#!/usr/bin/env bash
# prism-asset-prompt-templates-v1 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

REF=skills/prism-director/references/asset-prompt-templates.md

# AC-APT-001 蒸馏参考在位 + 十节结构
test -f "$REF" || fail "$REF missing"
for pat in "三条铁律" "风格正交" "通用 7 段 identity block" "人物卡" "场景卡" "道具卡" \
           "神兽卡" "群像卡" "四视图水印陷阱" "拟物化的真假陷阱" "变体与进化的命名规则" \
           "落盘映射" "候选数与成本" "自查清单" "授权与边界"; do
  rg -q "$pat" "$REF" || fail "asset-prompt-templates lacks section: $pat"
done

# AC-APT-002 identity block 七个显式标签全在场
for tag in '\[IDENTITY\]' '\[BODY\]' '\[FACE\]' '\[ATTIRE\]' '\[LAYOUT\]' '\[STYLE\]' '\[NEGATIVE\]'; do
  rg -q -- "$tag" "$REF" || fail "identity block lacks segment $tag"
done

# AC-APT-003 三条铁律 + 上游实测阈值在场（数字不是裸写）
for pat in "neutral flat lighting" "visual reference anchoring" "逐字复用" "前 200 token" "≤5" "40%" "5%"; do
  rg -q -- "$pat" "$REF" || fail "asset-prompt-templates lacks rule/threshold: $pat"
done
rg -q "单项目" "$REF" || fail "asset-prompt-templates lacks provenance caveat"

# AC-APT-004 风格正交接线（资产 × 风格 笛卡尔积 + 指向风格预设）
rg -q "lumenx-style-presets.json" "$REF" || fail "lacks style-preset wiring"
rg -q "笛卡尔积" "$REF" || fail "lacks orthogonality statement"
rg -q "positive_prompt" "$REF" || fail "lacks positive_prompt mapping"

# AC-APT-005 五类资产模板各自有 LAYOUT 视图定义
for pat in "4 宫格" "四宫格" "白底产品图" "尺度参照" "数量与密度约束"; do
  rg -q "$pat" "$REF" || fail "asset class template lacks: $pat"
done

# AC-APT-006 防坑规则在场
for pat in "NO text labels" "NO annotations" "the character IS" "wearing it" "NO human face"; do
  rg -q -- "$pat" "$REF" || fail "pitfall rule lacks: $pat"
done

# AC-APT-007 变体/进化语义（base 永不覆盖 + 保留谱系）
for pat in "base" "variant" "evolution" "永不覆盖" "谱系标记"; do
  rg -q -- "$pat" "$REF" || fail "variant/evolution rule lacks: $pat"
done

# AC-APT-008 落盘映射到 storyboard 三类 + creature/crowd 升级路径
for pat in "characters\[\]" "scenes\[\]" "props\[\]" "holder" "kind" "ponytail:" "creatures\[\]" "crowds\[\]"; do
  rg -q -- "$pat" "$REF" || fail "landing map lacks: $pat"
done

# AC-APT-009 fail-closed 边界（未过清单不进资产库）
rg -q "fail-closed" "$REF" || fail "lacks fail-closed boundary"
rg -q "AST-05" "$REF" || fail "lacks AST-05 reference"

# AC-APT-010 ATTRIBUTION 接线（模板三圣经 + ref 工艺 + 未复制运行时）
ATT=docs/ATTRIBUTION-drama-prompt-repos.md
test -f "$ATT" || fail "$ATT missing"
for pat in "ref-prompt-industrial" "角色圣经" "场景圣经" "道具圣经" "onlyshot"; do
  rg -q "$pat" "$ATT" || fail "ATTRIBUTION lacks $pat"
done
rg -q "asset-prompt-templates" "$ATT" || fail "ATTRIBUTION lacks distilled template pointer"

# AC-APT-011 上游模板原件仍在 vendor（未被误删，蒸馏≠搬走）
for t in 05_角色圣经.md 06_场景圣经.md 07_道具圣经.md; do
  test -f "vendor/skills/onlyshot/assets/templates/$t" || fail "vendor template missing: $t"
done
test -f vendor/skills/onlyshot/references/ref-prompt-industrial.md || fail "vendor ref-prompt-industrial missing"

# AC-APT-012 director 侧接线（资产门 / 语法表 指向本表）
rg -q "asset-prompt-templates" skills/prism-director/references/asset-consistency-gate.md \
  || fail "asset-consistency-gate does not reference asset-prompt-templates"
rg -q "asset-prompt-templates" skills/prism-director/references/prompt-syntax-table.md \
  || fail "prompt-syntax-table does not reference asset-prompt-templates"

# AC-APT-013 master 侧接线（提取框架指向本表）
rg -q "asset-prompt-templates" skills/prism-master/references/storyworld-extraction.md \
  || fail "storyworld-extraction does not reference asset-prompt-templates"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_asset_prompt_templates: all prism-asset-prompt-templates-v1 gates PASS"
