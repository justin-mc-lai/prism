# Architecture Blueprint

- status: draft
- project_mode: greenfield

## Scope
- system positioning
- module/service map
- data flow
- boundaries

<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-extract-v1:START -->
## Technical Delta Blueprint

- project_mode: `greenfield`
- feature: `prism-extract-v1`
- version: `v0.0.1`

### Source Refs
- prd: `docs/beacon/v0.0.1/prd/prism-extract-v1.md`
- user_story: `docs/beacon/v0.0.1/user-story/prism-extract-v1.md`
- test_case: `docs/beacon/v0.0.1/qa/test-cases/prism-extract-v1.md`

### Delivery Change Surface
- none
### Available Entry Surfaces
- none
### Current Service Facts
- none

### Must Change
- none

### Can Reuse
- none

### No-Expand Guardrails
- none

### Compatibility Rules
- none

### Delivery Constraints
- none

### Implement Handoff
- none
<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-extract-v1:END -->

<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-extract-v1:START -->
## Implementation Delivery Baseline

- baseline_id: `impl-delivery-baseline-v0.0.1-prism-extract-v1-R1`
- transaction_id: `tx-068582666a201875e`
- source_hash: `sha256:c61d7315393905a35b5df35cffba86a06515bebd8ba8521f4dd73731c51b3b1a`
- projection_seq: `1`
- version: `v0.0.1`
- feature: `prism-extract-v1`
- lifecycle_role: `pre-implement delivery blueprint projection`
- projection_refresh_trigger: `implement plan against the active frozen revision`
- branch_strategy: `single-branch`
- base_branch: `main`
- default_target_branch: `beacon/v0.0.1/prism-extract-v1`
- branch_prefix: `beacon/`
- use_git_worktree: `False`
- worktree_root: `/Users/apple/Developer/Personal/products/prism/prism-extract-v1`
- workspace_root: `/Users/apple/Developer/Personal/products/prism/prism-extract-v1`

### Delivery Service Scope
- direct_delivery_services: .
- writable_services: .
- reference_only_services: docs
- depends_on_features: -

### Plan-Time Gate Contract
- canonical envelope is the only delivery baseline source.
- deterministic implementation contract, git workflow contract, and implementation plan are projections.
- gates must block if projection metadata or service/branch/worktree fields drift.
<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-extract-v1:END -->

<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-campaign-schema-v1:START -->
## Technical Delta Blueprint

- project_mode: `greenfield`
- feature: `prism-campaign-schema-v1`
- version: `v0.0.1`

### Source Refs
- prd: `docs/beacon/v0.0.1/prd/prism-campaign-schema-v1.md`
- user_story: `docs/beacon/v0.0.1/user-story/prism-campaign-schema-v1.md`
- test_case: `docs/beacon/v0.0.1/qa/test-cases/prism-campaign-schema-v1.md`

### Delivery Change Surface
- none
### Available Entry Surfaces
- none
### Current Service Facts
- none

### Must Change
- none

### Can Reuse
- none

### No-Expand Guardrails
- none

### Compatibility Rules
- none

### Delivery Constraints
- none

### Implement Handoff
- none
<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-campaign-schema-v1:END -->

<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-campaign-schema-v1:START -->
## Implementation Delivery Baseline

- baseline_id: `impl-delivery-baseline-v0.0.1-prism-campaign-schema-v1-R5`
- transaction_id: `tx-20dcb24ead65e579c`
- source_hash: `sha256:8ed6568b270b7c6be9a4215a09f85e52e9ca4ef61a02bb570cd91a4860d70195`
- projection_seq: `1`
- version: `v0.0.1`
- feature: `prism-campaign-schema-v1`
- lifecycle_role: `pre-implement delivery blueprint projection`
- projection_refresh_trigger: `implement plan against the active frozen revision`
- branch_strategy: `single-branch`
- base_branch: `main`
- default_target_branch: `beacon/v0.0.1/prism-campaign-schema-v1`
- branch_prefix: `beacon/`
- use_git_worktree: `False`
- worktree_root: `/Users/apple/Developer/Personal/products/prism`
- workspace_root: `/Users/apple/Developer/Personal/products/prism`

