# draft-583-fr6-closeout · 2026-10-16

## §0 Headline
Card 583 amended (only the card edited, uncommitted): FR-6 gains the closeout mapping (`routed` hands `build` to `desk-done.sh`, one line in `desk-watch.sh`'s `close_worker`) with its reason, a stub-`desk-done.sh` test and a shadow control.
FR-6 and FR-7 drop "the comment line and"; X11 gains "(superseded by FR-8)".
Also updated: FIX ROUND 2 scope, `## NOT IN THIS JOB`, X13, `## RECORDS`. `BASE`, `TIP`, `RULINGS` stand.

## DECISIONS
- ASK DESK: the brain's cite says `shadow` maps itself to build at `desk-done.sh:53`; on the tip it is `:54`. The card says `:54`. Default: `:54`. [13:03 EDT]
- ASK DESK: the card says the new test's stub listing is "one idle `<job>-gate` row, tree clean, report committed" — the builder shapes the tmp repo; the exact fixture is its call. Default: as written. [13:03 EDT]
- ASK DESK: `desk-watch.sh`'s header comment and usage string still omit `routed` (preflight ISSUE 4, cosmetic); not in the brain's answer, left out. Default: out. [13:03 EDT]

## RECORDS
- Card: `docs/40 - DevDocs/prompts/2026-10-15/583-band-routing-card.md` (7 insertions, 6 deletions; `git diff --stat`).
- Proved on `git show`/`git grep ops/band-routing-1015`: `desk-watch.sh:59`, `:70` (two `case "$kind"`), `:108` `close_worker`, `:151` the `desk-done.sh` call; `desk-done.sh:46`, `:54`, `:55`, `:46-67`; `tests/ops/test_band_routing_1015.py:403`, `:411`, `:421` are the decorators, `:402` blank (the lines above `:411`, `:421` taken from the preflight, not re-read).
- The `ISSUE 2` line check: the card's X13/`## NOT IN THIS JOB`/scope now name the closeout mapping line. `## FIX ROUND 2 ORDER` lists no `desk-watch.sh` edit; unchanged.
- Nothing was run but reads; no test executed. No git write.

DRAFTED · decisions: 3
