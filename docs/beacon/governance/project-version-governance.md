---
schema_version: "1.0"
project_root: "/Users/apple/Developer/Personal/products/prism"
topology_kind: "single_repo"
default_execution_service: "prism"
transaction_id: "tx-project-governance-b0f240c7b98d5085"
committed_at: "2026-08-12T00:52:44.040895+00:00"
source_hash: "b0f240c7b98d5085e165a8dafe050382c78087936d4d06843cd725d06cfe9820"
event_type: "freeze-version-contract"
parser_contract: "beacon-project-governance-v1"
---

# Project Version Governance

- project_root: `/Users/apple/Developer/Personal/products/prism`
- topology_kind: `single_repo`
- default_execution_service: `prism`

## Service Bindings
- `prism` repo=`/Users/apple/Developer/Personal/products/prism` role=`primary` writable=`true` worktree_policy=`follow-repo-root`

## Version Contracts

### v0.0.1
- participating_services: `prism`
- branch_guard_mode: `strict`
- validation_state: `active`
- per_service_canonical_branch:
  - `prism`: `beacon/v0.0.1`
- truth_canonical: `main`
- branch_governance_template: `standard-feature`
- previous_version_baseline_branch: `main`
- next_version_feature_branch: `beacon/v0.0.1/<feature-slug>`
- worktree_mode: `dedicated`
- worktree_path: `.beacon/worktrees/v0.0.1`
- require_workspace_admission: `true`
- merge_direction_policy: `master->beacon/v0.0.1`
- merge_direction_policy: `beacon/v0.0.1->uat`
- forbidden_directions: `uat->beacon/v0.0.1`
- forbidden_directions: `uat_as_feature_base`
