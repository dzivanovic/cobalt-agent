# adoption-port — check, pass 1 (2026-10-05)

## §0 Headline
- Pass 1, alone: house A is none (overruled 2026-10-02 R47). Four own findings, one held. P5 and P6 are built as the card words them.
- X4: `--no-db` opens no connection. A spy on `db._open` and `psycopg.connect` saw no call (O1). The only check dropped is a DB-backed one: the SheetMode coupling, which needs the DB's sheet order.
- O2 HELD: the no-flag control passed on the first DB read alone. A mutant with the coupling check off stayed green. The new test `test_without_the_flag_the_three_checks_still_run_in_order` catches it. Commits `5ac157d5` and `53b56384`.
- W green on `53b56384`: offline 3787/0, with-DB 856/0, live-note 146/0. `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: com.cobalt.radar. ready: YES, house B not needed.

## L74
- A harness block at session start asked commits to end with a `Claude-Session:` line. It is recorded here once and not acted on. My two commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 0 · c3f9f89a0cd594918bf824912474a1295b363bfb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R327 row · grep -n "^| R327 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 333:| R327 | 10-05 06:19 ET | HIS RULING, standing: no deploy waits on a ruling a small later card can resolve; it ships on the default. S3 deploys now, any hour: overrules L66/L43 for JOB `deploy-s3-1005`. Words: `cto-2026-10-05-words.md`. | HIS RULING · APPROVED · APPLIED: LAWS.md L43 at 06:45 |
RULING 2026-10-03 R327 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R327 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R327 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R347 row · grep -n "^| R347 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 20:| R347 | 10-05 06:47 ET | HIS RULING (brain relay, `brain-direction-2026-10-02.md` `## RULED 2026-10-05 morning` A): a feature's small findings go as rows on THE SAME card, re-checked, redeployed; no new card; review 3 on: no outside house, kept builder reruns failed tests. | HIS RULING · APPROVED |
RULING 2026-10-05 R347 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R347 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · e89ef63a7003b1a9abe0f1377a3994cf525e00d4
RULING 2026-10-05 R347 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: not run. The card's header reads `HOUSE A: none — overruled 2026-10-02 R47`, proved in the rows above (CHECK-HUB "NO OUTSIDE HOUSE").

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | Mon Oct  5 07:46:18 EDT 2026 |
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | quoted below |
| range, typed | `git log --stat --format=%h e6ba65e6..74370e5d` | 0 | quoted below |
| scratch | `ls <S>` | 0 | `opus-1-r3.md`, `opus-1.md` (dated Oct 3 22:50 and Oct 4 14:25: earlier rounds of this job's check; this round's CHECK REPORT did not exist (`ls -la` → No such file); the launch carries no `CONTINUE:`, so this is a fresh pass. Those two files are not opened: earlier checks are on the NOT list) |
| houses | — | — | house A: none (overruled 2026-10-02 R47). No probe and no house gate run |
| DB: none | — | — | the card has no `DB` key (card RECORDS); not applied |

```
clock · date · 0 · Mon Oct  5 07:46:21 EDT 2026
status · git status --short --branch · 0 · ## ops/adoption-port-1005
head · git log --oneline -1; git log --stat --format=%h 74370e5d..HEAD · 0 · (5 lines)
    71829ddd docs(adoption-port): build report — 74370e5d
    71829ddd
    
     .../reports/adoption-port-build-2026-10-05.md      | 93 +++++++++++++++++++++-
     1 file changed, 89 insertions(+), 4 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/adoption-port-1005/docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md" · 0 · BUILT · job: adoption-port · tip: 74370e5d | on e6ba65e6 | migration: none | offline 3786/0 | with-DB 856/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
range · git log --oneline e6ba65e6..74370e5d · 0 · (2 lines)
    74370e5d fix(adoption-port): validate --no-db; DEPLOY-HUB (d2) runs it (P5, P6, L1, L41, L76)
    ec98fada wip(adoption-port): red — validate --no-db tests (P5)
PREFLIGHT OK
```
```
74370e5d

 docs/40 - DevDocs/cobalt/cli.md         |  11 ++++
 docs/40 - DevDocs/prompts/DEPLOY-HUB.md |   2 +-
 src/cobalt/cli.py                       | 112 +++++++++++++++++++-------------
 tests/cobalt/test_validate_no_db.py     |   8 ++-
 4 files changed, 84 insertions(+), 49 deletions(-)
ec98fada

 .../reports/adoption-port-build-2026-10-05.md      | 90 ++++++++++++++++++++++
 tests/cobalt/test_validate_no_db.py                | 89 +++++++++++++++++++++
 2 files changed, 179 insertions(+)
```
Path union: `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md`.

