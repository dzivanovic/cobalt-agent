"""`cobalt day-open` — the morning sweep, IN CODE (ruled 2026-09-14, A).

Six fixed checks (C1-C6), each capturing raw output verbatim and each
rendering PASS | FAIL | ERROR(command failed) — never a number the
report composed itself. See `runner.py` for the ordered list and
`models.overall_verdict` for how the six roll up into one GREEN / AMBER
/ RED line.

WHY IN CODE, NOT IN THE LOCAL SEAT'S PROMPT. Under the Qwen allowlist
the local seat can read and run fixed commands but never write files
(the built-in "edit" deny beats any `permissions.allow` rule), and L49
says the local seat reads and judges, never composes. So the checks run
in Cobalt's process, `cobalt day-open` writes the report itself, and the
local seat's only remaining job is to run this ONE allowed command and
add a verdict line on top of it (`cobalt day-open verdict "..."`, see
`cli.py`).
"""
