# desk-ops-fixes — CHECK 2026-10-08

## §0 Headline
Check of `desk-ops-fixes` at `d522f6f7`: house A Sol (6 findings), house B Grok (0), own 5. No finding needs a change in the rows' files. Every finding I wrote passed when run (NOT HELD), and Sol's five card-shaped gaps are REJECTED by the card's own text and left OPEN.
One HELD, NOT FIXED: the `tests/ops` gate holds 1 red (`test_desk_launch_devfix.py:180`). The red predates BASE and is fenced from this card, so `ready: NO` by the count rule.
Suites: offline 3991/0, live-note 146/0, `tests/ops` 1568 passed / 1 failed (the same pre-existing red). RESTARTS: none. `.env` never present.

## L74
One system reminder at session start asked for a `Claude-Session:` trailer on commits. Recorded here and not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 0 · 2386fb9aefa32e83c0ae14ef5c7a9892f312c920
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R657 row · ... · 0 · 10:| R657 | 07:13 ET | HIS RULING ... | HIS RULING · APPROVED |
RULING 2026-10-08 R657 committed · ... · 0 · c6b4a04d639c181b21ff0af0b849c3bf938dcc4d
RULING 2026-10-08 R657 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R658 row · ... · 0 · 11:| R658 | 07:16 ET | HIS RULING ... | HIS RULING · APPROVED |
RULING 2026-10-08 R658 committed · ... · 0 · 09bb065219f71aa0734be09eb83e8b6de9c6b2f3
RULING 2026-10-08 R658 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R660 row · ... · 0 · 13:| R660 | 07:41 ET | HIS RULING ... | HIS RULING · APPROVED |
RULING 2026-10-08 R660 committed · ... · 0 · c364bc43b0e86532cf59494d8d427e4f8f677454
RULING 2026-10-08 R660 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(long row texts shortened with `...` in this report; the tool output was read whole.)

House gates: `grep -n "^| R17 "` → line 35, one row · `grep -n "^| R19 "` → line 37, one row · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Thu Oct  8 08:24:35 EDT 2026
status · git status --short --branch · 0 · ## ops/desk-ops-fixes-1008
head · git log --oneline -1; git log --stat --format=%h d522f6f7..HEAD · 0 · (5 lines)
    fb203e62 docs(desk-ops-fixes): build report — d522f6f7
    fb203e62
     .../reports/desk-ops-fixes-build-2026-10-08.md     | 185 +++++++++++++++++++++
     1 file changed, 185 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/desk-ops-fixes-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../desk-ops-fixes-build-2026-10-08.md" · 0 · BUILT · job: desk-ops-fixes · tip: d522f6f7 | on b8b4f69c | migration: none | offline 3991/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 226565
range · git log --oneline b8b4f69c..d522f6f7 · 0 · (2 lines)
    d522f6f7 fix(desk-ops-fixes): desk is bg-only, unreadable list blocks, install-ops replaces plain files, close-timer notifies, close-wait rule (G1-G5, L1, L42)
    02d6222d wip(desk-ops-fixes): red — G1-G5 tests before the fix
