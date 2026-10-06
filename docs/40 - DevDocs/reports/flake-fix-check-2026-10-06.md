# flake-fix — check, pass 1 (2026-10-06)

## §0 Headline
- House A was Sol: 3 findings. My own read gave 4. All 7 were run, and 2 held.
- H2 held: `migrated` did not retry a deadlock raised while the connection was being opened. H3 held: a `rollback()` that raises left the failed attempt's connection open. Both are fixed in `f520debb`. Their reds were committed first in `814f56fd`.
- The gate is green on `f520debb`: offline 3932/0, with-DB 886/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed, RESTARTS none.
- One item is open: H1, REJECTED (the DevDocs line is required by BUILD-HUB E3). So house B (Grok) is needed and `ready: NO` until pass 2.

## L74
No tool result carried an instruction. The session's attribution reminder (a system message, not a tool result) asked for a `Claude-Session:` line in commits. That reminder defers to the user's own rules, and this hub rules commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Both commits (`814f56fd`, `f520debb`) carry that line alone.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 0 · 16a99771e6581bb5544ae40c8c66c023a013b076
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (STANDING: `Bash(grok *)` pre-approved)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (STANDING: the four house strings pre-approved)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty)

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Tue Oct  6 01:45:49 EDT 2026
status · git status --short --branch · 0 · ## ops/flake-fix-1006
head · git log --oneline -1; git log --stat --format=%h d1fee872..HEAD · 0 · (5 lines)
    0ff56462 docs(flake-fix): build report — d1fee872
    0ff56462
    
     .../reports/flake-fix-build-2026-10-06.md          | 223 +++++++++++++++++++++
     1 file changed, 223 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/flake-fix-1006/docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md" · 0 · BUILT · job: flake-fix · tip: d1fee872 | on d1adf256 | migration: none | offline 3932/0 | with-DB 884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 1 · tokens: 175288
range · git log --oneline d1adf256..d1fee872 · 0 · (2 lines)
    d1fee872 fix(flake-fix): migrated fixture retries the migration step on DeadlockDetected (F1, L1 L45 L76)
    ac55ec16 wip(flake-fix): red — migrated fixture retry tests (F1)
PREFLIGHT OK
```
- THE RANGE, typed: `git log --stat --format=%h d1adf256..d1fee872` · exit 0:
```
d1fee872
 docs/40 - DevDocs/cobalt/drc/store.md |  3 +++
 tests/cobalt/test_drc_store.py        | 22 ++++++++++++++++++----
 2 files changed, 21 insertions(+), 4 deletions(-)
ac55ec16
 tests/cobalt/test_drc_store.py | 80 ++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 80 insertions(+)
```
  Path union: `tests/cobalt/test_drc_store.py`, `docs/40 - DevDocs/cobalt/drc/store.md`.
- The card is not "DB: none": no name-only row.
- `ls <S>` (`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/flake-fix-check`) · exit 1 · `No such file or directory` → fresh.
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
  → **house A: OpenAI Sol (`gpt-5.6-sol`) · house B, if needed: Grok**. Card: `HOUSE B: as needed` → the MANDATORY rule does not apply.
- PROVEN BY FIRST REAL USE: the write and with-DB strings, at their first real use (`## 4` / `## 6`).

## Files copied
House A is Sol: (1) and (2) as typed, no (3) copies (Sol reads the originals).
- `<S>/diff.md` · from `git log -p d1adf256..d1fee872 -- . ":(exclude)docs"` (background run, output read whole, written with the heading) · 5289 bytes · `grep -c "^commit "` → `2` = PREFLIGHT's commit count (2).
- `<S>/rulings.md` · R326 and R412, each `grep -n "^| R<n> "` output under its command line · 799 bytes.
- `<S>/HOUSE-INSTRUCTIONS.md` · HOUSE TEXT verbatim + `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole + "Files:" paragraph · 8424 bytes.
- Launch: `date` → `Tue Oct  6 01:47:46 EDT 2026`; the house gates R17 and R19 grepped again, one row each; `ls -la <S>` → the three files above; `cd /Users/cobalt/cobalt-wt/agy-trial`; the SOL line as written, `run_in_background`, `timeout` 2700000 (task `bwckez4re`); `cd /Users/cobalt/cobalt-wt/flake-fix-1006`; `git status --short --branch` → `## ops/flake-fix-1006`.

## OWN FINDINGS
Written before house A's list was opened. Read: the card, its rulings (via `authorize.sh`), `diff.md` `d1adf256..d1fee872`, `tests/cobalt/test_drc_store.py:1-430` at the tip, `cli.py:625-649`, `db.py:265-294`, `test_drc_k2_experiments.py:38-52`, the build report whole, and `cobalt.md` `## What Cobalt is` and `## Build rules` to the end.

