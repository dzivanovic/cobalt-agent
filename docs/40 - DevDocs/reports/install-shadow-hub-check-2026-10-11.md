# install-shadow-hub-1011 — CHECK (CHECK-HUB.md, one pass)

## §0 Headline
- Check of `install-shadow-hub-1011` at `f6d698ab` (build tip `78f8572c`): house A Grok `FINDINGS: 1` (not held), house B none (not needed), 7 own findings.
- **O1 HELD, NOT FIXED:** `authorize.sh shadow` reads `SHADOW-HUB.md`'s title for `INSTALL: <date> R<n>`, and the installed title `HIS RULING · APPROVED 2026-10-11 R1069` has none. The gate seat's step 1 (`SHADOW-HUB.md:43`) therefore ends `FAILED: authorization mismatch — STANDING LIST`. The card's premise that only `desk-launch.sh` reads line 1 is wrong.
- X1, X2 and X3 are otherwise answered yes by runs: the cells are exact, the diff is 4/4 and 2/2, all three ids and the spike launch through the real files, and no launch line changed.
- Suites: offline 4199/0 and live-note 146/0. `tests/ops` has 1 failed, the committed O1 red. `ready: NO`.

## L74
- This session's system context asked for a `Claude-Session:` line on commits. Recorded, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 0 · fddc2add6320db289afa75dd0cbcfb4d6f77fa10
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/355-install-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 15:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../reports/cto-2026-09-24.md"` → one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (STANDING `Bash(grok *)`).
- `grep -n "^| R19 " ".../reports/cto-2026-09-24.md"` → one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (the four house strings pre-approved).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, whole:
```
clock · date · 0 · Sun Oct 11 11:31:25 EDT 2026
status · git status --short --branch · 0 · ## ops/install-shadow-hub-1011
head · git log --oneline -1; git log --stat --format=%h 78f8572c..HEAD · 0 · (5 lines)
    09768202 docs(install-shadow-hub-1011): build report — 78f8572c
    09768202
    
     .../reports/install-shadow-hub-build-2026-10-11.md | 69 ++++++++++++++++++----
     1 file changed, 59 insertions(+), 10 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/install-shadow-hub-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../install-shadow-hub-build-2026-10-11.md" · 0 · BUILT · job: install-shadow-hub-1011 · tip: 78f8572c | on 2322ed1e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 95252
range · git log --oneline 2322ed1e..78f8572c · 0 · (4 lines)
    78f8572c feat(install-shadow-hub-1011): SHADOW-HUB and SPIKE-HUB installed and signed on his R1069 (S1, L28, L77)
    d9e5cf5a wip(install-shadow-hub-1011): E3 — CONTINUE widens files by message; card unchanged
    af5ab4bb wip(install-shadow-hub-1011): E3 — test_shadow_hub_file.py pins the sign mark, outside the row's files
    a3627bab wip(install-shadow-hub-1011): red
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 2322ed1e..78f8572c` → `78f8572c` tests/ops/test_shadow_hub_file.py (4+, 2-) · `d9e5cf5a` the build report · `af5ab4bb` SHADOW-HUB.md (8), SPIKE-HUB.md (4), the build report · `a3627bab` tests/ops/test_desk_launch_shadow.py (11), tests/ops/test_spike_hub_file.py (6). Commit count 4.
- DB: none, `git diff --name-only --no-renames 2322ed1e..78f8572c` → whole: `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/prompts/SPIKE-HUB.md`, `docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, `tests/ops/test_spike_hub_file.py`. Every path under `docs/` or `tests/ops/`. Path union recorded for `## Scope`.
- `ls <S>` → `No such file or directory` (fresh).
- House probe, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → `grok: UP` · `gemini: UP` (exit 0). No `HOUSE A: OpenAI` header line: Sol not probed.
- Seats: **house A: Grok · house B: none (not needed)** — the card's line is `HOUSE B: as needed`.
- Self-check of the build: 3 of 3.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → whole:
```
3154 <S>/diff.md
9645 <S>/files/355-install-shadow-hub-card.md
24903 <S>/files/install-shadow-hub-build-2026-10-11.md
15920 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
4053 <S>/files/wt/docs/40 - DevDocs/prompts/SPIKE-HUB.md
16130 <S>/files/wt/docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md
13261 <S>/files/wt/tests/ops/test_desk_launch_shadow.py
9846 <S>/files/wt/tests/ops/test_shadow_hub_file.py
4065 <S>/files/wt/tests/ops/test_spike_hub_file.py
370 <S>/rulings.md
STAGED 10 files · 101347 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/install-shadow-hub-1011-check`.) `commits 2` against PREFLIGHT's 4: the diff excludes `docs`, and `git log --oneline 2322ed1e..78f8572c -- . ":(exclude)docs"` → `78f8572c`, `a3627bab` (2); `grep -c "^commit " <S>/diff.md` → `2`. The other two commits (`af5ab4bb`, `d9e5cf5a`) touch only `docs/`. ASK DESK 1 under `## DECISIONS`.
`stage-copy.sh`, each → `COPIED`:
- `COPIED 91778 <S>/files/wt/ops/desk/desk-launch.sh`
- `COPIED 3429 <S>/files/wt/ops/desk/install-fixed.sh`
- `COPIED 9304 <S>/files/wt/tests/ops/test_desk_launch_spike.py`
- `COPIED 14412 <S>/files/306-ops-hand-install-card.md`
- `COPIED 21858 <S>/files/cto-2026-10-11.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (11848 bytes, `ls -la <S>`): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
House A Grok started 11:33 ET (`date` 11:33:26), house gates re-run first (R17 row `:35`, R19 row `:37`, R19 commit `5055151d…`); cwd back in `<WT>`, `git status --short --branch` → `## ops/install-shadow-hub-1011`. House B: none (not needed).

