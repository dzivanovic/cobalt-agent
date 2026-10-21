# cos-tunables — check report 2026-10-20 (pass 1)

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · TIP `17f45d80` · seat `cos-tunables-check` (Opus 5.5).

## §0 Headline
The check of card 933 is done, and it is NOT ready: one test file the build changed lies outside the card's rows (`test_sheet_daymode_probe.py`, held by both houses). Admitting that path is Dejan's call.
Six findings: four of mine, two from Grok, none dropped. Two held and were fixed with tests only (`ace7a92a`): P1's owed-file raise, and the runner's own probe path. Two were rejected by card or hub lines and stay open, among them O1: an unreadable owed file loses every probe of that beat.
The deploy gate on `ace7a92a` is green: offline 8974/0, with-DB 5873/0, live-note 148/0, `cobalt_dev` 0013 with F2 = F0, `.env` removed.

## L74
The session's harness reminder (a system turn, 19:10 EDT) asked commits to end with a `Claude-Session:` line. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` (19:10:32):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · 8e03850ac9cde6fa37ba3e9fc4b89e73f0cfe04c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` (exit 0):
```
clock · date · 0 · Tue Oct 20 19:10:36 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-tunables
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h 17f45d80..HEAD · 0 · (6 lines)
    2b53b56b docs(cos-tunables): build report — 17f45d80
    2b53b56b
    
     .../reports/cos-tunables-build-2026-10-20.md       | 197 +++++++++++++++++++++
     .../reports/cos-tunables-build-2026-10-20.result   |  15 ++
     2 files changed, 212 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-tunables/docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md" · 0 · BUILT · job: cos-tunables · tip: 17f45d80 | on e69d5ab8 | migration: none | offline 4899/0 | with-DB 5871/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 3 of 3 | self-check: 1 of 3 | decisions: 3 · for Dejan: 0 · tokens: 180196
report: self-check 1 of 3 (recorded)
range · git log --oneline e69d5ab8..17f45d80 · 0 · (3 lines)
    17f45d80 fix(cos-tunables): pass S2 1
    2a8b0315 feat(cos-tunables): rows
    e3f05089 wip(cos-tunables): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: a routed card (BAND: MID), expected and recorded, not a finding.
- Self-check `1 of 3` (lower than 3): recorded; handed to the house as a fact.
- THE RANGE, `git log --stat --format=%h e69d5ab8..17f45d80` → `17f45d80`: `tests/cobalt/test_sheet_daymode_probe.py | 4 ++++`; `2a8b0315`: `configs/cobalt/jobs.yaml | 16`, `configs/cobalt/taxonomy/tunables.yaml | 4`, `docs/40 - DevDocs/cobalt/heartbeat/probes.md | 3`, `docs/40 - DevDocs/cobalt/heartbeat/runner.md | 3`, `src/cobalt/heartbeat/probes.py | 14`, `src/cobalt/heartbeat/runner.py | 2`; `e3f05089`: `tests/cobalt/test_cos_offline.py | 4`, `tests/cobalt/test_cos_probes.py | 55`, `tests/cobalt/test_cos_registry.py | 82`. Path union: those ten paths.
- The card is not "DB: none": no name-only row.
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-tunables-check` → `No such file or directory` (fresh).
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → `grok: UP` · `gemini: UP`. No `HOUSE A:` header line on the card.
- Seats: **house A: Grok · house B: none (not needed)** (the card's `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-tunables-check`), output whole:
```
25 <S>/STAGED-CARD
16691 <S>/diff.md
14651 <S>/files/933-cos-tunables-card.md
29678 <S>/files/cos-tunables-build-2026-10-20.md
27165 <S>/files/wt/configs/cobalt/jobs.yaml
40081 <S>/files/wt/configs/cobalt/taxonomy/tunables.yaml
7622 <S>/files/wt/docs/40 - DevDocs/cobalt/heartbeat/probes.md
4208 <S>/files/wt/docs/40 - DevDocs/cobalt/heartbeat/runner.md
39993 <S>/files/wt/src/cobalt/heartbeat/probes.py
20465 <S>/files/wt/src/cobalt/heartbeat/runner.py
23309 <S>/files/wt/tests/cobalt/test_cos_offline.py
4532 <S>/files/wt/tests/cobalt/test_cos_probes.py
4593 <S>/files/wt/tests/cobalt/test_cos_registry.py
7668 <S>/files/wt/tests/cobalt/test_sheet_daymode_probe.py
386 <S>/rulings.md
STAGED 15 files · 241067 bytes · commits 3
```
(`<S>` abbreviates the absolute path the script printed.) `commits 3` = PREFLIGHT's range count. The card's `## READ` files the script cannot derive, each `stage-copy.sh`: `COPIED 4960 <S>/files/cos-bootstrap-decisions-2026-10-20.md` · `COPIED 14955 <S>/files/wt/src/cobalt/cos/session.py` · `COPIED 6470 <S>/files/wt/src/cobalt/cos/run.py` · `COPIED 7022 <S>/files/wt/src/cobalt/hitl/actions.py` · `COPIED 23604 <S>/files/wt/src/cobalt/jobs/watchdog.py` · `COPIED 32603 <S>/files/wt/src/cobalt/smoke/checks.py` · `COPIED 77859 <S>/files/wt/tests/cobalt/test_smoke.py` · `COPIED 41777 <S>/files/wt/tests/cobalt/test_jobs.py`. `<S>/HOUSE-INSTRUCTIONS.md` written (the HOUSE TEXT verbatim, the PREFLIGHT facts for the house, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph). House A Grok started 19:12 (`run_in_background`, timeout 2700000) from `/Users/cobalt/cobalt-wt/agy-trial`; `git status --short --branch` after the return → `## ops/cos-tunables` / `?? SHADOW-INSTRUCTIONS.md`.

## OWN FINDINGS
Written 19:2x EDT, before any house file was opened. Read for the CHECK ASKS from the code, run at `## 4`: X1 from the diff (two `value:` lines, nothing else); (6) no score, rank, grade or size reads `cos.*` / `hitl.*`; the radar receipt's `tunables_sha256` is taken over the whole registry (`src/cobalt/radar/runner.py:548` `tunables_loader=lambda: load_tunables().by_key`), so it changes at deploy, as every tunables change does (`src/cobalt/radar/evaluate.py:51` "versioned by hash"): not a finding.

FINDING O1
ROW: P1 (X2, X3)
CLAIM: An unreadable owed file makes `probes.cos` raise `BootstrapOwedError` (`src/cobalt/heartbeat/probes.py:146`) inside the list literal of `take_beat` (`src/cobalt/heartbeat/runner.py:131-152`), so the whole PROBES stage of the beat is lost (every other probe with it), although `take_beat` says "Never raises on a red" (`runner.py:127`) and the sweep keeps that same file's error as a red line and goes on (`src/cobalt/jobs/watchdog.py:436-440`).
RUN: TEST — `tests/cobalt/test_cos_probes.py`
```python
def test_an_unreadable_owed_file_leaves_the_other_probes_standing(monkeypatch):
    from cobalt.heartbeat import probes, runner
    from cobalt.jobs import watchdog

    for name in ("database", "sheet_http", "sheet_daymode", "obsidian", "mainframe", "herdr",
                 "archiver_freshness", "seat_usage", "backup_freshness", "vaultwrite_blocks",
                 "redactions", "radar"):
        monkeypatch.setattr(probes, name, lambda *a, _n=name, **k: probes.Probe(_n, True, "faked"))
    monkeypatch.setattr(runner, "sweep", lambda **k: [])

    def unreadable():
        raise watchdog.BootstrapOwedError("constructed: not a JSON object keyed by label")

    monkeypatch.setattr(watchdog, "bootstrap_owed", unreadable)
    monkeypatch.setattr(probes, "_cos_enabled", lambda: True)
    beat = runner.take_beat(now=NOW, probe=False)
    names = [p.name for p in beat.probes]
    assert "database" in names and "cos" in names, names
    cos = next(p for p in beat.probes if p.name == "cos")
    assert cos.ok is False and "BootstrapOwedError" in cos.detail
```
EXPECT: `cobalt.jobs.watchdog.BootstrapOwedError: constructed: not a JSON object keyed by label` raised out of `runner.take_beat`.

FINDING O2
ROW: P1
CLAIM: P1's "An unreadable owed file raises (`BootstrapOwedError`, L1): it is not swallowed" is built (`probes.py:146`, `:181`, uncaught) but no test pins it: a `try/except` around either call would leave every test green (the build's DECISION 2).
RUN: COMMAND — `grep -n -F "BootstrapOwedError" tests/cobalt/test_cos_probes.py`
EXPECT: no line (exit 1).

