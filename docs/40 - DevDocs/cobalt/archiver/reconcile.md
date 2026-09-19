# `src/cobalt/archiver/reconcile.py`

New 2026-09-19 with the append-only redesign (chunk R). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §3 (V2-3),
§4, §6, §7.

## What it does
Every DECISION of the append-only night, as pure functions: which bars
are eligible, which of them are candidates, how storage and the download
compare, and what the target's outcome is. It performs no I/O, reads no
clock (the fetch instant is an argument) and touches no database, so the
whole design is testable exactly and offline — which is what made 66
tests possible before a single row was written.

Purity is asserted on the AST, not on prose: the module may only import
`datetime`, `decimal`, `enum`, `typing`, `zoneinfo`, `pydantic` and its
own `models`, and may not call `now()`, `open()`, `execute()` and the
like. The module docstring names `BarStore` while explaining why
`max(ts)` is the wrong watermark; that is prose, and the test knows the
difference.

## Why a separate watermark exists at all
`BarStore.watermark()` is `max(ts)` over `system.bars`, and the RADAR
POLLER writes that table too — every 100 s, i1, with a five-bar overlap
(`radar/poller.py:96-105`). The poller keeps only bars newer than
(its watermark − overlap), so a bar that was ABSENT at poll time and
appears LATER — a vendor restoration, a late print — is dropped by the
poller while `max(ts)` moves on without it.

Three houses produced the same sequence independently in round 2, and
all three are dated tests in `tests/cobalt/test_archiver_reconcile.py`:
Gemini's Monday 14:00–14:05 restoration seen Tuesday, Astra's Friday
10:02 addition seen Monday, Grok's NVDA Wednesday 10:17 seen Thursday.
The same fact defeats a `max(ts)` gap test (MSFT 08-27/09-04; AAPL
re-added), which is a fourth test. `poller_watermark` is therefore
carried on the result and used by NOTHING — a test asserts that three
different poller watermarks produce byte-identical decisions.

## Key functions/classes
- `INTERVAL_MINUTES` / `interval_duration(interval)` — the explicit
  i1/i2/i5/i15/i30 map. Anything else raises `ReconcileError`; there is
  no "assume one minute".
- `bar_closes_at(ts, interval)` — `ts` is the bar's OPEN.
- `is_complete(ts, interval, fetch_started_at)` — V2-3: eligible only
  when the bar has CLOSED at or before the instant captured BEFORE the
  request. A naive datetime is refused (ADR-0007).
- `et_date(ts)` — the America/New_York calendar date.
- `normalise_price` / `normalise_volume` / `bar_values` /
  `values_from_row` — to `NUMERIC(14,4)` and integer volume, the
  column's own shape. Equality is decided on these, so `100.0` and
  `100.0000` are the same bar rather than a restatement that withholds a
  target for a whole night.
- `split_export(bars, interval, fetch_started_at) -> Eligibility` —
  duplicates first, then completeness; bounds taken over ELIGIBLE bars
  only, with the raw bounds kept as diagnostics.
- `steady_state_dates(bars, fetch_started_at)` — range (b): the current
  ET day plus the two most recent COMPLETED session DATES the export
  carries.
- `plan_candidates(...) -> CandidatePlan` — §4's candidate range: the
  UNION of `ts > archived_through` and range (b). No progress row is a
  BOOTSTRAP (the whole eligible export). `.refusal` decides
  `empty_export` / `regression` BEFORE any read, so a failed target
  costs no query.
- `compare(candidates, stored) -> Comparison` — the four ways a key can
  land: equal, differing (field-level, with both values), incoming-only,
  stored-only.
- `TargetCounts` — §7's counters, whose identities live in a
  `model_validator`.
- `reconcile(plan, stored, *, poller_watermark=None) -> TargetPlan` —
  the whole of §6 and §7 for one target, as one function (L3).

## Data flow in/out
**In:** the parsed export (`list[Bar]`), the fetch instant, the target's
`archived_through`, and what the database holds over the candidate range
(`{ts: BarValues}`).
**Out:** a `CandidatePlan` (what to read) and a `TargetPlan` (what to
write): status, reason, the bars to offer, the incidents to persist, and
the new watermark — or `archived_through_after = None`, which is how a
frozen watermark is expressed.

## The decisions, in the order `reconcile` takes them
1. **`empty_export`** — no eligible complete bar (no rows, or rows that
   have not closed). FAILED, progress unchanged, and the next non-empty
   night still bootstraps.
2. **`regression`** — `export_newest < archived_through`, STRICTLY.
   FAILED, progress unchanged. EQUAL is fine: an illiquid name whose
   newest bar has not moved succeeds with zero inserts three nights
   running, and a half-day's 12:55 bar is NEWER than the previous
   night's 19:59 — both are tests, both answer Grok's round-3 dissent.
   Only an ACCEPTED export ever updates the baseline, so a failed
   night's observation is never compared against (the IMCC case).
3. **`gap`** — progress exists and `export_oldest > archived_through`.
   The incident is drafted BEFORE progress advances, worded
   "unavailable from the tested export interface", with
   suspected-unavailable distinguished from proven-missing. The usable
   range is still appended and the target is DEGRADED.
4. **`stored_only`** — keys in storage the download does not carry.
   FLAGGED, nothing deleted, DEGRADED.
5. **`restated`** — ANY OHLCV difference after normalisation. NO insert
   for the target tonight, stored rows untouched, progress unchanged,
   FAILED. **There is no automatic repair, by constant factor or
   otherwise**: a whole-export constant-factor difference — the
   split-like case — is still a withholding, and that is its own test.

`inserted = 0` because everything was already stored is SUCCESS.

## Gotchas
- **Range (b) is not a convenience, it is the mechanism.** An illiquid
  target whose progress already covers the newest bar is still
  re-compared over the last two sessions — that is what catches a vendor
  restatement at all.
- **A weekend, a holiday and a half day need no special case**, and this
  module needs no calendar: sessions are DATES PRESENT IN THE EXPORT, so
  a weekend simply has no date and a half day has one that ends early.
  Thanksgiving Thursday + Friday, the 09-07 → 09-08 holiday, and both
  DST transition dates are tests.
- **`late` vs `new`.** `late` is an incoming-only key at or below the
  PREVIOUS `archived_through`; on a bootstrap `late` is 0 by
  definition. Astra's round-3 objection was that the counters called
  ordinary new bars late — MSFT 19:59 after 19:58 is `new`, and that is
  a test.
- **`stored_only` is reported BESIDE the identities**, never inside
  them: its keys are not candidates and folding it in would make the
  arithmetic lie.
- **`invalid` is 0 by construction** while the collector fails a whole
  target on one bad row (`collector.py:146-170`). The counter exists so
  §7's identity survives a collector that one day returns partials.
- **A non-reconciling count cannot be constructed.** `TargetCounts`
  raises on any broken identity, and `TargetPlan.counts()` is the only
  way to build one. A night that cannot explain itself raises rather
  than renders (L57, L1).
