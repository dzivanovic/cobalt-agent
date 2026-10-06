# guard-g2 — CHECK REPORT (2026-10-06)

## §0 Headline
- Check of guard-g2 (tip was `ce19a3fd`, now `19f75dc6`). House A was Sol and house B was Grok, each `FINDINGS: 5`, and I wrote 5 of my own: 15 findings, none dropped.
- 11 held and all 11 are fixed in `19f75dc6`. 1 did not hold (O4: G1 does deny a piped query, which settles the build's ASK DESK 1). 3 were rejected and stay open (A3, A4, B3).
- Holes closed in the guard: a production word hidden from G2 by a line continuation, a `#` inside a word, a brace word or `--allow-prod`.
- Holes closed in the launcher: a marker built from shell quotes (`PROD""-READ:`) without its row, a `DISAPPROVED` or `production ready` row that still got the stamp, and a typed `<stamp>x`.
- Suites: offline 3932/0, live-note 146/0, tests/ops 1462 passed (1 xfailed). RESTARTS: none. 4 decisions for the desk, 0 for Dejan.

## L74
A system reminder of this session asked that commits end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 0 · b3e86930a2005934853ff0dc2e660a7d13d03140
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/21-guard-g2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R511 row · grep -n "^| R511 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 36:| R511 | 06:37 ET | HIS RULING: add the G2 row to `ops/desk/bare-guard.py`: a production read-only `db query` passes only for a seat citing an APPROVED HIS RULING row; all else refused. Words: `cto-2026-10-06-words.md` R511. Done by card, not a desk edit. | APPROVED — pending fold |
RULING 2026-10-06 R511 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R511 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 720c98b8555d085e1aeda2fb3932c2781354ff9d
RULING 2026-10-06 R511 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row; `grep -n "^| R19 " …cto-2026-09-24.md` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Tue Oct  6 08:02:41 EDT 2026
status · git status --short --branch · 0 · ## ops/guard-g2-1006
head · git log --oneline -1; git log --stat --format=%h ce19a3fd..HEAD · 0 · (5 lines)
    61999cc5 docs(guard-g2): build report — ce19a3fd
    61999cc5

     .../reports/guard-g2-build-2026-10-06.md           | 184 +++++++++++++++++++++
     1 file changed, 184 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/guard-g2-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/guard-g2-1006/docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md" · 0 · BUILT · job: guard-g2 · tip: ce19a3fd | on 3c257bb9 | migration: none | offline 3932/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 273887
range · git log --oneline 3c257bb9..ce19a3fd · 0 · (2 lines)
    ce19a3fd feat(guard-g2): G2 passes a launcher-stamped seat's one production db query (G2 R1 R2, L1 L3 L72)
    ff2d684a wip(guard-g2): red
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 3c257bb9..ce19a3fd` · 0 · ce19a3fd: `ops/desk/bare-guard.py` 37, `ops/desk/desk-launch.sh` 34, `tests/ops/test_desk_launch_prechecks.py` 28; ff2d684a: `tests/ops/test_bare_guard.py` 91, `tests/ops/test_desk_launch_prechecks.py` 151. Path union: the four row files.
- DB: none · `git diff --name-only --no-renames 3c257bb9..ce19a3fd` · 0 · `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py` — all under `ops/` or `tests/ops/`.
- `ls <S>` · 1 · `No such file or directory` → fresh.
- HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · 0 · `sol: UP` / `grok: UP` / `gemini: UP`.
- SEATS: house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · output whole:
```
22857 <S>/diff.md
13892 <S>/files/21-guard-g2-card.md
23875 <S>/files/guard-g2-build-2026-10-06.md
38714 <S>/files/wt/ops/desk/bare-guard.py
63362 <S>/files/wt/ops/desk/desk-launch.sh
52164 <S>/files/wt/tests/ops/test_bare_guard.py
49445 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
376 <S>/rulings.md
STAGED 8 files · 264685 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/guard-g2-check`.) Commits 2 = PREFLIGHT's range count; `grep -c "^commit " <S>/diff.md` → `2`.
- `stage-copy.sh <WT>/src/cobalt/db_query.py <S>/files/wt/src/cobalt/db_query.py` → `COPIED 7878 …` (`## READ` by symbol).
- `stage-copy.sh "…/reports/cto-2026-10-06.md" <S>/files/cto-2026-10-06.md` → `COPIED 17400 …` (the report `## READ` and `## ROWS` name).
- `<S>/HOUSE-INSTRUCTIONS.md` written: HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
- Houses started 08:04 ET (date 08:04:15): A Sol `b2s5c2k26`, B Grok `bz7c2czti`; `git status --short --branch` after return → `## ops/guard-g2-1006`.

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: G2 R2(ii) · X1
CLAIM: `marked_read` reads `words(command)` (`ops/desk/bare-guard.py:861`), whose shlex keeps a backslash-newline as a character while bash removes it, and G1's `scan` skips `\` plus the next character (`ops/desk/bare-guard.py:163-165`, `148-150`), so a second `--prod` or a `cobalt_brain` split by a line continuation passes G2 and G1 for a marked seat.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" --pr\\\nod',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT cobalt_br\\\nain"',
])
def test_g2_a_marked_seat_is_denied_a_production_word_split_by_a_line_continuation(roots, command):
    """check O1: bash joins `\\<newline>`; the second --prod or cobalt_brain is still there."""
    assert_denied(run(command, marked_seat(roots)), G2_ROUTE)
