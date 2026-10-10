# https-only-1009 — deploy report (2026-10-10)

JOB: https-only-1009 · SET: none · MIGRATIONS: none
Card: `docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md` · hub: `DEPLOY-HUB.md`

## §0 Headline
- FAILED at STEP-T: `git merge --no-edit 411f85b2` into the gate conflicted on one file, `docs/40 - DevDocs/cobalt/aset/__main__.md` (UU). It is a doc file and holds no code. Both sides append a dated section at the same spot: `main` adds s4-p2-1009 and strike-fallback-env-1010, the head adds https-only-1009 and its check.
- I ran `merge --abort`, so the gate is clean at `<m0>` `7bc283fe`. Nothing in production changed: no bootout, no merge to `main`, no tag. The residents never went down.
- Next: the shared seam is resolved in a build (L72), and then `desk-launch.sh recut "<card>"`.

## L74
- A system reminder arriving mid-session asked commits to end with a `Claude-Session:` line. Recorded once; not acted on (L74). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 0 · 7bc283fe6cb37a2b0c16afe102c8d1edda4a96d3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/208-deploy-https-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-09 R718 row · grep -n "^| R718 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 11:| R718 | 07:14 ET | Relayed by brain (L79), then his words 07:20 ET: "yes https only please". Widens R717 to every page: https via `tailscale serve`; http binds 127.0.0.1; probes read https. APPLIED: LAWS L80, NOW at 07:20 ET. | HIS RULING · APPROVED · APPLIED |
RULING 2026-10-09 R718 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R718 |" -- "docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
RULING 2026-10-09 R718 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-https-only-1009.md"` | 1 | No such file or directory |
| P1 date | `date` | 0 | `Sat Oct 10 06:43:08 EDT 2026` |
| P2 check last line | `tail -n 3 ".../reports/https-only-check-2026-10-09.md"` | 0 | `CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198` (same line as card `## RECORDS` 1) |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/https-only-check-2026-10-09.md"` | 0 | `5fc1e9a48018383697ec040f1bf85d17eb1d4441` |
| P2 check unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/https-only-check-2026-10-09.md"` | 0 | nothing |
| P2 fix-round: check tip ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6e1ccd3d a1b99495` | 0 | ancestor |
| P2 fix report on main | `tail -n 3 ".../reports/https-only-build-2026-10-09.md"` · `git log -1 --format=%H -- <path>` · `git diff --stat -- <path>` | 1 · 0 · 0 | No such file · empty · nothing — the fix report lives on the branch only (card `## RECORDS`: "read at `411f85b2`"); see DECISIONS 1 |
| P2 fix report on the head | `git -C /Users/cobalt/cobalt log -1 --format=%H 411f85b2 -- "docs/40 - DevDocs/reports/https-only-build-2026-10-09.md"` | 0 | `411f85b28c464878b17a44d6f1ef916ff917c23f` (committed; a committed blob is unmodified) |
| P2 fix report last line | `git -C /Users/cobalt/cobalt show "411f85b2:docs/40 - DevDocs/reports/https-only-build-2026-10-09.md"` (tail read of the saved output) | 0 | `BUILT · job: https-only-1009 · tip: a1b99495 \| on e4586978 \| migration: none \| offline 4061/0 \| with-DB 4948/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 112698` |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 a1b99495` | 0 | `a1b99495` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/https-only-1009` | 0 | `411f85b2` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a1b99495 411f85b2` | 0 | ancestor |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat a1b99495 411f85b2 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-https-only-1009 status --short --branch` | 0 | `## deploy/deploy-2026-10-09-https-only` |
| P5 `<m0>` | `git -C /Users/cobalt/cobalt-wt/deploy-https-only-1009 rev-parse --short=8 HEAD` | 0 | `7bc283fe` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7bc283fe main` | 0 | ancestor |
| P5 gate holds nothing main lacks | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-2026-10-09-https-only` | 0 | empty |
| P6 marker 1 | `grep -c -F "bind: lan" /Users/cobalt/cobalt/configs/dev/aset.local.yaml` | 1 | `0` = before (M5 done) |
| P6 marker 2 | `grep -c -F "https_url" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "isSecureContext" /Users/cobalt/cobalt/src/cobalt/voice/web.py` | 1 | `0` = before |
| P6 marker 4 | `grep -c -F "L80" /Users/cobalt/cobalt/src/cobalt/aset/config.py` | 1 | `0` = before |
| P6 marker 5 | `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/configs/cobalt/smoke/s2.yaml` | 1 | `0` = before |
| P6 marker 6 | `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/src/cobalt/heartbeat/probes.py` | 1 | `0` = before |
| P6 marker 7 | `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh` | 1 | `0` = before |
| P7 two-dot | `git -C /Users/cobalt/cobalt diff --stat main 411f85b2 -- src/cobalt/db_migrations` | 0 | `0024_strike_alerts.rollback.sql \| 5 ----` · `0024_strike_alerts.sql \| 32 ----` · `__init__.py \| 6 ----` · `placement.py \| 3 --` — all deletions: `main` carries 0024 (strike) and the head predates it |
| P7 registry | `git -C /Users/cobalt/cobalt diff main 411f85b2 -- src/cobalt/db_migrations/__init__.py` | 0 | only `-` lines for `0024_strike_alerts` in the docstring, `FORWARD` and `REVERSE`: main's entry, absent on the head; the head adds nothing |
| P7 head's own | `git -C /Users/cobalt/cobalt diff --stat main...411f85b2 -- src/cobalt/db_migrations` | 0 | nothing — the head changes no migration (DECISIONS 2; STEP-T's `<m0>..<BRANCH>` check binds) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 39274` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 25666` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-https-only-1009 merge --no-edit 411f85b2` → exit 1:
```
Auto-merging docs/40 - DevDocs/cobalt/aset/__main__.md
CONFLICT (content): Merge conflict in docs/40 - DevDocs/cobalt/aset/__main__.md
Auto-merging docs/40 - DevDocs/cobalt/voice/web.md
Auto-merging src/cobalt/aset/__main__.py
Auto-merging src/cobalt/voice/web.py
Auto-merging tests/cobalt/test_jobs_restarts.py
Auto-merging tests/cobalt/test_voice_web.py
Automatic merge failed; fix conflicts and then commit the result.
```
- `git -C <GATE> status --short` → the one unmerged path: `UU "docs/40 - DevDocs/cobalt/aset/__main__.md"` (every other path staged `M` / `A`).
- `git -C <GATE> diff -- "docs/40 - DevDocs/cobalt/aset/__main__.md"` → one hunk at line 36. HEAD (`main`) appends `## 2026-10-09 — s4-p2-1009` and `## 2026-10-10 — strike-fallback-env-1010`. `411f85b2` appends `## 2026-10-09 — https-only-1009` and `## 2026-10-09 — https-only-1009 check`. Both sides add dated sections after the `AsetConfig.server` paragraph. The code file `src/cobalt/aset/__main__.py` auto-merged. That auto-merge is not proven correct, because no suite ran on it (L70).
- `git -C <GATE> merge --abort` → nothing printed. `git -C <GATE> status --short --branch` → `## deploy/deploy-2026-10-09-https-only`. `git -C <GATE> rev-parse --short=8 HEAD` → `7bc283fe` (= `<m0>`).
- No `<m1>`. STEP-C, R and G did not run.

