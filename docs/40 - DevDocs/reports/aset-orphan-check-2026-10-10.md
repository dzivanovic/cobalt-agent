# aset-orphan-1010 — check report (2026-10-10)

## §0 Headline
Check of `aset-orphan-1010` at `1987849b`: 10 findings (own 4, Sol 1, Gemini 5; Grok produced no list), 0 dropped, 0 held, 0 fixed.
Rows A and B stand as built; the audit re-derived from the plists matches the build's table (15 plists, KeepAlive: radar, aset, herdr, obsidian; only aset pairs it with `AbandonProcessGroup`).
3 open, all one question (X2): `uv sync --inexact` ≡ `uv run`'s sync is unproven — `uv sync --help` is on no launch line. `## DECISIONS` 1.
Deploy gate on the tip: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS: com.cobalt.aset. ready: YES.

## L74
A system reminder in this session (not a tool result) asked commits to carry a `Claude-Session:` line; the hub's rule is `Co-Authored-By` only. No commit was made by this check.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 0 · 3718c3a2b8289cc40c6dcbb5b2484202ab5d9668
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sat Oct 10 09:30:42 EDT 2026
status · git status --short --branch · 0 · ## ops/aset-orphan-1010
head · git log --oneline -1; git log --stat --format=%h 1987849b..HEAD · 0 · (5 lines)
    f72dbb9a docs(aset-orphan-1010): build report — 1987849b
    f72dbb9a
    
     .../reports/aset-orphan-build-2026-10-10.md        | 223 +++++++++++++++++++++
     1 file changed, 223 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/aset-orphan-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/x29-fixture-1010/.env
report · tail -n 3 "…/aset-orphan-build-2026-10-10.md" · 0 · BUILT · job: aset-orphan-1010 · tip: 1987849b | on ddaae952 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 2 of 2 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 145288
range · git log --oneline ddaae952..1987849b · 0 · (2 lines)
    1987849b fix(aset-orphan-1010): start_aset.sh execs the venv python so launchd's pid is the python (A, B; L1, L42)
    c3da0511 wip(aset-orphan-1010): red
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h ddaae952..1987849b`:
```
1987849b
 ops/README.md                   |  2 +-
 ops/start_aset.sh               | 17 +++++++++++------
 tests/cobalt/test_jobs_reads.py |  2 +-
c3da0511
 tests/ops/test_launchd_orphan.py | 126 +++++++++++++++++++++++++++++++++++++++
```
Path union: `ops/README.md`, `ops/start_aset.sh`, `tests/cobalt/test_jobs_reads.py`, `tests/ops/test_launchd_orphan.py`. The card carries no `DB: none` line: the gate runs `all --deploy`.
`ls <S>` → `No such file or directory` (fresh).
House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
house A: Sol · house B: Grok. Card `HOUSE B: as needed`.

## Files copied
`stage-set.sh` · exit 0:
```
10355 …/aset-orphan-1010-check/diff.md
10592 …/files/222-aset-orphan-card.md
27744 …/files/aset-orphan-build-2026-10-10.md
22427 …/files/wt/ops/README.md
3514 …/files/wt/ops/start_aset.sh
10685 …/files/wt/tests/cobalt/test_jobs_reads.py
5317 …/files/wt/tests/ops/test_launchd_orphan.py
384 …/rulings.md
STAGED 8 files · 91018 bytes · commits 2
```
`stage-copy.sh` (each `COPIED <bytes> <dest>`): aset-orphan-answer-2026-10-10.md 4288 · DEPLOY-HUB.md 57118 · wt/src/cobalt/voice/scratch.py 10356 · wt/ops/start_mainframe.sh 25885 · wt/ops/run_backup.sh 1467 · wt/cobalt.sh 3515 · wt/configs/cobalt/jobs.yaml 20349 · wt/src/cobalt/jobs/restarts.py 12098 · wt/tests/ops/test_install_ops.py 8216 · wt/src/cobalt/archiver/store.py 14076 · plists: agent 1573 · archiver 3849 · aset 2209 · backup 4601 · cards-expire 4020 · daymode-propose 3452 · generated 4481 · heartbeat 3390 · herdr 4832 · mainframe 2271 · obsidian 2397 · prefill-daily 4199 · radar 1216 · replay 2482 · seat-usage 20416 (15 plists in `ops/` at the tip).

## OWN FINDINGS
Written before either house's list was opened. Read: the card, the diff `ddaae952..1987849b`, `ops/start_aset.sh`, `tests/ops/test_launchd_orphan.py`, `ops/com.cobalt.aset.plist`, the resident plists' `ProgramArguments`, the build report's sections the hub names, `pyproject.toml` (`grep -n -F "tool.uv"` → `84:[tool.uv.extra-build-dependencies]` only: no `default-groups`, no `package`, nothing that makes `uv run` and `uv sync` differ), the subprocess callers under `src/cobalt` reachable from `src/cobalt/aset` (`settings/cli.py:134` `subprocess.run(["git", "show", …])`, synchronous: a child that has ended before the call returns, `/usr/bin/git` on the plist's PATH, nothing from `.venv/bin`).

FINDING O1
ROW: X2 (row A's "Confirm `--inexact` with `uv sync --help` … and quote the line")
CLAIM: `ops/start_aset.sh:77` `uv sync --inexact` is claimed to sync what `uv run` synced, but no tool output in the build shows `uv sync --help` (build report `## DECISIONS` 1: refused).
RUN: COMMAND `uv sync --help`
EXPECT: the `--inexact` line of the help, quoted.

