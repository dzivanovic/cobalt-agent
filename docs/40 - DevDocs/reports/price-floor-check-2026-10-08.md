# price-floor-1008 — check report (2026-10-08)

## §0 Headline
- Checked `price-floor-1008` (`059da441..f105b82e`); house A Sol `FINDINGS: 2`, house B Grok `FINDINGS: 0`, my own read 1.
- HELD and FIXED: O1 — a row at or below the floor, read before its source failed on a later row, stayed a candidate; `runner.py` now floors each price as the row is read (`7d0ce9ec` red, `e34ad12c` fix).
- REJECTED, OPEN: A1 (rollback leaves a never-admitted `price_floor` row invalid — the card's row M specifies that rollback), A2 (DevDocs pages — required by the hub).
- Gate on `e34ad12c`: offline 4023/0 · with-DB 4910/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS `com.cobalt.aset com.cobalt.radar`. ready: YES.

## L74
A system reminder in this session asked that commits end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md"` · exit 0 · whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 0 · 76979452f6bc4de5701e8596d1486e4e3172ba96
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R692 row · grep -n "^| R692 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 45:| R692 | 11:53 ET | HIS RULING (words R692): global $5 price floor after lists are gathered, not in Finviz filters; brain specs it; built with in-flight fixes; desk tells him when S3 smoke can resume. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW at 11:55 ET (LAWS fold at the close) |
RULING 2026-10-08 R692 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R692 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 510ee1dad54dfa6e213184a52470bfd968931f1d
RULING 2026-10-08 R692 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
- House gate R17 · `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row).
- House gate R19 · `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row).
- R19 committed · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
- THE MECHANICAL ROWS · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · 0 · whole:
```
clock · date · 0 · Thu Oct  8 13:50:56 EDT 2026
status · git status --short --branch · 0 · ## ops/price-floor-1008
head · git log --oneline -1; git log --stat --format=%h f105b82e..HEAD · 0 · (5 lines)
    208dd2a7 docs(price-floor-1008): build report — f105b82e
    208dd2a7
    
     .../reports/price-floor-build-2026-10-08.md        | 227 +++++++++++++++++++++
     1 file changed, 227 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/price-floor-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/price-floor-1008/docs/40 - DevDocs/reports/price-floor-build-2026-10-08.md" · 0 · BUILT · job: price-floor-1008 · tip: f105b82e | on 059da441 | migration: 0023, rolled back | offline 4022/0 | with-DB 4909/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 397831
range · git log --oneline 059da441..f105b82e · 0 · (2 lines)
    f105b82e feat(price-floor-1008): the radar's price floor — once after every source, admitted members leave as price_floor, WATCH cards expire, floor in radar.yaml, 0023 (M, F1, F2, F5, F3, F4; L1, L3, L32, L76)
    e0713d36 wip(price-floor-1008): red — price floor tests and the 0023 order pins (M, F1-F5)
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 059da441..f105b82e` · 0 · two commits: `f105b82e` (33 files: `configs/cobalt/radar.yaml`, 10 DevDocs pages, `ops/desk/gate-lists.md`, `0023_radar_price_floor.sql` + rollback, `db_migrations/__init__.py`, `placement.py`, `radar/audit_export.py`, `config.py`, `evaluate_cli.py`, `handicap_dry_run.py`, `models.py`, `runner.py`, `store.py`, `replay/runner.py`, tests `test_radar_collector.py`, `test_radar_daily.py`, `test_radar_evaluate_cli.py`, `test_radar_handicap_group.py`, `test_radar_replay.py`, `test_radar_runner.py`, `test_replay_formations.py`, `test_replay_runner.py`, fixture `screen-handicap.real-shape.csv`); `e0713d36` (19 test files: the 16 order pins, `test_radar_config.py`, `test_radar_price_floor.py`, `test_radar_price_floor_db.py`). Path union recorded for `## Scope`.
- `ls <S>` · 1 · `No such file or directory` → fresh.
- self-check count in the build's last line: `3 of 3`.
- HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` (background) · 0 · whole: `sol: UP` / `grok: UP` / `gemini: UP`. → **house A: OpenAI Sol · house B: Grok**. Card `HOUSE B: as needed` (not mandatory).
- House gates re-run at 13:53 ET before the launch: R17 row `35:`, R19 row `37:` (one each).
- Houses started 13:53:46 ET (`date`), from `/Users/cobalt/cobalt-wt/agy-trial`: Sol (task `b349qcsf8`), Grok (task `bao1b1zip`), each `run_in_background`, `timeout` 2700000; return `cd`, `git status --short --branch` → `## ops/price-floor-1008`.

