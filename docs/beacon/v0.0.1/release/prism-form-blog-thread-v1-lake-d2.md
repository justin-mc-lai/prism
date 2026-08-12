# Release Brief — prism-form-blog-thread-v1（Lake D2）

- status: **release_candidate（QA passed · 等待人工确认）**
- QA: `run-20260812T084947791269` · 10/10 AC · 15/15 TC · release_confidence 1.0
- truth: R1 frozen

## Delivered

- `registry/form-registry.yaml`：blog / thread 形态注册（contract + lane + 生产链 + 门禁）
- `contracts/form-blog.contract.md`：四段式深度长文生产者契约
- `contracts/form-thread.contract.md`：倒金字塔 thread 契约（快道/标准道；canon 禁用快道）
- creation-mode-map 路由引用 + `scripts/check_blog_thread_forms.sh` exec PASS

## Still forbidden / deferred

- D3–D6 形态、vendor_pin、metrics、平台 API、海 closure 宣称
