## §0 Headline
Card 790 amended in place for preflight FAIL 26 and NOTES 1, 2, 3; nothing else touched, nothing committed.
- FAIL 26: `## RECORDS` now names the RESTARTS class home of `cli.py` and `loader.py` (static import reach to `com.cobalt.radar`, `jobs.yaml:203`).
- NOTE 1: V1/V2 insertion point is `cli.py:334`, before CROSS-CHECK 1 (`:335`), not inside `if disabled:` (`:328`).
- NOTE 2: RULINGS set to `none` (no row of his binds F16 close). NOTE 3: pytest counts removed.

## DECISIONS
- ASK DESK: RULINGS `none` is my reading of the search (only desk records mention F16 in the `cto-2026-10-*.md` reports; the ladder rows are scope). If the brain holds a ruling that binds F16 close and is not in those files, name it. [19:55 EDT] Default: `none`.

## RECORDS
- 2026-10-18 19:55 EDT from `date`. Card: `prompts/2026-10-18/790-f16-close-card.md`. Preflight: `reports/f16-close-preflight-2026-10-18.md`.
- Proved against main: `git diff --stat main -- src/cobalt/cli.py src/cobalt/taxonomy/loader.py configs/cobalt/jobs.yaml` is empty. `jobs.yaml:193` radar row, `:203` `imports: [cobalt.cli]`; `cli.py:146` imports `load_tunables`; `loader.py:76` `load_tunables`; `cli.py:318` Jobs (F17), `:328` `if disabled:`, `:330-333` NOT LOADED BY DESIGN lines, `:335` CROSS-CHECK 1.
- Card 790 changes: header `RULINGS: none`; row V1 insertion text; row C1 red-first cell (counts dropped, test names and reasons kept, `0 failed`, `0 errors` named as the hub gate); three `## RECORDS` lines (RESTARTS, RULINGS, insertion point), replacing the old RESTARTS line.
- Card 730's `RESTARTS:` header line (`:13`) is the form followed; its RECORDS did not carry a separate class-home line I could quote, so I used the preflight's own wording.
- Not done: no second preflight, no commit, no launch (L36). Note that the pytest counts removal also left NOTE 4 (red/green derived by reading) for the check to run.

DRAFTED · decisions: 1
