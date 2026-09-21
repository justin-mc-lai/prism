#!/usr/bin/env bash
# prism-style-presets-overlay-v1 exec gate（真实断言：缺一即 FAIL）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

OVERLAY=registry/style-presets.yaml
BASE=content/pipelines/ai-manga-drama/lumenx-style-presets.json
TMPL=skills/prism-director/references/asset-prompt-templates.md

# AC-SP-001 两文件在位
test -f "$OVERLAY" || fail "$OVERLAY missing"
test -f "$BASE" || fail "$BASE missing"

# AC-SP-002 合并结构可校验：id 唯一 + required_views 可解析 + 必填字段 + 类别声明
python3 - << 'PYEOF' || fail "style preset overlay structure invalid"
import json, sys, yaml
ov = yaml.safe_load(open("registry/style-presets.yaml"))
base = json.load(open("content/pipelines/ai-manga-drama/lumenx-style-presets.json"))

base_ids = [p["id"] for p in base["presets"]]
ov_presets = ov["presets"]
ov_ids = [p["id"] for p in ov_presets]

# 1. overlay 内部唯一
assert len(ov_ids) == len(set(ov_ids)), f"duplicate id inside overlay: {ov_ids}"

# 2. base × overlay 不冲突（合并前提）
clash = set(base_ids) & set(ov_ids)
assert not clash, f"id collision base/overlay: {clash}"

# 3. required_views 四个 id 均可解析到合并集
merged = set(base_ids) | set(ov_ids)
rv = ov["merge"]["required_views"]
assert set(rv) == {"live_action", "animation", "ink_wash", "guofeng"}, f"required_views keys: {set(rv)}"
for view, pid in rv.items():
    assert pid in merged, f"required view {view} -> {pid} not resolvable"

# 4. 每个 overlay preset 必填字段
required = ["id","category","name","name_zh","description","best_for","avoid_for","positive_prompt","negative_prompt"]
for p in ov_presets:
    for k in required:
        assert p.get(k), f"preset {p.get('id')} missing {k}"
    assert isinstance(p["best_for"], list) and p["best_for"], f"{p['id']} best_for not list"

# 5. 新类别已声明
declared = {c["id"] for c in ov["new_categories"]}
used = {p["category"] for p in ov_presets}
assert used <= declared, f"undeclared category used: {used - declared}"

# 6. 国风族在场（用户硬要求）
assert "gongbi_heavy_color" in ov_ids, "guofeng anchor preset missing"
cats = {p["category"] for p in ov_presets}
assert "chinese_traditional" in cats, "chinese_traditional family missing"

print(f"  overlay={len(ov_ids)} presets, base={len(base_ids)}, merged={len(merged)}")
PYEOF

# AC-SP-003 provenance 在场（lumenx MIT + 分层说明）
rg -q "alibaba/lumenx" "$OVERLAY" || fail "overlay lacks lumenx provenance"
rg -q "MIT" "$OVERLAY" || fail "overlay lacks license"
rg -q "原样拷贝" "$OVERLAY" || fail "overlay lacks base-verbatim note"

# AC-SP-004 消费方接线（模板 §1 指向 overlay 为 SoT）
rg -q "registry/style-presets.yaml" "$TMPL" || fail "asset-prompt-templates does not reference overlay SoT"
rg -q "registry/style-presets.yaml" content/pipelines/ai-manga-drama/lumenx-distillation.md \
  || fail "lumenx-distillation does not note the overlay"

# AC-SP-005 四种必备导演视角在 overlay 声明
for v in live_action animation ink_wash guofeng; do
  rg -q "$v" "$OVERLAY" || fail "overlay lacks required view: $v"
done

# AC-SP-006 国风族 ≥4（工笔/敦煌/汉服/国潮）
for pid in gongbi_heavy_color dunhuang_tang_dynasty hanfu_realistic guochao_modern; do
  rg -q "id: $pid" "$OVERLAY" || fail "guofeng family lacks $pid"
done

# AC-SP-007 新增族完整（国漫韩漫/轻量/类型）
for pid in chinese_manhua korean_webtoon bw_manga chibi_cute children_picture_book \
           urban_romance_photoreal period_drama_cn documentary_natural cyberpunk post_apocalyptic; do
  rg -q "id: $pid" "$OVERLAY" || fail "overlay lacks preset $pid"
done

# AC-SP-008 base 未被改写（15 预设仍在，且 overlay 未覆盖 id）
python3 -c "
import json
b=json.load(open('content/pipelines/ai-manga-drama/lumenx-style-presets.json'))
assert len(b['presets'])==15, 'base preset count changed'
assert b['version']==2, 'base version changed'
print('  base 15 presets intact, version 2')
" || fail "base lumenx presets mutated"

# no leak
test ! -f skills/_internal/adapters/SKILL.md || fail "adapter SKILL.md leak"

pass "check_style_presets: all prism-style-presets-overlay-v1 gates PASS"
