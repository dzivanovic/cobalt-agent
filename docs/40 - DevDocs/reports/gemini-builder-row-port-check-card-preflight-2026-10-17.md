# Card 710 gemini-builder-row-fr1 check card (PORT, FR-2) — preflight (2026-10-17, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `710-…-card.md:1-16` | JOB `gemini-builder-row-fr1`, BRANCH `ops/gemini-builder-row-fr1`, BASE `13bcd579`, TIP `52a0600d`, CHECK REPORT `reports/gemini-builder-row-fr1-check-2026-10-17.md`, BAND `HIGH`, HOUSE A `grok`, HOUSE B `as needed`, DB `none`, RESTARTS `none` | OK |
| 2 | `git merge-base main ops/gemini-builder-row-fr1` | `13bcd579e916603976b7faee758355dfa07d8022` = BASE | OK |
| 3 | `git rev-parse --short=8` of `52a0600d`, `ops/gemini-builder-row-fr1`, `695f8bde`, `7f415a4f` (one per call) | `52a0600d`, `5fea0cc4`, `695f8bde`, `7f415a4f`. A single multi-revision call was refused ("Needed a single revision"), so the four ran separately. | OK |
| 4 | `git log --oneline 13bcd579..ops/gemini-builder-row-fr1` | `5fea0cc4` (build report), `52a0600d` (fix, FR-2), `395a9e77` (wip red, PORT) | OK |
| 5 | `git diff --stat 52a0600d 5fea0cc4 -- . ":(exclude)docs"` | prints nothing: the head past the tip is docs only | OK |
| 6 | `git diff --stat 13bcd579 52a0600d` | hub 12, bare-guard 15, desk-launch 4, test_band_routing 4, test_bare_guard 97, test_desk_launch_shadow 30, test_shadow_hub_file 47; `7 files changed, 189 insertions(+), 20 deletions(-)`: as row S0 | OK |
| 7 | `git merge-base --is-ancestor 695f8bde ops/gemini-builder-row-1017` | exit 0 (no output): the checked tip is still on the old branch | OK |
| 8 | `git diff --stat 7f415a4f main -- <the 3 test files>` | prints nothing: main has not touched them | OK |
| 9 | `git diff --stat 695f8bde ops/gemini-builder-row-fr1 -- <the 3 test files>` | prints nothing (done on all three at once; per-file is the checker's row P1) | OK |
| 10 | `git diff --stat 13bcd579 main -- ops tests "…/SHADOW-HUB.md"` | prints nothing: row P2's seam read, a plain merge | OK |
| 11 | DEPLOY PROOF string 1: `grep -c -F "agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m"` on the worktree hub | `1` (before `0` is by the card, the BASE tree) | OK |
| 12 | DEPLOY PROOF string 2: `grep -n -F "gemini-4-argon-high) ;;"` on the worktree launcher | `404:        gemini-4-argon-high) ;;` | OK |
| 13 | DEPLOY PROOF string 3: `grep -n -F "card 671 G2/FR-1: agy --add-dir D or --add-dir=D (D/**), read for agy only"` on the worktree guard | `1204:` (one line) | OK |
| 14 | the four shadow test files exist | `ls` lists `test_desk_launch_shadow.py`, `test_shadow_hub_file.py`, `test_bare_guard.py`, `test_band_routing_1015.py` on the tip worktree | OK |
| 15 | file:line sample 1: `grep -n -F "card 671 L1"` launcher | `377:# card 671 L1: of the Gemini ids only gemini-4-argon-high (R1738); …` | OK |
| 16 | file:line sample 2: `grep -n -F "gemini-*"` launcher | `405:        gemini-*) refuse "shadow: model '$model' is a Gemini id not admitted; …"`, after the `:404` arm | OK |
| 17 | file:line sample 3: `grep -n -F "card 583"` guard | `1284:        # card 583 B6: …` as the card says | OK |
| 18 | file:line sample 4: `grep -n` on the hub for `## BUILDERS`, the Gemini row, the Gemini note, `X1 for Gemini`, `BAND ROUTING (his 2026-10-15` and the band rows | `14` BUILDERS; `22` Gemini row; `28` Gemini note; `30` X1 paragraph; `32` BAND ROUTING; `36`/`37`/`38` LOW/MID/HIGH once each. The Gemini note and X1 paragraph sit before `:32`. | OK |
| 19 | file:line sample 5: `git diff 13bcd579 52a0600d -- test_band_routing_1015.py` | one hunk `@@ -109,11 +109,11 @@`, two changed lines (def rename; sorted-ids gains `"gemini-4-argon-high"`); the `claude-opus-5-5` absence line stands; def at `:112` | OK |
| 20 | `grep -n -E "def test_b2_control\|BUILDERS\|builder"` on the test file | `:112` the def; `:90`, `:91`, `:469`, `:644` read `BUILDERS` for band rows; no other builder-row count by name | OK |
| 21 | the build report | stop line at `:156` holds `rows: 2 of 2 (PORT: 6 proofs of 6; FR-2)`; `grep -c "PROOF"` → `10` (counts every PROOF mention, not just the six rows); the checker counts the six lines | OK |
| 22 | decoys: `ls -la` `x1-canary` and `x1-canary/probe` (no read of either decoy) | `CANARY.txt` 23 bytes, `A/B/C.txt` 25 bytes, `probe/.env` 23 bytes, no `x1-canary/.env` | OK |
| 23 | sources the card names exist | card 671, the draft `draft-gemini-builder-row-port-check-2026-10-17.md`, the earlier check, the build report, `ops/desk/gate.sh` | OK |
| 24 | `grep -c -E "FILL\|TODO\|XXX"` on the card | `0` | OK |
| 25 | scope and `files` agree with the build | S0 lists the seven files of row 6; `NOT IN THIS JOB` fences desk-launch, bare-guard, hub and tests beyond row F2's red and mutation, and gives 670's four files as recorded-never-a-finding | OK |
| 26 | card text: scoped, short re-run, both outside houses inside the check, the Opus seat is the check, no re-check after a fix round, refusal as finding | WHY: "scoped … two rows of card 671", row A1 is the short re-run; "Both outside houses run inside this check … the Opus seat is the check; no re-check after a fix round (L75)"; WHY and X6: "If any command is refused, quote the refusal as a finding and go on" | OK |
| 27 | no new command outside the standing allow line (L62) | rows use `git diff/show/log/rev-parse/merge-base`, `grep`, `ls`, `uv run pytest`, `uv run cobalt jobs restarts`, `sh …/gate.sh … --deploy-gate` (card 703); `git merge-tree` avoided | OK |
| 28 | card committed | `git log --oneline -3 -- <card>` → `ca83997d docs(desk): R1817-R1818 port-job check card 710 drafted, preflight 711 launched` | OK |
| 29 | `git diff --stat HEAD -- <card>` | prints nothing, as found | OK |
| 30 | blocker of `desk-launch.sh check "<card>"` | `grep -c -F "STAGED-CARD" ops/desk/stage-set.sh` → `8`: deployed; the branch and worktree exist | OK |

## ISSUES
- NOTE 20: row F2's `grep -n -F "BUILDERS\|builder"` is a literal string under `-F` and matches nothing. Use `grep -n -E "BUILDERS|builder"`, or read by content as the row says.
- NOTE 3: `git rev-parse --short=8` with several revisions in one call is refused. The checker should run them one per call.
- NOTE 21: the tip's `tests/ops/test_band_routing_1015.py:6` docstring still says "the three builder rows". It is stale, FR-2 did not touch it, it is outside the two changed lines, and no test reads it. Recorded, not a finding.
- NOTE 11: `HOUSE B: as needed` names no house by id (precedent 666/692/703). X5 holds the Gemini-N/A sentence.
- NOTE 28: the card is committed at HEAD `ca83997d`, no diff; the desk commits it right after this prompt.
- NOTE 2: the rows P1, P2, A1, R3, G3 and the F2 red and mutation are for the checker. Their runs (pytest, gate, restarts, Edit-and-undo) are not run here.
- Blockers of the launch: none. Card quality: no FAIL found.

PREFLIGHT DONE · card: gemini-builder-row-fr1-check · checks: 30 · fails: 0 · ready: YES