PREFLIGHT OK
```
THE RANGE `git log --stat --format=%h b8b4f69c..d522f6f7`: d522f6f7 → `CTO-DESK-WAKEUP.md` +2, `ops/desk/close-timer.sh` 52, `ops/desk/desk-launch.sh` 29, `ops/desk/stop-guard.py` 79, `tests/ops/test_install_ops.py` 2 (5 files, +127 −37); 02d6222d → `tests/ops/test_close_timer.py` 71, `tests/ops/test_desk_wakeup_rule.py` 69, `tests/ops/test_install_ops.py` 66, `tests/ops/test_stop_guard.py` 64 (4 files, +252 −18). Commits: 2.
DB: none — `git diff --name-only --no-renames b8b4f69c..d522f6f7`: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `ops/desk/close-timer.sh`, `ops/desk/desk-launch.sh`, `ops/desk/stop-guard.py`, `tests/ops/test_close_timer.py`, `tests/ops/test_desk_wakeup_rule.py`, `tests/ops/test_install_ops.py`, `tests/ops/test_stop_guard.py` — every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` → `No such file or directory` (fresh).
House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0 · three lines whole:
```
sol: UP
grok: UP
gemini: OUT — OK.
```
house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed — the MANDATORY rule does not apply; both seats are up.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
36818 <S>/diff.md
16856 <S>/files/106-desk-ops-fixes-card.md
29445 <S>/files/desk-ops-fixes-build-2026-10-08.md
12060 <S>/files/wt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
6278 <S>/files/wt/ops/desk/close-timer.sh
65746 <S>/files/wt/ops/desk/desk-launch.sh
15322 <S>/files/wt/ops/desk/stop-guard.py
12395 <S>/files/wt/tests/ops/test_close_timer.py
2475 <S>/files/wt/tests/ops/test_desk_wakeup_rule.py
8216 <S>/files/wt/tests/ops/test_install_ops.py
25231 <S>/files/wt/tests/ops/test_stop_guard.py
1038 <S>/rulings.md
STAGED 12 files · 231880 bytes · commits 2
```
`stage-copy.sh`, one call each: `COPIED 4942 <S>/files/cto-2026-10-08.md` · `COPIED 6740 <S>/files/wt/src/cobalt/notify/mattermost.py` · `COPIED 1467 <S>/files/wt/ops/run_backup.sh` · `COPIED 4797 <S>/files/wt/ops/desk/wait-stop-line.sh` · `COPIED 2277 <S>/files/wt/ops/desk/idle-wake.py` · `COPIED 2112 <S>/files/wt/ops/desk/com.cobalt.close-timer.plist` · `COPIED 22364 <S>/files/wt/ops/README.md` · `COPIED 3429 <S>/files/wt/ops/desk/install-fixed.sh`.
`<S>/HOUSE-INSTRUCTIONS.md` written (16117 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` (the card has none), `## RECORDS`, and the Files paragraph.
Start (08:26:09 EDT, gates re-run: R17 line 35, R19 line 37, R19 commit `5055151d`): house A Sol, task `beecz64du`; house B Grok, task `b7d6ifx2a`; both `run_in_background`, timeout 2700000; `cd` back → `## ops/desk-ops-fixes-1008`.

## OWN FINDINGS
Written 08:3x EDT before either house list was opened. Premise check for G1 (C1): `grep -c -F "\"sessionKind\":\"bg\""` over this check's own transcript (a `claude --bg` session) → `148`: background transcripts do carry the key.

FINDING O1
ROW: G4
CLAIM: The clause "a failed send prints `NOTIFY FAILED: exit <n>` and the fire still exits 1" (`ops/desk/close-timer.sh:66-67`, `:72-73`) is pinned by no test: every test's stub sender exits 0.
RUN: TEST `tests/ops/test_close_timer.py`
```python
def test_check_o1_a_failed_send_prints_notify_failed_and_the_fire_still_exits_1(box):
    (box.rows.parent / "notify.sh").write_text("#!/bin/sh\nexit 3\n")
    box.launcher.unlink()
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode == 1
    assert "NOTIFY FAILED: exit 3" in done.stdout.splitlines()
```
EXPECT: if the clause is broken, the second assert fails; if built, green (NOT HELD).

FINDING O2
ROW: G4
CLAIM: The real-sender branch (`ops/desk/close-timer.sh:59-64`: source `$HOME/.cobalt_key` in a subshell, `uv run --project "$REPO" python -c …` with `close-timer: <line>` as the last argv) is pinned by no test; every test sets `COBALT_NOTIFY`.
RUN: TEST `tests/ops/test_close_timer.py`
```python
def test_check_o2_without_the_stub_the_sender_sources_the_key_and_runs_uv(box, tmp_path):
    home = tmp_path / "home"
    home.mkdir()
    (home / ".cobalt_key").write_text("export COBALT_MASTER_KEY=constructed-key-0001\n")
    uv = tmp_path / "bin" / "uv"
    uv.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$UV_ARGS"\nprintf "%s\\n" "${COBALT_MASTER_KEY:-unset}" > "$UV_KEY"\nexit 0\n')
    uv.chmod(0o755)
    box.launcher.unlink()
    env = dict(
        os.environ,
        PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}",
        FAKE_NOW=f"{EVENING} 21:05",
        COBALT_REPO_ROOT=str(box.repo),
        COBALT_WT_ROOT=str(box.wt),
        COBALT_DESK_LIST=str(box.listing),
        HOME=str(home),
        UV_ARGS=str(tmp_path / "uv-args.txt"),
        UV_KEY=str(tmp_path / "uv-key.txt"),
    )
    env.pop("COBALT_NOTIFY", None)
    env.pop("COBALT_MASTER_KEY", None)
    done = subprocess.run(["sh", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1
    args = (tmp_path / "uv-args.txt").read_text().splitlines()
    assert args[:4] == ["run", "--project", str(box.repo), "python"]
    assert args[-1] == f"close-timer: REFUSED: no launcher: {box.launcher}"
    assert (tmp_path / "uv-key.txt").read_text().strip() == "constructed-key-0001"
    assert "constructed-key-0001" not in done.stdout + done.stderr
    assert "NOTIFY FAILED" not in done.stdout
```
EXPECT: a broken branch fails one of the asserts; built as the row says, green (NOT HELD).