```
EXPECT: both cases fail `assert done.returncode == 2` with `(0, '')`.

FINDING O2
ROW: G2 R2(ii) · X1
CLAIM: `words()` calls `shlex.split(segment, comments=True)` (`ops/desk/bare-guard.py:287`), which starts a comment at a `#` inside a word; bash does not, so text after a mid-word `#` (a `cobalt_brain`, a second `--prod`) is invisible to `marked_read` (`:874`) and G1 sees no comment (`:157`, `#` only after a blank).
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"#cobalt_brain',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" x# --prod',
])
def test_g2_a_marked_seat_is_denied_a_production_word_behind_a_mid_word_hash(roots, command):
    """check O2: to bash a `#` inside a word starts no comment; what follows it is run."""
    assert_denied(run(command, marked_seat(roots)), G2_ROUTE)
```
EXPECT: both cases fail `assert done.returncode == 2` with `(0, '')`.

FINDING O3
ROW: G2 R2(ii) · X1 (a brace word)
CLAIM: `marked_read` tests `PROD` on each word as typed (`ops/desk/bare-guard.py:874`), not on its brace expansion (`braces`, `:769-780`, which G3 uses), so `--pro{d,}` (bash: `--prod --pro`) or `cobalt_b{r,}ain` passes G2 and G1 for a marked seat.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" --pro{d,}',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" cobalt_b{r,}ain',
])
def test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word(roots, command):
    """check O3: the shell brace-expands the word into a second --prod or cobalt_brain."""
    assert_denied(run(command, marked_seat(roots)), G2_ROUTE)
```
EXPECT: both cases fail `assert done.returncode == 2` with `(0, '')`.

FINDING O4
ROW: SCOPE (the fence: "a row that passes … a pipe") · the build's DECISIONS 1
CLAIM: the build's ASK DESK 1 says a marked `db query | grep x` passes G2 and then G1 (UNPROVEN); `pipe_problems` (`ops/desk/bare-guard.py:605-613`) tests every segment, the first included, so the first segment `COBALT_ENV=production …` is not a read-only filter and G1 denies it.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("tail", [" | grep x", " | head -n 1"])
def test_g2_a_marked_query_piped_into_a_read_filter_is_denied(roots, tail):
    """check O4: no row passes a pipe (the fence); G1 denies the query's segment."""
    done = run(PROD_QUERY + tail, marked_seat(roots))
    assert done.returncode == 2, done.stderr
    assert done.stderr.startswith(BLOCK_HEAD), done.stderr
```
EXPECT: if the build's ASK DESK 1 is right, `assert done.returncode == 2` fails with exit 0; if G1 denies, the test passes (the ASK is settled NOT HELD).

FINDING O5
ROW: G2 R1 (the `PROD-READ:` refusal, RED (g)) · X4
CLAIM: the refusal matches only the literal text `PROD-READ:` on the line (`ops/desk/desk-launch.sh:520`), but `run_launch` hands the line to `eval` (`:225`), so `PROD""-READ:` or `PROD-RE${X}AD:` typed after `follow it exactly.` launches unrefused with no proving row and reaches the seat's first message as the marker G2 trusts.
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`
```python
@pytest.mark.parametrize("typed", [' PROD""-READ: 2026-01-02 R2', " PROD-RE${X}AD: 2026-01-02 R2"])
def test_r1_a_marker_spelled_across_shell_quoting_without_its_row_is_refused(desk, tmp_path, typed):
    """check O5: eval makes the marker of `PROD""-READ:` or an empty expansion; with no proving
    row the line does not launch."""
    pfile = read_prompt(desk, no_proof(desk, "row absent"), typed=typed)
    done = dry_prompt(desk, tmp_path, pfile)
    assert done.returncode == 1, done.stdout
    assert done.stdout == ""
```
EXPECT: both cases fail `assert done.returncode == 1` with exit 0 and the printed line.

