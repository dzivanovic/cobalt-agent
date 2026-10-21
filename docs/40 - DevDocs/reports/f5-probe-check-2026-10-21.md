# f5-probe — CHECK 2026-10-21

## §0 Headline
- Check of f5-probe on `c2565a9f` → tip `a25a4f91`. House A was Grok (`FINDINGS: 6`). House B: none (card `HOUSE B: as needed`). Opus wrote 1 finding of its own.
- 7 findings, 0 dropped. 1 held and fixed: A5, the X6 rule-D pin was too weak; a new test pins the values and was shown red under two mutations. 1 not held (A6).
- 5 REJECTED and left open (O1, A1–A4). The card's rows say the behaviour is right, but each one needs a desk answer under `## DECISIONS`. O1 blocks the RECORDS' first `--keep-groups` capture: `/Users/cobalt/cobalt-wt/.f5-probe/` does not exist.
- Deploy gate green: offline 9070/0 · with-DB 5916/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS `com.cobalt.radar`.

## L74
- The session's system reminder (not a tool result) asked for a `Claude-Session:` line on commits. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; recorded once, not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 0 · 78109d443064d3cd410efcd65f8eccbf9d4ab222
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
HOUSE GATES: `grep -n "^| R17 "` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 "` → one row (line 37, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Wed Oct 21 13:14:18 EDT 2026
status · git status --short --branch · 0 · ## ops/f5-probe
head · git log --oneline -1; git log --stat --format=%h c2565a9f..HEAD · 0 · (6 lines)
    6bd5638f docs(f5-probe): build report — c2565a9f
    6bd5638f
    
     .../reports/f5-probe-build-2026-10-21.md           | 206 +++++++++++++++++++++
     .../reports/f5-probe-build-2026-10-21.result       |  15 ++
     2 files changed, 221 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f5-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f5-probe/docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.md" · 0 · BUILT · job: f5-probe · tip: c2565a9f | on d988d543 | migration: none | offline 4943/0 | with-DB 5915/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 10 of 10 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 261746