FINDING O3
ROW: G4
CLAIM: A missing `~/.cobalt_key` must still be loud: the subshell exits 78 (`ops/desk/close-timer.sh:61`) and `NOTIFY FAILED: exit 78` is printed, the fire exiting 1; no test pins it.
RUN: TEST `tests/ops/test_close_timer.py`
```python
def test_check_o3_no_key_file_prints_notify_failed_78(box, tmp_path):
    home = tmp_path / "home"
    home.mkdir()
    box.launcher.unlink()
    env = dict(
        os.environ,
        PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}",
        FAKE_NOW=f"{EVENING} 21:05",
        COBALT_REPO_ROOT=str(box.repo),
        COBALT_WT_ROOT=str(box.wt),
        COBALT_DESK_LIST=str(box.listing),
        HOME=str(home),
    )
    env.pop("COBALT_NOTIFY", None)
    done = subprocess.run(["sh", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1
    assert "NOTIFY FAILED: exit 78" in done.stdout.splitlines()
```
EXPECT: broken → an assert fails; built → green (NOT HELD).

FINDING O4
ROW: G4
CLAIM: `send_dm` does not raise on a disabled channel, it returns `SendResult(False, …)` (`src/cobalt/notify/mattermost.py:147-152`), and the `python -c` at `ops/desk/close-timer.sh:63` discards that result, so a disabled channel exits 0 and the fire prints no `NOTIFY FAILED` — a silent non-send.
RUN: COMMAND `grep -n -F "return SendResult(False" src/cobalt/notify/mattermost.py`
EXPECT: `152:        return SendResult(False, "channel disabled in configs/cobalt/notify.yaml", safe.hits)`

FINDING O5
ROW: G4
CLAIM: "The desk-missing notify never changes … the deferral … paths after it" (row G4; `ops/desk/close-timer.sh:118-133`) — no test runs a deferral fire with no `cto-desk` row.
RUN: TEST `tests/ops/test_close_timer.py`
```python
def test_check_o5_a_deferral_with_no_desk_notifies_once_and_still_defers(box):
    box.rows.write_text(HUB + "\n")
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode == 0, done.stderr
    assert "DEFERRED: deploy live — deploy-hub-set9" in done.stdout
    assert box.calls_made() == []
    assert box.notes() == [DESK_MISSING]
```
EXPECT: broken → an assert fails; built → green (NOT HELD).

OWN FINDINGS: 5

## Findings
House A Sol finished 08:33:26 EDT (exit 0; its final message, `FINDINGS: 6`, written by me to `<S>/house-a.md`). House B Grok finished 08:37:26 EDT (exit 0; it wrote `<S>/house-b.md` itself, 12 bytes: `FINDINGS: 0`). Both lists opened only after `## OWN FINDINGS` was written.
- S1 · Sol · SCOPE · the card's `tests/ops` gate is red on the tip, contrary to "0 failed" · COMMAND
- S2 · Sol · G4 · a disabled Mattermost channel returns `SendResult(False…)`; the timer discards it, exit 0, no `NOTIFY FAILED` · COMMAND
- S3 · Sol · G5 · the wake-up test pins only three fragments, not the rule's gating clauses · COMMAND
- S4 · Sol · G4 · the id-less-row "negative control" is red on BASE · COMMAND
- S5 · Sol · G3 · the link-elsewhere negative control is red on BASE (last-line shape moved) · COMMAND
- S6 · Sol · G5 · on a timed-out close whose report exists, the prescribed bare `desk-launch.sh close <date>` is refused (`desk-launch.sh:374`) · COMMAND
- House B (Grok): no findings.

## Dropped
none (every Sol block carries a `RUN: COMMAND` line beginning `uv run pytest` or `grep`).

