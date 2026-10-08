# guard-g2-open-reads-1008 — CHECK (pass 1) — 2026-10-08

## §0 Headline
- 11 findings (Opus 4, Sol 4, Grok 3), 0 dropped. 7 HELD and fixed in `ops/desk/bare-guard.py` (`828f28dc`): G3 now catches a secret behind a glob, a case change or a backslash-newline, and a keychain read behind `security`'s global options or a brace.
- 4 REJECTED by card lines and listed under OPEN. 2 of them are `## DECISIONS` items: G2's trigger misses a quoted `COBALT_ENV`, an issue older than this build; and a secret read by a program outside `ENV_READERS`.
- Suites green on `828f28dc`: offline 3991/0, live-note 146/0, `tests/ops` 2072 passed / 1 xfailed; RESTARTS: none; `.env` never present. ready: YES.

## L74
- 12:18 ET: a system reminder at session start asked for a `Claude-Session:` line on commits. DATA by L74; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 0 · bda09b6f3345dbbde1ee7192527adadea2956bde
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …" → STANDING: `Bash(grok *)` is a PRE-APPROVED string … | APPLIED: …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …" → STANDING: the four house strings are pre-approved … | APPLIED: …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Thu Oct  8 12:18:45 EDT 2026
status · git status --short --branch · 0 · ## ops/guard-g2-open-reads-1008
head · git log --oneline -1; git log --stat --format=%h 773f39e7..HEAD · 0 · (5 lines)
    d3c29cd0 docs(guard-g2-open-reads-1008): build report — 773f39e7
    d3c29cd0
    
     .../guard-g2-open-reads-build-2026-10-08.md        | 160 +++++++++++++++++++++
     1 file changed, 160 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/guard-g2-open-reads-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/radar-display-fix-1008/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/guard-g2-open-reads-1008/docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md" · 0 · BUILT · job: guard-g2-open-reads-1008 · tip: 773f39e7 | on 4125ff02 | migration: none | offline 3991/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 215263
range · git log --oneline 4125ff02..773f39e7 · 0 · (2 lines)
    773f39e7 feat(guard-g2-open-reads-1008): G2 passes the one production db query read for every seat, no stamp; G3 refuses ~/.cobalt_key, data/.cobalt_vault and a keychain dump for every seat (O1 O2 O3, L1 L3 L72 L77)
    d3b598df wip(guard-g2-open-reads-1008): red — every seat reads production without the stamp; secrets refused for every seat (O1 O2 O3)
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 4125ff02..773f39e7` · exit 0:
```
773f39e7
 ops/desk/bare-guard.py  | 56 +++++++++++++++++++++++++++++++++++--------------
 ops/desk/desk-launch.sh |  5 +++--
 2 files changed, 43 insertions(+), 18 deletions(-)
d3b598df
 tests/ops/test_bare_guard.py | 139 +++++++++++++++++++++++++++++++++++--------
 1 file changed, 115 insertions(+), 24 deletions(-)
