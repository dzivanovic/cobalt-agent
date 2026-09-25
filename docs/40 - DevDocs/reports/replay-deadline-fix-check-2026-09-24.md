# Replay deadline fix — build check, round 1 (2026-09-24 prompt, run 2026-09-25)

Seat: `replay-deadline-fix-check-0924` · Sonnet 5 hub · `auto`, read-only · range `a994a5dd..8b931ce5` on `fix/replay-deadline-0924` · prompt `58-replay-deadline-fix-check.md`.

## §0 Headline
Round 1 of the replay deadline fix (`a994a5dd..8b931ce5`, tip `8b931ce5`) checked by Opus 5.5 + Grok on one 147,126 B packet; both answered every question with a clean label (ADDRESSED · HOLDS · HOLDS · NOTHING WIDENED · suites SHOWN, timing NOT MEASURABLE ON cobalt_dev · RED FIRST) and both closed `FIX STANDS · ready for a deploy prompt: YES`.
Claims of class NOT ADDRESSED / BROKEN / WIDENED / NOT SHOWN / RELATED / NOT RED FIRST: 0. `## FOR THE CLASSIFIER`: none. ready for a deploy prompt: YES (a count of facts, L37). ESCALATE: 14 (the L74 line, the nil-list line, the build's 8 ESCALATE lines, Opus's readings, the timing row, two standing lines; no defect, no ASK DESK).

