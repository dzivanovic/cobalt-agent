# Card 692 band-routing-fr3-check — preflight (2026-10-17 10:12 EDT, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `692-…-card.md:1-15` | JOB `band-routing-1015`, CLASS K5, INSTALL none, BRANCH `ops/band-routing-1015`, WORKTREE `band-routing-1015`, BASE `f2ca3e1a`, TIP `4b62c2fa`, REPORT (worktree `band-routing-build-fr9-2026-10-17.md`), CHECK REPORT, HOUSE A `grok`, HOUSE B `as needed`, DB `none`, RESTARTS `none`, RULINGS `2026-10-15 R1532` | OK |
| 2 | `git rev-parse --short=8 4b62c2fa` | `4b62c2fa` (the fix commit: `fix(band-routing-1015): close step excepts …`) | OK |
| 3 | `git log --oneline -6 ops/band-routing-1015` | `6c0ba560` (report), `4b62c2fa` (fix), `9bd05618` (red), `da95e8c7` (report opened), `8b142c56`, `4fc9b9da`: as the card's WHY | OK |
| 4 | `git diff --stat 4b62c2fa 6c0ba560 -- . ":(exclude)docs"` | prints nothing (head is docs only) | OK |
| 5 | `git merge-base`: BASE `f2ca3e1a` | `git diff --stat f2ca3e1a ops/band-routing-1015` lists 17 files vs `4b62c2fa`: 16 earlier paths + `band-routing-build-fr9-2026-10-17.md`; no `src/`, `configs/`, `.claude/`; `desk-done.sh` absent | OK |
| 6 | `ls` of CHECK REPORT `reports/band-routing-check-fr3-2026-10-17.md` | `No such file or directory` (new path) | OK |
| 7 | `grep -c -E "«FILL\|TODO\|XXX"` on the card | `0` | OK |
| 8 | HOUSE A / HOUSE B | `HOUSE A: grok` present; `HOUSE B: as needed`; X6 holds the Gemini-id N/A sentence (brain 2026-10-17) | OK |
| 9 | RESTARTS | `RESTARTS: none`; the touched paths are `ops/desk/`, `docs/`, `tests/`; row R3 runs `uv run cobalt jobs restarts` on both ranges and compares | OK |
| 10 | FR-9 row has RED, control, quoted output | RED: mutations (a)(b)(c) + `--runxfail` on `9bd05618` text, each undone and proved by `git diff --stat 4b62c2fa -- <file>` empty; controls: build and other-line tests GREEN before/after; GREEN run `-k "check_o1 or fr9"` with PASSED lines quoted; hand run of the routed tree with two untracked lines | OK |
| 11 | scope: rows S0, FR-9, E1, M1, D1, R3, G1 vs `git diff --stat f2ca3e1a 4b62c2fa` | every `files` cell is in the diff or read-only; `desk-watch.sh` and the test file are read-only + undone mutations; `## NOT IN THIS JOB` fences the other desk scripts | OK |
| 12 | card tells checker to quote any refusal as a finding | WHY: "If any command or tool refuses, quote the refusal as a finding (what was refused, the exact text); do not work around it." | OK |
| 13 | no new command outside the standing allow line | rows use `git`, `uv run pytest`, `uv run cobalt jobs restarts`, `sh …/gate.sh`, `grep`, `ls`; the same shapes as card 666 (D1/R3/G1 there). `git merge-tree` deliberately avoided (M1). The G1 `log:` path is ASK DESK 2, not a fail | OK |
| 14 | `file:line` `desk-watch.sh` @ tip (`git grep -n`) | `:96` comment, `:97` `unclean() {`, `:99` `dirt=$(git -C … status --short 2>&1)`, `:100` `# card 583 FR-9: …`, `:113` `close_worker() {`, `:129` and `:138` `why=$(unclean)`. `:101` the `case`, `:102` `[ -z "$dirt" ] \|\| …` read in `git show`: match. Lines `:65`, `:74` (`routed)` arms) and the mapping line read in the same show: present | OK |
| 15 | `file:line` tests @ tip | `:494` `ROUTED_STOP`, `:496` `IDLE_GATE`, `:497` `IDLE_JOB_BUILD`, `:500` `class RWatch`, `:649` `test_check_o1_…`, `:663` `test_fr9_a_shadow_…`, `:673` `test_fr9_control_a_build_kind_…`, `:686` `test_fr9_control_a_routed_tree_with_any_other_…`; `grep xfail` of the file → no hit | OK |
| 16 | `file:line` `preflight.sh` / `desk-launch.sh` @ tip | `preflight.sh:159` `… [ "$other" = "?? SHADOW-INSTRUCTIONS.md" ]`; `desk-launch.sh:1817` `{ [ -z "$shadow" ] && [ -z "$routed_tree" ]; } \|\| [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] \|\| dirt=""` | OK |
| 17 | build report ends | last line `BUILT · job: band-routing-1015 · tip: 4b62c2fa | on f2ca3e1a | … rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 171440`; `## DECISIONS` at `:141`, `## E2 RED` at `:73` | OK |
| 18 | read sources exist | 583 card (`## FIX ROUND 3`/FR-9: 8 hits), 671, 670, `band-routing-check-fr2-2026-10-17.md` (O1 at `:6`, `:92`), `check-662-and-583-fr2-decisions-2026-10-17.md`, `draft-band-routing-fr3-check-2026-10-17.md`, fix-round-3 report in the worktree | OK |
| 19 | M1 stats vs own BASE | 583: `git diff --stat f2ca3e1a ops/band-routing-1015 -- <3 files>` → SHADOW-HUB 15, bare-guard 5, desk-launch 80 (90+/10-). 671 (BASE `7f415a4f`, head `7b22e411`): SHADOW-HUB 12, bare-guard 15, desk-launch 4 (22+/9-). 670 (BASE `f2140694`, head `9f281a6a`): prints nothing. Overlap 583/671 on all three files; 670 touches none: the card's claim and its draft agree | OK |
| 20 | card committed | `git log --oneline -3 -- <card>` → `573e96fd docs(desk): check cards 690 and 692 drafted, preflight prompts 694 and 695 (R1780)` | OK |
| 21 | `git diff --stat HEAD -- <card>` | prints nothing (empty), as found | OK |
| 22 | blocker of `desk-launch.sh check "<card>"`: `check-scratch-fr1` DEPLOYED? | NOT deployed: `grep -c "STAGED-CARD" ops/desk/stage-set.sh` on main → `0`; `git log --oneline main -3 -- ops/desk/stage-set.sh` newest is `dd4d968d` (no STAGED-CARD commit). Per the card's ORDER, the check must not launch yet | OK (a launch blocker, not a card fail: see ISSUES) |

## ISSUES
- BLOCK 22: `check-scratch-fr1` is not deployed (no `STAGED-CARD` in `stage-set.sh` on main as of 10:12 EDT). Same-JOB check cards 638/666/692 in `band-routing-1015-check` would still refuse staging. Desk: launch `desk-launch.sh check "<card>"` only after that DEPLOYED line; this is the card's own ORDER, not a card defect.
- NOTE 13: row R3/E1/G1 use `uv run …` and `sh …/gate.sh`; the card 666 rows use the same; an `ASK DESK` is not a fail. The G1 `log:` path is owed (ASK DESK 2).
- NOTE 16: `HOUSE B: as needed` names no house by id (666/638 precedent); `TIP 4b62c2fa` is the BUILT tip, head `6c0ba560` is docs only.
- NOTE 19: M1 hunk disjointness (583 vs 671 in `desk-launch.sh`, `bare-guard.py`, `SHADOW-HUB.md`) is not read here (stat only); the check reads the `@@` hunks. Deploy order 583, 671, 670, so a conflict falls on 671's deploy.
- Card quality: no FAIL found in the card itself. 

PREFLIGHT DONE · card: band-routing-fr3-check · checks: 22 · fails: 0 · ready: YES
