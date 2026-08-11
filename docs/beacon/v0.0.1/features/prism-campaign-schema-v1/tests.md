---
slug: prism-campaign-schema-v1
version: v0.0.1
revision_id: R1
materials_status: stale
package_shape: v1.6.10
---

# Tests: prism-campaign-schema-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-SCHEMA-001 | AC-SCHEMA-001 | `test -f registry/content-schema.yaml && rg -n "schema_version" registry/content-schema.yaml && rg -n "master-content" registry/content-schema.yaml && rg -n "storyworld" registry/content-schema.yaml && rg -n "campaign" registry/content-schema.yaml` | schema 注册表存在 |
| TC-SCHEMA-002 | AC-SCHEMA-002 | `test -f contracts/master-content.schema.yaml && rg -n "kind:" contracts/master-content.schema.yaml && rg -n "fact\|story" contracts/master-content.schema.yaml && rg -n "content/masters" contracts/master-content.schema.yaml` | Master 布局契约存在 |
| TC-SCHEMA-003 | AC-SCHEMA-003 | `test -f contracts/storyworld.schema.yaml && rg -n "canon-ledger" contracts/storyworld.schema.yaml && rg -n "content/storyworlds" contracts/storyworld.schema.yaml` | StoryWorld 契约存在 |
| TC-SCHEMA-004 | AC-SCHEMA-004 | `test -f contracts/campaign.schema.yaml && rg -n "campaign_id" contracts/campaign.schema.yaml && rg -n "lane" contracts/campaign.schema.yaml && rg -n "master_refs" contracts/campaign.schema.yaml` | Campaign 契约存在 |
| TC-SCHEMA-005 | AC-SCHEMA-005 | `test -f contracts/narrative-episode.schema.yaml && rg -n "episode_id" contracts/narrative-episode.schema.yaml && rg -n "canon_gate_status" contracts/narrative-episode.schema.yaml` | Episode 契约存在 |
| TC-SCHEMA-006 | AC-SCHEMA-006 | `test -f contracts/distribution-binding.schema.yaml && rg -n "binding_id" contracts/distribution-binding.schema.yaml && rg -n "content/distribution" contracts/distribution-binding.schema.yaml` | Binding 契约存在 |
| TC-SCHEMA-007 | AC-SCHEMA-007 | `rg -n "canon gate|canon_gate|illegal" contracts/narrative-episode.schema.yaml skills/_internal/orchestration/pipeline-contract.md && rg -n "fast_lane_skip" skills/_internal/orchestration/pipeline-contract.md` | canon 钩子与 illegal 声明 |
| TC-SCHEMA-008 | AC-SCHEMA-008 | `test -f contracts/master-freeze-checklist.md && rg -n "MAP-004" registry/adapter-migration-matrix.md && rg -n "distilled_schema" registry/adapter-migration-matrix.md` | MAP-004 加深 |
| TC-SCHEMA-009 | AC-SCHEMA-009 | `rg -n "US-PRISM-002|连载" docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md && rg -n "content/distribution/campaigns" skills/prism-goal/references/modes/loop-campaign.md` | 连载旅程路径对齐 |
| TC-SCHEMA-010 | AC-SCHEMA-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md && rg -n "Lake D" docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md` | 分湖边界存在 |
| TC-SCHEMA-011 | AC-SCHEMA-002 | `test -f content/masters/README.md && test -f content/masters/_examples/fact-sample/meta.yaml && test -f content/masters/_examples/story-sample/meta.yaml` | master scaffold 示例 |
| TC-SCHEMA-012 | AC-SCHEMA-003 | `test -f content/storyworlds/README.md && test -f content/storyworlds/_examples/demo-world/world.yaml` | storyworld scaffold 示例 |
| TC-SCHEMA-013 | AC-SCHEMA-004 | `test -f content/distribution/campaigns/_examples/serial-demo.yaml` | campaign 示例文件 |
| TC-SCHEMA-014 | AC-SCHEMA-007 | `rg -n "Illegal transitions|illegal" docs/beacon/v0.0.1/features/prism-campaign-schema-v1/truth.md` | illegal 转移在 truth 中覆盖 |
| TC-SCHEMA-015 | AC-SCHEMA-001 | `bash scripts/check_content_schema.sh` | exec-layer schema 校验脚本 PASS |