## RUNS
Form repairs: Sol's `grep -n -E '<a>|<b>'` commands were run as one `grep -n -F` per pattern (UNATTENDED RULES: fixed strings only, no `|`); S5's pattern holds backticks (the hook refused it: "this call contains a backtick") and was run on the test name alone. No assertion changed.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | test `test_check_o1_…notify_failed…exit_1` in `tests/ops/test_close_timer.py` | `1 passed, 15 warnings in 1.12s` | NOT HELD (removed) |
| O2 | own | test `test_check_o2_…sources_the_key_and_runs_uv` | `1 passed, 15 warnings in 1.08s` | NOT HELD (removed) |
| O3 | own | test `test_check_o3_no_key_file_prints_notify_failed_78` | `1 passed, 15 warnings in 0.97s` | NOT HELD (removed) |
| O4 | own | `grep -n -F "return SendResult(False" src/cobalt/notify/mattermost.py` | `152:        return SendResult(False, "channel disabled in configs/cobalt/notify.yaml", safe.hits)` | REJECTED — card G4: "runs `uv run --project "$REPO" python -c 'import sys; from cobalt.notify import send_dm; send_dm(sys.argv[1])'`" (the command is the card's, byte for byte; the build report `## FOR THE CHECK` names the behaviour) |
| O5 | own | test `test_check_o5_a_deferral_with_no_desk_…` | `1 passed, 15 warnings in 1.08s` | NOT HELD (removed) |
| S1 | Sol | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` | `1 failed, 1568 passed, 1 xfailed, 15 warnings in 445.79s (0:07:25)`; the one red `tests/ops/test_desk_launch_devfix.py:180: AssertionError` — `assert '«INSTALL' in "# DEVFIX-HUB — the fixed dev-maintenance file (INSTALLED 2026-10-07 · STANDING = INSTALL: 2026-10-07 R644 …"`. `git diff --stat b8b4f69c..HEAD -- tests/ops/test_desk_launch_devfix.py "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → nothing; the test file's last commit is `d51c2125` on both this branch and main (`git log --oneline -3 -- …` / `git -C /Users/cobalt/cobalt log --oneline -3 -- …`) | HELD, NOT FIXED — `tests/ops/test_desk_launch_devfix.py` (outside the rows' files; the red predates BASE and is not this build's — build DECISION W-1) |
| S2 | Sol | `grep -n -F "send_dm(sys.argv[1])" ops/desk/close-timer.sh` · `grep -n -F "return SendResult(False" src/cobalt/notify/mattermost.py` | `63:            uv run --project "$REPO" python -c 'import sys; from cobalt.notify import send_dm; send_dm(sys.argv[1])' "close-timer: $1"` · `152:        return SendResult(False, "channel disabled in configs/cobalt/notify.yaml", safe.hits)` | REJECTED — card G4, the same line as O4 (same finding) |
| S3 | Sol | `grep -n -A8 "^def test_the_wakeup_holds_the_close_wait_rule" tests/ops/test_desk_wakeup_rule.py` | `:36-43`: the loop over exactly `"CLOSE WAIT (his 10-08 R658)"`, `"wait-stop-line.sh \"<close report>\" '^CLOSE PUSHED '"`, `"desk-launch.sh close <date> yourself"` | REJECTED — card G5 (a): "The wake-up holds the line's fixed parts: `CLOSE WAIT (his 10-08 R658)`, `wait-stop-line.sh "<close report>" '^CLOSE PUSHED '`, `desk-launch.sh close <date> yourself`" |
| S4 | Sol | `grep -n -F "test_g4_id_less_rows_do_not_crash" "<build report>"` · `grep -n -F "DECISION G4-1" "<build report>"` | `100:- G4 test_g4_id_less_rows…: assert [] == ['close-timer...unch.sh desk']. The card names it a negative control, but its "exactly one desk-missing notify" cannot hold on BASE (DECISION G4-1).` · `174:- DECISION G4-1: …` | REJECTED — card G4: the test's required assertion ("exactly one desk-missing notify") is the card's; it cannot be green on BASE, which has no notify |
| S5 | Sol | `grep -n -F "test_an_existing_link_to_elsewhere_is_never_re_pointed" "<build report>"` | `95:- G3 test_an_existing_link_to_elsewhere_is_never_re_pointed: - install-ops: 1 linked, 1 replaced, 1 kept / + install-ops: 1 linked, 2 kept. Only the moved last-line shape is red; its KEPT alpha.sh and readlink asserts come before that line and pass.` | REJECTED — card G3: "`test_an_existing_link_to_elsewhere_is_never_re_pointed` (`:97-104`, its last-line assert moves to the new shape)" |
| S6 | Sol | `grep -n -F "CLOSE WAIT" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · `grep -n -F "the close report already exists" ops/desk/desk-launch.sh` | `44:CLOSE WAIT (his 10-08 R658): … It times out (exit 2) and the report still does not end in CLOSE PUSHED → run sh /Users/cobalt/.claude/ops/desk-launch.sh close <date> yourself; one §4 row.` · `374:        [ ! -e "$creport" ] \|\| refuse "the close report already exists: $creport (a new worker names its CONTINUE step)"` | REJECTED — card G5: the line's text is the card's verbatim (his 10-08 R658). The gap is real: a report that exists but never pushed makes the prescribed command REFUSE (loud, not silent). It stays OPEN |

No HELD test → no `wip(desk-ops-fixes): check red` commit; `git status --short --branch` after the removals → `## ops/desk-ops-fixes-1008` (clean).

## FIXES
none. S1 is HELD, NOT FIXED: the fix (`tests/ops/test_desk_launch_devfix.py:180`) is outside the rows' files and inside the fence ("Any file outside the ROWS' `files` cells").

## Suites
No commit of mine: the tip is the build's `d522f6f7` (HEAD `fb203e62` adds only the build report). DB: none card — W as `BUILD-HUB.md` gives it ((a0), (a), (e), `tests/ops`); `--deploy` not typed.
- RESTARTS: `uv run cobalt jobs restarts b8b4f69c..HEAD` → the table whole: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md M DOCS -` · `docs/40 - DevDocs/reports/desk-ops-fixes-build-2026-10-08.md A DOCS -` · `ops/desk/close-timer.sh M operator script; no Cobalt reader -` · `ops/desk/desk-launch.sh M operator script; no Cobalt reader -` · `ops/desk/stop-guard.py M operator script; no Cobalt reader -` · `tests/ops/test_close_timer.py M test/documentation; no resident -` · `tests/ops/test_desk_wakeup_rule.py A test/documentation; no resident -` · `tests/ops/test_install_ops.py M test/documentation; no resident -` · `tests/ops/test_stop_guard.py M test/documentation; no resident -` · `RESTARTS: none`.
- (a0) PREFLIGHT's `git diff --name-only --no-renames b8b4f69c..d522f6f7`: 8 paths, all under `ops/`, `tests/ops/`, `docs/` → `cobalt_dev: not taken (DB: none — 8 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-ops-fixes-1008 offline` → exit 0: `offline 3991/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-ops-fixes-1008-offline-20261008-084539.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-ops-fixes-1008 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-ops-fixes-1008-livenote-20261008-085546.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1: `1 failed, 1568 passed, 1 xfailed, 15 warnings in 445.79s (0:07:25)`, the one red `tests/ops/test_desk_launch_devfix.py:180` (S1; red before BASE, not this build's).
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/desk-ops-fixes-1008/.env` → `No such file or directory` (never present).

## Scope
PREFLIGHT path union (8 paths) against the rows' `files`: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` (G1, G2); `ops/desk/desk-launch.sh`, `tests/ops/test_install_ops.py` (G3); `ops/desk/close-timer.sh`, `tests/ops/test_close_timer.py` (G4); `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `tests/ops/test_desk_wakeup_rule.py` (G5). Every path is in a row. My commits: none.

## Checked against the branch
- (i) `git log --oneline d522f6f7..HEAD -- . ":(exclude)docs"` → empty (no commit of mine); `<tip now>` = `d522f6f7`.
- (ii) `git log --stat --format=%h d522f6f7..HEAD` → `fb203e62`: `.../reports/desk-ops-fixes-build-2026-10-08.md | 185 +++` only (docs).
- (iii) `git log --oneline b8b4f69c..HEAD -- ops/desk/install-fixed.sh ops/desk/desk-list.sh ops/desk/com.cobalt.close-timer.plist src` → empty.
- (iv) no HELD test was committed (S1 is a COMMAND finding; its fix lies outside the rows).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/desk-ops-fixes-1008`.
- (vi) `git log --stat --format=%h b8b4f69c..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate-list change owed.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command to rerun.
- (viii) L32: this report holds constructed values and repo paths only.

## OPEN
- S1 · HELD, NOT FIXED — `tests/ops/test_desk_launch_devfix.py:180` still asserts `«INSTALL` in `DEVFIX-HUB.md`, which his R644 install (`71629bcb`) removed. It is red on BASE and on main, outside this card's files. What would settle it: a one-line test fix on its own card (the desk's), then `tests/ops` → 0 failed.
- S2 / O4 · REJECTED — card G4 spells `send_dm(sys.argv[1])`. A Mattermost channel set `enabled: false` makes `send_dm` return `SendResult(False…)` (`mattermost.py:152`), so the timer exits 0 with no `NOTIFY FAILED` line, and the non-send is silent in `close-timer.out`. What would settle it: a ruling whether the timer must check `.sent` (e.g. `sys.exit(0 if send_dm(...).sent else 1)`), and a test with a stub `uv`.
- S3 · REJECTED — card G5 (a) names the three fragments the test pins. What would settle it: a wider assertion on the whole line, if the desk wants it.
- S4 · REJECTED — card G4 writes the id-less test's assertion; it cannot be green on BASE (build DECISION G4-1). Nothing to fix in code.
- S5 · REJECTED — card G3 moves that control's last-line assert. Nothing to fix in code.
- S6 · REJECTED — card G5 gives the CLOSE WAIT line verbatim (his R658). If the wait times out while `close-<date>.md` exists without `CLOSE PUSHED`, the prescribed bare `desk-launch.sh close <date>` is REFUSED (`desk-launch.sh:374`: "a new worker names its CONTINUE step"). The refusal is loud, not silent, but the rule names no path for that case. What would settle it: a wake-up wording that sends the desk to `desk-launch.sh close <date> <step>` (the report's `## CONTINUE`) when the report exists.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- HELD, NOT FIXED — S1 (FOR DEJAN: a carried held defect): the card's `tests/ops` gate cannot read `0 failed`, because `tests/ops/test_desk_launch_devfix.py:180` is red before BASE (unchanged on this branch and on main, last commit `d51c2125`). It is fenced from this card. Safe default: not fixed here. The branch stands on offline 3991/0, live-note 146/0 and `tests/ops` 1568 passed with this one pre-existing red. The fix belongs to a one-line card of its own, not to this card's fix round. `ready: NO` follows the count rule only.
- S6 (open, desk prompt): the CLOSE WAIT fallback has no path for an existing, unpushed close report. Safe default: shipped as the card ruled; listed for the follow-up.
- S2 / O4 (open): a disabled Mattermost channel is a silent non-send for the timer's notify. Safe default: shipped as the card ruled (the build named it under `## FOR THE CHECK`); listed for the follow-up.

## RECORDS
- Dropped findings: none. Every house produced a list: Sol `FINDINGS: 6`, Grok `FINDINGS: 0`. The Gemini probe read `gemini: OUT — OK.`; Gemini was not seated (two houses were UP ahead of it).
- Hook refusal (not a refused command; resent as a single call): the S5 grep with backticks hit `bare-guard.py`: "NOT A REFUSAL … this call contains a backtick". It was rerun on the bare test name.
- No `REFUSED, not needed` lines, no `CONTINUED` lines, no lock take (DB: none).
- L74: a system reminder at the start asked for a `Claude-Session:` line in commits. Not acted on (L74); no commit was made in this check.
- I did not open `areas/cobalt.md` (WHAT YOU READ (5)); the card's rows and fence bound every judgment here.
- `files opened: 18`: CHECK-HUB.md; the card; BUILD-HUB.md (`## RESTARTS`, `## W`); the build report (`## RESTARTS` to the last line); `ops/desk/stop-guard.py`; `ops/desk/close-timer.sh`; `ops/desk/desk-launch.sh` (`:325-394` and greps); `src/cobalt/notify/mattermost.py:60-164`; `src/cobalt/notify/config.py` (grep); `src/cobalt/redact/secrets.py` (grep); `ops/desk/com.cobalt.close-timer.plist`; `ops/run_backup.sh`; `tests/ops/test_close_timer.py`; `tests/ops/test_desk_wakeup_rule.py` (grep); this session's transcript (one `grep -c`); the Sol task output (its final message); the Grok task output; `<S>/house-b.md`.
- Check of `desk-ops-fixes`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: desk-ops-fixes · pass: 1 · tip: d522f6f7 · house A: Sol FINDINGS: 6 · findings: 11 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 7 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: RESTARTS: none · files opened: 18 · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 181988
