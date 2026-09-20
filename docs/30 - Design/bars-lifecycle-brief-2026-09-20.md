# BARS LIFECYCLE — tribunal brief 2026-09-20

**Proposing house:** Opus 5 (design hub `bars-brief-0920`), under L67 — the four houses rule on this and derive the final version.
**Tribunal:** 13:05 ET today (`cto-2026-09-19.md` §4 R10; it blocks nothing, R15 / L72).
**Authorization:** `cto-2026-09-18.md` §4 R15 lifted the hold as a TRIBUNAL design task; `cto-2026-09-20.md` §4 **R9** and **R9 (extended)** are RULED INPUTS, not questions.
**Nothing is implemented by this file.** No migration, no production write, no row deleted.

Binding law read in full before writing: L1, L3, L9, L10, L28, L42, L45, L52, L53, L57, L67, L68 (as amended today), L70.
**L53 is why no number below is chosen for him.** Every ceiling, cadence and retention PERIOD is presented as scenarios with consequences and a recommendation; none is settled here.

---

## §0 The proposal in ten lines

1. **`bars` becomes i1-only** (R9, ruled). Every non-i1 row is dropped — 3,553,219 of 8,834,532 rows, **40.22 %** of the table, 551.6 MiB.
2. **Nothing reads a non-i1 row.** Verified below, file:line, `src/` + `configs/` + the vault Lists note + smoke + DevDocs: **zero runtime readers.** The only non-i1 consumer is the archiver's own fetch list, which is a vault-note field, not code.
3. **Every dropped interval is exactly reproducible from i1.** Measured on production over 2,817,846 overlapping bars: **2,817,794 identical on all five OHLCV fields (99.9982 %)**; the 52 exceptions are all on ONE date (2026-09-03), all premarket, all ETFs, and in 49 of 52 the i1-derived bar is the *richer* one. i5, i15 and i30 match **100.0000 %**.
4. **The vendor cannot give any of it back.** Measured windows (2026-08-27): i1 ≈ **14 calendar days**, i5 ≈ 21, i15 ≈ 3 weeks, i30/h ≈ 9.6 months. Deleting an i1 bar older than ~14 days is **permanent**. Retention is therefore the one decision on this page that cannot be undone.
5. **The migration proof is not slow because of `interval`. It is slow because of `rows`, and rows are a function of TIME, not of ticker count.** At the measured September rate the i1-only table adds **266,541 rows per trading day** — so with no retention it reaches **72.4 M rows / 11.0 GiB / 852 s of proof per deploy in twelve months**, on today's ticker universe, with zero growth.
6. **Growth is not exponential and the evidence does not support calling it that.** The daily universe is flat (376–552 names/day over five days); the *cumulative distinct* set grows ≈81 names/trading day. Flat universe ⇒ table **linear** in time. Universe growing ⇒ table **quadratic** in time. Both are stated and costed below; neither is exponential, and the linear term already breaks us.
7. **Proposal, partitioning:** native **RANGE(`ts`) with ET-aligned bounds, WEEKLY to start, width revisable per period without touching history.** Monthly is already at its limit today (a month holds 5.6 M rows — as big as the whole i1 table).
8. **Proposal, the proof:** a **partition-scoped digest ledger** — a closed partition is digested once, has writes REVOKEd from every role, and thereafter proves itself from the catalog (`relfilenode` + row count); only the OPEN partition is re-read. With weekly partitions that is **15.7 s of both-sides proof instead of 106.8 s**, and it stays 15.7 s at 10 M rows or at 100 M.
9. **Proposal, sequencing:** ① stop writing non-i1 (a vault-note edit, zero code, already proven twice in production) → ② narrow the proof's scope by the migration's own DDL (1 chunk, no schema change, lands the biggest win first) → ③ copy i1 into the partitioned table ONLINE over quiet windows and swap by rename in a sub-second outage — **the copy is the deletion**, so no `DELETE`, no `VACUUM FULL`, no bloat → ④ retention as `DETACH` + cold file, never `DROP`.
10. **The thing a house should attack first:** §2.7 claims a weekly partition holds the proof at 15.7 s until ~2,000 tickers/day. If that arithmetic is wrong, the whole recommendation collapses back to daily partitions, and the build cost roughly doubles.

---

## §1 Measured ground, re-derived from production this session

Every query below was run by this hub at 2026-09-20 through `COBALT_ENV=production uv run cobalt db query --side system --prod` — read-only in code (`src/cobalt/db_query.py` `guard_select` accepts one `SELECT`/`WITH`; `read_rows` opens `BEGIN READ ONLY` and rolls back unconditionally).

### 1.1 The desk's 06:3x figures — all five re-derived, none differs

```sql
SELECT pg_total_relation_size('system.bars'), pg_relation_size('system.bars'), pg_indexes_size('system.bars')
```
→ `1438171136 / 903708672 / 534175744` = **1372 MB total, 862 MB heap, 509 MB indexes**. Matches the desk exactly.

```sql
SELECT interval, count(*), count(DISTINCT ticker), min(ts)::date, max(ts)::date
FROM system.bars GROUP BY interval ORDER BY 2 DESC
```

| interval | rows | tickers | first | last |
|---|---:|---:|---|---|
| i1 | 5,281,313 | 584 | 2026-07-30 | 2026-09-18 |
| i2 | 1,780,528 | 210 | 2026-07-30 | 2026-09-18 |
| i5 | 1,025,864 | 210 | 2026-06-05 | 2026-09-18 |
| i30 | 585,783 | 210 | **2025-08-08** | 2026-09-18 |
| i15 | 161,044 | 210 | 2026-06-05 | 2026-09-18 |
| **total** | **8,834,532** | **584** | | |

**Every figure in the desk's brief re-derives identically. Nothing differs.**

```sql
SELECT indexname, indexdef FROM pg_indexes WHERE schemaname='system' AND tablename='bars'
```
→ exactly ONE: `bars_pkey UNIQUE btree (ticker, "interval", ts)`, 509 MB.
No other index, **no foreign key in either direction, no trigger, no view** (`pg_constraint` / `pg_trigger` both checked). Grants: `cobalt_system` all, `cobalt_user` SELECT only.

Columns: `ticker text, interval text, ts timestamptz, open/high/low/close numeric, volume bigint` — all `NOT NULL`.

### 1.2 Extended-hours coverage — re-derived, identical to the desk's 07:0x read

```sql
WITH et AS (SELECT "interval" AS iv, (ts AT TIME ZONE 'America/New_York')::time AS t FROM system.bars)
SELECT iv, min(t), max(t),
       count(*) FILTER (WHERE t <  time '09:30') AS premarket,
       count(*) FILTER (WHERE t >= time '09:30' AND t < time '16:00') AS regular,
       count(*) FILTER (WHERE t >= time '16:00') AS afterhours
FROM et GROUP BY iv
```

| iv | first ET | last ET | premarket | regular | after-hours |
|---|---|---|---:|---:|---:|
| i1 | 04:00:00 | 19:59:00 | **1,136,902** | 3,297,163 | **847,248** |
| i2 | 04:00:00 | 19:58:00 | 440,493 | 989,146 | 350,889 |
| i5 | 04:00:00 | 19:55:00 | 283,104 | 514,305 | 228,455 |
| i15 | 09:30:00 | 15:45:00 | **0** | 161,044 | **0** |
| i30 | 09:30:00 | 15:30:00 | **0** | 585,783 | **0** |

Identical to R9 (extended). i15 and i30 are blind to the two sessions Monday's first live cards render in.

### 1.3 The number that forces the tribunal, and what actually drives it

`deploy-d3-2026-09-19.md` ESCALATE 4: the BEFORE+AFTER read of `bars` cost **106.8 s of a 149 s outage — 72 %** (53.29 s + 53.03 s). Five measurements of the same code exist:

| when | rows | s/side | rows/s |
|---|---:|---:|---:|
| 09-18 17:29 (`prod-proof-only-2`) | 8,591,339 | 46.73 | 183,852 |
| 09-18 later | 8,592,116 | 45.75 | 187,806 |
| 09-19 07:52 (`prod-proof-only-3`) | 8,834,532 | 51.99 | 169,927 |
| 09-19 deploy 1 | 8,834,532 | 47.05 | 187,769 |
| 09-19 deploy 3 | 8,834,532 | 53.29 | 165,782 |

**A finding that closes `prod-proof-only-3` ESCALATE 1.** Deploy 1 and deploy 3 read **the identical 8,834,532 rows** and differed by **13 %**. Superlinearity cannot be read out of a series whose two extremes share a row count; on this evidence the honest model is **linear at 170,000 rows/s per side, ±13 % host load**, and the 09-18→09-19 rise is inside that band. Every projection below uses 170,000 rows/s and states the band.

Why the proof is expensive at all, from the catalog:

