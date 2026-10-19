# f16-close-fr2 — build report (PORT2), 2026-10-19

## §0 Headline
PORT2 is built: F16's net change (`6452f70e..c5eafaf1`) is re-applied by Edit/Write on main `cb4e42ce`, tip `6fb73789`, no merge commit.
PROOF 5: `loader.py`, the test file and `loader.md` are byte-equal to `c5eafaf1`; `cli.py` and `cli.md` differ only by main's Genesis lines.
Card suite `75 passed, 1 skipped`; gate offline 4756/0; live-note 147/0; DEPLOY PROOF greps `1`, `1`, `1`.
The with-DB suite is left to the deploy gate (card ASK DESK 1). `COBALT_ENV=production … validate` is denied on this line: DECISION 1.

## L74
A system block asked commits to carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md" · 0 · 5031a022aee15f8a7cbb352112239c5a69537c8d
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
Session start (launch message carried `CONTINUE: PORT2`; no report existed, so the run began at AUTHORIZATION): `git status --short --branch` → `## ops/f16-close-fr2`; `git log --oneline -3` → `cb4e42ce`, `b742be67`, `abaf32b6`; `ls -la …/f16-close-fr2/.env` → No such file; `date` → `Mon Oct 19 12:35:35 EDT 2026`.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 19 12:35:44 EDT 2026
status · git status --short --branch · 0 · ## ops/f16-close-fr2
head · git log --oneline -1 · 0 · cb4e42ce docs(desk): draft prompt 858 f16 port2 (fresh job f16-close-fr2, brain)
diff · git diff --stat cb4e42ce · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f16-close-fr2 · 0 · cb4e42ce docs(desk): draft prompt 858 f16 port2 (fresh job f16-close-fr2, brain)
env here · ls /Users/cobalt/cobalt-wt/f16-close-fr2/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat cb4e42ce` | 0 | `docs(desk): draft prompt 858 f16 port2 (fresh job f16-close-fr2, brain)`; `docs/40 - DevDocs/prompts/2026-10-19/858-draft-f16-port2.md | 9 +++++++++` |
| RESTARTS empty | `uv run cobalt jobs restarts cb4e42ce..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |
| port set | `git diff --name-only 6452f70e c5eafaf1` | 0 | `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` (5, no report) |
| one commit | `git log --oneline 6452f70e..c5eafaf1` | 0 | `c5eafaf1 fix(f16-close-fr1): port F16 close onto main — …` only |
| main touched | `git diff --stat 6452f70e cb4e42ce -- <the 5>` | 0 | `cli.md | 3 +++`, `src/cobalt/cli.py | 2 ++`; the other 3 untouched |
| main since BASE | `git -C /Users/cobalt/cobalt log --oneline -1 main` | 0 | `6aeb289c docs(desk): f16 port2 builder launched R2053` |
| main since BASE, the 5 | `git diff --stat cb4e42ce main -- <the 5>` | 0 | nothing |
| seam (1)(2) | `git diff 6452f70e cb4e42ce -- src/cobalt/cli.py` | 0 | `@@ -87,6 +87,7 @@` `+from cobalt.genesis import cli as genesis_cli  # noqa: E402`; `@@ -553,6 +554,7 @@` `+    genesis_cli.add_parser(sub)` |
| seam (3) | `git diff 6452f70e c5eafaf1 -- src/cobalt/cli.py` | 0 | `@@ -335,6 +335,26 @@`: the F16 block, 20 added lines, before `# CROSS-CHECK 1` |
| seam (4) | `git diff 6452f70e cb4e42ce -- cli.md` | 0 | `@@ -137,3 +137,6 @@` `+## 2026-10-19 — f21-genesis-1013` and its line |
| anchor | `grep -n -F "CROSS-CHECK 1" src/cobalt/cli.py` | 0 | `339:    # CROSS-CHECK 1: the registry and ops/ name the same jobs. A registry` |
| symbol | `grep -n -F "def load_tunables" src/cobalt/taxonomy/loader.py` | 0 | `76:def load_tunables(path: Path = TUNABLES_PATH) -> TunableRegistry:` |
| sizes | `wc -l` of the 4 existing files | 0 | `595 src/cobalt/cli.py`, `246 src/cobalt/taxonomy/loader.py`, `142 …/cobalt/cli.md`, `119 …/taxonomy/loader.md` |

