# STALE MARKER CHECK — ROUND 1 (`68-stale-marker-check.md`)

## §0 Headline
Authorization verified against committed `cto-2026-09-21.md`/`cto-2026-09-22.md` rows (R36, R39, R46, R49, launch row R5); date gate held; PREFLIGHT green (build tip `ead43a0` on main tip `5b208a0`, 4/4 checkers UP). All four checkers (Grok, Gemini, Sol, Opus 5) checked the staged packet independently: 3 of 4 say BUILD STANDS/ready YES (Grok, Gemini, Opus with a minor report-accuracy note); Sol says FIX FIRST/ready NO on a real, file-verified test-coverage gap (the offline suite's fixtures can't distinguish "badge this ticker" from "badge every current row/active card," and never exercise a departed/excluded row sharing a stale ticker) — the shipped code itself is verified correctly ticker-keyed, so this is a proof gap, not a confirmed runtime defect. Status: DONE. ESCALATE count: 6.

## PREFLIGHT
| step | command | result |
|---|---|---|
| date gate | `date` | `Tue Sep 22 06:59:02 EDT 2026` → within 2026-09-21..2026-09-22, OK |
| R36 row | `grep -n "^| R36 " cto-2026-09-21.md` | found line 47, carries "a small STALE stamp on that ticker's row and on its card" |
| R36 committed | `git log -S"a small STALE stamp..." -- cto-2026-09-21.md` | `965bd0f440f7b24e3485eb860f642b596b51350a` (non-empty) |
| R39 row | `grep -n "^| R39 "` | found line 50, carries "All approved" |
| R46 row | `grep -n "^| R46 "` | found line 57, carries "instead of Astra you can use Sol" |
| R46 committed | `git log -S"instead of Astra you can use Sol"` | `53e059456750c0c9efcf50222a7a647630dc4b04` (non-empty) |
| R49 row | `grep -n "^| R49 "` | found line 60, carries "Approved" |
| R49 seat strings present | `grep -c -F` sol string / opus string | 1 / 1 |
| R49 seat strings committed | `git log -S` each | `60147d400b009db5a2518e02b8ab1fe5765db405` (both, non-empty) |
| launch row named | `grep -n "68-stale-marker-check.md"` both desk files | found: `cto-2026-09-22.md:16` (`\| R5 \|`) |
| launch row committed | `git log -S"68-stale-marker-check.md"` | `e491dc88202ac16f32f982cdc4edd99bcd037bb6` (non-empty) |
| date-gate approval row | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-22"` | found line 50 (R39) |
| date-gate approval committed | `git log -S` same literal | `77d4c5952ad405185f1d0110c887d3216129a438` (non-empty) |
| 13+3 rule strings vs `08-bars-chunk-e-check.md` | `grep -c -F` each | all ≥1 (grok/agy = 2, rest = 1) — no 0s, holds |
| Astra string in this launch line | inspection of the launch line in `68`'s own header | absent — no `gpt-6-astra` string in the run |
| `grok --version` | | `grok 1.0.25 (f7e67d6988e2) [stable]` exit 0 — UP |
| `agy --version` | | `1.2.8` exit 0 — UP |
| stale-marker worktree | `ls /Users/cobalt/cobalt-wt/stale-marker` | present |
| build report last line | `tail -n 3 stale-marker-build-2026-09-21.md` | last non-blank line: `STALE MARKER BUILT ead43a0 \| on 5b208a0 \| offline 2230/0 (351 skipped; baseline 2222/0) \| row badge on stale tickers only: proven \| card badges on stale tickers only: proven \| absent when healthy, output unchanged: proven \| stays current, ladder does not move: proven \| API JSON unchanged: proven \| card/scoring paths untouched: empty diff \| RESTARTS: com.cobalt.aset \| ESCALATE: 6` — tip `ead43a0`, main tip `5b208a0` |
| commits `<main tip>..<tip>` | `git log --oneline 5b208a0..ead43a0` | `ead43a0 docs(devdocs): radar_panel — STALE badge on row and card (R36 2026-09-21)`; `0d961e6 feat(radar): STALE badge on the pool row and card...` — 2 commits (C1+D1 shape; recorded, not fatal) |
| branch tip | `git log --oneline -1 s2/stale-marker-0921` | `ca9566f docs(report): stale marker build — badge on row + card, offline 2230/0, RESTARTS com.cobalt.aset` (report commit above `<tip>`, as expected) |
| staging list (`--stat`) | `git log --stat --oneline 5b208a0..ead43a0` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (+2), `src/cobalt/aset/radar_panel.py` (+59/-14), `tests/cobalt/test_radar_panel.py` (+95), `tests/cobalt/test_radar_panel_cards.py` (+176) — exactly the four expected paths, nothing else |
| `.env` in worktree | `ls .../stale-marker/.env` | "No such file or directory" — OK, no escalation |
| `scratch/tribunal-bars-0920` exists | `ls` | present (many prior tribunal folders) |
| `scratch/.../stale-marker-check` recovery | `ls` | "No such file or directory" — fresh run |
| stagger: `ops-6a-check-2026-09-22.md` | `tail -n 3` | last line `OPS 6A CHECK DONE ...` — finished, not blocking |
| stagger: `setups-one-check-2026-09-22.md` | `tail -n 3` | file absent — recorded not started, does not block |
| stagger: `stale-score-tribunal-2026-09-21.md` | `tail -n 3` | file absent — not started, does not block |
| stagger: `stale-score-tribunal-2026-09-22.md` | `tail -n 3` | file absent — not started, does not block |
| Codex launch shape | `grep -c -F "Experiment field: **reads started**" setups-tribunal-r2-2026-09-21.md` | `1` → Sol launch appends ` < /dev/null` |
| probe: SOL | `codex exec -m gpt-5.6-sol -s read-only ... "Reply with only the word OK." < /dev/null` (run_in_background) | printed `OK`, exit 0, no usage-limit text — UP |
| probe: OPUS | `claude -p --model claude-opus-5 "Reply with exactly the word OK"` (run_in_background) | printed `OK`, exit 0, no usage-limit text — UP |
| probe count | | 4 of 4 UP (Grok, Gemini, Sol, Opus) — launch all four |

