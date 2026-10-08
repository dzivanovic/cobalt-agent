## §0 Headline
- Card `118` row D amended for preflight check 15: `finally` now resets `ladderInFlight` only when `owned`.
- A skipped tick (`:1609`) no longer clears another fetch's flag. Header and rows A, B, C, E, F unchanged.
- New test `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag`, red on the bare-reset mutation.
- One defect in row C left unchanged (see DECISIONS 2).

## CHANGES
`docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md`, row D only, two edits:
- What: the sentence "A guard's `return` inside the `try` still runs `finally` and resets `ladderInFlight`" replaced by OWNERSHIP: `let owned=false;` before `try{`; `owned=true;` right after `ladderInFlight=true;` (before the fetch); `finally` runs `if(owned){ladderInFlight=false;}` beside row C's `clearTimeout(timer)`; `ladderInFlight||` stays the first clause of the first guard.
- Test: the `try{`-before-first-guard assertion kept, plus `let owned=false;` before `try{` and `owned=true;` between `ladderInFlight=true;` and `fetch('/radar'`. Added `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag`: every `ladderInFlight=false` sits inside `if(owned){…}` in `finally`; `owned=true;` is the only write after the declaration. Mutation partner: a bare `ladderInFlight=false;` in `finally` makes it raise.

## DECISIONS
1. `owned` over moving the guard before `try`: moving it would split the single combined guard at `:1609` and keep the other guards outside the `try`, undoing the row's "throw in a guard is said by the banner" property. `owned` is three small edits and keeps that property.
2. UNPROVEN, not fixed (out of scope): row C declares `const ctl`/`timer` inside the `try`, but `clearTimeout(timer)` runs in `finally`, where a block-scoped `const` is not visible (ReferenceError on every tick). The builder must declare `timer` before `try{` (beside `owned`). The desk should amend row C. Row C's `:1197` assertion text also now reads `finally{clearTimeout(timer); if(owned){ladderInFlight=false;}}`.

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `727ec63e` (card BASE `50b0cd87` unchanged per preflight NOTE 1).
- Read `src/cobalt/aset/radar_panel.py:1603`–`:1636`: `:1605` `let ladderInFlight=false;`, `:1609` first guard opens `if(ladderInFlight||…`, `:1611` `ladderInFlight=true;`, `:1612` `try{`, `:1630` `}finally{ladderInFlight=false;}`.
- Read the preflight, check 15 and `## ISSUES` (`radar-display-fix-preflight-2026-10-08.md:19`, `:24`–`:31`).
- Read the card in full before and after the edit; `git diff` not run.
- Read `areas/cobalt.md` (`## What Cobalt is`, `## Build rules`) and `topics/writing-rules.md`.

RADAR DISPLAY CARD AMENDED · decisions: 2
