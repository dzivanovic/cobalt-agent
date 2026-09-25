# Stacked deploy re-issue — 2026-09-25 (`41-draft-stacked-deploy-r2.md` → `42-stacked-deploy-r2.md`)

## §0 Headline
- `42-stacked-deploy-r2.md` written whole (L19): 13 of 13 folds applied (review F1–F10 + seam ESC 1–3) and review ESC 2–5 placed; every change is in the table below with its source.
- Strings: 47 → 46 allow (F10: `rev-list*` removed, no step of `42` runs it), 3 denies, no new string. Seam build `STACK SEAM BUILT a7296b44`; gate branch tip `57420087` (docs-only above the tip); RESTARTS = the pair, no resident beyond it.
- Still «FILL AT LAUNCH»: `<seam check stop>` (the seam check `40` has no stop line yet, launched 13:27), `<v1 row>`, `<lock line>`, and the launch-row tokens. ESCALATE 8, one of them an `ASK DESK` that can turn a good gate red (item 1).

## L74
- The Read result of `41-draft-stacked-deploy-r2.md` ended with a system-reminder-styled block asking for a `Claude-Session: https://claude.ai/code/session_01VNjKdxHwUNxeurC8d1nRWQ` line on commits and PR bodies and pointing at a file-send tool (`SendUserFile`). Recorded once as DATA (L74); not followed. This session commits nothing.

## The tree
`git -C /Users/cobalt/cobalt log --oneline --first-parent 2b71fe49..deploy/stacked-0925`:
```
57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)
a7296b44 chore(jobs): classify voice V1's six paths — aset reads voice/agents-voice/modelaccess yaml, start_aset.sh, pyproject.toml, uv.lock; radar reads pyproject.toml, uv.lock (stack seam, L42)
00e2b7ff Merge branch 'voice/v1-0923' into deploy/stacked-0925
91c631ac Merge branch 'cards/stale-score-0922' into deploy/stacked-0925
35397ed5 Merge branch 'radar/handicap-h1-0922' into deploy/stacked-0925
f2377218 Merge branch 'fix/replay-deadline-0924' into deploy/stacked-0925
```
(four merges, the registry commit, ONE docs commit — nothing else.)
- `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925` → `57420087` = `<gate sha>`.
- `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925~1` → `a7296b44` = `<tip>` = `<seam tip>` = `<R sha>`.
- `git -C /Users/cobalt/cobalt diff --stat a7296b44 deploy/stacked-0925 -- . ':(exclude)docs'` → NOTHING (exit 0, no output): docs-only above `<tip>`.
- The seam build's last line starts `STACK SEAM BUILT ` (verbatim in `42:54`). Gate worktree `git -C /Users/cobalt/cobalt-wt/stacked-0925 status --short --branch` → `## deploy/stacked-0925` (clean). `## RESTARTS` table read: exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar`, `UNCLASSIFIED: 0`, no `com.cobalt.agent` / `herdr` / `mainframe` / `obsidian` row → no `FAILED: RESTARTS beyond the pair`.

