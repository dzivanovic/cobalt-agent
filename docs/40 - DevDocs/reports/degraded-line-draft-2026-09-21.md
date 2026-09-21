# Degraded line — prompt draft report (2026-09-21)

Seat: Opus 5 prompt drafter `degraded-line-draft-0921` (prompt `prompts/2026-09-21/13-draft-degraded-line.md`). Main read at `2d6e018`. Drafted 07:5x–08:0x ET.

## §0 Headline
- Four prompts drafted, none launched: `14` build (Sonnet 5, offline), `15` ≥3-house build check, `16` evening deploy (Sonnet 5, inside the 20:00–21:00 pause, aset AND radar down per L66), `17` one-round house read of `16` (refuses at/after 19:30 ET).
- The degraded state lives in ONE list, `view.pool.banners`. The ladder is never refreshed on a timer, so the line is mirrored by `refreshPool` from the pool layer it just swapped in. No new route, no new payload field, `render_pool` untouched.
- Builder seat: Sonnet 5 (no write-path line is touched). New rule strings: 3, all in `16` and all branch-named (merge / rebase / rebase-abort).
- ESCALATE: 5 (which states the line carries, for him · no JS engine in the build · the 3 new strings · radar down tonight by L66 although R10 says "aset only expected" · the replay plist is not in LaunchAgents).

## WHERE THE DEGRADED STATE LIVES
| state | view field | file:line (main `2d6e018`) | rendered where today |
|---|---|---|---|
| DEGRADED · `Sources: <names>` | `PoolRecord.degraded` / `.degraded_sources` → `BannerView(level="degraded")` in `PoolView.banners` | `radar_panel.py:81-82`, `:579-583` | pool view, `render_pool` `:837-840`, placed at `:851` (below the ladder since `72c4f12`) |
| STALE · `Last scan is older than <2×interval> seconds` | `stale` → `BannerView(level="stale")`; also the `stale-data` outline class | `:577`, `:584-591`; class `:849` | pool view `:851`; outline on `#pool-layer` |
| RETAINED PRIOR-DAY DATA · `Showing trading day <d>` (amber) | `retained` → `BannerView(level="retained")` | `:576`, `:592-599` | pool view `:851` |
| REFRESH FAILED · `retained data is stale · <error>` | none: CLIENT-side, written by `refreshPool`'s catch into the old layer's `#refresh-status`, plus `refresh-failed` / `stale-data` classes | `:1112-1114` | pool view `#refresh-status` `:851` |
| (not carried) whole-page FAILED | `RadarPanelError` → `render_failed_page` | `:477-479`, `:1129-1131` | the whole page; no ladder exists, so no line is needed |
| (not carried) `cobalt-degraded` | a CARD dot's owner source | `:278` | card face — L52, untouched |

Finding: ONE server computation (`build_pool_view` `:577-599`) feeds three banner states; the fourth (REFRESH FAILED) is client-side. The ruling says "when a source is degraded" (= DEGRADED only); the prompt's safe default is "every state the pool view banners today" → `14` carries ALL FOUR and ESCALATEs the choice (ESCALATE 1).

## THE REFRESH FINDING
- `refreshLadder` (`:1066-1075`) runs ONLY after a tap POST (`:1082`), never on a timer; `refreshPool` (`:1103-1116`) runs every `interval` (`:1118`) and swaps `#pool-layer` by id with `payload.html` = `render_pool(view)` (`:1109-1111`, `:1134-1135`). So a line rendered once at page load, or inside the ladder, would go stale silently.
- The line cannot live inside `#pool-layer` (it must sit ABOVE `#ladder-layer`, test (a)), and putting it into `payload.html` would change the payload and break `holder.firstElementChild` (`:1110`).
- SPECIFIED (narrowest): server renders `#degraded-line` (always present, `hidden` when `view.pool.banners` is empty) from the SAME `view.banners` with the SAME inner markup as `render_pool` `:838`; `PANEL_JS` gets ONE function `mirrorDegraded(layer)` that copies the `.refresh-failure,.panel-banner` inner markup of the pool layer into the line, writing only when the text differs (an unchanged refresh writes nothing → the ladder cannot jump); called once after `oldLayer.replaceWith(next)` and once in the catch after the REFRESH FAILED write. No new route, no new payload field, no interval change, `render_pool` / `pool_api_payload` / `web.py` untouched.
- Why narrowest: it rides the one refresher that already runs; it reads the banners the pool layer already rendered (a second RENDERING, not a second computation, L3); it adds one server function, one page insertion, one CSS line (`.degraded-line{…}.degraded-line[hidden]{display:none}` — the `[hidden]` rule copies `.tap-strip[hidden]` `:1048`), one JS function and two calls.
- What stays unproven: no JS engine is in the builder's list (L70) — T1 (d) proves server/fragment parity through degraded → healthy → degraded plus the JS wiring by substring; a browser run is the desk's live confirmation with him.

