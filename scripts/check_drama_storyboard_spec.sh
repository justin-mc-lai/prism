#!/usr/bin/env bash
# drama-storyboard-spec exec gate（真实断言：缺一即 FAIL）
# 参考：skills/prism-director/references/drama-storyboard-spec.md（MJ-*）
# 契约：contracts/drama-storyboard-spec.contract.md · 实现：scripts/drama_spec.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

REF=skills/prism-director/references/drama-storyboard-spec.md
CON=contracts/drama-storyboard-spec.contract.md
IMPL=scripts/drama_spec.py
COMPILER=scripts/prompt_compiler.py
FX=content/pipelines/ai-manga-drama/fixtures/ep-xianxia-spec

test -f "$REF" || fail "$REF missing"
test -f "$CON" || fail "$CON missing"
test -f "$IMPL" || fail "$IMPL missing"
test -f "$FX/storyboard.json" || fail "manju fixture storyboard missing"

# 1. MJ 规则完整覆盖：参考必须含全部 86 条规则 ID（无缺、无多）
python3 - << 'PYEOF' || fail "MJ rule coverage incomplete"
from pathlib import Path
import re
groups = {
    "UNIT": 5, "FIELD": 4, "LINE": 5, "EMO": 8, "VFX": 4, "CONT": 8, "BLOCK": 9,
    "CAM": 2, "SFX": 4, "BAN": 3, "TPL": 8, "CHAR": 7, "SCENE": 12, "WEAP": 7,
}
expected = set()
for g, n in groups.items():
    for i in range(1, n + 1):
        expected.add(f"MJ-{g}-{i:02d}")
ref = Path("skills/prism-director/references/drama-storyboard-spec.md").read_text(encoding="utf-8")
found = set(re.findall(r"MJ-[A-Z]+-[0-9]{2}", ref))
missing, extra = expected - found, found - expected
assert not missing, f"missing rules: {sorted(missing)}"
assert not extra, f"unexpected rules: {sorted(extra)}"
print(f"MJ coverage: {len(found)}/{len(expected)} rules")
PYEOF

# 2. 阈值与关键量在场（可校验数字）
for pat in "15" "5-8" "3-5" "20%" "30 字" "5-6 字/秒" "7-8 字/秒" "4-5 字/秒" "十个字以内" "16:9" "纯白" "纯黑" "三格横向排列" "四格横向排列" "音频要求"; do
  rg -q -- "$pat" "$REF" || fail "drama-storyboard-spec lacks $pat"
done

# 3. 契约：gate_id + 十一判据 + reason codes + 禁止自证
for pat in "gate_id: drama-storyboard-spec" "十一判据" "fail-closed" "禁止自证通过: true" "drama_spec_beats_missing" "drama_spec_sfx_too_long" "drama_spec_blocking_missing" "drama_spec_banned_content"; do
  rg -q -- "$pat" "$CON" || fail "contract lacks $pat"
done

# 4. 契约源标注义务：条件化（题材+模型）非物理常数
rg -q "神魔修仙" "$CON" || fail "contract lacks conditioning caveat"
rg -q "Seedance 2.0" "$CON" || fail "contract lacks model conditioning"

# 5. 正向：fixture 过门
python3 "$IMPL" --storyboard "$FX/storyboard.json" > /dev/null || fail "fixture failed drama spec gate"
python3 scripts/ai_manga_drama.py validate --storyboard "$FX/storyboard.json" > /dev/null || fail "fixture failed combined validate"

# 6. 负向：每类违规命中对应 reason code（直接 import，不打洞 fixture）
python3 - << 'PYEOF' || fail "negative cases did not fail as expected"
import copy, json, sys
from pathlib import Path
sys.path.insert(0, "scripts")
from drama_spec import validate_drama_spec
base = json.loads(Path("content/pipelines/ai-manga-drama/fixtures/ep-xianxia-spec/storyboard.json").read_text(encoding="utf-8"))

def codes(sb):
    return " ".join(validate_drama_spec(sb)["errors"])

def mutate(fn):
    sb = copy.deepcopy(base); fn(sb); return codes(sb)

