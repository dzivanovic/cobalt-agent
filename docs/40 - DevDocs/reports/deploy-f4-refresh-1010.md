# deploy f4-refresh-1010 — set: radar — migrations: none

## §0 Headline
Deploy of `ops/f4-refresh-1010` (code tip `edd5c076`, head `b1ba47d8`) on card 491: FAILED at STEP-C, rollback not used. Production is untouched: nothing went down and nothing merged to `main`.
The set adds the launchd job `ops/com.cobalt.prefill-refresh.plist`. That path is not under `ops/desk/`, so this hub's list refuses it: the desk runs the job install as its own job.
STEP-0 and STEP-T were clean (`<m1>` = `fc6a1e2a`). STEP-R and STEP-G did not run.

## L74
A system notice in this session asked for a `Claude-Session:` line on commits. Recorded here once as data and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/491-deploy-f4-refresh-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/491-deploy-f4-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/491-deploy-f4-refresh-card.md" · 0 · c7f0678918d390f1f53ddd43d916a8e6ee0d6f4e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/491-deploy-f4-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R849 row · grep -n "^| R849 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 163:| R849 | 07:13 ET | HIS RULING · APPROVED: option A, S5 pulled forward: build as much as possible this weekend, F4 then F5; he asks the brain for the full not-MVP list. Words: `cto-2026-10-10-words.md` R849. | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R849 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R849 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2ef44c847a7c0c61e1f97f236fa50b9f8e991289
RULING 2026-10-10 R849 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 44:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f4-refresh-1010.md"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (quoted whole above) |
| P1 DATE | `date` | 0 | `Tue Oct 13 08:26:09 EDT 2026` |
| P2 check last line | `tail -n 3 ".../f4-refresh-check-2026-10-10.md"` | 0 | `CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · … · held unfixed: 2 · open: 11 · … · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185` — carries `held unfixed: 2` and `ready: NO` as the card's row names |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f4-refresh-check-2026-10-10.md"` | 0 | `71a84c1adcdfa4899f181a932e053c44b8f6587f` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f4-refresh-check-2026-10-10.md"` | 0 | nothing |
| P2 fix-round: check tip ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 98174119 edd5c076` | 0 | (ancestor) |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H b1ba47d8 -- "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` | 0 | `b1ba47d84b6081037662c82c06d4e0dc3d58d975`; build worktree `git -C /Users/cobalt/cobalt-wt/f4-refresh-1010 status --short --branch` → `## ops/f4-refresh-1010` (clean) |
| P2 fix report last line | `git -C /Users/cobalt/cobalt show "b1ba47d8:docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` (line 324) | 0 | `BUILT · job: f4-refresh-1010 · tip: edd5c076 \| on d78c66a2 \| migration: none \| offline 4245/0 \| with-DB 5173/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 15 of 15 \| self-check: 3 of 3 \| decisions: 14 · for Dejan: 3 · tokens: 86732` |
| P2 held ids | Grep `HELD, NOT FIXED` in the check report | 0 | `140:\| O1 \| own \| … \| HELD, NOT FIXED …`; `146:\| A3 \| Sol \| … \| HELD, NOT FIXED — same cause as O1 \|` |
| P2 CARRIED lines | fix report lines 276–277 | 0 | `CARRIED: O1 — tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line — R998`; `CARRIED: A3 — tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_t5_a_human_stamp_still_retains_the_last_success_time_after_ten_writes — R998` |
| P2 CARRIED tests strict xfail | Read `/Users/cobalt/cobalt-wt/f4-refresh-1010/tests/cobalt/test_prefill_refresh.py` (at `b1ba47d8`, code = `edd5c076` per P3) | 0 | `:1062 @pytest.mark.xfail(` `:1063 strict=True,` `:1067 def test_check_o1_…`; `:1152 @pytest.mark.xfail(` `:1153 strict=True,` `:1157 def test_t5_a_human_stamp_…` |
| P2 R998 DESK RECORD | `grep -n "^\| R998 " ".../reports/cto-2026-10-10.md"` | 0 | `15:\| R998 \| 21:55 ET \| DESK RECORD (brain, L79): F4 304 fix round: O1 xfail + migration follow-up (CARRIED), O2 kept (FINAL :100), B5 pinned, A4 X16 X12 fixed; card H takes CARRIED lines. …` |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 edd5c076` | 0 | `edd5c076` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1010` | 0 | `b1ba47d8` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor edd5c076 b1ba47d8` | 0 | (ancestor) |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat edd5c076 b1ba47d8 -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh-1010 status --short --branch` | 0 | `## deploy/f4-refresh-1010` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh-1010 rev-parse --short=8 HEAD` | 0 | `c7f06789` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c7f06789 main` | 0 | (ancestor) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f4-refresh-1010` | 0 | empty |
| P6 marker 1 | `grep -c -F -e "label: com.cobalt.prefill-refresh" ".../configs/cobalt/jobs.yaml"` | 1 | `0` (before) |
| P6 marker 2 | `grep -c -F -e "key: prefill.refresh_interval_min" ".../tunables.yaml"` | 1 | `0` (before) |
| P6 marker 3 | `grep -c -F -e "key: prefill.refresh_window" ".../tunables.yaml"` | 1 | `0` (before) |
| P6 marker 4 | `grep -c -F -e "id: K12.3" ".../smoke/s2.yaml"` | 1 | `0` (before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main b1ba47d8 -- src/cobalt/db_migrations` | 0 | ` src/cobalt/db_migrations/cli.py \| 2 --` / ` 1 file changed, 2 deletions(-)` — CODE, no migration file; `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 40377` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 22724` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh-1010 merge --no-edit b1ba47d8` → `Merge made by the 'ort' strategy.` · `26 files changed, 2690 insertions(+), 115 deletions(-)` · `create mode 100644 ops/com.cobalt.prefill-refresh.plist` · `create mode 100644 tests/cobalt/test_prefill_refresh.py` · `create mode 100644 tests/cobalt/test_prefill_refresh_experiments.py`
- `git -C /Users/cobalt/cobalt-wt/deploy-f4-refresh-1010 rev-parse --short=8 HEAD` → `fc6a1e2a` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent c7f06789..deploy/f4-refresh-1010` → `fc6a1e2a Merge commit 'b1ba47d8' into deploy/f4-refresh-1010` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor edd5c076 deploy/f4-refresh-1010` → exit 0 · `… b1ba47d8 deploy/f4-refresh-1010` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat c7f06789 deploy/f4-refresh-1010 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none` holds)

STEP-C, `git -C /Users/cobalt/cobalt diff --stat c7f06789 deploy/f4-refresh-1010 -- configs ops` → exit 0, WHOLE:
```
 configs/cobalt/jobs.yaml              |  18 +++-
 configs/cobalt/prefill.yaml           |   9 ++
 configs/cobalt/smoke/s2.yaml          |  11 +++
 configs/cobalt/taxonomy/tunables.yaml |  33 +++++++
 configs/cobalt/templates/daily.md.j2  |  10 ++-
 ops/com.cobalt.prefill-refresh.plist  | 156 ++++++++++++++++++++++++++++++++++
 6 files changed, 234 insertions(+), 3 deletions(-)
