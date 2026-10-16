# Card 622 jev-shadow-fr1 — preflight round 2 (read-only), 2026-10-16

Card `prompts/2026-10-16/622-jev-shadow-fr1-card.md` after the amend (commit `30104dbd`). `git diff HEAD --stat` over the card and `cto-2026-10-15.md` prints nothing (both committed, tree equals HEAD `f6ca1455`). Round 1's passing checks are not repeated.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log -p --format=%h d2365cef..HEAD -- <622>` | one commit `30104dbd`, two hunks: the `RULINGS:` line (`R1620` dropped, now `2026-10-15 R1532, 2026-10-15 R1535`) and the `Scope:` paragraph added at the top of `## FIX ROUND`. No other hunk | OK |
| 2 | `grep -n "\| R1532 \|\| R1535 \|" cto-2026-10-15.md` | `:99` R1535 `HIS RULING · APPROVED …`; `:102` R1532 `HIS RULING · APPROVED …`; each ONE line holding both words | OK |
| 3 | `git log -1 --format=%h -S"\| R1532 \|"` and the same for R1535 over that file | `1ddcdc64` and `1f067493`; `git diff HEAD --stat` of the file empty: both committed | OK |
| 4 | round 1 issue 1 vs the `Scope:` paragraph | answered: "builds ONLY row FR-O2 … Every row under `## ROWS` is DEPLOYED on main from card 591 (`0b7c569d`); the builder does not port, re-red or rebuild them: they are context, and 'RED on BASE' / 'reds on the P0 port' apply only to FR-O2's own test". That is the one-line statement round 1 asked for (the shape of card 603's WHY). The R1620 proof is moot: R1620 left `RULINGS:` (a desk row, L79; the amend report's decision) | OK |
| 5 | `grep -n -x -F -f 621-draft-jev-shadow-fr1.md <622>` | prints card `:19` only, the FR-O2 line, whole-line fixed-string equal to a line of prompt 621: byte for byte | OK |
| 6 | day key buildable: closed gate and day | `closed_cards` `route.py:538-550` (CHECK DONE gate `:589`, day = `git log -1 --format=%cs` of the check report `:548`) stays as the card says. Testable with the existing `_closed_card` / `_batch` / `DAY` fixtures | OK |
| 7 | day key buildable: "launched that day" | `launch_sha` `route.py:319-327` gives the launch commit; its date by the same `%cs` is a buildable key. Testable: a build card committed with empty `TIP:` on `DAY`, then its `TIP:` filled | OK |
| 8 | build-card definition buildable | the paragraph says "a `*-card.md` whose launch kind is build" and "never a check, deploy, devfix or prompt card" but names no content test; see ISSUES 1 | NOTE |
| 9 | header fields as round 1 (`CARD.md:17-20`) | `JOB`, `LADDER`, `BAND`, `INSTALL`, `BRANCH`, `WORKTREE`, `REPORT`, `CHECK REPORT`, `HOUSE B`, `RESTARTS`, `RULINGS` present; `BASE:` and `TIP:` empty (by design, the desk writes BASE at launch). `CHECK REPORT:` is filled (issue as round 1 NOTE 5, unchanged, desk accepted) | OK |

## ISSUES

1. NOTE (gap, the builder must decide and record under `## DECISIONS`): "launch kind is build" has no content test. `CARD.md:5` says ONE card per job: the build, the check (and PASS-2) launch on the SAME file, the desk filling `TIP` / `CHECK REPORT` in between. So a "check card" is not a second file; only deploy and devfix cards are separate files (`TAG` / `TABLE` headers, no `## ROWS`). The test must therefore read the card AT ITS LAUNCH COMMIT (`launch_sha`, empty `TIP:`), never the working copy (where `TIP:` is filled), and exclude by header: `TAG:` set or `TABLE:` set, or no `## ROWS`. The red fixture "build card plus its check card" must be built as two files (constructed check card: `TIP:` filled, no empty-`TIP` commit, so `launch_sha` raises). Default for the builder: build card = `*-card.md` with an empty-`TIP:` commit, a `BASE:` of 8 hex, no `TAG:` / `TABLE:` header, and a `## ROWS` section.
2. NOTE (gap, day keys can disagree): outcome rows keep the check-close day, decision rows take the build-launch day, but the scope says FR-O2's filter runs BEFORE the CHECK DONE gate. A card whose build launched day D and whose check closed D+1 then passes neither run: `--day D` has no CHECK DONE yet, `--day D+1` fails the launch-day filter, so it gets no decision row and, as the filter is applied first, no outcome row either, against "Outcome rows still read the check's CHECK DONE line". Same-day cards (all the F9 fixtures) are unaffected. Default: apply the build-card filter (kind) before the gate, the launch-day match to decision rows only, and record the straddling case under `## DECISIONS`.
3. NOTE: `%cs` is the committer's local date; the launch day and the close day use the same call, so they agree (carried from F9, not a defect).
4. NOTE: RESTARTS `com.cobalt.agent com.cobalt.radar` is a prediction; FR-O2 touches `src/cobalt/classify/route.py` and tests (radar only). The builder's `cobalt jobs restarts <BASE>..HEAD` decides (L42), as the card says.
5. Launch: the desk writes BASE (main HEAD) and re-commits the card so `authorize.sh` finds it unchanged. Nothing else blocks.

PREFLIGHT DONE · card: jev-shadow-fr1 · checks: 9 · fails: 0 · ready: YES
