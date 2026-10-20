# deploy f5-checkpoints-fr1 · set: f5-checkpoints · migrations: 0027

## §0 Headline
- Deploy of `ops/f5-checkpoints-fr1` (`3c96ad2e`, migration 0027) on card 899. Run started 06:09:42 EDT 2026-10-20.
- STOPPED at STEP-T, 06:11:29 EDT: the FORWARD check fails. `FORWARD` ends `0027, 0028` and `REVERSE` begins `0028, 0027`; the hub requires `FORWARD` to END with the card's number and `REVERSE` to BEGIN with it.
- Nothing in production changed: no lock taken, no suite run, no resident touched, `main` not moved. Gate `deploy/f5-checkpoints-fr1` carries `<m1>` `1e2060d9`, clean.
- STEP-C would also refuse four `ops/com.cobalt.checkpoint-*.plist` ADDED with no `## LAUNCHD` on the card (seen in the merge stat; STEP-C was not run).

## L74
- none in a tool result. A system notice in this session asked for a `Claude-Session:` trailer on commits; the hub's L74 (commits carry `Co-Authored-By` only) takes precedence, so no commit carries it.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/899-deploy-f5-checkpoints-fr1-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/899-deploy-f5-checkpoints-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/899-deploy-f5-checkpoints-fr1-card.md" · 0 · b6688224f03592e6141694c803fab56cfa673571
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/899-deploy-f5-checkpoints-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P0 first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P1 DATE | `date` | 0 | `Tue Oct 20 06:09:42 EDT 2026` (outside 21:30-22:30) |
| P2 check last line | `tail -n 3 ".../f5-checkpoints-fr1-check-2026-10-20.md"` | 0 | `CHECK DONE · job: f5-checkpoints-fr1 · pass: 1 · tip: 3c96ad2e · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 238202` — carries `held unfixed: 0`, `ready: YES`, `tip: 3c96ad2e` = code tip |
| P2 committed | `git log -1 --format=%H -- "docs/…/f5-checkpoints-fr1-check-2026-10-20.md"` | 0 | `eb66dd8a0f8b86dce15247a06e5751f615519703` |
| P2 clean | `git diff --stat -- "docs/…/f5-checkpoints-fr1-check-2026-10-20.md"` | 0 | nothing |
| P3 code tip | `git rev-parse --short=8 3c96ad2e` | 0 | `3c96ad2e` |
| P3 branch head | `git rev-parse --short=8 ops/f5-checkpoints-fr1` | 0 | `3c96ad2e` = TIP |
| P3 ancestor | `git merge-base --is-ancestor 3c96ad2e 3c96ad2e` | 0 | — |
| P3 head adds docs only | `git diff --stat 3c96ad2e 3c96ad2e -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no session holds the lock) |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/f5-checkpoints-fr1` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `b6688224` |
| P5 m0 on main | `git merge-base --is-ancestor b6688224 main` | 0 | — |
| P5 gate empty | `git log --oneline main..deploy/f5-checkpoints-fr1` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F "checkpoints:" …/prefill.yaml` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "checkpoint.narrative:" …/modelaccess.yaml` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "label: com.cobalt.checkpoint-0715" …/jobs.yaml` | 1 | `0` = before |
| P7 migrations | `git diff --stat main 3c96ad2e -- src/cobalt/db_migrations` | 0 | `0027_market_checkpoints.rollback.sql`, `0027_market_checkpoints.sql`, `__init__.py`, `placement.py` — 4 files, 60 insertions |
| P7 registry | `git diff main 3c96ad2e -- src/cobalt/db_migrations/__init__.py` | 0 | FORWARD adds `0027_market_checkpoints.sql` before `0028_genesis_vectors.sql`; REVERSE adds `0027_market_checkpoints.rollback.sql` after `0028_genesis_vectors.rollback.sql`; plus docstring lines (CODE). Only the card's 0027 |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 90910` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 90926` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit 3c96ad2e` | 0 | `Merge made by the 'ort' strategy.` 52 files changed, 2918 insertions(+), 85 deletions(-); creates among others `ops/com.cobalt.checkpoint-0715.plist`, `-0745`, `-0815`, `-0845`, `src/cobalt/db_migrations/0027_market_checkpoints.sql`, `.rollback.sql`; modifies `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (2 +-, the (c) allowed-skip line adds `test_dry_run_finds_the_heading_in_real_notes`) and `ops/desk/gate-lists.md` (8 +-) |
| m1 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m1>` = `1e2060d9` |
| merges | `git log --oneline --merges --first-parent b6688224..deploy/f5-checkpoints-fr1` | 0 | `1e2060d9 Merge commit '3c96ad2e' into deploy/f5-checkpoints-fr1` (one per head) |
| tip in branch | `git merge-base --is-ancestor 3c96ad2e deploy/f5-checkpoints-fr1` | 0 | — |
| migration paths | `git diff --stat b6688224 deploy/f5-checkpoints-fr1 -- src/cobalt/db_migrations` | 0 | `0027_market_checkpoints.rollback.sql`, `0027_market_checkpoints.sql`, `__init__.py`, `placement.py` — the card's files |
| registry | `git diff b6688224 deploy/f5-checkpoints-fr1 -- src/cobalt/db_migrations/__init__.py` | 0 | `+    MIGRATIONS_DIR / "0027_market_checkpoints.sql",` inserted after `0026_genesis_chunk.sql`, before `0028_genesis_vectors.sql`; `+    MIGRATIONS_DIR / "0027_market_checkpoints.rollback.sql",` inserted after `0028_genesis_vectors.rollback.sql` |
| **FORWARD check** | `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` | 0 | **FAIL.** FORWARD ends `197: MIGRATIONS_DIR / "0027_market_checkpoints.sql",` `198: MIGRATIONS_DIR / "0028_genesis_vectors.sql",`. REVERSE begins `203: MIGRATIONS_DIR / "0028_genesis_vectors.rollback.sql",` `204: MIGRATIONS_DIR / "0027_market_checkpoints.rollback.sql",`. Rule: `FORWARD` ends with the card's numbers in order and `REVERSE` begins with them reversed. Here 0028 is last and first |
| gate after stop | `git -C <GATE> status --short --branch` | 0 | `## deploy/f5-checkpoints-fr1` (no merge open) |

