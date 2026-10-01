# Mode: treatment-director

Director treatment / presentation map from frozen masters

## When to use

- User intent matches human verb **导** / triggers: 导, 导演, treatment, 分镜, 节拍, prism-director

## When not to use

- 改写母稿事实、直接成片、自证 QA、跳过母稿冻结

## Procedure

1. Restate the `director` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-002 strategy in `registry/adapter-migration-matrix.md`.
3. Read `../director-philosophy.md`（意图第一性 + 叙事系统）before acting.
4. Produce treatment per `../treatment-template.md`; score per `../qc-scorecard.md`.
5. 出 shot list / 分镜前，过 `../continuity-seven-laws.md`（七律 + 片段过渡四法 + 拆分粒度）；
   冲突时按该文件 §3 择一侧（Toonflow 上限口径 / ai-comic-studio 下限口径）并在方案内声明。
6. 落剧本/分镜文本按 `../script-templates.md`（完整剧本 / 分集剧本 / 镜头清单三模板）；
   **不手写成品提示词**——提示词由 `scripts/prompt_compiler.py` 编译（`contracts/asset-render.contract.md`）。
7. 漫剧分镜默认强制 `spec: manju-drama`（2026-10-01 起删除"若声明"可选口径）：落分镜脚本按
   `../drama-storyboard-spec.md`（MJ-*）：`shots[].beats[]` 填 5-8 子镜、每子镜 2-5s、音效必填 ≤10 字、
   字数/秒匹配情绪、在位站位锁定；beats 填写弹药库见 `../beats-prompt-templates.md`
   （分镜公式 / 运镜景别词库 / 8 套光影 / 音频公式）；进编译器前过
   `contracts/drama-storyboard-spec.contract.md`（`scripts/drama_spec.py`）。
   非漫剧形态须在方案内显式声明并经人工确认，不得以"未声明 spec"绕过本门。
8. Execute only this surface; write/read evidence paths explicitly.
9. Default `recommended_next_harness`: `produce` unless blocked.
10. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: distill treatment/QC norms; defer heavy generators to Lake D
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: treatment-director
public_id: director
lane: standard|fast|canon
recommended_next_harness: produce
map_ids_considered: ['MAP-002']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../director-philosophy.md` — 顶层公理/叙事系统/自媒体适配
- `../treatment-template.md` — treatment 核心模板 + 验收清单
- `../qc-scorecard.md` — 13 维评分卡 + 生产门 + 自动阻断
- `../continuity-seven-laws.md` — 分镜连续性七律 + 片段过渡四法 + 拆分粒度（设计期规范，非 QA 门）
- `../script-templates.md` — 完整剧本 / 分集剧本 / 镜头清单三模板 + storyboard 字段映射
- `../asset-prompt-templates.md` — 资产 ref 提示词（7 段 identity block + 五类资产卡）
- `../prompt-syntax-table.md` — 镜头提示词语法（8 段 / 7 字段 / 时长 / 切镜）
- `../drama-storyboard-spec.md` — 漫剧分镜脚本规范（MJ-*：分镜 15s ⊃ 子镜 3-5s / 在位站位锁定 / 音效必填 / 字秒预算；漫剧默认声明 `spec: manju-drama`，门 `contracts/drama-storyboard-spec.contract.md`）
- `../beats-prompt-templates.md` — beats 填写提示词弹药库（分镜公式 / 运镜景别词库 / 8 套光影 / 音频公式；源自社区高手实践，见文件内 ATTRIBUTION）
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Director 侧硬门（Lake B′ 蒸馏后）

1. 无一句话核心意图 + 目标受众 → 不产出完整 treatment，一次只问一个关键问题。
2. 事实/创意解读必须分栏标注；无源主张不得进入变体。
3. 产出必带 treatment 验收清单自评 + QC 评分；<45 分不得交接 produce。
