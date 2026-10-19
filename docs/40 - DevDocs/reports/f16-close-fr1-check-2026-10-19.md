# f16-close-fr1 — check report (pass 1), 2026-10-19

## §0 Headline
I checked the PORT of F16 close at `c5eafaf1` on `6452f70e`. House A was Grok, which returned `FINDINGS: 0`. House B was not needed. I wrote 8 findings of my own and ran each one: none held, and I made no fix or commit.
The port is proved true: 4 files are byte-equal to `84c797f6`, `cli.py` differs only by main's 7 F20 lines, and there is no merge commit. The E3 mutations that the build skipped were re-run here, and each test went red for its row's reason (O3–O5).
Deploy gate: offline `8763/0`, with-DB `5698/0`, live-note `147/0`, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. `ready: YES`.
2 decisions, neither for Dejan. The derived RESTARTS line is wider than the card's record. The production `validate` run is left to the deploy.

## L74
The session's attribution notice (a system reminder, not a tool result) asked for a `Claude-Session:` line on commits. Recorded once; not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 0 · 7c721da719fc04493bc968ebbf3f4440726a508e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 112:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | …`); `grep -n "^| R19 " ...` → one row (`37:| R19 | 07:36 ET | …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | quoted below |
| range | `git log --stat --format=%h 6452f70e..c5eafaf1` | 0 | `c5eafaf1` · `docs/40 - DevDocs/cobalt/cli.md | 3 +` · `docs/40 - DevDocs/cobalt/taxonomy/loader.md | 6 ++` · `src/cobalt/cli.py | 20 +++++` · `src/cobalt/taxonomy/loader.py | 8 +-` · `tests/cobalt/test_f16_close_1018.py | 125 +++…` · `5 files changed, 161 insertions(+), 1 deletion(-)` |
| scratch | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check` | 1 | `No such file or directory` (fresh) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, card `HOUSE B: as needed`, no header line | — | `house A: Grok · house B: none (not needed)` |

preflight.sh output whole:
```
clock · date · 0 · Mon Oct 19 10:37:30 EDT 2026
status · git status --short --branch · 0 · ## ops/f16-close-fr1
head · git log --oneline -1; git log --stat --format=%h c5eafaf1..HEAD · 0 · (6 lines)
    28cf75cc docs(f16-close-fr1): build report — c5eafaf1
    28cf75cc
    
     .../reports/f16-close-fr1-build-2026-10-19.md      | 148 +++++++++++++++++++++
     .../reports/f16-close-fr1-build-2026-10-19.result  |  15 +++
     2 files changed, 163 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f16-close-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f21-genesis-fr1/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/f16-close-fr1/docs/40 - DevDocs/reports/f16-close-fr1-build-2026-10-19.md" · 0 · BUILT · job: f16-close-fr1 · tip: c5eafaf1 | on 6452f70e | migration: none | offline 4737/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (PROOF 5 of 5) | self-check: 2 of 3 | decisions: 4 · for Dejan: 0 · tokens: 116212
