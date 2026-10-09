# Guard D1 preflight · card 162 · 2026-10-09

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 0a | `grep -n "refuse" ops/desk/desk-launch.sh` (build: `:722-741`, `:754-762`, `:895-911`) | JOB `guard-d1-1009` is `[a-z0-9-]`; BRANCH `ops/guard-d1-1009` plain; WORKTREE `guard-d1-1009` in pattern; LADDER, BASE, RULINGS non-empty; RULINGS `2026-10-08 R686` is `<date> R<n>`; TAG absent; `## ROWS` present; card path is `$PROMPTS/2026-10-09/162-guard-d1-card.md`, absolute | OK |
| 0b | build `REPORT` rule `desk-launch.sh:901-904` | requires `$WT/$wt/docs/40 - DevDocs/reports/*.md` = `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/…`. Card line 7: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md` → launcher prints `incomplete card: REPORT must be …` and exits | **FAIL** |
| 0c | BASE `1458693d`: `desk-launch.sh:899-900`, `git merge-base --is-ancestor 1458693d HEAD` | 8 hex, a commit, ancestor of HEAD `e1dfae75` (exit 0) | OK |
| 0d | header per `CARD.md:14,76-85` | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty as on a build card; `DB: none`; LADDER `OFF-LADDER — reports/cto-2026-10-08.md 2026-10-08 R707`; row 75 is R707 `RECORD` (brain's brief), a ladder cite, not a ruling | OK |
| 1 | `grep -n "^| R686 |" reports/cto-2026-10-08.md` | `:39` one row: `HIS RULING (words R686, standing) … APPROVED · HIS RULING · APPLIED` — `HIS RULING` before `APPROVED`, one line | OK |
| 2 | `git log -1 --format=%H -S"| R686 |" -- reports/cto-2026-10-08.md`; `git diff -U0` of that file | `4125ff02…`; the file's working-tree diff touches only the `OWED:` line 93, so row `:39` equals HEAD | OK |
| 3 | `grep -n` / reads of `ops/desk/bare-guard.py` | `:20-21` header (`G2 production (not deploy), but the one db query read (R686)`); `:57` `"G2": "route: production is the deploy hub's…"`; `:111` `PROD = re.compile(r"COBALT_ENV=production\|(?<![\w-])--prod(?![\w-])\|cobalt_brain")`; `:167-169` `elif c == "\\": i += 2`; `:288-293` `def words`; `:254` `def unquote_ansi_c`; `:773-784` `def braces`; `:845` `w.replace("\n", "")`; `:891` `PROD_READ`; `:895-930` `prod_read`; `:935-938` `segs = …` and `segs += …`; `:943` `if kind is not None and kind != "deploy" and PROD.search(command) and not prod_read(command):` | OK |
| 4 | reads of `tests/ops/test_bare_guard.py` | `:143` `G2_ROUTE`; `:223` `make_seat`; `:267-269` `assert_denied` (`assert done.returncode == 2, (done.returncode, done.stderr)`); `:272-274` `assert_allowed`; `:397-413`; `:446-450` `PROD_READS`; `:462` `UNSTAMPED_KINDS`; `:465-470` `unstamped_seat`; `:478-486`; `:489-511` `MARKED_DENIED` (`:502` is the `env COBALT_ENV=production` line); `:524-527`; `:532-538`; `:544` the python-literal continuation; `:548-590`; `:1164-1172` | OK |
| 5 | five spellings plus `--allow-prod` (brief `## CARD D1`) | T1 has `"…"`, `'…'`, `$'…'`, `prod''uction`, `env …`, plus a second assignment, `{uction,uction}`, continuation, `--"prod"`, `--pr{od,od}`; T2 has `--allow-prod` four ways | OK |
| 6 | `prod_read` stays the one pass (R686) | F1 leaves `prod_read`, `PROD`, `PROD_READ`, `ROUTE["G2"]` unchanged; C1 pins `PROD_READS` plus two quoted/unquoted `--prod` lines. I traced both new C1 lines through `prod_read` (`:904-930`): words equal `PROD_READ`, one `--prod`, no `--side` check on the second → pass on BASE and after | OK |
| 7 | "D1 builds after D2 deploys" | `NOT IN THIS JOB` and `RECORDS` say so. `git log -1 -- ops/desk/bare-guard.py` is `828f28dc` (no D2 commit), so D2 is not deployed yet | OK |
| 8 | control row C2 | non-production commands (`COBALT_ENV=dev uv run pytest -q`, `db migrate`, `--products`, three `grep`s, `pytest -k prod`) and deploy/`None` seats → `assert_allowed`. Traced against F1: `grep … "allow.prod"` has no leading dash; `-k` and `--products` match neither `PROD` nor `PROD_OPTION` | OK |
| 9 | each red fails on BASE for its stated reason (K25) | T1: raw string holds none of `COBALT_ENV=production`, `--prod` after a non-word char, `cobalt_brain` (quotes, `$'`, `''`, braces, `\`+newline break the literal); so `PROD.search(command)` misses, G1 sees one command → `(0, '')` at `:268`. T2: `--allow-prod` fails `(?<![\w-])--prod`. Read from code, not run (L70) | OK |
| 10 | K1 mutations 1-7 | each names a distinct clause of F1 and the tests that must go red; (5) uses `--products`, which C2 and `:410-413` carry | OK |
| 11 | every test offline | tests run the hook as a subprocess on a `tmp_path` seat; no network, no database; card line 30 forbids a typed production command | OK |
| 12 | no new command (R411, R412) | build runs `uv run pytest`, `git diff`, `uv run cobalt jobs restarts` (`grep -rl "jobs restarts" src/cobalt` → `jobs/config.py`); no new script | OK |
| 13 | RESTARTS class home per path (`## RECORDS`) | `bare-guard.py` operator script (`grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing, rerun now); `tests/ops/test_bare_guard.py` test; the report DOCS; expected `RESTARTS: none` | OK |
| 14 | `git log -1 -- <card>` and `-- <draft report>` | both `b155b95d817024a801f381367b523f457028a110`; neither is in `git status` | OK |
| 15 | `grep -rn "allow_abbrev" src` | prints nothing, as `RECORDS` says | OK |

## ISSUES
- FAIL · check 0b · card line 7 `REPORT:` is a main path; the build launcher requires `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md` (`desk-launch.sh:901-904`). Draft D6 kept the main path as ordered; the launcher refuses it. Fix the card line and recommit.
- NOTE · BASE `1458693d` is pre-D2 (D2 not deployed). Draft D1 says the desk sets BASE to main HEAD after the D2 merge; the launcher also needs the card committed unchanged (`:760-762`), so that edit is a recommit. Row numbers (`:943`, `:935-938`) shift with D2; the card already says re-prove by symbol.
- NOTE · LADDER cites R707, a `RECORD` row, not a ruling. The launcher does not read LADDER for a ruling, so it passes.
- NOTE · the card tracks no `HOUSE A`/`HOUSE B` value on a build card; the launcher reads them only on `overruled`, so this is fine.

PREFLIGHT DONE · card: guard-d1-1009 · checks: 16 · fails: 1 · ready: NO
