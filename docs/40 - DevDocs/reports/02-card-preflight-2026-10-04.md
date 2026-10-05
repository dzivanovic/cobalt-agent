# Card 02 f15-p2 — preflight 2026-10-04

Card `prompts/2026-10-04/02-f15-p2-card.md`, BASE `3c1f75b8`. Read-only. 8 checks, 2 FAIL, both on row T (it cites hub files that hold no id list at BASE). Every other fact holds.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `tail -n 2 …/drc-d5-1004/…/drc-d5-build-2026-10-04.md` | `BUILT · job: drc-d5 · tip: 3c1f75b8 \| on 3e40359a \| migration: none \| offline 3894/0 \| with-DB 867/0 …` | OK |
| 1b | `git merge-base --is-ancestor 3c1f75b8 drc/d5-reconcile-1004` | exit 0, no output | OK |
| 1c | `git diff --stat 979ec797 main -- src tests` | empty | OK (report: empty) |
| 2 | `git rev-parse --verify f15/p2-replay-1004`; `ls /Users/cobalt/cobalt-wt/` | `fatal: Needed a single revision`; no `f15-p2-1004` in the listing | OK |
| 3a | `git show 3c1f75b8:<path>` for each `files` path | exist: `src/cobalt/cards/predictions.py`, `src/cobalt/cards/cli.py`, `ops/desk/gate-lists.md`, `docs/40 - DevDocs/cobalt/cards/predictions.md`, `…/cards/cli.md`. `tests/experiments/f15_p2/` is not in the BASE tree (new; card does not mark it) | OK |
| 3b | `git grep` at BASE for cited names | `legs.py:677 def realized_r`; `legs_current_v` (legs.py:119, 287, 312…); `evaluate.py:163 EVALUATOR_VERSION = "s2p2.3"`, `:1523 class ReplayError(ValueError)`, `:1604 def published_numbers`, `:1618 def replay_receipt`; `store.py:1316 def receipt_for_run`, `:1101 create_radar_card`, `:1177 refresh_radar_card`, `:1284 write_receipt`, `:1393 tap_dot`; `scoring.py:259 def conviction`; `predictions.py` `PredictionRecord`, `write_record`; `test_radar_cards_db.py:45 def world()`; `0009_picks_missed.sql` `cf_r`, `mfe_r`, `excluded_by`, `is_current` | OK |
| 3c | `git diff --stat 979ec797 3c1f75b8` | 27 files. `cards/predictions.py`, `cards/cli.py`, the cards DevDocs pages and `tests/experiments/f15_p2/` are NOT in it. `ops/desk/gate-lists.md` IS (4 lines: D5's ids) | OK, see NOTES 1 |
| 3d | row T `what`: ids go "in `BUILD-HUB.md` (c), (c3) and `DEPLOY-HUB.md` STEP-G" | BASE `prompts/BUILD-HUB.md:82,85` and `prompts/DEPLOY-HUB.md:106` hold no id list: (c)/(c3) say "the PASS 1/PASS 2 command of `ops/desk/gate-lists.md`, plus…". BUILD-HUB `:77` (`## W`): "edits `ops/desk/gate-lists.md` … names that file in the row's `files`" | **FAIL** |
| 4 | card `## RECORDS` | `RESTARTS: derived (`cards/*.py`; quote `cobalt jobs restarts`)`: names the class of both src paths | OK |
| 5 | reports and FINAL | `cto-2026-09-29.md` `:154` R145 "HIS F15 RULINGS … R2-1 (c) decision grade = B (`transition_id`…". `:155` R146 "DESK RECORD (R127, L39): F15 R2-5 settled on the Anthropic seat's texts". FINAL has `## First-gate experiments` `:423`, `X6 :434`, `X7 :435`, `X10 :438`, `X11 :439`, `## SEAM :449`, `## CHUNKS :479`, `P2 :484`, `X12 :440`, `[F-33]`, `[F-35]`, `[F-44]`, `[F-25]`, RULED block `:304`, `Open point 2` `:270`. Build report: `## E2 RED :87` with X12 lines `:154-167`, `## DECISIONS :345` item 6 "DECISION X12 … No red, so the `transition_id` rule stands", `## RECORDS :363`, H2 rows `:222-224` carry the X6 (a), X6 (c) tests. Check report: `## §0 Headline :3`, `FINDING O1 :67` / `:220` "X6 (b) … NOT HELD (green)". `s3-reread-draft-2026-10-04.md` exists. FINAL `:356` / `:475` "P2 builds on a tree carrying `s3/exits-c4`" | OK |
| 6 | `grep -n "^| R219 " …/cto-2026-10-03.md` | `225:| R219 | 10-04 15:01 ET | HIS RULING: S3's K3, F15 P2, D5 run on the new workflow … \| HIS RULING · APPROVED \|` | OK |
| 7 | each row has red-first or red ids; row T names gate-lists | X: RUN, asserts nothing. P2-1, P2-2, P2-3: red tests named. T names `ops/desk/gate-lists.md`. T's red-first, "`git diff <BASE> -- <both hub files>` shows only these ids added", can never hold: row T will not touch the hubs, so that diff is empty | **FAIL** |
| 8 | `grep -c -F "«FILL"` | `0`. TIP, CHECK REPORT, HOUSE B are empty (card lines 6, 8, 9) | OK |

## ISSUES

- 3d: row T `what` says the ids go in `BUILD-HUB.md` (c), (c3) and `DEPLOY-HUB.md` STEP-G. At BASE those hubs hold no id list. The only home is `ops/desk/gate-lists.md` PASS 1 and PASS 2 (BUILD-HUB `## W` `:77`). Fix: drop the hub files from `what`.
- 7: row T `red first` tests the diff of the two hub files. Fix: "`git diff 3c1f75b8 -- ops/desk/gate-lists.md` shows only the `--deselect` ids at the end of PASS 1 and the same ids at the end of PASS 2".

## NOTES

1. `ops/desk/gate-lists.md` is the one path shared with `git diff 979ec797 3c1f75b8`: D5 added its ids at the end of PASS 1 and PASS 2. I read it as not a FAIL: BASE carries that diff, `## RECORDS` says row T edits the lines "AS THEY READ AT BASE", and `gate-lists.md` now holds the D5 ids in both lists. The build appends after `tests/cobalt/test_drc_d5_experiments_db.py` (PASS 1 end) and after `tests/cobalt/test_drc_d5_experiments_db.py` (PASS 2 end). The P1 precedent, `tests/cobalt/test_f15_p1_records_db.py`, is already in PASS 2.
2. R219 sits in `cto-2026-10-03.md`, stamped `10-04 15:01 ET`. The card's `2026-10-03 R219` matches the file, not the stamp.
3. FINAL "ONE read" is at `:336-342` at BASE (card cites `:337`–`:342`): the first line is `:336`, the card's range is one line off.
4. `tests/experiments/f15_p2/` is new; the card's `files` cell does not mark it new.
5. `cobalt jobs restarts` was not run (no production command in this seat).

PREFLIGHT DONE · card: 02 · checks: 8 · fails: 2 · ready: NO
