---
schema_version: "1.0"
project_root: "/Users/apple/Developer/Personal/products/prism"
topology_kind: "single_repo"
default_execution_service: "prism"
transaction_id: "tx-project-governance-558d39cd0dead5ff"
committed_at: "2026-08-11T03:30:35.682583+00:00"
source_hash: "558d39cd0dead5ff81daa0b0ad78e5bd7948a94f0ef892cb2d6dd22c5af20e08"
event_type: "update"
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
  - `prism`: `beacon/v0.0.1/prism-extract-v1`
- truth_canonical: `main`
- worktree_mode: `branch-only`
- worktree_path: `/Users/apple/Developer/Personal/products/prism/prism-extract-v1`
