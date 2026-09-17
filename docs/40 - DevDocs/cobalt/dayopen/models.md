# `src/cobalt/dayopen/models.py`

`Verdict` (PASS/FAIL/ERROR) per check, `CheckResult` (id, title, verdict,
detail, raw — `raw` is always the verbatim captured output the verdict
was quoted from), `Overall` (GREEN/AMBER/RED), and `overall_verdict()` —
the one place the roll-up rule lives (L57: replayable from this function
alone, not left implicit in the renderer): ERROR outranks FAIL. RED if
any check is ERROR (a broken probe); AMBER if none are ERROR but any is
FAIL (a real finding); GREEN if every check is PASS.

---

## 2026-09-17 — S2-P4: `KNOWN`, shared with `cobalt smoke`

- `Verdict.KNOWN` is new: a named, ruled condition (e.g. "no fill yet") that is reported, never a failure. Day-open's six checks do not emit it. `cobalt smoke` (S2-P4 STEP-9) does, and it uses this roll-up instead of owning a second one (L3).
- `overall_verdict(results)` accepts any sequence of objects with a `.verdict` (the `HasVerdict` protocol). The rule is RED if any check is ERROR, AMBER if any is FAIL, and GREEN otherwise; KNOWN never lowers it (plan-s2-p4 §1 F17).
- **An empty list now raises `ValueError`**: a sweep that checked nothing is not GREEN (L1). Day-open always passes six results, so its behaviour is unchanged.
