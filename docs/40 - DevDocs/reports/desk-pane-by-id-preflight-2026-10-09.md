# Preflight card 197 desk-pane-by-id · 2026-10-09

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header: `JOB desk-pane-by-id-1009`, `BRANCH ops/desk-pane-by-id-1009`, `WORKTREE desk-pane-by-id-1009`, `TIP`/`CHECK REPORT`/`HOUSE B` empty, `DB none` vs `desk-launch.sh:722-742,895-904` | keys needed (JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS) all present; job `[a-z0-9-]`; branch plain; TIP empty is the build shape | OK |
| 2 | `ls /Users/cobalt/cobalt-wt` and `git show-ref --verify refs/heads/ops/desk-pane-by-id-1009` | no `desk-pane-by-id-1009` directory; ref "not a valid ref" (`desk-launch.sh:905-911` takes the new-worktree path) | OK |
| 3 | REPORT `/Users/cobalt/cobalt-wt/desk-pane-by-id-1009/docs/40 - DevDocs/reports/desk-pane-by-id-build-2026-10-09.md` vs `desk-launch.sh:901-904` | matches `$WT/$wt/docs/40 - DevDocs/reports/*.md` | OK |
| 4 | `git -C /Users/cobalt/cobalt rev-parse --short=8 044f58b5` and `merge-base --is-ancestor 044f58b5 main` | `044f58b5`; exit 0 (a real main commit) | OK |
| 5 | RULINGS `2026-10-08 R685` vs `desk-launch.sh:245-272` (`ruling_row`) and L7a (`cto-desk-checklist.md:36`) | `cto-2026-10-08.md:38` is the one `^\| R685 \|` row; holds `HIS RULING` and `APPROVED`; `git show HEAD:` carries the same line (working-file diff is one deleted OWED line, not R685) | OK (see ISSUES 1) |
| 6 | `grep -c "«FILL"` on the card | 0 | OK |
| 7 | `grep -c -F` of P1 clause `no id there → \`herdr tab list\` (find the "CTO" tab)` on the wake-up (`git diff 044f58b5 HEAD` of it is empty, so BASE = working file) | 1; at line 14 | OK |
| 8 | `grep -c -F 'A pane → leave it, name it in the plate as closable.'` | 1; at line 22 | OK |
| 9 | `grep -c -F 'One herdr tab "CTO" with a live VIEW of you; create or re-attach as needed; close any other desk tab.'` | 1; at line 24 | OK |
| 10 | `grep -c -F '· pane <id>'` | 0 on BASE (P4 red is real); `HANDOVER: predecessor` at line 22 (twice: plain and `(stuck; ended by successor)`); item 1 at line 21 names no shape | OK |
| 11 | brain's red `grep -c 'VIEW it in the "CTO" tab'` on the wake-up | 0 (the sentence is in the checklist, `cto-desk-checklist.md:17` step 5 now reads "no VIEW, no tab"); card's own reds are the right ones | OK |
| 12 | card vs `desk-tab-answer-2026-10-09.md` `## FIX` lines 10-13 | P1 = FIX 1+4 (VIEW line); P2 = FIX 3; P3 = FIX 1+4 (item 4); P4 = FIX 2 (shape). FIX 5 fenced as NOW. Only `CTO-DESK-WAKEUP.md` in every `files` cell; nothing beyond FIX 1-4 | OK |
| 13 | `grep -n "HANDOVER" ops/desk/desk-wake.sh` line 75 | `hand = [m.group(1) for m in (re.match(r"^HANDOVER: .* at ([0-9]{2}:[0-9]{2})", l) for l in lines) if m]`. `.*` is greedy but the pattern is not end-anchored; on `HANDOVER: predecessor a → successor b at 15:01 · pane w2:pRY` it matches and captures `15:01`. `stop-guard.py`: no HANDOVER match. `desk-handover.sh`, `desk-launch.sh:407` name the word only | OK |
| 14 | commands named by the rows vs R411/R412 | `herdr pane run`, `herdr pane list`, `herdr tab create`, `herdr tab close`, `pgrep`, `claude stop/rm/attach`, `send-keys Enter` (H4): all exist today (`cto-desk.sh`, `desk-done.sh:65`, checklist W8, H4); no script or flag is added | OK (see ISSUES 2) |
| 15 | `git diff HEAD --stat` of the card; `git log` of it | empty diff; committed in `d8f9f4af` | OK |
| 16 | X2 on BASE: wake-up lines that still find the pane by label or leave a pane | line 3 SEAT `herdr tab "CTO"` (a description, not a lookup; outside the four rows); line 14 and 22 and 24 are rewritten by P1-P3 | OK (see ISSUES 3) |

## ISSUES
1. NOTE: R685's status cell reads `APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45`; L7a says "the status is never changed to APPLIED on that row". The launcher test (`*HIS RULING*APPROVED*`) passes, and builds already launched on R685 (R691). Not a launch blocker.
2. NOTE: the card's `## NOT IN THIS JOB` says `herdr tab close` and `herdr pane list` are commands "the file already names"; at BASE the wake-up holds `herdr tab close` 0 times and `herdr pane list` only as "never `herdr pane list`". Both are existing commands elsewhere, so no R411/R412 breach; the builder adds them as new text in the file.
3. NOTE: line 3 (`herdr tab "CTO"`) and the card's RECORDS (HEAD `a82d8b6f`, now `044f58b5`; the file is identical across both) stay as written; the first is outside the rows, the second is only a record. `cto-2026-10-08.md` has one uncommitted deleted OWED line (unrelated; R685 row intact in HEAD).
4. NOTE: the four reds are `RUN` greps (assert nothing), as the card says; P4's "after = 1" holds only if `· pane <id>` is written once (the `(stuck…)` variant takes no tail).

PREFLIGHT DONE · card: desk-pane-by-id-1009 · checks: 16 · fails: 0 · ready: YES
