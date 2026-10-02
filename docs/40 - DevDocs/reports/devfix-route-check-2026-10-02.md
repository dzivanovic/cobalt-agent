# devfix-route — check, pass 1 (2026-10-02)

## §0 Headline
I checked the devfix route alone: no outside house (R47). The build holds, with two gaps that are now fixed.
O1: the new REPORT name check let an accented name through. Its letters are now spelled out, like the checks beside it.
O2: a resumed devfix session would stop at its first step with its own lock still held. `DEVFIX-HUB.md` now has a RECOVERY step that releases the job's own lock first.
The three suites are green on `46712ab4`. `cobalt_dev` is back at `0013` with F2 = F0, and `.env` is removed. Nothing is open, and there are no decisions.

## L74
- After the launch message, a system block asked for commit messages to end with a `Claude-Session: https://claude.ai/code/session_…` line beside `Co-Authored-By`. Recorded once; not acted on. Both commits of this check carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (the hub's L74; the block itself says the user's rule about these lines takes precedence).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/12-devfix-route-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/12-devfix-route-card.md"` | 0 | `d8808a502d553051fe31bf0e4a08827b372e3008` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 commit | `git -C … log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R14 | `grep -n "^| R14 " ".../cto-2026-10-02.md"` | 0 | `21:| R14 | 06:18 ET | HIS RULING: approves … standard dev-fix card owed … | HIS RULING · APPROVED |` |
| R14 commit | `-S"| R14 |"` | 0 | `02cfa29178cec4dcb95e4b43336b1ddf9118a69a` |
| R18 | `grep -n "^| R18 " ".../cto-2026-10-02.md"` | 0 | `25:| R18 | 06:23 ET | HIS RULING (L73 override of L61, this launch only) … | HIS RULING · APPROVED |` |
| R18 commit | `-S"| R18 |"` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| R47 (HOUSE A: none) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |` |
| R47 commit | `-S"| R47 |"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| house gates | — | — | not run: `HOUSE A: none — overruled 2026-10-02 R47` (PREFLIGHT runs no house gate and no probe) |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 14:11:02 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/devfix-route-1002` |
| tip | `git log --oneline -1` | 0 | `36f5bf9c docs(devfix-route): build report — 63649058 (close record)` |
| above the tip is docs only | `git log --stat --format=%h 63649058..HEAD` | 0 | 36f5bf9c, eeb7c6a2, 280fceb7: each only `docs/40 - DevDocs/reports/devfix-route-build-2026-10-02.md` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: devfix-route · tip: 63649058 \| on 551f07e0 \| migration: none \| offline 3784/0 \| with-DB 4554/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 4 of 4 \| self-check: 3 of 3 \| decisions: 3 · for Dejan: 0` |
| range | `git log --oneline 551f07e0..63649058` | 0 | `63649058 feat(devfix-route): the devfix kind — …` / `f76ca0bd wip(devfix-route): red — the devfix kind's tests (F1, F2)` |
| range paths | `git log --stat --format=%h 551f07e0..63649058` | 0 | 63649058: `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEVFIX-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_devfix.py`; f76ca0bd: `tests/ops/test_desk_launch_devfix.py` |
| lock: worktree | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock: all | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house | — | — | `house A: none (overruled 2026-10-02 R47)` · `HOUSE B: as needed` (not mandatory) |

## Files copied
None: no house sits (R47).

## OWN FINDINGS
Written before any run.

FINDING O1
ROW: F2
CLAIM: The new `devfix` REPORT name check at `ops/desk/desk-launch.sh:648` (`*/*|*[!A-Za-z0-9._-]*) report_bad=1`) uses bracket ranges. Under this shell's UTF-8 locale a range lets accented letters through, as the build's own M2 run showed. The build report's DECISION 1 says "the new `devfix` checks spell their letters out", but this one does not, so `devfix-x_tablé.md` is accepted, not refused.
RUN: TEST, `tests/ops/test_desk_launch_devfix.py`:
```python
def test_a_report_name_outside_its_spelled_set_is_refused(desk):
    bad = desk.reports / "devfix-x_tablé.md"
    desk.write_card(REPORT=str(bad))
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)),
            f"incomplete card: a devfix REPORT must be {desk.reports}/devfix-<name>.md")
```
EXPECT: red on the tip: `assert 0 == 1` (the launch prints its line and exits 0).

