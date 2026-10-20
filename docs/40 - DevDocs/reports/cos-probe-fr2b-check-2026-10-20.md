# cos-probe-fr2b — check report (2026-10-20)

## §0 Headline
- The port at `9b912c83` is byte-equal to `dfea631a` over the three spec files; no code outside them moved (X1, X2).
- 8 findings of my own (Grok: `FINDINGS: 0`), each run: none held. The H4 reach over all seven items and the `FileNotFoundError` branch both run green.
- Deploy-gate pass on `9b912c83`: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`. RESTARTS: com.cobalt.radar.
- ready: YES · decisions: 0.

## L74
- The session's harness reminder (a system turn, 16:12) asked for a `Claude-Session:` line in commits. Recorded once as data (L74); acted on none. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 0 · f60d0993c3dad827d6de90944835b1fe647d49a9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
HOUSE GATES:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → exit 0, one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` → STANDING `Bash(grok *)` … `| APPLIED: \`LAWS.md\` L62 at 07:3x; …|`).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → exit 0, one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` → STANDING: the four house strings … `| APPLIED: \`LAWS.md\` L62 at 07:4x; …|`).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, whole:
```
clock · date · 0 · Tue Oct 20 16:12:40 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-probe-fr2b
head · git log --oneline -1; git log --stat --format=%h 9b912c83..HEAD · 0 · (6 lines)
    cdac46c5 docs(cos-probe-fr2b): build report — 9b912c83
    cdac46c5
    
     .../reports/cos-probe-fr2b-build-2026-10-20.md     | 210 +++++++++++++++++++++
     .../reports/cos-probe-fr2b-build-2026-10-20.result |  15 ++
     2 files changed, 225 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-probe-fr2b/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-probe-fr2b/docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md" · 0 · BUILT · job: cos-probe-fr2b · tip: 9b912c83 | on 656f2ca1 | migration: none | offline 4897/0 | with-DB 5869/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 166019
range · git log --oneline 656f2ca1..9b912c83 · 0 · (2 lines)
    9b912c83 fix(cos-probe-fr2b): port probe.py and the cos README byte-equal to dfea631a (P2, D0; L3, L72)
    2208f9bf wip(cos-probe-fr2b): red — test_cos_probe.py ported byte-equal to dfea631a (P1)
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Tue Oct 20 16:12:33 EDT 2026` |
| THE RANGE | `git log --stat --format=%h 656f2ca1..9b912c83` | 0 | `9b912c83` · `docs/40 - DevDocs/cobalt/cos/README.md | 6 ++` · `src/cobalt/cos/probe.py | 111 ++++++++++++++++++++++++---------` · `2 files changed, 87 insertions(+), 30 deletions(-)` · `2208f9bf` · `tests/cobalt/test_cos_probe.py | 161 +++++++++++++++++++++++++++++++++++++----` · `1 file changed, 147 insertions(+), 14 deletions(-)` |
| path union | (from THE RANGE) | — | `docs/40 - DevDocs/cobalt/cos/README.md`, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py` |
| DB | card header | — | no `DB: none` key: the gate runs `all` |
| `<S>` | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check` | 1 | `No such file or directory` (fresh) |
| HOUSE PROBES | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) | 0 | `grok: UP` · `gemini: UP` |
| SEATS | SEAT ORDER, no `HOUSE A:` header line | — | `house A: Grok · house B: none (not needed)` (`HOUSE B: as needed`) |
| self-check | build report last line | — | `self-check: 3 of 3` |

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, whole:
```
27 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/STAGED-CARD
22739 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/diff.md
11755 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/files/923-cos-probe-fr2b-card.md
26070 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/files/cos-probe-fr2b-build-2026-10-20.md
7999 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/files/wt/docs/40 - DevDocs/cobalt/cos/README.md
21496 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/files/wt/src/cobalt/cos/probe.py
25598 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/files/wt/tests/cobalt/test_cos_probe.py
386 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/rulings.md
STAGED 8 files · 116070 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count (2). The `## READ` reports, each `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <source> <S>/files/<name>`:
- `918-cos-probe-realhome-card.md` → `COPIED 17576 …/files/918-cos-probe-realhome-card.md`
- `cos-probe-fr2-check-2026-10-20.md` → `COPIED 18776 …/files/cos-probe-fr2-check-2026-10-20.md`
- `deploy-cos-probe-fr2.md` → `COPIED 29613 …/files/deploy-cos-probe-fr2.md`
The spec `git diff 27c35e37..dfea631a` is a command, not a file: not staged; `diff.md` (the port) stands in for it, the port being byte-equal (X1).
`<S>/HOUSE-INSTRUCTIONS.md` written (13281 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
HOUSE START: `date` 16:14:30; gates R17, R19 re-grepped (one row each); `ls -la <S>` (diff.md, files/, HOUSE-INSTRUCTIONS.md, rulings.md, STAGED-CARD); `cd <AGY>`; Grok started (background, timeout 2700000); `cd <WT>`; `git status --short --branch` → `## ops/cos-probe-fr2b`. House B: none (not needed).

## OWN FINDINGS
Written by 16:16 (`date` 16:16:16), before `<S>/house-a.md` was opened. Read: the card, card 918, the diff `656f2ca1..9b912c83` (three files), `probe.py:140-219` and `:420-523` at the tip, `test_cos_probe.py:1-200` at the tip, the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down).

