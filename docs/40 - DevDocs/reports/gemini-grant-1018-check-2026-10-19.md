# gemini-grant-1018 — check, 2026-10-19

## §0 Headline
Check of `gemini-grant-1018`, tip `fd9f0cb6` → `cd5e0d7c`. House A was Grok (2 findings); house B was none (as needed). I wrote 6 findings of my own, and none held.
Held: G-1 (JSON refusal ran after the read_url grep) is FIXED in `cd5e0d7c`. G-2 (the build report never quotes three G1 reds) is HELD, NOT FIXED, because the fix lies in the fenced build report.
Suites green: offline 8679/0 (deploy gate), live-note 147/0, tests/ops 4025 passed. DB: none.
ready: NO, on G-2 alone (a reporting gap; `git log -S` shows the three reds must be red on BASE). It goes to the fix round.

## L74
none (see `## RECORDS` for the attribution reminder).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 0 · b6eca9a1812fd9475b0aed23c99cbd8f492a08ac
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md" · 0 · nothing
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
House gates: `grep -n "^| R17 "` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 "` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 19 04:14:02 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-grant-1018
head · git log --oneline -1; git log --stat --format=%h fd9f0cb6..HEAD · 0 · (6 lines)
    3bfd3710 docs(gemini-grant-1018): build report — fd9f0cb6
    3bfd3710
    
     .../reports/gemini-grant-1018-build-2026-10-18.md  | 213 +++++++++++++++++++++
     .../gemini-grant-1018-build-2026-10-18.result      |  15 ++
     2 files changed, 228 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gemini-grant-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gemini-grant-1018/docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md" · 0 · BUILT · job: gemini-grant-1018 · tip: fd9f0cb6 | on c0ebb874 | migration: none | offline 8678/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 206491
range · git log --oneline c0ebb874..fd9f0cb6 · 0 · (2 lines)
    fd9f0cb6 feat(gemini-grant-1018): desk-launch.sh adds and removes the Gemini grant; grant-sweep (G1, G2, G3, H1; L1, L3, L28)
    324c8fe9 wip(gemini-grant-1018): red
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h c0ebb874..fd9f0cb6` · exit 0:
```
fd9f0cb6
 docs/40 - DevDocs/prompts/SHADOW-HUB.md |   4 +-
 ops/desk/desk-launch.sh                 | 260 +++++++++++++++++++++++++++++++-
 2 files changed, 255 insertions(+), 9 deletions(-)
324c8fe9
 tests/ops/test_desk_launch_shadow.py | 220 +++++++++++++++++++++++++++++++++--
 tests/ops/test_shadow_hub_file.py    |  16 +++
 2 files changed, 229 insertions(+), 7 deletions(-)
```
DB: none · `git diff --name-only --no-renames c0ebb874..fd9f0cb6` · exit 0 · whole: `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py` — every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · whole: `grok: UP` / `gemini: UP`. No `HOUSE A: OpenAI` header line → Sol not probed. `HOUSE B: as needed` → **house A: Grok (grok-4.7) · house B: none (not needed)**.
PROVEN BY FIRST REAL USE: the write strings (`Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)` — this report, first Write ok).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · whole:
```
25 …/gemini-grant-1018-check/STAGED-CARD
27558 …/gemini-grant-1018-check/diff.md
21244 …/gemini-grant-1018-check/files/800-gemini-grant-card.md
22380 …/gemini-grant-1018-check/files/gemini-grant-1018-build-2026-10-18.md
21185 …/gemini-grant-1018-check/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
149101 …/gemini-grant-1018-check/files/wt/ops/desk/desk-launch.sh
28655 …/gemini-grant-1018-check/files/wt/tests/ops/test_desk_launch_shadow.py
16397 …/gemini-grant-1018-check/files/wt/tests/ops/test_shadow_hub_file.py
762 …/gemini-grant-1018-check/rulings.md
STAGED 9 files · 287307 bytes · commits 2
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920`; commits 2 = PREFLIGHT's count.)
`sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh ".../2026-10-18/759-agy-read-card.md" <S>/files/759-agy-read-card.md` → `COPIED 16636 …/gemini-grant-1018-check/files/759-agy-read-card.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph). House A Grok started 04:15:51 EDT (`date`), gates re-run (R17 1 row, R19 1 row) before it; `git status --short --branch` after the return → `## ops/gemini-grant-1018`.

