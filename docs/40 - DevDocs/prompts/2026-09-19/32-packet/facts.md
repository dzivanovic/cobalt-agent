# 32-packet/facts.md — the hub's P4 CHECK C verdict rows that bind the round-2 fix chunk

Staged by the CTO desk 2026-09-19 from
`/Users/cobalt/cobalt-wt/agy-trial/scratch/review-p4-0919/REVIEW-C.md`
(the three-house check of `sprint-2/p4`, packet code tip `a59ee8c`).
**This file exists so the builder needs no `--add-dir /Users/cobalt/cobalt-wt`.**
Rows A1–A5 + the headline line are copied VERBATIM. Where your reading of the
code differs from a row, THE CODE WINS and the difference is an `## ESCALATE`
line — never a silent substitution.

## The hub's own headline, verbatim (REVIEW-C.md §0, line 5)

> Hub verification of Astra's 7 against the real files: **2 block shipping**
> (A1 empty formation rerun leaves stale current misses; A3 undeclared edit to
> the live ranking sort key, L52 — benign in effect, needs Dejan's word);
> **A4's BLOCKER framing is NOT REAL** (the committed cards fixture carries no
> `user_id`/reason fields; only cutter-vs-spec drift is real, MINOR); A2/A5
> real but overstated; A6/A7 real, already ESCALATE 3/13 and 2.

**THE TWO THAT BLOCK SHIPPING ARE A1 AND A3.** Not A2. Not A5.

## Verdict rows A1–A5, verbatim from REVIEW-C.md's `## Verdict table`

