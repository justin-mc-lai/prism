# Adapter contract: director

> Internal only. Not host-discoverable. Seven-segment per contracts/skill-contract-7seg.tpl.md
> Source: selfmedia-creator `selfmedia-director`（MAP-002 distill）
> Landing: skills/prism-director/references/（Prism 导演层权威；形态本体在 D2–D6）

## 1. identity
- skill_id: adapter-director
- public_or_adapter: adapter
- one_liner: Prism 导演层地基——意图第一性、treatment 模板、QC 评分卡；变体与分镜下沉到形态契约
- map_id: MAP-002 · strategy: distill

## 2. 决策边界
- 能决定：核心意图、叙事视角/语气/价值立场、情绪曲线、结构模型、钩子系统、变体拆分、QC 判定（导演侧）
- 不能决定：母稿事实/正典、成稿文字、QA 终判、公开发布
- 必须上抛：缺核心意图/受众（一次只问一个关键问题）、素材或权利约束不明、跨公开面路由、人工批准点

## 3. intake
- 必填输入：冻结母稿引用（MASTER 路径）+ 核心意图 + 目标受众 + 输出形态 + 目标平台
- 拒绝条件：无核心意图/受众却要求完整 treatment；无母稿却要求基于事实的方案；无证据却要求放行

## 4. output contract
- 人类面产出：不直接对人暴露本 adapter 名
- 机器面产出：`content/presentations/{vertical}/{slug}/{presentation_slug}/director-treatment.md` + presentation map + evidence refs
- 路径约定：成稿写入 content 层；证据写入 `.beacon/evidence/implement/prism-form-blog-thread-v1/` 等

## 5. gate
- 通过条件：treatment 验收清单全过（核心意图一句话/受众承诺具体/冲突真实/视角稳定/事实创意分离/non-goals 明确/下一门可见）
- QC 评分：55–65 生产就绪；45–54 列 top3 修复；35–44 重写；<35 停下问意图
- fail-closed：缺核心意图、无受众、无源事实主张、素材当既定事实、AI 真人形象无授权、暗示直接发布
- 证据路径：`content/presentations/.../director-treatment.md` + `.beacon/evidence/`

## 6. handoff
- 下一公开面：由 registry/public-surface.yaml + orchestration routing 决定
- 默认下一公开面：prism-produce（按 creation-mode-map 路由）
- 禁止跳过：treatment-approval（用户批准）、qa 与 human release 批准

## 7. 失败处理
- 可重试：角度/节拍/变体拆分调整、换素材假设
- 必须停并等人：核心意图/受众缺失、素材或权利约束、发布/正典/合规
- 禁止自证通过：true
