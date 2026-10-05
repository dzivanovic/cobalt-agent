# cobalt-guard-b — build report 2026-10-04

## §0 Headline

- Built in order: B1–B4, then B7 B8 (`8e68decd`), then B9 B10 (`c74edcd3`). On CONTINUE: E2 (20:06 ET), B11 was added, from his ruling 10-04 R283. G1's pipe list drops `awk`, and an awk pipe segment is denied with the resend sentence. G11's and B3's sentences stay beside it.
- Tip `3ecdd3dc` on `979ec797`. Offline 3782/0, `tests/ops` 1334/0, live-note 146/0. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- Every B11 red was red on `c74edcd3` for the row's reason, and every test was red under a mutation. Earlier controls that asserted an awk pipe is allowed now assert B11's deny. Every other test is green.
- Decisions: 4, none for Dejan. (1) Three B7/B8 ids were already green. (2) B9 yields to G11 where both deny. (3) B10 only adds denies. (4) R283 reverses the earlier awk-pipe controls, and they were rewritten as B11 pins.

## L74

A system reminder in this session (not a tool result) asked that commits end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74). The same request came again at each CONTINUE: E2 resume, the 20:06 ET one included. It was handled the same way each time.

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

### E2, second pass: B7 B8 (CONTINUE: E2, 19:27 ET)

The card, re-authorized at `14dbcd51` (`authorize.sh` → `AUTHORIZED`), now carries B7 and B8 (judge 19:27, desk row R273). HEAD was `1f2c19a9` (the check's O1 fix). Tests added at the end of `tests/ops/test_bare_guard.py`, committed `1218375f wip(cobalt-guard-b): red — B7 B8 tests on 1f2c19a9`.

`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=no tests/ops/test_bare_guard.py -k "b7_ or b8_"` → `3 failed, 7 passed, 476 deselected`:
- FAILED `test_b7_a_two_letter_prefix_of_compress_program_is_denied[sort --co=sh f]` and `[sort --co sh f]`: `test_bare_guard.py:1088` `assert 0 == 2`. That is the row's reason (allowed on 1f2c19a9).
- FAILED `test_b8_an_option_value_naming_env_is_denied[sort --files0-from=.env]`: `test_bare_guard.py:268: AssertionError: (0, '')` `assert 0 == 2`. That is the row's reason.
- PASSED, contrary to the card's "each allowed on 1f2c19a9": `test_b7_…[sort --compress=sh f]` (B2(b)'s `com` rule already denies it), `test_b8_…[sort --files0-from .env]` (`.env` is a plain word, which G3 already tests), `test_b8_…[sort --files0-from=/x/wt/job/.env]` (`is_env` takes the basename of the whole word, `.env`). The ids are kept as the card writes them. Each is shown red under a mutation in E3. See `## DECISIONS` 1.
- Controls PASS: `test_b7_sort_check_stays_allowed[sort --check f]`, `[sort -c f]`; `test_b8_an_option_value_not_naming_env_stays_allowed[sort --key=2 f]`, `[grep -n --include=*.py X .]`.

### E2, third pass: B9 B10 (CONTINUE: E2, 19:48 ET)

The card, re-authorized at `37e1e2c7` (`authorize.sh` → `AUTHORIZED`), now carries B9 and B10 (judge 19:47, desk row R281). HEAD was `776d0a13` (the report commit on `8e68decd`). Tests added at the end of `tests/ops/test_bare_guard.py`, committed `67039e11 wip(cobalt-guard-b): red — B9 B10 tests on 8e68decd`.