## L29 SEAT FINDING
Every line the build touches is in `src/cobalt/aset/radar_panel.py`: a new pure renderer, the `render_radar_page` f-string (`:1126`), `PANEL_CSS` (append), `PANEL_JS` (`refreshPool` + one new function). `grep -n -i "insert\|transition\|assert_writable\|execute\|commit\|write"` on main → only the docstring `:6`, `:8` ("this module itself never writes"). `PANEL_JS`'s `post()` (`:1076-1085`) and click handler (`:1086-1100`) reach the POST routes and are NOT touched; the POST handlers `web.py:1294-1391` are NOT touched. → NO write path → **Sonnet 5** (`14` says: a step needing `web.py`, `store.py`, `post()` or a POST handler STOPS and ESCALATEs — the seat would become Opus 5).

## WORKTREE CREATION
By THE DESK, as for `08` (R4): `git -C /Users/cobalt/cobalt worktree add -b s2/degraded-line-0921 /Users/cobalt/cobalt-wt/degraded-line main` — AFTER the launch row and the four prompts are committed on main. `git worktree add` is not in the hub's list.

## PROMPTS
| file | bytes | seat | hub / remote-control | stop line starts |
|---|---|---|---|---|
| `prompts/2026-09-21/14-degraded-line-build.md` | 36152 | Sonnet 5 | `degraded-line-build-0921` (cwd `~/cobalt-wt/degraded-line`) | `DEGRADED LINE BUILT` |
| `prompts/2026-09-21/15-degraded-line-check.md` | 28145 | Sonnet 5 | `degraded-line-check-0921` (cwd `~/cobalt-wt/agy-trial`) | `DEGRADED LINE CHECK DONE` |
| `prompts/2026-09-21/16-degraded-line-deploy.md` | 30359 | Sonnet 5 | `degraded-line-deploy-0921` (cwd `~/cobalt`) | `DEGRADED LINE DEPLOY DONE` |
| `prompts/2026-09-21/17-review-degraded-line-deploy.md` | 18027 | Sonnet 5 | `degraded-line-deploy-review-0921` (cwd `~/cobalt-wt/agy-trial`) | `DEGRADED LINE DEPLOY REVIEW DONE` |
Each carries `R__` for the desk's launch row.

## RULE PROOF
`grep -c -F -e "<string>"` (quotes included), one call per string, 08:0x ET:
- `14` vs `prompts/2026-09-21/02-bars-chunk-2-fix-r3.md`: all 16 allow + 3 deny = **1** each; `--add-dir` triplet = **1**. Whole segment `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` counts 1 in `14`, `08`, `02` (byte-identical).
- `15` and `17` vs `prompts/2026-09-20/08-bars-chunk-e-check.md`: all 14 allow + 3 deny = **1** each. Whole segment counts 1 in `15`, `17`, `09`, `12` and the approved `08-bars-chunk-e-check.md`.
- `16` vs `prompts/2026-09-19/02-deploy-stack-3.md`: 27 of 30 allow = **1** each (add, commit, reset --soft HEAD~1, tag, revert --no-edit, revert --abort, status, log, diff, rev-parse, rev-list, show, jobs, heartbeat show, bootout aset, bootout radar, bootstrap aset, bootstrap radar, kickstart aset, kickstart radar, print, curl 5010, grep, tail, ls, wc, date); the 3 branch-named = **0** (listed below). Deny list + add-dirs segment counts 1 in `11` and `16`. Contiguous runs of `16`'s line proven: the launchctl/curl run counts 1 in `02` and `16`; the status…bootout-aset run and the curl…date run count 1 in `11` and `16`; the first run (add … status) counts 1 in `16` — together they cover the whole line.

**NEW strings:**
- `"Bash(git -C /Users/cobalt/cobalt merge --ff-only s2/degraded-line-0921)"`
- `"Bash(git -C /Users/cobalt/cobalt-wt/degraded-line rebase main)"`
- `"Bash(git -C /Users/cobalt/cobalt-wt/degraded-line rebase --abort)"`
(`02`'s own strings with this branch and worktree named — the shape `11` carried this morning under R5; tonight they stand only on his approval of `16`'s launch line.)

