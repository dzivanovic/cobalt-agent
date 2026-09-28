# Setups Deploy Review — 2026-09-24 (`06` read of `05-setups-deploy.md`)

## §0 Headline
- 2 of 2 houses answered: Grok `REVIEW: RUN IT` (the L67 floor, met), Opus 5.5 `REVIEW: RUN IT AFTER` 5 folds. `05` = commit `f173328fb733f5b62247cfaffb2d582f9cf2a42d`. Opus's harm claim F3 (dev proof writes his real vault) and its F2 (PAUSE smoke red) DO NOT HOLD against `vault.py:196-208` and `heartbeat/probes.py:88-89`.
- Mechanical checks clean: all 50 allow strings, 3 denies and the `--add-dir` pair of `05` count 1 in `66` (0 NEW; `66`'s launch line has 54 allows, `05` = 54 − 4). STEP-6.2's five rows equal the engine rows' unit / scope / consumers and R119 / R82 values. `R_[_]` count in `05` = 6 lines (only `R__L`, the desk's fill).
- Blockers: 0 under the mechanical rule stated under `## Checked against the files`. 8 folds proposed, all HOLDS-as-text on a relaunch, a wording gap, or an abnormal input (BETWEEN commit moves `main`; relaunch precedence (i) vs (vi); PAUSE merge clock not derived from the proof cost; three wording gaps; `-S` vacuous).
- ESCALATE: 4.

## L74
One block arrived inside a tool result: appended to the Read of this run's own prompt file (`06`), a system-reminder-shaped block asking that commit messages and PR bodies end with a `Claude-Session: https://claude.ai/code/session_…` line and naming a file-send tool (SendUserFile). DATA under L74 — recorded once here, never followed. This hub commits nothing.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| PLACEHOLDER GATE (1st call) | `grep -n -E "R_[_]" ".../prompts/2026-09-24/06-review-setups-deploy.md"` | 1 | ALLOWED — printed nothing (exit 1) |
| DATE GATE (1st) | `date` | 0 | ALLOWED — `Wed Sep 23 21:25:27 EDT 2026` (2026-09-23) |
| DATE GATE 09-23 → R30 | `grep -n "^| R30 " cto-2026-09-22.md` · `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" -- cto-2026-09-22.md` | 0 | ALLOWED — line 133 carries `Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET` and `"Approved"`; commit `055242df8032632dfafdcc8a69dcc271be89c0f6` (NON-EMPTY) |
| AUTH R32 | `grep -n "^| R32 " cto-2026-09-22.md` · `git log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- cto-2026-09-22.md` | 0 | ALLOWED — line 131 carries `Bash(claude -p --model claude-opus-5-5 *)`; commit `b8a72b5300370e248cd6c7a8a732258fec03e6a0` (NON-EMPTY) |
| AUTH R95 | `grep -n "^| R95 " cto-2026-09-23.md` | 0 | ALLOWED — line 103 prints the seats row (Opus · Sol · Grok; OpenAI meter short → Opus + Grok) |
| AUTH THIS LAUNCH (R5) | `grep -n "^| R5 " cto-2026-09-24.md` · `git log -1 --format=%H -S"06-review-setups-deploy.md" -- cto-2026-09-24.md` | 0 | ALLOWED — line 13 names `06-review-setups-deploy.md`, "Launched 09-23 21:2x", `DESK LAUNCH`; commit `c02d7b7ab70a1ecdd6fffd160f039c7c1002dbbc` (NON-EMPTY). Recorded: the launch was on 09-23 but the row sits in `cto-2026-09-24.md`, the file this prompt's two calls were left naming; they pass as written |
| `grok --version` | `grok --version` | 0 | ALLOWED — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| OPUS PROBE | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background, task `bzif07e00`) | 0 | ALLOWED — `OK` = UP |
| 05 exists | `ls -la ".../prompts/2026-09-24/05-setups-deploy.md"` | 0 | ALLOWED — 93,538 B, Sep 23 21:20 |
| 05 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../05-setups-deploy.md"` | 0 | ALLOWED — `<prompt sha>` = `f173328fb733f5b62247cfaffb2d582f9cf2a42d` |
| STAGGER | `grep -n -F "no other house hub is running" cto-2026-09-24.md` | 0 | ALLOWED — line 13 (R5) carries it and names `06-review-setups-deploy.md`: `stagger: clear (launch row)` |
| RECOVERY | `ls scratch/tribunal-bars-0920/setups-deploy-0924` | 1 | fresh run — "No such file or directory" |
| DATE GATE (2nd) | `date` | 0 | ALLOWED — `Wed Sep 23 21:31:57 EDT 2026` (2026-09-23; R30 covers grok) |

