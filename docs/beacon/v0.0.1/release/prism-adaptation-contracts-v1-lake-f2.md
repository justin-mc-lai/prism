# Release Brief — prism-adaptation-contracts-v1（Lake F2）

- status: **release_candidate（QA passed · 等待人工确认）**
- QA: `run-20260812T193122703453` · 10/10 AC · 15/15 TC · release_confidence 1.0
- truth: R1 frozen

## Delivered

- `contracts/adaptation.contract.md`：adaptation_id/asset_ref/rights/royalty/approval + 默认只登记不授权 + 正典保护 + license 边界 + 敏感信息保护
- `registry/adaptation-adapters.yaml`：3 个改编 bridge（rights-record / royalty-calc / license-check）
- creation-mode-map 改编引用 + `scripts/check_adaptation.sh` exec PASS

## Still forbidden / deferred

- 平台授权 API、自动授权、自动公开、海 closure 宣称（全湖交付以版本级 release 确认收口为准）
