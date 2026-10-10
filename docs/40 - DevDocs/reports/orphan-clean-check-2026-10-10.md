# orphan-clean-1010 — check, 2026-10-10

## §0 Headline
Check of `orphan-clean-1010` on `0ddb7114`: house A Sol (4 findings), house B Grok (4), own read (1). All 9 HELD by their runs, all fixed in `ops/desk/orphan-clean.sh` (`769a6e36`). Red first: `01b3fabf`.
The two that mattered (X1): a pid reused after `ps -A` was signalled (the identity read at verify was never compared with the candidate's command); and a launchctl answer carrying the "Could not find service" text anywhere hid the job's own pid, so the healthy resident was signalled. Also: the lsof proof now runs again before each signal; every failing `ps` prints `UNVERIFIED:` before REFUSED.
Suites green on `769a6e36`: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · `tests/ops` 2747 passed / 0 failed · cobalt_dev 0013, F2 = F0 · `.env` removed · RESTARTS none. ready: YES.

## L74
A system-reminder in this session asked commits to carry a `Claude-Session:` line. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 0 · 2f00206a921ae779002d02e3dfef7c108b9c8a7e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 50:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row; `grep -n "^| R19 " …` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Sat Oct 10 13:09:19 EDT 2026
status · git status --short --branch · 0 · ## ops/orphan-clean-1010
head · git log --oneline -1; git log --stat --format=%h 0ddb7114..HEAD · 0 · (5 lines)
    848016d4 docs(orphan-clean-1010): build report — 0ddb7114
    848016d4
    
     .../reports/orphan-clean-build-2026-10-10.md       | 185 +++++++++++++++++++++
     1 file changed, 185 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/orphan-clean-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/orphan-clean-1010/docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md" · 0 · BUILT · job: orphan-clean-1010 · tip: 0ddb7114 | on 1286d448 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 186094
range · git log --oneline 1286d448..0ddb7114 · 0 · (2 lines)
    0ddb7114 feat(orphan-clean-1010): ops/desk/orphan-clean.sh finds, verifies and kills an aset orphan by pid (O1-O4, L1, L3)
    2dede2d3 wip(orphan-clean-1010): red
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h 1286d448..0ddb7114`:
```
0ddb7114
 ops/desk/orphan-clean.sh | 264 +++
2dede2d3
 tests/ops/test_orphan_clean.py | 478 +++
```
Path union: `ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py`.
`git diff --name-only --no-renames 1286d448..0ddb7114` → `ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py` (all under `ops/` / `tests/ops/`; the card header carries no `DB: none` line, its RECORDS say the desk may add it).
`ls <S>` → `No such file or directory` (fresh).
House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` → exit 0:
```
sol: UP
grok: UP
gemini: OUT — OK.
```
house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed (not mandatory).
Lock: not taken at PREFLIGHT; no with-DB step yet.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
29601 <S>/diff.md
10924 <S>/files/229-orphan-clean-card.md
23310 <S>/files/orphan-clean-build-2026-10-10.md
10375 <S>/files/wt/ops/desk/orphan-clean.sh
17458 <S>/files/wt/tests/ops/test_orphan_clean.py
367 <S>/rulings.md
STAGED 6 files · 92035 bytes · commits 2
```
(commits 2 = PREFLIGHT's range count.) `stage-copy.sh`, one call each:
```
COPIED 4288 <S>/files/aset-orphan-answer-2026-10-10.md
COPIED 26125 <S>/files/cto-2026-10-10.md
COPIED 10356 <S>/files/wt/src/cobalt/voice/scratch.py
COPIED 3223 <S>/files/wt/ops/start_aset.sh
COPIED 2209 <S>/files/wt/ops/com.cobalt.aset.plist
COPIED 11524 <S>/files/wt/ops/desk/job-clean.sh
COPIED 4332 <S>/files/wt/ops/desk/house-probe.sh
COPIED 5726 <S>/files/wt/tests/ops/test_house_probe.py
COPIED 39601 <S>/files/wt/docs/40-DevDocs/prompts/STANDING-LIST.md
COPIED 15062 <S>/files/wt/src/cobalt/voice/web.py
COPIED 11553 <S>/files/wt/src/cobalt/aset/config.py
```
`<S>/HOUSE-INSTRUCTIONS.md` written (13581 bytes): HOUSE TEXT verbatim, ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, Files paragraph.
Houses started 13:10:46 EDT (date before launch): Sol task `b97d68oqd`, Grok task `b33hlmmdo`; `git status --short --branch` after return → `## ops/orphan-clean-1010`.

## OWN FINDINGS
FINDING O1
ROW: O4 / X1
CLAIM: The identity a signal is checked against is read by `ps -p` at `ops/desk/orphan-clean.sh:205` AFTER the `lsof` proof (`:177`, `:188`), and `:206-211` only checks that its ppid is 1, never that its command is the candidate's `<path>/python -m cobalt.aset`; a pid reused between `ps -A` / `lsof` and that read by any ppid-1 process is saved as "the orphan" at `:212` and `signal()` (`:243-246`) then matches it and sends TERM to a process that was never a candidate.
RUN: TEST — `tests/ops/test_orphan_clean.py`:
```python
def test_identity_read_at_verify_is_the_candidates(fake):
    t = r851_table()
    # every `ps -p` reading of the orphan's pid shows another ppid-1 program: the pid was reused after lsof
    t["procs"][3].update(reused_after=0, reused_command="/usr/sbin/some-daemon --serve")
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert fake.calls("kill") == []
    never_the_residents(fake)
```
EXPECT: on the tip `assert fake.calls("kill") == []` fails (`[['-TERM', '7002']]`), or the returncode assertion fails first with exit 0.

## Findings
Sol finished 13:16:21 EDT (notice after `## OWN FINDINGS` was written; its final message, output lines 6029–6135, written by me to `<S>/house-a.md`). Grok finished 13:35:15 EDT, wrote `<S>/house-b.md` itself (3352 bytes) and replied with that path. Both lists were opened only at 13:35, after both finished.
- A1 · Sol · X1 · the lock/port proof is taken only at verify; before a signal only the identity is re-read, so a process that released both is still killed · TEST
- A2 · Sol · X2 · `Could not find service` anywhere in launchctl's output wins before the exit code, so a non-zero answer with other error text is read as "no job pid" · TEST
- A3 · Sol · O2 · a failing `ps -A` goes straight to REFUSED without the `UNVERIFIED:` line row O2 (4) requires · TEST
- A4 · Sol · X2 · a failing `ps -p` in `ident_of` goes straight to REFUSED without `UNVERIFIED:` · TEST
- B1 · Grok · X1 · the `ps -p` identity at verify is checked for ppid 1 only, not for the candidate's command; a reused pid is signalled (= O1) · TEST
- B2 · Grok · O2 · a failing `ps -A` prints no `UNVERIFIED:` (= A3) · TEST
- B3 · Grok · X1 · a `running` launchctl print that also carries the `Could not find service` text loses the job pid, and the job's own pid is signalled · TEST
- B4 · Grok · O2 · `ident_of` refuses a failing `ps -p` with no `UNVERIFIED:` (= A4) · COMMAND

## Dropped
none (every block carries a `RUN:` line followed by a test function or one command with an allowed beginning).

## RUNS
All eight TEST findings were pasted into `tests/ops/test_orphan_clean.py` as written (no form repair) and run on tip `0ddb7114` in one call, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_orphan_clean.py::<the 8>` → `8 failed, 15 warnings in 4.80s`.
- O1 · own · `test_identity_read_at_verify_is_the_candidates` · `assert 0 == 1`; stdout `RUN: kill -TERM 7002` / `KILLED: 7002 (TERM)` · HELD
- B1 · Grok · `test_x1_ps_p_command_must_still_be_python_m_aset` · `assert 0 == 1`; `RUN: kill -TERM 7002` / `KILLED: 7002 (TERM)` · HELD
- A1 · Sol · `test_resource_ownership_is_rechecked_before_signal` · `assert 0 == 1`; `RUN: kill -TERM 7002` / `KILLED: 7002 (TERM)` · HELD (row O4 names only the identity re-read; no row says a process that no longer holds the lock or port must be signalled, and X1 asks "at the moment of the signal")
- A2 · Sol · `test_launchctl_not_found_plus_other_error_is_unverifiable` · `assert 0 == 1`; `RUN: kill -TERM 7002` · HELD
- B3 · Grok · `test_x1_not_found_substring_does_not_hide_the_job_pid` · `assert [['-TERM', '7300']] == []`; `KILLED: 7300 (TERM)` · HELD
- A3 · Sol · `test_ps_a_failure_prints_unverified_then_refuses` · `assert 0 == 1` (`len([])`) · HELD
- B2 · Grok · `test_ps_a_stderr_prints_unverified_then_refuses` · `assert []`; stderr `REFUSED: ps -A exited 1: ps: permission denied`, stdout empty · HELD
- A4 · Sol · `test_ps_p_failure_prints_unverified_then_refuses` · `assert 0 == 1` (`len([])`); stdout ends `VERIFIED: 7002 holds lock …` · HELD
- B4 · Grok · COMMAND `grep -n -E '…|…'` — a regex alternation, outside the hub's fixed-string grep rule, so not typed; its claim is word for word A4's and is judged by A4's test above: red for the stated reason · HELD (by A4's run)
Held tests committed red before any fix: `01b3fabf wip(orphan-clean-1010): check red — O1 A1 A2 A3 A4 B1 B2 B3`.

## FIXES
`769a6e36 fix(orphan-clean-1010): …` — `ops/desk/orphan-clean.sh` only:
- O1 / B1: the identity read at verify must show ppid 1 AND, after the 5-word `lstart`, the candidate's exact command; else `UNVERIFIED: <pid> — ps -p shows another command` and the all-or-nothing REFUSED.
- A1: the lsof lock/port proof (now one function, `prove`) runs again in `signal()` before each signal; neither held → `UNVERIFIED:` then `REFUSED: <pid> no longer holds the lock or port before <SIG>`.
- A2 / B3: "no job pid" only when launchctl exits non-zero and its whole answer is the one line `Could not find service "<job>" in domain for user gui: 501`; everything else goes to the exit-code / `state` / `pid` parse.
- A3 / B2: a failing `ps -A` prints `UNVERIFIED: ? — ps -A exited <n>: <stderr>` before REFUSED.
- A4 / B4: `ident_of` prints `UNVERIFIED: <pid> — ps -p exited <n>: <stderr>` before REFUSED.
- The header names the re-run proof, the exact not-found line and the identity rule (X5).
After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_orphan_clean.py` → `44 passed, 15 warnings in 17.18s` (0 failed). DevDocs line: none. No page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts (the build recorded the same).

## Suites
RESTARTS, `uv run cobalt jobs restarts 1286d448..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md	A	DOCS	-
ops/desk/orphan-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_orphan_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```
`sh /Users/cobalt/cobalt/ops/desk/gate.sh orphan-clean-1010 all --deploy` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, no migration) → exit 0:
```
offline 4196/0
lock: waited 0 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/orphan-clean-1010-all-20261010-133821.log
```
No skip marked `OUTSIDE the allowed set`. Log: `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0) · `944:code: 769a6e36 (clean)` · `2084:lock released`.
The gate's suites do not hold `tests/ops`, so: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2747 passed, 1 xfailed, 15 warnings in 507.15s (0:08:27)`.
`ls /Users/cobalt/cobalt-wt/orphan-clean-1010/.env` → `No such file or directory`.

