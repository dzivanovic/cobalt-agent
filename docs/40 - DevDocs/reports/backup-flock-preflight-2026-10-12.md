# Card 441 backup-flock-1012 — preflight 2026-10-12

§0 One FAIL: header `RULINGS` lacks R1138 (K5, L81). Everything else holds at HEAD `bb30db97`. Fix the header line and it is ready. Five NOTEs below, none blocks.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- "…/441-backup-flock-card.md"` | empty (also empty for `src tests configs ops`) | OK |
| 2 | `grep -c "«FILL" <card>` | 1, line 7 (`BASE`) only | OK |
| 3 | card header `CLASS:` | no `CLASS:` key in the header; the card's `CLASS: K5` is line 3 — present, `K5` | OK |
| 4 | card header `RULINGS:` | `2026-10-12 R1289, 2026-10-12 R1295`; no R1138 anywhere in the card (`grep -o` hits: R1289, R1295 only) | **FAIL** |
| 5 | rows' kind (`reports/cto-2026-10-12.md:8`, `:14`, `:163`) | R1295 and R1289 = DESK RECORD (brain, L79); R1138 = HIS RULING · APPROVED | OK (rows), FAIL via #4 |
| 6 | `grep -rln -F "never a glob"` over reports and prompts/2026-10-12 | card line 19 and `440-draft-backup-flock.md:6` (quoted there as the brain's row "byte for byte"); the text in the card equals it. `cto-2026-10-12.md:14` holds a shorter R1289 record, not that text | OK (NOTE 1) |
| 7 | `grep -o -E "lock_wait_min\|BackupConfig\|backup.yaml"` on the card | `backup.yaml` ×4 (fence, READ, RECORDS), `BackupConfig` ×1 (X5); no `lock_wait_min`; no edit of any of the three | OK |
| 8 | `LOCK_WAIT_S = 1800` home | card (a): module constant in `restic.py` after `:48`, `#:` comment as `db_apply.py:58` (`BACKUP_MAX_AGE_S = 900`, confirmed) | OK |
| 9 | `git show HEAD:restic.py` / Read `restic.py:1-200`: `STAGING` `:48`; header `:9-17`; imports `:27-34`; `dump_database` `:155-159`; `snapshot` `:162-198`; refusals `:165-171`, `:176-177`; mkdir `:180`; `try` `:181`; dump `:184`; size `:185`; targets `:182`, `:186`; `finally` `:193-197`; glob `:196`; comment `:194-195` | every anchor matches | OK |
| 10 | `pgdump.py:99` `out.open("wb")`, `:105` size; `scratch.py:200`, `:211`, `:212-213` | match | OK |
| 11 | `test_backup.py` anchors: `_cfg` `:29-41`, `:87-89`, `TestSnapshotRefusals` `:133-148`, `TestMountGuard` `:151-201`, `TestStagingPath` `:204-226`, pin `:205-211`, import `:26` | match | OK |
| 12 | `test_db_apply.py:390` pin; `db_apply.py:56-58` | `assert db_apply.BACKUP_MAX_AGE_S == 900` at `:390`; constant `:58` | OK |
| 13 | `wc -l` restic, config, pgdump, cli, test_backup, backup.yaml | 295, 184, 117, 81, 226, 83 = card RECORDS | OK |
| 14 | `jobs.yaml` `:99`, `:203`, `:263`, `:268`; `ops/run_backup.sh:24`, `:39`; `cli.py:67`; `backup/cli.py:19`; `DEPLOY-HUB.md:39`, `:131`; `PRODWRITE-HUB.md:34`; `BUILD-HUB.md:12`, `:80` | all match (`timeout_s: 3600`, `at: "21:40"`, `imports: [cobalt.cli]`, `uv run cobalt backup run`) | OK |
| 15 | red reasons on BASE: T1 `FileNotFoundError` (glob `:196` unlinks run 1's… run 2's dump); T2 `DID NOT RAISE` (no lock); T3 `other.sql` missing (glob); T4 `AttributeError` | each named and follows from `:162-198`; the three row reds (two finish, lock past wait fails loud, other `*.sql` left) are T1, T2, T3 | OK (NOTE 2) |
| 16 | `.backup.lock` vs the only glob `*.sql` (`restic.py:196`, removed by F1); restic targets `cfg.sources` + dump path (`:182`, `:186`) | the lock file is matched by no glob, never unlinked (card (c)), never a target | OK |
| 17 | new commands on any seat line (R411, R412) | build line has `uv run pytest *` and `uv run cobalt jobs restarts *` (`BUILD-HUB.md:12`); deploy line has `backup run*`, `backup status*`, `jobs restarts *`; none new | OK |
| 18 | RESTARTS class homes in `## RECORDS` | `restarts.py:216-220`, `:225-228`, `:246` (`:220` "static import reach", `:246` "test/documentation; no resident") named; chain `jobs.yaml:203` → `cli.py:67` → `backup/cli.py:19` → `restic` proven by my reads; `aset` (`jobs.yaml:99`) imports `cobalt.aset.__main__`, whose only backup-free imports I grepped (no `backup` hit in `aset/__main__.py`), card's drafter computed `aset` → `cobalt.backup.config` only | OK (NOTE 3) |
| 19 | `RESTARTS: com.cobalt.radar` justified | `restic.py` is imported by `com.cobalt.radar` via `cobalt.cli`; `tests/` and `docs/` add none | OK |
| 20 | `FOR THE CHECK` ×2 and `FOR THE DEPLOY` lines | present (card lines 47, 48, 49). Check lines carry R1289 / R1295 text; the `FOR THE DEPLOY` text is the drafter's wording of R1295's windows, not a copied row | OK (NOTE 4) |
| 21 | deploy windows in the card | outside 09:30-16:00 ET and 21:30-22:30 ET — matches R1295 (`cto-2026-10-12.md:8`) | OK |
| 22 | decisions of `draft-backup-flock-2026-10-12.md` (5) and `draft-441-amend` (4) each have a stated default and the card agrees | 1 `DB` key left out → card has no `DB:` key; 2 `backup.yaml` key → overruled by R1295, card uses the constant; 3 hub timeout → fenced, window rule in `FOR THE DEPLOY`; 4 nightly `timeout_s` fenced (`NOT IN THIS JOB`); 5 build card, not a devfix; amend 1-4 stated | OK (NOTE 5) |

