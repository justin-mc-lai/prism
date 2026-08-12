---
slug: prism-form-image-post-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-form-image-post-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-IMG-001 | AC-IMG-001 | `test -f registry/form-registry.yaml && rg -n "image-post" registry/form-registry.yaml && rg -n "xhs" registry/form-registry.yaml` | form registry 注册 image-post/xhs |
| TC-IMG-002 | AC-IMG-002 | `test -f contracts/form-image-post.contract.md && rg -n "20 字|20字|caption|1-9|9 张|封面|乱码|图序|尺寸" contracts/form-image-post.contract.md` | 贴图契约含核心规则 |
| TC-IMG-003 | AC-IMG-003 | `test -f contracts/form-xhs.contract.md && rg -n "xhs-article-to-images|OCR|fail-closed|blocked" contracts/form-xhs.contract.md` | xhs 契约含 bridge 与 OCR 门 |
| TC-IMG-004 | AC-IMG-004 | `rg -n "form-image-post.contract|form-xhs.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由引用 form 契约 |
| TC-IMG-005 | AC-IMG-005 | `test -x scripts/check_image_post_forms.sh` | exec 脚本存在且可执行 |
| TC-IMG-006 | AC-IMG-005 | `bash scripts/check_image_post_forms.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-IMG-007 | AC-IMG-001 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/form-registry.yaml')); fs={f['form'] for f in d['forms']}; raise SystemExit(0 if {'image-post','xhs'}<=fs else 1)"` | registry 含 image-post+xhs |
| TC-IMG-008 | AC-IMG-006 | `rg -n "配置|配置化|禁止.*硬编码|kushi" contracts/form-image-post.contract.md && rg -n "account|账号" contracts/form-image-post.contract.md` | 账号配置化声明 |
| TC-IMG-009 | AC-IMG-007 | `rg -n "fail-closed|blocked|reason_code" contracts/form-image-post.contract.md contracts/form-xhs.contract.md` | bridge fail-closed |
| TC-IMG-010 | AC-IMG-008 | `rg -n "乱码|随机文字|图序|尺寸|分离|价值" contracts/form-image-post.contract.md && rg -n "证据|evidence" contracts/form-image-post.contract.md` | OCR/QA 门与证据 |
| TC-IMG-011 | AC-IMG-009 | `test -f skills/prism-qa/references/anti-slop-gate.md && test ! -f contracts/form-image-post.contract.md.qa` | maker≠checker 分离 |
| TC-IMG-012 | AC-IMG-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md && rg -n "D4|D5|D6" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md` | 分湖边界存在 |
| TC-IMG-013 | AC-IMG-010 | `rg -n "Illegal|illegal|宣称 Lake D" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md` | illegal 转移覆盖 |
| TC-IMG-014 | AC-IMG-002 | `rg -n "US-IMG-001|贴图包" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md` | 贴图包旅程可追溯 |
| TC-IMG-015 | AC-IMG-003 | `rg -n "US-IMG-002|小红书" docs/beacon/v0.0.1/features/prism-form-image-post-v1/truth.md` | xhs 旅程可追溯 |
