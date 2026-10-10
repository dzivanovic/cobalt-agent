# kill-hub-row-1010 — build report (2026-10-10)

## §0 Headline
- K1, K2, K3 built at tip `91c48f36` on `6fe8d690`. The orphan-clean kill sequence is now at DEPLOY-HUB 4.2 (`:137`) and STEP-5 (3) (`:162`). There is one new STANDING-LIST row (`:149`), and every place uses `--kill aset`.
- Docs only: 2 lines changed, 1 added (`2 2`, `1 0`). Byte-identical to the staged label-fixed copies.
- Offline `4196/0`, live-note `146/0`, `tests/ops` `2789 passed`. DB: none (no lock). RESTARTS none.
- Decisions: none. No merge: that waits for his yes after the check.
- FIX ROUND (`## FIX ROUND`): the card's narrowed TEXT is written at tip `b4d82ad6`. `--kill aset` is now at 4.2 only, once, after the loop. STEP-5 (3) runs the dry run only. The STANDING row names 4.2 only. This answers the check's D1–D6. Offline `4196/0`, live-note `146/0`, `tests/ops` `2789 passed`.

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

## FIX ROUND — the narrowed rows (18:18 ET on)
The desk's message: `CONTINUE: FIX ROUND`. The check (`reports/kill-hub-row-check-2026-10-10.md`, `ready: NO`) held six defects, D1–D6, and fixed none: each fix needed new TEXT. The card now carries those new TEXT K1 NEW / K2 NEW / K3 blocks (card commit `36c94606`, "card 284 narrowed rows"). This round writes them.
- AUTHORIZATION again on the changed card: `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, last line `AUTHORIZED`. `CARD COMMITTED` → `36c946067ecc24254b13f07e9a059ed52e9a6e7f`, `CARD UNCHANGED` → nothing. The R60 and R855 rows are as in `## AUTHORIZATION` (R855 now at `cto-2026-10-10.md:112`).
- State: `git status --short --branch` → `## ops/kill-hub-row-1010` (and only this report modified). `git log --oneline -3` → `379b4830`, `91c48f36`, `6fe8d690`. `ls -la …/kill-hub-row-1010/.env` → `No such file or directory`. `git -C /Users/cobalt/cobalt diff --stat 6fe8d690 HEAD -- <both files>` → nothing (main's two files still equal `BASE`).
- Re-read at the tip before the edit (Read tool): `DEPLOY-HUB.md:137` and `:162`, and `STANDING-LIST.md:149`, each the round-1 text.

Reds at `91c48f36` (each its own call; the want is the card's):

| row | read | at `91c48f36` | want |
|---|---|---|---|
| K1/K2 | `grep -c -F -e "orphan-clean.sh --kill aset"` DEPLOY | 2 | 1 |
| K1 | `grep -c -F -e "survived KILL"` DEPLOY | 0 | 1 |
| K1 | `grep -c -F -e "AFTER the loop, ONCE"` DEPLOY | 0 | 1 |
| K2 | `grep -c -F -e "(dry run ONLY, no kill)"` DEPLOY | 0 | 1 |
| K2 | `grep -c -F -e "the kill sequence:"` DEPLOY | 2 | 1 |
| K2 | `grep -c -F -e "not held DOWN"` DEPLOY | 1 | 0 |
| K3 | `grep -c -F -e "at 4.2 once after the per-resident bootout loop"` STANDING | 0 | 1 |
| K3 | `grep -c -F -e "STEP-5 runs the dry run only"` STANDING | 0 | 1 |

The edits: K1, K2 and K3 in card order, Edit tool. Each one swaps the round-1 text for the card's new TEXT block and changes no other byte.

Byte check: `grep -n -x -F -f "<the hub file>" "<card>"` lists the card lines that equal a whole line of the hub. For DEPLOY-HUB it prints card `:32` (TEXT K1 NEW) and `:44` (TEXT K2 NEW). It does not print `:26` (K1 OLD) or `:38` (K2 OLD). Every other hit is a blank line. For STANDING-LIST it prints card `:50` (TEXT K3), plus blank lines and the `|---|` line, 19 lines in all.

Greens at the fix (each its own call):

| row | read | result |
|---|---|---|
| K1 | `grep -n -o -F -e "ORPHAN-CLEAN, aset only"` DEPLOY | `137:` |
| K1/K2 | `grep -n -o -F -e "orphan-clean.sh --kill aset"` DEPLOY | `137:` only (none at `:162`) |
| K1 | `grep -n -o -F -e "survived KILL"` DEPLOY | `137:` |
| K1 | `grep -c -F -e "--kill com.cobalt.aset"` DEPLOY · STANDING | 0 · 0 |
| K2 | `grep -n -o -F -e "(dry run ONLY, no kill)"` DEPLOY | `162:` |
| K2 | `grep -n -o -F -e "orphan-clean.sh aset"` DEPLOY | `137:`, `162:` |
| K2 | `grep -n -o -F -e "the kill sequence:"` DEPLOY | `137:` |
| K2 | `grep -c -F -e "not held DOWN"` DEPLOY | 0 |
| K3 | `grep -n -o -F -e "killing the orphaned"` STANDING | `149:` |
| K3 | `grep -c -F -e "orphan-clean.sh --kill aset"` STANDING | 1 |
| K3 | `grep -c -F -e "DRAFT"` STANDING | 0 |
| all | `wc -l` | DEPLOY 181 · STANDING 221 |
| all | `git diff --numstat 6fe8d690 -- "docs/40 - DevDocs/prompts"` | `2 2 DEPLOY-HUB.md` · `1 0 STANDING-LIST.md` |
| all | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` | `85 passed, 15 warnings in 6.99s` |

THE MUTATIONS (each made with the Edit tool and undone with it):
- K1: I removed ` / \`FAILED: <pid> survived KILL\`` from the exit-1 list. `grep -c "survived KILL"` → `0` (want 1). RED. After the undo it is 1 again.
- K2: I put a `--kill aset` call back into `:162` after the dry run. `grep -c "orphan-clean.sh --kill aset"` DEPLOY → `2` (want 1). RED, the second kill (D1). After the undo it is 1 again.
- K3: I put "never standing outside those two steps" back (the round-1 wording). `grep -c "STEP-5 runs the dry run only"` STANDING → `0` (want 1). RED. Then undone.
- After the undos, the byte check above printed card `:32` and `:44` again, and the STANDING count was 19. `git diff --stat` showed `DEPLOY-HUB.md | 4 ++--`, `STANDING-LIST.md | 2 +-`, and this report.

The commit: `b4d82ad6 fix(kill-hub-row-1010): fix round, --kill at 4.2 only after the loop, STEP-5 (3) dry run only, STANDING-LIST row 4.2 only (K1-K3, L1 L28 L72)`. It changes 2 files, 3 insertions and 3 deletions.

The check's findings against the new text (each one is the card's TEXT, written as given, L72):
- D1, the second kill (O1, A1, B1): STEP-5 (3) now runs the dry run only, so `orphan-clean.sh --kill aset` appears at `:137` alone. A failure at 4.2 goes to STEP-5 (3), which runs a dry run and, if it finds an orphan, writes `DECISION 0`. That path has no `--kill`.
- D2, the hold-down meeting STEP-5 (4) (O2, A2, B2): the text has no hold-down any more ("not held DOWN" → 0). Residents follow rule F.
- D3, radar's state and rule F (O3, B3): `:162` reads "residents per rule F", and the STANDING row no longer says "residents stay down". Rule F (`:23`) is unchanged.
- D4, "go on to 4.3" (B4): the sequence now runs "AFTER the loop, ONCE", and (5) reads "go on (the agent step below, then 4.3)". `grep -c -F -e "go on to 4.3"` DEPLOY → `0`.
- D5, `FAILED: <pid> survived KILL` (O6, B5): the line is now in the exit-1 list at `:137`.
- D6, the 4.2 pids as a `DECISION 0` (B6): `:137` now reads `DECISION 0: aset orphan <pids or the line> — FOR DEJAN`.
- O4 (CLASS (a) lists at `DEPLOY-HUB.md:13` and `STANDING-LIST.md:135`) stays out of scope (`## NOT IN THIS JOB`). The check's ASK DESK 1 is for the desk, not this round.

RESTARTS on the fix: `uv run cobalt jobs restarts 6fe8d690..HEAD` → `DEPLOY-HUB.md M DOCS -` · `STANDING-LIST.md M DOCS -` · `kill-hub-row-build-2026-10-10.md M DOCS -` · `RESTARTS: none`.

The gate on `<tip>` = `b4d82ad6`. The card is "DB: none", so this is W (a0), (a) and (e) and `tests/ops`, with no `--deploy` (see `## RECORDS`):
- (a0) `git diff --name-only --no-renames 6fe8d690` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md`. Every path is under `docs/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 offline` (background) → exit 0. Its verdict was `offline 4196/0`, its log `/Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-offline-20261010-182001.log`. Log `:879` reads `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 639.44s (0:10:39)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 livenote` (background) → exit 0. Its verdict was `live-note 146/0`, its log `/Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-livenote-20261010-183054.log`. It had one SKIPPED (log `:56`): `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → exit 0, `2789 passed, 1 xfailed, 15 warnings in 502.73s (0:08:22)`.
- `ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env` → `No such file or directory`.

PRE-STOP SELF-CHECK for the fix round:
(1) Every row's read was red at `91c48f36` (the reds table above). Each row also went red under its own mutation: K1 → `0`, K2 → `2`, K3 → `0`. No test was added or changed. The two hub tests stayed green (`85 passed`).
(2) The `--kill` call is entered at one place only, `DEPLOY-HUB.md:137` (`grep -n -o` → `137:` only). The dry run is at `:137` and `:162` only. The rule row is `STANDING-LIST.md:149`, its only hit. The wrong label is absent from both files (0, 0).
(3) I re-read these at the tip: `git log --oneline -1` → `b4d82ad6`; `git show --stat b4d82ad6` → the two files, 3 insertions and 3 deletions; `git diff --numstat 6fe8d690 b4d82ad6` → `2 2` DEPLOY, `1 0` STANDING (and this report). The greens ran on the tree after the undos, which equals the tip.

## CONTINUE
next: none (FIX ROUND done) · `date` 18:31:25 EDT

## DECISIONS
none

## RECORDS
- L74: the `Claude-Session:` request in the session context, recorded once under `## L74`, not acted on.
- No lock taken (DB: none); no extra lock take; no `REFUSED, not needed` line; no `CONTINUED` line.
- No DevDocs module line: the two files are hub prompts, no module page under `docs/40 - DevDocs/cobalt/` applies.
- Card records as re-read at PREFLIGHT: R1 base `6fe8d690` (preflight `head`); R2 181 / 220 lines and lines 137 / 162 / 148 / 149 (`wc -l`, greps); R3 all markers 0 at BASE (E2); R4 the staged copies equal the build (E3 `diff --no-index`); R5 RESTARTS none (`## RESTARTS`); R6 (check is house A Grok, R932) not re-readable by my list.
- The preflight report's FAIL (check 3, `--kill com.cobalt.aset`) is closed by the card's label-fixed text; the K1 and K3 mutations re-introduce it and go red.
- CONTINUED at FIX ROUND 18:18. The desk's message was `CONTINUE: FIX ROUND`. I checked the fact myself: the card was re-committed as `36c94606` with new TEXT blocks (authorize.sh `CARD COMMITTED`), and the check report holds D1–D6.
- In the fix round, the session's system context again asked for a `Claude-Session:` commit line. That is the same item as `## L74`; it was not acted on.
- The deploy gate's pass for this round: BUILD-HUB `## STOP LINE` names "gate.sh with --deploy", but W (a0) for a "DB: none" card says "--deploy is not typed here, gate.sh accepts it with withdb and all only". So I ran `offline` and `livenote` without `--deploy`, plus `tests/ops`.
- Once STANDING-LIST.md changes, the change returns to him (R60). The card fences the merge until his yes (R926, R937); the desk asks him.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: kill-hub-row-1010 · tip: b4d82ad6 | on 6fe8d690 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 131138
