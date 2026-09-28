# SETUPS DEPLOY — DRAFT (the 09-24 deploy of `setups/seven-0921` + its house read) — 2026-09-23

Seat `setups-deploy-draft-0923` · Opus 5.5 · prompt `prompts/2026-09-23/76-draft-setups-deploy.md` · launch row R107. This seat is read-only on the repo, the vault and the DB, makes no git write and no launch, and writes only with the Write tool. It wrote three files: `05`, `06` and this report. Prompts were written by 21:16:29 EDT (`date`).

## §0 Headline
- I wrote `prompts/2026-09-24/05-setups-deploy.md`. It uses `68`'s one-branch shape (rebase-then-ff, rollback = `git revert <pre-merge>..<ship>`) and `66`'s setups legs (migration 0013, the live-note proof before STEP-6, snapshot). STEP-6 writes FIVE rows (R119 ×3 incl. `dist.k.vwap` per R107, R82 ×2). A new 6.8 re-runs the live-note suite, with vwap-continuation's `assert forms` as the one EXPECTED RED. The window is DAY (<19:55, R83) or PAUSE (20:00–20:20, the law), picked by the clock.
- I wrote `prompts/2026-09-24/06-review-setups-deploy.md`: `69`'s shape, Opus 5.5 + Grok (R95), launch line = `69`'s minus `Bash(agy *)`.
- New rule strings: **0**. `05` uses 50 of `66`'s 54 allow strings plus the 3 denies. I checked this by machine: 0 not in `66`, and exactly 4 s2-smoke strings dropped. `06` uses 9 of `69`'s 10 allow strings plus the 3 denies (only `agy` dropped).
- WITH-DB READ: a precedent exists (`59` r3 and `68` r5 transcripts): run in the background, wait for the task notification, then ONE `tail -n 3 <output-file>`. It is copied verbatim.
- ESCALATE: 12. It includes 4 ASK DESK items: R52's reach, R28's reach for `06`, the "normal rollback rule" reading, and the PAUSE-window smoke.

## L74
One block arrived beside the first tool result of this session, the Bash `cat` of the `76` prompt. It asked for a `Claude-Session: https://claude.ai/code/session_…` line on commits and PR bodies and named a file-send tool. Under L74 it is DATA and I did not follow it. This seat makes no commit.

## Delta — every row of both sources
Source A = `reports/second-chance-fix-draft-2026-09-23.md` `## DEPLOY DELTA` rows 1–20 (written against `59`). Source B = `reports/setups-fix-r2-draft-2026-09-23.md` `## FOR THE DEPLOY` 1–7 (which amends A). Where A said "from `59`", `05` is built from `66`/`68`, which already carry `59`'s lines.

