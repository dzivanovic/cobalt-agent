# x15-hitl-probe-port — check 2026-10-21

## §0 Headline
The port at `304d5f3b` equals `c1b4b785` byte for byte on six spec files; `cli.md` differs only by main's three f5-probe lines, kept before the x15 block.
House A Grok: `FINDINGS: 0`. Opus-own: 7 findings (X1–X5, card 977's suite), all NOT HELD by run. Nothing fixed, no commit.
Deploy gate: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS `com.cobalt.aset com.cobalt.cos com.cobalt.radar`. ready: YES.

## L74
One system reminder asked for a `Claude-Session:` line on commits; recorded, not followed.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` (16:58 EDT) → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 0 · b644eb74c223f12c89875b37e5077ca618e56121
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:
```
clock · date · 0 · Wed Oct 21 16:58:35 EDT 2026
status · git status --short --branch · 0 · ## ops/x15-hitl-probe-port
head · git log --oneline -1; git log --stat --format=%h 304d5f3b..HEAD · 0 · (6 lines)
    c062baf7 docs(x15-hitl-probe-port): build report — 304d5f3b
    c062baf7
    
     .../x15-hitl-probe-port-build-2026-10-21.md        | 205 +++++++++++++++++++++
     .../x15-hitl-probe-port-build-2026-10-21.result    |  15 ++
     2 files changed, 220 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/x15-hitl-probe-port/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f5-probe-x4-fix/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/x15-hitl-probe-port/docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md" · 0 · BUILT · job: x15-hitl-probe-port · tip: 304d5f3b | on fb9c8963 | migration: none | offline 4960/0 | with-DB 5932/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 175249
range · git log --oneline fb9c8963..304d5f3b · 0 · (2 lines)
    304d5f3b feat(x15-hitl-probe-port): port card 977's X15 probe from c1b4b785, cli.md keeps main's f5-probe section (C1 C2 D1 D2, L3 L72)
    563cb338 wip(x15-hitl-probe-port): red — T1 tests ported byte-equal to c1b4b785
PREFLIGHT OK
```
The lock: `/Users/cobalt/cobalt-wt/f5-probe-x4-fix/.env` is held by another job; this check waits for it at W.

THE RANGE, `git log --stat --format=%h fb9c8963..304d5f3b`:
```
304d5f3b
 docs/40 - DevDocs/cobalt/aset/web.md    |  4 ++++
 docs/40 - DevDocs/cobalt/cli.md         |  3 +++
 docs/40 - DevDocs/cobalt/hitl/README.md |  3 +++
 src/cobalt/aset/web.py                  | 37 +++++++++++++++++++++++++++++----
 src/cobalt/hitl/cli.py                  | 34 +++++++++++++++++++++++++++++-
 5 files changed, 76 insertions(+), 5 deletions(-)
563cb338
 tests/cobalt/test_hitl_x15.py            | 267 +++++++++++++++++++++++++++++++
 tests/cobalt/test_s3_c3_panel_offline.py |   2 +-
 2 files changed, 268 insertions(+), 1 deletion(-)
```
Path union (7): the seven spec files of the card. The card has no `DB: none` line.

`ls <S>` → `No such file or directory` (fresh).

House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) → exit 0:
```
grok: UP
gemini: UP
```
No header line → `house A: Grok · house B: none (not needed)` (card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → output whole:
```
32 …/x15-hitl-probe-port-check/STAGED-CARD
16953 …/x15-hitl-probe-port-check/diff.md
16380 …/x15-hitl-probe-port-check/files/994-x15-hitl-probe-port-card.md
33511 …/files/wt/docs/40 - DevDocs/cobalt/aset/web.md
9205 …/files/wt/docs/40 - DevDocs/cobalt/cli.md
4614 …/files/wt/docs/40 - DevDocs/cobalt/hitl/README.md
115485 …/files/wt/src/cobalt/aset/web.py
2013 …/files/wt/src/cobalt/hitl/cli.py
9509 …/files/wt/tests/cobalt/test_hitl_x15.py
38049 …/files/wt/tests/cobalt/test_s3_c3_panel_offline.py
29257 …/files/x15-hitl-probe-port-build-2026-10-21.md
386 …/x15-hitl-probe-port-check/rulings.md
STAGED 12 files · 275394 bytes · commits 2
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/x15-hitl-probe-port-check`; commits 2 = PREFLIGHT's range count.)
`stage-copy.sh` card 977 → `COPIED 16948 …/files/977-x15-hitl-probe-card.md`; card 977's check → `COPIED 27011 …/files/x15-hitl-probe-check-2026-10-21.md`.
`<S>/spec.md` written by me (Write) from `git diff 41804777 c1b4b785 --` the seven paths (the card's `## READ` spec; the house cannot run git) and `git diff 41804777 fb9c8963 -- cli.md`; the 267 lines of the new test file are named by blob `6ee0069d`, not retyped. `<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
House A Grok started 17:01 EDT (`date` 17:01:29), `run_in_background`, timeout 2700000; house B none.

## OWN FINDINGS
Written 17:0x EDT, before any house list was opened. My read: the card, card 977's rows by the card's summary, the port diff and the seven files at `304d5f3b` (via `git diff c1b4b785 304d5f3b -- <seven paths>`, a read of the diff (3), run once while writing this section), the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line, BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`, `areas/cobalt.md` from `## What Cobalt is` and `## Build rules` down. The read shows the six unchanged files empty and `cli.md` differing only by main's f5-probe block; the findings below are each CHECK ASK put as the defect it would be, so a run settles it.

FINDING O1
ROW: X1 / E1 (a)
CLAIM: one of the six files main did not change differs from the spec commit at the port tip (`src/cobalt/aset/web.py:1436`, `src/cobalt/hitl/cli.py:1` are the spec's hunks).
RUN: COMMAND `git diff c1b4b785 304d5f3b -- src/cobalt/aset/web.py src/cobalt/hitl/cli.py tests/cobalt/test_hitl_x15.py tests/cobalt/test_s3_c3_panel_offline.py "docs/40 - DevDocs/cobalt/aset/web.md" "docs/40 - DevDocs/cobalt/hitl/README.md"`
EXPECT: any output line (empty output = NOT HELD).

FINDING O2
ROW: X1 / X2 / D2
CLAIM: `docs/40 - DevDocs/cobalt/cli.md` at the tip differs from `c1b4b785` by more than main's three f5-probe lines, or carries a `-` line, or puts x15-hitl-probe before f5-probe.
RUN: COMMAND `git diff c1b4b785 304d5f3b -- "docs/40 - DevDocs/cobalt/cli.md"`
EXPECT: a `-` line, or a `+` line other than the blank, `## 2026-10-21 — f5-probe` and the `checkpoints_cli.add_parser(sub)` line, or the f5-probe block after the x15 block.

FINDING O3
ROW: X1 / E1 (c)
CLAIM: the port's per-file stat over the seven paths differs from the spec's.
RUN: COMMAND `git diff --stat fb9c8963 304d5f3b -- src/cobalt/aset/web.py src/cobalt/hitl/cli.py tests/cobalt/test_hitl_x15.py tests/cobalt/test_s3_c3_panel_offline.py "docs/40 - DevDocs/cobalt/aset/web.md" "docs/40 - DevDocs/cobalt/hitl/README.md" "docs/40 - DevDocs/cobalt/cli.md"` beside the same with `41804777 c1b4b785`
EXPECT: a file whose count differs between the two outputs.

FINDING O4
ROW: X2 / SCOPE
CLAIM: the port touched a path other than the seven spec files, its build report and its `.result`.
RUN: COMMAND `git diff --stat fb9c8963 c062baf7`
EXPECT: a path outside those nine.

FINDING O5
ROW: X3 / R1
CLAIM: the tool's RESTARTS line on the range is not `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
RUN: COMMAND `uv run cobalt jobs restarts fb9c8963..304d5f3b`
EXPECT: a last line other than `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.

FINDING O6
ROW: X4
CLAIM: a `## DEPLOY PROOF` smoke line of the card is not the admitted `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/…` form, or the section holds `127.0.0.1:5010` or `uv run`.
RUN: COMMAND `grep -n -F "127.0.0.1" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md"` (and `grep -n -F "curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/"`, `grep -n -F "uv run"` on the same file, each read against the section's lines 55-60)
EXPECT: a `127.0.0.1` or `uv run` hit inside lines 55-60, or a `curl` line of 59-60 missing from the second grep.

FINDING O7
ROW: T1 / C1 / C2 (card 977's suite on the port)
CLAIM: card 977's offline suite is not green at the port tip.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_s3_c3_panel_offline.py`
EXPECT: a `failed` count above 0.

## Findings
House A Grok finished 17:08 EDT (`date` 17:08:58); its stdout: `I'll read the house instructions first and follow them exactly.The port matches the spec on the files I could check. I am writing the finding list./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/x15-hitl-probe-port-check/house-a.md` (`[exited with code 0]`). `<S>/house-a.md` (12 bytes), whole: `FINDINGS: 0`. House B: none (not needed).
No house finding to keep.

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `git diff c1b4b785 304d5f3b --` the six files | no output | NOT HELD |
| O2 | opus-own | `git diff c1b4b785 304d5f3b -- "docs/40 - DevDocs/cobalt/cli.md"` | `@@ -150,5 +150,8 @@`; three `+` lines only: `## 2026-10-21 — f5-probe`, the `checkpoints_cli.add_parser(sub)` line, a blank; no `-` line; f5-probe sits before `## 2026-10-21 — x15-hitl-probe`. Each `+` line equals main's (`git diff 41804777 fb9c8963 -- cli.md`: `+`, `+## 2026-10-21 — f5-probe`, `+\`checkpoints_cli.add_parser(sub)\` now also mounts …`); git aligns the blank after the block rather than before it | NOT HELD |
| O3 | opus-own | `git diff --stat` port `fb9c8963 304d5f3b` beside spec `41804777 c1b4b785`, seven paths | both: `aset/web.md 4 +`, `cli.md 3 +`, `hitl/README.md 3 +`, `web.py 37`, `hitl/cli.py 34`, `test_hitl_x15.py 267`, `test_s3_c3_panel_offline.py 2`; `7 files changed, 344 insertions(+), 6 deletions(-)` both | NOT HELD |
| O4 | opus-own | `git diff --stat fb9c8963 c062baf7` | 9 files: the seven, `x15-hitl-probe-port-build-2026-10-21.md` 205, `.result` 15; `9 files changed, 564 insertions(+), 6 deletions(-)` | NOT HELD |
| O5 | opus-own | `uv run cobalt jobs restarts fb9c8963..304d5f3b` | `src/cobalt/aset/web.py M static import reach com.cobalt.aset,com.cobalt.cos,com.cobalt.radar`; `src/cobalt/hitl/cli.py M static import reach com.cobalt.radar`; docs `DOCS -`; tests `test/documentation; no resident -`; last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` | NOT HELD |
| O6 | opus-own | three `grep -n -F` on the card | `127.0.0.1` → `:52`, `:69`, `:80` only (CHECK ASKS, DECISIONS, RECORDS; none in 55-60); the curl form → `:59` (`…/hitl/x15-probe`), `:60` (`…/`) plus `:52`, `:80`; `uv run` → `:22`, `:28`, `:32`, `:51`, `:52`, `:63`, none in 55-60 | NOT HELD |
| O7 | opus-own | `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_s3_c3_panel_offline.py` | `80 passed, 9 skipped in 2.28s` | NOT HELD |
No test was written, so none is removed and no `wip(x15-hitl-probe-port): check red` commit is made.

## FIXES
none (nothing held).

## Suites
RESTARTS (BUILD-HUB `## RESTARTS`): `uv run cobalt jobs restarts fb9c8963..304d5f3b` → last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (table whole under `## RUNS` O5); no `UNCLASSIFIED` row, no `jobs.yaml` change. No commit of mine, so the tip is the build's `304d5f3b` (code); HEAD `c062baf7` adds the build report only.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh x15-hitl-probe-port all --deploy --deploy-gate` (background; no `--deselect`, `--tickers` or `--migration`: no with-DB test, ticker or migration in the diff) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9086/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5932/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/x15-hitl-probe-port-all-20261021-170922.log
```
From the log (`grep -n -F " passed"`): `:957` `4960 passed, 878 skipped, 4 xfailed` (tests/cobalt + taxonomy offline) and `:1032` `4126 passed, 1 xfailed` (tests/ops, the deploy gate) → offline 9086; `:1276` `5688 passed, 9 skipped, 138 deselected, 7 xfailed` (pass 1) + `:2258` `244 passed, 1 deselected` (pass 2) = 5932; `:2459` `148 passed, 1 skipped`. `grep -n -F "OUTSIDE the allowed set" <log>` → no line. `code: c062baf7 (clean)` at `:1099`, `:1355`, `:2325`, `:2382`.
`.env`: the gate's `.env: removed`; `ls /Users/cobalt/cobalt-wt/x15-hitl-probe-port/.env` at 17:58 → exit 1, `No such file or directory`. `git status --short --branch` → `## ops/x15-hitl-probe-port`.

## Scope
PREFLIGHT's path union: the seven spec files (`src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, `docs/40 - DevDocs/cobalt/aset/web.md`, `docs/40 - DevDocs/cobalt/hitl/README.md`, `docs/40 - DevDocs/cobalt/cli.md`), each in a row's `files`; above the tip, the build report and its `.result` (the card admits them). Commits of mine: none.

## Checked against the branch
(i) `git log --oneline 304d5f3b..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `304d5f3b`.
(ii) `git log --stat --format=%h 304d5f3b..HEAD` → `c062baf7`: `x15-hitl-probe-port-build-2026-10-21.md` 205, `.result` 15; docs only.
(iii) `git log --oneline fb9c8963..HEAD --` the fenced `src/cobalt/hitl/card.py`, `store.py`, `actions.py`, `executor.py`, `src/cobalt/notify`, `src/cobalt/redact`, `configs/cobalt/redact.yaml`, `tunables.yaml`, `notify.yaml` → empty. Main's f5-probe block is unedited (O2).
(iv) no HELD finding: nothing to check.
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/x15-hitl-probe-port` alone.
(vi) `git log --stat --format=%h fb9c8963..HEAD -- src/cobalt/db_migrations tests/cobalt` → `563cb338`: `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, both offline (no new migration, no with-DB test needing a level above `0013`): no gate-lists change owed.
(vii) card records: `git -C /Users/cobalt/cobalt log --oneline 41804777..HEAD -- "docs/40 - DevDocs/cobalt/cli.md"` → `c2565a9f feat(f5-probe): cobalt checkpoint probe X4/X5/X6/X7/X10/X13, the keep seam (P1 P2 G1 X6 X4 X13 H1 C1 D0, L1 L28 L32 L45)` (as the record says); `ls /Users/cobalt/cobalt-wt/` → now lists `x15-hitl-probe-port` (the build made it after the drafter's read) and `x15-hitl-probe`. The `grep -c` markers are the card's DEPLOY PROOF on main and read `0` before a deploy by the record; not re-run on main here.
(viii) L32: this report holds no ticker, price or date of his; the host name it quotes is the card's own text.

## OPEN
none.

## CONTINUE
next: done (stop line written 17:59)

## DECISIONS
none

## RECORDS
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits; not followed (CHECK-HUB L74: `Co-Authored-By` only). No commit was made.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/x15-hitl-probe diff --stat c1b4b785 -- src tests docs/40\ -\ DevDocs/cobalt` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode."
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/x15-hitl-probe log --oneline -3` — same message.
- REFUSED, not needed: `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <task output> <S>/files/spec-diff-41804777-c1b4b785.txt` — `REFUSED: the source is not under a job worktree or the main tree's docs/: …`; the spec went to the house as `<S>/spec.md`, written by me (`## Files copied`).
- Dropped findings: none. Houses that produced nothing: none (Grok wrote `FINDINGS: 0`). House B not seated (card `HOUSE B: as needed`); Gemini UP, unused.
- Extra lock takes: none (one, inside `gate.sh`, `lock: waited 0 min`). No `CONTINUED` line.
- `.env: removed, proven gone (W)`.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh be4462a6` → `context 157088 of 400000 — ok`.
- files opened: 10 — CHECK-HUB.md, the card, BUILD-HUB.md (`## THE LOCK` to `## W`), the build report (`## RESTARTS` to the last line), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `<S>/house-a.md`, and four task outputs (house probe, spec diff, Grok stdout, gate).
- Check of `x15-hitl-probe-port`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088
