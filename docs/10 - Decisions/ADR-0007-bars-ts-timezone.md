# ADR-0007 — `bars.ts`: reinterpret ET-under-UTC as true UTC

Date: 2026-09-04
Status: Accepted
Decided: with veto (Dejan) — **reinterpret, do not shift**.
Closes: the last open item of the 09-03/04 incident thread — *"`bars.ts`
= ET values under `+00` — Data-Model ADR rules it before any join;
prerequisite for 19b detector"* — and the `TESTARCH` follow-up left by
[ADR-0006](ADR-0006-rulings8-9-brain-cleanup-and-bars.md).
Relates to: ADR-0005 (the environment law), ADR-0006 (`bars` onto the
resolver). Delivered alongside F1 (`src/cobalt/session/`), which is the
other half of the same rule: **sessions are defined in ET, storage is
UTC, and no feature keys off wall-clock.**

## Context

`bars.ts` is `TIMESTAMPTZ`. Finviz's `/export/stock` CSV writes a bare
ET wall clock with no offset and no zone name — `09/03/2026 09:30 AM`
means 09:30 *America/New_York*. `collector._parse_finviz_datetime`
returned that as a **naive** `datetime`, psycopg handed the naive value
to a `timestamptz` column, and Postgres stamped it with the session
`TimeZone`, which on this server is `Etc/UTC`. The 09:30 ET opening bar
was therefore stored as `2026-09-03 09:30:00+00` — four hours early,
five in winter.

The whole corpus was wrong the same way, and the corpus is the evidence:

```
-- BEFORE: distribution of the stored wall-clock hour, all 4,755,477 rows
 wallclock_hour | count
 4  | 154865      10 | 467714      16 | 224304
 5  | 136850      11 | 467625      17 | 178378
 6  | 138489      12 | 467491      18 | 167456
 7  | 208015      13 | 467465      19 | 171430
 8  | 218156      14 | 467425
 9  | 352339      15 | 467475
```

Hours 04–19 inclusive and nothing else. That is exactly the ET session
window (premarket 04:00 → aftermarket close 20:00). Genuine UTC data
from the same window would occupy 08–23 in summer. The histogram alone
proves the entire table holds ET digits under a UTC label.

The single-row proof, `AAPL/i5`, 2026-09-03:

```
 ticker | interval | stored_ts                 | reads_as_utc | reads_as_et | correct_utc | volume
 AAPL   | i5       | 2026-09-03 09:30:00+00:00 | 09:30        | 05:30       | 13:30       | 569244
```

569,244 shares is the RTH opening print. It was sitting at a timestamp
that reads 05:30 ET — the middle of premarket, where the neighbouring
bars trade in the hundreds.

**Why it had to be ruled before anything joins `bars`.** The 19a radar
and the 19b trigger detector both join bars against session-aware logic.
A four-hour error is not a rounding problem: it makes every "was this
during RTH?" predicate wrong, every VWAP anchor wrong, and — because the
offset is 4 hours in summer and 5 in winter — wrong by a *different*
amount across the corpus, which is the kind of error that survives
spot-checking.

## Decision

**Reinterpret in place. Do not shift by a constant.**

```sql
ts = (ts AT TIME ZONE 'UTC') AT TIME ZONE 'America/New_York'
```

`ts AT TIME ZONE 'UTC'` strips the false label and yields the naive ET
wall clock the collector actually parsed. `AT TIME ZONE
'America/New_York'` then re-applies the *correct* zone, DST-aware per
row date. Rows in EST move 5 hours; rows in EDT move 4. A constant
`+ interval '4 hours'` would have been right for August and wrong for
January, silently.

**The primary key is dropped and re-added inside the same transaction.**
Converting `09:30` to `13:30` moves a row onto a timestamp that the
not-yet-converted 13:30 ET row still occupies, and a non-deferrable PK
checks uniqueness per row as the UPDATE walks the table — the migration
would fail on an artefact of row order, not on a real collision.
Dropping the constraint removes the false failure; **re-adding it is
itself the proof that the conversion introduced no real one.**

