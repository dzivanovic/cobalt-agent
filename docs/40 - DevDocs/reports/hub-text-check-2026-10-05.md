# hub-text — check, pass 1 (2026-10-05)

## §0 Headline
- I checked hub-text pass 1 alone, with no outside house (card `HOUSE A: none — overruled 2026-10-05 R412`). The tip is `6b939b00`. I made no commit.
- I wrote and ran 7 findings of my own. None is a defect of this build: every row of F1–F8 reads as the card gives it, and `test_hub_lines.py` passes 19/19.
- X2 found a gap outside this job. With (d2) gone, no deploy step treats a `RETIRE OWED` plist's validate line as recorded: 4.5 sends it to STEP-5. That is DECISION 1, as the card's X2 directs.
- The suites stand as built. The `tests/ops` red at `test_desk_launch_brain.py:285` is a base red (confirmed); it is the build's DECISION 1, not this card's.

## L74
No tool result carried an instruction. A system reminder in this session asked for a `Claude-Session:` commit trailer. I did not act on it: I made no commit, and CHECK-HUB L74 allows the `Co-Authored-By` line only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 0 · 2b645f29f26b2ee835566e370e87c8a3015efe25
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/26-hub-text-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
HOUSE A overruled 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
HOUSE A overruled 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (R17 / R19): not run — card header `HOUSE A: none — overruled 2026-10-05 R412`; PREFLIGHT runs no house gate and no probe.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:
```
clock · date · 0 · Mon Oct  5 14:24:45 EDT 2026
status · git status --short --branch · 0 · ## ops/hub-text-1005
head · git log --oneline -1; git log --stat --format=%h 6b939b00..HEAD · 0 · (5 lines)
    2abb7d99 docs(hub-text): build report — 6b939b00
    2abb7d99
    
     .../reports/hub-text-build-2026-10-05.md           | 205 +++++++++++++++++++++
     1 file changed, 205 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/hub-text-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/hub-text-1005/docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md" · 0 · BUILT · job: hub-text · tip: 6b939b00 | on a09ee1f0 | migration: none | offline 3786/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
range · git log --oneline a09ee1f0..6b939b00 · 0 · 6b939b00 feat(hub-text): fold R389, R390, R376, R375 MEASURE and R412 into the three hubs (F1-F8, L43, L68, L71, L75)
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h a09ee1f0..6b939b00` → `6b939b00` · `docs/40 - DevDocs/prompts/BUILD-HUB.md | 6 +++---` · `CHECK-HUB.md | 10 +++++-----` · `DEPLOY-HUB.md | 16 +++++++---------` · 3 files changed, 15 insertions(+), 17 deletions(-). Path union: the three hubs.
- DB: none: `git diff --name-only --no-renames a09ee1f0..6b939b00` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` — all under `docs/`.
- `ls <S>` → "No such file or directory" (fresh).
- house A: none (overruled 2026-10-05 R412) · no house gate, no probe.
- The lock: another session's `.env` sits in `launcher-fixround-1005`; this card is DB: none, no lock take.

## Files copied
none (no house; `## 1` not run).

## OWN FINDINGS
Written from my read of the card, the diff `a09ee1f0..6b939b00` (three hub files), the three hubs at the tip, the build report, `ops/desk/desk-context.sh`, the stop-line readers under `ops/desk/`, and `src/cobalt/cli.py:340-410` (X2). Nothing run yet.

