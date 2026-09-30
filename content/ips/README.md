# content/ips — IP 正典资产库

每个 IP 占一个 `{ip_id}/` 目录：

- `ip.yaml`：身份（`ip_id`/`title`/`kind`/`status`/`canon_revision`/`publish_identity_ref`）。
- `assets/{characters,scenes,props,styles}/<asset_id>/`：冻结 identity block + 引用图 + 谱系。

作品侧（`masters/`、`storyworlds/`、`distribution/campaigns/`、`episodes/`）通过
`imports[]: {from, asset, track|revision}` 引用 IP 资产；`track: latest` 为缺省，
解析时把源 `canon_revision` 落盘为 `resolved_revision`。

校验：`bash scripts/check_ip_model.sh`（违规打印 reason_code 并非零退出）。
迁移：`bash scripts/migrate_assets_to_ip.sh`（幂等，不丢资产）。

`_examples/` 为样例，不参与生产。
