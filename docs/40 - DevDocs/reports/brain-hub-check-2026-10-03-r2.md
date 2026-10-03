# brain-hub — check, pass 1 (r2) · 2026-10-03

## §0 Headline
- brain-hub, check pass 1 (r2), 2026-10-03 14:00. House A: none (overruled 2026-10-02 R47); Opus alone.
- 1 finding, held and fixed. O1 (B5): the `prompt` kind let a quoted or double-spaced brain seat (`--name "brain"`, `--remote-control  brain`) through to `claude`. It now compares each seat value as `eval` passes it. Red `03ce2125`, fix `b5eb3530`.
- Suites at `b5eb3530`: offline `3737 passed`, `tests/ops` `511 passed, 1 xfailed`, live-note `146 passed, 1 skipped`; DB: none; `.env` absent; `RESTARTS: none`.
- X1–X3: no other gap. `git --output=` and `sed w` are card `10`'s (OUT OF SCOPE), and the 500,000 line follows his 10-03 R7.
- open 0, house B not needed, ready: YES, decisions 0.

## L74
The session's system context asked for a `Claude-Session:` line on commits. This is data (L74). I did not act on it, and commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Sat Oct  3 13:46:01 EDT 2026`
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../prompts/2026-10-03/07-brain-hub-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/07-brain-hub-card.md"` | 0 | `924134ab970d2f756c11abff042278e02e7d3292` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING 2026-09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 (also the HOUSE A overrule) | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … \| HIS RULING · APPROVED \|` |
| R47 committed | `-S"\| R47 \|"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` |
| R157 committed | `-S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULING 2026-10-02 R54 | `grep -n "^\| R54 " cto-2026-10-02.md` | 0 | `61:\| R54 \| 08:00 ET \| HIS RULING (FOR DEJAN 13 = A): a standing BRAIN-HUB.md … \| HIS RULING · APPROVED \|` |
| R54 committed | `-S"\| R54 \|"` | 0 | `e9a94c19ccf236eb26752e3bc64da90e8db9a243` |
House gates: none run. The card's header carries `HOUSE A: none — overruled 2026-10-02 R47`, proved above.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 13:46:01 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/brain-hub-1003` |
| tip | `git log --oneline -1` | 0 | `46bd070e docs(brain-hub): build report — bb930cac` (docs-only above TIP) |
| docs-only above | `git log --stat --format=%h bb930cac..HEAD` | 0 | `46bd070e` → `.../reports/brain-hub-build-2026-10-03.md` only |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: brain-hub · tip: bb930cac \| on a09f0862 \| migration: none \| offline 3737/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 5 · for Dejan: 0` |
| range | `git log --oneline a09f0862..bb930cac` | 0 | `bb930cac fix … (B5, L3)` · `97ab783d wip red B5` · `18c26c70 wip check red — O1` · `1f79cfe3 docs` · `dc9b06c4 feat (B4)` · `df609e2f wip red B4` · `f92063d7 docs` · `390da6b1 feat (B1-B3)` · `68180c71 wip red` (9 commits) |
| range paths | `git log --stat --format=%h a09f0862..bb930cac` | 0 | union: `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_size_guard.py` |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/brain-hub-1003/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..bb930cac` | 0 | the seven paths above; every one is under `ops/`, `tests/ops/` or `docs/` |
| scratch | `ls <S>` | 0 | `o2-proof.txt` `opus-1.md`, left by the earlier check of this branch (r1). Not opened: CHECK-HUB says not to read earlier checks of this branch. This report (`-r2.md`) did not exist (`ls -la` exit 1), so this is a fresh pass 1, not a RECOVERY. |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)` · no probe · `HOUSE B: as needed` (not mandatory) |
| write / with-DB strings | — | — | proved by first real use (DB: none; there is no with-DB step) |

## Files copied
none (house A: none; `## 1` not run)