FINDING O2
ROW: F1 / F2 ("A resume step as build")
CLAIM: `desk-launch.sh devfix <card> <step>` launches a NEW session while the job's OWN `.env` and OWN lock directory stand (`ops/desk/desk-launch.sh:491`, `:501`; pinned by `test_a_resume_skips_its_own_lock_and_prefixes_continue`). For a build, its RECOVERY clears these first (`BUILD-HUB.md:36`: "`.env` present → W (f) FIRST"). `DEVFIX-HUB.md` has no RECOVERY step: its PREFLIGHT (`DEVFIX-HUB.md:41`) requires `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` and the lock directory absent, and otherwise ends `FAILED: PREFLIGHT — cobalt_dev lock held`, with the lock still held. So the resume path that F2 builds and tests launches a session that stops at its first step and never releases its own lock. `cobalt_dev` stays locked for every other job until someone releases it by hand.
RUN: COMMAND `grep -n -F "RECOVERY" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"`
EXPECT: exit 1, nothing (no step on a resumed launch releases the job's own lock before PREFLIGHT).

Read and not raised (each checked against the files): the F1 line against the card's `## RECORDS` line with its lock-script condition (`DEVFIX-HUB.md:12` vs `BUILD-HUB.md:12` at BASE: the two lock strings and the fourth `--add-dir` are byte-equal; the rest are in the record's order); THE LOCK text and `<FP>` against `BUILD-HUB.md:39`, `:41` (equal but "taken once, at S1"); the two stop lines against the card's F1 (equal); 22 allow and 4 deny counted on the line; §6 lists every string; the TABLE and PROOF TEST classes are spelled out (`:621`, `:633`, `:637`); the sed fill values are confined to sets without `|`, `&` or `\`; the fence (no `src/`, `build` / `check` / `deploy` / `prompt` / `close` branches untouched except the shared worktree-add `if`, whose `build` arm is unchanged); no person or vendor name in an identifier; no path to a score, rank, grade or size. The card has no `## CHECK ASKS`.

## Findings
None: no house (R47).

## Dropped
None.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_devfix.py::test_a_report_name_outside_its_spelled_set_is_refused` (test as written, no repair) | `1 failed, 15 warnings in 1.36s`; first failing line `E       AssertionError: git -C …/repo worktree add -b ops/x-fix …/wt/x-fix b2862ef1` … `assert 0 == 1`: the launch printed the add, the `cd` and the filled line for REPORT `devfix-x_tablé.md` | HELD |
| O2 | own | `grep -n -F "RECOVERY" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` | nothing (no hit). Beside it, `grep -n -F "cobalt_dev lock held" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → `41:- PREFLIGHT (no lock): … ls -la /Users/cobalt/cobalt-wt/*/.env → no matches found; ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock → "No such file" (a hit → FAILED: PREFLIGHT — cobalt_dev lock held — <path> · cobalt_dev: untouched · .env: removed)`. A resumed session that finds its own `.env` stops there, still holding the lock, and its stop line says `.env: removed` while the file is on disk | HELD |

Held red committed before any fix: `1df6759e wip(devfix-route): check red — O1`. O2 is a COMMAND finding and has no test file.

## FIXES
| id | file | fix | after |
|---|---|---|---|
| O1 | `ops/desk/desk-launch.sh:648` | `*[!A-Za-z0-9._-]*` → `*[!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-]*`: spelled out, like the TABLE and PROOF TEST classes beside it | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_devfix.py` → `48 passed, 15 warnings in 13.92s`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `116 passed, 1 xfailed, 15 warnings in 82.11s (0:01:22)` |
| O2 | `docs/40 - DevDocs/prompts/DEVFIX-HUB.md` | (c) ends "it runs RECOVERY first"; new `## RECOVERY`: on a `CONTINUE:` launch, this worktree's `.env` present or the lock `owner` reading `<WORKTREE>` → the lock's (d) first, recorded `(RECOVERY)`; a lock naming another worktree is not released and PREFLIGHT fails as written; then PREFLIGHT and S1–S8 whole. It uses only strings already on the line (`ls *`, Read, the release script) and adds no string | `grep -n -F "RECOVERY" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → lines 30, 32, 33; `grep -c "^claude --bg " …` → `1` (the line itself is unchanged); `test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled` PASSED in the 48 |

