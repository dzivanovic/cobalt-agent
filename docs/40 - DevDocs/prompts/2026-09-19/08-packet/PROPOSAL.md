# PROPOSAL — the Bar Archiver becomes append-only (design for the four-house tribunal, LAWS L67)

Proposing house: Anthropic (Fable, CTO desk), 2026-09-19. Status: PROPOSAL. The tribunal (Astra, Grok, Gemini, Fable) rules on it and derives the final version; nothing is built before that.

## 1. The owner's ruling this design must satisfy (his words, 2026-09-18, `cto-2026-09-18.md` R14/R15)
- "why is there an overwrite of three and a half million records every night while only the last day is new … i don't want to overwrite that i want to know where the watermark is for each ticker and I want to only add the new [bars] in the database that don't exist. I don't want to do this read and writes through the database and trash around the database to overlay 3 million records."
- "because it's a nightly run … when the database is quiet and the market is quiet there will be no half through the minute bars … each ticker should be updated as appropriate or if that's too much to calculate you could always just start from midnight and add another day each night … one day would not be three million rows".
Out of scope here, reserved for Sunday's bars-lifecycle tribunal: partitioning, retention, deriving i2/i5/i15/i30 from i1, the bounded migration proof. This design must not make any of those harder.

## 2. Facts (from the code on main; file:line in `facts.md`)
- One table `system.bars`, PK `(ticker, interval, ts)`, no other index, `ts` = bar OPEN in UTC. ≈8.6M rows, ≈390k genuinely new rows per trading day.
- Every night at 20:30 ET the archiver walks ≈1,000 (ticker, interval) targets (210 tickers from the trader's list note), downloads for each the WHOLE window Finviz serves (no date parameter has any effect: i1 ≈14 days ≈9,451 rows, i5 ≈21 days, i15 ≈3 weeks, i30 ≈9.6 months) and sends every row through `INSERT … ON CONFLICT (ticker, interval, ts) DO UPDATE SET open, high, low, close, volume`. Last night: 3,343,938 rows sent, ≈390k new. One transaction per target; `rows written` in the run report counts rows SENT, so inserts and no-op rewrites cannot be told apart.
- Why DO UPDATE exists (docstring): "a re-run refreshes a bar that Finviz may have finalized/revised since the last pull, rather than freezing it at its first-seen (possibly provisional) values."
- The archiver has NO bar-is-complete check: it stores the forming bar too; only the 20:30 schedule protects it.
- A second writer shares the same method: the radar's intraday poller (i1 only, pool members). It keeps only CLOSED bars (`ts + 1 min <= now`) newer than `watermark − 5 bars` and deliberately re-upserts those last 5 minutes to pick up revisions. `BarStore.watermark(ticker, interval)` = `SELECT max(ts)` already exists; the poller is its only caller.
- A test pins the refresh behaviour (`test_upsert_is_idempotent_and_refreshes_on_conflict`).
- Only one reader of `system.bars` exists in the new core: the formation replay, i1 only, last 14 days.
- NOT KNOWN: whether Finviz restates intraday history (late prints, corrections, split adjustment of past bars). Nothing in the repo measures it.

## 3. Proposed design
**D1 — Two write paths, named for what they do.** `BarStore.insert_new_bars(bars, watermark)` for the archiver: plain `INSERT … ON CONFLICT DO NOTHING` of the rows it is given. `upsert_bars` (DO UPDATE) stays, used ONLY by the radar poller for its 5-bar overlap. The pinned refresh test stays on `upsert_bars`; new tests pin "an existing bar is never modified by the archiver".

**D2 — Watermark per target, filtered client-side.** Per (ticker, interval): `w = max(ts)` (PK backward scan, one tiny query). From the downloaded window keep only bars with `ts > w`. `w` is NULL (first contact, backfill) → keep all. Nothing at or below the watermark is sent to Postgres. Expected nightly volume: ≈390k inserted rows instead of ≈3.34M upserted.

**D3 — Completeness rule in the archiver itself.** Keep only bars with `ts + interval_length <= now` — the same rule the poller uses. The 20:30 schedule makes this a no-op at night; it makes a manual or backfill run during market hours safe, which matters MORE under append-only because a forming bar would otherwise be frozen for ever (today the next night's DO UPDATE heals it).

**D4 — The restatement guard (what replaces DO UPDATE's one real job).** Before inserting, compare the K most recent STORED bars at or below the watermark (proposed K = 30) with the same timestamps in the download. All equal → insert. Any OHLCV difference → the target is marked `restated`: the new bars ARE still inserted, stored history is NOT touched, the run report lists the target with the count and the first differing timestamp, and the job result carries `restated_targets`. A loud flag, never a silent rewrite (L1, L9). Remedy = an explicit operator command `cobalt archiver restate <ticker> [<interval>]` that re-upserts that target's window with DO UPDATE — run by decision, not by the nightly job. The nightly run report over a few weeks answers the NOT KNOWN above with data.

**D5 — Gap guard.** If `w` is older than the OLDEST bar in the download (the archiver was down longer than Finviz's window), insert what exists and flag the target `gap` with both timestamps. History that Finviz no longer serves cannot be recovered; it must not vanish silently.

**D6 — Honest counters (L57).** Per target and per run: `rows_fetched`, `rows_inserted`, `rows_skipped_at_or_below_watermark`, `rows_skipped_incomplete`, `restated_targets`, `gap_targets`. The run report gains those columns; `Rows Written` means inserted.

**D7 — What is deliberately NOT done.** No interior-hole repair: a bar that Finviz adds later BELOW the watermark (a late print creating a minute that had no trades) is not inserted by the nightly run. The alternative — read every stored key of the window per target and insert the set difference — would find such bars but reads ≈3.3M index entries a night, which is the "trash around the database" the owner ruled out. D4's comparison window reports such a case as `restated` when it falls within the last K bars; older ones are found only by an explicit `restate`. No change to the schedule, the pacing (1.2 s between targets), the Finviz request count, the targets, the table, or the poller's behaviour.

## 4. Decision points for the tribunal (rule on each: ACCEPT / AMEND <how> / REJECT <why>)
- **D1** two methods vs one method with a mode flag.
- **D2** watermark filter vs set-difference vs "midnight, add one day" (the owner named the last one as an acceptable simpler form) — which is most robust to: a ticker the poller already wrote today; a half-day; a target whose last run failed; DST.
- **D3** is the completeness rule right for every interval (i30's last RTH bar opens 15:30 and closes 16:00)? Should the archiver also refuse to run inside an open session?
- **D4** K = 30; exact equality vs a tolerance; is "insert new bars anyway, never touch history, flag" the right behaviour when a split restates everything; should `restate` be automatic for a target whose WHOLE overlap differs by one constant factor?
- **D5** anything else a gap should do.
- **D6** counters sufficient for replay (L57)?
- **D7** is declining interior-hole repair acceptable; if not, what is the cheapest sound alternative?
- **D8 (open to the houses)** anything about partitioning or i1-only storage (Sunday) that this design would make harder.
- **D9 (open)** failure semantics: today one transaction per target and the run never aborts; is that still right when a target's insert is tiny?
