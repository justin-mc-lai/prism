---
slug: prism-release-av-gate-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-release-av-gate-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-RAV-001 | AC-RAV-001 | `rg -n "pending_human\|AI 标识\|asset-render" skills/prism-release/references/modes/draft-release.md` | mode 含 AV 交接三判据 |
| TC-RAV-002 | AC-RAV-001 | `rg -n "asset-render.contract\|render-adapters" skills/prism-release/references/modes/draft-release.md` | nested refs 接线 |
| TC-RAV-003 | AC-RAV-002 | `rg -n "AI 标识\|pending_human" skills/prism-release/SKILL.md` | SKILL 硬门/boundaries 含义务 |
| TC-RAV-004 | AC-RAV-002 | `rg -q "自动发布\|auto.*publish" skills/prism-release/SKILL.md && ! rg -q "bash.*publish.*--auto" skills/prism-release/SKILL.md` | 无自动发布路径 |
| TC-RAV-005 | AC-RAV-003 | `bash skills/prism-release/scripts/check_release_shell.sh` | surface exec 校验 PASS |
| TC-RAV-006 | AC-RAV-003 | `bash scripts/check_all_public_surfaces.sh` | 7 公开面零回归 |
| TC-RAV-007 | AC-RAV-001 | `rg -n "Illegal transitions" docs/beacon/v0.0.1/features/prism-release-av-gate-v1/truth.md && rg -n "无 AI 标识仍进入发布交接\|未过 QA 进入 release\|静默公开发布" docs/beacon/v0.0.1/features/prism-release-av-gate-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-RAV-008 | AC-RAV-002 | `test ! -f skills/_internal/adapters/SKILL.md` | adapter 无泄漏 |