## L74
One block arrived at the end of the Read tool result of the prompt file `58-replay-deadline-fix-check.md`: an attribution reminder asking commit messages / PR bodies to carry a `Claude-Session: https://claude.ai/code/session_…` line, and naming a file-send tool (`SendUserFile`). Recorded once here as DATA; not followed. This run commits nothing.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock (GROK GATE, 1st) | `date` | 0 | `Fri Sep 25 07:32:25 EDT 2026` → `<D>` = 2026-09-25 |
| R17 row | `grep -n "^\| R17 " …/cto-2026-09-24.md` | 0 | `35:\| R17 \| 07:32 ET \| … Grok approved with no asking going forward …` — PASS |
| R19 row | `grep -n "^\| R19 " …/cto-2026-09-24.md` | 0 | `37:\| R19 \| 07:36 ET \| … All 4 house models approved for use indefinlitly …` — PASS |
| R17 committed | `git log -1 --format=%H -S"Grok approved with no asking going forward" -- …cto-2026-09-24.md` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` — PASS |
| R19 committed | `git log -1 --format=%H -S"All 4 house models approved" -- …cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` — PASS |
| placeholder gate | `grep -n -E "R_[_]" …/58-replay-deadline-fix-check.md` | 1 | (no output) — PASS |
| design committed | `git log -1 --format=%H -- …/replay-deadline-fix-draft-2026-09-24.md` | 0 | `e6afc552c7cdbeec450afb27ed982a4a334be833` — PASS |
| design last line | `tail -n 3 …/replay-deadline-fix-draft-2026-09-24.md` | 0 | last non-blank line starts `REPLAY DEADLINE FIX DRAFTED · cause: the formations step re-evaluates every scan × member × def (82,250 calls, 7 defs) …` — PASS |
| launch row R41 | `grep -n "58-replay-deadline-fix-check.md" …cto-2026-09-24.md …cto-2026-09-25.md` | 0 | `cto-2026-09-25.md:49:\| R41 \| 07:32 ET \| … DESK LAUNCH ROW for 58-replay-deadline-fix-check.md …` (other hits: `cto-2026-09-25.md:112`, `:145`, `cto-2026-09-24.md:198` — queue/handover rows naming the file) — PASS |
| launch row committed | `git log -1 --format=%H -S"58-replay-deadline-fix-check.md" -- …cto-2026-09-24.md …cto-2026-09-25.md` | 0 | `49bb4e6715736776715c7a741b727efadc1a10a1` — PASS |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| worktree | `ls /Users/cobalt/cobalt-wt/replay-deadline` | 0 | present (AGENTS.md … uv.lock) |
| BUILT line | `tail -n 3 …/replay-deadline-fix-build-2026-09-24.md` | 0 | `REPLAY DEADLINE FIX BUILT 8b931ce5 \| on a994a5dd \| offline 2512/0 \| with-DB 2867/0 \| live-note 146/0 \| .env: removed \| FIX: 3 of 3 \| replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev \| ESCALATE: 8` — carries `\| .env: removed \|` and `FIX: 3 of 3` — PASS. `<tip>` = `8b931ce5`, `<base>` = `a994a5dd`; equals the prompt's filled header `a994a5dd..8b931ce5` (no tip mismatch) |
| D1 RED | `grep -n -F "## D1 RED" …build report` | 0 | one line: `46:## D1 RED`; the section's `git log --oneline -1` quote is `915b7b6e` (D2 says "Red committed: `915b7b6e` (`<red>`)") → `<red>` = `915b7b6e` |
| range | `git -C /Users/cobalt/cobalt log --oneline a994a5dd..fix/replay-deadline-0924` | 0 | 6 lines: `a6b99de0 docs(replay-deadline): build report — 8b931ce5` · `8b931ce5 fix(replay): the tunables-digest pins exclude the new replay.formations_reserve_s row …` · `332f44e1 docs(replay): formations cut + shared member prep — DevDocs + ADR-0010 amendment (R95)` · `12fac3cd fix(replay): the formations step is cut before the deadline as a named partial …; one bar read per ticker (R95)` · `d0898f75 fix(radar): one member prep per scan instant, shared by every def in the replay — no output byte changes (R95)` · `915b7b6e test(replay,radar): red — one member prep per scan, a cut formations step with a named partial, one bar read per ticker (R95)`. Count = 6 (red, FIX 1, FIX 2+3, docs, one D6 fix, report) — as expected |
| red is tests-only | `git show --stat --format=%H 915b7b6e` | 0 | 5 files, all `tests/cobalt/…`: `test_radar_evaluate.py`, `test_radar_evaluate_cli.py`, `test_replay_formations.py`, `test_replay_line.py`, `test_replay_runner.py` (368 insertions, 7 deletions) — PASS |
| no widening | `git log --oneline a994a5dd..fix/replay-deadline-0924 -- src/cobalt/db_migrations tests/fixtures` | 0 | EMPTY — PASS |
| `.env` | `ls /Users/cobalt/cobalt-wt/replay-deadline/.env` | 1 | `No such file or directory` — PASS |
| recovery | `ls scratch/tribunal-bars-0920/replay-deadline-fix-check` | 1 | `No such file or directory` — fresh run |
| stagger | `grep -n -F "no other house hub is running" …/cto-2026-09-25.md` | 0 | many rows match; `cto-2026-09-25.md:49` (R41) carries the literal AND names `58-replay-deadline-fix-check.md` ("STAGGER: no other house hub is running — `16` DONE 07:2x and stopped 07:29 (R39) …") — PASS |
| Opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | stdout `OK` (plus a harness warning about a `Bash(git push*:*)` deny-rule spelling in `../../cobalt/.claude/settings.local.json`) — UP |
| Grok probe | `grok --version` row above | 0 | UP |
| PROBES | | | **TWO UP (Opus, Grok)** — Sol not probed (METER to 09-26 06:47), no Gemini, no Astra. |

Not run by this hub: `mkdir`, the `s2-p2-cards` strings, the `codex exec` string, `agy`.