report: self-check 2 of 3 (recorded)
range · git log --oneline 6452f70e..c5eafaf1 · 0 · c5eafaf1 fix(f16-close-fr1): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT; V1 V2 C1 FIX1 SEAM; L1 L79)
PREFLIGHT OK
```
Self-check `2 of 3` is recorded and goes to the house as a fact. Another worktree (`f21-genesis-fr1`) holds `.env`: the lock is held by another job; this check waits for it at W.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, output whole:
```
22 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/STAGED-CARD
7585 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/diff.md
28737 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/790-f16-close-card.md
19277 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/f16-close-fr1-build-2026-10-19.md
7315 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/wt/docs/40 - DevDocs/cobalt/cli.md
6900 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/wt/docs/40 - DevDocs/cobalt/taxonomy/loader.md
27106 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/wt/src/cobalt/cli.py
10190 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/wt/src/cobalt/taxonomy/loader.py
4592 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/files/wt/tests/cobalt/test_f16_close_1018.py
384 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/rulings.md
STAGED 10 files · 112108 bytes · commits 1
```
`commits 1` = PREFLIGHT's range count (1). Added by `stage-copy.sh`, each `COPIED <bytes> <dest>`:
- `f16-close-1018-check-2026-10-19.md` (from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`) → `COPIED 33717`
- `f16-close-1018-build-2026-10-18.md`: from main's reports folder → `REFUSED: no such plain file: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-1018-build-2026-10-18.md` (the file was never on main: the PORT row does not port it); copied from the old worktree `/Users/cobalt/cobalt-wt/f16-close-1018/docs/40 - DevDocs/reports/` (read only) → `COPIED 31929`
- `wt/src/cobalt/playbook/config.py` → `COPIED 2043`; `wt/src/cobalt/playbook/cli.py` → `COPIED 6776`; `wt/src/cobalt/prefill/config.py` → `COPIED 8305`; `wt/src/cobalt/taxonomy/tunables.py` → `COPIED 4920`; `wt/tests/cobalt/test_validate_no_db.py` → `COPIED 5136`; `wt/tests/cobalt/test_playbook_offline.py` → `COPIED 18896`; `wt/docs/00 - Project/MVP-CHARTER-v0_2.md` → `COPIED 29164`; `wt/docs/00 - Project/SPRINT-LADDER-v0_1.md` → `COPIED 157329`
- `<S>/HOUSE-INSTRUCTIONS.md` written (Write): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, two facts (self-check `2 of 3`; the derived RESTARTS line), and the Files paragraph. `ls -la <S>` at 10:40 → `HOUSE-INSTRUCTIONS.md` 30874 bytes.

## OWN FINDINGS
Written 10:4x EDT, before either house list was opened.

FINDING O1
ROW: PORT (P1, P2)
CLAIM: The port differs from `84c797f6` in more than main's F20 lines in `src/cobalt/cli.py:87-89` and the F20 registrations; the four other ported files are not byte-equal to `84c797f6`.
RUN: COMMAND `git diff --stat 84c797f6 c5eafaf1 -- src/cobalt/cli.py src/cobalt/taxonomy/loader.py tests/cobalt/test_f16_close_1018.py "docs/40 - DevDocs/cobalt/cli.md" "docs/40 - DevDocs/cobalt/taxonomy/loader.md"` and `git diff 84c797f6 c5eafaf1 -- src/cobalt/cli.py`
EXPECT: if true, a path other than `src/cobalt/cli.py` in the stat, or a hunk in `src/cobalt/cli.py` other than the three F20 imports and the F20 comment plus three `add_parser(sub)` lines.

FINDING O2
ROW: PORT (P1)
CLAIM: The branch carries a merge commit, or an old report file of `s5/f16-close-1018`, in `6452f70e..HEAD`.
RUN: COMMAND `git log --merges --oneline 6452f70e..HEAD` and `git diff --name-only 6452f70e c5eafaf1`
EXPECT: if true, a merge line, or `f16-close-1018-build-2026-10-18.md` / `.result` among the names.

FINDING O3
ROW: V1, V2 (content of PORT; self-check gap, build DECISION 4)
CLAIM: On this ported tree the V1 and V2 refusal and control tests (`tests/cobalt/test_f16_close_1018.py:102`, `:117`, `:133`, `:146`) were never shown red; with the `_cmd_validate` block of `src/cobalt/cli.py:338-356` removed some of them may stay green.
RUN: COMMAND (with the block `src/cobalt/cli.py:338-356` removed by Edit, then restored) `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py`
EXPECT: if true, fewer than 4 failed under the mutation (each of the 4 V tests should fail: 2 `DID NOT RAISE`, 2 at the `startswith` assert).

FINDING O4
ROW: C1, FIX1 (content of PORT; X6)
CLAIM: On this ported tree the two C1 refusal tests (`tests/cobalt/test_f16_close_1018.py:152`, `:174`) were never shown red; with `src/cobalt/taxonomy/loader.py:88-92` removed one may stay green, and with `:88` reverted to `if not row.consumers` the blank-consumer test may stay green.
RUN: COMMAND (each mutation by Edit, then restored) `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py`
EXPECT: if true, under the first mutation fewer than 2 failed; under the second, `test_c1_a_row_whose_consumers_are_blank_is_refused` passes.