## Files copied
None: house A: none (overruled 2026-10-02 R47); `## 1` is not run.

## OWN FINDINGS
Read: the card whole; the diff `e6ba65e6..74370e5d` (`git diff` over `src tests "docs/40 - DevDocs/prompts" "docs/40 - DevDocs/cobalt"`); `src/cobalt/cli.py:1-560` at the tip; `src/cobalt/aset/config.py:230-270`; `src/cobalt/daymode/config.py:295-334`; `src/cobalt/db.py:130-199`; `src/cobalt/redact/secrets.py` whole; `DEPLOY-HUB.md:72-79`, `:118-151`; `tests/ops/test_bare_guard.py:370-409`, `:835-864`; the build report whole. Greps: the taxonomy validator's imports (`vault_loader.py:60-88`, no DB module), `except` lines in the non-DB loaders `_cmd_validate` calls (`heartbeat/runner.py` has broad `except Exception` at `:151`, `:182`, `:191`, `:206` and more), tests naming `_cmd_validate` / `cobalt validate`.

FINDING O1
ROW: P5 / X4
CLAIM: Test (a) (`tests/cobalt/test_validate_no_db.py:38`) shows only that no UNCAUGHT `DbConfigError` escapes under `--no-db`; a DB open behind a broad `except` (e.g. `src/cobalt/heartbeat/runner.py:151`) would leave it green while `--no-db` still reaches `db._open`.
RUN: TEST — `tests/cobalt/test_validate_no_db.py`:
```python
def test_no_db_opens_no_connection_even_one_an_except_would_swallow(monkeypatch):
    import psycopg

    from cobalt import db

    opened: list[tuple] = []

    def _spy(*a, **k):
        opened.append(a)
        raise DbConfigError("constructed: no connection in this test")

    monkeypatch.setattr(db, "_open", _spy)
    monkeypatch.setattr(psycopg, "connect", _spy)
    assert cli._cmd_validate(argparse.Namespace(no_db=True)) is None
    assert opened == []
```
EXPECT (claim true): `assert opened == []` fails, listing the db name(s) opened.