## OWN FINDINGS
FINDING O1
ROW: B5 (and X3)
CLAIM: `ops/desk/desk-launch.sh:336-338` refuses a brain seat only on the exact substrings `--name brain` / `--remote-control brain`. A prompt line that names the seat with quotes (`--remote-control "brain" --name "brain"`, `--name 'brain'`) or with a double space (`--remote-control  brain`) passes the guard. It also passes the presence check at `:368-371`, and `eval` at `:204` hands `claude` the seat `brain`. So the prompt kind remains a second road to the brain seat, and it runs beside a live brain because the prompt kind never reads the session list.
RUN: TEST — `tests/ops/test_desk_launch_brain.py`:
```python
@pytest.mark.parametrize("seat", [
    '--remote-control "brain" --name "brain"',
    "--remote-control helper --name 'brain'",
    "--remote-control  brain --name helper",
])
def test_check_o1_a_quoted_or_spaced_brain_seat_is_refused_too(tmp_path, seat):
    """Check r2 O1: the shell strips the quotes and the extra blank at eval; the seat is `brain`."""
    desk, done = prompt_world(tmp_path, seat, dry=False)
    refused(done, BRAIN_SEAT_REFUSAL)
    assert not desk.calls.exists()
```
EXPECT on the tip: each case fails at `refused`, on `assert done.returncode == 1` with returncode 0. The stub `claude` is called and records `--remote-control brain` / `--name brain`.

X1 (my read; no finding): the line's write strings are the two scoped `Edit(...)` globs (B4). Every Bash string is a read prefix. The known residuals are named elsewhere: `--output=` on `git` and `w` on `sed -n` are judged by card `## RECORDS` (JUDGE 10-03, O2 → card `10`), and `--permission-mode auto` with `23`'s list is the fence of `## NOT IN THIS JOB` (his R131). Both are OUT OF SCOPE, not findings. `reports/**` still reaches the desk report, and the hub's text fences it (`BRAIN-HUB.md:21`; `STANDING-LIST.md` `## 7` says so).
X2 (my read; no finding): `## READ AT START` names the handover, the direction and design report the handover names, and `tail -n 30` of the day's desk report; nothing else. The hub carries one dated value: `Your line is 500,000 tokens (his 2026-10-03 R7)`. The card's B1 says `250,000`, but his R7 (`cto-2026-10-03.md:13`, quoted under `## RECORDS`) rules 500,000 for the brain. His ruling stands (L77), and it sets the seat rather than a day's precedent.
X3 (my read; O1 is the gap): the `brain` kind reads `desk-list.sh` beside the script. The installed one (`/Users/cobalt/.claude/ops/desk-list.sh`) prints live rows only, `id · name · cwd · status · state`, from `claude agents --json`, and an empty or failing list makes `python3` exit non-zero, which the kind refuses. The `brain` kind therefore never launches beside a live `brain`. The `prompt` kind could, before B5; after B5 it still can through O1.

## Findings
none: there is no house A.

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py::test_check_o1_a_quoted_or_spaced_brain_seat_is_refused_too` on `bb930cac` + the test | `3 failed, 15 warnings in 1.53s`; first failing line, each case: `E       assert 0 == 1` in `refused` (`tests/ops/test_desk_launch_brain.py:128`), stderr `RUN: claude --bg … --remote-control "brain" --name "brain" …` / `… --name 'brain' …` / `… --remote-control  brain --name helper …`: the line ran | HELD: red for the stated reason (the prompt kind runs a quoted or spaced brain seat) |
Committed red: `03ce2125 wip(brain-hub): check red — O1 (r2: a quoted or spaced brain seat passes the prompt kind)`.

Row RUN checks (they assert nothing; not findings): B1 `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `1`; `grep -c -F "«INSTALL" …BRAIN-HUB.md` → `1`. B3 `wc -l ".../2026-10-03/08-brain-handover.md"` → `8 docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md` (≤ 40); `grep -c -F` of the fill token → `0`.

