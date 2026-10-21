# x15-hitl-probe — CHECK 2026-10-21

## §0 Headline
CHECK DONE, ready: YES, tip `c1b4b785`. House A Grok (3 findings) plus 3 of my own; 2 held (Grok A1, A2: the X15 tests pinned the readout by a bare string the script also holds and did not pin the script after the nodes it writes), both fixed in `tests/cobalt/test_hitl_x15.py` and shown red under the real mutations. No `src/` change.
Gate on `c1b4b785` with `--deploy --deploy-gate`: offline 9046/0 · with-DB 5892/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
2 decisions, none for Dejan: the commit count of the staged diff (ASK DESK 1), and the derived `com.cobalt.cos` restart against the card's fence (DECISION 2, out of scope).

## L74
One system message asked for a `Claude-Session:` commit line; not followed (`## RECORDS`).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/977-x15-hitl-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/977-x15-hitl-probe-card.md" · 0 · 8695a0819899196cd642b30a6a995e3e97fa59af
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/977-x15-hitl-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
THE HOUSE GATES (first read):
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (STANDING: `Bash(grok *)` pre-approved)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (STANDING: the four house strings pre-approved)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty)

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output WHOLE:
```
clock · date · 0 · Wed Oct 21 13:41:34 EDT 2026
status · git status --short --branch · 0 · ## ops/x15-hitl-probe
head · git log --oneline -1; git log --stat --format=%h ca39b027..HEAD · 0 · (6 lines)
    4e573d1a docs(x15-hitl-probe): build report — ca39b027
    4e573d1a
    
     .../reports/x15-hitl-probe-build-2026-10-21.md     | 100 +++++++++++++++++++--
     .../reports/x15-hitl-probe-build-2026-10-21.result |  15 ++++
     2 files changed, 109 insertions(+), 6 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/x15-hitl-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/x15-hitl-probe/docs/40 - DevDocs/reports/x15-hitl-probe-build-2026-10-21.md" · 0 · BUILT · job: x15-hitl-probe · tip: ca39b027 | on 41804777 | migration: none | offline 4918/0 | with-DB 5890/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 215902
range · git log --oneline 41804777..ca39b027 · 0 · (4 lines)
    ca39b027 fix(x15-hitl-probe): /hitl/x15-probe joins BASE_ROUTES' /hitl block (P1, K5, L72)
    26642074 wip(x15-hitl-probe): W — offline red outside the rows' files (ASK DESK W)
    3a5080a1 feat(x15-hitl-probe): /hitl/x15-probe, shared key script with k readout, dev hitl x15-send (S1 P1 P2 P3 D0, L1 L28 L32 L37)
    a7040a4a wip(x15-hitl-probe): red
PREFLIGHT OK
```
THE RANGE, typed: `git log --stat --format=%h 41804777..ca39b027` · exit 0:
```
ca39b027
 tests/cobalt/test_s3_c3_panel_offline.py | 2 +-
26642074
 .../reports/x15-hitl-probe-build-2026-10-21.md     | 180 +++++++++++++++++++++
3a5080a1
 docs/40 - DevDocs/cobalt/aset/web.md    |  3 +++
 docs/40 - DevDocs/cobalt/cli.md         |  3 +++
 docs/40 - DevDocs/cobalt/hitl/README.md |  3 +++
 src/cobalt/aset/web.py                  | 37 +++++++++++++++++++++++++++++----
 src/cobalt/hitl/cli.py                  | 34 +++++++++++++++++++++++++++++-
 tests/cobalt/test_hitl_x15.py           |  1 +
a7040a4a
 tests/cobalt/test_hitl_x15.py | 240 ++++++++++++++++++++++++++++++++++++++++++
```
Path union: `src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, `docs/40 - DevDocs/cobalt/aset/web.md`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/hitl/README.md`, `docs/40 - DevDocs/reports/x15-hitl-probe-build-2026-10-21.md`.
DB: the card carries no "DB: none" line → the DB-none row is not run.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
THE HOUSE PROBES: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) · exit 0 · lines WHOLE:
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line → OpenAI not probed. **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.
Self-check of the build: `3 of 3`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output WHOLE:
```
27 .../x15-hitl-probe-check/STAGED-CARD
16442 .../x15-hitl-probe-check/diff.md
16948 .../x15-hitl-probe-check/files/977-x15-hitl-probe-card.md
33239 .../x15-hitl-probe-check/files/wt/docs/40 - DevDocs/cobalt/aset/web.md
8797 .../x15-hitl-probe-check/files/wt/docs/40 - DevDocs/cobalt/cli.md
4614 .../x15-hitl-probe-check/files/wt/docs/40 - DevDocs/cobalt/hitl/README.md
23223 .../x15-hitl-probe-check/files/wt/docs/40 - DevDocs/reports/x15-hitl-probe-build-2026-10-21.md
115485 .../x15-hitl-probe-check/files/wt/src/cobalt/aset/web.py
2013 .../x15-hitl-probe-check/files/wt/src/cobalt/hitl/cli.py
8339 .../x15-hitl-probe-check/files/wt/tests/cobalt/test_hitl_x15.py
38049 .../x15-hitl-probe-check/files/wt/tests/cobalt/test_s3_c3_panel_offline.py
36130 .../x15-hitl-probe-check/files/x15-hitl-probe-build-2026-10-21.md
386 .../x15-hitl-probe-check/rulings.md
STAGED 13 files · 303692 bytes · commits 3
```
(`...` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920`.) `commits 3` against PREFLIGHT's range of 4: the diff is `-- . ":(exclude)docs"` and the fourth commit `26642074` touches only `docs/40 - DevDocs/reports/x15-hitl-probe-build-2026-10-21.md` (THE RANGE above) → see `## DECISIONS` ASK DESK 1.
`stage-copy.sh` (each exit 0), the files `## READ` names that the script cannot derive, plus the fixture module row P2 names:
```
COPIED 36631 <S>/files/wt/docs/30 - Design/F20-FINAL-2026-10-11.md
COPIED 2645 <S>/files/wt/src/cobalt/hitl/card.py
COPIED 6740 <S>/files/wt/src/cobalt/notify/mattermost.py
COPIED 3825 <S>/files/wt/src/cobalt/env.py
COPIED 4045 <S>/files/wt/tests/cobalt/test_hitl_web.py
COPIED 8424 <S>/files/wt/tests/cobalt/test_hitl_offline.py
COPIED 5685 <S>/files/wt/tests/cobalt/hitl_support.py
```
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph).

