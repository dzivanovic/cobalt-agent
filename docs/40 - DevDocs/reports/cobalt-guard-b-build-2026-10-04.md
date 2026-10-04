# cobalt-guard-b — build report 2026-10-04

## §0 Headline

- Built B1–B4 in `ops/desk/bare-guard.py`. `sort`, `cut`, `uniq` and `awk` can no longer read `.env`. `sort -o`/`--output`/`--compress-program`, a second `uniq` operand, and `awk -f` are now denied, both in a pipe and as a lone command.
- Tip `3c451126` on `979ec797`. Offline 3782/0, `tests/ops` 1277/0, live-note 146/0. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- Every new test failed on BASE for its row's reason and failed again when its fix was undone. A second fix commit pinned the ` < /dev/null` ending on a lone command.
- Decisions: none. One carried read sits in `## RECORDS`: B4 keys on the first word as typed.

## L74

A system reminder in this session (not a tool result) asked that commits end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 0 · 754394594c51760c8951e55d78e467c885d441e7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
RULING 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
RULING 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
RULING 2026-10-03 R33 row · grep -n "^| R33 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 39:| R33 | 11:08 ET | HIS RULING (via brain): read-only pipes allowed (each segment `grep`, `sed -n`, `cut`, `sort`, `uniq`, `head`, `tail`, `wc`, `awk`; no redirect, `&&`, `;`); amends 10-01 R45 part 1; card `10` Sunday ([words](cto-2026-10-03-words.md#r33)). | HIS RULING · APPROVED |
RULING 2026-10-03 R33 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R33 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · a09f08622ac8522adce99096f5af18faaed9e2ca
RULING 2026-10-03 R33 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

Mechanical rows: `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, output whole:

```
clock · date · 0 · Sun Oct  4 18:32:22 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cobalt-guard-b-1004
    ?? "docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 979ec797 Merge branch 'main' into deploy/set3b-1004
