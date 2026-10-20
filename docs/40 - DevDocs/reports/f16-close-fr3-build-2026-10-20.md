# f16-close-fr3 — build report (row PORT3) — 2026-10-20

## §0 Headline
PORT3 built: F16 close re-applied by Edit/Write onto main `4aa0481d`, tip `1aea7418`; 5 of 5 files byte-equal to the checked `6fb73789`.
Row suite `75 passed, 1 skipped`; gate offline `4790/0`, live-note `147/0`; with-DB left to the deploy gate (card).
Production `validate` smoke not typed (denied on this seat): ASK DESK 1. RESTARTS derived wider than the card: DECISION 2.

## L74
One block arrived as a system reminder at the start of this session asking that commit messages end with a `Claude-Session:` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md"` (02:04 EDT session start, `date`: `Tue Oct 20 02:04:54 EDT 2026`):

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 0 · 60efaf559903a7466a01ae1d20b0c679a3ac509a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 112:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| BASE | `git show --stat 4aa0481d` | 0 | `docs(desk): R2129-R2131 F16 attempt2 failed, 469 deployed, drafter 893` · `893-draft-f16-port3.md` +9, `cto-2026-10-20.md` 15 (+9 −6) · 2 files, 18 insertions, 6 deletions |
| port source set | `git diff --name-only cb4e42ce 6fb73789` | 0 | `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` (5, no report) |
| port source commits | `git log --oneline cb4e42ce..6fb73789` | 0 | `6fb73789 fix(f16-close-fr2): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT2; L1 L79)` |
| main drift over the five | `git diff --stat cb4e42ce 4aa0481d -- <the five>` | 0 | (empty) |
| net change to port | `git diff --stat 4aa0481d 6fb73789 -- <the five>` | 0 | cli.md +3, loader.md +6, cli.py +20, loader.py 8 (+7 −1), test file +125 · `5 files changed, 161 insertions(+), 1 deletion(-)` |
| symbol | `grep -n -F "def _cmd_validate" src/cobalt/cli.py` | 0 | `141:def _cmd_validate(args: argparse.Namespace) -> None:` |
| symbol | `grep -n -F "if disabled:" src/cobalt/cli.py` | 0 | `332:    if disabled:` |
| symbol | `grep -n -F "These are built and registered; their plists are not bootstrapped." src/cobalt/cli.py` | 0 | `337:        print("  These are built and registered; their plists are not bootstrapped.")` |
| symbol | `grep -n -F "CROSS-CHECK 1" src/cobalt/cli.py` | 0 | `339:    # CROSS-CHECK 1: the registry and ops/ name the same jobs. A registry` |
| symbol | `grep -n -F "def load_tunables" src/cobalt/taxonomy/loader.py` | 0 | `76:def load_tunables(path: Path = TUNABLES_PATH) -> TunableRegistry:` |
| callers | `grep -rn -F "load_tunables(" src` | 0 | 58 hits; every src caller calls `load_tunables()` on the engine file except `src/cobalt/strike/config.py:39` `load_tunables(path)`; vault_loader `:556`, `:598` use the engine registry; `src/cobalt/cli.py:250` inside validate (full list in the tool output, read at PREFLIGHT) |
| symbol | `grep -n -F "f21-genesis-1013" "docs/40 - DevDocs/cobalt/cli.md"` | 0 | `141:## 2026-10-19 — f21-genesis-1013` |
| symbol | `grep -n -F "## OFFLINE" -A 3 ops/desk/gate-lists.md` | 0 | `23:## OFFLINE` / `24-`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`` |
| sizes | `wc -l` | 0 | `595 src/cobalt/cli.py`, `246 src/cobalt/taxonomy/loader.py`, `142 docs/40 - DevDocs/cobalt/cli.md`, `119 docs/40 - DevDocs/cobalt/taxonomy/loader.md` (the test file is new) |
| restarts | `uv run cobalt jobs restarts 4aa0481d..HEAD` | 0 | only the untracked report `A DOCS -`; `RESTARTS: none` (empty code range) |

```
clock · date · 0 · Tue Oct 20 02:05:14 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f16-close-fr3
    ?? "docs/40 - DevDocs/reports/f16-close-fr3-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4aa0481d docs(desk): R2129-R2131 F16 attempt2 failed, 469 deployed, drafter 893
diff · git diff --stat 4aa0481d · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f16-close-fr3 · 0 · 4aa0481d docs(desk): R2129-R2131 F16 attempt2 failed, 469 deployed, drafter 893
env here · ls /Users/cobalt/cobalt-wt/f16-close-fr3/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card `## RECORDS` copied by reference (lines 82–97 of the card at `60efaf55`); re-read here: the PORT3 drafter's `git diff --stat cb4e42ce main -- <the five>` (empty) and `--stat main 6fb73789` (161 insertions, 1 deletion) — both re-run above, same result. `## READ` names no report (no `tail -n 3` owed).