range · git log --oneline d988d543..c2565a9f · 0 · (2 lines)
    c2565a9f feat(f5-probe): cobalt checkpoint probe X4/X5/X6/X7/X10/X13, the keep seam (P1 P2 G1 X6 X4 X13 H1 C1 D0, L1 L28 L32 L45)
    c6433002 wip(f5-probe): red
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h d988d543..c2565a9f` · 0 · c2565a9f: `docs/40 - DevDocs/cobalt/cli.md` +3, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` +3, `src/cobalt/prefill/checkpoint_probe.py` +378, `src/cobalt/prefill/checkpoints.py` 36 ±; c6433002: `tests/cobalt/test_checkpoint_probe.py` +467, `tests/cobalt/test_checkpoints_offline.py` +16. Path union: those six.
- DB: the card carries no `DB: none` line.
- `ls <S>` · 1 · `No such file or directory` (fresh).
- HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · `grok: UP` / `gemini: UP`
- SEATS: no `HOUSE A` header line; Grok UP → house A: Grok · house B: none (not needed — card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · whole:
```
21 <S>/STAGED-CARD
42880 <S>/diff.md
22916 <S>/files/973-f5-probe-card.md
26179 <S>/files/f5-probe-build-2026-10-21.md
8911 <S>/files/wt/docs/40 - DevDocs/cobalt/cli.md
8524 <S>/files/wt/docs/40 - DevDocs/cobalt/prefill/checkpoints.md
16278 <S>/files/wt/src/cobalt/prefill/checkpoint_probe.py
38528 <S>/files/wt/src/cobalt/prefill/checkpoints.py
19460 <S>/files/wt/tests/cobalt/test_checkpoint_probe.py
41657 <S>/files/wt/tests/cobalt/test_checkpoints_offline.py
386 <S>/rulings.md
STAGED 11 files · 225740 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f5-probe-check`; commits 2 = PREFLIGHT's range count.)
`stage-copy.sh` (the `## READ` files), each `COPIED`:
- 47241 `<S>/files/F5-FINAL-2026-10-11.md`
- 17357 `<S>/files/f5-x3-measure-2026-10-20.md`
- 11754 `<S>/files/970-f5-gate-run.md`
- 7386 `<S>/files/draft-f5-gate-run-2026-10-21.md`
- 21496 `<S>/files/wt/src/cobalt/cos/probe.py`
- 1643 `<S>/files/wt/src/cobalt/cos/cli.py`
- 10791 `<S>/files/wt/src/cobalt/modelaccess/client.py`
- 1800 `<S>/files/wt/src/cobalt/modelaccess/guard.py`
- 3825 `<S>/files/wt/src/cobalt/env.py`
- 10287 `<S>/files/wt/src/cobalt/daymode/note.py`
- 11824 `<S>/files/wt/src/cobalt/vault.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (24328 bytes): HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
House A Grok started 13:16 EDT (`date` 13:16:27; gates R17/R19 re-grepped, one row each); house B none (not needed). Return `cd` → `git status --short --branch` → `## ops/f5-probe`.

## OWN FINDINGS
Written before either house list was opened. Read: CHECK-HUB; BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`; the card; `git diff d988d543..c2565a9f` (src, tests, docs); `checkpoints.py:90-450`, `:560-810` at the tip; `test_checkpoint_probe.py` whole; `test_checkpoints_offline.py:120-210`; `env.py:20-80`; `modelaccess/client.py:46-68`, `:85-168`; `redact/guard.py:78-195`; `strike/measure.py:133-137`; F5-FINAL `:171-190`; `f5-x3-measure-2026-10-20.md:64-71`; `draft-f5-gate-run-2026-10-21.md` whole; the build report `:104-206`.

FINDING O1
ROW: G1 (with the card's `## RECORDS` "ROW (b) OWED")
CLAIM: `src/cobalt/prefill/checkpoint_probe.py:141-142` refuses `--keep-groups` when PATH's parent is not a directory, and nothing creates `KEEP_ROOT` (`:59`); `ls -la /Users/cobalt/cobalt-wt/.f5-probe` → `No such file or directory`, so the RECORDS' first-capture command `… probe X6 --keep-groups /Users/cobalt/cobalt-wt/.f5-probe/groups_sector_v140_real.csv` prints a FAIL and keeps no body as the tree stands.
RUN: TEST `tests/cobalt/test_checkpoint_probe.py`
```python
def test_check_o1_keep_root_absent_still_keeps(real_fetch_groups, world, groups_http, monkeypatch, capsys, tmp_path):
    from cobalt.prefill import checkpoints

    keep_root = tmp_path / "never-made"
    monkeypatch.setattr("cobalt.prefill.checkpoint_probe.KEEP_ROOT", keep_root)
    monkeypatch.setattr(checkpoints, "fetch_groups", real_fetch_groups)
    target = keep_root / "groups_real.csv"
    code, out, _ = _probe(monkeypatch, capsys, "X6", "--keep-groups", str(target))
    assert code == 0 and out.rstrip("\n").endswith(f"kept: {target}"), out
```
EXPECT: red — `PROBE X6 FAIL refused: --keep-groups PATH's parent is not a directory`, exit 1. The card (G1 "its parent a directory") says this is right, so the expected verdict is REJECTED and an `## DECISIONS` item: the directory must exist before the gate seat's first X6 run.

No other own finding: the boundary (`_dev_only` first, `_scratch`, `_keep_target`), rule D (`derive`), X4's request (`_request` = `narrate`'s, `checkpoints.py:423-433`), X13's refusal path (`checkpoints.py:682-694`, stores never reached) and the G1 seam (`checkpoints.py:237-249`, the no-`keep` call unchanged) read as the rows say. The redact counter row (a database write on a hit) is the build's own DECISION 2 and X13's pre-check its DECISION 1; neither is re-raised here.

