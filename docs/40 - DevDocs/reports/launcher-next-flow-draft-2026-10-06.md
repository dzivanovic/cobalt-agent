# launcher-next-flow card draft · 2026-10-06

## §0 Headline
- Card `prompts/2026-10-06/63-launcher-next-flow-card.md`: rows N6 (fix report read from the branch), N7 (recut fits 300), N8 (deploy card carries `--tickers`).
- Only `«FILL` is BASE. Every `file:line` read at main HEAD `3053fb9c`.
- N8 adds one optional argument, `deploy-card.sh --tickers`, and one `CARD.md` row; the hub gets one phrase on `DEPLOY-HUB.md:101`. No other new command.
- `jobs restarts` not run (`uv` is not on this seat's line); class homes proven from `restarts.py`, the build quotes the table.

## CARD
- JOB: launcher-next-flow · LADDER: OFF-LADDER — reports/next-flow-answer-2026-10-05.md 2026-10-05 R438
- BRANCH: ops/launcher-next-flow-1006 · WORKTREE: launcher-next-flow-1006 · BASE: «FILL: main HEAD at launch, 8 hex» · TIP, CHECK REPORT, HOUSE B: empty · DB: none
- REPORT: /Users/cobalt/cobalt-wt/launcher-next-flow-1006/docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md · RULINGS: 2026-10-05 R438
- RESTARTS homes: `ops/desk/*` operator script (`restarts.py:230`); `tests/ops/*` test/documentation (`:245-246`); `docs/…` DOCS (`:225-228`).

## DECISIONS
1. READ-ONLY, for the brain: does `deploy-card.sh` write a fix-round row? NO: it writes one row per job card, `ops/desk/deploy-card.sh:141`, whose 7th (`fix report`) cell is always empty; no line reads a fix report. A carried-defect row? NO: `grep -n -i -E "carried|defect"` on the script finds nothing. Nothing is built for either.
2. ASK DESK: where does the desk get the tickers it passes to `deploy-card.sh --tickers`? Default: from each build report's `stray rows: none (<tickers>)` line (`BUILD-HUB.md:87`), typed by the desk; no new job-card key. [before the build launches]
3. ASK DESK: N7 keeps what of the line's middle? His words give head through the first ` — ` and tail from ` · rollback:`. Default: the head, then as much of the middle as fits, `…`, then the tail (the test asserts only ≤300, head, tail, `…`). [before the build launches]
4. ASK DESK: `DEPLOY-HUB.md` P2 fix-round line still says the fix report is `committed and unmodified`, the scripts stop requiring it on `main`. Default: leave the hub line (fence: no hub change but `:101`); the desk rules a later hub row if it wants the wording changed. [before the deploy]

## RECORDS
- Read whole: `reports/next-flow-answer-2026-10-05.md`; `prompts/2026-10-02/21-launcher-checks-card.md`; `CARD.md`; `ops/desk/card-fill.sh`; `ops/desk/deploy-card.sh` `:1-219`.
- `ops/desk/desk-launch.sh`: `:785-872` (`ships_checked`: `:806` cell, `:841-857` `fixed_ok` with `:847` `-f`, `:848-850` log/diff, `:851` ancestor, `:852` last line, `:853-856` `BUILT ·`, `:858-859` refusal); `:1054-1127` (`recut`: `:1106-1108` the 300 test); 1197 lines.
- `ops/desk/deploy-step0.sh` `:328-412` (`:335` head, `:338` cell, `:379-384` tip test, `:387-405` fix round, `:389` `-f`, `:393-397` committed test); `rel` at `:129`; 526 lines.
- `grep -n -i tickers ops/desk`: only `gate.sh:2,19,72,84,97-112,160-163,187,463-476`; none in `deploy-card.sh`, `card-fill.sh`, `desk-launch.sh`. `CARD.md`: no `tickers`. `DEPLOY-HUB.md:101`: `the set's … --tickers … as the card gives them` (`grep -c -F` of that phrase → 1). `BUILD-HUB.md:79,87`.
- `ops/desk/desk-row.sh:52` `size(row) > 300` (`:40` `len`).
- Tests: `tests/ops/test_desk_launch_prechecks.py:556-572,580-644`; `tests/ops/test_deploy_step0.py:546-567,573-648`; `tests/ops/test_desk_launch_recut.py:38,60-226`; `tests/ops/test_deploy_card.py:113-207`; `tests/ops/test_gate.py:468-474` (tickers). No test pins `DEPLOY-HUB.md:101`.
- Evidence of N6: `reports/cto-2026-10-06.md:19` R553, `:115` R554; `reports/deploy-deploy-drc-d5-o1-b2-1006.md:75,95,105`.
- `src/cobalt/jobs/restarts.py:38,225-228,230,245-246`; `src/cobalt/jobs/cli.py:194-196` (`jobs restarts <git_range>`). Not run: no `uv` on this seat's allow line.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3053fb9c`.

LAUNCHER NEXT-FLOW CARD DRAFTED · decisions: 3
