# content/crossovers — 联名授权记录

一个作品若 `imports[]` 引用 ≥2 个 IP，即为**联名**，必须在此登记授权记录：
`content/crossovers/{crossover_id}.yaml`。字段与门见 `contracts/crossover.schema.yaml`。

校验：`bash scripts/check_ip_import_gate.sh`（违规打印 reason_code 并非零退出）。
`_examples/` 为样例，不参与生产。