| # | Astra finding (filed sev.) | what I read | hub result | blocks the branch shipping? |
|---|---|---|---|---|
| A1 | `runner.py:414–418` empty formation rerun skips reconcile (BLOCKER) | `git show a59ee8c:src/cobalt/replay/runner.py` lines 425–430: `if rows and not dry_run:` guards `deps.missed.reconcile(..., kind="formation")`; `movers_step`/`cards_step` reconcile unconditionally. `reconcile` docstring (code-03:1662-1673) "retire every predecessor this run … drops". Plan STEP-1 R2-1 (spec-01:135): "A subject whose miss disappears entirely on rerun … is retired" and the test list names "a trigger disappearing after a bar correction". `code-10:856` even asserts `"missed.reconcile:formation" not in calls` when everything is suppressed. `formation_replay` returns `status=unavailable` with no rows when P2 is absent — the guard cannot tell that from "available, zero rows" | **REAL** (severity fair; only the P2-absent case justifies the skip). Line refs 414–418 are new-file lines of the diff, real file 425–430 | **yes** — a spec-ruled retirement (R2-1) is unimplemented for the formation kind and its own test asserts the opposite; small fix (reconcile when `outcome.status != unavailable`) + one runner test. Runtime risk is low (rerun-only, receipt table), so this is spec conformance, not prod safety |
| A2 | `runner.py:387–388…` deadline does not bound sync replay/DB work (BLOCKER) | `runner.py:286-304`: `check_deadline` runs only between steps and before the vault write; only `run_async` is under `wait_for`; `formation_source(...)` and `missed.reconcile(...)` are synchronous. Module docstring lines 26–31 states exactly this design: "a running step is cut at the deadline (async work under `wait_for`); the vault write is re-checked immediately before it lands, so no write is ever late". Spec R1-16 (spec-01:169) demands "an enforced execution deadline with cleanup and no late vault write, leaving a measured margin" — "no late vault write" is met; it does not require bounding sync DB commits | **REAL as a limitation, severity overstated** — behavior as described is true and self-documented; the spec's stated bar (late vault write, margin, refusal inside the margin) is met. Downgrade to MINOR/MAJOR design note | no — matches the plan's own R1-16 wording; the remaining exposure is one in-process day's replay + a USER-side commit, with `timeout_s: 1800` as the watchdog |
| A3 | `radar/pool.py:183–190` None-filtered ranking sort key (BLOCKER, L52) | `code-01:608-618`: the `union` sort key's `max(...)` generator gained `and source.metrics.get(name, {}).get(session_metric) is not None`; comment "used to raise TypeError here (found S2-P4 STEP-2)". The value expression a few lines above was already None-filtered (`code-01:600-604`) and plan F2/STEP-2 (spec-01:137) says the recorded value must be "the same expression as `pool.py:143-144`". Effect: `max()` over a mix of None/Decimal, or two Nones, raised; now it returns the filtered max or None — every input that ran before ranks identically. Not listed among rows 2/4/6/8 or in either build report (`grep -i "TypeError\|None-filtered\|_ranked"` on the reports, facts, specs: nothing) | **REAL** — an undisclosed edit inside `_ranked`'s sort key (L52's "nothing here may touch ranking"); behaviorally crash→no-crash only | **yes — by the letter of L52, pending Dejan's ruling.** Effect is benign and I would recommend disclose-and-rule, not revert; it is his law to waive, not mine or the desk's |
| A4 | `_cut_p4_fixtures.py` omits §3's personal-data transforms (BLOCKER) | Spec-01:249 does require `user_id` → 1 and free-text reasons → `"<reason>"` for `cards-day.real-shape.json`, and `code-13:158-159,182-185` `_anonymize` = hex-suffix scrub + date shift only (`grep user_id\|reason` in code-13: nothing). BUT the actual committed fixture, `git show a59ee8c:tests/fixtures/replay/cards-day.real-shape.json` (7,544 B, read by me, counts only): sizings keys `created_at, direction, entry, id, state, stop, ticker` (11 rows); transitions keys `at, card_id, from_state, to_state` (37 rows) — **no `user_id`, no reason/note field exists to leak.** The fixture is the file spec-01:249 itself commissions; its tickers/card ids are inherent to it, so the docstring adds narrative only | **BLOCKER framing NOT REAL** (no personal field reaches the committed fixture). **Residual MINOR is real:** the cutter does not implement two spec-listed transforms; it stays correct only because the raw reads happen to omit those columns | no — nothing personal shipped; a comment/transform-drift cleanup at leisure |
| A5 | `test_p4_migrations.py` "both merge orders" (BLOCKER) | `code-12:1219-1240`: `base = [p for p in FORWARD if _migration_version(p) < 8]` is applied in BOTH parametrizations; on the rebased tree `FORWARD` includes 0006/0007, so `_simulate_p2_card_columns` (`ADD COLUMN IF NOT EXISTS`) is a no-op in `p4_before_p2`. The module docstring (code-12:934-938) still says "P2's 0006/0007 are not in this tree" — stale after the rebase. `_seed_membership` runs only after the first `_apply([0008,0009])`, so first-apply preservation of pre-existing rows is not what the digest equality proves | **REAL** — a test-quality defect (mislabelled case + stale docstring), not a migration defect; Q5 by three houses found the SQL additive with guards | no — the order question is moot once P2 is on main and P4 rebased onto it; 0008 is `ADD COLUMN IF NOT EXISTS` nullable on the production table. Tighten the test before the next migration, not before this ship |

## Rows NOT assigned this round (stated so nothing is carried silently)

- **A6** mixed-session fixtures can false-pass F13 — REAL, already owned by build-report-2's ESCALATE 3 / ESCALATE 13; re-cutting membership needs a production DB read, which this OFFLINE chunk may not do. Not yours.
- **A7** K3 reads a permitted frozen HOLD as red — REAL, already ESCALATE 2; the desk owes a ruling before the deploy smoke. Not yours.
- **A8** build-report-2 wording ("16 fund tickers blank" vs 8 distinct tickers, `build-report-2:162` vs `:149`) — REAL, MINOR; the desk fixes it before the memory fold. Not yours.
- **A9 / A10** — carried by reference / UNVERIFIABLE FROM READS. Not yours.

## The hub's own desk-decision line, verbatim (REVIEW-C.md line 80)

> **Desk decisions (not mine, L37):** (1) A1: fix before ship or rule it out;
> (2) A3: Dejan's ruling on the None-filter (L52); (3) A5 and A4-residual:
> fix-later items; (4) the packet is at `a59ee8c` but `sprint-2/p4` is at
> `c40f03c` — A1/A3 live in files the R16 retry commits may not have touched,
> but a re-check on the new tip is the desk's call.

The desk HAS made that call: this chunk runs on the current tip, and step 1 of
every item re-reads the live file before quoting a row.

## Desk's pre-read of A3, for the builder to CHECK, not to trust

The desk read `src/cobalt/radar/pool.py` on the current tip and
`git diff main -- src/cobalt/radar/pool.py`. Its finding, which your step 3 must
independently confirm or contradict:

- The `union` sort key (`pool.py:179-205`) is a 3-tuple:
  `(max(<filtered gen>, default=None) is None, -(max(<filtered gen>, default=0)), name)`.
  BOTH `max(...)` calls carry the new `is not None` filter (`pool.py:189`, `pool.py:198`).
- Pre-edit, element 2 was `-(max(<unfiltered gen>, default=0))`. Any generator
  containing a `None` raised `TypeError` there — including the single-`None` case
  that element 1 survives. So **every input that did not raise had an all-non-None
  or empty generator**, for which the filtered and unfiltered `max` are the same
  value, and the whole key tuple is identical.
- `union` is consumed at `pool.py:206` only as `position = union.index(ticker) + 1`,
  one component of `key`; the `candidates` set itself is never filtered by it.

If that holds on your read: **the edit changes no ranking and no pool membership;
it converts a crash into a defined placement.** L52 then still owns the
*disclosure*, which is Dejan's to rule — so step 3 writes a PINNING TEST ONLY and
touches not one line of `pool.py`.
