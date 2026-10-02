# worker-steps — check, pass 1 (2026-10-02)

## §0 Headline
- House A: none (overruled 2026-10-02 R47). Own read found 3 defects in `ops/desk/gate.sh`. All 3 HELD (red on `8f3c4876`) and all 3 are fixed (`0740722d` red, `e416589c` fix).
- O1: F2 = F0 could pass vacuously when one stderr line came before the fingerprint header. O2: a TERM during the lock take left `.env` and the lock behind. O3: the offline run inherited the caller's `COBALT_ENV`.
- W on `e416589c`: offline 3784/0 · with-DB 4554/0 (4383 + 171) · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: none.
- open 0 · house B: not needed · ready: YES · decisions: 0.

## L74
- None in a tool result. The session's own harness attribution reminder named a `Claude-Session:` line; per L74 and CHECK-HUB, commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started `Fri Oct  2 15:24:25 EDT 2026`.
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" CHECK-HUB.md` | 1 | (nothing) |
| card no placeholder | `grep -n -E "«FIL[L]" <card>` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- <card>` | 0 | `032d83a1b48625d592d79d579feafdc6619eab1c` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | line 46, `**HIS RULING**` … `APPROVED` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R47 (also HOUSE A overrule) | `grep -n "^| R47 " cto-2026-10-02.md` | 0 | line 54, `HIS RULING` … `HIS RULING · APPROVED` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| house gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | line 35, one row |
| house gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | line 37, one row |
| R19 committed | `git -C … log -1 --format=%H -S"| R19 |" -- cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 15:24:25 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/worker-steps-1002` |
| tip | `git log --oneline -1` | 0 | `65733f2a docs(worker-steps): build report — 8f3c4876` |
| docs-only above TIP | `git log --stat --format=%h 8f3c4876..HEAD` | 0 | `65733f2a`, `62ebfe0d`: each only `.../reports/worker-steps-build-2026-10-02.md` |
| built | `tail -n 3 <REPORT>` | 0 | `BUILT · job: worker-steps · tip: 8f3c4876 \| on 9fa18f14 \| migration: none \| offline 3784/0 \| with-DB 4554/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 3 · for Dejan: 0` |
| range | `git log --oneline 9fa18f14..8f3c4876` | 0 | `8f3c4876 feat(worker-steps): …(S1-S5, L3, L76, L35)` · `7e4ecee2 wip(worker-steps): red — the five step scripts do not exist (S1-S5)` |
| range paths | `git log --stat --format=%h 9fa18f14..8f3c4876` | 0 | `ops/desk/{authorize,gate,house-probe,preflight,stage-set}.sh`, `tests/ops/test_{authorize,gate,house_probe,preflight,stage_set}.py` |
| no .env here | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47); no house gate launch, no probe |

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Written before any run.

FINDING O1
ROW: S3 (X1)
CLAIM: `fingerprint` reads `<FP>`'s value as line 2 of the command's stdout AND stderr merged (`ops/desk/gate.sh:195` `> "$tmp/seg" 2>&1`, `ops/desk/gate.sh:299` `sed -n '2p'`); `cobalt db query` prints the header then the row on stdout (`src/cobalt/db_query.py:204-206`), so one stderr line before it (a `uv` warning) makes line 2 the header in F0 and F2 alike: `F2 = F0` holds while cobalt_dev is NOT back at 0013, exit 0.
RUN: TEST `tests/ops/test_gate.py::test_check_o1_a_warning_line_before_the_fingerprint_does_not_hide_a_changed_f2` — the three fingerprints each start with one `warning:` line, the third value row differs.
EXPECT: on the tip `assert done.returncode == 6` fails with 0.

FINDING O2
ROW: S3 (X1)
CLAIM: `take` runs `take-devdb-lock.sh` (it waits up to 90 min) before `taken=1` (`ops/desk/gate.sh:257-262`); a TERM that arrives while it runs is handled after the take returns 0, `cleanup` sees `taken` empty (`ops/desk/gate.sh:327`) and never releases: `.env` and the lock stay.
RUN: TEST `tests/ops/test_gate.py::test_check_o2_a_term_during_the_lock_take_still_releases` — a take stub that writes a marker, sleeps 2 s, then copies `.env`; SIGTERM to gate.sh on the marker.
EXPECT: on the tip `assert not (job / ".env").exists()` fails, and the release stub is never called.

FINDING O3
ROW: S3 (vii), X2
CLAIM: gate.sh passes the caller's environment through (`ops/desk/gate.sh:195` eval, no unset), so a caller with `COBALT_ENV` exported runs W (a) offline with `COBALT_ENV=dev`, not as the hub types it (no prefix, `BUILD-HUB.md` W (a)); the row's "(vii) offline makes one `uv run pytest` call with no `COBALT_ENV`" holds only because the test pops it (`tests/ops/test_gate.py:146`).
RUN: TEST `tests/ops/test_gate.py::test_check_o3_offline_runs_with_no_cobalt_env_even_when_the_caller_has_one`.
EXPECT: on the tip `assert call["COBALT_ENV"] is None` fails with `'dev'`.

X1–X4, read only (no finding beyond O1–O3): X1 — every other exit path traced in `cleanup` (`ops/desk/gate.sh:320-337`): a red, a failed query, exit 5, a refused livenote, INT/HUP/TERM after the take all roll back when `applied` and release when `taken`; O1, O2 are the two that do not hold. X2 — the order and prefixes match W (b)–(f) and THE LOCK; pinned by `test_withdb_green_runs_the_hub_commands_byte_for_byte_in_order`; O3 is the one environment gap. X3 — `authorize.sh` proves each row in `cto-<date>.md` of the card's own date (`ops/desk/authorize.sh:84`), committed by `-S` and present at HEAD (`:103-116`); no path found to AUTHORIZED for an uncommitted, unapproved or other-file row (see `## RECORDS` for the literal-text note). X4 — every staged file is written from `git show` and proved by `git hash-object --no-filters` against `git rev-parse` (`ops/desk/stage-set.sh:110-116`); the dest is pinned under `agy-trial/scratch/` with `..` refused (`:42-46`); git paths carry no `..`.

