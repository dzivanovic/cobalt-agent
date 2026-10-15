# Fix round on check card 603 — 2026-10-15

## §0 Headline
- Card `603-jev-shadow-check-card.md` edited in place: rows X0c, X0d, X0e, P0, R2 only.
- F1, F2, N1, N4 applied as carded; F3 applied as `ASK DESK` with the safe default.
- BASE, TIP, HOUSE B untouched. N2, N3, N5, N6: no change.
- Nothing run but reads; no git write.

## DECISIONS
- ASK DESK: X0e `uv run cobalt classify route-read` is off the check's allow line; default stands: a pytest-file driver calling `cmd_route_read` (`route.py:739`) covers the empty and the two-row ledger, else `REFUSED, not needed`. Add `uv run cobalt classify route-read *` to the allow line to run the CLI itself. [16:11 EDT]
- ASK DESK: X0d and X0e name a throwaway pytest file under `/Users/cobalt/cobalt-wt/jev-shadow-1015/scratch/`; whether a Write there is inside the check's allow line is not traceable from the preflight. Default: the check writes the file and records `REFUSED, not needed` if its Write is denied. [16:11 EDT]

## RECORDS
- `main` HEAD `0c3ef4a4`; tip `d0fdd674`, branch head `f298a7bf` (docs-only past the tip).
- Cites proved on `git show d0fdd674:src/cobalt/classify/route.py`: `cmd_route_read` `:739`, `load_route_config()` call `:740`, `routing_ledger` read `:744`, `--out-dir` `:764`, `route-read` parser `:762`, `_append` write `:473-476`. Cites of rows I did not touch were not re-proved.
- X0c: four fixed-string greps, one per call (`write_text`, `.open(`, `mkdir`, `.write(`).
- P0: classify tree `f4e8de85 d0fdd674`; `cli.py` and `cli.md` `d601b1f6 d0fdd674` (132 and 36 lines of main's drift named).
- R2: run from the worktree; main's `configs/cobalt/jobs.yaml` lacks the two `no_resident_reads` rows (preflight N4).
- X0d keeps `Router.body(router.qset, router.item(card))` at `route.py:703` and the five counts, now done in Python in the pytest driver instead of `grep -c`.

DRAFTED · decisions: 2
