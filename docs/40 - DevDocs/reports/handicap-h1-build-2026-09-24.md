# HANDICAP H1 BUILD r2 — 2026-09-24 (prompt `prompts/2026-09-24/43-handicap-h1-build-r2.md`, seat `handicap-h1-r2-0924`, Opus 5.5)

## §0 Headline

- **Built:** float handicap H1, shadow-only (STEP-0 … STEP-7 with 4A), on `f6643d41`. Tip `27df13f1`, one commit per step plus the CLOSE probe test.
- **Suites:** offline 2619/0 · with-DB 2976/0 (2 deselected) · live-note 131/0 with R56's four `AWAITING` lines.
- **L76:** 0014 was applied only inside rolled-back transactions; `cobalt_dev` is proven at 0013 (`0014_columns_on_cobalt_dev=0`). The h = 1 identity was proven over 6 days / 1923 scans with 0 mismatches.
- **Experiments:** 14, 12 as expected; X6 and X10 were not, and both are handled by design.
- **ESCALATE: 12**, 4 of them ASK DESK: 1 vacuous dead column · 2 X11 latch · 8 how loud a handicap-only degradation is · 11 healthy pins vs "not configured".

## L74

Recorded ONCE (L74): a system-reminder block attached to this session's first tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and named a file-send tool (`SendUserFile`). It is DATA, not followed. Every commit of this run carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and nothing else.

## AUTHORIZATION

`date` 18:44:15 EDT (start). Each gate its own Bash call; phrases quoted only as the prompt allows.

