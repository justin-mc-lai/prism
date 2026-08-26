# FactMaster: watermarks-remover

> kind: fact · pipeline: oss-pick-standard · 检索时刻: 2026-08-15

## 一句话

watermarks-remover 是一个 Python 编写的开源工具（Agent skill + stdlib HTTP 服务），
用于去除文本与文件中的多厂商 AI 溯源水印——包括不可见 Unicode 字符、统计采样水印与
C2PA/EXIF 等元数据——官方定位是「对你自己拥有的内容做隐私与卫生处理」。

## 来源（source_refs）

- 仓库: `https://github.com/guillaumemeyer/watermarks-remover`（default branch: main）
- 元数据: GitHub API `repos/guillaumemeyer/watermarks-remover`（检索时刻 2026-08-15）
- README: 仓库 README.md（检索时刻 2026-08-15）

## Canonical claims（每条带来源）

| # | 事实 | 来源 |
|---|------|------|
| 1 | 定位：去除多厂商 AI 溯源标记，用于「你拥有的内容」的隐私与卫生处理（privacy and hygiene on content you own） | README 首段 |
| 2 | 三层处理：A=不可见 Unicode/异体空格/bidi/标签字符（确定性脚本）；B=统计采样文本水印（agent 改写 + 可选 rewrite_text.py）；文件层=C2PA/EXIF/XMP 等元数据 | README「Layer」表 |
| 3 | 文件格式：PNG / JPEG / WebP / SVG / PDF / DOCX / ODT / HTML / Markdown | README Layer 表 |
| 4 | 覆盖厂商/生态（类级）：Claude、Gemini/SynthID-Text、OpenAI 溯源面、open-LLM Kirchenbauer 类水印 | README 首段 |
| 5 | 核心脚本仅需 Python 3.10+ 标准库（无第三方依赖、无 Docker 必需） | README「Start the service」 |
| 6 | 仓库创建于 2026-08-11，检索时刻 8,509 stars / 876 forks / 13 open issues | GitHub API |
| 7 | 协议 MIT | GitHub API license.spdx_id |
| 8 | Agent skill 是纯文本瘦客户端（不带代码），通过 HTTP 调用服务；默认 `WATERMARKS_SERVICE_URL=http://127.0.0.1:8765` | README「Install (agent skill)」 |
| 9 | 文本工具拒绝二进制输入（魔数 + 控制字节比检测；`--force-text` 可覆盖），防止把压缩字节当文本改写 | README「Text tools refuse binary input」 |
| 10 | HTTP 服务默认只绑 loopback；可用 `WATERMARKS_SERVER_API_KEY` 要求 Bearer 鉴权 | README「HTTP service」 |
| 11 | Layer B 改写钩子默认 `print-prompt`（无模型也可用）；可选 Ollama（默认仅 loopback）或 openai-compatible；远程端点需 `WATERMARKS_REWRITE_ALLOW_REMOTE=1`；API key 只从环境变量读取，绝不出现在命令行参数 | README env 表 |
| 12 | 两个 harness 镜像（CtrlRegen 像素去除、reverse-SynthID scorer）**从不发布**：前者上游 noai-watermark 无 LICENSE，后者为非商业 Research License | README「Docker / compose」 |
| 13 | markllm / markdiffusion harness 镜像已发布（上游 Apache-2.0） | README「Docker / compose」 |
| 14 | 最新 release v0.5.0 | README 首段 |
| 15 | 可选系统工具：c2patool（检查 C2PA）、exiftool（残留元数据，PDF 尤其）、qpdf（结构重建，真实 PDF 清理必需） | README「Optional system tools」 |

## 不确定性标注

- star/forks 为检索时刻快照（2026-08-15），会随时间变化。
- Layer B 统计水印的去除依赖模型改写，效果因文本与模型而异；README 未承诺检测率。
- 本仓库不提供「检测率/清除率」基准数据（README 未见独立基准）。

## 禁止改写

- 不得把「对你自己拥有的内容」边界写成「教人伪装 AI 内容/规避平台检测」。
- 不得声称可清除所有厂商水印或承诺通过任何检测。
- 不得把「从不发布的 harness」写成已发布能力。