cases = {
    "drama_spec_spec_flag_missing": lambda s: s.pop("spec"),
    "drama_spec_beat_count": lambda s: s["shots"][0].update(beats=s["shots"][0]["beats"][:4]),
    "drama_spec_beat_duration": lambda s: s["shots"][0]["beats"][0].update(duration_seconds=6),
    "drama_spec_sfx_missing": lambda s: s["shots"][0]["beats"][0].update(sfx=""),
    "drama_spec_sfx_too_long": lambda s: s["shots"][0]["beats"][0].update(sfx="一二三四五六七八九十一"),
    "drama_spec_line_too_long": lambda s: s["shots"][0]["beats"][0].update(dialogue="字" * 31),
    "drama_spec_blocking_missing": lambda s: s["shots"][0]["beats"][0].update(blocking=""),
    "drama_spec_camera_unknown": lambda s: s["shots"][0]["beats"][0].update(shot_size="中全景"),
    "drama_spec_vfx_missing": lambda s: s["shots"][0]["beats"][0].update(vfx=""),
    "drama_spec_banned_content": lambda s: s["shots"][0]["beats"][0].update(description="露出内脏与断肢"),
    "drama_spec_closeup_ratio": lambda s: [b.update(shot_size="中景") for b in s["shots"][0]["beats"]],
}
for code, fn in cases.items():
    got = mutate(fn)
    assert code in got, f"{code} not triggered; got: {got}"
print(f"negative cases: {len(cases)}/{len(cases)} reason codes triggered")
PYEOF

# 7. 编译产出：分镜脚本.md + 每分镜含音频要求固定行 + 子镜小节
python3 "$COMPILER" --episode "$FX" --style chinese_manhua > /dev/null
test -s "$FX/分镜脚本.md" || fail "分镜脚本.md missing"
test -s "$FX/drama-spec.json" || fail "drama-spec.json audit missing"
n_shots="$(rg -c '^## 分镜' "$FX/分镜脚本.md")"
test "$n_shots" = "4" || fail "expected 4 shot sections, got $n_shots"
n_audio="$(rg -c '音频要求：不要背景音乐，不要字幕，不要解说声音。' "$FX/分镜脚本.md")"
test "$n_audio" = "4" || fail "audio-required line count $n_audio != 4"
rg -q '^  - 0-3秒：' "$FX/分镜脚本.md" || fail "分镜脚本 lacks beat time slices"
rg -q "【人物：" "$FX/分镜脚本.md" || fail "分镜脚本 lacks 【人物：】 field"
rg -q "特效：" "$FX/分镜脚本.md" || fail "分镜脚本 lacks 特效 field"
rg -q "音效：" "$FX/分镜脚本.md" || fail "分镜脚本 lacks 音效 field"

# 8. manju 资产布局：16:9 四视图/三视图 + 无戏剧光污染
rg -q "人物四视图，16:9比例" "$FX/资产提示词.md" || fail "character manju layout missing"
rg -q "兵器三视图，16:9比例" "$FX/资产提示词.md" || fail "prop manju layout missing"
rg -q "无瞳孔颜色细节" "$FX/资产提示词.md" || fail "manju char eye rule missing"
rg -qi "cinematic lighting|lens flare|chiaroscuro" "$FX/资产提示词.md" && fail "asset prompt leaked drama-light token"

# 9. 确定性：两次编译逐字节一致（含 分镜脚本.md / drama-spec.json）
TMP="$(mktemp -d)"
for f in 资产提示词.md 图片提示词.md 视频提示词.md 分镜脚本.md drama-spec.json ep-xianxia-spec.srt; do cp "$FX/$f" "$TMP/"; done
python3 "$COMPILER" --episode "$FX" --style chinese_manhua > /dev/null
for f in 资产提示词.md 图片提示词.md 视频提示词.md 分镜脚本.md drama-spec.json ep-xianxia-spec.srt; do
  cmp -s "$TMP/$f" "$FX/$f" || fail "compiler not deterministic: $f"
done
rm -rf "$TMP"

# 10. registry 接线：shared_gates 引用本门
REG=registry/form-registry.yaml
rg -q "drama-storyboard-spec.contract.md" "$REG" || fail "form-registry lacks drama-storyboard-spec wiring"
rg -q "drama-storyboard-spec" skills/prism-director/references/modes/treatment-director.md \
  || fail "mode lacks drama-storyboard-spec ref"

pass "check_drama_storyboard_spec: all drama-storyboard-spec gates PASS"
