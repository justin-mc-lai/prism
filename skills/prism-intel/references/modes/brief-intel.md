# Mode: brief-intel

Evidence-backed topic/angle briefing via bridge + schema

## When to use

- User intent matches human verb **选** / triggers: 选, 选题, 信息差, 热点, briefing, prism-intel

## When not to use

- 全流程战役编排(用 prism-goal)、定母稿、导方案、产文、验收、发布

## Procedure

1. Restate the `intel` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-003 strategy in `registry/adapter-migration-matrix.md`.
3. Execute only this surface; write/read evidence paths explicitly.
4. Default `recommended_next_harness`: `master` unless blocked.
5. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: bridge primary to qi_dev.sh intel-radar; distill briefing schema only
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: brief-intel
public_id: intel
lane: standard|fast|canon
recommended_next_harness: master
map_ids_considered: ['MAP-003']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../briefing-schema.md` — 六段式 briefing 结构 + 不编造门 + 多源聚合顺序
- `../topic-radar.md` — 跨期选题雷达闭环（学→做→反、记忆分层、硬约束；本 mode 只做本次快照）
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## Intel 侧硬门（Lake B′ 蒸馏后）

1. 产出必须带检索时刻与可复核来源；快照类数据禁止写成恒久事实。
2. 无来源的「趋势判断」显式标注为推测；不编造趋势与指标。
3. bridge 缺失（qi_dev.sh 不可用）→ 输出 missing-evidence 标签并停止，不虚构雷达结果。

## Bridge recipe (when runtime available)

```bash
qi_dev.sh intel-radar doctor
qi_dev.sh intel-radar deep-plan "<topic>" --save
```

If bridge unavailable: stop with missing-evidence label; do not fabricate.