```sql
SELECT attname, correlation, n_distinct, avg_width FROM pg_stats WHERE schemaname='system' AND tablename='bars'
```
→ `ticker` correlation **−0.0299**. The probe is `SELECT (to_jsonb(t) - …)::text FROM system.bars AS t ORDER BY t.ticker, t.interval, t.ts` (`db_migrations/cli.py:326`) — ordered by a key whose leading column has *no* physical correlation, then JSON-serialised and md5-folded row by row. The cost is **per row and per column**, and the only lever is *how many rows are read*. Excluding `bars` from the digest was already rejected in code as "a weaker proof exactly where the most data lives" (`cli.py:32-33`); this brief does not re-propose it.

`bars` is **>98 % of the database**: every other table together is ≈26 MB (`pg_stat_user_tables`), which is why it is 99.6 % of the proof.

### 1.4 Constants derived once, used everywhere below

| constant | value | arithmetic |
|---|---|---|
| bytes per row | **162.79 B** | 1,438,171,136 ÷ 8,834,532 |
| **MiB per million rows** | **155.24** (97.55 heap + 57.68 index) | 1371.5 MiB ÷ 8.8345 M |
| rows per ticker per full day | **507.3** | 296,286 ÷ 584 (2026-09-14) |
| **rows per trading day, today's universe** | **266,541** | 3,465,033 ÷ 13 trading days (September) |
| proof throughput | **170,000 rows/s per side** (band 166 k–188 k) | §1.3 |

### 1.5 Write pressure today — why the heap is the shape it is

```sql
SELECT n_live_tup, n_dead_tup, n_tup_ins, n_tup_upd, n_tup_hot_upd, autovacuum_count FROM pg_stat_user_tables WHERE relname='bars'
```
→ live 8,841,722 · dead **1,432,386** · inserts 8,834,533 · **updates 41,053,107** · HOT updates 1,402,741 · autovacuums 29.

**4.6 tuple versions written per stored row, only 3.4 % of them HOT.** That is the nightly `ON CONFLICT DO UPDATE` overlay R14 already ruled against. At 97.6 MiB/M the heap is *not* materially bloated today (80 rows/page ≈ the theoretical density), but `bars_pkey` carries **60.5 bytes per entry** against a theoretical ≈40, so **≈170 MiB of the 509 MiB index is plausibly bloat** — an ESTIMATE from that arithmetic, not a measurement. The partition copy in §2.1 rebuilds it for free.

---

## §2 The seven questions

Every option carries: what it is · benefit with arithmetic · cost/downside · cost of being wrong · a recommendation. **Chunk = one prompt, one hub, one suite run.**

---

### §2.1 — Q1 PARTITIONING

His words (`cto-2026-09-18.md` R15): *"we also need to figure out how to partition that table and make it really highly accessible in the future."*

**The three real access patterns, from code:**

| pattern | shape | today's cost |
|---|---|---|
| **poller write** (`radar/poller.py:88-103`) | per ticker, ~5 rows, every ~100 s, ≈500 tickers, always the newest minutes | one `ON CONFLICT` probe into a 509 MiB index per row |
| **archiver append** (`archiver/runner.py:354`, `store.py:283`) | per (ticker, interval), the last ≈2 sessions, nightly, quiet | range read on a PK prefix — already cheap |
| **replay / backfill read** (`radar/replay.py:136`) | `interval='i1' AND ts >= day-14 AND ts < day+1`, **no ticker predicate** | **2,677,237 rows** for a single 15-day window, and the PK leads with `ticker`, so **no index helps it at all** |

`radar/store.py:326 i1_bars(ticker, start, end)` and `archiver/store.py:283 bars_in_range(...)` are PK-prefix reads and are fast today and after any option below.

**A design requirement that binds every RANGE option, and that a naive build will get wrong:** `ts` is `timestamptz` (UTC). An after-hours session runs 16:00–20:00 ET = 20:00–00:00 UTC, so **a UTC-midnight partition bound splits a trading session in half**. Partition bounds must be written in ET (`FROM ('2026-10-05 00:00:00-04') TO (...)`). No session crosses ET midnight, so ET-aligned bounds keep every session whole. This is checkable in the DDL and must be a test.

**Postgres facts that make this legal:** the partition key must appear in every unique constraint — `ts` is already the third column of `bars_pkey (ticker, interval, ts)`, so the PK survives unchanged and `INSERT … ON CONFLICT (ticker, interval, ts) DO UPDATE` on the parent is supported (PG 11+; we are on pg16). No FK, no trigger, no view depends on `bars` (§1.1), so a swap touches nothing else. Grants must be re-applied on the new parent — a named migration step, not an assumption.

| | **P1 — no partitioning; add an index for replay** | **P2 — RANGE(ts), MONTHLY, ET-aligned** | **P3 — RANGE(ts), WEEKLY, ET-aligned** *(recommended)* | **P4 — RANGE(ts), DAILY, ET-aligned** |
|---|---|---|---|---|
| **what it is** | leave the table whole; add `btree (ts)` or BRIN so replay's 15-day scan stops reading everything | one child table per calendar month | one child table per trading week (Mon–Sun ET) | one child table per calendar day |
| **benefit** | replay's 2.68 M-row scan becomes a range scan; **nothing else changes** | open partition ≈ **5,597,361 rows** (21 × 266,541) → bounded proof **32.9 s/side, 65.9 s both** — saves 41 s of 106.8 s | open partition ≈ **1,332,705 rows** (5 × 266,541) → bounded proof **7.8 s/side, 15.7 s both** — **saves 91 s of 106.8 s; the 149 s outage becomes ≈58 s** | open partition ≈ **266,541 rows** → **1.6 s/side, 3.1 s both** |
| **also** | — | retention = `DETACH`/`DROP` (instant, no `DELETE`, no `VACUUM`); per-partition index ≈ 323 MiB | same, per-partition index ≈ 77 MiB; poller writes into a small hot index | same, index ≈ 15 MiB; the best write locality |
| **cost** | 1 chunk. **Does nothing for the proof** (still 106.8 s) and nothing for retention. A second index adds ≈58 MiB/M rows and another write per insert | 3 chunks. Migration = a full copy of 5.28 M rows. **Already at its limit today**: one month ≈ the whole current i1 table | 3 chunks. 52 partitions/year; 12 at a 90-day retention. Week boundaries must be defined once and never drift | 4 chunks. **252 partitions/year, 730 at 2 years** — planner and `pg_class` overhead, and `\d+` becomes unusable by hand. Partition maintenance becomes load-bearing daily |
| **cost of being wrong** | cheap — `DROP INDEX`, seconds | expensive — re-partitioning to a narrower width is a second full copy (another 3 chunks) **unless** the width is changed going FORWARD only, which RANGE allows | same, and cheaper in practice: **the width of future partitions can be changed without touching one existing row** | cheap to widen going forward; the accumulated partition count is permanent until retention removes it |
| **verdict** | a stepping stone, not a design (L52) | fails on its own arithmetic today | **RECOMMENDED** | correct at full-market scale, premature now |

**Recommendation: P3 — weekly RANGE(`ts`), ET-aligned, width revisable per period.** The single reason: it is the only option whose measured open-partition proof (15.7 s) is under the existing outage budget *today* and stays there while the table grows, and RANGE lets the width narrow later for new periods without rewriting a single stored row.

**What it does to the migration proof cost, plainly:** 106.8 s → **15.7 s**, and it stops being a function of the table's size at all (§2.5, §2.7).

**Rejected without a table, and why, so it is not re-proposed:** LIST(`interval`) partitioning — mooted by R9, one interval survives. HASH(`ticker`) — spreads writes but every partition still holds every date, so it helps neither retention nor the proof.

---

### §2.2 — Q2 RETENTION AND DERIVATION