Verdict: AUTHORIZATION HOLDS, PREFLIGHT GREEN. Proceeding to stage the packet.

## Packet
Staged into `scratch/tribunal-bars-0920/stale-marker-check/` (no `mkdir` — the first Write created the folder). Every file verified byte-for-byte against its original via `diff` + `wc -c` (trailing-whitespace count on all four code-as-built sources was 0, so byte-exact was required and held); `proposal.md` and `ruling-r36.md` carry one added header line each (per the packet spec) — bodies verified identical after the header.

| file | bytes | check |
|---|---|---|
| built/radar_panel.py.part1 | 37051 | diff clean vs `head -n 980` of original |
| built/radar_panel.py.part2 | 21756 | diff clean vs `tail -n +981` of original |
| built/test_radar_panel.py.part1 | 21197 | diff clean vs `head -n 569` |
| built/test_radar_panel.py.part2 | 21242 | diff clean vs `tail -n +570` |
| built/test_radar_panel_cards.py | 31668 | diff clean, whole file (fits one part) |
| built/radar_panel.md | 9773 | diff clean, whole file |
| built/web-radar-routes.excerpt.py | 1534 | headed excerpt, lines 857-885 of `web.py` (route decorators confirmed via `grep -n "^@app.get"`) |
| build-diff.md | 33573 | `git log -p 5b208a0..ead43a0`; `grep -c "^diff --git"`=4 (matches --stat file count), `grep -c "^commit "`=2 (matches commit count) |
| build-report.md | 25886 | diff clean vs `stale-marker-build-2026-09-21.md` |
| build-prompt.md.part1 | 33965 | diff clean vs `head -n 41` of `51-stale-marker-build.md` |
| build-prompt.md.part2 | 12587 | diff clean vs `tail -n +42` |
| ruling-r36.md | 2473 | R36 row (line 47) + §13 lane bullet (line 356) of `cto-2026-09-21.md`, headed, verbatim |
| proposal.md | 12463 | headed; body diff clean vs `STALE-MARKER-PROPOSAL-2026-09-21.md` |
| clocks.excerpt.md | 17306 | 5 excerpts; anchors re-grepped — poller.py and evaluate.py's `refresh_card` and scoring.py's anchors had DRIFTED from the prompt's stated line ranges (real ranges used, drift disclosed in the file's own header) |
| QUESTIONS-CHECK.md | 7874 | `52`'s text verbatim with the R46 "four checkers" substitution, plus the file list |

