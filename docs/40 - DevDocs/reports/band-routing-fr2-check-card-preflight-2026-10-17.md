# Card 666 band-routing-1015-fr2-check — preflight (2026-10-17, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `666-…-card.md:1-15` against the 638 precedent | JOB `band-routing-1015`, LADDER, CLASS K5, INSTALL none, BRANCH `ops/band-routing-1015`, WORKTREE `band-routing-1015`, BASE `f2ca3e1a`, TIP `fda2300b`, REPORT (in worktree, `band-routing-build-fr6-2026-10-16.md`), CHECK REPORT, HOUSE A `grok`, HOUSE B `as needed`, DB `none`, RESTARTS `none`, RULINGS `2026-10-15 R1532`. No BAND line (the build card 583 has none). | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline -5 ops/band-routing-1015` | `4fc9b9da` (report), `fda2300b` (fix), `45b9d8c7` (red), `ac172ab9`, `7bf43c2b`: TIP `fda2300b` is the BUILT tip, head `4fc9b9da` | OK |
| 3 | `git diff --stat fda2300b 4fc9b9da -- . ":(exclude)docs"` | prints nothing | OK |
| 4 | `ls` of the CHECK REPORT path `reports/band-routing-check-fr2-2026-10-17.md` | `No such file or directory` (a new path) | OK |
| 5 | `grep -c "«FILL"` on the card | `0` | OK |
| 6 | HOUSE A present: header line | `HOUSE A: grok` (as 638) | OK |
| 7 | HOUSE B / Gemini N/A sentence (`grep` of the card, X7 `:57`) | `HOUSE B: as needed`; X7 holds "house B is N/A (the CLI rejects the id, K5 card pending), a harness record, not a finding (brain, 2026-10-17)" | OK |
| 8 | RESTARTS | `RESTARTS: none`; row R3 runs `uv run cobalt jobs restarts` on both ranges and compares to `none` | OK |
| 9 | scope: rows S0, FR-6, FR-7, FR-8, E1, D1, R3, T1, G1 | FR-6 to FR-8 are the three new rows; E1 is "a SHORT re-run" of FR-1 to FR-5 and B1-B6 with at most one mutation per row | OK |
| 10 | `git diff --name-only --no-renames 7bf43c2b fda2300b` | `SHADOW-HUB.md`, `band-routing-build-fr6-2026-10-16.md`, `desk-launch.sh`, `desk-watch.sh`, `tests/ops/test_band_routing_1015.py`: the five S0 lists | OK |
| 11 | `git diff --name-only --no-renames f2ca3e1a fda2300b` | 15 paths: BUILD-HUB, CARD, CHECK-HUB, SHADOW-HUB, `bare-guard.py`, `desk-launch.sh`, `desk-watch.sh`, `preflight.sh`, `test_band_routing_1015.py`, `test_check_hub_shadow.py` and five docs reports; no `src/`, `configs/`, `.claude/`; `desk-done.sh` absent | OK |
| 12 | `desk-done.sh` not in `files` (read of the card's `files` column, every row) | no row lists `desk-done.sh`; it appears in the text only as read-only evidence (FR-6) and as "a hunk there is a finding" (`## NOT IN THIS JOB`) | OK |
| 13 | the card tells the checker to quote any refusal as a finding: `grep -n -i refusal` of the card, CHECK-HUB and CARD.md | NO such sentence in the card. The card's "refusal" hits are the tested refusals (FR-6 `usage:`, FR-7 arms, `:994`). `CHECK-HUB.md:51` (a) says a refused added command is recorded under `## RECORDS` (`REFUSED, not needed: …`), not a finding | FAIL |
| 14 | `file:line` `desk-watch.sh` on the tip: `git grep -n` | `:65` `routed) report=… re='^(BUILT ·\|FAILED)'`, `:74` `routed) job=…; session="$job-gate"`, `:110` `close_worker() {`, `:153` mapping line `[ "$kind" = routed ] && echo build \|\| echo "$kind"` | OK |
| 15 | `file:line` `desk-launch.sh` on the tip | `:393` `--routed)`, `:992` and `:994` the `the card must be` refusals, `:997` charset arm, `:998` `..` arm, `:999` FR-1 arm `*/./*\|*//*)`, `:2356` the `watch=` line, `:287` `watch_line() {` (the card's `:991` pass-through is its `*/./*\|*//*) ;;` line; it was not printed by `-e` and is not re-read here) | OK |
| 16 | `file:line` tests on the tip | `:403` `test_o1_…`, `:419` `test_x5_…`, `:549` `test_fr6_the_routed_watcher_…`, `:607` `test_fr7_a_card_outside_…`, `:620` `test_fr7_control_…`, `:629` `test_fr8_the_429_…`, `:639` `test_fr8_control_…` all match. `:410` `test_o3_…`, `:570`, `:579`, `:588`, `:462` not printed by my pattern, matched by name only | OK (see N2) |
| 17 | `git grep -c "reading R1532's 'Terra backup'"` on `SHADOW-HUB.md` at the tip | `1` (the FR-8 clause; DEPLOY PROOF line `:64` expects `1`) | OK |
| 18 | `desk-done.sh` on the tip, `git grep -n` | `:47` `build) done_re='^BUILT'`, `:54` `shadow) done_re='^SHADOW (BUILT\|ROLE)'; kind=build` as FR-6 reads them; `desk-done.sh` is not in the 7bf43c2b..fda2300b diff (check 10) | OK |
| 19 | read-source files named by the card exist | the 583 card, drafters 645, 646, 651, `band-routing-check-fr1-r2`, `-fr1-decisions`, `band-routing-answer`, `cto-2026-10-14-words.md` all present; `cto-2026-10-15.md` holds `R1532` at `:102` `HIS RULING · APPROVED` | OK |
| 20 | RULINGS row: card carries only `2026-10-15 R1532` | row `:102` of `cto-2026-10-15.md` is `HIS RULING · APPROVED` (routing B) | OK |
| 21 | card committed: `git log --oneline -2 -- <card>` | `b5d62588 docs(desk): check card 666 for card 583 fix round 2 drafted, preflight prompt 667` | OK |
| 22 | `git diff --stat HEAD -- <card>` | prints nothing (empty), as found | OK |
| 23 | what blocks `desk-launch.sh check "<card>"` | not run (no `sh` in my allowed list, and the launch is not mine). Read-side blockers: none found beyond check 13; `authorize.sh` / `preflight.sh check` are the check seat's own first calls and I could not run them | OK (see N3) |

## ISSUES
- FAIL 13: the card has no sentence telling the checker to quote any refusal as a finding. `CHECK-HUB.md:51` says to record a refused added command under `## RECORDS`; the card only asks for the tested refusals. Desk: add the sentence to the card (a one-line edit of `## NOT IN THIS JOB` or `## CHECK ASKS`), or take the hub's rule and drop this check.
- N2 NOTE: lines `:410`, `:462`, `:570`, `:579`, `:588` of the test file and `desk-launch.sh:991` were not printed by my greps; the check seat confirms them with `grep -n` on the tip.
- N3 NOTE: `HOUSE B: as needed` names no house by id (the 638/633 precedent); `TIP fda2300b` is the BUILT tip (head `4fc9b9da`, docs only). The gate `log:` path is owed to the desk (draft ASK DESK 3).
- Blocks the check launch: only FAIL 13 if the desk wants it fixed first; no mechanical blocker found. Desk steps owed: edit the card (then commit), then `desk-launch.sh check "<card>"`.

PREFLIGHT DONE · card: band-routing-1015-fr2-check · checks: 23 · fails: 1 · ready: NO