**First, the derivation question is settled by measurement, not by argument.** Against production, each interval was rebuilt from stored i1 (bucket = epoch-floor; identical to `archiver/aggregate.py`'s ET wall-clock floor because every stored width divides 60 and ET offsets are whole hours) and compared field by field:

| derived | bars compared | identical on all five OHLCV fields | exceptions |
|---|---:|---:|---|
| i2 | 1,780,528 (**= every vendor i2 row**) | 1,780,476 | **52** |
| i5 | 835,818 | **835,818** | 0 |
| i15 | 131,950 | **131,950** | 0 |
| i30 | 69,550 | **69,550** | 0 |
| **total** | **2,817,846** | **2,817,794 (99.9982 %)** | **52** |

Coverage was checked separately: of 190,046 vendor i5 bars with no derived twin, **190,046 lie outside that ticker's own i1 span and 0 lie inside it** — so inside i1's coverage the derivation has no holes, only outside it.

*Full comparison query (i2 form; /300, /900, /1800 for the others):*
```sql
WITH src AS (SELECT ticker, to_timestamp(floor(extract(epoch FROM ts)/120)*120) AS bucket,
                    ts, open, high, low, close, volume
             FROM system.bars WHERE "interval"='i1'),
     agg AS (SELECT ticker, bucket, (array_agg(open ORDER BY ts))[1] AS o, max(high) AS h,
                    min(low) AS l, (array_agg(close ORDER BY ts DESC))[1] AS c, sum(volume) AS v
             FROM src GROUP BY ticker, bucket)
SELECT count(*), count(*) FILTER (WHERE a.o=b.open AND a.h=b.high AND a.l=b.low
                                    AND a.c=b.close AND a.v=b.volume)
FROM agg a JOIN system.bars b ON b."interval"='i2' AND b.ticker=a.ticker AND b.ts=a.bucket
```

**So: everything is derivable going forward, exactly. The boundary is per ticker and it is `min(ts)` of that ticker's i1.** Before that instant nothing can be derived — and beyond ≈14 calendar days back it can never be fetched again either.

**The extended-hours trap, carried and not buried.** i1/i5 carry 04:00–20:00; i15/i30 carry 09:30–15:45/15:30 only. A derived i15 or i30 built from all of i1 will therefore be **wider than the vendor's** and will not equal it. The 100 % match above holds because the comparison joins on the vendor's own keys, which exist only inside RTH. **Any derived i15/i30 must declare which it is — RTH-only (matches the vendor) or extended-inclusive (does not) — and the flag must be on the artifact, never implied.** After R9 this only matters for research output, since nothing on the card path reads above i1.

**A second trap found this session, which also disposes of Grok's half-day dissent for i30.** On the two 2025 half days the vendor's i30 grid still runs to 15:30 ET although the market closed at 13:00:

```sql
SELECT (ts AT TIME ZONE 'America/New_York')::time, volume FROM system.bars
WHERE ticker='SPY' AND "interval"='i30' AND (ts AT TIME ZONE 'America/New_York')::date = DATE '2025-11-28'
```
→ 13:00 457,893 · 13:30 101,591 · 14:00 663,756 · 14:30 12,129 · 15:00 11,247 · **15:30 20,965**. The vendor folds post-close extended prints into bars labelled regular-session. **i30 is not merely blind to extended hours; on a half day it silently mislabels them.** i1 has no such defect — it is stamped per minute and the session label is derived from the timestamp.

Now retention. **The vendor window is the whole decision** (measured 2026-08-27, `tribunal-archiver-r3-0919/finviz-windows.md`, tested against the live export): **i1 ≈ 14 calendar days**, i5 ≈ 21, i15 ≈ 3 weeks, i30/h ≈ 9.6 months, d/w ≈ 10 years, m ≈ full listing history. Seven date-range parameter names were tried and **all had zero effect** — depth is fixed per interval. **A deleted i1 bar older than ~14 days does not come back.**

**Real scenarios, computed from §1.4 (266,541 rows/trading day, 21 trading days/month, 155.24 MiB per million rows, 170,000 rows/s per side):**

| keep i1 for | steady-state rows | size | proof both sides, unpartitioned | vs "forever" at 12 months, saved |
|---|---:|---:|---:|---:|
| **30 calendar days** (≈21 td) | 5.60 M | **869 MiB** | 65.9 s | 66.85 M rows / **10.13 GiB** |
| **90 calendar days** (≈63 td) | 16.79 M | **2.55 GiB** | 197.5 s | 55.66 M rows / **8.44 GiB** |
| **365 calendar days** (≈252 td) | 67.17 M | **10.2 GiB** | 790 s (13.2 min) | 5.28 M rows / 0.80 GiB |
| **forever** | 72.45 M at 12 mo, 139.6 M at 24 mo | 11.0 GiB / 21.2 GiB | 852 s / 1,643 s | — |

**What stops being possible at each, concretely:**
- **30 days** — `radar/replay.py:136` reads a **14-calendar-day** window, so the live replay still fits with ≈7 days of slack, and `prior_sessions=5` fits. What dies: re-running an old day's counterfactual R against a changed rule set more than a month later; any month-over-month comparison. **L8 bites here**: a per-setup sample of n≥30 is not reachable in 21 trading days for anything but the most frequent setup, so EV stays "insufficient data" for most playbooks.
- **90 days** — a quarter. n≥30 becomes reachable for a setup that triggers ≈weekly per name. Seasonality and earnings-cycle questions still die.
- **365 days** — one full seasonal pass; the replay/counterfactual can be re-run against any rule change inside the year.
- **The missed-record counterfactual R (F12/F13)** loses nothing on the DAY at any retention — it reads the current session. It loses the *re-run*, which is the thing that makes a rule change auditable (L57).

| | **R1 — keep everything** | **R2 — rolling window, `DROP` the old partition** | **R3 — rolling window, `DETACH` + cold file, never `DROP`** *(recommended)* | **R4 — rolling window + a permanent derived rollup** |
|---|---|---|---|---|
| **what it is** | status quo; the table grows forever | past the window, the partition is dropped | past the window, the partition is detached and written to a compressed file on disk beside the DB; the table is dropped only after the file verifies | R3 plus a small permanent table of i1-derived daily/30-minute summaries kept forever |
| **benefit** | nothing is ever lost | the arithmetic above: at 30 days the table sits at 869 MiB permanently, forever, at any ticker count the window admits | same arithmetic, **and the decision is reversible**: a 30-day window can be widened later by re-attaching files the vendor would never re-serve | same, and a long-horizon question survives a short window at ≈1/500 of the storage |
| **cost** | 12-month proof 852 s; 24-month 1,643 s — a deploy becomes a half-hour outage. **Not a candidate** | 1 chunk. **Irreversible by construction.** A window chosen too tight is discovered months later with nothing to recover | 1.5 chunks (export + a verify-before-drop step). Disk grows ≈155 MiB per million archived rows — **UNVERIFIABLE FROM READS: `df -h /Users/cobalt/cobalt/data/postgres`** | 2.5 chunks. A second derived artifact is a second path (L3) unless it is generated by the one derivation function |
| **cost of being wrong** | catastrophic and slow — the way back is R2/R3 applied late, which deletes the same rows anyway | **total** — the vendor will not re-serve i1 past ≈14 days | **near zero** — re-attach the file | as R3, plus a rollup whose definition changed is a silently wrong history |
| **his test** | — | — | — | **a rollup is not dissectable into i1/i2, so R9's standing test says it is irrelevant.** It is listed only because it is the one shape that buys long horizons cheaply; **it needs his explicit exception or it does not exist** |

**Recommendation: R3.** The single reason: every other option on this page can be undone by running a migration again; retention is the only one the vendor makes permanent, and `DETACH`-to-file costs half a chunk more than `DROP` to remove that property entirely.

**The period itself is HIS (L53) and is not proposed here.**

---

### §2.3 — Q3 THE FORMING-BAR QUESTION

**The answer is mostly already built, and this is the cheapest section of the brief.**

- `radar/poller.py:88` fetches `Interval.I1` and nothing else — the poller **already writes i1 only**.
- `radar/poller.py:99-101`: `closed = [bar for bar in bars if bar.ts + timedelta(minutes=1) <= now and (threshold is None or bar.ts > threshold)]` — **the forming minute is excluded by construction, today, before any of this design.**
- `radar/anatomy/bars.py:87` `working_bars(i1, minutes, as_of=…)` never emits an unclosed bucket, and flags a closed bucket missing any minute (`complete=False`, `IncompleteBucket`). The derivation layer already refuses to fabricate a partial bar.
- The nightly archiver runs at 20:30 in `market_reset`, when the poller is idle — R15's premise holds.

**So what actually changes for a partitioned table:** nothing about *forming* bars, and exactly one new failure mode — **a write arriving for an instant no partition covers.** That is not a forming-bar problem; it is a maintenance problem, and it is the one way a partitioned `bars` can lose a write silently.

| | **F1 — pin today's behaviour, add nothing** | **F2 — pre-created horizon, NO `DEFAULT` partition** *(recommended)* | **F3 — `DEFAULT` partition as a safety net** |
|---|---|---|---|
| **what it is** | a test that asserts the poller drops the forming minute and that `working_bars` drops an unclosed bucket; no new machinery | a job creates partitions N periods ahead; there is **no** `DEFAULT`, so a write outside every range **raises** | a `DEFAULT` partition catches anything unrouted |
| **benefit** | 0.25 chunk; locks in behaviour that is currently only implied by code | L1 fail-loud, exactly: a missing partition is a loud `no partition of relation "bars" found`, at the poller, at 04:00, in the log, not six weeks later. A heartbeat probe asserting "≥N future partitions exist" makes it a **warning instead of an incident** | the poller never fails |
| **cost** | does not address the new failure mode at all | 1 chunk (creation job + probe + tests). A missed job = a poller failure the next period — which is why the probe exists | **the rows land somewhere, and the bounded proof's model breaks**: a `DEFAULT` partition is never "closed", so it must be digested every deploy. It also cannot be split later without a rewrite |
| **cost of being wrong** | the failure mode arrives unguarded | a loud failure at 04:00 ET on a Monday; fixed by one `CREATE TABLE … PARTITION OF` | **silent**: correct data in the wrong place, discovered when the proof cost stops falling |

**Recommendation: F2.** The single reason: a partitioned `bars` has exactly one silent-loss path, and `DEFAULT` is it.

**And for a derivation running while the poller is live:** `working_bars`'s `as_of` gate is already the correct rule and is already the one path — a 2-minute bucket is complete only when both minutes have closed *and* both rows are present. The derivation needs no lock and no coordination with the poller, because it never reads a row the poller has not committed and never emits a bucket whose last minute is still open. **This is already true; it needs a test, not a build.**

---

### §2.4 — Q4 THE REPAIR SEAM (carried OPEN dissent — A is ruled, B is not rejected on merit)

`09-19 R8` ruled **A**, his word, 09:30 ET: `restate --apply` and `backfill-missing` run **only in a QUIET WINDOW** — radar idle, ≥5 min after the last poll cycle completed, ≥10 min before the next session opens; **the live poller is not touched.** Built as `archiver/quiet.py`. **This brief does not re-rule A.**

**Gemini and Astra dissented for B, and their reasoning is a mechanism, not a preference.** Astra's sequence, verbatim from `TRIBUNAL-R3.md`: *"repair starts 03:59:50 (closed), poller fetches A 04:00:05, repair commits B 04:00:10, poller upserts A 04:00:20."* The collating hub's own verdict on that row: **"HOLDS on the mechanism (start-time check only)."** The supporting facts it verified from code: the poller takes **no** archive lock; its `before_commit` hook is optional (`poller.py:64` `… | None = None`); no staged code validates a repair generation (`poller.py:103`, `store.py:93-94`). A is a *bound*, not an exclusion — the FINAL design says so itself (§12 known limit 2: *"Option A's closing-side protection is a bound, not an exclusion. B is Sunday's."*).

| | **A — quiet window only** *(RULED, in force)* | **B — per-target repair marker the poller checks inside its write transaction** | **C — maintenance barrier that drains in-flight polling** | **D — repair on a DETACHED partition, then re-attach** |
|---|---|---|---|---|
| **what it is** | repairs refuse outside a quiet window; poller untouched | a repair sets a marker; the poller's write transaction reads it and discards a response fetched before the marker | a barrier that stops the poller, waits for in-flight fetches to land, holds until the repair releases | detach the partition holding the repair range, repair the detached copy, verify, re-attach |
| **benefit** | **zero risk to the live radar**, which is why it was ruled; already built | **closes the mechanism**: no repaired price can be overwritten, at any clock time. Removes the dependency on `archiver.repair.cycle_max_min` (O-2, PROPOSED 30, still a guessed bound) | strongest guarantee; also covers a repair crossing a session open | **the poller physically cannot reach the rows** — a detached partition is not part of `bars`. Needs no poller change and no lock, and it only exists if partitioning lands |
| **cost** | 0 (built). **Known limit stands**: Astra's 03:59:50 sequence | **touches the LIVE radar's write path** — the one thing R8 protected. 2 chunks + a three-house check + a shadow. L67 floor applies to the poller change itself | 3 chunks. A drain is new machinery on the live radar and a new way for the radar to stall | 1.5 chunks **on top of P3**. Only works for a repair confined to a closed period; a repair inside the open partition still needs A or B |
| **cost of being wrong** | a reviewed correction is silently overwritten; discovered only by a later audit | a bug in the poller's write path is a live-radar outage at 04:00 — the highest-consequence code in the system | as B, plus a stalled radar is indistinguishable from a dead one | low: a failed re-attach is loud and the original partition is still detached, not lost |

**The proposing house's recommendation, offered as input and not as a re-ruling: D for closed periods, A unchanged for the open one, and B held.** The single reason: D gets Gemini's and Astra's guarantee for the overwhelming majority of repairs (a repair of last month's data) **without touching the poller at all**, which is precisely what R8 protected — and it costs 1.5 chunks instead of 2 chunks plus a live-radar risk.