```
Path union: `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`.
- DB: none · `git diff --name-only --no-renames 4125ff02..773f39e7` · exit 0 · `ops/desk/bare-guard.py` / `ops/desk/desk-launch.sh` / `tests/ops/test_bare_guard.py` — every path under `ops/` or `tests/ops/`.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0 · `sol: UP` / `grok: UP` / `gemini: UP`.
- Seats: house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed.
- Build self-check: 3 of 3.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
18813 <S>/diff.md
11340 <S>/files/120-guard-g2-open-reads-card.md
22424 <S>/files/guard-g2-open-reads-build-2026-10-08.md
40428 <S>/files/wt/ops/desk/bare-guard.py
65831 <S>/files/wt/ops/desk/desk-launch.sh
57972 <S>/files/wt/tests/ops/test_bare_guard.py
326 <S>/rulings.md
STAGED 7 files · 217134 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/guard-g2-open-reads-1008-check`.) Commits 2 = PREFLIGHT's range count; `grep -c "^commit " <S>/diff.md` → `2`.
- `stage-copy.sh .../src/cobalt/db_query.py <S>/files/wt/src/cobalt/db_query.py` → `COPIED 7878 …` (`## READ` by symbol).
- `stage-copy.sh ".../prompts/2026-10-06/21-guard-g2-card.md" <S>/files/21-guard-g2-card.md` → `COPIED 13892 …` (`## READ`).
- `<S>/HOUSE-INSTRUCTIONS.md` written: HOUSE TEXT verbatim + ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS + Files paragraph. Sol reads the same `diff.md` / `rulings.md` (made by stage-set from git) and the originals.
- 12:20 ET: house A Sol (`bj0sb4nm5`) and house B Grok (`b597q5qbr`) started, one after the other, from `<AGY>`; back in `<WT>`, `git status --short --branch` → `## ops/guard-g2-open-reads-1008`.

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: O2 (X3)
CLAIM: `is_secret` (`ops/desk/bare-guard.py:802-804`) compares the basename for equality only, while `is_env` (787-794) matches the word as a glob; a glob that names a secret (`cat ~/.cobalt_k?y`) is expanded by bash to the key file and passes G3 for every seat.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    ["cat ~/.cobalt_k?y", "cat /Users/cobalt/.cobalt_ke*", "tail -c 9 data/.cobalt_v[a]ult"],
)
def test_g3_a_glob_naming_a_secret_is_denied(roots, kind, command):
    """check O1: bash expands the glob to the secret file, as is_env reads a glob for .env."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)
```
EXPECT: `AssertionError: (0, '')` for each case (exit 0, allowed).

FINDING O2
ROW: O2 (X3)
CLAIM: `keychain_read` (`ops/desk/bare-guard.py:807-812`) reads only the word right after `security`; a `security` global option before the subcommand (`security -q dump-keychain`, `security -v find-generic-password -w -s x`) passes G3; `export` (799) has no test.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "security -q dump-keychain",
        "security -v find-generic-password -w -s x",
        "security -l -q find-internet-password -w -s x",
        "security export -k login.keychain -o out.p12",
    ],
)
def test_g3_a_keychain_read_behind_a_global_option_is_denied(roots, kind, command):
    """check O2: security's global options (-h -i -l -q -v, -p prompt) stand before the command."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)
```
EXPECT: `AssertionError: (0, '')` for the three option-first cases; the `export` case passes.

FINDING O3
ROW: O2 (X3)
CLAIM: G3 tests a secret only under a verb of `ENV_READERS` (`ops/desk/bare-guard.py:86`, 829); `base64 ~/.cobalt_key`, `xxd ~/.cobalt_key` and `cp ~/.cobalt_key /tmp/k` print or copy the key and pass for every seat.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command", ["base64 ~/.cobalt_key", "xxd ~/.cobalt_key", "cp ~/.cobalt_key /tmp/k"]
)
def test_g3_a_secret_read_by_another_program_is_denied(roots, kind, command):
    """check O3: a program outside ENV_READERS still reads or copies the secret."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)
```
EXPECT: `AssertionError: (0, '')` for each case.

FINDING O4
ROW: O1 (X1, X2)
CLAIM: `prod_read` (`ops/desk/bare-guard.py:878-913`) proves a command's words, never the code it runs; a worker seat whose cwd is its worktree passes G2 (926), and `uv run cobalt` there runs that worktree's own `src/cobalt/db_query.py` with the `.env` `src/cobalt/cli.py:59` loads from that tree, so the read-only proof (RECORDS, `db_query.py:163,177`) holds for the main checkout's code only.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
def test_g2_a_worker_in_its_worktree_is_denied_the_production_read(roots):
    """check O4: the worktree's code is not the code the read-only proof read."""
    assert_denied(run(PROD_QUERY, unstamped_seat(roots, "worker")), G2_ROUTE)
```
EXPECT: `AssertionError: (0, '')` (allowed). Expected verdict: REJECTED by row O1 (a `worker` seat passes, by name) — a FOLLOW-UP, not a fix.

X2 and X4, read with no finding: `db_query.py:163` `BEGIN READ ONLY` and `:177` `conn.rollback()` in `finally` wrap every statement `guard_select` (98-126) accepts; the `desk-launch.sh` hunks in `<S>/diff.md` lines 131-149 are `#` lines only (proved by command at `## 7`).