## Findings
House A Grok finished 13:31 EDT (`date` 13:31:10; `ls -la <S>` → `house-a.md` 5926 bytes, written by Grok; stdout was the path). Its last line `FINDINGS: 6`. House B: none (not needed). Every block carries a `RUN:` with a `def test_` or an allowed command; none dropped.
- O1 · opus · G1 · `--keep-groups` refuses while `/Users/cobalt/cobalt-wt/.f5-probe/` does not exist; nothing creates it, so the RECORDS' first-capture command fails as the tree stands · TEST
- A1 · Grok · X1 · a secret-shaped kept body makes `redact` (record on) open `RedactionStore` and insert a `cobalt_redactions` row · TEST
- A2 · Grok · X3 · X6's gate NOT RUN line copies `check_demand`'s text, which carries the peak rpm figure · TEST
- A3 · Grok · X3 · an unknown `COBALT_ENV` value is printed in the FAIL clause · TEST
- A4 · Grok · X13 · an admitted late fire prints `admitted … (run_checkpoint not called)`, not `FAIL — <slot> <action> exit <n>` · TEST
- A5 · Grok · X6 · rule D's index and change steps are not pinned: zeroing both stays green · TEST
- A6 · Grok · D0 · `c2565a9f`'s stat does not include the two docs files · COMMAND

## Dropped
none

## RUNS
The six tests were put at the end of `tests/cobalt/test_checkpoint_probe.py` with the Edit tool and run together: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_checkpoint_probe.py -k "check_o1 or redact_hit_opens or gate_not_run_line or unknown_env_value or admitted_late_fire_is_not or undoing_rule_d" --tb=short` → `6 failed, 38 deselected in 0.73s`. No test's form was repaired.
- O1 · opus · TEST · `AssertionError: PROBE X6 FAIL refused: --keep-groups PATH's parent is not a directory` (`assert (1 == 0)`) · REJECTED — card G1 "PATH … not existing (no overwrite), its parent a directory": red for the stated reason, and the refusal is the row. Test removed; OPEN, `## DECISIONS` 1.
- A1 · Grok · TEST · `AssertionError: RedactionStore opened on a keep hit: [('init', None), ('record', 'modelaccess', ('openai_style_key',))] :: kept: refused (secret-shaped: openai_style_key)` · REJECTED — card G1 "`redact(<those lines>, channel="modelaccess")` with any hit → not written"; `redact/guard.py:93-95` gives `record=False` to the log guard only, and `src/cobalt/redact/*` and `src/cobalt/modelaccess/*` are in `## NOT IN THIS JOB`. It conflicts with P2(c) "no database at all"; the build already raised it as its DECISION 2. Test removed; OPEN, `## DECISIONS` 2.
- A2 · Grok · TEST · `AssertionError: PROBE X6 NOT RUN — Finviz gate: TotalDemandExceeded: REFUSED: total Finviz demand for checkpoint: peak 51.00 rpm at 07:45 ET over [radar, checkpoint], finviz_max_rpm=50 exceeds the ceiling` (constructed plan values) · REJECTED — card X6 (2) "a refusal → `NOT RUN — Finviz gate: <reason>`": the gate's rate, not a market figure; build DECISION 3. Test removed; OPEN.
- A3 · Grok · TEST · `AssertionError: PROBE X5 FAIL refused: COBALT_ENV is 'constructed-env-value' — set it to one of production, dev.` · REJECTED — card P2(a) "unset or unknown → `FAIL refused: <EnvConfigError's first sentence>`"; build DECISION 3. Test removed; OPEN.
- A4 · Grok · TEST · `AssertionError: PROBE X13 FAIL — 07:15 admitted at close + 5 min by window_refusal (run_checkpoint not called)` (`assert None`) · REJECTED — card P2 "Live cost per run: … X5, X7, X10, X13 none": calling `run_checkpoint` on an admitted window sends the gate check and 2 GETs; the clause departs from X13's `FAIL — <slot> <action> exit <n>` for that reason, the build's DECISION 1 (ASK DESK). Test removed; OPEN.
- A5 · Grok · TEST · `AssertionError: stayed green with PRICE_STEP and CHANGE_STEP at 0` (`tests/cobalt/test_checkpoint_probe.py:488`, run alone with `--tb=line`: `1 failed`) · HELD — the X6 pin checks phrase names only; rule D's values are unpinned (house text (5), an assertion too weak).
- A6 · Grok · COMMAND `git show --stat --format= c2565a9f` · output: `docs/40 - DevDocs/cobalt/cli.md | 3 +` · `docs/40 - DevDocs/cobalt/prefill/checkpoints.md | 3 +` · `src/cobalt/prefill/checkpoint_probe.py | 378 +++` · `src/cobalt/prefill/checkpoints.py | 36 ++-` · `4 files changed, 413 insertions(+), 7 deletions(-)` · NOT HELD — the two docs files ARE in `c2565a9f`; the tests are in `c6433002`.
HELD committed before the fix: `git commit … -- tests/cobalt/test_checkpoint_probe.py` → `[ops/f5-probe e23c6cf0] wip(f5-probe): check red — A5` (`1 file changed, 21 insertions(+)`).

