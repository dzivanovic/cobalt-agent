# guard-g2-open-reads-1008 — build report (2026-10-08)

## §0 Headline
- G2 now passes the one production read (`COBALT_ENV=production uv run cobalt db query --prod --side user|system …`) for every seat, no stamp (O1, his R686); every other production string stays denied.
- G3 now refuses `~/.cobalt_key`, `data/.cobalt_vault` and `security find-*-password`/`dump-keychain`/`export` for every seat, deploy and unknown too, by Bash and the Read tool (O2).
- desk-launch.sh: comments only (O3). Tip `773f39e7`; offline 3991/0, live-note 146/0, `tests/ops` 1918/0; DB: none; RESTARTS: none.
- One decision: D1, a `security` option before its subcommand is not refused (unproven, built as the card says).

## L74
A system reminder (not a tool result) asked commits to carry a `Claude-Session:` line, 11:39 ET. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` · exit 0 · 11:39 ET, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 0 · de7b573e420ae20d746db053110689303476e102
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing; brain relay then his own message): every seat may run read-only production reads, no stamp; production writes and secrets stay refused. bare-guard G2 changes by card `120` (drafter prompt `119`). | APPROVED · HIS RULING |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0, output whole:

```
clock · date · 0 · Thu Oct  8 11:40:11 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/guard-g2-open-reads-1008
    ?? "docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4125ff02 docs(desk): R686 his ruling open production reads, guard-g2 drafter prompt 119