## OWN FINDINGS
Written before either house list was opened. Each is a probe of a clause or CHECK ASK no build test pins; the CLAIM states the defect it would show.

FINDING O1
ROW: G1 (a) / X1
CLAIM: the `<grant>` ≥ 2 refusal (`ops/desk/desk-launch.sh:339`, `plan`) is pinned by no test; a file holding the grant twice may be written or admitted.
RUN: TEST `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o1_a_doubled_grant_is_refused_and_not_written(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    write_agy(desk, [grant, grant, *HOUSE])
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            f'shadow: gemini: {desk.agy} holds "{grant}" 2 times')
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()
```
EXPECT: if the claim holds, the `refused` assertion fails (exit 0 or another text).

FINDING O2
ROW: G2 (a) / X4
CLAIM: a `claude agents --json` row named `<n>-gate` with no pid (an ended seat) must make that rule an ORPHAN (`ops/desk/desk-launch.sh:303`); if any row with the name counted as LIVE, the launch would be refused.
RUN: TEST `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o2_a_gate_row_without_a_pid_is_an_orphan(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    other = f"write_file({desk.wt}/x-job-other/)"
    write_agy(desk, [other, *HOUSE])
    fake_claude(desk, agents=json.dumps([{"id": "s1", "pid": None, "name": "x-job-other-gate", "status": "idle", "state": "idle"}]))
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    assert f"ORPHAN: removed {other} from {desk.agy} (no live x-job-other-gate)" in done.stderr
    assert json.loads(desk.agy.read_text())["permissions"]["allow"] == [grant, *HOUSE]
```
EXPECT: if the claim holds, exit 1 with the serial-rule refusal.

FINDING O3
ROW: G1 (c) / X1
CLAIM: a relaunch whose grant is already present writes nothing, so its failed launch must leave the present grant in place (`ops/desk/desk-launch.sh:2684-2686`: the trap is set only after an add); if the trap were set on this path, the seat's live grant would be removed.
RUN: TEST `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o3_a_failed_relaunch_keeps_the_present_grant(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    write_agy(desk, [grant, *HOUSE])
    before = desk.agy.read_bytes()
    fake_claude(desk, bg_rc=1)
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 1, done.stderr
    assert f"GRANT: {grant} already in {desk.agy}" in done.stderr
    assert "GRANT: removed" not in done.stderr
    assert desk.agy.read_bytes() == before
```
EXPECT: if the claim holds, `GRANT: removed` is in stderr and the bytes differ.

FINDING O4
ROW: G1 (b) / X5
CLAIM: the empty-list add (`ops/desk/desk-launch.sh:357-358`, indent of the `[` line plus two spaces, no comma) and its trap removal are pinned by no test; the file may not come back byte-equal.
RUN: TEST `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o4_an_empty_allow_list_takes_the_grant_and_gives_it_back(desk):
    card = signed_gemini(desk)
    b = b'{\n  "permissions": {\n    "allow": [\n    ]\n  }\n}\n'
    desk.agy.write_bytes(b)
    line = f'      "write_file({desk.wt}/x-job-gemini/)"\n'.encode()
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    a = desk.agy.read_bytes()
    assert a.count(line) == 1 and a.replace(line, b"", 1) == b
    desk.agy.write_bytes(b)
    fake_claude(desk, bg_rc=1)
    failed = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert failed.returncode == 1, failed.stderr
    assert desk.agy.read_bytes() == b
```
EXPECT: if the claim holds, one of the byte assertions fails.

