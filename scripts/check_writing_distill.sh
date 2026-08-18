#!/usr/bin/env bash
# Lake B′ writing/humanize deep-distillation exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

# 1. prose-core 蒸馏
test -f skills/prism-produce/references/prose-core.md || fail "prose-core.md missing"
for pat in 像说话一样 一句话只讲一个意思 倒金字塔 主动语态 正面表述; do
  rg -q "$pat" skills/prism-produce/references/prose-core.md || fail "prose-core lacks $pat"
done

# 2. human-voice-prose 三道门 + 禁令
test -f skills/prism-produce/references/human-voice-prose.md || fail "human-voice-prose.md missing"
for pat in 材料门 说话位置 翻案腔 硬禁令清单 体裁裁决表 改稿七遍 冷读终检; do
  rg -q "$pat" skills/prism-produce/references/human-voice-prose.md || fail "human-voice-prose lacks $pat"
done
rg -q "5 件具体材料" skills/prism-produce/references/human-voice-prose.md || fail "human-voice-prose lacks 材料门阈值"

# 3. humanize-techniques 蒸馏
test -f skills/prism-produce/references/humanize-techniques.md || fail "humanize-techniques.md missing"
for pat in 句式长短交错 口语连接 800 字 平台差异 降套路提示词; do
  rg -q "$pat" skills/prism-produce/references/humanize-techniques.md || fail "humanize-techniques lacks $pat"
done

# 3c. 个人文风层蒸馏（2026-08-17 情报吸收）
test -f skills/prism-produce/references/personal-style-layer.md || fail "personal-style-layer.md missing"
for pat in 个人文风文件 修改学习循环 作者信息密度 场景口径 收尾自检; do
  rg -q "$pat" skills/prism-produce/references/personal-style-layer.md || fail "personal-style-layer lacks $pat"
done

# 3b. 体裁原型蒸馏（emotional-essay / oss-daily / visual-enrich）
test -f skills/prism-produce/references/emotional-essay-archetype.md || fail "emotional-essay-archetype.md missing"
for pat in 命名权 行为证据 否定定义 间接代入 7 拍 新区分 判别开关 失败模式; do
  rg -q "$pat" skills/prism-produce/references/emotional-essay-archetype.md || fail "emotional-essay lacks $pat"
done
test -f skills/prism-produce/references/oss-daily-archetype.md || fail "oss-daily-archetype.md missing"
rg -q "今日榜单" skills/prism-produce/references/oss-daily-archetype.md || fail "oss-daily lacks 榜单结构"
test -f skills/prism-produce/references/visual-enrich.md || fail "visual-enrich.md missing"
for pat in 官方文档站 manifest 图说 引导阅读; do
  rg -q "$pat" skills/prism-produce/references/visual-enrich.md || fail "visual-enrich lacks $pat"
done
rg -q "emotional-essay-archetype" contracts/writing.contract.md || fail "writing.contract lacks archetype ref"

# 4. anti-slop-gate 深化（场景档位 + 仲裁 + 停手门检）
for pat in 场景档位 仲裁顺序 不发明事实 停手门检 真人文本; do
  rg -q "$pat" skills/prism-qa/references/anti-slop-gate.md || fail "anti-slop-gate lacks $pat"
done
count=$(grep -c '^- ' skills/prism-qa/references/anti-slop-gate.md || true)
test "$count" -ge 30 || fail "anti-slop bullets <30 (got $count)"

# 5. check_human_voice.py 已 pin 且可运行
test -f scripts/check_human_voice.py || fail "check_human_voice.py missing"
python3 scripts/check_human_voice.py --help >/dev/null 2>&1 || fail "check_human_voice.py not runnable"
rg -q "MIT" scripts/check_human_voice.py || fail "check_human_voice.py lacks MIT attribution"

# 5b. check_readability.py Prism 原生实现 + 规则蒸馏
test -f scripts/check_readability.py || fail "check_readability.py missing"
python3 scripts/check_readability.py content/presentations/oss-picks/anydoc/blog-beginner/humanized.md --depth >/dev/null 2>&1 || fail "readability gate fails on blog sample"
python3 scripts/check_readability.py content/presentations/oss-picks/anydoc/thread-launch/humanized.md >/dev/null 2>&1 || fail "readability gate fails on thread sample"
rg -q "Readability 门" skills/prism-produce/references/prose-core.md || fail "prose-core lacks readability rules"

# 6. 写作契约已接线
rg -q "human-voice-prose" contracts/writing.contract.md || fail "writing.contract lacks human-voice-prose ref"
rg -q "仲裁顺序" contracts/writing.contract.md || fail "writing.contract lacks 仲裁顺序"

# 7. 盘点与矩阵补全
test -f registry/source-capability-inventory.md || fail "source-capability-inventory.md missing"
rg -q "MAP-016" registry/adapter-migration-matrix.md || fail "matrix lacks MAP-016"

# 8. bridge 安装器存在且幂等
test -x scripts/install_writing_bridges.sh || fail "install_writing_bridges.sh missing/not executable"

pass "check_writing_distill: all Lake B′ deep-distillation gates PASS"