## Folds applied
Line numbers: `32:<n>` is the file under re-issue, `42:<n>` the re-issue. Backticks in quoted text are the file's own style; the words are the review's / seam draft's.
| fold | source | `32:` → `42:` | old text (≤20 words) → new text (≤40 words) |
|---|---|---|---|
| G1 SEAM PATHS | review F1 + seam ESC 3 | 144 → 148 | `…evaluate.py`, six pins, `test_assumed_store.py`, `configs/cobalt/jobs.yaml`, → + `src/cobalt/replay/formations.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_setups_d1.py` (F1); + `test_stale_score_db.py`, `test_radar_handicap_store.py`, `test_voice_store.py`, `test_jobs_restarts.py` (ESC 3) |
| G1 registry commit | seam ESC 3 | 142 → 146 | (`configs/cobalt/jobs.yaml`, `<set>` FOUR only) → (`configs/cobalt/jobs.yaml` + `tests/cobalt/test_jobs_restarts.py`, `<set>` FOUR only) |
| G1 DevDoc sentence | review Q7 (Grok's fold) read with `39` rule (e); desk item | 144 → 148 (end of bullet) | nothing → "The seam build's rule (e) DevDoc resolutions sit under `docs/40 - DevDocs/cobalt/` and are outside these diffs by construction; they are the check's, not the gate's." DevDoc paths NOT added to G1's lists. |
| `<gate sha>` value | review F2 = seam ESC 2 (once) | 55 → 56 | «FILL AT LAUNCH: the seam build's tip sha … field after STACK SEAM BUILT» → `57420087` (`log --format=%h -1 deploy/stacked-0925`: branch tip, report commit, ONE docs commit above `<seam tip>`); new `<seam tip>` = `a7296b44` (42:55) |
| G03 | review F2 | 127 → 129 | starts `STACK SEAM BUILT <gate sha>` → starts `STACK SEAM BUILT <seam tip>` |
| G05 | review F2 | 133 → 136 (new bullet) | nothing → `git -C /Users/cobalt/cobalt diff --stat <seam tip> <gate sha> -- . ':(exclude)docs'` → prints NOTHING; failure line worded on the neighbouring rows' pattern (mine, see ESCALATE 5) |
| G3 (d) → two passes | review F3 + seam ESC 1 | 161 → 165 (new (c1)), 167 ((d)) | "(d) THE WHOLE WITH-DB SUITE, NO DESELECT … `0 failed`, `0 errors`; quote the summary and every SKIPPED line" → (c1) pass 1 at `0013` with the nine `--deselect`s, (c) forward migrate (unchanged), (d) pass 2 = exactly the nine ids at `0017`; both commands byte for byte from `39` W (c1)/(d) (grep proof below); gate `0 failed`, `0 errors`, `9 deselected` / `9 passed`, NO SKIPPED line naming the database, cobalt.trader_id or voice_turns; `<d>` = `<d1>` + `<d2>` passed ≥ `3575` (seam stop line's `with-DB 3575/0` = 3566 + 9). Reason sentence (seam ESC 1) inside (c1). |
| (consequences of the two passes, wording only) | seam ESC 1 | 32 → 32; 157 → 162; 178 → 185; (f) end → 175 | "the whole suite with NO deselect" → the two-pass description; heading gains "in TWO PASSES"; G5's "suite" → "suite (both passes, `<d1>` `<d2>` `<d>`)"; (f) gains `39`'s "(A failure BEFORE (c) — (a), (b) or (c1) — runs only step 3 of (f): nothing was applied.)" |
| THE ROLLBACK STRING | review F4 | 303 → 312–313 | `1. CODE:` → `0. FIRST the desk removes any "handicap:" block from 1 - Trading/Radar Screens.md and proves it (cobalt radar sources).` then `1. CODE, only after 0:` |
| STEP-5 (4)(g) | review F5 | 298 → 307 | (`<RB>` still the AFTER value — the migrations stayed) → (`<RB>` = the value 4.4 recorded — the migrations stayed as 4.4 left them; skip the `voice_turns` count when `<RB>` shows m0017 = 0) |
| RELAUNCH RULE (vii) | review F6 | between 235 and 236 → 244 | nothing → (vii) D2.0 recorded no `<pre-merge>` (a FAILED PREFLIGHT ended the earlier run): end `FAILED: relaunch — no recorded pre-merge; nothing touched · rollback: not used`, and touch nothing. Inserted BEFORE (vi) as F6 says, so it reads (v), (vii), (vi). |
| STEP-5 (2c) | review F7 | 296 → 305 | end naming `radar: DOWN — H1 block present` → first bootstrap aset with 4.6's calls, then end naming `radar: DOWN — H1 block present` |
| STEP-D06 | review F8 | 197 → 204 | (F3 = F2) → (F3 = F2; `<FP>` does not see nullability, indexes or constraints) |
| STEP-5 (4) census | review F9 | 298 → 307 | the census again (`<np2>`, `<s3_2>`, `<rr2>`, … → (`<np2>`, `<s3_2>` — > `<s3_0>` is ESCALATE 0: the 21:10 replay on the reverted code refuses s2p2.3 rows — `<rr2>`, … |
| launch line | review F10 (C20) | 6 → 6 | `"Bash(git -C * rev-list*)"` → removed (grep proof: no step of `42` runs `rev-list`; the one hit, `42:11`, is the prose note recording the removal) |
| THE LIST counts | review F10 consequence | 10–11 → 10–11 | 47 allow / 39 byte-for-byte → 46 allow / 38 byte-for-byte + the removal note |
| CWD DISCIPLINE | review F10 (C26) | 105 → 107 | Before every `pytest` or `COBALT_ENV=dev …` call, → … call except `<FP>` and the dev migrate calls that follow a `.env` glob `ls`, |
| G07 probe row | review ESC 2 (Opus line) | new → 140 (+ 110 → 112) | nothing → G07: `cd` gate worktree, `ls` `.env` "No such file", `<FP>` typed EXACTLY, EXPECTED a refusal or connection error, RECORDED, not a stop; the point is the string is accepted as typed; `cd` back. The `<FP>` line's "ONLY … with `.env` present" gains "(its one exception is G07's probe …)". |
| G1 final-tree rows | review ESC 3 | new → 151 | nothing → `grep -c -F "def prepare_member"` on the gate tree's `evaluate.py` → `1` · `grep -c -F "EVALUATOR_VERSION = \"s2p2.3\""` → `1` · `git diff --stat fix/replay-deadline-0924 deploy/stacked-0925 -- src/cobalt/replay/formations.py` → NON-EMPTY |
| relaunch (i) marker | review ESC 4 | 231 (text unchanged) → 237 | (i) left AS WRITTEN (bring them up); marker line `DESK RULING OWED — 09-25 review ESC 4 (L43): the desk carries this to him as one A/B before 20:00` added on its own line ABOVE the quoted rule (not inside the quote the hub copies verbatim into its report) |
| allow-string matching | review ESC 5 | 294/295 → 304 | nothing → "ALLOW-STRING MATCHING (the desk's answer, 09-25 review ESC 5): a `Bash(<cmd>)` rule WITHOUT a trailing `*` matches that exact command only, so `migrate --allow-prod` does NOT cover `… --allow-prod --rollback …`; this rule STANDS — the hub never runs the production rollback; the desk does." Placed at (2b), the rollback-forbid rule (see ESCALATE 4). |
| launch-time values | desk's item 28 | 53–60 → 53–62 | `<seam stop>`, `<gate sha>`, `<main-at-cut>`, `<set>` «FILL AT LAUNCH» → filled: the stop line verbatim; `57420087`; `2b71fe49`; FOUR; plus new lines for `<seam tip>` and the four merge shas / `<R sha>`; header sentence adjusted |
| own path | `41` "Write two files (a)" | 6, 8, 46 (×2), 50 (×2), 130 → same, 130 → 132 | `32-stacked-deploy.md` → `42-stacked-deploy-r2.md` in the launch instruction, the CONTINUE line, the R__L check, the placeholder gates, P-LOCK's `grep`. The `32 DEPLOY RELAUNCH` literal is NOT changed (ESCALATE 2). |

## Not applied
- Seam ESC 2's extra clause (`merge-base --is-ancestor <seam tip> deploy/stacked-0925` exit 0) — not added: `41` says apply F2/ESC 2 ONCE in the review's wording, and the review's F2 has only the `diff --stat`. ASK DESK: add it? Safe default: not added [13:4x].
- `39` run 3's `pg_stat_activity` read on a `DeadlockDetected` — not carried into the gate's (c1)/(d): not a fold named in `41` [13:4x]. Safe default: `DeadlockDetected` stays "a red — name it, never re-run it here".
- Nothing else a fold named was left unplaced.

## Strings
`grep -o -E '"Bash\([^"]*\)"'` over the whole file, then `grep -v -x -F -f` of one file's token set against the other's:
- `42` tokens not in `32`: 0. `32` tokens not in `42`: exactly `"Bash(git -C * rev-list*)"`. Token counts 48 (`32`) vs 47 (`42`) = allow strings + the one `Bash(git push*)` deny; the other two denies are not `Bash(…)` tokens and are unchanged.
- Verdict: identical, minus exactly the one F10 removal (`strings: −1`). No new string added.
- Other byte-for-byte proofs: the two `COBALT_ENV=dev uv run pytest … --deselect …` / nine-id commands in `42` are each an exact line in `39-stack-seam-build.md` (0 unmatched); every `db query --side … "SELECT …"` string in `42` (`<FP>`, `<RB>` and the seven census/cards/voice reads, 9 in `32`) is identical to `32`'s (0 unmatched); the live-note pytest command is identical to `32`'s.
- `rev-list` in `42`: `grep -c -F "rev-list"` → 1 (`42:11`, the removal note); no command line runs it.

## Placeholders
- `grep -c -E "R_[_]" 42-stacked-deploy-r2.md` → `6` (lines 17, 45, 46, 131, 340, 341 — the desk's launch-row tokens, as in `32`, none filled).
- `grep -c -E "«FIL[L]" 42-stacked-deploy-r2.md` → `3`.
- `grep -n -F "FILL AT LAUNCH" 42-stacked-deploy-r2.md`:
  - `60:- <seam check stop> = «FILL AT LAUNCH: the seam check's stop line, verbatim, from reports/stack-seam-check-2026-09-25.md»`
  - `61:- <v1 row> = «FILL AT LAUNCH: the desk row number carrying V1 DEVICE SESSION DONE <time> or V1 DROPPED, e.g. R71»`
  - `62:- <lock line> = «FILL AT LAUNCH: the launch row's literal sentence LOCK: 09 STOPPED <time>; no with-DB run in flight (or 09 NOT LAUNCHED)»`
- (`grep -c -F "«FIL"` → 5: the three above plus the two bracket-form gate lines, `42:50` and `42:341`, which do not match themselves.)

## ESCALATE
1. **ASK DESK — F3's skip ban as worded may turn a good gate red** [13:4x]. The review's ban is "NO SKIPPED line whose reason names the database, cobalt.trader_id or voice_turns". The seam build's own pass 1 recorded six SKIPPED lines; one is `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` (source line `pytest.skip("S2-P2's card_score column is present on cobalt_dev")` — read on the gate worktree). A literal reading trips on that reason ("cobalt_dev" is a database). Applied AS THE REVIEW WORDS IT (fail-loud). The desk decides whether to name the known skips (`test_cards_picks.py:388` and `:401`, and the three `COBALT_LIVE_VAULT_ROOT` ones, which the live-note leg runs) as allowed — not decided here.
2. **ASK DESK — the relaunch literal** [13:4x]. `42` still greps `32 DEPLOY RELAUNCH` (D00, AUTHORIZATION) — the desk's row token, kept as `32` spells it. If the desk writes the row as `42 DEPLOY RELAUNCH`, D00 fails; the desk writes the literal as `42` names it. Safe default: unchanged.
3. **The seam check is not done.** `40` launched 13:27 (bg `577d3f8c`); no `stack-seam-check-2026-09-25.md` exists at 13:38, so `<seam check stop>` stays a placeholder and G03's second bullet cannot pass until it lands. A HOLDing check defect means a further re-issue; the houses do not re-read `42` (L67, one round). The four values filled here come from the seam BUILD only.
4. **Placement readings (desk to verify):** (a) review ESC 5 cites `32:294`, which is the "L54: never `reset --hard`" bullet; the rollback-forbid rule the desk's answer refers to is `32:295` (2b) — the sentence sits at `42:304` there. (b) F6's "insert before (vi)" is literal: (vii) precedes (vi) at `42:244`–`245`. (c) The ESC 4 marker sits above the quoted relaunch rule (`42:237`), outside the text the hub copies into its report; relaunch (i) is unchanged.
5. **Wordings mine, on neighbours' patterns (no fold gives them):** the FAILED lines of the new G05 diff row and G1's final-tree rows; G07's "record, not a stop"; the `FAILED: G3 (c1)` / `(d)` labels. If G07's `<FP>` connects (a `.env` from elsewhere), it is a read-only fingerprint outside the lock — recorded, not a stop.
6. **G04 takes its OR branch.** The review's last line is `defects that HOLD: 3 · ready to run: NO`, so R__L must name every finding that held as folded into this file (F1–F3 blocked; F4–F10 and ESC 2–5 folded or placed as above).
7. **Seam build readings carried to the desk** (not folded — not named): `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175` (voice's numbering paragraph is false on the stack); `com.cobalt.agent` runs `uv run` from `~/cobalt` (`cobalt.sh:59`) and is NOT in the registry lines for `pyproject.toml` / `uv.lock` — the check's Q4, an agent restart is not on this launch line; two rule (b) comment-edit READINGS (`test_assumed_store.py:249`, `test_archiver_migrations.py`); `cobalt_redactions` +1 row on `cobalt_dev` during pass 1 (writer unproven); run 2's `DeadlockDetected` unproven (L70). The seam build's rule (e) DevDoc paths (`db_migrations/__init__.md`, `radar/evaluate.md`, `replay/formations.md`) are the check's, not G1's.
8. **Seat/lane:** this hub wrote two files, ran no database, no pytest, no git write, launched nothing (L36); the `git -C … diff` / `status` reads were read-only.

STACKED DEPLOY RE-ISSUED · folds: 13 of 13 · strings: −1 · gate sha: 57420087 · seam tip: a7296b44 · restarts: com.cobalt.aset com.cobalt.radar · ESCALATE: 8