Total packet: 290,348 bytes. Honest size ÷ 4 ≈ 72,587 bytes per checker (each checker reads the whole packet; this is the requested arithmetic, not a per-checker split).

`--stat` list (`git log --stat --oneline 5b208a0..ead43a0`) named exactly the four paths staged in `built/` — no extra path to stage.

Pre-launch listings (for the "checker wrote nothing" proof in §2):
- `ls -la scratch/tribunal-bars-0920/stale-marker-check` (cwd `agy-trial`): the 15 packet files/dirs above, all mine, timestamps 07:14–07:21 ET.
- `ls -la /Users/cobalt/cobalt-wt/stale-marker`: 27 entries, the worktree's normal tree (`.venv`, `.pytest_cache`, `src`, `tests`, `docs`, etc.), nothing of mine.

## CONTINUE
All four checkers returned (Gemini 07:26, Sol 07:32, Opus 07:28, Grok 07:36 ET — all inside the 45-minute clock, no TIMEOUT). Each answer's own file matches its background stdout verbatim (checked). No checker's ls-diff showed an unexpected write (Grok wrote only its own `grok-check.md`, per its approved allow rule; Sol/Opus/Gemini wrote nothing — no denial text found in any answer). Collation follows.
next: none — collation complete, closing.

## Per question
| question | grok | gemini | sol | opus | checkers challenging: n |
|---|---|---|---|---|---|
| 1 exactly the failing tickers | YES, all placements + frames proven by name | YES, same | NO — implementation correct but exactness test can't distinguish "this ticker" from "every current row/active card" (single-row/single-ticker fixture) | NO — same single-row/single-ticker gap for departed/excluded rows specifically | 2 |
| 2 one state | ONE STATE | ONE STATE | ONE STATE | ONE STATE | 0 |
| 3 stale badge / moving ladder | NONE; in-card lag is Q2-assumed | NONE; in-card lag confirmed | NONE; in-card lag confirmed, failed-refresh retains consistently | NONE; in-card lag confirmed both directions | 0 |
| 4 nothing else changed | NONE, hunks = C1 1-8, strip 4 children intact | NONE | NONE | NONE | 0 |
| 5 assertions | NONE weakened; (b) fixed self-contradiction pre-commit | NONE | NONE | NONE; pins are exact digests | 0 |
| 6a departed | RIGHT — card marked, row not, by design | RIGHT | RIGHT | RIGHT, but "his call" whether to also mark | 0 |
| 6b terminal | CONFIRM no badge | CONFIRM | (folded into Q4) | CONFIRM | 0 |
| 6c JS ticker key | safe for emitted HTML; `data-ticker` would break healthy pins | safe but could mis-key on unexpected HTML/whitespace | safe for emitted markup; fragile if a node were ever inserted first | safe; `data-ticker` would change healthy bytes | 0 |
| 6d exclude=True | sufficient; old equality test unchanged in meaning | sufficient | sufficient; route test additionally proves key absence | sufficient | 0 |
| 7 three clocks | outside-RTH window is the real gap; badge/evaluator mismatch loud only via score-suppressed (unproven from reads) | outside-RTH gap; loud via score_suppressed | outside-RTH gap + no_daily_bars path; not reliably loud (STALE banner/degraded line silent if scan fresh) | outside-RTH gap; loud only via suppressed line, silent on a fully-tapped card | 0 |

