# shadow-hub-1011 — check report (2026-10-11)

## §0 Headline
- Check of shadow-hub-1011: house A Sol (9 findings) and house B Grok (7), plus my own 5. That is 21 findings, every one run: 9 held and fixed, 1 not held, 9 rejected, 2 unsettled. None was dropped.
- Fixes, in `cd302109` (red first in `5b214968`):
  - The guard reads `sh -c`, and refuses a linked worktree and a linked instructions file.
  - The launcher refuses a linked spike scratch dir, and a role trial under any model but Grok.
  - The hub's pass S builds the rows, the results table gains a Gemini N/A row, and the hub states the DB-none stop fields.
- Suites on `cd302109`: offline 4199/0 · live-note 146/0 · tests/ops 3028 passed · DB: none (not taken) · `.env` absent · RESTARTS: none. ready: YES.
- 3 items FOR DEJAN feed his D1 sign-off: the Sonnet prompt sits after `--disallowedTools`; Sonnet's `Read` is unscoped (it reaches the main `.env`); Terra's shell and the spike's python writes rest on the sign-off and X1.

## L74
- One attribution block arrived in a system reminder at the start of the run, asking commits to end with a `Claude-Session:` line. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 0 · 4ea2b0ecc46790124c0f74f553ebbf8c84065808
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/324-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1009 row · grep -n "^| R1009 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 51:| R1009 | 06:13 ET | HIS RULING · APPROVED: Sol may sit as a seat in the checks the brain and desk require (317, 298 now); every build and every deploy waiting on his word is approved. Words `cto-2026-10-11-words.md` R1009. | APPLIED: LAWS L67 + NOW at 06:31 |
RULING 2026-10-11 R1009 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1009 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · aebcf44974dfbfd3e7eb7815b8a583c4f86e9e1c
RULING 2026-10-11 R1009 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:

```
clock · date · 0 · Sun Oct 11 09:04:06 EDT 2026
status · git status --short --branch · 0 · ## ops/shadow-hub-1011
head · git log --oneline -1; git log --stat --format=%h bc25c523..HEAD · 0 · (5 lines)
    397cd63b docs(shadow-hub-1011): build report — bc25c523
    397cd63b
    
     .../reports/shadow-hub-build-2026-10-11.md         | 210 +++++++++++++++++++++
     1 file changed, 210 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/shadow-hub-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/shadow-hub-1011/docs/40 - DevDocs/reports/shadow-hub-build-2026-10-11.md" · 0 · BUILT · job: shadow-hub-1011 · tip: bc25c523 | on 680eca0e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 11 of 11 | self-check: 3 of 3 | decisions: 6 · for Dejan: 1 · tokens: 405465
range · git log --oneline 680eca0e..bc25c523 · 0 · (2 lines)
    bc25c523 feat(shadow-hub-1011): SHADOW-HUB.md and SPIKE-HUB.md; launcher kinds shadow and spike; the guard's shadow and spike seats; the step scripts name kind shadow (S1-S5, S7, P1-P3; L29, L76, R411)
    f107f926 wip(shadow-hub-1011): red — S1-S5, S7, P1-P3 tests and the P4 RUN test
PREFLIGHT OK
```

- THE RANGE, `git log --stat --format=%h 680eca0e..bc25c523`: `bc25c523` → `SHADOW-HUB.md`, `SPIKE-HUB.md`, `ops/desk/{authorize.sh, bare-guard.py, desk-launch.sh, desk-watch.sh, preflight.sh, stop-guard.py}`, `tests/ops/{test_bare_guard.py, test_desk_watch.py}` (10 files, 424+/24-); `f107f926` → `tests/ops/{test_authorize.py, test_bare_guard.py, test_desk_launch_shadow.py, test_desk_launch_spike.py, test_desk_watch.py, test_preflight.py, test_shadow_hub_file.py, test_spike_hub_file.py, test_stop_guard.py}` (9 files, 1081+). Path union: 17 paths.
- DB: none — `git diff --name-only --no-renames 680eca0e..bc25c523` → 17 paths, every one under `docs/`, `ops/` or `tests/ops/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh`):
  ```
  sol: UP
  grok: UP
  gemini: UP
  ```
