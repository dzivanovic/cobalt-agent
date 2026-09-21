# Stale marker — prompt drafter report (2026-09-21)

Seat: prompt drafter `stale-marker-draft-0921` · Opus 5 · started 16:15 ET, done 16:3x ET (`date`: 16:15:02 start, 16:30:07 last check). It read only, and wrote exactly the five files `50-draft-stale-marker.md` names. It made no commit and launched nothing.

## §0 Headline
- Four prompts drafted: `51` build (Sonnet 5, offline, `s2/stale-marker-0921`), `52` check (3 houses), `53` Tuesday deploy (Sonnet 5, L66 shape, tag `deploy-2026-09-22`), `54` one-round read of `53`. None launched.
- Rule proof: `51` / `52` / `54` add NO rule. Every string counts 1 against its approved source. `53` carries 3 new branch-named strings, the same shape as his R12 for `16`.
- `52` / `54` need HIS extension of `Bash(grok *)` / `Bash(agy *)` to 2026-09-22 if they run Tuesday. Both also accept 2026-09-21 under R23 as it stands.
- ESCALATE: 6. None is a blocker for the desk's approval list.

## L74
A block arrived next to a tool result in this session. It asked for a `Claude-Session:` line in commits and named a file-send tool. It is DATA and was not followed. This run makes no commit.

