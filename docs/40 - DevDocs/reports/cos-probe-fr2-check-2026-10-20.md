# cos-probe-fr2 — check report (2026-10-20)

## §0 Headline
- CHECK DONE on `dfea631a` (build tip `74169800`). House A Grok returned `FINDINGS: 0`; house B was not needed.
- Three findings were mine, and all three held and are fixed in `probe.py`. O1: an auth-quote value with a trailing newline was quoted instead of `unread`. O2: a write over the planted `.mcp.json` was not counted as a written file. O3: `_x11`'s docstring still said "user-config".
- Deploy gate green: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS `com.cobalt.radar`.
- ready: YES · decisions: 0.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line in commits. Recorded as DATA (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md"` (13:41 EDT) → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 0 · b4c76fa2176d29b1ab69073d57d391fd2bde838a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | quoted below |
| range | `git log --stat --format=%h 27c35e37..74169800` | 0 | `74169800`: `docs/40 - DevDocs/cobalt/cos/README.md \| 3 +`, `src/cobalt/cos/probe.py \| 107 ++…--`, `2 files changed, 81 insertions(+), 29 deletions(-)` · `7b1427af`: `tests/cobalt/test_cos_probe.py \| 141 ++…-`, `1 file changed, 127 insertions(+), 14 deletions(-)` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, no header line; card `HOUSE B: as needed` | — | house A: Grok · house B: none (not needed) |

```
clock · date · 0 · Tue Oct 20 13:41:15 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-probe-fr2
head · git log --oneline -1; git log --stat --format=%h 74169800..HEAD · 0 · (6 lines)
    220eaa70 docs(cos-probe-fr2): build report — 74169800
    220eaa70
    
     .../reports/cos-probe-fr2-build-2026-10-20.md      | 193 +++++++++++++++++++++
     .../reports/cos-probe-fr2-build-2026-10-20.result  |  15 ++
     2 files changed, 208 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-probe-fr2/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-probe-fr2/docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md" · 0 · BUILT · job: cos-probe-fr2 · tip: 74169800 | on 27c35e37 | migration: none | offline 4895/0 | with-DB 5867/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 191388
range · git log --oneline 27c35e37..74169800 · 0 · (2 lines)
    74169800 fix(cos-probe-fr2): probe runs under the real HOME with a scratch cwd; cwd plant; auth quote (H1-H4, D0; L1, L28, L41)
    7b1427af wip(cos-probe-fr2): red — H1, H2, H3 tests, H4 control
PREFLIGHT OK
```

Path union (for `## Scope`): `docs/40 - DevDocs/cobalt/cos/README.md`, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, whole:
```
31 <S>/STAGED-CARD
20932 <S>/diff.md
17576 <S>/files/918-cos-probe-realhome-card.md
27510 <S>/files/cos-probe-fr2-build-2026-10-20.md
7679 <S>/files/wt/docs/40 - DevDocs/cobalt/cos/README.md
21300 <S>/files/wt/src/cobalt/cos/probe.py
24699 <S>/files/wt/tests/cobalt/test_cos_probe.py
386 <S>/rulings.md
STAGED 8 files · 120113 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr2-check`; commits 2 = PREFLIGHT's range count.) `## READ` files, each `stage-copy.sh`:
- `COPIED 14955 <S>/files/wt/src/cobalt/cos/session.py`
- `COPIED 8160 <S>/files/cos-gate-run-2026-10-20.md`
- `COPIED 23972 <S>/files/cos-probe-fr1-check-2026-10-20.md`
- `COPIED 4853 <S>/files/draft-cos-gate-rerun-2026-10-20.md`
- `COPIED 36631 <S>/files/F20-FINAL-2026-10-11.md`
- `COPIED 21804 <S>/files/877-cos-probe-card.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (19217 bytes, `ls -la <S>` 13:43). House A Grok started 13:43 (`grok -m grok-4.7 --sandbox cobalt-job …`, background, timeout 2700000); house B none (not needed). Back in `<WT>`: `git status --short --branch` → `## ops/cos-probe-fr2`.

## OWN FINDINGS
Written 13:5x, before either house list was opened.

FINDING O1
ROW: H3
CLAIM: `_AUTH_VALUE = re.compile(r"^[a-z0-9._-]+$")` with `.match` (`src/cobalt/cos/probe.py:78`, `:162`) accepts a value with a trailing newline (`$` matches before a final `\n`), so a value that is not a `[a-z0-9._-]` string is quoted instead of `unread`, and its newline reaches the stderr line and the FAIL clause.
RUN: TEST — `tests/cobalt/test_cos_probe.py`
```python
def test_auth_quote_a_value_with_a_trailing_newline_is_unread(rig, monkeypatch, capsys):
    rig.auth_code = 1
    rig.auth_stdout = json.dumps({"loggedIn": False, "authMethod": "none\n"})
    _code, out, err = _probe(monkeypatch, capsys, "X11")
    assert out.endswith("(loggedIn=false authMethod=unread)\n"), out
    assert "AUTH exit 1 · loggedIn=false authMethod=unread" in err, err
```
EXPECT: `AssertionError: PROBE X11 FAIL auth: … (loggedIn=false authMethod=none )`.

FINDING O2
ROW: H2 / X5
CLAIM: X2 / X10's written-file check subtracts every name present before the turn (`src/cobalt/cos/probe.py:362`, `:365`), so a session that WRITES the planted `.mcp.json` in its cwd is not a written file and the item can print OK: the check ignores more than the plant.
RUN: TEST — `tests/cobalt/test_cos_probe.py`
```python
def test_x2_a_write_over_the_plant_is_a_written_file(rig, monkeypatch, capsys):
    rig.script = lambda c: [_write(".mcp.json"), _init(), _result()]
    for item in ("X2", "X10"):
        code, out, _err = _probe(monkeypatch, capsys, item)
        assert code == 1 and "file written in cwd: .mcp.json" in out, (item, out)
```
EXPECT: `AssertionError: ('X2', 'PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)\n')`.

FINDING O3
ROW: H2
CLAIM: `_x11`'s docstring still calls the plant "a planted user-config server" (`src/cobalt/cos/probe.py:389`), while row H2 makes it a project-scope `work/.mcp.json` that is no longer his user config.
RUN: COMMAND — `grep -n -F "user-config" src/cobalt/cos/probe.py`
EXPECT: `389:    """X11 (FINAL `:84`): the init tool list with a planted user-config server."""`

CHECK ASKS, by reading (each settled by a run at `## 4` where a run exists): X1 — every write in `probe.py` is under `root` (`:214`, `:344-345`, `:360`); the docstring `(c)` (`:21-27`) and the README D0 section state the CLI's own state and the 67-session bound. X2 — `.claude.json` absent from `probe.py` (run at `## 4`); no `security`. X3 — the auth check is the first act inside the scrubbed env (`:499-503`), argv `AUTH_ARGV`, cwd `root / "work"`; quote = two keys (O1 the one gap). X4 — `ALLOWED_ENV` untouched (`session.py:54`); the env tests stand. X5 — the item bodies differ from BASE in paths and the `before` set only (O2 the gap). X6 — a post-deploy gate run, not this check's.

## Findings
House A Grok finished 13:56 (`date`); `<S>/house-a.md` (12 bytes) reads whole: `FINDINGS: 0`. Grok's stdout: the path only. House B: none (not needed). No house finding to keep.

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py::test_auth_quote_a_value_with_a_trailing_newline_is_unread` | `1 failed in 0.63s` · `AssertionError: PROBE X11 FAIL auth: claude auth status exit 1 under the real HOME (loggedIn=false authMethod=none )` | HELD |
| O2 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py::test_x2_a_write_over_the_plant_is_a_written_file` | `1 failed in 0.55s` · `AssertionError: ('X2', 'PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)\n')` | HELD |
| O3 | opus-own | `grep -n -F "user-config" src/cobalt/cos/probe.py` | ``389:    """X11 (FINAL `:84`): the init tool list with a planted user-config server."""`` | HELD |
Red commit: `3e406f66 wip(cos-probe-fr2): check red — O1, O2` (`1 file changed, 20 insertions(+)`). O3 is a COMMAND finding; its grep is its proof.

## FIXES
| id | fix | proof |
|---|---|---|
| O1 | `_auth_quote`: `_AUTH_VALUE.fullmatch` for `.match` | trio `74 passed in 4.74s` |
| O2 | `_live_scratch`: the before-set maps each cwd file to its bytes; an entry that is new or whose bytes changed counts as written | trio `74 passed in 4.74s` |
| O3 | `_x11` docstring: "a planted project-scope server" | `grep -n -F "user-config" src/cobalt/cos/probe.py` → nothing (exit 1) |
Trio = `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py`. DevDocs: `## 2026-10-20 — cos-probe-fr2 (check)` in `docs/40 - DevDocs/cobalt/cos/README.md`. Commit `dfea631a fix(cos-probe-fr2): auth quote value matched whole; a write over the plant is a written file; _x11 docstring (check O1, O2, O3)` (`2 files changed, 9 insertions(+), 4 deletions(-)`).

## Suites
RESTARTS · `uv run cobalt jobs restarts 27c35e37..HEAD` · exit 0 · whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
W on `dfea631a` · `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr2 all --deploy --deploy-gate` · exit 0 · verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2-all-20261020-135736.log
```
The offline figure 8970 includes `tests/ops` (the deploy gate). with-DB 5869 = the build's 5867 plus this check's two new offline-shaped tests, which pass 1 runs again. No skip marked `OUTSIDE`. `ls /Users/cobalt/cobalt-wt/cos-probe-fr2/.env` (14:44) → `No such file or directory`; `git status --short --branch` → `## ops/cos-probe-fr2`.

## Scope
PREFLIGHT's union `docs/40 - DevDocs/cobalt/cos/README.md`, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`, plus my commits on the same three paths: all within rows H1–H4 and D0. Nothing in the fence.

## Checked against the branch
- (i) `git log --oneline 74169800..HEAD -- . ":(exclude)docs"` → `dfea631a fix(cos-probe-fr2): …(check O1, O2, O3)` · `3e406f66 wip(cos-probe-fr2): check red — O1, O2`; `<tip now>` = `dfea631a`.
- (ii) `git log --stat --format=%h 74169800..HEAD` → `dfea631a`: `docs/40 - DevDocs/cobalt/cos/README.md`, `src/cobalt/cos/probe.py` · `3e406f66`: `tests/cobalt/test_cos_probe.py` · `220eaa70`: the build report and `.result` (docs). Every non-docs path is in rows H1–H4's `files`.
- (iii) `git log --oneline 27c35e37..HEAD -- src/cobalt/cos/session.py src/cobalt/cos/run.py src/cobalt/cos/listener.py src/cobalt/cos/tools.py src/cobalt/cos/cli.py src/cobalt/redact configs/cobalt/agents/cos.yaml configs/cobalt/taxonomy/tunables.yaml` → empty.
- (iv) `grep -n -F "def test_auth_quote_a_value_with_a_trailing_newline_is_unread" …` → `623:`; `grep -n -F "def test_x2_a_write_over_the_plant_is_a_written_file" …` → `631:`; `3e406f66` (red) sits below `dfea631a` (fix) in (i). O3 is a grep finding: `grep -n -F "user-config" src/cobalt/cos/probe.py` → nothing after the fix.
- (vi) `git log --stat --format=%h 27c35e37..HEAD -- src/cobalt/db_migrations tests/cobalt` → `3e406f66` and `7b1427af`, both `tests/cobalt/test_cos_probe.py` (offline); no migration, no with-DB file: no gate-list entry owed.
- (vii) card RECORDS greps, on main's tree now (nothing deployed yet, so these are the card's `before` values): `.claude.json` in `/Users/cobalt/cobalt/src/cobalt/cos/probe.py` → `2`; `under the scratch HOME` → `1`; the H1 test name in main's `test_cos_probe.py` → `0`. On this tip: `.claude.json` → `0`; `under the scratch HOME` → `0`.
- (viii) L32: this report holds constructed values only; no ticker, price, date, email or org id of his (the O1 test's value is the constructed `none\n`).

## OPEN
none (findings 3 · dropped 0 · held 3 · fixed 3 · held unfixed 0 · open 0). X6 (the live re-run of the six items after the deploy) is OUT OF SCOPE: `## NOT IN THIS JOB` gives it to the gate seat.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none

## RECORDS
- House A Grok: `FINDINGS: 0` (13:56). House B: none (not needed): the card says `HOUSE B: as needed`, and Gemini probed UP but did not sit.
- Dropped findings: none. No house produced nothing. No `REFUSED` line, no `CONTINUED`, no extra lock take (the gate's one take, `lock: waited 0 min`).
- L74: the session's attribution reminder asked for a `Claude-Session:` line. It was recorded once under `## L74` and not acted on.
- O2's fix keeps the X2 / X10 pass rule (no file written in the cwd) and narrows only what H2's before-set excused: the plant, unchanged, is still not a written file.
- I read `areas/cobalt.md` whole, so my read also took in `## Start here`, `## NOW` and `## Working rules`, which `## WHAT YOU READ` leaves out. Nothing from them was used.
- files opened: 12 — `CHECK-HUB.md`, the card, the build report, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`, `src/cobalt/cos/session.py` (`:50-129`), `areas/cobalt.md`, `BUILD-HUB.md` (`:1-40`, `:77-101`), `<S>/house-a.md`, and three task output files (the house probe, Grok's stdout, the gate).
- Check of `cos-probe-fr2`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-probe-fr2 · pass: 1 · tip: dfea631a · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 178055