Card `## RECORDS` copied by reference (card `:74-89`); re-read here: the 5-file set, the one commit, main's 2-file touch, the genesis hunks and the `CROSS-CHECK 1` anchor `:339` all hold as the PORT2 drafter recorded.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `cb4e42ce` → `4749 passed, 871 skipped, 4 xfailed, 36 warnings in 759.62s (0:12:39)` (exit 0). Its two `COBALT_LIVE_VAULT_ROOT not set` skips (`test_catalyst.py:365`, `test_predicate.py:262`) belong to the offline run; the live-note run below covers them.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.04s`; the one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
PORT2's `red first` is `none: a port; the proof is the PROOF lines and the suites`. No red written and no red commit. The tests are ported, already checked at `c5eafaf1`. Their reds are shown under mutation at E3.

## E3 THE ROWS
PORT2 was re-applied by Edit/Write only (no merge, cherry-pick or rebase), reading `git diff 6452f70e c5eafaf1` and `git show c5eafaf1:tests/cobalt/test_f16_close_1018.py`. Commit `6fb73789 fix(f16-close-fr2): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT2; L1 L79)`, 5 files, `161 insertions(+), 1 deletion(-)`.

PROOF (one line per file of `git diff --name-only 6452f70e c5eafaf1`):
- PROOF A1 `src/cobalt/taxonomy/loader.py`: `git diff --stat 6452f70e cb4e42ce` is empty for it, and so is `git diff --stat c5eafaf1 6fb73789` → byte-equal to `c5eafaf1`.
- PROOF A2 `tests/cobalt/test_f16_close_1018.py`: main untouched; `git diff --stat c5eafaf1 6fb73789` is empty → byte-equal.
- PROOF A3 `docs/40 - DevDocs/cobalt/taxonomy/loader.md`: main untouched; `git diff --stat c5eafaf1 6fb73789` is empty → byte-equal.
- PROOF B1 `src/cobalt/cli.py`: `git diff --stat c5eafaf1 6fb73789` → `2 ++`. `git diff c5eafaf1 -- src/cobalt/cli.py` shows only `+from cobalt.genesis import cli as genesis_cli  # noqa: E402` (hunk `@@ -87,6 +87,7 @@`) and `+    genesis_cli.add_parser(sub)` (hunk `@@ -573,6 +574,7 @@`): main's seam hunks (1) and (2). F16's `_cmd_validate` block (seam 3) sits between `print("  These are built and registered; their plists are not bootstrapped.")` and `# CROSS-CHECK 1`, exactly as in `c5eafaf1`.
- PROOF B2 `docs/40 - DevDocs/cobalt/cli.md`: `git diff --stat c5eafaf1 6fb73789` → `3 +++`, which is main's Genesis section (blank line, `## 2026-10-19 — f21-genesis-1013`, its line). `git diff main -- "docs/40 - DevDocs/cobalt/cli.md"` (pre-commit) → hunk `@@ -140,3 +140,6 @@`, only the blank line, `+## 2026-10-19 — f16-close-1018` and its one line added; no main line removed.
- PROOF count: 5 (3 byte-equal, 2 seam files). `git log --merges cb4e42ce..HEAD` is empty. `git diff --stat cb4e42ce 6fb73789` → the 5 files only (`cli.md` 3, `loader.md` 6, `cli.py` 20, `loader.py` 8 +-, the test file 125), so no report from the old job is ported.