FINDING O3
ROW: SCOPE
CLAIM: The build changed `tests/cobalt/test_sheet_daymode_probe.py:183-186` (commit `17f45d80`), a file in no row's `files`, to clear a red outside the rows, where the card's fence says "A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here".
RUN: COMMAND — `git diff --stat e69d5ab8..17f45d80 -- tests/cobalt/test_sheet_daymode_probe.py`
EXPECT: `tests/cobalt/test_sheet_daymode_probe.py | 4 ++++` · `1 file changed, 4 insertions(+)`.

FINDING O4
ROW: P1 (5)
CLAIM: The runner calls `probe_mod.cos(ts)` / `probe_mod.hitl(ts)` with `enabled=None` (`runner.py:150-151`), the path that reads the REAL row (`probes.py:129-132`, now `enabled: true`) and then the owed file; no test takes it: the new OWED test passes `enabled=True` (`tests/cobalt/test_cos_probes.py:108`, `:111`), and the only default-arg call, `probes.cos(NOW)` at `:53`, sits under `if … enabled is False` (`:52`), dead on the tip; `probes.hitl(NOW)` is called by no test.
RUN: COMMAND — `grep -n -F "probes.hitl(NOW)" tests/cobalt/test_cos_probes.py`
EXPECT: no line (exit 1).