**This is a recommendation to the tribunal. A stands until he rules otherwise; the dissents are carried forward verbatim in §5.**

---

### §2.5 — Q5 THE MIGRATION PROOF ITSELF

What it is today (`db_migrations/cli.py:307-340`): per table, `SELECT (to_jsonb(t) − excluded)::text FROM <rel> AS t ORDER BY <pk>`, streamed through a named cursor in 10,000-row batches, folded into one md5, **counted by the fold**. Run BEFORE and AFTER, inside the outage, under `REPEATABLE READ`. Its bytes are deliberately identical to the pre-2026-09-18 server-side aggregate so every historical digest stays comparable — that property is worth keeping and no option below breaks it.

| | **MP1 — status quo** | **MP2 — partition-scoped digest ledger + closed-partition REVOKE + `relfilenode` guard** *(recommended, needs P3)* | **MP3 — exempt `bars` from the content digest** | **MP4 — scope the content digest by the migration's own DDL** *(recommended as the interim)* |
|---|---|---|---|---|
| **what it is** | read the whole table twice, every deploy | a closed partition is digested **once**, writes are `REVOKE`d from every role including the migration role, and the digest is stored in `system.bars_digest`. Each deploy re-reads only the OPEN partition and proves the closed ones from the catalog: `pg_class.relfilenode` + `relpages` + row count unchanged | row count and schema only for bulk tables | the harness already knows every table each registered migration names; a table the migration does not touch gets `relfilenode` + `relpages` + row count instead of a content digest |
| **benefit** | the strongest proof there is | **106.8 s → 15.7 s** (open week 1,332,705 rows ÷ 170,000 × 2). **And it stops scaling with the table**: the number is a function of partition width only, so it is still 15.7 s at 72 M rows. A rewrite of a closed partition changes `relfilenode` and is caught; a row-level change is impossible because no role may write | 106.8 s → ≈0.5 s | **106.8 s → ≈0.5 s for every migration that does not name `bars` — which is most of them (0001–0011: four name it, seven do not).** Ships in 1 chunk with **no schema change and no partitioning**, so it is available before anything else on this page |
| **cost** | the whole lever left on the table; every future deploy pays | 2 chunks, and it depends on P3 landing first. The REVOKE must not break the archiver's *write* path into the open partition — a named test. A closed partition that must be repaired needs an explicit un-REVOKE, which is §2.4 option D's seam | **already rejected in code** (`cli.py:32-33`), and correctly: the weakest proof exactly where the data is | 1 chunk. **It is a real weakening**: a migration that touches `bars` *unintentionally* (a stray statement, a cascading `ALTER`) is caught only if it changes `relfilenode`, `relpages` or the row count. An in-place `UPDATE` of column values would pass |
| **cost of being wrong** | none; it is the status quo | if the ledger is wrong, a closed partition is trusted that should not be — mitigated because the REVOKE makes the untrusted case physically impossible, and one `--proof-only --full` re-reads everything | the failure it was written to catch goes undetected | a bad migration's content damage is found by the next full proof, not by that deploy. **Because it narrows a trust boundary, it is HIS ruling, not the tribunal's** |

**Recommendation: MP4 now, MP2 when P3 lands, and keep MP1 available as `--proof-only --full` for any deploy he wants proven the old way.** The single reason: MP4 removes 106.8 s from most deploys this week with one chunk and no schema change, and MP2 removes it from *all* deploys permanently once the partitions exist.

**A number the tribunal should check.** MP2's saving assumes the open partition is re-read at its **worst case** (Friday of a full week). The average is half that — ≈7.9 s both sides. Where two options differ by less than the ±13 % host-load band of §1.3, that is stated: **MP2 and MP4 are indistinguishable for a migration that does not touch `bars`** (both ≈0.5 s), and they differ only for one that does.

---

### §2.6 — Q6 i1 ONLY: HOW, AND WHAT BREAKS

**RULED INPUT (`cto-2026-09-20.md` R9 + R9 extended): `system.bars` stores i1 only; i1 is also the only source of session segmentation. Not reopened here.**

#### (a) Every reader of a non-i1 interval, before a row is deleted

Scan performed: `grep -rnE "\bi(1|2|5|15|30)\b"` over `src/` and `configs/`; every SQL string matching `system.bars`/`FROM bars`; every call site of the two range readers; the vault Lists note; `configs/cobalt/smoke/s2.yaml`; `docs/40 - DevDocs/`.