- **house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`)**. HOUSE B: as needed.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, per-file lines (bytes, dest under `<S>`):
```
79217 diff.md
28382 files/324-shadow-hub-card.md
24450 files/shadow-hub-build-2026-10-11.md
15505 files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
4028 files/wt/docs/40 - DevDocs/prompts/SPIKE-HUB.md
7623 files/wt/ops/desk/authorize.sh
52115 files/wt/ops/desk/bare-guard.py
80514 files/wt/ops/desk/desk-launch.sh
4961 files/wt/ops/desk/desk-watch.sh
9790 files/wt/ops/desk/preflight.sh
17527 files/wt/ops/desk/stop-guard.py
10754 files/wt/tests/ops/test_authorize.py
90852 files/wt/tests/ops/test_bare_guard.py
12529 files/wt/tests/ops/test_desk_launch_shadow.py
8974 files/wt/tests/ops/test_desk_launch_spike.py
22587 files/wt/tests/ops/test_desk_watch.py
18049 files/wt/tests/ops/test_preflight.py
7509 files/wt/tests/ops/test_shadow_hub_file.py
3939 files/wt/tests/ops/test_spike_hub_file.py
29215 files/wt/tests/ops/test_stop_guard.py
353 rulings.md
STAGED 21 files · 528873 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count. `stage-copy.sh`, each `COPIED <bytes> <dest>`:
- `files/model-bakeoff-redo-answer-2026-10-11.md` 8988 · `files/MODEL-BY-COMPLEXITY-FINAL-2026-10-10.md` 44359 · `files/330-sdk-spike-live.md` 6418 · `files/sdk-spike-live-preflight-2026-10-11.md` 2928
- `files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md` 32802 · `.../CHECK-HUB.md` 40252 · `.../BRAIN-HUB.md` 7665 · `.../2026-10-10/231-ops-hand-card.md` 17203
- `files/wt/ops/grok-sandbox.toml` 296 · `files/wt/ops/desk/idle-wake.py` 2277 · `files/wt/src/cobalt/jobs/restarts.py` 12098 · `files/wt/tests/ops/test_desk_launch_ops_hand.py` 14393 · `files/wt/tests/ops/test_desk_launch_devfix.py` 16643
- `<S>/HOUSE-INSTRUCTIONS.md` written (28080 bytes): the HOUSE TEXT, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
- Houses started 09:06:37 ET: house A Sol (`codex exec … gpt-5.6-sol -s read-only …`, task bnlglkryo), house B Grok (`grok -m grok-4.7 --sandbox cobalt-job …`, writes `house-b.md`, task bp3nivi04). `cd` back → `git status --short --branch` → `## ops/shadow-hub-1011`.

## OWN FINDINGS
Written 09:2x ET, before either house's list was opened.

FINDING O1
ROW: S3
CLAIM: The guard tests pass a constructed prompt (`tests/ops/test_bare_guard.py` `PASS_PROMPT`, no `'`, `(`, `)` or `/`), while the hub's real `<pass prompt>` (`docs/40 - DevDocs/prompts/SHADOW-HUB.md:29`) holds `(xAI)`, `tests/` and `rows'`; the guard may deny the hub's own prompt, so the gate seat could not run any builder.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize(
    "model,who",
    [("grok-4.7", "GROK (xAI)"), ("claude-sonnet-5-5", "SONNET 5.5 (Anthropic)"), ("gpt-5.6-terra", "TERRA (OpenAI)")],
)
def test_o1_the_hubs_own_pass_prompt_passes_the_guard(roots, model, who):
    prompt = (
        f"You are {who}, building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it "
        "exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. "
        "Reply with the list of files you wrote."
    )
    cmd = SHADOW_ROWS[model][2].replace("/Users/cobalt/cobalt-wt/<worktree>", str(roots.wt / JOB_WT))
    assert_allowed(run(cmd.replace("<pass prompt>", prompt), shadow_seat(roots, model)))
```
EXPECT: if the claim holds, `assert_allowed` fails (exit 2) for at least one model.

