# kill-hub-row-1010 — build report (2026-10-10)

## §0 Headline
- K1, K2, K3 built at tip `91c48f36` on `6fe8d690`. The orphan-clean kill sequence is now at DEPLOY-HUB 4.2 (`:137`) and STEP-5 (3) (`:162`). There is one new STANDING-LIST row (`:149`), and every place uses `--kill aset`.
- Docs only: 2 lines changed, 1 added (`2 2`, `1 0`). Byte-identical to the staged label-fixed copies.
- Offline `4196/0`, live-note `146/0`, `tests/ops` `2789 passed`. DB: none (no lock). RESTARTS none.
- Decisions: none. No merge: that waits for his yes after the check.

## L74
- The session's system context asked commits to also carry a `Claude-Session:` line. Recorded here once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md"` → exit 0, whole output:

```text
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · 0891e0839400e2c80abacc648f6eb72f00c6d937
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 98:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole output:

```text
clock · date · 0 · Sat Oct 10 16:59:13 EDT 2026
status · git status --short --branch · 0 · ## ops/kill-hub-row-1010
head · git log --oneline -1 · 0 · 6fe8d690 docs(desk): X29 deploy card 285, tip 3c00e204
diff · git diff --stat 6fe8d690 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/kill-hub-row-1010 · 0 · 6fe8d690 docs(desk): X29 deploy card 285, tip 3c00e204
env here · ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 6fe8d690` | 0 | `docs(desk): X29 deploy card 285, tip 3c00e204` · `.../prompts/2026-10-10/285-deploy-x29-card.md \| 29 ++++` · 1 file changed, 29 insertions(+) |
| wc | `wc -l DEPLOY-HUB.md STANDING-LIST.md` | 0 | `181` · `220` |
| symbol K1 | `grep -n -F "4.2 for each of" DEPLOY-HUB.md` | 0 | `137:4.2 for each of …` (whole line = TEXT K1 OLD) |
| symbol K2 | `grep -n -F "(3) THE RESTORE:" DEPLOY-HUB.md` | 0 | `162:- (3) THE RESTORE: …` (whole line = TEXT K2 OLD) |
| symbol K3 | `grep -n -F "Bash(launchctl print gui/501/*)" STANDING-LIST.md` | 0 | `148:` the `launchctl print` row; Read: `149` is the `Bash(/Users/cobalt/cobalt/cobalt.sh status)` row |
| launch line | `grep -n -F "Bash(sh /Users/cobalt/cobalt/ops/desk/*)" DEPLOY-HUB.md` | 0 | `11:` (the launch line) and `13:` (the CLASS (a) text) |
| STEP-5 once | `grep -n -F "STEP-5 is never entered twice" DEPLOY-HUB.md` | 0 | `164:` |
| tests reading STANDING-LIST | `grep -rn -F "STANDING-LIST" tests/ops` | 0 | `test_desk_launch_brain.py:498` reads the file; the others are constructed titles |
| tests reading DEPLOY-HUB | `grep -rn -F "DEPLOY-HUB" tests/ops` | 0 | `test_hub_lines.py:117` (launch line), `test_pass1_db_only.py:40` (STEP-G), `test_gate.py:30`, `test_deploy_card.py:428`; none pins line 137, 162 |
| orphan-clean.sh | Read `ops/desk/orphan-clean.sh` | — | `:76` `aset)` · `:77` `JOB=com.cobalt.aset` · `:82` `refuse "label '$label' is not in the label table (aset)"` · `:174` `orphan-clean: %s · none found` · `:250` `WOULD KILL: %s` · `:252` `orphan-clean: %s dry-run · verified %s · spared %s · killed 0` |
| card 229 O1 | `grep -n -F "\| O1 \|" 229-orphan-clean-card.md` | 0 | `16:` label table one entry `aset` → job `com.cobalt.aset` |
| READ tails | `tail -n 3` of the four READ reports | 0 | `KILL ROW DRAFTED · files: 2 · decisions: 2` · `KILL SEQUENCE AMENDED · files: 2 · decisions: 1` · `KILL LABEL FIXED · places: 3 · decisions: 2` · `PREFLIGHT DONE · prompts: kill-row · checks: 6 · fails: 1 · ready: NO` |
| restarts | `uv run cobalt jobs restarts 6fe8d690..HEAD` | 0 | one row: `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md A DOCS -` (this report, untracked) · `RESTARTS: none` |

The preflight report's one FAIL (check 3: `--kill com.cobalt.aset`) is the label the label-fix report changed to `aset`; the card's TEXT K1/K2/K3 carry `--kill aset`.

Card `## RECORDS`, copied and re-read where my list can:
- R1 base `6fe8d690` — re-read: preflight `head` and `main repo` rows above.
- R2 at BASE 181 / 220 lines, 137 / 162 / 148 / 149 as stated — re-read: `wc -l` and the three symbol greps above.
- R3 at BASE every marker count 0 — re-read at E2 (the reds).
- R4 source of the new text: the staged copies under `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/` — compared at E3 by `git -C … diff --no-index`.
- R5 RESTARTS none (DOCS) — re-read at RESTARTS.
- R6 the check is house A Grok (R932) — not re-readable by my list.