## Files copied
- `sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · last line `STAGED 56 files · 895928 bytes · commits 2` (commits = PREFLIGHT's 2). Per-file lines (bytes · dest under `<S>`): `105490 diff.md` · `36149 files/137-price-floor-card.md` · `38919 files/price-floor-build-2026-10-08.md` · `387 rulings.md` · under `files/wt/`: `1865 configs/cobalt/radar.yaml`, ten DevDocs pages (`18753 db_migrations/__init__.md`, `4413 placement.md`, `5558 radar/audit_export.md`, `2987 radar/config.md`, `6193 radar/evaluate_cli.md`, `2397 radar/handicap_dry_run.md`, `1776 radar/models.md`, `4670 radar/runner.md`, `4237 radar/store.md`, `8534 replay/runner.md`), `6485 ops/desk/gate-lists.md`, `1016 0023_radar_price_floor.rollback.sql`, `2195 0023_radar_price_floor.sql`, `11249 db_migrations/__init__.py`, `8415 placement.py`, `22831 radar/audit_export.py`, `8887 radar/config.py`, `21522 radar/evaluate_cli.py`, `22777 radar/handicap_dry_run.py`, `8444 radar/models.py`, `31203 radar/runner.py`, `24574 radar/store.py`, `26796 replay/runner.py`, tests `27273 test_archiver_migrations.py`, `14743 test_assumed_store.py`, `28678 test_drc_d2_fix_r1_db.py`, `4477 test_drc_d3_experiments.py`, `28790 test_drc_k1_store.py`, `25476 test_drc_store.py`, `6573 test_f15_p1_records_offline.py`, `4294 test_legs_migration.py`, `28345 test_p4_migrations.py`, `3917 test_radar_collector.py`, `10367 test_radar_config.py`, `11859 test_radar_daily.py`, `14214 test_radar_evaluate_cli.py`, `11682 test_radar_handicap_group.py`, `11357 test_radar_handicap_store.py`, `4973 test_radar_migration.py`, `17442 test_radar_price_floor.py`, `6695 test_radar_price_floor_db.py`, `19613 test_radar_replay.py`, `17858 test_radar_runner.py`, `23723 test_radar_score_migration.py`, `20754 test_replay_formations.py`, `49372 test_replay_runner.py`, `1738 test_seam_drc_s3_registry.py`, `11580 test_stale_score_db.py`, `31097 test_tenancy.py`, `12602 test_voice_store.py`, `7714 tests/fixtures/radar/screen-handicap.real-shape.csv`.
- `stage-copy.sh`, each `COPIED <bytes> <dest>`: `4243 files/price-floor-answer-2026-10-08.md`; `20664 files/wt/src/cobalt/radar/pool.py`; `75264 files/wt/src/cobalt/cards/store.py`; `10433 files/wt/src/cobalt/cards/models.py`; `3315 files/wt/src/cobalt/db_migrations/0004_radar_pool.sql`; `9317 …/0006_radar_score.sql`; `966 …/0020_drc_build_kinds.sql`; `745 …/0020_drc_build_kinds.rollback.sql`; `30657 files/wt/src/cobalt/replay/movers.py`.
- `<S>/HOUSE-INSTRUCTIONS.md` (Write): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph. Sol reads the same `diff.md` / `rulings.md` the script wrote from git.

## OWN FINDINGS
Written before either house list was opened. Read: the card whole, the build report whole, `git diff 059da441 f105b82e -- src configs ops` whole, `tests/cobalt/test_radar_price_floor.py` whole, `src/cobalt/radar/runner.py:110`–`:190` at the tip, `cards/store.py:240`–`:279`, `:960`–`:1045`, `radar/evaluate.py` `OpenRadarCard` (`:1268`–`:1287`), `replay/models.py:415`–`:444`, `radar/store.py:312`–`:351`, `cards/picks.py:176`–`:188`; greps of `members_for_day(` over `src`, `radar_membership` over `src/cobalt/**/*.py`, `price_floor|5.00` over `src/cobalt/radar`.

FINDING O1
ROW: F1 (X1)
CLAIM: In `_collect` a row's ticker is appended to `candidates` as it is read (`src/cobalt/radar/runner.py:167`), but its price reaches the scan's `prices` only after the whole source finished (`:173`–`:175`); a source that raises after reading a row at or below the floor leaves that ticker a candidate with `excluded_by` None, never floored.
RUN: TEST — `tests/cobalt/test_radar_price_floor.py`
```python
def test_a_floored_row_read_before_its_source_fails_is_still_removed():
    """X1: the screen reads PFXA at 4.00, then fails on a malformed row;
    the price already read still floors PFXA."""
    runner = _runner(Collector(screen=[_row("PFXA", "4.00"), {"Volume": "2"}]))
    candidates, source_sets = _collect(runner)
    assert "PFXA" not in {c.ticker for c in candidates}
    assert "PFXA" not in _seen(source_sets)
```
EXPECT: on the tip `AssertionError: assert 'PFXA' not in {'PFXA'}` at the first assert.

No other finding: the `card_store` read (`OpenRadarCard.card_id`, `.ticker`, `.state: str`, `evaluate.py:1271`–`:1275`) and `transition`'s keywords (`cards/store.py:248`–`:260`) match the runner's call; `Episode.excluded_by` is `Optional[str]` (`replay/models.py:429`), so `price_floor` rows reach `replay/runner.py:403` without a validation error; the only default `members_for_day` caller is `aset/radar_panel.py:616`; `src/cobalt/radar` holds no floor literal.

## Findings
Both houses finished: Sol at 14:00:06 ET (notice; `date`), Grok at 14:07:21 ET. `ls -la <S>` at 14:07: `diff.md`, `files/`, `house-b.md` (12 bytes), `HOUSE-INSTRUCTIONS.md`, `rulings.md`. House A's `house-a.md` written by me from Sol's FINAL message (output lines `:21774`–`:21804`, its `FINDINGS: 2`). House B's `house-b.md` written by Grok: `FINDINGS: 0` (its stdout ends with the path, exit 0).
THE DROP (each `RUN:` line followed by a `def test_` or one allowed command): none dropped.
- O1 · Opus · F1 (X1) · a row read at or below the floor before its source raises stays a candidate: its price is merged into `prices` only after the source finishes · TEST
- A1 · Sol · X7 · the rollback clears only admitted `price_floor` rows, so a never-admitted `price_floor` row makes the four-value CHECK fail · TEST (with-DB)
- A2 · Sol · SCOPE · the ten DevDocs pages the build changed sit in no row's `files` · COMMAND

## Dropped
none.

## RUNS
id · source · run · output · verdict
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_price_floor.py::test_a_floored_row_read_before_its_source_fails_is_still_removed` (test pasted as written) · `1 failed in 0.16s`; `E       AssertionError: assert 'PFXA' not in {'PFXA'}` at `tests/cobalt/test_radar_price_floor.py:232`; stderr `radar source screen:example_session_scan@b0a9859197ba failed: 'Ticker'` · **HELD**
- A1 · Sol · with-DB, ONE lock take (`take-devdb-lock.sh price-floor-1008 90` → `lock taken: price-floor-1008`, 14:21:07 ET; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's; `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` = F0); `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_price_floor_db.py::test_0023_rollback_handles_every_schema_valid_price_floor_row` (pasted as written) · `1 failed in 0.23s`; `psycopg.errors.CheckViolation: check constraint "radar_membership_excluded_by_check" of relation "radar_membership" is violated by some row` at `_apply(conn, [ROLLBACK])` (`:155`); `0001`…`0023` applied inside the test's own transaction; `<FP>` after → `664 35 272c95bbb12241e3611e4b36326ccf87` = F0; `release-devdb-lock.sh price-floor-1008` → `lock released`; `ls …/.env` → `No such file or directory` (14:21:27 ET) · **REJECTED — row M: "ROLLBACK … `UPDATE system.radar_membership SET excluded_by = NULL WHERE excluded_by = 'price_floor' AND entered_at IS NOT NULL` … Only admitted rows ever carry `price_floor` (row F2)"** — the card specifies this rollback; the never-admitted `price_floor` row is one no production path writes (F2, X3). Test removed again with Edit; OPEN.
- A2 · Sol · `git diff --name-only 059da441..f105b82e -- "docs/40 - DevDocs/cobalt"` · the ten pages exactly as its EXPECT lists · **REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"** (and `CHECK-HUB.md` `## 7` (ii) scopes only non-docs paths): the pages are required by the hub. OPEN.
- HELD test committed: `7d0ce9ec wip(price-floor-1008): check red — O1` (`tests/cobalt/test_radar_price_floor.py` only).

## FIXES
- O1 · `src/cobalt/radar/runner.py` `_collect`: the per-source `source_prices` map and its after-the-source merge are gone; each row's `_price` goes into the scan's `prices` as the row is read, before `candidates[ticker].append`. DevDocs: `docs/40 - DevDocs/cobalt/radar/runner.md` `## 2026-10-08 — price-floor-1008 check`. After the fix: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_price_floor.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_config.py tests/cobalt/test_radar_price_floor_db.py tests/cobalt/test_radar_replay.py tests/cobalt/test_radar_handicap_group.py tests/cobalt/test_radar_handicap_dead.py tests/cobalt/test_radar_handicap_dry_run.py tests/cobalt/test_radar_evaluate.py` → `155 passed, 5 skipped in 8.52s` (0 failed). Commit `e34ad12c fix(price-floor-1008): a row's price floors it as it is read, before a later row can fail its source (check O1)`.

## Suites
RESTARTS first (`BUILD-HUB.md` `## RESTARTS`): `uv run cobalt jobs restarts 059da441..HEAD` · 0 · the table's rows equal the build's (`## RESTARTS` of the build report) plus nothing new (my commits touch `src/cobalt/radar/runner.py` `static import reach com.cobalt.aset,com.cobalt.radar`, `docs/…/radar/runner.md` `DOCS`, and a `tests/` path); no `UNCLASSIFIED` row; last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.
W on `<tip now>` = `e34ad12c`, ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh price-floor-1008 all --deploy --deselect tests/cobalt/test_radar_price_floor_db.py --tickers PFLA,PFL0,PFL1,PFL2,PFL3,PFLB,PFLR,PFLS,PFLT,PFLU,PFDA,PFDB,PFDC --migration` (background), exit 0, completed 14:58 ET. Verdict lines whole:
```
offline 4023/0
lock: waited 7 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (PFLA,PFL0,PFL1,PFL2,PFL3,PFLB,PFLR,PFLS,PFLT,PFLU,PFDA,PFDB,PFDC)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4910/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/price-floor-1008-all-20261008-142216.log
```
- Log reads (`grep -n -F`): `:866` offline `4023 passed, 790 skipped, 1 xfailed` (the build's 4022 + O1's test); `:938` pass 1 `pass 1: whole (deploy)` command ends `--deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_radar_price_floor_db.py`; `:1091` `4715 passed, 7 skipped, 89 deselected, 3 xfailed` → d1 = 4715; `:1093` `dev forward: APPLIED 14:53:02`; `:1897` pass 2 `195 passed, 1 deselected` → d2 = 195; d1 + d2 = 4910; this build's with-DB ids PASSED at `:1891`–`:1896` (the six `test_radar_price_floor_db.py` tests). `grep -c -F "OUTSIDE the allowed set"` → `0`.
- `.env`: `ls /Users/cobalt/cobalt-wt/price-floor-1008/.env` → `No such file or directory` (14:58 ET); `git status --short --branch` → `## ops/price-floor-1008`.

## Scope
PREFLIGHT's path union (two build commits, `## PREFLIGHT` THE RANGE) plus my two commits: `tests/cobalt/test_radar_price_floor.py` (row F1/F2/F3/F4/F5's test file), `src/cobalt/radar/runner.py` (rows F1, F2, F3), `docs/40 - DevDocs/cobalt/radar/runner.md` (its DevDocs page). Every path inside a row's `files`, a test file, or DevDocs. Nothing under `## NOT IN THIS JOB`.

## Checked against the branch
- (i) `git log --oneline f105b82e..HEAD -- . ":(exclude)docs"` → `e34ad12c fix(price-floor-1008): a row's price floors it as it is read, before a later row can fail its source (check O1)` / `7d0ce9ec wip(price-floor-1008): check red — O1`. `<tip now>` = `e34ad12c`.
- (ii) `git log --stat --format=%h f105b82e..HEAD` → `e34ad12c`: `docs/40 - DevDocs/cobalt/radar/runner.md`, `src/cobalt/radar/runner.py`; `7d0ce9ec`: `tests/cobalt/test_radar_price_floor.py`; `208dd2a7`: the build report. Non-docs paths: `runner.py` (rows F1/F2/F3 `files`), the test file. No WIDENED.
- (iii) `git log --oneline 059da441..HEAD -- src/cobalt/radar/pool.py src/cobalt/aset/radar_panel.py src/cobalt/aset/web.py src/cobalt/cards/store.py src/cobalt/cards/models.py src/cobalt/replay/movers.py src/cobalt/dayopen/checks.py` → empty.
- (iv) `grep -n -F "def test_a_floored_row_read_before_its_source_fails_is_still_removed" tests/cobalt/test_radar_price_floor.py` → `227:def test_a_floored_row_read_before_its_source_fails_is_still_removed():`; its red commit `7d0ce9ec` sits below `e34ad12c` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/price-floor-1008`.
- (vi) THE GATE LISTS: `git log --stat --format=%h 059da441..HEAD -- src/cobalt/db_migrations tests/cobalt` → `0023_radar_price_floor.sql` + rollback (`f105b82e`) and `tests/cobalt/test_radar_price_floor_db.py` (`e0713d36`, needs 0023). `git diff 059da441..f105b82e -- ops/desk/gate-lists.md` (read in `## OWN FINDINGS`' diff): PASS 1 ends `--deselect tests/cobalt/test_radar_price_floor_db.py`, PASS 2 ends `tests/cobalt/test_radar_price_floor_db.py`; row M names `ops/desk/gate-lists.md`. The commands W executed (`:938`, `:1171`) are those lines plus the gate's `--deselect` copy. Carried.
- (vii) The card's RECORDS `git -C /Users/cobalt/cobalt log --all --oneline -- "src/cobalt/db_migrations/0023*"` → now `f105b82e feat(price-floor-1008): …` (this build's own commit; the record predates the build). The `ls`/`grep` records name `data/radar-cache` and other worktrees' files: not on this check's path to judge; the build re-read them at its PREFLIGHT.
- (viii) L32: this report holds constructed tickers (`PFXA`, `PFL*`, `PFD*`, `AAA`…) and the shipped config value only; no value of his.