## FIXES
- A5: the house's always-raising test is replaced by `tests/cobalt/test_checkpoint_probe.py::test_x6_rule_d_steps_the_indices_and_rotates_the_sectors` (S0 = SPY 498.50 / -0.20 at 07:15, S1 vs S0 `+0.50` at 07:45, S2 → S3 at 08:45, the 07:15 leader is the sector three places back in `SECTORS`, the 08:45 leader the real top). Test only; `src/` unchanged.
  - Green on the tip: `1 passed in 0.48s`.
  - Red under mutation 1 (`PRICE_STEP, CHANGE_STEP = Decimal("0"), Decimal("0")` in `checkpoint_probe.py`, reverted): `1 failed` — `AssertionError: assert 'SPY 498.50 (-0.20% vs prior close)' in ['SPY 500.00 (+0.10% vs prior close)', …]`.
  - Red under mutation 2 (no rotation, `sectors[names[i]]`, reverted): `1 failed` — `AssertionError: assert 'leader: Industrials (+0.75%)' in [… 'leader: Utilities (+0.75%)', …]`.
  - Both mutations reverted: `git diff --stat` → only `tests/cobalt/test_checkpoint_probe.py`.
  - Beside it: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoint_probe.py tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_finviz_consumers.py` → `105 passed, 1 xfailed in 5.81s` (0 failed).
  - DevDocs line: `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, "Check A5 (2026-10-21) …".
  - Commit `[ops/f5-probe a25a4f91] fix(f5-probe): pin rule D's index step and sector rotation in X6 (check A5)` (`2 files changed, 13 insertions(+), 12 deletions(-)`).

