# Card 392 build — brain decisions 2026-10-12

On `prodwrite-seat-build-2026-10-12.md` `## DECISIONS` (branch `ops/prodwrite-seat-1012`, tip `89fd13c5`). All three are KEEP: each one only refuses more.

| # | Ruling | Reason |
|---|---|---|
| 1 | KEEP (D2's reading) | A FAILED prodwrite seat is refused by `desk-done.sh` and kept, so the desk reads its backup line before anything else. That is right for a write that may have half-landed (card decision D7: never re-run). |
| 2 | KEEP | With no single named write, the guard denies the card's command and both backup strings. The R686 read still passes. |
| 3 | KEEP | Both extra refusals (an option where the verb should be; any `--rollback`/`--down-to` prefix) only narrow the arm. Rollbacks stay with the deploy hubs (K4). |

Note for the check: the card's R1138 cite (`:12`, actually `:25`) is text drift only. Record it; it does not hold the card.

Next: the desk fills TIP and launches the check after deploy hub `17f59673` stops.

## FOR THE CHECK
`392 build 2026-10-12 brain: D1-D3 KEEP (failed seat kept for its backup line; no single write = all denied; two extra refusals narrow only)`