diff · git diff --stat 4125ff02 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/guard-g2-open-reads-1008 · 0 · 4125ff02 docs(desk): R686 his ruling open production reads, guard-g2 drafter prompt 119
env here · ls /Users/cobalt/cobalt-wt/guard-g2-open-reads-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 4125ff02` | 0 | `docs(desk): R686 his ruling open production reads, guard-g2 drafter prompt 119` · 3 files changed, 12 insertions(+) (119-draft prompt, cto-2026-10-08-words.md, cto-2026-10-08.md) |
| caller | `grep -rn -F "marked_read(" ops tests src` | 0 | `ops/desk/bare-guard.py:854:def marked_read(command, s):` · `ops/desk/bare-guard.py:904:    if kind is not None and kind != "deploy" and PROD.search(command) and not marked_read(command, s):` |
| caller | `grep -rn -F "is_env(" ops tests src` | 0 | `bare-guard.py:783:def is_env(path):` · `:807: if verb(ws) in ENV_READERS and any(is_env(w) for w in env_words(ws[1:])):` · `:1022: return ("G3", ROUTE["G3"], path) if is_env(path) else None` |
| caller | `grep -rn -F "g3_bash(" ops tests src` | 0 | `bare-guard.py:805:def g3_bash(segs):` · `:901: deny = g3_bash(segs)` |
| symbol | `grep -n -F "MARKER" ops/desk/bare-guard.py` | 0 | `849:MARKER = re.compile(r" PROD-READ: 20\d\d-\d\d-\d\d R\d+")` · `863: if not MARKER.search(s["first"]):` |
| symbol | `grep -n -F 's["first"]' ops/desk/bare-guard.py` | 0 | `863:    if not MARKER.search(s["first"]):` (the only reader) |
| symbol | `grep -n -E "^(REFUSED_WORDS\|REFUSED_FUNCTIONS\|def guard_select\|def read_rows)\|BEGIN READ ONLY\|autocommit = False\|conn.rollback" src/cobalt/db_query.py` | 0 | `20:REFUSED_WORDS` · `25:REFUSED_FUNCTIONS` · `98:def guard_select` · `145:def read_rows` · `161: conn.autocommit = False` · `163: conn.execute("BEGIN READ ONLY")` · `177: conn.rollback()` |
| symbol | `grep -n -F ".cobalt_vault" src/cobalt_agent/skills/research/finviz_extractor.py` | 0 | `70: def __init__(self, vault_path: str = "data/.cobalt_vault"):` · `735: vault_path: str = "data/.cobalt_vault",` |
| READ | the Read tool on bare-guard.py 1-1088, test_bare_guard.py 1-620, desk-launch.sh 100-119 and 500-546 | — | every `file:line` of the card matches BASE (G2 call 904, marked_read 854-891, MARKER 849, PROD 107, ROUTE 56-71, ENV_READERS 82, is_env 783-790, g3_bash 805-812, Read rule 1022; tests 143, 223, 272, 277, 389-406, 446-549, 554-576; desk-launch.sh 115-116, 504-510 comment) |
| wc | `wc -l ops/desk/bare-guard.py tests/ops/test_bare_guard.py ops/desk/desk-launch.sh` | 0 | 1087 · 1398 · 1223 · 3708 total |
| tail | `tail -n 3 "docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md"` | 0 | last line: `- The guard never runs a command (\`bare-guard.py:5\`): it cannot run \`git\`; the commit proof is the launcher's (R1), the guard's proof is the marker (R2).` |
| RESTARTS | `uv run cobalt jobs restarts 4125ff02..HEAD` | 0 | one row, the untracked report (`DOCS`, `-`); `RESTARTS: none` |
| record | `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` | 1 | nothing (as the card records) |
| record | `grep -n -F "cobalt db query" /Users/cobalt/.claude/settings.json` | 0 | `53: "Bash(uv run cobalt db query *)",` · `54: "Bash(COBALT_ENV=production uv run cobalt db query *)"` |
| record | `grep -n -F "bare-guard.py" /Users/cobalt/.claude/settings.json` | 0 | `22: "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"` |

Card RECORDS copied (desk facts): READ-ONLY (`db_query.py` 20, 25-28, 98, 145, 161, 163, 176-177 — line numbers re-read above); DB SECRETS (his R686: no secret in the production DB); desk-launch.sh stamp kept for prompts in flight; RESTARTS classes (re-read: nothing under `ops/desk` in jobs.yaml); WHERE IT RUNS (settings.json:22 re-read); G2 keeps refusing a non-production read naming a PROD word; BASE `4125ff02` (re-read by preflight); the desk deploys by its own card.
DB: none → no lock probe, no with-DB string proven here.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 636.51s (0:10:36)` · exit 0 · 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.95s` · the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only (`tests/ops/test_bare_guard.py`), no `src/` or `ops/` edit. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py` on BASE code → `140 failed, 790 passed, 15 warnings in 30.38s`.

| red | tests | count | first line on BASE |
|---|---|---|---|
| RED (1) + (4) | `test_g2_every_seat_runs_a_production_db_query_without_the_stamp` over `UNSTAMPED_SEATS` (build, check, devfix, desk, brain via `make_seat`; worker via `marked_seat(where="none")`; plus card 21's former control (a) as `where` = none, later, body × brain, worker, desk) × `PROD_READS` | 15 × 3 = 45 | `E AssertionError: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev` at `test_bare_guard.py:273` (`assert_allowed`, exit 2 with G2_ROUTE) |
| CONTROL (e) unstamped | `test_g2_a_marked_query_with_a_separator_is_g1s_to_deny` on the 6 unstamped kinds × 3 tails | 18 | `E AssertionError: route: production is the deploy hub's; …` at `:538` (`assert G2_ROUTE not in line`): on BASE G2 denied before G1. The stamped seat's 3 cases passed |
| RED (3) | `test_g3_a_read_of_a_secret_is_denied_from_every_seat` (9 commands × 7 `KINDS`) and `test_g3_the_read_tool_on_a_secret_is_denied` (2 paths × 7) | 63 + 14 = 77 | `E AssertionError: (0, '')` at `:268` (`assert_denied`, exit 0 on BASE) |

45 + 18 + 77 = 140. Every CONTROL passed on BASE: `MARKED_DENIED` (now with `db apply`, `validate`, `uv run cobalt_brain`, `uv run python -c`) on the stamped seat and the 6 unstamped kinds; line-continuation, mid-word-hash, brace-word, `--allow-prod`, brace-side on the same 7 seats; `PROD_CALLS` denied on 6 kinds (worker added); deploy and unknown allowed (403-406, unchanged); `test_g2_a_marked_seat_runs_a_production_db_query` unchanged; `ENV_READS`, the `.env` Read tool keep `G3_ROUTE`; `ls -la` on both secrets, `cat /x/.cobalt_key.example`, `security list-keychains` allowed on 7 kinds.
Commit `d3b598df wip(guard-g2-open-reads-1008): red — every seat reads production without the stamp; secrets refused for every seat (O1 O2 O3)`.

## E3 THE ROWS
- O1 `ops/desk/bare-guard.py`: `marked_read(command, s)` → `prod_read(command)`; test (i) and `MARKER` deleted; every other line of the function unchanged; the G2 call `... and PROD.search(command) and not prod_read(command):`; header lines 20-21 and the comment/docstring cite R686. `uv run pytest -q -p no:cacheprovider --color=no --tb=line -k g2 tests/ops/test_bare_guard.py` → `313 passed, 617 deselected`.
- O2 `ops/desk/bare-guard.py`: `ROUTE["G3 secret"]` (card text), `SECRETS`, `KEYCHAIN_READS`, `is_secret(path)`, `keychain_read(ws)`; `g3_bash` tests `is_secret` (a `.env` hit keeps `ROUTE["G3"]`) and `keychain_read`; the Read rule returns `ROUTE["G3"]` for `.env`, `ROUTE["G3 secret"]` for a secret. Header `G3 .env read` → `G3 .env or secret read`.
- O3 `ops/desk/desk-launch.sh`: `git diff -U0 ops/desk/desk-launch.sh` → two hunks, every changed line starts with `#` after its indent (116 → 116-117; 507 → 508).
- `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py tests/ops/test_desk_launch_prechecks.py` → `1055 passed, 15 warnings in 79.17s`. `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `1918 passed, 1 xfailed, 15 warnings in 473.95s (0:07:53)`. `test_desk_launch_prechecks.py` unedited.

MUTATIONS (Edit tool, each undone with Edit before the next; `git diff --stat` after the last → only the fix: `bare-guard.py | 56`, `desk-launch.sh | 5`; `grep MUTATION` → 0):

| row | mutation | run | result | first failing |
|---|---|---|---|---|
| O1 | undo the fix: G2 call `not (prod_read(command) and " PROD-READ: " in s["first"])` | `-x --tb=line -k g2` | `1 failed, 44 passed` | `test_g2_every_seat_runs_a_production_db_query_without_the_stamp[build-None-…]`: `route: production is the deploy hub's; …` |
| O1 | drop the leading-shape test | `-k anything_but_the_one_query_shape` | `35 failed, 112 passed` | `[COBALT_ENV=production uv run cobalt db migrate --prod-stamped]` (and dev-rebuild, the doubled assignment, `NAME=x`, `env` × 7 seats) |
| O1 | drop the exactly-one-`--prod` test | `-x --tb=line -k anything_but_the_one_query_shape` | `1 failed, 56 passed` | `[COBALT_ENV=production uv run cobalt db query --side user "SELECT 1"-stamped]`: `AssertionError: (0, '')` |
| O1 | drop the `--side` test | same | `1 failed, 21 passed` | `[… --prod --side admin "SELECT 1"-stamped]`: `(0, '')` |
| O1 | drop the brace test | `-k "brace_word or brace_word_cannot_hide"` | `21 failed, 4 passed` | `--pro{d,}`, `cobalt_b{r,}ain`, `{--side,admin}` × 7 seats |
| O1 | drop the other-option test | `-k allow_prod_does_not_pass` | `7 failed` | `test_g2_allow_prod_does_not_pass_for_a_marked_seat[stamped]` … `[worker]` |
| O1 | drop the no-other-PROD-word test | `-k anything_but_the_one_query_shape` | `14 failed, 133 passed` | `[… "SELECT cobalt_brain"-stamped]` and `"SELECT '--prod'"` × 7 |
| O1 | drop the `shlex` equality test | `-k mid_word_hash` | `14 failed` | `[stamped-… "SELECT 1"#cobalt_brain]`, `x# --prod` × 7 |
| O2 | drop `.cobalt_key` | `-k secret` | `35 failed, 70 passed` | `cat ~/.cobalt_key`, `/Users/cobalt/.cobalt_key`, `.cobalt_ke{y,}`, `head -c 72`, Read tool × 7 kinds |
| O2 | drop `.cobalt_vault` | `-k secret` | `21 failed, 84 passed` | the two `.cobalt_vault` reads and the Read tool × 7 |
| O2 | drop the `security` test | `-x --tb=line -k "secret and security"` | `1 failed` | `[security find-generic-password -w -s cobalt-build]`: `(0, '')` |
| O2 | drop `is_secret` from the Read rule | `-k "secret or read_tool"` | `14 failed, 100 passed` | `test_g3_the_read_tool_on_a_secret_is_denied` × 2 paths × 7 |

No named test stayed green under its mutation; none rewritten.
Commit `773f39e7 feat(guard-g2-open-reads-1008): G2 passes the one production db query read for every seat, no stamp; G3 refuses ~/.cobalt_key, data/.cobalt_vault and a keychain dump for every seat (O1 O2 O3, L1 L3 L72 L77)`.
DevDocs: no page under `docs/40 - DevDocs/cobalt/` documents `ops/desk/bare-guard.py` or `desk-launch.sh` (Grep `bare-guard|desk-launch` there → only `jobs/restarts.md`, a mention); the precedent build `ce19a3fd` wrote none. None written (RECORDS).

## RESTARTS
`uv run cobalt jobs restarts 4125ff02..HEAD`:

```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `773f39e7`.
- (a0) `git diff --name-only --no-renames 4125ff02` → `ops/desk/bare-guard.py` · `ops/desk/desk-launch.sh` · `tests/ops/test_bare_guard.py` (the report was untracked then); every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-open-reads-1008 offline` · exit 0 → `offline 3991/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-open-reads-1008-offline-20261008-120536.log`. This build adds no test to that suite (its tests are in `tests/ops`, below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-open-reads-1008 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-open-reads-1008-livenote-20261008-120539.log`; `grep -n -F "SKIPPED" <log>` → `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` at tip → `1918 passed, 1 xfailed, 15 warnings in 479.41s (0:07:59)`, no SKIPPED line. The tests this build adds or changes: `test_g2_every_seat_runs_a_production_db_query_without_the_stamp`, `test_g3_a_read_of_a_secret_is_denied_from_every_seat`, `test_g3_the_read_tool_on_a_secret_is_denied`, `test_g3_a_secret_shown_present_or_a_near_name_is_allowed`; widened to seats: `test_g2_production_from_a_non_deploy_seat_is_denied`, `test_g2_a_marked_seat_is_denied_anything_but_the_one_query_shape`, `test_g2_a_marked_query_with_a_separator_is_g1s_to_deny`, the line-continuation, mid-word-hash, brace-word, `--allow-prod` and brace-side tests; removed (folded into the first): `test_g2_a_seat_without_the_marker_in_its_first_record_is_denied`.
- with-DB: not run (DB: none). (b)-(d), (f): not run (DB: none). `.env`: never present (preflight: `No such file or directory`).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: RED (1)/(4) 45 and CONTROL (e) unstamped 18 and RED (3) 77 red on BASE (E2, 140 failed, first lines quoted); every control turned red under a named mutation (E3 table: leading shape 35, one `--prod` 1 (-x), `--side` 1 (-x), brace 21, other option 7, other PROD word 14, shlex 14, `.cobalt_key` 35, `.cobalt_vault` 21, `security` 1 (-x), Read rule 14). The negative controls `ls -la` on the secrets, `cat /x/.cobalt_key.example`, `security list-keychains` stayed green under every mutation, as controls should; `test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed` and `test_g2_a_marked_seat_runs_a_production_db_query` are unchanged tests, green on BASE and tip. None rewritten.
(2) Every entry path pinned: `prod_read` has one caller (`bare-guard.py:926`, the G2 call) — pinned by RED (1) for 6 kinds and the controls on 7 seats, deploy/unknown by 403-406; `is_secret` callers `:829` (g3_bash, Bash — `SECRET_READS` × 7 kinds, including a brace word) and `:1046` (Read rule — `test_g3_the_read_tool_on_a_secret_is_denied` × 7); `keychain_read` caller `:832` — the three `security` reads × 7 kinds and `security list-keychains`. The `.env` route of both callers stays pinned by `test_g3_a_read_of_env_is_denied_from_every_seat` and `test_g3_the_read_tool_on_env_is_denied` (green at tip). `export` of `KEYCHAIN_READS` has no test of its own (the card's RED (3) list names none): DECISIONS D1 notes it with the option-first spelling.
(3) Re-read at tip: `grep -rn -F "prod_read(" ops tests src` → 878, 926; `grep -rn -F "is_secret(" ops tests src` → 802, 829, 1046; `grep -n -F "keychain_read(" ops/desk/bare-guard.py` → 807, 832; `grep -rn -F "marked_read" ops tests src` → nothing; `git log --oneline 4125ff02..HEAD` → the two commits below; the RESTARTS table and the gate lines are copied from their tool output above.

## FOR THE CHECK
- Range `4125ff02..773f39e7`: `d3b598df wip(guard-g2-open-reads-1008): red — …` · `773f39e7 feat(guard-g2-open-reads-1008): G2 passes the one production db query read for every seat, no stamp; G3 refuses ~/.cobalt_key, data/.cobalt_vault and a keychain dump for every seat (O1 O2 O3, L1 L3 L72 L77)`.
- Per row: reds in `## E2 RED`, mutations in `## E3 THE ROWS`, greens: `-k g2` 313 passed (O1); `tests/ops/test_bare_guard.py tests/ops/test_desk_launch_prechecks.py` 1055 passed (O1-O3); `tests/ops` 1918 passed, 1 xfailed (twice: before the commit and at tip).
- Caller greps: `## PREFLIGHT` (BASE) and PRE-STOP (3) (tip).
- RUN rows: none in this card.
- Suites: offline 3991/0, live-note 146/0 (commands and logs in `## W`); with-DB `not run (DB: none)`; `<F0>`/`<F1>`/`<F2>` `not run (DB: none)`; lock taken/released `not run (DB: none)`.
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- O3's diff: `git diff 4125ff02 -- ops/desk/desk-launch.sh` — lines 116-117 and 508, comments only.
- The build seat's own calls ran the main checkout's guard (card RECORDS, WHERE IT RUNS): a `-k` selector holding the word `cobalt_brain` was refused by G2 during the E3 mutations (RECORDS); the check meets the same.

## CONTINUE
next: none — BUILT (the desk verifies the artifact and launches the check)

## DECISIONS
- D1 ASK DESK (UNPROVEN, L70; not run): `keychain_read` reads the word right after `security`, as row O2 states. A spelling with a global option first (`security -q find-generic-password -w`, `security -v dump-keychain`) or `security -i` (interactive) is not that shape, so by reading the code it passes G3; and `export` has no test of its own. The card's X3 asks the check the keychain question. Safe default taken: built exactly the card's text, widened nothing.

## RECORDS
- L74: a system reminder at 11:39 ET asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- REFUSED, not needed: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -k "anything_but_the_one_query_shape and SELECT and cobalt_brain" tests/ops/test_bare_guard.py` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. Resent with `-k anything_but_the_one_query_shape` (the main checkout's G2 reads `cobalt_brain` in a selector as a production word; card RECORDS: it stays so).
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` holds `ops/desk/bare-guard.py` or `desk-launch.sh`; the precedent build `ce19a3fd` wrote none; none written.
- Card records re-read at PREFLIGHT: `ops/desk` absent from `configs/cobalt/jobs.yaml`; `settings.json:53-54` allow `uv run cobalt db query *` and `COBALT_ENV=production uv run cobalt db query *`; `settings.json:22` runs the main checkout's `bare-guard.py`; `db_query.py` 20, 25, 98, 145, 161, 163, 177.
- No extra lock take; `.env` never in this worktree.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: guard-g2-open-reads-1008 · tip: 773f39e7 | on 4125ff02 | migration: none | offline 3991/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 215263