## Scope
PREFLIGHT's union `ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py`, plus my commits on the same two files: every path is in rows O1–O4's `files`.

## Checked against the branch
(i) `git log --oneline 0ddb7114..HEAD -- . ":(exclude)docs"` → `769a6e36 fix(orphan-clean-1010): …` · `01b3fabf wip(orphan-clean-1010): check red — …`; tip now `769a6e36`.
(ii) `git log --stat --format=%h 0ddb7114..HEAD` → `769a6e36 ops/desk/orphan-clean.sh` · `01b3fabf tests/ops/test_orphan_clean.py` · `848016d4 …/reports/orphan-clean-build-2026-10-10.md` (docs). No WIDENED path.
(iii) `git log --oneline 1286d448..HEAD -- src ops/com.cobalt.aset.plist ops/start_aset.sh .claude/settings.json "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → empty.
(iv) `grep -n -F "def <test>" tests/ops/test_orphan_clean.py`, one line each: `484` O1 · `495` B1 · `504` A1 · `532` A2 · `547` B3 · `563` A3 · `578` B2 · `589` A4 (B4 by A4). `01b3fabf` (red) sits below `769a6e36` (fix) in (i).
(v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/orphan-clean-1010`.
(vi) `git log --stat --format=%h 1286d448..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate list owed.
(vii) The card's RECORDS name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (the one command is a `git -C … show`): nothing to run.
(viii) L32: the report holds constructed pids (7002, 7300) and the card's own incident pids only as quoted from the card; no ticker, price or date of his.

## OPEN
none.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none.

## RECORDS
- Dropped findings: none. Every house produced a list: Sol `FINDINGS: 4`, Grok `FINDINGS: 4`. Gemini probe `OUT — OK.` at PREFLIGHT (not seated; not needed).
- B4 (Grok's COMMAND) was not typed: `grep -n -E` with an alternation is outside the hub's fixed-string grep rule. Its claim is A4's word for word and was judged by A4's test.
- A1's fix runs the lsof proof before the KILL as well as before the TERM: an orphan that let go of both the lock and the port after a TERM is REFUSED, not KILLed. This follows X1's "at the moment of the signal"; the R854 shape (TERM ignored, the lock still held) still escalates (`test_kill_escalates_when_term_ignored` green).
- No `REFUSED, not needed` and no `CONTINUED` line. No extra lock take (the gate's one take, waited 0 min, released at log line 2084).
- Sol's run printed its findings twice; the final message (output lines 6029–6135) is `house-a.md`, as `## 1` (5) gives. Its earlier draft list (before line 6026) differs and is not the list.
- Not read: `areas/cobalt.md` (WHAT YOU READ (5)); nothing in this check turned on it.
- files opened: 11 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## RESTARTS`, `## W`); `ops/desk/orphan-clean.sh`; `tests/ops/test_orphan_clean.py`; the build report (`## RESTARTS` to the last line); the Sol output (house A); `<S>/house-b.md`; the house-probe output; the gate output; the `tests/ops` output.
- Check of `orphan-clean-1010`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: orphan-clean-1010 · pass: 1 · tip: 769a6e36 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 4 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 159076
