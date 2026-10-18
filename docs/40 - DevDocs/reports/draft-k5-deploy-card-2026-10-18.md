## §0 Headline
- Card written: `prompts/2026-10-18/721-deploy-card-fixes-card.md`, BASE `279c99ce`, BAND LOW, RULINGS `2026-10-18 R1833`.
- Row D1 (refuse a tip already on main) is complete and RED-first.
- Row D2 (smoke read job name) is `«FILL»`: the script holds no literal job name to replace. One decision.

## DECISIONS
1. ASK DESK: where does the smoke read take a literal job name? `deploy-card.sh` copies `## SMOKE READS` whole from each job card's `## DEPLOY PROOF` (`:566-576`); the deploy card's `JOB:` is the `--job` argument (`:618`, `:57`), never a job card's `JOB` (`:457`). The lesson (`cto-2026-10-15.md` HANDOVER PLAN) may mean the deploy card's `JOB` (should equal the build job's name) or a smoke read written by hand. [06:21 ET] Default: D2 is dropped and the card ships D1 only; the card still holds a `«FILL»` in D2, so the desk deletes that row (or names the seam) before the launch.

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `279c99ce` [06:21 EDT, `date`].
- `git -C /Users/cobalt/cobalt show main:ops/desk/deploy-card.sh`: read whole; `:550`, `:551-552`, `:457`, `:566-576`, `:618`.
- Read: `prompts/CARD.md`, `prompts/2026-10-16/671-gemini-builder-row-card.md`, `tests/ops/test_deploy_card.py:1-120`, `reports/cto-2026-10-15.md` HANDOVER PLAN, `topics/writing-rules.md`.
- Grep: `ops/desk/deploy-smoke.sh` and `DEPLOY-HUB.md` for a smoke read naming a job: none found.
- Nothing run, nothing committed.

DRAFTED · decisions: 0
