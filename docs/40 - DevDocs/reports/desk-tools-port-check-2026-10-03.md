# desk-tools-port — CHECK, pass 1 (2026-10-04)

## §0 Headline
- desk-tools-port, check pass 1, 2026-10-04 14:38 EDT. House A: none (overruled 2026-10-02 R47); Opus checked alone. Base `5ff16b1f`, tip `5c1d629f` (no commit of mine).
- 9 own findings, all run, none held. X1: every ported file matches its source head, except the P3 and P5 files. X2: the five launcher test files pass (`230 passed, 1 xfailed`). X3: both hooks exempt `cwd` `/Users/cobalt/cobalt` (`37 passed`).
- P4: the install JSON is valid and names the three hooks. The one line in neither parent is the unknown-kind pin, which the fence allows.
- Suites as built: offline 3751/0 · tests/ops 827/0 · live-note 146/0 · DB: none · `.env` absent · `RESTARTS: none` (re-derived).
- open 0 · house B not needed · ready: YES · decisions 0.

## L74
The session's system context carried a commit-attribution block asking for a `Claude-Session:` line on commits. Recorded once; not acted on (no commit was made in this check).

## AUTHORIZATION
Sun Oct  4 14:32:49 EDT 2026 (`date`).

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/07b-desk-tools-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/07b-desk-tools-port-card.md"` | 0 | `218baccfa6521e67886b28959ce9728fe81e1a58` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING 2026-09-30 R60 | `grep -n "^\| R60 " ".../cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... \| APPROVED \|` |
| R60 commit | `git -C ... log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (RULINGS, and HOUSE A overrule) | `grep -n "^\| R47 " ".../cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... \| HIS RULING · APPROVED \|` |
| R47 commit | `-S"\| R47 \|"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R157 | `grep -n "^\| R157 " ".../cto-2026-10-02.md"` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included ... \| HIS RULING · APPROVED \|` |
| R157 commit | `-S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R154 | `grep -n "^\| R154 " ".../cto-2026-10-02.md"` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check ... \| HIS RULING · APPROVED \|` |
| R154 commit | `-S"\| R154 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gates | not run: the card carries `HOUSE A: none — overruled 2026-10-02 R47` (no house gate, no probe) | — | — |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-port-1003` |
| head | `git log --oneline -1` | 0 | `525b5ae1 docs(desk-tools-port): build report — 5c1d629f (committed by the desk after the stop line)` |
| docs-only above TIP | `git log --stat --format=%h 5c1d629f..HEAD` | 0 | `525b5ae1` · `.../reports/desk-tools-port-build-2026-10-03.md \| 77 ++++++++++++++++++++--` (docs only) |
| BUILT | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: desk-tools-port · tip: 5c1d629f \| on 5ff16b1f \| migration: none \| offline 3751/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 5ff16b1f..5c1d629f` | 0 | `5c1d629f feat(...) P5` · `1e171885 wip(...): red — P5` · `5fa56360 docs(...): build report — 1c702713` · `1c702713 fix(...): port 07 ... 09 ... (P1, P3, P2)` · `d51c2125 wip(...): red — P1, P2` (5 commits) |
| path union | `git diff --name-only --no-renames 5ff16b1f..5c1d629f` (DB: none) | 0 | `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md`, `docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md`, `docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_launch_devfix.py`, `tests/ops/test_desk_size_guard.py`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py` — every path under `ops/`, `tests/ops/` or `docs/` |
| THE LOCK (DB: none) | `ls /Users/cobalt/cobalt-wt/desk-tools-port-1003/.env` | 1 | `ls: ...: No such file or directory` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)`; house B: as needed (card) |

## Files copied
none — no house (overruled 2026-10-02 R47).

## OWN FINDINGS
Written before any run (no house in this check). Read: the card, the diff `5ff16b1f..5c1d629f` (`desk-launch.sh` whole hunks, the two shared files, `BRAIN-HUB.md`, `test_desk_launch_devfix.py`), `07`'s own `desk-launch.sh` diff `a09f0862..b5eb3530`, both sides of `desk-watch.sh` / `wait-stop-line.sh` from `a09f0862`, `stop-guard.py`, `idle-wake.py`, `test_desk_launch_brain.py` whole, `test_stop_guard.py:1-115`, the build report from `## E3` down, the two source checks' `## §0`, `cobalt.md` from `## What Cobalt is` and `## Build rules` down.