Card suite, after the port: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_f16_close_1018.py tests/cobalt/test_validate_no_db.py tests/cobalt/test_strike_config.py tests/taxonomy/test_trade_defs.py` → `75 passed, 1 skipped, 15 warnings in 3.51s`. It ran again after both mutations were undone → `75 passed, 1 skipped, 15 warnings in 3.48s`.

MUTATIONS (Edit only, each undone with Edit):
- M1 (FIX1 / O1): `loader.py` refusal line set back to `if not row.consumers]`. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_f16_close_1018.py` → `1 failed, 6 passed in 1.20s`; first failing line `/Users/cobalt/cobalt-wt/f16-close-fr2/tests/cobalt/test_f16_close_1018.py:119: Failed: DID NOT RAISE <class 'cobalt.taxonomy.loader.TaxonomyConfigError'>` (`test_c1_a_row_whose_consumers_are_blank_is_refused`). Undone; `git diff c5eafaf1 -- src/cobalt/taxonomy/loader.py` → empty.
- M2 (FIX1 / O2): `from cobalt.playbook import deck` added after the playbook config import in `_cmd_validate`. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_playbook_offline.py::test_walk_slide_counts tests/cobalt/test_f16_close_1018.py::test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` → `1 failed, 1 passed in 0.86s`; first failing line `/Users/cobalt/cobalt-wt/f16-close-fr2/tests/cobalt/test_f16_close_1018.py:63: AssertionError: assert 'pptx' not in {…} = sys.modules`. Undone. The first undo dropped a space (`cfg =playbook_config…`), and `git diff c5eafaf1 -- src/cobalt/cli.py` showed it. I fixed it with Edit; `git diff --stat c5eafaf1 -- src/cobalt/cli.py` → `2 ++` (the genesis lines only).

DEPLOY PROOF greps on the worktree after the port: `grep -c -F "Playbook (F23): " src/cobalt/cli.py` → `1`; `grep -c -F "Daily refresh (F4): " src/cobalt/cli.py` → `1`; `grep -c -F "with no consumer (F16)" src/cobalt/taxonomy/loader.py` → `1`.

`COBALT_ENV=production uv run cobalt validate --no-db` was not run: `Bash(COBALT_ENV=production*)` is on this launch line's deny list, and BUILD-HUB says it is never typed. See DECISION 1.

## RESTARTS
`uv run cobalt jobs restarts cb4e42ce..HEAD` at `6fb73789` (whole):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/loader.md	M	DOCS	-
docs/40 - DevDocs/reports/f16-close-fr2-build-2026-10-19.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_f16_close_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No UNCLASSIFIED row. The derived set is wider than the card's `com.cobalt.radar`: on main at BASE, `loader.py` is also in the static import reach of `com.cobalt.aset` and `com.cobalt.cos` (L42: derived, not predicted). See RECORDS.

## W THE THREE SUITES
The card's PORT2 row sets the suites: FIX1's four-file line, the DEPLOY PROOF, and the gate's `## OFFLINE` line. The with-DB passes stay the deploy gate's own, under the dev lock (card ASK DESK 1: this job touches no with-DB test and no migration). The lock was not taken.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh f16-close-fr2 offline` → exit 0:
```
tests/ops: skipped (no ops paths)
offline 4756/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr2-offline-20261019-125045.log
```
  Log `:947` → `4756 passed, 871 skipped, 4 xfailed, 36 warnings in 733.45s (0:12:13)`; `grep -n -F "OUTSIDE the allowed set"` on the log → nothing. 4756 = E0's 4749 + the 7 tests of `tests/cobalt/test_f16_close_1018.py`.