DB: none → no lock probe; the with-DB strings are not used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 676.19s (0:11:16)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.11s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Every row's red first is a grep read plus existing tests; no row names a test to write, so no test file was written and no `wip(kill-hub-row-1010): red` commit exists (nothing to commit; precedent `reports/hub-text-build-2026-10-05.md` `## E2 RED`). Reds on `BASE` 6fe8d690, each its own call:

| row | read | on BASE | want after |
|---|---|---|---|
| K1 | `grep -c -F -e "ORPHAN-CLEAN, aset only"` DEPLOY | 0 | 1 |
| K1/K2 | `grep -c -F -e "orphan-clean.sh --kill aset"` DEPLOY | 0 | 2 |
| K1 | `grep -c -F -e "--kill com.cobalt.aset"` DEPLOY | 0 | 0 |
| K2 | `grep -c -F -e "each resident booted out and not held DOWN"` DEPLOY | 0 | 1 |
| K2 | `grep -c -F -e "orphan-clean.sh aset"` DEPLOY | 0 | 2 |
| K2 | `grep -c -F -e "the kill sequence:"` DEPLOY | 0 | 2 |
| K3 | `grep -n -F -e "killing the orphaned"` STANDING | no output (no hit) | `:149` |
| K3 | `grep -c -F -e "orphan-clean.sh --kill aset"` STANDING | 0 | 1 |
| K3 | `grep -c -F -e "--kill com.cobalt.aset"` STANDING | 0 | 0 |

`uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` on BASE → `85 passed, 15 warnings in 7.09s` (no row moves a line these tests pin; they stay green, as the card says).

## E3 THE ROWS
K1, K2, K3 in card order, Edit tool, each NEW = the card's TEXT block. Greens at the fix (each its own call):

