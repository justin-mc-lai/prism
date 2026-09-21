#!/usr/bin/env bash
# 镜头提示词语法门 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# 1. vendor 四源在位 + LICENSE 未被剔除
for v in short-drama-skills onlyshot su-ai-short-drama shuohao-skills; do
  test -d "vendor/skills/$v" || fail "vendor/skills/$v missing"
  find "vendor/skills/$v" -maxdepth 2 -iname "LICENSE*" | rg -q . || fail "vendor/skills/$v has no LICENSE"
done

# 2. 蒸馏参考非 stub：语法表九类断言
REF=skills/prism-director/references/prompt-syntax-table.md
test -f "$REF" || fail "$REF missing"
for pat in 三层分离 字段定式 分镜图 8 段定式 时长公式 切镜触发条件 动作戏语法 对话戏语法 五条视觉转化规则 失败模式 反向禁项; do
  rg -q "$pat" "$REF" || fail "prompt-syntax-table lacks $pat"
done

# 3. 硬阈值可校验（数字必须在场）
for pat in "12s" "15s" "6s" "8s" "20%" "60%" "1500"; do
  rg -q -- "$pat" "$REF" || fail "prompt-syntax-table lacks threshold $pat"
done

# 4. 阈值来源标注义务在场（不是裸数字）
rg -q "N=36" "$REF" || fail "prompt-syntax-table lacks N=36 provenance caveat"

# 5. contract 非 stub：八判据 + 拒绝码
CON=contracts/prompt-syntax.contract.md
test -f "$CON" || fail "$CON missing"
for pat in "gate_id: prompt-syntax" "三层分离" "时长合规" "切镜有据" "空镜配比" "动作语法" "提示词卫生" "反向禁项" "fail-closed" "禁止自证通过: true"; do
  rg -q "$pat" "$CON" || fail "prompt-syntax.contract lacks $pat"
done
for pat in prompt_syntax_master_missing prompt_syntax_assets_unclassified prompt_syntax_shot_fields_missing; do
  rg -q "$pat" "$CON" || fail "prompt-syntax.contract lacks reason_code $pat"
done
rg -q "八判据" "$CON" || fail "prompt-syntax.contract lacks gate count"

# 6. registry 接线：shared_gates + 五形态 producer_chain 引用
REG=registry/form-registry.yaml
rg -q "shared_gates:" "$REG" || fail "form-registry lacks shared_gates"
rg -q "prompt-syntax.contract.md" "$REG" || fail "form-registry lacks prompt-syntax wiring"
rg -q "asset-consistency.contract.md" "$REG" || fail "form-registry lost asset-consistency wiring"
for f in comic vlog book_video manga_drama live_drama; do
  awk -v f="- form: $f" '
    index($0, f) { p=1; next }
    p && /status:/ { p=0 }
    p && /prompt-syntax.contract/ { found=1 }
    END { exit !found }
  ' "$REG" || fail "form $f does not reference prompt-syntax.contract"
done

# 7. ATTRIBUTION 声明：四仓 + 未 vendor 的说明
ATT=docs/ATTRIBUTION-drama-prompt-repos.md
test -f "$ATT" || fail "$ATT missing"
for pat in YvonneMovingon A-cat-with-carrots doublesq97-ui eternityspring AIPrompts; do
  rg -q "$pat" "$ATT" || fail "ATTRIBUTION lacks $pat"
done
rg -q "切勿商业使用" "$ATT" || fail "ATTRIBUTION lacks AIPrompts exclusion reason"

# 8. 无泄漏：vendor 源不得含 .git
find vendor/skills/short-drama-skills vendor/skills/onlyshot vendor/skills/su-ai-short-drama vendor/skills/shuohao-skills -name ".git" | rg -q . \
  && fail "vendored repo contains .git"

# 9. yaml 可解析
python3 -c "import yaml,sys; yaml.safe_load(open('registry/form-registry.yaml')); yaml.safe_load(open('registry/adapter-index.yaml'))" \
  || fail "registry yaml not parseable"

pass "check_prompt_syntax: all prompt-syntax gates PASS"
