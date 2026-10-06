# guard-g2 card preflight — 2026-10-06

Card `21-guard-g2-card.md`, BASE `3c257bb9`. Read only; I ran no test and no production command.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c257bb9 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/guard-g2-1006` | `fatal: Needed a single revision` (exit 128) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/guard-g2-1006` | `No such file or directory` | OK |
| 1d | card header lines 6-11 | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `DB: none`; `RULINGS: 2026-10-06 R511` | OK |
| 2a | `grep -n "^| R511 " reports/cto-2026-10-06.md` | `20:\| R511 \| 06:37 ET \| HIS RULING: add the G2 row … \| APPROVED — pending fold \|` | OK (line number: see 3c) |
| 2b | the same row | holds `HIS RULING` and `APPROVED` | OK |
| 2c | `git log -1 --format=%h -S"\| R511 \|" -- reports/cto-2026-10-06.md` | `720c98b8` | OK |
| 3a | `bare-guard.py` (tree = BASE: `git diff --stat 3c257bb9 HEAD` and the working-tree diff are both empty for the guard, its test and `db_query.py`) lines 56, 106, 697-719, 722-744, 846-868 | `ROUTE` 56 · `PROD = re.compile(…)` 106 · `read_card` 697-719 · `seat` 722-744 with `prompt = …` at 727, kinds 733-742, return dict at 744 · `bash_rules` 846-868, G2 at 856-857 | OK |
| 3b | `bare-guard.py` header "lines 20-21 and 36-37 … the `G2 production (not deploy)` entry" | the entry is line 20 only (`G2 production (not deploy)`); 21 is G4/G7 text; 36-37 is the `COBALT_WT_ROOT` test-env comment, no G2 entry | FAIL |
| 3c | card RECORDS "R511 is line 19" (the draft report says line 19 too) | `grep -n` prints line 20 | FAIL |
| 3d | `tests/ops/test_bare_guard.py` 143, 189-212, 223-247, 250-274, 387-413 | `G2_ROUTE` 143 · `transcript` 189-212 · `make_seat` 223-247 · `call`/`run`/`assert_*` 250-274 · G2 block 387-413 | OK |
| 3e | `desk-launch.sh` 238-275, 252-261, 458, 451-476 | `ruling_row` 238-265, `ruling_items` 267-275, count `grep -c '^RULINGS:' … -eq 1` at 458, F5 comment 451-453, `ruled` 456-460 | OK |
| 3f | `src/cobalt/db_query.py` 157-158, 163, 211-215 | `requires --prod` 157-158 · `BEGIN READ ONLY` 163 · `--side` choices 211 · `--format` 213 · `--limit` 214 · `sql` 215 | OK |
| 3g | RECORDS: `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` · `settings.json:22` · `bare-guard.py:5` | no output · `22: "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"` · `5: … It never runs a command.` | OK |
| 4a | red `…db query --side user --prod "SELECT 1"` on a ruled brain seat, BASE | `seat()` 737-738 gives `brain` (cwd in repo, prompt `prompts/2026-01-01/30-survey.md`); `PROD.search` hits at 856 → `G2`, exit 2; `assert_allowed` fails on `returncode == 0`. Red for the stated reason. The two sibling reds (no `COBALT_ENV` word, `--prod` matches `PROD`; the two-item line) fail the same way | OK |
| 4b | green leg after the change | `scan` finds nothing in `… "SELECT 1"` (quoted text is skipped, `scan` 121-200) and `quote` is None; `g3_bash`, G4, G7 do not apply to `uv run`; `g1` (626) returns None on a no-find command; deploy already passes the same commands (`PROD_CALLS`, test 405) | OK |
| 4c | each negative control | no or two `RULINGS:` lines, `none`, bad item, missing file, no/two/non-approved/non-HIS-RULING row, no `production read`: `ruled_prod_reads` False. Build/check/devfix/desk: kind is not `brain`, so False. `migrate`, `--allow-prod`, `--prod=1`, second positional, `NAME=x`, `env`: `prod_read_shape` False (`--allow-prod` is hit by `PROD` only through the `COBALT_ENV=production` word the control carries; the card's "not caught by `PROD`" wording is loose, the result stands). Pipe/`;`: `scan` finds it. `cobalt_brain`: rejected by the literal test. Each stays on the G2 line, which comes first (856). Controls are green on BASE and the card says so; each is paired with the red seat | OK |
| 4d | where the card proves the approval | from the working-tree prompt and the working-tree `cto-<date>.md` only; no committed proof (draft DECISION 2). `G5` fence for `brain` (`bare-guard.py:926-931`) lets the brain write `reports/` and `prompts/20*/`, so a ruled-or-not brain seat can write a `RULINGS:` line into its own prompt, or a row into a `cto-<date>.md`, and the guard accepts it | FAIL |
| 5a | commands the build runs | `uv run pytest -q -p no:cacheprovider …` and `uv run cobalt jobs restarts <BASE>..HEAD` are `BUILD-HUB.md` line 12 allow entries (`Bash(uv run pytest *)`, `Bash(uv run cobalt jobs restarts *)`); no new command, no `ops/desk` script | OK |
| 5b | files | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` only; `desk-launch.sh`, `gate-lists.md`, settings fenced in `## NOT IN THIS JOB` | OK |
| 5c | K10 RESTARTS home | in `## RECORDS`: hook (operator, no resident), test, DOCS; expected `RESTARTS: none` | OK |
| 5d | hook file and install | stated in `## RECORDS`: repo file, user settings entry line 22 runs the main checkout, takes effect on the merge | OK |
| 6a | `grep -c -F "«FILL"` on the card | `0` | OK |
| 6b | `git diff --stat --` card and draft report; `git log -1 --format=%h --` each | diff empty; both `626c3ebb` | OK |

## ISSUES
- 3b FAIL: the header edit cites lines 20-21 and 36-37; the G2 entry is line 20 only and 36-37 is the test-env comment. Name line 20 (and 21 if the wording moves).
- 3c FAIL: R511 is line 20 of `cto-2026-10-06.md`, not 19 (card RECORDS and the draft report).
- 4d FAIL: the guard trusts files the brain seat itself may write (`bare-guard.py:926-931`). A brain seat can add `RULINGS: 2026-10-06 R511` to its own prompt (R511 does hold `production read`) and read production, or write its own `cto-<date>.md` row. The card needs a proof the seat cannot forge, for example: a prompt that is read-only to the seat (G5 denies a write to the seat's own prompt) and `reports/cto-*.md` rows read only if the file is not changed since HEAD (compare to `.git` objects without running a command), or a stated veto of the working-tree read by the desk. Add a control where the ruled seat edits its own prompt or row.

Not counted: X1 gap for the build to decide: `scan` does not flag an unquoted `$VAR`, `${…}`, brace or glob word, so a positional like `$X` or `{a,b}` is one word to `words()` but may expand to several in the shell (argparse then errors; no wider verb is reachable, since each option word is matched exactly). Cheap to close: refuse a positional holding an unquoted `$`, `{`, `*`, `?`, `~`.

PREFLIGHT DONE · card: guard-g2-21 · checks: 25 · fails: 3 · ready: NO