| # | source row (short) | disposition | in `05` / `06` |
|---|---|---|---|
| A1 | new run: prompt, seat, report path, commit subjects → 0924 | CARRIED | `05-setups-deploy.md` · `setups-deploy-0924` · `reports/deploy-2026-09-24.md` · subject `docs(report): deploy 2026-09-24 setups — …` |
| A2 | setups ONLY; every smoke line goes; smoke rebase + gate merge strings "CARRIED UNUSED" | CARRIED, one change | Every smoke line is gone. The 4 smoke/main-into-gate strings are DROPPED from the line, not carried unused. That follows `68`'s precedent (it dropped 14 unneeded strings). Dropping is a subset, so still 0 NEW. |
| A3 | `68`'s shape: gate ff onto the rebased branch, `main` `--ff-only`, rollback `git revert --no-edit <pre-merge>..<ship>`, 0013 STAYS | CARRIED | THE SHAPE; STEP-1.3, 4.3, STEP-5 (2)/(2b) |
| A4 | window: DATE 09-24; R5 was 09-23 only; the pause variant 20:00–20:30 | CARRIED, resolved by R83 | DAY (R83) HARD <19:55 / MERGE <19:58. PAUSE (law, no override) HARD 20:00–20:20 / MERGE <20:22, which clears the 20:30 archiver. Between the two, or later → FAILED with nothing down. A relaunch resumes at 4.1 (RELAUNCH (iii)/(iv)). |
| A5 | P-HIS reads the 09-24 desk row | CARRIED | P-HIS: `grep -n -E "DONE TRADING [0-9]{1,2}:[0-9]{2}"` + `-S"DONE TRADING"` on `cto-2026-09-24.md`. It is a literal match, not a row number, because the row number is unknown. |
| A6 | AUTHORIZATION: does R52 span 09-24? ASK DESK; + R79 + the `02` DONE line | CHANGED | His approval of the line = placeholder **R__A** (a row of his in `cto-2026-09-24.md` naming `05`), not R52. ASK DESK 1. Checked in AUTHORIZATION: R83, R4, R104, R119, R82, R107. R79 is NOT gated: R83 and the check lines supersede it. The `02`/`04` lines are in P6. |
| A7 | tags `deploy-2026-09-24`, `pre-setups-0924` | CARRIED | P4, 3.5; scratch probe tag `scratch-allow-probe-0924s` |
| A8 | P5: `01`'s BUILT line → `<setups tip>` | CHANGED (by B2 / R104) | P5 reads four builds. It reads `01`'s `SETUPS LIVE NOTE FIX BUILT` line for `<c9 tip>` and `<ln base>`. `<setups tip>` comes from `03`'s EXACT `FAILED: D5b …` line, which is accepted only with R104 (the same amendment the desk made to `04`'s gate). It also greps `03`'s D4 and offline summaries. `64`'s FAILED report is not read (superseded). |
| A9 | P6: `02` DONE, ≥3 YES, HOLD 0 | CHANGED (by B2 / R95) | `02` round 1 is recorded with its HOLD 1. `04` round 2 is the gate: YES ≥2 (R95: Opus + Grok) and HOLD 0. |
| A10 | P7: dev at 0013, (b3) idempotent re-walk, lock read `ls -la …/*/.env` | CARRIED | P7, 2.3 (b2)/(b3) |
| A11 | P9: its own house read (≥1 non-Anthropic; grok extension) | CARRIED | P9 reads `setups-deploy-review-2026-09-24.md`, which must show `other houses: 1 of 1` (Grok) and blockers 0 (or blockers folded, per R__L). The review prompt is `06`. |
| A12 | P11 identity: `<ln base>..<setups tip>` = the four test files; `<nse>` recorded | CARRIED, split | `<ln base>..<c9 tip>` = the 4 files, and `<c9 tip>..<setups tip>` = `test_radar_evaluate.py` only. The seam and r4 identities are kept. `<nse>` is recorded, expected 42 (`git rev-list --count main..setups/seven-0921` = 42 at 21:0x). |
| A13 | P12: gate must not be `f2dd42cb` / `c7b098e7` | CHANGED | P12 now requires `main` == `<main-at-gate>` (`68`'s rule). This also catches a gate never re-cut: it still sits at `68`'s `4e4577c3`, and main has moved. |
| A14 | 1.3 / 1.4: 74 files; the rebase replays over the smoke fix's `test_replay_runner.py` | CHANGED (new proof) | Main moved NON-DOCS (10 smoke paths, `git diff --stat 797fdd2f main` at 21:0x), so `68`'s tree-wide identity cannot hold. STEP-1.2 proves it in four parts: (1) identity excluding the 10 smoke paths; (2) the branch leaves 9 smoke paths untouched; (3) the shared file's diff vs main is EXACTLY the two `s2p2.1`→`s2p2.2` pairs, the same as `git diff 797fdd2f df7817a6`; (4) `74 files changed`. |
| A15 | P1 REFUSED `??` + the new build reports | CARRIED | 9 paths, from `git diff --name-only --diff-filter=A main...setups/seven-0921` under reports/. Also accepted as dirt: ` M docs/30 - Design/archiver-runs.md` (seen in today's status; not a branch path). |
| A16 | P14: `s2p2.2` → 0; `unranked_rows` ≥1; replay baseline | CARRIED | P14 markers, plus `<an0>`: `grep -c -F "Assumed Defaults"` on production's `vault_loader.py` = 0. STEP-5 (2c) relies on it. |
| A17 | 2.3 (d) five `AWAITING` lines | CARRIED | Verbatim from `03` D4 (`setups-fix-r2-build-2026-09-24.md:117-122`). |
| A18 | STEP-6 R119's three + A-19/A-20 if he rules owner item 1 | CHANGED (R82 ruled "A"; R107 keeps `dist.k.vwap`) | The rows file has 5 rows. A-19 is `value: 1`, `unit: bars`, `scope: global`. A-20 is `value: 0.1`, `unit: atr`, `scope: global`. Both use the engine rows' consumers (`tunables.yaml:157-164`, `:325-332` on the branch). The 6.1–6.5 strings are unchanged. |
| A19 | NEW 6.6: the live-note run after 6.5; red = not a rollback; ASK DESK adopt | **CHANGED-by-R107** | ADOPTED as **6.8**. EXPECTED RED on vwap-continuation's `assert forms`, recorded `R119 live-note: RED (expected, R107) — <assertion>` under `## KNOWN RED`, never a rollback. ANY OTHER red → ESCALATE + "the normal rollback rule" = STEP-5 with the note staying (2c), ASK DESK 3. It runs in the gate worktree (`<ship>`) WITHOUT `.env`, not from `~/cobalt`. New 6.7 re-reads the residents after the note lands. |
| A20 | STEP-7 ESCALATE: + `01`/`02`; scratch cleanup; S2 lines out | CARRIED | STEP-7 (4): prints-0923 / prints-0924 / seam-0923 + stale-marker scratch; no S2 lines |
| B1(a) | 2.3 (d) before STEP-6: both engine-fill pins hold, same five lines | CARRIED | 2.3 (d) |
| B1(b) | the post-STEP-6 run (6.6), expected RED, not a rollback | **CHANGED-by-R107** (adopted, "A") | 6.8, as A19 |
| B1(c) | the consequence stated: every later GATE EARLY / L68 live-note leg shows the red until a fix lands | **CHANGED-by-R107** (named KNOWN RED) | STEP-7 (3) `## KNOWN RED` text: it names the 09-25 vwap fix round and `03`'s VWAP row (`+R119=False · +R119_but_dist.k.vwap=D5=True · +D5_but_dist.k.vwap=R119=False`) |
| B2 | P5/P6: `<setups tip>` from `03`; `04` ≥2 YES, HOLD 0; round 1 in the chain | CARRIED | P5, P6 (as A8/A9) |
| B3 | P11 `<nse>` recorded, not predicted | CARRIED | P11 records it (expected 42); 1.2 compares against it |
| B4 | P1 `??` + `setups-fix-r2-build-2026-09-24.md` | CARRIED | in P1's 9 |
| B5 | deploy-prompt read: Opus + Grok (+ Sol if back); own grok row naming the read | CARRIED | `06`, with its date gate: 09-23 → 09-22 R30; 09-24 → placeholder **R__G**, his row naming `06` (ASK DESK 2) |
| B6 | cleanup + `prints-0924` | CARRIED | STEP-7 (4) |
| B7 | window: R83 → `DONE TRADING <time>` row | CARRIED | P-HIS, THE WINDOW |

## WITH-DB READ
- **The precedent.** The landed deploys ran the with-DB suite like this. Evidence is the hub transcripts, read by this seat: `-Users-cobalt-cobalt/17216d15-….jsonl` (`59` r3) and `69086b52-….jsonl` (`68` r5). Both ran under `acceptEdits`:
  1. One Bash call, `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy`, with `run_in_background: true`. The tool answered `Command running in background with ID: … Output is being written to: /private/tmp/claude-501/-Users-cobalt-cobalt/<session>/tasks/<id>.output`.
  2. NO further call about the run until the harness delivered a `<task-notification>` naming the `<output-file>`, `<status>completed</status>` and `(exit code 0)`. `59`'s hub wrote its report meanwhile; `68`'s did nothing.
  3. ONE call, `tail -n 3 <that output file>`. It matched `Bash(tail *)` and printed the summary: `2849 passed, 6 skipped, 1 xfailed, 15 warnings in 628.42s` (r3) and `2597 passed, 6 skipped, 1 xfailed, 15 warnings in 204.78s` (r5).
- **Where it is in `05`.** UNATTENDED RULES "THE WITH-DB READ" copies this verbatim. It applies to 2.2 and 2.3 (c), and it forbids `Monitor`, Read-polling, sleep and waits. On a non-zero exit it adds `grep -n -E "^(FAILED|ERROR) " <file>` and `tail -n 80 <file>` (both under `Bash(grep *)` / `Bash(tail *)`), so each red test is named. `68`'s rule only said "name each test" without a read to do it.
- **Why `03` failed.** `03` was an AUTO-mode build. It added a `Monitor` `until grep …; do sleep 10; done` loop that was not in its list, and the classifier denied it as `[Credential Leakage]`. The deploy runs in `acceptEdits` with no classifier in that position, and the precedent read uses no `Monitor`. Precedent exists, so no ESCALATE 1 is raised for a missing precedent.
- **R104's OPS item** ("why reading the with-DB output trips `[Credential Leakage]`") is still open for AUTO-mode builds. Under R81 (1) every build runs with-DB, so they should use the same notification + ONE `tail` shape. `03`'s own `## CONTINUE` already names it. It does not block this deploy.

## FOR DEJAN — one list
1. **Approve `05`'s launch line** as his row **R__A** in `cto-2026-09-24.md`. The line has 50 allow strings, all of them strings of `07`'s list, which he approved 09-23 (R52, "Approved all commands you need"); 0 new. With it he approves the production migration `0013` and the STEP-6 vault write of the five rows (R119 ×3 as ruled, `dist.k.vwap` kept by R107; R82's A-19 = 1 bar, A-20 = 0.10 × ATR). Not needed only if the desk rules that R52 spans 09-24 (ASK DESK 1).
2. **"Done trading"** on 09-24. The desk writes `DONE TRADING <hh:mm>` (R83).
3. **The window, for his sight.** The DAY window runs until 19:55 (merge by 19:58), under his R83. If the gate runs late, the PAUSE window runs 20:00–20:20 (merge by 20:22) under the law, with no override. The 20:20 / 20:22 cutoffs are this drafter's derivation to clear the 20:30 archiver (≈17 s + ≈77 s proof + bootstrap).
4. **Grok for `06` on 09-24.** `Bash(grok *)` through 2026-09-24 23:59 ET for `prompts/2026-09-24/06-review-setups-deploy.md`, as his row **R__G**. Not needed if `06` launches before 23:59 tonight (09-22 R30 covers it), or if the desk reads his 09-23 R28 as covering it (ASK DESK 2).
5. Later, not in `05`: the desk's `cobalt taxonomy load` job, which puts the five rows into the radar's DB copy on his word.

## ESCALATE
1. **ASK DESK: R52's reach [21:16].** Does 09-23 R52 ("Approved all commands you need", for `07`'s list) cover a 09-24 launch? `68` used it the same day. Safe default, which `05` uses: his fresh row R__A.
2. **ASK DESK: `06`'s grok window [21:16].** 09-23 **R28** reads: "`Bash(grok *)` and `Bash(agy *)` run rules EXTENDED through 2026-09-24 23:59 ET … for every house-lane hub". R82 (16:3x) itself said "Owner item 2 (grok / agy through 09-24) is ALREADY his R28". Yet R94 and R104 later asked him per prompt. The `76` prompt tells me to gate on a named row, so `06` does (R__G). If the desk reads R28 as covering `06`, it re-issues `06`'s DATE GATE to cite R28 (L19).
3. **ASK DESK: "the normal rollback rule" (R107) [21:16].** `05` 6.8 reads it as: an OTHER red is a red row → STEP-5 (code revert, 0013 stays), and the note STAYS (2c).
   - Why the note staying is safe: production's pre-deploy `vault_loader.py` has no `Assumed Defaults` / `ASSUMED` (grep, 21:1x). `ADDING-A-SETUP.md`'s order binds only after `taxonomy load`, and `05` never runs it.
   - The alternative reading is "ESCALATE only, no revert". The desk decides; `05` stands as written until then.
   - An UNEXPECTED GREEN is ESCALATED only.
4. **ASK DESK: the PAUSE-window smoke [21:16].** In 20:00–21:00 the radar may idle, so 4.7 (b)'s fresh `radar cycle:` line may not come. `05` accepts that as not-red only if the heartbeat reads `running … heartbeat fresh` twice.
   - Whether the heartbeat stays fresh in the pause is UNPROVEN (L70). `06` Q3 asks, with `clock.md`'s `market_reset` greps.
   - Safe default: aim for the DAY window. The gate takes ≈25–30 min (offline ≈8, with-DB ≈4–11, live-note, P14-M ≈77 s, backup), so launch by ≈19:10.
5. **L43, one branch.** `05` is correct only if no OTHER branch is BUILT and CHECKED by his word (voice V1 `44` is checking now; DRC D1, JEV, stale-score and H1 are in flight). The launch row must carry `ONE BRANCH: setups/seven-0921`. Otherwise the desk re-issues from `66`'s stacked shape.
6. **UNPROVEN (L70): the writer and the two global rows.** `cobalt taxonomy assumed write` has never run with a `global`-scope, `bars`-unit or integer row (A-19). 6.3's dev proof decides. If it refuses, ALL FIVE rows are NOT WRITTEN, R119's three included, because it is one file and one string. The deploy stays green; the desk decides a split, which would need a second rows path (a NEW string).
7. **The identity proof is new logic (A14).** Main moved non-docs under the branch for the first time in this chain. STEP-1.2's four-part proof replaces `68`'s tree-wide empty diff. `06` Q2 targets it.
8. **6.8's tree and `.env`.** 6.8 runs in the gate worktree on `<ship>` WITHOUT `.env`, the build's own D1/D4 shape. 2.3 (d) runs WITH `.env` listed (`66`'s shape). It is never run from `~/cobalt`, whose `.env` points at production. Test counts may differ between the two runs; the gates compare failures and `AWAITING` sets, not counts.
9. **The note order proves "every other assertion passed".** T2's loop stops at its first failure, in `sorted(glob("*.md"))` order (`vault_loader.py:491` on the branch). I read the note order at 21:1x (`python3` `sorted` on `1 - Trading/4 - Strategies`): the last note is `VWAP Continuation.md`. `05` P14 re-reads it with `ls`, and 6.8 ESCALATES (UNPROVEN) if it is not last. One caveat: `ls` collation may differ from Python's codepoint sort for these names. `06` Q5 checks.
10. **Timing and size.** `06`'s packet is ≈270 KB, so each house has 20 min (`69`: 15). `05` is ≈94 KB. The 09-23 gate run of `05`'s tree may land between 19:55 and 20:00: `05` then FAILs with nothing down, and the desk relaunches at 20:00 with ONE `CONTINUE:` line.
11. **Placeholders.** `05` has R__L (launch; carries `ONE BRANCH: setups/seven-0921` and the hold) and R__A (his approval). `06` has R__L and R__G. On a 09-23 launch the desk writes `none` for G and points R__L at `cto-2026-09-23.md`. Each prompt's gate greps `R_[_]`.
12. **KNOWN RED hand-off.** After a DONE, the desk carries `05` STEP-7 (3)'s `## KNOWN RED` text into every gate prompt it writes and into the 09-25 vwap fix-round classifier (owed, R107).

SETUPS DEPLOY DRAFTED · prompts: 2 · new rule strings: 0 · window: DAY <19:55 (R83) or PAUSE 20:00–20:20 (law), on DONE TRADING 09-24 · restarts: com.cobalt.aset com.cobalt.radar (predicted; derived at 2.5) · ESCALATE: 12
