# Draft — hub-deferred-1018 (prompt 786)

## §0 Headline
- Card written: `prompts/2026-10-18/787-hub-deferred-card.md`, BASE `170e90ca`, BAND HIGH, two rows (D1 the set check minus `<deferred set>`; D2 no `launchctl` call names it, plus smoke (f)).
- Five hub lines change: `DEPLOY-HUB.md:5`, `:89`, `:93`, `:94`, `:154`; one new test file `tests/ops/test_hub_deferred_1018.py` (3 red, 2 control on BASE).
- The hub calls neither `deploy-step0.sh` nor `deploy-outage.sh`; card 784's scripts are untouched.
- Not committed.

## DECISIONS
1. ASK DESK: smoke (f) is in scope [16:34]. Row 2 names only `launchctl` calls, but `DEPLOY-HUB.md:154` compares the tool's `RESTARTS:` after the merge to `<restart set>`: with cos listed again, F20's smoke (f) goes RED and STEP-5 runs. Default: D2 (b) subtracts `<deferred set>` there too (one line; STEP-5 (4) inherits it).
2. ASK DESK: the scripts the hub calls [16:34]. The prompt names `deploy-step0.sh` and `deploy-outage.sh` as the hub's; `git show main:…/DEPLOY-HUB.md` names neither (STEP-0 and STEP-4 are typed by the hub). Default: no script row; card 784 stays separate.
3. ASK DESK: the resume [16:35]. THE ONE RESUME (`:53`) does not re-run STEP-C, so `<deferred set>` would be lost. Default: D1 (c) writes it under `## RESTARTS`, and D2 (b) reads it from there; `:53` is not edited (check ask X3).

## RECORDS
- 16:33 `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `170e90ca`.
- 16:33 read `areas/cobalt.md` from `## What Cobalt is` and from `## Build rules` down; `prompts/CARD.md`; precedent `prompts/2026-10-18/784-cos-outage-card.md`.
- 16:33 `git -C /Users/cobalt/cobalt show "main:docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, read whole (188 lines); grep of it: `deferred` on `:5`, `:13`, `:89` only; `deploy-outage`, `deploy-step0`, `com.cobalt.cos` absent.
- 16:34 grep `ops/desk/deploy-step-c.sh`: `:285-286` prints `ADMITTED: %s · add · deferred`.
- 16:34 grep `prompts/2026-10-18/730-f20-card.md`: `:13` RESTARTS agent aset cos radar, `:14` `BOOTSTRAP: deferred com.cobalt.cos`, `:94` D8.
- 16:34 read `tests/ops/test_hub_text_1013.py` (the precedent form); `tests/ops/test_hub_lines.py:95-172`; grep `tests/ops/test_deploy_step_c.py` (hub asserts `:298-330`), `tests/ops/test_deploy_freeze_1014.py` (`:317-346`); no test or script holds the five changed lines' texts.
- 16:34 grep `reports/draft-cos-outage-2026-10-18.md` DECISION 1; `reports/f20-fix-preflight-2026-10-18.md:38` note 5.
- The prompt's `prompts/DEPLOY-HUB.md` is `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`.

DRAFTED · decisions: 3
