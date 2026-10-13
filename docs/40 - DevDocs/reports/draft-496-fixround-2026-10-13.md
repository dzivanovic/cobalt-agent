# draft-496-fixround — report (2026-10-13)

## §0 Headline
Card 496's fix round is drafted: header `TIP: 6c3402af`, three rows after OW1 (FR-D1, FR-O2, FR-A4); no existing row touched.
Each row quotes its RED proof from the check report. FR-A4 is a PIN, green on the tip, with two named mutations that turn it red.
Edited one file: `docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md`. 3 decisions, each with a default.

## DECISIONS
1. ASK DESK: the shape also lives in text outside FR-O2's files: `ops/desk/deploy-step-c.sh:106` (the awk check, `[a-z0-9-]+` words), `DEPLOY-HUB.md:13` and `CARD.md:64` (`1–4 words`). Launch refuses first, so STEP-C never sees a non-`cobalt` dry run. Default: not edited in this round (L75: touched tests and the deploy gate only); the desk decides a follow-up. [15:10 ET]
2. ASK DESK: card 304's real dry run is `uv run prefill refresh --dry-run` (`prefill` is its own script, `pyproject.toml:69`). Under the new shape its `## LAUNCHD` line is refused. Default: its line says `dry run: none`, or the desk names a `cobalt …` command. FR-O2's tests use a constructed `cobalt prefill refresh`. [15:10 ET]
3. ASK DESK: the existing card text (row L1, row (j), THE SHAPE) still says `uv run <1–4 words>` and `prefill refresh`. The prompt says not to touch existing rows, so FR-O2 states it supersedes them. Default: left as is. [15:10 ET]

## RECORDS
Time 15:07 ET (`date`). Every `file:line` below was read at `6c3402af`; the worktree `cobalt-wt/plist-step-c-1013` has `git rev-parse --short=8 HEAD` → `6c3402af`, and its files were grepped there.
- `git -C /Users/cobalt/cobalt show 6c3402af:docs/40\ -\ DevDocs/prompts/STANDING-LIST.md`: `:157` holds `NOT ON THIS LIST, by design: retiring or installing a launchd job` (the Grep on the saved output returned `157:`).
- `git show 6c3402af:ops/desk/desk-launch.sh`: the deploy case dry-run `case` is `:1563-1578` (`:1565` the `uv run …--dry-run` pattern, `:1569-1570` the word check, `:1574` the 4-word cap, `:1577` the refuse text).
- `git show 6c3402af:tests/ops/test_desk_launch_launchd.py` plus Grep in the worktree: `DRY` at `:32`; refusal cases `:194-198`; `card_line` `:138-139`.
- `git show 6c3402af:src/cobalt/jobs/watchdog.py` plus Grep: `BootstrapOwedError` raised `:79`, `:81`; caught `:439`; `"not loaded"` finding `:448`.
- `git show 6c3402af:tests/cobalt/test_jobs.py`: `TestBootstrapOwed._sweep` `:948`, its tests `:988-1012`; `test_ow1_not_json_is_refused_loud` is absent (removed by the check); house A's text (`<S>/house-a.md:40-78`) raised, it is not restored as written.
- `src/cobalt/smoke/checks.py` in the worktree: `bootstrap_owed` imported `:433`, called `:435`; `evaluate`'s `except Exception` is `:733`.
- `pyproject.toml:66-69` in the worktree: `cobalt` and `prefill` are separate scripts.
- R1418: `grep -n "^| R1418 "` in `reports/cto-2026-10-13.md` → `:26`, `DESK RECORD, brain (L79)`, the fix round's direction (D1, O2, the not-JSON test, A4 kept).
- RESTARTS class homes, by grep of `src/cobalt/jobs/restarts.py` (unchanged since the tip, `git diff --stat 6c3402af` empty): `docs/` → `DOCS` `:225-228`; `ops/desk/` → `operator script; no Cobalt reader` `:232`; `tests/` → `test/documentation; no resident` `:246`. Changed paths: `STANDING-LIST.md` (docs), `ops/desk/desk-launch.sh` (ops/desk), `tests/ops/test_desk_launch_launchd.py`, `tests/cobalt/test_jobs.py` (tests): no resident restart. The card's earlier RECORDS cite `:230` for the operator-script class; the class line is `:232` (this round's rows use `:232`; the earlier line is not edited).
- Nothing run: no test, no mutation, no launch. The RED proofs are the check report's `## RUNS` lines for O2 and A6; FR-A4's green-on-tip is a claim from reading `watchdog.py:439-448`, to be run by the builder.
- No commit made (no git write in this seat).

DRAFTED · decisions: 3