## Findings
Both houses finished: Sol at 08:16 (date 08:16:09; final message written by me to `<S>/house-a.md`, `FINDINGS: 5`), Grok at 08:21 (date 08:21:53; `<S>/house-b.md`, written by Grok, `FINDINGS: 5`). Every block carries a `RUN:` with a `def test_` or a `grep` line: none dropped.
- A1 · Sol · G2 R1 · `ruling_row`'s `*APPROVED*` matches `DISAPPROVED`, so R1 stamps a disapproved row · TEST
- A2 · Sol · G2 R1 (h) · a typed `<stamp>x` passes the equality test (only a digit suffix refused) · TEST
- A3 · Sol · G2 CONTROL (b) · the leading-shape mutation leaves CONTROL (b) as typed green; the build substitutes `db migrate --prod` · COMMAND
- A4 · Sol · G2 CONTROL (e) · CONTROL (e) is red on BASE (its G1 text), though the card counts it a control green on BASE · COMMAND
- A5 · Sol · X4 · `PROD-"READ:"` evades the literal refusal; eval rebuilds the marker in the first message · TEST
- B1 · Grok · X1 · `--allow-prod` beside `--prod` passes G2 (PROD's lookbehind skips it) · TEST
- B2 · Grok · X1 · the brace word `{--side,admin}` hides a second `--side` from the side test · TEST
- B3 · Grok · G2 (fence: a write verb) · a marked `db query --prod … "DELETE FROM t"` passes G2 · TEST
- B4 · Grok · X3 · `production ready` contains `production read`, so R1 stamps it · TEST
- B5 · Grok · G2 R1 (h) · a typed `<stamp>x` launches (same as A2) · TEST

## Dropped
none

## RUNS
Tests placed with the Edit tool as written (no form repair). Guard run: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py::<the seven>` → `9 failed, 2 passed` (O1, O2, O3, B1, B2, B3 red: `E   AssertionError: (0, '')` / `assert 0 == 2`, `tests/ops/test_bare_guard.py:268`; O4's two cases passed). Launcher run: `uv run pytest … tests/ops/test_desk_launch_prechecks.py::<the six>` → `7 failed` (first lines below).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `test_g2_a_marked_seat_is_denied_a_production_word_split_by_a_line_continuation` (2) | both `AssertionError: (0, '')`, `assert 0 == 2` | HELD |
| O2 | own | `test_g2_a_marked_seat_is_denied_a_production_word_behind_a_mid_word_hash` (2) | both `AssertionError: (0, '')` | HELD |
| O3 | own | `test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word` (2) | both `AssertionError: (0, '')` | HELD |
| O4 | own | `test_g2_a_marked_query_piped_into_a_read_filter_is_denied` (2) | 2 passed: G1 denies the pipe (the query's segment is no read-only filter) | NOT HELD — test removed; the build's ASK DESK 1 is settled: G1 denies `db query … \| grep x` |
| O5 | own | `test_r1_a_marker_spelled_across_shell_quoting_without_its_row_is_refused` (2) | `assert 0 == 1`; stdout `… follow it exactly. PROD""-READ: 2026-01-02 R2" --model …` and `… PROD-RE${X}AD: …` | HELD |
| A1 | Sol | `test_r1_a_disapproved_row_stamps_nothing` | `assert 'PROD-READ:' not in …`; stdout `… exactly. PROD-READ: 2026-01-02 R2" --model …` | HELD |
| A2 | Sol | `test_r1_a_typed_marker_with_a_suffix_is_refused` | `assert 0 == 1` (`refused`, line 224); stdout `… PROD-READ: 2026-01-02 R2x" …` | HELD |
| A3 | Sol | `grep -n -F "CONTROL (b) as typed" "docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md"` | `120:Said, per the card: CONTROL (b) as typed (\`db migrate\`, no \`--prod\`) stays green under the leading-shape mutation (the exactly-one test refuses it), so the control carries a second command \`db migrate --prod\`, which goes red. …` | REJECTED — R2(ii) "among its later words exactly one is `--prod`": the row's own clause refuses `db migrate` without `--prod`, so no leading-shape mutation can turn that command red; the build's `db migrate --prod` case carries the mutation. OPEN (card text) |
| A4 | Sol | `grep -n -F "test_g2_a_marked_query_with_a_separator_is_g1s_to_deny" "docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md"` | `86:| … | 3 | denied by G2 on BASE (exit 2 with \`G2_ROUTE\`); the test asserts G1's resend text | denied both times; on BASE by G2, not G1 — red only on the deny text …` | REJECTED — the card's CONTROL (e): "the test asserts the G1 text after"; denied on BASE as the card says. OPEN (card text) |
| A5 | Sol | `test_r1_an_obfuscated_typed_marker_without_proof_is_refused` | `AssertionError: ('', 'RUN: cd … follow it exactly. PROD-READ: 2026-01-02 R2` / `assert 0 == 1` — the stub claude received the marker | HELD |
| B1 | Grok | `test_g2_allow_prod_does_not_pass_for_a_marked_seat` | `AssertionError: (0, '')` | HELD |
| B2 | Grok | `test_g2_a_brace_word_cannot_hide_a_side_value` | `AssertionError: (0, '')` | HELD |
| B3 | Grok | `test_g2_a_marked_query_with_a_write_verb_is_denied` | `AssertionError: (0, '')` | REJECTED — R2(ii): a command passes on its words' shape (`db query`, one `--prod`, `--side` user/system, no other PROD word); R2 reads no SQL. The read path refuses it itself (`src/cobalt/db_query.py:154` `guard_select`, `:163` `BEGIN READ ONLY`). Test removed; OPEN |
| B4 | Grok | `test_r1_production_ready_is_not_a_production_read` | `assert 'PROD-READ' not in …`; stdout `… PROD-READ: 2026-01-02 R2" …` | HELD |
| B5 | Grok | `test_r1_a_typed_marker_with_a_non_digit_suffix_is_refused` | `assert 0 == 1` (line 224); stdout `… R2x" …` | HELD (same defect as A2) |

Held tests committed red before the fix: `5093b1ca wip(guard-g2): check red — O1 O2 O3 O5 A1 A2 A5 B1 B2 B4 B5`.

## FIXES
| fix | ids | what |
|---|---|---|
| `19f75dc6 fix(guard-g2): …` `ops/desk/bare-guard.py` `marked_read` | O1 O2 O3 B1 B2 | refuses a backslash-newline; refuses when `words()` differs from the same split without comments (a mid-word `#`); refuses a brace word whose expansion holds an option or a PROD word; refuses an option word naming `prod` other than `--prod` |
| same commit, `ops/desk/desk-launch.sh` prompt kind | A1 B4 | the stamp also needs the row's status cell to start `\| APPROVED` and `production read(s)` as a word (`grep -i -E "production reads?([^[:alpha:]]\|$)"`) |
| same commit, `ops/desk/desk-launch.sh` prompt kind | A2 B5 | a typed stamp counts only when followed by the closing `" ` |
| same commit, `ops/desk/desk-launch.sh` prompt kind | O5 A5 | the line must open `claude --bg "<Read sentence><stamp>" `: nothing after `follow it exactly.` but the stamp (a dated prompt with other message text: none on main, `Grep` over `prompts/`, 7 hits all hubs or a card) |

After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py tests/ops/test_desk_launch_prechecks.py` → `713 passed, 15 warnings in 61.58s`. DevDocs line: none — `bare-guard.py` and `desk-launch.sh` have no module page under `docs/40 - DevDocs/cobalt/` (the build's RECORDS say the same).

## Suites
DB: none card, W as `BUILD-HUB.md` gives it ((a0), (a), (e)) on tip `19f75dc6`:
- RESTARTS · `uv run cobalt jobs restarts 3c257bb9..HEAD` → the five paths `DOCS` / `operator script; no Cobalt reader` / `test/documentation; no resident`, last line `RESTARTS: none`.
- (a0) · `git diff --name-only --no-renames 3c257bb9` → `docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`, all under `docs/`, `ops/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 5 paths)`.
- (a) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-1006 offline` → `offline 3932/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-1006-offline-20261006-082634.log` · exit 0.
- (e) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh guard-g2-1006 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/guard-g2-1006-livenote-20261006-083645.log` · exit 0.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1462 passed, 1 xfailed, 15 warnings in 365.69s (0:06:05)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/guard-g2-1006/.env` → `No such file or directory` (never present this run).

