# draft-check-scratch-fr1-check — 2026-10-17

## §0 Headline
- Wrote `prompts/2026-10-16/690-check-scratch-fr1-check-card.md`: the K5 CHECK of `ops/check-scratch-fr1`, TIP `b093f192` on BASE `79f6f2f3`; no `«FILL`.
- The head `5f42c4f3` adds only the build report and its `.result` (`git diff --stat b093f192 5f42c4f3 -- . ":(exclude)docs"` printed nothing).
- Rows S0, MK-1, CL-1a, CL-1b, CL-2, SC1, H1, X6, F1 (card 583 collision by `git diff --stat` of each branch against its BASE), R2, G1 (deploy gate); the three retired tests are checked against the tip's script.
- Reads only; nothing run, nothing committed.

## DECISIONS
1. ASK DESK: the build's DECISION 1 (a same-JOB check card with no leading digit ranks `0`) is carried into the card as ask X3 with a recommendation owed. Default: keep `0`, no new test. [10:06 EDT]
2. ASK DESK: card 583 shows `stage-set.sh` and `test_stage_set.py` in `git diff --stat main ops/band-routing-1015` (34 and 201 lines) only because `main` moved past its BASE `f2ca3e1a`; against its BASE the branch touches neither. Row F1 says to diff against the BASE and not to read the `main` diff as card 583's. Default: as written. [10:06 EDT]
3. ASK DESK: `git merge-tree` is not on the allow line, so no merge dry run is in the card. Default: none; the `git diff --stat` path-set check stands. [10:06 EDT]
4. ASK DESK: the old helper `_two_card_copies` (`tests/ops/test_stage_set.py:375`) is now unused. The card asks the checker for one line (finding or note). Default: a note. [10:06 EDT]

## RECORDS
- `date` → Sat Oct 17 10:06:55 EDT 2026; `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3028f667`.
- `git -C /Users/cobalt/cobalt log --oneline ops/check-scratch-fr1 -5` → `5f42c4f3`, `b093f192`, `0d52929f`, `79f6f2f3`, `caebf457`.
- `git diff --stat 79f6f2f3 b093f192` → `ops/desk/stage-set.sh | 70`, `tests/ops/test_stage_set.py | 147`, `183 insertions(+), 34 deletions(-)`.
- Tip line numbers proved on `git show ops/check-scratch-fr1:ops/desk/stage-set.sh` and Grep of the worktree: marker write `:242`, marker branch `:108-121`, legacy branch `:122-154`, version test `:155-157`, JOB test `:158`, one caller `:173`, `rm -rf` `:194` and `:201`. The build report gives the caller as `:152` (BASE's number); the card says so.
- `git diff -U0 79f6f2f3 b093f192 -- tests/ops/test_stage_set.py`: two tests deleted, two marker lines added, one block appended from `:528`.
- Card 583: BASE `f2ca3e1a`, head `6c0ba560`; `git diff --stat f2ca3e1a ops/band-routing-1015 -- ops tests src configs` lists six files, none of them `stage-set.sh` or `test_stage_set.py`; its four hubs are listed too.
- Header values `BAND`, `RESTARTS`, `RULINGS`, `LADDER` copied from card 681; `grep -c -E "«FIL[L]"` on the card → `0`.

DRAFTED · decisions: 4