### Delivery Service Scope
- direct_delivery_services: .
- writable_services: .
- reference_only_services: docs
- depends_on_features: -

### Plan-Time Gate Contract
- canonical envelope is the only delivery baseline source.
- deterministic implementation contract, git workflow contract, and implementation plan are projections.
- gates must block if projection metadata or service/branch/worktree fields drift.
<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-campaign-schema-v1:END -->

<!-- BEACON:IMPLEMENTATION-DELIVERY-HOST:START -->
## Implementation Delivery Host

- version: `v0.0.1`
- feature_count: `3`
- transaction_id: `tx-5644c21cf8386d015`
- source_hash: `sha256:a8d47f55772585c6d4b0e9a5ff440be0bd95f1c530bd7aeb522ddbb5565a75ff`

### Registered Feature Baselines
- `prism-campaign-schema-v1` | revision=`R5` | branch=`beacon/v0.0.1/prism-campaign-schema-v1` | writable_services=. | depends_on=- | baseline_ref=`docs/beacon/v0.0.1/.machine/execution/implementation-delivery-baseline-prism-campaign-schema-v1.json`
- `prism-extract-v1` | revision=`R1` | branch=`beacon/v0.0.1/prism-extract-v1` | writable_services=. | depends_on=- | baseline_ref=`docs/beacon/v0.0.1/.machine/execution/implementation-delivery-baseline-prism-extract-v1.json`
- `prism-form-writing-v1` | revision=`R1` | branch=`beacon/v0.0.1/prism-form-writing-v1` | writable_services=. | depends_on=- | baseline_ref=`docs/beacon/v0.0.1/.machine/execution/implementation-delivery-baseline-prism-form-writing-v1.json`
<!-- BEACON:IMPLEMENTATION-DELIVERY-HOST:END -->

<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-form-writing-v1:START -->
## Technical Delta Blueprint

- project_mode: `greenfield`
- feature: `prism-form-writing-v1`
- version: `v0.0.1`

### Source Refs
- prd: `docs/beacon/v0.0.1/prd/prism-form-writing-v1.md`
- user_story: `docs/beacon/v0.0.1/user-story/prism-form-writing-v1.md`
- test_case: `docs/beacon/v0.0.1/qa/test-cases/prism-form-writing-v1.md`

### Delivery Change Surface
- none
### Available Entry Surfaces
- none
### Current Service Facts
- none

### Must Change
- none

### Can Reuse
- none

### No-Expand Guardrails
- none

### Compatibility Rules
- none

### Delivery Constraints
- none

### Implement Handoff
- none
<!-- BEACON:TECHNICAL-DELTA-BLUEPRINT:prism-form-writing-v1:END -->

<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-form-writing-v1:START -->
## Implementation Delivery Baseline

- baseline_id: `impl-delivery-baseline-v0.0.1-prism-form-writing-v1-R1`
- transaction_id: `tx-cfa8da4e0b1948f68`
- source_hash: `sha256:84d6214367545125a3fcc073cafaf4d47abc324ca50e4cff04a31a882aa6f9f6`
- projection_seq: `1`
- version: `v0.0.1`
- feature: `prism-form-writing-v1`
- lifecycle_role: `pre-implement delivery blueprint projection`
- projection_refresh_trigger: `implement plan against the active frozen revision`
- branch_strategy: `single-branch`
- base_branch: `main`
- default_target_branch: `beacon/v0.0.1/prism-form-writing-v1`
- branch_prefix: `beacon/`
- use_git_worktree: `False`
- worktree_root: `/Users/apple/Developer/Personal/products/prism`
- workspace_root: `/Users/apple/Developer/Personal/products/prism`

### Delivery Service Scope
- direct_delivery_services: .
- writable_services: .
- reference_only_services: docs
- depends_on_features: -

### Plan-Time Gate Contract
- canonical envelope is the only delivery baseline source.
- deterministic implementation contract, git workflow contract, and implementation plan are projections.
- gates must block if projection metadata or service/branch/worktree fields drift.
<!-- BEACON:IMPLEMENTATION-DELIVERY-BASELINE:prism-form-writing-v1:END -->
