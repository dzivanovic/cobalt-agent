# kill-hub-row-1010 — check read of the fix round (CHECK-HUB), 2026-10-11

## §0 Headline
CHECK DONE, ready: YES. The fix round's three lines equal the card's TEXT byte for byte (O1, O2), with `2 2` / `1 0` against `6fe8d690` (O3).
19 findings (11 mine, 8 from Grok; house B none, not needed). Held 0, dropped 0. 7 open, each REJECTED by a card line: A1–A5 (the card's "on BASE → 0" reds are against `6fe8d690`, not the pass-1 tip), A7 (residents per rule F is the ruled behaviour), and O7.
O7 is the one to read: THE ONE RESUME (`DEPLOY-HUB.md:53`, fenced) runs STEP-5 (3) and then reads (a)–(d) and can reach 4.2 again, while `:162` says "the run ends". After a failed kill, a relaunch could reach a second `--kill`. See `## DECISIONS`.
Suites at `b4d82ad6`: offline `4196/0`, live-note `146/0`, `tests/ops` `2789 passed`. No commit of mine. Main has since moved both hub files (`ca5c11aa`, `32a9f187`), away from `:137`, `:162` and `:149`.

## L74
A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded as data. Not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md"` · exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · df15e92ae79cc004fc59ed464680f10617322c85
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 157:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 "` → one row (line 35); `grep -n "^| R19 "` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:

```
clock · date · 0 · Sun Oct 11 09:46:27 EDT 2026
status · git status --short --branch · 0 · ## ops/kill-hub-row-1010
head · git log --oneline -1; git log --stat --format=%h b4d82ad6..HEAD · 0 · (5 lines)
    13bafad7 docs(kill-hub-row-1010): build report fix round — b4d82ad6
    13bafad7

     .../reports/kill-hub-row-build-2026-10-10.md       | 82 +++++++++++++++++++++-
     1 file changed, 80 insertions(+), 2 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/kill-hub-row-1010/docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md" · 0 · BUILT · job: kill-hub-row-1010 · tip: b4d82ad6 | on 6fe8d690 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 131138
range · git log --oneline 91c48f36..b4d82ad6 · 0 · (2 lines)
    b4d82ad6 fix(kill-hub-row-1010): fix round, --kill at 4.2 only after the loop, STEP-5 (3) dry run only, STANDING-LIST row 4.2 only (K1-K3, L1 L28 L72)
    379b4830 docs(kill-hub-row-1010): build report — 91c48f36
PREFLIGHT OK
```

THE RANGE, typed: `git log --stat --format=%h 91c48f36..b4d82ad6` · exit 0:

```
b4d82ad6

 docs/40 - DevDocs/prompts/DEPLOY-HUB.md    | 4 ++--
 docs/40 - DevDocs/prompts/STANDING-LIST.md | 2 +-
 2 files changed, 3 insertions(+), 3 deletions(-)
379b4830

 .../reports/kill-hub-row-build-2026-10-10.md       | 171 +++++++++++++++++++++
 1 file changed, 171 insertions(+)
```

Path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md`.

DB: none: `git diff --name-only --no-renames 91c48f36..b4d82ad6` · exit 0 → the same three paths, every one under `docs/`.

`ls <S>` (`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check`) · exit 0 → PRESENT: `diff-docs.md diff.md files house-a.md house-b.md HOUSE-INSTRUCTIONS.md rulings.md`. `ls -la` dates every entry Oct 10 17:28-17:41: the pass-1 check of this job (same JOB, so the same `<S>`). This launch carries no `CONTINUE:`, so this is not RECOVERY of my own run. I did not open any file in it.

House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:

```
grok: UP
gemini: UP
```

No header `HOUSE A: OpenAI` line, so Sol was not probed. `HOUSE B: as needed` → house A: Grok · house B: none (not needed).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" "/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check"` · exit 1:

```
REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check
```

The script refused before writing anything (`ops/desk/stage-set.sh:83-85`). No file was copied.

AFTER `CONTINUE: 1` (10:20 EDT, `<S>` moved to `kill-hub-row-1010-check-pass1` by the desk): the same call · exit 0:

```
107 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/diff.md
14463 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/284-kill-hub-card.md
25897 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/kill-hub-row-build-2026-10-10.md
58352 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
40606 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
16606 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/files/wt/docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md
368 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-hub-row-1010-check/rulings.md
STAGED 7 files · 156399 bytes · commits 0
```

`commits 0`, while PREFLIGHT's range has 2 commits. `diff.md` is the `":(exclude)docs"` diff (`stage-set.sh:121`, `k` counts `^commit ` in it at `:167`), and this card is DB: none with docs-only paths. `git log --oneline 91c48f36..b4d82ad6 -- . ":(exclude)docs"` · exit 0 → printed nothing. So the non-docs diff is complete and empty, and the count cannot reach 2 for any docs-only build. I went on; see `## DECISIONS`.

Added by me, because no house can run git: `<S>/diff-docs.md` (11437 bytes). It holds `git diff 91c48f36 b4d82ad6 -- "docs/40 - DevDocs/prompts"` (run in the background, exit 0, copied from its output) plus `git diff --numstat 91c48f36 b4d82ad6` → `2 2 DEPLOY-HUB.md`, `1 1 STANDING-LIST.md`, `171 0 kill-hub-row-build-2026-10-10.md`.

`stage-copy.sh`, one call each:
- `COPIED 2080 …/files/standing-list-kill-row-2026-10-10.md`
- `COPIED 2061 …/files/kill-sequence-amend-2026-10-10.md`
- `COPIED 819 …/files/kill-label-fix-2026-10-10.md`
- `COPIED 4333 …/files/kill-row-preflight-2026-10-10.md`
- `COPIED 10924 …/files/229-orphan-clean-card.md`
- `COPIED 17151 …/files/26-hub-text-card.md`
- `COPIED 12334 …/files/wt/ops/desk/orphan-clean.sh` (from `<WT>`)

Not copied: `ops/desk/bare-guard.py`. The card cites it only in the WHY and the fence, not in `## READ`.
`<S>/HOUSE-INSTRUCTIONS.md` (17191 bytes): the HOUSE TEXT verbatim, the card's `## ROWS` (with the TEXT blocks), `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS` whole, and the Files paragraph.
House gates at 10:22:51 EDT: R17 one row (line 35), R19 one row (line 37), `-S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`. Grok started at 10:23 EDT from `<AGY>` (`run_in_background`, timeout 2700000). After `cd <WT>`, `git status --short --branch` → `## ops/kill-hub-row-1010`.

## OWN FINDINGS
Written before either house list was opened. Each finding is stated as the defect it would be, so a NOT HELD run is a clean answer.

FINDING O1
ROW: K1, K2 (X4)
CLAIM: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:137` or `:162` at the tip is not byte-equal to the card's TEXT K1 NEW (card `:32`) or TEXT K2 NEW (card `:44`).
RUN: COMMAND `grep -n -x -F -f "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: among the non-blank hits, `137:` or `162:` is missing.

FINDING O2
ROW: K3 (X4)
CLAIM: `docs/40 - DevDocs/prompts/STANDING-LIST.md:149` at the tip is not byte-equal to the card's TEXT K3 (card `:50`).
RUN: COMMAND `grep -n -x -F -f "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/284-kill-hub-card.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: no `149:` among the non-blank hits.

FINDING O3
ROW: X4
CLAIM: against the card's TEXT OLD source `6fe8d690`, the two hub files change more than two lines plus one added line.
RUN: COMMAND `git diff --numstat 6fe8d690 b4d82ad6 -- "docs/40 - DevDocs/prompts"`
EXPECT: anything other than `2 2` for `DEPLOY-HUB.md` and `1 0` for `STANDING-LIST.md`.

FINDING O4
ROW: X1, K1, K2
CLAIM: `DEPLOY-HUB.md` has an `orphan-clean.sh` call beyond the three the rows build (`:137` dry run and `--kill aset`, `:162` dry run), or one with a label other than `aset`.
RUN: COMMAND `grep -n -o -F -e "orphan-clean.sh " "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: anything other than exactly `137:`, `137:`, `162:`.

FINDING O5
ROW: X1
CLAIM: the script the hub calls by absolute path (`/Users/cobalt/cobalt/ops/desk/orphan-clean.sh`, main) differs from `ops/desk/orphan-clean.sh` at `b4d82ad6`, whose printed lines (`:174`, `:250`, `:252`, `:296`) and label table (`:75-83`) the text quotes.
RUN: COMMAND `git -C /Users/cobalt/cobalt diff b4d82ad6 HEAD -- ops/desk/orphan-clean.sh`
EXPECT: a non-empty diff.

FINDING O6
ROW: X3
CLAIM: a hub line other than `DEPLOY-HUB.md:137`, or another seat's prompt, names `--kill aset`, which would imply that seat runs it under CLASS (a).
RUN: COMMAND `grep -rn -F -e "--kill aset" "docs/40 - DevDocs/prompts"`
EXPECT: a hit outside `DEPLOY-HUB.md:137`, `STANDING-LIST.md:149` and dated card files.

FINDING O7
ROW: X2, K2
CLAIM: two lines give different next steps after a dry run finds an orphan in a relaunch. `DEPLOY-HUB.md:162` (K2) says "the run ends under that DECISION 0". THE ONE RESUME (`DEPLOY-HUB.md:53`) runs STEP-5 (3) and "then read (a)–(d)", and when (a)–(d) hold it goes on through D0–D2 into 4.2 again. So after 4.2's `FAILED: <pid> survived KILL` and a FAILED stop, a `STEP-D0` relaunch could reach a second `--kill aset` on the same orphan, which the K3 row (`STANDING-LIST.md:149`, "no second kill") forbids.
RUN: COMMAND `grep -n -F "run STEP-5 (3) NOW" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `53:` with "otherwise run STEP-5 (3) NOW … then read (a)–(d)" and no exception for a STEP-5 (3) `DECISION 0: aset orphan`.

FINDING O8
ROW: X5, K2
CLAIM: the round-1 hold-down wording is still in `DEPLOY-HUB.md`, so STEP-5 (4) and the (5) `aset: <UP|DOWN>` field would meet a held-down aset.
RUN: COMMAND `grep -c -F "not held DOWN" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `1` or more.

FINDING O9
ROW: SCOPE (suite claim)
CLAIM: the build report's fix-round line `offline 4196/0` (`kill-hub-row-build-2026-10-10.md:221`, log `:879`) is not shown by its log.
RUN: COMMAND `grep -n -F "4196 passed" /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-offline-20261010-182001.log`
EXPECT: no hit, or a hit with `failed`.

FINDING O10
ROW: SCOPE (suite claim)
CLAIM: the build report's fix-round line `live-note 146/0` (`kill-hub-row-build-2026-10-10.md:222`) is not shown by its log.
RUN: COMMAND `grep -n -F "146 passed" /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-livenote-20261010-183054.log`
EXPECT: no hit, or a hit with `failed`.

FINDING O11
ROW: K3 (red first, last clause)
CLAIM: the two ops tests that read the hubs fail at the tip.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py`
EXPECT: `1 failed` or more.

## Findings
House A Grok's list: `<S>/house-a.md` (4641 bytes, 10:42 EDT), written by Grok itself, last line `FINDINGS: 8`. Its stdout was only the path. House B: none (not needed).
`grep -n -F "RUN:"` over it → 8 lines (`:4 :11 :18 :25 :32 :39 :46 :53`), each followed by one command line. All 8 kept.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| A1 | Grok | K1 | K1's red `ORPHAN-CLEAN, aset only` is already on the 4.2 line at `91c48f36`, so it does not fail on BASE. | COMMAND |
| A2 | Grok | K1 | `orphan-clean.sh --kill aset` is already on both removed lines at `91c48f36`, not 0 on BASE. | COMMAND |
| A3 | Grok | K2 | `the kill sequence:` and `orphan-clean.sh aset` are already on the removed STEP-5 line at `91c48f36`. | COMMAND |
| A4 | Grok | K3 | `killing the orphaned` is already at `91c48f36`; the STANDING hunk is `1 1`, so `wc -l` is not 220 → 221. | COMMAND |
| A5 | Grok | X4 | `91c48f36..` is `2 2`, `1 1` plus a report, not two changed lines plus one added line. | COMMAND |
| A6 | Grok | K2 | The build report's greens (`:98`, `:101`) claim `--kill aset` at `:162` and "not held DOWN"; the tip has neither. | COMMAND |
| A7 | Grok | X2 | A 4.2 failure does not keep aset down: STEP-5 (3) bootstraps per rule F; there is no second `--kill`. | COMMAND |
| A8 | Grok | X5 | STEP-5 (4)/(5) cannot tell a held-down aset from a restored one. | COMMAND |

## Dropped
none. Grok's commands begin `git -C /Users/cobalt/cobalt-wt/kill-hub-row-1010 diff`, which is `git diff` run in `<WT>` and is on my list (`Bash(git -C * diff*)`). I kept them; see `## RECORDS`.

## RUNS
Each command was run once at the tip (cwd `<WT>`, HEAD `13bafad7` = `b4d82ad6` plus the build report).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -n -x -F -f "<card>" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | non-blank hits: `137:4.2 for each of …` and `162:- (3) THE RESTORE: aset booted out → …` (every other hit is a blank line) | NOT HELD: both lines equal TEXT K1 NEW and K2 NEW byte for byte |
| O2 | own | same, on `STANDING-LIST.md` | non-blank hits: `149:| \`Bash(sh /Users/cobalt/cobalt/ops/desk/*)\` called as \`orphan-clean.sh --kill aset\` …` plus `|---|---|---|---|` lines | NOT HELD: `:149` equals TEXT K3 |
| O3 | own | `git diff --numstat 6fe8d690 b4d82ad6 -- "docs/40 - DevDocs/prompts"` | `2 2 docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `1 0 docs/40 - DevDocs/prompts/STANDING-LIST.md` | NOT HELD: X4 holds against TEXT OLD's source |
| O4 | own | `grep -n -o -F -e "orphan-clean.sh " DEPLOY-HUB.md` | `137:` `137:` `162:` | NOT HELD: three calls; with A6's run (`--kill aset` at `137:` only) and the round's `orphan-clean.sh aset` at `:137`, `:162`, all name `aset` |
| O5 | own | `git -C /Users/cobalt/cobalt diff b4d82ad6 HEAD -- ops/desk/orphan-clean.sh` | (no output) | NOT HELD: main's script equals the tip's; `:174` `none found`, `:252` `dry-run · verified <n>`, `:296` `FAILED: <pid> survived KILL` match the text (X1) |
| O6 | own | `grep -rn -o -F -e "--kill aset" "docs/40 - DevDocs/prompts"` | `DEPLOY-HUB.md:137` · `STANDING-LIST.md:149` · `2026-10-10/274-draft-kill-label-fix.md:3,5,6` · `2026-10-10/275-kill-row-repreflight-grok-read.md:4` | NOT HELD: the only hub line is `DEPLOY-HUB.md:137`; the other two hits are dated drafter prompts (X3) |
| O7 | own | `grep -n -F "run STEP-5 (3) NOW" DEPLOY-HUB.md` | `53:` "… otherwise run STEP-5 (3) NOW, whatever (a)–(d) say, and record the times … then read (a)–(d). … All of (a)–(d) true → … continue at STEP-D0, then D1 … and D2" | REJECTED — card K2 ("A verified orphan or exit 1 → no kill, … the run ends under the existing DECISION 0 path") and the fence ("Any other line of `DEPLOY-HUB.md`"): `:162` is as the card gives it, and `:53` is not this job's. The text is shown as claimed, so this stays OPEN |
| O8 | own | `grep -c -F "not held DOWN" DEPLOY-HUB.md` | `0` | NOT HELD (X5) |
| O9 | own | `grep -n -F "4196 passed" <offline log 182001>` | `879:4196 passed, 800 skipped, 1 xfailed, 36 warnings in 639.44s (0:10:39)` | NOT HELD |
| O10 | own | `grep -n -F "146 passed" <livenote log 183054>` | `57:146 passed, 1 skipped, 15 warnings in 25.21s` | NOT HELD |
| O11 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` | `85 passed, 15 warnings in 7.67s` | NOT HELD |
| A1 | Grok | `git -C <WT> diff -U0 91c48f36 HEAD -- ".../DEPLOY-HUB.md"` | `-4.2 … ORPHAN-CLEAN, aset only, once aset's print shows gone …` | REJECTED — card ROWS WHY ("each OLD is `git show 6fe8d690:<file>`") and card RECORDS line 1 (BASE = the pass-1 tip, a read of the fix round): the row's "on BASE → 0" reds are measured against `6fe8d690`. The fix round is pinned by the build's own reds at `91c48f36` (build report `:164-175`, e.g. `AFTER the loop, ONCE` 0 → 1, `survived KILL` 0 → 1). Shown as claimed; OPEN as card wording |
| A2 | Grok | same | the `-4.2` and `-- (3) THE RESTORE` lines both carry `orphan-clean.sh --kill aset` | REJECTED — as A1. At the tip it is `137:` only (A6 run) |
| A3 | Grok | same | the `-- (3) THE RESTORE` line carries `the kill sequence:` and `orphan-clean.sh aset` | REJECTED — as A1 |
| A4 | Grok | `git -C <WT> diff --numstat 91c48f36 HEAD -- ".../STANDING-LIST.md"` | `1 1 docs/40 - DevDocs/prompts/STANDING-LIST.md` | REJECTED — as A1; against `6fe8d690` it is `1 0` (O3) |
| A5 | Grok | `git -C <WT> diff --numstat 91c48f36 HEAD` | `2 2 DEPLOY-HUB.md` · `1 1 STANDING-LIST.md` · `249 0 docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md` | REJECTED — as A1 (O3 gives `2 2`, `1 0` against `6fe8d690`). The report row reads `249 0`, not the claimed `171 0`, because HEAD includes `13bafad7`. It is the build's own report, which the hub requires |
| A6 | Grok | `grep -n -F -e "orphan-clean.sh --kill aset" DEPLOY-HUB.md` | one hit, `137:` | NOT HELD: the report's `:98`–`:101` sit under `## E3 THE ROWS` of round 1, committed as `91c48f36` (report `:118`), and were true there. The fix round's greens (`:186` `137:` only, `:192` `not held DOWN` 0) match this run |
| A7 | Grok | `grep -n -F -e "each resident booted out" DEPLOY-HUB.md` | `162:` "… the run ends under that DECISION 0, residents per rule F. Then `launchctl bootstrap` each resident booted out, …", no `not held DOWN`, no `aset no bootstrap` | REJECTED — card K2 ("no hold-down, no new rule-F ending", "residents per rule F unchanged") and the build's fix of the pass-1 check's D2/D3: residents coming up per rule F is the ruled behaviour. Shown as claimed; OPEN |
| A8 | Grok | `grep -n -F -e "aset: <UP|DOWN|not in the set>" DEPLOY-HUB.md` | one hit, `164:` with no `held DOWN` or `orphan` | NOT HELD: K2 removed the hold-down (O8 → 0), so no held-down state exists to tell apart; an aset an orphan keeps from starting reads `DOWN` in (5) |

held: 0. No test was written, so there is no `wip(kill-hub-row-1010): check red` commit.

## FIXES
none (held: 0). No commit of mine; the tip stays `b4d82ad6` (HEAD `13bafad7`, docs only above it).

## Suites
On the tip `b4d82ad6` (HEAD `13bafad7`, docs only above it). There is no commit of mine. "DB: none" card: RESTARTS, then BUILD-HUB W (a0), (a), (e) and `tests/ops`; there is no `--deploy` (W (a0): "gate.sh accepts it with withdb and all only").
- RESTARTS: `uv run cobalt jobs restarts 91c48f36..HEAD` → `DEPLOY-HUB.md M DOCS -` · `STANDING-LIST.md M DOCS -` · `kill-hub-row-build-2026-10-10.md A DOCS -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 91c48f36` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md`. All under `docs/`. `cobalt_dev: not taken (DB: none — 3 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 offline` · exit 0 → `offline 4196/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-offline-20261011-104512.log`. Log `:879` reads `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 641.00s (0:10:41)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh kill-hub-row-1010 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/kill-hub-row-1010-livenote-20261011-105607.log`. Log `:57` reads `146 passed, 1 skipped, 15 warnings in 25.74s`. The one SKIPPED (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `2789 passed, 1 xfailed, 15 warnings in 507.38s (0:08:27)`.
- With-DB: not run (DB: none). `cobalt_dev: not taken`.
- `.env`: `ls /Users/cobalt/cobalt-wt/kill-hub-row-1010/.env` → `No such file or directory` (11:05 EDT). No lock was taken.

## Scope
PREFLIGHT's path union (`91c48f36..b4d82ad6`): `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (K1, K2), `docs/40 - DevDocs/prompts/STANDING-LIST.md` (K3), and `docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md` (the build's report). Every path is a row's `files` or the report. There is no commit of mine. Hunks: `@@ -137 +137 @@`, `@@ -162 +162 @@` and `@@ -146,7 +146,7 @@` (the one `:149` line); nothing inside the fence.

## Checked against the branch
- (i) `git log --oneline b4d82ad6..HEAD -- . ":(exclude)docs"` → no output. No commit of mine; `<tip now>` = `b4d82ad6`.
- (ii) `git log --stat --format=%h b4d82ad6..HEAD` → `13bafad7` · `.../reports/kill-hub-row-build-2026-10-10.md | 82 +++++++++++++++++++++-` · `1 file changed, 80 insertions(+), 2 deletions(-)`. Docs only.
- (iii) `git log --oneline 91c48f36..HEAD -- ops tests .claude "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → no output (fence held). The launch line `DEPLOY-HUB.md:11` and the other lines are outside the K1/K2 hunks (A1 run: `@@ -137 +137 @@`, `@@ -162 +162 @@` only).
- (iv) No HELD finding, so there is no test to find.
- (v) at `## 8`.
- (vi) `git log --stat --format=%h 91c48f36..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output. No migration and no with-DB test, so the gate lists are not needed.
- (vii) Card RECORDS line 2: `git -C /Users/cobalt/cobalt log --oneline -1` → now `af127d13 docs(desk): deploy card 353 shadow-hub, R1068` (main has moved since the card's `6fe8d690`). `git -C /Users/cobalt/cobalt diff --stat 6fe8d690 HEAD -- <both hub files>` → `DEPLOY-HUB.md | 2 +-` · `STANDING-LIST.md | 13 +++++++++++++`. So "main's working files equal BASE" no longer holds. `git -C /Users/cobalt/cobalt log --oneline 6fe8d690..HEAD -- <both files>` → `ca5c11aa feat(held-closed-1010): …` and `32a9f187 feat(ops-hand-install-1010): …`. Their hunks (`git -C /Users/cobalt/cobalt diff 6fe8d690 HEAD -- <both files>`): DEPLOY-HUB `@@ -56,7 +56,7 @@` (the P2 fix-round sub-bullet), and STANDING-LIST `@@ -218,3 +218,16 @@` (a new `## 8. OPS-HAND.md` after the file's end). Neither touches `:137`, `:162` or `:149`. The new `## 8` lists no `Bash(sh …)` string, so the ops-hand seat is not implied to run `orphan-clean.sh` (X3). Card RECORDS lines 3, 4 and 6 are about `BASE` content and the staged copies; O1–O3 and A1–A5 above re-read them through the diff. Line 5 (RESTARTS none) → `## Suites`.
- (viii) L32: this report holds no ticker, price or date of his. The times are clock times from `date`.

## OPEN
FOLLOW-UP (there is no second pass). Each item ran and showed its claim, and a card line says the built text is right:
- O7 (X2, K2): after a dry run in STEP-5 (3) finds an orphan, `DEPLOY-HUB.md:162` says "the run ends under that DECISION 0". THE ONE RESUME (`:53`) runs STEP-5 (3) "NOW … then read (a)–(d)" and, when they hold, goes on to D0–D2 and the outage. So after 4.2's `FAILED: <pid> survived KILL`, a `STEP-D0` relaunch could reach a second `--kill aset` on the same orphan. That would contradict the K3 row's "no second kill". To settle it: a card that adds, at `:53`'s (e), "a STEP-5 (3) `DECISION 0: aset orphan` ends the resume there" (`:53` is fenced here), or a desk ruling that the K2 "the run ends" binds the resume. See `## DECISIONS`.
- A1, A2, A3, A4, A5 (K1, K2, K3, X4): the card's red-first "on BASE → 0" and X4's `1 0` hold against `6fe8d690` (the TEXT OLD source; O3 → `2 2`, `1 0`), not against the card's `BASE: 91c48f36` (A4/A5 → `1 1`). The fix round itself was shown red by the build at `91c48f36` (build report `:164-175`). To settle it: card wording only. A fix-round card names `6fe8d690` for its "on BASE" reds, or gives reds at the pass-1 tip.
- A7 (X2): a 4.2 failure leads STEP-5 (3) to bootstrap aset per rule F, even with an orphan holding the lock or port. That is K2's ruled "residents per rule F unchanged, no hold-down" (and the pass-1 check's D2/D3 answer). To settle it: only a new ruling, if a held-down aset is wanted after all.

## CONTINUE
next: none (CHECK DONE 11:05 EDT)

## DECISIONS
- O7, OPEN, lies outside the card's rows (`DEPLOY-HUB.md:53` is fenced). A `STEP-D0` relaunch after a failed 4.2 kill runs STEP-5 (3)'s dry run. `:162` says "the run ends under that DECISION 0", but `:53` says "then read (a)–(d)" and, when they hold, goes on to D0, D1, D2 and the outage. So 4.2 could run `--kill aset` a second time on the same orphan, which the K3 row (`STANDING-LIST.md:149`) forbids. Proof: the O7 run (`grep -n -F "run STEP-5 (3) NOW"` → `53:`) and the A7 run (`:162`). Default taken: nothing changed (the card's TEXT is built as given; `:53` is fenced). The merge is fenced until his yes anyway (R926, R937). For the desk before that merge: either a one-line card at `:53` (e) ("a STEP-5 (3) `DECISION 0: aset orphan` ends the resume there"), or a ruling that K2's "the run ends" binds the resume.
- ASK DESK: `stage-set.sh` printed `commits 0`, but PREFLIGHT's range has 2 commits. CHECK-HUB `## 1` reads a mismatch as `FAILED: copy — the diff is incomplete`. Here the diff is not incomplete: `diff.md` excludes `docs`, and `git log --oneline 91c48f36..b4d82ad6 -- . ":(exclude)docs"` printed nothing. Any docs-only (DB: none) card will hit the same mismatch. Should the rule compare `k` to the non-docs commit count instead? [2026-10-11 10:22 EDT] Default taken: I went on (no more access, no house twice) and gave the houses the docs diff as `<S>/diff-docs.md`.

## RECORDS
- I opened none of the pass-1 files in `<S>`. CHECK-HUB's NOT list includes earlier checks of this branch.
- No lock was taken, no `.env` was written, and there was no commit (`git status --short --branch` → `## ops/kill-hub-row-1010`). A `wip` commit was not needed because nothing changed.
- First session (09:46–09:47 EDT): files opened: 4 — `CHECK-HUB.md`, the card `284-kill-hub-card.md`, `ops/desk/stage-set.sh` lines 1-110 (read to see what the refusal means), and the house-probe output file. Its ASK DESK (`<S>` not empty, 09:47 EDT; default: nothing touched, stopped under UNATTENDED RULES (b)) was answered by the desk's move of `<S>` to `kill-hub-row-1010-check-pass1`.
- CONTINUED at 1 10:20 EDT. The desk message read `CONTINUE: step 1 stage dir moved to pass1.` I checked it with `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/`: `kill-hub-row-1010-check-pass1` is listed and `kill-hub-row-1010-check` is not. RECOVERY calls: `git status --short --branch` → `## ops/kill-hub-row-1010`; `git log --oneline -1` → `13bafad7`; `ls -la <WT>/.env` → No such file. The ASK DESK under `## DECISIONS` is answered by this move.
- This session opened 20 more files: `CHECK-HUB.md` (again), the card (again), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), this report, `ops/desk/stage-set.sh` `:110-169`, `<S>/diff.md`, `<S>/rulings.md`, `DEPLOY-HUB.md` (`:1-40`, `:125-181`), `ops/desk/orphan-clean.sh`, `STANDING-LIST.md` `:138-153`, the build report (`:93-120`, `:121-250`), `BUILD-HUB.md` `:76-91`, `kill-sequence-amend-2026-10-10.md`, `kill-label-fix-2026-10-10.md`, `standing-list-kill-row-2026-10-10.md`, `kill-row-preflight-2026-10-10.md`, `<S>/house-a.md`, and three tool-output files (the `git diff` of the fix round, Grok's stdout, and main's diff of the two hubs). The gate verdict outputs were read with `tail`/Read and are counted as one. Read by `grep` only, not opened: card 229 (`| O1 `), `cto-2026-09-24.md` (R17, R19), the gate logs, and `house-a.md`'s `RUN:` lines. files opened: 24 (4 + 20).
- Not opened: LAWS.md (no law acted on beyond the card's one-liners), the pass-1 check report and `<S>-pass1`, the design document.
- Grok's commands began `git -C /Users/cobalt/cobalt-wt/kill-hub-row-1010 diff …`, not `git diff …`. I kept them as runnable (same command in `<WT>`, on my list), not dropped.
- Added by me to `<S>`: `diff-docs.md`, because the only diff the hub stages excludes `docs` and every commit here is docs-only (see `## DECISIONS`, the `commits 0` item).
- Houses: Grok `grok-4.7` started 10:23 EDT, its notice arrived by 10:43 EDT, and it wrote `house-a.md` (`FINDINGS: 8`) itself. House B: none (not needed; `HOUSE B: as needed`, Gemini UP at PREFLIGHT, not seated). No house produced nothing; no house sat twice.
- No `REFUSED, not needed` line. No lock take. No L74 block in a tool result. The session's system context again carried a `Claude-Session:` commit-line request; that is the same item as `## L74` and was not acted on (no commit was made).
- Main moved on both hub files after the card (`ca5c11aa`, `32a9f187`; `## Checked against the branch` (vii)). The hunks lie away from this branch's lines; the merge is the desk's (fenced).
- Check of `kill-hub-row-1010`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- The `house B:` field of the stop line reads `none (not needed)`, as PREFLIGHT records it. Gemini was UP, so `none available` would misstate it.

CHECK DONE · job: kill-hub-row-1010 · pass: 1 · tip: b4d82ad6 · house A: Grok FINDINGS: 8 · findings: 19 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 7 · house B: none (not needed) · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 24 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 242415
