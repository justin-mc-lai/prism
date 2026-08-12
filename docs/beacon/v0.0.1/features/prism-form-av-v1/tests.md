---
slug: prism-form-av-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-av-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-AV-001 | AC-AV-001 | `test -f registry/form-registry.yaml && rg -n "comic" registry/form-registry.yaml && rg -n "vlog" registry/form-registry.yaml && rg -n "book_video" registry/form-registry.yaml` | form registry 注册 AV 三形态 |
| TC-AV-002 | AC-AV-002 | `test -f contracts/form-av.contract.md && rg -n "comic-storyboard|openmontage|book_video|rnskill" contracts/form-av.contract.md` | AV 契约含三形态 bridge 路由 |
| TC-AV-003 | AC-AV-003 | `rg -n "treatment|presentation map|shot list|storyboard" contracts/form-av.contract.md` | director handoff 字段 |
| TC-AV-004 | AC-AV-004 | `rg -n "form-av.contract" skills/_internal/orchestration/creation-mode-map.md && rg -n "comic|book_video" skills/_internal/orchestration/creation-mode-map.md` | 路由引用 AV 契约 |
| TC-AV-005 | AC-AV-005 | `test -x scripts/check_av_forms.sh` | exec 脚本存在且可执行 |
| TC-AV-006 | AC-AV-005 | `bash scripts/check_av_forms.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-AV-007 | AC-AV-001 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; raise SystemExit(0 if {'comic','vlog','book_video'}<=fs else 1)"` | registry 含 AV 三形态 |
| TC-AV-008 | AC-AV-006 | `rg -n "AGPL|license|ATTRIBUTION|vendor_pin|批准" contracts/form-av.contract.md` | license 注记 |
| TC-AV-009 | AC-AV-007 | `rg -n "fail-closed|blocked|reason_code" contracts/form-av.contract.md` | bridge fail-closed |
| TC-AV-010 | AC-AV-008 | `rg -n "乱码|版权|分镜|图序|anti-slop" contracts/form-av.contract.md && rg -n "证据|evidence" contracts/form-av.contract.md` | QA 门与证据 |
| TC-AV-011 | AC-AV-009 | `test -f skills/prism-qa/references/anti-slop-gate.md && test ! -f contracts/form-av.contract.md.qa` | maker≠checker 分离 |
| TC-AV-012 | AC-AV-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md && rg -n "D6" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md` | 分湖边界存在 |
| TC-AV-013 | AC-AV-010 | `rg -n "Illegal|illegal|宣称 Lake D" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-AV-014 | AC-AV-002 | `rg -n "US-AV-001|漫画" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md` | 漫画旅程可追溯 |
| TC-AV-015 | AC-AV-002 | `rg -n "US-AV-002|vlog|US-AV-003|book_video" docs/beacon/v0.0.1/features/prism-form-av-v1/truth.md` | vlog/book_video 旅程可追溯 |
