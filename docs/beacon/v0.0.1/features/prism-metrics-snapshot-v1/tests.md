---
slug: prism-metrics-snapshot-v1
version: v0.0.1
revision_id: R1
materials_status: current
package_shape: v1.6.10
---

# Tests: prism-metrics-snapshot-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-MSNAP-001 | AC-MSNAP-001 | `test -f contracts/metrics-snapshot.contract.md && rg -n "snapshot_id|publication_ref|collected_at|来源" contracts/metrics-snapshot.contract.md` | 快照契约含核心字段 |
| TC-MSNAP-002 | AC-MSNAP-002 | `test -f registry/metrics-adapters.yaml && rg -n "snapshot" registry/metrics-adapters.yaml` | 快照 bridge 条目存在 |
| TC-MSNAP-003 | AC-MSNAP-003 | `rg -n "publication_ref|无 publication|measured" contracts/metrics-snapshot.contract.md` | measured 守卫 |
| TC-MSNAP-004 | AC-MSNAP-004 | `rg -n "metrics-snapshot.contract" skills/_internal/orchestration/creation-mode-map.md` | 路由快照引用 |
| TC-MSNAP-005 | AC-MSNAP-005 | `test -x scripts/check_metrics_snapshot.sh` | exec 脚本存在且可执行 |
| TC-MSNAP-006 | AC-MSNAP-005 | `bash scripts/check_metrics_snapshot.sh` | exec-layer 校验脚本 PASS（合法路径） |
| TC-MSNAP-007 | AC-MSNAP-002 | `python3 -c "import yaml,sys; d=yaml.safe_load(open('registry/metrics-adapters.yaml')); rs=[a for a in d.get('adapters',[]) if 'snapshot' in a.get('name','')]; raise SystemExit(0 if len(rs)>=2 else 1)"` | ≥2 个快照采集条目 |
| TC-MSNAP-008 | AC-MSNAP-006 | `rg -n "空快照|禁止|不编造|猜" contracts/metrics-snapshot.contract.md` | 空快照/不编造声明 |
| TC-MSNAP-009 | AC-MSNAP-007 | `rg -n "凭证|密钥|secrets|禁止入库" contracts/metrics-snapshot.contract.md` | 凭证保护 |
| TC-MSNAP-010 | AC-MSNAP-008 | `rg -n "fail-closed|blocked|reason_code" contracts/metrics-snapshot.contract.md` | bridge fail-closed |
| TC-MSNAP-011 | AC-MSNAP-009 | `rg -n "collected_at|来源|缺证据" contracts/metrics-snapshot.contract.md` | 证据要求 |
| TC-MSNAP-012 | AC-MSNAP-010 | `rg -n "Non-goals" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md && rg -n "E3|E4" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md && rg -n "海 closure" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md` | 分湖边界存在 |
| TC-MSNAP-013 | AC-MSNAP-010 | `rg -n "Illegal|illegal|宣称海" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md` | illegal 转移覆盖（非法拒绝路径） |
| TC-MSNAP-014 | AC-MSNAP-001 | `rg -n "US-MSNAP-001|快照" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md` | 快照旅程可追溯 |
| TC-MSNAP-015 | AC-MSNAP-006 | `rg -n "US-MSNAP-002|空快照" docs/beacon/v0.0.1/features/prism-metrics-snapshot-v1/truth.md` | 空快照路径可追溯 |