## Scope
PREFLIGHT path union: `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`, which are the row's four files. My commits touch the same four files and nothing else.

## Checked against the branch
- (i) `git log --oneline ce19a3fd..HEAD -- . ":(exclude)docs"` → `19f75dc6 fix(guard-g2): …` and `5093b1ca wip(guard-g2): check red — …`. `<tip now>` = `19f75dc6`.
- (ii) `git log --stat --format=%h ce19a3fd..HEAD` → `19f75dc6`: `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`; `5093b1ca`: `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`; `61999cc5`: the build report (docs). Every path sits in the row's files. Nothing WIDENED.
- (iii) `git log --oneline 3c257bb9..HEAD -- ops/desk/gate-lists.md .claude/settings.json src` → empty.
- (iv) each held test appears once: `tests/ops/test_bare_guard.py` 511 (O1), 520 (O2), 529 (O3), 534 (B1), 543 (B2); `tests/ops/test_desk_launch_prechecks.py` 1004 (O5), 1013 (A1), 1024 (A2), 1032 (A5), 1049 (B4), 1057 (B5). `5093b1ca` sits below `19f75dc6` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/guard-g2-1006`.
- (vi) `git log --stat --format=%h 3c257bb9..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No new migration and no new with-DB test, so the gate lists are not needed.
- (vii) card RECORDS: `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` → nothing (matches the record). `grep -n "^| R511 " …/cto-2026-10-06.md` → line 36 (the record said 22 and notes that the number moves); committed in `720c98b8` (authorize.sh row).
- (viii) L32: this report holds only constructed values (dates 2026-01-0x, `R2`, `SELECT 1`) and the desk's own row ids.

