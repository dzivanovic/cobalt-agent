# launcher-fixround-amend4 — card 21, rows F2-F4 (2026-10-05)

## §0 Headline
- Card `prompts/2026-10-02/21-launcher-checks-card.md` gained rows F2 (P2 in `deploy-step0.sh` + O1 test), F3 (`DEPLOY-HUB.md:58`), F4 (`CARD.md:47`) for the check's O1 and O4.
- Fence and `## NOT IN THIS JOB` widened; the header line and the gate sentence name the new rows. Nothing else touched.
- Not committed (L36). decisions: 1 (the rule's "literals" wording, below).

## CARD
- Line 16: adds the FIX ROUND sentence (the build builds F2, F3, F4 after F1; no re-check).
- New rows F2, F3, F4 after F1 (columns: row · what · red first · files). Each carries the rule text as given.
- F2 files: `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py`. F3: `DEPLOY-HUB.md` line 58 only, merge `main` first (card 26 changes line 57). F4: `CARD.md` lines 44-45 and 47.
- Line 30 (gate sentence): adds `tests/ops/test_deploy_step0.py` → `0 failed`, `0 xfailed`.
- `## NOT IN THIS JOB`: F2-F4 change list added; hub-file exclusion exempts `DEPLOY-HUB.md` line 58; `CARD.md` fence is lines 44-45 plus 47.

## DECISIONS
1. The rule says the literals and `tip: <code tip>` are read from the fix report's `BUILT ·` line. A BUILT line carries no `held unfixed: 0` / `ready: YES` (the build report's last line and the O1 test's fix report have none), and F1's launcher reads only `BUILT ·` and `tip:` there. I copied the rule as written into F2-F4. The builder reads the literals from the check's line and `tip: <code tip>` from the BUILT line unless the desk rules otherwise.

## RECORDS
- Read: card 21 whole; `reports/launcher-checks-check-2026-10-05.md` whole; `git -C /Users/cobalt/cobalt show main:ops/desk/deploy-step0.sh` (tip `bd658cd8`): literals line 337, P2 block 358-387, refusal line 382; `git -C /Users/cobalt/cobalt show ops/launcher-fixround-1005:tests/ops/test_deploy_step0.py`: the strict-xfail O1 test last in the file, assertion `"is not the row's code tip" not in last_line(done)`.
- Read: `DEPLOY-HUB.md` lines 54-60 (line 58 = P2, `main` now); `CARD.md` lines 38-51 (line 44-45 header, line 47 the sentence).
- Red-first greps at BASE: `is an ancestor of the code tip` in `DEPLOY-HUB.md` and `CARD.md` → 0 matches in both.
- `git diff --stat main` on `deploy-step0.sh`, `DEPLOY-HUB.md`, `CARD.md` → empty (working tree = `main` for them).
- L74: no instruction block in any tool result. The harness attribution reminder (commit lines) is not acted on: no git write.

LAUNCHER FIXROUND AMENDED 4 · decisions: 1