Not a "DB: none" card, but row PORT3 runs no with-DB step: its suites are the four-file line, the DEPLOY PROOF greps, the bare validate and the `## OFFLINE` line; `## PASS 1` / `## PASS 2` stay the deploy gate's own (card PORT3 row). No lock is taken in this job.

## E0 BASELINE
On BASE `4aa0481d`, nothing edited:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4783 passed, 873 skipped, 4 xfailed, 36 warnings in 723.99s (0:12:03)` (exit 0).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.67s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Row PORT3's `red first` column: `none: a port; the proof is the PROOF lines and the suites`. No red written, no red commit. The ported tests' reds are shown by the E3 mutations.

## E3 THE ROWS
Row PORT3, by Edit/Write only (no merge, cherry-pick, rebase or revert): the `_cmd_validate` block added after `src/cobalt/cli.py:337` (`print("  These are built and registered; ...")`) and before `# CROSS-CHECK 1` (then `:339`); the `load_tunables` refusal in `src/cobalt/taxonomy/loader.py:84-93`; `tests/cobalt/test_f16_close_1018.py` written from `git show 6fb73789:tests/cobalt/test_f16_close_1018.py`; the two DevDocs sections appended. Commit `1aea7418 fix(f16-close-fr3): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT3; L1 L79)` (`5 files changed, 161 insertions(+), 1 deletion(-)`).

PROOF (one line per file of `git diff --name-only cb4e42ce 6fb73789`; main drift over the five since `cb4e42ce` is empty, PREFLIGHT):

PROOF: src/cobalt/cli.py — `git diff --stat 6fb73789 1aea7418 -- src/cobalt/cli.py` → empty (byte-equal)
PROOF: src/cobalt/taxonomy/loader.py — `git diff --stat 6fb73789 1aea7418 -- src/cobalt/taxonomy/loader.py` → empty (byte-equal)
PROOF: tests/cobalt/test_f16_close_1018.py — `git diff --stat 6fb73789 1aea7418 -- tests/cobalt/test_f16_close_1018.py` → empty (byte-equal)
PROOF: docs/40 - DevDocs/cobalt/cli.md — `git diff --stat 6fb73789 1aea7418 -- "docs/40 - DevDocs/cobalt/cli.md"` → empty (byte-equal)
PROOF: docs/40 - DevDocs/cobalt/taxonomy/loader.md — `git diff --stat 6fb73789 1aea7418 -- "docs/40 - DevDocs/cobalt/taxonomy/loader.md"` → empty (byte-equal)

- `git diff --stat 4aa0481d 1aea7418` → the five files only, `5 files changed, 161 insertions(+), 1 deletion(-)` (equals `git diff --stat 4aa0481d 6fb73789 -- <the five>` at PREFLIGHT). No report file of an old build in it.
- `git log --merges --oneline 4aa0481d..1aea7418` → empty.
- Seam hunks: none (main touched none of the five since `cb4e42ce`).

Row suite, after the port: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py tests/cobalt/test_validate_no_db.py tests/cobalt/test_strike_config.py tests/taxonomy/test_trade_defs.py` → `75 passed, 1 skipped, 15 warnings in 3.36s` (run before and after the mutations; same result).

MUTATIONS (made and undone with Edit, never committed):
1. `loader.py` blank-consumer line back to `keys = [row.key for row in registry.tunables if not row.consumers]` → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_f16_close_1018.py` → `1 failed, 6 passed in 1.14s`; first failing line `tests/cobalt/test_f16_close_1018.py:119: Failed: DID NOT RAISE <class 'cobalt.taxonomy.loader.TaxonomyConfigError'>` (`FAILED ...::test_c1_a_row_whose_consumers_are_blank_is_refused`). Undone.
2. `from cobalt.playbook import deck` added after the playbook config import in `_cmd_validate` → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_offline.py::test_walk_slide_counts tests/cobalt/test_f16_close_1018.py::test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` → `1 failed, 1 passed in 0.83s`; first failing line `tests/cobalt/test_f16_close_1018.py:63: AssertionError: assert 'pptx' not in {...} = sys.modules`. Undone; the first undo left `cfg =playbook_...` (a space lost), seen in `git diff 6fb73789 -- src/cobalt/cli.py`, fixed by Edit; then `git diff 6fb73789 --stat -- <the four tracked files>` → empty.

DEPLOY PROOF greps on the tip (worktree files, which equal `1aea7418`):
- `grep -c -F "Playbook (F23): " src/cobalt/cli.py` → `1`
- `grep -c -F "Daily refresh (F4): " src/cobalt/cli.py` → `1`
- `grep -c -F "with no consumer (F16)" src/cobalt/taxonomy/loader.py` → `1`
- `COBALT_ENV=production uv run cobalt validate`: NOT typed — `Bash(COBALT_ENV=production*)` is on this seat's deny list and BUILD-HUB names it "Never typed". ASK DESK 1 under `## DECISIONS`.