## Findings
House A Grok finished 19:23 (exit 0; completion notice at 19:23:52, after `## OWN FINDINGS` was written); its stdout ended with the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-tunables-check/house-a.md` and the file (1029 bytes) ends `FINDINGS: 2`. House B: none (not needed). The drop: both blocks carry `RUN: COMMAND` followed by one `git diff` line: both kept.
- A1 · Grok · SCOPE · `tests/cobalt/test_sheet_daymode_probe.py:183-188` stubs `cos`/`hitl`; the file is in no row's files and the fence says a red outside the rows is not fixed here · COMMAND
- A2 · Grok · SCOPE · the two DevDocs pages `heartbeat/probes.md`, `heartbeat/runner.md` gain a `2026-10-20 — cos-tunables` section; neither is a row's file · COMMAND

## Dropped
none

## RUNS
- O1 · opus-own · TEST placed in `tests/cobalt/test_cos_probes.py`, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py::test_an_unreadable_owed_file_leaves_the_other_probes_standing` · `1 failed in 0.13s`; first failing line `E       cobalt.jobs.watchdog.BootstrapOwedError: constructed: not a JSON object keyed by label`, raised at `src/cobalt/heartbeat/runner.py:150: in take_beat` ← `src/cobalt/heartbeat/probes.py:146: in cos` · **REJECTED — P1: "An unreadable owed file raises (`BootstrapOwedError`, L1): it is not swallowed."** It is red for its stated reason (the whole PROBES stage is lost), but the card rules that the error propagates. The test was removed again with the Edit tool. OPEN.
- O2 · opus-own · COMMAND `grep -n -F "BootstrapOwedError" tests/cobalt/test_cos_probes.py` · no output (exit 1) · **HELD** (P1's raise clause has no test).
- O3 · opus-own · COMMAND `git diff --stat e69d5ab8..17f45d80 -- tests/cobalt/test_sheet_daymode_probe.py` · ` tests/cobalt/test_sheet_daymode_probe.py | 4 ++++` / ` 1 file changed, 4 insertions(+)` · **HELD, NOT FIXED — tests/cobalt/test_sheet_daymode_probe.py** (outside every row's files; the card fence says a red outside the rows is "never fixed here". Reverting the stub makes the offline suite red again in any checkout without the owed file, as W run 1 showed, so the change stays as it is and goes to the desk.)
- O4 · opus-own · COMMAND `grep -n -F "probes.hitl(NOW)" tests/cobalt/test_cos_probes.py` · no output (exit 1) · **HELD** (no test takes the runner's `enabled=None` path to OWED).
- A1 · Grok · COMMAND `git diff e69d5ab8..17f45d80 -- tests/cobalt/test_sheet_daymode_probe.py` · the diff adds `+            # cos and hitl read the registry and, once the row is enabled` / `+            # and not OWED, a real store. The owed file is gitignored desk` / `+            # state, so this test must not depend on it.` / `+            "cos", "hitl",` · **HELD, NOT FIXED — tests/cobalt/test_sheet_daymode_probe.py** (the same path as O3).
- A2 · Grok · COMMAND `git diff e69d5ab8..17f45d80 -- "docs/40 - DevDocs/cobalt/heartbeat/probes.md" "docs/40 - DevDocs/cobalt/heartbeat/runner.md"` · each page adds `## 2026-10-20 — cos-tunables` and one line · **REJECTED — BUILD-HUB E3: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"** (`probes.py` and `runner.py` are row P1's modules). OPEN.

The held tests were committed with the fix: O2 and O4 hold on a command, so their tests ARE the fix. No `wip(cos-tunables): check red` commit was made because there was no failing test to commit ahead of a code fix. Instead, each new test was shown red with the Edit tool against the one mutation it guards, then the mutation was undone:
- `test_an_unreadable_owed_file_raises_through_both_probes`. First mutation: `probes.cos` catches `BootstrapOwedError` and reads `frozenset()` → `1 failed in 0.06s`, `E       Failed: DID NOT RAISE <class 'cobalt.jobs.watchdog.BootstrapOwedError'>` (`test_cos_probes.py:124`). Second mutation: the same catch in `probes.hitl` → `1 failed in 0.07s`, the store was reached: `src/cobalt/heartbeat/probes.py:191: in hitl` / `E       RuntimeError: constructed: hitl tables are not created`.
- `test_the_runner_path_reads_the_real_row_then_the_owed_file`. Mutation: `probes.hitl` reads `enabled = False` in place of `_cos_enabled()` → `1 failed in 0.08s`, `E               AssertionError: assert ('unknown' in 'unknown — NOT PROBED, registry enabled: false (com.cobalt.cos)' and 'OWED' in …)`.
- After the undos, `git diff --stat` → ` tests/cobalt/test_cos_probes.py | 25 +++++++++++++++++++++++++` (src back at the tip).

## FIXES
- O2, O4: `ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)`. It adds two tests to `tests/cobalt/test_cos_probes.py` and one dated line to `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, with no code change. Run: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probes.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_offline.py tests/cobalt/test_sheet_daymode_probe.py` → `45 passed in 7.17s`.
- O3: HELD, NOT FIXED — tests/cobalt/test_sheet_daymode_probe.py
- A1: HELD, NOT FIXED — tests/cobalt/test_sheet_daymode_probe.py

## Suites
RESTARTS first, with the tip named: `uv run cobalt jobs restarts e69d5ab8..ace7a92a`. The `..HEAD` form is not used because it counts the untracked `SHADOW-INSTRUCTIONS.md`, as the build report records. Output whole:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-tunables-build-2026-10-20.result	A	DOCS	-
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No UNCLASSIFIED row. X5: the derived line names `com.cobalt.cos` beside the header's `com.cobalt.aset com.cobalt.radar`. The card's RECORDS make the derived line the record, and the hub skips cos as not loaded (card 869; `tests/ops/test_hub_cos_restart_1019.py` is present, `## Checked against the branch` (vii)).

The gate on the tip `ace7a92a`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy --deploy-gate` (19:25 → 20:13). Exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8974/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5873/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-192526.log
```
- `grep -n -F "OUTSIDE the allowed set" <log>` → no line. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1047`) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2329`) → `cobalt_dev: 0013 — F2 = F0`.
- The offline count, 8974, includes `tests/ops`, which `--deploy-gate` runs. The build's 4899 did not, and the two tests this check adds are among them.
- `.env`: removed by the gate; `ls /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory` (20:13).

## Scope
PREFLIGHT's path union (10 paths) plus `ace7a92a` (`tests/cobalt/test_cos_probes.py`, `docs/40 - DevDocs/cobalt/heartbeat/probes.md`). These are checked against the rows' files: T1 `tunables.yaml`, `test_cos_offline.py`; T2 `jobs.yaml`, `test_cos_registry.py`; P1 `probes.py`, `runner.py`, `test_cos_probes.py`; the two DevDocs pages by BUILD-HUB E3 / CHECK-HUB `## 5`. One path is in no row: `tests/cobalt/test_sheet_daymode_probe.py` (O3 / A1, HELD, NOT FIXED). Nothing lies inside the fence (`## Checked against the branch` (iii)).
OUT OF SCOPE, recorded and not opened as findings: the stale "`enabled: false`" wording in fenced files: `ops/start_cos.sh:8`, `ops/com.cobalt.cos.plist:7`, `src/cobalt/cos/__init__.py:7` (fence: `ops/…cos…`, `src/cobalt/cos/*`), and the test comment `tests/cobalt/test_jobs_reads.py:94`. `cobalt validate` no longer prints cos under `NOT LOADED BY DESIGN` (`src/cobalt/cli.py:332`): this is information, not a red.

## Checked against the branch
- (i) `git log --oneline 17f45d80..HEAD -- . ":(exclude)docs"` → `ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)`; `<tip now>` = `ace7a92a`.
- (ii) `git log --stat --format=%h 17f45d80..HEAD` → `ace7a92a`: `docs/40 - DevDocs/cobalt/heartbeat/probes.md | 3`, `tests/cobalt/test_cos_probes.py | 25`; `2b53b56b`: the build report and its `.result` (docs). Every non-docs path is a test file of a row. No WIDENED.
- (iii) `git log --oneline e69d5ab8..HEAD -- ops/com.cobalt.cos.plist ops/start_cos.sh data/deploy/bootstrap-owed.json src/cobalt/cos src/cobalt/hitl` → empty.
- (iv) `grep -n -F "def test_an_unreadable_owed_file_raises_through_both_probes" tests/cobalt/test_cos_probes.py` → `117:`; `grep -n -F "def test_the_runner_path_reads_the_real_row_then_the_owed_file" tests/cobalt/test_cos_probes.py` → `130:`. There is no `wip(cos-tunables): check red` commit: O2 and O4 hold on commands, their tests are the fix, and each was shown red under its mutation (`## RUNS`).
- (v) `ls /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cos-tunables` / `?? SHADOW-INSTRUCTIONS.md` (routed card, expected).
- (vi) `git log --stat --format=%h e69d5ab8..HEAD -- src/cobalt/db_migrations tests/cobalt` → test files only (`test_cos_probes.py`, `test_sheet_daymode_probe.py`, `test_cos_offline.py`, `test_cos_registry.py`), no migration and no with-DB test file: no gate-lists change needed.
- (vii) `ls …/tests/ops/test_hub_cos_restart_1019.py /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → both listed; `grep -n -F "timeout_s: 1200" configs/cobalt/jobs.yaml` → `217:    timeout_s: 1200`; `git -C /Users/cobalt/cobalt log --oneline -1 -- "docs/40 - DevDocs/reports/cos-bootstrap-decisions-2026-10-20.md"` → `bd7bc0c9 docs(prompts): 930/932/934 drafters (cutover tooling, tunables, 929 amend); brain decisions; R2201`. The `rev-parse` record is not on this seat's list, so it was not run.
- (viii) L32: this report holds no ticker, price or date of his. The values `10` and `30` are the card's DEFAULTS.

CHECK ASKS, answered from the runs:
- X1: yes. The tunables diff is the two `value:` lines, each `# DEFAULT (brain; his word may change it)` (the build's `grep -n -F` → `:1009`, `:1027`).
- X2: with cos listed, the sweep is OWED (`watchdog.py:441-446`), K18 is PASS with the OWED clause (`test_k18_reads_cos_as_owed_while_unloaded`), and `probes.cos` and `probes.hitl` are OWED-unknown, now on the runner's own `enabled=None` path too (O4's test). No consumer reads RED. One exception: an UNREADABLE owed file makes both probes raise, and the whole PROBES stage of the beat is lost (O1, REJECTED by the card's clause, OPEN).
- X3: with cos not listed, the sweep reads `not loaded` (red), K18 FAILs (`enabled but not loaded`), `probes.cos` is red "no heartbeat", and `probes.hitl` reaches `HitlStore.probe_counts()` on tables cos has not created. If that raises, the PROBES stage of the beat fails as in O1.
- X4: no test pins `enabled is False`, `value is None`, `10` or `30`. The second loop of `test_disabled_row_is_unknown` (`:52-55`) is dead while the row is enabled, and O4's test covers that path.
- X5: see `## Suites`.

## OPEN
- O1 · REJECTED (P1: "it is not swallowed"). An unreadable owed file loses every probe of the beat (`runner.py:131-152`), not only cos/hitl. Settled by: a ruling on whether `probes.cos` / `probes.hitl` should turn `BootstrapOwedError` into a red `Probe` naming the error, which is still loud, as the sweep does at `watchdog.py:436-440`. The test is in this report under O1.
- A2 · REJECTED (BUILD-HUB E3's dated DevDocs line). Settled by: nothing. The line is required.
- O3 · HELD, NOT FIXED — `tests/cobalt/test_sheet_daymode_probe.py`. Settled by: the desk or Dejan admitting the path into the card's files, or a ruling on another remedy.
- A1 · HELD, NOT FIXED — `tests/cobalt/test_sheet_daymode_probe.py` (the same path as O3).

## CONTINUE
next: none — CLOSE done; the desk verifies and commits the report.

## DECISIONS
1. FOR DEJAN — O3 HELD, NOT FIXED — `tests/cobalt/test_sheet_daymode_probe.py` (scope). Build commit `17f45d80` added `"cos", "hitl"` to the probes that `TestItIsWiredIntoTheBeat.test_the_runner_asks_it_right_after_sheet_http` stubs (+4 lines). The card's fence says a red outside the rows is "never fixed here". Without the stub, T2's enabled row makes that test reach Postgres in any checkout with no gitignored owed file (the build's W run 1: `cobalt.db.DbConfigError: Missing Postgres settings for the APP credential`). Safe default taken: left as committed, not reverted; reverting would put the suite red. Settling it needs this path admitted into the card's files: a card amendment, R-row.
2. FOR DEJAN — A1 HELD, NOT FIXED — `tests/cobalt/test_sheet_daymode_probe.py`. Grok's form of the same item as 1; the same safe default and the same settlement.
3. O1 REJECTED, OPEN. An unreadable `data/deploy/bootstrap-owed.json` makes `probes.cos` raise inside `take_beat`'s probe list, so that beat loses EVERY probe (database, sheet, radar …), not only the cos line. The card's P1 rules "it is not swallowed", so nothing was changed. Safe default taken: the card's behaviour stands. The follow-up is one question: should both probes return a red `Probe` that names the `BootstrapOwedError`? That is still loud, and it keeps the other probes standing, as the sweep already does at `watchdog.py:436-440`.

## RECORDS
- Findings: opus-own 4 (O1–O4), house A Grok 2 (A1, A2); dropped 0. Held 4 (O2, O3, O4, A1); fixed 2 (O2, O4); held unfixed 2 (O3, A1); open 4 (O1, A2, O3, A1).
- L74: one harness reminder (19:10) asked for a `Claude-Session:` commit line; not acted on.
- House A Grok: `FINDINGS: 2`, wrote `house-a.md` itself (19:23). House B: none (not needed, `HOUSE B: as needed`). No house produced nothing.
- The probe-output file of the house probe was first read with `cat` (a command I added, not refused, and it printed nothing). Every later task output was read with the Read tool.
- No extra lock take: the one take was inside the gate (`lock: waited 0 min`). `.env`: removed, proven gone (W, 20:13).
- `cobalt jobs restarts` was run with the tip named (`e69d5ab8..ace7a92a`): the `..HEAD` form counts the untracked `SHADOW-INSTRUCTIONS.md` (the build report's RECORDS).
- RESULT FILE: `cos-tunables-check-2026-10-20.result` was written beside this report on `main`. This seat has no commit string for the `/Users/cobalt/cobalt` checkout, so the desk commits the two together.
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 4f20a063-5480-4efe-b788-27dfd60d88b4` → `context 196640 of 400000 — ok` (20:13).
- files opened: 19. These are CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK`, `## E2`–`## W`); the build report; areas/cobalt.md (`## What Cobalt is`, `## Build rules` down); `src/cobalt/heartbeat/probes.py`; `src/cobalt/jobs/watchdog.py`; `src/cobalt/smoke/checks.py`; `src/cobalt/heartbeat/runner.py`; `src/cobalt/cli.py`; `src/cobalt/radar/evaluate.py`; `tests/cobalt/test_cos_probes.py`; `tests/cobalt/test_setups_d1.py`; `ops/README.md`; `ops/desk/deploy-step0.sh`; `<S>/house-a.md`; and three task-output files (the house probe, Grok, the gate). Directory greps also ran over `src/cobalt`, `tests` and `ops`.
- Check of `cos-tunables`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-tunables · pass: 1 · tip: ace7a92a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 4 · fixed: 2 · held unfixed: 2 · open: 4 · house B: none available · suites: offline 8974/0 · with-DB 5873/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: NO · decisions: 3 · for Dejan: 2 · tokens: 196640