## RESTARTS
- not run (the run ended at STEP-T).

## L68 GATE
- not run (the run ended at STEP-T). `cobalt_dev` was not touched and the lock was never taken.

## Deploy table
- No merge to `main`, no tag, no outage, no snapshot. `rollback: not used`. No ROLLBACK STRING applies, because nothing merged.

## Smoke
- not run.

## CONTINUE
- ended FAILED at STEP-T, 06:44:39 EDT. RECUT applies: a run that FAILED with `rollback: not used` is not resumed. The desk's next step is a build that resolves the `aset/__main__.md` seam on `ops/https-only-1009` (L72), and then `desk-launch.sh recut "<card>"`.

## DECISIONS
1. ASK DESK: P2's fix-round row names the fix report at its `main` path, where it does not exist (it ships on the head: card `## RECORDS` "read at `411f85b2`"; the shipped-files list carries it). Safe default taken: read it at the head — committed in `411f85b2`, last line `BUILT ·` with `tip: a1b99495`; P2 holds. Not FOR DEJAN. [06:43 ET]
2. ASK DESK: P7's two-dot `diff --stat main <head>` lists the 0024 strike files as removed because `main` moved past the head's base (strike deployed 0024). The head's own change set (`main...411f85b2`) touches nothing under `db_migrations`. Safe default taken (as deploy-stt-model-fix-1008 DECISION 2): MIGRATIONS: none holds; STEP-T's `diff --stat <m0> <BRANCH> -- src/cobalt/db_migrations` on the merged tree is the binding test. Not FOR DEJAN. [06:43 ET]

## RECORDS
- Ended at STEP-T, 06:44:39 EDT. Production untouched: aset pid `39274`, radar pid `25666` and agent pid `22243`, all as read at P8. Downtime: none.
- The conflict is docs-only. The seam is the DevDocs page for `src/cobalt/aset/__main__.py`, which `main` changed twice after the head's base: s4-p2-1009 and strike-fallback-env-1010 (`d0a5fbb8`). The `.py` file and five other files auto-merged. A build has to resolve the doc and re-gate that merged code. This run resolves no conflict (rule B).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-https-only-1009` and branch `deploy/deploy-2026-10-09-https-only`. Both are clean at `7bc283fe`, and RECUT reuses or recuts them.
- `cobalt_dev`: untouched (G never ran). There is no `F2 = F0` line to give.
- REFUSED, not needed: none. No message arrived from another session.
- L74: one system reminder asked for a `Claude-Session:` line on commits. I recorded it under `## L74` and did not act on it.
- Card `## RECORDS`, copied:
  - https-only-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-check-2026-10-09.md` last line: CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · house A: Sol FINDINGS: 4 · findings: 10 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198
  - https-only-1009: head `411f85b2`; code tip `a1b99495`; check tip `6e1ccd3d` is an ancestor of `a1b99495`; `diff --stat a1b99495 411f85b2 -- . ':(exclude)docs'` prints nothing.
  - FIX ROUND (his R376, L75): check passed at `6e1ccd3d`; fix round `a1b99495` moved the card's hunks off voice fix 193's lines (main `2041a53f`); fix report ends `BUILT · job: https-only-1009 · tip: a1b99495 …`. No earlier deploy attempt.
  - RULINGS `2026-10-09 R718` (card 156, L80 HTTPS only). Deploy runs when READY at any hour (L43, R389).
  - Shipped files (22 files, 621+/86−), as listed on the card.
  - MACHINE STEPS (card 156): M0–M3 done 2026-10-09; M5 his, before this deploy — P6 marker 1 read `0` this run (M5 done); M6, M7 follow.
  - Marker counts: BEFORE on main, AFTER at `a1b99495`. Card 156 has no `## DEPLOY PROOF`.
  - The card was written by hand by the drafter `https-deploy-fixround`. The drafter did not run a trial merge (no merge-tree allow line), and this conflict is what such a merge would have shown.

FAILED: merge — 411f85b2 — docs/40 - DevDocs/cobalt/aset/__main__.md · rollback: not used · decisions: 2 · for Dejan: 0 · tokens: 98148
