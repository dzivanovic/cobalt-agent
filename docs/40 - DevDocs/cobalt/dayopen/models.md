# `src/cobalt/dayopen/models.py`

`Verdict` (PASS/FAIL/ERROR) per check, `CheckResult` (id, title, verdict,
detail, raw — `raw` is always the verbatim captured output the verdict
was quoted from), `Overall` (GREEN/AMBER/RED), and `overall_verdict()` —
the one place the roll-up rule lives (L57: replayable from this function
alone, not left implicit in the renderer): ERROR outranks FAIL. RED if
any check is ERROR (a broken probe); AMBER if none are ERROR but any is
FAIL (a real finding); GREEN if every check is PASS.
