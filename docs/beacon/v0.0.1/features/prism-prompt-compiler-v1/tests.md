---
slug: prism-prompt-compiler-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-prompt-compiler-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-PPC-001 | AC-PPC-001 | `test -f skills/prism-director/references/script-templates.md && rg -n "完整剧本\|分集剧本\|镜头清单\|onlyshot" skills/prism-director/references/script-templates.md` | 三模板 + 上游出处在场 |
| TC-PPC-002 | AC-PPC-002 | `bash scripts/check_prompt_compiler.sh` | 编译器确定性 + 四产物 + 未知风格 fail-closed |
| TC-PPC-003 | AC-PPC-003 | `python3 -c "import json; s=json.load(open('content/pipelines/ai-manga-drama/storyboard-schema.json')); assert 'ref_image' in json.dumps(s)" && rg -n "ref_image\|_check_ref_image" scripts/ai_manga_drama.py` | schema + CLI 双向接线 |
| TC-PPC-004 | AC-PPC-004 | `test -f contracts/asset-render.contract.md && python3 -c "import yaml; yaml.safe_load(open('registry/render-adapters.yaml'))" && rg -n "credentials_never_in_repo\|fail-closed" contracts/asset-render.contract.md` | 契约七节 + 适配器 yaml 可解析 |
| TC-PPC-005 | AC-PPC-005 | `bash scripts/check_render_handoff.sh` | 无兜底反断言 + 三条负例 exit≠0 |
| TC-PPC-006 | AC-PPC-006 | `rg -n "asset-render.contract" contracts/form-manga-drama.contract.md && python3 -c "import yaml; d=yaml.safe_load(open('registry/form-registry.yaml')); m=[f for f in d['forms'] if f['form']=='manga_drama'][0]; assert 'prompt_compiler' in m['producer_chain'] and 'provider-only' in m['producer_chain']"` | 契约 + registry 链同步 |
| TC-PPC-007 | AC-PPC-007 | `bash scripts/check_prompt_compiler.sh && bash scripts/check_render_handoff.sh && bash scripts/check_asset_consistency.sh && bash scripts/check_prompt_syntax.sh && bash scripts/check_style_presets.sh && bash scripts/check_asset_prompt_templates.sh && bash scripts/check_director_distill.sh` | 新增门禁 PASS + 零回归 |
| TC-PPC-008 | AC-PPC-005 | `rg -n "Illegal transitions" docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/truth.md && rg -n "无凭证时产出任何|未过 \`prompt_compiler\` 直接进|片段缺失/规格不符仍拼接" docs/beacon/v0.0.1/features/prism-prompt-compiler-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-PPC-009 | AC-PPC-005 | `rg -n "missing_credential_terminates\|missing_clip_terminates\|no_local_fallback" registry/render-adapters.yaml` | 三条终止守卫入册 |
| TC-PPC-010 | AC-PPC-002 | `rg -n "ref_image" content/pipelines/ai-manga-drama/fixtures/ep-compile-test/storyboard.json` | fixture 覆盖 ref_image 路径 |