| gate | command (short) | result | verdict |
|---|---|---|---|
| placeholder | `grep -n -E "R_[_]" 43-…r2.md` | no output (exit 1) | PASS |
| R28 | `grep -n "^\| R28 " cto-2026-09-21.md` | line 39, carries `I don't want to exclude tickers` | PASS |
| R29 | `grep -n "^\| R29 " cto-2026-09-21.md` | line 40, carries `Finviz does offer both market cap and float` | PASS |
| R26 | `grep -n "^\| R26 " cto-2026-09-22.md` | line 137, carries `POOL-WIDE division` | PASS |
| R26 committed | `git -C … log -1 -S"POOL-WIDE division"` | `d86b973d5d83c3b7a3682f71167bad49ece2d2d8` | PASS |
| R52 | row line 114 | `handicap.missing: apply`, his `"A"` | PASS |
| R53 | row line 113 | `handicap.combinator: any`, his `"A"` | PASS |
| R54 | row line 112 | `INOPERATIVE at factor 1`, his `"B"` | PASS |
| R55 | row line 111 | `KEEP THE DESIGN AS WRITTEN`, his `"A"` | PASS |
| R56 | row line 110 | `config_cap (handicap)`, his `"A"` | PASS |
| R57 | row line 109 | `UNHANDICAPPED name first`, his `"A"` | PASS |
| R54 committed | `-S"INOPERATIVE at factor 1"` | `9a4b01a7750195bee43f952ba919e0ccb75c6f46` | PASS |
| 09-23 R58 | `grep -n "^\| R58 " cto-2026-09-23.md` | line 61, `"yes start both"`, `handicap H1` | PASS |
| 09-23 R58 committed | `-S"yes start both"` | `dab5c706126d2ca987cf32a262ecbfcb90ab6545` | PASS |
| R32 | line 131 | carries `claude-opus-5-5` | PASS |
| 09-24 R9 | line 23 | `GATE EARLY`, his `"A"` | PASS |
| 09-24 R10 | line 24 | `L76`, his `"A"` | PASS |
| L76 entry | `grep -n "^### L76 " LAWS.md` | line 435 | PASS |
| base tag | `git -C … log --oneline -1 deploy-2026-09-24` | `a2d320b8 Reapply "Merge branch 'main' into deploy/stacked-0923"` | PASS |
| launch row | `grep -n "43-handicap-h1-build-r2.md" cto-2026-09-24.md cto-2026-09-25.md` | `cto-2026-09-24.md:104: \| R85 \| 18:4x ET \| …` (also R62 line 76); `cto-2026-09-25.md`: No such file — recorded, not fatal (row is in 09-24) | PASS |
| launch row committed | `-S"43-handicap-h1-build-r2.md" -- cto-2026-09-2*.md` | `f6643d4150ae2ce6f91a798a4498bf74df46840c` | PASS |
| `.env` cp string in 09-22 | `grep -c -F` | 1 | PASS |
| `.env` rm string in 09-22 | `grep -c -F` | 1 | PASS |
| rm string committed | `-S"Bash(rm …handicap-h1/.env)"` | `055242df8032632dfafdcc8a69dcc271be89c0f6` | PASS |
| R30 | line 133 | both strings + his `"Approved"` | PASS |
| 09-23 R52 | line 55 | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *` + `"Approved all commands you need"` | PASS |
| live-vault string carried by `03` | `grep -c -F` | 1 | PASS |
| 19 allow strings in `47` | 19 × `grep -c -F -e` | 17 × `1`; the cp and rm strings `2` each | PASS (all ≥1) |
| 3 deny strings in `47` | `"AskUserQuestion"` `"EnterWorktree"` `"Bash(git push*)"` | 1 / 1 / 1 | PASS |
| removed string gone | `grep -c -F -e "\"Bash(COBALT_ENV=dev uv run cobalt db migrate)\"" 43-…r2.md` | 0 | PASS |

Disclosures (UNATTENDED RULES — commands outside the list's bare shapes; none was DENIED, none touched `.env`, none wrote outside the worktree): (1) the very first Bash call, before the rules had been read, was `cat` of the prompt file itself (read-only); (2) at 19:0x a no-op `cat >> /dev/null <<'EOF'` heredoc was typed by mistake (wrote nothing); (3) at 19:20 `cp /Users/cobalt/.claude/jobs/c1e75a7c/tmp/test_radar_handicap_group.py …/tests/cobalt/` placed a test file drafted in the job tmp — from then on every placement uses the Write tool; (4) at 20:15 a no-op `cat /dev/null` was typed while waiting (read nothing, wrote nothing).

## PREFLIGHT

`date` 18:45:17 EDT.

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Thu Sep 24 18:45:17 EDT 2026` |
| clean | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/handicap-h1-build-2026-09-24.md"` — only this run's own report (the prompt's mandated FIRST Write) |
| long status | `git status` | 0 | `On branch radar/handicap-h1-0922` / `Untracked files:` |
| re-cut | `git log --oneline -1` | 0 | `f6643d41 docs(desk): 09-24 R84 stale-score r2 BUILT …` — first launch, = main's tip at the re-cut → **`<main tip>` = `f6643d41`** (not `be4c79b5`) |
| main now | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `36288088 docs(desk): 09-24 §5 — H1 build c1e75a7c (lock) + …` — main moved after the cut (desk docs); recorded, not fatal |
| deploy under base | `git log --oneline f6643d41..a2d320b8` | 0 | EMPTY — PASS |
| 0013 under base | `ls src/cobalt/db_migrations` | 0 | lists `0013_tunables_slug_nullable.sql` and `.rollback.sql`; NO `0014_*` — PASS |
| 0013 registered | `grep -n "0013_tunables_slug_nullable" …/__init__.py` | 0 | `88:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",` · `93:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",` (+ docstring 38, 41) |
| own commits | `git log --oneline f6643d41..HEAD` | 0 | EMPTY |
| `.env` | `ls -la .env` | 1 | `ls: .env: No such file or directory` — PASS |
| LOCK (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — PASS |
| LOCK (b) | `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | 1 | `No such file or directory` — PASS |
| fixtures | `ls tests/fixtures/radar` | 0 | `_cut_p2_fixtures.py _cut_panel_fixtures.py _cut_setups_fixtures.py bars-rubberband.real-shape.json bars-setups-rubberband.real-shape.json card-settings.real-shape.json daily-bars-setups-rubberband.real-shape.csv daily-bars.real-shape.csv membership-setups-rubberband.real-shape.json panel-cards.contract.json panel-pool-block.real-shape.json panel-pool.real-shape.json pool-metrics.real-shape.csv radar-lists.example.md radar-screens.example.md radar-screens.real-shape.md` |
| experiments | `ls tests/experiments` | 0 | `setups_one` (no `__init__.py`) |
| retained days | `ls /Users/cobalt/cobalt/data/radar-cache` | 0 | `2026-09-17 2026-09-18 2026-09-21 2026-09-22 2026-09-23 2026-09-24` — six retained days (UTC-dated folders, see STEP-1) |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | 22 notes listed (READ ONLY) |
| handicap on main | `grep -rn "handicap" src/cobalt tests/cobalt configs/cobalt` | 1 | EMPTY — PASS |
| cd | `cd /Users/cobalt/cobalt-wt/handicap-h1` | 0 | — |
| pytest | `uv run pytest --version` | 0 | `pytest 9.0.2` (uv created `.venv` on first use) |
| restarts probe | `uv run cobalt jobs restarts f6643d41..HEAD` | 0 | `docs/40 - DevDocs/reports/handicap-h1-build-2026-09-24.md	A	DOCS	-` / `RESTARTS: none` |
| mkdir probe | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | no-op (the folder exists) |

No command DENIED.

### 27 cite → main line (main `f6643d41`, re-located by symbol)

| cited (`27`/`29`, on `d2d82e7`) | symbol | main line now |
|---|---|---|
| `pool.py:94-106` | `_metric_position` | 94-106 (unchanged) |
| `pool.py:109-212` | `_ranked` | 109-212 (unchanged) |
| `pool.py:215-400` | `decide` | 215-402 |
| `pool.py:326` re-sort point | `ordered, ranks, source_for, values = _ranked(…)` | 326 |
| `pool.py:39-62` | `Transition` | 39-55 |
| `pool.py:64-70` | `Decision` | 64-69 |
| `pool.py:283-324` held | the `held` loop / cap eviction | 283-321 |
| `models.py:99-116` | `PoolBlock` | 99-116 |
| `models.py` | `SourceSet` / `ExcludedBy` | 176-185 / 163-167 |
| `notes.py:88-` | `parse_note_bytes` | 88-150 |
| `notes.py:108` | `PoolBlock(**raw)` | 108 |
| `notes.py:394-460` | `load_sources` | 394-460; `pool_error` set at 412, 415 |
| `notes.py:64-65` | `ParsedSources.frozen` | 63-65 |
| `runner.py:103-150` | `_collect` | 103-168 |
| `runner.py:139-142` | metrics dict | 139-142 |
| `runner.py:186` | `decide(...)` call | 186 |
| `runner.py:189-206` | S1 `try` | 190-207 |
| `runner.py:245` | frozen poll hand-off `PollMember(row["ticker"], row.get("last_rank") …)` | 245 (non-frozen: 239-242) |
| `runner.py:319-323` | `pool_unit` | 319-323 |
| `runner.py:391-398` | `_number` | 391-398 |
| `runner.py:453-460` | `run_command` / `resident` | 453-464 |
| `store.py:29-38` | `open_members` | 29-38 |
| `store.py:46-63` | `members_for_day` | 46-63 |
| `store.py:65-170` | `apply_membership` | 65-169 |
| `config.py:100-117` | `is_not_equity` | 100-117 |
| `config.py:168-177` | `load_config`'s header check | 155-178 (check 168-177) |
| `cli.py:78` | `sources` subparser | 80-84 |
| `collector.py` cache | `FinvizScreenerCollector._cache` | 164-170 (`<cache>/<UTC date>/<source>-<UTC HHMMSS>.csv`) |
| `poller.py:84` | the poll sort | 84: `for member in sorted(members, key=lambda item: (item.rank, item.ticker)):` |
| `radar_panel.py:149-163` | `PoolRow` | 149-164 |
| `radar_panel.py:417` | `_row` `position=record.last_rank` | 417 |
| `radar_panel.py:542-545` | pool-row sort | 544-546 |
| `radar_panel.py:586-588` | degraded joiner | 586-590 |
| `radar_panel.py:830-845` | `_pool_table` | 829-854 |
| `radar_panel.py:857` | `render_pool` | 857 |
| `radar_panel.py:904` | `_badge` | 904 |
| `evaluate.py:143-166` | `FORMULA_FILES` / `canonical_sha256` | 175 / 187 |
| `db_migrations/cli.py` | `_apply` / `_rollback_paths` | 471 / 770 |
| `tests/cobalt/conftest.py:134` | `dev_db_tx` | 134 |

No cited symbol vanished.

## BASELINE

`date` 18:48:46 EDT. Tree: `<main tip>` `f6643d41`. DISCLOSED ORDER SLIP: the offline suite was started first; STEP-0's two DOCUMENTATION edits were made and committed (`4c1c92f2`, 18:49) while it ran, and the with-DB leg ran on `f6643d41` + that docs-only commit. No source, test, config or fixture byte differs from `<main tip>` in either leg.

- **OFFLINE** `uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider` → `2501 passed, 361 skipped, 1 xfailed, 15 warnings in 515.19s (0:08:35)` — **0 failed**. The two `SKIPPED` lines naming `COBALT_LIVE_VAULT_ROOT` (`tests/taxonomy/test_catalyst.py:365`, `tests/taxonomy/test_predicate.py:262`) are the offline suite's own (the live-note leg runs them).
- **LIVE-NOTE** (READ-ONLY, no lock) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `131 passed, 15 warnings in 27.32s`; no `SKIPPED` line; `AWAITING` lines, verbatim: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)` — **= R56's known state** (131 passed, 0 failed, the same four).
- **WITH-DB** (THE LOCK 18:57:54, `## LANE`) `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → `2854 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 588.78s (0:09:48)` — **0 failed**; deselected **2** (= EXPECTED). No `cobalt db` before or after. The six `SKIPPED`, verbatim: `test_cards_picks.py:383: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:396: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `test_catalyst.py:365` / `test_predicate.py:262` (COBALT_LIVE_VAULT_ROOT). TABLE-SET probe `tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`: in the run, not among the skips, 0 failed → GREEN (no other branch left a table on `cobalt_dev`).

## STEP-0

`grep -n "RULED B \[R26\]"` → no hit (not on main); `grep -n "only admits"` ADR-0009 → line 28 (not landed). Both edits made.

(a) v3 `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md`:
- BEFORE (heading, line 75): `**[F-09 · F-04 · F-18] Mechanism at the pool — OPEN FOR DEJAN — R2-1 (round 2 did not converge on R2-1.1; …). ASTRA PENDING (R13).** The proposal's sentence was: … Two positions stand, verbatim; this derive takes neither.` followed by the bullets A, B, reasons, file-check, the desk's A/B, "What waits on his answer", and `- **Common ground, both positions:** …`.
- AFTER: `**[F-09 · F-04 · F-18] Mechanism at the pool — RULED B [R26] (his "B", 12:28 ET 2026-09-22, \`cto-2026-09-22.md\` §4 R26: POOL-WIDE division). ASTRA PENDING (R13).**` / the derive-r2 report's `## OPEN FOR DEJAN` B paragraph BYTE FOR BYTE (its line 43, `**B — POOL-WIDE, Fable (round-1 item (c), ADOPT WITH replacement); grok round 2 \`ADOPT B\`:** "\`_ranked()\` is untouched. … The group values come from the source \`source_for[ticker]\` names."`) / `Position A (TIER-BOUND) was not ruled; its text stays in the derive-r2 report's OPEN FOR DEJAN block. [R26]` / `- **Common ground, both positions:** …` unchanged.
- `## Status after round 2` R2-1 row: Status `**OPEN FOR DEJAN** (item not converged)` → `**RULED B [R26]**`; Gates `H1's JSONB meaning … default named by the houses if silent: A.` → `H1 builds B's would-be rank (shadow); H2 builds B's division. [R26]`.
- §6: `**(OPEN FOR DEJAN — R2-1: the field NAMES of this JSONB are the same under A and B; … `decisive` by [R2F-03].)**` → `(R26 B: \`position\` = \`raw_rank\`; \`effective_position\` = the would-be pool-wide rank. [R26])`.
- Header line 14: `R2-1 **OPEN FOR DEJAN** (R2-1.1` → `R2-1 **RULED B [R26]** (R2-1.1`.
- [R54] one line inserted after `… The dry-run prints the header names it read and five raw cells."` in §3's [F-10] bullet, the prompt's text verbatim (`**[R54] RULED (his "B", 14:21 ET 2026-09-22, …) … ASTRA PENDING (R13).**`). Nothing removed.

(b) ADR-0009 line 28: `\`card_score\` is the only number that orders WATCH cards; pool \`last_rank\` only admits.` → grok's [F-08] text from "The one authority that reaches the card is `ladder_order`" through "In `live` both numeric inputs carry the stored `h`.", tagged `[amended 2026-09-22, FLOAT-HANDICAP-v3 [F-08]]`. `ladder_order` untouched.

(c) `git status` → only the two files. COMMIT `4c1c92f2 docs(design): float handicap — R26 pool-wide, R54 dead column` · `git show --stat HEAD`: `.../ADR-0009-radar-cards-seam-and-precondition-ast.md | 2 +-` · `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md | 19 +++++++++----------` · `2 files changed, 10 insertions(+), 11 deletions(-)`.

## STEP-1

Folder `tests/experiments/handicap_h1/` with its OWN `conftest.py` (no `tests/experiments/__init__.py`, main has none — L68 seam with `bars/chunk-e-0920` and `cards/stale-score-0922`'s `tests/experiments/stale_score/`). THE CACHE READER is `h1_cache.py` (test-support; moved into `src/cobalt/radar/handicap_dry_run.py` at STEP-6): it groups by `collector.py`'s naming and builds each scan's `SourceSet` list by CALLING `RadarRunner._collect` over a cache-backed collector — `_number`, `is_not_equity` and the header config are production's own calls, no second parser. `h1_support.py` holds the replay helpers and the constructed block (literals 20 / 300 / 0.8 / any / apply / shadow — this build's, not his).

**Grouping, proved first** (`test_h1_x0_grouping.py`). The first cache read FAILED: `h1_cache.CacheGroupingError: 2026-09-22: 1 file(s) fit no scan, first 'movers-gainers-211004.csv'`. That file is the nightly replay's mover export, which `replay/movers.py` writes into the same day folder (`:39`, `:374`) under its own name; the reader now matches it with THAT module's `_CACHE_NAME` regex (`:113`) and counts it apart — any other unmatched file is still a loud `CacheGroupingError`. Re-run, verbatim:
```
GROUPING day 2026-09-17: files 3251 · in scans 3251 · mover exports 0 · folders skipped 0 · scans 306
GROUPING day 2026-09-18: files 3377 · in scans 3377 · mover exports 0 · folders skipped 0 · scans 318
GROUPING day 2026-09-21: files 3473 · in scans 3473 · mover exports 0 · folders skipped 1 · scans 327
GROUPING day 2026-09-22: files 3464 · in scans 3463 · mover exports 1 · folders skipped 1 · scans 326
GROUPING day 2026-09-23: files 3473 · in scans 3471 · mover exports 2 · folders skipped 1 · scans 327
GROUPING day 2026-09-24: files 3167 · in scans 3167 · mover exports 0 · folders skipped 1 · scans 299
```
Every file lands in exactly one scan (asserted). Day folders are the collector's UTC date (`now.date()` on a UTC instant); every scanned session (04:00–20:00 ET) falls inside one UTC date. 2026-09-24 is TODAY's folder and was still being written by production while read (a partial day).

### X2
`uv run pytest -q -s tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py -p no:cacheprovider` (his pool block through `notes.parse_note`, read only; opens carried forward from the replay's own transitions; the first scan of the day starts EMPTY — production's first scan carries the prior day's rollovers, the replay does not), verbatim:
```
X2: day 2026-09-18 · scans 318 · RTH scans 128 · RTH scans after first_from 118
X2: first_from equity < seats: 118 of 118 scans
X2: all screens < seats: 0 of 118 scans
X2: marginal-seat tier tally: position 78, priority 6, stickiness 34
X2: every marginal seat decided on position: False
1 passed in 99.56s (0:01:39)
```
`X2: AS EXPECTED` — it ran and tallied; n = 1 day, 118 RTH scans after `first_from` (L8: descriptive). CONSEQUENCE (grok X2): 40 of 118 marginal seats were NOT decided on position (stickiness 34, priority 6) → the dry-run NEVER prints "keeps its seat iff `p ≤ h × c`". Tier rule (first match): held → stickiness (a RETAIN with `below_cap_streak > 0`) → none → priority (group differs) → first_from → position; stated in the module docstring.

### X4
`…/test_h1_x4_rollback_hazard.py` on MAIN's code. `tests/fixtures/radar/radar-screens.real-shape.md` carries NO fenced block (it is the propose-input fixture), so there is no pool block to insert into; the experiment ran on the committed `radar-screens.example.md` and on a SCRATCH COPY (pytest `tmp_path`) of his live `Radar Screens.md`, verbatim:
```
X4 [example fixture]: parse errors 2 (naming handicap: 1) · pool parsed: False · pool.handicap present: False
X4 [example fixture]: load_sources pool_error set: True (names handicap: True) · frozen: True
X4 [his live note (scratch copy)]: parse errors 2 (naming handicap: 1) · pool parsed: False · pool.handicap present: False
X4 [his live note (scratch copy)]: load_sources pool_error set: True (names handicap: True) · frozen: True
2 passed in 0.09s
```
`X4: AS EXPECTED` (main) — FREEZE with `pool_error`, no exception escapes `parse_note_bytes` / `load_sources`; n = 2 notes. Re-run under H1 code at STEP-2's end (below).

### X1
`…/test_h1_x1_blanks.py` (first run hit the grouping error above; re-run after the fix, then re-run once more with the dead-column count split out — the version quoted). Fixtures and per-day summary, verbatim; per-source lines are in the run output and summarised after:
```
X1 fixture radar/pool-metrics.real-shape.csv: equity rows 20 · blank float 0 · blank cap 0
X1 fixture replay/movers-gainers.real-shape.csv: equity rows 31 · blank float 1 · blank cap 1
X1 fixture replay/movers-losers.real-shape.csv: equity rows 41 · blank float 3 · blank cap 0
X1 day 2026-09-17: scans with a DEAD column (R54: handicap inoperative for the scan) 0 of 306 · if a source with no equity row counted as dead: 306 of 306
X1 day 2026-09-18: scans with a DEAD column (R54: handicap inoperative for the scan) 0 of 318 · if a source with no equity row counted as dead: 318 of 318
X1 day 2026-09-21: scans with a DEAD column (R54: handicap inoperative for the scan) 99 of 327 · if a source with no equity row counted as dead: 327 of 327
X1 day 2026-09-22: scans with a DEAD column (R54: handicap inoperative for the scan) 0 of 326 · if a source with no equity row counted as dead: 326 of 326
X1 day 2026-09-23: scans with a DEAD column (R54: handicap inoperative for the scan) 0 of 327 · if a source with no equity row counted as dead: 327 of 327
X1 day 2026-09-24: scans with a DEAD column (R54: handicap inoperative for the scan) 0 of 299 · if a source with no equity row counted as dead: 299 of 299
X1: retained days 6 · scans 1903 · (day, source) MOSTLY BLANK: 0
```
Per source, per day (7 sources = 3 lists + 4 screens): the highest equity-row blank ratio on any (day, source) is 22.896% float / 22.825% cap (a screen, 2026-09-21); every list ≤ 0.563%; `MOSTLY BLANK: 0`. One LIST carries ZERO equity rows on every scan of every day (`equity rows 0`).
`X1: AS EXPECTED` for the STOP rule (no source mostly blank); n = 6 days, 1903 scans. TWO FINDINGS carried: (a) under R54 as built, the handicap would have been INOPERATIVE for 99 of 327 scans on 2026-09-21 (one screen whose every equity row on those scans had a blank float/cap cell) and 0 scans on the other five days; (b) THE VACUOUS CASE: read literally, "every equity row of that source … blank" is TRUE for a source with no equity row, and his all-fund list would make the handicap inoperative on 1903 of 1903 scans. STEP-4A builds "a source with no equity row reaching ranking has no column to judge — neither dead nor live" and ESCALATES it (`## ESCALATE`, ASK DESK).

### X3
`…/test_h1_x3_cell_format.py`, verbatim:
```
X3: cells 1431984 · blank or '-' 259429 · parsed by _number 1172555 · non-blank unparseable 0 · carrying a letter or currency symbol 0
X3: Price × Shares Outstanding vs Market Cap on 587592 rows: ≤1% 440803 · 1–5% 48260 · >5% 98529 · worst relative gap 25.9720
```
`X3: AS EXPECTED` — no suffix, no currency symbol, no unparseable non-blank cell; 75.0% of rows within 1% and no 1000× (M vs B) signature (worst gap 25.97×, a per-name outlier, not a unit). The >5% tail (16.8%) is recorded, not a stop (multi-class share counts / stale caps are data, not units); n = 6 days, 1,431,984 cells.

### X9
`…/test_h1_x9_x10_x15_sources.py::test_x9…`, verbatim: `X9: list exports 13319 · lacking the float header 0 · lacking the cap header 0` · `X9: screen exports 6883 · lacking the float header 0 · lacking the cap header 0`. `X9: AS EXPECTED`; n = 20,202 exports.

### X10
Verbatim: `X10: (scan, ticker) pairs carried by ≥2 sources 37368 · float cells equal 37368, differ 0 · cap cells equal 22756, differ 14612`. `X10: NOT AS EXPECTED` — the CAP cell differs between two sources of one scan in 39.1% of multi-source pairs (float never). Magnitude not measured (any byte difference counted). Consequence (v3's column, not a stop): the verdict follows `source_for[ticker]` and the row stores `source` — built at STEP-4 (`HandicapRecord.source`).

### X5
Offline, verbatim: `X5: pool_unit source_sets[0].metrics keys ['float_m', 'market_cap_m', 'rvol', 'volume']` · `X5: runner.py:322 reads: "source_sets": [item.model_dump(mode="json") for item in source_sets],`. Stored half, inside THE LOCK (19:08:2x): `X5 stored: receipts 0 · carrying a pool_unit value 0 · whose source_sets carry metrics 0` — `cobalt_dev` holds no S5 receipt. `X5: AS EXPECTED` (the dump carries the extra keys; no stored receipt to count, said so).

### X6
Verbatim: `X6: rendered banner: <div class="panel-banner degraded"><b>DEGRADED</b> · Sources: handicap</div>` · `X6: reason rendered: False`. `X6: NOT AS EXPECTED` (only the name renders) — v3 X6's own consequence, NOT a stop: STEP-7 renders the reason. Also found by reading: `runner._pool_row` writes every `decision.degraded_sources` entry with the fixed reason `"source failure"` (`runner.py:371-373`), so the reason must be carried by the `Decision` and written by the runner (ESCALATE 3).

### X7
Verbatim: `X7: poller.py:84: for member in sorted(members, key=lambda item: (item.rank, item.ticker)):` · `X7: runner.py:240: PollMember(item.ticker, item.rank or 10**9)` · `X7: runner.py:245: PollMember(row["ticker"], row.get("last_rank") or 10**9)`. `X7: AS EXPECTED` — the poller sorts `(rank, ticker)` over the `PollMember`s it is given (the transition's `rank`, or `last_rank` when frozen). H1 does not change `Transition.rank`.

### X8
Constructed block (20 / 300, `any`; not his); the low-float screen picked by the substring `low_float` in its key (never printed), verbatim:
```
X8 day 2026-09-17: low-float screen equity rows 7113 · in group 7113 · OUTSIDE 0 · unknown 0
X8 day 2026-09-18: low-float screen equity rows 6432 · in group 6432 · OUTSIDE 0 · unknown 0
X8 day 2026-09-21: low-float screen equity rows 5984 · in group 5984 · OUTSIDE 0 · unknown 0
X8 day 2026-09-22: low-float screen equity rows 4142 · in group 4142 · OUTSIDE 0 · unknown 0
X8 day 2026-09-23: low-float screen equity rows 5081 · in group 5081 · OUTSIDE 0 · unknown 0
X8 day 2026-09-24: low-float screen equity rows 4822 · in group 4822 · OUTSIDE 0 · unknown 0
```
`X8: AS EXPECTED` — 0 outside under the constructed block; n = 6 days. The dry-run's "in the group by construction" sentence is therefore not suppressed by X8 — but the verdict under HIS thresholds is his block's, so the dry-run prints the line only from the day's own count under the block it replays (STEP-6).

### X11
Constructed block, verbatim:
```
X11 day 2026-09-17: tickers 428 · in group at least once 73 · verdict flipped within the day 0 · a tenth of in-group 7.3 · over: False
X11 day 2026-09-18: tickers 390 · in group at least once 59 · verdict flipped within the day 1 · a tenth of in-group 5.9 · over: False
X11 day 2026-09-21: tickers 356 · in group at least once 72 · verdict flipped within the day 2 · a tenth of in-group 7.2 · over: False
X11 day 2026-09-22: tickers 373 · in group at least once 69 · verdict flipped within the day 0 · a tenth of in-group 6.9 · over: False
X11 day 2026-09-23: tickers 322 · in group at least once 62 · verdict flipped within the day 0 · a tenth of in-group 6.2 · over: False
X11 day 2026-09-24: tickers 328 · in group at least once 67 · verdict flipped within the day 3 · a tenth of in-group 6.7 · over: False
```
`X11: AS EXPECTED` — no day exceeds a tenth of its in-group names (max 3 flips); continues, recorded; ASK DESK line under `## ESCALATE`. n = 6 days.

### X15
Verbatim: `X15 day 2026-09-17: screen exports 1109 · with a not-equity row ahead of an equity row 738` · `…09-18: 1151 · 832` · `…09-21: 1184 · 851` · `…09-22: 1181 · 853` · `…09-23: 1184 · 737` · `…09-24: 1074 · 774`. `X15: AS EXPECTED` (measure only; gates H2) — 4,785 of 6,883 screen exports (69.5%) carry a fund ahead of an equity row in export order; NOT fixed ([R2F-02]).

### XL76
Inside THE LOCK (19:08:0x): `COBALT_ENV=dev uv run pytest -q -s tests/experiments/handicap_h1/test_xl76_membership_harness.py`, verbatim:
```
XL76: files naming the three calls (9): test_cards_picks.py test_radar_evaluate.py test_radar_evaluate_cli.py test_radar_panel.py test_radar_replay.py test_radar_runner.py test_radar_store.py test_replay_formations.py test_replay_runner.py
XL76: callers=6
XL76 caller: test_cards_picks.py::TestFillWritesPick::test_fill_writes_exactly_one_pick_row_in_the_fill_transaction
XL76 caller: test_cards_picks.py::TestFillWritesPick::test_pick_row_snapshots_pool_rank_metric_and_value_at_pick_time
XL76 caller: test_cards_picks.py::TestFillWritesPick::test_pick_for_ticker_not_in_pool_records_not_in_pool_and_fill_succeeds
XL76 caller: test_cards_picks.py::TestFillWritesPick::test_degraded_or_missing_pool_row_writes_named_nulls_never_refuses_fill
XL76 caller: test_radar_panel.py::test_members_for_day_db_returns_both_open_and_left_and_scopes_pool_and_day
XL76 caller: test_radar_store.py::test_membership_values_round_trip_retain_and_hold_on_cobalt_dev
-- applying 0001_schemas.sql … -- applying 0013_tunables_slug_nullable.sql
XL76: apply_ms=37
XL76: harness_applies=True
2 passed in 0.15s
```
`XL76: AS EXPECTED` → **DECISION (A)**: `harness_applies=True`. At STEP-5 the H1 store tests and every listed caller whose query names a new column run under ONE fixture `migrated_radar` in ONE new support module `tests/cobalt/radar_migrated_support.py`; `tests/cobalt/conftest.py` is NOT edited. `callers` is a STATIC read (AST); STEP-5's with-DB run is the proof — any other test that fails on a new column is added to the list there. `open_members` is NOT given the new columns (neither the panel nor the dry-run reads it; `OpenMember` is `extra="forbid"`), which keeps the resident's own read untouched.

### COMMIT
`0598c6ac test(radar): H1 STEP-1 first-gate experiments X1–X11, X15, XL76 (v3 L70; L76)` · `git show --stat HEAD`: 12 files, all under `tests/experiments/handicap_h1/` (conftest.py, h1_cache.py, h1_support.py, nine `test_*.py`), `1184 insertions(+)`.

## STEP-2

### T (RED)
New `tests/cobalt/test_radar_handicap.py` (28 tests: six keys / no default / each key missing refused / seventh key refused / factor bounds / both Literal values of `missing`, `mode`, `combinator` / absent block = None and a byte-identical dump / the loud refusal through `parse_note_bytes` + `load_sources` naming `combinator` / a complete block parses under all four `missing × combinator` / `load_config` requires `export.handicap_headers` naming it). Run on the code as it stood, verbatim: `E   ImportError: cannot import name 'HandicapBlock' from 'cobalt.radar.models' (/Users/cobalt/cobalt-wt/handicap-h1/src/cobalt/radar/models.py)` · `1 error in 0.10s`. The "real-shape screens note" of (iii) is `radar-screens.example.md` — the only committed screens note with a pool block (same finding as X4; ESCALATE 6).

### C
- `src/cobalt/radar/models.py`: `HandicapBlock` (six keys, `extra="forbid"`, no default; `factor` `gt=0, le=1`; thresholds `gt=0`); `PoolBlock.handicap: HandicapBlock | None = None`; a wrap serializer drops the key when absent, so the mirror / `pool_unit` dumps of an absent block stay byte-identical.
- `src/cobalt/radar/config.py`: `HandicapHeaders {float, market_cap}`; `ExportConfig.handicap_headers` required; NOT added to `required_headers`.
- `configs/cobalt/radar.yaml`: `git diff` shows ONLY `+  handicap_headers:` / `+    float: Shares Float` / `+    market_cap: Market Cap`.
- GREEN: `28 passed in 0.10s`.
- **X4 re-run under H1**, verbatim: `X4 [example fixture]: parse errors 0 (naming handicap: 0) · pool parsed: True · pool.handicap present: True` · `X4 [example fixture]: load_sources pool_error set: True (names handicap: False) · frozen: True` · `X4 [his live note (scratch copy)]: parse errors 0 (naming handicap: 0) · pool parsed: True · pool.handicap present: True` · `X4 [his live note (scratch copy)]: load_sources pool_error set: True (names handicap: False) · frozen: True` — PARSES; the remaining `pool_error` is the harness's own `finviz_max_rpm=None` ("unmeasured"), not the handicap.

### A1
None needed (see SUITE).

### D
`docs/40 - DevDocs/cobalt/radar/models.md` (+ H1 STEP-2 paragraph), `docs/40 - DevDocs/cobalt/radar/config.md` (+ the handicap headers paragraph).

### SUITE
Offline (19:10–19:19): `2529 passed, 361 skipped, 1 xfailed, 15 warnings in 503.83s (0:08:23)` — **0 failed**; passed = 2501 + 28 new; skipped unchanged. With-DB: the step has no with-DB test (nothing of STEP-2 reaches `cobalt_dev`); no lock taken.
Then two exactness tests were added: `test_a_yaml_float_reaches_the_block_as_its_written_digits` (GREEN at once — pydantic keeps the written digits of a YAML float) and `test_a_factor_finer_than_the_stored_column_is_refused` (RED, verbatim `Failed: DID NOT RAISE <class 'pydantic_core._pydantic_core.ValidationError'>`) → `factor` gains `decimal_places=4` (the NUMERIC(6,4) column of v3 §6; a finer factor could not replay, L57 — ESCALATE 7) → the three radar model/config/notes files `68 passed in 0.32s`. The full offline suite covering these two is STEP-3's.

### COMMIT
`8f178af2 feat(radar): H1 STEP-2 HandicapBlock (six keys, no default) + export.handicap_headers (v3 [F-12], §3)` · `git show --stat HEAD`: `configs/cobalt/radar.yaml | 3 +` · `docs/40 - DevDocs/cobalt/radar/config.md | 4 +` · `docs/40 - DevDocs/cobalt/radar/models.md | 16 +++` · `src/cobalt/radar/config.py | 12 ++` · `src/cobalt/radar/models.py | 34 ++++-` · `tests/cobalt/test_radar_handicap.py | 229 +++` · `6 files changed, 296 insertions(+), 2 deletions(-)`.

## STEP-3

### T (RED)
New `tests/cobalt/test_radar_handicap_group.py` (29 tests): (i) `_collect` over the committed real-shape exports puts `float_m` / `market_cap_m` into `metrics` equal to `_number` of the configured headers, `volume` / `rvol` unchanged, a blank cell → `None`; (ii) the `any` and `all` verdict tables (9 rows each, strict `<` at the threshold, every threshold a literal of the test), a missing metrics row → `unknown`; (iii) every blank-float / blank-cap equity row of `movers-gainers` / `movers-losers.real-shape.csv` is never `no` (and `unknown` under `all`); (iv) the fixture: header == `pool-metrics.real-shape.csv`'s header, ≤ 20 rows, every row the header's width, ≥ 1 blank-float equity row, ≥ 1 fund row, the news / date columns blank; (v) the homogeneous screen: a metric multiplier leaves `_ranked()`'s order unchanged, and the B re-sort moves the screen. RED on the code as it stood, verbatim: `E   ModuleNotFoundError: No module named 'cobalt.radar.handicap'` (collection, so every test of the file was red).

### C
- `src/cobalt/radar/handicap.py` (new): `GroupVerdict`, `handicap_group()` — nothing that sorts.
- `src/cobalt/radar/runner.py`: the `_collect` metrics dict gains `float_m` / `market_cap_m` (that hunk only, at this step).
- FIXTURE (L45): `tests/fixtures/radar/screen-handicap.real-shape.csv` — written with the Write tool from a Read of the retained export `/Users/cobalt/cobalt/data/radar-cache/2026-09-21/screen-down_gappers-150021.csv`: header byte for byte; 7 of its 19 rows (5 equity incl. one with blank float AND cap, 1 fund … 2 equity large/small caps; `No.` values kept); the `News Time` / `News URL` / `News Title` / `Daily Digest` / `Earnings Date` / `IPO Date` / `Dividend Ex Date` cells blanked (dates and attribution out of the content); no date or preset id in the name.
- After C: `28 passed`, and the ONE designed RED, verbatim: `E       ImportError: cannot import name 'shadow_rank' from 'cobalt.radar.handicap'` (`test_the_pool_wide_re_sort_moves_the_homogeneous_screen` — the prompt's "written HERE RED, GREEN at STEP-4").

### A1
None: the runner / replay / evaluate / replay-runner / pool files `96 passed, 2 skipped` with the two new metric keys (no test pins the exact metrics dict).

### D
`docs/40 - DevDocs/cobalt/radar/handicap.md` (new), `docs/40 - DevDocs/cobalt/radar/runner.md` (+ H1 paragraph).

### SUITE
Offline (19:21–19:29): `1 failed, 2559 passed, 361 skipped, 1 xfailed, 15 warnings in 501.45s (0:08:21)`. The ONE failure is the prompt's designed RED `test_the_pool_wide_re_sort_moves_the_homogeneous_screen` (`ImportError: cannot import name 'shadow_rank'`), GREEN at STEP-4; no other red. passed = 2529 + 2 (STEP-2's exactness tests) + 28. No with-DB test in the step; no lock.

### COMMIT
`5693fe41 feat(radar): H1 STEP-3 float/cap into SourceSet.metrics + handicap_group (v3 §3 [F-10])` · `git show --stat HEAD`: `docs/40 - DevDocs/cobalt/radar/handicap.md | 7 +` · `docs/40 - DevDocs/cobalt/radar/runner.md | 4 +` · `src/cobalt/radar/handicap.py | 76 ++++++` · `src/cobalt/radar/runner.py | 4 +` · `tests/cobalt/test_radar_handicap_group.py | 257 +++` · `tests/fixtures/radar/screen-handicap.real-shape.csv | 8 +` · `6 files changed, 356 insertions(+)`.

## STEP-4

### T (RED)
New `tests/cobalt/test_radar_handicap_shadow.py` (17 tests: (i) B exactly — factors, the would-be ranks of the homogeneous pool, `position == raw_rank == rank`, the exact tie → unhandicapped first, the Decimal-vs-float tie; (ii) shadow never sorts — `missing × combinator`, whole-`Transition` equality minus the two handicap fields, with a sticky member in play; (iii) the fields and `HandicapRecord`'s ten keys, no `decisive`, the absent-block NULLs, the record's source / mode / missing / block sha256, an `unknown` name under `apply` and `skip`; (iv) fail-soft: one catch, raw ranking, NULL fields, `handicap` + the exception class in the reason, ONE ERROR record, and a block missing a key never reaching `decide()`; (v) `mode: live`; (vii) a HOLD carries none) and `tests/cobalt/test_radar_handicap_runner.py` (2 tests: the cycle passes `handicap_headers`; `_pool_row` writes `Decision.reasons`). RED on the code as it stood, verbatim: `E   ImportError: cannot import name 'HandicapRecord' from 'cobalt.radar.handicap'` (collection of the shadow file) · `E       KeyError: 'handicap_headers'` · `E       pydantic_core._pydantic_core.ValidationError: 1 validation error for Decision … reasons … Extra inputs are not permitted`.
A TEST OF MINE WAS WRONG FIRST: the Decimal case asserted `3 / 0.1 < 30`, which is false (`assert (3 / 0.1) < 30`). A probe (`$CLAUDE_JOB_DIR/tmp/test_probe_float.py`, run with `uv run pytest`) printed real flips; the first used, verbatim: `(7, '0.28', 25, '24.999999999999996')` — the test now uses raw 7 at factor 0.28 against raw 25 (`# a probe's printed output, copied verbatim`).

### C
- `src/cobalt/radar/handicap.py`: `HandicapRecord` (ten keys, `extra="forbid"`), `ShadowRank`, `shadow_rank()`, `LIVE_NEEDS_H2`.
- `src/cobalt/radar/pool.py`: `Transition` gains `raw_rank`, `handicap_factor`, `handicap`; `Decision` gains `reasons`; `decide(…, *, handicap_headers=None)`; the ONE call site + ONE `try` at **`pool.py:358`** (`except` at `:365`), right after `_ranked()` (`:346`, was `:326`); `raw_rank` / the record ride every transition whose `rank` comes from `ranks` (RETAIN, ADMIT, EXCLUDE, the two ranked LEAVEs); HOLD untouched; `handicap` appended to `degraded_sources` with its reason; the pool-level `degraded` flag unchanged (ESCALATE 8).
- `src/cobalt/radar/runner.py` (outside STEP-3's hunk — ESCALATE 3): the `decide()` call passes `handicap_headers=self.config.export.handicap_headers`; `_pool_row` writes `decision.reasons.get(source, "source failure")`.
- `git diff f6643d41 -U0 -- src/cobalt/radar/pool.py` hunk headers, verbatim: `@@ -11,0 +12 @@` · `@@ -15,0 +17,3 @@` · `@@ -55,0 +60,8 @@ class Transition` · `@@ -69,0 +82,3 @@ class Decision` · `@@ -220,0 +236,2 @@ def decide(` · `@@ -222 +239,4 @@ def decide(` · `@@ -327,0 +348,30 @@ def decide(` · `@@ -330 +380 @@` · `@@ -353 +403 @@` · `@@ -370 +420 @@` · `@@ -402 +452,11 @@` — NONE inside `_metric_position` (94-106) or `_ranked` (109-212).
- GREEN: shadow + runner-seam + group files `47 passed` (the STEP-3 homogeneous test GREEN).

### A1
None: `test_radar_pool.py` compares no whole `Transition` (it asserts fields), and `test_radar_pool.py` / `test_radar_runner.py` stayed green unchanged (`103 passed` beside the new files before the probe fix).

### D
`docs/40 - DevDocs/cobalt/radar/pool.md` (+ H1), `handicap.md` (+ the shadow rank), `runner.md` (+ the two seams).

### SUITE
Offline (19:32–19:41): `2578 passed, 361 skipped, 1 xfailed, 15 warnings in 504.79s (0:08:24)` — **0 failed** (the STEP-3 homogeneous RED is GREEN); passed = 2559 + 1 + 16 + 2. No with-DB test in the step; no lock.

### COMMIT
`a7928964 feat(radar): H1 STEP-4 shadow handicap in decide() — B would-be rank, never sorts, one fail-soft catch (v3 §1 [R26], §6, §7)` · `git show --stat HEAD`: `handicap.md | 4 +` · `pool.md | 22 +++` · `runner.md | 2 +` · `src/cobalt/radar/handicap.py | 117 +++` · `src/cobalt/radar/pool.py | 70 ++++-` · `src/cobalt/radar/runner.py | 8 +-` · `tests/cobalt/test_radar_handicap_runner.py | 47 +++` · `tests/cobalt/test_radar_handicap_shadow.py | 238 +++` · `8 files changed, 493 insertions(+), 15 deletions(-)`.

## STEP-4A

### T (RED)
New `tests/cobalt/test_radar_handicap_dead.py` (11 tests). The scan is two sources built by `_collect` from the committed exports — the redacted screen CSV (its columns blanked / made unparseable / dropped INSIDE the test) and `pool-metrics.real-shape.csv` (live). Run against STEP-4's commit `a7928964`: **6 RED**, verbatim — (i) ×2 `AssertionError: assert Decimal('0.8') == Decimal('1')` · (ii) the same · (iii) missing header, the same · unparseable cells, the same · (iv) `skip`: `AssertionError: assert 'dead column: Shares Float (screen:blanked@00000000000a)' in 'blank float and cap — unknown → not applied'`. **5 GREEN at STEP-4, by construction** — they pin that the new rule changes nothing else and cannot go red without a defect: (v) one blank cell on a live column follows `missing` (×2), (vi) no ERROR logged / factor never NULL, (vii) shadow never sorts on a dead-column scan, and the vacuous-source guard (ESCALATE 1).

### C
`src/cobalt/radar/handicap.py`: `dead_columns()` (**`handicap.py:88`**), `inoperative_reason()`, `INOPERATIVE`; `shadow_rank` calls it (`:170`) BEFORE any factor; a dead scan → factor 1 for every name, every record's reason and the scan's degraded reason `handicap inoperative — dead column: <header> (<source>)`. `pool.py`: no change (the STEP-4 call site already hands the step the headers). No new `try`; no hunk in `_ranked` / `_metric_position`. GREEN: dead + shadow + group + runner-seam files `58 passed in 0.30s`.

### A1
None.

### D
`docs/40 - DevDocs/cobalt/radar/handicap.md` (+ the dead column: R54, the definition, the vacuous reading).

### SUITE
Offline (19:42–19:50): `2589 passed, 361 skipped, 1 xfailed, 15 warnings in 503.51s (0:08:23)` — **0 failed**; passed = 2578 + 11. No with-DB test in the step; no lock.

### COMMIT
`f11836b8 feat(radar): H1 STEP-4A dead column → handicap inoperative at factor 1 for the scan, banner + reason (R54, v3 [F-10])` · `git show --stat HEAD`: `docs/40 - DevDocs/cobalt/radar/handicap.md | 4 +` · `src/cobalt/radar/handicap.py | 47 ++++++-` · `tests/cobalt/test_radar_handicap_dead.py | 193 +++` · `3 files changed, 240 insertions(+), 4 deletions(-)`.

## STEP-5

`ls src/cobalt/db_migrations` before writing: no `0014_*` (the number is this build's, L72 P-b). `placement.py` NOT changed (`radar_membership` is already `Side.SYSTEM`; no new table).

### T (RED)
New `tests/cobalt/test_radar_handicap_store.py` (8 offline + 3 with-DB) and the XL76 (A) support module `tests/cobalt/radar_migrated_support.py` (`migrated_radar`, `SavepointProxy`). Offline RED on STEP-4A's code, verbatim: `ValueError: list.index(x): x not in list` (registry) · `FileNotFoundError: … 0014_radar_handicap.sql` ×2 · `cobalt.db_migrations.cli.MigrationError: no registered migrations are newer…` (`_rollback_paths("0013")`) · `KeyError: 'radar_membership'` (digest exclusion) · `AssertionError: assert 'raw_rank=%s, handicap_factor=%s, handicap=%s::jsonb' in 'UPDATE radar_membership SET … rank_metric=%s, rank_value=%s WHERE …'` · `assert False` (`members_for_day` columns) — `7 failed, 1 passed, 3 skipped`. After C one failure was MY test's regex (it split `NUMERIC(6,4)` at its comma: `('handicap_factor', 'NUMERIC(6')`) — the regex was fixed, not the SQL.

### C
- `src/cobalt/db_migrations/0014_radar_handicap.sql`: `ALTER TABLE system.radar_membership ADD COLUMN IF NOT EXISTS raw_rank INTEGER, … handicap_factor NUMERIC(6,4), … handicap JSONB` (nullable, idempotent, no CHECK — [R2F-03]).
- `…/0014_radar_handicap.rollback.sql`: `DROP COLUMN IF EXISTS` exactly the three.
- `src/cobalt/db_migrations/__init__.py`: docstring lines; `FORWARD` gains `0014` after `0013`; `REVERSE` gains its rollback before `0013`'s.
- `src/cobalt/db_migrations/cli.py` (ESCALATE 3): `TABLE_DIGEST_EXCLUDED_COLUMNS["radar_membership"] = ("raw_rank", "handicap_factor", "handicap")`.
- `src/cobalt/radar/store.py`: `_handicap_json()` (re-validates through `HandicapRecord`); RETAIN / EXCLUDE updates and the INSERT write the three; HOLD and LEAVE untouched; `members_for_day` selects the three; `open_members` unchanged.

### A1 (each re-pointed at the same strength; the `0013` pins kept)
| test | old | new | tag |
|---|---|---|---|
| `test_assumed_store.py::test_0013_is_registered_forward_and_reverse` | `FORWARD[-1]` / `REVERSE[0]` = `0013` | `FORWARD[-2]` / `REVERSE[1]` = `0013` AND `FORWARD[-1]` / `REVERSE[0]` = `0014` | v3 §6 |
| `test_archiver_migrations.py::test_forward_ends_0008_0009_0010_0011` | last five `…0013` | last six `…0013, 0014` | v3 §6 |
| `test_archiver_migrations.py::test_reverse_begins_0011_0010_0009_0008` | first five `0013…` | first six `0014, 0013…` | v3 §6 |
| `test_archiver_migrations.py::test_rollback_down_to_0009_undoes_this_branch_alone_and_0007_also_reaches_p4` | `0013, 0011, 0010` / `0013…0008` | `0014, 0013, 0011, 0010` / `0014, 0013…0008` | v3 §6 |
| `test_archiver_migrations.py::test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it` | `[*range(1,12), 13]`, `numbers[-3:-1] == [10, 11]` | `[*range(1,12), 13, 14]`, `numbers[-4:-2] == [10, 11]` | v3 §6 |
| `test_p4_migrations.py::test_rollback_down_to_0007_reverses_everything_above_p2_newest_first` | `0013` head in the 0007 / 0009 / 0008 lists | `0014, 0013` head in each | v3 §6 |
| `test_tenancy.py::test_down_to_0004_selects_0009_0008_0007_0006_then_0005_reverse` | `selected[:5]` from `0013` | `selected[:6]` from `0014` | v3 §6 |
| XL76 callers → `migrated_radar`, assertions unchanged: `test_cards_picks.py::TestFillWritesPick::{test_fill_writes_exactly_one_pick_row_in_the_fill_transaction, test_pick_row_snapshots_pool_rank_metric_and_value_at_pick_time, test_pick_for_ticker_not_in_pool_records_not_in_pool_and_fill_succeeds, test_degraded_or_missing_pool_row_writes_named_nulls_never_refuses_fill}` (method-level `usefixtures`), `test_radar_panel.py::test_members_for_day_db_returns_both_open_and_left_and_scopes_pool_and_day`, `test_radar_store.py::test_membership_values_round_trip_retain_and_hold_on_cobalt_dev` (`dev_db_tx` → `migrated_radar`) | fixture `dev_db_tx` | fixture `migrated_radar` | L76 / XL76 (A) |

After A1: the migration/store/panel/tenancy/migrate-proof files `22 passed, 7 skipped` (store + p4) and `232 passed` for the wider set, 0 failed offline.

### D
`docs/40 - DevDocs/cobalt/radar/store.md`, `docs/40 - DevDocs/cobalt/db_migrations/__init__.md`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md` (+ H1 paragraphs).

### SUITE
- Offline (19:52–20:01): `2 failed, 2595 passed, 364 skipped, 1 xfailed, 15 warnings in 504.10s (0:08:24)` — the 2 reds were two more BY-DESIGN registry pins the targeted run had not covered (`test_radar_migration.py::test_rollback_selects_only_newer_files_newest_first`, `test_radar_score_migration.py::test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first`: `assert ['0014_radar_...rollback.sql'] == ['0013_tunabl...rollback.sql']`) → re-pointed (A1 rows below) → the two files `23 passed, 26 skipped`. The whole tree was then re-proved by the with-DB suite below (every offline test also runs there) and by STEP-6's offline suite.
- A1, the two late rows: `test_radar_migration.py::test_rollback_selects_only_newer_files_newest_first` — `[:5]` from `0013` → `[:6]` from `0014` · `test_radar_score_migration.py::test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first` — `newest_four` (5 names) and its three `[:5]` → the list with `0014` first and `[:6]`. Same objects, same strength (v3 §6).
- With-DB, THE LOCK (20:02, `## LANE`): the step's files `COBALT_ENV=dev uv run pytest -q -rs … test_radar_handicap_store.py test_radar_store.py test_radar_panel.py test_cards_picks.py test_p4_migrations.py test_archiver_migrations.py test_assumed_store.py` → `229 passed, 2 skipped in 3.55s` (the two skips are `test_cards_picks.py:388` / `:401`, the P2 skips of BASELINE) → `.env` removed, proven gone. Then the full suite, a fresh lock cycle: `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → `2953 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 587.76s (0:09:47)` — **0 failed**; the six skips are BASELINE's six, verbatim the same lines; every XL76 caller GREEN under `migrated_radar`; the rollback-transaction migration tests (`test_archiver_migrations.py`, `test_p4_migrations.py`) GREEN with `0014` in `FORWARD`; no other test failed on a missing column → XL76's static caller list was complete. `.env` removed, proven gone (20:12).

### COMMIT
`a16c97ff feat(db): 0014 — raw_rank, handicap_factor, handicap on radar_membership (float handicap H1, v3 §6)` · `git show --stat HEAD`: 19 files — the migration pair, `__init__.py`, `cli.py`, `store.py`, `radar_migrated_support.py`, `test_radar_handicap_store.py`, the nine re-pointed test files, three DevDocs — `436 insertions(+), 18 deletions(-)`.

## STEP-6

### T (RED)
New `tests/cobalt/test_radar_handicap_dry_run.py` (13: (i) identity on the committed real-shape scan under `missing × combinator` — absent vs a factor-1 block, every pre-H1 field and the order identical, `raw_rank == rank`, `effective_position == position`; `CORE_FIELDS` = the pre-H1 `Transition`; (ii) the dry-run over a constructed two-scan cache day built from the committed exports — scans, the [F-16] header lines, five raw cells, would-be kept/lost/took, the tier tally, the never-printed "iff" sentence, the not-configured h = 1-only pass, the identity over the day, an inoperative scan named; (iii) the `argparse` entry called in pytest — `--day` only (an invented `--factor` → `SystemExit`), a day not in the cache → `DryRunError: 2026-09-03 is not in the cache data/radar-cache`, a malformed day → `DryRunError … YYYY-MM-DD`; (iv) with-DB: the stored-membership comparison against rows THIS test inserts, under `migrated_radar`) and `tests/experiments/handicap_h1/test_x12_identity.py`. RED, verbatim: `E   ImportError: cannot import name 'handicap_dry_run' from 'cobalt.radar'`.

### C
- `src/cobalt/radar/handicap_dry_run.py` (new): the cache reader MOVED from `tests/experiments/handicap_h1/h1_cache.py` with its function bodies unchanged (`mover_exports`, `group_scans`, `CacheCollector`, `collect_scan`, `carry`, `open_rows`, the two regexes, `CachedScan`, `CacheGroupingError`; only the import block grew for the dry-run), then `replay_day`, `core`, `identity_mismatches`, `scan_line` / `_cut_tier`, `dry_run`, `stored_mismatches`, `render`, `command`. `h1_cache.py` is now a re-export of the moved names (no `rm` / `git mv` in this build's allowlist, so the old file could not be deleted; `git diff` shows it shrink by 201 lines while the new module carries the same bodies).
- `src/cobalt/radar/cli.py`: `radar handicap-dry-run --day <YYYY-MM-DD>` → `handicap_dry_run.command`; nothing more.
- GREEN: `12 passed, 1 skipped` (the with-DB test skips offline; it ran with-DB below).
- X2's consequence built: the "keeps its seat iff `p ≤ h × c`" sentence is NEVER printed; "in the group by construction" is not printed either (not needed; the cut-tier tally stands in).
- NOT BUILT (and not in this step's list): [F-16]'s "that day's stored ladder, top ten" — it reads stored CARDS (H3's `card_score` path); ESCALATE 9.

### A1
None.

### D
`docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md` (new), `docs/40 - DevDocs/cobalt/radar/cli.md` (+ the subcommand).

### X12 (retained-day identity)
`uv run pytest -q -s -p no:cacheprovider tests/experiments/handicap_h1/test_x12_identity.py -k "<two days>"`, three runs (one test per retained day; one run over all six exceeded the 10-minute tool ceiling and was stopped before any result — the module was then parametrized by day), his pool block through `notes.parse_note` (read only), the constructed block at factor 1, verbatim:
```
X12 day 2026-09-17: scans 306 · mismatches 0
X12 day 2026-09-18: scans 318 · mismatches 0
X12 day 2026-09-21: scans 327 · mismatches 0
X12 day 2026-09-22: scans 326 · mismatches 0
X12 day 2026-09-23: scans 327 · mismatches 0
X12 day 2026-09-24: scans 319 · mismatches 0
2 passed, 4 deselected in 412.01s · 2 passed, 4 deselected in 413.19s · (the 09-17/18 run) exited 0
```
Summed: **days 6 · scans 1923 · mismatches 0** — every retained day PREFLIGHT listed (2026-09-24 was still growing; 319 scans at the read). On 2026-09-23 two scans lack a `tier_c` list export in the cache (`radar source list:tier_c@5ab5c7188029 failed: list-tier_c-1: no retained export in this scan`); that source degrades identically in both passes, as a failed fetch did in production. `X12: AS EXPECTED`.

### SUITE
- Offline (20:14–20:23): `2609 passed, 365 skipped, 1 xfailed, 15 warnings in 540.13s (0:09:00)` — **0 failed**; passed = 2597 (STEP-5's tree) + 12; the skip count grows only by this build's own with-DB tests (4 since BASELINE: 3 in the store file, 1 here), each run with-DB.
- With-DB, THE LOCK (20:23): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_handicap_dry_run.py` → first run `1 failed, 12 passed`: MY test used a 2040 date and the store's session guard refused it, verbatim `cobalt.session.calendar.CalendarError: no NYSE calendar for 2040 (asked about 2040-01-03). Loaded years: [2025, 2026].` → the test's constructed instants moved to 2026-09-03 10:00 / 10:03 ET (a test-construction fix; the code unchanged) → a fresh lock cycle (20:24): `13 passed in 0.46s`. `.env` removed, proven gone after each.

### COMMIT
`71e0da42 feat(radar): H1 STEP-6 handicap-dry-run + the h=1 identity over every retained day (v3 §7, [F-16], X12)` · `git show --stat -C HEAD`: `cli.md | 2 +` · `handicap_dry_run.md | 5 +` · `src/cobalt/radar/cli.py | 9 +-` · `src/cobalt/radar/handicap_dry_run.py | 517 +++` · `tests/cobalt/test_radar_handicap_dry_run.py | 177 +++` · `tests/experiments/handicap_h1/h1_cache.py | 216 +---` · `tests/experiments/handicap_h1/test_x12_identity.py | 32 ++` · `7 files changed, 756 insertions(+), 202 deletions(-)`.

## STEP-7

### T (RED)
New `tests/cobalt/test_radar_handicap_panel.py` (10 tests, `test_radar_panel.py`'s pattern and helpers: `_small_snapshot` over `panel-pool.real-shape.json`, its first row given this file's CONSTRUCTED `handicap_factor` / `handicap`; the block set into the settings mirror):
- (i) A factor-0.8 row shows `<span class="badge badge-cobalt" title="owner COBALT">HANDICAP (shadow)</span>` and `float 5.1M / cap $88.2M → group (float and cap) · pos 3 → 7`.
- Factor NULL, or factor 1 with verdict `no`, shows no badge and no line.
- Unknown-not-applied shows `float —M / cap $—M → group (unknown) · unknown → not applied` and no badge.
- (ii) The header shows `handicap: shadow`; the block absent shows `not configured`.
- A `handicap` entry in `degraded_sources` gives `handicap: degraded (<reason>)` and, with the pool flag False, the DEGRADED banner `handicap (<reason>)`.
- A dead column gives `handicap: degraded — inoperative (dead column: Shares Float (screen:x@000000000000))`.
- `mode: live` gives `degraded`, never `live`.
- (iii) A handicapped row does not move (episode order identical).

RED, verbatim, first line per kind:
- `E   cobalt.aset.radar_panel.RadarPanelError: FAILED: invalid radar membership row: 2 validation errors for MembershipRecord … handicap_factor  Extra inputs are not permitted [type=extra_forbidden, input_value=Decimal('0.8000'), input_type=Decimal]`
- `E   AttributeError: 'PoolView' object has no attribute 'handicap_state'`
- The summary: `10 failed in 0.17s`.

### C
All in `src/cobalt/aset/radar_panel.py`:
- `MembershipRecord` gains `raw_rank` / `handicap_factor` / `handicap: HandicapRecord | None`. They are required but nullable, the `rank_metric` precedent; `HandicapRecord` is radar's own model, imported.
- `PoolRow` carries the three fields (`exclude=True`); `_row` passes them.
- `_handicap_cell` builds the badge and line in the ticker cell.
- `_handicap_state` sets `PoolView.handicap_state` / `handicap_detail` (`exclude=True`). The R54 prefix is `radar.handicap.INOPERATIVE`, imported, not re-typed.
- `_banner_name` gives the handicap entry its reason. The DEGRADED banner shows on `pool.degraded` OR a `handicap` entry.
- The header shows `handicap: <state> (<detail>)` for a configured block.
- The pool-row sort (`ordered`, `last_rank`) is unchanged.
- No CSS changed; the new classes `handicap-line` / `handicap-state` inherit.

**THE PIN CONFLICT (ESCALATE 11):** the first GREEN run turned `test_radar_panel_cards.py::test_bars_stale_badge_absent_and_output_unchanged_when_healthy[False|True]` red: `AssertionError: 127318e6… == f2e79add…`, the healthy block-absent pool HTML SHA. The prompt asks for two things that conflict:
- "not configured — shown, never implied" in the pool header.
- "a red there is a defect of your change".

Both are kept literally:
- With the block ABSENT, `render_pool` is main's byte for byte.
- `render_radar_page` shows `<div class="pool-meta" id="handicap-unconfigured">handicap: not configured</div>` directly above the pool layer.
- The new view fields are `exclude=True`, so the API pin holds.
- Configured states render in the pool header and refresh with it.
- The test for "not configured" was rewritten after RED to assert this: the page line, and no `handicap:` in the pool layer.

Consequence: the not-configured line is re-read on page load, not on the pool's poll.

GREEN: `tests/cobalt/test_radar_handicap_panel.py tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_aset_web.py` → `165 passed, 1 skipped in 1.64s` (every healthy pin GREEN, `test_radar_panel_cards.py` untouched).

### A1
- `tests/cobalt/test_radar_panel.py` `_small_snapshot` (the `row.setdefault` loop), `_two_current` (the `second.setdefault` site) and `test_bars_stale_badge_never_marks_a_departed_or_excluded_row_sharing_a_stale_ticker` (the `e1c` / `e2c` copies): each gains `setdefault` of `raw_rank`, `handicap_factor` and `handicap` to `None`. This is the same pre-deploy-NULL precedent as `rank_metric` / `rank_value` beside them. The committed `panel-pool.real-shape.json` itself is NOT rewritten (800 rows); the test sets its constructed values on the loaded rows (ESCALATE 12).
- `tests/cobalt/test_radar_panel.py::test_bars_stale_leaves_the_api_json_unchanged`: `set(payload["pool"]) == set(PoolView.model_fields) - {"bars_stale_tickers"}` becomes `- {"bars_stale_tickers", "handicap_state", "handicap_detail"}`. It is the same equality over the same payload; the two new fields are rendered, not serialized.

### D
`docs/40 - DevDocs/cobalt/aset/radar_panel.md` — the STEP-7 section (fields, badge and line, the state table, the banner, the healthy-pin gotcha).

### SUITE
- Offline (20:29–20:37): `2619 passed, 365 skipped, 1 xfailed, 15 warnings in 501.91s (0:08:21)` — **0 failed**. Passed = 2609 (STEP-6) + this step's 10; skipped unchanged.
- With-DB, THE LOCK (20:37): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_handicap_panel.py tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_aset_web.py` → `166 passed in 3.16s`. That includes `test_radar_panel::test_members_for_day_db…` on `migrated_radar`. `.env` was removed and proven gone.

### COMMIT
`9fb8a8e2 feat(aset): H1 STEP-7 /radar pool-row HANDICAP (shadow) badge + header state (v3 §4)` · `git show --stat HEAD` changed 4 files, `275 insertions(+), 6 deletions(-)`:

| file | change |
|---|---|
| `radar_panel.md` | `45 +` |
| `radar_panel.py` | `95 ++-` |
| `test_radar_handicap_panel.py` | `130 +` |
| `test_radar_panel.py` | `11 ++-` |

## EXPERIMENTS

| X | result | the line (verbatim output under `## STEP-1` / `## STEP-6`) |
|---|---|---|
| X1 | AS EXPECTED | no (day, source) mostly blank; R54 dead-column scans 99 of 327 on 2026-09-21, 0 elsewhere (1903 scans); the vacuous case → ESCALATE 1 |
| X2 | AS EXPECTED | marginal seats: position 78 · priority 6 · stickiness 34 → the "iff" sentence never printed |
| X3 | AS EXPECTED | 1,431,984 cells, 0 non-blank unparseable, 0 with a letter or symbol; 75% of rows within 1% of Price × Shares |
| X4 | AS EXPECTED | main: `pool_error set: True (names handicap: True) · frozen: True` — a freeze, not a crash; H1 parses the block |
| X5 | AS EXPECTED | `pool_unit` metrics carry `float_m`/`market_cap_m`; 0 stored receipts on `cobalt_dev` |
| X6 | NOT AS EXPECTED | only `Sources: handicap` rendered, no reason → built at STEP-7 (header + banner carry the reason) |
| X7 | AS EXPECTED | the poller sorts `(rank, ticker)`; H1 leaves `Transition.rank` unchanged |
| X8 | AS EXPECTED | low-float screen equity rows outside the constructed group: 0 on all 6 days |
| X9 | AS EXPECTED | 20,202 exports, 0 lacking either header |
| X10 | NOT AS EXPECTED | cap differs across sources in 14,612 of 37,368 pairs (float never) → verdict follows `source_for`, record stores `source` |
| X11 | AS EXPECTED | ≤ 3 flips a day, under a tenth of in-group every day → ASK DESK (ESCALATE 2) |
| X12 | AS EXPECTED | days 6 · scans 1923 · mismatches 0 (the h = 1 identity) |
| X15 | AS EXPECTED | 4,785 of 6,883 screen exports carry a fund ahead of an equity row (measured; gates H2) |
| XL76 | AS EXPECTED | decision (A): `harness_applies=True`, `apply_ms=37`, `callers=6`; CLOSE: `0014_columns_on_cobalt_dev` under `## CLOSE` |

Tally: **14 / 12 as expected / 2 not**. The grouping pre-check (`test_h1_x0_grouping.py`) is a proof of the reader, not an X.

## L52

- **(a) every number traceable:** float and cap are the export's own cells (`runner.py` `_collect` → `SourceSet.metrics`, `_number` of `export.handicap_headers`); X3 (no suffix / symbol / unparseable, 75% of rows within 1% of Price × Shares Outstanding) and X9 (both headers in every list and screen export); his values by KEY only (`HandicapBlock`); a dead column is never a silent un-handicap — inoperative at factor 1, banner and reason (`handicap.py` `dead_columns`, STEP-4A, R54).
- **(b) no second authority:** in shadow `last_rank` / `rank` are unchanged (the shadow-never-sorts tests), `ladder_order` untouched, ADR-0009 D4 amended at STEP-0.
- **(c) the seam is a real artifact:** the membership row — three columns (`0014`), `HandicapRecord` validated before write (`store.py` `apply_membership`, STEP-5).
- **(d) auditable:** `handicap_group()` and `shadow_rank()` are pure functions over stored inputs (the receipt's `pool_unit` carries the metrics, X5); the dry-run re-derives every retained day (`handicap_dry_run.py`, X12).

## CLOSE

Tip for all three suites: `27df13f1` (STEP-7 `9fb8a8e2` + the absence-probe test commit).

### OFFLINE
`uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider` (20:38–20:47) → `2619 passed, 365 skipped, 1 xfailed, 15 warnings in 506.48s (0:08:26)` — **0 failed, 0 errors**.

Against BASELINE (`2501 passed, 361 skipped`):
- passed = 2501 + 118. The 118 are this build's own offline tests, counted from each step's suite line: STEP-2 … STEP-7 raised passed 2501 → 2619.
- skipped = 361 + 4. The 4 are this build's own with-DB-only tests (3 in `test_radar_handicap_store.py`, 1 in `test_radar_handicap_dry_run.py`), each of which ran GREEN with-DB. BASELINE's 361 skips are unchanged.

→ `offline 2619/0`.

### WITH-DB (L76, THE LOCK 20:47:15 → 20:57:29)
`COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → `2976 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 586.95s (0:09:46)`, with **0 failed, 0 errors**, deselected **2**.
- The six skips are BASELINE's six, verbatim: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262`.
- `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` is GREEN in it: `-q` names no passing test, and no test failed or errored.
- Against BASELINE's `2854 passed`: +122 = 118 new offline tests + the 4 with-DB tests they skip offline.

→ `with-DB 2976/0`.

**THE `0014` ABSENCE PROBE** (same lock, after the suite): `COBALT_ENV=dev uv run pytest -q -s tests/experiments/handicap_h1/test_xl76_membership_harness.py`, verbatim:
```
XL76: callers=9
… (the six STEP-1 callers + test_radar_handicap_dry_run.py::test_the_h1_pass_is_compared_with_stored_membership_read_only + test_radar_handicap_store.py's two with-DB tests — all on migrated_radar)
-- applying 0001_schemas.sql … -- applying 0014_radar_handicap.sql
XL76: apply_ms=33
XL76: harness_applies=True
XL76: 0014_columns_on_cobalt_dev=0
3 passed in 0.17s
```
**`0014: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (XL76)`** · **`cobalt_dev: 0013`**. `.env` was then removed and proven gone (`ls` → `No such file or directory`, 20:57:29).

### EXPERIMENTS RE-RUN ON THE TIP (offline, no `.env`)
The single-call `uv run pytest -q -s tests/experiments/handicap_h1` was started and then stopped (TaskStop) before any result: X12 over six days exceeds the 10-minute tool ceiling. It was re-run as four calls:
- `uv run pytest -q -s tests/experiments/handicap_h1 --deselect tests/experiments/handicap_h1/test_x12_identity.py` → `15 passed, 3 skipped, 6 deselected in 194.63s (0:03:14)`.
  - Skipped: the `cobalt_dev` modules without `.env`, i.e. `test_xl76_membership_harness.py`'s harness test and absence probe, and X5's stored half.
  - Deselected: the six X12 days.
  - X2 and X4 read as recorded: `X2: marginal-seat tier tally: position 78, priority 6, stickiness 34`, and X4 under H1 `parse errors 0 (naming handicap: 0) · pool parsed: True · pool.handicap present: True`.
- X12 in three calls (`-p no:cacheprovider … test_x12_identity.py -k "<two days>"`):
  ```
  X12 day 2026-09-17: scans 306 · mismatches 0
  X12 day 2026-09-18: scans 318 · mismatches 0      (2 passed, 4 deselected in 430.20s)
  X12 day 2026-09-21: scans 327 · mismatches 0
  X12 day 2026-09-22: scans 326 · mismatches 0      (2 passed, 4 deselected in 407.72s)
  X12 day 2026-09-23: scans 327 · mismatches 0
  X12 day 2026-09-24: scans 319 · mismatches 0      (2 passed, 4 deselected in 409.80s)
  ```
  That is 6 days · 1923 scans · **0 mismatches**: the h = 1 identity is proven on the tip.

### LIVE-NOTE (READ-ONLY)
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (BASELINE's command, byte for byte) → `131 passed, 15 warnings in 24.48s`. There is no `SKIPPED` line. The `AWAITING` lines, verbatim:
```
AWAITING A RULING: backside
AWAITING A RULING: fashionably-late
AWAITING A DAY: hitchhiker
AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)
```
This is EXACTLY BASELINE's set, R56's four. → `live-note 131/0`.

### `git diff --stat f6643d41`
`59 files changed, 3855 insertions(+), 45 deletions(-)`. Every path is one named in STEP-0 … STEP-7, or the CLOSE absence-probe test (`test_xl76_membership_harness.py`, the file CLOSE names). None is outside.

Three of those paths sit outside a step's named hunk (ESCALATE 3):
- `runner.py` `decide` kwarg + `_pool_row` reasons
- `db_migrations/cli.py` digest exclusion
- the re-pointed test files (ALWAYS (iv))

### RESTARTS — `uv run cobalt jobs restarts f6643d41..HEAD` (verbatim; run with the report still untracked, so it lists it as `A DOCS`)
```
path	change	rule	restart
configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
docs/10 - Decisions/ADR-0009-radar-cards-seam-and-precondition-ast.md	M	DOCS	-
docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap.md	A	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md	A	DOCS	-
docs/40 - DevDocs/cobalt/radar/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/pool.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/store.md	M	DOCS	-
docs/40 - DevDocs/reports/handicap-h1-build-2026-09-24.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
src/cobalt/db_migrations/0014_radar_handicap.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0014_radar_handicap.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/handicap.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/handicap_dry_run.py	A	static import reach	com.cobalt.radar
src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/pool.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/radar_migrated_support.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_cards_picks.py	M	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_dead.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_dry_run.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_group.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_panel.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_runner.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_shadow.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_store.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/conftest.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/h1_cache.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/h1_support.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x0_grouping.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x1_blanks.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x3_cell_format.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x8_x11_group.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_x12_identity.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_xl76_membership_harness.py	A	test/documentation; no resident	-
tests/fixtures/radar/screen-handicap.real-shape.csv	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No row reads `UNCLASSIFIED`. The expected set (`com.cobalt.radar`, `com.cobalt.aset`) matches.

### `git log --oneline f6643d41..HEAD`
```
27df13f1 test(experiments): H1 CLOSE — the 0014 absence probe on cobalt_dev (L76, XL76; pg_catalog, read-only, rolled back)
9fb8a8e2 feat(aset): H1 STEP-7 /radar pool-row HANDICAP (shadow) badge + header state (v3 §4)
71e0da42 feat(radar): H1 STEP-6 handicap-dry-run + the h=1 identity over every retained day (v3 §7, [F-16], X12)
a16c97ff feat(db): 0014 — raw_rank, handicap_factor, handicap on radar_membership (float handicap H1, v3 §6)
f11836b8 feat(radar): H1 STEP-4A dead column → handicap inoperative at factor 1 for the scan, banner + reason (R54, v3 [F-10])
a7928964 feat(radar): H1 STEP-4 shadow handicap in decide() — B would-be rank, never sorts, one fail-soft catch (v3 §1 [R26], §6, §7)
5693fe41 feat(radar): H1 STEP-3 float/cap into SourceSet.metrics + handicap_group (v3 §3 [F-10])
8f178af2 feat(radar): H1 STEP-2 HandicapBlock (six keys, no default) + export.handicap_headers (v3 [F-12], §3)
0598c6ac test(radar): H1 STEP-1 first-gate experiments X1–X11, X15, XL76 (v3 L70; L76)
4c1c92f2 docs(design): float handicap — R26 pool-wide, R54 dead column
```
That is one commit per step (STEP-0 … STEP-7 with 4A), plus the CLOSE probe test. There are no wip commits.

### EMPTY DIFFS (each its own call against `f6643d41`)
Each of the following gave no output:
- `src/cobalt/radar/evaluate.py`
- `src/cobalt/cards`
- `src/cobalt/replay`
- `src/cobalt/radar/poller.py`
- `src/cobalt/aset/web.py`
- `src/cobalt/vaultwrite`
- `src/cobalt/settings`
- `tests/cobalt/test_radar_panel_cards.py`
- `tests/cobalt/conftest.py`
- `src/cobalt/db_migrations/placement.py`

### L32 SELF-CHECK
- `grep -rn "handicap" configs/cobalt` → `configs/cobalt/radar.yaml:25:  handicap_headers:` — the ONE key. Its two header names (`Shares Float`, `Market Cap`) sit on the next lines and do not carry the word.
- The R28 row was read with the Read tool (via `grep` of its row), and its two numbers were grepped with `grep -rn -F -c` over `handicap.py`, `handicap_dry_run.py`, `tests/experiments/handicap_h1`, the eight new `test_radar_handicap*.py` files and `radar_migrated_support.py`:
  - **R28 value 1: hits 2**
  - **R28 value 2: hits 2**
- All four hits are the same two lines: `tests/cobalt/test_radar_handicap_dry_run.py:162-163`, the microsecond fields of two constructed `datetime`s. These are unrelated literals, not his values.
- Every other file: 0.

### L68 — unmerged branches × the shared paths (`git -C /Users/cobalt/cobalt log --oneline --name-only f6643d41..<branch> -- <the prompt's path list>`)
| branch | shared path | their commits |
|---|---|---|
| `cards/stale-score-0922` | `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_assumed_store.py` (its `0015`, X30 took (A)) | `01ee8bcd` |
| `cards/stale-score-0922` | `tests/experiments/stale_score/*` (a sibling folder, no file shared) | `f0798537`, `3894d1a1`, `2bdc73df`, `358f1f75` |
| `cards/stale-score-0922` | `src/cobalt/aset/radar_panel.py` | none (its X22 found no scorer) |
| `drc/d1-trading-log` (carries DRC K1, `9a0fc900`) | `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py` (`0016`, `0018`) | `d583f6fd`, `96bee451`, `9a0fc900` |
| `voice/v1-0923` | `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py` (`0017`) | `69c376bd`, `28b6b0c6` |
| `bars/chunk-1a-0920` | — | none (empty output) |
| `bars/chunk-2-0920` | `src/cobalt/radar/runner.py` | `31f7109f` |
| `bars/chunk-2-0920` | `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py` (its `0012`) | `02d67a6e` |
| `bars/chunk-e-0920` | `tests/experiments/__init__.py` (NEW there: it makes `tests/experiments` a package; this build's `handicap_h1/` has no `__init__.py`, imports its helpers by rootdir basename — the gate re-proves collection) + `tests/experiments/bars_chunk_e/*` | `a6488d17` … `bab2d19d` (7) |

Every branch that shares `__init__.py` also takes the next migration number after `0014`, so each must re-point its registry pins onto a `FORWARD` list with `0014` in it. The gate re-proves that.

## FOR THE DEPLOY

(the deploy prompt's drafter copies these; this build ran none of them)
- **RESTARTS:** the `cobalt jobs restarts` table under `## CLOSE`, verbatim.
- **THE MIGRATION:** `0014_radar_handicap.sql` forward on production inside the deploy, rollback file `0014_radar_handicap.rollback.sql`; `cobalt db migrate --allow-prod` is the deploy hub's (L61). Production is at `0013` (`deploy-2026-09-24`); if stale score's `0015` ships in the same set, `FORWARD` order applies `0014` first. `DIGEST_EXCLUDED` now carries the three columns for `radar_membership`, so the migrate's own content proof reads `OK`, not `CHANGED` (ESCALATE 3; proven with-DB at STEP-5).
- **THE GATE (L68):** the integrated gate re-proves offline, with-DB (it takes the lock alone and MAY run `TestMigrationRoundTrip` — the deselect is this build's, under L76) and live-note on the combined tree; the `migrated_radar` fixture keeps the membership callers green whatever `cobalt_dev` holds.
- **ORDER, FORWARD:** residents down (L66) → merge → migrate → residents up → the pool runs with the block ABSENT (header `handicap: not configured`) → ONLY THEN may the desk write the block into his note (L65), `mode: shadow` (his value, read after) → read-only parser proof `cobalt radar sources` (no `pool_error`).
- **ROLLBACK, IN THIS ORDER (L65):** (1) the desk removes the `handicap:` block from his note FIRST, parser proof; (2) the code revert (L54 / L68); (3) `0014`'s rollback; (4) residents inside the pause (L43 / L66). Reversed, main's `PoolBlock` (`extra="forbid"`) refuses the key and the pool FREEZES — X4 on main: `pool_error set: True (names handicap: True) · frozen: True`, no exception escapes (a freeze, not a crash).
- **THE PRODUCTION DRY-RUN (read-only, the deploy's own acceptance, X12's second half):** `cobalt radar handicap-dry-run --day <a retained day>` from `~/cobalt` against production `radar_membership` — the `h = 1` pass must match stored membership, 0 mismatches (the command prints `stored membership: matched <n> scans · unmatched <n> · mismatches <n>`).
- **The shadow run** (v3 §7 (2)) starts when the block is written; the `shadow → live` approve is his, not before H3 (O1, [F-12]).

## FOR 45

What the checkers file-check (the executed outputs are quoted in this report): the commit per step (`git log --oneline f6643d41..HEAD` under `## CLOSE`); the B text in v3 as written at STEP-0 against `29` §1 / the derive-r2 report line 43 byte for byte; `_ranked` / `_metric_position` hunk-free (hunk headers under STEP-4); the ONE `try` in `decide()` (its `file:line` under STEP-4); `HandicapBlock` with no default (`test_the_block_has_exactly_the_six_keys_and_no_default`); the shadow-never-sorts test; STEP-4A's `dead_columns()` and its RED-then-GREEN tests (i)–(vii) plus the vacuous case (ESCALATE 1); the identity test and X12's output (STEP-6); the migration pair, its `FORWARD` / `REVERSE` placement after `0013`, and the rollback-transaction tests that prove it (STEP-5); XL76's output, its decision (A) and every caller moved onto `migrated_radar`; each experiment's line with its verbatim output (`## STEP-1`, `## EXPERIMENTS`); BASELINE's and CLOSE's three summaries; the XL76 absence line; the L32 self-check counts; the restarts table; the L68 table; the `27 cite → main line` table; the `## LANE` rows; the edits outside a step's named hunk (ESCALATE 3) and the pool-level `degraded` choice (ESCALATE 8).

## LANE

| time (`date`) | point | (a) `ls -la …/*/.env` | (b) DEVDB-HOLD | (c) after cp | (d) removed | verdict |
|---|---|---|---|---|---|---|
| 18:45:17 | PREFLIGHT (record only) | no matches found | No such file | — | — | free |
| 18:57:54 | BASELINE with-DB | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | exactly one: `-rw------- 1 cobalt staff 2186 Sep 24 18:57 /Users/cobalt/cobalt-wt/handicap-h1/.env` | `.env: removed, proven gone (BASELINE)` 19:08:21 | pass |
| 19:08:2x | STEP-1 XL76 | no matches found | No such file | exactly one (19:08) | `.env: removed, proven gone (STEP-1 XL76)` | pass |
| 19:08:4x | STEP-1 X5 stored half | no matches found | No such file | exactly one (19:08) | `.env: removed, proven gone (STEP-1 X5)` 19:08:43 | pass |
| 20:02:17 | STEP-5 step files (with-DB) | no matches found | No such file | exactly one (20:02) | `.env: removed, proven gone (STEP-5 files)` | pass |
| 20:02:3x | STEP-5 full with-DB suite | no matches found | No such file | exactly one (20:02) | `.env: removed, proven gone (STEP-5 suite)` 20:12:27 | pass |
| 20:23:4x | STEP-6 dry-run file (1st) | no matches found | No such file | exactly one (20:23) | `.env: removed, proven gone (STEP-6 a)` 20:24:01 | pass |
| 20:24:0x | STEP-6 dry-run file (2nd) | no matches found | No such file | exactly one (20:24) | `.env: removed, proven gone (STEP-6 b)` 20:24:13 | pass |
| 20:37:51 | STEP-7 panel files | no matches found | No such file | exactly one (20:37) | `.env: removed, proven gone (STEP-7)` | pass |
| 20:47:15 | CLOSE with-DB full suite + 0014 absence probe | no matches found | No such file | exactly one (20:47) | `.env: removed, proven gone (CLOSE)` 20:57:29 | pass |

## ESCALATE

(numbered as found; the ALWAYS items (i)–(xii) are gathered at CLOSE)

1. **ASK DESK — THE VACUOUS DEAD COLUMN (R54 as built)** [19:0x]: read literally, "every equity row of that source that reaches ranking has that cell blank" is TRUE for a source with NO equity row; X1 shows one of his lists carries zero equity rows on every scan of every retained day, so that literal reading makes the handicap INOPERATIVE on 1903 of 1903 scans. BUILT: a source with no equity row reaching ranking has no column to judge — neither dead nor live (STEP-4A test `test_a_source_with_no_equity_row_reaching_ranking_is_not_dead`). Under the build, 99 of 1903 scans (all on 2026-09-21, one screen) would have been inoperative. Not a stop; one line for the desk: keep this reading, or rule the literal one?
2. **ASK DESK — X11** [19:0x]: verdict flips within a day, constructed block: 0 / 1 / 2 / 0 / 0 / 3 per retained day against in-group 73 / 59 / 72 / 69 / 62 / 67 — under a tenth every day. Latch or not? (Not a stop.)
3. **EDITS OUTSIDE A STEP'S NAMED HUNK (needed, made, named):** `src/cobalt/radar/runner.py` beyond the `_collect` metrics dict — (a) the `decide()` call passes `handicap_headers=self.config.export.handicap_headers` (STEP-4A's dead-column reason names the configured header; `decide()` has no other way to it); (b) `_pool_row` writes `decision.reasons.get(source, "source failure")` instead of the fixed `"source failure"` (X6: without it no handicap reason reaches the pool row or the panel). `src/cobalt/db_migrations/cli.py` — `TABLE_DIGEST_EXCLUDED_COLUMNS["radar_membership"]` gains the three `0014` columns (without it `cobalt db migrate`'s own content proof would read `radar_membership` CHANGED after `0014` and roll the production migrate back; proven with-DB at STEP-5). Unmerged branches touching those files: listed in `## CLOSE` (L68).
4. **X10 NOT AS EXPECTED:** the CAP cell differs between two sources of one scan in 14,612 of 37,368 multi-source pairs (float never). The verdict follows `source_for[ticker]` and the record stores `source`, as v3 requires.
5. **X6 NOT AS EXPECTED:** the panel joined names only; STEP-7 renders the handicap reason.
6. **X4 / STEP-2 (iii) FIXTURE:** `tests/fixtures/radar/radar-screens.real-shape.md` has no fenced block (it is the propose-input fixture). X4 ran on `radar-screens.example.md` and on a tmp scratch copy of his live note; STEP-2's reader test runs on `radar-screens.example.md`.
8. **ASK DESK — how loud is a handicap-only degradation?** BUILT: `handicap` (with its reason) is appended to `Decision.degraded_sources` / the pool row's `degraded_sources`, and the panel renders it in the header state AND a banner — but the pool-level `degraded` flag stays the SOURCES' (unchanged). Why: `cards/picks.py:177-182` records every pick's pool rank as `unavailable: pool degraded (…)` whenever that flag is set, and in shadow the raw ranks are untouched by the handicap, so flipping it would erase valid pick data on every dead-column scan (99 on 2026-09-21). Consequence: the heartbeat radar probe (`heartbeat/probes.py:101-104`, which reads the flag) does NOT page on a handicap-only degradation. If the desk wants the page, the smallest change is in the probe (reading `degraded_sources` regardless of the flag) — not built here.
9. **[F-16]'s "that day's stored ladder, top ten, raw beside would-be" is NOT in the dry-run:** it reads stored CARDS and their `card_score`, the H3 path; STEP-6's own list of lines omits it. Blocks nothing in H1; for the H3 prompt.
10. **`h1_cache.py` could not be deleted** (no `rm` / `git mv` in the allowlist): it is a re-export of the moved reader.
11. **ASK DESK — the healthy pins vs "not configured, shown":** `test_radar_panel_cards.py` SHA-pins the block-absent pool HTML and API JSON, and the prompt forbids touching that file. BUILT: the block-absent pool layer is main's byte for byte, and `handicap: not configured` shows on the page just above it (`#handicap-unconfigured`). It is re-read on page load, not on the pool's poll: after the desk writes the block, the header shows `handicap: shadow` on the next poll, while the stale not-configured line stays until the page reloads. If the desk prefers it inside the pool header, the change is one line in `render_pool` plus a re-pin, which is the desk's to rule.
12. **`panel-pool.real-shape.json` not extended in the file:** the three fields are set to NULL by `setdefault` in `_small_snapshot` (A1). The constructed handicap values are set on the loaded row in `test_radar_handicap_panel.py`; the 800-row committed fixture is unchanged.
7. **`factor` scale:** `HandicapBlock.factor` refuses more than four decimals (`decimal_places=4`). The stored column is NUMERIC(6,4) (v3 §6), and a finer factor would not replay (L57). This is a schema consequence of v3's own column, not a value.

### ALWAYS (i)–(xii)
- **(i) NOT AS EXPECTED / UNPROVEN experiments:**
  - X10: sources disagree on cap. The verdict follows `source_for`, and the record names the source (ESCALATE 4).
  - X6: the panel joined names only; built at STEP-7 (ESCALATE 5).
  - No experiment is UNPROVEN.
- **(ii) The deploy's own acceptance:**
  - The production dry-run `cobalt radar handicap-dry-run --day <retained day>` against production `radar_membership` must read 0 mismatches.
  - After the desk writes the block, the read-only parser proof `cobalt radar sources` must show no `pool_error`.
  - Both are in `## FOR THE DEPLOY`; this build ran neither.
- **(iii) The rollback order:** the desk removes the `handicap:` block from his note FIRST. Reversed, main's `PoolBlock` freezes the pool; X4 found a freeze, not a crash.
- **(iv) A1 re-points, one line each:**
  - STEP-5: the 0014 registry pins in `test_assumed_store`, `test_archiver_migrations`, `test_p4_migrations`, `test_tenancy`, `test_radar_migration` and `test_radar_score_migration`.
  - STEP-5: the XL76 callers moved onto `migrated_radar` (`test_cards_picks` ×4, `test_radar_panel::test_members_for_day_db…`, `test_radar_store::test_membership_values_round_trip…`).
  - STEP-7: `test_radar_panel.py`'s three `setdefault` sites and `test_bars_stale_leaves_the_api_json_unchanged`'s excluded-field set.
  - Every one is listed with its before/after under its step's `### A1`.
- **(v) L68 seams:** the table under `## CLOSE`.
  - `db_migrations/__init__.py` plus the registry pins are shared with `cards/stale-score-0922` (0015), `drc/d1-trading-log` (0016, 0018), `voice/v1-0923` (0017) and `bars/chunk-2-0920` (0012).
  - `runner.py` is shared with `bars/chunk-2-0920`.
  - `tests/experiments/__init__.py` is new on `bars/chunk-e-0920`.
- **(vi) ASK DESK:** 1 (vacuous dead column), 2 (X11 latch), 8 (how loud a handicap-only degradation is), 11 (the healthy pins against "not configured, shown").
- **(vii) MEMORY: / RULING:** none.
- **(viii) R54 as built** (all in `tests/cobalt/test_radar_handicap_dead.py`):

  | Rule | Test |
  |---|---|
  | Scan-wide inoperative | `:112`, `:158`, `:171` |
  | One dead column suffices | `:122` |
  | A missing header is dead | `:128` |
  | Unparseable cells count as blank | `:133` |
  | `skip` does not change the outcome | `:139` |
  | The vacuous case | `:182` |

  X1's dead-column scans: 99 of 327 on 2026-09-21, 0 on the other retained days (ESCALATE 1).
- **(ix) Symbols moved since `d2d82e7`:** the `27 cite → main line` table. None vanished. Moved: `decide` to 215-402, `Transition` to 39-55, `_collect` to 103-168, the S1 `try` to 190-207, the header check to 155-178 and the `sources` subparser to 80-84.
- **(x) LANE STOP:** none. Every lock cycle passed (`## LANE`), and no other holder was seen.
- **(xi) THE DESELECT AND THE HARNESS (L76):**
  - `TestMigrationRoundTrip` was NOT run by this build: it commits every migration to `cobalt_dev`. The deploy's gate runs it.
  - XL76 took decision (A): `migrated_radar` in the NEW support module `tests/cobalt/radar_migrated_support.py`, with `tests/cobalt/conftest.py` untouched. The L68 gate needs it named.
  - CLOSE proof: `0014_columns_on_cobalt_dev=0`.
- **(xii) Live-note:** identical to R56's known state (131 passed, the same four `AWAITING` lines). Nothing to escalate.

**Process disclosures:** the four out-of-shape Bash calls are recorded once, with their times, under `## AUTHORIZATION` (line 48). None was denied, and none touched `.env`, the vault or a DB. At CLOSE, one `uv run pytest -q -s tests/experiments/handicap_h1` (the whole folder) was started and stopped with TaskStop before any result: X12 over six days exceeds the 10-minute tool ceiling, as at STEP-6. It was re-run as the folder with X12 deselected plus X12 in three two-day runs.

## CONTINUE

next: none — the run is complete. The desk verifies the artifact (L35), then launches `prompts/2026-09-24/45-handicap-h1-check-r2.md` (L67). Commits: `4c1c92f2` S0 · `0598c6ac` S1 · `8f178af2` S2 · `5693fe41` S3 · `a7928964` S4 · `f11836b8` S4A · `a16c97ff` S5 · `71e0da42` S6 · `9fb8a8e2` S7 · `27df13f1` CLOSE probe test · then this report's commit. `<main tip>` = `f6643d41`.

HANDICAP H1 BUILT 27df13f1 | on f6643d41 | experiments 14/12/2 | offline 2619/0 | with-DB 2976/0 | live-note 131/0 | migration: 0014 rolled back | cobalt_dev: 0013 | h=1 identity: proven | .env: removed | ESCALATE: 12
