# Release Brief — prism-campaign-schema-v1（Lake C）

- status: **release_candidate（QA passed · 等待人工确认）**
- QA: `run-20260811T232406916560` · 10/10 AC · 15/15 TC · release_confidence 1.0
- truth: R5 frozen（baseline `sha256:75836a098979…`）
- 人工确认: 未批准公开发布；确认后走正式 release 门

## Delivered

- `registry/content-schema.yaml`：5 类 schema 注册（master-content / storyworld / campaign / narrative-episode / distribution-binding）
- `contracts/*.schema.yaml`：5 个内容对象契约 + `master-freeze-checklist.md`（MAP-004 distilled_schema）
- `content/`：masters / storyworlds / distribution scaffold + 最小合法示例
- canon 钩子：episode `canon_gate_status` + `fast_lane_skip` illegal 声明（contracts + pipeline-contract）
- `scripts/check_content_schema.sh` exec-layer 校验 PASS
- 四件套重建并 R5 冻结；QA 证据与 acceptance-kit 落盘

## Still forbidden / deferred

- 公开发布（需人工二次批准）
- Lake D form producer chains / Lake E metrics / Lake F monetization / vendor_pin
- 宣称海 closure