## EVENING WINDOW
Chosen: `16` STARTS 20:00–20:15 ET (desk launches on a timer at ≈20:02); HARD CLOCK 20:25 ET re-checked immediately before the bootout — at or after it nothing goes down; ≈1 min outage (this morning's aset outage was 7 s) ends before 20:30. Why: the radar restarts only in the pause (L43/L66); the archiver's first nightly fires 20:30 and must not meet a half-deployed tree; 3.3 of `16` also proves the branch diff is empty for `src/cobalt/archiver`, `src/cobalt/radar`, `ops`, `configs`, so a rollback crossing 20:30 lands on a tree the archiver reads identically. `17` refuses at/after 19:30 so the desk can fold before 20:00.
Clock evidence (read from the files): pause `configs/cobalt/taxonomy/tunables.yaml:275-293` (`session.market_reset_open` "20:00", `_close` "21:00") · archiver `ops/com.cobalt.archiver.plist:56-60` Weekday 1–5 20:30 · replay `ops/com.cobalt.replay.plist:38-42` Weekday 1–5 21:10 · backup `ops/com.cobalt.backup.plist:73-79` Weekday 0–6 21:40 · radar in the pause logs `radar cycle: paused_market_reset scan_id=None` every ≈100 s (`logs/radar.err`, e.g. 2026-09-18 20:00:06 → 20:58:27). Matches the expected 20:02 / 20:25 / before 20:30; one narrowing: P0 refuses a START after 20:15 (preflight + rebase + gates need the margin before the 20:25 clock).
L68: unmerged branches today (`git log --branches --not main --simplify-by-decoration`): `bars/chunk-2-0920` `c19f304`, `bars/chunk-1a-0920` `6961ee0`, `bars/chunk-e-0920` `982d958`, `sprint-2/cards` `6694652`, `ops/agy-trial-0915` `6b7c5a4` — none lands tonight; only `s2/degraded-line-0921`.
Review lessons folded into `16` (`panel-deploy-review-2026-09-21.md` rows 5, 6, 7, 11): escaped `\?frame=phone` (4.5(c)) · branch identity P0b via `git -C … status --short --branch` on both checkouts (covered by `"Bash(git -C * status*)"`) · RELAUNCH RULE written into `## CONTINUE` at 3.4 (print both residents + main tip first; never a second bootout; no merge after 20:25) · log check tied to this start: `grep -c "Started server process"` in `aset.err` must grow past the P8 baseline, `Traceback` counts unchanged in both logs, a `paused_market_reset` line stamped at/after `<t up>` in `radar.err` (the launchd pid ≠ uvicorn's pid — this morning 35044 / 35050 — so the tie is by count and time, not pid).

## DIGEST FOR THE DESK
**14 build (Sonnet 5, offline, ~30–45 min):**
1. Verify R10 committed, launch row `R__` filled + committed, 19 strings count 1 in `02-bars-chunk-2-fix-r3.md`.
2. PREFLIGHT probes (worktree clean on `s2/degraded-line-0921`, `.env` absent), the drafter's grep quoted; BASELINE suite.
3. T1: five tests on the real page / real route / real fragment — (a) line before ladder when degraded, both frames, names the source, escapes; (b) healthy = `<div id="degraded-line" class="degraded-line" hidden></div>` + CSS `[hidden]` rule; (c) pool banners unchanged (guard, green on main); (d) line = fragment banners through degraded → healthy → degraded + JS wiring substrings; (e) `/radar` and `?frame=phone` routes. RED first, quoted.
4. C1: five places only — new `render_degraded_line`, one insertion in `render_radar_page`, one CSS line, `mirrorDegraded` + two calls in `refreshPool`, `__all__`. GREEN, diff quoted whole.
5. A1 (expected none), D1 (one DevDoc sentence + symbol list; `web.md` untouched).
6. CLOSE: full suite, `diff --stat main`, empty diffs for cards/radar/web.py/store.py/configs, RESTARTS (expect `com.cobalt.aset`), stop line `DEGRADED LINE BUILT …`.
**15 check (Sonnet 5 hub + Grok/Gemini/Astra, reads only, TODAY — grok/agy expire 23:59):**
1. DATE GATE; R13/R23/R10 + launch row; 17 strings count 1.
2. Build stop line must read `DEGRADED LINE BUILT`; stagger vs `17`'s report; Codex probe.
3. Stage code-as-built, routes excerpt, diff, build report, `14`, R10 row, drafter findings, QUESTIONS (placement · one path · staleness/jumping · nothing else changed · assertions · L52).
4. Launch three houses once each; file-check every claim; stop line `DEGRADED LINE CHECK DONE … defects that HOLD: <n>`.
**17 read of 16 (Sonnet 5 hub + three houses; refuses at/after 19:30 ET):**
1. DATE/clock gate; build must be BUILT; stagger vs `15`; Codex probe.
2. Stage `16`, R10, `02` line 3 + `11` line 1, both plists, the clock lines, branch stat, the four lessons, QUESTIONS (radar outside pause / archiver collision · stray paths · rules · resident-DOWN endings · waits · lessons folded · anything else).
3. File-check, own grep -c of every string; stop line `DEGRADED LINE DEPLOY REVIEW DONE … launch blockers that HOLD: <n>`. Desk folds into a re-issued `16`.
**16 deploy (Sonnet 5, cwd `~/cobalt`, launch ≈20:02 ET):**
1. P0 window 20:00–20:15; P0b both checkouts on the right branch; P1 main dirt accepted/refused; tag + empty-commit gate; heartbeat baseline; both pids + plist paths; radar paused; log baselines; `/radar` 200; marker absent.
2. AUTHORIZATION: R10, launch row, build line (all `proven`), check `defects that HOLD: 0` committed, review blockers 0 or folded.
3. Suite by identity; rebase in the worktree; code identity; RESTARTS = aset only; branch carries only its files; empty diff for radar/cards/archiver/session/migrations/configs/ops; tag `pre-degraded-line-0921`; relaunch rule written.
4. 4.1 clock <20:25 → bootout aset + radar → print 113 → ff-merge → bootstrap both → running with new pids.
5. Smoke: pids, log check tied to this start, three curls (`\?`), marker = 1, heartbeat.
6. Red → ONE rollback (bootout loaded, revert range, bootstrap both, re-smoke). Green → tag `deploy-2026-09-21b`, report `deploy-2026-09-21b.md` committed by pathspec; stop line `DEGRADED LINE DEPLOY DONE …`. Desk confirms the live page with him.

## READING
1. `render_degraded_line` repeats `render_pool`'s one-line banner inner f-string (`:838`) rather than refactoring `render_pool`: chosen so the pool view stays byte-identical and `render_pool` is absent from the diff; T1 (d) pins the two equal in every state.
2. A state CHANGE (a source degrades or recovers) moves the ladder by the line's height — inherent in "above the ladder"; an UNCHANGED refresh writes nothing.
3. Pre-existing, not ordered, not touched: the ladder itself refreshes only after a tap (`refreshLadder` `:1082`), never on the timer.
4. `11`'s shape kept `com.cobalt.radar` untouched under R5; tonight nothing is overruled, so `16` follows L66 literally (both residents).
5. `17`'s house timeout is 20 min (`12` used 12 min under a 09:10 clock); not a rule string.

## ESCALATE
1. **WHICH STATES THE LINE CARRIES — his call.** R10: "shown only when a source is degraded". The pool view banners four states (DEGRADED, STALE, RETAINED PRIOR-DAY DATA, REFRESH FAILED); `14` carries ALL FOUR (this prompt's safe default). RETAINED will show red in the line overnight until the first scan; narrowing to DEGRADED only is a one-line filter in two places. ASK DESK: carry all four (built), or DEGRADED only? [08:01 ET] — safe default: all four.
2. **No JS engine in the build (L70).** `stays current on refresh: proven` means server/fragment parity + JS wiring substrings; the live behaviour is confirmed by the desk with him after `16`.
3. **Three NEW strings** (above) in `16`'s launch line — they belong in the ONE approval list the desk brings him.
4. **Radar down tonight.** R10's row says "aset only expected" (that is the RESTARTS derivation); L66 stops BOTH residents before a merge, and nothing overrules it tonight → `16` bootouts/bootstraps the radar inside the pause. If he wants aset-only, that is his per-case override (L73); the desk records it and re-issues `16` with `11`'s radar-untouched proofs.
5. **`com.cobalt.replay.plist` is in `ops/` but NOT in `~/Library/LaunchAgents/`** (`ls` of both, 08:0x ET). Whether 21:10 replay is loaded from the repo path is not provable with this seat's reads (no `launchctl`); it does not touch `16`'s window. Desk item, not a blocker.

## L74
No block asking for a `Claude-Session:` line arrived inside a tool result in this run. The session's own system prompt carried one; this seat made no commit, so no attribution was written.

## CONTINUE
next: none — drafting done; the desk reads, fills `R__` in `14`–`17`, commits, asks him ONE approval list (the three NEW strings of `16` + the ESCALATE 1 / 4 choices), launches `14`.

DEGRADED LINE PROMPTS DRAFTED · prompts: 4 · builder seat: Sonnet 5 · refresh mechanism: refreshPool mirrors pool banners into line · new rule strings: 3 · READING: 5 · ESCALATE: 5
