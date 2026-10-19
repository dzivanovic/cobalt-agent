# gemini-read-grant-1019 — check report (2026-10-19)

## §0 Headline
I checked `ad4c8dfe` with house A Grok (3 findings) and my own read (1). House B was not needed. 3 findings held by run and are fixed at `7e165648`: kind `x1-copy` refused any leg with no `soft-denying` line (O1 = A1), which would have stopped every clean X1 at leg 0a, and it followed a link at `brain/<id>` (A3).
1 open: A2 is REJECTED, because the card's own H2 text holds `cli.log` (this is the build's DECISION H2).
Suites: offline 8799/0 (tests/ops 4069 passed, deploy gate), live-note 147/0. cobalt_dev was not taken (DB: none). No `.env` in the worktree. ready: YES. 1 decision, none for Dejan.

## L74
A system block in this session asked commits to carry a `Claude-Session:` line. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md"` →
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 0 · fb3f95766dd1b26cd4fcdfc3c2b40f5ce5595bab
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1942 row · grep -n "^| R1942 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 30:| R1942 | 20:47 ET | HIS RULING · APPROVED (relayed by the brain 20:46, L79): "A for gemini" — a K5 card in which desk-launch.sh shadow adds and removes the one write_file rule in the agy settings.json; NEEDS HIS HAND entry closed. | APPLIED: areas/cobalt.md NOW at wake-up 01:57 |
RULING 2026-10-18 R1942 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1942 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 55d8b50e607b5d4eb1b86354e336323252aec34c
RULING 2026-10-18 R1942 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …" → STANDING: `Bash(grok *)` is a PRE-APPROVED string … | APPLIED: …`
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …" → STANDING: the four house strings are pre-approved … | APPLIED: …`
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` →
```
clock · date · 0 · Mon Oct 19 10:14:09 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-read-grant-1019
head · git log --oneline -1; git log --stat --format=%h ad4c8dfe..HEAD · 0 · (6 lines)
    147d9cd8 docs(gemini-read-grant-1019): build report — ad4c8dfe
    147d9cd8
    
     .../gemini-read-grant-1019-build-2026-10-19.md     | 162 +++++++++++++++++++++
     .../gemini-read-grant-1019-build-2026-10-19.result |  15 ++
     2 files changed, 177 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gemini-read-grant-1019/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gemini-read-grant-1019/docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.md" · 0 · BUILT · job: gemini-read-grant-1019 · tip: ad4c8dfe | on 0ac7746e | migration: none | offline 8796/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 223806
range · git log --oneline 0ac7746e..ad4c8dfe · 0 · (2 lines)
    ad4c8dfe feat(gemini-read-grant-1019): Gemini call only from its worktree, x1-copy kind, X1 per leg, builder no-fetch text (C1, C2, T1, H2, H3; L1, L3, L67)
    4a215342 wip(gemini-read-grant-1019): red
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h 0ac7746e..ad4c8dfe` →
```
ad4c8dfe

 docs/40 - DevDocs/prompts/SHADOW-HUB.md |  8 +--
 ops/desk/bare-guard.py                  |  5 +-
 ops/desk/desk-launch.sh                 | 91 +++++++++++++++++++++++++++++++--
 3 files changed, 94 insertions(+), 10 deletions(-)
4a215342

 tests/ops/test_bare_guard.py         |  39 +++++++
 tests/ops/test_desk_launch_shadow.py | 197 +++++++++++++++++++++++++++++++++++
 tests/ops/test_shadow_hub_file.py    |  47 ++++++++-
 3 files changed, 281 insertions(+), 2 deletions(-)
