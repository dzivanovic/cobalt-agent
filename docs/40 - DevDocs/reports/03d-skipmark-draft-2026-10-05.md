## §0 Headline
- Row P7 added to card `03d`: one `skipif` mark on `test_without_the_flag_validate_still_reads_the_db`, file `tests/cobalt/test_validate_no_db.py` only.
- Mark: `@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")` (`test_drc_d4_fix_r1_runs.py:59`, `test_voice_plan.py:102`); the file also needs `import os`.
- Round line added to `## RECORDS`. `TIP` / `CHECK REPORT` untouched (`CARD.md` gives them to the desk). One decision: the test may fail with the DB env present.

## CARD
- Row `P7` after P6 in `prompts/2026-10-03/03d-adoption-port-card.md`: files `tests/cobalt/test_validate_no_db.py`; proof offline `1 skipped` plus the other four passing, with the DB env present not skipped, then the deploy gate, no re-check (R376).
- `## RECORDS`: `ROUND 2026-10-05 (2): P7 is 03d's second small finding, from deploy-03d-1005 FAILED G (c)`

## DECISIONS
- ASK DESK: with the DB env present, the autouse `dev_db_tx` (conftest) likely sets up before the file's `_no_db_settings` deletes `POSTGRES_HOST`, so `db.connect` is the faked one and opens the dev DB. Then `_cmd_validate(no_db=False)` may NOT raise `DbConfigError` and the test fails there. Not run here (no tests allowed). [before the build launches] Default: P7 stands as written; the builder reports the with-DB run as it comes out; no fix beyond the mark unless the desk rules one.

## RECORDS
- Read: the card (P5, P6, `## RECORDS`), `CARD.md` field table (`TIP` `:18`, `CHECK REPORT` `:20`), `conftest.py` at `53b56384` (`offline_skip_marks` is any `skipif`), the failed report `:99-106`, `test_validate_no_db.py` at `53b56384` (imports `argparse`, `sys`, `pytest`; no `os`).
- Decorator line numbers are from the working tree on `main`, not `53b56384`.
- Touched: the card only, plus this report. No Bash write, no test run.

03D ROW P7 DRAFTED · decisions: 1