**The collector is fixed at the boundary, not at the store.**
`_parse_finviz_datetime` now localizes to `America/New_York` and
converts to UTC, and `Bar.ts` is `AwareDatetime` — a naive value is a
loud Pydantic failure at the edge, not a wrong row three weeks later.
The format-handling half is split out as `_parse_finviz_wall_clock` so
the two concerns (Finviz's inconsistent date strings; the timezone) are
separately testable.

## Proof

Run 2026-09-04 18:34 EDT — outside the 20:00–21:30 archiver window, as
ruled. Duration 42 s, one transaction, committed.

| Gate | Before | After | Verdict |
|---|---|---|---|
| row count | 4,755,477 | 4,755,477 | equal |
| md5 over ordered rows, **excluding `ts`** | `b67c17759c63ad1e60bbfe58f807913e` | `b67c17759c63ad1e60bbfe58f807913e` | identical — OHLCV untouched |
| md5 over ordered rows, **including `ts`** | `7d27ac6c8109977c21620878e611c052` | `5aae362a251b5b04a37b40b99e3d512b` | differs — `ts` is the only change |
| the 2026-09-03 09:30 ET probe row | `09:30:00+00` | `13:30:00+00` | 09:30 ET, correct |
| `min(ts)` | `2025-08-08 09:30+00` | `2025-08-08 13:30+00` | +4h — 08-08 is EDT |
| `max(ts)` | `2026-09-04 16:45+00` | `2026-09-04 20:45+00` | +4h — 09-04 is EDT |
| ET wall-clock hour histogram | 04–19 | 04–19, **counts byte-identical** | the ET clock is preserved exactly; only its label changed |
| PK re-add | — | clean | no collision anywhere in 4.75M rows |

Both md5s order by the ORIGINAL stored value on both sides (after the
conversion that is `ts AT TIME ZONE 'America/New_York'`, which
reproduces the original naive digits), so the row order is identical by
construction rather than by assumption.

**Dry run first, on `cobalt_dev`.** A 10,296-row stratified sample was
loaded and the same script run against it with the transaction rolled
back. The sample was chosen to straddle both DST regimes and both 2026
transitions — and the per-date shift is the DST proof:

```
 et_date    | rows | min_stored             | min_converted          | shift
 2025-10-30 |   26 | 2025-10-30 09:30:00+00 | 2025-10-30 13:30:00+00 | 04:00:00   EDT
 2025-10-31 |   26 | 2025-10-31 09:30:00+00 | 2025-10-31 13:30:00+00 | 04:00:00   EDT
 2025-11-03 |   26 | 2025-11-03 09:30:00+00 | 2025-11-03 14:30:00+00 | 05:00:00   EST  <- fall back
 2026-01-14 | 2509 | 2026-01-14 09:30:00+00 | 2026-01-14 14:30:00+00 | 05:00:00   EST
 2026-03-06 | 2509 | 2026-03-06 09:30:00+00 | 2026-03-06 14:30:00+00 | 05:00:00   EST
 2026-03-09 | 2491 | 2026-03-09 09:30:00+00 | 2026-03-09 13:30:00+00 | 04:00:00   EDT  <- spring forward
 2026-09-03 |  192 | 2026-09-03 04:00:00+00 | 2026-09-03 08:00:00+00 | 04:00:00   EDT
```

The sample was truncated afterwards through `cobalt.devdb`, restoring
RULING 9's `cobalt_dev.bars = empty` invariant.

**The spring-forward gap is empty.** Zero rows carry a stored wall clock
in 02:00–02:59 on either transition date, so no row had to be resolved
out of a nonexistent local time. Markets are closed then; the query
confirms it rather than assuming it.

**The archiver now writes UTC — proven on the real path, not asserted.**
`COBALT_ENV=production uv run archiver --backfill AAPL` (5 intervals,
21,718 rows, 0 failures) at 18:56 EDT:

```
 ticker | interval | stored_utc             | et               | volume
 AAPL   | i5       | 2026-09-04 22:55:00+00 | 2026-09-04 18:55 | 3
```

22:55 UTC = 18:55 ET. The decisive number is the **table total: 4,755,477
→ 4,755,738, a growth of 261 rows against 21,718 written.** Every other
row upserted onto a key that already existed — which can only happen if
the run's timestamps agree with the reinterpreted corpus. Had the
collector still emitted ET-under-UTC, ~21,000 duplicate rows would have
appeared alongside them.

## Rollback

`docs/00 - Project/incident-2026-09-03/bars-dump-20260904T182807.sql` —
`pg_dump --data-only --table=bars` of `cobalt_brain`, taken immediately
before the migration and after the `TESTARCH` delete.

- size: 330,192,554 bytes (316 MB)
- sha256: `588573550abeb45e9d98ef4c0180cb908ef38fa91c9bad30857adaf20273d542`
- contents: 4,755,477 rows in the PRE-conversion (ET-under-UTC) shape

Restoring it means `TRUNCATE bars` then loading the dump; the file is in
the gitignored incident directory alongside RULING 8/9's dumps.

Note what rollback would now cost: the archiver has written UTC rows on
top since. A restore is a return to the defect, not a return to a clean
state — which is the ordinary shape of a data migration and the reason
the proof above is what it is.

## Consequences, and the judgement calls inside them

- **Reinterpret, not shift, was Dejan's veto and it is load-bearing.**
  A constant shift is simpler, faster, and produces an identical result
  for every row between March and November. It is wrong for the winter
  half of the corpus, and the wrongness is invisible: the data still
  looks like market hours, just an hour off. The DST-aware conversion
  costs nothing extra and cannot be wrong on a date basis.

- **`TESTARCH` was deleted first, so the dump is the rollback for THIS
  change only.** ADR-0006 left one test-residue row
  (`TESTARCH/i5/2026-08-28 09:30Z`) in production on purpose, reported
  for a ruling rather than removed on the operator's initiative. It was
  deleted here under the same guarded-transaction discipline as RULING 8
  (count before = 1, `ROW_COUNT` = 1, post-condition check inside the
  transaction, total 4,755,478 → 4,755,477). A scan for `%TEST%`,
  `%SMOKE%` and `%FORDATE%` tickers found nothing else.

- **The PK drop/re-add is the migration's own collision test.** The
  alternative — building a shadow table and swapping it — is faster on
  paper and loses the property that matters: `ADD PRIMARY KEY` failing
  inside the transaction would have rolled the whole thing back and told
  us *why*. It passed in 15.9 s on 4.75M rows.

- **`Bar.ts` became `AwareDatetime` rather than staying `datetime` with
  a convention.** The defect was a naive value crossing a boundary
  nobody was watching. A comment saying "always pass UTC" would have
  been true and would have failed again; a type that rejects naive
  values cannot.

- **`_parse_finviz_datetime` still returns one value, not a (value,
  zone) pair.** Callers get a tz-aware UTC instant. The ET wall clock is
  recoverable from it exactly, so nothing is lost, and there is one
  representation in the model and one in the column — the alternative
  invites a second convention to drift from the first.

- **The `session_clock` is the consumer this unblocks.**
  `cobalt.session.SessionClock.session()` refuses a naive datetime with
  a message that names this ADR. That is not decoration: the resolver is
  the first thing that will join against `bars`, and the refusal is what
  stops the same class of error entering through a different door.

## Alternatives rejected

- **`ts = ts + interval '4 hours'`.** Correct for EDT, silently wrong by
  an hour for every EST row (roughly a third of the corpus). Rejected on
  the veto, and it is the right veto.

- **Change the column to `TIMESTAMP` (no zone) and store ET.** Honest
  about what was there, and it makes every future join carry the zone
  question in the application instead of the database. It also breaks
  the moment a second data source arrives with a real offset — which is
  the direction the roadmap goes (TV webhook, Massive). One
  representation, UTC, in the column.

- **Set the Postgres session `TimeZone` to `America/New_York` and leave
  the data.** Makes the existing rows *read* correctly and every future
  row wrong in a new way, and it makes the answer depend on which client
  connects with which setting. The bug was a value that meant different
  things to different readers; this entrenches it.

- **Fix the collector and leave the corpus.** Would produce a table with
  three weeks of UTC on top of a year of ET, distinguishable only by
  date. Strictly worse than either doing it or not doing it.

- **Defer to the Data-Model + Vault design session.** That session is
  what the open item pointed at, and the item's own wording — "before any
  join" — is why it lands here instead: S1 delivers the session clock,
  and S2 joins bars. Waiting means designing the radar on top of a table
  known to be wrong.

## Follow-ups (not done here)

- **`bars` still has no `session` column.** F1 stamps `aset_sizings` and
  `vault_writes`; bars are market data, not Cobalt writes, and their
  session is derivable from `ts` through the same resolver. Revisit when
  S2's radar makes the derived cost real.
- **The NYSE calendar covers 2026 only.** `bars` starts 2025-08-08, so
  `session()` on the 2025 portion of the corpus raises `CalendarError`
  until `nyse-2025.yaml` is added. That is deliberate fail-loud
  behaviour, and it is a config file, not code.
- **The production vault still has no backup.** Unchanged, and still the
  largest open risk in the incident report.