## RESTARTS
`uv run cobalt jobs restarts 4aa0481d..HEAD` (HEAD `1aea7418`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr3-build-2026-10-20.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. The derived set is wider than the card's `com.cobalt.radar` (DECISION 2).

## W THE THREE SUITES
`<tip>` = `1aea7418`. Per row PORT3 the gate pass of this job is the `## OFFLINE` line of `ops/desk/gate-lists.md`; `## PASS 1` / `## PASS 2` stay the deploy gate's own under the dev lock (this job touches no with-DB test and no migration). Run as the gate's offline and live-note modes:
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh f16-close-fr3 offline` (exit 0) → `tests/ops: skipped (no ops paths)` · `offline 4790/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr3-offline-20261020-022006.log`. Executed (`grep -n -F "uv run pytest" <log>`): `2:$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; summary `949:4790 passed, 873 skipped, 4 xfailed, 36 warnings in 708.43s (0:11:48)`. 4790 = E0's 4783 + the 7 tests of `tests/cobalt/test_f16_close_1018.py`.
- (b)–(d), (f) with-DB: not run (card row PORT3: the deploy gate's own). No lock taken; no migration applied; `.env` never present.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh f16-close-fr3 livenote` (exit 0) → `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr3-livenote-20261020-023208.log`. Executed: `2:$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py tests/cobalt/test_playbook_live.py`; `57:147 passed, 1 skipped, 15 warnings in 26.17s`; the skip `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## PRE-STOP SELF-CHECK
(1) Every ported test shown red: `test_c1_a_row_whose_consumers_are_blank_is_refused` under mutation 1 (`:119 DID NOT RAISE`); `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` under mutation 2 (`:63 assert 'pptx' not in ... sys.modules`). The other five were shown red in the original build and its checks (`reports/f16-close-1018-build-2026-10-18.md`, `reports/f16-close-1018-check-2026-10-19.md`); the port is byte-equal to the checked `6fb73789` (PROOF), so they are carried, not re-proved here.
(2) Entry paths: `load_tunables` callers (PREFLIGHT `grep -rn -F "load_tunables(" src`): every src caller reads the engine file, which loads (`test_c1_the_engine_registry_loads`, green); the one path-taking caller `src/cobalt/strike/config.py:39` is pinned by `tests/cobalt/test_strike_config.py` (row suite, green). `_cmd_validate`: `tests/cobalt/test_validate_no_db.py` and the four V tests (green).
(3) Re-read at the tip: the five PROOF `git diff --stat 6fb73789 1aea7418` calls, `git diff --stat 4aa0481d 1aea7418`, the three DEPLOY PROOF greps, the RESTARTS table, both gate logs by `grep -n -F`.

## FOR THE CHECK
- Range `4aa0481d..1aea7418`: one commit, `1aea7418 fix(f16-close-fr3): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT3; L1 L79)`. No merge commit (`git log --merges` empty).
- PROOF: 5 of 5 files byte-equal to `6fb73789` (`## E3`).
- FIX1 ids, carried byte-equal from the checked tip:
FIXED: O1 — tests/cobalt/test_f16_close_1018.py::test_c1_a_row_whose_consumers_are_blank_is_refused
FIXED: O2 — tests/cobalt/test_f16_close_1018.py::test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded
- Mutations, row suite, DEPLOY PROOF greps: `## E3`. Suites and logs: `## W`. RESTARTS table: `## RESTARTS`.
- `<F0>` / `<F1>` / `<F2>`, lock times: not run (no with-DB step in row PORT3).
- P5 MERGE BASE: not run by the builder (the check seat and the desk record it).

## CONTINUE
next: CLOSE (done at 02:32 EDT)

## DECISIONS
1. ASK DESK 1: row PORT3 and `## DEPLOY PROOF` ask for `COBALT_ENV=production uv run cobalt validate`; this seat denies `Bash(COBALT_ENV=production*)` and BUILD-HUB lists it as never typed, so it was not run. Safe default taken: the smoke read stays the deploy hub's (on its launch line, `prompts/DEPLOY-HUB.md:11`); here the lines are shown by `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` and `test_v2_validate_prints_the_daily_refresh_line`, which run `_cmd_validate` on the real config files (green).
2. DECISION RESTARTS: the card expects `com.cobalt.radar`; the derived table at `1aea7418` reads `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`src/cobalt/taxonomy/loader.py` now reaches `aset` and `cos` as well). Safe default: the derived table stands in the stop line (L42); the deploy card's `RESTARTS:` comes from it.

## RECORDS
- Launch message carried `CONTINUE: PORT.`; no report and no commit existed on the branch (`git status --short --branch` → `## ops/f16-close-fr3`; `git log --oneline -3` → `4aa0481d` at top; `.env` → No such file), so the run began at AUTHORIZATION on BASE.
- With-DB passes not run and no lock taken, per row PORT3; `.env` never in this worktree.
- Mutation 2's undo first left one lost space (`cfg =playbook_config...`); caught by `git diff 6fb73789`, fixed by Edit before the commit.
- Old branches `ops/f16-close-fr1`, `ops/f16-close-fr2` and their worktrees not touched.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f16-close-fr3 · tip: 1aea7418 | on 4aa0481d | migration: none | offline 4790/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (PORT3; PROOF 5 of 5 byte-equal) | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 126090
