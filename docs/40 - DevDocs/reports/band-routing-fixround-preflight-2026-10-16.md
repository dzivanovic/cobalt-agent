# Card 583 band-routing-1015 — fix-round FR-1..FR-5 preflight (read-only) · 2026-10-16

Card: `prompts/2026-10-15/583-band-routing-card.md`. Direction: `reports/band-routing-check-decisions-2026-10-16.md`. Tip `ee21824d` (`git rev-parse ops/band-routing-1015` → `ee21824dab3f38805ce8b9739b20ba08f8882dd7`). Nothing was run but reads and greps; every RED is UNPROVEN until the builder quotes it (L70).

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -c -F` (7 key phrases: `a routed card: no`, `BUILT ·`, `R1532: Terra backup; 2026-10-14 item 7`, `its own fresh job card with`, `on a shadow card or a routed card`, `copied from the build card`, `/./`) on the direction | `6` lines hold them (rows 1-5 carry all seven) | OK |
| 2 | `grep -c -F` (FR-4 and FR-2 clauses, FR-5 clause, "FR row and a B row differ, the FR row wins") on the card | `4` lines: FR-1..FR-5 rows and `## FIX ROUND` carry the direction's words | OK |
| 3 | FR-1..FR-5 each: RED quoted whole on the tip, edit, control | FR-1 `--runxfail` → `1 failed`, `assert 0 == 1`; FR-2 `assert 0 == 2`; FR-3 `assert 'required' in ' optional '`; FR-4 phrase absent; FR-5 both counts 0. Each has a named control | OK |
| 4 | `files` cells and `## RECORDS` (`:106`) | FR-2 names `CHECK-HUB.md`, `test_check_hub_shadow.py`; FR-3 `CARD.md`; FR-4/FR-5 `SHADOW-HUB.md`; all name the test file; RESTARTS home "hub text, restart home = none" (K10), `RESTARTS: none` | OK |
| 5 | `grep -n "^## "` on the card | `## FIX ROUND` `:16`, `## ROWS` `:20`, `## NOT IN THIS JOB` `:54`, `## READ`, `## CHECK ASKS` `:75`, `## DEPLOY PROOF`, `## RECORDS`; `:18` says "Where an FR row and a B row differ, the FR row wins" | OK |
| 6 | `RULINGS` + `grep -E "DESK RECORD"` | `RULINGS: 2026-10-15 R1532` only (`:14`); no `DESK RECORD`; `:106` says the brain's check decisions are not a `HIS RULING` row | OK |
| 7 | ORDER / CHECK ASKS / WHY carry all five rows | `WHY` (`:22`) names O2, O4, O1, O3/G3, G2; `FIX ROUND ORDER` (`:52`) names FR-1..FR-5; `CHECK ASKS` X8..X12 (`:83-87`) | OK |
| 8 | `## NOT IN THIS JOB` (`:54-64`) | `:60` bars G1 (PASS-2); `:56` admits `CHECK-HUB.md` `:64`/`:117`; `:57` admits FR-1's one arm; `:58` admits FR-5's two clauses; `:61` matches FR-4. Nothing FR-1..FR-5 needs is barred | OK |
| 9 | the four drafter decisions vs the direction | 1 `L6_LINE` only (`test_check_hub_shadow.py:27`, the equality at `:75`) matches row 2; 2 "FR beats B" matches row 4 (`reports` says the direction wins); 3 `0` then `2` is the right count (two lines change); 4 the FR-1 wording and `//` test are the drafter's addition within row 1 ("`/./` or `//`, the error names the path") | OK |
| 10 | `git show ops/band-routing-1015:ops/desk/desk-launch.sh` — FR-1 anchors | `*[!A-Za-z0-9\ ._/-]*)` `:995`, `*..*) refuse "the card path holds '..'"` `:996` (one `case`, `:991` the `-card.md` arm; card says `:994-997`); `PROMPTS=` `:219`; `BAND_FROM=20261016` `:1642`, `band=$(field BAND)` `:1643`, day read `:1648` (card `:1635-1649`) | OK |
| 11 | same file — FR-3 anchors | `routed_tree=""` `:1790`, `1LOW\|1MID) routed_tree=1` `:1792`, dirt test `:1814` (card `:1788-1793`, `:1812-1815`); `preflight.sh` `:158-169` (card `:158-167`) | OK |
| 12 | `git show ops/band-routing-1015:…/CHECK-HUB.md` — FR-2 anchors | `grep -n` → exactly two lines, `:64` and `:117`, both `…on a shadow card, ?? SHADOW-INSTRUCTIONS.md … is expected and recorded, not a finding.` | OK |
| 13 | `git show ops/band-routing-1015:…/CARD.md` — FR-3 anchor; and the `SHADOW-HUB.md` — FR-4/FR-5 anchors | the `BAND` row's third cell is `optional` (the line after `DB`, before `RULINGS`); `BAND ROUTING (` paragraph holds `the fix round goes to the same builder, the backup is` and `never on a 429):`; `2. PREFLIGHT:` ends `…exceptions are read here.`; `SHADOW BUILT · job:` line starts with the backtick | OK |
| 14 | `grep -n` of the test file on the worktree (clean, on the tip) | `@pytest.mark.xfail(strict=True, …)` `:379`, its comment `:378`, `def test_o2_…` `:380` (card `:377-379` for comments plus decorator) | OK |
| 15 | `grep -rn -F` of "same builder", "never on a 429", "is expected and recorded", "2. PREFLIGHT:" over `tests/ops` | only `test_check_hub_shadow.py:29` (FR-2, the one constant); no test pins the `:28` clauses or the `:53` line; `SHADOW BUILT · job:` hits are test fixtures or `test_check_hub_shadow.py:88` (a substring, stays) | OK |
| 16 | placeholder scan (`«FILL`, `TODO`, `XXX`) in the card | none; the only `<tip>`/`<BASE>`/`<those nine files>` are the desk's `BASE`/`TIP` and prose | OK |
| 17 | `git diff --stat HEAD -- <card>`; `git log -2 -- <card>`; `rev-parse --short=8 HEAD` | diff empty (as found); the card is in `1fd1c499` (HEAD) and `8523214c`; the worktree `git status --short --branch` → `## ops/band-routing-1015`, clean | OK |
| 18 | `desk-launch.sh build "<card>" "FIX ROUND row FR-1"` blockers, by `grep` of the launcher | none found: the step holds only `[A-Za-z0-9 .-]` (`:2300`); the card is dated 2026-10-15 so BAND is not required (`BAND_FROM` `20261016`); the resume skips `worktree add` (`:2338`) and runs `lock_free` (`:1711`) | OK |

## ISSUES
- NOTE 1: no RED, control or test was run (read-only seat); each stays UNPROVEN until the builder quotes it on the tip.
- NOTE 2: `lock_free` (`:1711`) refuses the resume while another worktree's `.env` or the DB lock stands. The desk reads that at launch; I did not.
- NOTE 3: after FR-4 the `:28` sentence reads `…; a routed card's fix round is its own fresh job card with BAND: HIGH (brain 2026-10-16 note 7), the backup is the desk's hand launch…`: a comma splice, but it is the direction's wording.
- NOTE 4: the built B2 and B3 row text still says "the fix round goes to the same builder / its own original builder model". `## FIX ROUND` (`:18`) names the supersession, so the builder keeps those rows as written.
- NOTE 5: I could not run the installed `~/.claude/ops/desk-launch.sh`; the proofs read the tip's copy.

PREFLIGHT DONE · card: band-routing-1015-fixround · checks: 18 · fails: 0 · ready: YES