FINDING O2
ROW: X3 (S1 (c))
CLAIM: The Sonnet builder command allows `"Read"` with no path (`docs/40 - DevDocs/prompts/SHADOW-HUB.md:20`), so the claude `-p` call can read outside the worktree, the main repo's `.env` included; Grok's `cobalt-job` profile denies that file (`ops/grok-sandbox.toml:8`) and the Sonnet command has no equal.
RUN: COMMAND — `grep -n -F "--allowedTools \"Read\" \"Edit(//Users/cobalt/cobalt-wt/<worktree>/**)\"" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"`
EXPECT: one line, `20:| \`claude-sonnet-5-5\` | …`.

FINDING O3
ROW: X3 (S1 (c), Terra)
CLAIM: `codex exec -s workspace-write` (`docs/40 - DevDocs/prompts/SHADOW-HUB.md:21`) runs shell commands inside its sandbox and reads the whole disk; "writes only" for Terra then rests on the sign-off and X1, as the hub's own note says (`:26`).
RUN: COMMAND — `grep -n -F "X3's question" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"`
EXPECT: line 26, which leaves the question open. Whether codex runs a command needs a codex Terra call; that string is not on this check's list.

FINDING O4
ROW: X6 (P1 (e))
CLAIM: The spike seat can write outside `sdk-spike-1010` by a tool G5 does not see. The line allows the scratch venv's python on any file in the scratch dir (`docs/40 - DevDocs/prompts/SPIKE-HUB.md:22`), and a script the seat writes there can write any path and open the network. G5 fences only the Write and Edit tools (`ops/desk/bare-guard.py:1218-1220`).
RUN: COMMAND — `grep -n -F "Bash(/Users/cobalt/cobalt-wt/sdk-spike-1010/.venv/bin/python /Users/cobalt/cobalt-wt/sdk-spike-1010/*)" "docs/40 - DevDocs/prompts/SPIKE-HUB.md"`
EXPECT: one line, 22.

FINDING O5
ROW: X4 (S7)
CLAIM: S7 holds only at the builder call (`ops/desk/bare-guard.py:1151`, `os.path.lexists` at call time). A builder started in the background is still running when the gate seat takes the lock, and no guard rule stops that take, so `.env` can sit in the worktree during a builder pass. Only the hub's text rule prevents it (`SHADOW-HUB.md:34`).
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
def test_o5_no_guard_rule_holds_the_lock_take_while_a_builder_may_run(roots):
    seat = shadow_seat(roots)
    assert_allowed(run(builder(roots, "grok-4.7"), seat))
    assert_denied(run(f"sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh {JOB_WT} 90", seat), G7_ROUTE)