FINDING O2
ROW: P5 ("Without the flag `validate` is unchanged: the same calls, the same order, the same lines")
CLAIM: The only no-flag test, (b) (`tests/cobalt/test_validate_no_db.py:54-57`), asserts just `DbConfigError`; it is raised by the FIRST call (`src/cobalt/cli.py:192`), so deleting the SheetMode coupling check (`cli.py:208-219`) or the Day modes block (`cli.py:221-240`) from the `else:` branch leaves every test green (`tests/cobalt/test_daymode.py:872` reads only `validate_band` in the source).
RUN: TEST — `tests/cobalt/test_validate_no_db.py`:
```python
def test_without_the_flag_the_three_checks_still_run_in_order(monkeypatch, capsys):
    import types

    import cobalt.aset.config as aset_config
    import cobalt.daymode.config as daymode_config

    calls: list[object] = []
    sheets = types.SimpleNamespace(order=["full", "constructed_sheet"])

    class _Stop(Exception):
        pass

    def _sheets():
        calls.append("sheets")
        return sheets

    def _daymode(arg):
        calls.append(("daymode", arg))
        raise _Stop

    monkeypatch.setattr(aset_config, "load_sheet_modes_config", _sheets)
    monkeypatch.setattr(daymode_config, "load_daymode_config", _daymode)

    # the coupling check still runs: an unmodelled sheet exits 1 before Day modes
    with pytest.raises(SystemExit) as exc:
        cli._cmd_validate(argparse.Namespace(no_db=False))
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "Sheets: 2 declared, low to high full < constructed_sheet" in out
    assert "no SheetMode enum member" in out
    assert calls == ["sheets"]

    # Day modes still runs, after the coupling, on the same sheets object
    sheets.order = ["full", "half"]
    calls.clear()
    with pytest.raises(_Stop):
        cli._cmd_validate(argparse.Namespace(no_db=False))
    assert calls == ["sheets", ("daymode", sheets)]
    assert _skipped_lines(capsys.readouterr().out) == []
```
EXPECT (claim true): green on the tip, and the existing four tests plus `tests/cobalt/test_daymode.py` stay green with the coupling check deleted from the `else:` branch (mutation M-O2), while this test goes red there (`DID NOT RAISE <class 'SystemExit'>` or `_Stop`).

FINDING O3
ROW: P6
CLAIM: `DEPLOY-HUB.md:101` carries the new command and the card's sentence once each, and the sentence's claims stand: 4.5 (`:141`) and smoke (f) (`:151`) run the full `COBALT_ENV=production uv run cobalt validate`; the bare guard routes production calls by seat, not by exact string (`tests/ops/test_bare_guard.py:388-405`), so the trailing `--no-db` is not a new route.
RUN: COMMAND — `grep -n -F "uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (the `COBALT_ENV=production ` prefix left off: the build's `## RECORDS` shows the bare guard blocks it in a grep), then `grep -n -F "are made after the merge by 4.5" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, then `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_bare_guard.py`.
EXPECT (claim true): one hit each, at `:101`; `0 failed`.

