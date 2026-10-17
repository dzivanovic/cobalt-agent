# deploy gemini-builder-row — SET: none · MIGRATIONS: none

CARD: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/706-deploy-gemini-builder-row-card.md` · hub: `DEPLOY-HUB.md` · first launch (report absent: `ls -la` → `No such file or directory`).

## §0 Headline

FAILED at STEP-G (a): the integrated gate on `d7e7765f` is red on one `tests/ops` test, `test_band_routing_1015.py::test_b2_control_the_three_builder_rows_stand`. It pins three builder rows, and this set adds the Gemini row.
The band-routing test reached `main` after the build's base `7f415a4f`, so neither the build nor the check could see it. The fault is in the combination.
Nothing merged and production is untouched: RESTARTS none, residents never down, `cobalt_dev` not taken.
Next: a build updates that control test on a rebased branch, then a check, then `desk-launch.sh recut "<card>"`.

## L74

One block arrived as a system reminder at session start (not a tool result) asking that commits also end with a `Claude-Session:` line. Recorded once; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/706-deploy-gemini-builder-row-card.md"` → exit 0, whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/706-deploy-gemini-builder-row-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-17/706-deploy-gemini-builder-row-card.md" · 0 · cca71f6b6d09672e04bf03a19eb009375d0288f7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-17/706-deploy-gemini-builder-row-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1738 row · grep -n "^| R1738 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 74:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; answer: reports/gemini-bakeoff-answer-2026-10-17.md. Probe-id and builder cards drafted now; three builds after both deploy; routing B unchanged. | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1738 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy "<card>"` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Sat Oct 17 16:29:21 EDT 2026` — outside 21:30-22:30 ET |
| P2 check | `tail -n 3 ".../gemini-builder-row-check-2026-10-17.md"` | 0 | `CHECK DONE · job: gemini-builder-row · pass: 1 · tip: 7b986738 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8413/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 212150` — carries `held unfixed: 1` and `ready: NO` as the row names |
| P2 check | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/gemini-builder-row-check-2026-10-17.md"` | 0 | `dbbbb5c2a233e1ed71a179a85d03ad27fc2bcecb` |
| P2 check | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7b986738 695f8bde` | 0 | check tip is an ancestor of the code tip |
| P2 fix-round | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<fix report>"` (main) | 0 | nothing (the fix report lives on the branch, read at its head) |
| P2 fix-round | `tail -n 3 "<fix report>"` (main working tree) | 1 | `No such file or directory` — not on `main`; read at the branch head below |
| P2 fix-round | `git -C /Users/cobalt/cobalt log -1 --format=%H ops/gemini-builder-row-1017 -- "<fix report>"` | 0 | `06d31180aa1e04767df6eb6a00a50bf22ce70c06` (committed at the head) |
| P2 fix-round | `git -C /Users/cobalt/cobalt show "06d31180:<fix report>"` | 0 | last non-blank line `BUILT · job: gemini-builder-row · tip: 695f8bde \| on 7f415a4f \| migration: none \| offline 8416/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 123553`; line 274 `FIXED: O1 — tests/ops/test_bare_guard.py::test_k5_check_o1_an_add_dir_equals_form_in_the_hub_row_is_g7` |
| P2 held ids | `grep -n -F "HELD, NOT FIXED" "<check>"` | 0 | one id: `O1` (lines 152, 186, 219, 226) — named by the FIXED line |
| P2 FIXED test | `git -C /Users/cobalt/cobalt show 695f8bde:tests/ops/test_bare_guard.py` | 0 | `2538:def test_k5_check_o1_an_add_dir_equals_form_in_the_hub_row_is_g7(roots):` — no xfail decorator above it (lines 2535–2537: an assert of the prior test, two blanks) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 695f8bde` | 0 | `695f8bde` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-builder-row-1017` | 0 | `06d31180` = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 695f8bde 06d31180` | 0 | ancestor |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 695f8bde 06d31180 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/gemini-builder-row` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `cca71f6b` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor cca71f6b main` | 0 | ancestor |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/gemini-builder-row` | 0 | empty |
| P6 | marker 1 `grep -c -F "agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m" ".../SHADOW-HUB.md"` | 1 | `0` = before |
| P6 | marker 2 `grep -c -F "gemini-4-argon-high) ;;" .../desk-launch.sh` | 1 | `0` = before |
| P6 | marker 3 `grep -c -F "card 671 G2/FR-1: agy --add-dir D or --add-dir=D (D/**), read for agy only" .../bare-guard.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 06d31180 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 80523` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 24167` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE

- `git -C <GATE> merge --no-edit 06d31180` → `Merge made by the 'ort' strategy.` (auto-merged `SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`; 8 files changed, 511 insertions(+), 18 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `d7e7765f` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent cca71f6b..deploy/gemini-builder-row` → `d7e7765f Merge commit '06d31180' into deploy/gemini-builder-row` (one line, one head).
- `merge-base --is-ancestor 695f8bde deploy/gemini-builder-row` → exit 0; `merge-base --is-ancestor 06d31180 deploy/gemini-builder-row` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat cca71f6b deploy/gemini-builder-row -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat cca71f6b deploy/gemini-builder-row -- configs ops` →
  ```
   ops/desk/bare-guard.py  | 15 +++++++++++----
   ops/desk/desk-launch.sh |  4 +++-
   2 files changed, 14 insertions(+), 5 deletions(-)
  ```
  `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" cca71f6b deploy/gemini-builder-row` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>` = empty.

## RESTARTS

