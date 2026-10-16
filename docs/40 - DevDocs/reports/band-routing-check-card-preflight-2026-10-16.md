# Preflight — card 633 `band-routing-1015` (CHECK, K5) · 2026-10-16

Read only. Card: `prompts/2026-10-16/633-band-routing-check-card.md`. Tip read from `/Users/cobalt/cobalt-wt/band-routing-1015` (equal to head `115e1f37`; `git diff --stat bd9c24ac 115e1f37 -- . ":(exclude)docs"` prints nothing).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Header fields of `CARD.md` for a check (JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, RULINGS; DB optional) read from card lines 1-15 | all present. `TIP` (line 8) and `HOUSE B` (line 12) hold `«FILL: …»`: the desk's to write, named not failed. `BASE: f2ca3e1a`. `CHECK REPORT` is absolute under `reports/`. `DB: none`. `ls /Users/cobalt/cobalt-wt/band-routing-1015` lists the tree | OK |
| 2 | `grep -n -E "«FILL\|TODO\|TBD\|XXX\|<FILL"` over the card | two hits: `:8` (TIP) and `:12` (HOUSE B), both the desk's fields; no other placeholder token | OK |
| 3 | `git -C … rev-parse --short=8 ops/band-routing-1015` and `… bd9c24ac` | `115e1f37`, `bd9c24ac` (the card's head and tip) | OK |
| 4 | `git diff --name-only --no-renames f2ca3e1a bd9c24ac` (S0's list) | the 7 files S0 names, nothing else; all under `docs/`, `ops/`, `tests/ops/` (so `DB: none` holds) | OK |
| 5 | Rows cover build rows: card `## ROWS` ids | S0, B1, B2, B3, B4, B5, B6, A1-A4, R3, T1, G1; B1-B6 each a row with a mutation, a RED and controls named; R3 is the seventh | OK |
| 6 | `grep -c -F` of each `## FOR THE CHECK` clause in the card: `BUILT · job:` / `no seat removes` / `builds on Opus now` / `fix round: a fresh` | 2 / 1 / 2 / 1 (A1; A2; `## RECORDS`; `## NOT IN THIS JOB`). The `.result` and `shadow-shaped` clauses are rows B6/A3 and B5/A2. Each is a RUN with output quoted and its RED and control re-run | OK |
| 7 | The six build DECISIONS as asks | X8 (B6), X9 (B3-a), X10 (B3-b), X11 (B3-c), X12 (B3-d), X13 (B5); match build report `## DECISIONS` lines 184-189 | OK |
| 8 | Houses and Opus seat | `HOUSE A: grok` (line 11), `WHY` and X14 name both outside houses and the Opus check seat (brain condition 1); house B is the desk's fill | OK |
| 9 | `grep -c -F "L75"` over the card | 1: `Then ONE fix round by the builder, no re-check (L75)` in `WHY` | OK |
| 10 | `grep -n "deploy-gate" ops/desk/gate.sh` | `:2`, `:29`, `:99`, `:136`, `:147` (accepts `offline` and `all`), `:568`; card's G1 `gate.sh band-routing-1015 offline --deploy-gate` is valid | OK |
| 11 | RULINGS holds only `HIS RULING` and `APPROVED` rows | `RULINGS: 2026-10-15 R1532`; `grep -n "^\| R1532 " cto-2026-10-15.md` → `:102 … HIS RULING · APPROVED: routing B …` | OK |
| 12 | `file:line` sample, 14 anchors, against the tip's files: `desk-launch.sh` `:379` `routed=""`, `:393` `--routed)`, `:1642` `BAND_FROM`, `:1658`, `:1660`, `:1665-1666`, `:1668`, `:1682`, `:1683`, `:1715`, `:1720`, `:1737`, `:1792`, `:1814`; `preflight.sh` `:120`, `:159`, `:167`, `:169`; `bare-guard.py` `:1268`, `:1271`, `:1277-1281`; `CARD.md:23`, `:32`; `SHADOW-HUB.md:28`; `BUILD-HUB.md:12` | every one matches its content (Read of `desk-launch.sh:1640-1740` and greps) | OK |
| 13 | `grep -n -F ".result"` over `result-read.sh`, `deploy-card.sh`, `deploy-step0.sh`, `desk-launch.sh` (row A3) | `result-read.sh:5`, `deploy-card.sh:489`, `deploy-step0.sh:681`, `desk-launch.sh:1462`; all `${…%.md}.result` | OK |
| 14 | `grep -c -F "def test_"` of the test file; `grep -n -E "git show\|subprocess\|[0-9a-f]{8}"` | 24 defs (as the card's 36 cases); no `git show`; every hit is a `subprocess` line, no 8-hex hash | OK |
| 15 | DEPLOY PROOF before values on `main`: `grep -c -F "BAND"` of `CARD.md`; `grep -c -F "BAND_FROM"` of `desk-launch.sh` | `0`; `0` (card says before `0`) | OK |
| 16 | Card committed: `git status --short -- <card>`; `git diff HEAD --stat -- <card>`; `git log --oneline -2 -- <card>` | empty; empty; `38ac982d docs(desk): handover f2f973cd, check card 633 drafted, preflight prompt 634` | OK |

## ISSUES
- NOTE: what blocks the check launch: the desk must write `TIP: bd9c24ac` and `HOUSE B: as needed` (card `:8`, `:12`) and commit; `desk-launch.sh` refuses a `«FILL` in a field its kind needs. Nothing else blocks.
- NOTE: `LADDER` reads `OFF-LADDER — reports/cto-2026-10-15.md R1532`; `CARD.md:14` form is `OFF-LADDER — <report> <date> R<n>`; the date sits only in the file name. Same as the build card's line.
- NOTE: header lines `CLASS: K5` and `INSTALL: none` are not keys of the `CARD.md` check column; `desk-launch.sh` reads `CLASS` only for prodwrite (`:1873`), so both are ignored, harmless.
- NOTE: `HOUSE A: grok` is not a form `CHECK-HUB.md` names; the launcher's house loop (`desk-launch.sh:1066-1075`) skips a line with no `overruled`. Card 549 carries the same line.
- NOTE: the card's `WHY` and X14 say both houses run; `CHECK-HUB.md:25` seats house B only when `HOUSE B` begins `mandatory`. With `as needed` house B is `none (not needed)`. The desk's choice of `HOUSE B` decides it.
- NOTE: the build report cites `desk-launch.sh:1457` for the `.result` reader; the tip has it at `:1462`. The card does not cite the number.

PREFLIGHT DONE · card: band-routing-1015-check · checks: 16 · fails: 0 · ready: YES
