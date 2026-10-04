# DRC D5 — judge answers on the re-read's D5-a to D5-d (2026-10-04)

Source: `reports/s3-reread-draft-2026-10-04.md` `## DECISIONS`; card `prompts/2026-10-04/03-drc-d5-card.md`; design `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md`; his R90 (09-22). All four KEEP; no card text changes. Two follow-up rows.

| item | answer | reason |
|---|---|---|
| D5-a no-legs (pre-C1) card | KEEP the default | `insert_entry_leg` cannot carry an import id and `0021` refuses `trading_log` without one; `cards/legs.py` is fenced. `running_shares` already has the pre-C1 bases (`recomputed_shares`, `shares`), so exits and corrections still land and running equals the export. The unit line names the gap, so nothing is silent. The set of pre-C1 cards still open only shrinks. FOLLOW-UP 1 |
| D5-b exit time vs the `market_reset` gate | KEEP the default | `now` stays the build's clock, so the gate is never sidestepped; the export's time arrives as a correction through the same writer, which is append-only history (R67, L57: source `trading_log` plus the import id on both rows). A second build of the same day finds no diff and writes nothing |
| D5-c Cobalt leg with no DAS execution | KEEP the default | no writer removes a leg (`record_correction` refuses `shares <= 0`). R90 replaced "the build FAILs" with "built, with an unresolved line carried". This is the same shape: stored, rendered, carried. FOLLOW-UP 2 |
| D5-d which builds write `legs` | KEEP the default | only the event day's `check=True` build writes, and only for a trade without `inputs.carried_from`. A re-paired date or K3-8's notes rebuild must never write `legs` twice, and a carried trade's legs span days that one day-file cannot see. Both render `adjustment not written — <carried trade \| re-paired date>`, never a silent skip. FOLLOW-UP 1 covers the carried case |

FOLLOW-UP ROWS (direction TOMORROW table; not D5's job):
1. Carried and pre-C1 reconcile. A swing card (carried across days) and a pre-C1 card are never adjusted to DAS by D5. Needed later: a reconcile across the trade's day-file chain, and an import id on the entry leg (a `cards/legs.py` + `0021` change: product code, its own card, a migration).
2. Clearing a phantom Cobalt leg. An unresolved "Cobalt leg with no DAS execution" item has no clearing path except a later successful reconcile. Needed later: a void-correction kind in C2's writer (product code, a migration), or his word on another way to clear it.

FOR THE CHECK (D5): confirm that no `legs` write is reached from `plan_note`, a `--dry-run`, a re-paired date or K3-8's `rebuild_notes`; that each of the three not-written cases (pre-C1 entry leg, phantom leg, carried trade / re-paired date) renders its line; and that `now` passed to `record_exit` is the build's clock.
