---
slug: prism-title-lab-v1
version: v0.0.1
revision_id: R1
---

# Evidence — prism-title-lab-v1

| surface | authority | path |
|---------|-----------|------|
| package | requirement_truth | docs/beacon/v0.0.1/features/prism-title-lab-v1/truth.md |
| tests | test_truth | docs/beacon/v0.0.1/features/prism-title-lab-v1/tests.md |
| tasks | acceptance_truth | docs/beacon/v0.0.1/features/prism-title-lab-v1/tasks.md |
| source_corpus | support_advisory | https://github.com/BigPengSays/bigpeng-hot-gzh (MIT, verified 2026-08-18) |
| title_lab | support_advisory | skills/prism-produce/references/title-lab.md |
| title_corpus | support_advisory | skills/prism-produce/references/title-corpus.md |
| briefing_schema | support_advisory | skills/prism-intel/references/briefing-schema.md |
| title_gate | support_advisory | skills/prism-qa/references/anti-slop-gate.md |
| orchestration_gates | support_advisory | skills/_internal/orchestration/quality-gates.md |
| metrics_publication | support_advisory | contracts/metrics-publication.contract.md |
| review_loop | support_advisory | contracts/review-loop.contract.md |

实现后：`.beacon/evidence/implement/prism-title-lab-v1/AC-{001..005}.json` 每条包含
`ac_id`、`assertion`、`command`、`exit_code`、`stdout_tail`、`collected_at`、`artifact_refs`；
QA 只读 evidence，maker 不自证。
