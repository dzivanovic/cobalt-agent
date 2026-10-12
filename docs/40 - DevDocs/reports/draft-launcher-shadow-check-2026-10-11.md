## §0 Headline
Card 386 re-issued twice over: rows L1–L9, header `SWEEP: 3 more found`. L2, L4, L5, L6 are the brain's wording, byte for byte.
Sweep of 366's check path (launcher → preflight → CHECK-HUB → desk tools) found three more failing tests, folded shadow-only and two-sided: L7 `card-fill.sh:67-71`, L8 CHECK-HUB `## PREFLIGHT` `BUILT` sentence (hub text), L9 `desk-done.sh:21-28`.
`«FILL` only in BASE and TIP. Nothing outside the class appeared.

## DECISIONS
none

## RECORDS
- Reads 21:45 ET, `main` HEAD `9e8b5ece`: `ops/desk/preflight.sh:45-263` whole (status `:103-131`, head `:134-187`, env `:207-226`, report `:228-250`, range `:251-255`); `ops/desk/card-fill.sh` whole (`:67-71` the `BUILT` and `self-check: 3 of 3` tests); `ops/desk/desk-done.sh:1-39` (`:21-28` kinds); `ops/desk/job-clean.sh:1-30` and the grep hits `:80`, `:83`, `:204`; `grep BUILT|self-check|status --porcelain|status --short` over `ops/desk` (other files: `bare-guard.py:146`, `stop-guard.py:77`, `desk-watch.sh:44` already carry `SHADOW BUILT`; `deploy-card.sh`, `deploy-step0.sh`, `desk-launch.sh:1079`, `:1271` are deploy-only); `grep "held unfixed|ready: "` over `ops/desk` → `desk-launch.sh`, `deploy-card.sh`, `deploy-step0.sh` only (deploy); `gate.sh` and `stage-set.sh` grep → no read of the report's last line or the tree status; `tests/ops/test_card_fill.py`, `test_desk_done.py` test names.
- Earlier reads: first and second issue (21:40 and 21:43 ET) as in their records: cards 324, 340, 341, 366; `CARD.md`; `CHECK-HUB.md` whole; `SHADOW-HUB.md:61,76,78`; `tests/ops/test_preflight.py:30-232`; `test_desk_launch_prechecks.py:73-365`.
- Not rows: `job-clean.sh` (card mode needs a landed, clean tree; a shadow is never merged; salvage mode saves a dirty tree); deploy-side `BUILT ·` readers (a shadow is never deployed).
- Row L8's sentence and rows L7, L9 are the drafter's wording (the brain gave none); the desk may reword before the build.
- Card: `grep «FILL` → BASE and TIP lines only. No launch, no git write, no command beyond reads.

DRAFTED · decisions: 0
