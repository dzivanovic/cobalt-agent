# `src/cobalt/smoke/__init__.py`

The `cobalt smoke` package: the sprint-close smoke checklist in code (S2-P4
STEP-9, plan ruling R6 B). The docstring is the module map:

| File | Role |
|---|---|
| `models.py` | the suite schema (seven read-only check kinds), `SmokeContext`, `CheckOutcome`, `SmokeReport` |
| `config.py` | loads `configs/cobalt/smoke/<suite>.yaml`; every error carries a line number |
| `checks.py` | one evaluator per kind, the run's variables, the hand command per check |
| `report.py` | the numbered verdict table and the `reports/<suite>-smoke-<date>.md` file |
| `cli.py` | `cobalt smoke <suite> --cutoff … [--date] [--prod] [--json]` |

It follows the day-open pattern (plan §1 F17): each check captures its raw
output and renders PASS | FAIL | KNOWN | ERROR, and OVERALL comes from
day-open's own roll-up (`dayopen.models.overall_verdict`), not from a second
copy (L3).

It is read-only end to end, and no writer is imported. The sentinel test
`test_smoke_imports_no_writer_and_calls_no_write` holds this in two ways:
- **Static:** no writer module or writer name appears in this package's source.
- **Runtime:** every write surface is armed to raise while the committed suite runs.
