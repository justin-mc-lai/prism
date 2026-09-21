# Mode: extract-storyworld

Extract reusable asset roster (characters / scenes / props) from a novel, script, or outline

## When to use

- User intent matches human verb **定** 的资产提取支线 / triggers: 提取人物, 提取场景, 提取道具, 资产清单,
  拆角色, 拆场景, 拆道具, 小说资产, extract assets
- 输入是小说/剧本/大纲，需要先得到可复用资产清单

## When not to use

- 冻结正典本身（用 `freeze-master`）
- 写镜头、分镜、生成媒体、QA 判定、公开发布

## Procedure

1. Restate the `master` job in one sentence; confirm this is asset extraction, not canon freeze.
2. Read MAP MAP-004 strategy in `registry/adapter-migration-matrix.md`.
3. Read `../storyworld-extraction.md`（四层区分 + 三类字段 + 提取步骤）before acting.
4. Read the source script in full for the requested scope only; do not scan unrelated private dirs.
5. Emit the roster in the three-class shape of `content/pipelines/ai-manga-drama/storyboard-schema.json`
   （`characters[]` / `scenes[]` / `props[]`）；每一实体四选一：新建 / 复用 / 变体 / 未决。
6. 含混指代标「未决」，**不猜**；未决项不得流入下游分镜。
7. Default `recommended_next_harness`: `master`（继续冻结）或 `director`（已有冻结母稿时）。
8. Emit human card + machine face; stop at harness boundary.

## Output extras

```yaml
mode_id: extract-storyworld
public_id: master
lane: standard|fast|canon
recommended_next_harness: master|director
map_ids_considered: ['MAP-004']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../storyworld-extraction.md` — 提取判断框架（四层 / 三类 / 三规范）
- `../../prism-director/references/asset-consistency-gate.md` — 提取后的跨镜一致性门（下游）
- `contracts/storyworld.schema.yaml` — 落盘形状（characters/ scenes/ props/）
- `contracts/adaptation.contract.md` — 授权边界（本 mode 不做授权判断）

## Master 侧硬门（本 mode）

1. 每个实体必须四选一落地；**含混指代不得猜**，标「未决」。
2. 只引用可见事实；知识/目标/关系/情绪不搬进资产。
3. 不新增剧本没有的实体；不做授权判断。
4. 未决项不得流入分镜或图片提示词（fail-closed）。