Question 7, every checker's answer in full: see each checker's own file (`grok-check.md` §7, `gemini-check.md` (7), `sol-check.md` item 7, `opus-check.md` §(7)) — all four agree the badge follows the poller's clock (180s, RTH+error) only; the evaluator's `input_stale` (200s, all sessions) and the `no_daily_bars` path can leave a card with no badge, most clearly outside RTH; all four agree this can be silent elsewhere on the page unless the card's dots are stale-suppressed and untapped (Grok and Sol flag that whether `score_card` actually populates `score_suppressed` in that exact case is NOT CHECKABLE FROM READS — `score_card`'s body is outside the packet). This window is HIS, per L53 — not a build defect.

## Checked against the branch
| claim | who | file:line | verdict |
|---|---|---|---|
| Badge/tooltip built only from `pool.poll_failures` inside the `poll_only` gate, no second clock/threshold | all 4 | `radar_panel.py:613-619` (branch, matches `built/`) | HOLDS |
| Row badge passed only to the `current` table, never `departed`/`excluded` | all 4 | `radar_panel.py:884-886` | HOLDS |
| Card strip/ARMED/LEVELS badge placements exactly as named, terminal rows excluded | all 4 | `radar_panel.py:1005-1009,1038,1069-1091` | HOLDS |
| `exclude=True` present once, and every `bars_stale_tickers` reference is inside `PoolView`/`build_pool_view`/`render_pool`/`render_radar_page` | gemini, opus, grok | `radar_panel.py:193,647,874-884,1185` (branch, `grep -c "exclude=True"`=1; all `bars_stale_tickers` hits inside those four sites) | HOLDS |
| `--stat` names only the 4 expected paths; `main..HEAD` on `cards`/`radar`/`web.py`/`store.py`/`configs` is EMPTY | (my own check, standing) | `git -C /Users/cobalt/cobalt log --oneline 5b208a0..ead43a0 -- src/cobalt/cards src/cobalt/radar src/cobalt/aset/web.py src/cobalt/aset/store.py configs` | HOLDS (empty output) |
| No `-` diff line removes banner/`render_degraded_line`/`mirrorDegraded`/`pool_api_payload`/`post()`/click handler/`refreshLadder`, and no test assert removed without an equal replacement | grok, opus (independently) | `build-diff.md` (whole diff re-read) | HOLDS — every hunk in both test files is additions only; the four named renderer functions have no `-` line anywhere in the diff |
| **Sol's exactness-coverage claim: `_small_snapshot()` returns exactly ONE `current` row (always the stale one)** | sol | `tests/cobalt/test_radar_panel.py:122` (branch) — `return pool_row, [current, departed, never_admitted]`, one `current` | HOLDS |
| **Sol's claim: the `evaluated` card fixture uses ONE ticker, `FTFT`, for all 6 cards** | sol | `tests/cobalt/test_radar_panel_cards.py:123` — `sup.members("FTFT")`, `sup.fixture_bars("FTFT")` | HOLDS |
| **Opus's parallel claim: `card_ticker`/`GURE` are asserted absent from every pool category (current/departed/excluded), so no departed/excluded row ever shares a stale ticker in any test** | opus | `tests/cobalt/test_radar_panel_cards.py:398-402` — `assert card_ticker not in pool_tickers and "GURE" not in pool_tickers` | HOLDS |
| **But the shipped code itself is correctly keyed per-ticker, not "badge every current row / active card when any failure exists"** | (my own check, resolving whether Sol/Opus's coverage gap is also a runtime defect) | `radar_panel.py:839` (`bars_stale.get(row.ticker)`), `radar_panel.py:1069` (`stale = bars_stale.get(card.ticker)`) | HOLDS — the coverage gap is real (the test suite could not have caught a hypothetical over-broad implementation), but it is a TEST-EVIDENCE gap, not a defect in the code that ships; direct inspection shows per-ticker dict lookups, not a blanket flag |
| Grok's rebuttal: GURE's tip text differs from the row/card tips, so the title-set assertion in test (a) does distinguish it | grok | `test_radar_panel_cards.py:468-470` | HOLDS, but only narrows the gap for GURE specifically (which is never in any pool row/card); does not cover a same-ticker departed/current or multi-active-card scenario — Sol/Opus's gap stands |
| A claim about what a browser does with `mirrorStale`, or the badge's width in the 90px/70px column | all 4 | n/a | NOT CHECKABLE FROM READS (L70) — never a defect, per every checker's own framing |
| Whether `score_card` actually populates `score_suppressed` for a stale-untapped dot | grok, sol | `scoring.py` (`score_card`'s body not in packet) | NOT CHECKABLE FROM READS |

## Ready for the stacked deploy
| checker | CHECK line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK: BUILD STANDS · ready for its deploy: YES` | YES | — |
| gemini | `CHECK: BUILD STANDS · ready for its deploy: YES` | YES | — |
| sol | `CHECK: FIX FIRST mixed-ticker exactness and stale-card route tests · ready for its deploy: NO` | NO | "Mixed-ticker negative coverage and real card route evidence remain unproven." |
| opus | `CHECK: BUILD STANDS EXCEPT departed/excluded no-badge untested (tc:400-401,436-439); report §0 "8 RED" overclaims (5 red) · ready for its deploy: YES` | YES | — |

## ESCALATE
1. **Test-coverage gap in the exactness proof (HOLDS on file-check, both Sol and Opus, same root cause):** the offline suite's fixtures give exactly ONE `current` pool row (always the stale one) and ONE card ticker (`FTFT`, shared by all 6 evaluated cards), and assert `FTFT`/`GURE` are in no pool category at all. So no test could distinguish "badge the failing ticker" from "badge every current row / every active card whenever the pool is degraded," and no test exercises a departed/excluded row sharing a ticker with a current/card badge. Direct inspection of the shipped code shows it IS correctly keyed per-ticker (`bars_stale.get(row.ticker)`, `bars_stale.get(card.ticker)`) — this is a proof gap, not a known runtime defect, but it is real and unresolved by anything in this packet.
2. **Opus: the builder's report §0 headline overclaims** ("8 new tests RED on main's code") — the report's own T1 section shows 5 failed, 3 green-as-pins (`build-report.md:70-75`); HOLDS on file-check (confirmed against `build-report.md` as staged, byte-identical to the branch's report).
3. **Question 7, HIS clocks question (L53), quoted from all four, not a build defect:** the badge follows the poller's 180s/RTH-only/+error clock; the evaluator's 200s/all-sessions `input_stale` (and its separate `no_daily_bars` path) can leave a card with no badge, most clearly outside RTH. All four checkers agree this can be silent elsewhere on the page for a fully-tapped, stale-untapped-free card; whether `score_card` populates `score_suppressed` in that exact case is NOT CHECKABLE FROM READS (`score_card`'s body is outside the packet). This is the proposal's own ESCALATE 2, his to close, never a checker verdict on the build.
4. **In-card badge lag (Q2, all four, ASSUMED by the proposal):** the two in-card badges (ARMED `last`, LEVELS `last`) only update on the next `/radar` load or card action, not on a pool refresh, so a card's strip and its expanded detail can disagree about staleness in either direction for a window. The proposal already flags this as assumed-acceptable; every checker confirms the mechanism, none finds a defect in it.
5. **No browser ran (L70, all four):** live `mirrorStale` behavior and the badge's fit inside the 90px/70px strip column are unproven; not a defect, per every checker's own framing.
6. Packet mismatches: none. Checkers marked `WROTE:`: none (Grok's own `grok-check.md` is its approved write). `ASK DESK`: none needed — no step required a desk answer to continue.

STALE MARKER CHECK DONE · grok: CHECK: BUILD STANDS · ready for its deploy: YES · gemini: CHECK: BUILD STANDS · ready for its deploy: YES · sol: CHECK: FIX FIRST mixed-ticker exactness and stale-card route tests · ready for its deploy: NO · opus: CHECK: BUILD STANDS EXCEPT departed/excluded no-badge untested; report §0 overclaims · ready for its deploy: YES · houses that checked: 4 of 4 · defects that HOLD: 3 · ready for the stacked deploy: 3 of 4 · ESCALATE: 6