```
EXPECT: `assert_denied` fails: the take exits 0.

## Findings
House A Sol finished 09:16:05 ET (final message written to `<S>/house-a.md`, `FINDINGS: 9`). House B Grok finished 09:24:20 ET (wrote `<S>/house-b.md` itself, `FINDINGS: 7`; its blocks are numbered 1-5, 7, 6). Ids: A<n> = house A's FINDING n, B<n> = house B's.
- O1 · own · S3 · the guard may deny the hub's real `<pass prompt>` (`(xAI)`, `tests/`, `rows'`) · TEST
- O2 · own · X3 · the Sonnet command allows `"Read"` unscoped; reads outside the worktree, the main `.env` included · COMMAND
- O3 · own · X3 · `codex -s workspace-write` runs shell commands; "writes only" rests on the sign-off · COMMAND
- O4 · own · X6 · the spike's venv python runs a scratch script that writes anywhere; G5 sees Write/Edit only · COMMAND
- O5 · own · X4 · no guard rule stops the lock take while a background builder runs · TEST
- A1 · Sol · X6 · the spike launcher accepts `sdk-spike-1010` as a symlink to an outside dir · TEST
- A2 · Sol · X1 · G7 exception passes a builder whose worktree is a symlink to a wider place · TEST
- A3 · Sol · S1 · the hub narrows pass S and the fence to `src/` and `tests/`; S1 says pass S builds the rows · TEST
- A4 · Sol · S2 · the launcher launches a role trial (`ROLE:`) under a non-Grok model · TEST
- A5 · Sol · S5 · the results table has no `N/A — <where read>` row for the N/A model (Gemini) · TEST
- A6 · Sol · P1 · the P1 test compares to a hand copy `LINE_330`, not prompt 330 · TEST
- A7 · Sol · X6 · the spike's python writes outside scratch; G5 fences only Write/Edit · TEST
- A8 · Sol · X4 · a worktree seat may Write `.env` during a builder pass · TEST
- A9 · Sol · X3 · the Sonnet `"<pass prompt>"` sits after variadic `--disallowedTools`, read as a tool name · TEST
- B1 · Grok · X1 · `sh -c '<grok … wider glob>'` passes G7 (exit 0) · TEST
- B2 · Grok · X4 · `sh -c '<builder>'` passes while `.env` is on disk · TEST
- B3 · Grok · X6 · spike `cp` to a path outside scratch exits 0 · TEST
- B4 · Grok · S3 · a symlink named `SHADOW-INSTRUCTIONS.md` → `src/x.py` is a G5 pass · TEST
- B5 · Grok · X3 · Sonnet `"Read"` is unscoped (as O2) · TEST
- B7 · Grok · X3 · Terra `workspace-write` still runs a shell; the hub defers it · COMMAND
- B6 · Grok · S1 · the `SHADOW BUILT` line can only say `cobalt_dev: 0013`; no DB-none form · TEST

## Dropped
- none: every block of both houses carries a `RUN:` line followed by a `def test_` or one `grep` command line.