FINDING O5
ROW: X4
CLAIM: with another worktree's gemini rule present, an unreadable `claude agents --json` must refuse the real launch before any write (`ops/desk/desk-launch.sh:295-302`); no build test runs this on the launch path (only on `grant-sweep`).
RUN: TEST `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o5_an_unreadable_listing_refuses_the_launch_before_any_write(desk):
    card = signed_gemini(desk)
    write_agy(desk, [f"write_file({desk.wt}/x-job-other/)", *HOUSE])
    fake_claude(desk, agents_rc=1)
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            "shadow: gemini: claude agents --json could not be read; nothing written")
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()
    assert not (desk.wt / "x-job-gemini").exists()
```
EXPECT: if the claim holds, the refusal text differs, the bytes change, or the worktree exists.

FINDING O6
ROW: G2 (DEPLOY PROOF marker)
CLAIM: the words `(card 759 serial rule)` stand on exactly one line of the script (card G2 (a)).
RUN: COMMAND `grep -c -F "(card 759 serial rule)" ops/desk/desk-launch.sh`
EXPECT: if the claim of a defect holds, a count other than `1`.

## Findings
House A Grok finished at 04:33:03 EDT (`date` at the notice). It wrote `<S>/house-a.md` itself (1855 bytes), ending `FINDINGS: 2`; its stdout was only the path. House B: none (not needed).
- G-1 · Grok · G1 · read_url/execute_url grep runs before AGY_PY's JSON/shape refusals, so a truncated file mentioning `read_url(` gets the read_url refusal · TEST
- G-2 · Grok · G1 · the build report never quotes the three G1 refusal texts as first failing lines on BASE · COMMAND

## Dropped
none. `grep -n -F "RUN:"` matches each block: G-1 is followed by `def test_`, and G-2 is followed by a `grep` line.

## RUNS
The six tests (O1–O5 and G-1) were placed at the end of `tests/ops/test_desk_launch_shadow.py` and run together. Each was pasted as written, with no form repair. Run: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py -k "check_o1_a_doubled or check_o2_a_gate or check_o3_a_failed or check_o4_an_empty or check_o5_an_unreadable or truncated_json_that_mentions"` → `1 failed, 5 passed, 43 deselected, 15 warnings in 3.94s`.
- O1 · own · TEST `test_check_o1_a_doubled_grant_is_refused_and_not_written` · passed · NOT HELD (removed again)
- O2 · own · TEST `test_check_o2_a_gate_row_without_a_pid_is_an_orphan` · passed · NOT HELD (removed again)
- O3 · own · TEST `test_check_o3_a_failed_relaunch_keeps_the_present_grant` · passed · NOT HELD (removed again)
- O4 · own · TEST `test_check_o4_an_empty_allow_list_takes_the_grant_and_gives_it_back` · passed · NOT HELD (removed again)
- O5 · own · TEST `test_check_o5_an_unreadable_listing_refuses_the_launch_before_any_write` · passed · NOT HELD (removed again)
- O6 · own · COMMAND `grep -c -F "(card 759 serial rule)" ops/desk/desk-launch.sh` · `1` · NOT HELD
- G-1 · Grok · TEST `test_g1_truncated_json_that_mentions_read_url_is_the_json_refusal` · failed; first failing line: `E       AssertionError: REFUSED: shadow: gemini: <tmp>/agy-settings.json holds a read_url or execute_url rule; X1's fetch must stay refused` (`tests/ops/test_desk_launch_shadow.py:179`, called from `:749`) · **HELD**. Card G1 (a) puts the JSON refusal first, "after the readable-file refusal `:1756`". The build's DECISION 2 put all four refusals after the raw greps, to keep the one-line-file controls green. That reason covers the shape refusal only, because those controls hold valid JSON.
- G-2 · Grok · COMMAND `grep -n -F -e "is not valid JSON with a permissions.allow list" -e "is not one rule per line" -e "is not its WORKTREE" ".../gemini-grant-1018-build-2026-10-18.md"` · no output · **HELD, NOT FIXED — `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md`**. The build report does not quote the first failing line of `test_g1_invalid_json_…`, `test_g1_an_inline_allow_list_…` or `test_g1_a_job_that_is_not_its_worktree_…` (its `:79` says they "fell in the truncated part"), although card G1 asks for "first failing line each". The substance is settled by these runs: `git log --oneline -S"<text>" c0ebb874..fd9f0cb6 -- ops/desk/desk-launch.sh` → `fd9f0cb6 feat(gemini-grant-1018): …` for each of the three texts. Each enters at the fix commit, so BASE cannot print it, and each `refused(…)` assertion fails on BASE. The missing quote belongs to the build report, which the fence closes to this check (`## NOT IN THIS JOB`: "every report").
Red commit: `74217d0a wip(gemini-grant-1018): check red — G-1`.