## OWN FINDINGS
Written 11:35 ET, before either house list was opened.

FINDING O1
ROW: S1 (and X3)
CLAIM: The gate seat's own AUTHORIZATION (`SHADOW-HUB.md:43`, `sh …/authorize.sh shadow "<card>"`) fails on the new title: `ops/desk/authorize.sh:177-191` reads line 1 of the fixed file for `INSTALL: <date> R<n>` and, finding none in `HIS RULING · APPROVED 2026-10-11 R1069` (`SHADOW-HUB.md:1`), writes the row `STANDING LIST … the title names no INSTALL: <date> R<n>` and ends `FAILED: authorization mismatch — STANDING LIST`. The row's premise (card S1: "`desk-launch.sh` reads line 1 only for the token (`:892`), so any title without `«INSTALL` passes") misses this second reader.
RUN: TEST — `tests/ops/test_authorize.py`:
```python
def test_check_o1_the_real_shadow_title_names_its_standing_row(desk):
    """Check of card 355, O1: authorize.sh shadow reads SHADOW-HUB.md's title for INSTALL: <date> R<n>."""
    repo, card, env = desk
    real = (REPO / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md").read_text().split("\n", 1)[0]
    (repo / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md").write_text(real + "\n\nbody\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "the real title")
    done = authorize(env, "shadow", card)
    assert "the title names no INSTALL: <date> R<n>" not in done.stdout, done.stdout
```
EXPECT: red on the tip: `AssertionError` with the `STANDING LIST · sed -n 1p … · 1 · the title names no INSTALL: <date> R<n>: # SHADOW-HUB — …` row in stdout.

FINDING O2
ROW: X2
CLAIM: The tree's own `SHADOW-HUB.md`, unmodified (`:1`, `:19-21`), is refused by `desk-launch.sh shadow` for at least one of the three ids; the shipped `test_the_real_file_launches_a_signed_grok` (`tests/ops/test_desk_launch_shadow.py:276-292`) rewrites the title and never runs `claude-sonnet-5-5`.
RUN: TEST — `tests/ops/test_desk_launch_shadow.py`:
```python
def test_check_o2_the_real_file_verbatim_launches_each_builder(desk):
    """Check of card 355, O2 (X2): the tree's own SHADOW-HUB.md, as committed, for all three ids."""
    desk.set_hub(REAL.read_text())
    for slug, model in (("grok", "grok-4.7"), ("sonnet", "claude-sonnet-5-5"), ("terra", "gpt-5.6-terra")):
        done = desk.run(str(desk.card_for(slug)), "--model", model)
        assert done.returncode == 0, (model, done.stderr)
        line = done.stdout.splitlines()[-1]
        assert f'"{ALLOW[model]}" --disallowedTools ' in line
        assert f"MODEL: {model}" in line
```
EXPECT: if true, `AssertionError: ('<id>', 'REFUSED: …')`.

