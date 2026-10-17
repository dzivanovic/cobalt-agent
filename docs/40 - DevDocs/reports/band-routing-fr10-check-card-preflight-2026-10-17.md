# Card 703 band-routing-fr10-check — preflight (2026-10-17, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `703-…-card.md:1-15` | JOB `band-routing-1015`, CLASS K5, INSTALL none, BRANCH `ops/band-routing-1015`, WORKTREE `band-routing-1015`, BASE `f2ca3e1a`, TIP `05654335`, REPORT (worktree `band-routing-build-fr10-2026-10-17.md`), CHECK REPORT, HOUSE A `grok`, HOUSE B `as needed`, DB `none`, RESTARTS `none`, RULINGS `2026-10-15 R1532` | OK |
| 2 | `git rev-parse --short=8 ops/band-routing-1015` and `git rev-parse --short=8 05654335` | branch head `2880eb0e`; `05654335` resolves (the fix commit `fix(band-routing-1015): close step excepts the check seat's one untracked SHADOW-INSTRUCTIONS.md too (FR-10…)`); TIP = the code commit | OK |
| 3 | `git log --oneline ops/band-routing-1015 -6` | `2880eb0e`, `05654335`, `630542a7`, `061f6d6f`, `3f399b60`, `6c0ba560`: as the card's WHY | OK |
| 4 | `git diff --stat 05654335 2880eb0e -- . ":(exclude)docs"` | prints nothing (head is docs only) | OK |
| 5 | `git merge-base ops/band-routing-1015 main` | `f2ca3e1a9470a1bf0916d47a921b735f5316a927` = BASE | OK |
| 6 | `git diff --name-only --no-renames f2ca3e1a 05654335` | 19 paths: 4 hubs (`BUILD-HUB`, `CARD`, `CHECK-HUB`, `SHADOW-HUB`), 9 reports/`.result`, `bare-guard.py`, `desk-launch.sh`, `desk-watch.sh`, `preflight.sh`, `test_band_routing_1015.py`, `test_check_hub_shadow.py`; no `src/`, `configs/`, `.claude/`; `desk-done.sh` absent: as row S0 | OK |
| 7 | `git diff --stat 3f399b60 05654335` | report (35), `desk-watch.sh` (2), `test_band_routing_1015.py` (18): 3 files, 53+/2-; row S0's list | OK |
| 8 | `git diff 3f399b60 05654335 -- ops/desk/desk-watch.sh` | one hunk `@@ -98,7 +98,7 @@ unclean()`: `shadow\|routed)` → `shadow\|routed\|check)`; FR-6 arms and FR-9 comment untouched | OK |
| 9 | `ls` of CHECK REPORT `reports/band-routing-check-fr4-2026-10-17.md` | `No such file or directory` (new path) | OK |
| 10 | `grep -c -E "FILL\|TODO\|XXX"` on the card | `0` | OK |
| 11 | HOUSE A / HOUSE B | `HOUSE A: grok`; `HOUSE B: as needed`; X6 holds the Gemini-id N/A sentence (brain 2026-10-17) | OK |
| 12 | RESTARTS `none` vs touched paths | `ops/desk/`, `docs/`, `tests/` only; row R3 runs `uv run cobalt jobs restarts` on both ranges and compares | OK |
| 13 | FR-10 row: RED, controls, quoted output | RED: mutations (a) back to `shadow\|routed)` with `--runxfail`/plain, (b) widened `*)`, (c) glob equality, each undone, undo proved by `git diff --stat 05654335 -- <file>` printing nothing; controls: build and other-line tests GREEN before/after; GREEN run `-k "check_o1 or check_fr3 or fr9 or fr10"` with PASSED lines quoted; hand run in a tmp worktree; `grep` of `tree not clean` / `SHADOW-INSTRUCTIONS` for the CONSEQUENCE | OK |
| 14 | scoped to FR-10, FR-9 short re-run | WHY and X-asks: "scoped to FR-10: FR-9 and FR-6 to FR-8 get a short re-run only"; E1 is the short re-run with the pins (69 passed; 373 on the eight files) | OK |
| 15 | scope = `git diff --stat f2ca3e1a 05654335` files | every `files` cell is in the diff or read-only; `## NOT IN THIS JOB` fences `desk-launch.sh`, `desk-done.sh`, `preflight.sh`, `bare-guard.py`, hubs, `CARD.md`, tests beyond undone mutations | OK |
| 16 | M1 stats (stat only, not a merge) | 583: `git diff --stat f2ca3e1a ops/band-routing-1015 -- <3 files>` → SHADOW-HUB 15, bare-guard 5, desk-launch 80 (90+/10-). 671 (BASE `7f415a4f`): SHADOW-HUB 12, bare-guard 15, desk-launch 4 (22+/9-). 670 (BASE `f2140694`): prints nothing. Overlap 583/671 on all three files; 670 none: as the card and its draft say | OK |
| 17 | no new command outside the standing allow line (L62) | rows use `git`, `uv run pytest`, `uv run cobalt jobs restarts`, `sh …/gate.sh`, `grep`, `ls`; `git merge-tree` avoided; `grep -c -F "gate.sh band-routing-1015 offline --deploy-gate"` → `1` in 703 and `1` in 692 (G1 copied from 692); `log:` path is ASK DESK 2, not a fail | OK |
| 18 | card tells checker to quote any refusal as a finding | WHY ends: "If any command or tool refuses, quote the refusal as a finding (what was refused, the exact text); do not work around it."; CHECK ASKS X7 repeats it | OK |
| 19 | `file:line` `desk-watch.sh` @ tip (`git show ops/band-routing-1015:ops/desk/desk-watch.sh`, lines by `grep -n` on the worktree copy, same code) | `:72` `build\|check\|devfix) job=…`; `:97` `unclean() {`; `:100` `# card 583 FR-9: …`; `:101` `case "$kind" in shadow\|routed\|check) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] \|\| dirt="" ;; esac`; next line `[ -z "$dirt" ] \|\| { echo "tree not clean"; return; }`; `:113` `close_worker() {`; `why=$(unclean)` in it; `prodwrite`/`close` skip it (read in the show) | OK |
| 20 | `file:line` tests @ tip | `:494` `ROUTED_STOP`, `:496` `IDLE_GATE`, `:497` `IDLE_JOB_BUILD`, `:500` `class RWatch`, `:649` `test_check_o1_…`, `:663` `test_fr9_a_shadow_…`, `:673` `test_fr9_control_a_build_kind_…`, `:686` `test_fr9_control_a_routed_tree_with_any_other_…`, `:705` `test_check_fr3_o1_…`, `:720` `test_fr10_control_…`; `grep xfail` → no hit | OK |
| 21 | `file:line` `preflight.sh` / `desk-launch.sh` @ tip | `preflight.sh:159` `… { [ -n "$shadow" ] \|\| [ -n "$routed" ]; } && [ "$other" = "?? SHADOW-INSTRUCTIONS.md" ]`; `desk-launch.sh:1817` `{ [ -z "$shadow" ] && [ -z "$routed_tree" ]; } \|\| [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] \|\| dirt=""` | OK |
| 22 | sources the card names exist | 583 card (`FR-10`: 6 hits), 671, 670, `band-routing-check-fr3-2026-10-17.md`, `ops/desk/gate.sh` | OK |
| 23 | card committed | `git log --oneline -3 -- <card>` → `91f90808 docs(desk): FR-10 check card 703 drafted, preflight prompt 704` | OK |
| 24 | `git diff --stat HEAD -- <card>` | prints nothing, as found (prompt 704 likewise) | OK |
| 25 | blocker of `desk-launch.sh check "<card>"`: `check-scratch-fr1` DEPLOYED? | `grep -c -F "STAGED-CARD" ops/desk/stage-set.sh` → `8` on main: deployed; nothing blocks the launch | OK |

## ISSUES
- NOTE 11: `HOUSE B: as needed` names no house by id (666/692 precedent); `TIP 05654335` is the BUILT tip, head `2880eb0e` is docs only.
- NOTE 17: the G1 `log:` path is owed (ASK DESK 2), not a fail.
- NOTE 16: M1 hunk disjointness (583 vs 671 in the three files) is not read here (stat only); the check reads the `@@` hunks. Deploy order 583, 671, 670, so a conflict falls on 671's deploy.
- NOTE 19: preflight.sh treats a check as routed only on `BAND LOW\|MID` with a folder dated on or after 2026-10-16; this card (no BAND) sees none of that, which is the card's CONSEQUENCE paragraph, for the checker to answer.
- Blockers of the launch: none. Card quality: no FAIL found.

PREFLIGHT DONE · card: band-routing-fr10-check · checks: 25 · fails: 0 · ready: YES