```
- DB: none: `git diff --name-only --no-renames 0ac7746e..ad4c8dfe` →
```
docs/40 - DevDocs/prompts/SHADOW-HUB.md
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
tests/ops/test_bare_guard.py
tests/ops/test_desk_launch_shadow.py
tests/ops/test_shadow_hub_file.py
```
every path under `ops/`, `tests/ops/` or `docs/`.
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-read-grant-1019-check` → exit 1, `No such file or directory` (fresh).
- House gates: as under `## AUTHORIZATION`.
- `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → `grok: UP` · `gemini: UP` (no HOUSE A header line: Sol not probed).
- Seats: no header line; Grok UP → **house A: Grok · house B: none (not needed)** (card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` →
```
30 <S>/STAGED-CARD
23405 <S>/diff.md
42237 <S>/files/827-gemini-read-grant-card.md
23972 <S>/files/gemini-read-grant-1019-build-2026-10-19.md
25155 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
57058 <S>/files/wt/ops/desk/bare-guard.py
153793 <S>/files/wt/ops/desk/desk-launch.sh
104763 <S>/files/wt/tests/ops/test_bare_guard.py
37266 <S>/files/wt/tests/ops/test_desk_launch_shadow.py
18461 <S>/files/wt/tests/ops/test_shadow_hub_file.py
762 <S>/rulings.md
STAGED 11 files · 486902 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-read-grant-1019-check`; commits 2 = PREFLIGHT's range count.)
`## READ` files by symbol, `stage-copy.sh`:
- `COPIED 7277 <S>/files/wt/ops/desk/scratch-clean.sh`
- `COPIED 43727 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (9771 bytes at `ls -la`): the HOUSE TEXT verbatim, `## NOT IN THIS JOB` and `## CHECK ASKS` whole, the ROWS' prose (THE PROBLEM, the citations paragraph, TERMS, RUN 2) whole, and the ROWS table and `## RECORDS` by line reference to the byte-identical card copy (`RECORDS` line below).
House A Grok started 10:15 (`date` 10:15:53), `run_in_background`, `timeout` 2700000; house B none (not needed).

## OWN FINDINGS
Written 10:2x, before either house list was opened (house A Grok still running; no completion notice yet).

FINDING O1
ROW: T1 (X4)
CLAIM: `ops/desk/desk-launch.sh:1223-1224` writes `x1-<leg>.log` as `{ printf 'conversation %s\n' "$id"; grep -F "soft-denying" "$clog"; } > "$xlog" || refuse …`; the group's status is `grep`'s, which is 1 when `cli.log` holds no `soft-denying` line, so a leg with no denial — leg 0a, the one leg H2 requires to succeed — is REFUSED (`the write of … failed`) after both `x1-0a.transcript` and `x1-0a.log` were already written (T1: "any failed test is refuse … nothing written"). H2 then reads that REFUSED as `X1 RESULT: leg 0a transcript not copied` and stops the arm on every clean run. No test pins it: `agy_run` (`tests/ops/test_desk_launch_shadow.py`) always appends the `SOFT` line.
RUN: TEST — `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o1_a_leg_with_no_soft_denying_line_is_copied(desk):
    wt = x1wt(desk)
    home = agy_run(desk, str(wt))
    log = home / "log" / "cli-20260101_000000.log"
    log.write_text(log.read_text().replace(SOFT + "\n", ""))
    done = x1copy(desk, "x-job-gemini", "0a")
    assert done.returncode == 0, done.stderr
    assert (wt / "x1-0a.log").read_text() == f"conversation {ID}\n"
    assert done.stdout.splitlines()[-1] == "X1-COPY: 0a soft-denying 0"
```
EXPECT: `AssertionError: REFUSED: x1-copy: 0a the write of …/x1-0a.log failed` / `assert 1 == 0`.

Read, no runnable defect found (recorded, not findings):
- X2: the guard ledgers log only blocked calls; 10 ledgers hold `"cwd": "/Users/cobalt/cobalt-wt/agy-trial"` lines (Grep), but none also holds the session's start cwd, so no ledger proves the hook `cwd` follows a `cd`. Leg 0f is the only proof; verdict (1) catches an admitted agy call. Stays the build's DECISION 2.
- X1: `seat` normalizes with `os.path.normpath` only (`ops/desk/bare-guard.py:790`), so a `..` path equal to `<target>` is `<target>`; a symlink, a case variant, an empty or relative cwd differ from `<target>` byte for byte and are refused. Grok / Sonnet / Terra calls take no cwd test (`:1217`, `head == "agy"`).
- X5: `scratch-clean.sh` admits `<WT>/<worktree>/x1-<leg>.*` (root (a), untracked); H2 removes the copies only under verdict (7).
- X6: the hub diff touches lines 12, 30, 42, 59 only (`git diff 0ac7746e..ad4c8dfe`).

## Findings
House A Grok finished 10:30 (`date` 10:30:30); `ls -la <S>` → `house-a.md` 3003 bytes, written by Grok; stdout ended with its path and `[exited with code 0]`. Its last line `FINDINGS: 3`. Every block has a `RUN:` line followed by a `def test_`.
- A1 · Grok · T1 · zero `soft-denying` lines makes `x1-copy` refuse after `cp` wrote the transcript (`desk-launch.sh:1223-1224`) · TEST
- A2 · Grok · H2 · the `X1 for Gemini` line holds `cli.log`, which H2's test list says it must not (`SHADOW-HUB.md:30`) · TEST
- A3 · Grok · X4 · a symlink at `brain/<id>` is followed; only `transcript.jsonl` itself is checked for a link (`desk-launch.sh:1221`) · TEST
House B: none (not needed).

