# Guard D1 preflight r3 · card 162 · 2026-10-09

Main HEAD `ca320542`. Read-only: nothing was run (no pytest, no mutation); every OK is read from code (L70).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header vs `ops/desk/desk-launch.sh` build mode (`:722-762`, `:895-904`) | JOB `guard-d1-1009` is `[a-z0-9-]`; BRANCH `ops/guard-d1-1009` plain; WORKTREE `guard-d1-1009` in pattern; LADDER, BASE, RULINGS non-empty; RULINGS `2026-10-08 R686` is `<date> R<n>`; TAG absent; `## ROWS` present; `DB: none` | OK |
| 2 | build REPORT rule `desk-launch.sh:901-904`; card line 7 | needs `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/*.md`; card line 7 is `…/guard-d1-build-2026-10-09.md` | OK |
| 3 | `grep -n "R686" reports/cto-2026-10-08.md`; `ops/desk/authorize.sh:98` | one row `:39`: `HIS RULING (words R686, standing) … APPROVED · HIS RULING · APPLIED`; `HIS RULING` before `APPROVED`, one line (`*"HIS RULING"*APPROVED*`) | OK |
| 4 | `git log -1 --format=%H -S"\| R686 \|" -- reports/cto-2026-10-08.md` | `4125ff02c958…` (committed) | OK |
| 5 | `git log -1 1458693d`; `git merge-base --is-ancestor 1458693d HEAD`; `git diff --stat 1458693d HEAD -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py src/cobalt/db_migrations/cli.py src/cobalt/db_query.py` | BASE is 8 hex, real main commit `1458693dbde5…` (2026-10-09 11:35 -0400); ancestor of HEAD (exit 0); diff prints nothing, so every cite below is HEAD's | OK |
| 6 | reads of `ops/desk/bare-guard.py` | `:20-21` header; `:57` `"G2"`; `:111` `PROD`; `:168` backslash `i += 2`; `:254` `unquote_ansi_c`; `:288-293` `words`; `:773-784` `braces`; `:845` `w.replace("\n", "")`; `:891` `PROD_READ`; `:895-930` `prod_read`; `:935-938` `segs` (+ unwrapped); `:943` G2 test, text as the card quotes. `PROD_OPTION`, `prod_word` absent (grep prints nothing) | OK |
| 7 | reads of `tests/ops/test_bare_guard.py` | `:143` `G2_ROUTE`; `:223` `make_seat`; `:267-269`, `:272-274`; `:397-413`; `:446-450` `PROD_READS`; `:462`, `:465-470`; `:478-486`; `:489-512` `MARKED_DENIED` (`:502` `env COBALT_ENV=production`); `:524-527`; `:532-538`; `:544`; `:548-590`; `:1164-1172` | OK |
| 8 | `cli.py:836,1078`; `db_query.py:207-216` | `:836` `dbname = db.PROD_DB_NAME if args.allow_prod`; `:1078` `"--allow-prod"`; `db_query.py:211-212` `--side`, `--prod` | OK |
| 9 | the five spellings plus `--allow-prod` | T1: `"…"`, `'…'`, `$'…'`, `prod''uction`, `env …`, second assignment, `env …{uction,uction}`, continuation, `--"prod"`, `--pr{od,od}`; T2: `--allow-prod` four ways. `words()` strips quotes and decodes `$'…'` (`:254-293`); shlex keeps `\<nl>` as `\n` in the word, so `.replace("\n","")` yields `COBALT_ENV=production` (same as `g3_bash:845`) | OK |
| 10 | `prod_read` the one pass | F1 leaves `prod_read`, `PROD`, `PROD_READ`, `ROUTE["G2"]` and `and not prod_read(command)` alone. Both new C1 lines trace through `:904-930` to True (words equal `PROD_READ`, one `--prod`; `prod_read` asks no `--side` for the second) | OK |
| 11 | "D1 builds after D2 deploys" | `NOT IN THIS JOB` bullet 1 and `## RECORDS` bullet 1 say so; `git log -1 -- ops/desk/bare-guard.py` is `828f28dc` (no D2 commit) | OK (see NOTE 1) |
| 12 | control rows C1, C2 | no C2 line holds `COBALT_ENV=production`, `--prod`, `cobalt_brain` or a dash-led word with `prod` as a token (`allow.prod` has no dash; `-k`, `--products`, `-rn`, `-q` fail `PROD_OPTION`); G1 sees no separator. Deploy / `None` seats skip G2 (`kind != "deploy"`, `kind is not None`). `grep` of the test file: the only dash word holding `prod` as a substring on an allowed command is `--products` (`:410`) | OK |
| 13 | each red fails on BASE for its stated reason | T1: raw string misses `COBALT_ENV=production` (quotes, `$'`, `''`, braces, `\`+nl break the literal), `--prod`, `cobalt_brain`; `scan` finds no separator (`:167-169`); G1 passes → `(0, '')` at `:268`. T2: `(?<![\w-])--prod` needs two dashes before `prod`; `--allow-prod`, `--allow-{prod,x}` fail it → `(0, '')` | OK |
| 14 | K1 (1) drop `or any(prod_word…)` | back to BASE test → every T1, T2 case `(0, '')`; existing tests stay green | OK |
| 15 | K1 (2) drop `braces()` in `prod_word`, proved against `PROD_OPTION = ^-.*(?<![a-z])prod(?![a-z])` | `env COBALT_ENV=prod{uction,uction}`: unexpanded word has no leading `-`, `PROD` misses → fails. `--pr{od,od}`: no `prod` substring → both regexes miss → fails. T2 `--allow-{prod,x}`: `-` then `prod` between `{` and `,` → `PROD_OPTION` matches the unexpanded word → green. The card now says exactly this (the r2 FAIL is fixed) | OK |
| 16 | K1 (3) drop the `"\n"` join | `COBALT_ENV=product\nion` matches neither regex → the T1 continued case fails; no other case holds a newline | OK |
| 17 | K1 (4) drop the `PROD_OPTION` clause | `--allow-prod`, `--allow-prod --rollback …`, `nice … --allow-prod`, `--allow-{prod,x}` (expands to `--allow-prod`): `PROD` misses all → every T2 case fails. T1 `--"prod"` and `--pr{od,od}` reach `--prod`, `PROD` matches → stay green | OK |
| 18 | K1 (5) `PROD_OPTION` as `startswith("-") and "prod" in lower()` | `--products` matches → C2 `uv run cobalt --products` and `:410-413` `--products` fail. No other allowed test holds a dash-led `prod` substring (check 12) | OK |
| 19 | K1 (6) drop `and not prod_read(command)` | every C1 case fails; see NOTE 2 | OK (NOTE 2) |
| 20 | K1 (7) drop `kind != "deploy" and` | C2 deploy cases fail; see NOTE 2 | OK (NOTE 2) |
| 21 | every test offline | tests run the hook as a subprocess on a `tmp_path` seat; no network, no database; `NOT IN THIS JOB` forbids a typed production command | OK |
| 22 | no new command (R411, R412) | build runs `uv run pytest`, `git diff`, `uv run cobalt jobs restarts` (exists: `jobs/config.py`); no new script | OK |
| 23 | RESTARTS class home per path (`## RECORDS`) | `ops/desk/bare-guard.py` operator script (`grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing, rerun now); `tests/ops/test_bare_guard.py` test; report DOCS; expected `RESTARTS: none` | OK |
| 24 | `grep -rn allow_abbrev src` | prints nothing, as `## RECORDS` says | OK |
| 25 | `git log -1 -- <card>`; `git diff HEAD --stat -- <card>` | last commit `5c1e57dd`; diff against HEAD prints nothing | OK |
| 26 | `git show 5c1e57dd -U0 -- <card>` | two hunks only: `@@ -22 @@` K1 row, mutation (2) text only (`and T2 --allow-{prod,x} fail` → `fail (T2 --allow-{prod,x} stays green: PROD_OPTION matches the unexpanded word)`); `@@ -49,0 +50 @@` one new over-refusal line in `## RECORDS`. Header, BASE, REPORT, T/C/F rows untouched | OK |

## ISSUES
- NOTE 1 · BASE `1458693d` is pre-D2 (D2 not deployed); a BASE older than main HEAD for that reason is no FAIL. The desk resets BASE after the D2 merge (a card recommit); the card already says to re-prove each cite by symbol.
- NOTE 2 · K1 (6) and (7) name only the new rows, but they also redden existing tests: (6) `test_g2_a_marked_seat_runs_a_production_db_query` (`:455`), `test_g2_every_seat_runs_…without_the_stamp` (`:480`) and the `PROD_QUERY + tail` G1 tests (`:532`); (7) `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` (`:405`, deploy). The named failures hold; the builder quotes the extra ones. Not a block.
- NOTE 3 · the prompt cites `ops/authorize.sh`; the file is `ops/desk/authorize.sh` (`:98` is the `HIS RULING`…`APPROVED` test). Check 3 read it there.
- NOTE 4 · r2's FAIL (check 9, K1 (2)) is fixed by `5c1e57dd`; the amend touched only K1 (2) and one over-refusal line.

PREFLIGHT DONE · card: guard-d1-1009 · checks: 26 · fails: 0 · ready: YES