## FIXES
- G-1: FIXED. `ops/desk/desk-launch.sh` gains a new `AGY_PY` op, `parse`, which exits 0 once the JSON and `permissions.allow` check passes. The gemini block calls it right after `grule=`, before the `read_url(`/`execute_url(` grep, and the op list in the header comment names it. The shape, JOB, count and serial refusals stay where the build put them (its DECISION 2). After the fix: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` → `99 passed, 15 warnings in 13.54s`. Commit `cd5e0d7c fix(gemini-grant-1018): G1's JSON refusal runs before the read_url grep (check G-1)`. DevDocs line: none written. A Glob of `docs/40 - DevDocs/**/*desk*` finds no module page for `ops/desk/desk-launch.sh` under `docs/40 - DevDocs/cobalt/` (an operator script, no Cobalt module).
- G-2: HELD, NOT FIXED — `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md` (fenced; the fix round quotes the three first failing lines, or carries it).

## Suites
The tip is `cd5e0d7c`. DB: none, so the W form is (a0), (a) and (e), with `--deploy-gate` on the offline call.
- RESTARTS: `uv run cobalt jobs restarts c0ebb874..HEAD` → six rows (`SHADOW-HUB.md` DOCS, the build report `.md` and `.result` DOCS, `ops/desk/desk-launch.sh` `operator script; no Cobalt reader`, and the two test files `test/documentation; no resident`), all `-`; last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames c0ebb874` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md`, `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.result`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path is under `ops/`, `tests/ops/` or `docs/`, so **cobalt_dev: not taken (DB: none — 6 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-grant-1018 offline --deploy-gate` · exit 0 · `tests/ops: run (deploy gate)` / `offline 8679/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-grant-1018-offline-20261019-043606.log`. The build's figure was 8678, and the one added test is G-1's.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-grant-1018 livenote` · exit 0 · `live-note 147/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-grant-1018-livenote-20261019-043607.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 · `4025 passed, 1 xfailed, 16 warnings in 923.68s (0:15:23)`.
- with-DB: not run (DB: none). `.env`: never present. `ls /Users/cobalt/cobalt-wt/gemini-grant-1018/.env` → `No such file or directory` (05:04 EDT).

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (H1), `ops/desk/desk-launch.sh` (G1, G2), `tests/ops/test_desk_launch_shadow.py` (G1–G3), `tests/ops/test_shadow_hub_file.py` (H1). Each path is in some row's `files`. My commits are `74217d0a` (`tests/ops/test_desk_launch_shadow.py`) and `cd5e0d7c` (`ops/desk/desk-launch.sh`), both rows' files.

## Checked against the branch
- (i) `git log --oneline fd9f0cb6..HEAD -- . ":(exclude)docs"` → `cd5e0d7c fix(gemini-grant-1018): G1's JSON refusal runs before the read_url grep (check G-1)` / `74217d0a wip(gemini-grant-1018): check red — G-1`. `<tip now>` = `cd5e0d7c`.
- (ii) `git log --stat --format=%h fd9f0cb6..HEAD` → `cd5e0d7c` `ops/desk/desk-launch.sh | 8 +++++++-`; `74217d0a` `tests/ops/test_desk_launch_shadow.py | 12 ++++++++++++`; `3bfd3710` the build report and `.result` (docs). No path is outside the rows' files.
- (iii) `git log --oneline c0ebb874..HEAD -- ops/desk/bare-guard.py ops/desk/desk-done.sh ops/desk/job-clean.sh ops/desk/desk-watch.sh` → empty. The settings file is outside the repo. Cards 717–719, the dated prompts and the reports are not in the diff (ii).
- (iv) `grep -n -F "def test_g1_truncated_json_that_mentions_read_url_is_the_json_refusal" tests/ops/test_desk_launch_shadow.py` → `681:def test_g1_truncated_json_that_mentions_read_url_is_the_json_refusal(desk):`. In (i) its red commit `74217d0a` sits below its fix commit `cd5e0d7c`. G-2 is a COMMAND finding and has no test.
- (v) `ls /Users/cobalt/cobalt-wt/gemini-grant-1018/.env` → `No such file or directory`. `git status --short --branch` → `## ops/gemini-grant-1018`.
- (vi) `git log --stat --format=%h c0ebb874..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-list entry is owed.
- (vii) Card `## RECORDS` greps: `grep -c -F "write_file(/Users/cobalt/cobalt-wt/strike-fallback-env-1018-gemini/)" /Users/cobalt/.gemini/antigravity-cli/settings.json` → `0`, the same as the record. `grep -n -F '"allow"' …settings.json` was not run, because it prints a line of that file and the fence forbids the check to print the file. The record stands as the desk's.
- (viii) L32: this report holds only constructed test values and repo paths; it holds no ticker, price or date of his.

## OPEN
- G-2: HELD, NOT FIXED — `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md`. It is settled when the fix round quotes the first failing line on BASE of the three G1 refusal tests (`FIXED: G-2 — …`), or carries it (`CARRIED: G-2 — … — R<n>`).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
- **G-2: HELD, NOT FIXED — `docs/40 - DevDocs/reports/gemini-grant-1018-build-2026-10-18.md`.** Card G1's red column asks for each named test's first failing line on BASE. The build report gives none for `test_g1_invalid_json_is_refused_and_not_written`, `test_g1_an_inline_allow_list_is_refused` or `test_g1_a_job_that_is_not_its_worktree_is_refused`: its E2 `:79` says the lines "fell in the truncated part of the tool output". Grok's grep for the three refusal texts in the report prints nothing. The substance does hold: `git log -S` shows each text first enters at `fd9f0cb6`, so each of the three `refused(…)` assertions must fail on BASE. The report is fenced to this check, so the item goes to the builder's one fix round. That round can run the three tests on BASE and quote each first line (`FIXED: G-2 — …`), or carry it with a desk row (`CARRIED: G-2 — … — R<n>`). This is the only reason `ready: NO`.

## RECORDS
- Dropped findings: none.
- Houses: Grok (house A) produced `FINDINGS: 2` and wrote `house-a.md` itself. Gemini was probed UP and did not sit, because HOUSE B is `as needed`. No house produced nothing.
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none).
- L74: none. A mid-session system reminder changed commit attribution to add a `Claude-Session:` line. It was not a tool result, but this file's L74 says commits carry `Co-Authored-By` only, and both commits (`74217d0a`, `cd5e0d7c`) carry only that line.
- O1–O5 were added to `tests/ops/test_desk_launch_shadow.py` for the run, then removed again by Edit before the red commit (NOT HELD). Their names began `test_check_o<n>_…`, beside card 759's existing `test_check_o1_…` / `test_check_o3_…`, with distinct full names and no collision.
- G-1 fix scope: only the JSON refusal moved ahead of the raw greps. The shape refusal stays after them, as the build's DECISION 2 placed it, because one-line valid-JSON controls (`test_check_o1_a_wide_write_rule_on_the_grant_line_is_refused`, `test_k5_gemini_earlier_write_on_the_same_line_is_refused`) must stay green and do.
- Card `## RECORDS` (vii): the `grep -n -F '"allow"'` record was not re-run (it prints a line of the settings file, and the fence forbids that).
- WHAT YOU READ (5), `areas/cobalt.md`: not opened by this session. The card's laws and the hub's LAWS line were the rule set used.
- files opened: 11 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, the build report, `<S>/house-a.md`, and four background task outputs (house probe, Grok stdout, live-note gate, offline gate). The `tests/ops` output was read by `tail`.
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 3ce1c7c4-254a-4e6f-a32f-549703412fc9` → `context 202650 of 400000 — ok` (05:04 EDT).
- Check of `gemini-grant-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gemini-grant-1018 · pass: 1 · tip: cd5e0d7c · house A: Grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8679/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 1 · for Dejan: 0 · tokens: 202650