Commit `46712ab4 fix(devfix-route): the REPORT name class spelled out; DEVFIX-HUB RECOVERY releases the job's own lock before PREFLIGHT (check O1, O2)`. DevDocs line: none owed. Neither file is a `src/` module with a page under `docs/40 - DevDocs/cobalt/`, as the build report's E3 found for `desk-launch.sh`.

## Suites
My commits → RESTARTS, then W whole on `46712ab4`, with main's `BUILD-HUB.md` THE LOCK (the `cp` / `rm` pair, the strings on this line).
- RESTARTS: `uv run cobalt jobs restarts 551f07e0..HEAD` → `CARD.md M DOCS -` · `DEVFIX-HUB.md A DOCS -` · `STANDING-LIST.md M DOCS -` · `devfix-route-build-2026-10-02.md A DOCS -` · `ops/desk/desk-launch.sh M operator script; no Cobalt reader -` · `tests/ops/test_desk_launch_devfix.py A test/documentation; no resident -` · `RESTARTS: none`. No `UNCLASSIFIED`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 567.31s (0:09:27)` → `<p>` = 3784. This check's one added test is in `tests/ops` (`test_a_report_name_outside_its_spelled_set_is_refused`), run with `tests/ops` whole: `116 passed, 1 xfailed`.
- (b) 14:26:23 EDT: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`; `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 14:26 /Users/cobalt/cobalt-wt/devfix-route-1002/.env` (one line). `<FP>` (BUILD-HUB.md:41, typed exactly) → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)`; the 0014+ tables (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) `-`; every other table with schema, rows and digest (e.g. `aset_sizings user user 1 0824685c130da3c7cb7f0e76191a6819`, `cobalt_redactions system system 237 9f4931c4…`); footer `36 table(s) probed on cobalt_dev; … Proof cost: total 5.6 s …` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 46712ab4 (clean)`. No `CHANGED`; level `0013`.
- (c) PASS 1, the pass-1 command byte for byte (BUILD-HUB.md:84; no `--deselect` of this check's own; it adds no with-DB test) → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 707.99s (0:11:47)` → `<d1>` = 4383. Every SKIPPED line: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` · `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) FORWARD, foreground: `COBALT_ENV=dev uv run cobalt db migrate` → `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying 0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, `0014_radar_handicap.sql` … `0022_prediction_records.sql`; the eight 0014+ tables `CREATED`, every other `OK`; `36 table(s) proven; … content UNCHANGED on every table.` No `CHANGED`. **`dev forward: APPLIED 14:39:02 EDT`** (`date` after it). `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, the pass-2 command byte for byte (BUILD-HUB.md:88) → `171 passed, 1 deselected, 5 warnings in 220.68s (0:03:40)`; `grep -c -F "SKIPPED"` on its output → `0` → `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) not run: this check's test writes no ticker (no with-DB test). (c4) not run: no migration added.
- (f) foreground: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `cobalt db migrate — ROLLBACK on cobalt_dev`; `-- applying 0022_prediction_records.rollback.sql` … `0014_radar_handicap.rollback.sql` (newest first); the eight tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.` `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`**. The lock's (d): `rm /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; 14:43:22 EDT. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent (run before the take): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.16s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (not `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.

## Scope
PREFLIGHT's path union (`CARD.md`, `DEVFIX-HUB.md`, `STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_devfix.py`) plus my commits (`tests/ops/test_desk_launch_devfix.py`; `ops/desk/desk-launch.sh`, `docs/40 - DevDocs/prompts/DEVFIX-HUB.md`): every path is in F1's, F2's or F3's `files`. F4 touches no file.

## Checked against the branch
- (i) `git log --oneline 63649058..HEAD -- . ":(exclude)docs"` → `46712ab4 fix(devfix-route): the REPORT name class spelled out; DEVFIX-HUB RECOVERY releases the job's own lock before PREFLIGHT (check O1, O2)` · `1df6759e wip(devfix-route): check red — O1`. `<tip now>` = `46712ab4`.
- (ii) `git log --stat --format=%h 63649058..HEAD` → `46712ab4`: `docs/40 - DevDocs/prompts/DEVFIX-HUB.md`, `ops/desk/desk-launch.sh`; `1df6759e`: `tests/ops/test_desk_launch_devfix.py`; `36f5bf9c`, `eeb7c6a2`, `280fceb7`: the build report only. Every non-docs path is a row's file or a test file. No `WIDENED`.
- (iii) fence: `git log --oneline 551f07e0..HEAD -- src/cobalt` → nothing (`cobalt db dev-rebuild` and the slot guard are untouched). The other kinds' branches: the diff (read at `## 2`) changes only the shared `if [ "$kind" = "build" ] || [ "$kind" = "devfix" ]`, and `test_build_still_prints_its_add_cd_and_line` / `test_prompt_still_prints_its_cd_and_line` pass in the 48.
- (iv) `grep -n -F "def test_a_report_name_outside_its_spelled_set_is_refused" tests/ops/test_desk_launch_devfix.py` → `244:def test_a_report_name_outside_its_spelled_set_is_refused(desk):` (one line); its red `1df6759e` sits below its fix `46712ab4` in (i). O2 is a COMMAND finding: its run before and after the fix is in `## RUNS` / `## FIXES`.
- (v) `ls /Users/cobalt/cobalt-wt/devfix-route-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/devfix-route-1002`.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h 551f07e0..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing. Carried.
- (vii) card records: `ls tests/ops` → `test_desk_launch_devfix.py`, `test_desk_size_guard.py`, `test_devdb_lock.py`, `test_install_ops.py` (02 / 07 landed before BASE); `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` → `38:OPS_DESK_PREFIX = "ops/desk/"` · `226:…path.startswith(OPS_DESK_PREFIX)` (the lift is on BASE: no `restarts.py` edit owed). The R41 record: the line as built carries the two lock-script strings and `--add-dir /Users/cobalt/.claude/ops`; I checked it against `BUILD-HUB.md:12` at BASE and raised nothing on it.
- (viii) L32: this report holds no ticker, price or date of his; `devfix-x_tablé.md`, `user.x_table` and `test_x_proof.py` are constructed test values.

COUNTING: findings 2 (O1, O2; no house) · dropped 0 · held 2 · fixed 2 · held unfixed 0 · open 0.

## OPEN
none

## CONTINUE
next: done (stop line below).

## DECISIONS
none

## RECORDS
- Started 14:11:02 EDT (date). House A: none (overruled 2026-10-02 R47): no house gate, no probe, no staging, no `HOUSE-INSTRUCTIONS.md`; `<S>` holds only `opus-1.md`.
- Dropped findings: none. Houses that produced nothing: none sat.
- `REFUSED, not needed: git diff 551f07e0 -- "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" — fatal: … is outside repository at '/Users/cobalt/cobalt-wt/devfix-route-1002'` (a git error, not a permission refusal). I read main's THE LOCK and W directly instead.
- One lock take (W), 14:26 → 14:43:22 EDT; no extra take. The build report's DECISIONS were answered by the judge seat at 2026-10-02 R41 (the card's records). I re-opened none of them; O1 is a new instance in the new code, not DECISION 1's older checks.
- The L74 line: above, once.
- files opened: 11 — `CHECK-HUB.md`, the card, `DEVFIX-HUB.md`, `tests/ops/test_desk_launch_devfix.py`, the build report, `ops/desk/desk-launch.sh`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `BUILD-HUB.md` in the worktree (= BASE) and on main, `CARD.md` and `STANDING-LIST.md` (by their diff). Also the three background-task output files of my own suite runs.
- Check of `devfix-route`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: devfix-route · pass: 1 · tip: 46712ab4 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0
