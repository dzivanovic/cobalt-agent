"""`cobalt smoke` — the sprint-close smoke checklist, in code (S2-P4 STEP-9, R6 B).

    models.py  — the suite schema (seven read-only check kinds) and outcomes
    config.py  — loads `configs/cobalt/smoke/<suite>.yaml`; errors carry a line
    checks.py  — one evaluator per kind, the run's variables, hand commands
    report.py  — the numbered verdict table and the report file
    cli.py     — `cobalt smoke <suite> --cutoff … [--prod] [--json]`

Built on day-open's pattern (plan-s2-p4 §1 F17): every check captures its
raw output, renders PASS | FAIL | KNOWN | ERROR, and the OVERALL line is
day-open's own roll-up. Read-only end to end; no writer is imported.
"""
