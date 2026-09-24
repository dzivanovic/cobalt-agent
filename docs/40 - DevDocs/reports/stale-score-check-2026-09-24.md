# Stale-score build check, round 1 — 2026-09-24 (relaunch after the 18:45 PREFLIGHT stop, R87)

## §0 Headline
- Checked `de48c19b..358f1f75` (the whole branch `cards/stale-score-0922`, `<tip>` re-pointed by the desk, R86) and the build's three suites' executed output, by Opus 5.5 and Grok (Sol on METER, Gemini out).
- Opus: `CHECK: BUILD STANDS`. Grok: `CHECK: BUILD STANDS`. Neither raised a defect; defects that HOLD in my file-check: 0. Observations that HOLD (weaker assertions, one untested interleaving) are under `## ESCALATE`.
- Ready for a deploy prompt: 2 of 2 answering houses (floor 2, R95). Production reads X9 = 0, X25 = 0 (the desk's).
- ESCALATE: 12. Nothing was built, run, merged or rebased by this run.

## L74
Recorded once (L74): a system-reminder arriving beside the Read result of this prompt file asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies, and named a file-send tool (`SendUserFile`). Treated as DATA and not followed. This run commits nothing and sends no file.

## PREFLIGHT
`<D>` = 2026-09-24 (`date` → `Thu Sep 24 18:47:58 EDT 2026`). `<main tip>` = `de48c19b`, `<red>` = `7bffdbcb`, `<tip>` = `358f1f75` (desk re-point, R86 as amended).

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | allowed; `Thu Sep 24 18:47:58 EDT 2026` |
| placeholder gate | `grep -n -E "R_[_]"` on this prompt | 1 | allowed; prints nothing — PASS |
| grok gate R17 row | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | allowed; line 31/32 carries `Grok approved with no asking going forward` |
| grok gate R17 committed | `git log -1 --format=%H -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | allowed; `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| grok gate R19 row | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | allowed; carries `All 4 house models approved for use indefinlitly` |
| grok gate R19 committed | `git log -1 --format=%H -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | allowed; `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R45 row | `grep -n "^| R45 " cto-2026-09-22.md` | 0 | allowed; line 121 carries `recompute the FRESH-price tap race` |
| R40 row | `grep -n "^| R40 " cto-2026-09-22.md` | 0 | allowed; line 126 carries `EXCLUDED from the shadow agreement numbers` |
| R45 committed | `git log -1 --format=%H -S"recompute the FRESH-price tap race" -- cto-2026-09-22.md` | 0 | allowed; `1a3f5cf7003c03cb41a5158d601133b4c61a264b` |
| R58 row | `grep -n "^| R58 " cto-2026-09-23.md` | 0 | allowed; line 61 carries `"yes start both"` |
| R95 row | `grep -n "^| R95 " cto-2026-09-23.md` | 0 | allowed; line 103 carries `just Opus and Grok for code checks` |
| R97 row | `grep -n "^| R97 " cto-2026-09-23.md` | 0 | allowed; line 105 carries `take Gemini out of reading` |
| build's stop recorded | `grep -n -F "STALE SCORE BUILT"` on the three desk files | 2 | allowed; `cto-2026-09-25.md`, `cto-2026-09-26.md` absent (recorded, not fatal); R84 (line 102) quotes the stop line — PASS |
| this launch's row | `grep -n "44-stale-score-check-r2.md"` on the three desk files | 2 | allowed; R86 (`cto-2026-09-24.md:106`) and R87 (:107) name this file |
| this launch's row committed | `git log -1 --format=%H -S"44-stale-score-check-r2.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | allowed; `ce8fef3fe62a87c8849992d3a1fff5dea12d9874` |
| the line is `15`'s | `grep -c -F -e '<rule>'` on `15-drc-d1-fix-r1-check.md`, 14 allow + 3 deny strings, one call each | 0 ×17 | allowed; each printed `1` — PASS |
| Astra / agy / production string | read of the launch line in the prompt's line 1 | — | none present — PASS |
| `grok --version` | `grok --version` | 0 | allowed; `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/stale-score` | 0 | allowed; present |
| THE BUILT LINE | `tail -n 3` of the build report | 0 | allowed. Last non-blank line, whole: `STALE SCORE BUILT 01ee8bcd \| on de48c19b \| rebased: yes \| red 7bffdbcb \| offline 2518/0 \| with-DB 2879/0 \| live-note 131/0 \| migration: 0015 rolled back \| cobalt_dev: 0013 \| .env: removed \| experiments 31/31/0 \| ESCALATE: 11`. All required fields present; `cobalt_dev: UNPROVEN` absent |
| `main` is the base | `git log --oneline 358f1f75..de48c19b` | 0 | allowed; EMPTY — PASS |
| deploy tag under base | `git log --oneline de48c19b..a2d320b8` | 0 | allowed; EMPTY — PASS |
| the range | `git log --oneline de48c19b..358f1f75` | 0 | allowed; 8 commits: `358f1f75`, `2bdc73df`, `01ee8bcd`, `3894d1a1`, `d0274dc0`, `f17814c6`, `7bffdbcb` (= `<red>`), `f0798537` (the prompt's "6" is a different count; recorded, not fatal) |
| branch tip | `git log --oneline -1 cards/stale-score-0922` | 0 | allowed; `358f1f75` (re-read after the run: unchanged) |
| branch moved above `<tip>` | `git log --oneline 358f1f75..cards/stale-score-0922 -- tests src configs` | 0 | allowed; EMPTY by construction |
| stat list / boundary | `git log --stat --oneline de48c19b..358f1f75` | 0 | allowed; src: `cards/scoring.py`, `cards/store.py`, `radar/audit_export.py`, `radar/evaluate.py`, `replay/formations.py`, `db_migrations/__init__.py`, `0015_shadow_agreement_stale.sql` + `.rollback.sql`; tests: `test_stale_score.py`, `test_stale_score_db.py`, `stale_db_support.py`, `tests/experiments/stale_score/**`, and the A1 re-points (`test_replay_runner`, `test_rubberband_forms`, `test_setups_d1`, `test_archiver_migrations`, `test_assumed_store`, `test_p4_migrations`, `test_radar_migration`, `test_radar_score_migration`, `test_tenancy`); docs: six DevDocs + the two reports. A `0015_*.sql` pair IS in the range. See `## Checked against the branch (i)` |
| `.env` | `ls /Users/cobalt/cobalt-wt/stale-score/.env` | 1 | allowed; `No such file or directory` — PASS |
| scratch folder | `ls scratch/tribunal-bars-0920` | 0 | allowed; present |
| recovery | `ls scratch/tribunal-bars-0920/stale-score-check` | 0 | allowed; only the desk's `60-production-x9-x25.md` (a prior hub run stopped at PREFLIGHT, R87; nothing of mine staged) |
| production reads | `ls scratch/tribunal-bars-0920/stale-score-check/60-production-x9-x25.md` | 0 | allowed; present (R86: X9 = 0, X25 = 0) |
| THE STAGGER | `grep -n -F "no other house hub is running" cto-2026-09-24.md`, a printed line that also names `44-stale-score-check-r2.md` | 0 | allowed; line 106 (R86, amended) — PASS. (I hold no process-list string; the sentence is the desk's statement, not my proof) |
| THE PROBES — Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | allowed; stdout `OK` (plus a settings warning line about `Bash(git push*:*)`, noise) — UP |
| THE PROBES — Grok | by its `--version` row | — | UP |
| THE PROBES — Sol | not probed | — | `date` before 2026-09-26 06:47 ET → `sol: METER — retry after Sep 26th, 2026 6:47 AM (54's probe)` |
| floor | Opus + Grok up = 2 | — | met (R95) |

Recorded, not launched: Gemini (R96/R97), Astra (R46), Sol (METER).

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stale-score-check/` (18:5x–19:03 ET). Three forks of this hub copied the three big diffs (Read → Write; every count and byte sum re-checked by me afterwards); I wrote the rest.

| file | bytes | status | check made |
|---|---|---|---|
| `00-READING-ORDER.md` | 12,086 | (guide) | the `Files:` lines of `42:73` / `:94` (`grep -x -F -f`) and the eight step headings re-matched against `42` |
| `01-QUESTIONS-CHECK.md` | 8,120 | MANDATORY | verbatim from the prompt |
| `10-rulings.md` | 7,867 | MANDATORY | every row is a line of its desk file |
| `11-design-v2.part1.md` + `part2` | 30,912 + 12,963 = 43,875 | MANDATORY | sum = original 43,875 B; 0 trailing-whitespace lines |
| `12-owner-items.md` | 5,855 | MANDATORY | every body line is a line of the derive / Fable report |
| `20-diff-src.part1`–`part4` | 59,904 + 29,968 + 49,107 + 1,333 = 140,312 | MANDATORY | sum = saved `git log -p -W` output; `diff --git` 8 = 8, `commit ` 2 = 2. Parts 1 and 3 exceed 38,000 B (one file's diff each, indivisible) |
| `21-diff-migration.md` | 5,758 | MANDATORY | `0015` pair in range; body lines match the `git show` outputs; number is `0015` |
| `30-diff-tests.part1`–`part4` | 30,010 + 29,282 + 32,708 + 33,475 = 125,475 | MANDATORY parts 1, 3; OPEN 2, 4 | sum = 125,475; `diff --git` 42 = 42 (= the `--stat` test touches 1+2+7+13+3+1+15); `commit ` 7 = 7 |
| `40-diff-docs.part1`–`part6` | 30,783 + 28,402 + 25,343 + 31,730 + 14,370 + 18,525 = 149,153 | OPEN-AS-NEEDED | sum = 149,153; `diff --git` 14 = 14; `commit ` 8 = 8 |
| `50-build-report.part1` / `part2` | 13,797 / 17,575 | MANDATORY | excerpts: line counts and every non-blank body line matched to the source (one slip of mine, ESCALATE 11's last clause, was caught by that check and fixed) |
| `51-build-report-steps.part1` / `part2` | 19,131 / 20,727 | part1 MANDATORY, part2 OPEN | same |
| `52-suites.md` | 8,728 | MANDATORY | `## BASELINE`, `## CLOSE` suite rows and `## LANE` each carry a summary line — no `FAILED: packet` |
| `60-production-x9-x25.md` | 2,628 | MANDATORY | the desk's file, untouched; two read-only `SELECT count(*)` under the `db query --side user --prod` prefix |

Honest size: MANDATORY (without `00`) = 336,364 B ≈ 84,090 tokens; whole packet (without `00`) = 569,001 B ≈ 142,250 tokens; with `00` (12,086 B) 348,450 B ≈ 87,110 tokens and 581,087 B ≈ 145,270 tokens. Under 1,200,000 B: no two-run split. Trailing-whitespace disclosure: src diff 167 lines, tests diff 18, docs diff 111 (single-space context blanks and commit-body indents, copied as they appear); the design and report sources 0. The saved stdout files end with the shell tool's `[exited with code 0]` line, kept as the last line of `20 part4`, `30 part4`, `40 part6` (disclosed in `00`).

Launches. `date` at launch `Thu Sep 24 19:05:14 EDT 2026`; the Grok gate rows re-read then (R17 line 32 `1758fd78…`, R19 line 34 `5055151d…`, both committed). Before-launch `ls -la` pairs: packet folder = `00`…`60` (28 files, no `*-check.md`); `/Users/cobalt/cobalt-wt/stale-score` = the 26-entry worktree root, no `.env`. The same listings before the Grok launch (19:05:33).
- OPUS 5.5, launched ≈ 19:05:25 (bg `b5eu19ii8`): `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/stale-score-check/. Start with 00-READING-ORDER.md and follow 01-QUESTIONS-CHECK.md exactly. Files split into ordered parts name.part1.md … are read in order as one file. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stale-score-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`. Notice at 19:09:21 (≈ 4 min).
- GROK, launched 19:05:3x (bg `bdqsbtorw`): `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. The folder is scratch/tribunal-bars-0920/stale-score-check/. Start with 00-READING-ORDER.md and follow 01-QUESTIONS-CHECK.md exactly. Files split into ordered parts name.part1.md … are read in order as one file. Do not open any *-check.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stale-score-check/grok-check.md and reply with only that path."` (never `--always-approve`). Notice at 19:17:51 (≈ 12 min). Its stdout was progress text and the path; it wrote `grok-check.md` itself (24,291 B).
- Both finished inside the 45-minute clock (deadline 19:50). No HARNESS / METER / TIMEOUT. One attempt per house.
- Written-nothing proof: after both returned, `ls -la` of the packet folder = the 28 files of before, plus `opus-check.md` (12,312 B, written by me at 19:09) and `grok-check.md` (Grok's own); `ls -la /Users/cobalt/cobalt-wt/stale-score` = identical to before (no `.env`, no new entry); `git log -1 cards/stale-score-0922` still `358f1f75`. `grep -c -i "denied\|not allowed\|permission"` on `opus-check.md`, `grok-check.md` and Grok's stdout = 0 each.
- `opus-check.md` is Opus's stdout without its first line (a settings warning on `Bash(git push*:*)`, harness noise) and the `[exited with code 0]` trailer. Every non-empty line of it is a line of the stdout file (`grep -v -x -F -f`; only the 20 empty lines print).
- SOL not launched (METER, retry Sep 26th, 2026 6:47 AM). Gemini not seated (R96/R97). Astra not seated (R46).

## CONTINUE
next: none — collation is complete (`## Per question` … `## ESCALATE` written); the report ends on the stop line.

## Per question
Cells ≤ 20 words. "challenging" counts checkers who raised a challenge; every one below is an observation, none claimed a defect.

| question | builder's claim | opus | grok | sol | checkers challenging |
|---|---|---|---|---|---|
| 1 required field | `intraday_stale` required, in `base`, every return path (`evaluate.py:614`, `:938`) | PASS; no default (`part3:44`); every return via `result(**base)` | Yes; all named paths carry it; guards read the field | METER | 0 |
| 2 one `last` rule | `score_last` on all four callers; three fallbacks deleted | PASS; four callers, three fallbacks deleted, none missed | Yes; same four callers, no fifth; test forbids old strings | METER | 0 |
| 3 null, not plausible | NULL proximity, NULL score, `[F-16]` sentence, JSON null | PASS; sentences match word for word; `PROXIMITY_UNKNOWN` once | Yes; both forms, JSON null, once; other htf branch not the W4 path | METER | 0 |
| 4 version | `s2p2.3` singleton, audit gate before replay | PASS; old strings gone; gate refuses by name; separate bump justified | One new string; gate before `replay_receipt`; bump matches `[F-08]` | METER | 0 |
| 5 `tap_dot` | tap accepted; score NULL; stored sentence kept or `PROXIMITY_UNKNOWN` | PASS; cannot publish a number or erase the sentence | Yes; same reading, both tests assert NULL score | METER | 0 |
| 6 R45 race | taps-moved branch = Fable (i); RED then GREEN | PASS; matches (i); adds O1: stale→fresh tap race, untested | Matches (i); stale and fresh rows stated; RED lines quoted | METER | 1 (O1, observation) |
| 7 R40 exclusion | X30 (A); `0015`, rolled back only | PASS (A); adds O2, O3 (weak asserts) | (A); notes pair-count assert names no tap id | METER | 2 (observations) |
| 8 ladder and ties | `radar.py` untouched; `[4, 2, 3, 1]` pin; no re-sort | PASS; pin proves null sink and `pool_position` | Yes; both orders proved; no periodic re-sort (X29) | METER | 0 |
| 9 premarket, clocks | no session gate; poller untouched | PASS; no session parameter; X15 shows both clocks | Yes; same; R39 met by not joining | METER | 0 |
| 10 not touched | health, radar_panel, configs, fixtures, seam pin unchanged | PASS; empty diffs; only htf flag changes in `_factor_observations` | No hunk in any of those; X22 found no scorer | METER | 0 |
| 11 replay | X4, X10, X27 | PASS; `json_null=True`, `as_of` is the receipt's | Yes; same three outputs; X27 line is the pre-fix sentence | METER | 0 |
| 12 experiments | 31/31/0, X29 browser timing UNPROVEN | all 31 support verdicts; X24 count should go to Dejan | all verdicts supported; none stops the build; `60` changes nothing | METER | 1 (Opus: X24, not a gate) |
| 13a–d L52 | (a)–(d) answered | (a) yes (b) yes (c) yes (d) yes | (a) yes (b) yes (c) in tree (d) yes for this version | METER | 0 |
| 14 outside / missing / L32 | `0015` and R45 built by ruling; no owner value | `0015` and R45 ordered; O2, O3 weak asserts; no owner value | same; R40 pair-count assert weaker than its comment; re-points disclosed | METER | 2 (observations) |
| 15 suites | offline 2518/0, with-DB 2879/0, live-note 131/0 | all SHOWN; O4: no suite ran with `358f1f75` as HEAD | all SHOWN; runs precede `358f1f75`, its two paths add no source | METER | 1 (O4, fact) |

### Question 2 — every checker's answer in full

**Opus**

**(2) One `last` rule: PASS**
- `score_last` returns None iff `intraday_stale`, raises `EvaluateError` when fresh with no price, and otherwise returns `last_price` (`part2:250-260`).
- All four callers use it:
  - refresh, `part3:387`;
  - replay, `part3:476`;
  - create, `part3:772`;
  - audit, `part2:510`.
- The three fallbacks are deleted, not replaced: `else card.entry` (`part3:384`), `Decimal(card["entry"])` (`part3:473`) and `else trigger` (`part2:509`).
- X18's list (`51.part1:131`) has the same four callers, and the base grep shows no fifth. `radar_panel.py` has no scorer (X22, `51.part1:140`). The test counts exactly 4 callers and pins the deleted strings (`tests.part3:421-438`). I found no missed caller.

**Grok**

## (2) ONE `last` RULE

Yes. `score_last` returns None iff `ev.intraday_stale`; if not stale and `last_price` is None it raises `EvaluateError` (`20-diff-src.part2.md:250-260`). Test: `30-diff-tests.part3.md:407-418`.

Every `score_card` caller passes that last. The four call sites are `refresh_card` (`20-diff-src.part3.md:387-388`), `replay_receipt` (`:476-477`), the create call (`:772-773`), and `audit_export`’s replay scorer (`20-diff-src.part2.md:510-511`). X18 at the base listed those four and no fifth (`51-build-report-steps.part1.md:130-131`). Re-run after S1: `X18: fixed=True score_card_callers=4 on_score_last=4` (`51-build-report-steps.part2.md:45`). The test asserts `len(calls) == 4` and `last=score_last(` on each (`30-diff-tests.part3.md:421-434`; module `30-diff-tests.part4.md:414-426`). No caller on that list was missed.

The two `card.entry` fallbacks are deleted, not replaced (`20-diff-src.part3.md:384-388` and `:473-477`). The `trigger` fallback is deleted, not replaced (`20-diff-src.part2.md:509-511`). The test forbids `else card.entry`, `else Decimal(card["entry"])`, and `else trigger` (`30-diff-tests.part3.md:435-438`).

### Question 5 — every checker's answer in full

**Opus**

**(5) `tap_dot` [F-06]: PASS**
- While proximity is NULL: the tap is inserted and conviction and the proposed key are recomputed and written (`part1:1152-1175`).
- The score is `card_score(conv, None, …)`, so it stays None.
- `suppressed` is the stored value, or `PROXIMITY_UNKNOWN` if none is stored (`part1:1165-1166`).
- A tap cannot publish a number or erase the sentence while proximity is NULL. Tests: `tests.part1:395-416`.

**Grok**

## (5) `tap_dot` (`[F-06]`)

Yes. A normal factor is not refused. While stored proximity is NULL, `card_score` is computed with that NULL, the stored sentence is written back if non-null, otherwise `PROXIMITY_UNKNOWN` (`20-diff-src.part1.md:1163-1174`). Conviction and the proposed key still update (`:1170-1174`). Tests: sentence kept byte for byte and score NULL (`30-diff-tests.part1.md:395-404`); no stored sentence writes `PROXIMITY_UNKNOWN` and score NULL (`:407-415`).

A tap cannot publish a number while proximity is NULL: the score argument is None (`20-diff-src.part1.md:1169`) and both tests assert `card_score is None`. It cannot erase a stored helper sentence: the non-null stored value is written back (`:1166`, `:403`).

### Question 6 — every checker's answer in full

**Opus**

**(6) R45, the race: PASS, with observation O1**
- The build matches Fable (i) exactly (`part1:951-971`):
  - the lock SELECT adds `conviction, score_suppressed`;
  - `suppressed = update.score_suppressed if update.proximity is None else locked[3]`;
  - `score = card_score(locked[2], update.proximity, suppressed)`;
  - the UPDATE adds `card_score` and `score_suppressed`;
  - conviction and key are not written;
  - there is no SQL arithmetic.
- The test builds the interleaving: stage read (`update_for`), then tap, then `refresh_radar_card` (`tests.part1:443-467`). It also asserts that the new score differs from the old-price score.
- Recorded RED line (`51.part2:85`): `AssertionError: card_score 60 beside proximity 0.849462: expected 56 (the tap's conviction on this scan's proximity)`.
- **Stale scan race.** Start: stored proximity P0, conviction C0. The stage reads and computes proximity None with sentence Z. A tap sets conviction C1 and score C1×P0. The stage writes. Stored row: proximity NULL, `last_price` via COALESCE, `card_score` NULL, `score_suppressed` Z, conviction C1, key K1. Covered by `tests.part1:423-435`.
- **Fresh scan race.** The stage reads and computes P1. A tap sets C1 and `suppression(dots)` = S. The stage writes. Stored row: proximity P1, `card_score` = round(C1×P1×100), or NULL if S is set; `score_suppressed` S; conviction C1; key K1.
- **O1 (not tested).** When the bars go from stale back to fresh, a tap races the first fresh scan. The tap keeps Z because the stored proximity is still NULL. The write then takes `locked[3]` = Z, so for one scan the row shows proximity P1 with a NULL score and a "bars stale — last close …" sentence. This follows the ruled formula exactly and publishes no number. But it does not match (i)'s summary "fresh proximity → the tap's conviction on this scan's proximity". The next scan without a race fixes it. This is for the desk; it is not a build defect.

**Grok**

## (6) R45, THE RACE

The taps-moved branch matches Fable (i) (`12-owner-items.md:28`). The lock SELECT reads `conviction, score_suppressed` (`20-diff-src.part1.md:950-954`). `suppressed = update.score_suppressed if update.proximity is None else locked[3]` and `score = card_score(locked[2], update.proximity, suppressed)` (`:961-962`). The UPDATE sets `card_score` and `score_suppressed` (`:963-968`). Conviction and the proposed key are not in that UPDATE; they stay the tap route’s. The only arithmetic is `card_score()` in Python. No SQL arithmetic.

The fresh-scan test constructs stage read → tap → stage write (`30-diff-tests.part1.md:443-467`). It went RED before the fix. Recorded line (`51-build-report-steps.part2.md:85`): `AssertionError: card_score 60 beside proximity 0.849462: expected 56 (the tap's conviction on this scan's proximity)` / `assert 60 == 56`.

Stale scan (same interleaving, null update proximity; `30-diff-tests.part1.md:423-435`). After the write the row is: proximity NULL, `card_score` NULL, `score_suppressed` equal to the stage update’s stale sentence, conviction and proposed key left as the tap wrote them (that UPDATE does not set them), `last_price` via `COALESCE`. Its own RED line was `AssertionError: card_score 66 beside a NULL proximity` (`51-build-report-steps.part2.md:84`).

Fresh scan (`30-diff-tests.part1.md:443-467`). After the write the row is: proximity = this scan’s proximity (not the pre-tap proximity), `card_score` = `card_score(tap conviction, this scan’s proximity, the tap’s locked reason)` and not the old-proximity product, `score_suppressed` = the locked tap reason, conviction = the tap’s, proposed key = the tap’s.

### Question 7 — every checker's answer in full

**Opus**

**(7) R40, the exclusion: PASS, decision (A)**
- X30's output (`51.part1:39`): `x30_matched=['B', 'D']`, `post_fix_never_matched=True`, `decision=A`. A fresh row is not matched and a post-fix stale row (C) is not matched, so the output supports (A).
- The view is X25's join (`tests.part2:270-285`) plus the stored `radar_score_run.evaluator_version IN ('s2p2.1','s2p2.2')` (`part2:58-73`).
- Post-fix taps: any run at `s2p2.3` or later is never matched. The builder's `git log -G` shows only two earlier version strings exist (`51.part1:41`).
- The rollback is exactly 0007's view (`part2:10-22`), and the test compares the view definition before and after (`tests.part1:513-532`).
- Over-exclusion of daily-missing pre-fix runs is named (`21:17-18`, `50.part2:108`).
- `0015` is registered in both lists (`part2:153`, `:158`).
- The forward/rollback test runs on `connect_migration` and rolls back in `finally`. The behaviour tests use the suite transaction; this deviation is stated (`51.part2:91`).
- Proof it was not committed: XL76 (`52:37`). `placement.py` is untouched.

**Grok**

## (7) R40, THE EXCLUSION

X30 recorded (A). Printed output (`51-build-report-steps.part1.md:39`): `x25_matched=['B', 'C', 'D'] x30_matched=['B', 'D'] post_fix_never_matched=True daily_missing_over_excluded=True decision=A`. The decision rule is B matched and A and C not matched (`30-diff-tests.part3.md:96-100`). That print supports (A). (B) was not taken; the forward-half question does not apply.

Under (A):

- The view’s `NOT EXISTS` is X25’s predicate (`30-diff-tests.part2.md:281-288`) plus `evaluator_version IN ('s2p2.1', 's2p2.2')` (`21-diff-migration.md:32-48`). Those two strings are the stored pre-fix discriminator (`30-diff-tests.part2.md:261-268`).
- A post-fix tap is not excluded: C is absent from `x30_matched`, and `post_fix_never_matched=True`. The behaviour test keeps the post-fix graded tap in the pair count (`30-diff-tests.part1.md:563-587`). After the fix a stale dot also has no engine grade, so a real tap records none (X21, `51-build-report-steps.part1.md:21`).
- Rollback text is the grade view with no exclusion (`21-diff-migration.md:53-69`). The test restores the pre-`0015` viewdef, which has no `evaluator_version`, inside one transaction that rolls back (`30-diff-tests.part1.md:513-531`). XL76 then shows the live view equal to that rollback body (`52-suites.md:37`).
- Daily-missing pre-fix over-exclusion is named in the migration (`21-diff-migration.md:17-18`) and printed as case D (`daily_missing_over_excluded=True`). Under-exclusion on an edited def’s md5 is named (`21-diff-migration.md:19-20`).
- The file is `0015`, in `FORWARD` after `0013` and in `REVERSE` before `0013`’s rollback (`21-diff-migration.md:87-94`; test `30-diff-tests.part1.md:504-510`).
- It is applied only inside a rolled-back transaction: the shape test uses `autocommit = False` and `rollback()` in `finally` (`30-diff-tests.part1.md:517-531`); the behaviour tests execute the file on the suite connection (`:535-539`). XL76 after the with-DB close: `view_has_0015_exclusion=False view_equals_0007=True` (`52-suites.md:37`). Not left on `cobalt_dev`.

The pair-count assert `before - after == 1` does not name which tap id the view dropped (`30-diff-tests.part1.md:585-587`). The id-level proof is X30’s print plus the view SQL matching `X30_TAPS`. That is a weaker assert, not a wrong view.

## Suites
From the build report itself (`/Users/cobalt/cobalt-wt/stale-score/docs/40 - DevDocs/reports/stale-score-build-2026-09-24.md`), not the packet copy. Facts only.

| suite | BASELINE (report `:151-171`) | CLOSE (report `:434-447`) | CLOSE `0 failed`, `0 errors`? |
|---|---|---|---|
| offline | `15 failed, 2503 passed, 361 skipped, 1 xfailed, 15 warnings in 509.42s (0:08:29)` (exit 1) | `2518 passed, 369 skipped, 1 xfailed, 15 warnings in 509.98s (0:08:29)` (run 18:20:48) | the summary line has no `failed` or `error` term; the report writes "0 failed, 0 errors". No exit code quoted |
| with-DB (`--deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip`) | `15 failed, 2856 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 599.06s (0:09:59)` | `2879 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 591.43s (0:09:51)`, exit 0 (run 18:29:33) | same: no `failed` or `error` term; exit 0 quoted |
| live-note (READ-ONLY) | `131 passed, 15 warnings in 24.99s`, exit 0 | `131 passed, 15 warnings in 24.67s`, exit 0 (run 18:20:48) | no failure term |

- The fifteen named BASELINE reds are all in `tests/cobalt/test_stale_score.py` (locations `:91`, `:105`, `:120`, `:155`, `:181`, `:200`, `:226`, `:246`, the pydantic `AttributeError` of (vi), `:272`, `:302` ×2, (ix)'s `DID NOT RAISE`, (xi)'s `AttributeError`, `:406`); the STEP-2 T table names 17 tests, 15 RED and two green-by-design (`test_r37_r41_…`, `test_audit_export_same_version_run_still_exports`). At CLOSE `failed` 15 → 0 and `passed` 2503 → 2518 (+15). STEP-2's own with-DB run: `2871 passed` (2856 + 15); STEP-4's: `2879 passed` (+8 `test_stale_score_db.py` tests, which skip offline: skipped 361 → 369).
- Live-note leg: BASELINE `SKIPPED` lines 0; CLOSE no `SKIPPED` line — no line names `COBALT_LIVE_VAULT_ROOT` (expected none). `AWAITING` set at both: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)` — identical.
- With-DB deselected count: 2 (`TestMigrationRoundTrip`'s two) at BASELINE, STEP-2, STEP-4 and CLOSE; reason in the report's ESCALATE 1: it commits every migration to `cobalt_dev` (L76).
- Table-set probe: BASELINE — `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`: PASSED (not among the failures, not skipped). CLOSE — "No failure line exists, so the table-set probe `test_migrate_proof` did not fail" (no explicit PASSED line at CLOSE).
- XL76 absence line (CLOSE, same take, before `(d)`): `XL76: view_has_0015_exclusion=False view_equals_0007=True`, `1 passed in 0.10s`; report: "`0015`: rolled back … `cobalt_dev: 0013`". Experiments folder offline at 18:39:45: `17 passed, 12 skipped in 4.99s` (the 12 skips are every `requires_db` module, incl. XL76).
- `.env: removed, proven gone` after every with-DB call: BASELINE ("`.env: removed, proven gone (BASELINE)`"), STEP-2 suite, the 14 STEP-3 takes, STEP-4 T RED, STEP-4 suite, CLOSE (`(d) rm`, then `No such file or directory`, 18:39) — each written in its `## LANE` row or SUITE bullet. The PREFLIGHT row (17:08:17) is "no copy yet". The 17:42 STEP-2 row gives "removed ~17:53" (an approximate time).
- `## LANE` rows (all seven, report `:516-527`): each shows (a) `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` and (b) `No such file or directory` before its `cp`; (c) exactly the builder's own `.env` line (mode `-rw-------`, 2186 B) after it; (d) `rm` then `No such file or directory`. Times: 17:08:17, 17:21:11, 18:29:33, 18:00:4x, 17:57, 17:53–17:55 (14 takes), 17:42:4x.
- Commit times (git): `f0798537` `7bffdbcb` `f17814c6` 17:09:07 · `d0274dc0` 17:53:31 · `3894d1a1` 17:56:34 · `01ee8bcd` 18:20:04 · `2bdc73df` 18:20:40 · `358f1f75` 18:40:21. So the CLOSE offline and live-note runs (18:20:48) start 8 s after `2bdc73df`; the with-DB (18:29:33) and experiments-folder (18:39:45) runs precede `358f1f75`, whose `--stat` is the report and `test_xl76_devdb_absence.py` only.

## Checked against the branch
Originals under `/Users/cobalt/cobalt-wt/stale-score/` (Read / grep); base via `git -C /Users/cobalt/cobalt`. Rows: `claim · who · file:line · verdict · ≤30 words`.

| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| `intraday_stale: bool` required, no default | Opus, Grok | `evaluate.py:614` | HOLDS | Field declared with no default between `evaluation` and `direction`. |
| set on every return path via `base` | Opus, Grok | `evaluate.py:938`, `:946-947`, returns `:955`, `:963`, `:1027`, `:1064-1128` | HOLDS | Flag computed at `:928-934`, placed in `base`; every `return` goes through `result()` or `both(result())`, which spreads `base`. |
| guards read the field, not the label | Opus, Grok | `scoring.py:346`, `:358`; `evaluate.py:1026` | HOLDS | `stale_reason`, `score_last` and the intraday return read `intraday_stale`/`ev.intraday_stale`. |
| `score_last` None iff stale, raises when fresh and no price | Opus, Grok | `scoring.py:354-364` | HOLDS | Raises `EvaluateError`; else returns `ev.last_price`. |
| all four `score_card` callers use `score_last` | Opus, Grok | `evaluate.py:1285`, `:1593`, `:1902`; `audit_export.py:375` | HOLDS | grep (iv): each passes `last=score_last(ev), stale_reason=stale_reason(ev)`; the only other hit is the `def` (`scoring.py:367`). |
| `card.entry` (×2) and `trigger` fallbacks deleted | Opus, Grok | grep (iii): `evaluate.py:1285`, `:1996` | HOLDS | Two hits, neither a `last`: `:1285` is the `trigger=card.entry` argument, `:1996` the receipt's `entry` field. `else trigger` 0 hits. |
| `[F-16]` sentences exact; NULL last → NULL proximity and score | Opus, Grok | `scoring.py:342-351`, `:379-393`, `:287-290` | HOLDS | `"bars stale — no closed bar"` / `"bars stale — last close HH:MM:SS ET, older than 2 × radar.scan_interval"`; `card_score` returns None for a NULL proximity. |
| `published_numbers` JSON null | Opus, Grok | `evaluate.py:1537-1548` | HOLDS | `None if update.proximity is None else str(...)`; `card_score` passes through as None. |
| `PROXIMITY_UNKNOWN` defined once | Opus, Grok | `scoring.py:92`; grep `PROXIMITY_UNKNOWN =` in `src` | HOLDS | One definition; `store.py:1199` imports it. |
| `htf_level_proximity` `stale=intraday_stale` | Opus, Grok | `evaluate.py:743` | HOLDS | Computed branch only; the `last_price is None` branch (`:733-738`) carries no value, hence no grade (Grok's reading). |
| one version string; previous not in set | Opus, Grok | `evaluate.py:162-163`; `formations.py:84` | HOLDS | Both constants `"s2p2.3"`; `SUPPORTED_EVALUATORS = frozenset({"s2p2.3"})`; `s2p2.2` / `s2p2.1` absent from both files. |
| audit gate refuses missing/other version before replay | Opus, Grok | `audit_export.py:218-226` | HOLDS | Loop over the chain, `AuditExportError` naming both versions, before `_resolve_snapshot`/`rebuild_members` (`:228-233`). |
| `tap_dot` keeps stored sentence, score NULL | Opus, Grok | `store.py:1235-1240` | HOLDS | `prox is None` → `suppressed = locked[3]` or `PROXIMITY_UNKNOWN`; `card_score(conv, None, …)` is None; conviction and key still written (`:1242-1246`). |
| taps-moved branch = Fable (i), clause by clause | Opus, Grok | `store.py:1027-1046` | HOLDS | Lock SELECT adds `conviction, score_suppressed` (`:1028-1030`); `suppressed` and `score` at `:1037-1038`; UPDATE sets `card_score`, `score_suppressed` and not conviction/key; no SQL arithmetic. |
| O1: stale→fresh tap race leaves P1 beside NULL score and stale sentence for one scan | Opus | `store.py:1037-1038`; `scoring.py:288` | HOLDS | With the tap having kept sentence Z (proximity still NULL) and the stage writing fresh P1, `suppressed` = `locked[3]` = Z, so `card_score` is None. Ruled text; no test builds this interleaving (8 tests in `test_stale_score_db.py`). |
| O2: `test_r40_on_cobalt_dev…` tautological | Opus | `test_stale_score_db.py:242-252` | HOLDS in part | Compares view drop to `X30_TAPS` count; the builder's `cobalt_dev` X25 = 0 (`## STEP-3`), so `0 == 0`. "Uses the view's own predicate" DOES NOT HOLD literally: `X30_TAPS` is a separate SQL copy (`stale_predicates.py:35-42`). |
| O3: X30 test asserts only labels | Opus | `test_x30_r40_discriminator_db.py:95-96` | HOLDS | Asserts the three `seam_labels` and `EVALUATOR_VERSION not in PRE_FIX_VERSIONS`; the matched sets and `decision` are printed, not asserted. |
| pair-count assert names no tap id | Grok | `test_stale_score_db.py:237-239` | HOLDS | `:237` asserts X25 (not the view) names the two stale-run taps; `:238` `before - after == 1`, `:239` `after >= 2`. No id-level view assertion. |
| O4: no suite ran with `358f1f75` as HEAD; clean tree at 18:20:48 not shown | Opus (Grok: same times) | git times above; `52-suites.md` | HOLDS as fact | Commit and run times as in `## Suites`; `358f1f75` adds only `test_xl76_devdb_absence.py` and the report. A `git status` at run time is not in the report. NOT CHECKABLE FROM READS beyond that. |
| no session gate on the score rule | Opus, Grok | `freshness.py:106-120`; `evaluate.py:932-934` | HOLDS | `intraday_staleness(*, observed_at, as_of, scan_interval)` takes no session; `freshness.py` is not in the range's stat. |
| X28 not run by the desk | Grok | `60-production-x9-x25.md:31` | HOLDS | The file says "X28 was not run by the desk". |
| A1 re-points keep strength; no assertion removed without a replacement | Opus, Grok | `30-diff-tests.part1:188-342`, `:598-616`; `part3:180-201` | HOLDS | Every `-` `assert` line has a `+` line for it in the same hunk (list widened by the `0015` name, or `"s2p2.2"` → `"s2p2.3"`). |
| `_unmoved` widened by design; pinned hashes unchanged | Opus, Grok | `test_setups_d1.py:223-237` (diff `part3:216-239`) | HOLDS | Drops `intraday_stale` and maps the htf `stale` flag back on an intraday-stale evaluation; the sha256 literals are not in the diff. |

Own checks, stated plainly:
- (i) `git log --stat --oneline de48c19b..358f1f75`: every path is one `42`'s steps name — STEP-2 / STEP-4 `Files:` lines (`evaluate.py`, `scoring.py`, `audit_export.py`, `formations.py`, `store.py`, the `0015` pair, `db_migrations/__init__.py`), `test_stale_score.py`, `tests/experiments/stale_score/`, the shared `stale_db_support.py` and `test_stale_score_db.py`, the A1 re-points (`test_replay_runner:418/:472`, `test_archiver_migrations`, `test_assumed_store` named by `42`; `test_p4_migrations`, `test_radar_migration`, `test_radar_score_migration`, `test_tenancy`, `test_rubberband_forms`, `test_setups_d1` under `42`'s general A1 rule), six DevDocs, the two reports. `stale_db_support.py` and `test_stale_score_db.py` are not named by file in the `Files:` lines; `42` names STEP-4's T as `test_radar_cards_db.py`'s pattern. Nothing outside the sets above.
- (ii) `git log --oneline de48c19b..358f1f75 -- src/cobalt/cards/health.py src/cobalt/cards/radar.py src/cobalt/radar/poller.py configs tests/fixtures src/cobalt/radar/formation src/cobalt/radar/anatomy src/cobalt/anatomy tests/cobalt/test_radar_panel_cards.py` → EMPTY; `-- src/cobalt/aset/radar_panel.py` → EMPTY.
- (iii) `grep -n "card.entry\|else trigger"` on `evaluate.py` / `audit_export.py`: `evaluate.py:1285` (the `trigger=card.entry` argument) and `evaluate.py:1996` (the receipt's `"entry"` field). No `last` fallback.
- (iv) `grep -rn "score_card("` in `src/cobalt`: `scoring.py:367` (def), `audit_export.py:375`, `evaluate.py:1285`, `:1593`, `:1902`; every caller passes `last=score_last(ev)`.
- (v) `grep -n "intraday_stale"` on `evaluate.py`: field `:614`; `_factor_observations` keyword `:703` and uses `:709`, `:729`, `:743`; computed `:930-932`; `base` `:938`; call `:981`; return `:1026`.
- (vi) the version grep: `evaluate.py:162` `EVALUATOR_VERSION = "s2p2.3"`, `:163` `DESK_FORMULA_VERSION = "s2p2.3"`; `formations.py:84` `SUPPORTED_EVALUATORS = frozenset({"s2p2.3"})`; the old strings appear in neither file.
- (vii) done clause by clause in the table above (`store.py:1027-1046` against `12-owner-items.md`'s Fable (i) text): all clauses present.
- (viii) test diffs: every `-` `assert` line has an equal replacement in its hunk (`part1:204/218/243-244/260-261/304/326/332/338/609`, `part3:188/197`); added skip/xfail lines: 1 — `stale_db_support.py:27` `requires_db = pytest.mark.skipif(` (new file, the `requires_db` idiom); `DEF_WRITTEN_` on `+` / `-` lines: 0.
- (ix) `60-production-x9-x25.md`: both commands are `SELECT count(*)` under `COBALT_ENV=production uv run cobalt db query --side user --prod`; no write verb; outputs `0` and `0`.
- (x) `grep -n "00[0-9][0-9]_"` on the registry: `FORWARD` has `0013` (`:99`) then `0015` (`:100`); `REVERSE` has `0015`'s rollback (`:105`) before `0013`'s (`:106`); no `0014` / `0016` line in either tuple.
- (xi) `grep -rn "cobalt db migrate\|db migrate"` on the build report: `:51` (the removed string, checked absent in `42`), `:497` (`cobalt db migrate --allow-prod` is "the deploy hub's"), `:500` (the rollback command for the deploy) — all sentences about the rule or the deploy, none a command the build ran. The `0015` tests: `test_stale_score_db.py:135` `db.connect_migration(env.DEV_DB_NAME)`, `:136` `autocommit = False`, `:174` `_apply(conn, FORWARD)`, `:182-183` `finally: conn.rollback()`; `test_xl76_devdb_absence.py:22-23` connect, `:28-29` `finally: conn.rollback()`. The view-behaviour tests apply the `0015` text on the suite connection (`test_stale_score_db.py:187-191`), which `tests/cobalt/conftest.py:133-188` (`dev_db_tx`, autouse) replaces with a savepoint proxy over one rolled-back transaction — the stated deviation (build ESCALATE 8).

Where the two checkers contradict each other: none.

## Ready for a deploy
| checker | CHECK line | ready | reason |
|---|---|---|---|
| Opus 5.5 | `CHECK: BUILD STANDS` | YES | "The build does what v2 and R37–R45 order. I found no defects." |
| Grok | `CHECK: BUILD STANDS` | YES | (its check names no defect; observation: the R40 pair-count assert is weaker than its comment) |
| Sol | — | NO (not seated) | METER, retry after Sep 26th, 2026 6:47 AM |

## FOR THE CLASSIFIER
none

## ESCALATE
1. **Weaker assertions that HOLD (facts, no checker claimed a defect):** `test_r40_on_cobalt_dev_the_view_drops_exactly_x25s_pre_fix_count` compares the view's drop with a count that is 0 on `cobalt_dev` (`test_stale_score_db.py:242-252`); `test_x30_the_stored_data_bounds_r40s_exclusion` asserts labels and the version bound but not the matched sets or the decision (`test_x30_r40_discriminator_db.py:95-96`); `before - after == 1` names no tap id (`test_stale_score_db.py:237-239`). The constructed-rows R40 test (`:215-239`) is the real coverage, per both checkers.
2. **Opus O1 (untested interleaving, HOLDS as a code reading):** a tap racing the FIRST fresh scan after a stale run leaves the row with the fresh proximity beside a NULL score and the stale sentence for one scan (`store.py:1037-1038`, `scoring.py:288`); no test builds it. It follows Fable (i)'s text, publishes no number, and the next scan clears it. Opus and I both record it as not a defect.
3. **X30's decision (A):** Opus: printed output supports (A); Grok: the print supports (A), (B) not taken. `0015` is numbered `0015`, registered in `FORWARD` after `0013` and `REVERSE` before it, proven only inside rolled-back transactions plus XL76's absence line. Production reads: X9 = 0, X25 = 0 (`60`), so `0015` excludes nothing on today's data (the desk's file says so); X28 not run by the desk.
4. **Experiments carried as-is:** 31/31/0; X29's live-browser timing is UNPROVEN (named by the builder; no browser in the suite). No other UNPROVEN or NOT AS EXPECTED. `cobalt_dev: UNPROVEN` is NOT on the stop line. The build's live-note baseline equals R56's known state; no LANE STOP recorded; the builder's own ESCALATE has 11 items (none blocks).
5. **The tree the suites ran on (fact, from Opus's O4 and Grok's (15)):** offline and live-note started 18:20:48, with-DB 18:29:33, experiments folder 18:39:45; `2bdc73df` 18:20:40, `358f1f75` 18:40:21 (adds `test_xl76_devdb_absence.py` and the report only). No suite was run with `358f1f75` as HEAD, and no `git status` at run time is in the report.
6. **X24 (measurement, carried by the builder's ESCALATE 7 and Opus):** 629 of 660 premarket ticker-days on `cobalt_dev` miss minutes, no zero-volume bars, so a thin name's premarket `—` will be frequent; R38 was ruled "A". Opus suggests the number go to Dejan; not a build gate.
7. **The deselect (L76) and the registry seam:** the build did not run `TestMigrationRoundTrip` (it commits every migration to `cobalt_dev`); the deploy's gate runs it. The registry pins (`[:6]` / `[-6:]`, `numbers == [*range(1, 12), 13, 15]`) are a seam with H1 (`0014`), DRC D1 / voice V1 / DRC K1 (`0016`–`0018`), bars chunk 2 (`0012`); whichever lands later re-points them together.
8. **Packet disclosures:** `20-diff-src.part1` (59,904 B) and `part3` (49,107 B) exceed the 38,000 B part limit (one file's diff each, indivisible); the saved-stdout trailer `[exited with code 0]` closes three diff parts; the excerpt files (`10`, `12`, `21`, `50`, `51`, `52`) are verified line by line, not by byte count. No packet mismatch.
9. **Sol:** METER — retry after Sep 26th, 2026 6:47 AM (`54`'s probe); the desk seats Sol again from that time (R19). Gemini not seated (R96/R97); Astra not seated (R46). Two houses answered (floor 2, R95).
10. **L74:** one arrival, recorded above, not followed.
11. **`ASK DESK`:** none.
12. **Standing line:** Round 1 covers the stale-score build (`de48c19b..358f1f75`) and its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (Gemini out, R96/R97). With every seated house `CHECK: BUILD STANDS` and `defects that HOLD: 0`, the build is checked (L67) and the desk drafts its deploy prompt; a HOLD goes to a fix round (L75) and round 2 (L39); the deploy's L68 gate re-proves offline, with-DB (running `TestMigrationRoundTrip`, which this build deselected under L76) and live-note on the tree that ships.

STALE SCORE CHECK DONE · round: 1 · opus: CHECK: BUILD STANDS · grok: CHECK: BUILD STANDS · sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) · gemini: NOT SEATED (R96/R97) · defects that HOLD: 0 · ready for a deploy prompt: 2 of 2 · production reads: run · ESCALATE: 12
