# ops-hand-1010 — CHECK report (2026-10-10)

## §0 Headline
- Check of ops-hand-1010 on `2cb7a9ad`, one pass. House A was Sol (1 finding) and house B was Grok (3 findings). My own read found 3. No finding was dropped.
- 5 findings held, all in the launcher's ops-hand kind. The launch line could carry an extra command, a `$(…)`, a `--settings`/`--add-dir` flag, or a backslash-split `bypassPermissions`/`--dangerously-skip-permissions` past every gate and into `eval`. All 5 are fixed in `6a18ff95`.
- 2 findings are open (Sol A1 and Grok B1, the same point): G12 denies the R686 production read. I rejected both against H2 and D3. This is the build's DECISION 1, FOR DEJAN.
- Gate on `6a18ff95`: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev 0013, F2 = F0 · .env removed · RESTARTS: none. ready: YES.

## L74
One system block in this session asked for a `Claude-Session:` line in commit messages. It is data and was not acted on: both of my commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md"` · exit 0 ·
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 0 · 5d7af0764e17e841bcc08c58e5774a92a0b8fc83
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 65:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row; `grep -n "^| R19 " …cto-2026-09-24.md` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` → Sat Oct 10 13:58:07 EDT 2026.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 ·
```
clock · date · 0 · Sat Oct 10 13:58:16 EDT 2026
status · git status --short --branch · 0 · ## ops/ops-hand-1010
head · git log --oneline -1; git log --stat --format=%h 2cb7a9ad..HEAD · 0 · (5 lines)
    2399d3b9 docs(ops-hand-1010): build report — 2cb7a9ad
    2399d3b9
    
     .../reports/ops-hand-build-2026-10-10.md           | 194 +++++++++++++++++++++
     1 file changed, 194 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/ops-hand-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/orphan-clean-1010/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/ops-hand-1010/docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md" · 0 · BUILT · job: ops-hand-1010 · tip: 2cb7a9ad | on 1eb47b59 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 279960
range · git log --oneline 1eb47b59..2cb7a9ad · 0 · (2 lines)
    2cb7a9ad feat(ops-hand-1010): ops-hand seat kind, G12 closed class, OPS-HAND.md, launcher kind (H1-H5, L63 D1-D4 his, L3, L42)
    8fdd14d7 wip(ops-hand-1010): red — H1 H2 H4 tests, H5 pin
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h 1eb47b59..2cb7a9ad` · exit 0 ·
```
2cb7a9ad
 docs/40 - DevDocs/prompts/OPS-HAND.md | 22 +++++++++
 ops/desk/bare-guard.py                | 37 +++++++++++++--
 ops/desk/desk-launch.sh               | 87 ++++++++++++++++++++++++++++++++++-
 tests/ops/test_bare_guard.py          |  2 +
 4 files changed, 144 insertions(+), 4 deletions(-)
8fdd14d7
 tests/ops/test_bare_guard.py           | 156 ++++++++++++++++
 tests/ops/test_desk_launch_ops_hand.py | 315 +++++++++++++++++++++++++++++++++
 tests/ops/test_stop_guard.py           |  14 ++
 3 files changed, 485 insertions(+)
```
Path union: `docs/40 - DevDocs/prompts/OPS-HAND.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_ops_hand.py`, `tests/ops/test_stop_guard.py`. The card has no `DB: none` line: the gate runs `all --deploy`.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
THE OPENAI RULE (desk message, his R908): `pgrep -fl "codex exec"` · exit 1 · no output → no codex seat live.
THE HOUSE PROBES, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0 ·
```
sol: UP
grok: UP
gemini: UP
```
house A: Sol (OpenAI) · house B: Grok. HOUSE B: as needed (not mandatory).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 ·
```
34841 <S>/diff.md
16112 <S>/files/231-ops-hand-card.md
29080 <S>/files/ops-hand-build-2026-10-10.md
3041 <S>/files/wt/docs/40 - DevDocs/prompts/OPS-HAND.md
46798 <S>/files/wt/ops/desk/bare-guard.py
71016 <S>/files/wt/ops/desk/desk-launch.sh
79861 <S>/files/wt/tests/ops/test_bare_guard.py
12756 <S>/files/wt/tests/ops/test_desk_launch_ops_hand.py
28373 <S>/files/wt/tests/ops/test_stop_guard.py
367 <S>/rulings.md
STAGED 10 files · 322245 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/ops-hand-1010-check`.) `grep -c "^commit " <S>/diff.md` → `2` = PREFLIGHT's count.
`stage-copy.sh`, each `COPIED`: 17420 `files/wt/ops/desk/stop-guard.py` · 868 `files/wt/ops/desk/desk-list.sh` · 2674 `files/wt/ops/desk/desk-done.sh` · 21839 `files/wt/tests/ops/test_desk_launch_brain.py` · 16643 `files/wt/tests/ops/test_desk_launch_devfix.py` · 4288 `files/aset-orphan-answer-2026-10-10.md` · 29948 `files/cto-2026-10-10.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (16264 bytes). Houses started 14:00 ET (`date` 14:00:43), gates re-run (R17 line 35, R19 line 37), `pgrep -fl "codex exec"` exit 1 (none live) right before the Sol call; return `git status --short --branch` → `## ops/ops-hand-1010`.

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: H4 (X4)
CLAIM: the ops-hand block never refuses an unquoted `;` (or `&`, `|`) on the line (`ops/desk/desk-launch.sh:155-163` reads every token after `--disallowedTools` as a deny word, `:182-184` refuses only `<` `>`), so a line with ` ; <command>` after the deny list passes every gate and `run_launch` `eval`s it (`:233`).
RUN: TEST — `tests/ops/test_desk_launch_ops_hand.py`
```python
def test_check_o1_a_second_command_after_the_line_is_refused(desk):
    marker = desk.tmp / "o1-ran"
    desk.set_line(desk.line + f" ; touch {marker}")
    done = desk.run(dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert not marker.exists()
```
EXPECT: `assert done.returncode == 1` fails (0), the stub launch runs and `touch` makes the marker.