## Packet
Folder: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/replay-deadline-fix-check/` (created by the first Write; no `mkdir`). Every file is Read → Write below a one-line header naming its real path, range and tip. Git outputs were taken with `run_in_background` and Read from the harness's saved stdout files.

| file | bytes (`wc -c`) | what | check run |
|---|---|---|---|
| `diff.md` | 61,908 | part 1 = `git show 915b7b6e` (445 lines, 9 trailing-whitespace lines); part 2 = `git log -p --format="commit %H %s" 915b7b6e..8b931ce5` (652 lines, 58 trailing-whitespace lines) | `grep -c "^diff --git"` = 22 (5 red + 17 above it), `grep -c "^commit "` = 5, trailing-whitespace lines = 67 (9 + 58); `grep -v -x -F -f` both ways against the two saved outputs: only header and blank lines differ; every path D1–D6 names appears (5 tests + `test_setups_d1.py` / `test_setups_registries.py`, `tunables.yaml`, six `src/` files, six DevDocs + ADR-0010) |
| `code-at-tip.md` | 47,613 | `evaluate.py` 862–1184 · `frame.py` 163–248 (unchanged, context) · `evaluate_cli.py` 101–255 · `runner.py` 280–522 (CUT to `run_nightly`, see below) · `formation_misses` 324–353 · `render_line` 83–146 | 920 lines = 901 source lines + 19 header/blank lines; every non-blank line found in its source (`grep -v -x -F -f` over the six sources: only the six part headers differ); source files 0 trailing whitespace |
| `config-at-tip.md` | 1,348 | `tunables.yaml` 943–968 | every non-blank line found in the source; 0 trailing whitespace |
| `suites.md` | 18,133 | build report: D1 RED, D2 FIX 1, D4, D5, D6, D7, RESTARTS, FOR THE DEPLOY, ESCALATE, stop line | every non-blank line found in the build report; the reverse check shows the only build-report lines absent are the excluded sections (§0–PREFLIGHT, D3, CONTINUE) and blank lines; every section holds an executed summary (D4 `113 passed`, D5 `146 passed`, D6 `2512 passed`, D7 `2867 passed`) |
| `design.md` | 9,135 | drafter's `## Classification (L75)` (lines 10–30) + `## Where the time goes` (32–38) | every non-blank line found in the drafter's report |
| `evidence.md` | 2,962 | `replay.err` 18, 39, 60–69; `replay.log` 95, 467 | every line found in the two logs; ticker replacements: 0 (none carried one) |
| `QUESTIONS-REPLAY-DEADLINE.md` | 6,027 | the prompt's QUESTIONS text + the "Files in this folder:" paragraph | lines 2–9 of the copy found verbatim in the prompt |

