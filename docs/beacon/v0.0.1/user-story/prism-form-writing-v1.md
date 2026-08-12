---
slug: prism-form-writing-v1
version: v0.0.1
status: frozen
revision_id: R1
language: zh
canonical_ref: docs/beacon/v0.0.1/features/prism-form-writing-v1/truth.md
---

# User Stories — prism-form-writing-v1（Lake D1）

## US-WRITE-001 成稿链

prism-produce 拿到冻结母稿 → 按 `contracts/writing.contract.md` 选型（四段式 / 日榜倒金字塔 /
emotional-essay）成稿 → 人味层（bridge：selfmedia-humanize / humanizer-zh 等）→ prism-qa 按
`anti-slop-gate.md` 逐条核验并引用原文证据行 → release。

## US-WRITE-002 新增人味工具

只改 `registry/writing-adapters.yaml` 登记 bridge 命令；不改写作规则与主链。

## US-WRITE-003 bridge 缺失

工具缺失时明确 blocked + reason_code，不假装产出；由人决定安装或换桥。