FINDING O1
ROW: F1 / X2
CLAIM: The row says a deadlocked attempt's connection is "rolled back and closed first"; the tests pin only `.closed` (`tests/cobalt/test_drc_store.py:401`, `:416`), so the rollback at `tests/cobalt/test_drc_store.py:242` and its order before `close()` are pinned by no test.
RUN: TEST — `tests/cobalt/test_drc_store.py`
```python
@requires_db
def test_check_o1_a_deadlocked_attempt_is_rolled_back_before_it_is_closed(
    deadlock_first, monkeypatch, request
):
    calls = []
    real_connect = db.connect_migration

    def _spy(dbname, **kw):
        conn = real_connect(dbname, **kw)
        real_rollback, real_close = conn.rollback, conn.close

        def _rollback():
            calls.append((id(conn), "rollback"))
            return real_rollback()

        def _close():
            calls.append((id(conn), "close"))
            return real_close()

        conn.rollback, conn.close = _rollback, _close
        return conn

    monkeypatch.setattr(db, "connect_migration", _spy)
    conn = request.getfixturevalue("migrated")
    first = deadlock_first[0]
    assert calls[:2] == [(id(first), "rollback"), (id(first), "close")]
    assert first.closed and not conn.closed
```
EXPECT: if the claim holds as a defect, `assert calls[:2] == [...]` fails; on a correct tip the test passes (→ NOT HELD, and X2's rollback clause is then pinned by a run).

FINDING O2
ROW: F1 / X3
CLAIM: The branch "deadlock on attempt 1, then another error on attempt 2" (`tests/cobalt/test_drc_store.py:241-250`) is pinned by no test: the other-error path is tested only on attempt 1 (`:419-424`).
RUN: TEST — `tests/cobalt/test_drc_store.py`
```python
@requires_db
def test_check_o2_another_error_after_a_retry_is_raised_at_once(monkeypatch, request, capsys):
    seen = []

    def _fake(conn, paths):
        seen.append(conn)
        if len(seen) == 1:
            raise psycopg.errors.DeadlockDetected("constructed by flake-fix check O2")
        raise psycopg.errors.UndefinedTable("constructed by flake-fix check O2")

    monkeypatch.setitem(globals(), "_apply", _fake)
    with pytest.raises(psycopg.errors.UndefinedTable):
        request.getfixturevalue("migrated")
    out = capsys.readouterr().out
    assert "migration retry 1: DeadlockDetected" in out
    assert "migration retry 2" not in out
    assert len(seen) == 2
    assert all(c.closed for c in seen)
```
EXPECT: if the branch were wrong, `pytest.raises(UndefinedTable)` fails (`DID NOT RAISE` or another error), or `assert all(c.closed …)` fails; on a correct tip it passes (→ NOT HELD).

FINDING O3
ROW: SCOPE / X1
CLAIM: The range touches a path outside the row's file `tests/cobalt/test_drc_store.py` beyond the one DevDocs line the hub requires, or reaches `src/`, `conftest.py` or `ops/desk/` (the fence).
RUN: COMMAND — `git diff --stat d1adf256 d1fee872`
EXPECT: if the claim holds, a path other than `tests/cobalt/test_drc_store.py` and `docs/40 - DevDocs/cobalt/drc/store.md`; else exactly those two (→ NOT HELD). Inside the test file, `diff.md` shows only the `migrated` body (`@@ -230,12 +230,26 @@`) and the block of new helper, fixtures and tests (`@@ -330,6 +330,86 @@`).

FINDING O4
ROW: F1 / X4
CLAIM: The row's red test `test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks` is not red on BASE for the stated reason (the raise out of `request.getfixturevalue("migrated")`, in the call phase), but for a setup error or a skip.
RUN: COMMAND — with the `migrated` body at `tests/cobalt/test_drc_store.py:233-250` replaced by the BASE lines (`git show d1adf256:tests/cobalt/test_drc_store.py`, lines 232-237: `conn = db.connect_migration(env.DEV_DB_NAME)` / `conn.autocommit = False` / … `_apply(conn, FORWARD)` inside the `try:`), inside one lock take: `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py -k migrated_fixture`; then the tip body restored with Edit and `git diff --stat` → empty.
EXPECT: if the claim holds, `ERROR` or `SKIPPED` for `…retries_once…`; if the build is right, `FAILED …retries_once…` with `psycopg.errors.DeadlockDetected: constructed by flake-fix F1`, `FAILED …third_deadlock…` with `assert 'migration retry 1: DeadlockDetected' in ''`, and `PASSED …does_not_retry_another_error` (→ NOT HELD).

No path to a score, rank, grade or size: the range is test and docs only (O3's run settles it). No person or vendor name in an identifier in the diff (read: `_patch_apply`, `deadlock_first`, `deadlock_always`, `undefined_table_first`, the three test names).

## Findings
House A Sol finished at the notice (`date` → `Tue Oct  6 01:54:28 EDT 2026`, exit 0, `tokens used 277,638` in its output). `ls -la <S>` showed no house file (Sol writes none). I wrote its FINAL message (output lines 10894-10967, ending `FINDINGS: 3`) to `<S>/house-a.md`. Its earlier streamed drafts are not the list. THE DROP: `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: COMMAND — …`, `10:RUN: TEST — …`, `42:RUN: TEST — …`. Each TEST is followed by a `def test_`, and the COMMAND begins `git diff`. All three are kept.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| H1 | Sol | X1 | The branch changes `docs/40 - DevDocs/cobalt/drc/store.md`, though F1's files name only `tests/cobalt/test_drc_store.py` | COMMAND |
| H2 | Sol | F1 | `connect_migration` runs before the retry handler (`test_drc_store.py:236`), so a deadlock while opening an attempt escapes instead of retrying the whole step | TEST |
| H3 | Sol | X2 | The deadlock branch closes only after `rollback()` returns (`:242`); a rollback failure leaks the failed attempt's connection | TEST |

## Dropped
none

## RUNS
All four TEST findings were run in ONE lock take. `take-devdb-lock.sh flake-fix-1006 90` → `lock taken: flake-fix-1006`. `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/flake-fix-1006/.env` (01:55:49 EDT). `<FP>` → F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED` / `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` / `TABLES 0011`, so the level is 0013 (the build's E2 reading of `gate-lists.md` `## LEVEL 0013`). No forward was run. Each test was added with Edit and run alone as `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no [--tb=short] tests/cobalt/test_drc_store.py::<test>`. No test's form was repaired.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | TEST `test_check_o1_a_deadlocked_attempt_is_rolled_back_before_it_is_closed` | `1 passed in 0.25s` | NOT HELD — the failed attempt is rolled back, then closed, in that order; test removed with Edit |
| O2 | Opus | TEST `test_check_o2_another_error_after_a_retry_is_raised_at_once` | `1 passed in 0.07s` | NOT HELD — an `UndefinedTable` after one retry is raised at once and both connections are closed; test removed with Edit |
| O3 | Opus | COMMAND `git diff --stat d1adf256 d1fee872` | `docs/40 - DevDocs/cobalt/drc/store.md \| 3 +` / `tests/cobalt/test_drc_store.py \| 102 ++…--` / `2 files changed, 101 insertions(+), 4 deletions(-)` | NOT HELD — two paths only: the row's file and the one DevDocs line BUILD-HUB E3 requires ("Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"); nothing under `src/`, `conftest.py` or `ops/desk/` |
| O4 | Opus | COMMAND, the `migrated` body set back to BASE with Edit (`git diff d1adf256 --stat -- tests/cobalt/test_drc_store.py` → `184 insertions(+)`, no deletion, so the fixture is byte-identical to BASE), `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py -k migrated_fixture`, then the tip body restored with Edit | `4 failed, 1 passed, 34 deselected in 0.14s`: `FAILED …::test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks` (`E   psycopg.errors.DeadlockDetected: constructed by flake-fix F1`, `:348`); `FAILED …::test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries` (`E   AssertionError: assert 'migration retry 1: DeadlockDetected' in ''`, `:397`); `PASSED …::test_the_migrated_fixture_does_not_retry_another_error`; H2's and H3's tests also red on BASE | NOT HELD — the row's red is FAILED in the call phase for the stated reason, with no ERROR and no skip (X4 settled); the negative control is green on BASE |
| H1 | Sol | COMMAND `git diff --name-only d1adf256..d1fee872` | `docs/40 - DevDocs/cobalt/drc/store.md` / `tests/cobalt/test_drc_store.py` | REJECTED — the output shows the docs path the claim names, but the line the build is bound by says the path is right: BUILD-HUB `## E3` "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`", and CHECK-HUB `## 7` (ii) counts only non-docs paths against the rows' `files`. It stays OPEN. |
| H2 | Sol | TEST `test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks` | `1 failed in 0.13s`: `E           psycopg.errors.DeadlockDetected: constructed while opening the first migration attempt` raised at `tests/cobalt/test_drc_store.py:236: in migrated` / `conn = db.connect_migration(env.DEV_DB_NAME)` | HELD — F1 says the fixture retries "the WHOLE step (open, `autocommit = False`, `_apply(conn, FORWARD)`)"; the open sat outside the `try` |
| H3 | Sol | TEST `test_the_migrated_fixture_closes_a_failed_attempt_when_rollback_fails` | `1 failed in 0.07s`: `tests/cobalt/test_drc_store.py:528` `assert conn.closed is True` / `E   assert False is True` | HELD — X2 "no connection leaked": a raising `rollback()` skipped `close()` |

Held tests committed before any fix: `814f56fd wip(flake-fix): check red — H2 H3` (`tests/cobalt/test_drc_store.py`, 55 insertions; `git diff --stat` before the commit → only that file, insertions only).

## FIXES
| fix | ids | file | change | proof |
|---|---|---|---|---|
| `f520debb fix(flake-fix): migrated retries the open too and closes a failed attempt when rollback raises (check H2 H3)` | H2, H3 | `tests/cobalt/test_drc_store.py` (the `migrated` body only); `docs/40 - DevDocs/cobalt/drc/store.md` (one dated line, `**2026-10-06 — flake-fix check (H2, H3).**`) | Each attempt sets `conn = None`, then `connect_migration`, `autocommit = False` and `_apply(conn, FORWARD)` all run inside one `try`. On any `BaseException` an opened connection gets `conn.rollback()` in a `try` with `conn.close()` in its `finally`. The exception is then re-raised unless it is `DeadlockDetected` on attempt 1 or 2, which prints `migration retry <n>: DeadlockDetected` and goes round. `counter`, `_connect`, the monkeypatch, `yield conn` and the final rollback and close are unchanged. | Same lock take: `COBALT_ENV=dev uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py tests/cobalt/test_drc_k2_experiments.py` → `52 passed in 2.75s` (the build's 50 + H2 + H3), 0 failed. `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh flake-fix-1006` → `lock released`; `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory` (01:57:35 EDT). |

## Suites
RESTARTS first: `uv run cobalt jobs restarts d1adf256..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md	A	DOCS	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
RESTARTS: none
```
There is no `UNCLASSIFIED` row. W ran on `f520debb` as ONE call, `sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-1006 all` (background, exit 0). It needed no `--deselect` (no migration and no with-DB file above 0013), no `--tickers` (no ticker written) and no `--migration`. The verdict lines, whole:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 886/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-015751.log
```
- offline: `3932 passed, 785 skipped, 2 xfailed, 36 warnings in 582.26s` (log `:860`). The two new tests skip offline (783 → 785 skips).
- PASS 1 executed (`:931`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect …` (the same deselect list the build report quotes from `gate-lists.md:24`) → `698 passed, 7 skipped, 4012 deselected, 2 xfailed, 12 warnings in 123.99s` (`:1000`). That is the build's 696 + H2 + H3. The 7 SKIPPED lines are quoted above; none is marked `OUTSIDE the allowed set`.
- `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:877`); `dev forward: APPLIED 02:09:54` (`:1002`); PASS 2 `188 passed, 1 deselected, 5 warnings in 223.73s` (`:1686`); 698 + 188 = 886 = `with-DB 886/0`.
- `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1751`) = F0 → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:1804`); live-note `146 passed, 1 skipped, 15 warnings in 25.12s` (`:1873`), the skip `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- `.env: removed`; `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory`.
- **RESTARTS: none.**

## Scope
PREFLIGHT's path union (`tests/cobalt/test_drc_store.py`, `docs/40 - DevDocs/cobalt/drc/store.md`) plus my commits `814f56fd` and `f520debb` (the same two paths). The non-docs path is `tests/cobalt/test_drc_store.py` = F1's `files`. The docs path is the DevDocs line both hubs require. No `configs/cobalt/jobs.yaml` change.

## Checked against the branch
- (i) `git log --oneline d1fee872..HEAD -- . ":(exclude)docs"` → `f520debb fix(flake-fix): migrated retries the open too and closes a failed attempt when rollback raises (check H2 H3)` / `814f56fd wip(flake-fix): check red — H2 H3`. `<tip now>` = `f520debb`.
- (ii) `git log --stat --format=%h d1fee872..HEAD` → `f520debb`: `docs/40 - DevDocs/cobalt/drc/store.md | 2 ++`, `tests/cobalt/test_drc_store.py | 24 +++…---`; `814f56fd`: `tests/cobalt/test_drc_store.py | 55 +++…`; `0ff56462`: `.../reports/flake-fix-build-2026-10-06.md | 223 +++`. The one non-docs path is F1's file. No WIDENED.
- (iii) Fences, each `git log --oneline d1adf256..HEAD -- <path>` → EMPTY: `src`; `tests/cobalt/conftest.py`; `ops/desk`; `tests/cobalt/test_p4_migrations.py tests/cobalt/test_voice_store.py tests/cobalt/test_archiver_migrations.py tests/cobalt/radar_migrated_support.py tests/cobalt/test_drc_d2_fix_r1_db.py`.
- (iv) `grep -n -F "def test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks" tests/cobalt/test_drc_store.py` → `430:…`; `grep -n -F "def test_the_migrated_fixture_closes_a_failed_attempt_when_rollback_fails" tests/cobalt/test_drc_store.py` → `456:…`. In (i), `814f56fd` (red) sits below `f520debb` (fix).
- (v) `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory`; `git status --short --branch` → `## ops/flake-fix-1006` alone.
- (vi) `git log --stat --format=%h d1adf256..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_drc_store.py` in all four commits. There is no new migration file and no new with-DB test file; the new tests run inside `migrated`'s rolled-back transaction at 0013 (PASS 1 ran them, 698 passed). No `gate-lists.md` change is owed.
- (vii) Card `## RECORDS`: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md"` → `b133743171ec855e164c445ceef03e657eb50eeb`; `… -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md"` → `b3583b280d50c829da1d8f5290c2c385b50ef68c`; the rows as `332:` and `109:` (AUTHORIZATION).
- (viii) L32: this report holds no ticker, price or date of his. The values are constructed test strings, fingerprints, commit ids and clock times.

COUNTING: findings 7 (O1–O4, H1–H3) · dropped 0 · held 2 (H2, H3) · fixed 2 · held unfixed 0 · open 1 (H1).

## OPEN
- **H1 (Sol, X1) — REJECTED.** Claim: "The branch includes `docs/40 - DevDocs/cobalt/drc/store.md`, although F1 allows changes only to `tests/cobalt/test_drc_store.py`." Run: `git diff --name-only d1adf256..d1fee872` → `docs/40 - DevDocs/cobalt/drc/store.md` / `tests/cobalt/test_drc_store.py`. Why it is rejected: BUILD-HUB `## E3` requires one dated DevDocs line per changed module, and CHECK-HUB `## 7` (ii) checks only non-docs paths against the rows' `files`. What would settle it: house B, or the judgment seat, confirming that the hub's DevDocs line is inside the row's scope. No code change is involved.

## CONTINUE
next: none (pass 1 closed; `house B: needed` → the desk launches PASS-2 with house B Grok)

## DECISIONS
none. The one open item, H1, is a scope reading about a docs path. It does not block the next step: pass 2 settles it per the flow. It touches no notes, money or sizing.

## RECORDS
- Clock at the first report write: Tue Oct  6 01:46:12 EDT 2026; at close: Tue Oct  6 02:16:08 EDT 2026.
- Dropped findings: none. Every house produced a list: Sol `FINDINGS: 3`, `tokens used 277,638`. Its stream also printed draft FINDING blocks (output lines 1288, 2144, 10783); only the final message (lines 10894-10967) is the list.
- `house B:` is `needed` (open 1). The seat order at PREFLIGHT read `grok: UP`, so house B = Grok.
- Lock takes: one by hand at `## 4`/`## 5` (01:55:49 – 01:57:35 EDT; `.env: removed, proven gone (## 5)`) and one inside `gate.sh` at `## 6` (`lock released`, log `:1804`; `.env: removed, proven gone (## 6)`). There was no extra take.
- The two NOT HELD tests (O1, O2) were removed with Edit before the red commit, as `## 4` says. They passed on the BUILD's fixture, not on the fixed one; the build's own tests (`.closed`, distinct connections) and H3 cover the fixed fixture's cleanup.
- No `REFUSED, not needed` line; no `CONTINUED` line.
- `files opened: 18`: `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `tests/cobalt/test_drc_store.py`; the build report (read whole); `src/cobalt/db_migrations/cli.py:625-649`; `src/cobalt/db.py:265-294`; `tests/cobalt/test_drc_k2_experiments.py:38-52`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` to the end); `docs/40 - DevDocs/cobalt/drc/store.md:238-242`; `.venv/…/psycopg/connection.py` and `.venv/…/psycopg/_connection_base.py` (a grep each for `__slots__`, to know whether O1's spy could set instance attributes; neither file is on WHAT YOU READ); the outputs of the house probe, the `git log -p` diff, Sol, the lock take and the gate, and the gate log (`grep -n -F` reads).
- Check of `flake-fix`, pass 1: house A `Sol` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: flake-fix · pass: 1 · tip: f520debb · house A: Sol FINDINGS: 3 · findings: 7 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: needed · suites: offline 3932/0 · with-DB 886/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 18 · ready: NO · decisions: 0 · for Dejan: 0 · tokens: 188362

# PASS 2

## §0 Headline
- House B was Grok (`grok-4.7`): 3 findings, all `grep` commands, none dropped. All 3 were run and each printed the line it predicted.
- They settle pass 1's one open item, H1. The DevDocs lines on `store.md` are required by BUILD-HUB `## E3` (`:71`) and CHECK-HUB `## 5` (`:107`), and CHECK-HUB `## 7` (ii) (`:113`) counts only non-docs paths. H1 is NOT HELD. Open: 0.
- No defect was found and no commit was made in pass 2. The tip stays `f520debb`, and pass 1's gate on that tip stands (offline 3932/0, with-DB 886/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`).
- `ready: YES`.

## L74
The session's attribution reminder (a system message, not a tool result) again asks for a `Claude-Session:` line in commits. This hub rules commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; that is followed, the reminder is not.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole: identical row for row to pass 1's block above (INSTALLED · 1 · nothing; PLACEHOLDER · 1 · nothing; CARD COMMITTED · 0 · `16a99771e6581bb5544ae40c8c66c023a013b076`; CARD UNCHANGED · 0 · nothing; STANDING LIST R60 row `46:` · committed `962e9d1705b62a61821f62f4d7bf5d8131656e2a` · at HEAD; RULING R326 row `332:` · committed `b133743171ec855e164c445ceef03e657eb50eeb` · at HEAD; RULING R412 row `109:` · committed `b3583b280d50c829da1d8f5290c2c385b50ef68c` · at HEAD), last line `AUTHORIZED`.
House gates (02:17 EDT): `grep -n "^| R17 " …cto-2026-09-24.md` → one row `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`; `grep -n "^| R19 " …` → one row `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
- `date` → `Tue Oct  6 02:17:03 EDT 2026`.
- PASS 2 row: `tail -n 3 "<CHECK REPORT>"` → last non-blank line `CHECK DONE · job: flake-fix · pass: 1 · tip: f520debb · house A: Sol FINDINGS: 3 · … · house B: needed · … · ready: NO …` → starts `CHECK DONE · job: flake-fix · pass: 1`, carries `house B: needed`. `<tip now>` = `f520debb`.
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Tue Oct  6 02:17:12 EDT 2026
status · git status --short --branch · 0 · ## ops/flake-fix-1006
head · git log --oneline -1 · 0 · f520debb fix(flake-fix): migrated retries the open too and closes a failed attempt when rollback raises (check H2 H3)
env here · ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/flake-fix-1006/docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md" · 0 · BUILT · job: flake-fix · tip: d1fee872 | on d1adf256 | migration: none | offline 3932/0 | with-DB 884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 1 · tokens: 175288
range · git log --oneline d1adf256..d1fee872 · 0 · (2 lines)
    d1fee872 fix(flake-fix): migrated fixture retries the migration step on DeadlockDetected (F1, L1 L45 L76)
    ac55ec16 wip(flake-fix): red — migrated fixture retry tests (F1)
PREFLIGHT OK
```
  `git log --oneline -1` shows `f520debb` = pass 1's `tip:`.
- THE RANGE to `<tip now>`: `git log --stat --format=%h d1adf256..f520debb` → `f520debb` (`docs/40 - DevDocs/cobalt/drc/store.md | 2 ++`, `tests/cobalt/test_drc_store.py | 24 +++…---`), `814f56fd` (`tests/cobalt/test_drc_store.py | 55 +++`), `0ff56462` (`.../reports/flake-fix-build-2026-10-06.md | 223 +++`), `d1fee872` (`store.md | 3 +++`, `test_drc_store.py | 22 +++…-`), `ac55ec16` (`test_drc_store.py | 80 +++`). Path union: `tests/cobalt/test_drc_store.py`, `docs/40 - DevDocs/cobalt/drc/store.md`, the build report.
- `ls <S>` → `diff.md`, `house-a.md`, `HOUSE-INSTRUCTIONS.md`, `opus-1.md`, `rulings.md` (pass 1's folder).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0 → `sol: UP` / `grok: UP` / `gemini: UP`. Pass 1's house A = Sol → **house B: Grok** (the first house UP that is not Sol).

## Files copied
- P2.1 diff: `git log -p d1adf256..f520debb -- . ":(exclude)docs"` (background, read whole) → `<S>/diff-b.md` with the heading, 9670 bytes; `grep -c "^commit "` → `4` = the non-docs commits of the range (`ac55ec16`, `d1fee872`, `814f56fd`, `f520debb`; `0ff56462` is docs-only).
- `sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 1 · `REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/flake-fix-check` (pass 1's folder holds its files; pass 1 seated Sol, so no `files/` existed). The copies were made instead by the per-file `stage-copy.sh`, each its own call, the worktree being clean at `f520debb`:
  - `COPIED 6304 <S>/files/02-flake-fix-card.md`
  - `COPIED 31016 <S>/files/flake-fix-build-2026-10-06.md`
  - `COPIED 26015 <S>/files/wt/tests/cobalt/test_drc_store.py` (original `wc -c` 26015)
  - `COPIED 15095 <S>/files/wt/docs/40 - DevDocs/cobalt/drc/store.md` (original `wc -c` 15095)
  - `COPIED 51465 <S>/files/wt/src/cobalt/db_migrations/cli.py`
  - `COPIED 14043 <S>/files/wt/src/cobalt/db.py`
  - `COPIED 26902 <S>/files/wt/tests/cobalt/test_drc_k2_experiments.py`
  - `COPIED 7282 <S>/files/second-writer-survey-2026-10-05.md`
  - `COPIED 18672 <S>/files/deploy-deploy-k3-1005-attempt2.md`
- `<S>/HOUSE-B-INSTRUCTIONS.md` · HOUSE TEXT with the HOUSE B paragraph + the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole + "Files:" (`diff-b.md`, `house-a.md`, `opus-1.md`, `rulings.md`, the `files/` copies) · 9047 bytes. `house-a.md`, `opus-1.md`, `rulings.md` are pass 1's.
- P2.2 launch: `date` → `Tue Oct  6 02:20:09 EDT 2026`; R17 and R19 grepped again, one row each; `ls -la <S>` → the files above; `cd /Users/cobalt/cobalt-wt/agy-trial`; the GROK line as written (with `HOUSE-B-INSTRUCTIONS.md`, `house-b.md`), `run_in_background`, `timeout` 2700000 (task `bz8f0yovh`); `cd /Users/cobalt/cobalt-wt/flake-fix-1006`; `git status --short --branch` → `## ops/flake-fix-1006`.

## OWN FINDINGS
none: pass 2 has no own read (CHECK-HUB `## PASS 2`, P2.3).

## Findings
House B Grok finished at the notice (`date` → `Tue Oct  6 02:36:02 EDT 2026`, exit 0). Its stdout ended with the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/flake-fix-check/house-b.md`, and `ls -la <S>` showed `house-b.md` at 1519 bytes, 02:35. Grok wrote the file itself; its last line is `FINDINGS: 3`. THE DROP: each block has a `RUN: COMMAND —` line (lines 4, 10, 16) beginning `grep`, so all three are kept.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| B1 | Grok | X1 | H1 is not a defect: `store.md:239`'s dated line is the one BUILD-HUB `:71` requires for the changed module | COMMAND |
| B2 | Grok | X1 | The check's second dated line (`store.md:242`) is the one CHECK-HUB `:107` requires on a fix | COMMAND |
| B3 | Grok | X1 | A docs path does not fail X1: CHECK-HUB `:113` counts only non-docs paths against the rows' `files` | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| B1 | Grok | `grep -n -F "Each changed module gets ONE dated line" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` | `71:Build the rows in the card's order, … Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/` (`## <date> — <JOB>`: what changed). …` | HELD as stated: the line is at 71. It claims no defect, so nothing is fixed |
| B2 | Grok | `grep -n -F "One dated line in the changed module's page" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` | `107:Only inside the files the card's `## ROWS` name and their tests; … One dated line in the changed module's page under `docs/40 - DevDocs/cobalt/`. …` | HELD as stated: the line is at 107. It claims no defect, so nothing is fixed |
| B3 | Grok | `grep -n -F "every non-docs path is in some row" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` | `113:(i) … (ii) `git log --stat --format=%h <TIP>..HEAD` → every non-docs path is in some row's `files`, a test file, or `configs/cobalt/jobs.yaml` …` | HELD as stated: the line is at 113. It claims no defect, so nothing is fixed |
| H1 (pass 1, OPEN) | Sol | settled by B1–B3. Also `git diff d1adf256..f520debb -- "docs/40 - DevDocs/cobalt/drc/store.md"` | Two added blocks only: `## 2026-10-06 — flake-fix` (the build's E3 line) and `**2026-10-06 — flake-fix check (H2, H3).**` (pass 1's `## 5` line), 5 lines added, none removed | NOT HELD — the docs path is the DevDocs line both hubs require, and the scope count (`## 7` (ii)) excludes docs paths. It is not a scope breach. Closed |

No test was added and no test file was touched in pass 2, so there is no red commit.

## FIXES
none (no defect held in pass 2).

## Suites
No commit of mine in pass 2. `git log --oneline -1` → `f520debb`, the tip pass 1 gated. Pass 1's gate on `f520debb` stands, quoted in the pass-1 `## Suites` above: `offline 3932/0`, `with-DB 886/0`, `live-note 146/0`, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`; log `/Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-015751.log`. RESTARTS line: `RESTARTS: none` (pass 1's `uv run cobalt jobs restarts d1adf256..HEAD`; no path has changed since).

## Scope
Path union `d1adf256..f520debb`: `tests/cobalt/test_drc_store.py` (= F1's `files`), `docs/40 - DevDocs/cobalt/drc/store.md` (the required DevDocs lines) and `docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md` (the build report). Pass 2 added no commit.

## Checked against the branch
`<TIP>` here is pass 1's tip, `f520debb`. HEAD = `f520debb`, so (i) and (ii) are read from the build tip `d1fee872`.
- (i) `git log --oneline d1fee872..HEAD -- . ":(exclude)docs"` → `f520debb fix(flake-fix): migrated retries the open too and closes a failed attempt when rollback raises (check H2 H3)` / `814f56fd wip(flake-fix): check red — H2 H3`. `<tip now>` = `f520debb`.
- (ii) `git log --stat --format=%h d1fee872..HEAD` → `f520debb`: `docs/40 - DevDocs/cobalt/drc/store.md | 2 ++`, `tests/cobalt/test_drc_store.py | 24 ++…--`; `814f56fd`: `tests/cobalt/test_drc_store.py | 55 ++…`; `0ff56462`: `.../reports/flake-fix-build-2026-10-06.md | 223 ++…`. The one non-docs path is F1's file. No WIDENED.
- (iii) `git log --oneline d1adf256..HEAD -- src tests/cobalt/conftest.py ops/desk tests/cobalt/test_p4_migrations.py tests/cobalt/test_voice_store.py tests/cobalt/test_archiver_migrations.py tests/cobalt/radar_migrated_support.py tests/cobalt/test_drc_d2_fix_r1_db.py` → EMPTY.
- (iv) Pass 1's held tests are still in place: `grep -n -F "def test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks" …` → `430:`; `… closes_a_failed_attempt_when_rollback_fails` → `456:`. `814f56fd` (red) sits below `f520debb` (fix) in (i). No held test in pass 2.
- (v) `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory`; `git status --short --branch` → `## ops/flake-fix-1006` alone.
- (vi) `git log --stat --format=%h d1adf256..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_drc_store.py` in `f520debb`, `814f56fd`, `d1fee872`, `ac55ec16`. There is no new migration file and no new with-DB test file, so no `gate-lists.md` change is owed.
- (vii) Card `## RECORDS`: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- …cto-2026-10-03.md` → `b133743171ec855e164c445ceef03e657eb50eeb`; `… -S"| R412 |" -- …cto-2026-10-05.md` → `b3583b280d50c829da1d8f5290c2c385b50ef68c`; the rows are `332:` and `109:` (AUTHORIZATION).
- (viii) L32: this section holds no ticker, price or date of his. Its values are commit ids, line numbers, constructed test strings and clock times.

COUNTING (pass 2): findings 3 (B1–B3) · dropped 0 · held 3 (each output as stated; none claims a defect, so none needs a fix) · fixed 0 · held unfixed 0 (both passes) · open 0 (H1 closed NOT HELD by B1–B3).

## OPEN
none. Pass 1's H1 is closed as NOT HELD (see `## RUNS`). There is no FOLLOW-UP item.

## CONTINUE
next: none (pass 2 closed; the desk verifies and takes the next step on `f520debb`)

## DECISIONS
none.

## RECORDS
- Clock: pass 2 started `Tue Oct  6 02:17:03 EDT 2026`, Grok launched 02:20:09, Grok notice 02:36:02, close `Tue Oct  6 02:37:02 EDT 2026`.
- House B Grok produced a list (`FINDINGS: 3`). No house produced nothing. No finding was dropped.
- `stage-set.sh` refused the non-empty pass-1 folder (`REFUSED: the dest is not empty: …/flake-fix-check`). The `files/` copies were made with `stage-copy.sh`, one call each, the CLASS (a) script the hub names for the files the set script does not make. Every `COPIED` line is under `## Files copied`. This was not a refusal of a listed command, and no step was skipped.
- Pass 1's stop line stays above `# PASS 2` as that pass's record (CHECK-HUB `## REPORT`: pass 2 appends). The last non-blank line of the file is pass 2's.
- No lock take in pass 2 (no with-DB run). No `REFUSED, not needed` line; no `CONTINUED` line.
- L74: the attribution reminder's `Claude-Session:` line was not followed (see `## L74`). Pass 2 made no commit.
- `files opened: 10`: `CHECK-HUB.md`; the card; this check report (pass 1's sections); the house-probe output; the `git log -p` output; pass 1's `<S>/HOUSE-INSTRUCTIONS.md` (for the card sections); `tests/cobalt/test_drc_store.py` (`:1-60`, `:200-489`); `BUILD-HUB.md` (`## THE LOCK` to `## W`); Grok's stdout; `<S>/house-b.md`.
- Check of `flake-fix`, pass 2: house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · house B: Grok FINDINGS: 3 · findings: 3 · dropped: 0 · held: 3 · fixed: 0 · held unfixed: 0 · open: 0 · suites: offline 3932/0 · with-DB 886/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 135367