**Total: 147,126 B ÷ 4 ≈ 36,800 tokens per checker** (drafter's estimate ≈ 23–35k). **CEILING 150,000 B: under it, but only after the prompt's cut.** With `runner.py` staged whole (25,692 B instead of the 13.5 KB `run_nightly` part) the packet measured ≈ 160.5 KB (byte offsets from `grep -b` on the sources: `evaluate.py` part ≈ 16.7 KB, `frame.py` ≈ 3.6 KB, `evaluate_cli.py` ≈ 7.6 KB, `line.py` ≈ 3.0 KB, `formation_misses` ≈ 2.0 KB), so the prompt's cut applied: `runner.py` lines 280–522 (`run_nightly`, which contains `formations_step`, `line_step` and the step loop), headed as a cut with its line range. `formation_replay` (the `cut_at` pass-through) and `replay_deadline` are not staged as code; their changed lines are in `diff.md` part 2.

**Staging note (a defect of mine, corrected before any checker ran).** My first write of `diff.md` mistyped one context line (`_tunables_digest` for `_tunables_digests`), one docs line (`MoverRow` wording), stopped after the ADR/DevDocs part of commit `332f44e1` with an invented `## 2026-09-25 — placeholder` line, and left out commits `12fac3cd` and `d0898f75`. I found it by the `grep -v -x -F -f` check, fixed the two lines by Edit, replaced the invented tail with the real remainder, and re-ran the check both ways (line count 1,104 = 4 header lines + 445 + 3 header/blank lines + 652). The copy the checkers get is the checked one. The same check was run on every other file before launch.

**Fixture tickers.** The packet carries the tests' synthetic fixture tickers verbatim (as the QUESTIONS allow). No real-day ticker is in any packet file: the log lines in `evidence.md` carry none (0 replacements), and the source excerpts carry only variable names.

## Launch
- THE GROK GATE, second run, immediately before launch: `date` → `Fri Sep 25 07:46:19 EDT 2026`; `| R17 |` row (`cto-2026-09-24.md:35`) present, `git log -1 -S"Grok approved with no asking going forward"` → `1758fd78…`; `| R19 |` row (`:37`) present, `git log -1 -S"All 4 house models approved"` → `5055151d…`. PASS.
- Written-nothing proof, BEFORE both launches (`ls -la`): the packet folder lists exactly the seven staged files (`code-at-tip.md` 47613 · `config-at-tip.md` 1348 · `design.md` 9135 · `diff.md` 61908 · `evidence.md` 2962 · `QUESTIONS-REPLAY-DEADLINE.md` 6027 · `suites.md` 18133, mtimes 07:39–07:45); the worktree `/Users/cobalt/cobalt-wt/replay-deadline` lists `.claude .clinerules .env.example .git .gitignore .pytest_cache .venv .vscode AGENTS.md CLAUDE.md COBALT-REQUIREMENTS.md cobalt.sh configs dev_utils docker-compose.yml docs ops orchestration_plan.json pyproject.toml QWEN.md README.md scripts src tests uv.lock`, top-level mtime `Sep 25 07:19` (no `.env`).
- OPUS launched first, `run_in_background`, task `bj3lx1hgv`, `date` after the launch `Fri Sep 25 07:46:27 EDT 2026`. Launch line as run: `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/replay-deadline-fix-check/. Start with QUESTIONS-REPLAY-DEADLINE.md and follow it exactly. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/replay-deadline-fix-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`.
- GROK launched second, `run_in_background`, task `bp1d4qoxl`, `date` after the launch `Fri Sep 25 07:46:34 EDT 2026`. Launch line as run: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/replay-deadline-fix-check/. Start with QUESTIONS-REPLAY-DEADLINE.md and follow it exactly. Do not open any *-check.md file. Write your check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/replay-deadline-fix-check/grok-check.md and reply with only that path."` (never `--always-approve`).
- 45-minute clock: both launched 07:46; the ceiling was 08:31. No Gemini, no Sol, no Astra.
- Completions: OPUS returned exit 0 (the watch saw it at 07:48:31, ≈2 min after launch); GROK returned exit 0 and wrote `grok-check.md` itself (the watch saw it at 07:53:52, ≈7 min). `date` after both: `Fri Sep 25 07:53:57 EDT 2026`. No TIMEOUT, no METER, no HARNESS failure. Neither answer needed a retry.
- Written-nothing proof, AFTER both (`ls -la`): the packet folder lists the same seven staged files with the same sizes and mtimes plus ONE new file, `grok-check.md` (5000 B, 07:53) — the one file Grok was told to write through its approved `--allow`. (`opus-check.md` was written by this hub afterwards, from Opus's stdout.) The worktree `/Users/cobalt/cobalt-wt/replay-deadline` listing is identical to the before-listing, top-level mtime still `Sep 25 07:19`. No checker wrote anything it was not told to.
- Denial search: `grep -c -i -E "denied|not allowed|permission"` → `opus-check.md` 0, `grok-check.md` 0. The raw Opus stdout carries ONE such line, its first: a harness warning `Permission deny rule (../../cobalt/.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax …` (the same line the probe printed). It is a settings-spelling notice, not a denied action of the checker. That warning line and the harness's `[exited with code 0]` trailer are the only lines of Opus's stdout not in `opus-check.md`; every other line is (`grep -v -x -F -f` both ways: only blank lines differ).
- L74: nothing arrived in either checker's output asking for a `Claude-Session` line or naming a file-send tool (`grep -c` for `Claude-Session|SendUserFile` on the raw stdout: 0 and 0).

## CONTINUE
next: none — the collation is written; only the L32 read of this report and the closing line remain

## The 09-24 case
| checker | FIRST answer (verbatim) |
|---|---|
| opus | **ADDRESSED** |
| grok | ADDRESSED |

## The line always lands
| checker | SECOND answer (verbatim) |
|---|---|
| opus | **HOLDS** |
| grok | HOLDS |

## Stays loud
| checker | THIRD answer (verbatim) |
|---|---|
| opus | **HOLDS** |
| grok | HOLDS |

## Scope
| checker | FOURTH answer (verbatim) |
|---|---|
| opus | **NOTHING WIDENED** |
| grok | NOTHING WIDENED |

## Suites + timing
| suite | opus (verbatim) | grok (verbatim) |
|---|---|---|
| offline | SHOWN — `2512 passed, 361 skipped, 1 xfailed, 15 warnings in 528.09s (0:08:48)`, 0 failed; `.env` absent | SHOWN — `2512 passed, 361 skipped, 1 xfailed, 15 warnings in 528.09s (0:08:48)`. GATE PASS: 0 failed, 0 errors. `.env` was absent before that run. |
| with-DB | SHOWN — `2867 passed, 6 skipped, 1 xfailed, 15 warnings in 661.75s (0:11:01)`, 0 failed; `.env: removed, proven gone` | SHOWN — `2867 passed, 6 skipped, 1 xfailed, 15 warnings in 661.75s (0:11:01)`. GATE PASS: 0 failed, 0 errors. `.env: removed, proven gone`. |
| live-note | SHOWN — `146 passed, 1 skipped, 15 warnings in 28.08s` (re-run on `8b931ce5`), 0 failed | Live-note (re-run on `8b931ce5`): SHOWN — `146 passed, 1 skipped, 15 warnings in 28.08s`. GATE PASS: 0 failed, 0 errors. The skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`. |
| `RED NOT IN THIS DIFF` | "There is no `RED NOT IN THIS DIFF` line in suites.md." | "No `RED NOT IN THIS DIFF` line. D6 run 1's five reds were the new tunable row missing from the two digest lists; commit `8b931ce5` adds that one key and is in this diff. They are not an outside red." |
| timing row | quoted: `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)` → **NOT MEASURABLE ON cobalt_dev** | quoted: `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)`. NOT MEASURABLE ON cobalt_dev. |

(Two of Grok's cells — live-note and `RED NOT IN THIS DIFF` — run past 30 words; I quote them whole rather than trim them, so no answer is changed by cutting.)

**From the build report itself (the real file `/Users/cobalt/cobalt-wt/replay-deadline/docs/40 - DevDocs/reports/replay-deadline-fix-build-2026-09-24.md`, not the packet copy). Facts only, no verdict:**
- Offline (D6 run 2, line 144): `2512 passed, 361 skipped, 1 xfailed, 15 warnings in 528.09s (0:08:48)` — `GATE PASS: 0 failed, 0 errors`. It shows `0 failed`; no `error` count other than the written `0 errors`. (Run 1, line 135, was `5 failed, 2507 passed, 361 skipped, 1 xfailed, 15 warnings in 530.90s (0:08:50)`, RED, on the pre-fix commit `332f44e1`; its five reds are named in lines 137–142 and were cleared by `8b931ce5`.)
- With-DB (D7 (c), line 149): `2867 passed, 6 skipped, 1 xfailed, 15 warnings in 661.75s (0:11:01)` — `GATE PASS: 0 failed, 0 errors`.
- Live-note (D5 re-run on `8b931ce5`, line 131): `146 passed, 1 skipped, 15 warnings in 28.08s` — `GATE PASS`, `<lf>` 0; the one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- D4 green run (line 120): `113 passed, 4 skipped in 63.10s (0:01:03)`: 0 failed, 0 errors.
- `.env: removed, proven gone` IS written (line 151: `rm …/.env` → exit 0; `ls …/.env` → `No such file or directory`). My own `ls /Users/cobalt/cobalt-wt/replay-deadline/.env` at preflight: `No such file or directory`.
- Timing row (D7 (c2), line 150), quoted: `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)` — the command's own output carries `replay 2026-09-24: no membership episodes for pool 'primary'` and `replay 2026-09-24: scans=0 formations=0 path_b_only=0 counts={} writes: none`; `<t0>` `Fri Sep 25 07:19:18 EDT 2026`, `<t1>` `Fri Sep 25 07:19:25 EDT 2026`.
- `RED NOT IN THIS DIFF` lines in the build report: `grep -c -F` → 0.

## Red first
| checker | SIXTH answer (verbatim) |
|---|---|
| opus | **RED FIRST** |
| grok | RED FIRST |

## Checked against the branch
No checker claim of class NOT ADDRESSED, BROKEN, WIDENED, NOT SHOWN, RELATED or NOT RED FIRST was made (both checkers gave the clean label to all six questions), so there is no such claim to walk. What I walked instead, in the real files, facts only:

| claim / fact | who | file:line | result | note |
|---|---|---|---|---|
| Opus's code-at-tip line citations `:117` (prep-or-build), `:745` (`cut_at`), `:754` / `:522` (the two WARNING lines), `:788` / `:790` (`formation_cut` into `render_line`, the pre-write `check_deadline`), `:819` (the end-of-run `raise`) | opus | `code-at-tip.md` (grep) | HOLDS | each cited line carries the named text |
| `MemberPrep` checks only `(membership_id, as_of)` (Opus reading 2; the build's ESCALATE 5) | opus | `src/cobalt/radar/evaluate.py:975` (worktree) | HOLDS | the guard compares `(prep.membership_id, prep.as_of) != (member.membership_id, member.as_of)`; nothing checks `tunables` / `defaults` / `clock` |
| A cut rerun "reconciles only the rows it evaluated, so it would retire earlier complete rows" (Opus reading 1) | opus | `src/cobalt/replay/runner.py:470–480` (worktree) | NOT CHECKABLE FROM READS — `missed.reconcile` (the store) is not in the packet; the runner's own comment says `reconcile` "retires every predecessor of this run"; run it against a store with earlier rows to settle | a reading the checker itself called "not a defect" (L70: never restated as one) |
| `job_result()["formation_cut"]` (Opus / Grok THIRD) | both | `tests/cobalt/test_replay_runner.py` (`diff.md` part 1) | asserted by T9 only; the body of `job_result()` is not in the packet | the builder's suite record says T9 passes; not re-run here |

Also stated by me, from the real files:
- **(i) L32:** I read this whole report once before the closing line. `no real-day ticker written` — the only tickers anywhere in the packet are the tests' synthetic fixture tickers, copied verbatim into `diff.md` / `suites.md` (and quoted once by Grok inside its own answer); none is written by me in this report.
- **(ii) One path and the stale-score seam.** In the tip's `evaluate_member` (`src/cobalt/radar/evaluate.py:974`): `prep = prep if prep is not None else prepare_member(member, tunables=tunables, defaults=defaults, clock=clock)` — `evaluate_member` without a `prep` reaches `prepare_member` (one path); `member_frames` (`:956`) also goes through `prepare_member(...).frames(False)`. The `intraday_stale` block at tip (`:1021–1026`: `if last_bar is None: intraday_stale = True` / `else:` / `intraday_stale = intraday_staleness(observed_at=last_bar.ts + timedelta(minutes=1), as_of=member.as_of, scan_interval=scan_interval).stale`) is the same five lines as `git -C /Users/cobalt/cobalt show a994a5dd:src/cobalt/radar/evaluate.py` lines 960–965 (Read of the saved output). It is byte-identical in text; only the lines around it changed (base `:957–959` built `series`, `run`, `params` above it; tip `:1019–1020` read `prep.run`, `prep.params` above it, and `:1027–1028` read `prep.daily_ok` and `prep.frames(...)` below it). Nothing inside the block changed.

## Ready for a deploy
| checker | CHECK REPLAY DEADLINE line | ready | reason (verbatim) |
|---|---|---|---|
| opus | `CHECK REPLAY DEADLINE: FIX STANDS · ready for a deploy prompt: YES` | YES | (the YES line carries no reason text) |
| grok | `CHECK REPLAY DEADLINE: FIX STANDS · ready for a deploy prompt: YES` | YES | (the YES line carries no reason text) |

## FOR THE CLASSIFIER
none

## ESCALATE
1. **L74:** one block arrived at the end of the Read tool result of the prompt file `58-replay-deadline-fix-check.md` (an attribution reminder asking for a `Claude-Session: …` line and naming a file-send tool). Recorded once under `## L74`; not followed. Nothing of the kind arrived from either checker.
2. **DEFECT REMAINS:** none, from either checker. **A checker that did not check:** none. **A checker that wrote a file it was not told to:** none (Grok wrote only `grok-check.md`, as told). **A packet mismatch:** none in what the checkers read. My first write of `diff.md` had errors that I found and corrected before any checker launched (see `## Packet`, "Staging note"). **`ASK DESK`:** none.
3. **The build's ESCALATE lines, verbatim (build report lines 202–212):**
   1. AUTHORIZATION: **timing: approved** (`cto-2026-09-25.md:26` R18, "approve command"). D0 raised no ESCALATE (06:05 ET, before 15:00; `main` == `<base>`).
   2. D1 interruption, recorded: one call off the launch list (`git -C /Users/cobalt/cobalt diff main...cards/stale-score-0922 -- …`) raised a permission box, which was cancelled. The desk resumed the run at D1 by message (06:43 ET) under the rule "only listed shapes". The seam was then read with `git diff main...cards/stale-score-0922 -- src/cobalt/radar/evaluate.py`. Nothing else ran off-list.
   3. D2 shareability: **frames shareable**, `anatomy/frame.py:105-114, :228-239, :245, :578-590, :625-627` read (see D2).
   4. Test edits outside "append at the end", each named for the check: (i) `test_replay_formations.py:385`, `test_formation_sources_name_every_argument_p2s_entrypoint_takes`: `cut_at` is added to the excluded per-run arguments (D1). (ii) `test_setups_d1.py` `ADDED_KEYS` and `test_setups_registries.py` `STEP3_KEYS` gain the one new row (D6 run 1: 5 reds; the D1 taxonomy clause applied in `tests/cobalt/`). No pin hash and no assertion changed.
   5. READING for the check, not built: `MemberPrep` checks only `(membership_id, as_of)`, as specified. It is correct only when every def sharing it uses the same `tunables` / `defaults` / `clock` as the prep. `replay_formations` guarantees that structurally (one `rows`), and the resident never passes a prep. A guard on those three would be a widening, not a FIX row.
   6. L74: one block arrived in a tool result (a `Claude-Session:` commit line plus a file-send tool). Recorded once under `## L74`, not followed.
   7. **FOR THE DEPLOY:** see `## FOR THE DEPLOY` (the `evaluate_member` seam with stale-score, the digest lists, the first live proof, the rollback shape).
   8. **THE MEASUREMENT:** `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)`. The check and the desk read it; this build produces no timing evidence. The structural guard is T2 (frame pairs built once per `bind_side`, not once per def).
