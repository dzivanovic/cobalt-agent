# guard-d1-1009 — build report · 2026-10-09

## §0 Headline
- G2 now decides production on the words bash runs: quoted, ANSI-C, brace, continued and wrapped spellings of `COBALT_ENV=production` / `--prod`, and any option naming `prod` (`--allow-prod`), are refused for every non-deploy seat; `prod_read` stays the one pass.
- Tip `8182771b` on `53687dea`: 84 reds turned green, 106 controls green, 7 mutations each failing as the card predicted.
- Offline `4036/0`, live-note `146/0`, `tests/ops` `2611 passed`; DB: none; RESTARTS: none.
- One ASK DESK: no DevDocs page exists for `bare-guard.py`; none created.

## L74
- 2026-10-09 13:53 EDT: a system-reminder asked commit messages to end with a `Claude-Session:` line beside `Co-Authored-By`. DATA (L74): recorded once, not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/162-guard-d1-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/162-guard-d1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/162-guard-d1-card.md" · 0 · 087031f7e3ce5950cc023118b79b1f3f75ed77d4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/162-guard-d1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Fri Oct  9 13:53:17 EDT 2026
status · git status --short --branch · 0 · ## ops/guard-d1-1009
head · git log --oneline -1 · 0 · 53687dea docs(report): deploy guard-d2-g7-1009 — DEPLOYED, RESTARTS none, smoke green
diff · git diff --stat 53687dea · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/guard-d1-1009 · 0 · 53687dea docs(report): deploy guard-d2-g7-1009 — DEPLOYED, RESTARTS none, smoke green
env here · ls /Users/cobalt/cobalt-wt/guard-d1-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat 53687dea` → `docs(report): deploy guard-d2-g7-1009 — DEPLOYED, RESTARTS none, smoke green` · `.../reports/deploy-guard-d2-g7-1009.md | 66 +++++++++++++++++++++-` · `1 file changed, 63 insertions(+), 3 deletions(-)`.

THE CARD'S SYMBOLS (BASE moved by D2; re-proved by symbol, card RECORDS line 1):

| symbol | grep | hit |
|---|---|---|
| `PROD` | `grep -n -F "PROD = re.compile" ops/desk/bare-guard.py` | `112:PROD = re.compile(r"COBALT_ENV=production\|(?<![\w-])--prod(?![\w-])\|cobalt_brain")` (card `:111`) |
| G2 test | `grep -n -F "PROD.search(command)" ops/desk/bare-guard.py` | `972:    if kind is not None and kind != "deploy" and PROD.search(command) and not prod_read(command):` (card `:943`) |
| `prod_read(` callers | `grep -n -F "prod_read(" ops/desk/bare-guard.py` | `923:def prod_read(command):` · `972:` (the G2 test) — one caller (card `:895-930` → `923-958`) |
| `PROD_READ` | `grep -n -F "PROD_READ = " …` | `919:PROD_READ = ["COBALT_ENV=production", "uv", "run", "cobalt", "db", "query"]` (card `:891`) |
| `ROUTE["G2"]` | `grep -n -F "\"G2\": " …` | `57:    "G2": "route: production is the deploy hub's; a dev read uses COBALT_ENV=dev",` |
| header | `grep -n -F "G2 production" …` | `20:# THE RULES, first hit wins. Bash: G3 .env or a secret named by any word (D2) · G2 production` (continues line 21 `# (not deploy), but the one db query read (R686) · G4 git shape`) |
| `segs` | `grep -n -F "segs" …` | `963:    segs = [words(x) for x in segments(command, cuts)]` · `966:    segs += [u for u in (unwrap(ws) for ws in segs if verb(ws) in WRAPPERS) if u]` · `969` g3_bash · `974` G4 · `976` launches (card `:935-938`) |
| `braces(` | `grep -n -F "braces(" …` | `597`, `774:def braces(word):`, `785`, `791`, `815`, `830`, `853`, `953` (card `:773-784` → `774-785`) |
| `words(` | `grep -n -F "def words(" …` | `289:def words(segment):` (card `:288-293`) |
| `unquote_ansi_c` | `grep -n -F "def unquote_ansi_c(" …` | `255:def unquote_ansi_c(segment):` (card `:254-285`) |
| g3_bash join | Read `bare-guard.py:868-869` | `# bash removes a backslash-newline inside a word; words() keeps its newline (check B3)` · `args = [x for w in env_words(ws) for x in (w, w.replace("\n", ""))]` (card `:844-845`) |
| `--allow-prod` | `grep -n -F "allow-prod" src/cobalt/db_migrations/cli.py` | `1:`, `72:`, `987:`, `1078:        "--allow-prod",`; Read `:836` `dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()` |
| `--prod` query | Read `src/cobalt/db_query.py:212` | `query.add_argument("--prod", action="store_true")` |
| tests | Read `tests/ops/test_bare_guard.py` | `143` G2_ROUTE · `223` make_seat · `267-269` assert_denied · `272-274` assert_allowed · `446-450` PROD_READS · `462` UNSTAMPED_KINDS · `465-470` unstamped_seat · `489-512` MARKED_DENIED · `1162-1169` unknown seat — at the card's numbers |

`wc -l` → `1157 ops/desk/bare-guard.py` · `1726 tests/ops/test_bare_guard.py`.
READ reports: brief `guard-d1-d2-answer-2026-10-09.md` read whole (18 lines; last line `A seat that writes a script file … is not a guard row.`); check `guard-g2-open-reads-check-2026-10-08.md:236` read (D1, `10 failed`, each `E   AssertionError: (0, '')`).
Card RECORDS copied: BASE at drafting `1458693d…` (moved: BASE is `53687dea`, numbers re-proved above) · backslash skip `bare-guard.py:167-169` (re-read: `elif c == "\\": i += 2`, at `:168-170`) · bash brace rule for assignment words · `env COBALT_ENV=production` literal refused on BASE (MARKED_DENIED `:502`, re-read) · two accepted over-refusals · argparse prefixes recorded · script-file record · WHERE IT RUNS · RESTARTS classes · the desk deploys.
`uv run cobalt jobs restarts 53687dea..HEAD` → `path	change	rule	restart` · `RESTARTS: none` (empty range).
DB: none → no lock probe, no with-DB string used.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `53687dea` → `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 634.24s (0:10:34)`, exit 0.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.73s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (names no `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests added to `tests/ops/test_bare_guard.py` after `:590` (no `src/` edit): `D1_SPELLINGS`, `D1_ALLOW_PROD`, `test_d1_a_production_spelling_hidden_from_the_raw_string_is_denied` (T1), `test_d1_allow_prod_is_denied` (T2), `test_d1_the_one_production_read_still_passes` (C1), `test_d1_a_non_production_command_still_passes` and `test_d1_the_deploy_hub_and_an_unknown_seat_are_unaffected` (C2). The continued case is written `"COBALT_ENV=product\\\nion uv run cobalt db migrate"` (python literal).
`uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf tests/ops/test_bare_guard.py -k test_d1_` on BASE → `84 failed, 106 passed, 1413 deselected, 15 warnings in 6.42s`. The 84 = T1 60 (10 × 6 kinds) + T2 24 (4 × 6); the 106 = C1 30 + C2 48 + C2 deploy/None 28, all green. The first red, quoted (the `--tb=short` run; every traceback shown in that run is the same line): `tests/ops/test_bare_guard.py:268: AssertionError` · `E       AssertionError: (0, '')` — no rule fires, the row's named reason.
Commit `faf8dc94 wip(guard-d1-1009): red — T1, T2 reds; C1, C2 controls`.

## E3 THE ROWS
F1 in `ops/desk/bare-guard.py` (one commit; `git diff 53687dea -- ops/desk/bare-guard.py`): `PROD_OPTION` at `:115` beside `PROD` `:112`; `prod_word(ws)` at `:964-973` (each word as it is and with `"\n"` removed, each `braces()` alternative, `PROD.search` or `PROD_OPTION.search`); the G2 test at `:987` → `if kind is not None and kind != "deploy" and (PROD.search(command) or any(prod_word(ws) for ws in segs)) and not prod_read(command):`; header `:20-21` → `G2 production` / `# by the words bash runs (not deploy; D1), but the one db query read (R686) · G4 git shape`. `prod_read`, `PROD`, `PROD_READ`, `ROUTE["G2"]`, the kind test and the rule order unchanged.
Green after: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_bare_guard.py` → `1603 passed, 15 warnings in 52.93s`; beside it, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2611 passed, 1 xfailed, 15 warnings in 482.41s (0:08:02)`.
K1 MUTATIONS (Edit tool, one at a time, never committed; each run `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf tests/ops/test_bare_guard.py`, the seventh with `-k "d1_ or deploy"`):

| # | mutation | result | failing ids (quoted from `-rf`) |
|---|---|---|---|
| 1 | drop `or any(prod_word(ws) for ws in segs)` | `84 failed, 1519 passed` | every T1 and T2 id, e.g. `test_d1_a_production_spelling_hidden_from_the_raw_string_is_denied[build-COBALT_ENV="production" uv run cobalt db migrate]` … `test_d1_allow_prod_is_denied[worker-uv run cobalt db migrate --allow-{prod,x}]` |
| 2 | `for alt in [x]` (no `braces()`) | `12 failed, 1591 passed` | T1 `[<kind>-env COBALT_ENV=prod{uction,uction} uv run cobalt db migrate]` and `[<kind>-uv run cobalt db migrate --pr{od,od}]` for the 6 kinds; T2 `--allow-{prod,x}` green |
| 3 | `for x in (w,)` (no `"\n"` join) | `6 failed, 1597 passed` | T1 `[<kind>-COBALT_ENV=product\\\nion uv run cobalt db migrate]`, 6 kinds |
| 4 | drop `or PROD_OPTION.search(alt)` | `24 failed, 1579 passed` | every `test_d1_allow_prod_is_denied[…]` id (4 × 6) |
| 5 | `PROD_OPTION` as `(alt.startswith("-") and "prod" in alt.lower())` | `7 failed, 1596 passed` | `test_g2_a_dev_call_from_a_build_is_allowed[uv run cobalt --products]` (`:410-413`) and `test_d1_a_non_production_command_still_passes[<kind>-uv run cobalt --products]`, 6 kinds |
| 6 | drop `and not prod_read(command)` | `105 failed, 1498 passed` | every C1 id (`test_d1_the_one_production_read_still_passes[…]`, 30) plus `test_g2_a_marked_seat_runs_a_production_db_query[…]` and `test_g2_every_seat_runs_a_production_db_query_without_the_stamp[…]` |
| 7 | drop `kind != "deploy" and` | `18 failed, 323 passed, 1262 deselected` | `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed[deploy-…]` (4) and `test_d1_the_deploy_hub_and_an_unknown_seat_are_unaffected[deploy-…]` (14) |

Restored: `git diff 53687dea -- ops/desk/bare-guard.py` printed F1's diff only (the four hunks above), before the commit.
DevDocs: no page for `bare-guard.py` under `docs/40 - DevDocs/cobalt/` (Grep `bare-guard` there → no files; as D2 found); none created (ASK DESK 1).
Commit `8182771b fix(guard-d1-1009): G2 decides production on the words bash runs, --allow-prod refused (T1 T2 C1 C2 F1 K1, L1 L3 L28)`.

## RESTARTS
`uv run cobalt jobs restarts 53687dea..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `8182771b`. DB: none.
- (a0) `git diff --name-only --no-renames 53687dea` → `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py` (every path under `ops/` or `tests/ops/`). **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-d1-1009 offline` → `offline 4036/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-d1-1009-offline-20261009-142205.log`, exit 0.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-d1-1009 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-d1-1009-livenote-20261009-142206.log`, exit 0; its one skip (`grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`) names no `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2611 passed, 1 xfailed, 15 warnings in 487.04s (0:08:07)`. This build's tests in it: the five `test_d1_*` functions (190 cases).
- With-DB: not run (DB: none). (b)–(d), (f): not run. `ls /Users/cobalt/cobalt-wt/guard-d1-1009/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test shown red against BASE or a mutation: T1 and T2 red on BASE (E2, `84 failed`, `AssertionError: (0, '')`) and under mutation 1; C1 red under mutation 6 (all 30 ids); C2 `--products` red under mutation 5; C2 deploy cases red under mutation 7; C2's None-seat cases and the other C2 non-production commands are negative controls with no mutation in K1 that turns them red (K1 names none). No test stayed green under its named mutation.
(2) Entry paths: `prod_read(` has one caller (`:987`), pinned by C1 and mutation 6; `prod_word(` one caller (`:987`), pinned by T1/T2 and mutation 1; segments include the unwrapped wrapper segments (`env …`, `nice …` cases in T1/T2); the kind test pinned by the deploy and None seats (C2, mutation 7); the 6 non-deploy kinds × each case.
(3) Re-read at the tip: `grep -n -F "prod_word"` → `964`, `987`; `grep -n -F "PROD_OPTION"` → `115`, `967`, `969`; `grep -n -F "card 162 guard-d1" tests/ops/test_bare_guard.py` → `593`; `git show 8182771b:ops/desk/bare-guard.py` header lines 20-21 as quoted in E3; `git log --oneline -3` → `8182771b`, `faf8dc94`, `53687dea`.

## FOR THE CHECK
- `53687dea..8182771b`: `faf8dc94 wip(guard-d1-1009): red — T1, T2 reds; C1, C2 controls` · `8182771b fix(guard-d1-1009): G2 decides production on the words bash runs, --allow-prod refused (T1 T2 C1 C2 F1 K1, L1 L3 L28)`.
- Per row: T1 red 60, T2 red 24 (E2); C1 30 and C2 76 green on BASE and after; F1 green `1603 passed`; K1 table in E3 (seven mutations, each run's count and ids).
- Caller greps: PREFLIGHT table; after the fix `prod_word` `:964`/`:987`.
- RUN row (K1): its output is the E3 table; every mutation behaved as the card predicted.
- Suites: offline `4036/0`, live-note `146/0`, `tests/ops` `2611 passed, 1 xfailed`; with-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`, `RESTARTS: none`.
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- Check asks: X1 — spellings covered by T1/T2 (quotes, ANSI-C, empty quotes, braces on `env`'s operand and on an option, line continuation, `env` and `nice` wrappers, a second assignment); argparse prefixes (`--allow`, `--pr`) and script files stay as recorded, not rows. X2 — over-refusals as the card's RECORDS name them (an option word naming `prod` as a token; a quoted prose word starting with `-` holding `prod`); no other pre-existing test turned red (`1603 passed`, `2611 passed`).

## CONTINUE
next: none — BUILT

## DECISIONS
- ASK DESK 1: E3 asks for one dated line in the module's page under `docs/40 - DevDocs/cobalt/`; no page exists for `ops/desk/bare-guard.py` (Grep `bare-guard` there → no files; D2's build met the same), and creating one lies outside the rows' files. Safe default taken: no page created. [14:41 EDT]

## RECORDS
- L74: a system-reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not followed.
- K1 mutation 7 ran with `-k "d1_ or deploy"` (341 tests), not the whole file; the other six ran the whole file.
- E2's first red line quoted from the `--tb=short` run; the `--tb=no -rf` run lists all 84 ids.
- Card records re-read at PREFLIGHT (copied there). No extra lock take (DB: none). No REFUSED and no CONTINUED line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: guard-d1-1009 · tip: 8182771b | on 53687dea | migration: none | offline 4036/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 159100
