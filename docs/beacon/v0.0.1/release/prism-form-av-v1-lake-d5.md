# Release Brief — prism-form-av-v1（Lake D5）

- status: **release_candidate（QA passed · 等待人工确认）**
- QA: `run-20260812T090408217552` · 10/10 AC · 15/15 TC · release_confidence 1.0
- truth: R1 frozen

## Delivered

- form-registry：comic / vlog / book_video 注册
- `contracts/form-av.contract.md`：三形态 bridge 路由（comic-storyboard / openmontage / book-video / rnskill）、director handoff 字段、license 注记（AGPL bridge 优先）、QA 门、fail-closed
- creation-mode-map：vlog 行更新 + comic / book_video 行新增 + `scripts/check_av_forms.sh` exec PASS

## Still forbidden / deferred

- D6 publish 桥、vendor_pin 全量（license 门）、metrics、平台 API、海 closure 宣称
