# v0.0.1 内容源架构索引（Prism）

## Canonical 面（Lake C 已落 content schema）

- `content/masters/{vertical}/{slug}/`：母稿（FactMaster / StoryMaster）
- `content/presentations/{vertical}/{slug}/{presentation_slug}/`：展示变体
- `content/distribution/`：campaign / binding / job
- `content/publications/`：发布记录
- `content/storyworlds/`：故事世界 bible / canon ledger（Lake C）

### Lake C 新增约束

- `registry/content-schema.yaml`：master / storyworld / campaign / episode / binding 契约索引
- `contracts/*.schema.yaml`：内容对象 schema 契约
- `scripts/check_content_schema.sh`：内容 schema 本地校验入口

## 本版已落地

- `skills/prism-*/`：7 公开面 production-sample
- `skills/_internal/orchestration/`：编排内核
- `skills/_internal/adapters/`：adapter 契约 stub
- `registry/public-surface.yaml` / `registry/adapter-index.yaml` / `registry/adapter-migration-matrix.md`
- `docs/beacon/v0.0.1/features/prism-extract-v1/`：Lake B feature package（frozen R1）

## 投影面

- `docs/beacon/v0.0.1/.machine/`：CLI 生成机器投影
- `.beacon/evidence/`：实现/QA/release 证据

## 双母稿（规范继承）

- FactMaster：source_refs + canonical_claims + 来源证据
- StoryMaster：story bible + canon ledger + 角色/时间线/episode
