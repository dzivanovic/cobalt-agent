# `src/cobalt/daymode/store.py`

## What it does
One `day_modes` row per trading day. Database from `COBALT_ENV`
(RULING 7/9).

## Schema
`trade_date` (PK) · `stage` · `proposed` · `reason` · `decided` ·
`decided_by` · `decided_at` · `overrule_reason` · `attested_sheet` ·
`attested_at` · `session` · `created_at`

The date is the primary key, so the 09:00 job is **idempotent by
construction**: a second run updates the proposal instead of stacking a
second one the sheet would have to choose between.

## What is NOT persisted
**Stage 1 has no row.** "The lowest enabled mode" is a system rule
computed from config; persisting it would store a constant and invite
someone to edit the stored copy instead of the config. A row appears
when the 09:00 job proposes, and `decided` stays NULL until he
answers — which is exactly the state the sheet reads as "still on the
stage-1 mode".

There is no row for a Sunday, a holiday, or any day before 09:00.

## Rules the store enforces
- **An overrule carries its reason.** Checked against what was actually
  *proposed*, re-read here rather than trusted from the caller — the
  sheet's hidden field is not the authority on what Cobalt said.
- **A re-run never un-answers a decision.** `upsert_proposal` replaces
  `proposed`/`reason` and leaves `decided` alone.
- A row created by an early attestation carries no proposal, and
  `decide()` refuses on it rather than treating `''` as a proposal.
- Every write goes through the F1 guard — refused in `market_reset`.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Declares `SIDE = Side.USER` (ADR-0008 D2 — the side is chosen PER STORE, never per process).
which sheet he is trading today, and what he decided.

`_connect()` passes it to the factory; `ensure_schema()` asserts the two-layer schemas exist before running its own DDL, naming `cobalt db migrate` if they do not.
