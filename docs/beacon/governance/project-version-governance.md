---
schema_version: "1.0"
project_root: "/Users/apple/Developer/Personal/selfmedia/prism"
topology_kind: "single_repo"
default_execution_service: "prism"
transaction_id: "tx-project-governance-28dbca0ace9f284f"
committed_at: "2026-09-30T06:56:58.697759+00:00"
source_hash: "28dbca0ace9f284f29249fb124278cd038b7231833464f1212e855aa54e20a67"
event_type: "freeze-version-contract"
parser_contract: "beacon-project-governance-v1"
---

# Project Version Governance

- project_root: `/Users/apple/Developer/Personal/selfmedia/prism`
- topology_kind: `single_repo`
- default_execution_service: `prism`

## Service Bindings
- `prism` repo=`/Users/apple/Developer/Personal/selfmedia/prism` role=`primary` writable=`true` worktree_policy=`follow-repo-root`

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