## OPEN
- A3 · REJECTED (R2(ii)): CONTROL (b) as typed cannot go red under the leading-shape mutation. To settle it, the desk accepts the build's `db migrate --prod` case or amends the card text.
- A4 · REJECTED (CONTROL (e) "asserts the G1 text after"): (e) is red on BASE on its deny text only. To settle it, the desk accepts this or amends the card text.
- B3 · REJECTED (R2(ii) reads no SQL): a marked `db query … "DELETE FROM t"` passes the guard, and `guard_select` / `BEGIN READ ONLY` refuse it at run time. To settle it, the desk rules whether the fence's "a write verb" covers SQL text.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK (B3, OPEN): is "a write verb" in the fence the SQL text of the one `db query` (for example `DELETE`)? R2(ii) passes a command on its words' shape and reads no SQL. The read path refuses the statement itself (`src/cobalt/db_query.py:154` `guard_select`, `:163` `BEGIN READ ONLY`). Default taken: built as R2(ii). The test was removed and nothing changed. [08:37 from date]
2. ASK DESK (A3, A4, OPEN): the card's red-first text says CONTROL (b) as typed goes red under the leading-shape mutation, and calls (e) green on BASE. Run outputs show (b) as typed is refused by R2's exactly-one-`--prod` clause, so the build added `db migrate --prod`, and (e) is red on BASE on its G1 deny text, as the card's own (e) sentence requires. Default taken: the build's tests stand and nothing changed. [08:37 from date]
3. ASK DESK (outside the fence): `ruling_row` (`ops/desk/desk-launch.sh:261`, `*"HIS RULING"*APPROVED*`) also accepts a `DISAPPROVED` status for every kind that calls it (cards' RULINGS, F5). A1 proved this only for the prompt stamp, which is fixed inside the R1 block. `ruling_row` itself is shared, so changing it would change other kinds (fence). Default taken: left unchanged; this is a follow-up for a card. [08:37 from date]
4. ASK DESK (UNPROVEN, L70, outside the fence): my R1 refusal covers only the prompt kind. As read from the code, the `desk` kind launches the wake-up file's typed line with no `PROD-READ:` test (`ops/desk/desk-launch.sh:385-402`), and the guard counts a marked desk seat (`MARKED_KINDS`). No test was run. Default taken: none; this is a follow-up for a card. [08:37 from date]

## RECORDS
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits. Recorded once under `## L74` and not acted on.
- Dropped findings: none. Every house produced a list (Sol `FINDINGS: 5`, Grok `FINDINGS: 5`).
- O4 (own) NOT HELD: its test was removed. B3 (Grok) REJECTED: its test was removed. Both are in `## RUNS`.
- Sol's raw output (9,367 lines, task `b2s5c2k26`) holds its streamed findings and its final list. I wrote `<S>/house-a.md` from the final list (its lines 9296-9365).
- No lock taken; no `.env` at any step. No `REFUSED` call. No `CONTINUE`.
- files opened: 13 — CHECK-HUB.md, the card, BUILD-HUB.md (THE LOCK, E2–W), `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `src/cobalt/db_query.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`, the build report, `areas/cobalt.md` (What Cobalt is; Build rules down), `<S>/house-b.md`, Sol's output (house A), the range diff output.
- Check of `guard-g2`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: guard-g2 · pass: 1 · tip: 19f75dc6 · house A: Sol FINDINGS: 5 · findings: 15 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 5 · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 216430