| row | read | result |
|---|---|---|
| K1 | `grep -n -F -e "ORPHAN-CLEAN, aset only"` DEPLOY | `137:` (one hit; whole line = TEXT K1 NEW) |
| K1/K2 | `grep -c -F -e "orphan-clean.sh --kill aset"` DEPLOY | 2 · `-n -o` → `:137`, `:162` |
| K1/K3 | `grep -c -F -e "--kill com.cobalt.aset"` both files | 0 · 0 |
| K2 | `grep -n -o -F -e "each resident booted out and not held DOWN"` DEPLOY | `162:` |
| K2 | `grep -n -o -F -e "orphan-clean.sh aset"` DEPLOY | `137:`, `162:` |
| K2 | `grep -n -o -F -e "the kill sequence:"` DEPLOY | `137:`, `162:` |
| K3 | `grep -n -o -F -e "killing the orphaned"` STANDING | `149:` |
| K3 | `grep -n -o -F -e "orphan-clean.sh --kill aset"` STANDING | `149:` (1) |
| K3 | `grep -c -F -e "DRAFT"` STANDING | 0 |
| all | `wc -l` | DEPLOY 181 (= BASE) · STANDING 221 (BASE 220) |
| all | `git diff --numstat 6fe8d690` | `2 2 DEPLOY-HUB.md` · `1 0 STANDING-LIST.md` |
| all | `git -C <worktree> diff --no-index <file> /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/<file>` | no output for both files: byte-identical to the staged label-fixed copies (card RECORDS R4) |
| all | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` | `85 passed, 15 warnings in 6.94s` |

THE MUTATIONS (Edit tool, each undone with the Edit tool):
- K1: `--kill aset` at 4.2 (3) → `--kill com.cobalt.aset` (the defect the label fix removed). `grep -c "orphan-clean.sh --kill aset"` DEPLOY → `1` (want 2); `grep -c "--kill com.cobalt.aset"` DEPLOY → `1` (want 0). RED. Undone → `2`.
- K2: "each resident booted out and not held DOWN" → "each resident booted out" (the BASE wording). `grep -c` → `0` (want 1). RED. Undone → `1`.
- K3: the row's first cell `--kill aset` → `--kill com.cobalt.aset`. `grep -c "orphan-clean.sh --kill aset"` STANDING → `0` (want 1). RED. Undone.
- After the undos: both `diff --no-index` against the staged copies print nothing; `git diff --stat` → `DEPLOY-HUB.md | 4 ++--`, `STANDING-LIST.md | 1 +`, 2 files, 3 insertions, 2 deletions.

Commit `91c48f36 fix(kill-hub-row-1010): orphan-clean kill sequence at DEPLOY-HUB 4.2 and STEP-5 (3), STANDING-LIST row (K1-K3, L1 L28 L72)`.
DevDocs module line: none. No module under `docs/40 - DevDocs/cobalt/` changed (the two files are hub prompts, not modules).

## RESTARTS
`uv run cobalt jobs restarts 6fe8d690..HEAD` → whole table:

```text
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md	A	DOCS	-
RESTARTS: none
```
No UNCLASSIFIED row. (The report row is the untracked report in the working tree.)

## W THE THREE SUITES
`<tip>` = `91c48f36`.
- (a0) `git diff --name-only --no-renames 6fe8d690` → whole: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md`. Every path starts with `docs/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 offline` (background) → exit 0, verdict `offline 4196/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-offline-20261010-171406.log` · log `:879` `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 672.22s (0:11:12)`. This build adds no test.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 livenote` (background) → exit 0, verdict `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-livenote-20261010-172532.log` · its one SKIPPED (log `:56`): `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `2789 passed, 1 xfailed, 15 warnings in 523.91s (0:08:43)`, exit 0.
- With-DB: not run (DB: none). (b)–(d), (f): not run.
- `ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every row's reads were shown red: on BASE (E2 table, every count 0 / no hit) and against a mutation per row (E3 MUTATIONS: K1 → `1`/`1`, K2 → `0`, K3 → `0`). No test was added or changed; the two existing ops tests are not row reds (they pin no moved line) and stayed green before and after (`85 passed` both).
(2) Entry paths: the kill sequence is entered at two places only, `DEPLOY-HUB.md:137` (4.2) and `:162` (STEP-5 (3)), each pinned by `grep -n -o` (`orphan-clean.sh aset`, `orphan-clean.sh --kill aset`, `the kill sequence:` → `:137`, `:162` only), and the rule row at `STANDING-LIST.md:149` (only hit). The wrong label is absent from both files (`--kill com.cobalt.aset` → 0, 0). The script's label table (`orphan-clean.sh:76-82`, `aset` only) and printed lines (`:174`, `:250`, `:252`) were read at PREFLIGHT; the text names `none found`, `dry-run · verified <n>`, `WOULD KILL: <pid>`, matching them.
(3) Re-read at the tip: `git log --oneline -1` → `91c48f36`; `git show --stat 91c48f36` → the two files, 3 insertions, 2 deletions; `git diff --numstat 6fe8d690 91c48f36` → `2 2` DEPLOY, `1 0` STANDING; `git status --short --branch` → `## ops/kill-hub-row-1010` plus only this untracked report, so the E3 greps (run on the tree equal to the tip, after the undos) are the tip's.

## FOR THE CHECK
- Range `6fe8d690..91c48f36`: one commit, `91c48f36 fix(kill-hub-row-1010): orphan-clean kill sequence at DEPLOY-HUB 4.2 and STEP-5 (3), STANDING-LIST row (K1-K3, L1 L28 L72)`.
- Per row: reds `## E2 RED`; mutations and greens `## E3 THE ROWS`.
- Byte check: both files equal the staged label-fixed copies (`diff --no-index` empty), and the diff is exactly 2 changed lines plus 1 added (X4: `git diff --numstat` → `2 2`, `1 0`).
- Caller greps: `## PREFLIGHT` (tests reading the two hubs; none pins `:137`, `:162`, `:148-149`).
- RUN rows: none in the card.
- Suites: offline `4196/0` (`gate.sh … offline`), live-note `146/0` (`gate.sh … livenote`), `tests/ops` `2789 passed, 1 xfailed`; with-DB not run (DB: none).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Card records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (CLOSE done) · built at `date` 17:26:10 EDT

## DECISIONS
none

## RECORDS
- L74: the `Claude-Session:` request in the session context, recorded once under `## L74`, not acted on.
- No lock taken (DB: none); no extra lock take; no `REFUSED, not needed` line; no `CONTINUED` line.
- No DevDocs module line: the two files are hub prompts, no module page under `docs/40 - DevDocs/cobalt/` applies.
- Card records as re-read at PREFLIGHT: R1 base `6fe8d690` (preflight `head`); R2 181 / 220 lines and lines 137 / 162 / 148 / 149 (`wc -l`, greps); R3 all markers 0 at BASE (E2); R4 the staged copies equal the build (E3 `diff --no-index`); R5 RESTARTS none (`## RESTARTS`); R6 (check is house A Grok, R932) not re-readable by my list.
- The preflight report's FAIL (check 3, `--kill com.cobalt.aset`) is closed by the card's label-fixed text; the K1 and K3 mutations re-introduce it and go red.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: kill-hub-row-1010 · tip: 91c48f36 | on 6fe8d690 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 130803
