## §0 Headline
Card 731 amended in place to clear preflight r3's FAIL 21: K6 and DECISION 3 now say `0026` (`0025_dml_roles` is on main).
K6's RED is `FORWARD[-1].name == "0025_dml_roles.sql"`; its head-pin grep is `grep -rn "0025" tests`.
Also cleared: the `## RECORDS` BASE/F4 note and the unused `ASK DESK` definition. BASE, TIP, CHECK REPORT untouched. Nothing committed.

## DECISIONS
None open. No `ASK DESK`.

## RECORDS
- Proven by content at HEAD `f36676c0`: `db_migrations/__init__.py` lines 174-175 `FORWARD` ends `0024_strike_alerts.sql`, `0025_dml_roles.sql`; lines 180-181 `REVERSE` starts `0025_dml_roles.rollback.sql`; `ls db_migrations` shows no `0026`; `tests/cobalt/test_f15_p1_records_offline.py:28` asserts `FORWARD[-1].name == "0025_dml_roles.sql"`. `git grep` at `40e646ed` shows the same `0025_dml_roles` lines.
- F4 on main at `40e646ed`: `daily.py:856` `ensure_daily_note`, `:705` `format_stamp`, `prefill.yaml:24` `daily_refresh:`, `jobs.yaml:214` `label: com.cobalt.prefill-refresh`.
- Edits to the card: K6 (`0026`, RED, grep `0025`); DECISION 3; line 83 (ASK DESK definition removed, no decision uses it); `## RECORDS` BASE line, F4 line, anchors line (`FORWARD` ends `0025`), migration-number line.
- Drafted 2026-10-19 06:17 EDT (`date`).

DRAFTED · decisions: 0