FINDING O1
ROW: X1 (P1, P2)
CLAIM: a file the card ports "from `git show <head>:<path>`" differs at the tip from its source head outside the rows (P3, P5) that change it.
RUN: COMMAND `git diff --stat b5eb3530 5c1d629f -- "docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md" "docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md" tests/ops/test_desk_launch_brain.py tests/ops/test_desk_size_guard.py ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts/BRAIN-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`; `git diff --stat a6bef8cb 5c1d629f -- <09's eight files>`; `git diff --stat b5eb3530 1c702713 -- <BRAIN-HUB.md, test_desk_launch_brain.py, 08-brain-handover.md, brain-hub-build report>`.
EXPECT: a stat row for `08-brain-handover.md`, the brain-hub build report, or any of `09`'s eight files; or a P1-only file differing at `1c702713` (before P5).

FINDING O2
ROW: P2 (BASE's side of the two watch scripts)
CLAIM: taking `09`'s `desk-watch.sh` and `wait-stop-line.sh` byte for byte drops a line `03c`/`18` added at BASE (`ops/desk/desk-watch.sh:14`, `ops/desk/wait-stop-line.sh` `export LC_ALL=C`).
RUN: COMMAND `git diff a09f0862 5ff16b1f -- ops/desk/desk-watch.sh ops/desk/wait-stop-line.sh` against `git diff a09f0862 a6bef8cb -- ops/desk/desk-watch.sh ops/desk/wait-stop-line.sh`.
EXPECT: a BASE-side `+` line absent from `09`'s side.

FINDING O3
ROW: X2
CLAIM: in the merged `ops/desk/desk-launch.sh`, one of `recut`, `brain`, the unknown-kind list, the `prompt` brain-seat refusal or the optional `TREE STATE` no longer works in its dry run.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_recut.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_brain.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py`
EXPECT: a failed id in one of the five files.

FINDING O4
ROW: P5
CLAIM: `--fable` is an entry path the live-brain refusal (`ops/desk/desk-launch.sh` the `live=` loop, `:477`) is not pinned on: no test runs `--fable` beside a live `brain`.
RUN: TEST `tests/ops/test_desk_launch_brain.py`
```python
@pytest.mark.parametrize("dry", [True, False])
def test_check_o4_fable_beside_a_live_brain_is_refused_and_nothing_runs(desk, dry):
    desk.live([(DESK, "cto-desk"), (BRAIN, "brain")])
    done = desk.launch_run("brain", str(desk.handover), "--fable", dry=dry)
    refused(done, f"a session named brain is live ({BRAIN})")
    assert not desk.calls.exists()
```
EXPECT: red — the `--fable` line printed or `claude` run beside a live brain.

FINDING O5
ROW: P5
CLAIM: the tree's own `BRAIN-HUB.md` still carries its install token, so `--fable` on the tree's hub must be refused like the default; no test runs `--fable` on a hub holding the token (`ops/desk/desk-launch.sh:447`, the `«INSTALL` check before the model word).
RUN: TEST `tests/ops/test_desk_launch_brain.py`
```python
def test_check_o5_fable_on_a_hub_still_carrying_its_install_token_is_refused(desk):
    desk.hub.write_text(f"# BRAIN-HUB ({INSTALL})\n\n{STANDIN_LINE}\n")
    desk.commit("token")
    done = desk.launch_run("brain", str(desk.handover), "--fable", dry=False)
    refused(done, "the fixed file still carries its")
    assert not desk.calls.exists()
```
EXPECT: red — Fable launched on an uninstalled hub.

FINDING O6
ROW: X3
CLAIM: `ops/desk/stop-guard.py:57-62` / `:122` or `ops/desk/idle-wake.py:39-41` no longer exempt a `cwd` of `/Users/cobalt/cobalt` (the desk, the brain).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py`
EXPECT: `test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report` (`test_stop_guard.py:101`) or `test_a_cwd_outside_the_worktrees_writes_nothing` (`test_idle_wake.py:82`) failed.

FINDING O7
ROW: P4
CLAIM: the install text in `ops/desk/stop-guard.py:19-31`, quoted in the build report's `## RECORDS`, is not valid JSON or does not name the three hooks as the row states.
RUN: COMMAND `uv run pytest -q -rP -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k i1_run`
EXPECT: failed, or captured stdout other than PreToolUse/Bash → `bare-guard.py`, Stop → `stop-guard.py`, Notification `idle_prompt` → `idle-wake.py`.

FINDING O8
ROW: P3
CLAIM: `STANDING-LIST.md` holds `07`'s `## 7.` section other than exactly once.
RUN: COMMAND `grep -c -F "## 7. " "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: a count other than `1`.

FINDING O9
ROW: SCOPE
CLAIM: a path in the range lies outside the rows' files (`07`'s files, `09`'s files, the P3 pair, the P5 four) and outside the fence's one exception (the unknown-kind list).
RUN: COMMAND `git diff 5ff16b1f 5c1d629f -- tests/ops/test_desk_launch_devfix.py` (the one path in neither `git diff --name-only a09f0862 b5eb3530` nor `… a6bef8cb`).
EXPECT: a changed line other than the unknown-kind refusal text.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `git diff --stat b5eb3530 5c1d629f -- <07's seven paths>` · `git diff --stat a6bef8cb 5c1d629f -- <09's eight paths>` · `git diff --stat b5eb3530 1c702713 -- BRAIN-HUB.md test_desk_launch_brain.py 08-brain-handover.md brain-hub-build report` | 07: only `BRAIN-HUB.md \| 8`, `STANDING-LIST.md \| 43`, `desk-launch.sh \| 131`, `test_desk_launch_brain.py \| 97`, `test_desk_size_guard.py \| 7` (the P3/P5/merged files); `08-brain-handover.md` and the brain-hub build report absent (identical). 09: (nothing) — all eight identical. 07 at `1c702713` (before P5): (nothing) — the four unshared files identical | NOT HELD |
| O2 | Opus | `git diff a09f0862 5ff16b1f -- ops/desk/desk-watch.sh ops/desk/wait-stop-line.sh` · `git diff a09f0862 a6bef8cb -- …` | BASE's side: one `+export LC_ALL=C` in each file; `09`'s side carries `+export LC_ALL=C` in each (desk-watch after the W1 header comment, wait-stop-line before `WT=`) | NOT HELD |
| O3 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_recut.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_brain.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` (background) | `230 passed, 1 xfailed, 15 warnings in 56.09s`, exit 0 (the xfail is G3's strict probe, as at both parents per the build report) | NOT HELD |
| O4 | Opus | the test, added with Edit to `tests/ops/test_desk_launch_brain.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py -k "check_o4 or check_o5"` | `3 passed, 66 deselected, 15 warnings in 1.11s` (O4 ×2 dry/real, O5 ×1) | NOT HELD — removed again with Edit |
| O5 | Opus | the same run | (above) | NOT HELD — removed again with Edit; `git status --short --branch` → `## ops/desk-tools-port-1003` (clean) |
| O6 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` | `37 passed, 15 warnings in 2.30s` (X3: `test_stop_guard.py:106` and `test_idle_wake.py:85` both run `cwd` `/Users/cobalt/cobalt`; by reading, `stop-guard.py:59` requires the `/Users/cobalt/cobalt-wt/` prefix) | NOT HELD |
| O7 | Opus | `uv run pytest -q -rP -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k i1_run` | `1 passed, 29 deselected, 15 warnings in 0.86s`; captured stdout: `PreToolUse` `matcher` `Bash` → `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`; `Stop` → `python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py`; `Notification` `matcher` `idle_prompt` → `python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py` — byte-identical to the build report's `## RECORDS` block | NOT HELD |
| O8 | Opus | `grep -c -F "## 7. " "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | `1` | NOT HELD |
| O9 | Opus | `git diff 5ff16b1f 5c1d629f -- tests/ops/test_desk_launch_devfix.py` | one changed line, `:383`: `… recut, desk, prompt, close, install-ops` → `… recut, desk, prompt, brain, close, install-ops` | NOT HELD (the fence's one exception) |

Nothing held → no `wip(desk-tools-port): check red` commit.

## FIXES
none — nothing held.

## Suites
No commit of mine → the build's lines stand (`suites: as built (no commit)`), quoted from its report at `5c1d629f`:
- offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 576.81s (0:09:36)`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `827 passed, 1 xfailed, 15 warnings in 321.69s (0:05:21)`.
- live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest … ` → `146 passed, 1 skipped, 15 warnings in 26.39s` (the skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).
- with-DB: not run (DB: none; R154). `cobalt_dev`: not taken. `.env`: never present (`ls` → No such file, PREFLIGHT and `## 7` (v)).
- RESTARTS, re-derived by me: `uv run cobalt jobs restarts 5ff16b1f..HEAD` → 17 rows (6 DOCS, 5 `operator script; no Cobalt reader`, 6 `test/documentation; no resident`), no `UNCLASSIFIED`; last line `RESTARTS: none`.

## Scope
PREFLIGHT's path union (17 paths): `07`'s seven files (P1; `STANDING-LIST.md` and `test_desk_size_guard.py` under P3; `BRAIN-HUB.md`, `desk-launch.sh`, `test_desk_launch_brain.py`, `STANDING-LIST.md` also under P5), `09`'s eight files (P2), this job's build report (docs), and `tests/ops/test_desk_launch_devfix.py` — one line, the unknown-kind pin, the fence's one exception (O9). My commits: none.

## Checked against the branch
- (i) `git log --oneline 5c1d629f..HEAD -- . ":(exclude)docs"` → (nothing): no commit of mine; `<tip now>` = `5c1d629f`.
- (ii) `git log --stat --format=%h 5c1d629f..HEAD` (PREFLIGHT) → `525b5ae1`, the build report only.
- (iii) `## NOT IN THIS JOB` fences no path (it names "a line in neither parent except the unknown-kind list", `git merge` / `rebase`, the settings write); the one line in neither parent is O9's, the allowed one; the settings write: `~/.claude/settings.json` is outside the repo and no commit touches it.
- (iv) no HELD finding.
- (v) `ls /Users/cobalt/cobalt-wt/desk-tools-port-1003/.env` → No such file (below, at close); `git status --short --branch` → `## ops/desk-tools-port-1003`.
- (vi) TREE STATE: unchanged — `git log --stat --format=%h 5ff16b1f..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing).
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command (file:line cites and the desk's preflight/judge facts); nothing to run.
- (viii) L32: this report quotes no ticker, price or date of his; the only dates are job and ruling dates.

## OPEN
none. findings 9 · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## CONTINUE
next: none — the desk verifies and commits this report (CHECK DONE, pass 1).

## DECISIONS
none

## RECORDS
- Check of `desk-tools-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- No house ran (card header `HOUSE A: none — overruled 2026-10-02 R47`): no files staged, no house gate or probe, `## 1` and `## 3` not run. `<S>` holds only `opus-1.md`, written as a pointer to this report's four sections with the counts, NOT a whole copy as `## 8` says; house B is not needed, so no reader depends on it. A pass 2, if ever ordered, copies the sections whole first.
- P5's rulings (R188, R189, R191) are cited in the files as "his 2026-10-04 R…"; their rows sit in `cto-2026-10-03.md` (Grep tool, pattern `^\| R(188|189|191) ` over `reports/cto-2026-10-0*.md` → `cto-2026-10-03.md:194`, `:195`, `:197`, each `HIS RULING (brain relay)` · `APPROVED — pending fold`). A proof by `cto-<date>.md` from the cited date would look in a file that does not exist. Not a finding: the card writes the date the same way, and the rows are found.
- The O3 run was in flight while O4/O5 were added and removed (added after it started; I did not prove whether it collected them). Either way the O3 verdict stands: all three O4/O5 ids also passed in their own call.
- O4/O5 are passing tests, removed again per `## 4`: `--fable` beside a live brain and on a hub holding its install token are refused today but stay unpinned by the build's suite. A gap only a build can pin (BRAIN-HUB "A gap a check CANNOT close goes to the builder"); not a defect — the refusal comes from code that does not branch on the flag.
- `## READ` names `07-brain-hub-card.md` and `09-worker-watch-card.md`: not opened; their check reports' `## §0` (r2) were read, and `desk-launch.sh` was compared at BASE, `07`'s tip and `09`'s (unchanged by `09`) through `git diff`.
- `.env`: never present (DB: none, R154); no lock taken.
- files opened: 22 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK` to `## W`); cto-2026-09-30.md, cto-2026-10-02.md, cto-2026-10-03.md (one row each by grep); the build report (from `## E3`, and its tail); `cobalt.md` (`## What Cobalt is`, `## Build rules` down); brain-hub-check-2026-10-03-r2.md and worker-watch-check-2026-10-03-r2.md (`## §0`); `ops/desk/desk-launch.sh`, `desk-watch.sh`, `wait-stop-line.sh` (by diff and grep); `ops/desk/stop-guard.py`; `ops/desk/idle-wake.py`; `BRAIN-HUB.md`, `STANDING-LIST.md` (by diff and grep); `tests/ops/test_desk_launch_brain.py`; `test_stop_guard.py` (`:1-115`); `test_idle_wake.py` (grep); `test_desk_launch_devfix.py`, `test_desk_size_guard.py` (by diff).

CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
