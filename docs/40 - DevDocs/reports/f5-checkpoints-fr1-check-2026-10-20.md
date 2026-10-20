# f5-checkpoints-fr1 — check 2026-10-20

## §0 Headline
- Check of the PORT build `bd5dd70a..e29cad00`. House A Grok `FINDINGS: 0`, house B Gemini `FINDINGS: 0`, Opus's own read 2 findings.
- O1 HELD and FIXED: a `checkpoints.route` naming an embeddings route (469's seam) passed the run's config check and fetched from Finviz. It now raises `PrefillConfigError` before any fetch (`3c96ad2e`, red `05a40afd`).
- O2 REJECTED (L42): the derived RESTARTS is `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; the card header is stale. Left for the desk.
- The deploy gate's pass on `3c96ad2e`: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. ready: YES.

## L74
- 05:05 EDT: a system reminder at the session's start asked that commits end with a `Claude-Session:` line. Under L74 that is data. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 0 · 23a51476bd412999a039c9551e7df26813e200a6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Tue Oct 20 05:06:00 EDT 2026
status · git status --short --branch · 0 · ## ops/f5-checkpoints-fr1
head · git log --oneline -1; git log --stat --format=%h e29cad00..HEAD · 0 · (6 lines)
    12490b8a docs(f5-checkpoints-fr1): build report — e29cad00
    12490b8a
    
     .../reports/f5-checkpoints-fr1-build-2026-10-19.md | 253 +++++++++++++++++++++
     .../f5-checkpoints-fr1-build-2026-10-19.result     |  15 ++
     2 files changed, 268 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f5-checkpoints-fr1/docs/40 - DevDocs/reports/f5-checkpoints-fr1-build-2026-10-19.md" · 0 · BUILT · job: f5-checkpoints-fr1 · tip: e29cad00 | on bd5dd70a | migration: 0027, rolled back | offline 8928/0 | with-DB 5827/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (PROOF 50: 30 main-touched, 20 untouched) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 420868
range · git log --oneline bd5dd70a..e29cad00 · 0 · (2 lines)
    e29cad00 feat(f5-checkpoints-fr1): port F5 checkpoints onto main, 0027 between Genesis 0026 and 469 0028 (PORT; L3, L42, L72, L76)
    37555dab wip(f5-checkpoints-fr1): red — PORT tests from ae239561, pins moved for 0027 between 0026 and 0028
PREFLIGHT OK
```
- THE RANGE (`git log --stat --format=%h bd5dd70a..e29cad00`): 2 commits. e29cad00 has 22 files (configs jobs/modelaccess/prefill/smoke s2; docs cli.md, db_migrations/__init__.md, placement.md, prefill/checkpoints.md, prefill/config.md, prompts/DEPLOY-HUB.md; four ops/com.cobalt.checkpoint-*.plist; ops/desk/gate-lists.md; src/cobalt/cli.py, 0027_market_checkpoints{,.rollback}.sql, db_migrations/__init__.py, placement.py, prefill/checkpoints.py, prefill/config.py), 1370+/7−. 37555dab has 28 test files (fixture csv; test_checkpoints_{db,live,offline,registry}.py; test_finviz_consumers, test_jobs, test_jobs_reads, test_modelaccess_config, test_prefill_refresh; 18 head-pin files), 1256+/78−. Path union: 50 files.
- DB: the card is not "DB: none" (K6/K12 add a migration).
- `ls <S>` → `No such file or directory` (fresh).
- house probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · lines whole:
```
grok: UP
gemini: UP
```
- Seats: no `HOUSE A:` header line, so house A = Grok (the first house UP). The card's `HOUSE B:` line reads `as needed`. But this build writes his daily note (K7), and the card itself says `HOUSE B mandatory` twice (`## RECORDS` BAND HIGH line; row FIX1 says "`HOUSE B` stays mandatory"). The hub's MANDATORY rule covers a build that writes his vault notes. Both houses are UP, so I took the safe default and seated house B = Gemini. This adds a check and grants no access. See `ASK DESK 1` under `## DECISIONS`.
- `house A: grok · house B: gemini`.
- PROVEN BY FIRST REAL USE: the write and with-DB strings are proved at their first use (`## 4`–`## 6`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → last line `STAGED 55 files · 1034144 bytes · commits 2` (commits 2 = PREFLIGHT's range count). Its per-file lines (bytes · dest under `<S>`): STAGED-CARD 15 · diff.md 172700 · files/731-f5-card.md 58649 · files/f5-checkpoints-fr1-build-2026-10-19.md 38165 · and under files/wt/: configs/cobalt/jobs.yaml 27232 · modelaccess.yaml 4153 · prefill.yaml 2067 · smoke/s2.yaml 29219 · docs/…/cobalt/cli.md 8198 · db_migrations/__init__.md 21910 · db_migrations/placement.md 5396 · prefill/checkpoints.md 6890 · prefill/config.md 3804 · prompts/DEPLOY-HUB.md 68471 · ops/com.cobalt.checkpoint-0715/0745/0815/0845.plist 2828 each · ops/desk/gate-lists.md 8081 · src/cobalt/cli.py 27306 · 0027_market_checkpoints.rollback.sql 328 · 0027_market_checkpoints.sql 2146 · db_migrations/__init__.py 13855 · placement.py 9364 · prefill/checkpoints.py 37044 · prefill/config.py 9990 · tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv 1406 · test_archiver_migrations.py 29589 · test_assumed_store.py 17153 · test_checkpoints_db.py 4973 · test_checkpoints_live.py 3280 · test_checkpoints_offline.py 38420 · test_checkpoints_registry.py 2533 · test_dml_roles_offline.py 2643 · test_drc_d2_fix_r1_db.py 29443 · test_drc_d3_experiments.py 5698 · test_drc_k1_store.py 29489 · test_drc_store.py 26176 · test_f15_p1_records_offline.py 8140 · test_finviz_consumers.py 8125 · test_jobs.py 41777 · test_jobs_reads.py 11580 · test_legs_migration.py 4763 · test_modelaccess_config.py 7223 · test_p4_migrations.py 29362 · test_prefill_refresh.py 56987 · test_radar_handicap_store.py 11696 · test_radar_migration.py 5450 · test_radar_price_floor_db.py 7212 · test_radar_score_migration.py 24572 · test_seam_drc_s3_registry.py 2550 · test_stale_score_db.py 12024 · test_tenancy.py 31574 · test_voice_store.py 13256 · rulings.md 755.
`stage-copy.sh`, one call each, each `COPIED <bytes> <dest>`: F5-FINAL 47241 · F4-FINAL 78381 · f4-f5-seam report 4503 · card 304 34139 · card 448 33548 · prefill/market.py 3642 · prefill/daily.py 54690 · vaultwrite/writer.py 59962 · vaultwrite/migrations/0004_vault_writes_sync_revert.sql 2263 · radar/notes.py 30852 · strike/detector.py 15532 · strike/measure.py 12596 · session/calendar.py 6207 · daymode/note.py 10287 · modelaccess/config.py 6498 · ops/com.cobalt.cards-expire.plist 4020.
`HOUSE-INSTRUCTIONS.md` (34715 bytes): the HOUSE TEXT verbatim, then `## ROWS`, `## NOT IN THIS JOB` and `## CHECK ASKS` copied whole. One deviation: the PORT row cell and the card's `## RECORDS` are not repeated there. Each is a pointer to the byte-identical card copy `files/731-f5-card.md`, named for the house to read whole. Recorded under `## RECORDS`.
Houses started 05:09 EDT (`date` 05:09:24): house A Grok (task bo6d2kd97), house B Gemini (task b7a5qn17l), each one attempt, `run_in_background`, timeout 2700000. After `cd <WT>`, `git status --short --branch` → `## ops/f5-checkpoints-fr1`.

## OWN FINDINGS
Written before either house's list was opened. Read for them: the card, the diff `bd5dd70a..e29cad00` (the F5 hunks of the main-touched src/config/ops/hub files; `git diff --stat ae239561 e29cad00` over the 20 main-untouched files, which names only `prefill/checkpoints.md`, `test_checkpoints_db.py` and `test_checkpoints_offline.py`, matching the build's PROOF lines); `src/cobalt/prefill/checkpoints.py:640-848`; the two `0027` SQL files; `db_migrations/cli.py` `_apply` (`:631-642`: FORWARD re-runs every file, each idempotent, so `0027` sorted below an already-applied `0028` is applied on a later `migrate`); `git diff 40e646ed bd5dd70a` over every module `checkpoints.py` imports (only `modelaccess/` changed: 469's `EmbedRoute` and the discriminated `routes` union); the build report `## RESTARTS`, `## W`, `## FOR THE CHECK`, its last line.

FINDING O1
ROW: PORT (2) seam with 469 / K7 ("a config error crashes before any fetch")
CLAIM: `src/cobalt/prefill/checkpoints.py:664` checks only that `checkpoints.route` is a key of the registry. Since 469 the registry also holds `openai_embeddings` routes (`modelaccess/config.py` `AnyRoute`), so `route: local.embed` passes the check. The run then fetches from Finviz, writes the unit, and degrades the narrative only at the model call. It never crashes before the fetch.
RUN: TEST — `tests/cobalt/test_checkpoints_offline.py`
```python
def test_check_o1_an_embeddings_route_is_a_config_error_before_any_fetch(cp, monkeypatch):
    from cobalt.prefill import checkpoints
    from cobalt.prefill.config import PrefillConfigError, load_checkpoints_config

    cfg = load_checkpoints_config().model_copy(update={"route": "local.embed"})
    monkeypatch.setattr(checkpoints, "load_checkpoints_config", lambda *a, **kw: cfg)
    with pytest.raises(PrefillConfigError):
        run(cp, "0745", at(7, 45))
    assert cp.gets == 0
```
EXPECT: `Failed: DID NOT RAISE <class 'cobalt.prefill.config.PrefillConfigError'>`.

FINDING O2
ROW: X5 / R1
CLAIM: The RESTARTS derived on the tip is not the card header's set (`731-f5-card.md:13`, `com.cobalt.aset com.cobalt.radar`). `src/cobalt/prefill/config.py` also reaches main's F20 resident `com.cobalt.cos` (build report `:181-182`).
RUN: COMMAND — `uv run cobalt jobs restarts bd5dd70a..e29cad00`
EXPECT: last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`; the `src/cobalt/prefill/config.py` row names `com.cobalt.cos`; the four plists read `plist in diff; new one-shot, bootstrap once`; no `UNCLASSIFIED`.

## Findings
Both lists were opened only after `## OWN FINDINGS` was written. House B (Gemini) finished first: `date` 05:13:54, read then, and its printed answer was written to `<S>/house-b.md` without the harness's `[exited with code 0]`. House A (Grok) finished at `date` 05:17:24. It wrote `<S>/house-a.md` itself (12 bytes) and replied with that path. `ls -la <S>` → `house-a.md 12`, `house-b.md 3719`.
- House A (grok): `<S>/house-a.md` reads exactly `FINDINGS: 0`. No finding blocks.
- House B (gemini): a prose summary of what it checked (renumber case (b), seams, pin moves, FIX1 lines, X1–X6, all "check out"), then `FINDINGS: 0`. No `FINDING <n>` blocks.

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | opus-own | PORT seam 469 / K7 | an `openai_embeddings` route passes `checkpoints.py:664`; the run fetches instead of crashing on config | TEST |
| O2 | opus-own | X5 / R1 | derived RESTARTS adds `com.cobalt.cos` to the header's set | COMMAND |

## Dropped
none (neither house wrote a `FINDING` block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py::test_check_o1_an_embeddings_route_is_a_config_error_before_any_fetch` | `1 failed in 0.46s`; first failing line `E       Failed: DID NOT RAISE <class 'cobalt.prefill.config.PrefillConfigError'>` (`tests/cobalt/test_checkpoints_offline.py:893`); the fixture state shows `gets=2` | HELD |
| O2 | opus-own | `uv run cobalt jobs restarts bd5dd70a..e29cad00` | `src/cobalt/prefill/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` · the four plists `plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-HHMM` · no `UNCLASSIFIED` · last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` | REJECTED — L42 "RESTARTS derived": the derived line is the right one, and the card header (`731-f5-card.md:13`) is the stale value. The builder already raised this as its DECISION 1. Stays OPEN for the desk's header update. |
Red commit: `05a40afd wip(f5-checkpoints-fr1): check red — O1` (the test file only).

## FIXES
- O1: `src/cobalt/prefill/checkpoints.py`. After the "is a route" check, `run_checkpoint` now also refuses a route that is not a chat `Route` (`cobalt.modelaccess.config.Route`) with `PrefillConfigError`, before the calendar, gate or fetch. Dated line in `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (`## 2026-10-20 — f5-checkpoints-fr1`). After the fix, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_checkpoints_registry.py tests/cobalt/test_finviz_consumers.py tests/cobalt/test_modelaccess_config.py` → `117 passed, 1 xfailed in 3.71s` (0 failed). Commit `3c96ad2e fix(f5-checkpoints-fr1): an embeddings checkpoints.route is a config error before any fetch (check O1)`.

## Suites
RESTARTS first (`BUILD-HUB.md` `## RESTARTS`): `uv run cobalt jobs restarts bd5dd70a..HEAD` (HEAD `3c96ad2e`) → 53 rows, no `UNCLASSIFIED`. The `src/cobalt/prefill/config.py` row reads `static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`. The four plists read `plist in diff; new one-shot, bootstrap once: com.cobalt.checkpoint-HHMM`. Last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
W, ONE call on tip `3c96ad2e`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-checkpoints-fr1 all --deploy --deploy-gate --deselect tests/cobalt/test_checkpoints_db.py --migration` (background) → exit 0. Verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8929/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5828/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-checkpoints-fr1-all-20261020-051828.log
```
- Offline 8929 is the build's 8928 plus the O1 test.
- `grep -n -F "OUTSIDE" <log>` → nothing: every pass-1 skip is inside the allowed set.
- `grep -n -F "PASSED tests/cobalt/test_checkpoints_db.py" <log>` → `:2251` `test_migration_round_trip`, `:2252` `test_unique_rerun_keeps_one_row`, `:2253` `test_0815_base_is_a_copy`, `:2254` `test_purge_with_a_checkpoint_row_succeeds`.
- `cobalt_dev: 0013 — F2 = F0`. `.env: removed`; `ls /Users/cobalt/cobalt-wt/f5-checkpoints-fr1/.env` → `No such file or directory` (06:06:02 EDT, `date`).
- O1 was shown red before its fix (`## RUNS`).

## Scope
PREFLIGHT's path union, the 50 files of `bd5dd70a..e29cad00`, plus my commits: `05a40afd` `tests/cobalt/test_checkpoints_offline.py` (K2–K8/PORT files; a test file) and `3c96ad2e` `src/cobalt/prefill/checkpoints.py` (rows K2–K8 `files`) plus `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (row D0 `files`; the dated DevDocs line). Nothing else.

## Checked against the branch
- (i) `git log --oneline e29cad00..HEAD -- . ":(exclude)docs"` → `3c96ad2e fix(f5-checkpoints-fr1): an embeddings checkpoints.route is a config error before any fetch (check O1)` · `05a40afd wip(f5-checkpoints-fr1): check red — O1`. `<tip now>` = `3c96ad2e`.
- (ii) `git log --stat --format=%h e29cad00..HEAD` → `3c96ad2e`: `docs/…/prefill/checkpoints.md`, `src/cobalt/prefill/checkpoints.py` · `05a40afd`: `tests/cobalt/test_checkpoints_offline.py` · `12490b8a`: the build report and its `.result` (docs). Every non-docs path is in a row's `files` or is a test file.
- (iii) fence: `git log --oneline bd5dd70a..HEAD -- src/cobalt/prefill/daily.py src/cobalt/prefill/cli.py src/cobalt/vaultwrite/writer.py src/cobalt/vaultwrite/merge.py src/cobalt/daymode/note.py src/cobalt/prefill/market.py src/cobalt/radar/notes.py src/cobalt/strike/detector.py configs/cobalt/templates/daily.md.j2 configs/cobalt/taxonomy/tunables.yaml` → EMPTY. (The fence's F4 lines inside shared files, such as jobs.yaml's prefill-refresh row and test_finviz_consumers.py's F4 lines: the F5 hunks above add lines only, beside them.)
- (iv) `grep -n -F "def test_check_o1_an_embeddings_route_is_a_config_error_before_any_fetch" tests/cobalt/test_checkpoints_offline.py` → `887:` (one line). Its red commit `05a40afd` sits below its fix `3c96ad2e` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/f5-checkpoints-fr1`.
- (vi) THE GATE LISTS: `git log --stat --format=%h bd5dd70a..HEAD -- src/cobalt/db_migrations tests/cobalt` → the new `0027_market_checkpoints.sql` (`e29cad00`) and the new with-DB `test_checkpoints_db.py` (`37555dab`). `git diff bd5dd70a e29cad00 -- ops/desk/gate-lists.md` (read at `## 2`) → PASS 1 ends `--deselect tests/cobalt/test_checkpoints_db.py`, PASS 2 ends `tests/cobalt/test_checkpoints_db.py`. Row K12 names `ops/desk/gate-lists.md` in its `files`. The gate ran that file's lines (log `pass 1: whole (deploy)`; the four PASSED lines in pass 2). Carried.
- (vii) card `## RECORDS`, the `ls` record: `ls src/cobalt/db_migrations` → … `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, `0027_market_checkpoints.rollback.sql`, `0027_market_checkpoints.sql`, `0028_genesis_vectors.rollback.sql`, `0028_genesis_vectors.sql`, `cli.py`, `dev_rebuild.py`, `placement.py` (now holds `0027`, as PORT builds). The other records' commands are `git grep` / `git diff` / `rev-parse` forms, which are not on this check's list. Not re-run.
- PORT CHECK ASK proofs: `git log --merges --oneline bd5dd70a..HEAD` → EMPTY (no merge commit). `git diff --stat ae239561 e29cad00` over the 20 main-untouched files → only `prefill/checkpoints.md` (2 +-), `test_checkpoints_db.py` (10), `test_checkpoints_offline.py` (12), each the 0027 renumber / case-(b) slot, which agrees with the build's PROOF lines. `grep -rn -F "0026_market" src tests ops configs "docs/40 - DevDocs/cobalt"` → nothing. `FORWARD` / `REVERSE` / docstring / placement agree on `0027` between `0026` and `0028` (diff read at `## 2`). The old build report is not in the range (PREFLIGHT's range stat).
- (viii) L32: this report holds constructed test values and repo facts only; no ticker, price or date of his.

## OPEN
- O2 — REJECTED (L42). The derived RESTARTS line `com.cobalt.aset com.cobalt.cos com.cobalt.radar` is correct by L42. The card header `RESTARTS: com.cobalt.aset com.cobalt.radar` is stale. Settled by the desk updating the card header (or by a `SETTLED: O2 — R<n>` record). The deploy restarts all three.

## CONTINUE
next: none — CHECK DONE (the desk commits this report and its `.result`).

## DECISIONS
1. ASK DESK 1 [05:06 EDT]: the card's `HOUSE B:` line says `as needed`, but the build writes his daily note and the card says `HOUSE B mandatory` twice (`## RECORDS` BAND HIGH; row FIX1). Default taken: house B seated (Gemini, UP), one attempt; it produced `FINDINGS: 0`. Nothing more is owed under either reading.
2. O2 (open, for the desk): the card header's `RESTARTS:` should read `com.cobalt.aset com.cobalt.cos com.cobalt.radar`, as derived on `3c96ad2e`. Default taken: the stop line carries the derived set (L42), and the deploy restarts all three. The builder raised the same item as its DECISION 1.

## RECORDS
- L74: one item at 05:05 EDT (`## L74`). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- `HOUSE-INSTRUCTIONS.md`: the PORT row cell and the card's `## RECORDS` are pointers to the byte-identical card copy `files/731-f5-card.md`, not repeated inline. Every other required section is copied whole. Neither house reported a missing file.
- Houses: house A Grok, one attempt, 05:09 → 05:17, wrote `house-a.md` itself (`FINDINGS: 0`). House B Gemini, one attempt, 05:09 → 05:13, its printed answer written by me to `house-b.md` (`FINDINGS: 0`). Neither produced a finding block, so nothing was dropped.
- No dropped finding; no REFUSED call; no CONTINUE message; no extra lock take (the one take was inside `gate.sh`: `lock: waited 0 min`, released, `.env: removed`).
- The `.result` file is written beside this report. The commit of both is the desk's (LAUNCH: "commits the report after the check"); this check's commit strings run in `<WT>` only.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 6f1c0479-9f06-4072-95fa-1a81f32afef6` → `context 238202 of 400000 — ok`.
- files opened: 17 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK`–`## W`); the build report; `areas/cobalt.md` (the two allowed sections); `src/cobalt/prefill/checkpoints.py`; `0027_market_checkpoints.sql`; `0027_market_checkpoints.rollback.sql`; `src/cobalt/db_migrations/cli.py` (grep, `_apply`); `src/cobalt/modelaccess/__init__.py` (grep); `tests/cobalt/test_checkpoints_offline.py`; `docs/…/prefill/checkpoints.md` (tail); the house-probe output; the Gemini output; the Grok output; `<S>/house-a.md`; the gate output.
- Check of `f5-checkpoints-fr1`: house A `grok`, house B `gemini` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f5-checkpoints-fr1 · pass: 1 · tip: 3c96ad2e · house A: grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: gemini FINDINGS: 0 · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 238202
