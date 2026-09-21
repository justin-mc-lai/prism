# Mode: draft-release

Draft handoff and human-gated publish/schedule

## When to use

- User intent matches human verb **发** / triggers: 发, 草稿, 发布, 定时, release, prism-release

## When not to use

- 无 QA 放行、静默公开发布、跳过人工批准、改母稿

## Procedure

1. Restate the `release` job in one sentence; confirm lake scope (B/B′ vs deferred C–F).
2. Read MAP MAP-008 strategy in `registry/adapter-migration-matrix.md`.
3. **AV / manga 形态：交接核验三判据**（任一不过即阻断，见下方 §AV/manga 交接门）：
   - `video-manifest.json` 的 `release_gate == pending_human`（AV 终态；仓库内无自动发布路径）
   - 成片带 **AI 提示标识**（总局令第 16 号义务）；无标识即 `release_ai_label_missing`
   - 无任何自动公开发布路径；公开发布须人工二次批准并留痕
4. Execute only this surface; write/read evidence paths explicitly.
5. Default `recommended_next_harness`: `stop` unless blocked.
6. Emit human card + machine face; stop at harness boundary.

## Adapter policy

- Strategy: bridge draft tools; defer vendor sync-ai pin; human approval always
- Prefer bridge/distill; vendor_pin only Lake D+ with ATTRIBUTION.
- Human face: public verbs only. Machine face: optional `map_id`.

## Output extras

```yaml
mode_id: draft-release
public_id: release
lane: standard|fast|canon
recommended_next_harness: stop
map_ids_considered: ['MAP-008']
```

## Nested refs (load on demand)

- `../human-card-handoff.md`
- `../adapter-migration-pointer.md`
- `../../../../contracts/asset-render.contract.md` — 渲染交接门（§6 AI 标识强制 / §7 `pending_human` handoff）
- `../../../../registry/render-adapters.yaml` — provider 槽位与凭证变量名（无兜底反断言）
- Kernel under `skills/_internal/orchestration/` when routing conflicts

## AV/manga 交接门

AV / manga 形态的成片**终态是 `release_gate: pending_human`**，本面只做草稿交接，不发布。

| # | 判据 | 不过时 |
|---|---|---|
| 1 | `video-manifest.json.release_gate == pending_human` | 阻断（状态异常，交人工） |
| 2 | 成片带 AI 提示标识（总局令第 16 号） | `release_ai_label_missing` |
| 3 | 无自动公开发布路径；公开须人工二次批准留痕 | 拒绝静默发布 |

依据 `contracts/asset-render.contract.md` §6/§7；本面**不**判定 QA，也**不**改契约语义。

## Human approval gate

- `draft` actions may proceed with recorded intent.
- `publish` / `schedule` require explicit human confirmation in the card decision section.
- Read `skills/_internal/orchestration/publish-approval.md` before any public action.
- AV / manga：`pending_human` 为终态；仓库内**不存在**自动公开发布命令。