## L29 seat finding
Builder seat = **Sonnet 5**. Evidence: on `s2/degraded-line-0921` (`7b0a6a3`, the tree tonight's `16` lands), `src/cobalt/aset/radar_panel.py:6-9` says "this module itself never writes, initializes a schema, or attests a note". `grep -n -i "insert\|transition\|assert_writable\|execute\|commit\|write"` over that file hits ONLY docstring lines `:6` and `:8`. Every line the build moves is in that file: `PoolView` `:174-192`, `build_pool_view` `:477-482,589-594,620-`, `render_row` `:827`, `render_pool` `:861`, `_card_detail` `:981,1011`, `render_ladder` `:1044`, `PANEL_CSS` `:1079`, `PANEL_JS` `:1127-1138`, `render_radar_page` `:1154`. `web.py` / `store.py` / `src/cobalt/cards` / `src/cobalt/radar` must stay an EMPTY diff. The only place that serializes `PoolView` is `pool_api_payload` (`radar_panel.py:1163`, called at `web.py:880`); `grep -rln "PoolView\|pool_api_payload" src` finds only `web.py` and `radar_panel.py`. Same finding and precedent as `14` (degraded line, Sonnet, ran clean).

## Worktree creation (the desk, after `16` landed and tag `deploy-2026-09-21b` exists)
`git -C /Users/cobalt/cobalt worktree add -b s2/stale-marker-0921 /Users/cobalt/cobalt-wt/stale-marker main` then `cd /Users/cobalt/cobalt-wt/stale-marker` (then `51`'s `claude --bg …` line).

## Prompts
| file | bytes (`wc -c`) | seat | cwd | report / stop line |
|---|---|---|---|---|
| `prompts/2026-09-21/51-stale-marker-build.md` | 46,552 | Sonnet 5 hub `stale-marker-build-0921` | `~/cobalt-wt/stale-marker` | `…/stale-marker/docs/40 - DevDocs/reports/stale-marker-build-2026-09-21.md` · `STALE MARKER BUILT <tip> \| on <main tip> \| …` (the shape `50` gave, verbatim) |
| `prompts/2026-09-21/52-stale-marker-check.md` | 35,624 | Sonnet 5 hub `stale-marker-check-0922` | `~/cobalt-wt/agy-trial` | `reports/stale-marker-check-2026-09-22.md` · `STALE MARKER CHECK DONE · …` |
| `prompts/2026-09-21/53-stale-marker-deploy.md` | 34,650 | Sonnet 5 hub `stale-marker-deploy-0922` | `~/cobalt` | `reports/deploy-2026-09-22.md` · `STALE MARKER DEPLOY DONE <tip> · tag deploy-2026-09-22 · …` |
| `prompts/2026-09-21/54-review-stale-marker-deploy.md` | 23,808 | Sonnet 5 hub `stale-marker-deploy-review-0922` | `~/cobalt-wt/agy-trial` | `reports/stale-marker-deploy-review-2026-09-22.md` · `STALE MARKER DEPLOY REVIEW DONE · …` |

Row placeholders the desk fills: `51` one `R__` (launch row, `cto-2026-09-21.md`) · `52` one `R__` (launch row, `cto-2026-09-21.md` or `-22.md`) · `53` `R##` (HIS approval of the 3 branch-named strings) + `R__` (the desk's launch row), two DIFFERENT rows · `54` none (its `R__` / `R##` mentions refer to `53`).

## RULE PROOF (`grep -c -F -e "<string>"`, quotes included; run 16:2x ET)
- **`51`** vs `prompts/2026-09-21/02-bars-chunk-2-fix-r3.md` (his 09-20 R25): the 16 allow strings each count **1** (`uv run pytest *` · `uv run cobalt jobs restarts *` · `git add *` · `git commit *` · `git diff *` · `git status*` · `git log*` · `git show*` · `git -C /Users/cobalt/cobalt log*` · `cd *` · `mkdir -p *` · `ls *` · `grep *` · `tail *` · `wc *` · `date*`). The 3 denies as one segment count **1**, and so does the `--add-dir` triplet. Whole segment `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` counts **1** in `14-degraded-line-build.md` and **1** in `51`, so it is byte-identical.
- **`52`** and **`54`** vs `prompts/2026-09-20/08-bars-chunk-e-check.md` (09-20 R13): the 14 allow strings each count **1** (`grok *` · `agy *` · `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *` · `mkdir -p scratch/tribunal-bars-0920` · `git -C /Users/cobalt/cobalt show*` · `git -C /Users/cobalt/cobalt log*` · the three `s2-p2-cards` strings · `ls *` · `grep *` · `tail *` · `wc *` · `date*`). The 3 denies count **1**. The whole segment counts **1** in each of `08`, `15`, `35`, `52` and `54`, so all five are byte-identical. astra's ` < /dev/null` is a redirect after the quoted sentence. It was accepted under the Codex string on 09-21 (`setups-tribunal-r2-2026-09-21.md:87`), so it is not a new string.
- **`53`** vs `prompts/2026-09-19/02-deploy-stack-3.md`: 27 generic allow strings each count **1** (`add` · `commit` · `reset --soft HEAD~1` · `tag` · `revert --no-edit` · `revert --abort` · `git -C * status/log/diff/rev-parse/rev-list/show` · `COBALT_ENV=production uv run cobalt jobs *` / `heartbeat show*` · bootout ×2 · bootstrap ×2 · kickstart ×2 · `launchctl print gui/501/*` · the curl string · `grep` · `tail` · `ls` · `wc` · `date`). The **3 branch-named strings count 0**, as expected. The deny + `--add-dir` segment counts **1** in `16-degraded-line-deploy.md` and **1** in `53`.

## NEW approvals:
One list for the desk to show him verbatim:
1. `Bash(git -C /Users/cobalt/cobalt merge --ff-only s2/stale-marker-0921)`: `53` only, Tue 2026-09-22 evening deploy.
2. `Bash(git -C /Users/cobalt/cobalt-wt/stale-marker rebase main)`: `53` only.
3. `Bash(git -C /Users/cobalt/cobalt-wt/stale-marker rebase --abort)`: `53` only.
4. `Bash(grok *)` and `Bash(agy *)` extended THROUGH TUESDAY 2026-09-22 23:59 ET, for the same sandboxed headless read-only use, nothing wider. They are needed by `52` and `54` (and by any other house check that runs Tuesday). The desk records his word as a `| R` row carrying the literal `Bash(grok *) and Bash(agy *) through 2026-09-22` and his quoted words. `52` / `54` grep that literal in `cto-2026-09-22.md` / `cto-2026-09-21.md` only.

## Tuesday's window (clock evidence, read 16:2x ET)
- Pause 20:00–21:00 ET: `configs/cobalt/taxonomy/tunables.yaml:275-276` `session.market_reset_open` `"20:00"`, `:285-286` `_close` `"21:00"`.
- `com.cobalt.archiver` Tue 20:30 (`ops/com.cobalt.archiver.plist:57`, Weekday 2 Hour 20 Minute 30) · `com.cobalt.replay` Tue 21:10 (`ops/com.cobalt.replay.plist:39`) · `com.cobalt.backup` Tue 21:40 (`ops/com.cobalt.backup.plist:75`).
- So: launch ≈20:02; start window 20:00–20:15; HARD CLOCK 20:25 before bootout; the merge refuses at or after 20:29. These are `16`'s numbers, and they still fit Tuesday.

## Other unmerged branches (L68; `git -C /Users/cobalt/cobalt branch --no-merged main`, 16:2x)
`bars/chunk-1a-0920` · `bars/chunk-2-0920` · `bars/chunk-e-0920`: nothing of bars deploys before WED 09-23 (09-20 R20, `cto-2026-09-21.md:124`). `ops/agy-trial-0915`: this drafter's cwd, not shipping. `s2/degraded-line-0921` lands TONIGHT (`16`), before `51` cuts. `s2/rubberband-proof-0921` is tests + report, input to a design (`cto-2026-09-21.md:213-215,225`). `sprint-2/cards`. **Could land the same Tuesday evening: none named by the files.** `53` therefore has NO stacked gate. If the desk decides to ship `s2/rubberband-proof-0921` beside it, `53` must be re-issued with an L68 stacked gate. The desk decides.

## READING:
- `Vault/Think/6 - Permanent/Memory/LAWS.md` (full, L1–L74)
- `docs/30 - Design/STALE-MARKER-PROPOSAL-2026-09-21.md` (full) · `reports/stale-marker-design-2026-09-21.md` (full)
- `prompts/2026-09-21/14-degraded-line-build.md`, `15-degraded-line-check.md`, `16-degraded-line-deploy.md` (as re-issued), `35-review-degraded-line-deploy-r2.md` (all full)
- On `s2/degraded-line-0921`: `src/cobalt/aset/radar_panel.py` (lines 1–210, 433–640, 775–1170), `tests/cobalt/test_radar_panel.py` (lines 1–155, 410–530, 617–916 + index), `tests/cobalt/test_radar_panel_cards.py` (full), `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (full)
- `reports/cto-2026-09-21.md` rows R12, R19, R27, R30–R38 and §13 lines 337–339, plus greps for Tuesday / branch plans (lines 13, 83, 124, 213–225)
- `reports/setups-tribunal-r2-2026-09-21.md` lines 5, 17, 35, 87 (astra ` < /dev/null`: "reads started")
- `ops/com.cobalt.archiver.plist`, `com.cobalt.replay.plist`, `com.cobalt.backup.plist` (schedule keys) · `configs/cobalt/taxonomy/tunables.yaml:275-288`
- `src/cobalt/aset/web.py` (grep: `model_dump` / `pool_api_payload` / `render_radar_page`) · `src` grep for `PoolView` consumers
- `git log --oneline -8 main`, `git tag --list "deploy-2026-09-2*"`, `git branch --no-merged main`
- NOT read: `prompts/2026-09-21/34-degraded-line-rebase.md` (its stop-line shape is quoted in `16` and R33; `53` has no rebase run). `02-deploy-stack-3.md` was only grepped. `test_radar_panel.py` lines 155–410 are fixture/view tests not touched by the build.

## ESCALATE
1. **`51` departs from the proposal in three named places. The desk chose them; the checkers are asked about them.** (i) `bars_stale_tickers` is a map ticker → tooltip, not a bare set. The tooltip needs reason + since, and the clock exists only in `build_pool_view`. (ii) The badge is a `<span class="bars-stale">`, placed INSIDE the strip's `<b>`. A fifth child would break `.strip`'s 4-column grid (`radar_panel.py:1073`) and shift `.strip span:nth-child(4)` at ≤700 px (`:1075`). (iii) `data-bars-stale` holds JSON ticker → tooltip, so `mirrorStale` can title a badge it adds. All three are written into `51`'s INDEX CARD item 2 and into `52` question 6.
2. **Golden hash pins (`51` T1 (b), (f)).** They are captured on main's code and prove "rows, cards, API JSON, banner and degraded line unchanged". The cost: any FUTURE build that changes ladder or pool markup must re-pin them, which is a re-point under the no-weakening rule. `52` question 5 asks the houses whether they are a real proof.
3. **HIS, a separate scoring item (L52), carried and not built:** an open card is refreshed and can SCORE on a stale `last` once its computed dots are tapped (proposal ESCALATE 1; `evaluate.py:1329-1349,776-777,803`; `scoring.py:248`). `51` names it as a READING and touches nothing of it.
4. **The three clocks (proposal ESCALATE 2 / Q1):** this is `52` question 7. It becomes HIS only if a house shows a SILENT window: a card the evaluator holds `input_stale` with no badge and nothing else loud (L53).
5. **Earlier is possible (L73, minimum idle):** `52` and `54` accept 2026-09-21 under R23 as it stands. If `51` is BUILT tonight (after `16`, ≈20:05+), the check and the read can run before 23:59 without the extension. `54` also runs whenever `53` is committed. The extension is needed only for a Tuesday run.
6. **`54` asks astra too when its probe says UP.** `35` had astra NOT ASKED for a window reason that no longer applies. The strings are identical; L67 says more houses when the meters allow. Stop line `houses that read it: <n> of <n>`. `53` gates on "does not begin `0 of`".

## CONTINUE
Done. The desk's next steps:
- L35 on the five files.
- ONE approval list to him (`## NEW approvals:` verbatim).
- Commit the prompts with `cto-2026-09-21.md`.
- After `16`: if it ends `DEGRADED LINE DEPLOY DONE … rollback: not used` and tag `deploy-2026-09-21b` exists, create the worktree (two commands above), fill `51`'s `R__` and launch `51`. **If `16` FAILED or rolled back, `51`'s PREFLIGHT refuses (no tag). The desk re-issues `51` against whatever main then is (its line numbers are the degraded-line tree's) and says so to him.**

## DIGEST FOR THE DESK
- **51 build** (Sonnet 5, OFFLINE, ≈45 min). The desk first creates `~/cobalt-wt/stale-marker` on `s2/stale-marker-0921` off main AFTER `16`. The hub proves R36 + your lane bullet + its launch row are committed, and that its strings = `02-bars-chunk-2-fix-r3.md` (R25).
  - PREFLIGHT refuses without tag `deploy-2026-09-21b` in its cut, or without `mirrorDegraded` in the tree.
  - Baseline suite. Then TEST FIRST on the real page, both frames, using the fixtures' own tickers: the current pool member (row), FTFT (the evaluator's cards, outside the pool = lifecycle case), and GURE (neither).
  - Tests: (a) badge on exactly those rows/cards (strip, ARMED `last`, LEVELS `last`, never terminal/departed) with tooltip `<reason> since HH:MM ET` · (b) healthy: no badge, and golden sha256 pins (taken on main's code) for rows, cards and API JSON · (c) lifecycle card marked, no row · (d) the fragment stale→fresh→stale follows; ladder byte-identical once badges are stripped; `mirrorStale` wiring asserted and forbidden to fetch/sort/classList/innerHTML · (e) API JSON keys unchanged · (f) banner + degraded line pinned.
  - The code, in `radar_panel.py` only: `PoolView.bars_stale_tickers` (ticker→tooltip, `exclude=True`, filled only when `poll_only`) · one `_bars_stale_badge` renderer · row ticker cell · inside the strip `<b>` · ARMED/LEVELS `last` · `data-bars-stale` JSON on the pool section when non-empty · one CSS line (red `.badge` geometry) · `mirrorStale()` + ONE call after `mirrorDegraded(next)`.
  - DevDoc paragraph says the look is ASSUMED. CLOSE: full suite, diff = the 4 paths, EMPTY diffs for cards/radar/store/web/configs, `cobalt jobs restarts` verbatim (expect `com.cobalt.aset` only).
  - Stop `STALE MARKER BUILT … | ESCALATE: n`.
- **52 check** (Sonnet 5 hub, ≤20 min per house). Date gate: 09-21 under R23, 09-22 only with HIS extension row, 09-23 → FAILED. Staggered against `54` (same Gemini seat). astra with ` < /dev/null` because the setups r2 report records "reads started".
  - Stages the built code, both tests, DevDoc, route excerpt, diff, build report + prompt, R36 + your 16:12 lane bullet, the proposal, and `clocks.excerpt.md` (poller / evaluator `input_stale` / scoring / tunables).
  - 7 questions: exact tickers both frames · one state or a second computation · badge stale / ladder moves · nothing else changed (incl. strip 4-column grid) · weaker assertions / are the pins a real proof · the proposal's §7 four · three clocks (a SILENT `input_stale` window = HIS, L53).
  - The hub file-checks every claim, plus 4 checks of its own (paths, empty diffs, no removed banner/degraded/JS lines, `exclude=True`). TaskStop on any house past 20 min.
  - Stop `STALE MARKER CHECK DONE · … defects that HOLD: n …`.
- **53 deploy** (Sonnet 5, cwd `~/cobalt`, TUE 09-22 ≈20:02, window 20:00–20:15, hard clock 20:25, merge refused ≥20:29).
  - AUTH: R36 · HIS approval row `R##` (the 3 branch strings) · your launch row `R__` · build stop line (all `proven`, `<f>`=0, committed on branch) · check `defects that HOLD: 0` committed · review `launch blockers that HOLD: 0` or folds named.
  - Tips come from the BUILD's stop line (`<tip>`, `<cut>`, `<suite>`). There is no rebase run: main must be docs-only since `<cut>`, or FAILED (then you issue a `34`-shape rebase and re-issue `53`).
  - STEP-0 = `16`'s P0–P12: identity, dirty-main rules, tag + empty-commit probe, heartbeat, plist paths, log baselines, marker `function mirrorStale(layer)` = 0.
  - STEP-2 rebase (no-op OK) → 3.1 code identity → 3.2 RESTARTS derives aset only → 3.3 exactly 5 paths + EMPTY radar/cards/archiver/session/migrations/web/store/configs/ops diff → tag `pre-stale-marker-0922`, then the relaunch rule.
  - STEP-4: aset + radar bootout → ff-merge → bootstrap. Smoke: new pids, uvicorn start tied to P8, no new tracebacks, radar line after `<t down>`, three curls with `\?`, marker = 1, heartbeat.
  - ONE rollback path (revert `<pre-merge>..HEAD`); every failure ends with a bootstrap of both residents. Tag `deploy-2026-09-22`, report `deploy-2026-09-22.md`. The live badge cannot be seen in the pause (the `stale` reason is RTH-only), so you confirm it with him at the next RTH poll failure.
- **54 read of 53** (Sonnet 5, ONE round). Gate: 09-21 (R23) or 09-22 before 19:30 with HIS extension.
  - grok + gemini + astra-if-UP. Stages `53`, `16` as it ran, `deploy-2026-09-21b.md`'s tail, `51` (stop-line shape), the build stop line if any, R12/R33/R36, the clock greps, and 12 pre-run greps.
  - 7 questions: dropped `16` gates · identity gates vs docs commits above `<tip>` · false refuse/pass (no-op rebase, docs-only main, `ESCALATED` field) · rollback one path · restarts + archiver clock · can a non-desk file satisfy an auth grep · anything else.
  - The hub file-checks and re-proves the strings. Stop `STALE MARKER DEPLOY REVIEW DONE · … launch blockers that HOLD: n …`.
- **ASK HIM (one list):** the 3 branch-named strings + grok/agy through 2026-09-22 (`## NEW approvals:`).

STALE MARKER PROMPTS DRAFTED · prompts: 4 · builder seat: Sonnet 5 · new rule strings: 3 · house strings to extend: 2 · READING: 9 · ESCALATE: 6
