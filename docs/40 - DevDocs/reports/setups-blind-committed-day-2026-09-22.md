# SETUPS BLIND COMMITTED DAY — 2026-09-22

## §0 Headline
Blind re-derivation of the 17 committed-day `DEF_WRITTEN_*` pins from bars + neutral shapes + public rules alone. Gemini (`agy`) FAILED on a harness permission denial before writing anything; fell back to Opus 5 (same house as the builder, disclosed). Result: 17 of 17 fields UNDERIVABLE — the packet's excerpts correctly withhold the engine detectors (extension lifecycle, EMA/VWAP/ATR, leg roles, level set, RangeBreak) the four setups need, so this is L70-expected, not a defect. 2 house-raised packet-quality items (a daily/intraday bars contradiction; an ambiguous `stop.buffer` unit) plus a CRLF byte-identity gap on one fixture file, both disclosed below. HOLD 1 stays open — no value could be closed.

## AUTHORIZATION
- `grep -n "17-setups-blind-committed-day.md" cto-2026-09-22.md` → R15 row present, filled in (not `__`): "The desk launches `17-setups-blind-committed-day.md` ... HOLD 1's closure for the 17 EXISTING `DEF_WRITTEN_*` pins ..." — line 34.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"17-setups-blind-committed-day.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` → `6700f4562e4142f6a1bffb3d2625154800613b60` (non-empty). Launch row committed on main.
- `grep -n "^| R49 " cto-2026-09-21.md` → line 60, carries `claude -p --model claude-opus-5`. Confirmed.
- `grep -n "^| R39 " cto-2026-09-21.md` → line 50, `Bash(agy *)` "through 2026-09-22 23:59 ET".
- `grep -c -F -e "<rule>" 66-setups-one-check.md` for each of the nine allow strings, three deny strings, and the `--add-dir` triplet, each its own call:
  - `"Bash(agy *)"` → 2 · `"Bash(claude -p --model claude-opus-5 *)"` → 2 · `"Bash(git -C /Users/cobalt/cobalt show*)"` → 1 · `"Bash(git -C /Users/cobalt/cobalt log*)"` → 1 · `"Bash(ls *)"` → 1 · `"Bash(grep *)"` → 1 · `"Bash(tail *)"` → 1 · `"Bash(wc *)"` → 1 · `"Bash(date*)"` → 1
  - `"AskUserQuestion"` → 2 · `"EnterWorktree"` → 2 · `"Bash(git push*)"` → 1
  - `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt` (as one string) → 1
  - All ≥1. AUTHORIZATION PASSES.

## PREFLIGHT
| command | exit | result |
|---|---|---|
| `date` | 0 | Tue Sep 22 10:52:40 EDT 2026 — DATE GATE: `<D>` = 2026-09-22, within R39's Gemini/agy window (through 2026-09-22 23:59 ET) |
| `agy --version` | 0 | `1.2.8` |
| `claude -p --model claude-opus-5 "Reply with exactly the word OK"` (background, 3 min) | 0 | `OK` |
| STAGGER: `tail -n 1 float-handicap-tribunal-2026-09-21.md` | 0 | `FLOAT HANDICAP TRIBUNAL R1 DONE · ... · ESCALATE: 3` — starts with the required token, house lane free |
| `git -C /Users/cobalt/cobalt log --oneline -1 setups/seven-0921` | 0 | `60ddac4 docs(report): setups one build — BUILT dd4a9b9, 9 of 9 steps, offline 2419/0, with-DB 540/0, ESCALATE 32` |
| `git -C /Users/cobalt/cobalt log --oneline 60ddac4..setups/seven-0921 -- <pinned+staged paths>` | 0 | EMPTY — no drift since `60ddac4` |
| `ls /Users/cobalt/cobalt-wt/setups-c1/tests/fixtures/radar` | 0 | `bars-rubberband.real-shape.json`, `card-settings.real-shape.json`, `daily-bars.real-shape.csv` present (plus panel/pool fixtures not staged) |

