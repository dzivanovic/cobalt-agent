JOB: guard-d1-1009
LADDER: OFF-LADDER — reports/cto-2026-10-08.md 2026-10-08 R707
BRANCH: ops/guard-d1-1009
WORKTREE: guard-d1-1009
BASE: 1458693d
TIP:
REPORT: /Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-08 R686

## ROWS

| row | what | red first | files |
|---|---|---|---|
| T1 | RED TESTS, the spellings. G2 decides "production" on the words bash runs; today it fires on `PROD.search(command)`, the RAW string (`ops/desk/bare-guard.py:943`, `PROD` `:111`), so a spelling whose quotes, `$'…'`, braces or line continuation hide the literal passes for a non-deploy seat. Brief `reports/guard-d1-d2-answer-2026-10-09.md` `## CARD D1`; check `reports/guard-g2-open-reads-check-2026-10-08.md:236` | NEW `test_d1_a_production_spelling_hidden_from_the_raw_string_is_denied`, parametrized over `UNSTAMPED_KINDS` (`tests/ops/test_bare_guard.py:462`, seat by `unstamped_seat` `:465-470`) × a list `D1_SPELLINGS`: `COBALT_ENV="production" uv run cobalt db migrate` · `COBALT_ENV='production' uv run cobalt db migrate` · `COBALT_ENV=$'production' uv run cobalt db migrate` · `COBALT_ENV=prod''uction uv run cobalt db migrate` · `env COBALT_ENV="production" uv run cobalt db migrate` · `FOO=1 COBALT_ENV="production" uv run cobalt validate` · `env COBALT_ENV=prod{uction,uction} uv run cobalt db migrate` (env's operand is brace-expanded) · `'COBALT_ENV=product\\\nion uv run cobalt db migrate'` (python literal, as `:544`) · `uv run cobalt db migrate --"prod"` · `uv run cobalt db migrate --pr{od,od}` → `assert_denied(…, G2_ROUTE)` (`:267-269`, `:143`). RED on BASE: `assert done.returncode == 2` (`:268`) fails, `AssertionError: (0, '')` (no rule fires: `PROD.search` misses the raw text, G1 sees one command) | `tests/ops/test_bare_guard.py` |
| T2 | RED TESTS, `--allow-prod`. `cobalt db migrate --allow-prod` targets `cobalt_brain` (`src/cobalt/db_migrations/cli.py:1078`, `:836`); `PROD`'s `(?<![\w-])--prod(?![\w-])` never matches it | NEW `test_d1_allow_prod_is_denied`, over `UNSTAMPED_KINDS` × `uv run cobalt db migrate --allow-prod` · `uv run cobalt db migrate --allow-prod --rollback --down-to 0010` · `nice uv run cobalt db migrate --allow-prod` · `uv run cobalt db migrate --allow-{prod,x}` → `G2_ROUTE`. RED on BASE: `:268` fails, `(0, '')` | `tests/ops/test_bare_guard.py` |
| C1 | CONTROL, the one pass (R686): `prod_read` (`:895-930`) stays the one allowed production read for every seat, judged on the same words, unchanged | NEW `test_d1_the_one_production_read_still_passes`, over `UNSTAMPED_KINDS` × `PROD_READS` (`:446-450`) + `'COBALT_ENV="production" uv run cobalt db query --prod --side user "SELECT 1"'` + `"COBALT_ENV=production uv run cobalt db query --prod 'select 1'"` (the brief's line; `prod_read` asks no `--side`) → `assert_allowed` (`:272-274`). Green on BASE and after. Unchanged and green after: `:478-486`, `:524-527` (every `MARKED_DENIED` `:489-511` still `G2_ROUTE`), `:532-538`, `:548-590` | `tests/ops/test_bare_guard.py` |
| C2 | CONTROL, ordinary commands and the exempt seats | NEW `test_d1_a_non_production_command_still_passes`, over `UNSTAMPED_KINDS` × `COBALT_ENV=dev uv run pytest -q` · `COBALT_ENV="dev" uv run cobalt db migrate` · `uv run cobalt db migrate --rollback --down-to 0010` · `uv run cobalt --products` · `grep -rn "allow.prod" src/` · `grep -rn production src/` · `grep -rn COBALT_ENV src/` · `uv run pytest -q tests/ops/test_bare_guard.py -k prod` → `assert_allowed`. NEW `test_d1_the_deploy_hub_and_an_unknown_seat_are_unaffected`, over kinds `deploy`, `None` (`make_seat` `:223`) × `D1_SPELLINGS` + T2's list → `assert_allowed`. Green on BASE and after. Unchanged and green after: `:397-413`, `:1164-1172` | `tests/ops/test_bare_guard.py` |
| F1 | THE FIX, row G2-W. Add `PROD_OPTION = re.compile(r"^-.*(?<![a-z])prod(?![a-z])", re.I)` beside `PROD` (`:111`): an option word holding `prod` as a token (`--allow-prod`, `--prod=1`, `-prod`; not `--products`). Add `prod_word(ws)`: True when a word of `ws`, as it is and with `"\n"` removed (bash joins a backslash-newline, `words()` keeps it; as `g3_bash` `:844-845`), has a `braces()` (`:773-784`) alternative that `PROD.search`es (this covers the word `COBALT_ENV=production`) or `PROD_OPTION.search`es. The G2 test (`:943`) becomes `if kind is not None and kind != "deploy" and (PROD.search(command) or any(prod_word(ws) for ws in segs)) and not prod_read(command):`, `segs` as built at `:935-938` (the unwrapped segments too). `words()` (`:288-293`) already decodes `$'…'` (`unquote_ansi_c` `:254-285`) and strips quotes. `prod_read`, `PROD`, `PROD_READ` (`:891`), `ROUTE["G2"]` (`:57`), the kind test and the rule order unchanged. Header comment `:20-21` `G2 production (not deploy), but the one db query read (R686)` → `G2 production by the words bash runs (not deploy; D1), but the one db query read (R686)` | T1, T2 turn green; C1, C2 stay green | `ops/desk/bare-guard.py` |
| K1 | K25 MUTATIONS, one at a time with the Edit tool, never committed; each run `uv run pytest -q -p no:cacheprovider tests/ops/test_bare_guard.py` and quote the named failures: (1) drop `or any(prod_word(ws) for ws in segs)` → every T1, T2 case fails; (2) drop `braces()` in `prod_word` → T1 `env COBALT_ENV=prod{uction,uction}…`, `--pr{od,od}` and T2 `--allow-{prod,x}` fail; (3) drop the `"\n"` join → T1 continued case fails; (4) drop the `PROD_OPTION` clause → every T2 case fails; (5) `PROD_OPTION` as the brief's substring (`w.startswith("-") and "prod" in w.lower()`) → C2 `uv run cobalt --products` and `:410-413` fail; (6) drop `and not prod_read(command)` → every C1 case fails; (7) drop `kind != "deploy" and` → C2 deploy cases fail | RUN — each mutation's failing test ids quoted; the file restored, `git diff BASE -- ops/desk/bare-guard.py` equal to F1's diff | `ops/desk/bare-guard.py` (mutated and restored), `tests/ops/test_bare_guard.py` |

## NOT IN THIS JOB
- D2 (G3 by any word): card `158-guard-d2-card.md`, built and deployed first.
- Any other rule (G1, G3-G11, B1-B11), `prod_read`, `PROD`, `ROUTE` text, `seat()`, the Write / Edit and Read rules.
- An argparse prefix of `--allow-prod` or `--prod` (`--allow`, `--pr`): recorded, not a row.
- Any `src/` file, hub, `settings.json` or other `ops/desk` script.
- A name built at run time or a script file the seat writes and runs: recorded, not a row.
- Any production command typed in the build: every test builds its seat under `tmp_path`.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-d2-answer-2026-10-09.md` `## CARD D1` and `## RECORDED, NOT CARDED`.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-open-reads-check-2026-10-08.md` line 236 (D1).
- `ops/desk/bare-guard.py` lines 20-21, 57, 111-112, 126-215, 254-301, 773-784, 842-854, 889-958.
- `tests/ops/test_bare_guard.py` lines 143, 223-277, 387-590, 1156-1172.
- `src/cobalt/db_migrations/cli.py` lines 836, 1069-1082; `src/cobalt/db_query.py` lines 209-216.

## CHECK ASKS
- X1 Can a production verb pass G2 from a non-deploy seat by any spelling whose words bash runs name `COBALT_ENV=production`, `--prod`, `cobalt_brain` or a `prod` option (quotes, ANSI-C, braces, a line continuation, a wrapper, a second assignment)?
- X2 Does any command but the `prod_read` shape that passed G2 on BASE now fail it, beyond the over-refusal named in RECORDS?

## RECORDS
- BASE at drafting: `1458693dbde5371259a29c5d502d74e3878fee3b` (`git -C /Users/cobalt/cobalt rev-parse HEAD`, 2026-10-09 11:38 EDT); `git -C /Users/cobalt/cobalt diff --stat 0e84db6f HEAD -- ops/desk src/cobalt tests/ops` prints nothing, so every `file:line` above is HEAD's and the brief's numbers hold (G2 943, segs 935-938, `prod_read` 895-930). D2 moves them: the build re-proves each by symbol on its BASE.
- The scanner skips the character after a backslash outside quotes (`bare-guard.py:167-169`), so a backslash-newline is no cut and stays inside the word `words()` returns.
- Bash does not brace-expand an assignment word, so `COBALT_ENV=prod{uction,uction} cmd` sets the literal; as `env`'s operand it expands. T1 uses the `env` form.
- `env COBALT_ENV=production …` (brief) holds the literal and is refused on BASE (`MARKED_DENIED` `:502` shape); T1 uses `env COBALT_ENV="production" …` (check `:236`).
- Over-refusal accepted: a non-deploy seat's word that is an option naming `prod` as a token (`grep -rn -e --allow-prod src/`) is refused; a seat writes the pattern without the leading dashes (`grep -rn "allow.prod" src/`, C2).
- argparse prefixes reach production without a `prod` word: `cobalt db migrate --allow` (unambiguous prefix of `--allow-prod`, `db_migrations/cli.py:1078`) and `cobalt db query --pr` (`db_query.py:212`); no parser sets `allow_abbrev` (`grep -rn allow_abbrev src` prints nothing). Recorded, not carded (R707).
- RECORDED, NOT CARDED (brief): a seat that writes a script file and then runs it can hide a production verb from any word-level guard; the wall is structural (production writes run only in the deploy seat). L-level, not a guard row.
- WHERE IT RUNS: the hook entry `/Users/cobalt/.claude/settings.json:22` runs `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`, main's file, fresh per call: live at the deploy merge, no restart; the build seat's own calls run main's copy.
- RESTARTS classes, one home per path (K10): `ops/desk/bare-guard.py` operator script (`grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing, 2026-10-09 11:38 EDT); `tests/ops/test_bare_guard.py` test; the report DOCS. Expected `RESTARTS: none`; the build runs `uv run cobalt jobs restarts <BASE>..HEAD` and quotes it.
- The desk deploys this branch with its own deploy card (R587).