## FIXES
| id | file | change | proof | commit |
|---|---|---|---|---|
| O1 | `ops/desk/desk-launch.sh` (B5's file) | The `prompt` kind now takes every `--name` / `--remote-control` value (`grep -o -e '--name[ =]*[^ ]*' -e '--remote-control[ =]*[^ ]*'`), strips the flag, blanks, `=` and quotes, and refuses when one value is exactly `brain`. That is the value `eval` hands `claude`. It replaces the four fixed-substring patterns. | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py tests/ops/test_desk_size_guard.py` → `77 passed, 1 xfailed, 15 warnings in 9.13s`. The B5 cases and the negative controls (`brain-survey`, `brainy`) are among them. | `b5eb3530 fix(brain-hub): the prompt kind reads the seat value as eval hands it, quotes and blanks stripped (check O1)` |
DevDocs line: not written. `ops/desk/desk-launch.sh` has no page under `docs/40 - DevDocs/cobalt/`: `Grep desk-launch` there finds only `jobs/restarts.md`, a page of another module, outside the rows' files. The build wrote none either.

## Suites
On `<tip now>` = `b5eb3530` (DB: none: RESTARTS, then W (a0), (a), (e) and `tests/ops`):
- RESTARTS: `uv run cobalt jobs restarts a09f0862..HEAD` → seven rows (`08-brain-handover.md` A DOCS · `BRAIN-HUB.md` A DOCS · `STANDING-LIST.md` M DOCS · build report A DOCS · `ops/desk/desk-launch.sh` M `operator script; no Cobalt reader` · `tests/ops/test_desk_launch_brain.py` A `test/documentation; no resident` · `tests/ops/test_desk_size_guard.py` M `test/documentation; no resident`), all `-`; last line `RESTARTS: none`. No `UNCLASSIFIED` row.
- (a0) `git diff --name-only --no-renames a09f0862` → the seven PREFLIGHT paths; every one is under `docs/`, `ops/` or `tests/ops/`. `cobalt_dev: not taken (DB: none — 7 paths)`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 636.66s (0:10:36)`, exit 0: 0 failed, 0 errors. This check adds no test there.
- `tests/ops`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `511 passed, 1 xfailed, 15 warnings in 203.47s (0:03:23)`, exit 0. The build had 508; this check adds the 3 cases of O1.
- (e) LIVE-NOTE: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.84s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; it does not name `COBALT_LIVE_VAULT_ROOT`.
- (b)–(d), (f): not run (DB: none). `cobalt_dev`: not taken, so it stands at `0013`. `.env`: `ls /Users/cobalt/cobalt-wt/brain-hub-1003/.env` → `No such file or directory` (14:00).

## Scope
PREFLIGHT's path union (seven paths, every one in a row's `files` or the build report): `BRAIN-HUB.md` (B1, B4), `STANDING-LIST.md` (B2, B4), `08-brain-handover.md` (B3), `ops/desk/desk-launch.sh` (B2, B5), `tests/ops/test_desk_launch_brain.py` (B2, B4, B5), `tests/ops/test_desk_size_guard.py` (B5), the build report. My commits: `tests/ops/test_desk_launch_brain.py` (B5's test file) and `ops/desk/desk-launch.sh` (B5's file). No path outside the rows.

## Checked against the branch
| check | command | output |
|---|---|---|
| (i) my commits | `git log --oneline bb930cac..HEAD -- . ":(exclude)docs"` | `b5eb3530 fix(brain-hub): … (check O1)` · `03ce2125 wip(brain-hub): check red — O1 …`; `<tip now>` = `b5eb3530` |
| (ii) paths | `git log --stat --format=%h bb930cac..HEAD` | `b5eb3530` `ops/desk/desk-launch.sh` · `03ce2125` `tests/ops/test_desk_launch_brain.py` · `46bd070e` the build report (docs). Every non-docs path is in B5's `files`. |
| (iii) fence | `git log --oneline a09f0862..HEAD -- ".../prompts/JUDGE-HUB.md" ".../prompts/JUDGE-CARD.md"` | (empty). The fence's other items are no path (allow list: B1's test compares `23`'s line, green; laws, memory, NOW: nothing under `/Users/cobalt/Vault` in the diff; launching: none). |
| (iv) O1 test | `grep -n -F "def test_check_o1_a_quoted_or_spaced_brain_seat_is_refused_too" tests/ops/test_desk_launch_brain.py` | `396:def test_check_o1_…(tmp_path, seat):`; its red `03ce2125` sits below its fix `b5eb3530` in (i) |
| (v) .env, branch | `ls <WT>/.env` · `git status --short --branch` | `ls: /Users/cobalt/cobalt-wt/brain-hub-1003/.env: No such file or directory` · `## ops/brain-hub-1003` |
| (vi) TREE STATE | `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` | (empty): `TREE STATE: unchanged` holds |
| (vii) card RECORDS | — | no record names an `ls`, `grep` or `git -C … log` command; nothing to run |
| (viii) L32 | — | this report holds no ticker, price or date of his; the values are constructed test values, commit ids and ruling rows |

## OPEN
none (`findings: 1`, `held: 1`, `fixed: 1`, `held unfixed: 0`; nothing REJECTED or UNSETTLED). OUT OF SCOPE, not open: `--output=` on the brain's `git -C` strings, `w` on `sed -n` (card `## RECORDS`, JUDGE 10-03 → card `10`); the auto-mode classifier and `23`'s allow list (`## NOT IN THIS JOB`, his R131).

## CONTINUE
next: none (pass 1 done 14:00; house B not needed)

## DECISIONS
none

## RECORDS
- House A: none (overruled 2026-10-02 R47). `## 1` and `## 3` were not run; no list was staged and no house was launched.
- `<S>` already held `o2-proof.txt` and `opus-1.md` from the earlier check of this branch (r1). I did not open them, because CHECK-HUB forbids reading earlier checks of this branch. I did not overwrite them either: this pass's `## 8` copy is `<S>/opus-1-r2.md`. House B is not needed, so no house reads it.
- His R7 (10-03), which sets the hub's measure line, `grep -n "^| R7 " ".../reports/cto-2026-10-03.md"` → `13:| R7 | 06:22 ET | HIS RULING (brain session): the brain's replacement line is 500,000 tokens; it measures before long writes and above 500,000 asks to be replaced; in 00-brain-handover.md … | HIS RULING · APPROVED — pending fold |`. The card's B1 text says `250,000`; the hub follows his ruling (L77). Not a finding.
- No DevDocs line: `ops/desk/desk-launch.sh` has no page under `docs/40 - DevDocs/cobalt/` (see `## FIXES`).
- The wait at W used the Monitor tool (a shell `until grep … ; do sleep 15; done` over the two suite output files). No step names that command; it ran and was not refused. The first one fired early on a loose pattern and was re-armed on pytest's summary line. It changed nothing.
- No `REFUSED` line, no `CONTINUED` line, no lock take (DB: none). The L74 item is under `## L74`.
- files opened: 16 — `CHECK-HUB.md`; the card `07-brain-hub-card.md`; `cto-2026-09-30.md`, `cto-2026-10-02.md` (ruling rows by grep); `cto-2026-10-03.md` (R7 row by grep, X2: beyond the list, for a value the hub carries); `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the build report (`## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, last lines, headings); the diff `a09f0862..bb930cac`; `ops/desk/desk-launch.sh`; `tests/ops/test_desk_launch_brain.py`; `tests/ops/test_desk_size_guard.py`; `docs/40 - DevDocs/prompts/BRAIN-HUB.md`; `docs/40 - DevDocs/prompts/STANDING-LIST.md`; `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`; `/Users/cobalt/.claude/ops/desk-list.sh` (X3: beyond the list, the session list the `brain` kind calls by name).
- **Check of `brain-hub`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).**

CHECK DONE · job: brain-hub · pass: 1 · tip: b5eb3530 · house A: none (overruled 2026-10-02 R47) · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0
