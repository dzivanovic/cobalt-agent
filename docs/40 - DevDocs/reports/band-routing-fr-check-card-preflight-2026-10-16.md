# Card 638 band-routing-1015-fr-check — preflight (2026-10-16, Sonnet 5.5, read-only)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header vs `CARD.md` (read of `638-…-card.md:1-15`) | JOB, LADDER, CLASS K5, INSTALL, BRANCH `ops/band-routing-1015`, WORKTREE, BASE `f2ca3e1a`, TIP `c8c5ca90`, REPORT (in worktree), CHECK REPORT (under reports/), HOUSE A `grok`, HOUSE B `as needed`, DB `none`, RESTARTS `none`, RULINGS `2026-10-15 R1532`; all required check fields present and valid. BASE and TIP are the desk's: `git log` shows `c8c5ca90` is the BUILT tip, head `3ac61a2f` | OK |
| 2 | `grep -c -F "«FILL"` on the card | `0` (no placeholder token) | OK |
| 3 | rows per FR-1..FR-5 (`grep -n -F -o`) | FR-1 `:24`, FR-2 `:25`, FR-3 `:26`, FR-4 `:27`, FR-5 `:28`; each a RUN with quoted output, a RED (restore `git show ee21824d:<file>`, undo, `git diff --stat c8c5ca90 -- <file>` empty) and a control; plus S0, H1, B*, D1, R3, T1, G1 | OK |
| 4 | O2/O4 closed: `grep -n -F -e xfail -e runxfail tests/ops/test_band_routing_1015.py` (worktree) | no hit. Tip test file has `test_o2_…` (no marker) plus `test_fr1_…`, `test_fr2_…`, `test_fr3_…`, `test_fr4_…`, `test_fr5_…` and their controls. H1 row runs the test without `--runxfail` | OK |
| 5 | B1-B6 re-run row | `B*` row names B1-B6 with one mutation per row where the first check ran one. Tip test file holds `test_b1_…` to `test_b6_…` and all controls | OK |
| 6 | builder DECISION is an ask | row D1 and ask X1 (`:53`); tip `test_o2_…` asserts `returncode == 1` and `"REFUSED: the card path holds '/./' or '//'" in done.stderr` (the changed assertion) | OK |
| 7 | houses and Opus seat named | HOUSE A `grok`; X7 "Both outside houses run here … The Opus check seat is the brain's condition 1". HOUSE B is `as needed`, so the second house is not named by id (as on 633) | OK (see ISSUES N2) |
| 8 | `grep -n -e "deploy-gate" -e "offline" ops/desk/gate.sh` | `:2` usage line has `[--deploy-gate]`; `:29` option text; `:136` `--deploy-gate) deploy_gate=1`; `:146-147` accepted for `offline`/`all` | OK |
| 9 | RULINGS rows: `grep -n -F R1532 reports/cto-2026-10-15.md` | `:102` `R1532 … HIS RULING · APPROVED` (routing B). Card RULINGS holds only `2026-10-15 R1532` | OK |
| 10 | G1 PASS-2 out of scope | `## NOT IN THIS JOB` `:40`: "never a finding, never a fix here"; H1 and `## RECORDS` repeat it | OK |
| 11 | sample `desk-launch.sh` on the tip (`git show ops/band-routing-1015:ops/desk/desk-launch.sh`) | `:996 *..*)`, `:997 */./*\|*//*) refuse "the card path holds '/./' or '//': $card"`, `:1643 BAND_FROM=20261016`, `:1652 band_row()` — all four match the card | OK |
| 12 | sample `CHECK-HUB.md:64`, `:117` (worktree = head, docs-only past the tip) | both read `on a shadow card or a routed card (BAND LOW or MID, dated on or after BAND_FROM), … is expected and recorded, not a finding` | OK |
| 13 | sample `CARD.md:23`, `:32` | `:23` BAND row, check cell `required when the build card carries BAND: LOW or MID (copied from it); optional otherwise`; `:32` the paragraph | OK |
| 14 | sample `SHADOW-HUB.md:28`, `:53`, `:70` | `:28` `BAND ROUTING (` with `its own fresh job card with BAND: HIGH` and `never on a 429 (R1532: Terra backup; 2026-10-14 item 7: …)`; `:53` `2. PREFLIGHT:` and `:70` `` `SHADOW BUILT · job: `` each end with the `(a routed card: no SHADOW OF; stop line BUILT · as :28)` note | OK |
| 15 | sample test lines: `git show` of the tip test file | `test_o2_…` carries `returncode == 1` then the path-refusal assert; `test_fr1_…` and `_control_…`, `test_fr2_…`, `FR2_CLAUSE`, `test_fr3_…`, `test_fr4_…`, `test_fr5_…` and `FR5_NOTE`, `test_fr3_control_…` present. Two line numbers are off, see ISSUES N1. 11 anchors matched in all (≥5) | OK |
| 16 | S0 scope: `git diff --name-only --no-renames ee21824d c8c5ca90` | exactly CARD.md, CHECK-HUB.md, SHADOW-HUB.md, `ops/desk/desk-launch.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py` | OK |
| 17 | `git diff --stat c8c5ca90 3ac61a2f -- . ':(exclude)docs'` | prints nothing (head adds docs only) | OK |
| 18 | `git diff --name-only --no-renames f2ca3e1a c8c5ca90` | 11 files: BUILD-HUB, CARD, CHECK-HUB, SHADOW-HUB, `bare-guard.py`, `desk-launch.sh`, `preflight.sh`, the two tests, two build-report files under docs; no `src/`, `configs/`, `.claude/` | OK |
| 19 | `git diff --stat ee21824d c8c5ca90 -- ops/desk/desk-launch.sh tests/ops` | `desk-launch.sh 1 +`; `test_band_routing_1015.py 97`; `test_check_hub_shadow.py 3 +-` (matches the card's "two insertions one deletion"); 3 files | OK |
| 20 | card committed: `git log --oneline -2 -- <card>` and `git diff --stat HEAD -- <card>` | `38ec27bf docs(desk): fix-round check card 638 drafted, preflight prompt 639`; diff against HEAD is empty. Other files of `main` are dirty (not the card) | OK |
| 21 | `ops/desk/desk-done.sh` read for X5 | file name from the card not found by `grep "BUILT ·"` (no hit). X5 tells the checker to read `ops/desk/desk-done*` by content, so the check does that itself | OK (see ISSUES N3) |

## ISSUES
- N1 NOTE: card row FR-1 gives `tests/ops/test_band_routing_1015.py:377-382` for `test_o2_…` and `:388`, `:397` for the FR-1 tests; I read the file by `git show` only (no line numbers printed) and matched by content, not by line. The check seat should confirm the lines with `grep -n` on the tip.
- N2 NOTE: `HOUSE B: as needed` and X7 name no second house by id; this is the 633 precedent and the desk's default, so not a fail.
- N3 NOTE: `desk-done.sh` has no `BUILT ·` literal; X5 must read `desk-done*`, `gate.sh`, `deploy-card.sh` and the check arm by content and may find the reader elsewhere.
- N4 NOTE: head `3ac61a2f` is `ops/band-routing-1015`; card TIP `c8c5ca90` is the BUILT tip (the desk may re-write it).
- Blocks the check launch: nothing. Desk steps owed: none beyond `desk-launch.sh check "<card>"`.

PREFLIGHT DONE · card: band-routing-1015-fr-check · checks: 21 · fails: 0 · ready: YES