- with-DB: not run (card ASK DESK 1; the deploy gate's PASS 1 / PASS 2). `<F0>`/`<F1>`/`<F2>`: not run. Lock: not taken.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh f16-close-fr2 livenote` → exit 0:
```
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f16-close-fr2-livenote-20261019-130312.log
```
  Log `:57` → `147 passed, 1 skipped, 15 warnings in 27.21s`; `grep -n -F "COBALT_LIVE_VAULT_ROOT not set"` on the log → nothing.
- `ls /Users/cobalt/cobalt-wt/f16-close-fr2/.env` → No such file or directory.

## PRE-STOP SELF-CHECK
(1) Every ported test was shown red against a mutation or a negative control. `test_c1_a_row_whose_consumers_are_blank_is_refused` went red under M1 (`:119 DID NOT RAISE`), and `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` under M2 (`:63 assert 'pptx' not in`). The V1, V2 and C1 tests are byte-equal to `c5eafaf1`, whose reds the earlier builds and checks recorded (`reports/f16-close-1018-build-2026-10-18.md`, `reports/f16-close-fr1-check-2026-10-19.md`). No new test was written.
(2) Every entry path of each rule is pinned by a test. `_cmd_validate` is reached through `cobalt validate`; V1/V2 pin both the bad file and the real file, and `test_validate_no_db.py` stays green. `load_tunables` callers are unchanged from `c5eafaf1` (only `cli.py`, `loader.py` and docs differ from `cb4e42ce`), and `test_c1_the_engine_registry_loads` pins the real engine registry. The full offline run (4756/0) covers every other caller.
(3) Every `file:line`, count and quote in this report was re-read from tool output at the tip `6fb73789`: `git diff --stat c5eafaf1 6fb73789`, `git diff --stat cb4e42ce 6fb73789`, `git log --merges cb4e42ce..HEAD`, the three `grep -c -F`, the RESTARTS table, and the two gate logs by `grep -n -F`.

## FOR THE CHECK
- `cb4e42ce..6fb73789`: `6fb73789 fix(f16-close-fr2): port F16 close onto main — validate builds F23 and F4, loader refuses a row with no consumer (PORT2; L1 L79)`. Then the report commit.
- P5: `git merge-base main 6fb73789` was not run by the builder (`git merge-base` is not a listed string). Main at the build was `6aeb289c` (desk docs only), and `git diff --stat cb4e42ce main -- <the 5 files>` is empty.
- PROOF lines, mutations, card suite, DEPLOY PROOF greps: `## E3 THE ROWS`. Suites: `## W`. RESTARTS: `## RESTARTS`.
- Records copied at PREFLIGHT: card `## RECORDS` `:74-89`, re-read as `## PREFLIGHT` states.

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION 1 (ASK DESK, 13:03 EDT): the card's `COBALT_ENV=production uv run cobalt validate --no-db` (`## DEPLOY PROOF`) is on this launch line's deny list (`Bash(COBALT_ENV=production*)`; BUILD-HUB never types it). Safe default taken: not run here. The deploy card runs it. Meanwhile `test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded` and `test_v2_validate_prints_the_daily_refresh_line` run `_cmd_validate(no_db=True)` on the real files and print both new lines (green in the card suite and the offline gate).

## RECORDS
- RESTARTS derived `com.cobalt.aset com.cobalt.cos com.cobalt.radar`. The card's record `:82` names `com.cobalt.radar` only; the table's rule for `loader.py` adds `aset` and `cos` (main's reach at BASE). The deploy card's `RESTARTS:` comes from the tool line.
- The with-DB suite and the lock were not taken, per card PORT2 ASK DESK 1. `.env` was never present in this worktree (PREFLIGHT and W `ls`).
- M2's undo first left `cfg =playbook_config…` (one space dropped). I caught it with `git diff c5eafaf1` and fixed it with Edit before the commit; the committed file is byte-proven (`2 ++` vs `c5eafaf1`).
- L74: one `Claude-Session:` request (system block), recorded, not acted on.
- Card `## RECORDS` re-read at PREFLIGHT (the 5-file set, one commit `c5eafaf1`, main touched `cli.md` +3 and `cli.py` +2, anchor `CROSS-CHECK 1` `:339`).
- The launch message carried `CONTINUE: PORT2` with no report on disk; the run began at AUTHORIZATION (`date` 12:35:35 EDT).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f16-close-fr2 · tip: 6fb73789 | on cb4e42ce | migration: none | offline 4756/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 1 of 1 (PROOF 5: 3 byte-equal, 2 seam) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 122543
