# Bars chunk 2 — build check (hub `bars-chunk-2-check-0920`, 2026-09-20)

## §0 Headline
- Checked branch `bars/chunk-2-0920` (`e15d03e..47ef9af`) from reads alone: **2 of 3 houses** answered (grok, gemini); **astra: METER** (usage limit, no answer). Hub file-checked 45 claims: 36 HOLD, 7 DO NOT HOLD, 2 NOT CHECKABLE FROM READS.
- Both houses: inert YES on the CHECK line, composition SOUND, hard boundary HELD, ready for a deploy prompt **NO** (gemini `FIX FIRST`, grok `STANDS EXCEPT`) — both name the child-name shape (`bars_p_20261026` here vs `bars_p_2026w44` in chunk 1a); the hub confirms it from both branches' files.
- Grok's body also finds the write-failure arm makes a second bounds read main never makes (`poller.py:198`), and test 9 passes for the wrong reason; the hub confirms both, and finds tests 5/5b abort before the row-order path.
- ESCALATE: 13 (incl. one `ASK DESK`: astra could not check a live-write-path chunk).

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | DATE GATE (R23) · `date` | 0 | allowed — `Sun Sep 20 19:41:15 EDT 2026` (before 2026-09-22: gate PASSES) |
| 2 | AUTH · `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | allowed — 6 commits, newest `4e72d65` |
| 3 | AUTH · `grep -n "^\| R13 " …cto-2026-09-20.md` | 0 | allowed — line 86, R13 13:33 ET "Push and approved everything…", BARS TRIBUNAL launch |
| 4 | AUTH · `grep -n "^\| R23 " …` | 0 | allowed — line 206, R23 17:47 ET "yes": `Bash(grok *)`, `Bash(agy *)` stand THROUGH MONDAY 2026-09-21 23:59 ET |
| 5 | AUTH · `grep -n "^\| R25 " …` | 0 | allowed — line 262, R25 17:58 ET "approved": prompts 10 + 11 launch lines, no new rule |
| 6 | AUTH · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R25 \|" -- …cto-2026-09-20.md` | 0 | allowed — `e15d03eac2076366a3009b2d56ac40cba92dd6fc` (non-empty: R25 is committed on main) |
| 7 | STOP-LINE GATE · `tail -n 3 …/bars-chunk-2/docs/40 - DevDocs/reports/bars-chunk-2-2026-09-20.md` | 0 | allowed — last non-blank line starts `BARS CHUNK 2 BUILT ` (quoted below) |
| 8 | `git -C /Users/cobalt/cobalt log --oneline e15d03e..47ef9af` | 0 | allowed — 7 commits (`76e3a77`, `02d67a6`, `c798a0a`, `c941d30`, `31f7109`, `929ff23`, `47ef9af`); non-empty |
| 9 | `git -C /Users/cobalt/cobalt log --oneline -1 bars/chunk-2-0920` | 0 | allowed — branch tip `427c752 docs(report): bars chunk 2 stop line` (above `<tip>`; touches only the builder's report, +2 lines) |
| 10 | `git -C /Users/cobalt/cobalt log --stat --oneline e15d03e..47ef9af` | 0 | allowed — staging list + boundary check (below) |
| 11 | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 12 | `agy --version` | 0 | allowed — `1.2.7` |
| 13 | `ls /Users/cobalt/cobalt-wt/bars-chunk-2` | 0 | allowed — worktree present |
| 14 | `wc -c` branch `poller.py` / main `poller.py` | 0 | allowed — branch **13,236 B**; main **4,981 B** (baseline) |
| 15 | `wc -c` staged `poller.py` / `archiver-store.py` (round-1 copies) | 0 | allowed — 4,981 B = main poller; 14,076 B = main `store.py` (14,076 B). No re-stage needed |
| 16 | `ls scratch/tribunal-bars-0920` | 0 | allowed — `0001_bars.sql`, `models.py`, `poller.py`, `r3/`, `chunk-e-check/` all present |
| 17 | `ls scratch/tribunal-bars-0920/chunk-2-check` | 1 | `ls: …/chunk-2-check: No such file or directory` — RECOVERY: fresh run |
| 18 | THE CODEX PROBE `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answer `OK`, no usage-limit text → **astra: UP** (at 19:4x; the check itself later hit the limit — see `## Packet` house rows) |

Builder's stop line (verbatim, last non-blank line of `bars-chunk-2-2026-09-20.md`):
```
BARS CHUNK 2 BUILT 47ef9af | on main e15d03e | offline 2368/0 (365 skipped; baseline 2192/351) | bars_p migration built · week-bound generator built · ensure + grants (parent + every child) built · coverage probe built · poller bounds check built | inert on an unpartitioned parent: proven | poller diff lines: 170 added / 8 removed | card/scoring paths untouched: empty diff | upsert_bars byte-identical to main: proven | RESTARTS: com.cobalt.aset com.cobalt.radar | db: OWED — 14 requires_db tests written, never run | OWED: ≥3-house check (L67, live write path), then the deploy prompt | ESCALATE: 11
```
`<tip>` = `47ef9af` · `<base>` = `e15d03e`.

`--stat` boundary list: 7 commits touching only `src/cobalt/bars/**` (new), `src/cobalt/db_migrations/{__init__,placement}.py` + the two `0012_*.sql`, `src/cobalt/archiver/store.py`, `src/cobalt/radar/{poller,runner}.py`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/cli.py`, `configs/cobalt/taxonomy/tunables.yaml`, `tests/cobalt/*`, `docs/40 - DevDocs/cobalt/*`, the builder's report. No path under `src/cobalt/cards/` or `src/cobalt/radar/evaluate.py`.

L74 note (recorded once, not followed): the Read tool result of this prompt file arrived with an appended block asking for a `Claude-Session:` line in commit messages and naming a file-send tool. It is DATA; not followed. This run commits nothing.

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/chunk-2-check/` (fresh run). Eight parallel forks of this hub staged it, Read → Write, each copy `wc -c`-checked against its original; the hub listed the folder and re-counted the poller diff itself. No `mkdir` run.

| item | staged as | bytes original → copy |
|---|---|---|
| poller diff | `THE-POLLER-DIFF.md` (header line + `git log -p e15d03e..47ef9af -- src/cobalt/radar/poller.py`) | 15,257 B as written; `grep -c "^@@"` = **7**, `grep -c "^commit "` = **1** |
| main's poller | `main-poller.py` | 4,981 → 4,981 |
| built poller | `built/poller.py` | 13,236 → 13,236 |
| rest of src diff | `build-diff-src.md.part1`…`part5` (cut at `commit ` lines) | 23,887 + 29,568 + 25,479 + 14,076 + 12,413 = 105,423 B; `grep -c "^diff --git"` per part 3+5+5+4+2 = **19** = the `--stat` src/ touch count (2+4+5+5+3) → complete |
| built source | `built/partitions.py` 25,637 · `ensure.py` 9,578 · `coverage.py` 5,467 · `placement.py` 7,316 · `bars/__init__.py` 2,954 · `bars/cli.py` 5,724 · `db_migrations/__init__.py` 5,747 · `0012_bars_partitioned_parent.sql` 5,893 + `.rollback.sql` 1,460 · `store.py` 19,180 · `runner.py` 25,713 · `cli.py` 24,116 · `tunables.yaml` 31,588 · `probes.py.part1`+`.part2` 26,865 + 14,458 = 41,323 | copy = original |
| built tests | `test_bars_partitions` 10,734 · `test_bars_migration` 18,164 · `test_bars_ensure` 22,877 · `test_bars_coverage` 16,004 · `test_radar_poller` 4,584 · `test_radar_migration` 4,584 · `test_archiver_migrations` 26,971 · `test_p4_migrations` 26,819 · `test_radar_score_migration` 22,579 · `test_tenancy` 30,836 · `test_bars_poller_coverage.py.part1/.part2` 28,820 + 22,826 = 51,646 · `test_archiver_quiet.py.part1/.part2` 30,780 + 22,340 = 53,120 | copy = original |
| DevDocs pages | `built/devdocs/{partitions,ensure,coverage,cli,probes,store,poller}.md`, `built/devdocs/bars/__init__.md`, `built/devdocs/db_migrations/__init__.md` | copy = original |
| baselines | `main-store.py` 14,076 · `main-0006.sql` 9,317 · `main-0010.sql` 5,257 · `../0001_bars.sql` 1,347 (= wc of main's) | equal |
| builder's report | `build-report.md.part1`…`part4` (part3 begins `## THE POLLER DIFF`; part4 begins `## SPEC vs CODE`) | 16,975 + 16,520 + 15,613 + 14,545 = 63,653 |
| what the builder was told | `build-prompt.md.part1`+`part2` | 19,373 + 32,280 = 51,653 |
| spec (re-used, verified) | `../chunk-e-check/spec-final-s3.md` (50 lines; `COMPOSITION NOTE` line 13), `spec-final-s6.md` (29), `spec-final-s8.md` (25; row `\| 2 \|` line 16) | not re-staged |
| spec (new) | `spec-final-s2.md` (FINAL 20–53), `spec-final-s4.md` (102–121), `spec-final-s5.md` (122–152), ranges match `grep -n "^## "` | 36 / 22 / 33 lines |
| v3, rulings, gate | `../r3/DERIVED-v3.md.part1/.part2` (present) · `owner-rulings-r19-r25.md` (staged: `../owner-rulings.md` had 0 hits for R22; 8 rows) · `../chunk-e-check/build-report.md.part4` + `chunk-e-check-report.md.part1` (29,400 → 29,400) | |
| `QUESTIONS-CHECK.md` | verbatim from the prompt + the file-list paragraph | written by the hub |

Naming: flat base names under `built/`; collisions keep a subfolder (`built/bars/__init__.py`, `built/bars/cli.py`, `built/db_migrations/__init__.py`, two DevDocs `__init__.md`); `built/cli.py` is `src/cobalt/cli.py`.

Packet defects (recorded, not fatal):
- **Whitespace in the diff copies.** In `THE-POLLER-DIFF.md` and `build-diff-src.md.part*`, every whitespace-only line (38 four-space commit-message blanks, 38 one-space context blanks in the src diff) came out empty (written from tool results): 190 B short of the raw output, one further byte unexplained. Said so in QUESTIONS-CHECK's list. Full-file copies are exact by `wc -c`.
- **Hunk count mismatch:** committed poller diff = **7** `@@` hunks (1 commit); the builder's `## THE POLLER DIFF` narrates **11** (`### Hunk 1` … `### Hunk 11`, `bars-chunk-2-2026-09-20.md:476–593`). The report's quoted diff and the committed diff differ in how many hunks they count (presumably the builder's finer split). The houses read the committed diff.
- Test copies were `wc -c`-compared only, not content-diffed.

House rows (one attempt each, never re-asked):
- **grok**: DONE; wrote `chunk-2-check/grok-check.md` itself (exit 0). `CHECK: BUILD STANDS EXCEPT child-name-shape vs 1a, test-9 newest fixture, ungated write-failure refresh · inert on an unpartitioned parent: YES · composition note: SOUND · hard boundary: HELD · ready for its deploy prompt: NO · child names disagree with 1a's pattern`.
- **gemini**: DONE; its printed answer written byte for byte to `chunk-2-check/gemini-check.md`. `CHECK: FIX FIRST chunk 1a child partition name shape mismatch (`bars_p_<YYYY>w<WW>` vs `bars_p_<YYYYMMDD>`) · inert on an unpartitioned parent: YES · composition note: SOUND · hard boundary: HELD · ready for its deploy prompt: NO · child partition name mismatch against chunk 1a.`
- **astra**: `astra: METER` — probe said UP at 19:4x, the check run then ended (exit 1, ~815 KB of file-read echoes, no final message, no `CHECK:` line) with, verbatim: `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 11:43 PM.` Marker file `chunk-2-check/astra-check.md`.

## CONTINUE
next: (none — the report is complete; the desk reads it as the fourth house).

## Inertness
Each house's (a)(b)(c)(d) IN FULL, unedited, then the hub's file-check.

### gemini
> (a) Clean cycle, fetch failure, write failure, and RTH stale case are explicitly tested hunk by hunk against main's poller on the same store fakes (`test_bars_poller_coverage.py:303`). The built `poll()` makes the same calls in the same order and returns the same `PollResult`. Control differs only to execute the single `self.store.partition_bounds()` read (`built/poller.py:151`).
> (b) The test asserts against MAIN'S BEHAVIOUR. It fetches `src/cobalt/radar/poller.py` out of git, executes it dynamically, and asserts identical behaviour: `assert _comparable(mine) == _comparable(theirs)` and `assert [c for c in mine_store.calls if c[0] != "partition_bounds"] == main_store.calls`.
> (c) The bounds reader can be reached on an unpartitioned parent. It costs one catalog query (`partition_bounds()`) per cycle.
> (d) There is NO path where the new code runs before the bounds verdict is known. The read is inside the `try` block immediately following variable initialization at the start of the `poll` loop (`built/poller.py:151`).

### grok
> **(a) Same calls, same order, same `PollResult` vs `main-poller.py`?**
>
> Shared spine after the one bounds read is today’s: `bucket.acquire` → `fetch` → `watermark` → `closed` filter (`poller.py:162-166` = main `:98-102`) → `upsert_bars` → `StageDropped` name check → `error`/`stopped_at` or `newest` + RTH `stale`. On a plain table `classify_coverage` returns every index covered (`partitions.py` `if not reading.partitioned`) and `submitted is closed` (`poller.py:180`).
>
> | case | same as main? | notes |
> |---|---|---|
> | clean | YES, minus the one bounds read | `submitted is closed`; end-of-cycle refresh skipped (`poller.py:255` `if bounds.partitioned`) |
> | fetch failure | YES, minus the one bounds read | except at `:153-159` = main `:89-95`; no classify; no second read |
> | write failure | NO | after `scrub`, new code always `_refresh_bounds` (`poller.py:198`) then re-classify; main goes straight to `error` + `stopped_at` (`main-poller.py:112-115`) |
> | RTH stale | YES, minus the one bounds read | `newest` from `submitted`; on a plain table `submitted is closed` so the expression is today’s (`poller.py:240-247` = main `:117-124`) |
>
> Branches where control can differ (unpartitioned parent):
>
> | file:line | when | vs main |
> |---|---|---|
> | `built/poller.py:136-142` | `partition_bounds()` raises (not `StageDropped`) | main never reads bounds; would fetch/write; new path returns `CycleAbort(coverage_unknown)` |
> | `built/poller.py:198-200` | write failure, any parent | extra bounds read always; if that read raises → abort `coverage_unknown` instead of `error`+`stopped_at` |
> | `built/poller.py:144-146`, `:174-179`, `:255-261` | partitioned only | `current_period_abort` / end refresh; no-ops when `partitioned=False` |
>
> On a healthy catalog, (a)’s four cases still produce the same failures / written / `stopped_at` as main. The write-failure extra read is the one live-path change F2’s first sentence (“existing poller path unchanged”) does not name.
>
> **(b) The test — main’s behaviour, or a re-description?**
>
> `test_1_inertness_on_an_unpartitioned_parent_matches_main_exactly` (`built/test_bars_poller_coverage.py.part1:303-348`) fetches `main:src/cobalt/radar/poller.py` from git and runs both pollers on the same fakes. That is MAIN’S `poll()`, not a restatement of the new classifier.
>
> Quoted assertion:
>
> ```
> assert _comparable(mine) == _comparable(theirs)
> assert [c for c in mine_store.calls if c[0] != "partition_bounds"] == main_store.calls
> ```
>
> `_comparable` (`:290-296`) keeps only `(ticker, reason, since)`, `written`, `stopped_at`. It drops `aborted`, `unpersisted`, `uncovered`, and `PollFailure.detail`. The call assertion drops every `partition_bounds`. So the test cannot fail on: an extra bounds read (the write-failure refresh), a filled `unpersisted` tally, or a non-None `detail`. `test_1d` (`:368-372`) covers `aborted`/`unpersisted`/`uncovered` only on the clean path.
>
> Verdict: asserts against MAIN’S real `poll()` for the shared fields; it is not a re-description of the new code; it is a **projection**, and the write-failure extra read is invisible to it.
>
> **(c) Bounds reader on an unpartitioned parent, cost per cycle?**
>
> Reached. `poller.py:137` always calls `store.partition_bounds()`. `BarStore._partition_bounds_on` (`store.py:246-253`): one `pg_class.relkind` lookup; `relkind != 'p'` → `PartitionReading(partitioned=False)` and no `pg_inherits` walk. Cost: **one catalog query per cycle**, then pure `current_period_abort` (None) and per-ticker `classify_coverage` (no I/O). A write failure adds a second catalog query (`poller.py:198`). End-of-cycle refresh is skipped.
>
> **(d) New code before the bounds verdict is known?**
>
> No new branch runs *before* the read except main’s existing dropped-carried-failure loop (`poller.py:104-114` = main `:67-81`). The new `try/except` *is* the read (`:136-142`): on success the verdict exists; on failure the cycle aborts `coverage_unknown` without fetch. `current_period_abort` and `classify_coverage` run after `bounds` is bound. No new log or metric before that.

### astra
No answer (METER).

### hub file-check of the above (from `built/poller.py`, `main-poller.py`, `test_bars_poller_coverage.py`)
- **(a)** `built/poller.py:198` — `bounds, retry = self._refresh_bounds(bounds)` — sits in the write-failure `except` arm and is NOT guarded by `bounds.partitioned` (the end-of-cycle refresh at `:255` is). On a plain table a write failure therefore makes a second `partition_bounds()` call that main never makes, also sets `unpersisted[ticker]` (`:197`), and a raising refresh returns `CycleAbort(coverage_unknown)` (`:199-200`, `:285-291`) where main records `error` + `stopped_at` and continues (`main-poller.py:112-115`). A raising FIRST read likewise returns an abort before any fetch (`:136-142`). Gemini's "control differs only to execute the single … read" does not match this; grok's table does. Gemini's `built/poller.py:151` for the read is not the read: it is `await self.bucket.acquire()`; the read is `:137` (grok cites `:137` correctly).
- **(b)** `_comparable` is `test_bars_poller_coverage.py:290-296` (failures as `(ticker, reason, since)`, `written`, `stopped_at`); the call assertion is `:347`; `_main_poller_module` (`:202-236`) runs main's file from `git show main:src/cobalt/radar/poller.py`, so the comparison is real for those fields. `main` is a moving ref: the test compares against whatever `main` holds when it runs.
- **(c)** `store.py:246-253` (relkind lookup, returns `PartitionReading(partitioned=False)` when `relkind != 'p'`) and `:280-283` (`partition_bounds` opens its own connection, `self._connect()`): one new connection + one catalog query per cycle on the plain-table path, two on a write failure. That the real reader answers "not partitioned" on the real `system.bars` is exercised only by `test_bars_poller_coverage.py:1234` (`requires_db`, never run) — NOT CHECKABLE FROM READS.
- **(d)** Before `:136` the new code is only the `_result` closure definition (`:120-130`) and two empty dicts (`:117-118`); nothing runs before the verdict.

## The composition note
### gemini (in full)
> COMPOSITION SOUND. P-closed explicitly includes the period of `max(closed.ts)` in what is defined as "current", and F2 mandates missing current coverage aborts RED. Together, treating missing `max(closed.ts)` periods as RED aborts while treating older holes as historical per-ticker `no_partition` failures perfectly satisfies both rules without contradiction. The CODE implements the composition exactly as FINAL words it in `built/partitions.py:226` (`current_missing`) and handles the detach escalation at `built/poller.py:206`.

### grok (in full)
> **COMPOSITION SOUND.**
>
> F2 (verbatim, `spec-final-s3.md:7-9`) never defines “current”; it aborts on missing current coverage and classifies `no_partition` only for uncovered submitted timestamps. P-closed (verbatim, `:10`) supplies the definition: period of `now` **and** of `max(closed.ts)` when `closed` is non-empty. Historical = older than both. Astra’s “historical-only holes remain local to the affected ticker” is the residual of that definition, not a second veto. Monday 04:00:30 with W0 missing is current under P-closed because that is where every ticker’s `closed` would write — F2 is not contradicted.
>
> Code implements that paragraph, not something else:
>
> - `current_period_abort` (`partitions.py` via the poller-diff hunk at `build-diff-src.md.part1:125-167`): `now`, plus `newest_closed` when given.
> - `classify_coverage` (`:225-228`): `current_missing = current_period_abort(..., newest_closed=max(timestamps)) is not None`.
> - `poller.py:144-146` (before first fetch, `now` only); `:174-179` (per ticker once `closed` exists).
>
> Consequence (a) in the builder’s ESCALATE — grok’s “one ticker one cycle late” is conditional on the detached week being older than that ticker’s newest closed minute — follows from P-closed; it is not a misread. OWNER ITEM only if he wants the walk unconditional against P-closed.

### astra
No answer (METER). No failing sequence was given by either house.

### hub: does the code implement FINAL's composition as worded?
`current_period_abort` `partitions.py:567-608` names `now`'s period and, when given, `newest_closed`'s; `classify_coverage` `:611-681` sets `current_missing` from `current_period_abort(reading, now, newest_closed=max(timestamps))` (`:667-670`) and puts every other uncovered timestamp in `uncovered` with week-range detail (`:653-680`); the poller calls the first check before the first fetch with `now` only (`poller.py:144-146`) and the second per ticker after its `closed` exists (`:171-179`). Two facts the houses did not quote: `closed`/`max(closed.ts)` is **per ticker** in the code (`:178`), and that abort fires **after that ticker's fetch and after earlier tickers in the same cycle may already have committed** (their `written[...]` stand); only `now`'s period is checked before anything is written. `test_6d` (`test_bars_poller_coverage.py:725-749`) asserts the cycle stops (`"BBB" not in result.written`).

## The thirteen poller tests
Columns: `#` · name · present (file:line, original `tests/cobalt/test_bars_poller_coverage.py`) · performs the item (grok / gemini / astra) · wrong-reason risk (grok / gemini / astra) · houses challenging.

| # | name | present | performs | wrong-reason | chall. |
|---|---|---|---|---|---|
| 1 | inertness (4 parametrised cases) | `:303` | YES for shared fields / YES / — | YES — `:347` strips `partition_bounds`; `_comparable` strips `unpersisted`/`aborted`/`detail` / NO / — | 1 |
| 2 | missing period of `now` aborts before first fetch | `:380` (+2b Monday `:404`) | YES / YES / — | NO / NO / — | 0 |
| 3 | unreadable bounds → `coverage_unknown` | `:458` | YES / YES / — | NO / NO / — | 0 |
| 4 | historical hole: covered rows, one `no_partition` | `:504` (4b–4f `:518-559`) | YES / YES / — | NO / NO / — | 0 |
| 5 | current-only and BOTH, either row order | `:571`, `:587` | YES / YES / — | NO / NO / — (hub: both abort at `poller.py:144-146`, see claim 16) | 0 |
| 6 | detach between bounds read and write | `:627` (6b `:650`) | YES / YES / — | NO / NO / — | 0 |
| 7 | zero-submitted-row cycle refreshes coverage | `:757` (7b, 7c) | YES / YES / — | NO / NO / — | 0 |
| 8 | non-routing write error keeps `error`, no range | `:801` (8b `:813`) | YES / YES / — | NO / NO / — | 0 |
| 9 | `newest` from persisted rows + prior watermark | `:825` (9b `:850`, 9c `:887`) | NO — does not perform the freshness claim; 9b is the Monday abort / YES / — | YES — gap bar 1 week old, watermark 10 min old, both `> max_age_s=180`, `stale` planted either way / NO / — | 1 |
| 10 | historical `no_partition` preserved through error-success | `:898` (10b, 10c) | YES / YES / — | NO / NO / — | 0 |
| 11 | rolled-back batch recorded separately from uncovered | `:942` (11b `:968`) | YES / YES / — | NO / NO / — | 0 |
| 12 | operator DETACH inside a scan, one ticker one cycle late | `:667` (`test_6c`, docstring "TEST 12"; other branch `test_6d` `:725`) | YES for a historical DETACH / YES / — | NO / NO / — | 0 |
| 13 | `StageDropped` propagates untouched | `:980` (13b `:994`, 13c `:1007`) | YES / YES / — | NO / NO / — | 0 |

Present: 13 of 13 (both houses; hub opened lines 1–1115 and 1195–1284). No test is numbered 12 in the file (the fork's map). Exception parsing: `test_nothing_in_the_poller_parses_the_exception` `:1026-1055`; `StageDropped` name check identical in shape to main (`poller.py:190-191` = `main-poller.py:110-111`; same shape at `:139-140`, `:288-289`).

## Migration 0012, ensure and the probe
| item | grok | gemini | astra | hub file-check |
|---|---|---|---|---|
| empty parent, `PARTITION BY RANGE (ts)`, PK `(ticker, interval, ts)` | yes | yes | — | HOLDS `0012_…sql:73-84` |
| `CHECK (interval = 'i1')` | yes | yes | — | HOLDS `:83` (`bars_p_interval_is_i1`) |
| no `DEFAULT` partition | yes | yes | — | HOLDS (none in the file) |
| OWNER TO cobalt_system + explicit grants | yes; "0006's OWNER + explicit GRANT pattern, not 0006's `SELECT, REFERENCES` list" | yes "(`main-0006.sql` style)" | — | `:106-109`: OWNER, `GRANT ALL … cobalt_system`, `GRANT SELECT … cobalt_user`; `main-0006.sql:198-199` uses `SELECT, REFERENCES` to `cobalt_user` and no `GRANT ALL` — grok's wording HOLDS |
| column list identical to `../0001_bars.sql` | yes | yes | — | HOLDS `:74-81` vs `0001_bars.sql:19-26`; parser test `test_bars_migration.py:214` |
| no `DROP`/`TRUNCATE`/`DETACH`, never names `system.bars` | yes (boundary regex test) | yes "the text contains no …" | — | executable SQL HOLDS (tests scan comment-stripped code, `test_bars_migration.py:279, 283`); the RAW text does name them in comments (`:10`, `:11`, `:68`; rollback `:6`, `:8-11`) |
| rollback drops only the relation it created | yes | yes | — | HOLDS `rollback.sql:27` (`DROP TABLE IF EXISTS system.bars_p;`, no `CASCADE`) |
| `FORWARD`/`REVERSE` order; `0012` free | yes | yes | — | HOLDS: 02d67a6 diff of `db_migrations/__init__.py` — FORWARD ends `0011`, `0012`; REVERSE begins `0012`, `0011`; base registry ended `0011` |
| plan reaches back to `min(ts)`, forward `horizon`, contiguous, no DEFAULT | yes | yes | — | HOLDS `partitions.py:242-297` (start = `min(min_ts, now)`, `week_bounds` to `now + horizon`) |
| idempotent (second plan empty, existing child untouched) | yes | yes | — | HOLDS as to logic (`:281-297` matches existing children by STORED BOUND TEXT); tests `test_bars_ensure.py:150, 163`. That the server's `pg_get_expr` text equals `render_bound`'s text: NOT CHECKABLE FROM READS — settled by `test_a_childs_bounds_are_exactly_what_the_generator_emits` on `cobalt_dev` |
| no `DETACH`/`DROP`/`TRUNCATE` in the statement set (R22) | yes | yes | — | HOLDS `ensure.py:138-156` (only `CREATE TABLE IF NOT EXISTS … PARTITION OF` and `GRANT`); test `test_bars_ensure.py:210` |
| grants applied AND asserted on parent AND every child, loud | grok: applied to `plan.missing`, asserted on parent + missing, "not re-asserted on `plan.present`"; ACCEPTABLE | gemini: "parent and every child" | — | `ensure.py:248-251`: asserted on `[PARENT_TABLE] + plan.missing` only; an existing child is not re-asserted — grok's wording HOLDS, gemini's does not |
| `ensure` refuses an unpartitioned relation loudly | yes | yes | — | HOLDS `ensure.py:222-235`; `test_bars_ensure.py:306` |
| wired to no resident / cron | yes | yes | — | HOLDS `test_bars_ensure.py:380-390`: scans each job spec's `label` + `what` for `"bars partitions"` / `"partitions ensure"` |
| bound generator: contiguity 2026–2027; no bound in 04:00–20:00 ET; 169 h / 167 h; `TO(n)` = `FROM(n+1)`; instant an argument | yes | yes | — | HOLDS: tests `test_bars_partitions.py:49, 59, 87, 111`; `week_of`/`week_bounds` take instants (`partitions.py:155-193`); grok says the CLI reads the clock and passes it in (`bars/cli.py`, not re-opened by hub) |
| probe inert before swap, decided before config is read | yes | yes | — | HOLDS `probes.py:492-500`; `coverage_verdict` `partitions.py:439-446`; tests `test_bars_coverage.py:187, 360, 369` |
| by bounds, never a child count | yes | yes | — | HOLDS `partitions.py:448-469` (duration off the contiguous region); `test_bars_coverage.py:153` |
| U1: loud refusal, never a default, never 15 | yes | yes | — | HOLDS `coverage.py:52-100` (`CoverageUnknown`), `tunables.yaml:852` `value: null`; tests `:240, 293, 393`; `test_bars_coverage.py:306` asserts `"15"` absent from the module body |
| AMBER/RED/margin rows `status: proposed` with citation | yes (`:866-900`) | yes | — | HOLDS: `tunables.yaml:852, 866, 880, 891` — `status: proposed`, `source: ruling`, citations in `consumers` |

## The hard boundary
Hub: `git -C /Users/cobalt/cobalt log --oneline e15d03e..47ef9af -- src/cobalt/cards src/cobalt/radar/evaluate.py` → **EMPTY** (recorded verbatim: no output). Also EMPTY: `… -- src/cobalt/archiver/cli.py src/cobalt/archiver/collector.py src/cobalt/radar/evaluate_cli.py src/cobalt/aset`.

| item | grok | gemini | astra | hub |
|---|---|---|---|---|
| per-target lock | HELD (`test_the_poller_holds_no_lock_and_no_generation`) | HELD | — | HELD in code: `test_bars_poller_coverage.py:1058-1070` scans comment-stripped `poller.py`; no lock in `poller.py` |
| generation | HELD | HELD | — | HELD, same scan |
| `complete` | HELD (builder claim; packet diff does not touch it) | HELD | — | no diff under `cards/` or `evaluate.py` (EMPTY above); `poller.py` diff names no `complete` |
| any detector's refusal | HELD (no detector module in the src diff) | HELD | — | EMPTY above; `runner.py` +18/−0 only (`31f7109`) |
| card paths | nothing reaches a card | — | — | `git log` EMPTY above |
| cycle abort reaches the runner via | existing `stamp_failure(…, failed_stage="bars")` (`runner.py:302-319`), `CycleAbort` rides on `PollResult.aborted`, not raised | same, cites `built/runner.py:326` | — | HOLDS `runner.py:302-319` (gemini's `:326` is the sibling `except StageDropped`; the calls are `:312`, `:322`) |

## ESCALATEs and READINGs
Builder's `## ESCALATE` (i)–(xi) and its 6 READINGs; `SPEC vs CODE` = 18 rows.

| item | house | verdict — reason verbatim |
|---|---|---|
| SPEC vs CODE, 18 rows | gemini | "All 18 items ACCEPTABLE." |
| SPEC vs CODE | grok | ACCEPTABLE except two rows: **inert "byte for byte" — WRONG — `poller.py:198` refresh is not gated on `bounds.partitioned`; write-failure is not main's path**; **child names vs 1a — WRONG as a stacked seam** |
| (i) 1 module path | gemini / grok | narrowest YES / narrowest YES — "a `cobalt <noun>` command" / `cli.py:490-510` layout |
| (i) 2 child names `bars_p_YYYYMMDD` | gemini | **WRONG — chunk 1a expects `bars_p_<YYYY>w<WW>`, this branch emits `bars_p_<YYYYMMDD>`** |
| (i) 2 | grok | narrowest YES locally; **NO against 1a's `bars_p_<YYYY>w<WW>`** — "QUESTIONS-CHECK ninth" |
| (i) 3 operator `Side.SYSTEM` | gemini / grok | narrowest YES / narrowest YES — ADR-0008 D1 one-factory lint |
| (i) 4 ANY hole vs AMBER | gemini / grok | narrowest YES / narrowest YES — "literal reading makes AMBER unreachable"; grok: OWNER ITEM if he wants every forward shortfall RED |
| (i) 5 probe reads `system.bars` | gemini / grok | narrowest YES / narrowest YES |
| (i) 6 uncovered range = the week `ensure` would create | gemini / grok | narrowest YES / narrowest YES — L57 |
| (ii) 14 `requires_db` never run | gemini / grok | ACCEPTABLE / ACCEPTABLE — "not a defect (L70); first run OWED before deploy" |
| (iii) placement one row; children unruled until 1a | gemini / grok | ACCEPTABLE / ACCEPTABLE as stated; "name-shape mismatch is the real seam" |
| (iv) U1 loud refusal | gemini / grok | ACCEPTABLE / ACCEPTABLE |
| (v) U20/U21 not invented | gemini / grok | ACCEPTABLE / ACCEPTABLE |
| (vi) deploy-prompt notes | gemini / grok | ACCEPTABLE / ACCEPTABLE |
| (vii) composition (a)(b) | gemini / grok | ACCEPTABLE / ACCEPTABLE — "consequences, not mis-builds"; OWNER ITEM only if he wants the walk unconditional |
| (viii) named range not persisted | gemini / grok | ACCEPTABLE / ACCEPTABLE — "OWNER ITEM for a later card-facing surface" |
| (ix) DevDocs symbol check absent | gemini / grok | ACCEPTABLE / NOT CHECKABLE FROM READS — L70, not a defect |
| (x) heredoc outside the bare-shape rule | gemini / grok | ACCEPTABLE / **OWNER ITEM for launch hygiene, not this code** |
| (xi) pre-existing tests rewritten, not loosened | gemini / grok | ACCEPTABLE / ACCEPTABLE from the report's account |
| anything the design REQUIRED that is absent from `built/` | gemini / grok | "Nothing required by the design is missing from `built/`." / "None found that this packet can see, except: whether `bars_coverage` is invoked by the heartbeat run loop" |

**The child-name-shape seam (question NINTH).** This branch: `partitions.py:86-98` — `child_name` → `f"{PARENT_TABLE}_{monday.astimezone(ET).strftime('%Y%m%d')}"`, i.e. `bars_p_20261026` for the week of Monday 2026-10-26 (`test_bars_partitions.py:239` asserts `bars_p_20261026`; grok's own reading of the test). Chunk 1a (`git -C /Users/cobalt/cobalt show bars/chunk-1a-0920:src/cobalt/db_migrations/placement.py`, branch tip `8dddf2b`, after its fix X9): `_PARTITION_CHILD = re.compile(r"^bars_p_(?P<year>[0-9]{4})w(?P<week>[0-9]{2})\Z")` — its comment records `bars_p_<YYYY>w<WW>` as a `READING:` "because the child name shape is not readable from `main`", and `patterned_side` returns `None` for any other name, so `side_of("bars_p_20261026")` raises `KeyError`. The two spellings for the same week: **`bars_p_20261026`** (this branch) vs **`bars_p_2026w44`** (chunk 1a's shape; grok's spelling — ISO week 44 by arithmetic, not run). This branch's report ESCALATE (iii) (`build-report.md.part4:71-79`) names that the children have no placement rule until 1a's pattern lands, OWED to the stacked-tree gate, but not the shape difference; its READING (i)2 says "Nothing names them". `placement.py`: this branch's edit is +10 lines in `CREATED_TABLES` (a 9-line comment block and the one row `"bars_p": Side.SYSTEM`), no neighbour reflowed, no second pattern rule (`git log -p -1 02d67a6 -- src/cobalt/db_migrations/placement.py`).

## Checked against the branch
Originals: `/Users/cobalt/cobalt-wt/bars-chunk-2/…` (Read), main under `/Users/cobalt/cobalt/`, shas via `git -C /Users/cobalt/cobalt show|log`. G = gemini, K = grok. Line numbers are the ORIGINAL files'.

| # | claim · who | file:line | verdict | note |
|---|---|---|---|---|
| 1 | control differs only in one bounds read (`built/poller.py:151`) · G | `poller.py:136-142`, `:197-200` | DOES NOT HOLD | write-failure arm makes a second read + `unpersisted`; a raising first read aborts; `:151` is `bucket.acquire` |
| 2 | write-failure arm always refreshes, main goes straight to `error` · K | `poller.py:198`; `main-poller.py:112-115` | HOLDS | `_refresh_bounds` unguarded by `bounds.partitioned` |
| 3 | raising `partition_bounds()` aborts `coverage_unknown` with no fetch · K | `poller.py:136-142` | HOLDS | main never reads bounds |
| 4 | `_comparable` keeps 3 fields; call assertion drops `partition_bounds` · K | `test_bars_poller_coverage.py:290-296, 347` | HOLDS | write-failure extra read is invisible to test 1 |
| 5 | test 1 runs main's real `poll()` from git · G, K | `:202-236, 312, 342, 344, 347` | HOLDS | for the compared fields; `main` ref is live |
| 6 | one catalog query per cycle on a plain table, a second on write failure · G, K | `store.py:246-253, 280-283`; `poller.py:137, 198` | HOLDS | each `partition_bounds()` opens its own connection |
| 7 | real reader answers "not partitioned" on the real plain `system.bars` · G, K | `test_bars_poller_coverage.py:1234` | NOT CHECKABLE FROM READS | run: that `requires_db` test on `cobalt_dev` |
| 8 | nothing new runs before the bounds verdict · G, K | `poller.py:117-130, 136-142` | HOLDS | closure def + two dicts only |
| 9 | code implements the composition as FINAL words it · G, K | `partitions.py:567-608, 667-670`; `poller.py:144-146, 174-179` | HOLDS | `closed` is per ticker (`:178`); see composition section |
| 10 | `current_missing` at `built/partitions.py:226` · G | `partitions.py:553, 668` | DOES NOT HOLD | line reference wrong; substance holds |
| 11 | detach escalation at `built/poller.py:206` · G | `poller.py:204-209` | HOLDS | `after.current_missing` → abort |
| 12 | `poller.py:151` is the bounds read · G | `poller.py:151` | DOES NOT HOLD | `:151` is `await self.bucket.acquire()`; read is `:137` (same claim as row 1's citation; counted once more for the "(d)" citation) |
| 13 | none of the 13 tests passes for the wrong reason · G | tests 1, 5, 5b, 9 | DOES NOT HOLD | see rows 14–16 |
| 14 | test 1 can pass for the wrong reason (projection) · K | `:290-296, 347` | HOLDS | the `write_failure` case's second read is stripped |
| 15 | test 9 passes for the wrong reason · K | `:825-847`; `poller.py:160-166` | HOLDS | `gap` (NOW−7d) ≤ `threshold` (watermark−2 min) so `closed`=[]; `stale` comes from the watermark either way; no `no_partition` asserted |
| 16 | tests 5 / 5b cannot pass for the wrong reason · K (G: NO) | `:571-583, 587-610`; `poller.py:144-146` | DOES NOT HOLD | reading covers only an old/middle week, so `now`'s period is missing → abort at `:144-146` before any fetch; row order never reached |
| 17 | nothing parses `e`; only `type(e).__name__` · G, K | `poller.py:139, 142, 190, 288, 291`; test `:1026-1055` | HOLDS | every `str(e)` is `scrub(str(e))` |
| 18 | `StageDropped` name check is main's · G, K | `poller.py:190-191` = `main-poller.py:110-111` | HOLDS | same `except BaseException` shape |
| 19 | `upsert_bars`/`upsert_bars_on` additions-only · G, K | `git log --numstat` `store.py` `112 0` (`c941d30`); diff read in full | HOLDS | new `datetime` import, `_parse_bound_literals`, `_partition_bounds_on`, `partition_bounds` |
| 20 | no compensating rollback logic · G, K | `poller.py:197` (`len(submitted)`); `:184-223` | HOLDS | E-12 itself not re-run |
| 21 | 0012 shape: PK, CHECK, no DEFAULT, owner, grants · G, K | `0012_…sql:73-109` | HOLDS | |
| 22 | raw 0012 text contains no DROP/TRUNCATE/DETACH and never names `system.bars` · G | `0012_…sql:10, 11, 68`; rollback `:6, 8-11` | DOES NOT HOLD | true of executable statements; comments name them |
| 23 | column list identical to 0001 · G, K | `0012:74-81`; `0001_bars.sql:19-26` | HOLDS | |
| 24 | grants follow `main-0006.sql` pattern · G, K | `0012:106-109`; `main-0006.sql:198-199` | HOLDS | as K words it (pattern, not the same list) |
| 25 | rollback drops only `system.bars_p` · G, K | `rollback.sql:27` | HOLDS | |
| 26 | FORWARD/REVERSE order; `0012` free · G, K | 02d67a6 `__init__.py` diff | HOLDS | |
| 27 | grants asserted on parent AND every child · G | `ensure.py:248-251` | DOES NOT HOLD | parent + `plan.missing` only |
| 28 | grants asserted on parent + new children only · K | `ensure.py:248-251` | HOLDS | |
| 29 | `ensure` refuses a non-partitioned relation · G, K | `ensure.py:222-235`; `test_bars_ensure.py:306` | HOLDS | |
| 30 | statement set has no DETACH/DROP/TRUNCATE · G, K | `ensure.py:138-156`; test `:210` | HOLDS | |
| 31 | `ensure` is in no resident / cron · G, K | `test_bars_ensure.py:380-390` | HOLDS | test scans `label` + `what` of each job spec |
| 32 | generator: contiguity, no bound in 04:00–20:00, 169 h / 167 h, TO=FROM, instant an argument · G, K | `partitions.py:155-193`; tests `test_bars_partitions.py:49, 59, 87, 111` | HOLDS | |
| 33 | plan reaches back and forward, idempotent · G, K | `partitions.py:242-297`; tests `test_bars_ensure.py:150, 163` | HOLDS | |
| 34 | existing children match the server's stored bound text · builder (ii) / G, K | `partitions.py:281-297` | NOT CHECKABLE FROM READS | run: `test_a_childs_bounds_are_exactly_what_the_generator_emits` on `cobalt_dev` |
| 35 | probe inert before the swap, before config · G, K | `probes.py:492-500` | HOLDS | |
| 36 | probe judges by bounds · G, K | `partitions.py:448-469`; `test_bars_coverage.py:153` | HOLDS | |
| 37 | U1 loud refusal, never 15 · G, K | `coverage.py:52-100`; `tunables.yaml:852`; `test_bars_coverage.py:240, 293, 306` | HOLDS | |
| 38 | thresholds/margin `status: proposed` with citation · G, K | `tunables.yaml:852, 866, 880, 891` | HOLDS | |
| 39 | whether the heartbeat runner calls `bars_coverage` is not checkable · K | `heartbeat/runner.py:131-148`; `grep -rn bars_coverage src/cobalt` | HOLDS (resolved) | `__all__` omits it (K); the hub finds no caller: `take_beat` lists 12 probes, none is `bars_coverage`; only `probes.py` names it; the branch does not touch `heartbeat/runner.py`; the build prompt (step 4, `build-prompt.md.part2:39`) asks for the probe "in `heartbeat/probes.py` beside `archiver_freshness`" |
| 40 | hard boundary: lock, generation, `complete`, detector refusal all HELD · G, K | `test_…:1058-1070`; `git log` EMPTY | HOLDS | |
| 41 | abort reaches the runner via the existing `failed_stage` device · G, K | `runner.py:302-319` | HOLDS | G's `:326` is off (`:312`, `:322`) |
| 42 | named range in memory only; `stamp_poll` writes `{ticker, reason, since}` · K | `runner.py:288-290`; `poller.py:37-50` | HOLDS | |
| 43 | placement edit is exactly one row, no second pattern · G, K | 02d67a6 `placement.py` diff | HOLDS | +10 lines: 9 comment + 1 row |
| 44 | child shape `bars_p_YYYYMMDD` vs chunk 1a `bars_p_<YYYY>w<WW>` · G, K | `partitions.py:86-98`; `1a:placement.py` `_PARTITION_CHILD` | HOLDS | both spellings quoted above |
| 45 | report names the placement gap as OWED, not the shape · (hub) | `build-report.md.part4:71-79` | HOLDS | shape difference not named in (iii) |

Hub observations NOT raised by a house (facts from files, no recommendation):
- **O1 — `PollFailure.detail` has no reader.** `grep -rn "no_partition\|\.detail" src/cobalt/radar src/cobalt/aset`: the only writers are `poller.py:216, 232`; the runner builds its persisted rows from `ticker, reason, since` only (`runner.py:288-290`) and rebuilds carried records with no `detail` (`runner.py:270-277`); the poller's `failures.setdefault((ticker, NO_PARTITION), …)` (`poller.py:230-233`) keeps a carried record (detail `None`) rather than the new one. So the named range is on no log line, no health row and no persisted row today; the builder's (viii) says "in memory for the cycle … recomputed from the bounds every cycle".
- **O2 — order at the runner.** `stamp_poll(… polled_at=instant …)` runs at `runner.py:286-296` for an aborted cycle too; `stamp_failure(failed_stage="bars")` follows at `:302-319`; the S5 evaluate stage (`:333`) still runs afterwards, as it does for the existing `lifecycle_refusal` device (`:320-329`).
- **O3 — a per-ticker abort after earlier commits.** The P-closed abort at `poller.py:174-179` can fire on ticker N after tickers 1…N−1 committed in the same cycle (`test_6d` asserts only that later tickers are not written).

## Ready for a deploy prompt
| house | ready | reason (verbatim) |
|---|---|---|
| grok | NO | "child names disagree with 1a's pattern" (`CHECK: BUILD STANDS EXCEPT child-name-shape vs 1a, test-9 newest fixture, ungated write-failure refresh`) |
| gemini | NO | "child partition name mismatch against chunk 1a" (`CHECK: FIX FIRST …`) |
| astra | — | METER, did not check |

Facts from the hub's own file-check:
- **poller diff:** 1 commit (`31f7109`), `170 8` by `git log --numstat` (170 added / 8 removed, = the stop line), 7 `@@` hunks; `runner.py` `18 0`.
- **`upsert_bars` / `upsert_bars_on` additions-only:** `store.py` `112 0` (`c941d30`), both method bodies untouched.
- **card/scoring diffs empty:** `log … -- src/cobalt/cards src/cobalt/radar/evaluate.py` → no output.
- **`RESTARTS:`** line in the stop line: `RESTARTS: com.cobalt.aset com.cobalt.radar` (names the radar resident).
- **`requires_db` tests written and never run:** 14 = 3 (`test_bars_poller_coverage.py:1204, 1233, 1253`) + 7 (`test_bars_migration.py:333, 365, 377, 397, 428, 441, 460`) + 4 (`test_bars_ensure.py:457, 485, 515, 552`), matching the builder's 14.

## ESCALATE
1. **gemini `CHECK: FIX FIRST`** — chunk 1a child partition name shape (`bars_p_<YYYY>w<WW>` vs `bars_p_<YYYYMMDD>`).
2. **Child-name-shape mismatch with chunk 1a** — both houses; hub confirmed from both branches' files (`partitions.py:86-98` vs chunk 1a `placement.py` `_PARTITION_CHILD`, tip `8dddf2b`); `bars_p_20261026` would raise `KeyError` in 1a's `side_of`; not named in this branch's report.
3. **grok `BUILD STANDS EXCEPT`** — three items (child-name shape, test-9 newest fixture, ungated write-failure refresh); `ready for its deploy prompt: NO`.
4. **Inertness on a write failure** — grok: the arm is "NO" (`poller.py:198`), while its own CHECK line says inert YES; gemini's "only one read" (claim 1) does not hold; a raising first read or refresh aborts the cycle where main continues (`poller.py:136-142, 198-200`).
5. **A house-called wrong-reason test that the hub's file-check HOLDS** — test 1 (grok: projection, `:290-296, 347`) and test 9 (grok: `:825-847`, `closed` empty, `stale` planted either way).
6. **Tests 5 / 5b (hub finding; both houses answered NO)** — both abort at `poller.py:144-146` before any fetch, so P-closed's second clause and row order are not reached by them (claim 16); test 2b is the case that reaches it.
7. **`ASK DESK: chunk 2 is a live-write-path change and only 2 houses could check it (astra: METER) — is a second attempt wanted before the deploy prompt? [20:07 ET]`**
8. **Hunk count:** the report's quoted diff and the committed diff differ — 11 narrated hunks vs 7 committed `@@` hunks.
9. **Diff copies in the packet lost their whitespace-only lines** (76 lines, 190 B); the houses read them so.
10. **`bars_coverage` has no caller** in the branch (`heartbeat/runner.py:131-148` untouched); grok's NOT CHECKABLE is resolved by the hub (claim 39).
11. **Named range (O1):** `PollFailure.detail` has no reader; carried `no_partition` records keep `detail=None` (`poller.py:230-233`, `runner.py:270-277`).
12. **Runner order and per-ticker abort (O2, O3):** an aborted cycle still runs `stamp_poll` first and the evaluate stage after; the closed-period abort is per ticker, after earlier tickers' commits.
13. **Owner items the houses named:** grok — composition (a) "one ticker one cycle late" is conditional (only if he wants it unconditional); the ANY-hole vs AMBER reading (only if he wants every forward shortfall RED); (viii) the named range for a later card-facing surface; (x) the builder's heredoc outside the bare-shape rule (launch hygiene).

BARS CHUNK 2 CHECK DONE · grok: "CHECK: BUILD STANDS EXCEPT child-name-shape vs 1a, test-9 newest fixture, ungated write-failure refresh · inert on an unpartitioned parent: YES · composition note: SOUND · hard boundary: HELD · ready for its deploy prompt: NO · child names disagree with 1a's pattern" · gemini: "CHECK: FIX FIRST chunk 1a child partition name shape mismatch (`bars_p_<YYYY>w<WW>` vs `bars_p_<YYYYMMDD>`) · inert on an unpartitioned parent: YES · composition note: SOUND · hard boundary: HELD · ready for its deploy prompt: NO · child partition name mismatch against chunk 1a." · astra: METER · houses that checked: 2 of 3 · inert on an unpartitioned parent: 2 of 2 YES · composition note: 2 SOUND / 0 UNSOUND · hard boundary: 2 HELD / 0 CROSSED · poller tests present: 13 of 13 · claims that HOLD against the branch: 36 · DO NOT HOLD: 7 · ready for a deploy prompt: 0 of 2 · ESCALATE: 13
