# Tests: prism-title-lab-v1

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-001 | AC-001 | `test -f skills/prism-produce/references/title-lab.md && rg -q '路径 A|路径 B|同义改写|首选' skills/prism-produce/references/title-lab.md` | exit 0 |
| TC-002 | AC-002 | `rg -q '选题角度.*标题公式建议|标题公式建议' skills/prism-intel/references/briefing-schema.md` | exit 0 |
| TC-003 | AC-003 | `rg -q '标题门' skills/prism-qa/references/anti-slop-gate.md && rg -q '标题门' skills/_internal/orchestration/quality-gates.md && rg -q '同义改写|18–32|前 16 字' skills/prism-qa/references/anti-slop-gate.md` | exit 0 |
| TC-004 | AC-004 | `test -f docs/ATTRIBUTION-corpora.md && rg -q 'MIT|BigPengSays' docs/ATTRIBUTION-corpora.md && test -f skills/prism-produce/references/title-corpus.md && rg -q '来源|检索' skills/prism-produce/references/title-corpus.md` | exit 0 |
| TC-005 | AC-005 | `rg -q 'title_formula|is_preferred' contracts/metrics-publication.contract.md && rg -q '4 周|基线' contracts/review-loop.contract.md && rg -q '人工' contracts/review-loop.contract.md` | exit 0 |
| TC-006 | AC-003 | `rg -q 'Illegal transitions|illegal' docs/beacon/v0.0.1/features/prism-title-lab-v1/truth.md && rg -q '跳过标题门|未人工批准' docs/beacon/v0.0.1/features/prism-title-lab-v1/truth.md` | exit 0（非法转移覆盖） |
| TC-EXEC-001 | AC-001 | `python3 -c "from pathlib import Path; t=Path('skills/prism-produce/references/title-lab.md').read_text(encoding='utf-8'); assert '首选' in t and '公式' in t and '兑现' in t; print('ok')"` | exit 0 且 stdout 含 ok |
