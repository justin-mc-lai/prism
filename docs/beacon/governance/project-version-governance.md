---
schema_version: "1.0"
project_root: "/Users/apple/Developer/Personal/products/prism"
topology_kind: "single_repo"
default_execution_service: "prism"
transaction_id: "tx-project-governance-18f7de4386d7d0ca"
committed_at: "2026-09-29T16:10:41.340239+00:00"
source_hash: "18f7de4386d7d0ca7fce279ab009690cb4afb23cf1b2603979f4308b2303e570"
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