| site | file:line | what interval it uses | breaks when non-i1 rows go? |
|---|---|---|---|
| radar poller (the only intraday writer) | `radar/poller.py:88, 96` | `Interval.I1` hardcoded | **no** |
| live engine bar read | `radar/store.py:332-333` | `interval = 'i1'` literal | **no** |
| replay snapshot build | `radar/replay.py:136` | `interval = 'i1'` literal | **no** |
| replay cards / formations | `replay/runner.py:383, 410` | `Interval.I1` | **no** |
| movers coverage check | `replay/movers.py:543` | `Interval.I1` | **no** |
| card audit export | `radar/audit_export.py:335` | via `i1_bars` | **no** |
| evaluate CLI | `radar/evaluate_cli.py:188` | via `i1_bars` | **no** |
| archiver watermark | `archiver/store.py:173` | default `"i1"`, called with `Interval.I1` from the poller | **no** |
| archiver nightly / shadow | `archiver/runner.py:354`, `shadow.py:155` | **whatever the Lists note's `archive:` says** | **no** — it stops fetching them, which is the point of (d) |
| `restate` / `backfill-missing` default | `archiver/cli.py:341` | `archive_progress` rows for that ticker, **else `[Interval.I1]`** | **no** — `system.archive_progress` is **empty (0 rows, measured)**, so it already falls back to i1 |
| `s2.yaml` smoke | `configs/cobalt/smoke/s2.yaml:297, 342` | `movers_daily.bars_archived`, set from an **i1** fetch | **no** |
| `count_rows()` | `archiver/store.py:182` | interval-agnostic `count(*)`; **called only from `tests/cobalt/test_archiver_store.py:55,60`** | **no** |
| DevDocs prose | `archiver/__init__.md:119`, `probes.md:109`, `collector.md:28-29`, `store.md:60`, `reconcile.md:41` | documentation only | **no runtime effect; five DevDoc edits owed at sprint close** |

**Finding: there are NO readers of a non-i1 interval anywhere in `src/`, `configs/` or the smoke suite. Zero.** The only non-i1 *consumer* is the archiver's fetch list, which is a field in the vault Lists note, not code. The statement in `areas/cobalt-product-definition.md` 2026-09-18 that "consumers read i5/i30 rows today" is **not true against the current tree** and should be corrected at the fold.

**Two code paths that will become dead but must not be deleted casually:** `archiver/models.py:22-26` (the `Interval` enum) is what `archiver/aggregate.py:18` uses to *label* a derived bar (`Interval(f"i{minutes}")`), so removing the members would break the derivation for the very widths R9 wants derived. **Keep the enum; it stops describing storage and starts describing derivation.** Note its hidden constraint: `aggregate()` can only produce widths in {1,2,5,15,30} — a request for i3 or i10 raises. That is a real limit on "derive whatever we need" and is worth ruling on separately.

#### (b) Does a derived i2 equal the vendor's i2 exactly?

**Measured, full overlapping range — §2.2.** Every one of the **1,780,528** vendor i2 rows has a derived twin; **1,780,476 are identical on all five fields (99.9971 %)**. The **52** exceptions:

```sql
… WHERE NOT (a.o=b.open AND a.h=b.high AND a.l=b.low AND a.c=b.close AND a.v=b.volume)
```
→ **1 distinct day (2026-09-03), 18 tickers, all between 04:00 and 08:08 ET — every one of them premarket, every one an ETF or index product** (SPY, QQQ, DIA, IWM, GLD, SLV, TLT, USO, XBI, XLB/E/F/K/U/V, IGV, QTUM, SOXL, DRAM). Direction: **derived volume ≥ vendor volume in 52 of 52**, and the derived range is a strict superset in **49 of 52** (the three exceptions are DRAM 04:02, DRAM 04:04, QTUM 04:00, where the vendor's low is 0.04–0.10 lower). Worked example, DIA 2026-09-03 04:06 ET, one i1 bar in the bucket: derived high 532.15 / vendor 532.04, same volume 111. Worst volume divergences: GLD 07:54 derived 1,824 vs vendor 1; USO 08:06 derived 371 vs vendor 2; DRAM 07:52 derived 2,451 vs vendor 281.

**Reading: this does not qualify his ruling, it strengthens it.** On one premarket morning the vendor's own i2 export was truncated relative to its own i1 export. The i1-derived bar is the honest one. **If a house wants to argue the other way, the burden is the three DRAM/QTUM bars** — three bars out of 2.8 million, all premarket, all on a day the vendor was already demonstrably inconsistent with itself.

i5, i15 and i30 match **exactly, 100.0000 %, zero exceptions** (§2.2).

#### (c) The deletion of 3,553,219 rows

| | **D1 — one in-place `DELETE` + `VACUUM FULL`** | **D2 — batched `DELETE` in quiet windows + plain `VACUUM`** | **D3 — rewrite to a new table and swap** | **D4 — fold the deletion into the partition copy** *(recommended)* |
|---|---|---|---|---|
| **what it is** | `DELETE FROM system.bars WHERE interval <> 'i1'` then `VACUUM FULL` | 100 k-row batches over several quiet windows, then plain `VACUUM` + `REINDEX CONCURRENTLY` | `CREATE TABLE bars_new AS SELECT … WHERE interval='i1'`, build the PK, rename | the P3 migration copies **only** i1 rows into the new partitioned table. **The copy is the deletion.** |
| **benefit** | one statement; disk fully reclaimed | **no outage at all** — the residents never read those rows. 346.6 MiB of freed heap is reused by ≈3.5 M future i1 rows (≈13 trading days of writes) | fastest full reclaim: 5.28 M-row copy + one index build | **zero extra cost — the deletion is free.** Frees 551.6 MiB, rebuilds `bars_pkey` (recovering the ≈170 MiB of estimated index bloat, §1.5), and reclaims disk without any `VACUUM FULL` |
| **cost / lock** | `DELETE` holds ROW EXCLUSIVE (readers unaffected); `VACUUM FULL` holds **ACCESS EXCLUSIVE and rewrites the whole table**, needing ≈820 MiB of extra disk. **ESTIMATE, from the proof's measured 8.8 M rows in 53 s: ≈3–6 min total with residents down** — well past the 149 s outage budget | 1 chunk. 3.55 M dead tuples must be vacuumed; the heap never shrinks on disk (space is reused, not returned); `bars_pkey` bloat gets worse before `REINDEX CONCURRENTLY` fixes it | 2 chunks and a real outage for the swap; **and it is P3's migration done twice** | 0 additional chunks. Constrained to P3's schedule — it happens **during** partitioning, not before |
| **cost of being wrong** | a `VACUUM FULL` that overruns the window is an extended outage on a live-account system | low — reversible only in the sense that the rows are gone either way | the old table survives under a name until dropped: rollback is one rename | **lowest**: the legacy table survives under `bars_legacy` until he says drop it; rollback is two renames, sub-second |
| **when** | before or after partitioning; either way a separate outage | **any time — before partitioning, no deploy needed** | replaces P3 | **during P3** |

**Recommendation: D4, with D2 available if the tribunal wants the 40 % gone before partitioning is designed.** The single reason: partitioning already rewrites every surviving row, so any separate deletion is the same work done twice, plus a `VACUUM FULL` we would otherwise never run.

**Order that follows from this:** the deletion happens **during** the partitioning change, never before it and never after it.

#### (d) Stopping the poller and the archiver writing the other four

- **The poller needs no change at all.** `radar/poller.py:88` already fetches `Interval.I1` only.
- **The archiver's intervals are not in code.** They are the `archive:` list in each enabled block of the vault Lists note (`/Users/cobalt/Vault/Think/1 - Trading/Radar Lists.md`), read through `radar/sources.py:59-67 archive_targets()` → `archiver/config.py:34`. Today: **tier_a (185 tickers) `archive: [i1, i2, i5, i15, i30]`, `backfill_default: true`** · **tier_b (25 tickers) `archive: [i1, i5, i30]`** · tier_c (55) `archive: []`. 185 + 25 = **210 — exactly the 210 tickers measured in every non-i1 interval.**
- **The change is two lines in that note** — set both `archive:` lists to `[i1]`. **Zero code. Zero deploy. Zero migration.** Under L65 the desk makes that edit on his ruling; under L28 it is a human note, not a Cobalt write path.
- **It is already proven in production, twice.** tier_b's `i2` and `i15` were removed from that note earlier this month and the writes simply stopped: `max(ts)` for the 25 tier_b tickers is **i2 → 2026-09-03, i15 → 2026-09-02**, while i1/i5/i30 run to 2026-09-18. Nothing broke, nothing was reported, no code changed.
- **Side effect worth naming:** `backfill_targets()` (`sources.py:70-79`) returns the `backfill_default` block's `archive` list, so `cobalt archiver backfill-missing <ticker>` today fetches all five intervals. After the edit it fetches one. **That also cuts the archiver's nightly Finviz demand from ≈1,000 requests to ≈210** — a fifth — which is real headroom against the 50 rpm L53 ceiling and against `09-19 R34`'s total-demand refusal.

**Cost: 0 chunks, 1 desk edit, reversible by editing the note back (though the rows it would have written are gone past the vendor window).**

#### (e) What the freed 40 % does to the proof cost

| | rows | proof/side @170 k rows/s | both sides | share of a 149 s outage |
|---|---:|---:|---:|---:|
| today | 8,834,532 | 52.0 s | **106.8 s** (measured) | **72 %** |
| i1 only | 5,281,313 | **31.1 s** | **62.1 s** | 42 % of 149 s; the outage itself falls to **≈104 s**, of which the proof is **60 %** |
| i1 only **+ weekly partitions + MP2** | 1,332,705 read | **7.8 s** | **15.7 s** | **the outage falls to ≈58 s; the proof is 27 % of it** |

Arithmetic: 5,281,313 ÷ 170,000 = 31.07 s; × 2 = 62.14 s; 106.8 − 62.1 = **44.7 s saved by the deletion alone**. 1,332,705 ÷ 170,000 = 7.84 s; × 2 = 15.68 s; 106.8 − 15.7 = **91.1 s saved with partitions**. Both carry the ±13 % band of §1.3: the deletion saves 39–50 s, the partitioned proof saves 89–93 s.

**Stated plainly: the deletion is worth ≈45 s once; partitioning is worth ≈91 s every deploy, forever, and does not decay as the table grows. They are not alternatives — the deletion is free inside the partitioning work (D4).**

#### (f) Is i1's extended-hours coverage complete enough to derive on?

Measured on 2026-09-14 (584 tickers, the fullest recent day):

| session | ET minutes available | rows/ticker (mean) | density |
|---|---:|---:|---:|
| premarket 04:00–09:29 | 330 | 120.4 | **36.5 %** |
| regular 09:30–15:59 | 390 | 312.9 | **80.2 %** |
| after-hours 16:00–19:59 | 240 | 74.0 | **30.8 %** |

That looks alarming until the distribution is read. Per-ticker daily row counts that day: min 2 · p25 335 · **median 486** · p75 728 · p95 953 · **max 960**. And for liquid names the grid is **perfect**:

```sql
SELECT ticker, count(*), count(*) FILTER (WHERE t < time '09:30'), … GROUP BY ticker ORDER BY 2 DESC LIMIT 8
```
→ NVDA, AMD, INTC, GOOGL, AVGO, MU, NOK, KORU: **960 rows each = 330 premarket + 390 regular + 240 after-hours. The complete extended-session minute grid, every minute, no holes.**

**So a "gap" in i1 is overwhelmingly a minute in which an illiquid name did not trade — which is not missing data** (`replay/cards.py:150` already says exactly this: *"a minute with no trade has no i1 bar, and that is not missing data"*). Zero-volume bars are 0.07 % of the day, so the vendor emits a bar where there was a print and omits it where there was not.

**How to tell a vendor gap from a poller gap — a rule that is measurable and cheap:**

```sql
SELECT count(DISTINCT (ts AT TIME ZONE 'America/New_York')::time) FROM system.bars
WHERE "interval"='i1' AND ts >= … AND ts < …
```
→ on 2026-09-14 this returns **960 of 960 minutes present**, with **135 tickers in the thinnest minute and 258 at the median**. **A vendor gap is per-ticker and correlates with illiquidity; a poller gap removes a minute for EVERY ticker at once.** So: if a minute in [04:00, 20:00) has **zero** rows across the whole table on a trading day, that is a poller/system gap and is an incident; if a minute has rows for some tickers and not others, it is the tape. This is one query, it runs in under a second, and it belongs in the heartbeat. `radar/anatomy/bars.py:16` already records that the two "look identical in `system.bars`" — this makes them distinguishable at the *table* level, which is where the distinction actually exists.

Calendar check over the whole i1 span: the only absent weekdays are **2026-09-05 (Saturday)**, 2026-09-06 (Sunday) and **2026-09-07 (Labor Day, in `configs/cobalt/calendar/nyse-2026.yaml`)**. **No trading day is missing.**

One observation the tribunal should not skip: distinct tickers per day in i1 falls **584 → 536 → 481 → 423 → 337** across 2026-09-14 → 09-18 while `radar_membership` shows 536 → 376 → 379 → 552 → 462 over the same days. The two do not track. That is either archive lag on the most recent days or a coverage loss, and **it is not explained by anything in this brief** — it is a measurement worth one query before the design is built on today's numbers.

**Verdict on (f): yes, i1 is complete enough to derive on, and the proof is that every derived interval matched the vendor's exactly (§2.2). The density figure is a property of the tape, not of the archive.**

#### (g) Where session segmentation lives today

**It already lives in exactly one place, it is already config-driven, and it is already timestamp-derived — so R9 (extended) costs almost nothing to satisfy.**

| layer | file:line | what it holds |
|---|---|---|
| the resolver | `src/cobalt/session/clock.py:210` `_windows_for()` / `session(ts)` | builds the day's ordered `[start, end)` windows and walks them; refuses a naive datetime (ADR-0007's lesson as a precondition) |
| the boundaries | `configs/cobalt/taxonomy/tunables.yaml:239-315` | `session.premarket_open` (04:00), `rth_open` (09:30), `rth_close` (16:00), `aftermarket_close` (20:00), `market_reset_open/close`, plus `early_close.rth_close` (13:00) and `early_close.aftermarket_close` (17:00) — each with a named consumer (F16) |
| the calendar | `configs/cobalt/calendar/nyse-2025.yaml`, `nyse-2026.yaml` | holidays and early closes only; weekends derived; **fail-loud on an uncovered year** |
| the one consumer on bars | `radar/anatomy/bars.py:135 rth_only(series, clock)` | keeps buckets that open **and** close inside RTH |