## OWN FINDINGS
Read: the card, the diff `41804777..ca39b027` (`git diff 41804777 ca39b027 -- src tests/cobalt/test_s3_c3_panel_offline.py`), `tests/cobalt/test_hitl_x15.py`, `src/cobalt/aset/web.py:1380-1579`, `src/cobalt/env.py:1-95`, `src/cobalt/notify/mattermost.py` whole, `src/cobalt/cli.py:528-618`, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK`, `## DECISIONS`, `## RECORDS` and last line. Greps: `location.hash` over `src` → one line, `web.py:1444`; `hitl-k` over `src` → `web.py:1440,1445,1446,1453,1502,1505`; the three D0 headings → `cli.md:153`, `hitl/README.md:38`, `aset/web.md:409`.

FINDING O1
ROW: R1 / SCOPE (X6)
CLAIM: The derived restart set of this branch names `com.cobalt.cos` (`src/cobalt/aset/web.py` sits in its static import reach), while the card header reads `com.cobalt.aset com.cobalt.radar` and `## NOT IN THIS JOB` fences "kickstarting `com.cobalt.cos`" — a deploy that restarts what the tool derives would kickstart the resident X15 gates.
RUN: COMMAND `uv run cobalt jobs restarts 41804777..HEAD`
EXPECT: the row `src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` and the last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.

