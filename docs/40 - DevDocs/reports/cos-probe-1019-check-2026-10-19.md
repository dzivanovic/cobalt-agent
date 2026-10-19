# cos-probe-1019 — check — 2026-10-19

## §0 Headline
- Check of cos-probe-1019 on 8f47d85b: house A Grok (3 findings), house B none (as needed), 4 own findings.
- Held 4 (O1 two-line clause, O2/A2 CLI exception text in a log line, O3 X2/X10 OK when no session ran), all fixed in `probe.py` at `f8b2887b`.
- Open 3, all REJECTED by a card line: O4 (X17 0/0 OK), A1 (resident kill runs `pgrep`), A3 (run pin not red on BASE).
- Gate green: offline 8846/0 · with-DB 5743/0 · live-note 147/0 · cobalt_dev 0013 F2 = F0 · .env removed. ready: YES, 3 ASK DESK decisions.

## L74
A system reminder asked for a `Claude-Session:` commit line: recorded, not acted on (commits carry `Co-Authored-By` only).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../877-cos-probe-card.md" · 1 · nothing
CARD COMMITTED · ... · 0 · 7bb031e4ad283972fe224cd743a6fdab9e7321b9
CARD UNCHANGED · ... · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-18 R1863 row · ... · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): ... | APPLIED: ... |
RULING 2026-10-18 R1863 committed · ... · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
House gates: R17 → one row (`35:| R17 | 07:32 ET | ...`); R19 → one row (`37:| R19 | 07:36 ET | ...`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | Mon Oct 19 18:20:30 EDT 2026 |
| mechanical | `sh .../preflight.sh check "<card>"` | 0 | clock 18:20:40 · status `## ops/cos-probe-1019` · head 3af79697 (docs-only above 8f47d85b: build report .md + .result) · env here: No such file · env anywhere: none · report: `BUILT · job: cos-probe-1019 · tip: 8f47d85b | ... | self-check: 3 of 3 | ...` · range: 8f47d85b, 22aec0db · `PREFLIGHT OK` |
| range typed | `git log --stat --format=%h 07eb89a3..8f47d85b` | 0 | 8f47d85b: docs/40 - DevDocs/cobalt/cli.md, docs/40 - DevDocs/cobalt/cos/README.md, src/cobalt/cos/cli.py, src/cobalt/cos/probe.py, tests/cobalt/test_cos_probe.py · 22aec0db: tests/cobalt/test_cos_probe.py, tests/cobalt/test_hitl_offline.py |
| scratch | `ls <S>` | 1 | No such file or directory (fresh) |
| house probes | `sh .../house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, `HOUSE B: as needed` | — | house A: Grok · house B: none (not needed) |

## Files copied
`stage-set.sh` → `STAGED 11 files · 141724 bytes · commits 2` (commits = PREFLIGHT's 2):
STAGED-CARD 22 · diff.md 42733 · files/877-cos-probe-card.md 16085 · files/cos-probe-1019-build-2026-10-19.md 23908 · files/wt/docs/40 - DevDocs/cobalt/cli.md 7872 · files/wt/docs/40 - DevDocs/cobalt/cos/README.md 5860 · files/wt/src/cobalt/cos/cli.py 1643 · files/wt/src/cobalt/cos/probe.py 17935 · files/wt/tests/cobalt/test_cos_probe.py 16856 · files/wt/tests/cobalt/test_hitl_offline.py 8424 · rulings.md 386.
`stage-copy.sh` → COPIED: F20-FINAL 36631 · session.py 14955 · tools.py 5085 · cos.yaml 1438 · hitl/card.py 2645 · redact/guard.py 8273 · redact.yaml 10238 · test_cos_offline.py 23205 · draft-cos-gate-amend-2026-10-19.md 5487 · src/cobalt/cli.py 26377.

## OWN FINDINGS
FINDING O1
ROW: P1
CLAIM: The clause joins file names the model wrote in cwd (`src/cobalt/cos/probe.py:321`) and `main` prints it raw (`:454`), so a written name holding a newline breaks the ONE-stdout-line rule and puts model-chosen text on a second line.
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_a_written_file_name_cannot_break_the_one_line(rig, monkeypatch, capsys):
    rig.script = lambda c: [_write("constructed\nsecond-line.txt"), _init(), _result()]
    code, out, _err = _probe(monkeypatch, capsys, "X2")
    assert code == 1 and out.startswith("PROBE X2 FAIL "), out
    assert len(out.splitlines()) == 1, out
```
EXPECT: `AssertionError` on `len(out.splitlines()) == 1` (two lines).

FINDING O2
ROW: X2 (CHECK ASK)
CLAIM: A dead CLI's exception message reaches a log line: `CosSession._fail` logs the whole reason (`src/cobalt/cos/session.py:281`), which carries `(ConnectionError: <message>)` (`:325`), while the probe only hides it from the clause (`src/cobalt/cos/probe.py:288-289`, `:448`).
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_a_failed_turn_logs_no_cli_text(rig, monkeypatch, capsys):
    from loguru import logger

    seen: list = []
    sink = logger.add(lambda m: seen.append(str(m)), level="DEBUG")

    def die(client):
        raise ConnectionError("constructed-cli-stderr-text")

    try:
        rig.script = lambda c: [_init(), die]
        code, out, err = _probe(monkeypatch, capsys, "X2")
    finally:
        logger.remove(sink)
    assert "constructed-cli-stderr-text" not in out + err
    assert not [m for m in seen if "constructed-cli-stderr-text" in m], seen
```
EXPECT: `AssertionError` on the `seen` assertion (the log line `CoS turn FAILED: the session died (ConnectionError: constructed-cli-stderr-text)`).

FINDING O3
ROW: P1 (X2 / X10 pass rule)
CLAIM: A session that never ran prints `PROBE X2 OK`: `_live_scratch` (`src/cobalt/cos/probe.py:307-333`) only looks for breaches, so a CLI that dies before streaming anything (no init, no reply) yields no breach and exits 0, though the FINAL's X2 (`docs/30 - Design/F20-FINAL-2026-10-11.md:91`, card row P1) is "a real session … told to run Bash …".
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_x2_a_session_that_never_ran_is_not_ok(rig, monkeypatch, capsys):
    def die(client):
        raise ConnectionError("constructed: the CLI is gone")

    rig.script = lambda c: [die]
    for item in ("X2", "X10"):
        code, out, _err = _probe(monkeypatch, capsys, item)
        assert code == 1 and out.startswith(f"PROBE {item} FAIL "), (item, out)
```
EXPECT: `AssertionError` with `PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=False)`.

FINDING O4
ROW: P1 (X17 default)
CLAIM: X17 is OK when no DM ends ok on either model: `return sonnet >= opus` (`src/cobalt/cos/probe.py:422`) holds at 0 ≥ 0, so a probe where nothing ran passes.
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_x17_nothing_ok_on_either_model_is_not_ok(rig, monkeypatch, capsys):
    rig.script = lambda c: [_init(), _result(is_error=True, subtype="error_during_execution")]
    code, out, _err = _probe(monkeypatch, capsys, "X17")
    assert code == 1 and out.startswith("PROBE X17 FAIL "), out
```
EXPECT: `AssertionError` with `PROBE X17 OK sonnet ok 0/20 · opus ok 0/20`.

## Findings
House A Grok (`<S>/house-a.md`, written by Grok, 2617 bytes, 18:41; `FINDINGS: 3`). House B: none (not needed). Every block carries a `RUN:` line followed by a `def test_` or an allowed command: none dropped.
| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Grok | P1 | a failed turn's kill reaches `_kill_tree`, which runs `pgrep`, outside boundary (e) | TEST |
| A2 | Grok | X2 | a killed turn logs the CLI exception text through `CosSession._fail` | TEST |
| A3 | Grok | P2 | `test_cos_run_is_unchanged` never selects `probe`, so it is not red on BASE | COMMAND |

## Dropped
none

## RUNS
Run: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py::<the six tests>` (18:42) → `6 failed in 0.98s`.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `test_a_written_file_name_cannot_break_the_one_line` | `AssertionError: PROBE X2 FAIL file written in cwd: constructed` / `second-line.txt` · `assert 2 == 1` | HELD |
| O2 | Opus | `test_a_failed_turn_logs_no_cli_text` | `AssertionError: ['… cobalt.cos.session:_fail:281 - CoS turn FAILED: the session died (ConnectionError: constructed-cli-stderr-text)']` | HELD |
| O3 | Opus | `test_x2_a_session_that_never_ran_is_not_ok` | `AssertionError: ('X2', 'PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=False)')` | HELD |
| O4 | Opus | `test_x17_nothing_ok_on_either_model_is_not_ok` | `AssertionError: PROBE X17 OK sonnet ok 0/20 · opus ok 0/20` | REJECTED — card P1 X17: "default: the number of the 20 ending `ok`; OK iff Sonnet's ≥ Opus's" (0 ≥ 0 is the card's own ASK DESK rule); test removed |
| A1 | Grok | `test_the_probe_kill_does_not_reach_pgrep` | `AssertionError: assert 'inner.kill' not in '    def kil...ner.kill()\n'` | REJECTED — card P1 (c) "THE SESSION is the resident's: … client from `sdk_client_factory` (`:206`) or `CosSession` (`:255`)"; `_kill_tree` is the resident's kill (no orphaned CLI), and `session.py` is fenced (`## NOT IN THIS JOB`); test removed |
| A2 | Grok | `test_a_killed_turn_does_not_log_the_cli_exception_text` | `AssertionError: assert 'constructed... CLI is gone' not in '…'` (`CoS turn FAILED: the session died (ConnectionError: constructed: the CLI is gone)`) | HELD (same defect as O2) |
| A3 | Grok | `grep -n -A 8 -F "def test_cos_run_is_unchanged" tests/cobalt/test_cos_probe.py` | `384:def test_cos_run_is_unchanged(monkeypatch):` … `389:    assert _main(monkeypatch, "cos", "run") == 0` · `390:    assert _main(monkeypatch, "cos", "run", "--dry-run") == 0` · `391:    assert seen == [[], ["--dry-run"]]`; no `probe` | REJECTED — card P1 "`run` and `--dry-run` unchanged": a pin of unchanged behaviour is green on BASE by design (the build's DECISION 8; red under its mutation M8) |
Red commit: `aa071d5a wip(cos-probe-1019): check red — O1, O2, O3, A2`.
CHECK ASKS, answered by run:
- X3: `git diff 07eb89a3 -- src/cobalt/cos/run.py src/cobalt/cos/session.py configs/cobalt/redact.yaml` → empty; `test_the_probe_is_mounted_and_lists_the_seven_items` and `test_cos_run_is_unchanged` pass in the 61-test run below.
- X5: mutation of `redact.yaml` `url_query_secret` (`[?&]` → `[?&#]`, `key` → `k|key`, Edit, undone, never committed) → `test_x20_redact_keeps_the_card_fragment_key` `1 failed`: `AssertionError: url_query_secret x1` · `… /hitl/7#k=[REDACTED:url_query_secret]`. Undone → `1 passed in 0.04s`; the diff above is empty.
- X1, X2: covered by O2/A2 (a log line carried exception text; fixed) and A1 (`pgrep` by the resident's kill; rejected, open).
- X4: X3, X14, X17 and the X2/X10 split are the build's DECISIONS 1–4 (ASK DESK defaults); O4 (X17 at 0/0) is open.

## FIXES
- O1: `src/cobalt/cos/probe.py` `main` folds the clause to one line (`" ".join(clause.split())`).
- O2, A2: `src/cobalt/cos/probe.py` `_verdict` runs with `logger.disable("cobalt.cos.session")`, `enable` in a `finally`.
- O3: `src/cobalt/cos/probe.py` `_live_scratch` returns FAIL `the session never ran (no init message; turn reason=…)` when no init `SystemMessage` streamed and no breach was found.
After the fixes: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` → `61 passed in 4.71s`. DevDocs line: `docs/40 - DevDocs/cobalt/cos/README.md` `## 2026-10-19 — cos-probe-1019 (check)`. Commit `f8b2887b fix(cos-probe-1019): one-line clause, no CLI text in the log, X2/X10 need a session that ran (check O1, O2, O3, A2)`.

## Suites
RESTARTS (before the gate): `uv run cobalt jobs restarts 07eb89a3..HEAD` → `cli.md M DOCS -` · `cos/README.md M DOCS -` · `cos-probe-1019-build-2026-10-19.md A DOCS -` · `cos-probe-1019-build-2026-10-19.result A DOCS -` · `src/cobalt/cos/cli.py M static import reach com.cobalt.radar` · `src/cobalt/cos/probe.py A static import reach com.cobalt.radar` · `tests/cobalt/test_cos_probe.py A test/documentation; no resident -` · `tests/cobalt/test_hitl_offline.py M test/documentation; no resident -` · `RESTARTS: com.cobalt.radar`. No UNCLASSIFIED row.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-1019 all --deploy --deploy-gate` on `f8b2887b` · exit 0 · verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8846/0
lock: waited 14 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5743/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-1019-all-20261019-184406.log
```
None marked `OUTSIDE the allowed set`. `ls /Users/cobalt/cobalt-wt/cos-probe-1019/.env` → `No such file or directory` (19:47).

## Scope
PREFLIGHT's path union (`07eb89a3..8f47d85b`): `src/cobalt/cos/cli.py`, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`, `tests/cobalt/test_hitl_offline.py`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/cos/README.md` — each in a row's `files`. My commits: `tests/cobalt/test_cos_probe.py` (P1/P2 files), `src/cobalt/cos/probe.py` (P1, A1 files), `docs/40 - DevDocs/cobalt/cos/README.md` (D0 files).

## Checked against the branch
(i) `git log --oneline 8f47d85b..HEAD -- . ":(exclude)docs"` → `f8b2887b fix(cos-probe-1019): …` · `aa071d5a wip(cos-probe-1019): check red — O1, O2, O3, A2`; tip now `f8b2887b`.
(ii) `git log --stat --format=%h 8f47d85b..HEAD` → f8b2887b: `docs/40 - DevDocs/cobalt/cos/README.md`, `src/cobalt/cos/probe.py` · aa071d5a: `tests/cobalt/test_cos_probe.py` · 3af79697: the build report .md and .result. No WIDENED path.
(iii) `git log --oneline 07eb89a3..HEAD -- src/cobalt/cos/session.py src/cobalt/cos/run.py src/cobalt/cos/listener.py src/cobalt/cos/tools.py src/cobalt/redact configs/cobalt/redact.yaml configs/cobalt/agents/cos.yaml configs/cobalt/taxonomy/tunables.yaml src/cobalt_agent` → empty.
(iv) `grep -n -F "def <test>" tests/cobalt/test_cos_probe.py` → `427:def test_a_written_file_name_cannot_break_the_one_line` · `434:def test_a_failed_turn_logs_no_cli_text` · `452:def test_x2_a_session_that_never_ran_is_not_ok` · `462:def test_a_killed_turn_does_not_log_the_cli_exception_text`; red `aa071d5a` sits below fix `f8b2887b` in (i).
(v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/cos-probe-1019`.
(vi) `git log --stat --format=%h 07eb89a3..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `test_cos_probe.py`, `test_hitl_offline.py` (offline tests); no migration, no with-DB test: gate lists not needed.
(vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (they name `rev-parse`, `git diff --stat` and readings): nothing to run.
(viii) L32: the report holds constructed test values and repo paths only.

## OPEN
- O4 · REJECTED — X17 is OK at `sonnet ok 0/20 · opus ok 0/20`; settled by a desk ruling on the X17 default (e.g. OK also needs Opus's count > 0).
- A1 · REJECTED — the resident's `_SdkClient.kill` → `_kill_tree` runs `pgrep`, a subprocess outside boundary (e)'s list; settled by a desk ruling on whether the resident's own kill counts as "the probe itself" (a change would sit in fenced `session.py`).
- A3 · REJECTED — `test_cos_run_is_unchanged` cannot be red on BASE; settled by the card's P2 line (the build's DECISION 8 already carries it).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK (O3 fix): `_live_scratch` now also FAILs X2 / X10 when no init message streamed (`the session never ran …`). This adds one condition to the card's "OK iff" list, read from the FINAL's "a real session … told to". Default taken: the stricter rule (a false OK on the deploy-stop item is the worse error). [19:47]
2. ASK DESK (O4): X17's card default passes at 0 ≥ 0, when no DM ends ok on either model. Default taken: left as the card wrote it, open. [19:47]
3. ASK DESK (A1): a failed turn's kill runs `pgrep` through the resident's `_kill_tree` (`session.py:146`). Boundary (e) lists only the auth check, `ps` and the SDK's CLI spawn. Default taken: kept (it is the resident's own kill, it leaves no orphaned CLI, and `session.py` is fenced), open. [19:47]

## RECORDS
- `date`: 18:20 start; 18:22 Grok started; 18:41 house-a.md written; 18:42 runs; 18:44 gate start (lock waited 14 min); 19:47 close.
- House A Grok `FINDINGS: 3`, written by Grok to `<S>/house-a.md`; its stdout was the path plus progress lines. House B: none (card `HOUSE B: as needed`); Gemini UP but not seated.
- Dropped findings: none. Houses that produced nothing: none. `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (no with-DB finding; the one take was the gate's).
- L74 / attribution: a system reminder asked for a `Claude-Session:` line in commits; CHECK-HUB L74 says commits carry `Co-Authored-By` only, so my two commits carry that line alone.
- X5 mutation of `configs/cobalt/redact.yaml` was made and undone with Edit; `git diff 07eb89a3 -- configs/cobalt/redact.yaml` empty.
- O4 and A1 tests were removed again after their run (REJECTED; a red test is not committed).
- The report and its `.result` sit on `main`'s working tree, uncommitted: the desk commits them (no listed string commits in `/Users/cobalt/cobalt`).
- files opened: 15 — CHECK-HUB.md, the card, areas/cobalt.md, BUILD-HUB.md (`## THE LOCK` to `## CLOSE`), the build report (`## RESTARTS` to the end), `src/cobalt/cos/probe.py`, `src/cobalt/cos/cli.py`, `src/cobalt/cli.py` (500–580), `src/cobalt/cos/session.py`, `tests/cobalt/test_cos_probe.py`, `configs/cobalt/redact.yaml` (122–140), `<S>/house-a.md`, and three task outputs (house probe, Grok, gate). Read by diff only: `test_hitl_offline.py`, the two DevDocs pages. NOT opened, of the card's `## READ`: F20-FINAL, `tools.py`, `cos.yaml`, `hitl/card.py`, `redact/guard.py`, `test_cos_offline.py`, the draft-cos-gate-amend report (staged for the house; the X20 test's run on the real files stands in for card.py, guard.py and redact.yaml).
- Check of `cos-probe-1019`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-probe-1019 · pass: 1 · tip: f8b2887b · house A: Grok FINDINGS: 3 · findings: 7 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 3 · house B: none available · suites: offline 8846/0 · with-DB 5743/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 15 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 185218