diff · git diff --stat 979ec797 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cobalt-guard-b-1004 · 0 · 979ec797 Merge branch 'main' into deploy/set3b-1004
env here · ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 979ec797` | 0 | `commit 979ec79706cb62726698922ce825f01e733b3732` · `Merge: ce213e11 34d9af1d` · `Merge branch 'main' into deploy/set3b-1004` · `docs/40 - DevDocs/reports/deploy-set3b-1004.md \| 116 +++` · `1 file changed, 116 insertions(+)` |
| symbol | `grep -n -F "ENV_READERS" ops/desk/bare-guard.py` | 0 | `74:ENV_READERS = ("cat", "grep", "sed", "head", "tail", "less")` · `545:        if verb(ws) in ENV_READERS and any(is_env(w) for w in ws[1:]):` |
| symbol | `grep -n -F "READ_FILTERS" ops/desk/bare-guard.py` | 0 | `73:READ_FILTERS = ("grep", "sed", "cut", "sort", "uniq", "head", "tail", "wc", "awk")` · `396:        if ws[0] not in READ_FILTERS:` |
| symbol | `grep -n -F "BLOCK = (" ops/desk/bare-guard.py` | 0 | `44:BLOCK = (` |
| callers | `grep -rn -F "awk_writes(" ops tests/ops` | 0 | `ops/desk/bare-guard.py:372:def awk_writes(args):` · `ops/desk/bare-guard.py:403:        if ws[0] == "awk" and awk_writes(ws[1:]):` |
| callers | `grep -rn -F "pipe_problems(" ops tests/ops` | 0 | `ops/desk/bare-guard.py:389:def pipe_problems(command, cuts):` · `ops/desk/bare-guard.py:420:        problems = pipe_problems(text, cuts)` |
| callers | `grep -rn -F "g3_bash(" ops tests/ops` | 0 | `ops/desk/bare-guard.py:543:def g3_bash(segs):` · `ops/desk/bare-guard.py:586:    deny = g3_bash(segs)` |
| callers | `grep -rn -F "sed_problem(" ops tests/ops` | 0 | `ops/desk/bare-guard.py:303:def sed_problem(args):` · `ops/desk/bare-guard.py:400:            p = sed_problem(ws[1:])` |
| callers | `grep -rn -F "g1(" ops/desk/bare-guard.py` | 0 | `408:def g1(command):` · `598:    deny = g1(command)` |
| symbol | `grep -n -F "def is_env(" ops/desk/bare-guard.py` | 0 | `533:def is_env(path):` |
| symbol | `grep -rn -F "ROUTE[" ops/desk/bare-guard.py` | 0 | 12 hits; G3 at `546:            return ROUTE["G3"]` and `707:        return ("G3", ROUTE["G3"], path) if is_env(path) else None` |
| test helpers | Grep `^def \|^G3_ROUTE` in `tests/ops/test_bare_guard.py` | — | `144:G3_ROUTE = (` · `223:def make_seat(` · `250:def call(` · `263:def run(` · `267:def assert_denied(` · `272:def assert_allowed(` · G11 tests at 356, 377 · G3 tests at 432–457 |
| wc | `wc -l ops/desk/bare-guard.py tests/ops/test_bare_guard.py` | 0 | `737 ops/desk/bare-guard.py` · `969 tests/ops/test_bare_guard.py` |
| READ tail | `tail -n 3 ".../reports/cobalt-guard-check-2026-10-04.md"` | 0 | last line: `CHECK DONE · job: cobalt-guard · pass: 1 · tip: a2e19ceb · house A: none (overruled 2026-10-02 R47) · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 3739/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 1` |
| READ tail | `tail -n 3 ".../reports/cobalt-guard-build-2026-10-04.md"` | 0 | last line: `BUILT · job: cobalt-guard · tip: 21b9e21f \| on a8d8a848 \| migration: none \| offline 3739/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 11 of 11 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0` |
| RESTARTS | `uv run cobalt jobs restarts 979ec797..HEAD` | 0 | `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	A	DOCS	-` · `RESTARTS: none` (no commit in the range; the tool lists the untracked report) |

READ, as read: check report O4 (`check-…:99-117`, 4 ids), O5 (`:119-137`, 5 ids, test text quoted in the card), `## DECISIONS` 1 (O4) and 2 (O5, FOR DEJAN); build report `## DECISIONS` 1 (`awk -f <file>` runs a program G11 cannot read).

Card `## RECORDS`, copied: (1) his 2026-10-03 R33 carried in its read-only intent; B1–B4 narrow its wording; on his veto list (desk rows R241, R247, R248). (2) RESTARTS class home: `ops/desk/bare-guard.py` → `M operator script; no Cobalt reader -`; `tests/ops/test_bare_guard.py` → `M test/documentation; no resident -`; the report → `A DOCS -`; expected `RESTARTS: none`. (3) `cobalt-guard` ships at `a2e19ceb`; BASE is main after set 3 deployed. (4) The four read strings stay off every session line until this card ships. (5) judge 2026-10-04: D1 CHANGE (B2 by form), D2 CHANGE (B4), D3 KEEP — desk row R254. Re-read: (2) the report row re-read by the RESTARTS run above; (3) `git -C /Users/cobalt/cobalt log` not run for `a2e19ceb`; the CHECK DONE line above names `tip: a2e19ceb`.

Card header `DB: none`: no lock probe, no with-DB red; W is (a0), (a), (e).

## E0 BASELINE

On `979ec797`, before any edit.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 594.11s (0:09:54)`, exit 0. Last skip line: `SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` (offline run; the live-note run below covers it).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.49s`, exit 0. Its one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED

Tests written in `tests/ops/test_bare_guard.py` (no `src/` or `ops/` edit), committed `82c5c7a2 wip(cobalt-guard-b): red — B1–B4 tests on BASE`.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py -k "check_guard_o4 or check_guard_o5 or b2_ or b3_ or b4_"` → `18 failed, 10 passed, 443 deselected, 15 warnings in 1.54s`; progress `FFFFFFFFFFFFF.......F.FFFF..`.
- B1 `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied` (5 ids, restored as the check report O5 wrote it): each `test_bare_guard.py:268: AssertionError: (0, '')` / `assert 0 == 2`. That is the row's reason: each command is allowed on BASE.
- B2 `test_check_guard_o4_a_filter_that_writes_or_runs_is_denied` (the check's 4 ids plus `sort -uo out`, `sort -oout`, `sort --out=x`, `sort --compress=sh`, each after `grep X f |`): 8 × `test_bare_guard.py:1017` `assert 0 == 2`. Controls `test_b2_a_sort_or_uniq_that_only_reads_stays_allowed` (7 ids: the card's 4 `grep X f | sort -u`, `sort -k2,2n f`, `sort --unique f`, `grep X f | uniq -c`, plus `grep X f | uniq -f 1 -`, `uniq -f 1 f`, `uniq -s2 -w3 f`) PASS.
- B3 `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied`: `test_bare_guard.py:1039` `assert 0 == 2`. Control `test_b3_an_awk_program_in_the_command_stays_allowed` PASSES.
- B4 `test_b4_a_lone_sort_uniq_or_awk_that_writes_is_denied` (4 ids: `sort -o out f`, `uniq f out`, `awk -f p.awk f`, `awk '{print > "x"}' f`): 4 × `test_bare_guard.py:1061` `assert 0 == 2`. Controls `test_b4_a_lone_sort_or_awk_that_only_reads_stays_allowed` (`sort f`, `awk '{print $1}' f`) PASS.

No RUN row. No with-DB red (DB: none).

## E3 THE ROWS

All in `ops/desk/bare-guard.py`. The rows were built in order, each followed by a run of `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py`:
- B1: `ENV_READERS` += `sort cut uniq awk` → `13 failed, 458 passed` (o5 green; the 13 reds are B2–B4's).
- B2 + B3: `sort_writes` (a short-option word holding `o`; a long name that is a prefix of `output`, or starts `com` and is a prefix of `compress-program`), `uniq_writes` (a second operand; the word after a short option ending `f`/`s`/`w` is a value; `-` is an operand; `--` ends options), `awk_file` (`-f…`, `--file`, `--file=…` before `--`; the values of `-F`/`-v` are skipped), and `filter_problem`, called from `pipe_problems` in place of the bare G11 call → `4 failed, 467 passed` (only B4's reds remain).
- B4: in `g1`, a command with nothing found (a lone command) runs `filter_problem` on its words; a hit → the resend sentence → `471 passed`.

THE MUTATIONS (Edit tool; each undone, then `git diff --stat` → `ops/desk/bare-guard.py | 74 +++…` `1 file changed, 70 insertions(+), 4 deletions(-)`, the fix):
- M1 (B1): `ENV_READERS` back to `("cat", "grep", "sed", "head", "tail", "less")`; `-k check_guard_o5` → `5 failed, 466 deselected`; first: `test_bare_guard.py:268: AssertionError: (0, '')`.
- M2 (B2): `if False and` in front of the sort and uniq checks of `filter_problem`; `-k "check_guard_o4 or b2_"` → `8 failed, 7 passed`; first: `test_bare_guard.py:1017: AssertionError:` `assert 0 == 2`.
- M2c (B2 negative controls): `sort_writes` denies every short option (`elif a.startswith("-"):`) and `uniq_writes` skips no option value (`pass` for `i += 1`); `-k b2_` → `4 failed, 3 passed`; first: `test_bare_guard.py:273: AssertionError: NOT A REFUSAL. … contains `sort` with `-o`, `--output` or `--compress-program`. …` `assert 2 == 0`. The 4 reds: `grep X f | sort -u`, `sort -k2,2n f`, `grep X f | uniq -f 1 -`, `uniq -f 1 f`. (`uniq -s2 -w3 f` stays green under it: attached digits never take the next word.)
- M3 (B3): `if False and awk_file(...)`; `-k b3_` → `1 failed, 1 passed`; first: `test_bare_guard.py:1039: AssertionError:` `assert 0 == 2`.
- M4 (B4): `p = None` in place of `filter_problem(ws)` in `g1`; `-k b4_` → `4 failed, 2 passed`; first: `test_bare_guard.py:1061: AssertionError:` `assert 0 == 2`.

After the mutations: the line wrapped and the header comment given B1–B4; `471 passed`. Committed `87576deb fix(cobalt-guard-b): read-only filters stay read-only; sort cut uniq awk read no .env (B1-B4, L1 L3 L72)`.

SECOND FIX COMMIT (self-check 2 found an entry path no test pinned: a lone command ending ` < /dev/null`, which `g1` strips before the B4 path). Added the id `sort -o out f < /dev/null` to the B4 test. Under M4 → `5 failed, 2 passed`, the new id among them (`test_bare_guard.py:1063` `assert 0 == 2`); undone, `git diff --stat` → `tests/ops/test_bare_guard.py | 2 ++`; `472 passed`. Committed `3c451126 fix(cobalt-guard-b): pin the house-probe ending on a lone sort (B4, K25 2)`. RESTARTS and W ran again on it (one more gate pair, `## RECORDS`).

DevDocs line: `ops/desk/bare-guard.py` has no page under `docs/40 - DevDocs/cobalt/` (`Grep bare-guard` over `docs/40 - DevDocs` → reports and prompts only), and the card fences every file but its two (`## NOT IN THIS JOB`). No line written; see `## RECORDS`.

## RESTARTS

`uv run cobalt jobs restarts 979ec797..HEAD` at `3c451126`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. The same table at `87576deb`. Matches the card's class home.

## W THE THREE SUITES

`<tip>` = `3c451126`. (a0) `git diff --name-only --no-renames 979ec797` → `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.

- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, verdict `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-190004.log`; executed `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (log line 2) → `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 595.98s (0:09:55)` (log line 828).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, verdict `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-190005.log`; executed `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`; `146 passed, 1 skipped, 15 warnings in 28.58s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1277 passed, 1 xfailed, 15 warnings in 347.65s (0:05:47)`, exit 0. The tests this build adds, all in this run: `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied` (5), `test_check_guard_o4_a_filter_that_writes_or_runs_is_denied` (8), `test_b2_a_sort_or_uniq_that_only_reads_stays_allowed` (7), `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied`, `test_b3_an_awk_program_in_the_command_stays_allowed`, `test_b4_a_lone_sort_uniq_or_awk_that_writes_is_denied` (5), `test_b4_a_lone_sort_or_awk_that_only_reads_stays_allowed` (2).
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (19:10 ET).

## PRE-STOP SELF-CHECK

(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." Evidence: o5 red at E2 (`:268` `assert 0 == 2`) and under M1; o4 red at E2 (`:1017`) and under M2; the b2 controls red under M2c (4 of 7; `uniq -s2 -w3 f` is not reachable by that mutation, named above); b3 red at E2 (`:1039`) and under M3, its control green throughout; b4 red at E2 (`:1061`) and under M4, including the added probe-ending id (`:1063`); b4 controls green. No test stayed green under its row's mutation.
(2) "Every entry path of each rule pinned by a test." Callers at tip: `grep -n -F "filter_problem(" ops/desk/bare-guard.py` → `441:def filter_problem(ws):` · `469:        p = filter_problem(ws)` (pipe_problems: pinned by o4, b3) · `487:        p = filter_problem(ws) if ws else None` (g1 lone: pinned by b4, including the ` < /dev/null` ending). `grep -n -F "ENV_READERS"` → `76:` · `615:        if verb(ws) in ENV_READERS …` (g3_bash: pinned by o5 as a single command and as a pipe segment). `grep -n -F "awk_file("` → `394:` def · `448:` (pinned by b3 `-f`, `-fp.awk`, `--file=p.awk`, `--file p.awk`, and b4 lone). `grep -n -F "_writes("` → `409:def sort_writes` · `425:def uniq_writes` · `443:` / `445:` / `450:` the calls in `filter_problem`. Flag combinations pinned: clustered `-uo`, attached `-oout`, abbreviated `--out=x` / `--compress=sh`, uniq values `-f 1`, `-s2 -w3`, `-` as an operand. Seat kinds: the new rules are kind-free like G1/G3, and the tests use the build seat, as the check's O4/O5 tests do.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." The greps above were re-run at the tip; RESTARTS ran at `3c451126`; the commit list is from `git log --oneline 979ec797..HEAD`. The E2/E3 test-file lines (`:268`, `:1017`, `:1039`, `:1061`, `:1063`) are quoted from the runs that printed them.

## FOR THE CHECK

`979ec797..3c451126`:
- `82c5c7a2 wip(cobalt-guard-b): red — B1–B4 tests on BASE`
- `87576deb fix(cobalt-guard-b): read-only filters stay read-only; sort cut uniq awk read no .env (B1-B4, L1 L3 L72)`
- `3c451126 fix(cobalt-guard-b): pin the house-probe ending on a lone sort (B4, K25 2)`

The per-row reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`; the caller greps are in `## PRE-STOP SELF-CHECK` (2) and PREFLIGHT; RESTARTS is above. No RUN row. With-DB suite: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none). The records copied at PREFLIGHT are in `## PREFLIGHT`.

Points for the check to weigh (the card's own words, not decisions): B2's `o`-in-a-short-option rule over-denies `sort -t o …` (the card accepts this). Like a pipe segment, B4 keys on the first word as typed (`ws[0]`), so a lone `/usr/bin/sort -o out f` or `LC_ALL=C sort -o out f` does not meet B4. A pipe segment of that shape is already denied as "not a read-only filter". See `## RECORDS`.

## CONTINUE

next: none (built). The desk verifies the artifact and launches the check (`CHECK-HUB.md`).

## DECISIONS

none

## RECORDS
- L74: a system reminder asked for a `Claude-Session:` line in commits; recorded once under `## L74`, not acted on.
- Extra gate pair: W ran twice (`87576deb`: `offline 3782/0` log `/Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-184917.log`, `live-note 146/0` log `/Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-184918.log`, `tests/ops` `1276 passed, 1 xfailed`), then again on `3c451126` after the second fix commit (self-check 2).
- A `tests/ops` run was started after B4 (`uv run pytest … tests/ops`, moved to the background at its 120 s timeout) and was still running while the E3 mutations were applied. Its exit-0 result is not evidence for any tree and is not cited; `tests/ops` was rerun at each tip.
- No DevDocs line: `ops/desk/bare-guard.py` has no module page under `docs/40 - DevDocs/cobalt/`, and the card fences every file but its two.
- Carried read, not a rule of this card (like the check's `$VAR` and `grep -r` reads, which stay open): B4 keys on the first word as typed, as a pipe segment does, so a lone `sort`/`uniq`/`awk` written by path or behind `NAME=` does not meet it. The allow strings waiting for him (`Bash(sort *)` and the rest) match only the bare verb.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cobalt-guard-b · tip: 3c451126 | on 979ec797 | migration: none | offline 3782/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
