# Launcher card 324 amend · 2026-10-11

## §0 Headline
- Card 324 amended from its preflight ISSUES 1, 2, 5 and NOTES 3, 7; scope, RULINGS and launch lines untouched.
- P3 is now a pin: BASE already fences a spike seat as `worker`; the G4 assertion is dropped.
- Shadow stop heads added to `STOP` and `STOP_HEADS` (S4), with tests; `desk-watch` gets `$job-gate`.
- BASE read: `518c1bd1`. Line numbers differ from the preflight's HEAD `921b6bf5`; the card now cites the BASE ones.

## DECISIONS
- ASK DESK: the card names no spike stop head and no spike desk-watch session (the spike has no `JOB`/`REPORT` header), so neither was added. Add `SPIKE DONE ·` and a spike watch kind? [by the next card amend] default: no, the spike stays unwatched by `desk-watch.sh`.

## RECORDS
- Edit 1, `324-shadow-hub-card.md` row P3: G4 assertion and the `git status` case dropped; red stated as a pin. Proof: `bare-guard.py:767-768` (`elif wt: kind = "worker"`), `:685-689` (`worktree_of`), `:1124-1135` (`g5`: scratch write → None `:1127-1128`; outside → `ROUTE["G5 fence"]` `:1135`). Read: `bare-guard.py` 683-693, 762-770, 1113-1143.
- Edit 2, row S4: `"SHADOW BUILT ·"`, `"SHADOW ROLE ·"` to `stop-guard.py` `STOP` (`:71-80`, grep `STOP` hit `:71`) and `bare-guard.py` `STOP_HEADS` (`:128`, used `:1088`); tests: three in `test_stop_guard.py`, one in `test_bare_guard.py` (G6, `.env` fixture, `g6` `:1084-1103`; BASE red because `:1088` passes an unlisted head). `idle-wake.py:8-9, 42` writes `report_last_line` with no `STOP` filter (grep `STOP` in it: no match); the build confirms. Read: `stop-guard.py` 66-83, `bare-guard.py` 124-130, 1080-1111, `idle-wake.py` grep.
- Edit 3, row S4: `session="$job-gate"` for `shadow` plus a watch test (`<job>-gate` found, `<job>-shadow` not). Proof: `desk-watch.sh:47` (`build|check|devfix` → `$job-$kind`), case `:38-42`. Read: `desk-watch.sh` 25-60 and grep `session=|re=`.
- Edit 4, row S2: red sentence now quotes the first refusal: `desk-launch.sh:758` (count), `:762-767` (`:766` "two resume steps"), `:778`. Read: `desk-launch.sh` 756-779, grep on usage lines.
- Edit 5, row S5: "not a ranking" → "a routing table by band"; `never "failed"` removed. Proof: grep `rank|failed` on the card matches only line 21 (the test column's forbidden-word list).
- Also read: the preflight whole, the card whole, `writing-rules.md`, `areas/cobalt.md` headings (`:20`, `:33`), `330-sdk-spike-live.md` grep (no stop head named).
- No test run, no git write, no launch.

CARD 324 AMENDED · decisions: 1