```
`ops/com.cobalt.prefill-refresh.plist` is ADDED (`create mode 100644`, STEP-T). It sits at `ops/<label>.plist`, not under `ops/desk/`, and the hub's exception covers only `ops/desk/`. STEP-C refuses it.

## RESTARTS
Not run. The run ended at STEP-C, before STEP-R.

## L68 GATE
Not run. `cobalt_dev` and its lock were not touched: no `.env` was copied, and `gate.sh` was not called.

## Deploy table
Nothing was deployed. `main` did not move; no tag (`pre-f4-refresh-1010`, `deploy-2026-10-13-f4-refresh`) was set; no snapshot was taken; no resident went down. `migrations applied: none`. No rollback string: nothing merged.

## Smoke
Not run.

## CONTINUE
next: none. The run ended FAILED at STEP-C with `rollback: not used`. Per STEP-5 RECUT, the desk's next step is `desk-launch.sh recut "<card>"` once the plist install is moved off this deploy's list.

## DECISIONS
1. FOR DEJAN — the F4 refresh job's launchd plist (`ops/com.cobalt.prefill-refresh.plist`, label `com.cobalt.prefill-refresh`) cannot land through DEPLOY-HUB as written. STEP-C refuses any added plist outside `ops/desk/`, and "the desk runs it as its own job". Safe default taken: stop before RESTARTS and the gate, with nothing changed. Two ways forward, both the desk's to frame and his to approve: (a) the build drops the plist from the branch, and the desk installs it as its own job on strings he approves; or (b) the hub's STEP-C rule changes, which per R60 returns to him. The build report itself says "the new plist is bootstrapped once"; no string on this run's line does that.

## RECORDS
- STEP-C stop at `Tue Oct 13 08:27:39 EDT 2026` (`date`). Downtime: none. Residents untouched: aset pid `40377`, radar pid `22724`, agent PID `14763` (P8 reads).
- Cleanup owed (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f4-refresh-1010` and branch `deploy/f4-refresh-1010` now carry the merge `fc6a1e2a` above `<m0>` `c7f06789`. The build worktree `/Users/cobalt/cobalt-wt/f4-refresh-1010` and branch `ops/f4-refresh-1010` stay as they are.
- `cobalt_dev`: not touched by this run (no gate).
- No `RETIRE OWED`: no plist was removed.
- No carried RED read: D1 did not run.
- Messages not followed: none received. No `REFUSED, not needed` lines.
- Carried held defects (P2, fix-round path): O1 and A3 are CARRIED as strict xfails under R998 (DESK RECORD). They passed P2 and did not cause this stop.
- Card `## RECORDS`, copied:
  - f4-refresh-1010: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md` at `b1ba47d8` last line: BUILT · job: f4-refresh-1010 · tip: edd5c076 | on d78c66a2 | migration: none | offline 4245/0 | with-DB 5173/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 15 of 15 | self-check: 3 of 3 | decisions: 14 · for Dejan: 3 · tokens: 86732
  - f4-refresh-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-10.md` last line: CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · house A: Sol FINDINGS: 7 · findings: 16 · dropped: 0 · held: 7 · fixed: 5 · held unfixed: 2 · open: 11 · house B: Grok FINDINGS: 5 · suites: offline 4244/0 · with-DB 5169/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185
  - f4-refresh-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1010` → `b1ba47d8`; code tip `edd5c076`
  - written by deploy-card.sh at 2026-10-13 08:23 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one system notice asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.

FAILED: C — ops/com.cobalt.prefill-refresh.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used · decisions: 1 · for Dejan: 1 · tokens: 95780