THE HOUSE: PRIMARY = Gemini (`agy`), confirmed alive and within R39's window. FALLBACK (Opus 5) probed alive too but not needed — primary stands.

## Packet
Staged under `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-blind-committed/` by Read → Write, whitespace-gap check first.

| file | original path | lines | bytes original | bytes staged | parts |
|---|---|---|---|---|---|
| `bars-rubberband.real-shape.json` (5 parts) | `setups-c1/tests/fixtures/radar/bars-rubberband.real-shape.json` | 1-9202 | 183,837 | 183,837 (sum of 5 parts) | 5 (36,494 / 36,823 / 36,928 / 36,899 / 36,693 B; cut only after a `},` line, each ≤38,000 B) |
| `daily-bars.real-shape.csv` | `setups-c1/tests/fixtures/radar/daily-bars.real-shape.csv` | 1-76 | 3,406 | 3,330 | 1 — **KNOWN GAP:** original is CRLF (76 `\r` bytes, `grep -c $'\r'` = 76); the Write tool normalizes to LF and this text interface cannot emit a bare `\r`. Content (every field, every row) is otherwise byte-identical — confirmed by re-reading both. Not a data alteration; flagged, not silently passed. |
| `card-settings.real-shape.json` | `setups-c1/tests/fixtures/radar/card-settings.real-shape.json` | 1-102 | 1,966 | 1,966 | 1 — byte-identical |
| `radar_p2_support.excerpt.py` | `setups-c1/tests/cobalt/radar_p2_support.py` | 36-37, 41-48, 51-62, 65-68, 108-109, 112-113 | — (excerpt) | 1,768 | 1 — `FORMED_AT` (line 38, between `TRADE_DATE` and `fixture_bars`) deliberately excluded: not in the named symbol list, and its comment ("11:40 ET, path A per the fixture") looks like an engine-derived formation anchor, so it is treated like the `:40-42` exclusion in spirit even though it does not match the literal forbidden-string grep. |
| `setups_shapes.excerpt.py` | `setups-c1/tests/cobalt/setups_shapes.py` | 45-93, 94-128, 129-203, 205-218, 258-266, 316-345, 346-377, 378-406, 407-412, 423-475 | — (excerpt) | 16,971 | 1 — never opened `:1-44` |
| `tunables.excerpt.yaml` | `setups-c1/configs/cobalt/taxonomy/tunables.yaml` | 32-39, 60-71, 73-80, 157-164, 201-211, 215-222, 226-233, 237-244, 247-257, 260-269, 313-321, 382-389, 391-398, 400-407, 664-671 | — (excerpt) | 5,100 | 1 — `A-19` not found under that tag (noted in TASK.md, not guessed) |
| `SETUPS-AT-DEFAULTS-FINAL.excerpt.md` | `docs/30 - Design/SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md` | 68-213 | — (excerpt) | 27,368 | 1 |
| `TASK.md` | written by the hub | — | — | 4,545 | 1 |

Forbidden-string sweep (`grep -c "DEF_WRITTEN_\|formed_bar_ts =\|FORMED "`) on all 12 staged files: 0 everywhere.

