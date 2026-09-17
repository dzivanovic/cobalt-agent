# `src/cobalt/cards/picks.py`

F3 (S2-P4 ruling R2): a **pick** is any card reaching FILLED — manual now,
radar later. At that moment Cobalt records his pick next to Cobalt's own
rank for the name, so the DRC can later show "his pick and Cobalt's rank
for every card". This module owns the row; DRC rendering lands in S3.

## Where it runs
`CardStore.fill()` calls `record_pick(conn, card_id, transition_id, now)`
after the FILLED hop, **inside the fill's one USER transaction**, wrapped in
`SAVEPOINT pick` (`PICK_SAVEPOINT`). `record_pick` opens no connection,
switches no role and never commits. Any exception rolls back to the
savepoint only: the fill still commits, `FillResult.pick_recorded` is
False, and the gap shows up as MISSING in `cobalt cards picks`. See
`cards/store.md` for the transaction shape.

`record_pick` refuses (raises `PickError`) if the card row is absent or the
transition id is not that card's FILLED hop — a pick is never attached to
the wrong ledger row.

## What the row snapshots, at pick time
**Pool** (`pool_snapshot`). It reads, schema-qualified on the USER
connection (ADR-0008 allows qualified cross-side reads):
- `system.radar_pool` for the configured `radar.yaml` `pool_key`:
  `members`, `last_scan_id`, `last_scan_at`, `degraded`, `failed_stage`.
- `system.radar_membership`: the admitted episode open at `now`
  (`entered_at <= now AND (left_at IS NULL OR left_at > now)`). Its
  `last_rank`, `rank_metric` and `rank_value` are copied.

`pool_basis` names why a pool field may be null:

| `pool_basis` | Meaning | `not_in_pool` |
|---|---|---|
| `pool` | pool readable | true only when no open episode for the ticker |
| `unavailable: pool row missing` | no `radar_pool` row | true |
| `unavailable: pool failed_stage=<stage>` | last scan failed a stage | true |
| `unavailable: pool degraded (<sources>)` | pool flagged degraded | true |

The table CHECK `not_in_pool = (pool_member_id IS NULL)` keeps the flag and
the link consistent. A degraded or failed pool never refuses the fill.

**Card score** (`score_snapshot`). It is read only if S2-P2's
`aset_sizings.card_score` and `conviction` columns exist (checked in
`information_schema`, so no code change is needed when P2 merges).

| `score_basis` | When |
|---|---|
| `unavailable: S2-P2 not merged` | no `card_score` column |
| `unavailable: S2-P2 conviction column absent` | `card_score` without `conviction` |
| `unavailable: no taps` | `conviction` is NULL |
| `unavailable: card_score suppressed` | conviction present, score NULL |
| `card_score` | ranked |

The **cohort** is open radar cards (`COHORT_STATES` = WATCH/ARMED/TRIGGERED)
with a non-null score, **plus the picked card itself**. After the FILLED hop
it is no longer open, and it would otherwise drop out of its own ranking
(Astra R1-6). `rank_in_cohort` uses competition ranking (`TIE_POLICY`):
rank = 1 + the number of cohort cards with a strictly higher score, and ties
share a rank. `focus_top4 = rank <= FOCUS_TOP_N` (4). `score_inputs` (JSONB)
stores the ordered cohort, tie policy, cohort states and conviction, so the
rank replays from stored inputs (L57).

## Models
All Pydantic, `extra="forbid"`: `CohortEntry`, `PoolSnapshot`,
`ScoreSnapshot` (validates that a rank exists exactly when the basis is
`card_score`, and that any other basis starts `unavailable: `), `PickRow`
(validated before INSERT), `PickReportRow` (one FILLED transition
left-joined to its pick).

## `cobalt cards picks` report
`render_picks_report(rows, day=, cutoff=)` returns `(text, missing)`. Rows
come from `CardStore.filled_with_picks(day)`: every FILLED **transition**
on that ET day (Astra R1-7). Rows are not selected by current state, card
date or `filled_at`, so a card that later CLOSED still shows. A transition
with no pick prints `MISSING` and counts toward exit 1. With `cutoff` (the
P4 deploy instant, smoke check K6), an earlier gap prints
`MISSING (before cutoff)` and does not count.

## Public names
`COHORT_STATES` · `CohortEntry` · `FOCUS_TOP_N` · `PICK_SAVEPOINT` ·
`PickError` · `PickReportRow` · `PickRow` · `PoolSnapshot` · `ScoreSnapshot` ·
`TIE_POLICY` · `configured_pool_key` · `pool_snapshot` · `rank_in_cohort` ·
`record_pick` · `render_picks_report` · `score_snapshot`

## Tests
`tests/cobalt/test_cards_picks.py`: offline (typed result, ties, report and
exit codes, the transaction shape on every fill route, savepoint failure
paths) and `requires_db` on cobalt_dev (the fill → pick path end to end,
hub-run).
