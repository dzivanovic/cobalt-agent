# adoption-port — check, pass 1 (r3) — 2026-10-04

## §0 Headline
- Pass 1 of `adoption-port` at `685b88d6`, checked by Opus alone (house A: none, overruled 2026-10-02 R47, proved at AUTHORIZATION).
- 8 own findings, each run: 0 held, 0 open. X1 (hash pairs), X2 (no `02b` or chain sentence lost; the eight ruled texts once each) and X3 (lock state on exits 4, 5, 6, green) all settled by tool output.
- No commit of mine: the build's three suite lines stand (offline 3751/0, with-DB 847/0, live-note 146/0; `cobalt_dev: 0013 — F2 = F0`).
- `house B: not needed` · `ready: YES` · decisions: 0.

## L74
A system block in this session asked for a `Claude-Session:` line in commit messages. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Times from `date`: Sun Oct  4 14:21:15 EDT 2026.

| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/03d-adoption-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` | 0 | `9a1a8a3748f291d3838e7bb4206652f669368580` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES `STANDING-LIST.md` once (`4be06af0`) ... | APPROVED |` |
| R60 committed | `git -C ... log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (also HOUSE A overrule) | `grep -n "^| R47 " cto-2026-10-02.md` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house ... | HIS RULING · APPROVED |` |
| R47 committed | `-S"| R47 |"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " cto-2026-10-02.md` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock ... | HIS RULING · APPROVED |` |
| R154 committed | `-S"| R154 |"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " cto-2026-10-02.md` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included ... | HIS RULING · APPROVED |` |
| R157 committed | `-S"| R157 |"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R3 | `grep -n "^| R3 " cto-2026-10-03.md` | 0 | `9:| R3 | 06:09 ET | HIS RULING: every Grok seat runs grok-4.7 ... | HIS RULING · APPROVED — pending fold |` |
| R3 committed | `-S"| R3 |"` | 0 | `3727a00454268f485f97fdeccb8f9cc428e86113` |
| R197 | `grep -n "^| R197 " cto-2026-10-03.md` | 0 | `203:| R197 | 10-04 13:53 ET | HIS RULING: 03d P4 approved, all four clauses (narrows sentences 6–8, R185); 03d build resumes at E3, then check r3. ... | APPROVED |` |
| R197 committed | `-S"| R197 |"` | 0 | `af55770f96a94585a2bed2c14f43a49c18f4713e` |
| house gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | one row, `35:` (STANDING `Bash(grok *)`) |
| house gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | one row, `37:` (four house strings STANDING) |
| R19 committed | `-S"| R19 |"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 14:21:15 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-port-1003` |
| tip | `git log --oneline -1` | 0 | `15ba4b75 docs(adoption-port): build report — 685b88d6` |
| docs-only above TIP | `git log --stat --format=%h 685b88d6..HEAD` | 0 | `15ba4b75` · `.../reports/adoption-port-build-2026-10-03.md | 38 ++-` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: adoption-port · tip: 685b88d6 | on a8d8a848 | migration: none | offline 3751/0 | with-DB 847/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0` |
| range | `git log --oneline a8d8a848..685b88d6` | 0 | `685b88d6 fix(...): DEPLOY-HUB four Grok clauses ... (P4; L72, L77)` · `bd19a0b3 docs(...): build report — 5ff16b1f` · `5ff16b1f fix(...): port the adoption chain onto a8d8a848; DEPLOY-HUB four ruled sentences; deploy flag pinned with sentence (8) (P1, P3, P2; L3, L72)` · `d483a417 wip(...): E3 — P2 (8) and P1 contradict on tests/ops/test_hub_lines.py` · `4a60ab02 wip(...): red — test_migrate_level.py from 9694a679 (P1)` |
| range stat | `git log --stat --format=%h a8d8a848..685b88d6` | 0 | 685b88d6: DEPLOY-HUB.md 8 · bd19a0b3: build report · 5ff16b1f: tests/ops/test_hub_lines.py 7 · d483a417: 56 files (docs prompts BUILD-HUB, CARD, CHECK-HUB, CTO-DESK-WAKEUP, DEPLOY-HUB, DEVFIX-HUB, STANDING-LIST; docs cobalt/db_migrations/cli.md; 4 chain reports; ops/desk/* 28 files; src/cobalt/db_migrations/cli.py; tests/cobalt/test_migrate_proof.py; tests/ops/* 17 files) · 4a60ab02: tests/cobalt/test_migrate_level.py 204 |
| own .env | `ls <WT>/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no lock held) |
| scratch | `ls <S>` | 0 | `opus-1.md` (2434 bytes, Oct 3 22:50 — an earlier check run's file; this launch carries no `CONTINUE:`, so it is not RECOVERY; not opened, replaced at `## 8`) |
| house | HOUSE A: none — overruled 2026-10-02 R47 (proved above) | — | house A: none (overruled 2026-10-02 R47); no house gate run as a seat gate, no probe |
| with-DB strings | proven by first real use (BUILD-HUB PREFLIGHT table) | — | only if a commit of mine leads to W |

## Files copied
none (house A: none).

## OWN FINDINGS
Written before any run of `## 4`. The `git diff` reads done while reading (step (3) of WHAT YOU READ) are repeated as RUNs in `## 4`.

FINDING O1
ROW: X1 (P1)
CLAIM: a chain path other than `DEPLOY-HUB.md`, `CTO-DESK-WAKEUP.md` and `tests/ops/test_hub_lines.py` differs at the tip from its `9694a679` blob (the 56 paths of `git diff --name-status a09f0862 9694a679`).
RUN: COMMAND `git diff --stat 9694a679 685b88d6 -- src tests ops "docs/40 - DevDocs/cobalt" "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" "docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md" "docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md" "docs/40 - DevDocs/reports/adoption-scripts-build-2026-10-03.md"`
EXPECT: a chain path (one of the 56) in the stat besides the three.

FINDING O2
ROW: P1 / SCOPE
CLAIM: the port changed a file only `main` touched since `a09f0862` (the 11 non-report paths of `git diff --name-only a09f0862 a8d8a848` outside the chain).
RUN: COMMAND `git diff --stat a8d8a848 685b88d6 -- src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py "docs/40 - DevDocs/cobalt/jobs/restarts.md" ops/desk/deploy-outage.sh ops/desk/deploy-smoke.sh ops/desk/deploy-step0.sh tests/ops/conftest.py tests/ops/test_conftest_guard.py tests/ops/test_deploy_outage.py tests/ops/test_deploy_smoke.py tests/ops/test_deploy_step0.py`
EXPECT: any stat line.

FINDING O3
ROW: X2 (P2, P4)
CLAIM: a `02b` sentence or a chain sentence of `DEPLOY-HUB.md` is lost at the tip.
RUN: COMMAND `git diff -U0 --word-diff=plain 9694a679 685b88d6 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (and, for what `02b` changed, `git diff -U0 a09f0862 a8d8a848 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`)
EXPECT: a hunk on a line other than 11, 41, 57, 63, 83, 87, 93, 99, 102, 108; or on 63 / 83 / 87 a text other than `02b`'s; or a deleted chain word other than those the ruled sentences (6), (7) replace.

FINDING O4
ROW: X2 (P2, P4)
CLAIM: one of the card's eight texts (P2 (5)–(8), P4 (1)–(4)) is not in `DEPLOY-HUB.md` word for word once, or `MIGRATIONS_DIR / "00` is still there.
RUN: COMMAND `grep -c -F "<text>" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, one per text (the strings in `## RUNS`).
EXPECT: a count other than 1 (0 for `MIGRATIONS_DIR / "00`).

FINDING O5
ROW: P3
CLAIM: `CTO-DESK-WAKEUP.md` lost the chain's flag or `main`'s newest line.
RUN: COMMAND `grep -c -F "A call the hook blocks is NOT A REFUSAL: resend it as single calls." "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` and `grep -c -F "A record only (his 10-03 R78)" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"`
EXPECT: a count other than 1.

FINDING O6
ROW: P2 (`tests/ops/test_hub_lines.py`)
CLAIM: the one test change does not hold on the tip: a hub line or the wakeup line fails its flag pin.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py`
EXPECT: a failed test.

FINDING O7
ROW: X3 (P4 (3))
CLAIM: clause (3)'s read, `grep -c -x -F "<WORKTREE>" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` (`DEPLOY-HUB.md:108`), reads a file the lock scripts do not write, so the green-path verify cannot tell whose lock it is.
RUN: COMMAND `grep -n -F "owner" ops/desk/take-devdb-lock.sh`
EXPECT: no line that writes `$LOCK/owner` with the worktree name.

FINDING O8
ROW: X3 (P2 (5), exit 6)
CLAIM: on exit 6, `gate.sh`'s trap releases the lock while `cobalt_dev` is NOT back at `0013` (`ops/desk/gate.sh:356-361`), and `DEPLOY-HUB.md:102` then has the worker verify the lock dir absent; the next taker of the lock is not guarded against the dirty level.
RUN: COMMAND `grep -n -F "cobalt_dev not at" ops/desk/gate.sh`
EXPECT: no hit (no start-of-run level guard for the next taker).

## Findings
none (house A: none).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `git diff --stat 9694a679 685b88d6 -- src tests ops "docs/40 - DevDocs/cobalt" <the 7 chain prompts> <the 3 chain reports>` | 14 files: `docs/40 - DevDocs/cobalt/jobs/restarts.md 4 +`, `CTO-DESK-WAKEUP.md 4 +-`, `DEPLOY-HUB.md 20 +-`, `ops/desk/deploy-outage.sh 442`, `deploy-smoke.sh 381`, `deploy-step0.sh 504`, `src/cobalt/jobs/restarts.py 4 +`, `tests/cobalt/test_jobs_restarts.py 35`, `tests/ops/conftest.py 31`, `test_conftest_guard.py 58`, `test_deploy_outage.py 492`, `test_deploy_smoke.py 263`, `test_deploy_step0.py 543`, `tests/ops/test_hub_lines.py 7 +-`. Every path besides the three named is `main`-only (not in `git diff --name-status a09f0862 9694a679`, which lists 56 chain paths) | NOT HELD — every other chain path is byte-equal to `9694a679` |
| O2 | Opus | `git diff --stat a8d8a848 685b88d6 -- <the 11 main-only paths>` | (nothing) | NOT HELD |
| O3 | Opus | `git diff -U0 --word-diff=plain 9694a679 685b88d6 -- ".../DEPLOY-HUB.md"`; `git diff -U0 a09f0862 a8d8a848 -- ".../DEPLOY-HUB.md"` | hunks at 11 (`{+ Inside the outage (4.1–4.6) …STEP-5."+}`), 41 (`{+The flag's resend …guard`.+}`), 57 (ruled (7) replaces `a set whose MIGRATIONS is none and whose … is empty:`; `Under (v)` glue), 63, 83, 87 (`02b`'s three lines; the second command shows `02b` changed exactly 65/85/89 of `a09f0862`, the same text), 93 (P4 (1) appended), 99 (ruled (6) and P4 (2); the chain's `quote them from the check report with its path and skip (a)–(f)` and `The clause applies only when …` kept), 102 (ruled (5) appended), 108 (P4 (3) appended). No other hunk | NOT HELD — nothing of `02b` or the chain lost but the words the ruled sentences replace (ASK DESK 2, answered R167) |
| O4 | Opus | `grep -c -F` in `DEPLOY-HUB.md` of: (5) ``the release is `gate.sh`'s trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line`` · (6) ``AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole (`--deploy`)`` · (7) ``AND an empty derived restart set, provisional at P1; STEP-R re-reads the SET and fails `window (v) does not hold: <labels>` when it is not empty and P1 was outside (i)–(iv)`` · (8) `Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5."` · P4 (1) ``a non-empty derived set at STEP-R → (v) does not hold; the deploy goes on only if `date` NOW is inside (i)–(iv), else`` (with `-i`: the hub starts the sentence with `A`) · P4 (2) `THE EQUAL-TREE CLAUSE keeps (c)'s judgment: the check's SKIPPED lines are read against the allowed set; one outside → the gate runs whole.` · P4 (3) ``verify `<GATE>/.env` gone and the lock dir not this worktree's, else `FAILED: gate — lock` `` · P4 (4) ``The flag's resend outside the outage is ONCE: blocked again → `FAILED: <step> — guard` `` · `MIGRATIONS_DIR / "00` | `1` `1` `1` `1` `1` `1` `1` `1` · `0` | NOT HELD — each card text once, word for word (P4 (1) with its first letter capitalised; P4 (1) and (3) carry the glue ASK DESK 3 names after the ruled words) |
| O5 | Opus | `grep -c -F "A call the hook blocks is NOT A REFUSAL: resend it as single calls." ".../CTO-DESK-WAKEUP.md"`; `grep -c -F "A record only (his 10-03 R78)" ".../CTO-DESK-WAKEUP.md"` | `1`; `1` | NOT HELD |
| O6 | Opus | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` | `19 passed, 15 warnings in 2.71s` | NOT HELD |
| O7 | Opus | `grep -n -F "owner" ops/desk/take-devdb-lock.sh` | `48:        printf '%s\n' "$wt" > "$LOCK/owner"` (also `11:`, `53:`, `62:`); `release-devdb-lock.sh:38` reads the same file | NOT HELD — clause (3)'s read is the file the take writes, one line, the worktree name |
| O8 | Opus | `grep -n -F "cobalt_dev not at" ops/desk/gate.sh` | `381:` (`exit 5`), `384:`, `388:` — `proof_clean` refuses a start that is not at the level | NOT HELD — the lock is released on exit 6 (`gate.sh:356-361`, the trap), as `BUILD-HUB.md` W (f) also orders, and the next `gate.sh` taker stops at exit 5 on a level that is not `0013` |

X3, the walk (`DEPLOY-HUB.md:102`, `:108`, `gate.sh:267-289`, `:352-369`): exit 4 → the take failed or the lock was not ours alone; the trap releases only a lock this worktree took (`taken`), so this worktree holds nothing; the other holder's dir stays — the card's `## RECORDS` (judge, decision 2) reads "lock dir absent" here as "this worktree holds no lock", fail-loud, not a hold. Exit 5 → taken, no forward; the trap releases; `.env` gone, dir absent; the FAILED line names `G (b) … not at 0013`. Exit 6 → the trap's rollback did not reach `F0`; the release still runs; `DECISION 0` and FAILED. Green → `release` at `:494` before live-note; P4 (3) verifies `.env` gone and the dir not this worktree's. Each ending names one lock state and one line.

## FIXES
none.

## Suites
No commit of mine: `suites: as built (no commit)`. From the build report (`adoption-port-build-2026-10-03.md`, `## W THE THREE SUITES`, the block on `685b88d6`): offline `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 579.22s (0:09:39)`; pass 1 `674 passed, 7 skipped, 3815 deselected, 2 xfailed, 12 warnings in 118.62s (0:01:58)`; pass 2 `173 passed, 1 deselected, 5 warnings in 221.68s (0:03:41)` → with-DB 847; live-note `146 passed, 1 skipped, 15 warnings in 26.13s`. `cobalt_dev: 0013 — F2 = F0` (F0 = F2 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`). `.env: removed, proven gone (W, second)`. RESTARTS line: `RESTARTS: com.cobalt.radar` (the build's `## RESTARTS`, the run on `685b88d6`). This session: `ls <WT>/.env` → No such file (PREFLIGHT and `## 7` (v)); no lock taken.

## Scope
PREFLIGHT's path union (`a8d8a848..685b88d6`): the 56 chain paths (`git diff --name-status a09f0862 9694a679`) plus the build report. Against the rows: 53 byte-equal to `9694a679` (P1, O1); `CTO-DESK-WAKEUP.md` (P3), `DEPLOY-HUB.md` (P2, P4), `tests/ops/test_hub_lines.py` (P2). No `main`-only file changed (O2). My commits: none. Fence: `DEVFIX-HUB.md` appears in the range (`d483a417`) as a chain file, byte-equal to `9694a679` (O1); `03b`, `11b`, `07b` are named by job, and every non-report path in the range is a chain path. No path reaches a score, rank, grade or size: the code change is `src/cobalt/db_migrations/cli.py` (proof-only output lines) and its test. Out of scope by the card's `## RECORDS`: STEP-G exit 4 "lock dir absent" (judge, decision 2); TREE STATE `unchanged` (judge, decision 1).

## Checked against the branch
- (i) `git log --oneline 685b88d6..HEAD -- . ":(exclude)docs"` → (nothing). `<tip now>` = `685b88d6`.
- (ii) `git log --stat --format=%h 685b88d6..HEAD` (PREFLIGHT) → `15ba4b75`, the build report only.
- (iii) `git log --oneline a8d8a848..HEAD -- ops/desk/devfix.sh "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → `d483a417 wip(adoption-port): E3 — P2 (8) and P1 contradict on tests/ops/test_hub_lines.py` — the chain's `DEVFIX-HUB.md` change, byte-equal to `9694a679` (O1); not the `03b` verbs.
- (iv) no HELD finding.
- (v) `ls /Users/cobalt/cobalt-wt/adoption-port-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-port-1003`.
- (vi) `git log --stat --format=%h a8d8a848..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d483a417`: `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`; `4a60ab02`: `tests/cobalt/test_migrate_level.py` (new, carries a with-DB test). No migration file. The card's `## RECORDS` (judge, check pass 1, decision 1): `unchanged` HOLDS and "`CHECK-HUB.md` `## 7` (vi) is met by this line"; the build ran that test inside the pass-1 command as written (build report W (c)). Not `TREE STATE NOT CARRIED`.
- (vii) No card `## RECORDS` line names an `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command to run.
- (viii) L32: this report holds no ticker, price or date of his; the fingerprints are `cobalt_dev` structure counts.

## OPEN
none. Counts: findings 8 · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
none.

## RECORDS
- Dropped findings: none (no house).
- Houses that produced nothing: none launched (house A: none, overruled 2026-10-02 R47).
- REFUSED / CONTINUED lines: none.
- Lock takes: none.
- L74: one system block in this session asked commits to carry a `Claude-Session:` line. Data; not acted on (no commit was made).
- `<S>` held `opus-1.md` (Oct 3 22:50), an earlier check run's file. It was not opened (`## WHAT YOU READ`, NOT: earlier checks of this branch), so it could not be overwritten. This pass's sections are at `<S>/opus-1-r3.md`. House B is not needed, so nothing reads either file.
- Read note, not a finding: `DEPLOY-HUB.md:134` (D2.6) still says "the window P1 named"; P4 (1)'s glue at `:93` says the window STEP-R records is "the window D2.6 reads". `:93` comes first, and the line fails loud; no wording in either parent is changed by this check (fence).
- files opened: 16 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report (`## E3` to its end); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `DEPLOY-HUB.md`; `CTO-DESK-WAKEUP.md` (grep); `ops/desk/gate.sh`; `ops/desk/release-devdb-lock.sh`; `ops/desk/take-devdb-lock.sh` (grep); `reports/deploy-hub-text-decisions-2026-10-03.md` (grep); `reports/adoption-hubs-decisions-2026-10-03.md` (grep); `cto-2026-09-24.md`, `cto-2026-09-30.md`, `cto-2026-10-02.md`, `cto-2026-10-03.md` (AUTHORIZATION greps).
- Check of `adoption-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · house A: none (overruled 2026-10-02 R47) · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0