## House
- **PRIMARY (Gemini, `agy --model gemini-3.1-pro-high`):** called with the task sentence, `run_in_background: true`. Output: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json ... [exited with code 0]`. A HARNESS line (permission auto-denial), not a computation result. `blind-values.md` was NOT created (`ls` confirmed empty). Per STEP-2, fell back to the other house once.
- **FALLBACK (Opus 5, `claude -p --model claude-opus-5`):** the code-check seat, R49 — the SAME house as the builder (Opus 5 built `setups/seven-0921`), so its use here is recorded as **"blind but same-house as the builder"** per the prompt's own framing, not a fully independent L67 house. Ran `--permission-mode plan`, `--allowedTools "Read" "Grep" "Glob"`, wrote no file itself (its own words: "I wrote no file, although TASK.md asked for `blind-values.md`: your instruction and plan mode both forbid writes"). Complete output read and transcribed VERBATIM by this hub into `blind-values.md`. `wc -c blind-values.md` = 4,349 B.

**Result: 16 of 17 fields UNDERIVABLE.** Every formed bar, side, trigger and stop across all four slugs is UNDERIVABLE — the house names, per field, the specific unstaged detector/rule it needed (extension lifecycle, `htf_range_break`, `bar_break_trigger`, the tracked-extreme stop resolver, EMA/VWAP/ATR seeding, leg roles, the level set, the RangeBreak lifecycle, etc.). The one field with a number, rubberband's last close, has TWO candidates (5.6300 / 5.5750) because the excerpts don't state the as-of bar-visibility cutoff. The house raised 2 of its own ESCALATE items (a daily-bars/intraday-bars contradiction in the fixture; an ambiguous `stop.buffer` unit).

## ORDER
Order proof (T1 < T2 ≤ T3), each its own call:
- `ls -lT blind-values.md` → T1 = `Sep 22 11:14:31 2026`
- `date` → T2 = `Tue Sep 22 11:14:49 EDT 2026`
- ONLY NOW, the first read of the pins this session, one file per call:
  - `grep -n "^DEF_WRITTEN_" test_rubberband_forms.py` → lines 56, 58, 60, 62, 64 — matches THE 17 PINS table exactly.
  - `grep -n "^DEF_WRITTEN_" test_setups_nine_ema.py` → lines 221, 223, 225, 227 — matches.
  - `grep -n "^DEF_WRITTEN_" test_setups_vwap_cont.py` → lines 203, 205, 207, 209 — matches.
  - `grep -n "^DEF_WRITTEN_" test_setups_second_chance.py` → lines 198, 200, 202, 204 — matches.
- `date` → T3 = `Tue Sep 22 11:15:05 EDT 2026`

T1 (11:14:31) < T2 (11:14:49) ≤ T3 (11:15:05) — proof holds. No earlier tool call of this session named any of the four pin files except inside this prompt's own text (17-setups-blind-committed-day.md's THE 17 PINS table); this transcript is the record.

## Comparison
Normalisation: prices as decimals (trailing zeros ignored); timestamps as instants; side compared literal-for-literal. 17 rows, one per pinned constant.

| slug | field | pinned | blind | verdict |
|---|---|---|---|---|
| rubberband | formed bar | `2026-01-06 16:22:00+00:00` (`datetime(2026, 1, 6, 16, 22, tzinfo=UTC)`) | UNDERIVABLE | UNDERIVABLE |
| rubberband | side | `short` | UNDERIVABLE | UNDERIVABLE |
| rubberband | trigger | `5.5000` | UNDERIVABLE | UNDERIVABLE |
| rubberband | stop | `5.81` | UNDERIVABLE | UNDERIVABLE |
| rubberband | last close | `5.5750` | UNDERIVABLE — two candidates offered contingent on an unstated as-of cutoff rule: `5.6300` (bar visible at ts ≤ as_of) or `5.5750` (only completed bars) | UNDERIVABLE — note: one candidate (`5.5750`) is textually identical to the pin; the house did not commit to it as its answer (it named the missing cutoff rule), so this is recorded as UNDERIVABLE, not MATCH, per L37 (no guessing on the house's behalf) |
| nine-ema-scalp | side | `long` | UNDERIVABLE | UNDERIVABLE |
| nine-ema-scalp | formed bar | `2026-01-06T15:36:00+00:00` | UNDERIVABLE | UNDERIVABLE |
| nine-ema-scalp | trigger | `4.7930` | UNDERIVABLE | UNDERIVABLE |
| nine-ema-scalp | stop | `4.64` | UNDERIVABLE | UNDERIVABLE |
| vwap-continuation | side | `long` | UNDERIVABLE | UNDERIVABLE |
| vwap-continuation | formed bar | `2026-01-06T20:04:00+00:00` | UNDERIVABLE | UNDERIVABLE |
| vwap-continuation | trigger | `24.8120` | UNDERIVABLE | UNDERIVABLE |
| vwap-continuation | stop | `24.75` | UNDERIVABLE | UNDERIVABLE |
| second-chance | side | `long` | UNDERIVABLE | UNDERIVABLE |
| second-chance | formed bar | `2026-01-06T16:22:00+00:00` | UNDERIVABLE | UNDERIVABLE |
| second-chance | trigger | `5.3000` | UNDERIVABLE | UNDERIVABLE |
| second-chance | stop | `5.21` | UNDERIVABLE | UNDERIVABLE |

**fields: 17 · MATCH: 0 · MISMATCH: 0 · UNDERIVABLE: 17**

## ESCALATE
No MISMATCH this run — nothing to FIX-or-OWNER. Every one of the 17 rows is UNDERIVABLE, expected per L70 (NOT a defect) for a design that leans on EMA/VWAP/ATR/extension/level-set/leg-role detectors this packet correctly withheld (they are engine code, not staged rules). Per field, what the house named as missing and what a CODE-CAPABLE independent seat (Sol, read/write, back Sat 2026-09-26 06:47 ET per `cto-2026-09-22.md` R13 — a NEW string would be needed) would add, still blind:

| slug | field | missing rule / computation | what Sol would add (still blind) |
|---|---|---|---|
| rubberband | formed bar | `Extension.state == culminating` needs the extension-lifecycle detector (`extension.py`, not staged) | compute the extension lifecycle on the staged bars and resolve `culminating \| none` |
| rubberband | side | `A-01` needs `ext.direction`; the day-1 HTF avoid needs `htf_range_break` (`daily.py:182-196`, not staged) | same detector + `htf_range_break` on the staged daily/intraday series |
| rubberband | trigger | `bar_break_trigger` (`structure.py:82-93`) not staged; only `bars_cleared: 2, direction: any` known | implement the two-bar-clear trigger price rule on the staged bars |
| rubberband | stop | the tracked-extreme resolver + buffer/round-away/ten-cent nudge (`structure.py:70-79`, `:96-116`) not staged | compute the tracked extreme and apply the buffer once its unit is ruled (ESCALATE 2 below) |
| rubberband | last close | the as-of bar-visibility cutoff (ts ≤ as_of vs. only-completed-bars) is not stated in the excerpts | close the row once the cutoff convention is named |
| nine-ema-scalp | side, formed bar, trigger, stop | EMA9/EMA21 seeding (§5, `A-05` not staged); leg roles (`A-07`/`A-14` not staged); `InPlay.state` pool admission (`evaluate.py:320` not staged); `catalyst_ref.resolver` is null and no constructed fill supplies it | compute seeded EMA9/EMA21 and leg roles on the staged bars; the `catalyst_ref` null-resolver reading needs a ruling, not code — flag to the desk, not Sol |
| vwap-continuation | side, formed bar, trigger, stop | VWAP anchor/price-source (`A-12` not staged); seeded ATR (`A-05` not staged, blocks `dist ≤ 1.7×ATR`); leg roles; pivot definition `cfg(pivot.n)` (not staged, only `trendline.min_pivots`); `Level_ref(resistance).rejected` (`A-18` not staged) | compute VWAP, seeded ATR and pivots on the staged bars once `A-12`/`A-05`/`pivot.n` are staged or ruled |
| second-chance | side, formed bar, trigger, stop | the level set (`A-17` not staged); the RangeBreak `accepted` rule (not stated); `event(retest)` tolerance needs ATR (not computable); the `turn_candle`/`event(stop_hit)`/`Range(prior)` stop refs (`A-22`, `A-21`, `A-23` not staged) | compute levels, RangeBreak lifecycle and the retest/turn refs on the staged bars once `A-17` and ATR seeding are staged |

House's own ESCALATE (2), packet-quality notes, not MISMATCHes:
1. **Daily/intraday contradiction in the committed fixture.** `daily-bars.real-shape.csv`'s `FTFT,2026-01-06` row reads O 6.15 H 7.18 L 5.813, but the RTH intraday bars for that same date open at 4.5690 (`14:30:00+00:00`) and trade as low as 4.8500 (`16:20:00`) — below the daily row's stated low. `fixture_daily` (staged) passes the same-day row through unfiltered. Whether the real `daily.py` excludes the trade date from the daily series it hands the HTF avoid is not staged, so the HTF-avoid input this packet gives is suspect. Owner: the desk / the fixture's author, not a code fix.
2. **`stop.buffer` unit is ambiguous.** `tunables.excerpt.yaml`: `value: 0.02, unit: cents` — could read 0.02¢ or $0.02, and every stop above needs it once its detector is staged. Owner: a ruling, not code.

House used: **Opus 5** (`claude -p --model claude-opus-5`) — the FALLBACK, PRIMARY (Gemini/`agy`) having FAILED on a harness permission denial before producing any output. Recorded per the prompt's own instruction as **"blind but same-house as the builder"** (Opus 5 also built `setups/seven-0921`) — a same-house check, not a fully independent L67 house; this is disclosed, not concealed.

Files/keys NOT staged, and why:
- `radar_p2_support.py:38` (`FORMED_AT`) — not in the named symbol list (`fixture_bars`, `fixture_daily`, the settings reader, `defaults`, `TRADE_DATE`, `engine_tunables`, `FIXTURES`); its comment ("11:40 ET, path A per the fixture") reads as an engine-derived formation anchor, so excluded in the spirit of the `:40-42` exclusion even though it did not match the literal forbidden-string grep.
- `tunables.yaml` — the `A-19` tag: no row in the file carries that literal tag; the key it would presumably annotate, `range_break.failed_trap_bars`, IS staged under its own name (value: null).
- `daily-bars.real-shape.csv` byte-identity gap — the original has CRLF line endings (76 `\r` bytes); the Write tool normalizes to LF and this text interface cannot emit a bare `\r`. Every field/row is otherwise identical (confirmed by re-reading both files). Not a data alteration — a tooling limit, disclosed in `## Packet`.
- Every file on the NEVER-STAGED list (the four pinned test files, `test_setups_lego.py`, `test_setups_hitchhiker.py`, every other `test_setups_*.py`, the build report, `65-setups-one-build.md`, `56-setups-c1-build.md`, `setups_shapes.py:1-44`, round 1's check reports, `scratch/tribunal-bars-0920/setups-one-check/`, `12`'s cut report outside `## FOR 13`, any `DEF_WRITTEN_` line) — none opened before the house answered; the pins were opened only in `## ORDER`, after `blind-values.md` existed.

ASK DESK: none this run — no question needed a human answer; the PRIMARY→FALLBACK house substitution and the CRLF gap were both resolved by the prompt's own stated rules (STEP-2's "a METER/HARNESS line → the other house once"; the safe default of disclosing rather than forcing a byte match I cannot produce through this interface).

**ESCALATE: 19** (17 UNDERIVABLE field rows above + 2 house-raised packet-quality items). The file/key NOT-STAGED notes and the CRLF gap are housekeeping disclosures, not counted separately — they are already covered as packet notes in `## Packet` and above.

## CONTINUE
next: NOT YOURS — the desk reads this comparison; `16` stages it as HOLD 1's closure for the existing pins (17's own run is DONE).

SETUPS BLIND COMMITTED DAY DONE · house: Opus 5 (fallback; Gemini/agy FAILED — harness permission denial) · slugs: 4 · fields: 17 · MATCH: 0 · MISMATCH: 0 · UNDERIVABLE: 17 · ESCALATE: 19
