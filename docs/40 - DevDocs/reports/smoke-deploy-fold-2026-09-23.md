# Smoke-Only Deploy Fold — 2026-09-23 (`71`: `69`'s read folded into `68`, re-issued in place, L19)

## §0
- `68-smoke-only-deploy.md` re-issued IN PLACE: 6 folds applied (blocker fold 2 first) + the desk line in the header. Uncommitted — the desk commits it.
- Launch line (now line 7): byte-identical to HEAD's line 6 (`md5` `00a91b59…` both). 0 strings added, widened or changed.
- Every new command matches a string already on the line: `rev-parse --short deploy/stacked-0923` → `"Bash(git -C * rev-parse*)"`; `ls -la …/stacked-0923/.env` → `"Bash(ls *)"`; `rm /Users/cobalt/cobalt-wt/stacked-0923/.env` → `"Bash(rm /Users/cobalt/cobalt-wt/stacked-0923/.env)"`.
- `R__L` count unchanged at 3 (lines 49, 51, 141). Diff: 1 file, 8 insertions, 7 deletions.

## Folds
Line numbers are the re-issued file's. The header insert moves every later line down by 1 from HEAD's numbering; the review's `part2:N` = HEAD line 160+N.

| fold | review row | line | before → after |
|---|---|---|---|
| 2 (BLOCKER) | in-run partial revert | 282 (STEP-5 (2)) | `… log --oneline -8 quoted → (3), labelled safe state: <NEW code kept \| partial revert — the desk decides> — revert failed: <error>` → `… log --oneline -8 quoted → run (2)'s PROVE IT diff; empty → (3); non-empty → do NOT bring the residents up, end FAILED: STEP-5 (2) — partial revert — <paths> · rollback: used — aset: DOWN — radar: DOWN`. Consistent with line 287 ("ONLY endings with a resident DOWN are … (2)'s unproven revert"). |
| 1 | gate name re-read | 225 (3.1) | appended: `And git -C /Users/cobalt/cobalt rev-parse --short deploy/stacked-0923 must EQUAL <ship>, else FAILED: 3.1 — gate branch moved · rollback: not used`. |
| 1 | same | 244 (4.3) | appended to the HEAD bullet: `… must EQUAL <ship>, else 4.6 first, then FAILED: 4.3 — gate branch moved · rollback: not used`. |
| 3 | relaunch (ii) after an ended run | 230 | `Otherwise a revert was interrupted: go to STEP-5 (1) at once;` → `If it is any other committed stop line (SMOKE ONLY DEPLOY DONE, or FAILED with rollback: not used), end FAILED: relaunch — the run already ended; the desk decides · rollback: <as that line>. Only when the report has no stop line above # SECOND RUN was a revert interrupted: go to STEP-5 (1) at once;` |
| 4 | relaunch `.env` | 230 ((ii) "never recorded" clause) | `… else end FAILED: relaunch — main moved …` → `… else FIRST ls -la /Users/cobalt/cobalt-wt/stacked-0923/.env; if listed, rm /Users/cobalt/cobalt-wt/stacked-0923/.env and ls -la again (STEP-2.3 (e)); then end FAILED: relaunch — main moved …` |
| 4 | same | 233 ((v)) | `End FAILED: relaunch — partial gate …` → `FIRST ls -la …/.env; if listed, rm …/.env and ls -la again (STEP-2.3 (e)); then end FAILED: relaunch — partial gate …` |
| 5 | "NEVER crossed" wording | 38 | `The 20:00 pause, the 20:30 archiver, the 21:10 replay (Mon–Fri) and the 21:40 backup (daily) are NEVER crossed by a residents-down window.` → `The 20:30 archiver, the 21:10 replay (Mon–Fri) and the 21:40 backup (daily) are never crossed by the run's own window (STEP-5 excepted, STEP-5 (0)); a window opened before 19:58 may close after 20:00, inside the 20:00–21:00 pause.` (the review's `part2:114` is written as its step name, `STEP-5 (0)`) |
| 6 | new `_inflight` file mid-run | 247 (4.5) | `exit 1 on EXACTLY <val0>'s docs/_inflight/ lines, or exit 0.` → `exit 0, or exit 1 with ONLY lines of the form docs/_inflight/…: docs/_inflight/ may hold only README.md (a new such file is named in ## Smoke, not RED).` 4.7 (f) (line 268) reads `→ as 4.5`, so it inherits the fold and its text is unchanged (the smallest change). |
| desk line | desk-side note (not counted) | 5 (header) | NEW: `DESK LINE (not a hub step …): from launch until 68 writes its stop line, the desk HOLDS every other with-DB run and every .env copy (the setups fix round, R78 "runs in parallel", included), and writes that hold on the launch row (THIS LAUNCH, below).` Written as "the launch row", not as the placeholder token, so the placeholder count stays 3. |

## ESCALATE
- ASK DESK: P9 (line 141) passes only on `blockers: 0` or an `R__L` row that names the held blocker as folded. `69`'s line reads `blockers: 1`, so the `R__L` row must name fold 2 (STEP-5 (2), line 282) as folded. [16:53 ET]
- The review cites `68` by HEAD's part1/part2 line numbers. After this re-issue, every line after line 4 sits one lower (the DESK LINE insert). [16:53 ET]
- `<val0>` (P14, line 159) is still recorded as before. 4.5 no longer compares against it, and it is kept as a baseline reading. [16:53 ET]

SMOKE DEPLOY FOLDED · folds applied: 6 · blocker folded: yes · strings widened or added: 0 · ESCALATE: 3
