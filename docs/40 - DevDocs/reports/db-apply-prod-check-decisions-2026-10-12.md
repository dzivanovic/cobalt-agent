# Card 417 check — brain decisions and the deploy order, 2026-10-12

On `reports/db-apply-prod-check-2026-10-12.md` `## DECISIONS` (ready YES, tip `fba1454e`).

| # | Ruling | Reason |
|---|---|---|
| 1 | KEEP | The staging count excludes docs; harmless. |
| 2 | KEEP | Comparing the apply file against HEAD is stricter than the row. |
| 3 | KEEP | A NUL-byte refusal before the parse only refuses more; the parse tree stays the fence. |

## DEPLOY ORDER (the queue the desk holds for the brain's word)
417 restarts aset. The 10-10 plan row holds every aset-restarting deploy until the aset orphan recut 256 lands (the old start script orphans python at bootout; deploy `fd33fb60` failed at 4.2). One at a time:
1. 284 (`--kill`, deploy card 356)
2. 256 (the aset orphan recut)
3. 417
4. 304 (F4)

The results sitting (hub 427) needs no deploy: launch it once its preflight passes, not after 417 (R1138 part 3).

## FOR THE CHECK
`417 check 2026-10-12 brain: D1-D3 KEEP; deploy queue in order 284, 256, 417 (restarts aset, so after 256), 304; results sitting not tied to 417`