FINDING O1
ROW: X2
CLAIM: With (d2) gone, no step of `DEPLOY-HUB.md` treats a `registry <-> plists` line for a `RETIRE OWED` label as recorded. 4.5 (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:139`) and smoke (f) (`:149`) send "any other failing line" to STEP-5. `src/cobalt/cli.py:352-354` prints `FAILED: <plist> is not readable as a plist` for a registry entry whose plist is gone. This was true of 4.5 before this build too; (d2) was the only step that carried the clause.
RUN: COMMAND `grep -n -F "RETIRE OWED" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: hits at `:50`, `:87`, `:174` only; none at `:139` (4.5) or `:149` (smoke (f)).

FINDING O2
ROW: X1 / X5 (F1, F5)
CLAIM: A hub still says a restart window or a night count binds a deploy, or still carries (d2) / `--no-db`, or a step still reads "the window P1 named" / `window:`.
RUN: COMMAND `grep -n -i "window" <each hub>`; `grep -n -i -F "window:"` DEPLOY-HUB; `grep -n -F "(d2)"`, `grep -n -F -e "--no-db"`, `grep -n -i -F "per night"`, `grep -n -i -F "a night"`, `grep -n -i -F "one deploy"` over the three hubs.
EXPECT if true: a hit beyond DEPLOY `:26` and `:57`, both of which state the opposite (no window binds).

FINDING O3
ROW: X3 (F4 (a))
CLAIM: A worker cannot get its `tokens:` figure from `desk-context.sh <session id>`, where the id is the last part of the job directory its prompt names.
RUN: COMMAND `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh fb16a942` (this session's job directory, `/Users/cobalt/.claude/jobs/fb16a942`) and `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh ccc04360` (the build session: the only other transcript in `~/.claude/projects/-Users-cobalt-cobalt-wt-hub-text-1005/`).
EXPECT if true: `no transcript for <id>` or a non-zero exit.

FINDING O4
ROW: X4 (F4 (a))
CLAIM: A desk script reads a stop line by field position, so the new last field ` · tokens: <n>` breaks it.
RUN: COMMAND `grep -n -r -F "for Dejan" /Users/cobalt/cobalt/ops/desk` and `grep -n -r -F "decisions:" /Users/cobalt/cobalt/ops/desk`; then read each stop-line reader the earlier Grep found (`desk-done.sh:22-25`, `desk-watch.sh:38-41`, `desk-launch.sh:816,828`, `card-fill.sh:67`, `preflight.sh:204`, `deploy-step0.sh:360-383`, `stop-guard.py:41-44`, `bare-guard.py:105,878`).
EXPECT if true: a reader that indexes a field or anchors on `for Dejan: <n>` at the end of the line.

FINDING O5
ROW: F4 (a), F6–F8
CLAIM: A stop line or a prose line of the three hubs still ends `for Dejan: <n>` with no `tokens:` field, or CHECK-HUB still says "You write no token figure".
RUN: COMMAND Grep tool, pattern ``for Dejan: <n>` `` (backtick right after) and ``for Dejan: <n> · tokens: <n>` `` over each hub, count; `grep -c -F "You write no token figure"` CHECK-HUB at the tip.
EXPECT if true: an old-form count above 0, or new-form counts other than BUILD 2 · CHECK 3 · DEPLOY 2.

FINDING O6
ROW: SCOPE (NOT IN THIS JOB: `tests/ops/test_hub_lines.py` run, not edited)
CLAIM: A row moved a line `tests/ops/test_hub_lines.py` pins.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py`
EXPECT if true: a failure.

FINDING O7
ROW: SCOPE (the build's DECISION 1)
CLAIM: The `tests/ops` red at `tests/ops/test_desk_launch_brain.py:285` is this build's, not the base's.
RUN: COMMAND `git diff --stat a09ee1f0 6b939b00 -- "docs/40 - DevDocs/prompts/BRAIN-HUB.md" tests/ops/test_desk_launch_brain.py`, then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled`
EXPECT if true: a non-empty diff stat (the build touched one of the two files).

## Findings
none (house A: none).

## Dropped
none.

## RUNS
All runs were in `<WT>` at `6b939b00` plus the docs-only report commit `2abb7d99`, between 14:25 and 14:28 EDT (`date`).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -n -F "RETIRE OWED" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | hits at `50:` (REPORT, `## RECORDS` names "a `RETIRE OWED`"), `87:` (STEP-C, "record `RETIRE OWED: <label>`"), `174:` (item 3, "every `RETIRE OWED`"). None at `:139` (4.5) or `:149` (smoke (f)). `src/cobalt/cli.py:352-354`: a registry entry whose plist cannot be read → `FAILED: <name> is not readable as a plist` | the output is shown, for its stated reason. **OUT OF SCOPE**: the card's NOT IN THIS JOB fences "Any other hub rule", and CHECK ASK X2 says "it is a `## DECISIONS` item, not a fix in this job". It is not a clause of F5 left unbuilt, since F5 deletes the (d2) bullet whole. 4.5 lacked the clause at BASE too. → DECISION 1 |
| O2 | own | `grep -n -i -F "window"` over the three hubs; then `"window:"`, `"(d2)"`, `-e "--no-db"`, `"per night"`, `"a night"`, `"one deploy"` over the three hubs | `window`: DEPLOY `:26` ("…no restart window and no per-night count binds it (his R389)") and `:57` ("- **P1 DATE**: `date`, recorded in the row. No restart window binds a deploy (L43, his R389)…") only. Each of the other six: no output, exit 1 | NOT HELD. The only two hits state that no window binds. X1 and X5 answered: no hit remains |
| O3 | own | `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh fb16a942` (this session) · `… desk-context.sh ccc04360` (the build session) | `context 122505 of 400000 — ok` · `context 206307 of 400000 — ok` | NOT HELD. X3: a worker reads its id from the job directory its prompt names (`/Users/cobalt/.claude/jobs/fb16a942`), and the script prints a figure after `context`, both for itself and for the build's id |
| O4 | own | `grep -n -r -F "for Dejan" /Users/cobalt/cobalt/ops/desk` · `grep -n -r -F "decisions:" /Users/cobalt/cobalt/ops/desk` · the Grep of `BUILT\|CHECK DONE\|DEPLOYED` over `ops/desk` and a read of `deploy-step0.sh:358-383` | no output, exit 1 (both). Every reader is a head or substring match: `desk-done.sh:22-25` `done_re='^BUILT'` / `'^CHECK DONE'` / `'^DEPLOYED'`; `desk-watch.sh:38-41` `re='^(BUILT\|FAILED)'` …; `desk-launch.sh:816` `"CHECK DONE"*"pass: 1"*"house B: needed"*`, `:828` `"BUILT · job: $job · tip: $tip "*`; `preflight.sh:204` `"BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*`; `card-fill.sh:67` `re.match(r"BUILT · job: (\S+) · tip: ([0-9a-f]{8})(?=\s\|$)"`; `stop-guard.py:41-44` and `bare-guard.py:105` head tuples; `deploy-step0.sh:369-370` `case "$last" in *"$lit"*)` and `:378` `grep -o -E '(^\| )tip: …'` | NOT HELD. X4: no script reads a field by position or anchors on the line's end |
| O5 | own | Grep (tool) ``for Dejan: <n>` `` count over the three hubs · Grep ``for Dejan: <n> · tokens: <n>` `` · `grep -c -F "You write no token figure"` CHECK-HUB | `Found 0 total occurrences across 0 files` · BUILD `:43 :106`, CHECK `:58 :127 :129`, DEPLOY `:50 :179` (2 / 3 / 2) · `0` | NOT HELD |
| O6 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` | `19 passed, 15 warnings in 2.84s` | NOT HELD |
| O7 | own | `git diff --stat a09ee1f0 6b939b00 -- "docs/40 - DevDocs/prompts/BRAIN-HUB.md" tests/ops/test_desk_launch_brain.py` · `uv run pytest … tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` | no output (the build touched neither file) · `1 failed, 15 warnings in 0.88s`, first failing line `tests/ops/test_desk_launch_brain.py:285: AssertionError` — `assert '«INSTALL' in '# BRAIN-HUB — the standing brain seat (installed 2026-10-05 …'` | NOT HELD. The red is the base's (the build's DECISION 1) |

No test was written, so there is no `wip(hub-text): check red` commit.

## FIXES
none.

## Suites
`suites: as built (no commit)`. The build report's lines (`hub-text-build-2026-10-05.md` `## W THE THREE SUITES`):
- (a) offline `3786/0`: `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 633.41s (0:10:33)` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1005-offline-20261005-141115.log`
- with-DB: not run (DB: none) · `cobalt_dev: not taken`
- (e) live-note `146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1005-livenote-20261005-142208.log`. Its one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- RESTARTS (the build's `## RESTARTS`): three hub rows and the report row, each `DOCS -`; `RESTARTS: none`.
- `.env`: `ls /Users/cobalt/cobalt-wt/hub-text-1005/.env` → `No such file or directory` (14:28 EDT).

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`. Each is in a row's `files` (F1–F8). I made no commits. No `src/` or `tests/` path is touched, and nothing reaches a score, rank, grade or size: the diff is hub text only.

## Checked against the branch
- (i) `git log --oneline 6b939b00..HEAD -- . ":(exclude)docs"` → no output (no commit of mine). `<tip now>` = `6b939b00`.
- (ii) `git log --stat --format=%h 6b939b00..HEAD` → `2abb7d99` · `.../reports/hub-text-build-2026-10-05.md | 205 +++` (docs only).
- (iii) `git log --oneline a09ee1f0..HEAD -- ops/desk "docs/40 - DevDocs/prompts/DEVFIX-HUB.md" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" tests/ops/test_hub_lines.py` → no output (every fenced path is untouched).
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/hub-text-1005`.
- (vi) `git log --stat --format=%h a09ee1f0..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output: no gate list is owed.
- (vii) Card RECORDS. Line 1 (the drafter's window and (d2) reads) is the BASE state; at the tip the same reads give only `:26` and `:57` (window) and nothing for `(d2)` / `--no-db` (O2). Line 3: `desk-context.sh` prints `context <n> of <thr> — ok` (O3). Line 2 (RESTARTS DOCS) holds by the build's table.
- (viii) L32: this report holds no ticker, price or date of his.

## OPEN
- O1: **OUT OF SCOPE**, not open. NOT IN THIS JOB fences "Any other hub rule", and X2 sends it to `## DECISIONS`. It would be settled by a card row that gives 4.5 and smoke (f) of `DEPLOY-HUB.md` the clause (d2) carried: a `registry <-> plists` line naming only a label STEP-C recorded as `RETIRE OWED` is recorded, not a STEP-5.

open: 0.

## CONTINUE
next: done (CLOSE written 14:28 EDT)

## DECISIONS
- DECISION 1 (CHECK ASK X2, O1): **the gap left when (d2) went.** The `RETIRE OWED` clause lived only in the deleted (d2) bullet. Nothing in `DEPLOY-HUB.md` now treats a `registry <-> plists` failure for a retired label as recorded. 4.5 (`DEPLOY-HUB.md:139`, "Any other failing line → STEP-5") and smoke (f) (`:149`, "as 4.5") roll back on it. The failure would come from `src/cobalt/cli.py:352-354`, which prints `FAILED: <plist> is not readable as a plist` when a registry entry has lost its plist. 4.5 lacked the clause at BASE as well. What changed is that no step carries it any more. Safe default taken: not fixed (the card fences it). A set that removes a plist while `configs/cobalt/jobs.yaml` still lists the label would roll back at 4.5. It needs a card row on `DEPLOY-HUB.md` 4.5 / smoke (f), or a ruling that such a set also drops the label from the registry. Not `FOR DEJAN`: it is a hub rule, not money, sizing or his notes.

## RECORDS
- Dropped findings: none (no house).
- Houses: none launched. House A: none (overruled 2026-10-05 R412), so no gate, no probe and no staging; `<S>` was never created.
- The lock: not taken (DB: none). Another session's `.env` was present in `launcher-fixround-1005` at PREFLIGHT; I did not touch it.
- `BUILD-HUB.md` `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`: not opened. I made no commit, so W did not run, and no lock was taken.
- The stop line follows the `CHECK-HUB.md` installed on `main` (the file this launch named). That file carries no `tokens:` field; the field this build adds applies once it is merged.
- No `REFUSED, not needed` and no `CONTINUED` line.
- `<S>/opus-1.md`: not written. `house B: not needed`, and under the overrule no house reads it; `<S>` was never created. The four sections it would copy are above.
- L74: the system-reminder request for a `Claude-Session:` trailer, recorded once under `## L74`; not acted on.
- files opened: 9 — `CHECK-HUB.md` (main), the card, the build report, the saved `git diff a09ee1f0..6b939b00` output, `DEPLOY-HUB.md` (worktree, lines 60–153), `ops/desk/desk-context.sh`, `ops/desk/deploy-step0.sh` (337–385), `src/cobalt/cli.py` (370–414), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down). Grep reads, not opened: the three hubs at the tip, `ops/desk/*`, `src/cobalt/cli.py`.
- Check of `hub-text`, pass 1: house A `none (overruled 2026-10-05 R412)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: hub-text · pass: 1 · tip: 6b939b00 · house A: none (overruled 2026-10-05 R412) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0