`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:

```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-gemini-builder-row
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-gemini-builder-row
Installed 254 packages in 997ms
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md	A	DOCS	-
docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.result	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```

No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with the residents up. `<launchd set>` = empty.

## L68 GATE

The equal-tree clause does not hold (the check's stop line carries `with-DB 0/0`, and its tip `7b986738` ≠ the code tip `695f8bde`): the gate runs whole (`--deploy`).

- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.38s` — `0 failed` (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-gemini-builder-row all --deploy --deploy-gate` (no `--deselect`: the build was DB: none and deselected nothing; TICKERS: none; no `--migration`) → exit 1, verdict lines whole:
  ```
  tests/ops: run (deploy gate)
  RED (exit 1): 1 failed, 3918 passed, 1 xfailed, 16 warnings in 860.03s (0:14:20)
  E       AssertionError: assert ['claude-sonn...', 'grok-4.7'] == ['claude-sonn...', 'grok-4.7']
  E         
  E         At index 1 diff: 'gemini-4-argon-high' != 'gpt-5.6-terra'
  E         Left contains one more item: 'grok-4.7'
  E         Use -v to get more diff

  tests/ops/test_band_routing_1015.py:116: AssertionError
  ...
  1 failed, 3918 passed, 1 xfailed, 16 warnings in 860.03s (0:14:20)
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-gemini-builder-row-all-20261017-163122.log
  ```
- (a) OFFLINE, first run (log line 888): `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 674.90s` → `[exit 0]`. The `tests/ops` run (log 890–976, W line `tests/ops: run (deploy gate)`): **RED** — `tests/ops/test_band_routing_1015.py::test_b2_control_the_three_builder_rows_stand`, `:116` `assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"])`: the merged `SHADOW-HUB.md` `## BUILDERS` now holds four rows (`claude-sonnet-5-5`, `gemini-4-argon-high`, `gpt-5.6-terra`, `grok-4.7`).
- The gate stopped at (a): no lock taken, no `cobalt_dev` step, no forward. `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file. `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- WHY (read-only, quoted): the test is not in the build's base — `git -C /Users/cobalt/cobalt log --oneline -3 7f415a4f -- tests/ops/test_band_routing_1015.py` → nothing; on `main`: `git -C /Users/cobalt/cobalt log --oneline -3 main -- tests/ops/test_band_routing_1015.py` → `05654335 fix(band-routing-1015): close step excepts the check seat's one untracked SHADOW-INSTRUCTIONS.md too (FR-10, L1 L72)`, `630542a7 …`, `3f399b60 …`. The band-routing set reached `main` after `7f415a4f`; its control test pins exactly three builder rows, and this set adds the fourth. A fault of the combination, not seen by the build (offline 8416/0) or the check (8413/0), which ran on the older base.
- GATE RED. Not green on `d7e7765f`. No fix commit in this run (rule B).

## Deploy table

Nothing merged to `main`; nothing in production changed; no resident went down; no snapshot, no tag. `<m0>` `cca71f6b` · `<m1>` `d7e7765f` (gate branch only) · `<restart set>` none · `<launchd set>` none · migrations applied: none.

## Smoke

Not reached.

## CONTINUE

next: none — FAILED at STEP-G (a). The desk's next step is `desk-launch.sh recut "<card>"` after a build fixes the combination (RECUT).

## DECISIONS

- DECISION 1 (blocks the next deploy): `tests/ops/test_band_routing_1015.py::test_b2_control_the_three_builder_rows_stand` pins `## BUILDERS` to exactly `grok-4.7`, `claude-sonnet-5-5`, `gpt-5.6-terra`; this set adds `gemini-4-argon-high` on purpose (R1738). The fix is a build's (rule B, L68): a fix round on card 671 (or a small card) that rebases on `main` and updates that control to four rows, then its check, then a recut of this deploy. Safe default taken: the run ends FAILED, nothing merged. Not for Dejan: R1738 already rules the Gemini row in; the test change is engineering.

## RECORDS

- Gate log: `/Users/cobalt/cobalt-wt/.gate-logs/deploy-gemini-builder-row-all-20261017-163122.log`.
- `cobalt_dev`: not taken (the gate stopped at (a)); lock dir absent; `<GATE>/.env` absent.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-gemini-builder-row` and branch `deploy/gemini-builder-row` (it carries the merge `d7e7765f`; `main` does not); `RECUT` cleans them.
- No `RETIRE OWED`, no `BOOTSTRAP OWED` (STEP-C: `ADMITTED 0`). No downtime. No `REFUSED, not needed` line. No `CONTINUE` message arrived.
- L74: the `Claude-Session:` reminder at session start, not followed (see `## L74`).
- The card's records, copied:
  - gemini-builder-row: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md` at `06d31180` last line: BUILT · job: gemini-builder-row · tip: 695f8bde | on 7f415a4f | migration: none | offline 8416/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 123553
  - gemini-builder-row: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-check-2026-10-17.md` last line: CHECK DONE · job: gemini-builder-row · pass: 1 · tip: 7b986738 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8413/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 212150
  - gemini-builder-row: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-builder-row-1017` → `06d31180`; code tip `695f8bde`
  - written by deploy-card.sh at 2026-10-17 16:28 ET (`date`); trial merge of the heads onto main in order: clean
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 9d183e3f` → `context 120388 of 400000 — ok`. Ended `Sat Oct 17 16:57:30 EDT 2026`.

FAILED: gate — G (a) — tests/ops/test_band_routing_1015.py::test_b2_control_the_three_builder_rows_stand (pins three builder rows; this set adds gemini-4-argon-high) · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 120388
