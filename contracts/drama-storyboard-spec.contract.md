# Gate contract: drama-storyboard-spec（漫剧分镜脚本规范门）

> 执行契约。判断框架蒸馏见 `skills/prism-director/references/drama-storyboard-spec.md`
> （规则 ID `MJ-*`，源：神魔修仙漫剧分镜填写规范，未 vendor，见 `docs/ATTRIBUTION-drama-prompt-repos.md`）。
> 适用**分镜脚本阶段**；`spec: manju-drama` 的分镜强制过本门，未声明则跳过（向后兼容）。
> 与 `asset-consistency.contract.md` / `prompt-syntax.contract.md` **叠加**：资产门管跨镜事实，
> 语法门管提示词语法，本门管**分镜脚本填写完整性**（子镜节拍 / 在位站位 / 音效 / 台词预算）。

## 1. identity

- gate_id: drama-storyboard-spec
- 适用形态: manga_drama（神魔修仙/仙侠题材优先；`spec: manju-drama` 触发）
- 定位: **设计期硬门 + QA 复核门**——分镜不进 `prompt_compiler.py` 前必须过
- 实现: `scripts/drama_spec.py`（确定性；被 `scripts/ai_manga_drama.py validate` 调用）

## 2. 决策边界

- 能决定：子镜节拍合规、音效/台词预算、在位站位语句在场与否、景别运镜枚举、禁项命中
- 不能决定：母稿事实与正典（`prism-master`）、资产身份归类（资产一致性门）、QA 最终 verdict、公开发布

## 3. intake（director handoff 必填）

- `storyboard.json` 过 `storyboard-schema.json`（`spec` 字段为 `manju-drama` 时触发本门）
- 每个分镜 `shots[]` 声明 `beats[]`（子镜）；子镜含 `shot_size`/`camera_move`/`vfx`/`sfx`/
  `emotion`/`speech_rate`，以及 `on_screen` 与 `blocking`（在位/站位）
- 资产四视图在 `characters[].traits` 遵循 MJ-CHAR（无手持物 / 无戏剧光 / 不写瞳孔色）

拒绝：缺 `beats[]` / 子镜字段缺失 / 无 `spec: manju-drama` 却含 beats → blocked + reason_code
（`drama_spec_beats_missing` / `drama_spec_beat_fields_missing` / `drama_spec_spec_flag_missing`）。

## 4. output

- 编译产物：`分镜脚本.md`（MJ-TPL 格式，`spec: manju-drama` 时由 `prompt_compiler.py` 产出）+
  原有 `资产提示词.md` / `图片提示词.md` / `视频提示词.md` / `{episode}.srt`
- 审计记录：episode 目录 `drama-spec.json`（每分镜子镜数、Σ秒数、特写占比、音效/台词预算、命中项）
- 证据：`.beacon/evidence/qa/drama-storyboard-spec/SCORECARD.json`

## 5. gate（十一判据，任一失败 fail-closed）

1. **分镜节拍**：每个分镜子镜数 5-8（MJ-UNIT-02），每个子镜 2-5s（MJ-UNIT-03），
   `Σ 子镜时长 = shot.duration_seconds`（MJ-UNIT-01 的调和口径）
2. **特写配比**：每个分镜 `特写|大特写` 子镜数 ≥1 且占比 ≤40%（MJ-UNIT-04；源口径 20%-30%，
   小样本放宽上界，下界由「≥1」保证）
3. **子镜字段定式**：每子镜六元组齐全（`shot_size`/`camera_move`/`vfx`/`dialogue`/`sfx`/
   `description`）（MJ-FIELD-01）
4. **音效**：每子镜 `sfx` 非空、非「无」、≤10 字（MJ-FIELD-02 / MJ-SFX-01/02）
5. **台词预算**：每子镜 `dialogue` ≤30 字，超 30 字须拆（MJ-LINE-01）；字/秒落在情绪档
   （正常 5-6 / 激动 7-8 / 低沉 4-5，容差 ±1）（MJ-LINE-02/03）
6. **在位与站位**：每子镜 `on_screen ≥1` 且 `blocking` 非空（MJ-BLOCK-01..09）
7. **景别/运镜**：`shot_size` ∈ 景别枚举（MJ-CAM-01）；`camera_move` ∈ 运镜枚举（MJ-CAM-02）
8. **特效**：每子镜 `vfx` 非空（MJ-VFX-01）；命中可视觉化要求（MJ-VFX-02）
9. **场景画面**：shot 的 `scene_ref` 解析到 `scenes[]`，含 `kind`（内/外景）与 `variant`（日/夜）（MJ-TPL-02）
10. **音频要求固定行**：`分镜脚本.md` 每分镜含 `音频要求：不要背景音乐，不要字幕，不要解说声音。`（MJ-FIELD-04 / MJ-TPL-08）
11. **禁止内容**：`description`/`dialogue`/`vfx` 不命中血腥/恐怖/色情黑名单（MJ-BAN-01..03）

阈值来源标注义务：本门阈值来自**单题材（神魔修仙）+ 单模型（即梦 Seedance 2.0）**的社区实践，
**非物理常数**；换题材/换模型须重测并更新 `drama-storyboard-spec.md`，未重测即引用视为无证据。

## 6. 与其他门的关系

- `asset-consistency.contract.md`：先归类资产，再落本门子镜字段
- `prompt-syntax.contract.md`：本门管**分镜脚本填写**，语法门管**镜头提示词语法**（下游强化）
- `form-manga-drama.contract.md` / `form-av.contract.md`：本门作为分镜阶段附加判据
- `skills/prism-qa/references/anti-slop-gate.md`：管文案人味，不管分镜填写

## 7. handoff / 失败处理

- 位于 director → produce 交接（进 `prompt_compiler.py` 前）与 prism-qa 复核两处执行
- 可重试：补/并/拆子镜、修音效字数、拆长台词、补站位语句、换景别运镜
- 必须停：母稿事实冲突、命中禁项、`spec` 声明与 beats 结构不一致、任何发布动作
- 禁止自证通过: true

## 8. reason_code 全表（`scripts/drama_spec.py` 产出）

| reason_code | 触发 |
|---|---|
| `drama_spec_spec_flag_missing` | 含 `beats[]` 但未声明 `spec: manju-drama` |
| `drama_spec_beats_missing` | `spec: manju-drama` 的分镜缺 `beats[]` |
| `drama_spec_beat_fields_missing` | 子镜六元组/情绪/语速/在位/站位字段缺失 |
| `drama_spec_beat_count` | 子镜数不在 5-8 |
| `drama_spec_beat_duration` | 子镜时长不在 2-5s，或 Σ 子镜时长 ≠ shot.duration |
| `drama_spec_closeup_ratio` | 每分镜特写数 <1 或占比 >40% |
| `drama_spec_sfx_missing` | 子镜音效为空或写「无」 |
| `drama_spec_sfx_too_long` | 子镜音效 >10 字 |
| `drama_spec_line_too_long` | 子镜台词 >30 字 |
| `drama_spec_line_rate` | 字/秒偏离情绪档（正常 5-6 / 激动 7-8 / 低沉 4-5，容差 ±1） |
| `drama_spec_blocking_missing` | 在位人数缺失或 `blocking` 为空 |
| `drama_spec_camera_unknown` | 景别或运镜不在 MJ-CAM 枚举 |
| `drama_spec_vfx_missing` | 子镜特效为空 |
| `drama_spec_banned_content` | 命中 MJ-BAN 血腥/恐怖/色情黑名单 |
