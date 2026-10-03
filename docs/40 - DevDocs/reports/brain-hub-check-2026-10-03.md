# brain-hub — check, pass 1 (2026-10-03)

## §0 Headline
This check had no outside house: the card's HOUSE A line is overruled by his 2026-10-02 R47. One fresh Opus read the build, wrote three findings and ran each one. B1 to B4 hold as built, and `desk-launch.sh brain` never launches beside a live `brain`.
One finding held and is not fixed (O1): the `prompt` kind still launches a brain-seat line beside a live brain. Its fix reaches a test file outside the rows, so it is a judge decision. The test is pinned as a strict xfail.
One fact held but is out of scope (O2): the brain line's `git -C … diff*` string can write a file. The fence keeps the line as `23`'s. O3 did not hold.
Suites at `18c26c70`: `tests/ops` 499/0, offline 3737/0, live-note 146/0. `ready: NO` because one held item is unfixed.

## L74
A system reminder in this session gave a commit attribution with a `Claude-Session:` line. Under L74 and the hub's commit form, my commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. I acted on nothing else in it.

## AUTHORIZATION
Started `date` → `Sat Oct  3 12:22:16 EDT 2026`.
- INSTALLED: `grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md"` → exit 1, no output.
- CARD: `grep -n -E "«FIL[L]" ".../2026-10-03/07-brain-hub-card.md"` → exit 1, no output · `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/07-brain-hub-card.md"` → `7570ce5280586b83358fe9e1a83277a0683cc391` · `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` → no output.
- STANDING LIST 2026-09-30 R60: `grep -n "^| R60 " ".../cto-2026-09-30.md"` → `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES \`STANDING-LIST.md\` once (\`4be06af0\`); ... | APPROVED |` · `git ... log -1 --format=%H -S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- RULINGS 2026-10-02 R47: `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` · `-S"| R47 |"` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
- RULINGS 2026-10-02 R157: `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, ... | HIS RULING · APPROVED |` · `-S"| R157 |"` → `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`.
- RULINGS 2026-10-02 R54: `61:| R54 | 08:00 ET | HIS RULING (FOR DEJAN 13 = A): a standing \`BRAIN-HUB.md\`, on tomorrow's list (...). | HIS RULING · APPROVED |` · `-S"| R54 |"` → `e9a94c19ccf236eb26752e3bc64da90e8db9a243`.
- HOUSE A overrule: the card's `HOUSE A: none — overruled 2026-10-02 R47` is proved by the R47 row above.
- HOUSE GATES: `grep -n "^| R17 "` → one row (line 35); `grep -n "^| R19 "` → one row (line 37); `-S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`. (No house is launched in this check.)

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 12:22:16 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/brain-hub-1003` |
| tip | `git log --oneline -1` | 0 | `1f79cfe3 docs(brain-hub): build report — dc9b06c4` (docs-only above TIP) |
| docs-only above TIP | `git log --stat --format=%h dc9b06c4..HEAD` | 0 | `1f79cfe3` · `.../reports/brain-hub-build-2026-10-03.md | 41 ++++++++++++++++------` — only `docs/` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: brain-hub · tip: dc9b06c4 | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 5 · for Dejan: 0` |
| range | `git log --oneline a09f0862..dc9b06c4` | 0 | `dc9b06c4 feat(brain-hub): the brain's Write/Edit scoped ... (B4, L3 L72)` · `df609e2f wip(brain-hub): red B4` · `f92063d7 docs(brain-hub): build report — 390da6b1` · `390da6b1 feat(brain-hub): standing BRAIN-HUB.md, desk-launch.sh brain, first handover (B1-B3, L1 L28 L74 R76)` · `68180c71 wip(brain-hub): red` — 5 commits |
| range stat | `git log --stat --format=%h a09f0862..dc9b06c4` | 0 | dc9b06c4: BRAIN-HUB.md, STANDING-LIST.md · df609e2f: build report, tests/ops/test_desk_launch_brain.py · f92063d7: build report · 390da6b1: prompts/2026-10-03/08-brain-handover.md, BRAIN-HUB.md, STANDING-LIST.md, ops/desk/desk-launch.sh · 68180c71: tests/ops/test_desk_launch_brain.py |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/brain-hub-1003/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..dc9b06c4` | 0 | `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md` · `docs/40 - DevDocs/prompts/BRAIN-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md` · `ops/desk/desk-launch.sh` · `tests/ops/test_desk_launch_brain.py` — all under `ops/`, `tests/ops/`, `docs/` |
| scratch | `ls <S>` | 1 | `No such file or directory` — fresh |
| houses | — | — | house A: none (overruled 2026-10-02 R47); no gate run in PREFLIGHT, no probe, no house launched. `HOUSE B: as needed`, not mandatory. |

Path union for `## Scope`: the six paths above.