FINDING O2
ROW: H4 (X4)
CLAIM: a `$(…)` inside a double-quoted deny string passes (the deny check `:155-163` wants each string present, not only those; no gate refuses `$` or a backtick), and `eval` (`:233`) expands it.
RUN: TEST — `tests/ops/test_desk_launch_ops_hand.py`
```python
def test_check_o2_a_command_substitution_in_a_deny_string_is_refused(desk):
    marker = desk.tmp / "o2-ran"
    desk.set_line(desk.line + f' "Bash($(touch {marker}))"')
    done = desk.run(dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert not marker.exists()
```
EXPECT: `assert done.returncode == 1` fails (0); the marker is made.

FINDING O3
ROW: H4 (H3's bound "a persisted allow cannot widen it")
CLAIM: a flag outside H3's shape passes the launcher: no gate compares the line's other words (`tool_list … rest`) with H3's line, so `--settings '{"disableAllHooks":true}'` (which turns off the PreToolUse hook that carries G12) or `--add-dir /Users` (H3: "No `--add-dir`") is launched.
RUN: TEST — `tests/ops/test_desk_launch_ops_hand.py`
```python
@pytest.mark.parametrize("extra", ["--settings '{\"disableAllHooks\":true}'", "--add-dir /Users"])
def test_check_o3_a_flag_outside_the_shape_is_refused(desk, extra):
    desk.set_line(desk.line.replace(" --allowedTools ", f" {extra} --allowedTools ", 1))
    done = desk.run()
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
```
EXPECT: `assert done.returncode == 1` fails (0) for both cases: the dry run prints the cd and the widened line.

Read and found nothing to write a finding on: G12 against X1 (`env`/`command`/`nohup` wrappers, `\kill`, `$'…'`, braces, `-s`, `-n`, `--`, a leading zero, `%1`, a double blank, a trailing blank, `$PID`, `/bin/kill` are all non-fullmatch, `ops/desk/bare-guard.py:1067`; a newline, `;`, `|`, `&`, a redirect, a backtick and `$(` are G1 first, `:1056`, a read-only pipe needs every segment a read filter, `:636`); X2 (`seat()` reads only `first_message`, the first user record with text, `:691-719`, `:751`; HUBS wins first, `:758`); X3 (only the usage line changed, `desk-launch.sh:311`; the `:675`-pinned none-of text unchanged); X4 for `ps`/`pgrep`/`launchctl print` (no write option reaches G12 past G1's redirect deny).

## Findings
Sol finished 14:04 ET (`date` 14:04:59; FINAL message written by me to `<S>/house-a.md`, its `FINDINGS: 1` line). Grok finished 14:19 ET (`date` 14:19:41; it wrote `<S>/house-b.md` itself, 2324 bytes, `FINDINGS: 3`; stdout was the path only).
- A1 · Sol · H1 · G12 (`bare-guard.py:1059`) denies the R686 production `db query` read that H1 says still passes · TEST
- B1 · Grok · H1 · the same: G2 lets the R686 read pass (`:1047`), G12 denies it (`:1059`), `test_bare_guard.py:2012` pins the deny · TEST
- B2 · Grok · H4 · `--permission-\mode bypass\Permissions` after the deny list is not counted (`desk-launch.sh:639`) nor the `bypassPermissions` substring (`:643`); eval runs it as bypassPermissions · TEST
- B3 · Grok · H4 · `--dangerously-skip-\permissions` passes the substring gate (`:643`); eval hands claude the flag · TEST

## Dropped
none — every block of both houses carries a `RUN:` line followed by a `def test_`.

## RUNS
Each test put in its file with Edit and run alone (`uv run pytest -q -rs -p no:cacheprovider --color=no <file> -k …`), no form repaired.
- O1 · own · `tests/ops/test_desk_launch_ops_hand.py::test_check_o1_a_second_command_after_the_line_is_refused` · FAILED, `assert 0 == 1`; stderr `RUN: claude --bg "Read '…' …" … "Bash(sudo *)" ; touch …/o1-ran` · HELD
- O2 · own · `::test_check_o2_a_command_substitution_in_a_deny_string_is_refused` · FAILED, `assert 0 == 1`; stderr `RUN: … "Bash($(touch …/o2-ran))"` · HELD
- O3 · own · `::test_check_o3_a_flag_outside_the_shape_is_refused[--settings '{"disableAllHooks":true}']` and `[--add-dir /Users]` · both FAILED, `assert 0 == 1`; the dry run printed the cd and the line with the extra flag · HELD
- B2 · Grok · `::test_a_second_mode_spelled_with_a_backslash_is_refused` · FAILED, `AssertionError: (0, '… Bash(sudo *) --permission-mode bypassPermissions')` (the stub claude recorded it) · HELD
- B3 · Grok · `::test_a_skip_permissions_flag_spelled_with_a_backslash_is_refused` · FAILED, `AssertionError: (0, '… Bash(sudo *) --dangerously-skip-permissions')` · HELD
  Summary of the launcher run: `6 failed, 35 deselected, 15 warnings in 2.21s`.
- A1 · Sol · `tests/ops/test_bare_guard.py::test_h1_the_ops_hand_seat_keeps_the_r686_production_read` · FAILED, `AssertionError: route: ops-hand runs only its class (…); anything else is a card` / `assert 2 == 0` · REJECTED — H2: "Every Bash call of the seat that no earlier rule denies passes only when its words are ONE of … Anything else → exit 2"; D3: "A wider class is a new card". The build's DECISION 1 (FOR DEJAN) took this default. Test removed again with Edit (it would hold the suite red); OPEN.
- B1 · Grok · `::test_h1_the_r686_production_read_still_passes_for_ops_hand` · FAILED, the same line, `assert 2 == 0` · REJECTED — the same card lines as A1; removed; OPEN.
  Summary of the guard run: `2 failed, 1755 deselected, 15 warnings in 1.05s`.
HELD tests committed before the fix: `8e8352de wip(ops-hand-1010): check red — O1 O2 O3 B2 B3`.

## FIXES
- O1 O2 O3 B2 B3 · `ops/desk/desk-launch.sh`, kind `ops-hand`, after the copied "text after" gate: (1) refuse a backslash, `$`, a backtick, `;`, `&` or `|` anywhere on the line (H3's line holds none; these are what `eval` acts on inside or outside `"…"`); (2) every `--disallowedTools` word must be one `"…"` string; (3) the words outside the two lists must be exactly `claude --bg "<Read sentence>" --model <[A-Za-z0-9._-]+> --permission-mode default --remote-control ops-hand --name ops-hand` (no `--settings`, no `--add-dir`). Placed after every earlier gate, so each earlier refusal keeps its own reason. Run after the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_ops_hand.py tests/ops/test_desk_launch_brain.py tests/ops/test_desk_launch_devfix.py tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py` → `1997 passed, 15 warnings in 101.75s`. Commit `6a18ff95 fix(ops-hand-1010): ops-hand launch line held to H3's shape before eval (check O1 O2 O3 B2 B3)`. DevDocs: `grep -rl -F "desk-launch.sh" "docs/40 - DevDocs/cobalt"` → only `cobalt/jobs/restarts.md` (not this module's page); no page for the module, so no line written (as the build recorded).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 1eb47b59..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	A	DOCS	-
docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_ops_hand.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
`sh /Users/cobalt/cobalt/ops/desk/gate.sh ops-hand-1010 all --deploy` on `6a18ff95` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, no ticker and no migration in this range). Exit 0. Verdict lines, whole:
```
offline 4196/0
lock: waited 7 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/ops-hand-1010-all-20261010-142300.log
```
No line is marked `OUTSIDE the allowed set`. Then `ls /Users/cobalt/cobalt-wt/ops-hand-1010/.env` → `No such file or directory` (14:59 ET); `git status --short --branch` → `## ops/ops-hand-1010`. The tests/ops files this check touched ran green at the fix: `1997 passed` (under `## FIXES`).

## Scope
PREFLIGHT's path union (`docs/40 - DevDocs/prompts/OPS-HAND.md` H3; `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` H1/H2; `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_ops_hand.py` H4; `tests/ops/test_stop_guard.py` H5) plus my commits: `tests/ops/test_desk_launch_ops_hand.py` and `ops/desk/desk-launch.sh`, both H4's files. Nothing is outside the rows' files and nothing is inside the fence.

## Checked against the branch
- (i) `git log --oneline 2cb7a9ad..HEAD -- . ":(exclude)docs"` → `6a18ff95 fix(ops-hand-1010): ops-hand launch line held to H3's shape before eval (check O1 O2 O3 B2 B3)` · `8e8352de wip(ops-hand-1010): check red — O1 O2 O3 B2 B3`. `<tip now>` = `6a18ff95`.
- (ii) `git log --stat --format=%h 2cb7a9ad..HEAD` → `6a18ff95` `ops/desk/desk-launch.sh` (H4's files) · `8e8352de` `tests/ops/test_desk_launch_ops_hand.py` (a test file) · `2399d3b9` the build report (docs). No other path.
- (iii) `git log --oneline 1eb47b59..HEAD -- ops/desk/orphan-clean.sh <the six hubs> "docs/40 - DevDocs/prompts/STANDING-LIST.md" src .claude ops/com.cobalt.aset.plist` → empty.
- (iv) `grep -n -F "def <name>" tests/ops/test_desk_launch_ops_hand.py`, one line each: O1 `:318`, O2 `:327`, O3 `:337`, B2 `:344`, B3 `:351`; `8e8352de` (check red) sits below `6a18ff95` (fix) in (i).
- (vi) `git log --stat --format=%h 1eb47b59..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not owed.
- (vii) the card's `## RECORDS` name `git -C /Users/cobalt/cobalt show` and `git diff --stat` reads, no `ls`, `grep` or `git -C … log` command: nothing to run.
- (viii) L32: this report holds no ticker, price or date of his; the pids and labels quoted are the card's constructed test values.

## OPEN
- A1 (Sol) and B1 (Grok), REJECTED — the R686 production `db query` read is denied by G12 for the ops-hand seat. Both tests ran red for their stated reason. H1's words "the R686 production `db query` read still passes" sit beside H2's "Anything else → exit 2" and D3's "A wider class is a new card". What would settle it: his ruling on the build's DECISION 1. Either the read stays out (as built, pinned by `test_h2_x1_any_other_spelling_is_denied[COBALT_ENV=production …]`), or G12 admits it, which is a one-line change in `ops_class` and needs his row (D3). FOLLOW-UP.

## CONTINUE
next: none — check complete

## DECISIONS
- FOR DEJAN — the R686 read for the ops-hand seat (A1, B1; the build's DECISION 1). Two houses independently read H1 as requiring the production `db query` read to pass. The tip denies it under G12. Default taken: as built (denied), since H2 and D3 put anything outside the class on a new card. His word decides it. If he admits the read, the fix round adds `prod_read(command)` to `ops_class` and flips the pinned test.

## RECORDS
- Desk message (cto-desk, his R908 / brain R909): one OpenAI seat at a time, with `pgrep -fl "codex exec"` before any codex call. I followed it as a narrowing (fewer seats, never more access). `pgrep` ran twice, before the probe and right before the Sol call, and both exited 1 with no live codex. The OpenAI seat was held by this check's house A (Sol), 14:00–14:04 ET.
- Dropped findings: none. Houses that produced nothing: none.
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (one take, inside the gate, after a 7 min wait).
- L74: the `Claude-Session:` block (see `## L74`), recorded once, not acted on.
- The two REJECTED tests (A1, B1) were removed again with Edit, so they are not in any commit. The commit's tree holds only the five HELD tests.
- files opened: 14 — CHECK-HUB.md; the card; BUILD-HUB.md (THE LOCK, E2, RESTARTS, W); the probe output; `<S>/diff.md`; `ops/desk/bare-guard.py`; `ops/desk/desk-launch.sh`; `docs/40 - DevDocs/prompts/OPS-HAND.md`; the build report; `areas/cobalt.md` (What Cobalt is, Build rules down); Sol's output; Grok's output; `<S>/house-b.md`; the gate output.
- Check of `ops-hand-1010`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: ops-hand-1010 · pass: 1 · tip: 6a18ff95 · house A: Sol FINDINGS: 1 · findings: 7 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 3 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 195546
