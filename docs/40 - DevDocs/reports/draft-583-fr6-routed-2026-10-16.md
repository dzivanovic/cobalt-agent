# draft-583-fr6-routed — card 583 FR-6 shape A (2026-10-16)

## §0 Headline
- Card 583 amended, only by Edit: FR-6 is shape A (kind `routed`, `re='^(BUILT ·\|FAILED)'`, session `<job>-gate`); `ops/desk/desk-watch.sh` joins the files for its two `routed` case arms.
- Updated: `## FIX ROUND 2` scope paragraph, the FR-6 row (edit, `test_x5_…` assertion, control, files cell), `## NOT IN THIS JOB` desk-watch clause, X13, `## RECORDS`.
- Decisions 3, 4, 5 keep their defaults; `BASE`, `TIP`, `RULINGS` untouched. Nothing was run.

## DECISIONS
1. ASK DESK: the prompt's `:71-75` for the second `case "$kind"` block counts the closing `esac` line; the arms are `:71-74` (`:75` not read). The card keeps the prompt's range in `## NOT IN THIS JOB`; the builder finds the arms by content. Default taken: as is. [12:59]

## RECORDS
- Read: the prompt; the card whole; `reports/draft-583-fr6-2026-10-16.md`; on `ops/band-routing-1015` by `git show` / `git grep -n`: `desk-watch.sh` whole (`:59`, `:60-66`, `:70`, `:71-74`), `desk-launch.sh` (`:287-288`, `:379`, `:394`, `:1667`, `:2354`).
- Each is recorded in the card's `## RECORDS` last entry.
- Not done: no git write, no launch, no test run.

DRAFTED · decisions: 1