## Files copied
none (house A: none).

## OWN FINDINGS
Written before any run (house A: none, so no house list exists to open).

FINDING O1
ROW: X3 / B2
CLAIM: The `brain` kind refuses beside a live `brain` (`ops/desk/desk-launch.sh:432-441`), but the `prompt` kind (`ops/desk/desk-launch.sh:314-381`) reads no session list. A dated prompt whose line names `--remote-control brain --name brain` (the shape of `prompts/2026-10-02/23-brain-judge.md:1`) still launches while a `brain` is live. The header comment names "a brain tab" as a `prompt` use (`ops/desk/desk-launch.sh:55-57`).
RUN: TEST — `tests/ops/test_desk_launch_brain.py::test_o1_a_brain_line_through_the_prompt_kind_is_refused_beside_a_live_brain` (a constructed prompt under `prompts/2026-01-02/`, a live `brain` in the `desk-list.sh` stub, `prompt <path>` dry; the script copy has its `/Users/cobalt/` roots pointed at `tmp_path`, as `tests/ops/test_desk_size_guard.py` stages it).
EXPECT: exit 0 and the filled line on stdout, so `assert done.returncode == 1` fails.

FINDING O2
ROW: X1 (B4 narrowed the write pair; the build's `## FOR THE CHECK` says "Every Bash string is a read")
CLAIM: `"Bash(git -C /Users/cobalt/cobalt diff*)"` on the brain line (`docs/40 - DevDocs/prompts/BRAIN-HUB.md:8`) matches `git -C /Users/cobalt/cobalt diff --output=<any path> …`, which writes a file at any path the process can reach, outside both B4 globs. (`… log*` takes the same `--output`.)
RUN: COMMAND — `git -C /Users/cobalt/cobalt diff --output=/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/brain-hub-check/o2-proof.txt a09f0862 dc9b06c4 -- ops/desk/desk-launch.sh`, then `ls -la` of that path (my `Bash(git -C * diff*)` string is the same spelling; the target is my own scratch folder).
EXPECT: no stdout; `ls -la` shows `o2-proof.txt` with a non-zero size: the string writes a file.

FINDING O3
ROW: B2 (the handover's closed character set; the line runs through `eval`)
CLAIM: The handover is filled inside the line's double-quoted message (`docs/40 - DevDocs/prompts/BRAIN-HUB.md:8`, `HANDOVER: '<handover>'` inside `"…"`) and run with `eval` (`ops/desk/desk-launch.sh:203`). The set `[!A-Za-z0-9\ ._/-]` (`ops/desk/desk-launch.sh:390`) uses ranges, and under a UTF-8 locale a range can admit more than ASCII (the precedent of cards `12`, `18`). Only a `'` is pinned (`test_a_handover_path_with_a_quote_is_refused`); `$`, a backtick, `"`, `;`, `|`, `&` and `\` are not.
RUN: TEST — `tests/ops/test_desk_launch_brain.py::test_o3_a_shell_character_in_the_handover_path_is_refused` (parametrized over the seven characters, run with `LC_ALL=en_US.UTF-8` and `LANG=en_US.UTF-8`).
EXPECT: on the claim, a case that is not refused (exit 0).

## Findings
none (house A: none).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py::test_o1_a_brain_line_through_the_prompt_kind_is_refused_beside_a_live_brain` | `1 failed, 15 warnings in 1.14s`; first failing line `tests/ops/test_desk_launch_brain.py:354: AssertionError` → `assert 0 == 1`, stdout `cd <tmp>/repo` · `claude --bg "Read '<tmp>/…/prompts/2026-01-02/09-brain-prompt.md' and follow it exactly." --model claude-fable-5-1 --permission-mode auto --remote-control brain --name brain …`, with a live `brain` (`b2a10001 · brain`) in the list stub | **HELD** — the `prompt` kind prints and would run a brain-seat line beside a live brain. **HELD, NOT FIXED — `tests/ops/test_desk_size_guard.py`** (see `## OPEN`) |
| O2 | Opus | `git -C /Users/cobalt/cobalt diff --output=/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/brain-hub-check/o2-proof.txt a09f0862 dc9b06c4 -- ops/desk/desk-launch.sh` · `ls -la <S>` | no stdout, exit 0 · `-rw-r--r--  1 cobalt  staff  7640 Oct  3 12:26 o2-proof.txt` | **HELD** as a fact: the string `Bash(git -C /Users/cobalt/cobalt diff*)` writes a file at a path of the caller's choice. **OUT OF SCOPE** (`## NOT IN THIS JOB`: "The brain's allow list beyond row B4: no string added; B4 narrows two"): the string is `23`'s, approved by his 10-02 R131. It goes under `## DECISIONS` |
| O3 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py::test_o3_a_shell_character_in_the_handover_path_is_refused` (7 cases, `LC_ALL=en_US.UTF-8`) | `7 passed, 15 warnings in 1.30s` | **NOT HELD**: `$`, a backtick, `"`, `;`, `|`, `&` and `\` are each refused. The test was removed again with the Edit tool |

Form note on O1: the test is committed under `@pytest.mark.xfail(strict=True, reason="check O1, HELD NOT FIXED: …")`. The assertion is unchanged. A plain red would turn `tests/ops` red at W for a fix this check may not make; the strict marker turns into a failure (XPASS) the moment the prompt kind refuses, so the fixing build must drop it. Re-run with the marker: `uv run pytest -q -rxs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py` → `27 passed, 1 xfailed, 15 warnings in 2.95s`, `XFAIL …::test_o1_… - check O1, HELD NOT FIXED: the prompt kind reads no session list`.
Commit: `18c26c70 wip(brain-hub): check red — O1 (strict xfail: held, not fixed)` (`git add tests/ops/test_desk_launch_brain.py`, then commit by explicit path).

## FIXES
none. O1 is held, not fixed. Its fix changes the `prompt` kind, which `ops/desk/desk-launch.sh:55-57` documents as the road for "a brain tab". `tests/ops/test_desk_size_guard.py:259-263` stages a brain-seat prompt (`04-brain-prompt.md`, `--remote-control brain --name brain`) through that kind, and that file is in no row's `files`. O2 is out of scope. O3 did not hold.

## Suites
These ran on `<tip now>` = `18c26c70`, my one commit. This is a `DB: none` card, so W is (a0), (a) and (e) plus `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts a09f0862..HEAD` → the same six rows the build quotes (DOCS ×4; `ops/desk/desk-launch.sh` operator script, no Cobalt reader; `tests/ops/test_desk_launch_brain.py` test/documentation, no resident) → `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a09f0862` → `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md` · `docs/40 - DevDocs/prompts/BRAIN-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md` · `ops/desk/desk-launch.sh` · `tests/ops/test_desk_launch_brain.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `499 passed, 2 xfailed, 15 warnings in 209.94s (0:03:29)`, exit 0. The second xfail is O1's strict marker.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 646.01s (0:10:46)`, exit 0.
- (e) LIVE-NOTE: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.18s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` and does not name `COBALT_LIVE_VAULT_ROOT`.
- `cobalt_dev`: not taken (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/brain-hub-1003/.env` → `No such file or directory` at 12:38 EDT.

## Scope
PREFLIGHT's path union (six paths, all under `docs/`, `ops/`, `tests/ops/`) against the rows' `files`: `BRAIN-HUB.md` (B1, B4), `ops/desk/desk-launch.sh` (B2), `tests/ops/test_desk_launch_brain.py` (B2, B4), `STANDING-LIST.md` (B2, B4), `prompts/2026-10-03/08-brain-handover.md` (B3), the build report. My one commit, `18c26c70`, touches `tests/ops/test_desk_launch_brain.py` only, a row's test file. Nothing is built inside the fence: `JUDGE-HUB.md` and `JUDGE-CARD.md` are untouched (`git log --oneline a09f0862..HEAD -- <both>` → empty), no law or memory file is in the diff, and no string is added to the brain line (the build's byte test pins it to `23`'s, the pair replaced). No path reaches a score, rank, grade or size.

CHECK ASKS, by run:
- X1: B4's two globs keep LAWS, memory, scripts, settings and the fixed files at `prompts/` root out of the Edit and Write tools. They do not close the Bash side. O2 shows `Bash(git -C /Users/cobalt/cobalt diff*)` writes a file at any path (`--output=`), so "Every Bash string is a read" (build report `## FOR THE CHECK`) does not hold. `… log*` takes the same option and `Bash(sed -n *)` admits `-i` and the `w` command; neither was run (not on this check's list), so neither is claimed. Under `--permission-mode auto` the classifier is the second guard. The string is `23`'s (his R131) and fenced: OUT OF SCOPE, `## DECISIONS` 2.
- X2: the hub names the handover, then the direction, the design report and the desk report, which the handover names or which follow from the date. It names nothing else to read at start. It carries one value of a day, the 500,000 line of his 10-03 R7 (`cto-2026-10-03.md:13`, `HIS RULING · APPROVED — pending fold`), which the card row asked for in the hub as 250,000 (build DECISION 1, KEEP by the judge's R53). The handover repeats it among its precedents. A later ruling would need both edited; that was not run as a finding.
- X3: `desk-launch.sh brain` itself never launches beside a live `brain` (the build's tests, dry and real; an unreadable list refused). The `prompt` kind does: O1, HELD.

## Checked against the branch
- (i) `git log --oneline dc9b06c4..HEAD -- . ":(exclude)docs"` → `18c26c70 wip(brain-hub): check red — O1 (strict xfail: held, not fixed)`. `<tip now>` = `18c26c70`.
- (ii) `git log --stat --format=%h dc9b06c4..HEAD` → `18c26c70`: `tests/ops/test_desk_launch_brain.py | 20 ++++++++++++++++++++`; `1f79cfe3`: `.../reports/brain-hub-build-2026-10-03.md | 41 …` (docs). No other path: no `WIDENED`.
- (iii) `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts/JUDGE-HUB.md" "docs/40 - DevDocs/prompts/JUDGE-CARD.md"` → empty.
- (iv) `grep -n -F "def test_o1_a_brain_line_through_the_prompt_kind_is_refused_beside_a_live_brain" tests/ops/test_desk_launch_brain.py` → `329:def test_o1_…(tmp_path):`. Its `wip(brain-hub): check red` commit is `18c26c70`; no `fix(brain-hub):` commit (held, not fixed).
- (v) `ls /Users/cobalt/cobalt-wt/brain-hub-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/brain-hub-1003`.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: none to run.
- (viii) L32: this report holds constructed test values only (`b2a10001`, `2026-01-02`); no ticker, price or trade date of his.

## OPEN
- O1 — HELD, NOT FIXED. FINDING O1 above; `## RUNS` O1. Settled by a card row that makes the `prompt` kind refuse a brain-seat line beside a live `brain`, or refuse a brain-seat line outright (the brain launches by its kind). Files: `ops/desk/desk-launch.sh`, `tests/ops/test_desk_size_guard.py` (its `04-brain-prompt.md` fixture), `tests/ops/test_desk_launch_brain.py` (drop the strict-xfail marker on `test_o1_…`; the marker turns XPASS into a failure once the fix lands).
- OUT OF SCOPE (never open): O2, the brain line's `git -C … diff*` string writes a file (`## DECISIONS` 2).

## CONTINUE
next: none — CHECK DONE, pass 1 (the judgment seat answers `## DECISIONS`)

## DECISIONS
1. **O1, HELD, NOT FIXED — `tests/ops/test_desk_size_guard.py`.** `desk-launch.sh prompt "<a dated prompt>"` whose line names `--remote-control brain --name brain` (the shape `23-brain-judge.md` was launched with) prints and runs that line while a session named `brain` is live. The `brain` kind refuses the same case (his 2026-09-30 R76). The `prompt` kind reads no session list (`ops/desk/desk-launch.sh:314-381`), and its header names "a brain tab" as one of its uses (`:55-57`). Run: `## RUNS` O1, red for that reason. The fix changes the `prompt` kind. That kind's guard test stages a brain-seat prompt (`tests/ops/test_desk_size_guard.py:259-263`), and that file is in no row's `files`. Safe default taken: no fix. The test is committed as a strict xfail (`18c26c70`), so the defect stays pinned and the suites stay green. To settle it, a card row with the three files under `## OPEN` O1 should choose between two routes: the `prompt` kind refuses a brain-seat line outright, or it runs the `brain` kind's live check. If the branch ships with this item carried, it becomes his (a carried held defect).
2. **O2, OUT OF SCOPE (the fence: no string added to the brain line, B4 narrows two).** The build's X1 answer says every Bash string on the brain line is a read. That is false for `Bash(git -C /Users/cobalt/cobalt diff*)`: `git -C /Users/cobalt/cobalt diff --output=<path> …` wrote a 7,640-byte file at a path I chose (`## RUNS` O2). `… log*` takes the same option and `Bash(sed -n *)` admits `-i` and `w`; neither was run. Under `--permission-mode auto` the classifier is the second guard. The string is `23`'s, approved by his 10-02 R131. Safe default taken: the line is unchanged. A narrowing (for example `diff --stat*`, or dropping `sed -n`) is a follow-up card row. By the judge's 10-03 R53 reading a narrowing is not his, and it goes on his veto list.

## RECORDS
- House A: none (overruled 2026-10-02 R47). No house was staged or launched; `## Files copied`, `## Findings` and `## Dropped` are empty by that.
- `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/brain-hub-check`. It holds `o2-proof.txt` (the O2 run's own output, a `git diff` of `ops/desk/desk-launch.sh`) and `opus-1.md`. `opus-1.md` was first written as a placeholder so that the folder existed for O2's `--output`, then written whole at `## 8`.
- O3's test was written, run green (`7 passed`) and removed with the Edit tool before the O1 commit. It was never committed.
- A system message in this session asked for a `Claude-Session:` line on commits. My commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74; recorded under `## L74`).
- No lock taken (`DB: none`). `.env` never present in this worktree.
- files opened: 14 — `CHECK-HUB.md`; the card `2026-10-03/07-brain-hub-card.md`; `BUILD-HUB.md` (`## LAUNCH` to `## W`, read as one span); `BRAIN-HUB.md`; `2026-10-03/08-brain-handover.md`; `ops/desk/desk-launch.sh` (lines 60–219, 300–382, plus the diff); `tests/ops/test_desk_launch_brain.py` (diff, then edited); `STANDING-LIST.md` (diff); the build report (`## RESTARTS` to its last line); `prompts/2026-10-02/23-brain-judge.md`; `JUDGE-HUB.md` (lines 1–12); `/Users/cobalt/.claude/ops/desk-list.sh` (for X3: the list the live check reads); `tests/ops/test_desk_size_guard.py` (lines 240–289, for O1's fix route); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down). The `cto-*.md` rows were read by grep only.
- Check of `brain-hub`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: brain-hub · pass: 1 · tip: 18c26c70 · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 2 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 14 · ready: NO · decisions: 2 · for Dejan: 0