## ISSUES
- FAIL #4: header `RULINGS` is `2026-10-12 R1289, 2026-10-12 R1295`; add `2026-10-12 R1138` (his rule, K5, L81; HIS RULING · APPROVED, `cto-2026-10-12.md:163`). The card text also never names R1138.
- NOTE 1: the card's quoted row is the brain's text as the desk stored it in prompt 440; `cto-2026-10-12.md` R1289 (`:14`) holds only a short record. The card matches 440 byte for byte, not R1289's own line.
- NOTE 2: T1's red on BASE relies on the fake `_snapshot_one` pause being longer than run 2's start-to-dump time (the event orders run 2's start, a sleep orders the race). Name a second `Event` (run 2's dump written) that run 1's fake snapshot waits on, so the red is not timing luck (X4).
- NOTE 3: `com.cobalt.aset` reach is the drafter's `reach.py` result; I read no restic import in `aset/__main__.py` but did not re-run `import_graph`. The build's R3 table is the value.
- NOTE 4: `FOR THE DEPLOY` is not in any prompt (grep of 442: no hit); it states R1295's windows. Not a copy of a row.
- NOTE 5: R1289 and `OWED` say "devfix card (K2/K5)"; the card is a build card, `CLASS: K5` only, as the draft's decision 5 states.
- DEPLOY: the card needs a deploy hub (card 441's own `deploy:` card; none exists yet). Blockers: (1) build, then check ready YES must come first; (2) card 439 (recut-archive) resumed at STEP-D0 by hub `171b5948` must end `DEPLOYED` or `FAILED` first (one deploy at a time); (3) `DEPLOY-HUB.md` has no row keeping D2.4 off 21:30-22:30 ET (R1295: "hub row owed in the next hub-text card"); D2.4 `backup run` runs FOREGROUND with `timeout` 600000 (`:39`, `:131`), shorter than the 1800 s wait; the desk keeps the launch off the window; (4) the restart of `com.cobalt.radar` needs a time outside 09:30-16:00 ET.
- RISK (fenced, from the draft's decision 4): a nightly that waits 30 min plus a ~7 GB dump may pass `timeout_s: 3600` (`jobs.yaml:263`); margin unmeasured.

PREFLIGHT DONE · card: backup-flock-1012 · checks: 22 · fails: 1 · ready: NO
