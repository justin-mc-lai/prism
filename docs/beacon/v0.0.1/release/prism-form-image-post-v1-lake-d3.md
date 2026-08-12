# Release Brief — prism-form-image-post-v1（Lake D3）

- status: **release_candidate（QA passed · 等待人工确认）**
- QA: `run-20260812T085444996257` · 10/10 AC · 15/15 TC · release_confidence 1.0
- truth: R1 frozen

## Delivered

- form-registry：image-post / xhs 注册
- `contracts/form-image-post.contract.md`：title≤20 无前缀、caption 独立、1-9 张/超9拆条、封面本地排版、OCR/QA 门、账号配置化
- `contracts/form-xhs.contract.md`：bridge xhs-article-to-images + OCR 门 + fail-closed
- creation-mode-map 路由 + `scripts/check_image_post_forms.sh` exec PASS

## Still forbidden / deferred

- D4–D6、vendor_pin、metrics、平台 API、海 closure 宣称