There is **no second copy**: no SQL, no collector-side, no card-engine literal. A grep for `09:30`/`16:00`/`04:00` across `src/` returns only docstrings, `archiver/runner.py:49` (which reads the *same tunables*), and CLI argument help text.

**What is actually missing: premarket and after-hours siblings of `rth_only()` — roughly ten lines.** Today only RTH can be selected. Cost to make i1-derived segmentation the one path under L3: **0.25 chunk and a test**, because the path already exists and already handles early closes.

#### (h) Boundary and edge cases, with real dates to test against

| case | does it change an answer? | why, and the date to test |
|---|---|---|
| a bucket straddling 09:30 | **No — provably.** | Every stored width divides 60 and ET offsets are whole hours, so a 2/5/15/30-minute bucket **starts exactly at** 09:30, 16:00, 04:00 and 20:00. No bucket can straddle a session boundary. `radar/anatomy/bars.py:98-101` relies on this and says so. |
| **half day** | **Yes, for i30 — and it is another reason it goes.** | Vendor i30 on **2025-11-28** and **2025-12-24** carries bars to 15:30 ET against a 13:00 close, with real post-close volume folded into regular-session bars (§2.2). i1 has no such defect. |
| **half day, for i1** | **UNKNOWN — and it is the one edge case with no evidence.** | 2026's early closes are **2026-11-27** and **2026-12-24** — both in the future. The i1 archive begins 2026-07-30, so **no half day has ever been observed in i1.** The test must be written against the clock (`early_close.rth_close = 13:00`, `early_close.aftermarket_close = 17:00`) and re-verified live on 2026-11-27. |
| holiday | No. | **2026-09-07** (Labor Day) — zero rows in every interval, correctly. |
| DST transition | **Not verified, and it is a real risk for partition bounds.** | The next is **2026-11-01** (EDT→EST). ET-aligned partition bounds must be written with the *correct* offset per period (`-04` before, `-05` after). A bound written with a fixed offset silently shifts a session by an hour. **Test date: the week of 2026-11-01.** |
| weekend | No. | Partitions defined Mon–Sun ET; weekends simply carry no rows. |

---

### §2.7 — Q7 GROWTH: design for the table we will have

His words: *"that number is growing, so the growth of the database structure is exponential and not linear … we need to account for the growth of the number of tickers that are coming in daily and also give it room to grow even more."*

**The arrival rate, measured first, as instructed.**

```sql
WITH fs AS (SELECT ticker, min(trade_date) AS d0 FROM system.radar_membership GROUP BY ticker)
SELECT d0, count(*), sum(count(*)) OVER (ORDER BY d0) FROM fs GROUP BY d0 ORDER BY d0
```

| first seen | new tickers | cumulative distinct |
|---|---:|---:|
| 2026-09-14 | 536 | 536 |
| 2026-09-15 | 72 | 608 |
| 2026-09-16 | 47 | 655 |
| 2026-09-17 | 94 | 749 |
| 2026-09-18 | 111 | **860** |

`radar_membership` begins 2026-09-14 — **five trading days of history, and that is the whole evidence base.** Tickers *active per day*: 536 · 376 · 379 · 552 · 462 — **no trend.** New distinct names: +72, +47, +94, +111 — mean **81 per trading day**, no trend either.