## RUNS
Tests added with Edit, each run with `uv run pytest -q -p no:cacheprovider --color=no <file> -k …`.
- O1 · own · `test_o1_the_hubs_own_pass_prompt_passes_the_guard` ×3 · `3 passed` · NOT HELD (removed)
- O2 · own · `grep -n -F -e "--allowedTools \"Read\" \"Edit(//…<worktree>/**)\"" SHADOW-HUB.md` (form repaired once: `-e`, the first spelling gave `grep: unrecognized option`) · `20:| \`claude-sonnet-5-5\` | … --allowedTools "Read" "Edit(//Users/cobalt/cobalt-wt/<worktree>/**)" …` · REJECTED — S1 (c) spells the Sonnet command with `"Read"` exactly
- O3 · own · `grep -n -F "X3's question" SHADOW-HUB.md` · `26:- Terra: … is X3's question: "writes only" for Terra rests on the sign-off and X1.` · UNSETTLED — whether codex runs a command needs a `codex exec -m gpt-5.6-terra` call; that string is not on this check's list
- O4 · own · `grep -n -F "Bash(/Users/cobalt/cobalt-wt/sdk-spike-1010/.venv/bin/python /Users/cobalt/cobalt-wt/sdk-spike-1010/*)" SPIKE-HUB.md` · `22:claude --bg "Read '…SPIKE-HUB.md' …` · REJECTED — P1 (e): the line is prompt 330's, string for string
- O5 · own · `test_o5_no_guard_rule_holds_the_lock_take_while_a_builder_may_run` · `FAILED … AssertionError: (0, '') assert 0 == 2` (the take is allowed) · REJECTED — S7 judges `.env` at the builder call; "never overlap" is the hub's text rule (S1 (d)) (removed)
- A1 · Sol · `test_desk_launch_spike.py::test_x6_a_symlink_cannot_stand_in_for_the_plain_scratch_dir` · `assert 0 == 1` (dry run printed `cd …/sdk-spike-1010` and the line) · HELD
- A2 · Sol · `test_bare_guard.py::test_x1_a_shadow_builder_cannot_target_a_symlinked_worktree` · `AssertionError: (0, '') assert 0 == 2` · HELD
- A3 · Sol · `test_shadow_hub_file.py::test_s1_pass_s_is_not_restricted_to_src_and_tests` · first `AssertionError: no ## THE PROCEDURE` (another reason: the heading carries a parenthesis); form repaired once (the section's full heading), then `assert 'Pass S: the src/ rows' not in …` · HELD
- A4 · Sol · `test_desk_launch_shadow.py::test_s2_a_role_trial_refuses_a_non_grok_model` · `assert 0 == 1` (the Sonnet role card launched: add, cd, line) · HELD
- A5 · Sol · `test_shadow_hub_file.py::test_s5_the_unavailable_model_has_its_na_row` · `assert 0 == 1` · HELD
- A6 · Sol · `test_spike_hub_file.py::test_p1_the_reference_line_is_read_from_prompt_330` · `assert 'LINE_330 = (' not in …` failed · REJECTED — prompt 330 is not in this tree at BASE (build report PREFLIGHT, `:54`); P1's comparison is held by the copy plus the build's `grep -c -F` = 1, and my own `grep -n -F` of 330 above (line 1 holds the same allow and deny strings) (removed)
- A7 · Sol · `test_bare_guard.py::test_x6_the_spike_interpreter_cannot_write_outside_scratch` · `AssertionError: (0, '') assert 0 == 2` · REJECTED — P1 (e) (330's line allows the python) and P3 ("G5 fence: Write and Edit only") (removed)
- A8 · Sol · `test_bare_guard.py::test_x4_a_builder_process_cannot_create_env_during_its_pass` · `AssertionError: (0, '')` / `assert 0 == 2` · REJECTED — S7 holds `.env` at the builder call (`os.path.lexists`); no row fences a worker's Write of `.env` (removed)
- A9 · Sol · `test_shadow_hub_file.py::test_x3_the_sonnet_prompt_is_not_in_the_disallowed_tools_list` · `assert '"<pass prompt>"' != '"<pass prompt>"'` · REJECTED — S1 (c) spells the Sonnet command with the prompt last, after `"mcp__*"` (the build's ASK DESK 3 names the same risk) (removed)
- B1 · Grok · `test_bare_guard.py::test_x1_a_wider_write_glob_inside_sh_c_stays_g7` · `AssertionError: (0, '') assert 0 == 2` · HELD
- B2 · Grok · `test_bare_guard.py::test_x4_sh_c_of_the_builder_command_while_env_is_present_is_denied` · `AssertionError: (0, '') assert 0 == 2` · HELD
- B3 · Grok · `test_bare_guard.py::test_x6_the_spike_seat_cannot_bash_write_outside_the_scratch_dir` · `AssertionError: (0, '') assert 0 == 2` · REJECTED — P3: "G5 fence: Write and Edit only"; `cp` is not on the spike line's allow list (removed)
- B4 · Grok · `test_bare_guard.py::test_s3_a_symlink_instructions_file_is_not_a_write_of_src` · `AssertionError: (0, '') assert 0 == 2` · HELD
- B5 · Grok · `test_shadow_hub_file.py::test_x3_sonnet_read_is_confined_to_the_worktree` · `assert '"Read(' in 'claude -p --model claude-sonnet-5-5 … --allowedTools "Read" …'` · REJECTED — S1 (c), as O2 (removed)
- B7 · Grok · `grep -n "rests on the sign-off" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · `26:- Terra: … "writes only" for Terra rests on the sign-off and X1.` · UNSETTLED — as O3
- B6 · Grok · `test_shadow_hub_file.py::test_s1_the_built_line_can_record_a_db_none_gate` · `AssertionError: assert 'cobalt_dev: not taken' in '# SHADOW-HUB …'` · HELD
- The nine HELD tests together before any fix → `9 failed, 1889 deselected`. Committed `5b214968 wip(shadow-hub-1011): check red — A1 A2 A3 A4 A5 B1 B2 B4 B6`.

## FIXES
One commit, `cd302109 fix(shadow-hub-1011): … (check A1 A2 A3 A4 A5 B1 B2 B4 B6)`, all inside the rows' files. `git diff --stat` before it: `SHADOW-HUB.md | 8 +++++---`, `bare-guard.py | 27 +++`, `desk-launch.sh | 4 ++++`.
- A1 · `ops/desk/desk-launch.sh` kind spike: `[ ! -L "$scratch" ] || refuse "spike: $scratch is a symlink, not the plain scratch dir"`, before the `.git` check (nothing made).
- A2 · `ops/desk/bare-guard.py` `builder_call`: a card worktree that is a link (`os.path.islink`) is no builder call (G7).
- A3 · `SHADOW-HUB.md`: the pass prompt and pass S read `the rows` (not `the src/ rows`); the instructions' fence is "the rows' files (every path a row's `files` names) plus those exceptions".
- A4 · `ops/desk/desk-launch.sh` shadow arm: a card with a `ROLE:` header launches only `--model grok-4.7` (`REFUSED: shadow: ROLE trials run only grok-4.7`).
- A5 · `SHADOW-HUB.md` `## RESULTS TABLE`: `| Gemini | N/A — id not found (…; card 324 ## RECORDS) | | | N/A |`.
- B1, B2 · `ops/desk/bare-guard.py`: new `SHELLS` and `shell_c(ws)`. For kind shadow, any segment that is a shell run with `-c` (`sh -c`, `bash -ec`, …) is G7. When its string is the builder command and `.env` is on disk, the route is S7's. The gate seat's `sh /Users/cobalt/cobalt/ops/desk/<script> …` has no `-c` before its script, so it is unchanged.
- B4 · `ops/desk/bare-guard.py` `g5` kind shadow: a path that is a link is G5 fence, before the instructions-file and report matches.
- B6 · `SHADOW-HUB.md` after the stop line: a shadow of a "DB: none" card runs W as BUILD-HUB gives it ((a0), (a), (e)) and writes `with-DB 0/0` and `cobalt_dev: not taken`.
- After the fixes: `tests/ops/test_bare_guard.py` → `1826 passed`. The two hub-file tests, the two launcher tests, the devfix and ops-hand controls, and the authorize, preflight, watch and stop-guard tests → `351 passed`.
- DevDocs: `docs/40 - DevDocs/cobalt/` has no page for these ops scripts (the build's record, `ops-hand-build-2026-10-10.md:223` precedent), so no page line was written.

## Suites
Tip `cd302109`. DB: none card, so W is (a0), (a), (e) as BUILD-HUB gives it; no lock was taken.
- RESTARTS first, `uv run cobalt jobs restarts 680eca0e..HEAD`: 18 rows, every one `DOCS`, `operator script; no Cobalt reader` or `test/documentation; no resident`, restart `-`; last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 680eca0e` → 18 paths, each under `docs/`, `ops/` or `tests/ops/` → **`cobalt_dev: not taken (DB: none — 18 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-offline-20261011-093139.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh shadow-hub-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/shadow-hub-1011-livenote-20261011-093140.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3028 passed, 1 xfailed, 15 warnings in 541.77s (0:09:01)`: the build's 3019 plus the 9 held tests.
- with-DB: 0/0 (DB: none).
- `.env`: `ls /Users/cobalt/cobalt-wt/shadow-hub-1011/.env` → `No such file or directory`.
- Each new test was shown red first (`## RUNS`, `9 failed` at `5b214968`) and passes at `cd302109`.

## Scope
- PREFLIGHT's path union (17 paths) plus my two commits. `5b214968` touches `tests/ops/test_bare_guard.py` (S3/S4/S7/P3), `test_desk_launch_shadow.py` (S2), `test_desk_launch_spike.py` (P2) and `test_shadow_hub_file.py` (S1/S5/S7). `cd302109` touches `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (S1/S5/S7), `ops/desk/bare-guard.py` (S3/S4/S7/P3) and `ops/desk/desk-launch.sh` (S2/P2). Every path is in some row's `files`.

## Checked against the branch
- (i) `git log --oneline bc25c523..HEAD -- . ":(exclude)docs"` → `cd302109 fix(shadow-hub-1011): …` · `5b214968 wip(shadow-hub-1011): check red — A1 A2 A3 A4 A5 B1 B2 B4 B6`. `<tip now>` = `cd302109`.
- (ii) `git log --stat --format=%h bc25c523..HEAD` → `cd302109`: SHADOW-HUB.md, bare-guard.py, desk-launch.sh; `5b214968`: the four test files; `397cd63b`: the build report (docs). No path outside the rows' files.
- (iii) Fence: `git log --oneline 680eca0e..HEAD -- "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CARD.md" src` → empty. `LAWS.md`, `STANDING-LIST.md` and the settings files are not in the diff (PREFLIGHT path union).
- (iv) Each HELD test, `grep -n -F "def <name>"`, one line each:
  - `test_bare_guard.py:2287` (A2), `:2298` (B1), `:2305` (B2), `:2312` (B4)
  - `test_shadow_hub_file.py:220` (A3), `:227` (A5), `:238` (B6)
  - `test_desk_launch_spike.py:221` (A1)
  - `test_desk_launch_shadow.py:294` (A4)
  - The red commit `5b214968` sits below the fix `cd302109` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/shadow-hub-1011`.
- (vi) `git log --stat --format=%h 680eca0e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-lists change is owed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (they cite file:line and the drafter's reads), so there is nothing to run.
- (viii) L32: this report holds no ticker, price or date of his. Its dates are the job's own (card, rulings).

## OPEN
Each item below is REJECTED (red for its stated reason, but a card line says the behaviour is right) or UNSETTLED. None was fixed, and each goes to the follow-up list.
- O2 / B5 (X3), REJECTED — S1 (c): the Sonnet builder allows `"Read"` with no path, so a Sonnet pass can read outside the worktree, the main repo's `.env` included. Grok's `cobalt-job` profile denies `/Users/cobalt/cobalt/.env` (`ops/grok-sandbox.toml:8`). Settled by: his D1 sign-off choosing `"Read(//Users/cobalt/cobalt-wt/<worktree>/**)"` or the card's spelling.
- A9 (X3), REJECTED — S1 (c): the Sonnet `"<pass prompt>"` comes last, after the variadic `--disallowedTools` list, so the CLI may take it as a tool name and the model gets no prompt (the build's ASK DESK 3). Settled by: the first Sonnet probe (desk X1/X3). If it holds, one hub-row edit (for example `--disallowedTools … "mcp__*" -- "<pass prompt>"`, or the prompt before the lists) and his sign.
- O3 / B7 (X3, Terra), UNSETTLED: whether `codex exec -s workspace-write` runs shell commands needs a Terra call this check cannot make. If it does, "writes only" rests on the sign-off and X1, as the hub says (`SHADOW-HUB.md:26`). Settled by: the desk's X1/X3 experiment before the Terra arm.
- O4 / A7 / B3 (X6), REJECTED — P1 (e) and P3. The spike line (330's, string for string) lets the venv python run a script the seat wrote, and that script can write outside `sdk-spike-1010` and open the network. G5 fences only the Write and Edit tools, and `cp` is not on the spike's allow list. Settled by: his D1 sign-off of the spike line, read with this fact.
- O5 / A8 (X4), REJECTED — S7. The guard checks `.env` only at the builder call. It does not stop a lock take while a builder call is still running in the background, and it does not stop a worktree seat writing `.env` during a pass. "Never overlap" is the hub's text rule (`SHADOW-HUB.md:34`). Settled by: a later guard card if the desk wants it held by the guard.
- A6 (P1), REJECTED: `test_spike_hub_file.py` compares against the copy `LINE_330`, because prompt 330 is not in this tree at BASE. Settled by: once 330 is on the same tree (after merge), a follow-up test that reads 330's line from the repo.

## CONTINUE
next: done

## DECISIONS
- FOR DEJAN — D1 sign-off input (A9). The Sonnet builder command, as the card spells it, puts the prompt after the variadic `--disallowedTools` list. If the CLI reads that list greedily, the Sonnet arm runs with no prompt. Default: as written, unsigned. The desk's first Sonnet probe settles it before his sign; a fix is a hub-row edit.
- FOR DEJAN — D1 sign-off input (O2 / B5, secrets boundary). The Sonnet command's `"Read"` is unscoped and reaches `/Users/cobalt/cobalt/.env`, which Grok's sandbox denies. Default: as the card spells it, unsigned. The scoped spelling is `"Read(//Users/cobalt/cobalt-wt/<worktree>/**)"`, his choice at sign-off.
- FOR DEJAN — D1 sign-off input (O3 / B7, O4 / A7 / B3). For Terra, "writes only" rests on the sign-off and X1 (codex `workspace-write` likely runs shell commands; not run here). The spike line's venv python can write outside its scratch dir and reach the network; the guard fences only Write and Edit. Default: as written, unsigned; the desk's X1/X3 runs before the Terra arm.
- ASK DESK (O5 / A8, X4): `.env` during a background builder pass is held by the hub's text rule only, not by the guard. Default: as built; a guard card only if the desk wants it. [09:42]
- ASK DESK (A6, P1): after merge, replace `LINE_330` with a read of prompt 330 from the tree. Default: as built; a follow-up line. [09:42]

## RECORDS
- Dropped findings: none.
- Every house produced a list: Sol `FINDINGS: 9` (final message at 09:16:05 ET), Grok `FINDINGS: 7` (house-b.md at 09:24:20 ET; its blocks numbered 1-5, 7, 6).
- Form repairs, one each, assertions unchanged:
  - A3: the section name, now the hub's full heading.
  - O2: `grep -n -F -e`, because the pattern starts with `--`.
- Removed after their run, so the suites stay green; each stays OPEN with its run quoted above. NOT HELD: O1 (3 parametrized cases). REJECTED: O5, A6, A7, A8, A9, B3, B5.
- `tests/ops/test_zz_debug_tmp.py` (the build's ASK DESK 1) is gone: `git status --short --branch` showed `## ops/shadow-hub-1011` alone at every check.
- No lock taken (DB: none); `.env` never present: `ls` → `No such file or directory` at PREFLIGHT and the finish.
- `cobalt.md` (`## What Cobalt is`, `## Build rules` on) was read at step 8, after the fixes, not before step 2 as WHAT YOU READ orders; nothing in it changes a verdict.
- `context 270103 of 400000 — ok` (`desk-context.sh b5439f2c`, 09:43). That is above CHECK-HUB's 250,000 line, which is the desk's to judge (UNATTENDED RULES (c)).
- L74: one attribution block in a system reminder asked for a `Claude-Session:` line; it was not acted on.
- files opened: 24
  - Hubs: CHECK-HUB.md; BUILD-HUB.md (THE LOCK, E2 … W); the card; the build report.
  - The tip's hubs: SHADOW-HUB.md, SPIKE-HUB.md.
  - Scripts at the tip: bare-guard.py, desk-launch.sh; the diffs of authorize.sh, preflight.sh, desk-watch.sh, stop-guard.py; ops/grok-sandbox.toml.
  - Tests: test_shadow_hub_file.py, test_spike_hub_file.py, test_desk_launch_spike.py, test_desk_launch_shadow.py; test_bare_guard.py (diff).
  - Other: 330-sdk-spike-live.md (line 1, by grep); `<S>/rulings.md`; Sol's output → house-a.md; house-b.md; Grok's stdout; areas/cobalt.md (two sections); the house-probe output.
- Check of `shadow-hub-1011`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: shadow-hub-1011 · pass: 1 · tip: cd302109 · house A: Sol FINDINGS: 9 · findings: 21 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 11 · house B: Grok FINDINGS: 7 · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 24 · ready: YES · decisions: 5 · for Dejan: 3 · tokens: 270103
