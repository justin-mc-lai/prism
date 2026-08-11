#!/usr/bin/env bash
set -euo pipefail

test -f registry/content-schema.yaml
test -f contracts/master-content.schema.yaml
test -f contracts/storyworld.schema.yaml
test -f contracts/campaign.schema.yaml
test -f contracts/narrative-episode.schema.yaml
test -f contracts/distribution-binding.schema.yaml
test -f contracts/master-freeze-checklist.md

test -f content/masters/README.md
test -f content/masters/_examples/fact-sample/meta.yaml
test -f content/masters/_examples/story-sample/meta.yaml
test -f content/storyworlds/README.md
test -f content/storyworlds/_examples/demo-world/world.yaml
test -f content/distribution/campaigns/_examples/serial-demo.yaml
test -f content/distribution/bindings/_examples/serial-demo-wechat.yaml

rg -n "schema_version" registry/content-schema.yaml
rg -n "master-content|storyworld|campaign|narrative-episode|distribution-binding" registry/content-schema.yaml
rg -n "kind_enum|fact|story" contracts/master-content.schema.yaml
rg -n "canon-ledger|characters/|timeline/" contracts/storyworld.schema.yaml
rg -n "campaign_id|lane|master_refs" contracts/campaign.schema.yaml
rg -n "canon_gate_status|review_required|passed|failed" contracts/narrative-episode.schema.yaml
rg -n "binding_id|endpoint_ref" contracts/distribution-binding.schema.yaml
rg -n "distilled_schema|MAP-004" contracts/master-freeze-checklist.md registry/adapter-migration-matrix.md
rg -n "content/distribution/campaigns|content/storyworlds" skills/prism-goal/references/modes/loop-campaign.md
rg -n "canon gate|fast_lane_skip|generated" skills/_internal/orchestration/pipeline-contract.md

echo "check_content_schema: pass"
