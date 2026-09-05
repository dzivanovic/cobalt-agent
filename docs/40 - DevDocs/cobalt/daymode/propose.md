# `src/cobalt/daymode/propose.py`

## What it does
Stage 1's system rule (`stage1_mode`), the 09:00 proposal (`propose`),
the assembled reason (`build_reason`), and "what is in force right now"
(`decided_or_stage1`).

## The proposal rule
```
proposed = clamp( max(lowest_enabled, ceiling_after_step_downs) )
```
Start at the highest permitted rung; **step down once per adverse
signal**; clamp into `enabled_modes`. Every step-down names itself in
the reason, so the sentence is a *derivation*, not a summary.

| Signal | Effect |
|---|---|
| daily stop hit on the prior trading day | -> floor |
| `no prior DRC` | one rung down |
| today is an early close | one rung down |
| first session after a multi-day close | one rung down |
| `trade_count_band` still PLACEHOLDER | -> floor |

Signals **compound downwards** and never cancel: 2026-11-27 is both an
early close and the first session after Thanksgiving, so it steps down
twice.

## Status of this rule set — PROVISIONAL
The step-downs are deliberately crude, are marked as such in the reason
he reads, and belong to the **Rules Engine design session**; the whole
list is meant to be replaced wholesale rather than tuned.
`daymode.trade_count_band.{min,max}` ship as PLACEHOLDER tunables for
the same reason — and while unruled, the band is itself an adverse
signal that pins the proposal to the floor. Conservative in the only
direction it is safe to be wrong.

## At S1
With `enabled_modes: [reduced]` the clamp makes the proposal `reduced`
every time, and the reason says why. The ladder logic still runs in
full, and the tests exercise the higher rungs by enabling them in
config — which is the point of deriving the ladder rather than
hardcoding it.

## The reason string
Assembled from four **named** inputs: the prior trading day's FILLED
count and any daily-stop marker, the prior DRC, today's calendar, and
the band. Never an LLM — it is a derivation from counted rows and
config. A figure Cobalt cannot source is stated as absent
(`no prior DRC`, loud, and surfaced in the sheet banner), never filled
in.

## Undecided ≠ decided
`decided_or_stage1(row, cfg)` returns the stage-1 floor whenever
`decided` is NULL. A proposal is **not** a decision: an unanswered 09:00
question leaves the floor in place, which is the safe direction.

## Non-trading days
`propose()` returns `None` on a weekend or holiday — no proposal, no
row. Returning `None` rather than raising is deliberate: the launchd job
fires Mon–Fri and a holiday is not an error condition.
