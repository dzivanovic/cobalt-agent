JOB: deploy-card-fixes-1018
LADDER: OFF-LADDER — reports/cto-2026-10-15.md HANDOVER PLAN (3) 2026-10-18 R1833
CLASS: K5
INSTALL: none
BRANCH: ops/deploy-card-fixes-1018
WORKTREE: deploy-card-fixes-1018
BASE: 279c99ce
TIP: cc4995b6
REPORT: /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-card-fixes-1018-check-2026-10-18.md
HOUSE B: as needed
BAND: LOW
DB: none
RESTARTS: none
RULINGS: 2026-10-18 R1833

## ROWS

Scope: one gap of `ops/desk/deploy-card.sh` (brain R1601; desk lesson 10-15, `reports/cto-2026-10-15.md` HANDOVER PLAN (3)). Nothing else in the script changes. Every `file:line` below was read with `git show main:ops/desk/deploy-card.sh` at the drafting (`## RECORDS`); re-read each by content before the edit (BUILD-HUB E3).

| row | what | red first | files |
|---|---|---|---|
| D1 | `deploy-card.sh` REFUSES a job whose code tip is already an ancestor of main. Today the per-job loop proves the tip is an ancestor of the branch head (`:550`, `git -C "$REPO" merge-base --is-ancestor "$ctip" "$head" \|\| refuse …`) and that the head adds nothing outside docs/ (`:551-552`), and never reads main: a branch already merged into main still gets a card (brain R1601). THE EDIT: ONE new line directly after `:552`, in the loop, `ctip` being the code tip (the fix tip on a fix round, `:542`): `git -C "$REPO" merge-base --is-ancestor "$ctip" refs/heads/main && refuse "$job: code tip $ctip is already an ancestor of main $(git -C "$REPO" rev-parse --short=8 refs/heads/main); nothing to deploy"`. The refusal names the job, the tip and main's short hash, and exits 1 with nothing written, as every `refuse`. The header comment (`:8-11`, the REFUSED list) gains the clause `the code tip is already an ancestor of main;` after `the code tip is not an ancestor of the head;`; keep the phrase `already an ancestor of main` on ONE line (a wrap inside it makes the DEPLOY PROOF marker read `1`, not `2`). No other line of the script changes | In `tests/ops/test_deploy_card.py`, NEW `test_d1_a_tip_already_on_main_is_refused`: from a `Desk` (`:47-120`), merge `ops/alpha` into the tmp `main` with `git merge --no-edit ops/alpha` (a merge commit, identity from `GIT_ENV`; not `--ff-only`, which fails because `Desk` commits on `main` after `ops/alpha` branched), commit nothing else, run the script on the `alpha` card alone; asserts exit 1, the output holds `alpha`, the alpha tip and `already an ancestor of main`, and `desk.out` does not exist. RED on `BASE`: exit 0 and the card written (`assert 1 == 0` reversed: `returncode == 0`). CONTROL (green after, red on `BASE` by the same test): the same run's stderr holds main's `rev-parse --short=8 main`. CONTROL 2 (green on `BASE` and after): the unmerged two-job run of the existing tests (`:1-300` of the file) stays green, so a tip not on main is still written. Quote whole: `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_card.py -k d1` → `1 failed` on `BASE`, `0 failed` after; then the whole file `0 failed` | `ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py` |

## NOT IN THIS JOB
- Any line of `ops/desk/deploy-card.sh` but the one new line of D1, its header-comment clause; no other refusal, no `held_rule`, no trial merge, no `--fix-report` rule changes.
- `ops/desk/deploy-smoke.sh`, `ops/desk/desk-launch.sh`, `prompts/DEPLOY-HUB.md`, `prompts/CARD.md`: untouched.
- `test_llm.py` BASE reds (a separate defect card, HANDOVER PLAN (3)).
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `ops/desk/deploy-card.sh` lines 1-31 (header comment), 454-577 (the per-job loop: `:457` JOB, `:520-521` `ctip` and `head`, `:541-542` fix round, `:550-552` the ancestor and docs-only refusals, `:566-576` DEPLOY PROOF), 585-608 (trial merge), 616-641 (the card text).
- `tests/ops/test_deploy_card.py` lines 1-120 (the `Desk` fixture), 210-222 (the DEPLOY PROOF fills-markers-and-smoke-reads test).
- `reports/cto-2026-10-15.md` HANDOVER PLAN (3) and its LESSONS.

## CHECK ASKS
- X1 Is D1's new line the only added line of `deploy-card.sh` besides the header-comment clause (`git diff <BASE> -- ops/desk/deploy-card.sh`), and does it read `ctip` after the fix-round reassignment at `:542`?
- X2 Does a branch not yet on main, with or without `--fix-report`, still write its card (the existing tests green, unedited)?

## DEPLOY PROOF
- `grep -c -F "already an ancestor of main" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `2`
- deploy-card tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_card.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- Drafter `draft-k5-deploy-card` (prompt 720), 2026-10-18 06:21 EDT from `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `279c99ce` (the BASE).
- `git -C /Users/cobalt/cobalt show main:ops/desk/deploy-card.sh` read whole: `:550` the head ancestor refusal, `:551-552` the docs-only refusal, `:457` the job card's JOB, `:566-576` DEPLOY PROOF to MARKERS and SMOKE READS, `:618` the deploy card's `JOB: $name`.
- `grep -c -F "already an ancestor of main"` after the edit is `2`: the header-comment clause and the refusal line. Both count; the desk re-reads it at the deploy.
- BAND LOW: two files (`ops/desk/`, `tests/ops/`), one new line and one new test, no migration (0-2).
- RESTARTS (K10): `ops/desk/` → "operator script; no Cobalt reader" (`src/cobalt/jobs/restarts.py:38`, `:232`); `tests/` → `:246`; derived from the code, the builder's `cobalt jobs restarts` line is the record.
- The tmp `Desk` fixture's `ops/alpha` branch is created off `main` and holds one code and one docs commit (`tests/ops/test_deploy_card.py:73-86`); `Desk` commits "checks and cards" on `main` after it branched (`:100-101`), so a merge commit (`git merge --no-edit ops/alpha`, not `--ff-only`) of it into `main` makes the code tip an ancestor of main.