FINDING O2
ROW: P3 (X4)
CLAIM: P3 (e)'s second branch, `X15 NOT SENT <result.detail>` exit 1 (`src/cobalt/hitl/cli.py:46-48`), is pinned by no test: every P3 test returns `SendResult(True, …)` (`tests/cobalt/test_hitl_x15.py:180`).
RUN: TEST `tests/cobalt/test_hitl_x15.py`
```python
def test_x15_send_not_sent_prints_one_line_exit_1(monkeypatch, capsys):
    from cobalt.notify.result import SendResult

    sent: list[str] = []

    def _send(message, **_k):
        sent.append(message)
        return SendResult(False, "channel disabled in configs/cobalt/notify.yaml")

    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", _send)
    monkeypatch.setattr("cobalt.hitl.store.HitlStore", _raise)
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr("cobalt.hitl.card.page_base_url", lambda: "https://sheet.example.invalid")
    with pytest.raises(SystemExit) as exc:
        _cli(monkeypatch, "hitl", "x15-send")
    assert exc.value.code == 1
    assert len(sent) == 1
    out = capsys.readouterr()
    assert out.out == "X15 NOT SENT channel disabled in configs/cobalt/notify.yaml\n"
    assert re.search(r"[0-9a-f]{32}", out.out + out.err) is None, "the key is never printed"
```
EXPECT: if the branch is wrong, `assert exc.value.code == 1` or the `out.out ==` line fails; built as the card says, it passes (a pin, not a defect).

FINDING O3
ROW: P3 (X4)
CLAIM: When `send_dm` raises (`mattermost.py:72-77`, `COBALT_MASTER_KEY` unset — the case the build's own `## RECORDS` P3d line met under `COBALT_ENV=dev`), the CLI's generic handler (`src/cobalt/cli.py:611-613`) prints the exception, and no test pins that the key stays out of that output.
RUN: TEST `tests/cobalt/test_hitl_x15.py`
```python
def test_x15_send_raise_prints_no_key(monkeypatch, capsys):
    from cobalt.notify.mattermost import MattermostError

    seen: list[str] = []

    def _send(message, **_k):
        seen.append(message)
        raise MattermostError("HTTP 400 on /posts: constructed body")

    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", _send)
    monkeypatch.setattr("cobalt.hitl.store.HitlStore", _raise)
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr("cobalt.hitl.card.page_base_url", lambda: "https://sheet.example.invalid")
    with pytest.raises(SystemExit) as exc:
        _cli(monkeypatch, "hitl", "x15-send")
    assert exc.value.code == 1
    assert len(seen) == 1
    out = capsys.readouterr()
    assert re.search(r"[0-9a-f]{32}", out.out + out.err) is None, "the key is never printed"
    assert "X15 SENT" not in out.out
```
EXPECT: if the key leaks on the raise path, the `re.search` assertion fails; otherwise it passes (a pin).

## Findings
House A Grok finished 13:57 (`date` 13:57:49; notice exit 0; `ls -la <S>` → `house-a.md` 2690 bytes, 13:57). House B: none (not needed). `<S>/house-a.md` written by Grok; its stdout was only the path. Its last line: `FINDINGS: 3`. Each block carries a `RUN:` line followed by a test function or a `uv run pytest` line → none dropped.
- A1 · Grok · P1 · the probe test pins the readout by bare `hitl-k-state` / `k: missing`, both also inside `_hitl_key_script()`, so dropping `_hitl_k_readout()` stays green · TEST
- A2 · Grok · S1 · nothing pins the key script after the nodes it writes, on the probe or the real page; swapping them leaves every X15 test green · TEST
- A3 · Grok · S1 / suite line · the report's S1 green line quotes `5 passed, 13 deselected`; the file collects 14, so 9 are deselected · COMMAND

## Dropped
none

## RUNS
- O1 · own · `uv run cobalt jobs restarts 41804777..HEAD` · exit 0 · `src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` · `src/cobalt/hitl/cli.py	M	static import reach	com.cobalt.radar` · last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` · REJECTED — `## NOT IN THIS JOB`: "Loading, bootstrapping or kickstarting `com.cobalt.cos`" (the output is shown as stated; what the deploy restarts is the deploy's; the build carries the same item as its DECISION R1) → OUT OF SCOPE, `## DECISIONS` 2.
- O2 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py::test_x15_send_not_sent_prints_one_line_exit_1` · `1 passed in 0.44s` · NOT HELD (removed again with the Edit tool).
- O3 · own · `… tests/cobalt/test_hitl_x15.py::test_x15_send_raise_prints_no_key` · `1 passed in 0.40s` · NOT HELD (removed again with the Edit tool).
- A1 · Grok · `… tests/cobalt/test_hitl_x15.py::test_probe_readout_pin_is_the_script_text` · `1 failed in 0.41s` — `tests/cobalt/test_hitl_x15.py:297: AssertionError` / `E       assert 'class="hitl-k-state"' in 'def test_probe_route_touches_no_store(no_store):…` · HELD (the probe test's readout pin is the bare string the script also holds).
- A2 · Grok · `… tests/cobalt/test_hitl_x15.py::test_script_after_the_nodes_is_unpinned` · `1 failed in 0.06s` — `tests/cobalt/test_hitl_x15.py:303: AssertionError` / `E       assert ('index(' in 'def test_probe_route_touches_no_store(no_store):…` · HELD (no test pins the script after the nodes it writes).
- A3 · Grok · `uv run pytest -q -p no:cacheprovider --color=no --collect-only tests/cobalt/test_hitl_x15.py -k "readout_logic or one_source"` · `5/14 tests collected (9 deselected) in 0.02s` · NOT HELD — the same `-k` over `tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py` prints `5/18 tests collected (13 deselected) in 0.03s`: the report's `5 passed, 13 deselected` is that two-file run (its row names `test_hitl_web.py` beside it); the quoted line omits its file arguments, it does not misstate a count.
Red commit: `9dfc91d9 wip(x15-hitl-probe): check red — A1 A2` (test file only).

