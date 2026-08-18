---
name: writing-agent
description: |
  完整写作流程：选题、搜集证据、审稿与导出；去 AI 味是其中一环。
  子 skill：style-modeler、web-article-extractor、workflow-producer。
  完整 monorepo 在 vendor/writing-skills/writing-agent/。
  触发：writing-agent、完整写作流程、写作工作流。
metadata:
  upstream: https://github.com/dongbeixiaohuo/writing-agent
  vendor_path: vendor/writing-skills/writing-agent
---

# writing-agent

完整上游在 `vendor/writing-skills/writing-agent/`。

## 项目内可直接调用的子 skill

| 子目录 | 用途 |
|--------|------|
| `style-modeler/` | 风格建模 |
| `web-article-extractor/` | 网页文章提取 |
| `workflow-producer/` | 工作流生产 / 编排 |

详见上游 README：`vendor/writing-skills/writing-agent/README.md`。