FINDING O5
ROW: FIX1 (X7)
CLAIM: On this tree `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` (`tests/cobalt/test_f16_close_1018.py:117`) stays green under the deck-import mutation when `test_walk_slide_counts` runs first.
RUN: COMMAND (with `from cobalt.playbook import deck  # noqa: F401` added after `src/cobalt/cli.py:342`, then removed) `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_offline.py::test_walk_slide_counts tests/cobalt/test_f16_close_1018.py::test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded`
EXPECT: if true, `2 passed`; if false, `1 failed, 1 passed` at `assert "pptx" not in sys.modules`.

FINDING O6
ROW: P4, PORT (the card's offline suite)
CLAIM: The card's four-file suite is not `0 failed` on the tip.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py tests/cobalt/test_validate_no_db.py tests/cobalt/test_strike_config.py tests/taxonomy/test_trade_defs.py`
EXPECT: if true, a `failed` count above 0.

FINDING O7
ROW: P4 (DEPLOY PROOF greps)
CLAIM: One of the three DEPLOY PROOF strings is not exactly once in its file at the tip.
RUN: COMMAND `grep -c -F "Playbook (F23): " src/cobalt/cli.py`, `grep -c -F "Daily refresh (F4): " src/cobalt/cli.py`, `grep -c -F "with no consumer (F16)" src/cobalt/taxonomy/loader.py`
EXPECT: if true, a count other than `1`.

FINDING O8
ROW: X3
CLAIM: A caller of `load_tunables` passes a file other than the engine registry whose rows may lack consumers.
RUN: COMMAND `grep -rn -F "load_tunables(" src tests`
EXPECT: if true, a call with an argument other than the engine path, a tmp file of these tests or `strike/config.py:39` (whose `path` defaults to `TUNABLES_PATH`, `src/cobalt/strike/config.py:36`).

## Findings
House A Grok: notice 10:49 EDT (`date`); `ls -la <S>` → `house-a.md` 12 bytes; its content whole: `FINDINGS: 0`. Grok's stdout ended with the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f16-close-fr1-check/house-a.md` and `[exited with code 0]`. No finding block: nothing kept.
House B: none (not needed; card `HOUSE B: as needed`).

## Dropped
none (house A wrote no finding block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `git diff --stat 84c797f6 c5eafaf1 -- <the 5 files>`; `git diff 84c797f6 c5eafaf1 -- src/cobalt/cli.py` | stat: `src/cobalt/cli.py | 7 +++++++` · `1 file changed, 7 insertions(+)`; the diff: `@@ -84,6 +84,9 @@` adds `from cobalt.cos import cli as cos_cli`, `from cobalt.hitl import cli as hitl_cli`, `from cobalt.agents import cli as agents_cli`; `@@ -566,6 +569,10 @@` adds `# F20 C4d: read and dry-run only; no approve subcommand (F-21).`, `cos_cli.add_parser(sub)`, `agents_cli.add_parser(sub)`, `hitl_cli.add_parser(sub)`. Nothing else | NOT HELD |
| O2 | opus-own | `git log --merges --oneline 6452f70e..HEAD`; `git diff --name-only 6452f70e c5eafaf1` | empty; the five ported names only (`docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py`) | NOT HELD |
| O3 | opus-own | block `src/cobalt/cli.py:338-356` removed by Edit (the comment kept); `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_f16_close_1018.py` | `4 failed, 3 passed in 1.74s`; first lines: `:46: Failed: DID NOT RAISE any of (… ValidationError …, … PlaybookConfigError …, … SystemExit …)`, `:62: assert False` (the `Playbook (F23): ` line), `:75: Failed: DID NOT RAISE any of (… PrefillConfigError …, … SystemExit …)`, `:82: assert False` (the `Daily refresh (F4): ` line). Restored by Edit; `git diff --stat c5eafaf1 -- src/cobalt/cli.py` → empty | NOT HELD (each V test red for its row's reason) |
| O4 | opus-own | (a) `src/cobalt/taxonomy/loader.py:88-92` removed by Edit; (b) `:88` set to `if not row.consumers`; the same pytest line each time | (a) `2 failed, 5 passed in 1.21s`: `:103: Failed: DID NOT RAISE <class 'cobalt.taxonomy.loader.TaxonomyConfigError'>`, `:119: Failed: DID NOT RAISE …`; (b) `1 failed, 6 passed in 1.21s`: `:119: Failed: DID NOT RAISE <class 'cobalt.taxonomy.loader.TaxonomyConfigError'>` (the blank-consumer test). Restored by Edit; `git diff --stat c5eafaf1 -- src/cobalt/taxonomy/loader.py` → empty | NOT HELD |
| O5 | opus-own | `from cobalt.playbook import deck  # noqa: F401` added after the playbook config import by Edit; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_offline.py::test_walk_slide_counts tests/cobalt/test_f16_close_1018.py::test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` | `1 failed, 1 passed in 0.94s`; `tests/cobalt/test_f16_close_1018.py:63: AssertionError: assert 'pptx' not in {…} = sys.modules`. Removed by Edit; one space the undo dropped (`cfg =playbook_config…`) was put back by Edit; `git diff --stat c5eafaf1 -- src tests` → empty | NOT HELD |
| O6 | opus-own | `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py tests/cobalt/test_validate_no_db.py tests/cobalt/test_strike_config.py tests/taxonomy/test_trade_defs.py` | `75 passed, 1 skipped, 15 warnings in 3.57s` | NOT HELD |
| O7 | opus-own | the three `grep -c -F` | `1`, `1`, `1` | NOT HELD |
| O8 | opus-own | `grep -rn -F "load_tunables(" src tests` | every call takes no argument (the engine file `TUNABLES_PATH`) except the def `src/cobalt/taxonomy/loader.py:76`, `src/cobalt/strike/config.py:39` (`load_tunables(path)`, `path` defaults to `TUNABLES_PATH` at `:36`) and the two tmp files of `tests/cobalt/test_f16_close_1018.py:104`, `:120`. `vault_loader.py:556`, `:598` load the engine file and merge vault rows through `merge_tunables`, which `load_tunables` never sees | NOT HELD |

Mutation output lines that carried config values of the real files are not quoted (L32).

## FIXES
none (nothing held).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 6452f70e..c5eafaf1` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No UNCLASSIFIED row; no commit of mine, so the gate ran on the build's tip `c5eafaf1`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f16-close-fr1 all --deploy --deploy-gate` (started 10:51, notice by 11:39 EDT) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8763/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5698/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr1-all-20261019-105126.log
```
`grep -n -F "OUTSIDE the allowed set" <log>` → nothing. The `COBALT_LIVE_VAULT_ROOT` skips are pass 1's; the live-note run covers them (`live-note 147/0`).
- offline `8763/0` · with-DB `5698/0` · live-note `147/0` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`; `ls /Users/cobalt/cobalt-wt/f16-close-fr1/.env` → `No such file or directory` (11:39).
- New tests of this check: none (nothing held).

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` (all five in row PORT's `files`). Commits of this check: none.

## Checked against the branch
- (i) `git log --oneline c5eafaf1..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `c5eafaf1`.
- (ii) `git log --stat --format=%h c5eafaf1..HEAD` → `28cf75cc`: `.../reports/f16-close-fr1-build-2026-10-19.md | 148`, `.../reports/f16-close-fr1-build-2026-10-19.result | 15` (docs only).
- (iii) `git log --oneline 6452f70e..HEAD -- src/cobalt/taxonomy/tunables.py src/cobalt/taxonomy/vault_loader.py src/cobalt/taxonomy/store.py configs/cobalt/taxonomy/tunables.yaml configs/cobalt/playbook.yaml configs/cobalt/prefill.yaml src/cobalt/playbook src/cobalt/prefill src/cobalt/classify ops` → empty (the fence untouched; X1: no config value changed).
- (iv) no held finding.
- (v) `ls <WT>/.env` → "No such file"; `git status --short --branch` → `## ops/f16-close-fr1` alone.
- (vi) `git log --stat --format=%h 6452f70e..HEAD -- src/cobalt/db_migrations tests/cobalt` → `c5eafaf1`: `tests/cobalt/test_f16_close_1018.py | 125` only, an offline test file; no migration, no with-DB test above `0013`: no gate-list change owed.
- (vii) card `## RECORDS` greps re-run: `grep -c "^  - key:" configs/cobalt/taxonomy/tunables.yaml` → `100`; `grep -c "^    consumers:" …` → `100` (the record says `94` / `94`, read on an older main; main gained rows with F20; the counts still match, and `test_c1_the_engine_registry_loads` loads all of them green). `git -C /Users/cobalt/cobalt log --oneline -1 main` → `f1aea317 docs(desk): Genesis port check report f21-genesis-fr1, ready YES`.
- (viii) L32: no value of his is quoted; the mutation outputs that printed config values were not copied.
- CHECK ASKS: P1 = O1, O2 (true); P2 = O1 plus `git diff 6452f70e c5eafaf1 -- "docs/40 - DevDocs/cobalt/cli.md"` (main's `## 2026-10-18 — f20-cos-1018` section kept, F16's three lines added after it, nothing removed); P3 = O4, O5, and the test at `tests/cobalt/test_f16_close_1018.py:117-130` has no `pptx_loaded` skip; P4 = O6, O7, the gate above. RESTARTS is NOT `com.cobalt.radar` alone: the derived line names `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (DECISION 1). The production `validate --no-db` is not typed here (`Bash(COBALT_ENV=production*)` is denied) (DECISION 2). X2/X4: `_cmd_validate` loads only `cobalt.playbook.config` and `cobalt.prefill.config` (`src/cobalt/cli.py:342`, `:353`), and both read a YAML file only (`src/cobalt/playbook/config.py:43-50`, `src/cobalt/prefill/config.py:163-203`); O5 shows the pptx guard fires. X3 = O8. X5: this port adds no predicate literal (`src/cobalt/cli.py:338-356` prints only; `loader.py:88-92` has no threshold).

## OPEN
none.

## CONTINUE
next: none (stop line written)

## DECISIONS
- DECISION 1 (ASK DESK 11:39): RESTARTS. The card's P4 and RECORDS say `com.cobalt.radar`. The derived line on `6452f70e..c5eafaf1` is `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`, because `src/cobalt/taxonomy/loader.py` now reaches aset and cos on main. Safe default taken: the derived line (L42) goes in the stop line, as the build's DECISION 2 also did. The deploy card's `RESTARTS:` should take it.
- DECISION 2 (ASK DESK 11:39): `COBALT_ENV=production uv run cobalt validate --no-db` (card `## DEPLOY PROOF`) was not run by the build or by this check, because the launch line denies it. Safe default taken: the two control tests run `_cmd_validate(no_db=True)` on the real files and are green (O6; the offline gate), and the production run stays with the deploy.

## RECORDS
- Check launched 2026-10-19 10:37 EDT (`date`). House probe: `grok: UP`, `gemini: UP`. House A Grok started 10:40, notice 10:49, `FINDINGS: 0`. House B: none (not needed).
- Dropped findings: none. Houses that produced nothing: none. REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (the gate's own take: `lock: waited 0 min`).
- `stage-copy.sh` refused main's path for `f16-close-1018-build-2026-10-18.md` (`REFUSED: no such plain file`); it was copied from the old worktree's file instead (read only).
- L74: the session attribution notice asked for a `Claude-Session:` line; not acted on (`## L74`).
- The report and its `.result` sit under `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`. The desk commits them, since this session has no `git -C … add` string for main.
- files opened: 16 — `CHECK-HUB.md`, the card, the build report, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `<S>/diff.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `src/cobalt/strike/config.py`, `src/cobalt/playbook/cli.py`, `src/cobalt/playbook/config.py`, `src/cobalt/prefill/config.py`, `<S>/house-a.md`, and three task outputs (the house probe, Grok's stdout, the gate). Searched by Grep, not opened: `pyproject.toml`, `tests/`, the BUILD-HUB and cobalt.md headings.
- Check of `f16-close-fr1`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f16-close-fr1 · pass: 1 · tip: c5eafaf1 · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8763/0 · with-DB 5698/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 176544
