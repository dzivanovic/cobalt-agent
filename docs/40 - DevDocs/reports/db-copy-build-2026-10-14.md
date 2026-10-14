# Build report — db-copy-1014 (card 547)

## §0 Headline
All six rows are built on `0e136e4f` (base `0a151491`). `gate.sh` has a copy mode, but it stays off until the lists file holds both `## COPY` sections. That needs the code card.
The new script is `devdb-copy-env.sh`. The launcher no longer treats a marked copy's `.env` as the lock. The lists file and BUILD-HUB W (b) each gained one line, and the no-clutter pin now exempts that W (b) line.
Results: offline 4328/0, live-note 146/0, `tests/ops` 3642 passed with 0 failed. DB: none, so the lock was never taken. RESTARTS: none.
There are 3 decisions, none for Dejan.

## L74
One system note asked for a `Claude-Session:` line on commits. It is recorded here once and was not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · 916f60f02a5b9e45be0b9de4e8cb9627f59a9d97
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Wed Oct 14 16:41:59 EDT 2026
status · git status --short --branch · 0 · ## ops/db-copy-1014
head · git log --oneline -1 · 0 · 0a151491 docs(report): deploy hub-text-1013-fr1 — DEPLOYED, smoke green, RESTARTS none
diff · git diff --stat 0a151491 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/db-copy-1014 · 0 · 0a151491 docs(report): deploy hub-text-1013-fr1 — DEPLOYED, smoke green, RESTARTS none
env here · ls /Users/cobalt/cobalt-wt/db-copy-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 0a151491` | 0 | `docs(report): deploy hub-text-1013-fr1 — DEPLOYED, smoke green, RESTARTS none` · `1 file changed, 71 insertions(+), 3 deletions(-)` |
| G1 (c) | `grep -n -F "held_env" ops/desk/gate.sh` | 0 | `255:held_env() {` · `286:    held_env` |
| G1 (b) | `grep -n -F "PASS1_DEPLOY=" ops/desk/gate.sh` | 0 | `194:PASS1_DEPLOY=$(cat "$tmp/pass1_deploy")` |
| G1 (f) | `grep -n -F "proof_clean" ops/desk/gate.sh` | 0 | `375:proof_clean() {` · `418:    proof_clean` · `427:    proof_clean` |
| L1 | `grep -n -F "with-DB launch refused: the cobalt_dev lock is held (" ops/desk/desk-launch.sh` | 0 | `1087:        [ ! -e "$f" ] \|\| refuse "with-DB launch refused: the cobalt_dev lock is held ($f) (L76)"` |
| L1 callers | Grep `lock_free\|lock_dir_free` in `desk-launch.sh` | 0 | `1082:lock_free() {` · `1091:lock_dir_free() {` · `1610:    [ -z "$step" ] \|\| lock_free` · `1717:    [ -z "$step" ] \|\| lock_free` · `1768:    lock_free` · `1769:    lock_dir_free` · `1820:    lock_free` · `1821:    lock_dir_free` |
| H1 | `grep -n -F -e "- (b) THE LOCK" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` | 0 | `83:- (b) THE LOCK (a)–(b), …, the proof-only → \`LEVEL 0013\`. Any other level: the gate releases and exits 5.` |
| D1 | `grep -n -F "## COPY" ops/desk/gate-lists.md` | 1 | (nothing) |
| D1 (15) | `grep -n -F "def test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order" tests/ops/test_gate.py` | 0 | `234:def test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order(gate):` |
| wc | `wc -l` of the five edited files | 0 | `511 ops/desk/gate.sh` · `48 ops/desk/gate-lists.md` · `2259 ops/desk/desk-launch.sh` · `112 docs/40 - DevDocs/prompts/BUILD-HUB.md` · `71 tests/ops/test_build_hub_no_clutter.py` |
| READ tail | `tail -n 3 …/survey-blockers-2026-10-12.md` | 0 | `SURVEYED · rows: 33 · decisions: 3` |
| RESTARTS | `uv run cobalt jobs restarts 0a151491..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

I re-read the card's `file:line`s from the files at BASE. They hold as the card states:
- `gate.sh`: `:255` `held_env`, `:267` `take`, `:288` "ours alone", `:291` `release`, `:352` `cleanup`, `:375` `proof_clean`, `:422-501` `do_withdb`.
- `desk-launch.sh`: `:1082-1089` `lock_free`, `:1091-1098` `lock_dir_free`, `:2119-2121`.
- `gate-lists.md`: `:3-8`, `:10`; the first heading line is `:17` `## OFFLINE`.
- `test_build_hub_no_clutter.py`: `:15` `BASE`, `:27-30` `base_lines()`, `:57` the test.
- `test_devdb_lock.py`: the six tests at `:279`, `:290`, `:300`, `:308`, `:318`, `:329`.

The card's `## RECORDS`, copied: the drafter read at `main` HEAD `0ffb6949`, with amends at `f52e9280` and `beb4c6f8`. The ruling is R1471. Desk decision brain R1472: a card pins only the lines its own card changes. The name length is 50 in all. Re-read here: the line numbers above.

DB: none. No lock probe was taken and no with-DB string was used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 657.57s (0:10:57)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.44s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`; no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`tests/ops/test_db_copy_1014.py` (NEW) was written with no `src/` or `ops/` edit. `uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/ops/test_db_copy_1014.py` on BASE → `28 failed, 4 passed`.
- E1 (1)-(4), all 13 cases: `AssertionError: sh: …/ops/desk/devdb-copy-env.sh: No such file or directory` / `assert 127 == 0` (or `== 2`). This is the row's reason (the script does not exist).
- G1 (5) `…creates_runs_on_the_copy_and_drops`: `assert ('dev-copy drop cobalt_dev_x_job' in ['fp', 'proof', 'pytest', 'forward', 'fp', 'pytest', ...])`. No `dev-copy` call.
- G1 (6) `…a_second_build_takes_the_lock…`: `assert not True` where `(…/wt / '.cobalt_dev.lock').exists`. The lock is held during the first run.
- G1 (7) `…a_create_that_fails…`: `assert 0 == 1`. The sections are ignored and the run is green.
- G1 (8) `…a_red_suite_still_drops_the_copy`: `assert 'pytest' == 'dev-copy dro...alt_dev_x_job'`, log `['fp', 'proof', 'pytest']`.
- G1 (9) `…half_a_copy_mode…`, 4 cases: `assert 0 == 1`. Not refused.
- G1 (11) `…over_50_characters…`: `assert 0 == 1`. Not refused.
- G1 (19) `…leftover_marker_and_env…`: no `dev-copy` call (`kinds[2:4]`).
- L1 (12) `…build_resume_ignores…copy_env`: `REFUSED: with-DB launch refused: the cobalt_dev lock is held (…/wt/beta/.env) (L76)` / `assert 1 == 0`.
- L1 (13b) `…deploy_launch_is_still_refused…`: `assert 'the cobalt_dev lock is held by' in '…the cobalt_dev lock is held (…/wt/beta/.env) (L76)…'`. RED on BASE, though the card says GREEN: `lock_free` refuses before `lock_dir_free` is reached (DECISION 1).
- D1 (14): `assert 0 == 1` (`count('## COPY CREATE')` in the header).
- H1 (16): `assert 0 == 1` (`len([])`, no line holds `## COPY CREATE`).
- H1 (18): `assert 'startswith("- (b) THE LOCK")' in '…test_build_hub_no_clutter.py…'`.
- PASSED on BASE (the named negative controls): (10) `test_g1_without_the_sections_the_gate_runs_on_the_one_lock`, (13a) `test_l1_an_env_with_no_marker_is_still_the_lock`, (15) `test_d1_the_real_lists_file_holds_no_copy_section_yet`, (17) `test_h1_the_launch_lines_of_the_hubs_carry_no_new_allow_string`.

Commit `8152c66e wip(db-copy-1014): red — card 547 tests (E1, G1, L1, D1, H1)`.

## E3 THE ROWS
The rows were built in card order on the fix commit `0e136e4f`.
- **E1** NEW `ops/desk/devdb-copy-env.sh`. `-k test_e1` → `13 passed`. I added one extra positive control: `test_e1_the_longest_name_the_pattern_allows_is_placed`, at 50 characters.
- **G1** `ops/desk/gate.sh`:
  - the `# THE COPY (card 547 db-copy, his R1471):` paragraph;
  - `unset COBALT_DEV_DB_NAME`;
  - a second reader block after `PASS1_DEPLOY=`;
  - the `held_env` skip;
  - `release [short]`;
  - helpers `copy_name`, `copy_cmd`, `copy_create`, `copy_drop`, `copy_env`, `copy_end`;
  - the `cleanup` copy end before the release;
  - `proof_clean [<copy>]`;
  - the `do_withdb` copy branch and end;
  - the name check before the mode dispatch.

  `-k test_g1` → `11 passed`. `tests/ops/test_gate.py tests/ops/test_devdb_lock.py tests/ops/test_db_copy_1014.py` → `100 passed`; the only 5 failures were rows not yet built.
- **L1** `ops/desk/desk-launch.sh` `lock_free`: one skip line and its comment. `-k "test_l1 or launch or resume or deploy"` over `test_db_copy_1014.py` and `test_devdb_lock.py` → `10 passed`.
- **D1** `ops/desk/gate-lists.md`: one paragraph. D1 together with the two `test_gate.py` pins → `4 passed`.
- **H1** `BUILD-HUB.md:83`: the one sentence. `tests/ops/test_build_hub_no_clutter.py`: the `- (b) THE LOCK` exemption on both sides, plus a one-line count.

ORDER run: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_db_copy_1014.py tests/ops/test_devdb_lock.py tests/ops/test_gate.py tests/ops/test_hub_lines.py tests/ops/test_build_hub_no_clutter.py` → `140 passed, 15 warnings in 88.27s (0:01:28)`.

THE MUTATIONS. Each was made and undone with Edit and never committed. After undoing, `git diff --stat` printed nothing (the E1 script was untracked then) and `-k "test_g1 or test_e1"` → `24 passed`.

| row | mutation | result (first failing line) |
|---|---|---|
| E1 | the `*[!a-z0-9_]*` refusal disabled | `2 failed, 11 passed`: `[cobalt_dev_A]`, `[cobalt_dev_a-b]` `assert 0 == 2` (`copy env placed: alpha`) |
| E1 | `-le 50` → `-le 51` | `1 failed, 12 passed`: `[cobalt_dev_aaaa…(40)]` `assert 0 == 2` |
| G1 | `held_env` skips every marked worktree, its own too | `1 failed, 10 passed`: (19) `cobalt_dev lock not ours alone after the take — ` / `assert 4 == 0` |
| G1 | `held_env` skips none (fix undone) | `1 failed, 10 passed`: (6) `cobalt_dev lock not ours alone after the take — …/x-job/.env …/y-job/.env` / `assert 4 == 0` |
| G1 | the trap's copy end disabled | `1 failed, 10 passed`: (8) `assert 'pytest' == 'dev-copy dro...alt_dev_x_job'` |
| G1 | the half-mode refusal and the 50 limit both removed | `3 failed, 8 passed`: (9) two half cases `assert 0 == 1`; (11) `assert 'REFUSED: copy name too long' in ''` |
| L1 | the skip line made `continue` (every `.env` skipped) | `1 failed, 2 passed`: (13a) `assert 0 == 1` |
| D1 | the paragraph's first line made a heading `## COPY CREATE and …` | `2 failed`: (14) `count('## COPY CREATE')` `assert 0 == 1`; (15) `assert not ['## COPY CREATE and …']` |
| H1 | the no-clutter exemption removed, with line 83 changed | `1 failed, 4 passed`: `test_no_other_line_changes_from_base` `At index 80 diff: '- (b) THE LOCK …'` |

H1 (16) under its fix undone is the E2 red above.

Commit `0e136e4f feat(db-copy-1014): gate copy mode, devdb-copy-env.sh, launcher skips a marked copy, lists and hub lines (E1 G1 L1 D1 H1, L76 L81)`.

DEPLOY PROOF at the tip: `grep -c -F "card 547 db-copy"` → `gate.sh:1`, `devdb-copy-env.sh:1`, `desk-launch.sh:1`, `gate-lists.md:1`. `grep -c -F "## COPY CREATE"` → `gate-lists.md:1`, `BUILD-HUB.md:1`.

## RESTARTS
R5 RUN. `uv run cobalt jobs restarts 0a151491..HEAD` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/devdb-copy-env.sh	A	operator script; no Cobalt reader	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_db_copy_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
There is no UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `0e136e4f`.
- (a0) `git diff --name-only --no-renames 0a151491` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `ops/desk/desk-launch.sh` · `ops/desk/devdb-copy-env.sh` · `ops/desk/gate-lists.md` · `ops/desk/gate.sh` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_db_copy_1014.py`. Every path starts `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 offline` → `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-offline-20261014-170250.log` (exit 0).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-livenote-20261014-170251.log` (exit 0).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3642 passed, 1 xfailed, 16 warnings in 762.19s (0:12:42)` (exit 0).
- with-DB: not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason, against BASE (E2) or against a mutation (E3 table). The four negative controls each went red under a mutation: (10) is the E3 G1 "skips none" and default runs plus the BASE pass; (13a) under the L1 mutation; (15) under the D1 mutation; (17) has no fix to undo. Its pin is the launch lines carrying no new allow string, and it stays green by construction (the launch lines were not touched; `test_hub_lines.py` is green). One deviation: (13b) was RED on BASE, not green (DECISION 1).

(2) Callers:
- `lock_free`: `desk-launch.sh:1610` and `:1717` (build and check resume), `:1768` and `:1820` (deploy kinds).
  - (12) pins a build resume with a marked `.env`.
  - (13b) pins a deploy launch with a marked `.env` and the lock directory.
  - (13a) pins a build resume with an unmarked `.env`.
  - The check-resume caller `:1717` with a marked `.env` has no test of its own (DECISION 2).
- `held_env`: called only from `take()` (`gate.sh` `:286` at BASE). Pinned by (6), (19) and (10).
- `proof_clean`: both calls are pinned by (5) and (7).
- `cleanup`: pinned by (7), (8) and (5).

(3) Re-read at the tip:
- `grep -n -F "card 547"` over the five files: `gate.sh:39`, `devdb-copy-env.sh:3`, `desk-launch.sh:1087`, `gate-lists.md:11`, `BUILD-HUB.md:83`.
- `grep -c -F` counts as in E3.
- `git log --oneline 0a151491..HEAD` → `0e136e4f`, `8152c66e`.
- `uv run cobalt jobs restarts` on the tip.

## FOR THE CHECK
- Range `0a151491..0e136e4f`: `8152c66e wip(db-copy-1014): red — card 547 tests (E1, G1, L1, D1, H1)` · `0e136e4f feat(db-copy-1014): gate copy mode, devdb-copy-env.sh, launcher skips a marked copy, lists and hub lines (E1 G1 L1 D1 H1, L76 L81)`.
- Per row: the reds are under E2, the mutations and greens under E3, the caller greps under PREFLIGHT and the self-check (2).
- R5 RUN output whole: under RESTARTS.
- Suites: offline 4328/0, live-note 146/0, `tests/ops` 3642 passed with 0 failed. With-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- Copy-mode behaviour worth a look (X1-X6):
  - In copy mode, F0 for the rollback compare is the copy's own first fingerprint. The template's goes to the log as `F0: `, the copy's as `F0 (<copy>): `.
  - The copy's proof-only lines go to the log only. The step-2 release's `.env: removed` goes to the log only, so stdout is today's lines plus `copy: <copy> created` and `copy: <copy> dropped`. The verdict lines without the sections are pinned by (10).
  - `copy_name` also refuses when `devdb-copy-env.sh` is not beside `gate.sh` in copy mode.
  - `gate.sh` unsets a caller's `COBALT_DEV_DB_NAME` at its start (X3).
  - X2 exit paths after the create: a red suite, a forward red, a rollback ≠ F0, INT/TERM/HUP and a failed `place` all go through `cleanup` → `copy_end` before the release.
  - A failed create sets no `made`, so nothing is dropped at the trap. Test (7) pins this.
  - A take that times out exits before any copy exists.

## CONTINUE
next: done (BUILT)

## DECISIONS
- DECISION 1 (row L1, test (13b)): the card says `test_l1_a_deploy_launch_is_still_refused_while_the_lock_directory_is_held_even_with_a_marked_env` is GREEN on BASE. It is RED on BASE: `lock_free` refuses first with `the cobalt_dev lock is held (<path>)`, not `held by`. After L1 it is green, and it proves `lock_dir_free` stands. Safe default taken: the test keeps the card's assertion (`held by`).
- DECISION 2 (self-check (2)): the check-resume caller `desk-launch.sh:1717` of `lock_free` has no test of its own with a marked `.env`. It runs the same function as the pinned build resume `:1610`. Safe default taken: no test added (rows only); the check may pin it.
- DECISION 3 (row G1): in copy mode, the stray-rows line `DECISION 0: the suite left <t> rows on cobalt_dev` keeps its text and its exit 1, though the rows sat on the copy, which is then dropped. Safe default taken: unchanged (the card names no change; BUILD-HUB H1 says the stray rows go with the copy).

## RECORDS
- No DevDocs line was added. There is no page under `docs/40 - DevDocs/cobalt/` for an `ops/desk/` script (Grep for `gate.sh|desk-launch.sh|gate-lists` there: only `jobs/restarts.md` and `db_migrations/cli.md`, both of which name them as paths).
- One `git commit` was blocked by the bare-command hook because its message held the word `.env` (`route: .env is never read …`). It was resent with the message reworded; nothing else changed.
- One E2 test line was rewritten before the red run: a vacuous `… or True` assertion in (7) became a check that no call before the failed create carries `COBALT_DEV_DB_NAME`.
- I added one positive control beyond the card: `test_e1_the_longest_name_the_pattern_allows_is_placed` (50 in all is placed).
- The card's records, as re-read at PREFLIGHT, are listed there. ASK DESK 1-4 of the card stand: copy mode stays off until the code card adds the `cobalt db dev-copy` verb, the `COBALT_DEV_DB_NAME` seam, and the two sections.
- The L74 line is under `## L74`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: db-copy-1014 · tip: 0e136e4f | on 0a151491 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 219435