4. **Opus's two "readings for the desk (not findings)"**, quoted: "A cut rerun that has a deadline reconciles only the rows it evaluated, so it would retire earlier complete rows for that day. The nightly first run has no earlier rows, and reruns started after the backup have no deadline." and "`MemberPrep` checks only `(membership_id, as_of)` (the build report's ESCALATE 5). Only `replay_formations` passes a prep, and it uses one tunables mapping for every def." My file-check: the second is walked (`evaluate.py:975`); the first is NOT CHECKABLE FROM READS (table above). Neither is a claim that HOLDS as a defect; `## FOR THE CLASSIFIER` stays `none`.
5. **The timing row is a measurement for the desk, not a finding (L70):** `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)` — nobody has a measured figure for FIX 1's effect on the 82,250-evaluation day; both checkers said only `NOT MEASURABLE ON cobalt_dev`. Opus adds, as a reading and not a finding, that the line lands only if the work after the cut (one scan already in flight, `formation_misses`, reconcile) fits inside the 120 s reserve; the pre-write check refuses the write if it does not.
6. **Standing line:** "Round 1 covers the replay deadline fix only (`a994a5dd..8b931ce5`) and its three suites' executed output and timing row, checked by Opus 5.5 + Grok under his 09-23 R95 (Sol METER; Gemini out, R96/R97). With both `ready … YES` and no claim that HOLDS, the branch is checked (L67) and rides the 2026-09-25 deploy's stacked set (L43 / L68) with stale-score + H1, else the next evening."
7. **Standing line:** "The deploy's L68 gate re-proves offline, with-DB and live-note on the stacked tree; the seam with `cards/stale-score-0922` is `evaluate_member`'s head (`intraday_stale`), `tests/cobalt/test_replay_runner.py` and `src/cobalt/replay/formations.py`; T1 and T2 re-run there are the proof. The first live proof is the 2026-09-25 21:10 replay ending DONE before 21:35:00 ET with the miss line in `DRC-2026-09-25.md`; a night that CUTS lands a PARTIAL line and ends FAILED — the design question the drafter listed, not a defect of this check."

REPLAY DEADLINE FIX CHECK DONE · round: 1 · opus: CHECK REPLAY DEADLINE: FIX STANDS · ready for a deploy prompt: YES · grok: CHECK REPLAY DEADLINE: FIX STANDS · ready for a deploy prompt: YES · ready for a deploy prompt: YES · ESCALATE: 14