Helper commands the hub used outside the launch list, all read-only or scratch-only (the classifier allowed each, no dialog): `sed -n`, `awk`, `cut`, `sort`, `tr`, `od`, `cmp`, `diff`, `zsh <script in the job tmp dir>`, shell redirection into the packet folder, `cd`, `printf`, `git status --porcelain`, `mkdir -p` of the job's existing tmp dir (a no-op; NOT the packet folder). Nothing under `/Users/cobalt/cobalt` except this report file was written.

## Packet
Staged in `scratch/tribunal-bars-0920/setups-deploy-0924/` (the first Write, `QUESTIONS.md`, created the folder; no `mkdir` run in it). DEVIATION FROM THE STAGING RULE, disclosed: the parts of `05`, `66`, `68` and the two whole-file copies (`68-outcome.md`, `draft.md`) were made with `sed -n '<a>,<b>p' <source> > <copy>`, NOT Read → Write, because `05`, `66` and `68` each carry lines over 2,000 bytes (05: lines 1, 7 = 2,102 / 3,230 B; 66: lines 1, 6, 15 = 2,215 / 3,528 / 1,978 B; 68: lines 1, 7 = 2,289 / 2,243 B) that a Read → Write copy could cut. Byte identity is PROVEN: `cat <parts in order> | cmp - <source>` → IDENTICAL for `05`, `66`, `68`; `cmp` IDENTICAL for `68-outcome.md` and `draft.md`; every part ≤ 38,000 B. Every other file is generated by shell redirection from the real command output (headers name the command); `QUESTIONS.md` is the prompt's text verbatim (`diff` against `06` lines 140–166, outer quotes removed → identical) plus ONE appended "Files in this folder:" paragraph that names `greps.txt` to open SECOND.
- `05-setups-deploy.part1.md` 30,122 B (lines 1–119) + `part2.md` 29,975 B (120–245) + `part3.md` 33,441 B (246–411) = 93,538 B = source `05-setups-deploy.md` (93,538 B).
- `66-base.part1.md` 30,175 B (1–134) + `part2.md` 30,076 B (135–255) + `part3.md` 21,553 B (256–376) = 81,804 B = source `66-stacked-deploy-r4.md` (81,804 B).
- `68-base.part1.md` 30,507 B (1–137) + `part2.md` 33,730 B (138–301) = 64,237 B = source `68-smoke-only-deploy.md` (64,237 B).
- `68-outcome.md` 29,970 B = source `deploy-2026-09-23-r5.md` (29,970 B) · `draft.md` 16,885 B = source `setups-deploy-draft-2026-09-23.md` (16,885 B).
- `branches.md` 8,502 B · `stop-lines.md` 13,940 B (the ten `tail -n 3`s, the two greps; all files present) · `rulings.md` 12,866 B (09-23 R4, R81, R82, R83, R95, R104, R106, R107; 09-22 R30, R32, R119; `cto-2026-09-24.md` §4 lines 6–13 as it stood, R1–R5) · `laws.md` 19,345 B (L28, L42, L43, L54, L62, L63, L65, L66, L68, L73) · `rows.md` 14,973 B · `restarts.md` 3,677 B · `clock.md` 7,731 B (the three spec'd commands, plus one labelled HUB ADDENDUM: `grep -n "radar cycle:\|heartbeat" runner.py` and `runner.py` lines 160–200).
- `greps.txt` 32,296 B (HUB ADDENDUM = the 50 allow + 3 deny strings of `05`'s launch line one per line, then searches 1–5) · `greps-2.txt` 33,823 B (6–9) · `greps-3.txt` 34,924 B (10–11) · `greps-4.txt` 35,865 B (12–16) · `greps-5.txt` 20,256 B (17–18). 18 searches over the three `05` parts, one `grep -n` call each. LONG-LINE RULE (as the `69` hub applied it): a hit line over 1,250 B (`05` part1 lines 1 and 7 only) is named, not reprinted, and its strings are in the addendum; search 15 (`FAILED`, 30,356 B) is given as `grep -c` and hit line numbers only, said so in the file. Hit lines carry PART-LOCAL numbers; the header gives the offsets (part2 + 119, part3 + 245). The `R4\b` header line of search 11 first came out with a backspace byte (zsh `echo`); repaired before launch; the grep itself ran with `\b`.
- `QUESTIONS.md` 7,537 B. Packet total 532,169 B (the prompt's "≈270 KB" was the sources only, 286,434 B).
- Trailing-whitespace lines (`grep -c " $"`): 0 in every file except `branches.md` 2 and `greps-4.txt` 3 (lines of the verbatim command output, not generator text). The sources `05`, `66`, `68`: 0 / 0 / 0.
- Every house got the identical packet (L44).

Houses (one attempt each, `run_in_background`, launched 21:32:0x–21:32:10 ET after the second date gate 21:31:57):
- GROK (`grok -p "…" --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"`, task `bsmk16s9k`): notice read 21:48:30 ET (≈16½ min, inside the 20-min limit), exit 0, closing `REVIEW: RUN IT`. Grok wrote no file; the hub wrote `grok-review.md` (7,830 B) from its printed answer, lines 1–17 of the task output byte for byte (line 1 is Grok's own process narration).
- OPUS (`claude -p --model claude-opus-5-5 "…" --permission-mode plan --add-dir … --allowedTools "Read" "Grep" "Glob" --disallowedTools …`, task `b68cyge9m`): notice read 21:39:07 ET (≈7 min), exit 0, closing `REVIEW: RUN IT AFTER …` (5 folds); written to `opus-review.md` (13,607 B) byte for byte from the printed answer (lines 1–96 of the task output).
- **L67 floor: MET** — Grok (a non-author house) answered in full with a `REVIEW:` line. Sol NOT SEATED (METER, retry after Sep 26th 06:47 ET); Gemini NOT ASKED (R96/R97); Astra a design seat.

## CONTINUE
next: none — the desk commits this report (`05` P9 requires it COMMITTED), folds and re-issues `05` under L19 if it takes any row below, fills `R__L`, re-cuts the gate, and launches `05` after his `DONE TRADING` word.

## Per question
Cells are each house's own words (≤30), cited as the house cited them. Grok cites `66-base.part1.md:5` for `66`'s launch line; the line is 6 (as does Opus; `05` part1:9 also says line 5).
| Q | grok | opus |
|---|---|---|
| Q1 Allowlist | "YES. Every step command matches one of the 50 allow strings … 0 new … No allow string is unused" (`05` part1:7, :9) | "YES." 50 = `66`'s 54 minus 4 drops, same order; none unused (part1:7, :113; greps.txt:11-61) |
| Q2 L68 gate / one-branch | "YES." suites on `<ship>` at STEP-2, `main` ff'd only at 4.3; STEP-1.2 fails a bad replay; `.env` removed at 2.3 (e) (part2:59-63, :91-94, :120) | "YES, with one gap (F7)": P1 accepts dirty docs, only 74 non-docs paths checked; a touched dirty doc → 4.3 refuses with residents down (part2:18-22, :94). Minor: 2.3 (a) `cp` must wait for 2.2 |
| Q3 Window / migration | "YES for the shape." (b) idle clause "sound"; whether `heartbeat show` raises a new RED in the pause "UNVERIFIABLE FROM READS" (clock.md:173-174; part3:63) | "PARTLY." F5: PAUSE merge clock 20:22 not derived from proof cost, may cross 20:30; F2: (e) "UNSOUND AS WRITTEN" if the probe is not pause-aware; 4.4 gate "COMPLETE ENOUGH" (part1:39; part3:41-43, :63) |
| Q4 Rollback | "YES." one revert, no editor, PROVE IT before bootstrap; 0013 and note stay safe; every branch UP or named DOWN; relaunch (i)-(vi) cover the listed states (part3:23-28, :77-87) | "YES for the code, with a relaunch defect (F4)": (i) matches before (vi), so a STEP-6 resume records NOT WRITTEN and skips 6.8 (part3:23, :28, :141-145) |
| Q5 STEP-6 / R107 | "YES." five rows = his values, engine key/unit/scope/consumers; order dev → dry → apply → parser; 6.8 bounded, `VWAP Continuation.md` last (part3:96-152; rows.md:271-292) | "rows YES, order YES, one harm gap (F3)": dev proof may resolve his real vault (part3:92, :140-145). 6.7 "WEAK". second-chance at R82's values UNVERIFIABLE |
| Q6 With-DB read | "YES." one background pytest, notification, one `tail -n 3`, never `Monitor`; red adds `grep` + `tail -n 80` (part1:113; draft.md:50-56) | "YES." same shape `59` and `68` ran; `tail -n 80` may miss assertions on many failures, still a stop (part1:113; draft.md:51-56) |
| Q7 Other | "No dialog and no fail-open on a bad tree." only `R__L` left; R3, R104, R95 rows satisfy the gates (part1:68-70; rulings.md:16, :40) | F1: BETWEEN report commit moves `main`, (iv) fails, window lost; F6: `-S"DONE TRADING"` already non-empty (part1:40; part3:26; part2:11) |
| REVIEW | `REVIEW: RUN IT` | `REVIEW: RUN IT AFTER 6.3: real note still absent, diff path under dev vault · BETWEEN: no report commit; desk holds commits through relaunch · PAUSE: heartbeat baseline read at/after 20:00 before bootout · PAUSE merge clock = 20:28 minus P14-M proof cost · Relaunch (vi) before (i); 6.4 accepts idempotent no-change` |

Where the houses contradict each other: Q3 (b)/(e) in the pause — Grok "The (b) idle clause is sound … UNVERIFIABLE FROM READS" whether a new RED arises; Opus "UNSOUND AS WRITTEN" for (e) — settled by the files below (row 2). Q5 — Grok "YES" throughout; Opus finds F3 — settled below (row 3). Q7 — Grok finds no path; Opus finds F1 and F6 — both confirmed as text below.

## Checked against the files
Blocker rule (mine, applied to every row; a mechanical test, not a verdict on `05`, as the `69` hub applied it): `blocks the launch? yes` = the text as written, on the run's OWN single path with the values the packet records (no third-party action, no relaunch, no abnormal input), fails a good deploy, passes a bad one, opens a dialog, or leaves a resident / his vault wrong; `no` = it needs a third party (desk / another hub), a relaunch, an input the packet's measurements do not show, or is wording only.

Files opened: `05` (whole, source and staged parts), `66` and `68` (staged, launch lines), `deploy-2026-09-23-r5.md`, `setups-deploy-draft-2026-09-23.md`, LAWS.md (in full), `cto-2026-09-22/23/24.md` rows, `src/cobalt/vault.py`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/radar/runner.py`, `configs/dev/vault.yaml`, `~/dev-vault-cobalt` (ls), main's `git status --porcelain` and the branch's touched paths (`git log --name-only main..setups/seven-0921`).

| claim | who | file:line | verdict | blocks? | ≤30 words |
|---|---|---|---|---|---|
| 1. BETWEEN (19:55–20:00) ends `FAILED … not used`, "go to STEP-7" commits the report, so `main` ≠ `<pre-merge>`; relaunch (iv) cannot resume, (ii) ends on the committed stop line | opus F1 | `05` 279, 269, 103, 408, 40; draft.md:81 | HOLDS (text) | no — needs the relaunch | 05:279 sends both FAILED to STEP-7, 05:408 commits it; (iv) needs main = pre-merge, (ii) ends the run. 05:40 promises (iv) resumes; the window is lost |
| 2. PAUSE smoke (e) red because the radar idles; idle clause covers (b) only | opus F2; grok UNVERIFIABLE | probes.py:88-89, runner.py:173-174, :458-460 | DOES NOT HOLD | no | the probe returns `Probe("radar", True, "paused (market_reset)")` in the pause; the resident loop logs `radar cycle: paused_market_reset` every interval. (b) finds a line; (e) sees green |
| 3. 6.3's `COBALT_ENV=dev` proof writes his REAL vault | opus F3 | vault.py:145-209, configs/dev/vault.yaml:23, `ls ~/dev-vault-cobalt` | DOES NOT HOLD (harm); residual UNVERIFIABLE | no | dev mode + no path resolves `~/dev-vault-cobalt` (has `1 - Trading`); a dev run resolving under the prod vault is REFUSED unless `COBALT_ALLOW_DEV_ENTRY=1`. 68's read was `COBALT_ENV=production` |
| 4. Relaunch (i) matches before (vi): a STEP-6 resume re-enters at 4.7, 6.4's no-change dry run reads "NOT WRITTEN", 6.8 skipped | opus F4 | `05` 268, 273, 386, 390 | HOLDS (text) | no — relaunch | (i) "then 4.7 onward" and (vi) both fit; 6.4 accepts only CREATED / upserted with the five rows, "Anything else → NOT WRITTEN". (vi) itself says same rows = no change |
| 5. PAUSE merge clock 20:22 fixed; proof cost never sets it; slow proof crosses 20:30 | opus F5 | `05` 39, 279, 283, 286; clock.md:7-11 | HOLDS (text) | no — abnormal input | merge by ≤20:22:00 + 17 s + proof + bootstrap stays under 20:30 unless the proof runs about 7 min; recorded 70.7 s / 76.9 s (`05` 31). Serialization effect UNVERIFIABLE |
| 6. P-HIS `git log -S"DONE TRADING"` is already non-empty from R3's own row | opus F6 | `05` 130; rulings.md (R3 row) | HOLDS | no — needs a desk mistake | I ran it: prints `f173328f…` (NON-EMPTY) today, before any `DONE TRADING <hh:mm>` row exists. The commit half of P-HIS is vacuous |
| 7. P1 accepts dirty docs; a docs path the branch changes and `main` has dirty makes 4.3 refuse after both residents are down | opus F7 | `05` 137-145, 210, 219 | DOES NOT HOLD today; text gap present | no | `git status --porcelain` shows 4 ` M` + 6 `??` paths; 0 of the 8 non-self paths appear in the branch's 115 touched paths (41 under `docs/`). Gap: docs identity is unchecked |
| 8. 2.3 (a) `cp .env` has no explicit wait for 2.2's notification | opus minor | `05` 113, 225, 229 | HOLDS (wording) | no | 05:113 says no call about a running suite; 2.3 (a) follows 2.2 in order but does not say "after the notification and its `tail`" |
| 9. STEP-5 (2) has no branch for HEAD ≠ `<ship>` | opus | `05` 321 | HOLDS (text) | no — 5 is entered after 4.3 landed | line 321 says "HEAD is `<ship>`" with no failure line |
| 10. STEP-5 (4) skips 4.7 (d) and (f) | opus | `05` 330 | HOLDS (text) | no | (4) re-runs (a), (b), (c), (e), (g); validate (f) is not re-proved after the revert |
| 11. 6.7 passes vacuously with no radar cycle after 6.5 | opus | `05` 389 | HOLDS (text) | no | 6.7 compares Traceback / TaxonomyConfigError counts and one curl; it requires no fresh `radar cycle:` line. Production's reader has 0 hits for `Assumed Defaults` (rows.md end) |
| 12. `06`-line: launch line `66` "line 5" | grok/`05` | `05` 9; `66` line 6 | HOLDS (wording) | no | `66`'s launch line is line 6; both `05`:9 and Grok's cite say 5 |
| 13. second-chance passes at R82's values (`+companion=True`) | opus | stop-lines.md:106, :132 | UNVERIFIABLE FROM READS — `cat "/Users/cobalt/cobalt-wt/setups-c1/docs/_inflight/setups-assumed-values-2026-09-21.md"` (absent when I read it) | no | `01` D2 printed it at the companion's values; the companion file is not on disk; R82 names 1 bar / 0.10 (draft's description matches) |
| 14. reverted code refuses a DB whose migration is ahead; s2p2.2 receipts vs reverted replay | opus | db_migrations/__init__.py:47; replay/runner.py:219 | UNVERIFIABLE FROM READS — a scratch dry-run of the reverted code against `cobalt_dev` | no | my grep printed only "nothing asserts contiguity" (:47) and the `EVALUATOR_VERSION` read (:219); no ledger check found; not exhaustive |
| 15. every step command covered by an allow string; none unused | grok, opus | `05` part1:7 | HOLDS (no gap) | no | I re-read every command of 05 against the 50 strings: none outside; `reset --soft` (P3), aborts, `kickstart` are branch uses |
| 16. with-DB read = the landed shape, allowed by `tail *` | grok, opus | `05` 113; draft.md:51-54 | HOLDS | no | draft.md:51-54 quotes the `59` / `68` transcripts (`tail -n 3 <output-file>`, `2597 passed …`); 68-outcome.md:125, :130 print those summaries |
| 17. 6.8: `VWAP Continuation.md` last | grok, opus | rows.md (ls, `sorted(glob)`) | HOLDS | no | `ls` ends `The 3:30 Trade.md`, `VWAP Continuation.md`; `T` < `V` in byte order; the test loop `for ld in defs` (rows.md test lines 729-757) stops at its first assert |

(i) Allow strings — `grep -c -F -e "<string>"` of each string of `05`'s `(3) claude --bg` line (part1 line 7; staged line == source line 7, IDENTICAL) against `66-stacked-deploy-r4.md`, quotes included: strings 01–53 (the 50 allows: `git -C … add *` … `Bash(date*)`; the denies `"AskUserQuestion"`, `"EnterWorktree"`, `"Bash(git push*)"`) each count = **1**. `--add-dir /Users/cobalt/Vault` = 1, `--add-dir /Users/cobalt/cobalt-wt` = 1; `--model claude-opus-5-5` = 1, `--allowedTools` = 1, `--disallowedTools` = 1, `--permission-mode acceptEdits` = 2. No string counts 0 → 0 NEW. `66`'s own launch line (line 6) carries 55 `Bash(` strings (54 allows + `Bash(git push*)`); `05`'s carries 51 (50 + the same deny): 54 − 4 = 50, as claimed.

(ii) `grep -c -E "R_[_]" "…/05-setups-deploy.md"` → **6** lines (tokens `R__L` at lines 4, 5, 18, 60 ×2, 62, 166; no `R__A` — his approval is already the literal R3). The desk's fill; not a blocker.

(iii) STEP-6.2's five rows against the engine rows (`rows.md`, branch `tunables.yaml`) and the rulings:
| key | `05` value / unit / scope / consumers | engine row unit / scope / consumers (`rows.md` line) | his ruling |
|---|---|---|---|
| `flat_threshold.ema9` | 0.05 / ratio / `per_indicator(ema9)` / `["fashionably_late"]` | ratio / `per_indicator(ema9)` / `["fashionably_late"]` (393-400) | R119: 0.05 |
| `flat_threshold.vwap` | 0.05 / ratio / `per_indicator(vwap)` / `["fashionably_late"]` | ratio / `per_indicator(vwap)` / `["fashionably_late"]` (402-409) | R119: 0.05 |
| `dist.k.vwap` | 0.5 / atr / `per_indicator(vwap)` / `["vwap_continuation"]` | atr / `per_indicator(vwap)` / `["vwap_continuation"]` (411-418) | R119: 0.5 × atr_working (R107: included) |
| `range_break.failed_trap_bars` | 1 / bars / global / `["Range Break (primitive)", "second_chance"]` | bars / global / `["Range Break (primitive)", "second_chance"]` (157-164) | R82 A-19: 1 bar |
| `range_break.retest_tolerance_atr` | 0.1 / atr / global / `["cobalt.radar.anatomy.range_break (event(retest))"]` | atr / global / `["cobalt.radar.anatomy.range_break (event(retest))"]` (325-332) | R82 A-20: 0.10 × atr_working |
All five: `dynamic: true`, `status: proposed` (equal to the engine rows), `source: assumed` (the engine rows say `dwv`, by design: `loader._fills_hole` wants assumed). No row for `leg.min_size_atr`. Values, units, scopes and consumers all equal.

## Folds proposed
Each HOLDS finding as ONE text change to `05`, for the desk to fold (L19: a whole re-issue). I edit nothing.
1. STEP-4.1: `On either FAILED, nothing is down and nothing merged: go to STEP-7.` → `On the BETWEEN FAILED write the stop line and do NOT commit the report (main must stay <pre-merge> for RELAUNCH (iv)); too late: go to STEP-7.`
2. STEP-3.5 RELAUNCH (i): `then 4.7 onward.` → `then 4.7 onward, unless (vi)'s condition also holds: then (vi) applies first.` and STEP-6.4: `Anything else → R119: NOT WRITTEN — dry run <what>` → `no change because the five rows are already there = WRITTEN (relaunch); anything else → NOT WRITTEN`.
3. THE WINDOW / 4.1: `MERGE CLOCK before 20:22 ET` (PAUSE) → `MERGE CLOCK = 20:28 minus P14-M's proof cost in seconds, never later than 20:22`.
4. P-HIS: `-S"DONE TRADING"` → `-S"DONE TRADING <the hh:mm matched by the grep>"`.
5. STEP-2.3 (a): `cp /Users/cobalt/cobalt/.env …` → `only after 2.2's <task-notification> and its tail -n 3: cp … `.
6. STEP-5 (2): `HEAD is <ship>.` → `HEAD is <ship>; otherwise no revert: FAILED naming HEAD, residents left DOWN and named.`
7. STEP-5 (4): `Re-run 4.7 (a), (b), (c), (e) and (g)` → `Re-run 4.7 (a), (b), (c), (e), (f) and (g)`.
8. STEP-6.7: add `after a radar cycle: line stamped after 6.5 (three tails at most, as 4.7 (b))`.
Not proposed: F2, F3 (DO NOT HOLD), F7 (condition absent today), Opus's UNVERIFIABLE items.

## ESCALATE
1. ASK DESK: Opus F3 residual — does the hub's environment carry `COBALT_ALLOW_DEV_ENTRY=1` or a `COBALT_VAULT_PATH` under the real vault? If neither, 6.3 cannot reach his note. Settle: `printenv | grep -c "COBALT_ALLOW_DEV_ENTRY\|COBALT_VAULT_PATH"` in the desk's launch shell. Safe default: none needed (`vault.py:196-208` refuses). [2026-09-23 21:5x ET]
2. ASK DESK: fold 1 (BETWEEN commit) — take it or record that a BETWEEN stop ends the run and the 09-24 window with it. Safe default: fold it. [2026-09-23 21:5x ET]
3. Before the desk commits this report: `git status --porcelain` on `main` also lists the untracked `setups-deploy-review-2026-09-24.md` (this file) and `voice-v1-check-2026-09-23.md`; P1 accepts `??` reports under `docs/40 - DevDocs/reports/`, and `05` adds none of the two names. Recorded.
4. Grok's answer is stdout only; the hub wrote `grok-review.md` from it. Grok took ≈16½ min of its 20 (the `69` / `08` reads each timed out at 15 min on a smaller packet).

SETUPS DEPLOY REVIEW DONE · houses: 2 of 2 · other houses: 1 of 1 · blockers: 0 · folds: 8