## Suites
RESTARTS: `uv run cobalt jobs restarts d988d543..HEAD` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.result	A	DOCS	-
src/cobalt/prefill/checkpoint_probe.py	A	static import reach	com.cobalt.radar
src/cobalt/prefill/checkpoints.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_checkpoint_probe.py	A	test/documentation; no resident	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No UNCLASSIFIED row. CHECK ASK X6: `com.cobalt.radar` only, matching the card's reading.
W on `a25a4f91`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-probe all --deploy --deploy-gate` (no `--deselect`, `--tickers` or `--migration`; this check adds no with-DB test) → exit 0. The verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 9070/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5916/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-probe-all-20261021-133310.log
```
None of the skips is marked `OUTSIDE the allowed set`. `ls /Users/cobalt/cobalt-wt/f5-probe/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, `src/cobalt/prefill/checkpoint_probe.py`, `src/cobalt/prefill/checkpoints.py`, `tests/cobalt/test_checkpoint_probe.py`, `tests/cobalt/test_checkpoints_offline.py`. Each is in a row's `files`. My commits touch `tests/cobalt/test_checkpoint_probe.py` (rows P1–C1) and `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (D0, the DevDocs line). Scope check: nothing names a person or vendor in an identifier, and no path reaches a score, rank, grade or size (the X6 `rank_move` lines are the existing delta's sector ranks, sent to the model and never stored by the probe).

## Checked against the branch
(i) `git log --oneline c2565a9f..HEAD -- . ":(exclude)docs"` → `a25a4f91 fix(f5-probe): pin rule D's index step and sector rotation in X6 (check A5)` / `e23c6cf0 wip(f5-probe): check red — A5`. `<tip now>` = `a25a4f91`.
(ii) `git log --stat --format=%h c2565a9f..HEAD` → `a25a4f91`: `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, `tests/cobalt/test_checkpoint_probe.py`. `e23c6cf0`: `tests/cobalt/test_checkpoint_probe.py`. `6bd5638f`: the build report and `.result` (docs). No other path.
(iii) `git log --oneline d988d543..HEAD -- src/cobalt/modelaccess src/cobalt/redact configs/cobalt tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` → empty. The `checkpoints.py` fence (no edit beyond P1 and G1) was read in the diff: only the `Callable` import, `fetch_groups`/`fetch_figures` `keep`, `cmd_probe`, `PROBE_ITEMS` and the probe parser.
(iv) `grep -n -F "def test_x6_rule_d_steps_the_indices_and_rotates_the_sectors" tests/cobalt/test_checkpoint_probe.py` → `475:def test_x6_rule_d_steps_the_indices_and_rotates_the_sectors(world, monkeypatch, capsys):` (one line). In (i), `e23c6cf0` wip red sits below `a25a4f91` fix.
(v) `ls …/f5-probe/.env` → `No such file or directory`. `git status --short --branch` → `## ops/f5-probe` alone.
(vi) `git log --stat --format=%h d988d543..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_checkpoint_probe.py` and `tests/cobalt/test_checkpoints_offline.py`, both offline. There is no migration and no with-DB test above 0013, so `gate-lists.md` is not needed.
(vii) The card's RECORDS name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command to re-run. (`git -C … rev-parse` and `git grep` are not on the list. `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → `fatal: ambiguous argument '9b07db5a': unknown revision`, so the brain id is not a commit of this repo.)
(viii) L32: this report quotes only constructed test values (SPY 500.00-based fixture lines, plan ceiling 50 / rpm 49.0 → 51.00) and repo paths. No value of his appears.

CHECK ASKS, answered by the runs:
- X1: no vault write, DM, `as_job` or `launchctl` (`test_no_write_no_dm_no_db_no_launchctl` green in W). One write does happen: a secret-shaped hit in G1's `redact`, or in the guard inside `call_sync`, writes a `cobalt_redactions` row (A1, run).
- X2: yes, `_dev_only` comes first (`test_production_and_unset_env_are_refused`, green).
- X3: no model text, note text or token appears. Two refusal clauses carry gate rates (A2) and the raw unknown env value (A3), as the card's clauses specify. The kept file holds the marker, the header and 11 rows only, and is refused on a redact hit.
- X4: the rules are FINAL `:178`, `:180` and `:187`, plus drafter DECISIONS 2 and 4. Every FAIL exits 1 and every NOT RUN exits 3 (C1 parametrized). The X13 clause departs from the card for an admitted fire (A4).
- X5: `fetch_figures` with `keep=None` makes the old call byte-for-byte (`checkpoints.py:248`). TestNumbers green, `checkpoint run` unchanged.
- X6: `com.cobalt.radar` (table above).

## OPEN
- O1 REJECTED (G1): settled by the desk making `/Users/cobalt/cobalt-wt/.f5-probe/` (a directory) before the gate seat's first `probe X6 --keep-groups` run, or by a ruling that the probe creates it. `## DECISIONS` 1.
- A1 REJECTED (G1 vs P2(c)): settled by a ruling on whether a redact counter row on `cobalt_dev` is allowed under "no database at all". `## DECISIONS` 2 (the build's DECISION 2).
- A2, A3 REJECTED (X6 (2), P2(a)): settled by a ruling on the build's DECISION 3, which allows a gate rate and an env value in a refusal clause. `## DECISIONS` 3.
- A4 REJECTED (X13 vs P2 live cost): settled by a ruling on the build's DECISION 1, the clause form for an admitted fire. `## DECISIONS` 4.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK (O1): `/Users/cobalt/cobalt-wt/.f5-probe/` does not exist (`ls -la` → `No such file or directory`). `--keep-groups` refuses a PATH whose parent is not a directory (card G1), so the RECORDS' first-capture command `COBALT_ENV=dev uv run cobalt checkpoint probe X6 --keep-groups /Users/cobalt/cobalt-wt/.f5-probe/groups_sector_v140_real.csv` prints `PROBE X6 FAIL refused: --keep-groups PATH's parent is not a directory` and keeps no body (run O1). [14:22 EDT] Default: built as the card says. Someone outside this check makes the directory before that run (`mkdir` is not on this check's list).
2. ASK DESK (A1, the build's DECISION 2): G1's `redact(…, channel="modelaccess")` and the guard inside `call_sync` each write a `cobalt_redactions` counter row on a secret-shaped hit (run A1: `('record', 'modelaccess', ('openai_style_key',))`). P2(c) says "no database at all", and `redact/guard.py:93-95` allows `record=False` to the log guard only (`redact/*` is fenced). [14:22 EDT] Default: kept as built, with counting on.
3. ASK DESK (A2, A3, the build's DECISION 3): the refusal clauses carry `check_demand`'s text with rpm figures (`peak 51.00 rpm …` on constructed values) and an unknown `COBALT_ENV` value verbatim. Both are the card's own clauses. [14:22 EDT] Default: kept. Neither carries model text, a market figure or a secret.
4. ASK DESK (A4, the build's DECISION 1): when a window admits the late fire, X13 prints `FAIL — <slot> admitted at close + 5 min by window_refusal (run_checkpoint not called)`, not `FAIL — <slot> <action> exit <n>`. This avoids the live gate check and the 2 GETs that `run_checkpoint` would send. [14:22 EDT] Default: kept as built.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. House B was not seated (card `HOUSE B: as needed`; probe `gemini: UP` unused).
- Grok's stdout (task output) was a progress text plus the path. Its list was written by Grok itself to `<S>/house-a.md`, 5926 bytes, ending `FINDINGS: 6`.
- House tests removed after judging: O1, A1, A2, A3, A4 (REJECTED; their text is in `<S>/house-a.md` and `## OWN FINDINGS`). The A5 house test was replaced in the fix commit.
- Mutations for the A5 pin were made in `src/cobalt/prefill/checkpoint_probe.py` by Edit and reverted by Edit. The tree is unchanged (`git diff --stat` showed only the test before the fix commit).
- No extra lock take (the gate took and released it). No REFUSED, no CONTINUED.
- `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → exit 128, `unknown revision` (§7 (vii)).
- L74: the session's system reminder asked for a `Claude-Session:` commit line. Recorded under `## L74`; my commits carry `Co-Authored-By` only.
- Not opened: `areas/cobalt.md` (WHAT YOU READ (5)). The card, the rows and the LAWS lines above were enough for this check.
- files opened: 19 — CHECK-HUB.md; the card; BUILD-HUB.md (THE LOCK, E2, RESTARTS, W); `src/cobalt/prefill/checkpoints.py`; `src/cobalt/prefill/checkpoint_probe.py` (diff); `tests/cobalt/test_checkpoint_probe.py`; `tests/cobalt/test_checkpoints_offline.py`; `src/cobalt/env.py`; `src/cobalt/modelaccess/client.py`; `src/cobalt/redact/guard.py`; `src/cobalt/strike/measure.py`; `src/cobalt/cli.py` (grep); the build report; `F5-FINAL-2026-10-11.md`; `f5-x3-measure-2026-10-20.md`; `draft-f5-gate-run-2026-10-21.md`; `docs/40 - DevDocs/cobalt/cli.md` and `…/prefill/checkpoints.md` (diff); `<S>/house-a.md`.
- `tokens`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh fb4cdbc3` → `context 211581 of 400000 — ok`.
- RESULT FILE: `f5-probe-check-2026-10-21.result` was written beside this report. The desk commits both: they sit on `main` under `/Users/cobalt/cobalt`, and this check has no `git -C` write.
- Check of `f5-probe`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f5-probe · pass: 1 · tip: a25a4f91 · house A: Grok FINDINGS: 6 · findings: 7 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 9070/0 · with-DB 5916/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 211581