## Findings
12:31 ET both houses finished (Sol 12:24, Grok 12:31); `ls -la <S>` → `house-b.md` 3728 bytes (written by Grok); `house-a.md` written by me from Sol's final message (task output lines 6926-6968, `FINDINGS: 4`).
| id | house | row | claim | form |
|---|---|---|---|---|
| O1 | Opus | O2 X3 | a glob naming a secret (`.cobalt_k?y`) passes G3; `is_secret` is equality, `is_env` is a glob | TEST |
| O2 | Opus | O2 X3 | `security -q dump-keychain` (a global option first) passes G3; `export` untested | TEST |
| O3 | Opus | O2 X3 | `base64`/`xxd`/`cp` of `~/.cobalt_key` pass: not in `ENV_READERS` | TEST |
| O4 | Opus | O1 X1 X2 | a worker in its worktree passes G2; `uv run cobalt` runs that tree's code, not the code the read-only proof read | TEST |
| A1 | Sol | X3 | `security -q find-generic-password …` and `security {dump-keychain,}` pass G3 | TEST |
| A2 | Sol | X1 | `… db query --prod "SELECT 1"` with no `--side` passes G2 | TEST |
| A3 | Sol | O2 | `security export` is in `KEYCHAIN_READS` but no test pins it | COMMAND |
| A4 | Sol | O2 | case-insensitive secret match is unpinned: no upper-case fixture | COMMAND |
| B1 | Grok | X1 | a production verb with `COBALT_ENV` quoted / ANSI-C / brace / backslash-newline, `--"prod"`, `--pr{od,od}`, `--allow-prod` never meets `PROD.search`, passes G2 | TEST |
| B2 | Grok | X3 | `security -q|-v <read>` passes G3 | TEST |
| B3 | Grok | X3 | a glob or a backslash-newline in a `.env` / secret path passes G3 | TEST |

## Dropped
none — every block of both houses carries a `RUN:` line with a `def test_` or an allowed command.

