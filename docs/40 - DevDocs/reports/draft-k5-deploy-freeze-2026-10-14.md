# draft-k5-deploy-freeze — 2026-10-14

## §0 Headline
Card 546 written: `prompts/2026-10-14/546-deploy-freeze-card.md` (JOB `deploy-freeze-1014`, K5, R1471), 3 rows D1, F1, H1 plus R5.
D1 new `ops/desk/deploy-shipped.sh` (the one list of shipped paths); F1 `ops/desk/pre-commit` guard refuses only shipped paths until the report is committed, then all; H1 `DEPLOY-HUB.md:15` and D2.0 `:129`.
Every test is new in `tests/ops/test_deploy_freeze_1014.py`, pins by content, no BASE hash. No overlap with 521, 523, 537. Nothing was run.

## DECISIONS
- ASK DESK 1: where the guard gets the shipped paths. Default: the deploy card found by `JOB:` + `BASE: main`, heads from its `TIP:`, `git diff --name-only main...<head>`, plus `DEPLOY-HUB.md`; unreadable or ambiguous = freeze all. Alternative: a state file written by `desk-launch.sh` at launch (more code, a new file). [07:45 ET]
- ASK DESK 2: when the full freeze starts. Default: when the deploy's REPORT is committed on `main` (D2.0), because 4.3 `--ff-only` and `:140` need `main` unmoved from D2.0 to the merge. Before D2.0 only shipped paths are frozen. The re-verify sits at the start of D2.0 and `:114`, `:132`, `:140` stand. Alternative: a non-ff merge at 4.3, which changes the rollback string (`revert -m 2`); not drafted. [07:45 ET]
- ASK DESK 3: `desk-launch.sh:1727` (refusal text) and `:2232` (reminder "no desk commit on main until the stop line") now overstate the freeze. Default: not changed in this card (that file is not in its fence); a later wording card. [07:45 ET]
- ASK DESK 4: cards 542-545 are drafted in the same hour and their rows were not written when this was read. Default: this card claims `ops/desk/pre-commit:3-4,29-34`, `DEPLOY-HUB.md:15,129` and `ops/desk/deploy-shipped.sh`; the desk compares line ranges when it commits them. [07:45 ET]
- UNPROVEN (L70): the hook test relies on `git commit` running a copied hook with `COBALT_REPO_ROOT` and a stub `claude` on `PATH`; the shape is `test_desk_row.py:225-226` but nothing was executed here. The builder runs it red-first.

## RECORDS
- 2026-10-14 07:37 ET (`date`), `main` HEAD `0ffb6949` (`git rev-parse --short=8 HEAD`). `git diff --stat HEAD` over `ops/desk/pre-commit`, `desk-launch.sh`, `desk-commit.sh`, `deploy-card.sh`, `DEPLOY-HUB.md`, `tests/ops` printed nothing, so the reads by the file tools are HEAD's.
- Read: `prompts/CARD.md`; `2026-10-13/523-hub-text-card.md`, `516-sweep-pin-card.md`, `521-gate-tests-ops-card.md` (grep), `2026-10-14/537-deploy-smoke-string-card.md`; `ops/desk/pre-commit` whole; `desk-commit.sh` whole; `desk-launch.sh:495-535`, `:965-985` (grep hits `:1727`, `:2232`, `:541`); `deploy-card.sh:20-40`, `:580-603`; `DEPLOY-HUB.md:13-15`, `:108-116`, `:120-147`; `reports/cto-2026-10-14.md` rows R1471, R1472; `-words.md` R1471; `survey-blockers-2026-10-12.md` row 21 (the old KEEP); `reports/deploy-hub-text-1013.md` last 2500 bytes; `tests/ops/test_desk_row.py` whole.
- `grep -n "freeze"` in `survey-blockers-2026-10-12.md` and `DEPLOY-HUB.md` printed no hit: the rule is named there as "no desk commit while a deploy hub is live" (row 21) and `DEPLOY-HUB.md:15`.
- `ls -la .git/hooks/pre-commit` → symlink to `ops/desk/pre-commit`; `git config --get core.hooksPath` exit 1. `git ls-files` for `ops/desk/deploy-shipped.sh` and `tests/ops/test_deploy_freeze_1014.py`: nothing (new).
- One Bash call (`git show HEAD:… | sed`) was refused by the bare-command hook as a pipe; it was not retried as a pipe. No other refusal.

DRAFTED · decisions: 4