FINDING O1
ROW: E1 / X1 (b)
CLAIM: the port differs from `dfea631a` in one of the three spec files (`src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`, `docs/40 - DevDocs/cobalt/cos/README.md`).
RUN: COMMAND `git diff dfea631a 9b912c83 -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"`
EXPECT: any diff line.

FINDING O2
ROW: E1 / X1 (c)
CLAIM: code outside the spec moved between `dfea631a` and the tip.
RUN: COMMAND `git diff --stat dfea631a 9b912c83 -- src tests configs ops`
EXPECT: any stat line.

FINDING O3
ROW: E1 / X1 (a)
CLAIM: the tip's stat over the three paths from `27c35e37` is not the card's table (README `6`, `probe.py` `111`, `test_cos_probe.py` `161`; 234 insertions, 44 deletions).
RUN: COMMAND `git diff --stat 27c35e37 9b912c83 -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"`
EXPECT: a count other than 6 / 111 / 161, or a summary other than `3 files changed, 234 insertions(+), 44 deletions(-)`.

FINDING O4
ROW: X2 (SCOPE)
CLAIM: the branch touches a path other than the three spec files, the build report and its `.result`.
RUN: COMMAND `git log --stat --format=%h 656f2ca1..HEAD`
EXPECT: a fifth path.

FINDING O5
ROW: X4
CLAIM: `probe.py` still names `.claude.json`.
RUN: COMMAND `grep -c -F ".claude.json" src/cobalt/cos/probe.py`
EXPECT: a count above `0`.

FINDING O6
ROW: D0 / DEPLOY PROOF 4
CLAIM: the README heading marker does not read the card's `after` `2` (the cause of card 918's rollback).
RUN: COMMAND `grep -c -F "## 2026-10-20 — cos-probe-fr2" "docs/40 - DevDocs/cobalt/cos/README.md"`
EXPECT: a count other than `2`.