```sql
WITH first_seen AS (SELECT ticker, min(ts) AS t0 FROM system.bars WHERE "interval"='i1' GROUP BY ticker)
SELECT date_trunc('week', t0 AT TIME ZONE 'America/New_York')::date, count(*) FROM first_seen GROUP BY 1 ORDER BY 1
```
→ 2026-07-27: 1 · 08-03: 1 · 08-10: 183 · 08-17: 25 · 08-24: 113 · 08-31: 261 · **nothing since 2026-09-03**. This is *archive onboarding*, not arrival: it says when each cohort was added to the watchlists, and `bars` holds **584 distinct tickers against `radar_membership`'s 860** — the archive is already 276 names behind the radar universe.

**What the evidence supports, said plainly, because it is not what the word "exponential" implies:**

- Rows per trading day = (tickers that day) × 507.3. **Tickers per day is flat.** ⇒ the table is **LINEAR in time**, at ≈266,541 rows/trading day, *with no ticker growth at all*.
- If the daily universe grows by a constant k names/day, cumulative rows are **QUADRATIC in time**, not exponential.
- **Exponential would require the daily universe itself to compound**, and a ticker universe cannot: it is coupon-collecting from a finite pool of liquid US names (a few thousand), so arrivals must saturate. Five days is far too short to see the saturation, which is the honest limit of this measurement.
- **The linear term alone already breaks us**, which is the finding that matters: at today's flat universe, with zero growth, the i1-only table reaches **72.4 M rows and 852 s of proof in twelve months.**

**Three scenarios, all at 507.3 rows/ticker/day, 21 trading days/month, 155.24 MiB per million rows, 170,000 rows/s per side:**

**S-FLAT — the measured rate continued (≈500 tickers/day, 266,541 rows/trading day):**

| horizon | rows | size | proof both sides, unpartitioned |
|---|---:|---:|---:|
| today | 5.28 M | 820 MiB | 62 s |
| +1 month | 10.88 M | 1.65 GiB | 128 s |
| +3 months | 22.07 M | 3.35 GiB | 260 s |
| +6 months | 38.86 M | 5.89 GiB | 457 s |
| +12 months | 72.45 M | 10.98 GiB | **852 s (14.2 min)** |
| +24 months | 139.6 M | 21.2 GiB | **1,643 s (27.4 min)** |

**S-GROW — a faster rate he might want (+10 *active* names per trading day on a 500 base; his own 09-18 expectation was "10–20 new names a day"). Rows over N trading days = 507.3 × (500N + 5N(N+1)):**

| horizon | rows | size | proof both sides |
|---|---:|---:|---:|
| +1 month (N=21) | 11.78 M | 1.79 GiB | 139 s |
| +3 months (N=63) | 31.49 M | 4.77 GiB | 370 s |
| +6 months (N=126) | 77.83 M | 11.8 GiB | 916 s |
| +12 months (N=252) | **230.9 M** | **35.0 GiB** | **2,716 s (45 min)** |
| +24 months (N=504) | **778.7 M** | **118 GiB** | **9,161 s (2.5 h)** |

**S-CEILING — a deliberate cap on the stored set (C tickers/day), with a retention window W trading days. Steady state = C × 507.3 × W, and it never grows again:**

| C | W = 21 td (≈30 days) | W = 63 td (≈90 days) | W = 252 td (≈365 days) |
|---|---|---|---|
| 600 | 6.39 M · 992 MiB · 75 s | 19.17 M · 2.91 GiB · 226 s | 76.7 M · 11.6 GiB · 902 s |
| 1,500 | 15.98 M · 2.42 GiB · 188 s | 47.9 M · 7.27 GiB · 564 s | 191.8 M · 29.1 GiB · 2,256 s |
| 5,000 (full market) | 53.3 M · 8.08 GiB · 627 s | 159.8 M · 24.2 GiB · 1,880 s | 639 M · 96.9 GiB · 7,519 s |

**And the same three scenarios with a partition-scoped proof (§2.5 MP2), which is the point of the whole design:**

| daily universe | rows in the open WEEK | proof both sides | rows in the open DAY | proof both sides |
|---|---:|---:|---:|---:|
| 500 (today) | 1.33 M | **15.7 s** | 266 k | 3.1 s |
| 1,500 | 3.80 M | **44.8 s** | 761 k | 9.0 s |
| 3,000 | 7.61 M | 89.5 s | 1.52 M | 17.9 s |
| 5,000 (full market) | 12.68 M | **149 s — the entire current outage** | 2.54 M | **29.9 s** |

**Where each option stops working, and the warning sign:**

| option | breaks when | today | the warning sign |
|---|---|---|---|
| **no partitioning** | the moment retention is unbounded | **already broken** at 12 months in every scenario | the `proof cost:` line in every deploy's output, already at 106.8 s |
| **monthly partitions** | rows/day > 243,000 (5.1 M per month at a 30 s/side budget) | **266,541/day — already past it** | the open partition's `probe secs` exceeds the previous month's |
| **weekly partitions** | rows/day > 1.02 M, i.e. **> ≈2,010 tickers/day** | 500/day — 4× headroom | same line, trending up week over week |
| **daily partitions** | rows/day > 5.1 M, i.e. **> ≈10,050 tickers/day** | beyond the whole US market | partition count / planning time, not proof time |

**The design property that answers his instruction to "give it room to grow even more":** with RANGE partitioning, **the width of *future* partitions can be narrowed without touching one stored row.** So the answer to growth is not to pick the right width today — it is to pick a width that is right today and to make narrowing it a config change rather than a migration. **That is why weekly is recommended over monthly (already at its limit) and over daily (premature): weekly has 4× headroom and can become daily for the next period at any time, for free.**

| | **G1 — no ceiling, weekly partitions, retention his** *(recommended)* | **G2 — no ceiling, daily partitions from day one** | **G3 — a hard ceiling on the stored ticker set** |
|---|---|---|---|
| **what it is** | store whatever the radar sees; weekly partitions; retention bounds the total | as G1 with daily partitions | cap how many tickers may be archived per day, in the Lists note |
| **benefit** | 15.7 s proof today, 44.8 s at 1,500 tickers/day; width narrows for free when the warning sign fires | 3.1 s today, 29.9 s at full market — headroom to the end of any plausible growth | the only option where total size is **bounded independently of retention**; makes the Finviz demand model exact |
| **cost** | must watch one number and act on it; a missed narrowing costs proof seconds, never data | 252 partitions/year from day one, for headroom nothing needs yet; partition maintenance becomes daily and load-bearing | **a ticker not archived is a ticker with no history, permanently** (14-day vendor window). It is also an L53 CAP and therefore **HIS** |
| **cost of being wrong** | one period of a slow proof; narrow the next one | operational overhead that is hard to undo downward | **the worst on this page**: the name he wanted to study is the one not stored |

**Recommendation: G1.** The single reason: it is the only option that keeps every name the radar touches — which is what makes a missed-record counterfactual honest — while putting the growth risk on a number the deploy prints every time and that can be fixed for free going forward.

---

## §3 What this costs to build, in chunks

A chunk = one prompt, one hub, one suite run. Every build is checked by ≥3 houses (L67); each check is counted separately and is not in these numbers.

| # | chunk | cost | what must be RULED before it starts |
|---|---|---:|---|
| **0** | **Stop writing non-i1** — two `archive:` lists in the vault Lists note set to `[i1]`; desk edit under L65; before/after diff in the desk report; a read-only parse proof afterwards | **0 chunks** (one desk edit) | nothing — R9 already rules it. **Available today.** |
| **1** | **MP4** — the proof's content digest scoped by the migration's own DDL; everything else gets `relfilenode` + `relpages` + row count; `--proof-only --full` keeps the old behaviour | 1 | **HIS**: narrowing a trust boundary (§4 item 5) |
| **2** | **Partition maintenance** — creation-ahead job, no `DEFAULT`, heartbeat probe for the future-partition horizon, ET-aligned bounds with a DST test (2026-11-01) | 1 | the partition WIDTH (tribunal, recommended weekly) |
| **3** | **The partitioned table, built online** — new partitioned `bars`, i1 rows copied in batches during quiet windows (**the copy is the deletion**, D4), grants re-applied, verified row-for-row against `bars_legacy` | 2 | width; and that the copy runs OUTSIDE any deploy window |
| **4** | **The swap** — two renames inside a deploy. Sub-second. `bars_legacy` kept until he says drop | 0.5 | L66 residents down; L43 window; L68 gate |
| **5** | **MP2** — `system.bars_digest`, REVOKE on closed partitions, `relfilenode` guard, proof integration | 2 | chunk 3 landed |
| **6** | **Retention** — `DETACH` + compressed cold file + verify + drop; period from config, validated on load (L10) | 1.5 | **HIS**: the retention period, and `DETACH`-to-file vs `DROP` (§4 items 1–2) |
| **7** | **Derivation + session segmentation** — `premarket_only`/`after_hours_only` beside `rth_only`; an RTH-vs-extended flag on every derived artifact; a `cobalt bars derive` read path over the one `aggregate()` | 1 | the `Interval` enum's {1,2,5,15,30} limit (§2.6a) |
| **8** | **Gap classifier** — the per-minute "zero tickers in this minute = system gap" query as a heartbeat probe (§2.6f) | 0.5 | nothing |
| **9** | **DevDocs + suite + smoke** — five DevDoc corrections, the s2 smoke read, the `Interval` docstrings | 1 | nothing |
| | **total** | **≈10.5 chunks** | |

