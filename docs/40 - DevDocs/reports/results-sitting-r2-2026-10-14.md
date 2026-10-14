# Results sitting, round 2 — the Grok row — 2026-10-14

## §0 Headline
- Cells closed 5 of 5, open 0, one house 0: Astra and the blind Opus seat (`RESULTS SITTING R2 OPUS DONE`) gave the SAME grade on every cell; Grok ruled all five apart (same five grades, SELF: yes). Floor MET (Astra UP, ruled all five; Opus seat done).
- Closing line of all three houses: `SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW`. Per band (lookup, not a routing rule): LOW Grok 378 CAN BUILD · Grok 365 WITH A REVIEW; MID Grok 368 CAN BUILD · Grok 379 WITH A REVIEW; HIGH Grok 371 NOT YET. Insufficient data (n=2/2/1).
- Self-vendor rulings counted: 0. REDACTIONS: 0. Opus-seat claims checked: 17 HOLD of 17 checked. House claims that DO NOT HOLD: 3 (all on how "open" or a duplicate is cited; no grade moves). Experiments named: 10 (E1–E10, none run by this hub). Owner items: 1 (Grok's, apart). ESCALATE: 5.
- Nothing routes by this sitting; routing takes effect only on his word (L29).

## AUTHORIZATION
Hub: Sonnet 5.5 (`claude-sonnet-5-5`), `results-sitting-r2-1014`. Each row below was its own Bash call, 2026-10-14 17:33–17:40 EDT.

| row | file:line | carries | committed (`git log -1 -S`) |
|---|---|---|---|
| R1069 | cto-2026-10-11.md:74 | `tribunal seats approved` | 2322ed1e |
| R1019 | cto-2026-10-11.md:123 | `can build every band` | df9a39ed |
| R1014 | cto-2026-10-11.md:128 | `ROUTING, not exclusion` | 9198f2f9 |
| R908 | cto-2026-10-10.md:104 | `ONE OpenAI seat at a time` | fcded711 |
| R109 | cto-2026-09-22.md:56 | `Make all Opus 5.5 for now` | 75b2aa57 |
| R17 | cto-2026-09-24.md:35 | `Grok approved with no asking going forward` (GROK GATE) | 1758fd78 |
| R19 | cto-2026-09-24.md:37 | `All 4 house models approved` (ASTRA GATE) | 5055151d |
| R1315 | cto-2026-10-13.md:152 | `Kept Grok builds 378, 368, 371, 379 may now be scored` | 692ff5ae |
| R1319 | cto-2026-10-13.md:148 | `Grok row n=2/2/1; sitting on it` | 760e8bf7 |
| R1350 | cto-2026-10-13.md:117 | `Grok row, sitting, routing table` | e0adf140 |
| R1451 | cto-2026-10-13.md:20 | (read; Grok 365 X1 record) | n/a |
| R1452 | cto-2026-10-13.md:19 | `Grok declines the X1 probe` | e250f052 |
| R1468 | cto-2026-10-14.md:16 | `sitting round 2 on the Grok row is his ruled plan` | 3b4c8a63 |
| launch row R1496 | cto-2026-10-14.md:36 | names `532-results-sitting-r2-tribunal.md` · `Fable seat: yes` · `grok read: ruled R1315` · `grok runs: 1 of 3` · `openai seat: free (no OpenAI session live)` | f435de77 |

INPUTS DONE AND COMMITTED: the five Grok checks' last line starts `CHECK DONE` (378 archiver-429-grok, 365 strike-fallback-env-1010-grok, 368 radar-display-fix-1008-grok, 379 worktree-salvage-grok, 371 s4-p1-1009-grok); `git log -1 -- <check>` non-empty for each (ed8587ab, 8b813ca7, 18fbb7d5, 8b813ca7, 8b813ca7); originals `archiver-429-check-2026-10-10.md` (2b243142) and `worktree-salvage-check-2026-10-07.md` (74b8bbce) committed; `complexity-shadow-results-2026-10-11.md` last non-blank line `TABLE DONE · rows: 11 · unknown: 21`. THE TWO PROMPTS: `532` and `533` both committed (c274c988).

THIS LAUNCH LINE ADDS NO RULE: `grep -c -F -e` of each of the thirteen allow strings and three deny strings (quotes included) against `427-results-sitting-tribunal.md` → 1 for every one (16 of 16). No `gpt-5.6-sol`, `gpt-5.6-terra`, `claude -p --model` or `Bash(agy *)` in this hub's launch line. The Anthropic seat is not launched by this hub.

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` | 0 | Wed Oct 14 17:33:13 EDT 2026 |
| 2 | R17 grep (GROK GATE) | 0 | carries `Grok approved with no asking going forward` — allowed |
| 3 | R19 grep (ASTRA GATE) | 0 | carries `All 4 house models approved` — allowed |
| 4 | STAGGER: launch row R1496 | 0 | `grok runs: 1 of 3` · `openai seat: free (no OpenAI session live)` — allowed |
| 5 | slug check `grep -c -F "gpt-6-astra" /Users/cobalt/.codex/models_cache.json` | 0 | `1` |
| 6 | CODEX PROBE `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK." < /dev/null` (background) | 0 | reply `OK`, 2,359 tokens — **astra: UP** |
| 7 | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 8 | `ls scratch/tribunal-bars-0920` | 0 | present |
| 9 | `ls scratch/tribunal-bars-0920/results-sitting/r2` | 1 | No such file or directory — fresh run |

THE FLOOR: Astra UP, Grok up; the Opus seat runs beside from `533`.

## Packet
Folder `scratch/tribunal-bars-0920/results-sitting/r2/` (under `/Users/cobalt/cobalt-wt/agy-trial/`, gitignored). Read from `/Users/cobalt/cobalt/` (main at `f435de77`), Read → Write; every source is committed (`git log -1 --format=%H -- <path>` per source, below). No file is split into parts; no cut was needed.

| file | bytes | source(s) |
|---|---|---|
| `00-READING-ORDER.md` | 2,618 | written last |
| `01-QUESTIONS.md` | 5,543 | 532 prompt text, verbatim, plus the "Files in this folder:" list |
| `02-greps.txt` | 31,425 | the searches of 532 §1, run by this hub, full output; hand-transcribed into the Write tool (see ESCALATE: a line-level mechanical comparison was possible only for the excerpt files, not this one) |
| `10-RESULTS-TABLE.md` | 8,701 | `reports/complexity-shadow-results-2026-10-11.md` WHOLE (8,442 B at source; 1 trailing-whitespace line, line 34 `Read: `, stripped by Write = 1 B) under the ordered header line |
| `11-STAGE-ANSWER.md` | 4,505 | `reports/bakeoff-results-stage-answer-2026-10-11.md` WHOLE (4,505 B, 0 trailing-whitespace lines, byte-identical size) |
| `12-shadow-hub.excerpt.md` | 3,587 | `prompts/SHADOW-HUB.md` :37-38, :72-103 (source 15,934 B; 0 trailing-whitespace lines) |
| `13-grok-LOW.excerpt.md` | 15,038 | C1 378 and C2 365 checks |
| `14-grok-MID.excerpt.md` | 10,491 | C3 368 and C4 379 checks |
| `15-grok-HIGH.excerpt.md` | 9,118 | C5 371 check |
| `18-baseline.excerpt.md` | 28,693 | the five originals |
| `19-rulings.md` | 3,646 | R1014, R1019, R1069 (cto-2026-10-11.md :128 :123 :74), R908 (cto-2026-10-10.md :104), R1315 :152, R1319 :148, R1350 :117, R1451 :20, R1452 :19 (cto-2026-10-13.md), R1468 (cto-2026-10-14.md :16) |
| `20-round1.excerpt.md` | 4,117 | `reports/results-sitting-2026-10-12.md` :3-7, :78-88, :103-108 |
| `27-laws-excerpt.md` | 13,710 | LAWS.md :130-131, :204-207, :215-219, :338-354, :363-364, :387-388 |
| **TOTAL** | **141,192** | MANDATORY (00,01,02,10,11,12,13,14,15,18,19) 123,365 B; under the 200,000 B ceiling |

Excerpt bounds (found with `grep -n -e "^## " -e "^CHECK DONE"`; each anchor is the heading at the stated line): `§0` = `## §0 Headline` to the line before `## L74`; `HELD` = `## OWN FINDINGS` to the line before `## Dropped`; `STOP` = the `CHECK DONE` line.
- 378 archiver-429-grok-check: §0 :3-9 · HELD :121-267 · STOP :381. 365 strike-fallback-env-1010-grok-check: §0 :3-8 · HELD :89-130 · STOP :226.
- 368 radar-display-fix-1008-grok-check: §0 :3-8 · HELD :98-152 · STOP :254. 379 worktree-salvage-grok-check: §0 :3-8 · HELD :104-142 · STOP :216.
- 371 s4-p1-1009-grok-check: §0 :3-7 · HELD :144-255 · STOP :351.
- Originals: archiver-429-check-2026-10-10: §0 :3-9 · HELD :108-161 · STOP :258. strike-fallback-env-check-2026-10-10: §0 :3-7 · HELD :98-130 · STOP :223. radar-display-fix-check-2026-10-08: §0 :3-7 · HELD :93-149 · STOP :246. worktree-salvage-check-2026-10-07: §0 :3-7 · HELD :92-136 · STOP :213. s4-p1-check-2026-10-09: §0 :3-8 · HELD :71-146 · STOP :279.

Verification of the excerpt copies: `grep -n -v -x -F -f <source> <staged>` (fixed-string, whole-line) printed, for every excerpt/whole file (10, 11, 12, 13, 14, 15, 18, 19, 20, 27), only my own header lines, blank lines and (for 10) the `Read:` line whose trailing space Write stripped — every content line of every staged excerpt exists verbatim in its source. For `02-greps.txt` that check does not apply (its lines carry the grep line-number prefixes); I compared it by eye line by line against the tool output and corrected 6 transcription errors found that way (a wrong finding count, two altered log-path fragments, a garbled sentence, a dropped sentence, a wrong `git log` line) BEFORE any house saw it; a residual transcription error elsewhere in `02-` cannot be excluded.

Per-source `git log -1`: all sources are on main; the check reports resolved in AUTHORIZATION above; `SHADOW-HUB.md`, `results-sitting-2026-10-12.md`, `bakeoff-results-stage-answer-2026-10-11.md` and `complexity-shadow-results-2026-10-11.md` read from main without uncommitted changes (`git status` of the main checkout was not run by this hub: no git write or status tool beyond `log`/`show` is in its approved line).

REDACTION (`73` §1's `grep -c -E "TSLA|372[.]82|374[.]50"` on every staged file): 00 …; 01 0 · 02 0 · 10 0 · 11 0 · 12 0 · 13 0 · 14 0 · 15 0 · 18 0 · 19 0 · 20 0 · 27 0 (00 is checked after its write, below). Any other ticker, price, share count, P&L or config value of his: none found (the tickers in the staged tests are synthetic `TESTARCH`, `ZZD1`, `ZZD2`, `ZZD7`, `ZZMA`, `AAA`). REDACTIONS: 0.

NOT STAGED: any daily-note text, `Rules.md`, any note of his, any vault or production row; the build reports beyond `02-greps.txt`; the check reports beyond the ranges; `ops/grok-sandbox.toml`.

Hub slips recorded: twice I issued a `Write` to a path outside the sitting folder (`/Users/cobalt-wt/placeholder-never-used` and `…-2`) by mistake; both were refused (`EACCES: permission denied, mkdir '/Users/cobalt-wt'`) and wrote nothing.

## CONTINUE
Both houses are finished and captured (astra 17:45, grok 17:49); the Opus seat report is read. next: none — the report is complete at the stop line below. (Both houses finished inside 20 minutes: astra 3 min, grok 7 min; no house is running.)

## Clock
| time | trigger | action |
|---|---|---|
| 17:33:13 | PREFLIGHT row 1 | start |
| 17:41:51 | packet staged | `date` after `00-READING-ORDER.md` |
| 17:42:27 | pre-launch | `date`, R17, R19 and the launch row (R1496: grok runs 1 of 3, openai seat free) re-run: all pass |
| 17:42:36 | launch | GROK (`b5kl66973`) and ASTRA (`binajmyv2`) launched together in one message, `run_in_background`, one attempt each; launched ≈ 17:42:30; 20-minute deadline ≈ 18:02:30 |
| 17:46:02 | astra completion notice | astra 3 min, exit 0, ruled all five; grok 3.5 min in, still running; `astra-ruling.md` written |
| 17:49:41 | grok completion notice | grok ≈ 7 min (launched ≈17:42:30), exit 0; it wrote `grok-ruling.md` itself (14,798 B), ends `SITTING: …`; within the 20-minute deadline, no TIMEOUT |
| 17:49:48 | collate step: Independence | `grep -c -F -e "-ruling"` on both ruling files |
| 17:50:11 | collate step: file-check | git log / reads of the real files |
| 17:51:23 | collate step: Opus-seat report | `tail -n 3` of its report: last non-blank line starts `RESULTS SITTING R2 OPUS DONE ` (read at 17:49:48 after both houses had finished); claims checked FC1–FC17 |
| 17:53:16 | close | `date` before replacing the in-progress last line with the stop line |

## Cells table
SELF = each house's own mark. Grok marked all five `yes` (own vendor, APART, counted on no cell); Astra and the Opus seat marked all five `no`. Counted houses on every cell: Astra + the Opus seat. RESULT by lookup only; Grok's grade never moves a RESULT.

| cell | band · card | grok (APART, not counted) | astra | opus | SELF g/a/o | result | reason ≤25 words per house |
|---|---|---|---|---|---|---|---|
| C1 | LOW · 378 archiver-429 | AT LEVEL | AT LEVEL | AT LEVEL | yes/no/no | **CLOSED AT LEVEL** | Astra: opus-own 1 vs 1, extra 0. Opus: derived original 1 (O1; A4 same defect, Sol), extra 0. Grok: same. |
| C2 | LOW · 365 strike-fallback-env-1010 | CLOSE BELOW | CLOSE BELOW | CLOSE BELOW | yes/no/no | **CLOSED CLOSE BELOW** | Astra: opus-own 2 vs 1, extra 1. Opus: same; both test gaps, distinct rows A and B. Grok: same. |
| C3 | MID · 368 radar-display-fix-1008 | AT LEVEL | AT LEVEL | AT LEVEL | yes/no/no | **CLOSED AT LEVEL** | Astra: shadow opus-own 0 vs original 2, G2 Grok's, excluded. Opus: same, G2 = original's O1 defect, uncounted. Grok: same. |
| C4 | MID · 379 worktree-salvage | CLOSE BELOW | CLOSE BELOW | CLOSE BELOW | yes/no/no | **CLOSED CLOSE BELOW** | Astra: opus-own 3 vs derived 2, extra 1. Opus: same; shadow O1 = original O1 defect. Grok: same. |
| C5 | HIGH · 371 s4-p1-1009 | BELOW | BELOW | BELOW | yes/no/no | **CLOSED BELOW** | Astra: opus-own 4 vs 2, extra 2; red was one test, cleared by one S2 re-pass (cap 2). Opus: same. Grok: same. |
| closing line | | `SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW` | `SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW` | `SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW` (its report's last line: `RESULTS SITTING R2 OPUS DONE · SITTING: … · apart: none · withdrawn: 0 · ESCALATE: 0`) | | | |

Opus verdict words are copied from its `## Grades`; it marked `STAKE: yes` on every cell (the baseline is its own model's work) and `SELF: no`.

## Self-vendor, recorded apart
GROK — OWN VENDOR, APART, NOT COUNTED (brain §3). The five rulings below are Grok's file `scratch/tribunal-bars-0920/results-sitting/r2/grok-ruling.md` as written by Grok (14,798 B; Grok wrote it itself through its allow string; line-number citations in it refer to the staged packet files). Never summed; `self-vendor rulings counted: 0`. Verdicts and reasoning copied UNEDITED. The file's remaining sections (THE FACT BASE table, EXPERIMENTS, OWNER, WRONG FACTS) live whole in the ruling file; the claims in them are file-checked and quoted where they bear, under the sections below.

### C1 — Grok LOW 378 archiver-429 — AT LEVEL
Shadow Opus-own held 1 (`13-grok-LOW.excerpt.md:162`: `held: 1 (opus-own 1 · house 0)`; the one held is O1, decimal `Retry-After: 7.5` accepted, `13-grok-LOW.excerpt.md:17-30`). Original prints `held: 5` with no opus-own split (`18-baseline.excerpt.md:71`). Derived Opus-own held 1: of the five held, O1 is Opus and A4 is Sol on that same overflow (`18-baseline.excerpt.md:7`, `:63`); A3 is Sol (`:62`); B1 and B2 are Grok (`:66-67`). O2, A1, A2 are open, not held (`18-baseline.excerpt.md:11`). extra = 1 − 1 = 0.
The two O1s are not one defect: original O1 is an all-digit value too large for a float (`18-baseline.excerpt.md:20-21`); shadow O1 is a decimal the row maps to `None` (`13-grok-LOW.excerpt.md:19`). One Opus-own each, so the count does not collapse. Build `suites at first run: green`, passes 2 (`02-greps.txt:69`). No red.
SELF: yes

### C2 — Grok LOW 365 strike-fallback-env-1010 — CLOSE BELOW
Shadow Opus-own held 2 (`13-grok-LOW.excerpt.md:218`: `held: 2 (opus-own 2 · house 0)`; O1 and O2, `13-grok-LOW.excerpt.md:167`). Original Opus-own held 1: the round-1 LOW baseline (`12-shadow-hub.excerpt.md:10`) and the check, whose one held finding is O1, Opus (`18-baseline.excerpt.md:76`, `:111`, `:117` `held: 1`); A1 Sol is open, not held (`18-baseline.excerpt.md:77`, `:112`). extra = 2 − 1 = 1.
O1 and O2 are distinct. O1 is row A, `override` stays `False`, unpinned at `__main__.py:30` (`13-grok-LOW.excerpt.md:177-181`; mutation stayed green, `02-greps.txt:20`). O2 is row B, `elapsed >= REPEAT_ERROR_S` unpinned at `strike.py:560` (`13-grok-LOW.excerpt.md:183-187`; mutation stayed green, `02-greps.txt:21`). H1 is Grok and rejected, not held (`13-grok-LOW.excerpt.md:168`, `:213`). First run green, passes 2 (`02-greps.txt:72`). X1 was not run and is not scored (`02-greps.txt:115`, `19-rulings.md:28`).
SELF: yes

### C3 — Grok MID 368 radar-display-fix-1008 — AT LEVEL
Shadow Opus-own held 0 (`14-grok-MID.excerpt.md:6`, `:69`: `held: 1 (opus-own 0 · house 1) · grok-own 1`). The one held finding is G2, Grok’s (`14-grok-MID.excerpt.md:64`); it counts toward nothing. Original Opus-own held 2: the round-1 MID baseline (`12-shadow-hub.excerpt.md:10`). The check held 3 (`18-baseline.excerpt.md:187`): O1 and O2 are Opus (`18-baseline.excerpt.md:178-179`); A3 is Sol (`:184`); O3, A1, A2 are open (`18-baseline.excerpt.md:123`). extra = 0 − 2 = −2. No extra held.
O1 and O2 are distinct defects of one test, matching the baseline’s distinct count of 2: O1 moves the banner out of the branch (`18-baseline.excerpt.md:133-137`); O2 widens the threshold to `3*interval*1000` (`18-baseline.excerpt.md:147-151`). Shadow O1–O3 are rejected, not held (`14-grok-MID.excerpt.md:7`, `02-greps.txt:27-29`). First run green, passes 2 (`02-greps.txt:75`).
SELF: yes

### C4 — Grok MID 379 worktree-salvage — CLOSE BELOW
Shadow Opus-own held 3 (`14-grok-MID.excerpt.md:122`: `held: 3 (opus-own 3 · house 0)`; O1, O2, O3, `14-grok-MID.excerpt.md:75`). Original prints `held: 4` with no split (`18-baseline.excerpt.md:244`). Derived Opus-own held 2: the four held are O1 Opus, O2 Opus, A1 Sol, A2 Sol (`18-baseline.excerpt.md:193`). A3 is Sol, B1 and B2 are Grok, and none of those three is in the held list (`18-baseline.excerpt.md:237-241` against `:193`). extra = 3 − 2 = 1.
Shadow O1 and original O1 are one defect (an untracked file is deleted when `status.showUntrackedFiles=no`: `18-baseline.excerpt.md:203` and `14-grok-MID.excerpt.md:86`). That identity does not change 3 − 2. The other four are distinct: original O2 is a skip-worktree edit lost (`18-baseline.excerpt.md:219`); shadow O2 is the W3 `.env` report-order gap (`14-grok-MID.excerpt.md:102`); shadow O3 is the W1 `main` refusal with no empty-stdout pin (`14-grok-MID.excerpt.md:108`). Grok’s A1 did not hold (`14-grok-MID.excerpt.md:76`). Build first run green, passes 2, tip `b43b85fe` (`02-greps.txt:78`). The `tests/ops` 1 failure is the check’s own O1 test, committed red at `0a046551` (`14-grok-MID.excerpt.md:78`), not a model red after the cap and not a harness red. Ancestry of `0a046551` over `b43b85fe` is UNVERIFIED — `02-greps.txt` §6 logs only `main`.
SELF: yes

### C5 — Grok HIGH 371 s4-p1-1009 — BELOW
Shadow Opus-own held 4 (`15-grok-HIGH.excerpt.md:125`: `held: 6 (opus-own 4 · house 2; grok-own 2)`). The 4 are O1–O4 (`15-grok-HIGH.excerpt.md:6`). House 2 and grok-own 2 are the same two, H2 and H3 (`02-greps.txt:45`); they count toward nothing. Original Opus-own held 2: the round-1 HIGH baseline (`12-shadow-hub.excerpt.md:10`). The check held 4 (`18-baseline.excerpt.md:335`) because each of two defects was found by Opus and by Sol (`18-baseline.excerpt.md:251`). extra = 4 − 2 = 2.
Original pairs are one defect each, so Opus-own stays 2, not 4: O1 (`18-baseline.excerpt.md:262-263`) and Sol A3 (`:325`) are the extra full-interval sleep; O3 (`18-baseline.excerpt.md:293`) and Sol A2 (`:324`) are the tick-start clock. Shadow O1–O4 are four defects: refusals unlogged (`15-grok-HIGH.excerpt.md:16`), a failed build ends the strike thread (`:44`), the MISSED sweep counts a post-close bar (`:74`), a token `CollectorError` writes no summary (`:92`). First-run red is the model’s own `test_lag_rows_equal_hand_computed_values` (`02-greps.txt:88`, `:96`), not the lock, the DB level, or `.env`. One S2 cleared it; passes 3 means T, S, and one S2 (`02-greps.txt:87`, `:101`); the cap is 2 (`12-shadow-hub.excerpt.md:2`). Scored gate is green (`02-greps.txt:88`, `:107`). The residual-red BELOW trigger does not fire. BELOW is the extra of 2.
SELF: yes

Grok's closing text (after its SITTING line, in its file's last paragraph as printed to stdout): "Opus-own extra is 0, 1, −2, 1, and 2. Grok’s own findings are not in those counts. C5’s first-run red was the model’s lag-rows test and was green after one re-pass, so the BELOW grade is the extra of 2, not a leftover red. One owner head remains: L27, named in the stage answer and not in this packet." (stdout of task `b5kl66973`, not a line of `grok-ruling.md`.)

## Per band
Lookup of SHADOW-HUB :90-93 (`CLOSED AT LEVEL` → CAN BUILD · `CLOSED CLOSE BELOW` → WITH A REVIEW · `CLOSED BELOW` → NOT YET). Exactly these lines:
- `LOW — Grok (378): CAN BUILD · Grok (365): WITH A REVIEW · insufficient data (n=2 per band)`
- `MID — Grok (368): CAN BUILD · Grok (379): WITH A REVIEW · insufficient data (n=2 per band)`
- `HIGH — Grok (371): NOT YET · insufficient data (n=1 per band)`
- `Grok declined X1 (R1451, R1452): stated, not scored. Sonnet and Terra: round 1, closed (results-sitting-2026-10-12.md). Opus 5.5, Sol: can build (his word R1019, not measured).`
- `An indication for his word, not a routing rule: the desk writes the routing table from these grades; routing takes effect only on his word (L29).`

## Wording offered, verbatim
This sitting offers no wording to fold: neither counted house proposed a replacement text (the question set asks for grades, a fact base, experiments, an owner line and wrong facts). The three SITTING lines are in `## Cells table`; each house's experiments are quoted whole under `## Experiments named (L70)`.

## Checked against the files
Real files opened under `/Users/cobalt/cobalt/` (and `git -C /Users/cobalt/cobalt log/show` for shadow-branch commits). `claim · who · file:line · verdict · note`. Houses: G = Grok (apart), A = Astra, O = Opus seat.

| # | claim | who | file:line | verdict | note |
|---|---|---|---|---|---|
| CH1 | original archiver-429 held = 5: O1 (Opus), A4 (Sol, "same defect as O1"), A3 (Sol), B1, B2 (Grok); Opus-own 1 | G, A, O | `archiver-429-check-2026-10-10.md:168,172,173,175,176,258` | HOLDS | ARITHMETIC OK: extra = 1 − 1 = 0 |
| CH2 | original strike-fallback-env Opus-own 1 (O1 HELD); Sol A1 REJECTED/open; Grok none | G, A, O | `strike-fallback-env-check-2026-10-10.md:137,138,223` | HOLDS | ARITHMETIC OK: 2 − 1 = 1 |
| CH3 | shadow 365 held 2 = O1 (row A, `override`) + O2 (row B, 60 s boundary): distinct defects | G, A, O | `strike-fallback-env-1010-grok-check-2026-10-11.md:94,100,137,138,226` | HOLDS | different rows, files and clauses |
| CH4 | original radar-display-fix held 3: O1, O2 Opus; A3 Sol; Opus-own 2 | G, A, O | `radar-display-fix-check-2026-10-08.md:158,159,163,246` | HOLDS | |
| CH5 | shadow 368 opus-own 0; held G2 is Grok's; O1–O3 REJECTED | G, A, O | `radar-display-fix-1008-grok-check-2026-10-11.md:160-164,254` | HOLDS | ARITHMETIC OK: 0 − 2 = −2 (no extra) |
| CH6 | original worktree-salvage held 4: O1, O2 Opus; A1, A2 Sol; A3, B2 REJECTED, B1 NOT HELD; Opus-own 2 | G, A, O | `worktree-salvage-check-2026-10-07.md:144-150,213` | HOLDS | ARITHMETIC OK: 3 − 2 = 1 |
| CH7 | shadow 379 held 3 = O1, O2, O3 (opus-own 3) | G, A, O | `worktree-salvage-grok-check-2026-10-11.md:149-151,216` | HOLDS | |
| CH8 | shadow 379 O1 is the same defect as the original's O1 (`status --porcelain` blind to untracked files under `showUntrackedFiles=no`) | G, O | original `:97,:144`; shadow `:5,:149` | HOLDS | does not change 3 − 2 |
| CH9 | 379's check tip `0a046551` is the check's own red-test commit on top of the build `b43b85fe` (history `0a046551` ← `34edea9d` build report ← `b43b85fe`) | A, O (G: UNVERIFIED) | `git log -4 0a046551` → `0a046551 2026-10-13 20:51:46 wip(…): check red — O1` · `34edea9d 15:53:44 docs(…): build report — b43b85fe` · `b43b85fe 15:40:48 feat(…): rows` | HOLDS | settles Grok's "ancestry UNVERIFIED"; the `git diff --stat` between them was not run (its commit messages name only a docs commit and a test commit) |
| CH10 | original s4-p1 held 4 = two defects each found twice: O1/A3 (loop waits interval + tick), O3/A2 (`seen_at` tick start); Opus-own 2 | G, A, O | `s4-p1-check-2026-10-09.md:155,156,157,158,279` | HOLDS | ARITHMETIC OK: 4 − 2 = 2 |
| CH11 | astra's cite for the duplicates, `s4-p1-check-2026-10-09.md:135-141` | A | `:135-141` is the findings table (O1, O3, A1…A5, B1…B4); the "same defect" text is at `:156,:158` | DOES NOT HOLD as cited (:135-141) — substance HOLDS at :156,:158 | no grade moves |
| CH12 | shadow 371 held 6 = opus-own 4 (O1–O4) + grok-own 2 (H2, H3); open 8 = 6 held-unfixed + H1, H4 | G, A, O | `s4-p1-1009-grok-check-2026-10-11.md:264-267,269-270,324-326,351` | HOLDS | |
| CH13 | 371 first-run red = one test (`test_lag_rows_equal_hand_computed_values`, `tests/cobalt/test_strike_measure.py:111` AssertionError) in the builder's own code/test, not the lock, the dev DB level or `.env`; cleared by ONE S2 re-pass; passes 3 (T, S, S2) | G, A, O | build report `:5,:84,:160,:184` (via `02-greps.txt`) | HOLDS | the red is an assertion in a test file; no lock/DB/`.env` text is attached to it; cap is 2 (`SHADOW-HUB.md:37`) |
| CH14 | 371 with-DB 4804 + 197 = 5001 | A | build report `:154` (lines :1096, :1904 of its log) | ARITHMETIC OK | 4804 + 197 = 5001 |
| CH15 | 379 `tests/ops` 1507 passed + 1 failed, the failure being O1's test | A, G | `worktree-salvage-grok-check-2026-10-11.md:7` | HOLDS | 1507 + 1 = 1508 ARITHMETIC OK |
| CH16 | 368 "open 5 matches six findings minus held G2" | A | `radar-display-fix-1008-grok-check-2026-10-11.md:229-233` | DOES NOT HOLD (as membership) | OPEN lists O1, O2, O3, G2, G3 = 5: G2 is IN it and G1 (not held, dropped) is not; the count 5 is as printed |
| CH17 | 368 "Findings 6 = held 1 + open 5" | G | same | DOES NOT HOLD (as stated) | 1 + 5 = 6 ARITHMETIC OK, but G2 is in both lists and G1 in neither |
| CH18 | open counts of the other cells (378 open 1 = O1; 379 open 3 = O1–O3; 365 open 1 = H1 only) | G, A, O | `archiver-429-grok-check…:357`; `worktree-salvage-grok-check…:192-194`; `strike-fallback-env-1010-grok-check…:204-207` | HOLDS as printed | `## OPEN` of 365 also lists O1, O2 (held) and a follow-up: the reports count "open" differently (O's FC15) |
| CH19 | R908 states no numeric cap of three Grok sessions; `11-STAGE-ANSWER.md:21` attributes one to it | A | `cto-2026-10-10.md:104` (R908: "several Grok sessions may run at the same time"); R1350 `cto-2026-10-13.md:117` "cap 3" | HOLDS | |
| CH20 | R1451 says `grok -p` stops after its first message; R1452 says the command is not broken, Grok declines the probe | A | `cto-2026-10-13.md:20`, `:19` | HOLDS | |
| CH21 | "Grok read" still shown as his open word at `11-STAGE-ANSWER.md:40`; R1315 settled it | G, A | `11-STAGE-ANSWER.md` §4; `cto-2026-10-13.md:152` | HOLDS | |
| CH22 | the staged `10-RESULTS-TABLE.md` carries 379 in the LOW cell of the Grok row; this sitting has C4 as MID | A | staged `10-RESULTS-TABLE.md` Grok row; `draft-grok-second-cards-2026-10-11.md:5` ("MID: `worktree-salvage` … score 4 → card 379") | HOLDS | |
| CH23 | the failed Gemini probe is not a build-gate failure (365) | A | `strike-fallback-env-1010-grok-check-2026-10-11.md:4,59-61` | HOLDS | |
| CH24 | 378 band = LOW (score 1 by card fields, 2 by RESTARTS) | O | `draft-grok-second-cards-2026-10-11.md:4` | HOLDS | |
| CH25 | Opus-own shadow 378 = 1 and the build report passes 2 / first run green | G, A, O | `archiver-429-grok-check…:381`; build report `:197` | HOLDS | |

Claims that HOLD (rows HOLDS): CH1 CH2 CH3 CH4 CH5 CH6 CH7 CH8 CH9 CH10 CH12 CH13 CH15 CH18 CH19 CH20 CH21 CH22 CH23 CH24 CH25 = 21; ARITHMETIC OK rows: CH14 (and the arithmetic noted in CH1, CH2, CH5, CH6, CH10, CH15, CH17). DOES NOT HOLD: CH11, CH16, CH17 = 3. Not settled by reads: the suite totals and pass ledgers of C1–C4 (the staged excerpts and `02-greps.txt` repeat the CHECK DONE / SHADOW BUILT lines; they match those lines — an independent rerun is an EXPERIMENT, not a read).

## Opus-seat claims, file-checked
Its report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/results-sitting-r2-opus-2026-10-14.md`; read after both houses had finished and `## Cells table` was written (no Opus text reached a house). `tail -n 3`: last non-blank line `RESULTS SITTING R2 OPUS DONE · SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW · apart: none · withdrawn: 0 · ESCALATE: 0`. Read: `## Grades`, `## Self-attack`, `## WRONG FACTS`.

| # | claim (Opus report line) | file:line | verdict | note |
|---|---|---|---|---|
| FC1 | archiver original: five held, O1 Opus, A4 Sol "same defect as O1", A3 Sol, B1 Grok, B2 Grok (:19) | `archiver-429-check-2026-10-10.md:168-176` | HOLDS | |
| FC2 | worktree original: four held O1, O2 Opus; A1, A2 Sol (:46) | `worktree-salvage-check-2026-10-07.md:144-147` | HOLDS | |
| FC3 | s4-p1 original O1 :155, A3 :156 same defect; O3 :157, A2 :158 same defect (:55) | `s4-p1-check-2026-10-09.md:155-158` | HOLDS | |
| FC4 | radar original O1, O2 HELD :158-159; Sol A3 HELD :163 (:37) | `radar-display-fix-check-2026-10-08.md:158,159,163` | HOLDS | |
| FC5 | strike original O1 HELD :137; Sol A1 REJECTED :138 (:28) | `strike-fallback-env-check-2026-10-10.md:137,138` | HOLDS | |
| FC6 | `0a046551` → `34edea9d` (build report) → `b43b85fe` (:49, :79) | `git log -4 0a046551` | HOLDS | |
| FC7 | R1452 (16:15 ET) says 365 "relaunches into pass T"; the scored build commits are `b8418447 2026-10-13 15:44:31` (red) and `ca850d5f 15:47:49` (rows), the build-report commit `6cb30071 16:19:46` (:125) | `git log -3 6cb30071`; `cto-2026-10-13.md:19` | HOLDS (the times); its inference (the row's time vs the relaunch it names) is UNVERIFIABLE FROM READS | the Opus seat marks it "does not change a grade" |
| FC8 | original tip `71d34bd9`: `test_salvage_a_tree_on_main_is_refused` asserts `done.stdout == ""`, `REFUSED` (:48) | `git show 71d34bd9:tests/ops/test_gate_clean.py:431-440` | HOLDS | |
| FC9 | original `_salvage_refused_after_report` (:366-377, stdout starts `INSPECT: worktree`) and the `.env` case (:609-619) (:48) | same file `:366-378,:609-619` | HOLDS | |
| FC10 | `skip-worktree` occurs 0 times in the Grok 379 check (:50, :104) | `worktree-salvage-grok-check-2026-10-11.md` (`grep -n -F`) → no output | HOLDS | |
| FC11 | the Sonnet arm's check held the SAME `override` gap (:32, :100) | `strike-fallback-env-1010-sonnet-check-2026-10-11.md:192` (O1 HELD, `override=True` leaves A1/A2 green) | HOLDS | |
| FC12 | the original strike test file has no `override` (:32) | `git show f47ad2f0:tests/cobalt/test_strike_fallback_env.py` read whole: its fake `load_dotenv(*args, **kwargs)` records the path and never names `override` | HOLDS | its sibling claim about `60.0` / `REPEAT_ERROR_S` in `test_strike_fallback.py` at that tip was NOT re-run by this hub: UNCHECKED, not HOLDS |
| FC13 | bands 378 LOW, 379 MID (:85) | `draft-grok-second-cards-2026-10-11.md:4-5` | HOLDS | |
| FC14 | the original s4-p1 check considered `session_close` only for intrabar and found no breach (:59) | `s4-p1-check-2026-10-09.md:127` | HOLDS | |
| FC15 | open counts: the reports count held-unfixed items as open in C1 (:357), C4 (:192-194), C5 (:326) and in C3's OPEN (:229-233), but C2's `## OPEN` (:204-207) lists H1, O1, O2 and a follow-up while its CHECK DONE prints `open: 1` (:70) | the five Grok checks as cited | HOLDS | the printed `open: 1` = H1 only; no grade moves |
| FC16 | 368: O1–O3 REJECTED, G2 HELD and the same defect as the original's O1 (:36, :39) | `radar-display-fix-1008-grok-check…:160-164`; original `:98` | HOLDS | G2 = banner-write-leaves-branch test stays green; original O1 = same clause |
| FC17 | 378: open 1 = O1 (:66) | `archiver-429-grok-check…:357-358` | HOLDS | |

Opus-seat claims checked: **17 HOLD of 17 checked**; one sibling claim (FC12's `60.0` / `REPEAT_ERROR_S` read at `f47ad2f0`) UNCHECKED. Withdrawn by the seat: 0. Its X1–X6 are listed under `## Experiments named (L70)`.

## Experiments named (L70)
`experiment · named by · = packet item · what it gates · result that would change a grade`. None was run by this hub (it runs nothing); all are EXPERIMENTS, never grades.

| id | what to run (dev, scratch worktree) | named by | gates | result that would change a grade |
|---|---|---|---|---|
| E1 | 365 at `ca850d5f`: the recovery-reset mutation, original B tests and the check's O3 test separately | Astra X1 | C2 | a fresh check establishing an additional distinct in-scope held defect → Opus-own 3, extra 2 → C2 BELOW |
| E2 | 379: reproduce O1; isolate the O2/O3 test mutations | Astra X2 | C4 | one held finding disproved → shadow 2, extra 0 → C4 AT LEVEL |
| E3 | 371 at `ed512d5f`: reproduce O1–O4 independently, including O3's prerequisite (a WATCH card left open after the close) | Astra X3 | C5 | one distinct held finding disproved → extra 1 → C5 CLOSE BELOW |
| E4 | 379: `git merge-base --is-ancestor b43b85fe 0a046551` and `git diff --stat b43b85fe 0a046551` | Grok X1 (apart) | C4 | not an ancestor, or the range changes `job-clean.sh` beyond the red test → C4 re-opens on `b43b85fe`; the ancestry half is answered by CH9 (HOLDS), the diff half not run |
| E5 | 378 at `3e60d5f6`: run the original's held test `test_check_o1_a_huge_retry_after_is_still_a_typed_rate_limit` (`archiver-429-check-2026-10-10.md:116-120`) | Opus X1 | C1 | red → the build carries the original's defect unheld; the count moves to 2 vs 1 only if the sitting admits a held finding the shadow check did not run |
| E6 | 365's original tip `f47ad2f0`: apply the shadow check's two mutations (`override=True`; `>` for `>=` at `REPEAT_ERROR_S`), run A1, A2, B1–B5 | Opus X2 | C2 (and the baseline) | green under both → the original has the same two gaps (FC12 shows no `override` in its test file): C2's extra measures the check seat, not the build; changes the grade only on a re-count of the baseline |
| E7 | 368 at `ff0f2e0f`: run the original's O2 test `test_the_stale_line_test_fails_when_the_threshold_is_widened` | Opus X3 | C3 | red → a second original defect is in the Grok build; moves C3 only if counted |
| E8 | 379 at `b43b85fe`: run the original's O2 test `test_salvage_saves_an_edit_hidden_by_skip_worktree` | Opus X4 | C4 | red → Grok build has 4 defects vs 2: BELOW if counted |
| E9 | 371: the shadow's O1–O4 tests at `444e32b5` (the original's tip); the original's O1 and O3 tests at `ed512d5f` | Opus X5 | C5 | two or more red on the original → C5 moves toward CLOSE BELOW or AT LEVEL on a re-count |
| E10 | 365 at `ca850d5f`: the original's O1 test `test_o1_a_pass_whose_exception_cannot_be_printed_never_stops_the_thread` | Opus X6 | C2 | red → C2 carries 3 defects vs 1: BELOW if counted |

## OWNER ITEMS
- Astra: `none` (its text: the remaining questions are technical; his routing word is reserved as ruled). Opus seat: `none` (no head passes the owner test; X1–X6 are runnable). Grok (APART): `L27 — 11-STAGE-ANSWER.md:40 still names it as his open word beside the routing table; 27-laws-excerpt.md:9 only points at it … this packet does not contain L27, so no house can say what it requires. The routing word is already his and is not an owner item here.` — head claimed: NOT NAMED (it says the packet lacks L27; it names none of his money / data / laws / trading judgement as the reason no house can decide it). It is not made a precondition to anything.
- The stage answer's own statement (`11-STAGE-ANSWER.md` §4) lists "Grok read" and "L27" as his two open words; "Grok read" is settled by R1315. Owner items: **1** (Grok's, apart).

## WRONG FACTS claimed
| claim | who | file-check |
|---|---|---|
| `10-RESULTS-TABLE.md` Grok row (365/371/379 INCOMPLETE, no stop line or check; 378/368 UNSCORED; "X1 FAILED 365") is contradicted by the later checks and R1315 | G, A | HOLDS — the table is headed as predating the rebuilds; `13-` :218, `14-` :122, `15-` :125 and R1315 (`19-rulings.md`) carry the later facts; not a wrong fact of the table when written |
| `10-` :20 places 379 in the LOW column; this sitting has it MID | A, G | HOLDS (CH22) |
| the blanket `insufficient data (n=1 per band)` is superseded by n=2/2/1 (R1319) | A, G | HOLDS — `cto-2026-10-13.md:148` |
| `11-STAGE-ANSWER.md:40,43` "Grok read" still open | G, A | HOLDS (CH21) |
| `11-STAGE-ANSWER.md:21` attributes the three-Grok cap to R908 | A | HOLDS (CH19) |
| R1451's "`grok -p` stops after its first message" corrected by R1452 | A | HOLDS (CH20) |
| R1452's "365 relaunches into pass T" vs the 365 commits at 15:44:31 and 15:47:49 | O | HOLDS as to the times (FC7); inference UNVERIFIABLE FROM READS |
| `10-` :12 baseline 1 / 2 / 2 is not wrong (matches C2, C3, C5; derived C1 = 1, C4 = 2) | G | HOLDS |
No claimed wrong fact moves a grade.

## Independence
- `grep -c -F -e "-ruling"` on `grok-ruling.md` → 6; on `astra-ruling.md` → 5. Every matching line (read with `grep -n`) is a citation of the packet file `19-rulings.md` (the pattern `-ruling` matches `-rulings.md`); none opens, names or quotes another house's `*-ruling.md` file. No `READ ANOTHER RULING`. `astra-ruling.partial.md` does not exist. The Opus seat is blind by launch (its report line 1 and its NOT-opened list at :140); its report names no file of this sitting's folder. No breach.

## L74
none. (No tool result in this run carried a block asking for a `Claude-Session` line or naming a file-send tool; the Opus seat's report and the Grok 365 check each record such a block once in their own `## L74` — theirs, not repeated here.)

## ESCALATE
1. OWNER ITEM, apart: Grok's L27 line (`## OWNER ITEMS`): head NOT NAMED against the owner test; no precondition; Grok's, counted nowhere.
2. House claims that DO NOT HOLD: CH11 (Astra's cite `s4-p1-check:135-141`), CH16 (Astra, 368 open-5 membership), CH17 (Grok, 368 "6 = 1 + 5"). None moves a grade.
3. REDACTIONS: 0 (the three literals 0 in every staged file; no other ticker, price, share count, P&L or config value of his found).
4. `02-greps.txt` was hand-transcribed into the Write tool; six transcription errors were found by eye and fixed before launch; no mechanical diff of that file was possible (the excerpt files were mechanically compared and show no differing content line); a residual error in `02-` cannot be excluded.
5. Hub slips: two `Write` calls aimed at a path outside the sitting folder (`/Users/cobalt-wt/placeholder-never-used`, `…-2`) by mistake; both refused `EACCES`; nothing written.
Not escalated: no OPEN / ONE HOUSE / NOT RULED cell; no differing original count for C1 or C4 (all three houses derive 1 and 2); no house text scores X1 (Grok: "X1 was not run and is not scored"; Astra: "the decline is stated, not scored"); no Opus-seat claim DOES NOT HOLD; no claim to route a card, change a model or amend L29; no `RE-OPENS A RULING`; no independence breach; astra's probe was `UP`; THE FLOOR: MET.

RESULTS SITTING R2 DONE · grok: SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW (apart: C1 C2 C3 C4 C5) · astra: SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW · opus: SITTING: C1 AT LEVEL · C2 CLOSE BELOW · C3 AT LEVEL · C4 CLOSE BELOW · C5 BELOW · cells closed: 5 of 5 · open: 0 · one house: 0 · claims that HOLD: 21 · owner items: 1 · ESCALATE: 5
