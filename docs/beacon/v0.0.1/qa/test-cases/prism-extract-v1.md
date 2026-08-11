---
slug: prism-extract-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-extract-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-EXTRACT-001 | AC-EXTRACT-001 | `test -d .git && test -f README.md && test -f AGENTS.md` | 独立仓存在 |
| TC-EXTRACT-002 | AC-EXTRACT-002 | `rg -n "Lake B|Prism|1\\+6" docs/beacon/v0.0.1/constitution/prism-constitution.md && test -f docs/beacon/v0.0.1/constitution/lake-a-prism-canon-v1-r3.truth.md` | 宪法迁入存在 |
| TC-EXTRACT-003 | AC-EXTRACT-003 | `test -f skills/prism-goal/SKILL.md && test -f skills/prism-intel/SKILL.md && test -f skills/prism-master/SKILL.md && test -f skills/prism-director/SKILL.md && test -f skills/prism-produce/SKILL.md && test -f skills/prism-qa/SKILL.md && test -f skills/prism-release/SKILL.md` | 七公开面壳存在 |
| TC-EXTRACT-004 | AC-EXTRACT-004 | `rg -n "scheme: A-1plus6" registry/public-surface.yaml && rg -n "max_public_harnesses: 6" registry/public-surface.yaml && rg -n "public_id: goal" registry/public-surface.yaml` | 公开面注册表合法 |
| TC-EXTRACT-005 | AC-EXTRACT-005 | `rg -n "^## 1\\. identity" contracts/skill-contract-7seg.tpl.md && rg -n "^## 2\\. 决策边界" contracts/skill-contract-7seg.tpl.md && rg -n "^## 7\\. 失败处理" contracts/skill-contract-7seg.tpl.md` | 七段模板存在 |
| TC-EXTRACT-006 | AC-EXTRACT-006 | `rg -n "这次做了什么" contracts/human-card.md && rg -n "需要你决定" contracts/human-card.md && rg -n "下一步" contracts/human-card.md && rg -n "机器面" contracts/human-card.md` | 人类卡契约存在 |
| TC-EXTRACT-007 | AC-EXTRACT-007 | `test -f skills/_internal/orchestration/skill-routing.md && test -f skills/_internal/orchestration/quality-gates.md && test -f skills/_internal/orchestration/creation-mode-map.md && test -f skills/_internal/orchestration/pipeline-contract.md` | 编排内核迁入 |
| TC-EXTRACT-008 | AC-EXTRACT-008 | `rg -n "MAP-001" registry/adapter-index.yaml && rg -n "MAP-009" registry/adapter-index.yaml && test ! -f skills/_internal/adapters/SKILL.md` | adapter 索引且不可见 |
| TC-EXTRACT-009 | AC-EXTRACT-009 | `rg -n "prism-canon-v1" docs/beacon/v0.0.1/constitution/prism-constitution.md && rg -n "selfmedia-creator" registry/adapter-index.yaml && rg -n "R3" docs/beacon/v0.0.1/constitution/prism-constitution.md` | 源溯源存在 |
| TC-EXTRACT-010 | AC-EXTRACT-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-extract-v1/truth.md && rg -n "Lake D" docs/beacon/v0.0.1/features/prism-extract-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-extract-v1/truth.md` | 分湖边界存在 |
| TC-EXTRACT-011 | AC-EXTRACT-003 | `python3 -c "from pathlib import Path; n=sum(1 for p in Path('skills').glob('prism-*/SKILL.md') if 'public_surface: true' in p.read_text()); raise SystemExit(0 if n==7 else 1)"` | 恰好 7 个公开面 frontmatter |
| TC-EXTRACT-012 | AC-EXTRACT-008 | `python3 -c "from pathlib import Path; n=len(list(Path('skills/_internal/adapters').glob('*.contract.md'))); raise SystemExit(0 if n>=7 else 1)"` | ≥7 adapter 契约 stub |
| TC-EXTRACT-013 | AC-EXTRACT-010 | `rg -n "Illegal transitions|illegal|跳过 QA|宣称 Lake D" docs/beacon/v0.0.1/features/prism-extract-v1/truth.md` | illegal 转移覆盖存在 |
