# Gate contract: prompt-syntax（镜头级提示词语法）

> 执行契约。判断框架蒸馏见 `skills/prism-director/references/prompt-syntax-table.md`；
> 适用 comic / manga_drama / live_drama 分镜阶段、vlog / book_video 分镜阶段。
> 与 `contracts/asset-consistency.contract.md` 叠加：资产门管跨镜事实，本门管提示词语法。

## 1. identity

- gate_id: prompt-syntax
- 适用形态: manga_drama、live_drama（分集剧本+分镜）、comic（多集）、vlog / book_video（分镜阶段）
- 上游蒸馏（vendor + license 见 `docs/ATTRIBUTION-drama-prompt-repos.md`）:
  - `vendor/skills/short-drama-skills`（MIT）— 字段定式 / 时长公式 / 切镜阈值
  - `vendor/skills/onlyshot`（MIT）— 8 段定式 / ref 分层 / 失败模式
  - `vendor/skills/su-ai-short-drama`（MIT）— 景别机位选择理由
  - `vendor/skills/shuohao-skills`（Apache-2.0）— 切分与校验顺序

## 2. 决策边界

- 能决定：字段取舍、时长估算、切镜判定、提示词分层归属、阈值命中与否
- 不能决定：母稿事实与正典、资产身份/变体归类（属资产一致性门）、QA 最终 verdict、公开发布

## 3. intake（director handoff 必填）

- 已冻结母稿引用（`master_ref`）+ 已归类资产（过 `asset-consistency.contract.md`）
- shot list / storyboard：每镜含 `start_state` / `end_state` / `duration_s` / `dialogue` 字段；
  manga_drama 路由下须过 `storyboard-schema.json`

拒绝：缺母稿引用 / 资产未归类 / 分镜无 start-end 字段 → blocked + reason_code
（`prompt_syntax_master_missing` / `prompt_syntax_assets_unclassified` / `prompt_syntax_shot_fields_missing`）

## 4. output

- 提示词：`content/presentations/{vertical}/{slug}/{form}-{ep}/图片提示词.md` + `视频提示词.md`
  （manga_drama 沿用 `content/pipelines/ai-manga-drama/` 落盘约定）
- 审计记录：同目录 `prompt-syntax.json`（每镜时长估算依据 + 切镜理由 + 命中阈值 + 字符数）
- 证据：`.beacon/evidence/implement/prism-prompt-syntax-v1/AC-PS-001.json`

## 5. gate（八判据，任一失败 fail-closed）

1. **三层分离**：同一事实只在一层声明；ref 层无情绪/镜头语言/剧情词，分镜层无身份重描
2. **字段定式**：§1 必填字段齐全，顺序一致；【台词】逐字未改；【主体】无代词/「同上」
3. **时长合规**：按公式估算；冲突取大；单镜 ≤12s（动作戏 ≤15s）；静帧 ≤6s；
   长对白 >8s 已拆
4. **切镜有据**：每个切点命中必切条件（地点/时间/关系/权力/情绪/动作逆转）；
   无新信息的切镜 = 废镜，须合并
5. **空镜配比**：单 beat 内非叙事空镜 ≤20%；T1 ≤60%；T2 不连续两次
6. **动作语法**：关键动作三段式；切点落在运动轨迹中；物理反馈存在；
   关键动作独占镜头；写字受伤有伤口镜
7. **提示词卫生**：字符数 <1500（换模型须重测并记录新阈值）；视觉指纹在开头；
   敏感词四类已过；单 ref 同框（多 ref 同框即阻断）
8. **反向禁项**：§9 清单逐条排除（抽象质量词 / 字幕 / 空表情 / 拟物写人形动作）
9. **画面肯定式（AC-ITB-004）**：画面元素描述禁用否定式（形如 `no <元素>`、`不要 <元素>` 描述画面内容）；
   命中即阻断，`reason_code=image_negation_not_affirmative`。对字幕与音频的否定约束不在此列
10. **能力域前置（AC-ITB-005）**：produce 前须声明 `provider` + `model`，分镜动作与对白须落在
    `reachable` 白名单内；动作不可达 → `action_outside_model_domain`，对白不可达 → `dialogue_outside_model_domain`，
    两类均在**设计期**退回（不进生成）
11. **阈值来源（AC-ITB-007）**：`iteration_budget`、`max_downgrades`、`reachable` 白名单必须带
    `threshold_source`（来源 + 测试条件：题材 + 模型）；缺失即 `threshold_source_missing`
12. **生成预算（AC-ITB-001/002/003，见 `prism-shot-iteration-budget-v1`）**：每镜 `attempts` 不得超过
    `iteration_budget`（否则 `iteration_budget_exceeded`）；超预算须有 `convergence` 降级记录
    （`simplified` / `redesigned`）且 `downgrades` 不超过 `max_downgrades`（否则 `shot_aborted`）；
    `dialogue_source=post_dub` 即 `post_dub_fallback_forbidden`（对白失败只能改镜头设计）

阈值来源标注义务：onlyshot 的字符数与一致性百分比为单项目 N=36 实测，
引用时须带来源与测试条件；换模型未重测即引用 → 视为无证据。

## 6. 与其他门的关系

- `asset-consistency.contract.md`：先归类资产（三分法），再落本门字段；本门是下游强化
- `form-av.contract.md` §5 / `form-manga-drama.contract.md` §5：本门作为分镜阶段的附加判据
- `skills/prism-qa/references/anti-slop-gate.md`：管文案人味，不管镜头语法

## 7. handoff / 失败处理

- 位于 director → produce 交接与 prism-qa 复核两处执行；结论供 QA SCORECARD 引用
- 可重试：重排字段、重估时长、合并废镜、拆长镜、压字符数
- 必须停：母稿事实冲突、资产未归类却已出提示词、发布动作
- 禁止自证通过: true