FINDING O7
ROW: X3 / X4 (the H4 control's reach)
CLAIM: the H4 control `test_cos_probe.py` `test_the_probe_opens_no_file_under_the_real_home` runs only X2, X11, X12; X10, X3, X14 and X17 (`probe.py:480-482`) are never run under the open recorder, so one of them may open or write a file under the real HOME unpinned.
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_check_o7_no_item_opens_or_writes_under_the_real_home(rig, monkeypatch, capsys, tmp_path):
    import builtins
    import io

    real = tmp_path / "real-home"
    (real / ".claude").mkdir(parents=True)
    state = {real / ".claude.json": b'{"constructed": true}', real / ".claude" / "settings.json": b"{}"}
    for path, data in state.items():
        path.write_bytes(data)
    monkeypatch.setenv("HOME", str(real))
    opened: list[str] = []

    def recording(inner):
        def call(file, *args, **kwargs):
            if isinstance(file, (str, bytes, os.PathLike)):
                opened.append(os.fsdecode(os.fspath(file)))
            return inner(file, *args, **kwargs)
        return call

    monkeypatch.setattr(builtins, "open", recording(builtins.open))
    monkeypatch.setattr(io, "open", recording(io.open))
    monkeypatch.setattr(os, "open", recording(os.open))
    for item in ITEMS:
        _probe(monkeypatch, capsys, item)
    root = str(real.resolve())
    under = [p for p in opened if os.path.abspath(p).startswith(root) or p.startswith(str(real))]
    assert under == [], under
    assert opened, "the recorder saw no open at all"
    assert sorted(str(p.relative_to(real)) for p in real.rglob("*")) == [
        ".claude", ".claude.json", ".claude/settings.json"]
    for path, data in state.items():
        assert path.read_bytes() == data, path
```
EXPECT: `assert under == []` fails naming a path under `real-home`, or the rglob list holds a new entry.

FINDING O8
ROW: P2 / build `## DECISIONS` 1
CLAIM: the `FileNotFoundError` branch of `_auth_exit` (`src/cobalt/cos/probe.py:176-177`) does not give the FAIL line `exit 127 under the real HOME (loggedIn=unread authMethod=unread)` with nothing spawned; no test reaches it.
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_check_o8_no_claude_on_path_is_exit_127_and_nothing_spawns(rig, monkeypatch, capsys):
    wrapped = subprocess.run

    def no_claude(argv, *args, **kwargs):
        if list(argv)[:1] == ["claude"]:
            raise FileNotFoundError("constructed: no claude on PATH")
        return wrapped(argv, *args, **kwargs)

    monkeypatch.setattr(subprocess, "run", no_claude)
    code, out, err = _probe(monkeypatch, capsys, "X11")
    assert code == 1
    assert out == ("PROBE X11 FAIL auth: claude auth status exit 127 under the real HOME "
                   "(loggedIn=unread authMethod=unread)\n"), out
    assert "AUTH exit 127 · loggedIn=unread authMethod=unread" in err, err
    assert rig.fakes == [], "the factory is never called"
```
EXPECT: one of the asserts fails (another line, another exit, or a spawn).

## Findings
House A Grok: completion notice 16:24 (`date` 16:24:16); `ls -la <S>` → `house-a.md` 12 bytes. Its stdout: `I'll read the house instructions first and follow them exactly.The port matches the spec's rows, the quoted runs, and the check asks. I am writing that result./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2b-check/house-a.md`. `house-a.md` whole: `FINDINGS: 0`. No `FINDING` block: nothing kept. House B: none (not needed).

## Dropped
none (house A wrote no block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `git diff dfea631a 9b912c83 --` the three paths | nothing | NOT HELD |
| O2 | opus | `git diff --stat dfea631a 9b912c83 -- src tests configs ops` | nothing | NOT HELD |
| O3 | opus | `git diff --stat 27c35e37 9b912c83 --` the three paths | `README.md | 6 ++` · `probe.py | 111 +++++++++++++++++------` · `test_cos_probe.py | 161 ++++++++++++++++++++++++++++++---` · `3 files changed, 234 insertions(+), 44 deletions(-)`; the same command on `27c35e37 dfea631a` → the same four lines, line for line | NOT HELD |
| O4 | opus | `git log --stat --format=%h 656f2ca1..HEAD` | `cdac46c5` (build report `.md` 210, `.result` 15) · `9b912c83` (README 6, probe.py 111) · `2208f9bf` (test_cos_probe.py 161): five paths, the three spec files and the build report pair | NOT HELD |
| O5 | opus | `grep -c -F ".claude.json" src/cobalt/cos/probe.py` | `0` | NOT HELD |
| O6 | opus | `grep -c -F "## 2026-10-20 — cos-probe-fr2" "docs/40 - DevDocs/cobalt/cos/README.md"` | `2` (= the card's `after`) | NOT HELD |
| O7 | opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py::test_check_o7_no_item_opens_or_writes_under_the_real_home` | `1 passed in 0.64s` | NOT HELD (removed with Edit) |
| O8 | opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py::test_check_o8_no_claude_on_path_is_exit_127_and_nothing_spawns` | `1 passed in 0.51s` | NOT HELD (removed with Edit) |
After the two removals: `git status --short --branch` → `## ops/cos-probe-fr2b`; `git diff --stat dfea631a -- tests/cobalt/test_cos_probe.py` → nothing. No test form was repaired. Nothing held: no `wip(cos-probe-fr2b): check red` commit.
Card offline suite: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` → `74 passed in 4.75s`.
CHECK ASKS: X1 — O1, O2, O3 (equal, empty, empty). X2 — O1 (byte-equal: an empty `git diff` between the two commits over each path), O4 (no other file). X3 — `probe.py` writes at `:214` (`root / "work"` mkdir), `:344`, `:345`, `:360`, all under the `cos-probe-` root; O7 runs all seven items under a recorder: nothing opened or made under the real HOME; the CLI's state and the 67-session bound are stated at `probe.py:22-28` and in the README's `cos-probe-fr2` section. X4 — O5 `0`; `grep -n -F "security" src/cobalt/cos/probe.py` → no line (exit 1); the H4 control's mutation was red at build (M6, `:529`), not re-run here. X5 — no finding re-decides R2177 option A or card 918's check.
Build `## DECISIONS` 1 (the untested `FileNotFoundError` branch): run as O8, green — the branch gives `exit 127 … (loggedIn=unread authMethod=unread)` and spawns nothing. Not carried.

## FIXES
none (nothing held).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 656f2ca1..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No UNCLASSIFIED row; matches the card header.
W on `9b912c83` (no commit of mine): `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr2b all --deploy --deploy-gate` (background) → exit 0, whole:
```
tests/ops: run (deploy gate)
offline 8970/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5869/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2b-all-20261020-162528.log
```
Log reads (`grep -n -F`): `OUTSIDE` → nothing; `:956` `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 721.00s (0:12:00)` and `:1030` `4073 passed, 1 xfailed, 16 warnings in 884.27s (0:14:44)` (tests/ops) → offline 8970; `:1273` `5625 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 882.05s (0:14:42)` + `:2255` `244 passed, 1 deselected, 5 warnings in 236.61s (0:03:56)` → with-DB 5869; `:2456` `148 passed, 1 skipped, 15 warnings in 26.43s` (the skip is the `COBALT_TEST_LIVE_DRC` one, not `COBALT_LIVE_VAULT_ROOT`); `:1047` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `:2329` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (= F0).
- offline 8970/0 · with-DB 5869/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0`.
- `.env: removed`; `ls /Users/cobalt/cobalt-wt/cos-probe-fr2b/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cos-probe-fr2b`.
- RESTARTS: com.cobalt.radar.

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/cobalt/cos/README.md` (D0), `src/cobalt/cos/probe.py` (P2), `tests/cobalt/test_cos_probe.py` (P1); plus the build report and `.result` (card-allowed). The check made no commit: nothing of its own in scope.

## Checked against the branch
- (i) `git log --oneline 9b912c83..HEAD -- . ":(exclude)docs"` → nothing: no commit of mine; `<tip now>` = `9b912c83`.
- (ii) `git log --stat --format=%h 9b912c83..HEAD` → `cdac46c5` only, `cos-probe-fr2b-build-2026-10-20.md` (210) and `.result` (15): docs only. No `WIDENED`.
- (iii) the fence: `git log --oneline 656f2ca1..HEAD -- src/cobalt/cos/session.py src/cobalt/cos/run.py src/cobalt/cos/listener.py src/cobalt/cos/tools.py src/cobalt/cos/cli.py src/cobalt/redact configs/cobalt/agents/cos.yaml configs/cobalt/taxonomy/tunables.yaml` → EMPTY.
- (iv) no HELD finding: nothing to grep.
- (vi) `git log --stat --format=%h 656f2ca1..HEAD -- src/cobalt/db_migrations tests/cobalt` → `2208f9bf` `tests/cobalt/test_cos_probe.py` only: no migration, no with-DB test file (an offline test file). No gate-lists change owed.
- (vii) card `## RECORDS`: `ls ".../reports/cos-probe-fr2-build-2026-10-20.md"` → `No such file or directory` (as recorded); `ls ".../reports/cos-probe-fr2-check-2026-10-20.md"` → listed (as recorded); `ls /Users/cobalt/cobalt-wt/` → `cos-probe-fr2b` now listed (made by the desk at launch, after the drafter's read; not a defect). The record's `git merge-base` and `git grep` commands are not on this check's list: not typed.
- (viii) L32: no real value of his in this report; the test values quoted are constructed.

## OPEN
none. COUNTING: findings 8 (opus-own 8 · house A 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none

## RECORDS
- Started 16:12:33 EDT (`date`); W done, close 17:12 (`date` 17:12:46).
- L74: the harness reminder of 16:12 asked for a `Claude-Session:` line in commits; recorded once under `## L74`, not followed. This check made no commit.
- House A Grok produced `FINDINGS: 0` (no block). House B not seated (card `HOUSE B: as needed`; Gemini was UP and not launched).
- Dropped findings: none. Houses that produced nothing: none. `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (the gate took and released its own).
- Tests O7 and O8 were written into `tests/cobalt/test_cos_probe.py`, ran green, and were removed with Edit; the file is byte-equal to `dfea631a` again (`git diff --stat dfea631a -- tests/cobalt/test_cos_probe.py` → nothing).
- Build `## DECISIONS` 1 settled by O8's run (green): the `FileNotFoundError` branch behaves as the row states.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 04698d1d` → `context 165122 of 400000 — ok`.
- files opened: 12 — `CHECK-HUB.md`; card 923; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report; card 918; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `src/cobalt/cos/probe.py`; `tests/cobalt/test_cos_probe.py`; `<S>/house-a.md`; and three task outputs (the house probe, Grok's stdout, the gate's verdict). Also tailed: the old check report's last lines and its `.result` (for the stop-line field forms).
- Check of `cos-probe-fr2b`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-probe-fr2b · pass: 1 · tip: 9b912c83 · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165122