FINDING O2
ROW: B (build report `## DECISIONS` 5)
CLAIM: `tests/ops/test_launchd_orphan.py:54–55`, the "last line is not an exec" branch of `orphan_prone`, has no negative-control case; if it returned None the helper would pass a resident whose script ends `uv run …` without `exec`.
RUN: TEST `tests/ops/test_launchd_orphan.py`
```python
def test_b4_a_script_that_does_not_exec_is_flagged(tmp_path):
    ops_dir = tmp_path / "ops"
    no_exec = _script(ops_dir, "start_noexec.sh", "uv run python -m x")
    reason = orphan_prone(_plist(tmp_path, "no-exec", no_exec, True, True), ops_dir)
    assert reason is not None and "not an exec" in reason
```
EXPECT: if the claim holds (branch broken), `assert reason is not None …` fails.

FINDING O3
ROW: X3
CLAIM: the build report's audit (`## E3 THE ROWS` row B) misses a KeepAlive plist: the set is not exactly radar, aset, herdr, obsidian.
RUN: COMMAND `grep -l -F "<key>KeepAlive</key>" ops/com.cobalt.agent.plist ops/com.cobalt.archiver.plist ops/com.cobalt.aset.plist ops/com.cobalt.backup.plist ops/com.cobalt.cards-expire.plist ops/com.cobalt.daymode-propose.plist ops/com.cobalt.generated.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.herdr.plist ops/com.cobalt.mainframe.plist ops/com.cobalt.obsidian.plist ops/com.cobalt.prefill-daily.plist ops/com.cobalt.radar.plist ops/com.cobalt.replay.plist ops/com.cobalt.seat-usage.plist`
EXPECT: a fifth file beside the four.

FINDING O4
ROW: B / X3
CLAIM: a plist with `AbandonProcessGroup` true is missing from the audit table's eleven (aset, agent and the nine one-shots).
RUN: COMMAND `grep -l -F "<key>AbandonProcessGroup</key>" ops/com.cobalt.agent.plist ops/com.cobalt.archiver.plist ops/com.cobalt.aset.plist ops/com.cobalt.backup.plist ops/com.cobalt.cards-expire.plist ops/com.cobalt.daymode-propose.plist ops/com.cobalt.generated.plist ops/com.cobalt.heartbeat.plist ops/com.cobalt.herdr.plist ops/com.cobalt.mainframe.plist ops/com.cobalt.obsidian.plist ops/com.cobalt.prefill-daily.plist ops/com.cobalt.radar.plist ops/com.cobalt.replay.plist ops/com.cobalt.seat-usage.plist`
EXPECT: a radar, herdr, obsidian or mainframe line.