## Dropped
none

## RUNS
Each run alone on the tip `ad4c8dfe` (tests pasted with the Edit tool, no form repair): `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short <the four ids>` → `4 failed, 15 warnings in 1.62s`.
- O1 · own · `tests/ops/test_desk_launch_shadow.py::test_check_o1_a_leg_with_no_soft_denying_line_is_copied` · `AssertionError: REFUSED: x1-copy: 0a the write of …/x1-0a.log failed` / `assert 1 == 0` · HELD
- A1 · Grok · `tests/ops/test_desk_launch_shadow.py::test_t1_zero_soft_denying_lines_still_exits_0` · `AssertionError: REFUSED: x1-copy: 0c the write of …/x1-0c.log failed` / `assert 1 == 0` · HELD (the same defect as O1)
- A2 · Grok · `tests/ops/test_shadow_hub_file.py::test_h2_the_x1_line_does_not_name_cli_log` · `AssertionError: assert 'cli.log' not in 'X1 for Gemi... to 0f (X1).'` (`… no agy, cli.log still points at leg 0e's run …`) · REJECTED — card row H2: the line "is replaced WHOLE by" the card's quoted text, which holds `cli.log still points at leg 0e's run` (amend 838 NOTE 1); the build's DECISION H2 kept the text verbatim. The test was removed again with the Edit tool. OPEN.
- A3 · Grok · `tests/ops/test_desk_launch_shadow.py::test_t1_a_linked_brain_directory_is_refused` · `AssertionError: X1-COPY: 0c conversation 00000000-…-000000000001 … X1-COPY: 0c copied …/x1-0c.transcript (12 bytes)` / `assert 0 == 1` · HELD (CHECK ASK X4 "follow a link")
Committed before any fix: `7a6d6408 wip(gemini-read-grant-1019): check red — O1, A1, A3`.

## FIXES
- O1, A1: `ops/desk/desk-launch.sh` kind `x1-copy`: `soft` is counted before the copy, and the log's `grep -F "soft-denying"` runs only when `soft` is not `0`, so a leg with no denial writes `conversation <id>` alone and exits 0; a failed log write now removes both copies before it refuses (T1's "nothing written").
- A3: the same block refuses when `brain`, `brain/<id>`, `.system_generated` or `logs` under `$AGY_HOME` is a link (`x1-copy: <leg> <dir> is a link`), before the transcript test.
- `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` → `133 passed, 15 warnings in 17.35s`.
- Committed `7e165648 fix(gemini-read-grant-1019): x1-copy copies a leg with no soft-denying line, refuses a link on the transcript path (check O1, A1, A3)`.
- DevDocs: no module page exists under `docs/40 - DevDocs/cobalt/` for `ops/desk/desk-launch.sh` (the build report's RECORDS, same search); none created.

## Suites
On `7e165648`. RESTARTS first: `uv run cobalt jobs restarts 0ac7746e..HEAD` → 8 rows (SHADOW-HUB.md DOCS; the build report and `.result` DOCS; `bare-guard.py`, `desk-launch.sh` "operator script; no Cobalt reader"; the three test files "test/documentation; no resident"), `RESTARTS: none`; no UNCLASSIFIED row.
"DB: none" card, W as BUILD-HUB gives it:
- (a0) `git diff --name-only --no-renames 0ac7746e` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.md`, `docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **cobalt_dev: not taken (DB: none — 8 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-read-grant-1019 offline --deploy-gate` → `tests/ops: run (deploy gate)` · `offline 8799/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-read-grant-1019-offline-20261019-103214.log` (exit 0). In the log: `941:4730 passed, 866 skipped, 4 xfailed, 36 warnings in 748.08s (0:12:28)` and `1015:4069 passed, 1 xfailed, 16 warnings in 913.68s (0:15:13)` (tests/ops, which holds the three check tests; the separate tests/ops line of (a0) is this run).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-read-grant-1019 livenote` → `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-read-grant-1019-livenote-20261019-110030.log` (exit 0).
- with-DB: not run (DB: none).
- `.env`: `ls /Users/cobalt/cobalt-wt/gemini-read-grant-1019/.env` → `No such file or directory` (never present).
- Each new test was shown red first (`## RUNS`) and passes at the tip.

