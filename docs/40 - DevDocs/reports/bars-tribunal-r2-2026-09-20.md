# Bars tribunal — round 2 (hub `bars-tribunal-r2-0920`, 2026-09-20)

## §0 Headline
- 3 of 3 houses ruled the DERIVED v2 fold: grok `BUILD WITH 4 FIXES T2 T3 T4 T7` · astra `BUILD WITH 6 FIXES T2 T3 T4 T7 T9 WRONG FACTS` · gemini `DO NOT BUILD`. Nobody said `BUILD THE DERIVED VERSION`. RESOLVED by all three: T1 T5 T6 T8 MISSING. Not resolved by any house: T2 T3 T4 T7 T9 WRONG FACTS.
- Five `NEW DEFECT INTRODUCED BY THE FOLD` (gemini T4, T9 · astra WRONG FACTS · grok T7, WRONG FACTS). Attack (a) the T0 fence, (d) the poller distinction, (e) the gap states: named broken by all three houses; on the files: (a) HOLDS in the form "a writer reaches below T0 whenever it runs more than 2 days before the swap", (d) and (e) HOLD against `poller.py` and DERIVED §3.7. Attack (b) the trigger ledger: all three assert bypass routes — every one is a PostgreSQL behaviour, NOT CHECKABLE FROM READS.
- Hub tally on the files: 14 failing sequences HOLD · 3 DO NOT HOLD (gemini's "silently lost", gemini's 10-td cost, astra's vendor-hole reading) · 6 NOT CHECKABLE (§ Checked). ESCALATE: 0. No `NO RULING LINE`, no HARNESS, METER or TIMEOUT.
- The desk decides what a round 3 is; L67 allows at most one more. Nothing was built, migrated or deleted; nothing was written outside `scratch/tribunal-bars-0920/r2/` and this report.

## PREFLIGHT

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| date gate | `date` → `Sun Sep 20 14:11:12 EDT 2026` | 0 | allowed — not 2026-09-21, gate passes |
| authorization | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` → 68cf65e, 65ae682, 8ea21a6, 2079acc, dd7e9a7, a6cc75c | 0 | allowed |
| authorization | `grep -n "^| R13 " …/cto-2026-09-20.md` → line 86, 13:33 ET, "Push and approved everything. Please start all the process and inform me when you have something for me to rule on. I'm expecting you to run for a while." — matches the prompt's quotation | 0 | allowed |
| grok | `grok --version` → `grok 1.0.25 (f7e67d6988e2) [stable]` | 0 | allowed |
| agy | `agy --version` → `1.2.7` | 0 | allowed |
| round-1 folder | `ls scratch/tribunal-bars-0920` → `astra-ruling.md`, `gemini-ruling.md`, `grok-ruling.md`, BRIEF.md.part1/.part2, QUESTIONS.md, poller.py, aggregate.py, anatomy-bars.py, clock.py, migrate-proof.excerpt.py, owner-rulings.md, finviz-windows.md, … | 0 | allowed — three `*-ruling.md` present |
| recovery | `ls scratch/tribunal-bars-0920/r2` → `No such file or directory` | 1 | allowed — fresh run, nothing staged |
| CODEX PROBE | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) → `OK`, `[exited with code 0]`, no usage-limit text | 0 | allowed → **astra: UP** |

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/r2/` (no `mkdir` run; the first Write created the folder). Read → Write, no file split into parts. `wc -c` against the original after writing:

| staged file | original | bytes | match |
|---|---|---|---|
| `DERIVED.md` | `docs/30 - Design/BARS-LIFECYCLE-DERIVED-v2-2026-09-20.md` | 50,716 | yes |
| `round1-grok.md` | `scratch/tribunal-bars-0920/grok-ruling.md` | 15,461 | yes |
| `round1-gemini.md` | `…/gemini-ruling.md` | 7,715 | yes |
| `round1-astra.md` | `…/astra-ruling.md` | 21,329 | yes |
| `round1-fable.md` | `docs/30 - Design/bars-tribunal-fable-ruling-2026-09-20.md` | 24,792 | yes |
| `poller.py` / `aggregate.py` / `anatomy-bars.py` / `clock.py` | round-1 folder | 4,981 / 1,568 / 5,559 / 12,394 | yes (all four) |
| `migrate-proof.excerpt.py` / `owner-rulings.md` / `finviz-windows.md` | round-1 folder | 7,601 / 7,086 / 5,303 | yes (all three) |
| `round1-checked.md` | round-1 report lines 154–212 (`## Checked against the files` through the arithmetic table; the stop line at :214 excluded) | 59 lines | line range copied whole; a range, not a file, so no byte original to `wc` |
| `ev-runner.excerpt.py` | `src/cobalt/archiver/runner.py` 225–260 | — | excerpt, each headed by its real path + range |
| `ev-reconcile.excerpt.py` | `archiver/reconcile.py` 55–80 | — | excerpt |
| `ev-archiver-cli.excerpt.py` | `archiver/cli.py` 325–345 and 455–490 (two excerpts, one file) | — | excerpt |
| `ev-migrate-rollback.excerpt.py` | `db_migrations/cli.py` 660–705 | — | excerpt |
| `ev-db.excerpt.py` | `db.py` 255–285 | — | excerpt |
| `ev-schemas.excerpt.sql` | `db_migrations/0001_schemas.sql` 25–45 | — | excerpt |
| `ev-placement.excerpt.py` | `db_migrations/placement.py` 20–70 | — | excerpt |
| `ev-watermark.excerpt.py` | `archiver/store.py` 160–185 | — | excerpt |
| `QUESTIONS-R2.md` | the prompt's QUESTIONS-R2 text, verbatim | — | body verbatim; ONE paragraph appended after it — "Files in this folder:" (the file list the prompt says QUESTIONS-R2 carries) |

Excerpts were read from `/Users/cobalt/cobalt/src/cobalt/` on main between 14:11 and 14:21 ET today. The brief is NOT re-staged; `QUESTIONS-R2.md` points at round 1's `../BRIEF.md.part1`, `../BRIEF.md.part2`.

Launched 14:21:21 ET, all three `run_in_background`, independent, one attempt each, spellings per `01-review-harness.md` §2.1–2.3 (Grok `--sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)"`, writes `r2/grok-ruling-r2.md` itself; Gemini `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m`, prints; Astra `codex exec … -s read-only`, prints). Each launch sentence: "You are <HOUSE>. The folder is scratch/tribunal-bars-0920/r2/ . … Start with QUESTIONS-R2.md and follow it exactly."

### House rows (as they landed)
| house | landed | how | ruling line |
|---|---|---|---|
| gemini | ≈14:2x ET (first) | exit 0, printed; written byte for byte to `r2/gemini-ruling-r2.md` | `RULING R2: DO NOT BUILD — T0 fence drops intraday data; proof causes massive deploy outages.` |
| astra | ≈14:3x ET | exit 0, printed; the final message after `tokens used` (188 lines) written to `r2/astra-ruling-r2.md`; the ≈2,600-line codex stream above it (file reads) is not the answer and is not kept | `RULING R2: BUILD WITH 6 FIXES T2 T3 T4 T7 T9 WRONG FACTS` |
| grok | 14:33 ET (file mtime) | wrote `r2/grok-ruling-r2.md` (10,276 bytes) itself; replied with only the path | `RULING R2: BUILD WITH 4 FIXES T2 T3 T4 T7` |

## Rulings table
`R` = RESOLVED · `NR` = NOT RESOLVED · `ND` = NEW DEFECT INTRODUCED BY THE FOLD. F-nn = the fold row the house names.

| point | grok | gemini | astra | agreement | each NR / ND in ≤30 words |
|---|---|---|---|---|---|
| T1 | R | R | R | 3-0 R | astra also withdraws N1 (daily width) — "not a prerequisite" |
| T2 | NR | NR | NR | 3-0 NR | F-06: grok — failing `ts` unknown at `:106`, read `e.diag` before `scrub`, split first-sight batch by week · gemini — poller cannot dissect, ALWAYS abort · astra — no bound inventory, mixed batch, coverage-unknown abort |
| T3 | NR | NR | NR | 3-0 NR | F-15/F-16: replica-role or trigger-disable `UPDATE` on a sealed child passes trigger + `relfilenode` + membership; grok/gemini want `n_tup_*` equality and `ENABLE ALWAYS`; astra adds a seal-publication race, function no-op swap |
| T4 | NR | ND | NR | 3-0 unresolved (1 as ND) | F-19/F-21: writers run at `now` with a 14-day window; copy earlier than swap−2 d ⇒ nightly upsert/first-sight reaches `ts < T0`. grok 10-19→10-05 < 10-07; astra want change capture; gemini 17-day window |
| T5 | R | R | R | 3-0 R | — |
| T6 | R | R | R | 3-0 R | — |
| T7 | ND | NR | NR | 3-0 unresolved (1 as ND) | F-34/F-35: "older than newest stored bar" ≠ fetched — leave/re-enter (IMCC 09-14→10-12; gemini month) and first contact (astra NVDA 09-21, 09-04) label never-fetched minutes no-print |
| T8 | R | R | R | 3-0 R | — |
| T9 | R | ND | NR | split 1-2 | F-43/F-41/F-42: gemini — registering new partitions before swap makes MP1 digest both (~186 s); astra — 0b "waits for nothing", chunk 4 gates, R measures U8 before triggers exist, §4b-2 contradicts R gate |
| MISSING | R | R | R | 3-0 R | grok adds four tests implied by its fixes |
| WRONG FACTS | ND | R | ND | split 1-2 | grok: §7 delta uses 10 td, T0 = 16 calendar days ≈ 12 td ⇒ 37.6 s · astra: §3.6 states as fact the i1 export "missed a print" (U10 open) |

| attack | grok | gemini | astra |
|---|---|---|---|
| (a) T0 fence | BROKEN BY grok — copy Mon 10-19, nightly 20:30 reaches NVDA 10-05 < T0 10-07, `DO UPDATE` rewrites a copied row; preflight hours before drain | BROKEN BY gemini — vendor window 17 d: first-sight writes `T0−1 d` into legacy after copy, stranded | BROKEN BY astra — correction after same-day preflight, or a response reaching 09-04; outage reads only `ts ≥ T0`, `REPLACED` passes stale |
| (b) trigger ledger | BROKEN BY grok — `replica` role, `DISABLE TRIGGER`, detach→drop trigger→`UPDATE`→attach; PG behaviour NOT CHECKABLE | BROKEN BY gemini — `SET session_replication_role = replica; UPDATE … close = 0`; NOT CHECKABLE | BROKEN BY astra — `replica` role, trigger-function no-op swap, seal-publication race; NOT CHECKABLE |
| (c) cost range | HELD (arithmetic holds; breaks as a forecast: lower-bound rows, honest T0 ⇒ delta 37.6 s) | BROKEN BY gemini — "10 td not 15, 31.3 s" (hub: DOES NOT HOLD under whole-partition digests) | BROKEN BY astra — 22.0 s is not `append`'s worst (first-contact writes, 31.358 s for two prior weeks); 1,040–2,010 assumes 5 scanned days |
| (d) poller | BROKEN BY grok — failing `ts` only in `e.diag`, `scrub` runs first; `closed`/`now` cannot say | BROKEN BY gemini — cannot dissect; would abort for a historical hole | BROKEN BY astra — no partition inventory at that line; mixed current+historical batch either way wrong |
| (e) gap states | BROKEN BY grok — IMCC leaves 09-14, re-enters 10-12: 09-15…09-27 never fetched → no-print | BROKEN BY gemini — leaves a month, re-enters: 16 days never fetched → no-print | BROKEN BY astra — NVDA first contact 09-21, export from 09-07, 09-04 labelled no-print |
| (f) build order | HELD — R waits on 1a+2, gates chunk 3; chunk 4 most dangerous | BROKEN BY gemini — 1a registration ⇒ every deploy digests legacy + partitions | BROKEN BY astra — 0b before chunk 0, chunk 4 gates, U8 before triggers, §4b-2 vs `R passed`; chunk 4 still most dangerous |

## Not resolved and new defects, verbatim

### GROK (`RULING R2: BUILD WITH 4 FIXES T2 T3 T4 T7`; raw: `r2/grok-ruling-r2.md`)

**T2 — NOT RESOLVED**
> NOT RESOLVED. F-06's reason holds against `poller.py:96-102`: first-sight `watermark is None` → `threshold is None` → `closed` is the whole ~14-day export, so my always-abort would halt all ~500 names on one new mover. The derived distinction cannot be made from what the poller knows at `:88-115` without the failing row's `ts`. At `:106` it has `closed`, `now`, `watermark`, and `e`. `closed` intersects both the current week and a historical hole. `now` is the wrong proxy: Monday 2026-10-12 04:00 ET the 04:00 bar is not closed (`:99-101`), so `closed` is still Friday 19:59 (previous week) while `now` is already in the new week. The failing `ts` is only in `e.diag.detail`; the next line is `scrub(str(e))`. §3.2 never says to read it.
>
> Sequence if the abort test is `any(bar.ts in current week for bar in closed)` — the only test `closed`/`now` support: XYZ first-sight Monday 2026-10-12 04:05, week of 2026-09-28 detached, one `executemany` spans both, cycle aborts, ~500 names unpolled, cards show Friday as live. Sequence if they cannot tell and stay per-ticker: week of 2026-10-12 missing at 04:01, every ticker `continue`s, same Friday cards all morning.
>
> Replacement: on `no_partition`, read the failing `ts` from the exception (or `pg_partition_tree` for that `ts`) **before** `scrub`; abort the cycle iff that `ts` is in the current period; else record class `no_partition` with ticker + uncovered range and continue. Split first-sight `executemany` by week so a historical hole does not roll back that ticker's current-week bars.

**T3 — NOT RESOLVED**
> NOT RESOLVED. Replacing child `REVOKE` is right: harness is superuser (`ev-db.excerpt.py:16-22`, `ev-schemas.excerpt.sql:11-16`); a child `REVOKE` does not bind a parent-routed write. A row-level trigger **on the child** does fire for parent-routed `INSERT`/`UPDATE`/`DELETE` and for a superuser. It does **not** fire for `TRUNCATE` (caught by a new `relfilenode`), `ATTACH`/`DETACH` (caught by `pg_inherits` OID membership), or under `session_replication_role = replica` unless created `ENABLE ALWAYS`. `COPY FROM` does fire `INSERT` triggers in origin role.
>
> §3.3's in-outage SEALED path is only membership + `relfilenode` + trigger enabled. That misses the zero-volume `UPDATE` my T3 named, the moment the migration disables the trigger or sets replica role — both legal for this superuser harness. `relfilenode` unchanged; dirty never set; prints `SEALED_BASELINE_TRUSTED`. He sizes off zero volume until the evening bracket (~426 s at 72.45 M, residents up). Same-evening is not an acceptable first net on a live-account database.
>
> Also evades both trigger and `relfilenode`: `SET session_replication_role = replica` then `UPDATE`; `DISABLE TRIGGER` then `UPDATE`; `DETACH`, drop trigger, in-place `UPDATE`, `ATTACH`, recreate trigger (same OID, trigger looks enabled).
>
> Replacement: create the dirty trigger `ENABLE ALWAYS`. In the outage, every non-OPEN non-dirty partition must equal its last-seal `(relfilenode, n_tup_ins, n_tup_upd, n_tup_del)` — the F-13 guard, not only on MP4. Any move forces a content digest of that partition in the same run. Evening bracket stays as the second net. U7 fail-safe: a stats reset breaks equality → re-digest, never "counters went down so no writes".

**T4 — NOT RESOLVED**
> NOT RESOLVED. F-19's reason does **not** hold against `ev-runner.excerpt.py:15-29` (whole export, **no range cut**, `upsert_bars` `DO UPDATE`) or `poller.py:96-102` (first-sight whole export). T0 is `swap − 16d`. Writers run at **now**, and the vendor window is ~14 calendar days (`finviz-windows.md:12`). Online copy is "outside any deploy window", resumable — not inside the last 2 days before swap.
>
> Sequence: swap Friday 2026-10-23 20:40 ET, T0 = 2026-10-07. Copy starts Monday 2026-10-19. Monday 20:30 `_upsert_targets` fetches NVDA i1 oldest ≈ 2026-10-05 04:00 (`10-19 − 14d`). `2026-10-05 < T0`. `DO UPDATE` rewrites a row already copied online. If that close moved 141.20 → 141.00, Friday's `ts < T0` preflight fails, 5.28 M-row copy wasted, no swap (a slower night / failed deploy). If they swap anyway, wrong prices. Same hole on a first-sight poller write that day. `restate`/`backfill-missing` refuse `< T0` does not bind runner or poller. `ev-reconcile.excerpt.py:18` (`STEADY_STATE_SESSIONS = 2`) cannot reach T0. A repair started before the first batch and committed after that ticker's copy is the same `ts < T0` write; preflight is the only net, and only if it still runs. A batch with the stated `ts < T0` predicate does not straddle; a `WHERE interval='i1'` batch without `ts` does. Same-day preflight at 10:00, change at 11:00, drain at 20:40: equality has already passed.
>
> Replacement: from the first batch until swap, **every** writer range-cuts `ts >= T0` (poller, runner, `upsert_bars`, restate, backfill), fail-loud on `ts < T0`. T0 = `copy_start − (remeasured vendor window + 2 days)`, not `swap − 16`. Re-copy or change-capture any `< T0` row that still changes. Preflight of `ts < T0` immediately before the writer drain, not hours earlier.

**T7 — NEW DEFECT INTRODUCED BY THE FOLD**
> NEW DEFECT INTRODUCED BY THE FOLD. DST/half-day/`premarket_only`/open-minute skip/584→337 gate adopted (F-33). `no_print_as_fetched` = absent and older than that ticker's newest stored bar is false.
>
> Sequence: IMCC leaves the pool 2026-09-14, newest stored 2026-09-14 19:59 (`poller.py:67-70`). Not on lists, no nightly fill. Re-enters 2026-10-12. Watermark still 09-14; fetch returns ~14 calendar days (09-28 → 10-12); upsert writes those; newest = 10-12. Minutes 2026-09-15 04:00 → 2026-09-27 19:59 are absent and older than newest → `no_print_as_fetched`. They were never fetched; the vendor window is closed. A later successful day also flips yesterday's `ingestion_failure` into `no_print` once any newer bar exists. First contact NEWCO IPO 2026-11-16 09:30, first poll 10:00, newest 09:59: 04:00–09:29 same-day classified no-print though never in the export.
>
> Replacement: `no_print_as_fetched` only inside the range a **successful fetch actually covered** — `[max(watermark_before_fetch, oldest_returned_ts), newest_after_fetch]`. Minutes older than the last successful fetch's vendor window stay `unknown`. Do not infer coverage from `max(ts)` alone. `complete` / detector refusal stay unchanged.

**WRONG FACTS — NEW DEFECT INTRODUCED BY THE FOLD**
> NEW DEFECT INTRODUCED BY THE FOLD. Round-1 four are corrected in §3.11. New: §7 "delta ≈ 2.67 M rows, ≈31 s digest" uses 10 td. T0 = 16 calendar days ≈ 12 weekdays (swap Fri 2026-10-23 → T0 Wed 2026-10-07 = 12 td), 12 × 266,541 × 2 ÷ 170,000 = 37.6 s, not 31 s. After the T4 T0 fix (T0 pulled back to copy start) the delta is larger still. Proof-cost 15.7 / 22.0 / 47.0 arithmetic from §7's own lines holds (15 td = three dirty weekly children, not 15 days inside 16 calendar; Tuesday append 7 td = Fri week + Mon-Tue). It breaks as a forecast where 266,541 is a lower bound (§3.8) and where T0 is honest.

### GEMINI (`RULING R2: DO NOT BUILD — T0 fence drops intraday data; proof causes massive deploy outages.`; raw: `r2/gemini-ruling-r2.md`)

**T2 — NOT RESOLVED**
> NOT RESOLVED — The poller change (§3.2) attempts to abort the cycle only when the uncovered instant is in the current period. But `poller.py` lines 96-105 passes the entire `closed` batch to `upsert_bars`. When Postgres raises a `no_partition` exception for the batch, the poller only catches the generic `BaseException`. It has no way to dissect the exception to see which instant failed. It will wrongly abort the live 04:00 cycle for a historical hole, halting the radar for all 500 names. Exact replacement wording: "A missing partition raises a batch exception that Python cannot dissect. The cycle MUST abort for any `no_partition` failure, relying on `ensure` idempotency for recovery. Do not attempt to distinguish historical from current holes."

**T3 — NOT RESOLVED**
> NOT RESOLVED — The fold correctly declined my MP4 amendment because `UPDATE` leaves `relfilenode` unchanged, but its sealed-ledger replacement is also broken. A superuser migration running `SET session_replication_role = replica; UPDATE system.bars SET close = 0;` bypasses the row-level dirty trigger. Because `UPDATE` leaves `relfilenode` unchanged, it evades the in-outage check entirely, silently corrupting sealed history. Additionally, the fold's cost arithmetic fails: `upsert` nights fetch a 14-day vendor window, which contains exactly 10 trading days, not 15. Multiplying 3 weeks by 5 days ignores the calendar; the true `upsert` cost is 10 days (2,665,410 rows) = 31.3 s, not 47.0 s. Exact replacement wording: "The sealed ledger cannot trust triggers against a superuser; it must compute `n_tup_ins, n_tup_upd, n_tup_del` alongside `relfilenode` to catch in-place updates. The proof cost must state 31.3 s for a 10-day `upsert`."

**T4 — NEW DEFECT INTRODUCED BY THE FOLD**
> NEW DEFECT INTRODUCED BY THE FOLD — The fold modified my amendment (F-17), claiming "no online-copied row has a legitimate writer". This fails against the code: the poller (`poller.py` 96-102) does not enforce T0. If a new ticker enters the pool and the vendor window is 17 days, the poller's first-sight fetch writes the entire 17-day export into `bars_legacy`. Because Chunk 3 (the `< T0` copy) has already passed, and Chunk 4 only delta-copies `>= T0`, the row at T0 - 1 day is permanently stranded in legacy and silently lost. Exact replacement wording: "The T0 fence fails because the poller does not enforce it. Chunk 4 MUST execute a final catch-up `INSERT` inside the swap's ACCESS EXCLUSIVE lock covering all `ts`, using an anti-join to skip already-copied rows."

**T7 — NOT RESOLVED**
> NOT RESOLVED — Gap states (§3.7) cannot be safely retroactively inferred from `newest_stored_bar`. If a ticker leaves the pool, is unpolled for a month, and re-enters, its first fetch pulls 14 days. The 16 days prior to that window were never fetched. Yet because they are older than the `newest_stored_bar` (the 14th day), they will be falsely flagged `no_print_as_fetched` (implying the market traded but volume was zero). Exact replacement wording: "Gap states cannot be inferred from `newest_stored_bar` for tickers that leave and re-enter the pool. A true gap classifier requires an explicit ledger of fetched ranges."

**T9 — NEW DEFECT INTRODUCED BY THE FOLD**
> NEW DEFECT INTRODUCED BY THE FOLD — The build order (§3.9) places the chunk 1a `placement.py` pattern registration BEFORE chunk 3 (the online copy). As soon as chunk 1a lands, `_probe_all` will start digesting the new partitions. While chunk 3 slowly copies 3.5 million rows into them, EVERY unrelated deploy will use MP1 to full-table digest BOTH `bars_legacy` (106s) AND the new partitions (up to 80s). This creates a massive ~186-second deploy outage for days before the swap. Exact replacement wording: "The new partitioned table MUST NOT be registered in `placement.py` for migration proofs until Chunk 4's swap, or Chunk 5's MP2 must land BEFORE Chunk 3's copy begins."

### ASTRA (`RULING R2: BUILD WITH 6 FIXES T2 T3 T4 T7 T9 WRONG FACTS`; raw: `r2/astra-ruling-r2.md`)

**T2 — NOT RESOLVED**
> The historical/current distinction is useful, but the specified exception class does not supply enough information to make it.
>
> At `poller.py:104–115`, the poller has `closed`, `now`, and an exception. It has no partition-bound inventory or structured uncovered timestamp. A PostgreSQL check-violation class alone does not distinguish missing partition routing from other CHECK failures.
>
> Concrete sequence: at 04:01 on 2026-09-21, a first-contact NVDA batch contains historical rows and the closed 04:00 row. A historical child and the current child are both missing. Routing can fail on the historical row first. Classifying only that first failure as historical continues through the universe despite missing current coverage. Conversely, treating every mixed batch containing current rows as a current-period failure lets one historical hole abort otherwise healthy AMD polling.
>
> F-06's reason for preserving per-ticker handling **holds**, but its implementation information is missing. F-09's coverage requirement supplies the appropriate foundation.
>
> **Exact replacement wording:**
> > Identify missing-partition failures using structured store diagnostics and partition bounds, not the exception class or batch maximum alone. After rolling back a failed batch, determine all uncovered submitted timestamps and independently verify coverage of the current period. Missing current coverage aborts the cycle and marks radar health RED; historical-only holes remain per-ticker failures with explicit reconciliation ranges. If coverage cannot be established, abort with an explicit coverage-unknown failure. Test a batch containing both historical and current holes, regardless of which row fails first.

**T3 — NOT RESOLVED**
> The trigger approach improves ordinary-write detection, but does not establish the claimed proof boundary.
>
> The two reasons for rejecting child REVOKE **hold**: `ev-db` explicitly gives the migration harness a superuser connection without `SET ROLE`; child privileges do not independently block ordinary parent-routed access. F-15's replacement is therefore justified in direction, but incomplete in execution.
>
> For PostgreSQL 16 behavior:
>
> | Operation | Effect on the proposed row trigger |
> |---|---|
> | Parent-routed INSERT/UPDATE/DELETE | Relevant child row triggers fire. |
> | Ordinary superuser DML | Triggers fire; superuser status alone does not suppress them. |
> | `session_replication_role = replica` | Ordinary origin triggers do not fire; `ENABLE ALWAYS` is required for this case. |
> | `COPY FROM` | Insert triggers normally fire, subject to trigger configuration and replication role. |
> | `TRUNCATE` | Row triggers do not fire. A statement-level TRUNCATE trigger is a separate mechanism; ordinary committed truncation changes the relation's storage identity. |
> | ATTACH/DETACH | Row triggers do not fire. Membership checks detect a surviving membership change, not necessarily a detach/change/reattach sequence. |
>
> Concrete escape: a migration sets replication role to `replica`, changes NVDA's 2026-08-31 close in a SEALED child, restores the role, and commits. The child OID, `relfilenode`, membership and enabled trigger remain unchanged. The ledger remains clean. The evening bracket may detect the damage, but wrong prices have already passed deployment.
>
> A second escape needs no trigger disable: replace the trigger function with a no-op, UPDATE that row, and restore the function. Checking that the trigger exists and is enabled misses this. The superuser authority shown in `ev-db` permits the operations.
>
> Detection that evening is **not an acceptable substitute for the existing pre-commit rejection of altered prices**, absent an explicit owner decision accepting that exposure. The existing harness in `ev-migrate-rollback` rolls back `CHANGED` before commit.
>
> The sealing process also lacks a concurrency rule. Suppose preflight reads Friday's NVDA row, a poller commits a correction and sets an already-true dirty flag, and preflight then publishes its earlier digest and clears dirty. The ledger now describes stale content as clean. Merely adding a generation column does not prevent that race.
>
> The arithmetic multiplications in §7 are mostly correct; the advertised range is not:
>
> - Five trading days: **15.679 seconds** at 170,000 rows/s/side.
> - Seven trading days: **21.950 seconds**.
> - Fifteen trading days: **47.037 seconds**.
> - Eleven trading days: **34.494 seconds**.
>
> But **22.0 seconds is not append's worst case**. Append mode changes the nightly archiver; it does not change the poller's first-contact whole-export upsert. On Monday 2026-09-21, a new ticker can dirty both preceding weekly partitions. With those weeks populated, their ten trading days alone cost **31.358 seconds**, before Monday's rows. Repairs or accumulated dirty history can exceed the fifteen-day model too.
>
> The **1,040–2,010 ticker threshold assumes only five days are scanned**. At a thirty-second per-side budget and 170,000 rows/s:
>
> | Scanned trading days | 507.3 rows/ticker/day | 960 rows/ticker/day |
> |---|---:|---:|
> | 5 | 2,011 tickers | 1,063 tickers |
> | 7 | 1,436 tickers | 759 tickers |
> | 15 | 670 tickers | 354 tickers |
>
> At 166,000 rows/s, fifteen dense days reach the budget around **346 tickers**. Further, §3.8 calls the daily row rate provisional; it cannot support an unconditional upper bound. Nor is five days of current-week rows a literal minimum on Monday.
>
> **Exact replacement wording:**
> > MP1 remains the default. MP2 may trust a sealed baseline only under a demonstrated invalidation and sealing protocol. Seal publication must serialize with writes, atomically recording a digest, exact count and generation without clearing a concurrent invalidation. Unexpected changes to SEALED content are incidents; do not silently replace the trusted baseline. Use ALWAYS DML triggers, explicit TRUNCATE handling, and validation of bounds, schema, membership and trigger definitions. Digest the union of partitions invalidated before or during the migration and compare against their trusted pre-migration content. Privileged operations capable of bypassing invalidation require an in-transaction content proof before commit; an evening bracket is additional detection, not deployment authorization. If bypass cannot be excluded, use MP1.
> >
> > Report 15.7, 22.0 and 47.0 seconds as conditional scan examples, not a best/worst guarantee. Compute capacity from actual scanned partitions, settled density and measured throughput. Include first-contact poller writes, repairs and dirty backlog in every mode. Report separately the full retained-history work moved outside the outage.

**T4 — NOT RESOLVED**
> F-19's reason for declining transactional change capture **does not hold against the staged writers**.
>
> `ev-runner` explicitly says "no range cut" and sends the whole export to upsert. `poller.py:96–102` imposes no oldest timestamp for first contact; an existing ticker's threshold depends on its watermark and the unstaged overlap setting. `ev-reconcile` specifies two completed sessions **that the export actually carries**, not a universal calendar-age enforcement rule. `ev-archiver-cli` shows repair entry points, but no transaction-time fence or draining of already-admitted repairs.
>
> Concrete sequence, using the design's planned Monday swap:
>
> 1. T0 is 2026-09-05 00:00 ET.
> 2. Online copying includes NVDA 2026-09-04 15:58.
> 3. Same-day preflight confirms equality.
> 4. An already-admitted repair commits a correction afterward, or a subsequent vendor response extends to September 4 and the unrestricted runner upserts it.
> 5. Outage reconciliation reads only `ts ≥ T0`.
> 6. `REPLACED` passes while the new table retains the stale September 4 price.
>
> A measured fourteen-day NVDA export does not prohibit a different ticker or later response from reaching farther back. The August 27 MSFT observation in `finviz-windows.md` is evidence of that response, not an enforceable writer limit.
>
> A batch straddling T0 is harmless only if copying applies the predicate to every row and every later source change below T0 is captured or prohibited. Batch boundaries alone provide no protection.
>
> Rollback also remains underspecified: market timestamp does not identify when an old row was corrected after swap. A September 1 correction made after cutover must be reverse-reconciled even though its `ts` predates cutover. The vendor window does not itself terminate database-based rollback on day fifteen.
>
> **Exact replacement wording:**
> > Before the first copy snapshot, establish transactional capture of every i1 insert, update and delete, including transactions already in flight. Copy resumable batches with explicit timestamp predicates. Drain writers, apply captured changes through a common commit boundary, and verify complete source-i1/target-i1 equality before committing cutover. T0 may divide copy work but does not replace change capture unless an enforced, drained write fence proves that every writer is excluded from the copied region.
> >
> > After cutover, reverse reconciliation uses transactionally recorded changes or a complete authoritative comparison, including corrections to old timestamps and deletions. Drain writers during rollback and verify equality before reopening service. Rollback expires when the required retained data or reconciliation mechanism is removed, not automatically when the vendor window reaches day fifteen. Rehearse and state the resulting outage.

**T7 — NOT RESOLVED**
> F-34's reason for declining a per-cycle success table does **not justify substituting newest-bar inference for acquisition evidence**. The proposed table-size comparison does not establish that compact range evidence is infeasible, and `unknown` requires no new table.
>
> Concrete sequence: NVDA first enters the monitored pool on 2026-09-21. Its first fetched export begins September 7 and contains September 21 bars. No September 4 minute was fetched. Nevertheless, §3.7 labels every absent September 4 minute `no_print_as_fetched`, because it is older than NVDA's newest stored bar.
>
> The staged poller expressly allows first contact and drops carried failures for names outside the pool. Neither a later watermark nor an absent failure record proves coverage during an earlier absence.
>
> A second sequence preserves the defect within recent history: NVDA's 10:17 fetch fails, a later export supplies 10:18 but has a hole at 10:17, and the successful poll clears its generic error. The classifier overwrites uncertainty with "no print." A returned export can itself be incomplete; fetched absence is not proof that no trade occurred.
>
> **Exact replacement wording:**
> > A newest stored bar proves no coverage of earlier missing minutes. `observed` requires a persisted row. `no_print_as_fetched` requires retained evidence that a successful fetched response covered the relevant minute and omitted it; it describes that response, not confirmed absence of trading. `ingestion_failure` requires an acquisition or persistence failure covering the minute. All remaining absences are `unknown`. Store compact coverage evidence where justified, or retain `unknown`; never infer successful coverage from a watermark. Preserve the supporting evidence and classification at card time. Completeness and detector refusals remain unchanged.

**T9 — NOT RESOLVED**
> R is correctly placed before chunk 3 and explicitly gates it. That part of F-42 is resolved. Retention also has an explicit owner gate and restore drill before DETACH.
>
> The remaining dependency graph permits damaging activation:
>
> - Chunk **0b waits for nothing**. Deploy it before Monday's shadow night while the effective lists still request five intervals: i5/i15/i30 writes fail, and the shadow night no longer measures the unchanged five-interval baseline promised by §3.5.
> - Chunk **4 waits only for 3 and deployment gates**, not explicitly for completed writer closure, derivation/consumer readiness, or the source/target invariant tests.
> - R must measure U8's dirty-trigger overhead, yet chunk **5 introduces that mechanism only after swap**. The implementation needed for that measurement must exist in development before R.
> - §4b-2 says that without the authorized scale copy, chunks 3–4 go unrehearsed. That contradicts the mandatory `R passed` gate.
>
> Chunk 4 remains the **most dangerous data operation**, because a successful-looking cutover or rollback can lose acknowledged corrections. Chunk 3 is now independently dangerous if the unsupported T0 assumption is allowed to substitute for capture.
>
> **Exact replacement wording:**
> > Separate implementation from production activation. Prepare 0b early, but activate i1-only writer refusal together with the authorized effective-list transition after the required shadow night. Before chunk 3, require G0 green, the capture or enforced-fence implementation complete, and production-scale R passed. Before chunk 4, require verified writer closure, consumer/derivation readiness and complete i1 equality checks. Implement and test the seal mechanism in development before R if R measures its overhead; production MP2 activation may remain after swap and the owner's ruling. If the scale rehearsal is not authorized or cannot pass, chunks 3–4 remain blocked.

**WRONG FACTS — NEW DEFECT INTRODUCED BY THE FOLD**
> §3.6 turns an unresolved discrepancy into a causal finding: "the i1 export missed a print."
>
> For DRAM 2026-09-03 04:02 and 04:04, and QTUM 04:00, the staged checked report explicitly leaves the constituent rows and chart comparison unverified. A lower vendor-i2 low establishes disagreement if the reported comparison is correct. It does not distinguish a missing i1 print from an incorrect i2 value, inconsistent adjustment, or another vendor discrepancy.
>
> **Exact replacement wording:**
> > Three reported buckets have vendor-i2 lows below the corresponding derived-i1 lows. Their constituent rows, discrepancy classification and agreement with the trader's chart remain unverified. Treat these as unresolved cross-interval discrepancies; do not assign the cause to a missed i1 print until the preserved evidence supports that conclusion.
>
> The remaining consequential factual errors—the bounded cost range, newest-bar coverage inference, and automatic day-fifteen rollback expiry—are covered by T3, T7 and T4.

## Advice on the owner's rulings — changes since round 1
Counts of `UNCHANGED`: **grok 8** (items 2, 3, 4, 6 and §4b-1…4) · **gemini 7** (items 1–6 and §4b-3; three §4b items carry new advice because round 1 had no such items) · **astra 7** (items 1, 2, 3, 4, 6, §4b-1, §4b-4).

| item | house | round 1 | round 2 | the harm |
|---|---|---|---|---|
| 1 retention | grok | "90 calendar days hot." | "**CHANGED — 365 days hot** (keep everything hot until the restore drill, then 365)." | "Under §3.3 the in-outage proof no longer grows with retention; 90 days is now lost bars he cannot replay, vendor closed, EV stuck at insufficient data. Price of 365 is disk (~10.2 GiB/yr) and an evening bracket (~426 s at 12 months, residents up), not a 04:00 outage." |
| 5 proof scope | grok | "Narrow the proof only with the T3 DML-counter guard; `--full` stays." | "**CHANGED** — YES to 5b only with in-outage DML-counter equality on sealed (`ENABLE ALWAYS` trigger); 5a only with both guards; `--full` stays." | "Bare 5b as written: wrong prices pass the deploy and sit under cards until evening." |
| 5 proof scope | astra | "Recommend no MP4 authorization as written; shortening a deploy by trusting catalog metadata can leave wrong prices undetected." | "**CHANGED:** Retain MP1 until T3 passes; neither metadata guards nor evening detection justify wrong prices passing a deploy." | wrong prices passing a deploy |
| §4b-2 scale rehearsal (astra's 8) | astra | (new item — no round-1 advice) | "**CHANGED:** Authorize the bars-only rehearsal or hold chunks 3–4; an unmeasured cutover risks lost corrections and an unbounded deploy outage." | lost corrections; an unbounded deploy outage |
| §4b-3 lists timing (astra's 9) | astra | (new item) | "**CHANGED:** Activate lists and writer refusal together after the required shadow night; otherwise that night produces failures instead of the promised comparison." | a shadow night that measures failures, not the baseline |
| §4b-1 K | gemini | (new item) | "K = 50 random names nightly, alert on any mismatch." | (none stated) |
| §4b-2 rehearsal | gemini | (new item) | "YES, absolutely required to measure the true disk watermark and copy durations." | (none stated) |
| §4b-4 budget | gemini | (new item) | "30 seconds per side is the maximum acceptable deploy delay." | (none stated) |

Hub note (fact, not advice): gemini's item 5 round-2 line is `UNCHANGED` (round 1: "Yes (MP4)"), while its own T3 text calls the sealed ledger broken and asks for `n_tup_*` counters; both are quoted above, unedited.

## Checked against the files
Files = the staged copies in `r2/` (byte-matched to main, table above) or the real files on main. `D:N` = `DERIVED.md` line N (the staged copy is byte-identical to the original, same numbering). `poller:N` = `poller.py:N`. PostgreSQL behaviour, psycopg exception contents, vendor windows and row counts cannot be settled from reads: `NOT CHECKABLE FROM READS`, with the experiment (L70 — never restated as a defect). No database query was run.

### Claims about today's code and about DERIVED
| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | At the catch site the poller holds `closed`, `now`, `watermark`, `e`; it has no partition-bound inventory; the failing timestamp is not read | grok, astra, gemini | `poller:104–115` (`closed` 98–102, `except BaseException as e` 106) | HOLDS |
| 2 | `scrub(str(e))` runs at the first statement after the `StageDropped` test, before any field of the exception is used | grok | `poller:112` | HOLDS |
| 3 | The failing row's `ts` is in `e.diag.detail` / can be read from the psycopg exception | grok | — | NOT CHECKABLE FROM READS — experiment: on `cobalt_dev`, insert a batch into a partitioned table with a missing partition and print `e.diag.message_detail` |
| 4 | First sight (`watermark is None` → `threshold is None`) upserts the whole export (~14 d), one `upsert_bars(closed)` call | grok, gemini, astra | `poller:96–102, 105` | HOLDS |
| 5 | The still-open minute is excluded from `closed` (`bar.ts + 1 min <= now`): at 04:00:30 `closed` ends at the previous session's last bar | grok | `poller:99–101` | HOLDS |
| 6 | The nightly `upsert` mode sends the whole export through `upsert_bars` with no range cut; `upsert_bars_on` is `DO UPDATE` | grok, astra | `ev-runner.excerpt.py:15–29`; `ev-watermark.excerpt.py:5–11` | HOLDS |
| 7 | `STEADY_STATE_SESSIONS = 2` is "sessions that the export actually carries", not a calendar-age cap | astra, grok | `ev-reconcile.excerpt.py:15–19` | HOLDS |
| 8 | `restate` / `backfill-missing` accept any interval and no `ts` bound today; the `< T0` refusal exists only in DERIVED | astra, grok | `ev-archiver-cli.excerpt.py:35–52`; `D:104` | HOLDS (code has no fence; the refusal is a design line covering only those two commands) |
| 9 | DERIVED bounds neither the gap between the online copy (chunk 3) and the swap (chunk 4), nor writers other than restate/backfill, below T0 | grok, astra, gemini | `D:104` ("`restate`/`backfill-missing` refuse any range `< T0`"), `D:146–147` (chunk 3 "G0 green, R passed"; chunk 4 waits for 3) | HOLDS |
| 10 | With T0 = swap − 16 d and a 14-day export, a writer running on day N reaches `ts < T0` iff N < swap − 2 d (grok's example: night 10-19, oldest 10-05 < T0 10-07 for a 10-23 swap) | grok | `finviz-windows.md:12`; `D:104` | ARITHMETIC OK — export oldest = N − 14 d; T0 = S − 16 d; N − 14 < S − 16 ⇔ S − N > 2 |
| 11 | The same-day preflight equality over `ts < T0` would stop the swap if a copied row changed (so a changed row is not "silently lost") | (hub, against gemini/grok) | `D:105` ("same-day preflight proves digest equality over `ts < T0` … "), `D:191` (U2 "a failed equality stops the swap") | HOLDS — gemini's "silently lost" DOES NOT HOLD; grok's "if they swap anyway" is conditional on ignoring a failed equality |
| 12 | After the same-day preflight, a writer with a 14-day export cannot reach `ts < S − 16 d`; astra's post-preflight correction needs a window ≥ 17 d or a repair that DERIVED's own refusal does not block | astra, gemini | `finviz-windows.md:12` (14 d, measured 2026-08-27); `D:104, 190` (U1) | NOT CHECKABLE FROM READS — experiment: `uv run cobalt archiver restate NVDA i1` preview → `export_oldest` today (U1) |
| 13 | DERIVED §3.3's in-outage SEALED check is ledger membership, `relfilenode`, and "the trigger exists and is enabled" — no counter equality, no function-body or `ENABLE ALWAYS` check | grok, astra, gemini | `D:94` | HOLDS |
| 14 | The harness connects as the docker superuser with no `SET ROLE` | grok, astra, gemini | `ev-db.excerpt.py:17–20`; `ev-schemas.excerpt.sql:11–16` | HOLDS |
| 15 | The harness rolls back on any `CHANGED` before commit | astra | `ev-migrate-rollback.excerpt.py:33–39` (`cli.py:693–696`) | HOLDS |
| 16 | A row trigger does / does not fire under `session_replication_role = replica`, on `TRUNCATE`, `ATTACH`/`DETACH`, `COPY`; `UPDATE` leaves `relfilenode` unchanged; trigger-function replacement is invisible to an "exists and enabled" check; `DETACH` → change → `ATTACH` keeps the child OID | grok, astra, gemini | — | NOT CHECKABLE FROM READS — experiments on `cobalt_dev` PG16: create the trigger on a partition; (i) `SET session_replication_role = replica; UPDATE`, (ii) `TRUNCATE`, (iii) `DETACH`/`UPDATE`/`ATTACH`, (iv) `CREATE OR REPLACE FUNCTION` with a no-op body then `UPDATE`; read the dirty flag, `pg_class.relfilenode`, `pg_inherits` before/after |
| 17 | DERIVED specifies no rule serialising seal publication against a concurrent write (only a `generation` column is named) | astra | `D:91, 96` (grep for serializ/advisory/compare-and-: none) | HOLDS as a text gap; whether the race loses a change is PG concurrency — NOT CHECKABLE FROM READS (experiment: two sessions, preflight publish vs. a writer commit, on `cobalt_dev`) |
| 18 | `_probe_all` digests exactly the tables in `MOVED + SEEDED + CREATED`; a table not registered there is not probed; DERIVED says `_probe_all` "registers" partition children, `bars_digest`, `bars_legacy` but does not say when | gemini | `migrate-proof.excerpt.py:96–98`; `ev-placement.excerpt.py:5–58`; `D:82, 142–145` | HOLDS as to mechanism; timing of registration vs. chunk 3 NOT CHECKABLE FROM READS — experiment: on `cobalt_dev`, register the partitioned table, run `cobalt db migrate --proof-only`, read the probe seconds |
| 19 | §4b-2 "Without it chunks 3–4 go to production unrehearsed" vs. chunk 3 waits for "G0 green, R passed" and R waits for 1a (which holds the scale copy) | astra | `D:172` vs `D:145–146` (DERIVED against itself — both lines quoted) | HOLDS — the two lines cannot both be followed if his word for the copy is withheld |
| 20 | R "measures U4, U5, U8, U11" (U8 = trigger overhead) but waits for 1a and 2 only; the triggers come with chunk 5, after the swap | astra | `D:145, 148, 197` (U8) | HOLDS |
| 21 | Chunk 0b "waits for nothing" and refuses non-i1 in `upsert_bars_on`/`insert_new_bars`; `upsert_bars` calls `upsert_bars_on`; the lists still name non-i1 intervals until chunk 0; the run's per-target `except Exception` records failure | astra | `D:139, 111–112`; `archiver-store.py:121`; `lists-archive-fields.md`; `ev-runner.excerpt.py:29–33` | HOLDS — 0b before chunk 0 fails those targets in the shadow night |
| 22 | §3.7 defines `no_print_as_fetched` as "absent, OLDER than that ticker's newest stored bar" — no fetched-range test; the poller writes only bars inside the export it received | grok, gemini, astra | `D:124`; `poller:96–102` | HOLDS |
| 23 | A ticker's watermark stays at its last stored bar while it is out of the pool; on re-entry the export (~14 d) is written and becomes the newest bar, minutes between are absent and older than it (IMCC 09-14→10-12; gemini "a month"; astra NVDA first contact) | grok, gemini, astra | `poller:67–70, 96–102` | HOLDS as a sequence on the code and §3.7's text; the tickers' real histories NOT CHECKABLE FROM READS |
| 24 | A failed cycle's `error` record is popped on the next successful upsert; a vendor-export hole at 10:17 is indistinguishable from no print — the rule's name is "as fetched", i.e. absent from the fetched export | astra | `poller:116`; `anatomy-bars.py:13–17` (round-1 file: "a minute with no print and a minute that was never fetched look identical") | DOES NOT HOLD as a misclassification — the label names exactly the response it describes; it is the objection's premise (no-print ≠ no trade), not a case where the label is false |
| 25 | A NEWCO IPO's 04:00–09:29 minutes "never in the export" are misclassified no-print | grok | — | NOT CHECKABLE FROM READS — a name absent before its IPO genuinely had no print; whether the export carries earlier minutes is a vendor fact |
| 26 | `bars` has no write-time column (PK `(ticker, interval, ts)`, OHLCV), so DERIVED's reverse delta "rows written to the new table since the swap" names no way to find an old-`ts` correction | astra | `0001_bars.sql:18–28` (round-1 folder); `D:107` | HOLDS |
| 27 | DERIVED says rename-rollback ends at day 15 because the vendor cannot re-serve the gap; astra: a database rollback does not depend on the vendor | astra | `D:107` | NOT A FILE FACT — a reading of the same sentence; quoted, not decided |
| 28 | DERIVED §3.6 states as a finding "the i1 export missed a print"; round 1's check marked it NOT CHECKABLE and §6 U10 is open | astra | `D:117`; `round1-checked.md` row 34; `D:199` (U10) | HOLDS |
| 29 | Fold F-06's reason: an always-abort halts all ~500 names on one new mover whose first-sight export overlaps a detached week | grok (holds), gemini (asserts the opposite) | `poller:96–102, 84–115`; `D:30` | HOLDS — the reason holds against the code; gemini's replacement contradicts it |

### Numbers the houses gave
| # | claim | who | steps copied | check |
|---|---|---|---|---|
| A1 | 5 / 7 / 15 / 11 td at 170,000 rows/s/side: 15.679 / 21.950 / 47.037 / 34.494 s | astra | rows = td × 266,541; × 2 ÷ 170,000 | ARITHMETIC OK (1,332,705; 1,865,787; 3,998,115; 2,931,951 rows) |
| A2 | 10 td (two prior weekly partitions) = 31.358 s | astra | 2,665,410 × 2 ÷ 170,000 | ARITHMETIC OK (31.358) |
| A3 | scan-days table at 30 s/side: 5 td 2,011 / 1,063; 7 td 1,436 / 759; 15 td 670 / 354; 15 td at 166,000 rows/s ≈ 346 | astra | 5,100,000 ÷ td ÷ 507.3 or ÷ 960; 4,980,000 ÷ 15 ÷ 960 | ARITHMETIC OK (2,010.6 / 1,062.5; 1,436.1 / 758.9; 670.2 / 354.2; 345.8) |
| A4 | The 1,040–2,010 threshold assumes 5 scanned days | astra | `D:215` divides by 5 | TRUE (arithmetic line) |
| A5 | "22.0 s is not append's worst case; first-contact writes are unchanged by append" | astra | `D:89` (b) lists `poller:96–102` as a writer of older weeks; the 22.0 line counts only `reconcile.py:71` | HOLDS as a reading of DERIVED |
| G1 | "14-day export = exactly 10 trading days, not 15; upsert cost = 10 td = 2,665,410 rows = 31.3 s" | gemini | 10 × 266,541 = 2,665,410; × 2 ÷ 170,000 | ARITHMETIC OK (31.36 s; "31.3" is truncated). The premise DOES NOT HOLD under §3.3: the digest reads WHOLE dirty partitions (`D:94`, `D:98` "all three young weeks dirty (15 td)"), so a 14-day window touching three weekly children costs up to 3 × 5 td |
| G2 | "MP1 on `bars_legacy` (106 s) + the new partitions (up to 80 s) = ~186 s" | gemini | `D:98`, `D:225–226`: 5,281,313 rows × 2 ÷ 170,000 = 62.1 s | WRONG AT "up to 80 s": §7 gives 62.1 s for all 5,281,313 i1 rows; 106.8 + 62.1 = 168.9 s. ("3.5 million rows" is also off: 3,553,219 is the non-i1 count; the copy is i1) |
| Gr1 | T0 = 16 calendar days ≈ 12 td; 12 × 266,541 × 2 ÷ 170,000 = 37.6 s, not 31 s (swap Fri 10-23, T0 Wed 10-07) | grok | 3,198,492 × 2 ÷ 170,000 | ARITHMETIC OK (37.63 s); 12 td counts 10-07…10-22 (3 + 5 + 4); DERIVED's "≈10 td" is the two-full-weeks minimum of 16 calendar days |
| Gr2 | "15 td = three dirty weekly children; Tuesday append 7 td = Fri week + Mon–Tue" | grok | 3 × 5; 5 + 2 | ARITHMETIC OK |
| Gr3 | "~426 s at 72.45 M rows, residents up" (evening bracket) | grok | `D:95`, `D:225` | TRUE (quoted from DERIVED) |

### Sequence ledger (the count in the last line)
HOLDS (code-side steps confirmed on the files) — **14**: gemini T2 (#1) · astra T2 (#1, #4) · grok T2 (#2, #5) · grok T4 night-reaches-below-T0 (#10) · gemini T7 (#22, #23) · astra T7 first contact (#22, #23) · grok T7 IMCC (#23) · astra T9 0b (#21) · astra T9 R/U8 (#20) · astra T9 §4b-2 (#19) · astra WRONG FACTS §3.6 (#28) · grok WRONG FACTS delta (Gr1) · astra `append` 22.0 s (A5) · astra rollback identification (#26).
DOES NOT HOLD — **3**: gemini T4 "silently lost" (#11) · gemini T3 "10 td not 15" (G1) · astra T7 second sequence, vendor hole (#24).
NOT CHECKABLE FROM READS — **6**: gemini T3 replica-role `UPDATE` · astra T3 replica-role + function no-op · astra T3 seal-publication race · grok T3 replica / `DISABLE TRIGGER` / detach-attach · astra T4 post-preflight correction / gemini T4 17-day window (window U1; #12) · gemini T9 registration timing (#18).

### Where a house says the design contradicts itself
- astra T9 (§4b-2 vs the `R passed` gate): quoted at #19 — `D:172` "Without it chunks 3–4 go to production unrehearsed, which 2 of 4 houses refuse." and `D:146` row `3 | Online copy ts < T0 | G0 green, R passed`.
- astra T9 (U8): `D:145` R "measures U4, U5, U8, U11" and `D:148` "5 | MP2: ledger, triggers, seal states, brackets…" waiting for "4".
- gemini T3 vs DERIVED's own words: `D:94` and `D:98`. gemini's premise is at G1.
- No house shows the design reaching scoring, ranking or a card value; grok's and astra's T2 sequences concern card freshness only (round 1's row 37 stands).

BARS TRIBUNAL ROUND 2 DONE · grok: RULING R2: BUILD WITH 4 FIXES T2 T3 T4 T7 · gemini: RULING R2: DO NOT BUILD — T0 fence drops intraday data; proof causes massive deploy outages. · astra: RULING R2: BUILD WITH 6 FIXES T2 T3 T4 T7 T9 WRONG FACTS · houses that ruled: 3 of 3 · points RESOLVED by all: T1, T5, T6, T8, MISSING · points NOT RESOLVED by any house: T2, T3, T4, T7, T9, WRONG FACTS · new defects: 5 · attacks that BROKE the design: a, c, d, e, f (b asserted by 3 houses, NOT CHECKABLE FROM READS) · failing sequences that HOLD against the code: 14 · NOT CHECKABLE: 6