X1 (no finding, a read): after row A `ProgramArguments[0]` is `start_aset.sh` (`com.cobalt.aset.plist:25`) and its last line `exec`s the venv python (`ops/start_aset.sh:78`), so launchd's pid becomes the python. `uv sync --inexact` (`:77`) runs in the foreground and has ended before the `exec`. A bootout that lands DURING the sync signals bash only (AbandonProcessGroup) and leaves the `uv sync` child to finish on its own: no port, no scratch lock (the python has not started), seconds long — not an orphan of the kind row A names. No test can pin a live launchd pid; the deploy's 4.6 `launchctl print` and row C are where it is seen.
X3: card says 16 plists at `d0a5fbb8`; `git show ddaae952:ops/` lists 15 `com.cobalt.*.plist` (the card's own enumeration names 15). The build's `## DECISIONS` 2 already says so.

## Findings
House A = Sol (`<S>/house-a.md`, `FINDINGS: 1`); house B = Gemini (`<S>/house-b.md`, `FINDINGS: 5`; seated after Grok produced NO FINDINGS LINE). Every block carries a `RUN:` line followed by a `def test_` or one command line with an allowed beginning: none dropped.
- A1 · Sol · X2 · the build never quoted `uv sync --help` / `uv run --help`; report :198 says "NOT quoted" · COMMAND (`grep -n -F 'NOT quoted' …`)
- B1 · Gemini · X1 · launchd's pid is the python; nothing between sync and exec is left · COMMAND (`grep -n -B 1 "exec " ops/start_aset.sh`)
- B2 · Gemini · X2 · `uv sync --inexact` = `uv run`'s sync, shown by quoting help · TEST (`test_x2_help`, runs `uv sync --help` through `subprocess`; no file named)
- B3 · Gemini · X3 · re-derive the audit, one line per plist · TEST (`test_x3_audit`, ends `assert False`; no file named)
- B4 · Gemini · W (row "3") · the report's with-DB 5093/0 claim shows no suite output line · COMMAND (`grep -n "pass 1, executed command" …`)
- B5 · Gemini · B · the "not an exec" branch is unpinned · TEST (`test_b3_negative_control_missing_exec`, ends `assert False`)

## Dropped
none.

## RUNS
- O1 · own · `uv sync --help` · not run: not a listed prefix (the build's launch line refused it too) · UNSETTLED — the command is not on my list
- O2 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_launchd_orphan.py::test_b4_a_script_that_does_not_exec_is_flagged` · `1 passed, 15 warnings in 0.80s` · NOT HELD (the branch flags a non-`exec` last line; test removed)
- O3 · own · `grep -l -F "<key>KeepAlive</key>" ops/com.cobalt.*.plist` (15 named) · `ops/com.cobalt.aset.plist`, `ops/com.cobalt.herdr.plist`, `ops/com.cobalt.obsidian.plist`, `ops/com.cobalt.radar.plist` · NOT HELD (four, as the audit)
- O4 · own · `grep -l -F "<key>AbandonProcessGroup</key>" …` (15 named) · agent, archiver, aset, backup, cards-expire, daymode-propose, generated, heartbeat, prefill-daily, replay, seat-usage (11) · NOT HELD (the audit's eleven; none of radar, herdr, obsidian, mainframe)
- A1 · Sol · `grep -n -F 'NOT quoted' '…/aset-orphan-build-2026-10-10.md'` · ``198:- X2: `uv sync --help` was refused on this launch line; NOT quoted (`## DECISIONS` 1).`` · UNSETTLED — the line shows the proof is missing (the build's own DECISION 1); the claim it stands for (`uv sync --inexact` ≡ `uv run`'s sync) is settled only by `uv sync --help` / `uv run --help`, not on my list. Nothing in the rows' files to fix
- B1 · Gemini · `grep -n -B 1 "exec " ops/start_aset.sh` · `77-uv sync --inexact` / `78:exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset` · NOT HELD (the output confirms row A; no defect claimed)
- B2 · Gemini · `test_x2_help` · not run: its body runs `uv sync --help` through `subprocess`, a command not on my list; running it inside a test would step around the launch line · UNSETTLED — the command is not on my list
- B3 · Gemini · `uv run pytest -q -rs -p no:cacheprovider --color=no -s tests/ops/test_launchd_orphan.py::test_x3_audit` (put in that file; the finding named none) · `1 failed` at its own `assert False, "Audit table printed"`; printed table: agent `cobalt.sh` absent True · archiver uv absent True · aset `start_aset.sh` True True · backup `run_backup.sh` absent True · cards-expire uv absent True · daymode-propose uv absent True · generated uv absent True · heartbeat uv absent True · herdr `herdr` {SuccessfulExit: False} absent · mainframe `start_mainframe.sh` absent absent · obsidian `Obsidian` True absent · prefill-daily uv absent True · radar uv {SuccessfulExit: False} absent · replay uv absent True · seat-usage uv absent True · NOT HELD (red only for its unconditional `assert False`; the table equals the build's audit line for line; test removed)
- B4 · Gemini · `grep -n "pass 1, executed command" "docs/…/aset-orphan-build-2026-10-10.md"` · `179:- (c) pass 1, executed command (`952`), WHOLE: …` ; and `grep -n -F "with-DB 5093/0" /Users/cobalt/cobalt-wt/.gate-logs/aset-orphan-1010-all-20261010-083000.log` · `2089:with-DB 5093/0` · NOT HELD (the report's :165 line is the gate's own verdict line, in its log)
- B5 · Gemini · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_launchd_orphan.py::test_b3_negative_control_missing_exec` (form repaired once: the `from tests.ops.test_launchd_orphan import …` line dropped, the names are in the file; assertion unchanged) · `1 failed` at `assert False, "Clause pinned"` (line 157), after `assert res is not None and "not an exec" in res` passed · NOT HELD (red only for the unconditional `assert False`; the branch works; test removed)
After the removals `git status --short --branch` → `## ops/aset-orphan-1010` (tree at the tip). Held: 0 · no `wip(aset-orphan-1010): check red` commit.

## FIXES
none (nothing held).

## Suites
No commit of mine: the tip is the build's `1987849b`.
RESTARTS, `uv run cobalt jobs restarts ddaae952..HEAD` · 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md	A	DOCS	-
ops/README.md	M	operations documentation; no resident	-
ops/start_aset.sh	M	resident reads	com.cobalt.aset
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/ops/test_launchd_orphan.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
(the card's RECORDS expectation, matched.)
`sh /Users/cobalt/cobalt/ops/desk/gate.sh aset-orphan-1010 all --deploy` (09:44 start, background) · exit 0, verdict lines WHOLE:
```
offline 4196/0
lock: waited 35 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/aset-orphan-1010-all-20261010-094437.log
```
`grep -n -F "OUTSIDE the allowed set" <log>` → nothing. The build's own test file at the tip: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_launchd_orphan.py` → `7 passed, 15 warnings in 0.81s`.
`.env`: `ls /Users/cobalt/cobalt-wt/aset-orphan-1010/.env` → `No such file or directory` (10:48).

## Scope
PREFLIGHT's path union — `ops/start_aset.sh` (row A), `ops/README.md` (row A, the `:31` Runs cell), `tests/cobalt/test_jobs_reads.py` (row A, the `:100` docstring citation), `tests/ops/test_launchd_orphan.py` (rows A, B) — each inside a row's `files`. No commit of mine. No plist, `jobs.yaml`, `cobalt.sh` or `src/` path in the range.

## Checked against the branch
- (i) `git log --oneline 1987849b..HEAD -- . ":(exclude)docs"` → nothing: no commit of mine; `<tip now>` = `1987849b`.
- (ii) `git log --stat --format=%h 1987849b..HEAD` → `f72dbb9a` · `.../reports/aset-orphan-build-2026-10-10.md | 223 +++` (docs only).
- (iii) `git log --oneline ddaae952..HEAD -- <the 15 plists> configs/cobalt/jobs.yaml cobalt.sh src ops/desk/orphan-clean.sh` → EMPTY. (`DEPLOY-HUB.md` lives on `main`, not in this range.)
- (iv) no HELD finding: nothing to check.
- (vi) `git log --stat --format=%h ddaae952..HEAD -- src/cobalt/db_migrations tests/cobalt` → `1987849b` · `tests/cobalt/test_jobs_reads.py | 2 +-` (a docstring; no migration, no new with-DB test): gate lists not needed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 ddaae952 -- . ":(exclude)docs"` → nothing (code at the base = code read by the drafter); `git -C /Users/cobalt/cobalt log --oneline -1` → `89e80b09 docs(desk): R886 X29 built d083ec76, card fields filled` (main has moved past the draft's `c3a484e4`, docs commit). RESTARTS record: matched (`## Suites`).
- (viii) L32: this report holds no ticker, price or date of his.

## OPEN
One question, three items (O1 own, A1 Sol, B2 Gemini), each UNSETTLED — the command is not on my list:
- X2: does `uv sync --inexact` (`ops/start_aset.sh:77`) sync what `uv run` synced (project, default groups, lock, extraneous packages)? Settled by quoting `uv sync --help` (`--inexact`) and `uv run --help` (its sync and `--exact` default) from `/Users/cobalt/cobalt`: a seat whose line lists `Bash(uv sync --help)` and `Bash(uv run --help)`. Read so far (not proof): `pyproject.toml` carries no `[tool.uv]` key that makes the two differ (`grep -n -F "tool.uv"` → `84:[tool.uv.extra-build-dependencies]` only).

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
1. X2 is UNPROVEN and the job depends on it (open: O1, A1, B2). Neither the build's nor this check's launch line lists `uv sync --help` / `uv run --help`, and the check does not run an unlisted command through a test (B2's body would). ASK DESK: run the two help reads once (a listed string on the fix round's or the deploy's line) and quote the `--inexact` line — or accept the card's statement as is [10:49]. Safe default taken: the line stays as built; no fix (nothing held); the item ships on the follow-up list. Not his (no notes, money or sizing logic touched).

## RECORDS
- Findings, by house: own O1–O4, Sol A1, Gemini B1–B5. Dropped: none. Grok: NO FINDINGS LINE (above).
- NOT HELD tests put in `tests/ops/test_launchd_orphan.py` and removed again with the Edit tool (O2, B3, B5); `git status` back at the tip.
- B5 form repaired once: the `from tests.ops.test_launchd_orphan import …` line dropped (the names are in the file); assertion unchanged. B3 placed in `tests/ops/test_launchd_orphan.py` (the finding named no file).
- X1 read (not a finding): the aset process's one reachable child is `src/cobalt/settings/cli.py:134` `subprocess.run(["git", "show", …])`, synchronous; the card's fence line ("no `subprocess` … under `src/cobalt/aset` or `src/cobalt/voice`") is literally true — that call lives under `src/cobalt/settings`. A bootout during it would leave a `git show` to end on its own: no port, no lock.
- The card's "16 at `d0a5fbb8`": `git show ddaae952:ops/` lists 15 plists (the build's DECISIONS 2 says the same).
- One lock take, inside `gate.sh` (waited 35 min; another worktree held `.env` at PREFLIGHT); no extra take. `.env: removed, proven gone (W)`.
- Not opened: `areas/cobalt.md` (WHAT YOU READ (5)); the card's rows and fence carried what the judgment needed.
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `ops/start_aset.sh`, `tests/ops/test_launchd_orphan.py`, `ops/com.cobalt.aset.plist`, the build report (`:86–224`), the probe output, Sol's output (`:6640–6709`), Grok's output, Gemini's output, the gate output, and this report; by `grep` only: `pyproject.toml`, `src/cobalt/settings/cli.py`, the 15 plists, `cto-2026-09-24.md`, the two gate logs.
- Check of `aset-orphan-1010`: house A `Sol`, house B `Gemini` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- 09:37 Sol (house A) exited 0 with `FINDINGS: 1`; its final message written by me to `<S>/house-a.md`. Its transcript shows it ran read-only `grep` commands inside its sandbox (it was told to run none); the list's form is unaffected.
- 09:38 Grok (house B) exited 0 with NO FINDINGS LINE and no `house-b.md`; its whole stdout: "I'll read the house instructions in full first, then follow them exactly.The check is a read-only review of one build. I'll read the diff and the build report first, then write each finding before looking for the next.The diff and the report are in. Next I’ll read the start script, the new test, and the plists the audit depends on." Seat B → Gemini (next UP, not sat), one attempt, started 09:39 (house gates last run 09:32 at `## 1` (5), same session).
- Sol's `diff.md` and `rulings.md` are the ones `stage-set.sh` wrote from git (one set serves both houses).

CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · house A: Sol FINDINGS: 1 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Gemini FINDINGS: 5 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668