## OPEN
- A1 (Sol, X7) · REJECTED — row M specifies the rollback as `… AND entered_at IS NOT NULL`, resting on F2 (only admitted rows ever carry `price_floor`). FOLLOW-UP: a rollback on a DB holding a never-admitted `price_floor` row (no production path writes one; X3) raises `CheckViolation` and aborts. What would settle it: a ruling whether the rollback should also clear never-admitted rows (`excluded_by` cannot go NULL there: `0004:48` needs `entered_at` or `excluded_by`), or refuse loudly first. Not his notes, money or sizing.
- A2 (Sol, SCOPE) · REJECTED — `BUILD-HUB.md` `## E3` requires one dated DevDocs line per changed module; `CHECK-HUB.md` `## 7` (ii) scopes only non-docs paths. FOLLOW-UP: none needed unless the desk wants DevDocs pages named in card `files`.

## CONTINUE
next: none (the desk verifies and launches the next step)

## DECISIONS
none

## RECORDS
- L74: one system reminder asked for a `Claude-Session:` line in commits; recorded under `## L74`, not acted on.
- Extra lock take: one, for A1's with-DB run (taken 14:21:07, released 14:21:27 ET, F0 before = after = `664 35 272c95bbb12241e3611e4b36326ccf87`, `.env: removed, proven gone (step 4)`). The gate took its own (waited 7 min).
- House A Sol: `FINDINGS: 2`, final message at output `:21774`–`:21804`; written by me to `<S>/house-a.md`. House B Grok: `FINDINGS: 0`, written by Grok to `<S>/house-b.md`. No house produced nothing; no seat replaced.
- Dropped: none. REFUSED, not needed: none. CONTINUED: none.
- Sol's `diff.md` / `rulings.md` are the ones `stage-set.sh` wrote from git (one staging serves both houses).
- The A1 test was removed again with Edit after its REJECTED run; it is in no commit.
- files opened: 21 — `CHECK-HUB.md`; the card; the build report; `BUILD-HUB.md` (`## THE LOCK` … `## W`); the saved `git diff 059da441 f105b82e -- src configs ops` output; `tests/cobalt/test_radar_price_floor.py`; `src/cobalt/radar/runner.py`; `src/cobalt/cards/store.py`; `src/cobalt/radar/evaluate.py` (`OpenRadarCard`); `src/cobalt/replay/models.py`; `src/cobalt/radar/store.py`; `src/cobalt/cards/picks.py` (grep); `tests/cobalt/test_radar_price_floor_db.py`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the house probe output; Sol's output; Grok's output; `<S>/house-b.md`; the lock-take output; the gate output; `docs/40 - DevDocs/cobalt/radar/runner.md` (tail).
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 69f03c58` → `context 228719 of 400000 — ok`.
- Check of `price-floor-1008`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: price-floor-1008 · pass: 1 · tip: e34ad12c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4023/0 · with-DB 4910/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 228719
