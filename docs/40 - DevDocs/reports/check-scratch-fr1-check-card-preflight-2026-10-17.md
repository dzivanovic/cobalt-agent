# Card 690 check-scratch-fr1-check — preflight (2026-10-17, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read of `690-…-card.md:1-16` | JOB `check-scratch-fr1`, LADDER OFF-LADDER, CLASS K5, INSTALL none, BRANCH `ops/check-scratch-fr1`, WORKTREE `check-scratch-fr1`, BASE `79f6f2f3`, TIP `b093f192`, REPORT (in worktree), CHECK REPORT, HOUSE A `grok`, HOUSE B `as needed`, BAND MID, DB none, RESTARTS none, RULINGS `2026-10-12 R1138`, `2026-10-15 R1532`. JOB, LADDER, BASE, BAND, RESTARTS, RULINGS equal build card 681's header | OK |
| 2 | `git rev-parse --short=8 b093f192` and `79f6f2f3` | `b093f192`, `79f6f2f3`; `git log --oneline -5 ops/check-scratch-fr1`: `5f42c4f3` (report), `b093f192` (fix), `0d52929f` (red), `79f6f2f3`, `caebf457` — TIP is the code commit, BASE is under it | OK |
| 3 | `git diff --stat b093f192 5f42c4f3 -- . ":(exclude)docs"` | prints nothing | OK |
| 4 | `git diff --name-only --no-renames 79f6f2f3 5f42c4f3` | the build report and its `.result` under `docs/`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` — as row S0 says | OK |
| 5 | `ls` of CHECK REPORT `reports/check-scratch-fr1-check-2026-10-17.md` | `No such file or directory` (a new path) | OK |
| 6 | HOUSE A / HOUSE B | `HOUSE A: grok`; `HOUSE B: as needed`; X9 holds the brain's 2026-10-17 note (Gemini the only candidate → N/A is a harness record) | OK |
| 7 | RESTARTS vs touched paths | `RESTARTS: none`; touched paths `ops/desk/`, `tests/`, `docs/` only; row R2 runs `uv run cobalt jobs restarts 79f6f2f3..b093f192` and compares | OK |
| 8 | `git diff --stat 79f6f2f3 b093f192` | `ops/desk/stage-set.sh \| 70 +++++++++++++--------`, `tests/ops/test_stage_set.py \| 147 …`, `2 files changed, 183 insertions(+), 34 deletions(-)` — equals row S0 and RECORDS | OK |
| 9 | `git diff --stat 79f6f2f3 5f42c4f3 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` | prints nothing | OK |
| 10 | `git -C /Users/cobalt/cobalt-wt/check-scratch-fr1 status --short --branch` | `## ops/check-scratch-fr1` (clean) | OK |
| 11 | `git diff 79f6f2f3 b093f192 -- ops/desk/stage-set.sh` | four hunks only: header comment (`:7-8`), first `find` of `clearable()` (`:98`, `! -name STAGED-CARD`), prior-card block (`:108-154`), marker line (`:242`) — as S0 says | OK |
| 12 | scope vs card 583: `git diff --stat f2ca3e1a ops/band-routing-1015 -- ops tests src configs` | `bare-guard.py 5`, `desk-launch.sh 80`, `desk-watch.sh 9`, `preflight.sh 26`, `test_band_routing_1015.py 904`, `test_check_hub_shadow.py 3`, `6 files changed, 1015 insertions(+), 12 deletions(-)`; neither `stage-set.sh` nor `test_stage_set.py` is in it — row F1's expected result | OK |
| 13 | `grep -rn -F "stage-set"` over `ops/desk/desk-launch.sh`, `desk-watch.sh`, `preflight.sh` (main copies; the 583 branch copies read whole by `git show`) | no hit in any; desk-watch.sh and preflight.sh on `ops/band-routing-1015` read whole, no `stage-set` or `STAGED-CARD` | OK |
| 14 | no new command outside the standing allow line (L62) | commands: `git show/diff/log/status`, `grep`, `wc`, `uv run pytest`, `uv run cobalt jobs restarts`, `sh /Users/cobalt/cobalt/ops/desk/gate.sh …`, Edit under `cobalt-wt/**` for mutations. `git merge-tree` is not used (F1 names `ASK DESK`); G1's `log:` path is an `ASK DESK 2` | OK |
| 15 | the card tells the checker to quote any refusal as a finding: `grep -n -i "refus"` of the card | `:20` "If a command is refused, quote the refusal as a finding."; `:24` "name any hunk outside"; F1 `:32` `ASK DESK` for `git merge-tree` | OK |
| 16 | file:line `stage-set.sh` on the tip: `grep -n -F "STAGED-CARD"` | `:7`, `:8`, `:98`, `:109`, `:113`, `:116`, `:118`, `:242` — equals the card's H1 list | OK |
| 17 | file:line `stage-set.sh`: `grep -n` of `rm -r`, `clearable`, `copied=`, `sort -t`, `no prior card copy`, `fail()` | `rm -rf "$dest"` `:194`; `rm -rf -- "$dest"` `:201`; `clearable` `:90` (comment), `:92` (definition), `:173` (call); `copied=""` `:108`; `copied="$dest/files/$m"` `:121`; `sort -t "$tab" -k1,1n -k2,2 \| tail -n 1 \| cut -f2-` `:147`; `miss="no prior card copy: $dest/files/$m"` `:120`, `…/*-card.md` `:152`; `fail()` `:192`; `hash-object` `:155`; `--find-object` `:156` — all as the card says | OK |
| 18 | file:line: the legacy and tail lines | `head=$(sed '/^$/q' "$f")` `:132`; `mine="$mine${n:-0}$tab$f` `:137`; `others=` `:140`; JOB test `:158`; `prior=$(field "CHECK REPORT" "$copied")` `:159`; `cat-file -e "main:…"` `:165` — as the card says | OK |
| 19 | `grep -c -F "more than one prior card copy"` on the worktree's `stage-set.sh` | `0` (BASE holds it once, by the diff's removed line) | OK |
| 20 | file:line `tests/ops/test_stage_set.py` on the worktree: `grep -n -E "^def test_(mk1\|mk2\|cs1\|fr1)…"` | `test_mk1_…` `:531`, `:540`; `test_mk2_…` `:574`, `:597`, `:612`, `:637`, `:651`; `test_cs1_…` `:359`, `:420`, `:424`, `:428`, `:432`, `:436`, `:509`; `test_fr1_…` `:465`, `:480`; `_two_card_copies` `:375`; `_copy_no_prompts_card` `:384`; `same_job_check_card` `:556`; `commit_report` `:567`; `test_c10_` `:301`, `test_c11_` `:318`, `test_c12_` `:330`; `test_c2_c9_…` `:288` — equals the card | OK |
| 21 | the marker lines in the tests: `grep -n "STAGED-CARD"` | `:394` (after the `x-card.md` write at `:393`), `:519` (after the `write_bytes` at `:518`), appended uses from `:535` — as X6 says | OK |
| 22 | `_two_card_copies` use | defined at `:375`, no `_two_card_copies(` call in the `def test_` list above (the two tests that used it are deleted) — the card's H1 asks "finding or note": it is a NOTE (N1) | OK |
| 23 | `git show ops/check-scratch-fr1:ops/desk/stage-set.sh` read whole | the marker write `:242` follows the two `copy` lines and precedes the `files/wt` loop; `fail "STAGED-CARD write failed"` (card DEPLOY PROOF greps it, 1 hit) | OK |
| 24 | the card is committed: `git log --oneline -3 -- <card>` | `573e96fd docs(desk): check cards 690 and 692 drafted, preflight prompts 694 and 695 (R1780)` | OK |
| 25 | `git diff --stat HEAD -- <card>` | prints nothing (empty), as found | OK |
| 26 | READ files exist | build card 681, check cards 641/648/677 under `prompts/2026-10-16/`, the decisions report `check-662-and-583-fr2-decisions-2026-10-17.md` named by the card; the build report is in the worktree (git: `5f42c4f3`) | OK |
| 27 | what blocks `desk-launch.sh check "<card>"` | nothing found read-side: card committed and clean, TIP = code commit, head above it docs only (preflight.sh's `head` rule), CHECK REPORT new, worktree clean, branch exists. `preflight.sh check` and `authorize.sh` are the check seat's own first calls; I could not run them (no `sh` on my allow line) | OK (N2) |

## ISSUES
- N1 NOTE: `_two_card_copies` (`tests/ops/test_stage_set.py:375`) is unused after the two retirements; dead helper in a file the build card fenced to four edits. A note, as the draft chose; not a fail.
- N2 NOTE: G1's `gate.sh … --deploy-gate` and its `log:` path are owed to the desk (`ASK DESK 2` in the card); I did not run it. F1's `git merge-tree` is `ASK DESK`, by design.
- N3 NOTE: `HOUSE B: as needed` names no house id (precedent 633/638/666/677). X9 carries the Gemini N/A note.
- N4 NOTE: `.claude/settings.json` and `.claude/settings.json.bak` are dirty/untracked on `main`; the card names them under NOT IN THIS JOB and the branch diff holds no `.claude/` path.
- Blocks the check launch: nothing. Desk step: `sh /Users/cobalt/.claude/ops/desk-launch.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/690-check-scratch-fr1-check-card.md"`.

PREFLIGHT DONE · card: check-scratch-fr1-check · checks: 27 · fails: 0 · ready: YES
