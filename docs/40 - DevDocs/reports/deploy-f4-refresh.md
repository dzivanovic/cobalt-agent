# deploy f4-refresh · SET: none · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md` · hub: `DEPLOY-HUB.md` · seat: deploy-hub-f4-refresh · model: Opus 5.5 (`claude-opus-5-5`)

## §0 Headline
FAILED at STEP-C, before anything in production changed. The set adds `ops/com.cobalt.prefill-refresh.plist`, but card 778 has no `## LAUNCHD` line that names it, so `deploy-step-c.sh` refused it.
Authorization, preflight (P0–P8) and STEP-T passed (`<m1>` `70ec2e80`). No gate, merge or outage ran. The residents were never touched.
Next: the desk adds a `## LAUNCHD` line (`add` or `deferred`) to the card, then runs `desk-launch.sh recut`.

## L74
- The session's harness attribution reminder asked for a `Claude-Session:` line on commits. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 0 · 69d0d2e851a2bd1ab62664b5271dbc2e36cf669a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 87:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-f4-refresh.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sun Oct 18 11:48:39 EDT 2026` (outside 21:30-22:30 ET) |
| P2 check | `tail -n 3 ".../f4-refresh-check-2026-10-18.md"` | 0 | `CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500` (carries `held unfixed: 0` and `ready: YES`; tip `51b03e00` = row's code tip) |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/f4-refresh-check-2026-10-18.md"` | 0 | `220f03a11d7462cb5cfc9f30153dc7d2e0d740b7` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/f4-refresh-check-2026-10-18.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 51b03e00` | 0 | `51b03e00` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1018` | 0 | `7b291371` (= row, = TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 51b03e00 7b291371` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 51b03e00 7b291371 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh status --short --branch` | 0 | `## deploy/f4-refresh` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh rev-parse --short=8 HEAD` | 0 | `8df4ca7d` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8df4ca7d main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f4-refresh` | 0 | empty |
| P6 marker 1 | `grep -c -F "label: com.cobalt.prefill-refresh" …/configs/cobalt/jobs.yaml` | 1 | `0` (before) |
| P6 marker 2 | `grep -c -F "key: prefill.refresh_interval_min" …/tunables.yaml` | 1 | `0` (before) |
| P6 marker 3 | `grep -c -F "key: prefill.refresh_window" …/tunables.yaml` | 1 | `0` (before) |
| P6 marker 4 | `grep -c -F "id: K12.3" …/configs/cobalt/smoke/s2.yaml` | 1 | `0` (before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 7b291371 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · pid 80523 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · pid 24167 |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh merge --no-edit 7b291371` → `Merge made by the 'ort' strategy.` (28 files changed, 2934 insertions(+), 115 deletions(-); creates `ops/com.cobalt.prefill-refresh.plist`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_prefill_refresh_experiments.py` and the build report pair)
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh rev-parse --short=8 HEAD` → `70ec2e80` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 8df4ca7d..deploy/f4-refresh` → `70ec2e80 Merge commit '7b291371' into deploy/f4-refresh` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 51b03e00 deploy/f4-refresh` → exit 0 · `… 7b291371 deploy/f4-refresh` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 8df4ca7d deploy/f4-refresh -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none holds)
- STEP-T clean, no conflict.

### STEP-C
`git -C /Users/cobalt/cobalt diff --stat 8df4ca7d deploy/f4-refresh -- configs ops` → whole:
```
 configs/cobalt/jobs.yaml              |  18 +++-
 configs/cobalt/prefill.yaml           |   9 ++
 configs/cobalt/smoke/s2.yaml          |  11 +++
 configs/cobalt/taxonomy/tunables.yaml |  33 +++++++
 configs/cobalt/templates/daily.md.j2  |  10 ++-
 ops/com.cobalt.prefill-refresh.plist  | 156 ++++++++++++++++++++++++++++++++++
 6 files changed, 234 insertions(+), 3 deletions(-)
```
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/778-deploy-f4-refresh-card.md" 8df4ca7d deploy/f4-refresh` → exit 1, whole:
```
REFUSED: ops/com.cobalt.prefill-refresh.plist — no ## LAUNCHD line names com.cobalt.prefill-refresh
FAILED: C — ops/com.cobalt.prefill-refresh.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used
```
The run ends at STEP-C. STEP-R, G, D0–D2, the outage and smoke did not run. Production was not touched: no bootout, no merge to `main`, no migration, no backup, no tag. The `cobalt_dev` lock was never taken.

## RESTARTS
not run (STEP-C ended the run).

## L68 GATE
not run (STEP-C ended the run). No `GATE GREEN` line.

## Deploy table
- `<m0>` `8df4ca7d` · `<m1>` `70ec2e80` (gate branch `deploy/f4-refresh` only; `main` unmoved by this run)
- `<pre-merge>` / `<stack-final>`: none · tags: none set (`pre-f4-refresh` and `deploy-2026-10-18-f4-refresh` not created) · outage: none · migrations applied: none · snapshot: none · RESTARTS done: none · LAUNCHD done: none
- ROLLBACK STRING: not used (nothing merged).

## Smoke
not run.

## CONTINUE
next: none. The run ended FAILED at STEP-C with `rollback: not used`; the desk's next step is `desk-launch.sh recut "<card>"` after the card is fixed (hub, STEP-5 RECUT).

## DECISIONS
1. The card has no `## LAUNCHD` section, but the set adds `ops/com.cobalt.prefill-refresh.plist` (Label `com.cobalt.prefill-refresh`; marker 1 adds the same label to `configs/cobalt/jobs.yaml`). STEP-C refuses any added plist that no `## LAUNCHD` line names. Safe default taken: stop with nothing changed. Desk: rewrite card 778 with a `## LAUNCHD` line for `prefill-refresh`, `add` if this deploy should load it or `deferred` if the bootstrap waits for its gate items. Check that the build card row lists the path in its `files` cell, then recut. This is the desk's card fix and not a ruling (the R1833 run-everything ruling covers it).

## RECORDS
- STEP-C `REFUSED: ops/com.cobalt.prefill-refresh.plist — no ## LAUNCHD line names com.cobalt.prefill-refresh` (quoted above).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f4-refresh` and branch `deploy/f4-refresh` now carry the merge `70ec2e80`. The desk's recut cleans them. Nothing was committed into the gate tree by hand (rule B).
- `cobalt_dev`: untouched; the lock was never taken (P4 found no `.env` in any worktree).
- `REFUSED, not needed: sh /Users/cobalt/cobalt/ops/desk/desk-context.sh session_01AGJ3KiVy9fu1avNu2M2bmp — no transcript for session_01AGJ3KiVy9fu1avNu2M2bmp` (exit 2; the same with the bare id). I found the session id `4620d884-d360-4144-bdcf-91f6968aa01c` with `ls -t` of the project transcripts. The tokens figure comes from that call: `context 92887 of 400000 — ok`.
- L74: one attribution block asking for a `Claude-Session:` line, recorded under `## L74`, not acted on.
- Card `## RECORDS`, copied:
  - f4-refresh-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-18.md` last line: CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · house A: Grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8538/0 · with-DB 5552/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500
  - f4-refresh-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1018` → `7b291371`; code tip `51b03e00`
  - written by deploy-card.sh at 2026-10-18 11:34 ET (`date`); trial merge of the heads onto main in order: clean
- Stopped at `Sun Oct 18 11:49:33 EDT 2026` (`date`).

FAILED: C — ops/com.cobalt.prefill-refresh.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 92887