## Findings
none — no house.

## Dropped
none.

## RUNS
Each run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::<test>`, on `8f3c4876`'s code. No form repair was needed.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `test_check_o1_a_warning_line_before_the_fingerprint_does_not_hide_a_changed_f2` | `1 failed` · `assert 0 == 6`; stdout `cobalt_dev: 0013 — F2 = F0` with F2 ≠ F0 | HELD |
| O2 | own | `test_check_o2_a_term_during_the_lock_take_still_releases` | `1 failed` · `AssertionError: .env: STILL PRESENT — …/wt/x-job/.env` | HELD |
| O3 | own | `test_check_o3_offline_runs_with_no_cobalt_env_even_when_the_caller_has_one` | `1 failed` · `AssertionError: assert 'dev' is None` | HELD |
Red commit: `0740722d wip(worker-steps): check red — O1 O2 O3`.

## FIXES
| id | file | fix | after |
|---|---|---|---|
| O1 | `ops/desk/gate.sh` `fingerprint` | the value row is the line after the `cols rels views_md5` header (awk), never line 2 of stdout+stderr | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `80 passed, 15 warnings in 25.84s` |
| O2 | `ops/desk/gate.sh` `take` | `taken=1` before `take-devdb-lock.sh` runs, cleared on a non-zero exit; the release gives back only a lock that names this worktree (`git show aeefb6df:ops/desk/release-devdb-lock.sh`) | same run |
| O3 | `ops/desk/gate.sh` top | `unset COBALT_ENV COBALT_LIVE_VAULT_ROOT`: the only prefixes are the hub's | same run |
Commit: `e416589c fix(worker-steps): gate.sh reads F after its header, releases a lock taken under a signal, and drops the caller's COBALT_ENV (check O1 O2 O3)`. No DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (`grep` of `ops/desk` there hits only `jobs/restarts.md`), and the card fences every existing file.

## Suites
On `e416589c`, BUILD-HUB `## RESTARTS` then `## W` whole:
- RESTARTS: `uv run cobalt jobs restarts 9fa18f14..HEAD` → 11 rows (the build report: DOCS; five `ops/desk/*.sh`: `operator script; no Cobalt reader`; five `tests/ops/*`: `test/documentation; no resident`), last line `RESTARTS: none`.
- (a) offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 567.06s (0:09:27)` → **offline 3784/0**. The lock was taken only after it finished.
- (b) lock: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `cp …/.env …/worker-steps-1002/.env`; `ls -la …/*/.env` → the one line `…/worker-steps-1002/.env`. `<FP>` → F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `migrate --proof-only` → `PROOF ONLY on cobalt_dev`; the post-0013 tables (`drc_*`, `legs`, `prediction_records`, `voice_turns`) are absent, i.e. at 0013; `NOTHING WAS APPLIED`.
- (c) pass 1, the hub's command byte for byte (no deselect added) → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 704.72s (0:11:44)`. The SKIPPED lines: `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev) · `test_cards_picks.py:401` (real S2-P2 0007 applied…) · `test_radar_evaluate.py:695`, `test_s3_c4_experiments.py:95`, `taxonomy/test_catalyst.py:365`, `taxonomy/test_predicate.py:262` (COBALT_LIVE_VAULT_ROOT not set — the hub runs …) · `test_replay_line.py:266` (requires_vault: COBALT_TEST_LIVE_DRC …).
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` → applied up to `0022_prediction_records.sql`, `content UNCHANGED on every table.`; **dev forward: APPLIED 15:51:14**. F1 `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2, the hub's command byte for byte → `171 passed, 1 deselected, 5 warnings in 220.45s (0:03:40)`. with-DB = 4383 + 171 = **4554/0**.
- (c3r) not run: this build adds no with-DB test and writes no ticker (TREE STATE: unchanged).
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → 0022 … 0014 reversed newest first, `content UNCHANGED on every table.`; F2 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **cobalt_dev: 0013 — F2 = F0**. `rm …/worker-steps-1002/.env`; `ls …/.env` → `No such file or directory`; `ls -la …/*/.env` → `no matches found` → **.env: removed, proven gone (W)**.
- (e) live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.43s`; the one skip is `COBALT_TEST_LIVE_DRC`, and none names COBALT_LIVE_VAULT_ROOT → **live-note 146/0**.

