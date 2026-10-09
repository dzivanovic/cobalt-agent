# Guard D1 preflight r2 · card 162 · 2026-10-09

Main HEAD `eef792cf`. Nothing was run (no pytest, no mutation); every OK below is read from code (L70).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 0a | `grep -n "refuse" ops/desk/desk-launch.sh` (`:722-762`) | JOB `guard-d1-1009` is `[a-z0-9-]`; BRANCH `ops/guard-d1-1009` plain; WORKTREE `guard-d1-1009` in pattern; LADDER, BASE, RULINGS non-empty; RULINGS `2026-10-08 R686` is `<date> R<n>`; TAG absent; `## ROWS` present; card path `$PROMPTS/2026-10-09/162-guard-d1-card.md`, absolute; `DB: none` | OK |
| 0b | build `REPORT` rule `desk-launch.sh:901-904`; card line 7 | requires `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/*.md`; card line 7 is `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md`. Matches; `CARD.md:19` agrees | OK |
| 0c | `git -C … rev-parse HEAD`; `git -C … merge-base --is-ancestor 1458693d HEAD`; `git log -1 1458693d` | BASE is 8 hex, commit `1458693dbde5…` (2026-10-09 11:35 -0400), ancestor of HEAD `eef792cf` (exit 0). `git diff --stat 1458693d HEAD -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py src/cobalt/db_migrations/cli.py src/cobalt/db_query.py` prints nothing | OK |
| 0d | `grep -n "^\| R686 " reports/cto-2026-10-08.md`; `ops/authorize.sh:84-122` | `:39` one row: `HIS RULING (words R686, standing) … APPROVED · HIS RULING · APPLIED`. `HIS RULING` before `APPROVED`, one line (the `*"HIS RULING"*APPROVED*` test, `authorize.sh:98`) | OK |
| 0e | `git log -1 --format=%H -S"\| R686 \|" -- reports/cto-2026-10-08.md`; `git diff -U0` of that file | `4125ff02c9587ca901d9d5c418f378b8c77593a9`; working-tree diff touches only the `OWED:` line 93, so row `:39` equals HEAD | OK |
| 1 | `grep -n` and reads of `ops/desk/bare-guard.py` | `:20-21` header; `:57` `"G2"`; `:111` `PROD`; `:168` `i += 2` (scanner skips the char after `\`, card `:167-169`); `:254` `unquote_ansi_c`; `:288-293` `words`; `:773-784` `braces`; `:845` `w.replace("\n", "")`; `:891` `PROD_READ`; `:895-930` `prod_read`; `:935-938` `segs`; `:943` the G2 test, text as the card quotes it; `:928` already refuses `--allow-prod` inside `prod_read`. All cites hold | OK |
| 2 | reads of `tests/ops/test_bare_guard.py` | `:143` `G2_ROUTE`; `:223` `make_seat`; `:267-269`, `:272-274`; `:397-413`; `:446-450` `PROD_READS`; `:462`, `:465-470`; `:478-486`; `:489-512` `MARKED_DENIED` (`:502` is the `env COBALT_ENV=production` line); `:524-527`; `:530-540`; `:544` the python-literal continuation; `:548-590`; `:1164-1172`. All cites hold | OK |
| 3 | `grep -n -e "allow-prod" -e "PROD_DB_NAME" src/cobalt/db_migrations/cli.py`; `grep -n -e "--prod" -e "--side" src/cobalt/db_query.py` | `cli.py:836` `dbname = db.PROD_DB_NAME if args.allow_prod`, `:1078` `"--allow-prod"`; `db_query.py:211-212` `--side`, `--prod` | OK |
| 4 | five spellings plus `--allow-prod` | T1: `"…"`, `'…'`, `$'…'`, `prod''uction`, `env …`, second assignment, `{uction,uction}`, continuation, `--"prod"`, `--pr{od,od}`; T2: `--allow-prod` four ways | OK |
| 5 | `prod_read` stays the one pass | F1 leaves `prod_read`, `PROD`, `PROD_READ`, `ROUTE["G2"]` as they are; the `and not prod_read(command)` clause stays. I traced both new C1 lines through `prod_read` (`:904-930`): words equal `PROD_READ`, one `--prod`, no `--side` on the second → True; green on BASE and after | OK |
| 6 | "D1 builds after D2 deploys" | `NOT IN THIS JOB` first bullet and `## RECORDS` (first bullet) say so. `git log -3 -- ops/desk/bare-guard.py` head is `828f28dc` (no D2 commit); card `158` exists, D2 not deployed yet. BASE is pre-D2; the card says to re-prove each cite by symbol | OK |
| 7 | control rows C1, C2 | C2 (`COBALT_ENV=dev uv run pytest -q`, `db migrate`, `--rollback --down-to 0010`, `--products`, three `grep`s, `pytest -k prod`) and the deploy/`None` seats: none holds `COBALT_ENV=production`, `--prod`, `cobalt_brain` or a dash-led word with `prod` as a token (`allow.prod` has no leading dash; `-k` and `--products` fail `PROD_OPTION`). G1 sees no separator in any of them. C1 as check 5 | OK |
| 8 | each red fails on BASE for its stated reason | T1: raw string misses `COBALT_ENV=production` (quotes, `$'`, `''`, braces, `\`+newline break the literal), `--prod` (quote or brace splits it) and `cobalt_brain`, so `PROD.search(command)` is False; `scan()` finds no separator (a backslash skips its next char, `:167-169`); G1 passes → `(0, '')` at `:268`. T2: `--allow-prod` and `--allow-{prod,x}` fail `(?<![\w-])--prod` (single dash before `prod`) → `(0, '')`. Read, not run | OK |
| 9 | K1 mutations 1-7 | (1), (3), (4), (5), (6), (7) each name a clause of F1 and tests that must go red, and I traced them so. (2) does not: with `braces()` dropped, `prod_word` tests the unexpanded word, and `PROD_OPTION` (`^-.*(?<![a-z])prod(?![a-z])`) still matches `--allow-{prod,x}` (`prod` after `{`, before `,`). So T2 `--allow-{prod,x}` stays green under (2); the card says it fails | **FAIL** |
| 10 | every test offline | tests run the hook as a subprocess on a `tmp_path` seat; no network, no database; `NOT IN THIS JOB` forbids a typed production command | OK |
| 11 | no new command (R411, R412) | build runs `uv run pytest`, `git diff`, `uv run cobalt jobs restarts` (`grep -rl "jobs restarts" src/cobalt` → `jobs/config.py`); no new script | OK |
| 12 | RESTARTS class home per path (`## RECORDS`) | `ops/desk/bare-guard.py` operator script (`grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing, rerun now); `tests/ops/test_bare_guard.py` test; report DOCS; expected `RESTARTS: none` | OK |
| 13 | `git log -1 -- <card>`; `git diff HEAD --stat -- <card>` | last commit `9db1211c094f…`; diff against HEAD prints nothing; the card is not in `git status` | OK |
| 14 | `git -C … show 9db1211c --format= -U0 -- <card>` | one hunk `@@ -7 +7 @@`: `REPORT:` main path → `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md`. Nothing else changed in the card (`--stat`: card 1 line each way; the commit also touches card 164 and the amend report) | OK |
| 15 | `grep -rn "allow_abbrev" src` | prints nothing, as `## RECORDS` says | OK |

## ISSUES
- FAIL · check 9 · K1 mutation (2) predicts T2 `--allow-{prod,x}` fails; it will not, because `PROD_OPTION.search` matches the unexpanded word. Fix the card: drop `--allow-{prod,x}` from (2)'s list (it still fails under (4)), or change T2's case to `--allow-p{rod,x}`, where only the expansion holds `prod`. Recommit the card.
- NOTE · over-refusal beyond `## RECORDS`: `PROD_OPTION` runs on every word, so a quoted prose word that starts with `-` and holds `prod` as a token (`git commit -m "- fix prod notes"`, `echo "-- prod"`) is refused for a non-deploy seat. A card line naming it would do; not a block.
- NOTE · BASE `1458693d` is pre-D2 (D2 not deployed). The desk resets BASE to main HEAD after the D2 merge, which is a card recommit; the card already says to re-prove each cite by symbol.
- NOTE · the previous preflight's one FAIL (0b, `REPORT:` main path) is fixed by `9db1211c`.

PREFLIGHT DONE · card: guard-d1-1009 · checks: 20 · fails: 1 · ready: NO
