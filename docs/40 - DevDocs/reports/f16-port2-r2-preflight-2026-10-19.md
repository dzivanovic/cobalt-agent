# Preflight R2 — card 790 `f16-close-fr2` (prompt 862), 2026-10-19

Read-only. Card `prompts/2026-10-18/790-f16-close-card.md`. The amend is COMMITTED (`5031a022`, "card 790 amended (X6 count)"), not uncommitted. main HEAD at the run: `5031a022`. Round 1 (`reports/f16-port2-preflight-2026-10-19.md`, 23 checks): everything not re-run below is carried as passed.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log --oneline -3 -- <card>` | `5031a022` amend, `3cfb077d` re-head, `ef60f42f` | OK |
| 2 | `git diff HEAD -- <card>` | empty (card committed and clean) | OK |
| 3 | `git diff --stat 3cfb077d 5031a022 -- <card>` and `--word-diff=porcelain -U0` | 7 ins, 7 del, 7 hunks, all in the three allowed edits: (1) `94`→`100` at the C1 control, X6 and the RECORDS loaders line (two numbers); (2) `:1084/:1096`→`:1148/:1160` (scope text, F4 RECORDS line), `cli.py:146`→`cli.py:150`; (3) the old PORT row gains `(context only, superseded by PORT2)`. No other edit. BASE, header, X1–X7, P-asks untouched. | OK |
| 8e | `grep -n load_tunables src/cobalt/cli.py` | `150` import (and `250`); card now says `cli.py:150` | OK (was FAIL) |
| 8f | `grep -n "key: prefill.refresh_" tunables.yaml` | `1148` window, `1160` interval_min; card now `:1148`, `:1160` | OK (was FAIL) |
| 8g | `grep -c "^  - key:"` and `grep -c "^    consumers:"` on `tunables.yaml` | `100` and `100`; card now says `100` at the C1 control, X6, RECORDS | OK (was FAIL) |
| 4 | `grep -n -E "\b94\b\|1084\|1096\|cli\.py:146\|«FILL"` on the card | no match | OK |
| N2 | NOTE 2: old PORT row (line 26) | reads `BASE = main HEAD at launch (header: 6452f70e) (context only, superseded by PORT2).` | OK |
| 5 | `git rev-parse --short=8 main` | `5031a022`; the card's BASE is still `cb4e42ce` (docs-only commits behind; the desk refills it at the launch, not a fail) | OK |
| — | Other cites on lines the amend touched (lines 17, 23, 26, 65, 77, 80, 82): `tunables.py:103`, `loader.py:76-85`, `jobs.yaml`, `daily.py` cites unchanged by the amend | carried from round 1 (8c, 8d passed) | OK |
| — | Round 1 checks 1–10 and 8a–8d, 8h–8l not touched by the amend | carried as passed | OK |

## ISSUES
- None blocking. Round 1's one blocker (X6 count `94` vs `100`) is fixed, and so are the stale cites and NOTE 2.
- NOTE: BASE `cb4e42ce` trails main (`5031a022`) by docs-only commits; the desk sets BASE to main HEAD at the launch so P5 holds.
- NOTE: no `RESTARTS:`/`CLASS:` header line (unchanged since round 1; RESTARTS is in `## RECORDS`).

PREFLIGHT DONE · card: f16-close-fr2 · checks: 11 · fails: 0 · ready: YES