## Scope
PREFLIGHT's path union: `SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, each in a row's `files` (C1, T1, H2, H3). My commits: `ops/desk/desk-launch.sh` (T1's `files`, inside its `x1-copy` block, which the fence leaves open) and `tests/ops/test_desk_launch_shadow.py` (T1's test file). No path inside `## NOT IN THIS JOB`.

## Checked against the branch
- (i) `git log --oneline ad4c8dfe..HEAD -- . ":(exclude)docs"` → `7e165648 fix(gemini-read-grant-1019): x1-copy copies a leg with no soft-denying line, refuses a link on the transcript path (check O1, A1, A3)` · `7a6d6408 wip(gemini-read-grant-1019): check red — O1, A1, A3`. `<tip now>` = `7e165648`.
- (ii) `git log --stat --format=%h ad4c8dfe..HEAD` → `7e165648` `ops/desk/desk-launch.sh | 12 +++++++++---`; `7a6d6408` `tests/ops/test_desk_launch_shadow.py | 42 ++++`; `147d9cd8` the build report and its `.result` (docs). No WIDENED path.
- (iii) `git log --oneline 0ac7746e..HEAD -- ops/desk/scratch-clean.sh ops/desk/desk-done.sh ops/desk/job-clean.sh ops/desk/desk-watch.sh` → empty. The other fenced items (the agy settings file, cards 717-719, launch lines) are no path of the diff (PREFLIGHT's name list).
- (iv) `grep -n -F "def <name>" tests/ops/test_desk_launch_shadow.py` → `893:def test_check_o1_a_leg_with_no_soft_denying_line_is_copied(desk):` · `904:def test_t1_zero_soft_denying_lines_still_exits_0(desk):` · `917:def test_t1_a_linked_brain_directory_is_refused(desk):`; `7a6d6408` (red) sits below `7e165648` (fix) in (i).
- (vi) `git log --stat --format=%h 0ac7746e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate list owed.
- (vii) The card's RECORDS commands all read under `/Users/cobalt/.gemini/` (`ls -la ~/.gemini/antigravity-cli/cli.log`, `grep` on its `log/cli-*.log`): not run — `## NOT IN THIS JOB` keeps the check off `~/.gemini`; the reports they cite are not on the check's read list.
- (viii) L32: this report holds constructed test values and paths only.

- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/gemini-read-grant-1019` alone.

## OPEN
- A2 (Grok, H2): REJECTED — `test_h2_the_x1_line_does_not_name_cli_log` runs red for its stated reason, but row H2 orders the line replaced WHOLE by text that holds `cli.log`. What would settle it: the desk rewords verdict (1) without `cli.log` and restores the assert, or records the text as right (a `SETTLED: A2 — R<n>` row).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- A2 (REJECTED, open; card text against card test): row H2's verbatim text names `cli.log` in verdict (1), and H2's test list says the line must not. The default I took: the hub stands as the card wrote it and the test is not added. The desk settles it in the fix round (reword verdict (1), or a `SETTLED` row). The build's DECISION H2 is the same item.

## RECORDS
- L74: one system block in this session asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Dropped findings: none. Every house produced its list (house A Grok `FINDINGS: 3`); house B not seated (`HOUSE B: as needed`).
- `HOUSE-INSTRUCTIONS.md` carried the ROWS table rows (C1-P1, ORDER) and the card's `## RECORDS` by line reference to the byte-identical copy `files/827-gemini-read-grant-card.md`, not inlined; the HOUSE TEXT, the ROWS prose, `## NOT IN THIS JOB` and `## CHECK ASKS` are inlined whole.
- A3's fix refuses a link at any of the four directories below `$AGY_HOME` on the transcript path. The card's T1 (6) names only the file. If real agy ever makes `brain/<id>` a link, x1-copy refuses and that leg FAILS (`transcript not copied`); this is the safe side.
- No extra lock take (DB: none). No `REFUSED, not needed` line. No `CONTINUED` line.
- files opened: 26 — CHECK-HUB.md, the card, the build report, BUILD-HUB.md (`## THE LOCK` to `## W`), `ops/desk/scratch-clean.sh`, `ops/desk/bare-guard.py` (`:780-829`), `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, `reports/cto-2026-09-24.md` (grep), `<S>/house-a.md`, 10 guard ledgers under `/Users/cobalt/cobalt-wt/.ledger/` (Grep, X2), the offline gate log (grep), and 4 task outputs (probe, Grok, the two gate calls).
- Check of `gemini-read-grant-1019`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gemini-read-grant-1019 · pass: 1 · tip: 7e165648 · house A: Grok FINDINGS: 3 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8799/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 197976
