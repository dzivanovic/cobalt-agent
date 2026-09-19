You are an independent reviewer from another house, reading the WHOLE updated build of branch
`archiver/append-0919` for the first time (you did not read round 1). You cannot run commands —
everything you need is already here as files. `spec-final-design.md` (or the excerpt you were given,
if your read was split by area) is the tribunal-derived FINAL design this build implements.
`verdicts-r1.md` is round 1's verdict table, so you know what was ALREADY found and fixed — read it for
context, but verify the CURRENT code yourself; do not assume a round-1 "REAL" finding is still present,
and do not assume a round-1 fix is correct just because `facts.md` or `build-report.md` say so (both are
claims, not settled fact — L35). The `build-*.diff` file(s) you were given are pieces of the WHOLE
non-docs three-dot diff `main...archiver/append-0919 -- src tests configs`; if you were given only one
area's file, answer only the questions your files can answer and write "N/A THIS CALL" for the rest —
another call covers the others, and the hub will merge every call's answers into one verdict.

This code has not merged, does not run against production today, and its `requires_db` tests (23 of
them, all written offline) have NEVER run. It deploys in `upsert` mode only (today's behaviour,
unchanged except for one new advisory lock and a read-only shadow compare) for N shadow nights before
anyone considers switching it to `append`, against a live production Postgres 16 database with an
8.4M-row `bars` table.

For every finding give SEVERITY (BLOCKER = the code does not do what the design required, breaks an
existing invariant, or contradicts a LAW (L1 fail-loud, L3 one-path, L10 config-validated-on-load, L45
real-shape fixtures, L52 nothing here may touch scoring/ranking/cards, L57 replayable/reconciling
values) / MAJOR / MINOR), FILE + LINE (from the diff you were given), the EVIDENCE you read (quote it),
and the FAILING SCENARIO; say "none found" rather than inventing.

GENERAL (answer from whichever files you have):
(Q1) Does anything in your file(s) touch `src/cobalt/radar/`, `configs/` (beyond the one
`tunables.yaml` block, if your bucket includes it), or `ops/`? Does anything reach scoring, ranking, or
a value that lands on a trading card (L52)? Any secret, credential, path, or connection string visible?

BUCKET A (settings, heartbeat, store/incidents/progress) — if you have `build-A-settings-heartbeat-store.diff`:
(Q2) Do the seven `archiver.*` config keys resolve from ONE Pydantic model, with `write_mode` validated
to EXACTLY `upsert`/`append` (no `.strip()`/`.lower()` normalisation) and the shipped value `upsert`?
(Q3) F1 (round 1's blocker): does `store.py` now have a connection-taking `upsert_bars_on(conn, bars)`
sibling to the connection-opening `upsert_bars`, with only ONE copy of the `ON CONFLICT … DO UPDATE`
SQL text (L3)? Does `insert_new_bars` take `conn` first and never open/commit its own connection?
(Q4) Does the heartbeat's `archiver_freshness` probe stay red (never green) while any
`archive_incidents` row is unresolved, and does an unreadable incidents table degrade LOUDLY (naming the
migration) rather than crashing the heartbeat run or silently reporting green?

BUCKET B (migrations, reconcile) — if you have `build-B-migrations-reconcile.diff`:
(Q5) Do the migration registry's `FORWARD`/`REVERSE` tuples end/begin with `0010`/`0011` in the position
the design requires? Does the `archive_incidents` CHECK constraint enumerate EXACTLY
`gap, restated, stored_only, empty_export, regression` (five, no more, no fewer), and does the partial
unique index carry `NULLS NOT DISTINCT WHERE resolved_at IS NULL` (F7)? Are both migrations purely
additive (no ALTER/index/trigger touching `system.bars`)?
(Q6) In `reconcile.py`, is the `late` comparator exactly `<=` against the PREVIOUS `archived_through`
(design §7)? Does the candidate-range function union `ts > archived_through` with the two most recent
completed sessions, DST- and holiday-aware? Does an unknown interval fail loud rather than silently
defaulting?

BUCKET C (runner, shadow, report) — if you have `build-C-runner-shadow-report.diff`:
(Q7) Does the `write_mode` dispatch happen BEFORE any append-specific step, with the `upsert` branch
sending the whole export through `upsert_bars` exactly as today (no completeness filter, no range cut,
no comparison gate, no progress/incident write)? F6: is the shadow artifact's night now derived from the
ET calendar date (via `SessionClock.to_et`), not a raw `.date()` on a UTC instant — and is this the
ONLY change in `runner.py` beyond round 1's shipped shape?
(Q8) Does the shadow compare run strictly after the fetch and before the write, and is it read-only —
does an exception or timeout inside it leave the write and the summary identical to a shadow-off night?

BUCKET D (quiet window, archiver CLI) — if you have `build-D-quiet-cli.diff`:
(Q9) F1/F2: does `_cmd_restate` now write bars via the connection-taking sibling INSIDE the same
`target_transaction()` block as the pre-commit re-check, with the re-check running AFTER the write, so a
failed re-check rolls both the bar write and the incident write back together? Do the two named boundary
tests (`test_gemini_close_boundary_poller_lag`, `test_astra_open_boundary_repair_crosses_open`) now
invoke the real command path, not only `quiet_verdict`?
(Q10) F3/Q10: find the differing-value and equal-value race tests. Do they assert WHICH value survives
a race (not merely that "no bar row changed"), and is the assertion honest about what a fake can prove
versus what needs a real transaction (L45)?
(Q11) F4: for the four tests round 1 named (`test_the_refusal_exit_code_is_two`,
`test_both_mutating_commands_are_refused_in_every_scanned_session`, `test_previews_always_run`,
`test_backfill_missing_never_calls_upsert_bars`), do the rewritten versions actually invoke a
command/handler rather than asserting a class attribute or an unexercised monkeypatch?
(Q12) Is there still NO `--force` flag anywhere (the parser rejects it on both repairs), and does the
quiet-window refusal text still carry every observed value and the earliest allowed start?

CROSS-CUTTING (answer if your bucket touches it):
(Q13) Does anything you read contradict, weaken, or silently reinterpret any of round 1's SEVEN fixes
(F1–F7) as `verdicts-r1.md` describes them? Say so explicitly if you find nothing, and explicitly if you
find something.

End with, for each finding you were able to check, one line per round-1 item your bucket covers:
`F<n>: FIXED / NOT FIXED / REGRESSED / N/A THIS CALL`. Then, on its own final line:
`VERDICT (THIS CALL): CLEAN / FIX FIRST <finding numbers> / UNSAFE / PARTIAL (bucket <letter> only)`.
