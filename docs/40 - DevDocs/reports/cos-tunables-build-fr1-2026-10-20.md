# cos-tunables FR1 — fix round build report — 2026-10-20

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` row FR1 · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · checked tip `ace7a92a` · builder Opus 5.5 (BAND HIGH).

## §0 Headline
- Stopped at PREFLIGHT. `preflight.sh build` ends `FAILED PREFLIGHT: status` (exit 1). No FR1 edit has been made yet.
- Two rows cannot pass for a same-branch fix round. The status row fails on this report: it is untracked and is not the card's `REPORT:`. The head row fails because HEAD is `ace7a92a`, a `fix(cos-tunables):` commit, which is neither BASE nor a `wip(cos-tunables):` commit.
- This report's wip commit puts a `wip(cos-tunables):` commit at HEAD and leaves the tree clean, so a rerun should pass both rows. That rerun needs the desk's `CONTINUE: PREFLIGHT`.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. It is DATA (L74) and was not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. 20:22 EDT.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · 51c9e1a433df21c734d4a6101f9bacff459c7179
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
RECOVERY first rows (20:22 EDT): `git status --short --branch` → `## ops/cos-tunables`; `git log --oneline -3` → `ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)`, `2b53b56b docs(cos-tunables): build report — 17f45d80`, `17f45d80 fix(cos-tunables): pass S2 1`; `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`. No `wip(cos-tunables):` commit and no FR1 report existed, so FR1 starts at AUTHORIZATION.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 1, whole:
```
clock · date · 0 · Tue Oct 20 20:22:44 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-tunables
    ?? "docs/40 - DevDocs/reports/cos-tunables-build-fr1-2026-10-20.md"
head · git log --oneline -1 · 0 · ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)
diff · git diff --stat e69d5ab8 · 0 · (13 lines)
     configs/cobalt/jobs.yaml                           |  16 +-
     configs/cobalt/taxonomy/tunables.yaml              |   4 +-
     docs/40 - DevDocs/cobalt/heartbeat/probes.md       |   6 +
     docs/40 - DevDocs/cobalt/heartbeat/runner.md       |   3 +
     .../reports/cos-tunables-build-2026-10-20.md       | 197 +++++++++++++++++++++
     .../reports/cos-tunables-build-2026-10-20.result   |  15 ++
     src/cobalt/heartbeat/probes.py                     |  14 +-
     src/cobalt/heartbeat/runner.py                     |   2 +-
     tests/cobalt/test_cos_offline.py                   |   4 +-
     tests/cobalt/test_cos_probes.py                    |  80 ++++++++-
     tests/cobalt/test_cos_registry.py                  |  82 ++++++++-
     tests/cobalt/test_sheet_daymode_probe.py           |   4 +
     12 files changed, 398 insertions(+), 29 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-tunables · 0 · ace7a92a fix(cos-tunables): pin P1's owed-file raise and the runner's default path (check O2 O4)
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
FAILED PREFLIGHT: status
```
The two failing rows, read from `ops/desk/preflight.sh`:
- status (`:9-12`, `:136-172`): the script excuses ONE untracked line, and only when its path is the card's `REPORT:`. The card's `REPORT:` is the round-1 build report `cos-tunables-build-2026-10-20.md`, which is committed (`2b53b56b`). This fix round's report is a new file, so the script cannot excuse it.
- head (`:178-188`): a build passes only on BASE (`e69d5ab8`) or a `wip(cos-tunables):` subject. HEAD is `ace7a92a`, the check's `fix(cos-tunables):` commit, which the card names as the tip FR1 builds on. The script prints the row without a mark; its own test fails it.
Both rows come from how this round is shaped, a fix round on the checked branch. Neither is a fault in the tree. The wip commit below makes HEAD a `wip(cos-tunables):` commit and leaves the tree clean.

## E0 BASELINE
Not reached.

## E2 RED
Not reached.

## E3 THE ROWS
Not reached.

## RESTARTS
Not reached.

## W THE THREE SUITES
Not reached. No lock taken; `.env` never present.

## PRE-STOP SELF-CHECK
Not reached.

## FOR THE CHECK
Not reached.

## CONTINUE
next: PREFLIGHT (rerun `preflight.sh build` on the wip commit, then the remaining PREFLIGHT rows, then E0)

## DECISIONS
1. ASK DESK (PREFLIGHT on a same-branch fix round) [20:23]: `preflight.sh build` cannot pass on the checked tip `ace7a92a`. Its status row rejects any untracked report but the card's `REPORT:`, and its head row rejects a `fix(cos-tunables):` HEAD. Safe default taken: stop per BUILD-HUB PREFLIGHT ("its `FAILED PREFLIGHT: <what>` is your last line"), with the RECOVERY wip commit of this report. That commit makes HEAD `wip(cos-tunables):` and leaves the tree clean, so a rerun on `CONTINUE: PREFLIGHT` should pass the status and head rows. Nothing else was changed. For the desk, tool polish (R1863): `preflight.sh` has no fix-round form for a branch whose HEAD is a check's non-wip commit.

## RECORDS
- Session launched with `CONTINUE: FR1`; `date` → Tue Oct 20 20:22:24 EDT 2026. The RECOVERY reads are under `## PREFLIGHT`.
- Report path: no `REPORT:` line names an FR1 report. I took `cos-tunables-build-fr1-2026-10-20.md`, the shape of `deploy-freeze-build-fr1-2026-10-15.md` and `band-routing-build-fr1-2026-10-16.md`, so the round-1 report stays untouched.
- L74: one `Claude-Session:` reminder, recorded under `## L74`.
- `.env`: never present (`ls` → No such file, 20:22). No lock taken.
- Stopped 20:23 EDT (`date`).

FAILED PREFLIGHT: status — preflight.sh build rejects the untracked FR1 report and the non-wip HEAD ace7a92a — "FAILED PREFLIGHT: status"