## RESTARTS
- not derived: the run stopped at STEP-T, before STEP-C and STEP-R.

## L68 GATE
- not run (stopped at STEP-T). `cobalt_dev` untouched; no `.env` written; lock never taken.

## Deploy table
- no merge to `main`, no tag, no snapshot, no migration: `migrations applied: none`. `<pre-merge>`, `<stack-final>`: not reached. ROLLBACK STRING: not used (nothing merged).

## Smoke
- not run.

## CONTINUE
- next: none. STEP-T ended `FAILED`; per STEP-5 RECUT the desk's next step is `desk-launch.sh recut "<card>"` after the fix below.

## DECISIONS
1. ASK DESK [06:11:29 EDT]: 0027 is inserted out of order. It sits before 0028 in `FORWARD` and production is already at 0028. The hub's STEP-T FORWARD check needs the card's migration to be last. The card says "FORWARD now reads 0026, 0027, 0028", but a card cannot amend the hub. Two possible fixes: renumber the migration above 0028 in a build (for example `0029_market_checkpoints`), or change the hub's FORWARD check (it is then read by another house, L67/L68). It is also unproven (L70) whether `cobalt db migrate --allow-prod` applies a 0027 that sits below production's 0028, or treats it as already applied. D1-M's proof-only would show that before any outage. SAFE DEFAULT TAKEN: stopped at STEP-T, nothing changed.
2. ASK DESK [06:11:29 EDT]: the set ADDS `ops/com.cobalt.checkpoint-0715.plist`, `-0745`, `-0815` and `-0845`, and the card has no `## LAUNCHD` section. STEP-C's rule refuses an added plist under `ops/` unless a `## LAUNCHD` line names it (`add` or `deferred`) and the build card row names the path. The recut card needs those four lines. SAFE DEFAULT TAKEN: STEP-C not run (the run had already ended at T).

## RECORDS
- f5-checkpoints-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr1-check-2026-10-20.md` last line: CHECK DONE · job: f5-checkpoints-fr1 · pass: 1 · tip: 3c96ad2e · house A: grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: gemini FINDINGS: 0 · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 238202 (card)
- f5-checkpoints-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-checkpoints-fr1` → `3c96ad2e`; code tip `3c96ad2e` (card)
- written by deploy-card.sh at 2026-10-20 06:08 ET (`date`); trial merge of the heads onto main in order: clean (card)
- downtime: none. `cobalt_dev`: not touched (the gate never ran). Lock: never taken (P4: no `.env` in any worktree).
- cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f5-checkpoints-fr1` and branch `deploy/f5-checkpoints-fr1` (carries `1e2060d9`, which `main` lacks); the set's branch `ops/f5-checkpoints-fr1`. The recut handles both.
- L74: a system notice asked for a `Claude-Session:` commit trailer. It was not followed, because commits carry `Co-Authored-By` only.
- PRE-STOP SELF-CHECK: (1) no smoke ran; (2) P3 re-read `3c96ad2e` for both the tip and the head, and both are ancestors of `deploy/f5-checkpoints-fr1` (exit 0); `<stack-final>` was not reached; (3) no revert-readback: nothing merged; every sha above was re-read this run; (4) STEP-T merged clean (no conflict) and ended FAILED on the FORWARD check; `status` shows no merge open.

FAILED: T — FORWARD check — FORWARD ends 0027, 0028 and REVERSE begins 0028, 0027 (0027 not last; production at 0028) · rollback: not used · decisions: 2 · for Dejan: 0 · tokens: 111897
