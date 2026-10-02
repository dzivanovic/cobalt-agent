JOB: slot-guard
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R18
BRANCH: ops/slot-guard-1002
WORKTREE: slot-guard-1002
BASE: 1df251b9
TIP:
REPORT: /Users/cobalt/cobalt-wt/slot-guard-1002/docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/slot-guard-check-2026-10-02.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: row S1
RULINGS: 2026-10-02 R18, 2026-10-02 R47

## ROWS

| row | what | red first | files |
|---|---|---|---|
| S0 | RUN — asserts nothing. Which steps consume `aset_sizings` slots, measured. At W, with the lock held, the slot read `<SL>` (typed exactly, below) after (b), after (c), after (c2), after (c3) and after (f); quote each `max_attnum · dropped · live`, the `-rA` line of `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips`, and the `ADD COLUMN` count of each registry migration that alters `aset_sizings` (`grep -c -F "ADD COLUMN" <file>` on `0004`, `0007`, `0021`, `0022`). `DECISION S0`: the growth per phase and the steps that cause it | — (tool output quoted) | none (read only) |
| S1 | Every `cobalt db migrate` run (forward, `--proof-only`, `--rollback`) prints, after its proof table, inside its existing transaction and read-only: one `SLOTS WARN <schema>.<table> max_attnum <n> of 1600 · dropped <d> · live <l> · fix: cobalt db dev-rebuild <schema>.<table> (dev only)` line for each relation in `system` / `"user"` with `max(attnum)` ≥ `SLOT_WARN_AT` (1200, a module constant beside `DEFAULT_LOCK_TIMEOUT_S` in `src/cobalt/db_migrations/cli.py`), else ONE line `SLOTS ok · highest <schema>.<table> <n> of 1600`. The read is ONE function, `slot_report(conn)`, in `src/cobalt/db_migrations/dev_rebuild.py` (card 11's module), used by S1 and S2 (L3). A `--proof-only` on production prints the same line and changes nothing | offline, in `tests/cobalt/test_dev_rebuild_cli.py`: a fake connection answering `(user, aset_sizings, 1581, 1527, 54)` → the WARN line exactly; `(user, aset_sizings, 664, 610, 54)` → `SLOTS ok · highest user.aset_sizings 664 of 1600`; the two ends of the `≥ 1200` edge. with-DB, in `tests/cobalt/test_dev_rebuild_db.py`: `slot_report` on `cobalt_dev` at `0013` returns for `"user".aset_sizings` the same three numbers `<SL>` reads, inside a rolled-back transaction. RED on `BASE`: `ImportError: cannot import name 'slot_report'` | `src/cobalt/db_migrations/dev_rebuild.py`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md` |
| S2 | The with-DB suite checks headroom before its first test. In `tests/cobalt/conftest.py`, a session-start hook that runs only when the Postgres settings are present: `slot_report` on `cobalt_dev`; any relation with `1600 − max_attnum` < `SLOT_FAIL_HEADROOM` (64: the largest committed churn of one suite run, S0's figure, plus the 33 a rolled-back test adds inside its transaction — `test_radar_score_migration.py:497`–`506` re-adds `0007` after `0021`/`0022`) → `pytest.exit("cobalt_dev column slots: <table> <n> of 1600 — run a devfix (cobalt db dev-rebuild <table>) before any with-DB gate", returncode=3)` before any test runs; `max_attnum` ≥ `SLOT_WARN_AT` → one line in the terminal summary, the run goes on. Offline runs are untouched. The decision is a pure function `slot_verdict(rows, warn_at, fail_headroom)` beside `slot_report` | offline, in `tests/cobalt/test_dev_rebuild_cli.py`: `slot_verdict` on `1581` → `fail`; on `1537` → `fail`; on `1536` → `warn`; on `1199` → `ok`; with no rows → `ok`. RED on `BASE`: the name does not exist. The hook itself is shown at W: pass 1's summary carries the `SLOTS` line or nothing, quoted | `tests/cobalt/conftest.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py` |

## NOT IN THIS JOB
- `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`: no hub text in this job. The row that made the hubs quote the `SLOTS` line (the drafter's S3) moved to the 2026-10-03 adoption card, because card 16 (ops-seam) rewrites the same lock lines today. `TREE STATE: row S1` therefore writes NO hub line: S1's with-DB test lives in `tests/cobalt`, needs no migration above `0013` and runs inside the pass-1 command as written; say so under `## RECORDS` with the `-rs` proof that it ran.
- `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip`: its committed rollback to `0001` stays as written (it proves every reverse script for real); a narrower `--down-to` is a `## DECISIONS` item, never built here.
- Any registry migration; `cobalt db dev-rebuild` itself (card 11); `desk-launch.sh` and `DEVFIX-HUB.md` (card 12).
- A real rebuild on `cobalt_dev`; any production write.
- Any allow string; the pass-1 / pass-2 commands beyond what row S1's tests need.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-01-1.md` `## L68 GATE` (c).
- `tests/cobalt/test_tenancy.py` `_migrate` (~668) and `TestMigrationRoundTrip` (~693–720).
- `tests/cobalt/test_radar_score_migration.py` `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` (~412–510).
- `src/cobalt/db_migrations/0004_radar_pool.rollback.sql`, `0007_radar_cards.rollback.sql`, `0021_legs.rollback.sql`, `0022_prediction_records.rollback.sql`: the `aset_sizings` `DROP COLUMN` lines.
- `tests/cobalt/conftest.py` (the `requires_db` gate and the Postgres settings check, ~117).

## RECORDS
- `<SL>`, the slot read, as the deploy hub ran it on `cobalt_dev` (`deploy-2026-10-01-1.md` (c)), typed whole: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT max(a.attnum) AS max_attnum, count(*) FILTER (WHERE a.attisdropped) AS dropped, count(*) FILTER (WHERE NOT a.attisdropped) AS live FROM pg_catalog.pg_attribute a WHERE a.attrelid = '\"user\".aset_sizings'::regclass AND a.attnum > 0"`.
- THE CAUSE, READ FROM CODE AND UNPROVEN (L70) — S0 measures it. Two committed paths free no slot and add new ones on `aset_sizings`: (1) `TestMigrationRoundTrip` (pass 2 of every build, check and deploy) runs `db migrate --rollback --down-to 0001` then `db migrate` in a subprocess that commits (`test_tenancy.py:697`–`710`): it drops and re-adds `0004`'s 2, `0007`'s 25, `0021`'s 3 and `0022`'s 1 columns = 31 slots a run; (2) W / G (c2) forward and (f) rollback commit `0021` + `0022`: 4 slots a run. The rolled-back test that failed (`test_radar_score_migration.py:497`–`506`) frees its slots at rollback, but needs about 33 free inside its transaction. `1527` dropped ÷ ~35 a gate ≈ 44 with-DB pass-2 runs. (the drafter, 06:27 ET)
- RESTARTS class homes: `src/cobalt/db_migrations/*.py` → "static import reach" (`src/cobalt/jobs/restarts.py:210`); `tests/cobalt/*` → "test/documentation" (`:239`); `docs/…` → DOCS (`:219`). No `configs/` path. (the drafter, 06:27 ET)
- Cut by the brain 09:20 ET (`reports/brain-direction-2026-10-02.md`): rows S0–S2 only; the base is card 11's BUILT tip; the check is the fresh Opus session alone (2026-10-02 R47).
- The judge seat's answers to the build's DECISIONS (2026-10-02 R41): (1) a failed slot read is printed `SLOTS UNKNOWN` under a savepoint and never aborts the migrate run: kept; (2) `SLOT_FAIL_HEADROOM` stays 64 (33 must fit after the read in pass 1, 32 in pass 2); (3) the hook's exit and warn branches are pinned by a test the build added on the judge's answer. `TREE STATE: row S1` writes no hub line (this card's NOT IN THIS JOB); that is not `TREE STATE NOT CARRIED`.
