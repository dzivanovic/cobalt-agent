# radar-direction-color — preflight round 2 of card 89, after the amend (2026-10-07, read-only)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card header (unchanged by the amend, see check 3) | `BASE: «FILL: main HEAD at launch, 8 hex»` (the one fill token); `BRANCH ops/radar-direction-color-1007`, `WORKTREE radar-direction-color-1007`; `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `RULINGS: 2026-10-07 R625`; no `DB` key (rows are `src/` and `tests/cobalt/`) | OK |
| 2 | `grep -n R625 reports/cto-2026-10-07.md` | `:19 \| R625 \| 10:15 ET \| HIS RULING … a radar card's header row and title are green for long, red for short … \| HIS RULING · APPROVED \|` | OK |
| 3 | `git -C /Users/cobalt/cobalt diff 1667b512 HEAD -- <card>` | one hunk, one row: row C line, `-`/`+` pair only. Header, rows A, B, D, NOT IN THIS JOB, READ, CHECK ASKS and RECORDS are context or untouched: nothing but row C moved | OK |
| 4 | `git rev-parse --short=8 HEAD`; `git diff --stat f6d31607 HEAD -- src tests configs` | HEAD `4c6c4331`; no output: `src`/`tests`/`configs` equal the card's drafting HEAD, so every `file:line` of round 1 still holds | OK |
| 5 | Read `radar_panel.py:1422`–`:1424` | `<div class="card-title">…`; `:1423` `<span class="direction {card.direction}">{"↑" if card.direction == "long" else "↓"}</span>`; `:1424` `<span>{e(card.setup)} → {e(card.trade)}</span>{outside}</div>` | OK |
| 6 | Round 1 check 6 (`:1467`–`:1470`), valid by check 4 | strip is `class="strip"`, 4 children, ticker in `<b>` | OK |
| 7 | Round 1 check 7 (`:1496`–`:1501`), valid by check 4; `grep` of `radar_panel.py` just now | `.direction.long/.short`, `.dot.filled.colour-0` `#3a1119`, `.colour-2` `#0f2a1c`, `--green`, `--red`, phone rule `.strip span:nth-child(4){display:none}` at `:1499`: all exist, no new colour | OK |
| 8 | Round 1 check 8 (`:1481`, `:1402`–`:1403`, `:1559`, `:234`, `:381`, `:865`–`:867`, `:908`, `web.py:903`–`:909`), valid by check 4; `grep -n direction radar_panel.py` | `:234`, `:381` `Literal["long","short"]`; `:908` sign; `:1481` terminal row; as cited | OK |
| 9 | Round 1 check 9 (test file lines), valid by check 4 | `:189`, `:224`–`:240`, `:393`–`:397`, `:440`, `:472`, `:493`–`:508`, `:519` as cited | OK |
| 10 | `grep -n "dir-" src/cobalt/aset/radar_panel.py` | no output: `dir-` is absent on BASE, so the class, count and CSS tests are red on BASE | OK |
| 11 | Red on BASE, row A `…carry_the_direction_class_and_arrow` | BASE strip `class="strip"`, no arrow; title `class="card-title"` → red as stated | OK |
| 12 | Red on BASE, row A `…unknown_direction_is_marked_never_guessed` | BASE `:1423` renders `↓` for any non-long value, no `dir-unknown` → red as stated; `_field` `:1109` shows `—` for `None`, no crash | OK |
| 13 | Control green on BASE and after | `direction` `None`/`"sideways"` fails the `Literal` at `:865`–`:867` → `RadarPanelError: FAILED: invalid radar card row` | OK |
| 14 | Row B test red on BASE | four rules absent (`dir-` count 0); colour, `@media`, `:root` compares use BASE text | OK |
| 15 | Row C(1), `dir-` exactly twice per article | 0 on BASE (check 10); after the build the two sites are strip and title only; `why-line`, `semaphore`, `health-line`, WATCH block carry none | OK |
| 16 | Row C(2) amended identity: `expanded` minus title, minus (a) `LEVELS` 1R/2R, (b) CARD `data-field="direction"` span, (c) IN-TRADE `{direction}`. Read `:1105`–`:1111`, `:1340`–`:1341`, `:1358`, `:1422`–`:1424`, `:1433`, `:1435`; `grep -n direction radar_panel.py` | (a) `:1433` the two `<span class="field">1R/2R <b>…</b>` spans, from `:908` sign. (b) `:1435` `_field(card, "direction", "direction", card.direction)` → `<span class="field" data-field="direction">direction {badge} <b>long\|short</b></span>` (`:1111`–`:1112`). (c) `:1340`–`:1341` `<div class="running"><b>…</b> · {e(direction)} · …`, fed by `:1358` `direction=card.direction`. Every print of `direction` in `radar_panel.py` is `:234`, `:381`, `:908`, `:912`, `:1299`, `:1341`, `:1358`, `:1423`, `:1435`, `:1481`; `:1423` is the title (removed), `:1481` is the terminal row, outside `expanded`. So the three removals are complete: the amended control is true | OK |
| 17 | Row A mirrors precedent pins and tests | `mirrorStale` reads `.strip b` (`:1559`); the arrow goes in the 3rd span, so the `<b>` pins `:472`, `:519` hold; `.strip span:nth-child(4)` hides only the 4th span. Other test files read only `PANEL_CSS` substrings and degraded-line pins | OK |
| 18 | Rows match R625 and nothing else | R625: header row and title green for long, red for short. Card: strip and title tint, arrow on the strip, nothing in the card body. Row D is the restarts run only | OK |
| 19 | No new command | no new command, route, setting or migration; the one command is the existing `uv run cobalt jobs restarts <BASE>..HEAD` (R411, R412) | OK |
| 20 | RESTARTS class homes (round 1, `restarts.py:205`–`:253`, `jobs.yaml:90`, `:194`), valid by check 4 | `radar_panel.py` static import reach; test file no resident; build report DOCS; `com.cobalt.aset` and `com.cobalt.radar` by reach; all in the card's `## RECORDS` | OK |
| 21 | `RESTARTS:` line | no `RESTARTS:` header key (CARD.md defines none); `## RECORDS` bullet reads `expected com.cobalt.aset com.cobalt.radar`, the set of check 20 | OK |
| 22 | `git diff --stat HEAD -- card draft src tests` | no output: card and draft committed and clean | OK |

## ISSUES
- NOTE: round 1 FAIL (check 16) is fixed: the amended row C removes all three direction prints inside `expanded` (1R/2R, CARD field `:1435`, IN-TRADE `:1341`). The title's own `{card.direction}` is inside the removed title div.
- NOTE: the amend moved only row C (check 3). Rows A, B, D and the header were not re-read line by line: their cites hold because `src`/`tests`/`configs` are unchanged since `f6d31607` (check 4) and the card diff touches only row C.
- NOTE: for the build, the CARD field span holds a nested badge `<span>`, so the test should cut it by its `data-field="direction"` open tag through the closing `</span>` of the field, not the first `</span>`. A first-`</span>` cut leaves residue and the control fails.
- NOTE: `BASE` is still the one fill token for the desk. The `RESTARTS` set is read from code only; row D runs it.
- NOTE: the draft's decisions 1-3 are the desk's kept defaults and were not checked against.

PREFLIGHT DONE · card: radar-direction-color-89 · checks: 22 · fails: 0 · ready: YES