**The ordering is not negotiable in two places:** chunk 0 before anything (it is free and it stops the bleeding), and the deletion inside chunk 3 — never as its own outage.

**Migration risk on a 1.4 GiB table, stated honestly:** chunks 3 and 4 are designed specifically so that **no long lock ever happens**. The copy is batched, online, outside any deploy; the only ACCESS EXCLUSIVE moment is two renames. **What the deploy actually risks is the swap, and its rollback is two renames back — sub-second, with `bars_legacy` physically intact.** Disk during the transition is ≈2× (an extra ≈820 MiB) — **UNVERIFIABLE FROM READS**, see §6.

---

## §4 What is HIS to rule (L53 and anything that reaches the card)

| # | the ruling owed | why it is his, not ours | what the brief gives him |
|---|---|---|---|
| **1** | **The i1 retention period** — 30 / 90 / 365 days / forever | L53: a retention period is a ceiling. And it is the one decision on this page the vendor makes permanent | §2.2's table: rows, MiB, proof seconds, what analysis dies, and the L8 sample-size consequence at each |
| **2** | **`DETACH` to a cold file, or `DROP`** | it decides whether item 1 is reversible | R3 vs R2 in §2.2; ≈0.5 chunk and ≈155 MiB per archived million rows is the entire price of reversibility |
| **3** | **A ceiling on the stored ticker set, or none** | L53: a cap | §2.7 G1 vs G3 — and the plain warning that an unarchived name has no history, permanently |
| **4** | **The repair seam: A stands, or B, or the D variant** | R8 was his; the dissents were carried to him | §2.4's four options and §5's verbatim dissents |
| **5** | **May the migration proof narrow its scope** (MP4) for tables a migration does not name | it weakens a trust boundary on a live-account system — not a tribunal call | §2.5: it saves 106.8 s on most deploys and would miss an unintended in-place `UPDATE` |
| **6** | **May a permanent i1-derived rollup exist** (§2.2 R4) | it fails his own standing R9 test ("not dissectable into i1/i2 ⇒ irrelevant"), so only he can except it | the cost (2.5 chunks) and the benefit (long horizons at ≈1/500 the storage) |

**Everything else in this brief is the tribunal's to settle**, including the partition width, the ET-alignment rule, the `DEFAULT`-partition question, the deletion method and the build order. Those are engine tunables and mechanisms, not ceilings.

---

## §5 Open dissents carried in

**Carried, still open, from `TRIBUNAL-R3.md` "Dissents for the owner", verbatim:**

1. **Gemini, on the repair seam (option B).** *"relying solely on the session clock to gate repairs ignores that delayed poller threads can still hold stale data when a repair commits; when the poller finally writes, it will overwrite your reviewed corrections with bad data … Until we enforce a strict per-target lock with generation checks for the poller … we cannot guarantee the integrity of the database."*
2. **Astra, on the same seam.** *"A repair started before scanning opens can still have its corrected prices overwritten."* And in full: *"Before enabling either mutating command, enforce exclusion covering in-flight poller fetches and writes, the complete repair transaction, and any scanning-session opening during that interval … A startup clock check, an estimated finish time or a lock ignored by the poller is insufficient. If enforced exclusion is unavailable, refuse mutation loudly; read-only preview remains available."*
3. **Astra, known limit 1 (mixed prices after a vendor restatement).** *"The unchanged poller can continue mixing old and adjusted prices despite the red dashboard."* Carried into `spec-final-design.md` §12.1; **this brief makes it worse, not better**, because under i1-only there is no i5/i30 copy to cross-check a restatement against, and because the append mode ahead of us does not heal it. **A house should attack this.**

**Answered by measurement this session, and therefore NOT carried:**

- **Grok, half-day closes.** His sequence was about the archiver's clock check. Against i30 it is worse than he argued — the vendor's i30 grid runs to 15:30 on a 13:00 close with post-close volume folded into regular bars (§2.2, 2025-11-28 / 2025-12-24). Against an **i1-only** table it is moot: i1 is stamped per minute and the session label is derived from the timestamp through `session/clock.py`, which already reads `early_close.rth_close`. **The remaining exposure is that no half day has ever been observed in i1 — 2026-11-27 is the first (§2.6h).**
- **`prod-proof-only-3` ESCALATE 1, "the proof grew 4.8× faster than the row count."** Not established: deploy 1 and deploy 3 read the *same* 8,834,532 rows and differed 13 % (§1.3). Under L70 an unproven escalate is not carried as a defect. **The measurement that would settle it is named in §6.**

---

## §6 `UNVERIFIABLE FROM READS`

Seven, each with the exact command that settles it (L70). None of these is asserted anywhere above.

1. **The vendor window, re-verified today.** The i1 ≈ 14 days / i5 ≈ 21 / i30 ≈ 9.6 months table is dated **2026-08-27** (`tribunal-archiver-r3-0919/finviz-windows.md`) and `system.archive_progress` is **empty (0 rows, measured)**, so production carries no current record of it. → `UNVERIFIABLE FROM READS — uv run cobalt archiver restate NVDA i1` (preview-only, read-only; it prints the fetched export's `export_oldest`/`export_newest`), or simply the first `append` night, Monday 2026-09-21 20:30, which populates `archive_progress`.
2. **The proof's query plan**, and therefore whether its cost is index-scan heap churn or serialisation CPU. `guard_select` accepts only `SELECT`/`WITH`, so `EXPLAIN` cannot run through my allowlist. → `UNVERIFIABLE FROM READS — psql -d cobalt_brain -c "EXPLAIN (ANALYZE, BUFFERS) SELECT (to_jsonb(t))::text FROM system.bars AS t ORDER BY t.ticker, t.\"interval\", t.ts"` on `cobalt_dev` at production scale.
3. **Whether the 47.05 s ↔ 53.29 s spread is host load or heap/index bloat.** → `UNVERIFIABLE FROM READS — VACUUM (ANALYZE) system.bars` on `cobalt_dev` at production scale, then `cobalt db migrate --proof-only` before and after; if the time does not move, it is host load and §1.3's linear model stands.
4. **The end-to-end cost of replay's 15-day read.** The row count is measured (2,677,237 for 2026-09-04→09-19) but the tool wraps every query in `LIMIT 1000`, so the transfer cost into Python is not. → `UNVERIFIABLE FROM READS — uv run cobalt radar replay-build --day 2026-09-18` timed on `cobalt_dev`.
5. **Disk headroom for the 2× transition and for cold retention files.** → `UNVERIFIABLE FROM READS — df -h /Users/cobalt/cobalt/data/postgres`.
6. **Real timings for D1/D2/D3 on a 1.4 GiB table** — every duration in §2.6c is an ESTIMATE scaled from the proof's measured 8.8 M rows in 53 s. → `UNVERIFIABLE FROM READS — restore a production-scale `cobalt_dev` and time `DELETE`, `VACUUM FULL` and the `INSERT … SELECT` copy.`
7. **Whether `INSERT … ON CONFLICT (ticker, interval, ts) DO UPDATE` on the partitioned parent performs equivalently for the poller.** It is *legal* (the PK contains the partition key; pg16), but the per-write cost is unmeasured. → `UNVERIFIABLE FROM READS — a `cobalt_dev` benchmark of `BarStore.upsert_bars` against a partitioned and an unpartitioned table at 500 tickers × 5 rows.`

**One correction owed at the fold, not an UNVERIFIABLE:** `areas/cobalt-product-definition.md` 2026-09-18 says the derivation layer must come first because "consumers read i5/i30 rows today". Against the current tree **no consumer reads any non-i1 row** (§2.6a). The line should be corrected when the desk next writes memory (L58).

---

*Hash convention for the stop line below: a file cannot contain its own digest, so the sha256 quoted is over **this document without its stop line** — verify with `sed -n "1,$(($(wc -l < FILE)-1))p" FILE | shasum -a 256`.*

BARS BRIEF READY 322b414313eb73e275ffb6433eb5b64664bfe800fac19bf563b60c240d68d345 · questions answered: 7/7 · options costed: 26 · his rulings owed: 6 · carried dissents: 3 · UNVERIFIABLE: 7