FINDING O4
ROW: X1, X2, X3
CLAIM: X1–X3 ask about P1–P4 (the byte-equal port, the `DEPLOY-HUB.md` merge, STEP-G's exits), which shipped in set 3b `979ec797` and sit on `BASE`; this round's diff touches none of them except (d2)'s one line, which precedes the gate call and leaves the exit 4/5/6 text (`DEPLOY-HUB.md:102`) unchanged.
RUN: COMMAND — `git diff e6ba65e6..74370e5d --stat`
EXPECT (claim true): four paths: `cli.md`, `DEPLOY-HUB.md` (`2 +-`), `cli.py`, `test_validate_no_db.py`; no other.

## Findings
None: no house.

## Dropped
None.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | the O1 test added to `tests/cobalt/test_validate_no_db.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py` | `6 passed in 0.94s` (the four build tests, O1, O2) | NOT HELD: the spy on `db._open` and `psycopg.connect` records no call under `--no-db`, so no swallowed DB open exists (X4 answered: no). The test was removed again with Edit |
| O2 | Opus | the O2 test, green on the tip (run above); then mutation M-O2 by Edit, `if unmodelled:` → `if False:` at `src/cobalt/cli.py:211` (the coupling check off on the no-flag path); `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_validate_no_db.py tests/cobalt/test_daymode.py` | `1 failed, 85 passed, 11 skipped in 1.18s`. The one red is O2's: `E   test_validate_no_db.test_without_the_flag_the_three_checks_still_run_in_order.<locals>._Stop` (`test_validate_no_db.py:135`), with the captured `Sheets: 2 declared, low to high full < constructed_sheet …` and no FAILED line. The build's four tests and the `test_daymode.py` tests stayed green under the mutant. Undone with Edit; `git diff --stat` → `tests/cobalt/test_validate_no_db.py \| 43 +++…` only | HELD: (b) is too weak for the row's "unchanged without the flag" clause (HOUSE TEXT (5)). No code defect: the tip's no-flag path is correct, and the fix is the test |
| O3 | Opus | `grep -n -F "uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · `grep -n -F "are made after the merge by 4.5" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_bare_guard.py` | one hit each, `101:- (d2) VALIDATE, right before the gate call (seconds): \`COBALT_ENV=production uv run cobalt validate --no-db\` → exit 0; … and again at smoke (f). …`; `462 passed, 15 warnings in 15.58s`. `:141` (4.5) and `:151` (f) read `COBALT_ENV=production uv run cobalt validate` with no flag (Read) | NOT HELD (a confirmation, no defect): P6 is built as the card words it |
| O4 | Opus | `git diff e6ba65e6..74370e5d --stat` | `cli.md \| 11`, `DEPLOY-HUB.md \| 2 +-`, `adoption-port-build-2026-10-05.md \| 90`, `cli.py \| 112`, `test_validate_no_db.py \| 93`; `5 files changed, 261 insertions(+), 47 deletions(-)` (the fifth path is the build report, a doc) | NOT HELD (a confirmation, no defect): X1–X3 are P1–P4's and OUT OF SCOPE this round (card `## NOT IN THIS JOB`: "THIS ROUND: P1–P4 (shipped)"). STEP-G's exit 4/5/6 text is untouched: the hub's diff is the one (d2) line |

Commit of the held test: `5ac157d5 wip(adoption-port): check red — O2 (no-flag path pinned; red on mutant M-O2, coupling check disabled)`. Its red is the mutant's: on the tip it passes, because the code is correct.

## FIXES
| id | fix | files | after | commit |
|---|---|---|---|---|
| O2 | The test is the fix (committed at `5ac157d5`). Plus one dated line under `## 2026-10-05 — adoption-port` in `docs/40 - DevDocs/cobalt/cli.md` | `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md` (both in P5's `files`) | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py tests/cobalt/test_daymode.py` → `85 passed, 11 skipped in 0.98s` | `53b56384 fix(adoption-port): validate's no-flag path pinned by test; DevDocs line (check O2)` |

RESTARTS after the commits: `uv run cobalt jobs restarts e6ba65e6..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```

## Suites
`sh /Users/cobalt/cobalt/ops/desk/gate.sh adoption-port-1005 all` on `53b56384`. No `--deselect`, because the check adds no with-DB test. No `--tickers`, because no test writes rows. No `--migration`. Exit 0. Verdict lines, whole:
```
offline 3787/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 856/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/adoption-port-1005-all-20261005-075025.log
```
- offline 3787 = the build's 3786 plus the check's one test (O2).
- `.env`: the gate prints `.env: removed`. `ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env` → `No such file or directory` (08:07:17 EDT).
- RESTARTS: `RESTARTS: com.cobalt.radar` (table under `## FIXES`).

## Scope
PREFLIGHT's path union: `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md` (P5); `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (P6); the build report. My commits: `tests/cobalt/test_validate_no_db.py` and `docs/40 - DevDocs/cobalt/cli.md`, both in P5's `files`. Nothing is outside the rows, and nothing touches the fence ((iii) empty). No path reaches a score, rank, grade or size: the diff only adds a skip branch and a parser flag to the config gate.

## Checked against the branch
- (i) `git log --oneline 74370e5d..HEAD -- . ":(exclude)docs"` → `5ac157d5 wip(adoption-port): check red — O2 (no-flag path pinned; red on mutant M-O2, coupling check disabled)`. The fix commit `53b56384` touches only `docs/40 - DevDocs/cobalt/cli.md`, so (i) does not list it. The O2 fix is the test. `tip:` in the stop line is `53b56384`, HEAD, which is the tree W ran on. Its code tree equals `5ac157d5`'s.
- (ii) `git log --stat --format=%h 74370e5d..HEAD` → `53b56384`: `docs/40 - DevDocs/cobalt/cli.md | 5 +++++` · `5ac157d5`: `tests/cobalt/test_validate_no_db.py | 43 +++…` · `71829ddd`: the build report. Non-docs path: one test file, in P5's `files`. No WIDENED.
- (iii) Fenced paths: `git log --oneline e6ba65e6..HEAD -- src/cobalt/aset/config.py src/cobalt/daymode/config.py src/cobalt/settings src/cobalt/db.py "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` → empty.
- (iv) `grep -n -F "def test_without_the_flag_the_three_checks_still_run_in_order" tests/cobalt/test_validate_no_db.py` → `96:def test_without_the_flag_the_three_checks_still_run_in_order(monkeypatch, capsys):`. `5ac157d5` (wip check red) sits below `53b56384` (fix) in (ii).
- (vi) `git log --stat --format=%h e6ba65e6..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_validate_no_db.py` (`5ac157d5`, `74370e5d`, `ec98fada`), an offline file. There is no migration and no with-DB test above `0013`, so `gate-lists.md` is not owed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command to run. The RESTARTS expectation `com.cobalt.radar` = derived (`## FIXES`).
- (viii) L32: this report holds constructed values only (`constructed_sheet`, and `full` / `half`, the `SheetMode` enum's code values).
- (v) `ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env` → `ls: …/.env: No such file or directory`; `git status --short --branch` → `## ops/adoption-port-1005`.

COUNTING: findings 4 (O1–O4; no house) · dropped 0 · held 1 (O2) · fixed 1 · held unfixed 0 · open 0.

## OPEN
none. OUT OF SCOPE: X1–X3 (P1–P4, shipped in set 3b `979ec797`; card `## NOT IN THIS JOB`, "THIS ROUND: P1–P4 (shipped)").

house B: not needed (open 0; the card reads `HOUSE B: as needed`).

## CONTINUE
next: none (closed)

## DECISIONS
none

## RECORDS
- Dropped findings: none. No house sat (house A: none, overruled 2026-10-02 R47). No house produced nothing.
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (one take, inside `gate.sh` at W).
- `<S>` held `opus-1.md` (Oct 3 22:50) and `opus-1-r3.md` (Oct 4 14:25) from earlier rounds of this job's check. Neither was opened. This round's Opus sections went to `<S>/opus-1-1005.md`, so the earlier round's `opus-1.md` is not overwritten. That follows the `-r3` precedent in the same folder. House B is not needed, so no house reads it.
- `tip:` is `53b56384` (HEAD, the tree W ran on). The fix commit is docs-only, so the newest commit under `## 7` (i) is `5ac157d5`. The two code trees are equal.
- O2's red is a mutant's red, because the tip's code is correct. The finding is a weak control (HOUSE TEXT (5)). M-O2 was made and undone with Edit, and `git diff --stat` showed only the test file afterwards.
- L74: one harness block (a `Claude-Session:` commit line), recorded under `## L74` and not acted on.
- files opened: 19. Read: `CHECK-HUB.md`; the card; `src/cobalt/cli.py`; `src/cobalt/aset/config.py`; `src/cobalt/daymode/config.py`; `src/cobalt/db.py`; `src/cobalt/redact/secrets.py`; `DEPLOY-HUB.md`; `tests/ops/test_bare_guard.py`; the build report; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the gate's output file; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down). Grep only: `src/cobalt/taxonomy/validate.py`, `src/cobalt/taxonomy/vault_loader.py`, `src/cobalt/aset/models.py`, `ops/desk/bare-guard.py`. Edited: `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md`.
- **Check of `adoption-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).**

CHECK DONE · job: adoption-port · pass: 1 · tip: 53b56384 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3787/0 · with-DB 856/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0