## RUNS
Each TEST pasted at the end of the G3 section of `tests/ops/test_bare_guard.py`, run alone on tip `773f39e7` (+ the test), `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py::<test>`. First failing line in every red: `E   AssertionError: (0, '')` at `tests/ops/test_bare_guard.py:268` (exit 0, allowed).
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `::test_g3_a_glob_naming_a_secret_is_denied` | `21 failed` | HELD |
| O2 | Opus | `::test_g3_a_keychain_read_behind_a_global_option_is_denied` | `21 failed, 7 passed` (the 7 = `export`, as EXPECT said) | HELD |
| O3 | Opus | `::test_g3_a_secret_read_by_another_program_is_denied` | `21 failed` | REJECTED — row O2: "the readers stay `ENV_READERS` (82)"; fence: "A secret read by a program the guard does not parse … owed, a `## DECISIONS` item". Test removed. |
| O4 | Opus | `::test_g2_a_worker_in_its_worktree_is_denied_the_production_read` | `1 failed` | REJECTED — row O1 RED (1): "`worker` (cwd under the worktree root …)" passes, by name. Test removed. |
| A1 | Sol | `::test_g3_a_keychain_read_cannot_hide_its_subcommand` | `14 failed` | HELD |
| A2 | Sol | `::test_g2_a_production_query_without_side_is_denied` | `7 failed` | REJECTED — row O1: "every other line of the function stays byte for byte … every `--side` value … in `SIDES`" (no required side); harmless: `src/cobalt/db_query.py:211` `required=True` exits before any connection. Test removed. |
| A3 | Sol | `grep -n -F "security export" <tip test file>` (run on `git show 773f39e7:tests/ops/test_bare_guard.py`, saved; the working file already held my O2 test) | no output | HELD |
| A4 | Sol | `grep -n -F ".COBALT_KEY"` and `grep -n -F ".COBALT_VAULT"` on the same tip file (the house's one `-E` alternation split into two fixed strings — form repair, UNATTENDED RULES) | no output, no output | HELD |
| B1 | Grok | `::test_x1_a_production_verb_hidden_from_prod_search_passes_g2` | `10 failed` | REJECTED — row O1: "The G2 call (904) becomes `... and PROD.search(command) and not prod_read(command):`" (the trigger stays `PROD.search`, unchanged since BASE); fence: "A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here." Test removed. → DECISIONS D1. |
| B2 | Grok | `::test_x3_a_keychain_dump_with_a_global_option_first_is_denied` | `35 failed` | HELD |
| B3 | Grok | `::test_x3_a_secret_path_whose_basename_the_guard_does_not_see_is_denied` | `49 failed` | HELD |
Red commit (the HELD tests, before any fix): `0b75c88b wip(guard-g2-open-reads-1008): check red — O1 O2 A1 B2 B3`. A3 is pinned by O2's `export` case; A4's new test `test_g3_a_secret_named_in_another_case_is_denied` passes on the tip by design (it pins existing code) and was shown red by mutation: `.lower()` dropped from `is_secret` → `7 failed`, first line `E   AssertionError: (0, '')`; undone.

## FIXES
| fix | commit | files | proof |
|---|---|---|---|
| `is_secret` matches the word as a glob after brace expansion, lower-cased, a leading dot literal (as `is_env`); `keychain_read` brace-expands the words after `security`, skips its global options (`-p`, or a cluster ending `p`, takes a value) and tests the first command word; `g3_bash` tests each operand as given and with its newlines removed (shlex keeps a backslash-newline's newline; bash removes it); A4's case test added | `828f28dc fix(guard-g2-open-reads-1008): G3 reads a secret behind a glob, a case or a backslash-newline, and a keychain read behind security's options or a brace (check O1 O2 A1 A3 A4 B2 B3)` | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` | first try at B3 left the backslash-newline cases red (`21 failed, 1063 passed`), fixed as above; then `tests/ops/test_bare_guard.py` → `1084 passed`; with `tests/ops/test_desk_launch_prechecks.py` → `1209 passed` |
DevDocs: no page under `docs/40 - DevDocs/cobalt/` holds `ops/desk/bare-guard.py` (the build report RECORDS the same); none written.

## Suites
On tip `828f28dc` (DB: none card: RESTARTS, then W (a0), (a), (e) and `tests/ops`; no `--deploy`, no lock).
- RESTARTS · `uv run cobalt jobs restarts 4125ff02..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 4125ff02` → `docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md` · `ops/desk/bare-guard.py` · `ops/desk/desk-launch.sh` · `tests/ops/test_bare_guard.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-open-reads-1008 offline` · exit 0 → `offline 3991/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-open-reads-1008-offline-20261008-123723.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-open-reads-1008 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-open-reads-1008-livenote-20261008-123724.log`; `grep -n -F "SKIPPED" <log>` → `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `2072 passed, 1 xfailed, 15 warnings in 480.81s (0:08:00)`; `grep -c -F "SKIPPED"` → `0`. The build's 1918 plus the 154 cases this check adds.
- `.env`: `ls <WT>/.env` → `No such file or directory` (never present; no lock taken).

## Scope
PREFLIGHT path union: `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py` (+ the build report under `docs/`). My commits touch `ops/desk/bare-guard.py` (row O2's file) and `tests/ops/test_bare_guard.py` (rows O1/O2's test file) only.

## Checked against the branch
- (i) `git log --oneline 773f39e7..HEAD -- . ":(exclude)docs"` → `828f28dc fix(…)` · `0b75c88b wip(guard-g2-open-reads-1008): check red — O1 O2 A1 B2 B3`; `<tip now>` = `828f28dc`.
- (ii) `git log --stat --format=%h 773f39e7..HEAD` → `828f28dc`: `ops/desk/bare-guard.py | 29`, `tests/ops/test_bare_guard.py | 10`; `0b75c88b`: `tests/ops/test_bare_guard.py | 76`; `d3c29cd0`: the build report (docs). Every non-docs path is a row's file. No WIDENED.
- (iii) `git log --oneline 4125ff02..HEAD -- tests/ops/test_desk_launch_prechecks.py ops/desk/gate-lists.md src` → empty. X4: `git diff 4125ff02..HEAD -- ops/desk/desk-launch.sh` → two hunks, every `-`/`+` line a `#` comment (lines 116-117, 508). No code line changed.
- (iv) `grep -n -F "def <test>" tests/ops/test_bare_guard.py` → O1 `697:`, O2 `712:`, A4 `718:`, A1 `735:`, B2 `751:`, B3 `769:` (A3 is pinned by O2's `export` case at 712). Each sits in `0b75c88b` (red), which is below `828f28dc` (fix) in (i). A4's test came in with the fix and was shown red by mutation (`## RUNS`).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/guard-g2-open-reads-1008`.
- (vi) `git log --stat --format=%h 4125ff02..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate lists are needed.
- (vii) card RECORDS: `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` → nothing (exit 1), as recorded.
- (viii) L32: this report holds no ticker, price or date of his. The paths `~/.cobalt_key` / `data/.cobalt_vault` are the card's own names, and the test values are constructed.

## OPEN
FOLLOW-UP items. None is fixed here, and no second pass follows.
- O3 · REJECTED — row O2 "the readers stay `ENV_READERS`". `base64`, `xxd` and `cp` of `~/.cobalt_key` pass for every seat (`21 failed` when the test asserts a deny). Settled by: widen G3's readers, or deny any operand naming a secret for every verb but `ls`. → D2.
- O4 · REJECTED — row O1 names the `worker` seat. A worker in its worktree passes G2, and `uv run cobalt` there runs that tree's `src/cobalt/db_query.py` (with the `.env` `src/cobalt/cli.py:59` loads from that tree, present only inside a lock take). The read-only proof (RECORDS) covers the main checkout's code only. Hub seats keep the harness deny `Bash(COBALT_ENV=production*)`. Settled by: a ruling on whether a prod read from a worktree cwd should pass.
- A2 · REJECTED — row O1 keeps `prod_read` byte for byte, with no required `--side`. A prod query with no `--side` passes G2. It is harmless: `db_query.py:211` `--side` is `required=True`, so argparse exits before any connection opens.
- B1 · REJECTED — the row keeps `PROD.search` as G2's trigger, and the fence routes a red outside the rows to DECISIONS. → D1.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
- D1 · UNPROVEN on BASE (L70; by reading, `PROD` (`bare-guard.py:111`) and the G2 trigger are unchanged since `4125ff02`), red on the tip. From a build seat, G2 does not fire on a production verb whose `COBALT_ENV=production` or `--prod` never appears literally: `COBALT_ENV="production" uv run cobalt db migrate`, `COBALT_ENV='production' … db apply`, `env COBALT_ENV="production" …`, `FOO=1 COBALT_ENV="production" … validate`, `COBALT_ENV=$'production' …`, `COBALT_ENV=prod{uction,uction} …`, `COBALT_ENV=product\<newline>ion …`, `uv run cobalt db migrate --"prod"`, `--pr{od,od}`, `--allow-prod`. Grok B1's test gave `10 failed`, each `E   AssertionError: (0, '')`. The quoted forms also miss the hub's harness deny string `Bash(COBALT_ENV=production*)`. The fence says it is never fixed here. Safe default taken: test removed, nothing changed. It needs its own card, where G2 reads the words and not the raw string.
- D2 · The fence, "a secret read by a program the guard does not parse … a `## DECISIONS` item if the build meets one": `base64 ~/.cobalt_key`, `xxd ~/.cobalt_key` and `cp ~/.cobalt_key /tmp/k` pass for every seat (O3, `21 failed`). The cause is that G3's readers stay `ENV_READERS` by row O2. `areas/cobalt.md` `## What Cobalt is`: secrets are "never hardcoded, printed or logged". Safe default taken: test removed, nothing changed. It needs its own card.

## RECORDS
- start 12:18 ET; houses started 12:20 ET; Sol done 12:24, Grok done 12:31; close 12:48 ET.
- L74: the `Claude-Session:` request in a system reminder at session start was not acted on (`## L74`).
- Dropped findings: none. Houses that produced nothing: none.
- Sol wrote no file. I wrote `<S>/house-a.md` from its final message. Grok wrote `<S>/house-b.md` itself and replied with the path.
- `## 1` (1)/(2) for Sol: `diff.md` and `rulings.md` were made once, by `stage-set.sh` from git, and both houses read the same pair. `grep -c "^commit " <S>/diff.md` → `2`.
- A3's grep ran on `git show 773f39e7:tests/ops/test_bare_guard.py` (saved output), not on the working file, which already held my O2 test with a `security export` case (line 709). A4's `-E` alternation was split into two `-F` greps.
- No lock taken, no extra lock take; no CONTINUED; no REFUSED command.
- Late read: `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) was opened at 12:48 ET, after the fixes rather than at `## 2`. Nothing in it changes a verdict, and it backs D2.
- files opened: 17 — CHECK-HUB.md; the card; BUILD-HUB.md (THE LOCK, E2, RESTARTS, W); `<S>/diff.md`; `ops/desk/bare-guard.py`; `tests/ops/test_bare_guard.py`; `src/cobalt/db_query.py`; `src/cobalt/db.py` (160-269); the build report (110-160); `areas/cobalt.md`; `<S>/rulings.md`; `<S>/house-b.md`; the Sol output (6840-6970); the Grok output; the probe output; the offline gate output; the live-note gate output.
- Check of `guard-g2-open-reads-1008`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: guard-g2-open-reads-1008 · pass: 1 · tip: 828f28dc · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 3 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 227244