`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py -k "b9_ or b10_"` → `29 failed, 9 passed, 486 deselected`:
- B9 `test_b9_an_awk_program_that_reads_a_file_it_names_is_denied`, 6 ids: the card's 3 (`awk 'BEGIN{while(getline l < ".env") print l}'`, `awk 'BEGIN{ARGV[1]=".e" "nv"; ARGC=2} {print}'`, `awk '@include "x"'`), plus `awk '@load "x"'`, `awk 'BEGIN{ARGC=1} {print}' f` and the pipe segment `grep X f | awk '{getline l < "y"; print l}'`. Each fails `test_bare_guard.py:268: AssertionError: (0, '')` `assert 0 == 2`. That is the row's reason: each is allowed on `8e68decd`.
- B10 `test_b10_a_wrapped_command_is_judged_as_the_command_it_runs`, 18 ids: the card's 5 (`time sort -o out f`, `nice -n 5 sort -o out f`, `env A=1 sort -o out f`, `command sort -o out f`, `xargs awk -f p.awk`), plus `time nice sort -o out f`, `timeout 5 sort -o out f`, `timeout -s KILL 5 uniq f out`, `stdbuf -oL sort -o out f`, `nohup uniq f out`, `/usr/bin/env -i A=1 /usr/bin/sort -o out f`, `xargs -0 -n 1 awk '{print > "x"}'`, and six where the command cannot be found (`time`, `xargs`, `timeout 5`, `env A=1`, `env -S 'sort -o out f'`, `nice --foo sort f`). Each fails `test_bare_guard.py:1158` `assert 0 == 2`.
- B10 `test_b10_every_guard_rule_judges_the_wrapped_command`, 5 ids: G3 `time cat /x/wt/job/.env`, `xargs sort --files0-from=.env`, `env A=1 awk 'BEGIN{getline l < "y"}'`; G4 `time git push`; G7 `nohup claude -p x`. Each fails `:268` `assert 0 == 2`.
- Controls PASS: `test_b9_an_awk_program_that_reads_only_its_operands_stays_allowed` (`awk '{print $1}' f`, `grep X f | awk '{print $1}'`); `test_b10_a_wrapped_read_stays_allowed` (`time sort f` (the card's), `nice -n 5 sort f`, `env A=1 sort -u f`, `timeout 5 grep -n X f`, `time -p wc -l f`); `test_b10_a_wrapper_in_a_pipe_stays_denied` (`grep X f | time sort`, `grep -l X f | xargs grep -n Y`, each still denied as "not a read-only filter"; see `## DECISIONS` 3).

### E2, fourth pass: B11 (CONTINUE: E2, 20:06 ET)

The card, re-authorized at `f4391a0a` (`authorize.sh` → `AUTHORIZED`; it now also proves RULINGS row 2026-10-03 R283, `| HIS RULING · APPROVED — pending fold |`), now carries B11. HEAD was `6a06a3ee` (the report commit on `c74edcd3`). The card says "allowed on 8e68decd"; `c74edcd3` left `READ_FILTERS` and `pipe_problems` as they were, so the reds ran on `c74edcd3`. Committed `4edae759 wip(cobalt-guard-b): red — B11 tests on c74edcd3`.

Added: `test_b11_an_awk_pipe_segment_is_denied` (the card's `grep X f | awk '{print $1}'`, plus `awk '{print $1}' f | head -1` and `grep X f | sort | awk 'NF > 1'`), `test_b11_g11_and_b3_stay_as_defence_on_an_awk_segment` (`grep X f | awk '{print > "f"}'` keeps G11's sentence, `grep X f | awk -f p.awk` keeps B3's, each beside B11's), and the control `test_b11_a_pipe_without_awk_stays_allowed` (the card's `grep X f | cut -f2`, plus `grep X f | sort -u | head -3`).
Earlier controls that his ruling R283 reverses were rewritten as B11 pins (`## DECISIONS` 4): card 10's `test_g11_any_other_awk_segment_stays_allowed` (6 ids × 2 seat kinds) became `test_b11_an_awk_segment_g11_passes_is_denied_as_no_filter`; B3's control `test_b3_an_awk_program_in_the_command_stays_allowed` became `test_b3_b11_an_awk_program_in_the_command_is_denied_as_no_filter`; B9's control lost its pipe id `grep X f | awk '{print $1}'` (it is the card's B11 red) and keeps the lone `awk '{print $1}' f`.

`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py -k "b11"` → `18 failed, 2 passed, 510 deselected, 15 warnings in 1.45s`:
- FAILED, each at `test_bare_guard.py:997` (`assert_resend`) or `:1203` with `assert 0 == 2` / `returncode=0`: the 12 rewritten card 10 ids, the B3 rewrite and the 3 `b11_an_awk_pipe_segment` ids. That is the row's reason: each awk pipe is allowed.
- FAILED at `:1001`, the 2 defence ids: `assert 'a pipe `|` with `awk`, not a read-only filter' in '`awk` with `system(`, `>` or `|` in its program'` (and `in '`awk -f`, a program the guard cannot read'`). They are denied, but not as B11 denies them.
- PASSED: `test_b11_a_pipe_without_awk_stays_allowed[grep X f | cut -f2]` and `[grep X f | sort -u | head -3]`.

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

### E3, second pass: B7 B8

Both rows are in `ops/desk/bare-guard.py`.
- B7: in `sort_writes`, `name.startswith("com") and …` became `len(name) >= 2 and "compress-program".startswith(name)`. Then `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py` → `1 failed, 485 passed`, and the one red is B8's `[sort --files0-from=.env]`.
- B8: new `env_words(args)` returns the operands plus the text after the first `=` of each `--name=value` word, plus the word after a bare `--files0-from`. `g3_bash` tests `is_env` over `env_words(ws[1:])`. The same run → `486 passed`.

THE MUTATIONS (Edit tool, each undone):
- M7 (undoes B7): back to `name.startswith("com")`. `-k b7_` → `2 failed, 3 passed`: `[sort --co=sh f]` and `[sort --co sh f]`, first `test_bare_guard.py:1088` `assert 0 == 2`.
- M7b (the compress clause off, `if False and …`): `-k b7_` → `3 failed, 2 passed`. `[sort --compress=sh f]` is now red too (`:1088`).
- M7c (control: any long name starting `c`): `-k b7_` → `1 failed, 4 passed`. FAILED `test_b7_sort_check_stays_allowed[sort --check f]` at `test_bare_guard.py:273`: `NOT A REFUSAL. … contains `sort` with `-o`, `--output` or `--compress-program`. …` `assert 2 == 0`. `[sort -c f]` cannot go red under a long-option mutation, because B2(a) (a short option holding `o`) governs it.
- M8 (undoes B8: both `env_words` branches `if False and …`): `-k b8_` → `1 failed, 4 passed`. Only `[sort --files0-from=.env]` fails (`:268` `assert 0 == 2`).
- M8b (B8 on, the plain-word test off: `out = []`): `-k b8_` → `5 passed`. B8 alone denies all three ids.
- M8c (both off: `out = []` and both branches `if False and …`): `-k b8_` → `3 failed, 2 passed`. All three ids are red (`:268` `assert 0 == 2`).
- M8d (control: every `--name=value` taken as `.env`): `-k b8_` → `2 failed, 3 passed`. FAILED `[sort --key=2 f]` and `[grep -n --include=*.py X .]` at `:273` with `route: .env is never read; …` `assert 2 == 0`.
After the mutations, `git diff` showed only the fix, and `tests/ops/test_bare_guard.py` → `486 passed`. Committed `8e68decd fix(cobalt-guard-b): --co is compress-program; G3 reads option values (B7 B8, L1 L72)`.

### E3, third pass: B9 B10

Both rows are in `ops/desk/bare-guard.py`.
- B9: `awk_writes`' word walk became `awk_program(args)` (the words that can be program text), used by `awk_writes` and by a new `awk_reads` (`AWK_READS = ("getline", "ARGV", "ARGC", "@include", "@load")`). `g3_bash` denies with `ROUTE["G3"]` when `verb(ws) == "awk" and awk_reads(ws[1:])`. The first run, `uv run pytest -q -p no:cacheprovider --color=no --tb=no tests/ops/test_bare_guard.py`, gave `24 failed, 500 passed`: the 23 B10 reds plus card 10's `test_g11_an_awk_segment_that_can_write_is_denied[grep X f | awk '{ "date" | getline d; print d }']`, which now got G3's route instead of G11's sentence. Both deny. So B9 now yields when G11 also denies (`and not awk_writes(ws[1:])`; `## DECISIONS` 2). Rerun → `23 failed, 501 passed`, all of them B10.
- B10: `WRAPPERS`, `WRAP_FLAGS`, `WRAP_VALUES` and `unwrap(ws)`. `unwrap` returns the words of the command a wrapper runs, past every wrapper's known options (a value option takes the next word, `=value`, or an attached value), `--`, NAME=value words and timeout's duration. Wrappers can nest. It returns None when an option is not known or no word is left. `g1`'s lone path now reads `ws = unwrap(words(text))`, replacing the NAME= strip loop, and None gives the resend sentence with `a wrapper whose command the guard cannot find`. `bash_rules` adds each wrapper segment's unwrapped words to `segs`, so G3, G4 and G7 judge them too. `pipe_problems` is unchanged. → `524 passed`.

THE MUTATIONS (Edit tool, each undone):
- M9 (undoes B9: `if False and …` in `g3_bash`): `-k "b9_ or g11_ or b10_every"` → `7 failed, 27 passed`. The 6 b9 ids and `env A=1 awk 'BEGIN{getline l < "y"}'` are red, first at `:268` `AssertionError: (0, '')` `assert 0 == 2`.
- M9c (B9 without the G11 yield): `-k "b9_ or g11_"` → `1 failed, 28 passed`. FAILED `test_g11_…[grep X f | awk '{ "date" | getline d; print d }']` at `:360`: `AssertionError: route: .env is never read; …`. This pins the yield.
- M9b (control: `"print"` added to `AWK_READS`): `-k b9_` → `2 failed, 6 passed`. Both b9 controls are red at `:273`, `assert 2 == 0`, with G3's route.
- M10 (undoes B10: `if True or name not in WRAPPERS:` in `unwrap`): `-k b10_` → `23 failed, 7 passed`. Every B10 red id is red; first `:1158` `assert 0 == 2`.
- M10b (the `bash_rules` addition off: `if u and False`): `-k b10_` → `5 failed, 25 passed`. Exactly the 5 `b10_every` ids are red, while the lone-command ids stay green through `g1`.
- M10c (control: `return None` right after a wrapper is seen): `-k b10_a_wrapped_read` → `5 failed`. All 5 controls are red at `:273` with `… contains a wrapper whose command the guard cannot find. …` `assert 2 == 0`.
- M10d (the pipe pin: `ws = unwrap(words(seg)) or words(seg)` in `pipe_problems`): `-k b10_a_wrapper_in_a_pipe` → `2 failed`, both at `:1186` `assert 0 == 2`.
After the mutations, `git diff ops/desk/bare-guard.py` showed only the fix plus the header comment (B9, B10). `tests/ops/test_bare_guard.py` → `524 passed`. Committed `c74edcd3 fix(cobalt-guard-b): awk file-reading constructs are G3; a wrapped command is judged as itself (B9 B10, L1 L72)`.

### E3, fourth pass: B11

In `ops/desk/bare-guard.py`: `READ_FILTERS` loses `awk` (`grep sed cut sort uniq head tail wc`, line 79). In `pipe_problems`, a segment not in the list adds `a pipe `|` with `<verb>`, not a read-only filter` and skips the other checks, except for `awk`: its segment goes on to `filter_problem`, so G11's and B3's sentences stay beside B11's (the card: "G11, B3 and B9 stay as defence"; B9 is G3 and runs first, unchanged). The header comment names B11.
The first run, `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py`, gave `2 failed, 528 passed`: card 10's `test_g1_a_read_only_pipe_is_allowed[awk '{print $1}' f | sort -u-None]` and `[…-build]`, at `:273` with `… a pipe `|` with `awk`, not a read-only filter. …` `assert 2 == 0`. My E2 grep (`| awk`) had missed this awk-first control. It is reversed by R283 like the others: the id moved from `PIPES_ALLOWED` to `test_b11_an_awk_pipe_segment_is_denied` (`## DECISIONS` 4). Rerun → `529 passed, 15 warnings in 16.86s`.

THE MUTATIONS (Edit tool, each undone):
- M11 (undoes B11: `awk` back in `READ_FILTERS`): `-k b11` → `19 failed, 2 passed, 508 deselected`. Every B11 red is red, the moved id `[awk '{print $1}' f | sort -u]` among them; first `test_bare_guard.py:996: AssertionError: assert 0 == 2`.
- M11b (the defence off: `if True or ws[0] != "awk": continue`): `-k "b11 or g11_ or b3_"` → `12 failed, 19 passed`: the 9 `test_g11_an_awk_segment_that_can_write_is_denied` ids, `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied` and both `b11_g11_and_b3` ids. First line of `-k b11_g11_and_b3`: `:1000: AssertionError: … a pipe `|` with `awk`, not a read-only filter. …` `assert '`awk` with `system(`, `>` or `|` in its program' in 'a pipe `|` with `awk`, not a read-only filter'`.
- M11c (control: `cut` and `sort` out of `READ_FILTERS`): `-k b11_a_pipe_without_awk` → `2 failed`, both at `:273` `assert 2 == 0` (`… a pipe `|` with `cut`, not a read-only filter. …`, `… with `sort` …`).
After the mutations, `git diff ops/desk/bare-guard.py` showed only the fix and the header line, and `tests/ops/test_bare_guard.py` → `529 passed, 15 warnings in 17.44s`. Committed `3ecdd3dc fix(cobalt-guard-b): an awk pipe segment is not a read-only filter (B11, L1 L72 L77)` (the code and the moved id).

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

At `8e68decd` (second pass), `uv run cobalt jobs restarts 979ec797..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	M	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

At `c74edcd3` (third pass), `uv run cobalt jobs restarts 979ec797..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	M	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

At `3ecdd3dc` (fourth pass), `uv run cobalt jobs restarts 979ec797..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	M	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES

`<tip>` = `3c451126`. (a0) `git diff --name-only --no-renames 979ec797` → `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.

- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, verdict `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-190004.log`; executed `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (log line 2) → `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 595.98s (0:09:55)` (log line 828).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, verdict `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-190005.log`; executed `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`; `146 passed, 1 skipped, 15 warnings in 28.58s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1277 passed, 1 xfailed, 15 warnings in 347.65s (0:05:47)`, exit 0. The tests this build adds, all in this run: `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied` (5), `test_check_guard_o4_a_filter_that_writes_or_runs_is_denied` (8), `test_b2_a_sort_or_uniq_that_only_reads_stays_allowed` (7), `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied`, `test_b3_an_awk_program_in_the_command_stays_allowed`, `test_b4_a_lone_sort_uniq_or_awk_that_writes_is_denied` (5), `test_b4_a_lone_sort_or_awk_that_only_reads_stays_allowed` (2).
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (19:10 ET).

SECOND PASS, `<tip>` = `8e68decd`. (a0) `git diff --name-only --no-renames 979ec797` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-193005.log`. Log line 828: `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 602.83s (0:10:02)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-193006.log`. Line 57: `146 passed, 1 skipped, 15 warnings in 28.49s`. Its only skip is line 56, `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1291 passed, 1 xfailed, 15 warnings in 347.66s (0:05:47)`, exit 0. Added in this pass: `test_b7_a_two_letter_prefix_of_compress_program_is_denied` (3), `test_b7_sort_check_stays_allowed` (2), `test_b8_an_option_value_naming_env_is_denied` (3), `test_b8_an_option_value_not_naming_env_stays_allowed` (2).
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (19:40 ET).

THIRD PASS, `<tip>` = `c74edcd3`. (a0) `git diff --name-only --no-renames 979ec797` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-195417.log`. Log line 828: `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 596.81s (0:09:56)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-195418.log`. Line 57: `146 passed, 1 skipped, 15 warnings in 28.20s`. Its only skip is line 56, `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1329 passed, 1 xfailed, 15 warnings in 350.06s (0:05:50)`, exit 0. Added in this pass: `test_b9_an_awk_program_that_reads_a_file_it_names_is_denied` (6), `test_b9_an_awk_program_that_reads_only_its_operands_stays_allowed` (2), `test_b10_a_wrapped_command_is_judged_as_the_command_it_runs` (18), `test_b10_every_guard_rule_judges_the_wrapped_command` (5), `test_b10_a_wrapped_read_stays_allowed` (5), `test_b10_a_wrapper_in_a_pipe_stays_denied` (2).
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (20:04 ET).

FOURTH PASS, `<tip>` = `3ecdd3dc`. (a0) `git diff --name-only --no-renames 979ec797` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-200937.log`. Log line 828: `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 597.55s (0:09:57)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-200938.log`. Line 57: `146 passed, 1 skipped, 15 warnings in 28.70s`. Its only skip is line 56, `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1334 passed, 1 xfailed, 15 warnings in 349.08s (0:05:49)`, exit 0. Added or changed in this pass: `test_b11_an_awk_pipe_segment_is_denied` (4), `test_b11_g11_and_b3_stay_as_defence_on_an_awk_segment` (2), `test_b11_a_pipe_without_awk_stays_allowed` (2), `test_b11_an_awk_segment_g11_passes_is_denied_as_no_filter` (12, rewritten), `test_b3_b11_an_awk_program_in_the_command_is_denied_as_no_filter` (rewritten); `test_b9_…_stays_allowed` (now 1 id) and `test_g1_a_read_only_pipe_is_allowed` (now 7 ids × 2) shrank.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (20:19 ET).

## PRE-STOP SELF-CHECK

(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." Evidence: o5 red at E2 (`:268` `assert 0 == 2`) and under M1; o4 red at E2 (`:1017`) and under M2; the b2 controls red under M2c (4 of 7; `uniq -s2 -w3 f` is not reachable by that mutation, named above); b3 red at E2 (`:1039`) and under M3, its control green throughout; b4 red at E2 (`:1061`) and under M4, including the added probe-ending id (`:1063`); b4 controls green. No test stayed green under its row's mutation.
(2) "Every entry path of each rule pinned by a test." Callers at tip: `grep -n -F "filter_problem(" ops/desk/bare-guard.py` → `441:def filter_problem(ws):` · `469:        p = filter_problem(ws)` (pipe_problems: pinned by o4, b3) · `487:        p = filter_problem(ws) if ws else None` (g1 lone: pinned by b4, including the ` < /dev/null` ending). `grep -n -F "ENV_READERS"` → `76:` · `615:        if verb(ws) in ENV_READERS …` (g3_bash: pinned by o5 as a single command and as a pipe segment). `grep -n -F "awk_file("` → `394:` def · `448:` (pinned by b3 `-f`, `-fp.awk`, `--file=p.awk`, `--file p.awk`, and b4 lone). `grep -n -F "_writes("` → `409:def sort_writes` · `425:def uniq_writes` · `443:` / `445:` / `450:` the calls in `filter_problem`. Flag combinations pinned: clustered `-uo`, attached `-oout`, abbreviated `--out=x` / `--compress=sh`, uniq values `-f 1`, `-s2 -w3`, `-` as an operand. Seat kinds: the new rules are kind-free like G1/G3, and the tests use the build seat, as the check's O4/O5 tests do.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." The greps above were re-run at the tip; RESTARTS ran at `3c451126`; the commit list is from `git log --oneline 979ec797..HEAD`. The E2/E3 test-file lines (`:268`, `:1017`, `:1039`, `:1061`, `:1063`) are quoted from the runs that printed them.

SECOND PASS (B7 B8, tip `8e68decd`):
(1) b7 `--co=sh` and `--co sh` red at E2 (`:1088` `assert 0 == 2`) and under M7. b7 `--compress=sh` was green at E2 (see `## DECISIONS` 1) and red under M7b. Control `--check` red under M7c; control `-c` cannot be reached by a long-option mutation (named in E3). b8 `=.env` red at E2 (`:268`) and under M8. b8 `--files0-from .env` and `=/x/wt/job/.env` were green at E2 and red under M8c, and M8b shows B8 alone denies them. Both b8 controls red under M8d.
(2) Callers at tip: `grep -n -F "env_words(" ops/desk/bare-guard.py` → `616:def env_words(args):` · `630:` inside `g3_bash`. `grep -n -F "g3_bash(" …` → `628:` def · `671:    deny = g3_bash(segs)` (bash_rules; pinned by the b8 single-command ids; the pipe-segment path is the same loop at `:630`, pinned by o5's `grep -n X f | sort /x/wt/job/.env`). `grep -n -F "sort_writes(" …` → `409:` def · `443:` in `filter_problem` (lone path: the b7 ids; pipe path: o4's `grep X f | sort --compress=sh`). `ENV_READERS` at `:76` holds `sort cut uniq awk`. `grep -n -F "is_env(" …` → `606:` def · `630:` · `792:` (the Read tool's G3, whose input is a path, not words: B8 does not apply).
(3) The greps above were re-run at `8e68decd`. RESTARTS ran at `8e68decd`. The suite lines were read from the gate logs with `grep -n -F`. The commit list is from `git log --oneline 979ec797..HEAD`.

THIRD PASS (B9 B10, tip `c74edcd3`):
(1) Every b9 id was red at E2 (`:268`) and again under M9. The b9 controls went red under M9b. The G11 yield is pinned by card 10's own test, red under M9c. Every b10 id of the first two B10 tests was red at E2 (`:1158` / `:268`) and again under M10. The 5 `b10_every` ids were red under M10b. The 5 b10 controls went red under M10c, and the 2 pipe pins went red under M10d. No test stayed green under its mutation.
(2) Callers at the tip:
- `grep -n -F "unwrap(" ops/desk/bare-guard.py` → `225:def unwrap(ws):` · `561:        ws = unwrap(words(text))` (g1's lone path, pinned by `b10_a_wrapped_command_…`: every wrapper, nesting, a path, NAME=, `=`/attached/next-word values, and six cannot-find shapes) · `749:    segs += [u for u in (unwrap(ws) for ws in segs if verb(ws) in WRAPPERS) if u]` (bash_rules → G3, G4, G7, pinned by `b10_every`).
- A wrapped command inside a pipe goes through the same line 749, and its pipe segment is still denied by `pipe_problems` (pinned by `b10_a_wrapper_in_a_pipe`).
- `grep -n -F "awk_reads(" …` → `461:` def · `706:` in `g3_bash` (lone, pipe segment and wrapped, pinned by b9 and `b10_every`).
- `grep -n -F "awk_program(" …` → `439:` def · `458:` (`awk_writes`, pinned by every G11 test, all green) · `464:` (`awk_reads`).
- `grep -n -F "WRAPPERS" …` → `83:` · `237:` · `749:`.
- Seat kinds: B9 is G3 and kind-free. B10 follows each rule's own kinds, and the tests use the build seat, as G3, G4 and G7 apply to it.
(3) The greps above were re-run at `c74edcd3`, and RESTARTS ran at `c74edcd3`. The suite lines were read from the gate logs with `grep -n -F`, and the `tests/ops` line with `tail -n 3` of its output. The commit list is from `git log --oneline 979ec797..HEAD`.

FOURTH PASS (B11, tip `3ecdd3dc`):
(1) Every B11 red was red at E2 on `c74edcd3` (`:997` / `:1203` `assert 0 == 2`, the defence ids at `:1001`) and again under M11. The one moved card 10 id (`awk '{print $1}' f | sort -u`) was allowed on `c74edcd3` (it was a passing control there) and is red under M11. The defence is pinned by M11b (card 10's 9 G11 ids, B3's red and both `b11_g11_and_b3` ids). The controls went red under M11c. No test stayed green under its mutation.
(2) Callers at the tip: `grep -rn -F "READ_FILTERS" ops tests/ops` → `ops/desk/bare-guard.py:79:` the tuple · `:536:        if ws[0] not in READ_FILTERS:` (its only reader, in `pipe_problems`). `grep -n -F "pipe_problems(" ops/desk/bare-guard.py` → `529:` def · `570:        problems = pipe_problems(text, cuts)` (g1's pipe path). The awk segment as the first, middle and last segment is pinned (`awk … | head -1`, `grep | sort | awk`, `grep | awk`), with both seat kinds (`None`, `build`) through the 6 rewritten card 10 ids. A lone awk is not a pipe and B11 leaves it to B4/G11/B9 (`test_b4_a_lone_sort_or_awk_that_only_reads_stays_allowed`, `test_b9_…_stays_allowed[awk '{print $1}' f]`, green). A wrapped awk in a pipe was already denied (`b10_a_wrapper_in_a_pipe`).
(3) The greps above were re-run at `3ecdd3dc`, and RESTARTS ran at `3ecdd3dc`. The commit list is from `git log --oneline 979ec797..HEAD`.

## FOR THE CHECK

FOURTH PASS, `979ec797..3ecdd3dc` adds (after the report commit `6a06a3ee`):
- `4edae759 wip(cobalt-guard-b): red — B11 tests on c74edcd3`
- `3ecdd3dc fix(cobalt-guard-b): an awk pipe segment is not a read-only filter (B11, L1 L72 L77)`

The reds, mutations and greens are in `### E2, fourth pass` and `### E3, fourth pass`. Suites: `offline 3782/0`, `tests/ops 1334 passed, 1 xfailed`, `live-note 146/0`. With-DB, F0/F1/F2 and the lock: not run (DB: none). The earlier controls that B11 reverses are listed in `## DECISIONS` 4.

THIRD PASS, `979ec797..c74edcd3` adds (after the report commit `776d0a13`):
- `67039e11 wip(cobalt-guard-b): red — B9 B10 tests on 8e68decd`
- `c74edcd3 fix(cobalt-guard-b): awk file-reading constructs are G3; a wrapped command is judged as itself (B9 B10, L1 L72)`

The reds, mutations and greens are in `### E2, third pass` and `### E3, third pass`. Suites: `offline 3782/0`, `tests/ops 1329 passed, 1 xfailed`, `live-note 146/0`. With-DB, F0/F1/F2 and the lock: not run (DB: none). The card's FOR THE CHECK: the B9 and B10 reds are green, and every earlier card 10 and guard-b test is green (`tests/ops/test_bare_guard.py` `524 passed`).

Points for the check to weigh (not decisions):
- B9 matches the five names as substrings of any program word, so `awk '{print "ARGV"}'` is over-denied.
- B10's option lists are closed. An option outside them means the command cannot be found, and the call is denied: `xargs -a FILE` (it reads a file), `time -o FILE` (GNU time, it writes), `env -S` / `env -C`, and clustered flags such as `xargs -0r`.
- `command -v` / `-V` are read as flags, so `command -v sort -o x` is judged as `sort -o x`.

SECOND PASS, `979ec797..8e68decd` adds (after the report commit `a9fe5090` and the check's `f5815a0e wip(cobalt-guard-b): check red — O1` and `1f2c19a9 fix(cobalt-guard-b): a lone sort uniq awk by path or behind NAME= meets B4 (check O1)`):
- `1218375f wip(cobalt-guard-b): red — B7 B8 tests on 1f2c19a9`
- `8e68decd fix(cobalt-guard-b): --co is compress-program; G3 reads option values (B7 B8, L1 L72)`
The reds, mutations and greens are in `### E2, second pass` and `### E3, second pass`. Suites: `offline 3782/0`, `tests/ops 1291 passed, 1 xfailed`, `live-note 146/0`. With-DB, F0/F1/F2 and the lock: not run (DB: none).

First pass, `979ec797..3c451126`:
- `82c5c7a2 wip(cobalt-guard-b): red — B1–B4 tests on BASE`
- `87576deb fix(cobalt-guard-b): read-only filters stay read-only; sort cut uniq awk read no .env (B1-B4, L1 L3 L72)`
- `3c451126 fix(cobalt-guard-b): pin the house-probe ending on a lone sort (B4, K25 2)`

The per-row reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`; the caller greps are in `## PRE-STOP SELF-CHECK` (2) and PREFLIGHT; RESTARTS is above. No RUN row. With-DB suite: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none). The records copied at PREFLIGHT are in `## PREFLIGHT`.

Points for the check to weigh (the card's own words, not decisions): B2's `o`-in-a-short-option rule over-denies `sort -t o …` (the card accepts this). Like a pipe segment, B4 keys on the first word as typed (`ws[0]`), so a lone `/usr/bin/sort -o out f` or `LC_ALL=C sort -o out f` does not meet B4. A pipe segment of that shape is already denied as "not a read-only filter". See `## RECORDS`.

## CONTINUE

next: none (built, fourth pass B11 at `3ecdd3dc`). The desk verifies the artifact and launches the check (`CHECK-HUB.md`).

## DECISIONS

1. ASK DESK: the card says B7's `sort --compress=sh f` and B8's `sort --files0-from .env` and `sort --files0-from=/x/wt/job/.env` are "each allowed on 1f2c19a9". They PASSED there (`-rA` at E2): B2(b)'s `com` rule, G3's plain-word test and `is_env`'s basename of the whole word already denied them. E2 says to rewrite such a test until its red is the row's reason. But these commands are the card's own, and no rewrite of them can fail on `1f2c19a9`. Safe default taken: the ids are kept as the card writes them, as pins. Each is shown red under a mutation (M7b, M8c), and M8b shows B8 alone denies the two B8 ids. Not for Dejan.
2. ASK DESK: B9 overlaps card 10's G11 on `grep X f | awk '{ "date" | getline d; print d }'`. Both deny it. With G3 first, B9 changed the deny sentence, and card 10's test `test_g11_an_awk_segment_that_can_write_is_denied` went red. The card's record says every card 10 test stays green. Safe default taken: B9 yields to G11 when G11 also denies the program (`and not awk_writes(ws[1:])`), so the call is still denied with G11's sentence. This is pinned by M9c. Not for Dejan.
3. ASK DESK: B10 says a wrapper command "is judged by every guard rule as the command that follows". Read literally in a pipe, `grep -l X f | xargs grep -n Y` would become allowed, because `grep` is a read-only filter. That would widen R33's segment list, and `xargs` could read files named by the input, `.env` among them. Safe default taken: B10 only adds denies. A pipe segment led by a wrapper stays "not a read-only filter", as it was on `8e68decd`. This is pinned by `test_b10_a_wrapper_in_a_pipe_stays_denied` and M10d. Not for Dejan: it keeps his R33 list as written.
4. ASK DESK: B11 reverses earlier controls that asserted an awk pipe is allowed. They are card 10's `test_g11_any_other_awk_segment_stays_allowed` (6 ids × 2 kinds) and `PIPES_ALLOWED` id `awk '{print $1}' f | sort -u`, B3's control `test_b3_an_awk_program_in_the_command_stays_allowed`, and B9's control id `grep X f | awk '{print $1}'`. The card's records (R273, R281) say every earlier card 10 and guard-b test stays green. His later ruling 10-04 R283 ("guard G1 drops awk (B11)") makes that impossible for these ids. Safe default taken: his ruling governs (L77). Each such id is kept and now asserts B11's deny (`AWK_NOT_FILTER`). Two tests were renamed so that a name does not say "stays allowed" (`test_b11_an_awk_segment_g11_passes_is_denied_as_no_filter`, `test_b3_b11_an_awk_program_in_the_command_is_denied_as_no_filter`). Every other earlier test is unchanged and green. Not for Dejan: it carries his ruling as written.

## RECORDS
- L74: a system reminder asked for a `Claude-Session:` line in commits; recorded once under `## L74`, not acted on.
- Extra gate pair: W ran twice (`87576deb`: `offline 3782/0` log `/Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-184917.log`, `live-note 146/0` log `/Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-184918.log`, `tests/ops` `1276 passed, 1 xfailed`), then again on `3c451126` after the second fix commit (self-check 2).
- A `tests/ops` run was started after B4 (`uv run pytest … tests/ops`, moved to the background at its 120 s timeout) and was still running while the E3 mutations were applied. Its exit-0 result is not evidence for any tree and is not cited; `tests/ops` was rerun at each tip.
- No DevDocs line: `ops/desk/bare-guard.py` has no module page under `docs/40 - DevDocs/cobalt/`, and the card fences every file but its two.
- Carried read, not a rule of this card (like the check's `$VAR` and `grep -r` reads, which stay open): B4 keys on the first word as typed, as a pipe segment does, so a lone `sort`/`uniq`/`awk` written by path or behind `NAME=` does not meet it. The allow strings waiting for him (`Bash(sort *)` and the rest) match only the bare verb.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- CONTINUED at E2 19:27 ET. The desk's `CONTINUE: E2.` named no fact. Verified: `authorize.sh` on the amended card → `AUTHORIZED` (card commit `14dbcd51`, unchanged); `git status --short --branch` → `## ops/cobalt-guard-b-1004` and the report only; HEAD `1f2c19a9`; `.env` → No such file. The card's new rows B7 and B8 (judge 19:27, desk row R273) were built. The message itself added nothing.
- L74, second time: this session's system reminder again asked for a `Claude-Session:` line in commits. Not acted on. `1218375f` and `8e68decd` carry `Co-Authored-By` only.
- Second-pass card record (judge 19:27, R273), re-read: B7 and B8 go on his veto list. FOR THE CHECK: the B7/B8 reds are green at `8e68decd`. Every earlier guard-b and card 10 test stays green (`tests/ops` 1291 passed, 1 xfailed).
- Another gate pair, the third: offline and live-note on `8e68decd` (logs in `## W`).
- CONTINUED at E2 19:48 ET. The desk's `CONTINUE: E2.` named no fact. Verified: `authorize.sh` on the amended card → `AUTHORIZED` (card commit `37e1e2c7`, unchanged); `git status --short --branch` → `## ops/cobalt-guard-b-1004` and the report (its last line set to `RESUMED`); HEAD `776d0a13`; `.env` → No such file. The card's new rows B9 and B10 (judge 19:47, desk row R281) were built. The message itself added nothing.
- L74, third time: this session's system reminder at this resume asked for a `Claude-Session:` line in commits. Not acted on. `67039e11` and `c74edcd3` carry `Co-Authored-By` only.
- Third-pass card record (judge 19:47, R281), re-read: B9 fences awk's file-reading constructs, not names, and is a judgment, not a proof. `Bash(awk *)` stays off every line until his word. `cut`, `sort` and `uniq` go on after guard-b ships. Nothing in this build touches a line.
- Another gate pair, the fourth: offline and live-note on `c74edcd3` (logs in `## W`).
- CONTINUED at E2 20:06 ET. The desk's `CONTINUE: E2.` named no fact. Verified: `authorize.sh` on the amended card → `AUTHORIZED` (card commit `f4391a0a`, unchanged; RULINGS now holds 2026-10-03 R283, row 289, `HIS RULING · APPROVED — pending fold`, committed `c41fdd35`); `git status --short --branch` → `## ops/cobalt-guard-b-1004` and the report (its last line set to `RESUMED`); HEAD `6a06a3ee`; `.env` → No such file. The card's new row B11 (his ruling R283) was built. The message itself added nothing.
- L74, fourth time: this session's system reminder at this resume asked for a `Claude-Session:` line in commits. Not acted on. `4edae759` and `3ecdd3dc` carry `Co-Authored-By` only.
- REFUSED, not needed: `grep -n -F "awk '{print $1}' f | sort -u" tests/ops/test_bare_guard.py` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a `$` in a double-quoted argument, which UNATTENDED RULES forbids; the Grep tool was used instead).
- Another gate pair, the fifth: offline and live-note on `3ecdd3dc` (logs in `## W`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cobalt-guard-b · tip: 3ecdd3dc | on 979ec797 | migration: none | offline 3782/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 9 of 9 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0