FINDING O3
ROW: X2
CLAIM: The tree's own `SPIKE-HUB.md` (`:1`, `:22`, `:24`) is refused by `desk-launch.sh spike` (`ops/desk/desk-launch.sh:390-414`); no test runs the real file through the launcher (`tests/ops/test_desk_launch_spike.py` builds its hub from `line_for`).
RUN: TEST — `tests/ops/test_desk_launch_spike.py`:
```python
def test_check_o3_the_real_spike_hub_launches(desk):
    """Check of card 355, O3 (X2): the tree's own SPIKE-HUB.md, its Read path pointed at the tmp file."""
    real = (REPO / "docs" / "40 - DevDocs" / "prompts" / "SPIKE-HUB.md").read_text()
    hub = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SPIKE-HUB.md"
    assert real.count(hub) == 1
    desk.fixed.write_text(real.replace(hub, str(desk.fixed)))
    desk.commit("the real file")
    done = desk.run("spike", str(desk.prompt))
    assert done.returncode == 0, done.stderr
    assert f"PROMPT: '{desk.prompt}'" in done.stdout.splitlines()[-1]
```
EXPECT: if true, `AssertionError: REFUSED: …`.

FINDING O4
ROW: X1
CLAIM: A `## BUILDERS` sign cell of `SHADOW-HUB.md:19-21` is not exactly `2026-10-11 R1069 · HIS RULING · APPROVED` (Terra's with its network note); the shipped `test_s1_every_sign_cell_holds_his_row` (`tests/ops/test_shadow_hub_file.py:148-151`) asserts `in`, not equality.
RUN: TEST — `tests/ops/test_shadow_hub_file.py`:
```python
@pytest.mark.parametrize("model", IDS)
def test_check_o4_each_sign_cell_is_exactly_his_row(model):
    """Check of card 355, O4 (X1)."""
    want = "2026-10-11 R1069 · HIS RULING · APPROVED"
    if model == "gpt-5.6-terra":
        want += " · network: off (workspace-write default; X1 proves it)"
    assert builders(text())[model][4] == want
```
EXPECT: if true, `AssertionError: assert '<cell>' == '<want>'` for an id.

FINDING O5
ROW: X1
CLAIM: The diff of the two real files is more than line 1 and the sign lines.
RUN: COMMAND — `git diff --numstat 2322ed1e..78f8572c -- "docs/40 - DevDocs/prompts"`
EXPECT: if true, a count other than `4 4` for `SHADOW-HUB.md` or `2 2` for `SPIKE-HUB.md`.

FINDING O6
ROW: X2
CLAIM: A `claude --bg` launch line of either file changed in the range (a new `<`, `>`, `\`, `$`, backtick, `;`, `&` or `|` would need one).
RUN: COMMAND — `git diff -G "^claude --bg" --stat 2322ed1e..78f8572c -- "docs/40 - DevDocs/prompts"`
EXPECT: if true, a file listed; empty output if no launch line changed.

FINDING O7
ROW: X3
CLAIM: Another script under `ops/` reads `SHADOW-HUB.md`'s title or sign text beside `desk-launch.sh` and `authorize.sh` (O1).
RUN: COMMAND — `grep -rn -F "SHADOW-HUB" ops`
EXPECT: if true, a hit beyond `ops/desk/authorize.sh`, `ops/desk/desk-launch.sh`, `ops/desk/bare-guard.py` (reads `## BUILDERS` command cells only, `:1107-1149`), `ops/desk/stop-guard.py` and `ops/desk/preflight.sh` comments.

## Findings
House A Grok finished 11:53 ET (`date` 11:53:30; task exit 0, stdout ends with the path). `ls -la <S>` → `house-a.md` 926 bytes, written by Grok. Its last line `FINDINGS: 1`. House B: none (not needed).
THE DROP: `FINDING 1` has a `RUN: COMMAND` line followed by one `grep` line → kept.
- G1 · Grok · SCOPE · the build report on the tip still stops at E3 (`(pending)` sections, `FAILED: E3` last line), so the suite lines it quotes are not there · COMMAND

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `tests/ops/test_authorize.py::test_check_o1_the_real_shadow_title_names_its_standing_row`, alone | `1 failed, 15 warnings in 0.99s`; first failing line `tests/ops/test_authorize.py:317: AssertionError`, stdout holds `STANDING LIST · sed -n 1p "…/SHADOW-HUB.md" · 1 · the title names no INSTALL: <date> R<n>: # SHADOW-HUB — … HIS RULING · APPROVED 2026-10-11 R1069` and ends `FAILED: authorization mismatch — STANDING LIST` | **HELD** — red for its stated reason: `authorize.sh shadow` (the gate seat's AUTHORIZATION, `SHADOW-HUB.md:43`) fails on the installed title |
| O2 | own | `tests/ops/test_desk_launch_shadow.py::test_check_o2_the_real_file_verbatim_launches_each_builder`, alone | first run `1 failed`: `subprocess.CalledProcessError … 'commit', '-q', '-m', 'card x-job-grok'` (the fixture already commits the grok card; "nothing to commit") — form repaired once (the grok card taken as `desk.card`, the assertion unchanged); rerun `1 passed, 15 warnings in 1.23s` | NOT HELD — the unmodified real file launches all three ids (X2 answered: yes); test removed again |
| O3 | own | `tests/ops/test_desk_launch_spike.py::test_check_o3_the_real_spike_hub_launches`, alone | `1 passed, 15 warnings in 0.89s` | NOT HELD — the real `SPIKE-HUB.md` passes `desk-launch.sh spike` (X2 answered: yes); test removed again |
| O4 | own | `tests/ops/test_shadow_hub_file.py::test_check_o4_each_sign_cell_is_exactly_his_row`, alone | `3 passed, 15 warnings in 0.79s` | NOT HELD — each cell is exactly the ruling text, Terra's with its note (X1 answered: yes); test removed again |
| O5 | own | `git diff --numstat 2322ed1e..78f8572c -- "docs/40 - DevDocs/prompts"` | `4	4	docs/40 - DevDocs/prompts/SHADOW-HUB.md` · `2	2	docs/40 - DevDocs/prompts/SPIKE-HUB.md` | NOT HELD (X1: 4/4, 2/2) |
| O6 | own | `git diff -G "^claude --bg" --stat 2322ed1e..78f8572c -- "docs/40 - DevDocs/prompts"` | empty | NOT HELD — no launch line changed (X2) |
| O7 | own | `grep -rn -F "SHADOW-HUB" ops` | 9 hits: `desk-launch.sh:41`, `:330`, `:888`; `stop-guard.py:76`; `preflight.sh:4`; `bare-guard.py:16`, `:95`; `authorize.sh:3`, `:51` | NOT HELD beyond O1 — no reader other than `desk-launch.sh` (token, sign cell) and `authorize.sh` (title, O1) reads the title or the sign text (X3) |
| G1 | Grok | `grep -n -e "^FAILED:" -e "^(pending)$" "docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md"` (in `<WT>`, HEAD `09768202`) | empty (exit 1) | NOT HELD — Grok read the report as staged from `TIP` `78f8572c` (a wip copy); the final report is the docs commit `09768202` above `TIP`, ending `BUILT · … self-check: 3 of 3` |
Removed tests: `git status --short --branch` after removal → `## ops/install-shadow-hub-1011` · ` M tests/ops/test_authorize.py` (O1 only). Red commit: `f6d698ab wip(install-shadow-hub-1011): check red — O1`.

## FIXES
none. O1 is **HELD, NOT FIXED — `docs/40 - DevDocs/prompts/SHADOW-HUB.md:1`**: the file is a row's file, but the row gives line 1's text word for word (`HIS RULING · APPROVED 2026-10-11 R1069`) and turns down the `INSTALL: <date> R<n> of his approval of STANDING-LIST.md` form on purpose ("a text about another file"). A fix that adds `INSTALL: <date> R<n>` changes the row's text and names R1069 as the STANDING LIST row: a desk decision, `## DECISIONS` 2.

## Suites
DB: none card. W as `BUILD-HUB.md` gives it, (a0), (a), (e), plus `tests/ops`, on tip `f6d698ab`:
- RESTARTS: `uv run cobalt jobs restarts 2322ed1e..HEAD` → 7 rows: SHADOW-HUB.md, SPIKE-HUB.md and the build report `DOCS -`; the 4 `tests/ops` files `test/documentation; no resident -`. Last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 2322ed1e` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/prompts/SPIKE-HUB.md`, `docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md`, `tests/ops/test_authorize.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`, `tests/ops/test_spike_hub_file.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 offline` → exit 0, verdict `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-offline-20261011-115446.log` (`:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 641.99s (0:10:41)`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1, `1 failed, 3126 passed, 1 xfailed, 15 warnings in 587.55s (0:09:47)`. The one failure is `test_check_o1_the_real_shadow_title_names_its_standing_row`, O1's held red (its `STANDING LIST … the title names no INSTALL: <date> R<n>` line is at output `:63`). It is red by design until O1 is fixed (`## DECISIONS` 2).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh install-shadow-hub-1011 livenote` → exit 0, verdict `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/install-shadow-hub-1011-livenote-20261011-120541.log`.
- With-DB: not run (DB: none). `.env`: never present; `ls …/install-shadow-hub-1011/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union (6 paths: two hubs, the build report, three `tests/ops` files) plus my commit `f6d698ab`, which touches `tests/ops/test_authorize.py`, a test file holding the held finding's test. The rows' `files` are the two hubs and the three test files. The build report is docs, and `test_authorize.py` is a check test. Nothing is inside the fence.

## Checked against the branch
- (i) `git log --oneline 78f8572c..HEAD -- . ":(exclude)docs"` → `f6d698ab wip(install-shadow-hub-1011): check red — O1`. `<tip now>` = `f6d698ab`.
- (ii) `git log --stat --format=%h 78f8572c..HEAD` → `f6d698ab` tests/ops/test_authorize.py (11+) · `09768202` the build report. No other path.
- (iii) `git log --oneline 2322ed1e..HEAD -- ops/desk/desk-launch.sh ops/desk/bare-guard.py ops/desk/authorize.sh ops/desk/install-fixed.sh` → empty.
- (iv) `grep -n -F "def test_check_o1_the_real_shadow_title_names_its_standing_row" tests/ops/test_authorize.py` → `309:def test_check_o1_the_real_shadow_title_names_its_standing_row(desk):`. Its red commit `f6d698ab` has no `fix(…)` above it: O1 is held unfixed.
- (v) `ls …/.env` → "No such file or directory"; `git status --short --branch` → `## ops/install-shadow-hub-1011` alone (12:06).
- (vi) `git log --stat --format=%h 2322ed1e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty, so there are no gate lists to carry.
- (vii) Card records:
  - `git -C /Users/cobalt/cobalt log -1 --format=%h -- "docs/40 - DevDocs/reports/cto-2026-10-11.md"` → `98642e25`. That is no longer `2322ed1e`: the desk report moved after drafting. R1069 still stands at HEAD (authorize.sh row `:15`; `rulings.md` at staging `:16`), and its commit by `-S` is `2322ed1e…`.
  - `grep -n -o "«SIGN"` on the tip's `SHADOW-HUB.md` → empty (the record's three hits were BASE).
- (viii) L32: no ticker, price or value of his in this report. The dates and row numbers are desk ruling ids from the card.

## OPEN
- O1: HELD, NOT FIXED — `docs/40 - DevDocs/prompts/SHADOW-HUB.md:1`. To settle it, the card's S1 must say what line 1 carries for `authorize.sh`, then the builder's fix round runs. `test_check_o1_…` goes green when the title holds `INSTALL: <date> R<n>` followed by a non-digit and naming an approved row (`authorize.sh:180-190`). `test_s4_kind_shadow_reads_shadow_hub_and_the_build_rows` (`tests/ops/test_authorize.py:293`) shows the expected title shape.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK [11:32 ET]: `stage-set.sh` printed `commits 2` against PREFLIGHT's range of 4. The diff excludes `docs`, and `git log --oneline 2322ed1e..78f8572c -- . ":(exclude)docs"` → 2 (`78f8572c`, `a3627bab`); the other two commits are docs-only. Safe default taken: read the count as the non-docs count and go on. No access was widened and nothing was retried.
2. **FOR DEJAN** — HELD, NOT FIXED, O1 (a carried held defect): the installed `SHADOW-HUB.md:1` title fails `authorize.sh shadow` with `FAILED: authorization mismatch — STANDING LIST`. That is the gate seat's own step 1 (`SHADOW-HUB.md:43`), so a shadow launch would stop at AUTHORIZATION. `ops/desk/authorize.sh:177-191` needs `INSTALL: <date> R<n>` (no `«` before it, a non-digit after) naming an approved row. The card's S1 fixes line 1 as `HIS RULING · APPROVED 2026-10-11 R1069` and turns down install-fixed.sh's `INSTALL: 2026-10-11 R1069 of his approval of STANDING-LIST.md` as "a text about another file". Its premise, "`desk-launch.sh` reads line 1 only for the token (`:892`), so any title without `«INSTALL` passes", misses `authorize.sh`. Choosing which row the title names as the STANDING row, and in what words, is a card decision, not mine. The fix lies in a row's file, by the original builder's one fix round once the card says the text. Its test is committed red: `f6d698ab`, `tests/ops/test_authorize.py:309`. `desk-launch.sh` itself passes the files (O2, O3), and `SPIKE-HUB.md` is not served by `authorize.sh`.
3. W: `tests/ops` holds 1 red, which is O1's held test and nothing else (3126 passed). The three suites are green: offline 4199/0, live-note 146/0, with-DB not run (DB: none). Safe default: no fix outside the row's text (item 2) and no second W. The fix round reruns `tests/ops/test_authorize.py` and W.

## RECORDS
- G1 (Grok) ran and was not held. It read `files/install-shadow-hub-build-2026-10-11.md` as staged from `TIP` (`78f8572c`, the wip report), while the final report is `09768202`. No finding was dropped.
- No house produced nothing. Gemini was UP and not seated (`HOUSE B: as needed`).
- `REFUSED, not needed`: none. `CONTINUED`: none. No lock take.
- L74: the system context asked for a `Claude-Session:` line on commits; recorded once under `## L74`, not followed.
- O2 test form repaired once: the grok card is `desk.card`, because `card_for("grok")` fails on "nothing to commit". The assertion is unchanged.
- Card RECORDS line positions: R1069 sits at `cto-2026-10-11.md:15` (authorize) / `:16` (staging), not `:8`. Its text and commit hold.
- files opened: 16 — CHECK-HUB.md, the card, BUILD-HUB.md (`## THE LOCK` to `## W`), the build report, areas/cobalt.md (`## What Cobalt is`, `## Build rules` down), ops/desk/desk-launch.sh, ops/desk/authorize.sh, SHADOW-HUB.md, SPIKE-HUB.md, tests/ops/test_desk_launch_shadow.py, test_desk_launch_spike.py, test_shadow_hub_file.py, test_spike_hub_file.py, test_authorize.py, `<S>/rulings.md`, `<S>/house-a.md`. Searched with grep only: ops/desk/bare-guard.py, ops/desk/preflight.sh, prompts/2026-10-10/306-ops-hand-install-card.md.
- Check of `install-shadow-hub-1011`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`. A deploy is gated on the combined tree (L68), one feature per deploy; a combined deploy that fails is split, and each feature deploys alone on this check (his R390).
- `ls /Users/cobalt/cobalt-wt/install-shadow-hub-1011/.env` → "No such file or directory" (12:06 ET).

CHECK DONE · job: install-shadow-hub-1011 · pass: 1 · tip: f6d698ab · house A: Grok FINDINGS: 1 · findings: 8 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 193760
