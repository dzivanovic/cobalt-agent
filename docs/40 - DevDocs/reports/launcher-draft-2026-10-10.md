## §0 Headline
- Card `prompts/2026-10-10/244-launcher-card.md` written: row A builds `deploy-card.sh --fix-report` with RED tests; rows B and C are diagnose-first.
- The accepted-list of D0 is `DEPLOY-HUB.md:113` prose; no `ops/desk/` script reads it, so B and C are UNKNOWN as script edits.
- RESTARTS: none. `BASE` is a `«FILL»` for the desk.

## CHANGES
- Wrote `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md` (header per the prompt; `DB:` omitted; `## ROWS` A B C, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS` X1-X4, `## RECORDS`).
- Wrote this report. Nothing else touched.

## DECISIONS
1. A1 (default taken): option form `--fix-report "<job>=<path>"`, repeatable; the row's code tip becomes the fix report's `BUILT ·` `tip:`, the check's tip must be its ancestor (the `desk-launch.sh:856-869` rule), the literals still come from the CHECK report.
2. A2 (default taken): the fix report is read at the branch head (`git show <head>:<rel>`), as `desk-launch.sh:862`, never from main.
3. B1: UNKNOWN. The "accept-list of held items named fixed" is in no `ops/desk/` script (grep `named fixed|accept` hits only `house-probe.sh`, `bare-guard.py:1086`, `install-fixed.sh:8`, `desk-launch.sh:105`). Row B is RUN, diagnose-first (L70); an edit only if the builder finds the list in `ops/desk/`.
4. C1: UNKNOWN as a script edit. D0's ACCEPTED list is `DEPLOY-HUB.md:113`, a fixed file; `deploy-step0.sh:515-518` records `git status` and never gates. Row C is RUN; the one-line `?? .claude/settings.json.bak` addition is the desk's `install-fixed.sh` job, fenced out of this card.

## RECORDS
- `date`: Sat Oct 10 08:06 EDT 2026.
- `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- ops/desk tests/ops src/cobalt/jobs/restarts.py` printed nothing: every file read is identical to `d0a5fbb8` (read in the working tree, equal by that diff). `DEPLOY-HUB.md` and `CARD.md` differ by 4 lines docs-only since `d0a5fbb8` (the diff on `DEPLOY-HUB.md`); I read them on HEAD.
- Read at `d0a5fbb8` (by the diff): `ops/desk/deploy-card.sh` whole (`:55` unknown option refused, `:106-164` per-card read, `:138` check tip, `:143-144` docs-only rule, `:147` empty last cell, `:199-222` card text); `ops/desk/desk-launch.sh:804-884` (`frep` `:820`, `fixed_ok` `:856-869`); `ops/desk/deploy-step0.sh:1-120`, `:480-527` (`main status` `:515-518`, recorded only); `ops/desk/preflight.sh:1-140`; `tests/ops/test_deploy_card.py:20-210` and its `def test_` list; `tests/ops/test_deploy_step0.py:546-606` (names only); `src/cobalt/jobs/restarts.py` whole (`:38`, `:230-232`, `:240-243`, `:245-246`).
- Rows quoted from the reports: `cto-2026-10-09.md` R810 ("156 deploys on the fix-round SHIPS row (CARD.md :48, K3 precedent), card by a drafter; follow-up row `deploy-card.sh --fix-report` goes to the launcher card"); `cto-2026-10-10.md` R828 ("`.bak` stays his; D0 list row on the launcher card"); `cto-2026-10-10.md` R824 (the `.bak` left, decisions 1).
- `areas/cobalt.md` NOW OPS line: "a launcher card is owed: `deploy-card.sh --fix-report`, D0 accepts `.claude/settings.json.bak`".
- `DEPLOY-HUB.md:113` STEP-D0 MAIN, read on HEAD: ACCEPTED ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`.
- Not run: the `git show d0a5fbb8:<path>` form for each file (each would print a whole file); the diff above proves identity instead.

LAUNCHER CARD DRAFTED · decisions: 4