## Scope
Path union of the range: `ops/desk/authorize.sh`, `ops/desk/gate.sh`, `ops/desk/house-probe.sh`, `ops/desk/preflight.sh`, `ops/desk/stage-set.sh`, `tests/ops/test_authorize.py`, `tests/ops/test_gate.py`, `tests/ops/test_house_probe.py`, `tests/ops/test_preflight.py`, `tests/ops/test_stage_set.py` — each in a row's `files`. My commits touch `tests/ops/test_gate.py` and `ops/desk/gate.sh` only (row S3's files).

## Checked against the branch
- (i) `git log --oneline 8f3c4876..HEAD -- . ":(exclude)docs"` → `e416589c fix(worker-steps): …(check O1 O2 O3)` · `0740722d wip(worker-steps): check red — O1 O2 O3`; tip now = `e416589c`.
- (ii) `git log --stat --format=%h 8f3c4876..HEAD` → `e416589c` `ops/desk/gate.sh` · `0740722d` `tests/ops/test_gate.py` · `65733f2a`, `62ebfe0d` the build report (docs). No other path; no WIDENED.
- (iii) fence: `git log --oneline 9fa18f14..HEAD --` BUILD-HUB.md, CHECK-HUB.md, DEPLOY-HUB.md, STANDING-LIST.md, `ops/desk/desk-launch.sh`, `ops/desk/stage-copy.sh` → empty. `git diff --stat 9fa18f14 HEAD -- src configs` → empty. Every path in the range is an added file (RESTARTS `change` = `A`), so no existing file was edited.
- (iv) `grep -n -F "def test_check_o" tests/ops/test_gate.py` → `430` O1 · `440` O2 · `471` O3, one each; `0740722d` (red) sits below `e416589c` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/worker-steps-1002`.
- (vi) TREE STATE unchanged: `git log --stat --format=%h 9fa18f14..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. Carried.
- (vii) None of the card's `## RECORDS` lines names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command; nothing to re-run.
- (viii) L32: this report holds only constructed test values and `cobalt_dev` schema fingerprints; no ticker, price or date of his.
- COUNTING: findings 3 (own 3, house 0) · dropped 0 · held 3 · fixed 3 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: done

## DECISIONS
none.

## RECORDS
- No house sat: the card's `HOUSE A: none — overruled 2026-10-02 R47` (R47 proved under AUTHORIZATION). `## 1` and `## 3` were not run, `<S>` was never created, and `<S>/opus-1.md` was not written because house B is not needed and no pass 2 follows.
- The session's harness carried a reminder to add a `Claude-Session:` trailer to commits. Per CHECK-HUB L74, the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- X3, a literal-text note (not a finding): `authorize.sh` accepts a row that holds `HIS RULING` and then the text `APPROVED` anywhere after it (`ops/desk/authorize.sh:97`), exactly as the hub's AUTHORIZATION grep rule reads; a row whose cell says `NOT APPROVED` would pass both. The script mirrors the hub, and the card says S1 does what the hub says, no more.
- R41 (1), the level read: `migrate --proof-only` prints no `CHANGED` in any state (`src/cobalt/db_migrations/cli.py:680-691`), so `gate.sh`'s "no CHANGED" test on it can never fire; its real guard is `on cobalt_dev` plus exit 0. This is the known follow-up R41 (1) names (a `LEVEL` line, the 2026-10-03 adoption card), not a finding.
- No DevDocs line: no module page covers `ops/desk/`, and the card fences every existing file.
- One lock take (W), none extra.
- Read, not reached: `areas/cobalt.md` (WHAT YOU READ (5)) was not opened; the build report was read by `tail` only (its last line); `tests/ops/test_{authorize,preflight,stage_set,house_probe}.py` were not opened (the 80-test `tests/ops` run covers them green).
- files opened: 14 — CHECK-HUB.md; the card; BUILD-HUB.md (worktree, `## AUTHORIZATION` → `## W`); `ops/desk/{gate,authorize,preflight,stage-set,house-probe}.sh`; `tests/ops/test_gate.py`; `src/cobalt/db_migrations/cli.py` (440–489, 575–694); `src/cobalt/db_query.py` (grep); `git show aeefb6df:ops/desk/take-devdb-lock.sh`; `git show aeefb6df:ops/desk/release-devdb-lock.sh`; the build report (`tail -n 3`).
- Check of `worker-steps`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: worker-steps · pass: 1 · tip: e416589c · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0
