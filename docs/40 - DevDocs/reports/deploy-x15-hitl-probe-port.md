# deploy x15-hitl-probe-port · set: x15-hitl-probe-port · migrations: none

## §0 Headline
- Deploy of `ops/x15-hitl-probe-port` (code tip `304d5f3b`, head `c062baf7`) through gate branch `deploy/x15-hitl-probe-port`.
- FAILED at STEP-R: the restart set holds `com.cobalt.cos` and `com.cobalt.cos` is loaded (pid 40998). Its bootout and bootstrap strings are not on the deploy list (R60).
- Production untouched: no gate run, no merge to `main`, no resident down, no tag. Rollback not used.
- Desk's next step: get the cos strings ruled by Dejan, then `desk-launch.sh recut "<card>"`.

## L74
- One harness reminder asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 0 · 0ecd722a31cfd3b84c8849de5b123c502d1d64d6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Wed Oct 21 20:43:07 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../x15-hitl-probe-port-check-2026-10-21.md"` | 0 | `CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088` — carries `held unfixed: 0`, `ready: YES`, `tip: 304d5f3b` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md"` | 0 | `20f9db1dedf2232da182cd05e9181c6182edced9` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 304d5f3b` | 0 | `304d5f3b` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x15-hitl-probe-port` | 0 | `c062baf7` = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 304d5f3b c062baf7` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 304d5f3b c062baf7 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/x15-hitl-probe-port` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `0ecd722a` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0ecd722a main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/x15-hitl-probe-port` | 0 | empty |
| P6 | `grep -c -F "def _hitl_key_script" .../aset/web.py` | 1 | `0` = before |
| P6 | `grep -c -F '@app.get("/hitl/x15-probe"' .../aset/web.py` | 1 | `0` = before |
| P6 | `grep -c -F 'add_parser("x15-send"' .../hitl/cli.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main c062baf7 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 6720` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 31938` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit c062baf7` | 0 | `Merge made by the 'ort' strategy.` (9 files, 564 insertions, 6 deletions: `src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, docs) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d0dc4ec1` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 0ecd722a..deploy/x15-hitl-probe-port` | 0 | `d0dc4ec1 Merge commit 'c062baf7' into deploy/x15-hitl-probe-port` |
| code tip in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 304d5f3b deploy/x15-hitl-probe-port` | 0 | — |
| head in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c062baf7 deploy/x15-hitl-probe-port` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 0ecd722a deploy/x15-hitl-probe-port -- src/cobalt/db_migrations` | 0 | nothing — `none` holds |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat 0ecd722a deploy/x15-hitl-probe-port -- configs ops` | 0 | nothing |
| STEP-C | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 0ecd722a deploy/x15-hitl-probe-port` | 0 | `STEP-C: ADMITTED 0` — `<launchd set>` empty, `<deferred set>` empty |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port
Installed 257 packages in 601ms
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	M	DOCS	-
docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.result	A	DOCS	-
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_hitl_x15.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. `<deferred set>`: empty. com.cobalt.agent: recorded retired — not restarted (not in the set anyway).

NOT LOADED read: `launchctl print gui/501/com.cobalt.cos` → exit 0, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `state = running`, `pid = 40998`. Loaded → the hub's rule ends the run: `cd /Users/cobalt/cobalt` (then `ls -la /Users/cobalt/cobalt/.env` → listed, cwd back).

## L68 GATE
Not run (the run ended at STEP-R, before any suite).

## Deploy table
None. Nothing merged to `main`; no tag set; no snapshot; no resident down. `<pre-merge>`, `<stack-final>`: not reached.

## Smoke
Not reached.

## CONTINUE
Ended FAILED at STEP-R, 20:44:18 ET. No resume: a `rollback: not used` ending is recut by the desk (`desk-launch.sh recut "<card>"`).

## DECISIONS
1. FOR DEJAN — `com.cobalt.cos` is in the derived restart set (`src/cobalt/aset/web.py` reaches it) and is now loaded (cos-bootstrap-2, DEPLOYED today, `dc27deda`). The deploy list has no `bootout` / `bootstrap` / `kickstart` string for `com.cobalt.cos` (R60), so no deploy that touches `web.py` can pass STEP-R until he approves those strings for the list (or rules another way). Safe default taken: stop with production untouched.

## RECORDS
- Downtime: none. No production change; `main` not moved by this run except this report's commit.
- `cobalt_dev`: not touched (STEP-G never ran; lock never taken).
- Gate worktree `/Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port` and branch `deploy/x15-hitl-probe-port` left at `<m1>` `d0dc4ec1` with a fresh `.venv` (from `uv run` at STEP-R); cleanup owed to the desk's recut (L46).
- Token figure: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 7a4ed320` → `context 97803 of 400000 — ok`. Two earlier tries with other ids printed `no transcript for …` (exit 2).
- L74: one harness reminder asked for a `Claude-Session:` line in commits; recorded, not acted on.
- Card `## RECORDS`, copied:
  - x15-hitl-probe-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md` last line: CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088
  - x15-hitl-probe-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x15-hitl-probe-port` → `c062baf7`; code tip `304d5f3b`
  - written by deploy-card.sh at 2026-10-21 20:42 ET (`date`); trial merge of the heads onto main in order: clean

FAILED: RESTARTS — com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60), they are asked of Dejan · rollback: not used · decisions: 1 · for Dejan: 1 · tokens: 97803