## FIXES
- A1, A2 (one fix, `tests/cobalt/test_hitl_x15.py`, a row's file): `test_probe_route_touches_no_store` now asserts `body.count('class="hitl-k-state">k: missing<') == 1` and `body.index('class="hitl-k-state"') < body.index("<script>")`; `test_real_page_shows_the_readout_above_approve` asserts the readout and the last `class="hitl-k"` field sit before `<script>`. No `src/` change.
  - The held tests and the files beside them: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_s3_c3_panel_offline.py` → `80 passed, 9 skipped in 2.44s`.
  - The behaviour the findings name, shown red under the strengthened tests (Edit tool, each undone): (m1) `_hitl_k_readout()` dropped from `hitl_x15_probe` → `-k "touches_no_store"` `1 failed, 15 deselected` — `test_hitl_x15.py:129: assert 0 == 1`; (m2) the probe's script placed before the readout → `1 failed` — `test_hitl_x15.py:130: assert 4339 < 4093`; (m3) `hitl_detail`'s script moved to the head of `forms` → `-k "real_page"` `1 failed` — `test_hitl_x15.py:162: assert 5229 < 4648`. After the undo `git diff --stat -- src` → nothing.
  - DevDocs: one dated line in `docs/40 - DevDocs/cobalt/aset/web.md` under `## 2026-10-21 — x15-hitl-probe`.
  - Commit `c1b4b785 fix(x15-hitl-probe): X15 tests pin the readout element and the script after it (check A1 A2)`.

## Suites
RESTARTS (BUILD-HUB `## RESTARTS`) before the gate: `uv run cobalt jobs restarts 41804777..HEAD` · exit 0 · the table as in `## RUNS` O1 plus no new row (my commits touch a test file and a docs page); no `UNCLASSIFIED` row; last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
THE GATE on `c1b4b785`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh x15-hitl-probe all --deploy --deploy-gate` (background) · exit 0 · verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9046/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5892/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/x15-hitl-probe-all-20261021-135955.log
```
From the log (`grep -n -F`): `:956` `4920 passed, 878 skipped, 4 xfailed` (tests/cobalt + tests/taxonomy) and `:1031` `4126 passed, 1 xfailed` (tests/ops, deploy gate) → `offline 9046/0`; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1048`); pass 1 `:1274` `5648 passed, 9 skipped, 138 deselected, 7 xfailed`; pass 2 `:2256` `244 passed, 1 deselected` → `with-DB 5892/0`; `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2330`) = F0; live-note `:2457` `148 passed, 1 skipped`. `OUTSIDE the allowed set` → no line. The pass-1 SKIPPED lines naming `COBALT_LIVE_VAULT_ROOT` belong to pass 1; the live-note pass ran with the root set.
- offline 9046/0 · with-DB 5892/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0`.
- `.env: removed`; `ls /Users/cobalt/cobalt-wt/x15-hitl-probe/.env` → `No such file or directory`; `git status --short --branch` → `## ops/x15-hitl-probe` (14:49).
- Every held finding's test passes (A1, A2 in the `80 passed` run and in the gate); each was shown red first (`## RUNS`).

## Scope
PREFLIGHT's path union (`src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, the three D0 pages, the build report) plus my commits (`tests/cobalt/test_hitl_x15.py`, `docs/40 - DevDocs/cobalt/aset/web.md`): every path is in a row's `files` (S1/P1/P2/P3, P1 for the guard test, D0) or is the build report. No fenced path touched ((iii) below).

## Checked against the branch
- (i) `git log --oneline ca39b027..HEAD -- . ":(exclude)docs"` → `c1b4b785 fix(x15-hitl-probe): X15 tests pin the readout element and the script after it (check A1 A2)` · `9dfc91d9 wip(x15-hitl-probe): check red — A1 A2`. `<tip now>` = `c1b4b785`.
- (ii) `git log --stat --format=%h ca39b027..HEAD` → `c1b4b785`: `docs/40 - DevDocs/cobalt/aset/web.md`, `tests/cobalt/test_hitl_x15.py`; `9dfc91d9`: `tests/cobalt/test_hitl_x15.py`; `4e573d1a`: the build report and its `.result`. Non-docs paths: `tests/cobalt/test_hitl_x15.py` only (a test file, a row's file). No WIDENED.
- (iii) `git log --oneline 41804777..HEAD -- src/cobalt/hitl/card.py src/cobalt/hitl/store.py src/cobalt/hitl/actions.py src/cobalt/hitl/executor.py` → empty. `git log --oneline 41804777..HEAD -- src/cobalt/notify src/cobalt/redact configs/cobalt/redact.yaml configs/cobalt/taxonomy/tunables.yaml configs/cobalt/notify.yaml src/cobalt/db_migrations` → empty. The function fences (`hitl_approve`, `hitl_deny`, `_hitl_key_sha`, `_hitl_refusal`, `hitl_list`): the `src/` diff (`## OWN FINDINGS` read) has hunks at `@@ -1433,6 +1433,26 @@` (the two helpers), `@@ -1448,6 +1468,17 @@` (the probe), `@@ -1465,6 +1496,7 @@` and `@@ -1473,10 +1505,7 @@` (inside `hitl_detail`) — none in a fenced function (X3).
- (iv) A1 `grep -n -F "def test_probe_readout_pin_is_the_script_text" tests/cobalt/test_hitl_x15.py` → `254:def test_probe_readout_pin_is_the_script_text():`; A2 `grep -n -F "def test_script_after_the_nodes_is_unpinned" tests/cobalt/test_hitl_x15.py` → `263:def test_script_after_the_nodes_is_unpinned():`. `9dfc91d9` (check red) sits below `c1b4b785` (fix) in (i).
- (vi) `git log --stat --format=%h 41804777..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_hitl_x15.py` and `tests/cobalt/test_s3_c3_panel_offline.py`, both offline; no migration, no with-DB test above `0013` → gate lists not owed.
- (vii) Card records: `ls /opt/homebrew/bin/node` → `/opt/homebrew/bin/node`. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` is not a listed prefix → not typed; BASE `41804777` is the range PREFLIGHT's `preflight.sh` read. `ls /Users/cobalt/cobalt-wt/` (drafter's "fresh") is a pre-build fact, overtaken by the build. `git -C /Users/cobalt/cobalt log --oneline -1` → `829e806a docs(desk): X15 977 built, check launched, R2293-R2294`.
- (v) `ls /Users/cobalt/cobalt-wt/x15-hitl-probe/.env` → `No such file or directory`; `git status --short --branch` → `## ops/x15-hitl-probe` alone.
- (viii) L32: this report quotes constructed test values only (the constructed key pattern, `sheet.example.invalid`, `@constructed`); no ticker, price or date of his.

## OPEN
none open. OUT OF SCOPE: O1 (the derived `com.cobalt.cos` restart; `## NOT IN THIS JOB` fences kickstarting `com.cobalt.cos`) — settled by the deploy's reading of `## DECISIONS` 2, not by this branch.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
- ASK DESK 1: `stage-set.sh` printed `commits 3`; PREFLIGHT's range holds 4. The excluded commit `26642074` is docs-only (the build report), and the house diff excludes `docs` by its own spelling. Is `<k>` the count of the docs-excluded diff? [13:43] Safe default taken: proceed with the staged set (no access widened); the build report at `files/x15-hitl-probe-build-2026-10-21.md` carries that commit's content.
- DECISION 2 (O1, OUT OF SCOPE; the build's DECISION R1 again, now shown by my run): `uv run cobalt jobs restarts 41804777..HEAD` ends `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`web.py` is in `com.cobalt.cos`'s static import reach); the card header reads `com.cobalt.aset com.cobalt.radar` and the fence names kickstarting `com.cobalt.cos` as not in this job, while X15 gates that resident. Which restart set the deploy of this branch runs, and whether `com.cobalt.cos` is restarted (or is not loaded at all yet), is the deploy's to decide. Safe default taken: nothing changed; the tool's line is the record; no `jobs.yaml` edit.

## RECORDS
- Session context (a system message, not a tool result) asked for a `Claude-Session:` line on commits. Recorded once, not followed: my commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).
- Dropped findings: none. Houses that produced nothing: none. House B: none (card `HOUSE B: as needed`; Gemini UP but not seated).
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (the one take was inside `gate.sh`).
- One extra listed run, mine: `uv run pytest … --collect-only tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py -k "readout_logic or one_source"` to settle A3 (`## RUNS`).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh fe0c09af` → `context 179514 of 400000 — ok`.
- files opened: 14 (Read tool) — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`:35-96`); the house-probe output; `tests/cobalt/test_hitl_x15.py`; `src/cobalt/env.py`; `src/cobalt/notify/mattermost.py`; `src/cobalt/aset/web.py` (`:1380-1579`); `src/cobalt/cli.py` (`:528-618`); the build report (`:75-122`, `:123-202`, `:235-269`); Grok's stdout; `<S>/house-a.md`; the gate output; `docs/40 - DevDocs/cobalt/aset/web.md` (`:405-411`). Read by grep only: `src/cobalt/redact/guard.py`, `configs/cobalt/redact.yaml`, `src/cobalt/notify/result.py`, `cto-2026-09-24.md` (R17, R19), the gate log. Not opened: `areas/cobalt.md` (the card and this file carry the rules the check acted on).
- Check of `x15-hitl-probe`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: x15-hitl-probe · pass: 1 · tip: c1b4b785 · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9046/0 · with-DB 5892/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 179514
