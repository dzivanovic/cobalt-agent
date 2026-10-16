# Card 583 band-routing-1015 — FR-6 to FR-8 preflight round 2 · 2026-10-16

Card: `prompts/2026-10-15/583-band-routing-card.md` (FIX ROUND 2, amended). Branch tip read: `7bf43c2b`. Read-only: nothing run but reads; no test executed. Issue 1 (closeout hole) closed; issues 2 and 3 closed; ready YES.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <card>`; `git log --oneline -- <card>` | diff empty (as found); last commit `3ee7bf75` | OK |
| 2 | round 1's checks 2-5 (FR-6 vs direction, ASK DESK / shape-B leftovers, `desk-watch.sh` count, scope/NOT IN/X13/RECORDS agreement) re-read on the amended card | FR-6 row (`:53`) holds kind `routed`, one `case` arm in each of the two `case "$kind"` blocks, `^(BUILT ·\|FAILED)`, session `<job>-gate`; RED quoted whole (`2 failed` / `2 xfailed`); no shape-B text left | OK |
| 3 | issue 1: FR-6 row names the closeout mapping line and the stub test | `:53` "THE CLOSEOUT … ONE mapping line in `desk-watch.sh` (found by content, in `close_worker`) hands `build` to `desk-done.sh` when `$kind` is `routed`"; `test_fr6_a_routed_closeout_hands_build_to_desk_done` (stub records args, stub called once with `build`, RED: called with `routed`); control `test_fr6_control_a_shadow_card_closeout_still_passes_shadow` (stub called with `shadow`) | OK |
| 4 | issue 1: `desk-done.sh` not in `files` | `grep -n -o -F "desk-done.sh"` → hits only at `:53` (FR-6 row text, files cell lists `desk-launch.sh`, `desk-watch.sh`, test file), `:66`, `:97`, `:122`; `:22` scope names no `desk-done.sh` file; every hit says "stays out" / "untouched" | OK |
| 5 | issue 1: `## NOT IN THIS JOB` `:66`, scope `:22`, X13 `:97`, `## RECORDS` `:122` agree | all four say: `desk-watch.sh` only the `routed` arm in each of the two `case "$kind"` blocks plus the one closeout mapping line (`close_worker`, tip `:151`); `desk-done.sh` stays out; X13 asks the mapping, the shadow control and `desk-done.sh` untouched | OK |
| 6 | issue 2: `grep -n -F "comment line"` of the card | one hit, `:48` (FR-1 row, history: "comment lines and the decorator" of the O2 xfail, built in round 1). None in FR-6 (`:53`), FR-7 (`:54`); `:122` says "the comment-line words are out of FR-6 and FR-7". On the tip `:377` has a blank line `:376` and no decorator (FR-1 marker already gone) | OK (see issue 1) |
| 7 | issue 2: FR-6 and FR-7 marker wording vs the tip | both say "only the `@pytest.mark.xfail(strict=True, …)` decorator … the line above it is blank"; tip `:402`, `:410`, `:420` blank (git grep `-B1`), decorators at `:403`, `:411`, `:421` | OK |
| 8 | issue 3: `grep -n -F "superseded by FR-8"` | `:95` (X11: "cite R1532 and 2026-10-14 item 7 (superseded by FR-8)") and `:122` | OK |
| 9 | the card's diff `fbc8a069..HEAD` touches only those places | hunks: `:22` (scope: + "and its one closeout mapping line"), `:53` (FR-6), `:54` (FR-7 marker wording), `:66` (NOT IN THIS JOB), `:95` (X11), `:97` (X13), `:122` (RECORDS, new line). No header, `RULINGS`, `BASE`, `TIP`, FR-8, ORDER, DEPLOY PROOF line changed | OK |
| 10 | diff of the FR-6 row vs round 1: nothing else moved | added: THE CLOSEOUT sentence, the marker wording, `test_fr6_a_routed_closeout_hands_build_to_desk_done`, `test_fr6_control_a_shadow_card_closeout_still_passes_shadow`, the `close_worker` mapping in the files cell; the WATCH edit, the `routed` arms, `test_x5_…` one assertion, `test_fr6_the_routed_watcher_…`, `test_fr6_control_a_high_card_…`, RED text unchanged | OK |
| 11 | FR-7 row diff | only the marker sentence; the arm, refusal text, sweep, tests, control unchanged | OK |
| 12 | FR-8 unchanged and byte-equal to direction | FR-8 row `:55` and B3 `:43` not in the diff; citation present as in round 1 (`:43`, `:55`, `:70` per round 1 check 8) | OK |
| 13 | `RULINGS` / DESK RECORD | header `RULINGS: 2026-10-15 R1532` unchanged (not in diff); `:122` says `RULINGS` stands | OK |
| 14 | ORDER note (card 641 deploys before this round's check) | `:22`, `:61` unchanged | OK |
| 15 | restart class | `:120` unchanged (`desk-watch.sh` → "operator script; no Cobalt reader"); `RESTARTS: none` stands | OK |
| 16 | `file:line` samples on `git show`/`git grep ops/band-routing-1015:<file>` (12 of them) | `desk-watch.sh:60` `build) … ^(BUILT\|FAILED)`; `:64` `shadow) … ^(SHADOW BUILT\|SHADOW ROLE\|FAILED)`; `:71` `build\|check\|devfix` session `$job-$kind`; `:72` `shadow` `$job-gate`; `:108` `close_worker() {`; `:151` `out=$(sh "$here/desk-done.sh" "$rid" "$report" "$kind")`; `desk-done.sh:54` `shadow) done_re='^SHADOW (BUILT\|ROLE)'; kind=build ;;`; `:55` `*) refuse "unknown kind: $kind"`; `desk-launch.sh:287` `watch_line() {`, `:991` `"$PROMPTS"/*-card.md) ;;`, `:997` `*/./*\|*//*)`, `:1643` `BAND_FROM=20261016`, `:1667` `exec sh "$0" shadow "$card" --model "$bid" --routed`, `:2354` `watch=$(watch_line "$kind" "$card")`; `test_band_routing_1015.py:403`, `:411`, `:421` decorators, `:402`/`:410`/`:420` blank | OK |
| 17 | allow string for `desk-watch.sh routed` | launcher allow `Bash(sh /Users/cobalt/.claude/ops/*)` covers any kind (round 1 check 15); card makes no allow change | OK |
| 18 | what blocks `desk-launch.sh build "<card>" "FIX ROUND row FR-6"` | nothing found: card committed and clean (check 1); branch tip `7bf43c2b` is the card's; card is dated 2026-10-15 with no `BAND`, so the BAND gate does not apply (Opus line). Card 641 blocks only this round's CHECK, not the build | OK |

## ISSUES

1. NOTE: `grep -n -F "comment line"` finds `:48` (FR-1 row, built in round 1, "the comment lines and the decorator" of the O2 xfail); history of a built row, not FR-6/FR-7. Tip `:377` shows no marker or comment above the `def`. No action.
2. NOTE: `desk-watch.sh`'s header comment and usage string (`:2`, `:49`) still omit `routed` (cosmetic; left out by the desk's default).
3. NOTE: `desk-watch.sh:59`/`:70` (the `case "$kind" in` lines) were located by the adjacent arms `:60`/`:71` — my pattern for the `case` line itself did not match; the arms sit where the card says.

PREFLIGHT DONE · card: band-routing-1015-fixround2 · checks: 18 · fails: 0 · ready: YES
