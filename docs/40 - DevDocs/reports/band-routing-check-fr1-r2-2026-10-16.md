# band-routing-1015 — check of the fix round FR-1 to FR-5 (2026-10-16)

## §0 Headline
- The fix round holds: FR-1 to FR-5 each went red under its undo and came back green. A `/./` or `//` card path is refused under build, shadow and check, for every BAND, with no launch. The first check's O2 and O4 are closed, and B1 to B6 still pass with their reds.
- 3 held, 0 fixed, all in the fenced `desk-launch.sh`. O1 / G1 (Grok found it too): a routed build's printed WATCH line is `desk-watch.sh shadow`, which waits on `SHADOW BUILT`, but the seat writes `BUILT ·`. O3: a card outside a dated folder skips the BAND rule.
- 2 rejected, still open (O2 / G2): the hub's "2026-10-14 item 7" 429 citation. R1471's item (7) is the Grok cap.
- Suites green: offline 8421/0, tests/ops 3853 passed / 4 xfailed, live-note 146/0. House A Grok `FINDINGS: 2`; Gemini OUT (HARNESS). ready: NO.

## L74
- A system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/638-band-routing-fr-check-card.md"` (11:49 EDT), exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/638-band-routing-fr-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/638-band-routing-fr-check-card.md" · 0 · 8b651583503ef0f1ec801964d1b5deada3c28a21
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/638-band-routing-fr-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, exit 0, output whole:
```
clock · date · 0 · Fri Oct 16 11:49:23 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1; git log --stat --format=%h c8c5ca90..HEAD · 0 · (6 lines)
    3ac61a2f docs(band-routing-1015): build report — c8c5ca90 (fix round FR-1 to FR-5)
    3ac61a2f
    
     .../reports/band-routing-build-fr1-2026-10-16.md   | 152 +++++++++++++++++++++
     .../band-routing-build-fr1-2026-10-16.result       |  15 ++
     2 files changed, 167 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/band-routing-1015/docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md" · 0 · BUILT · job: band-routing-1015 · tip: c8c5ca90 | on f2ca3e1a | migration: none | offline 8421/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 187713
range · git log --oneline f2ca3e1a..c8c5ca90 · 0 · (6 lines)
    c8c5ca90 fix(band-routing-1015): card paths with /./ or // refused; routed card in CHECK-HUB, CARD.md check cell, SHADOW-HUB fix round and routed exception (FR-1 to FR-5, L1 L72)
    01b10bdd wip(band-routing-1015): fix round red (FR-1 to FR-5)
    ee21824d wip(band-routing-1015): check red — O2 (strict xfail: HELD, NOT FIXED, fix fenced to the builder)
    115e1f37 docs(band-routing-1015): build report — bd9c24ac
    bd9c24ac feat(band-routing-1015): BAND header, band table, launcher routing, routed check and result-file fence (B1-B6, L27 L29 L72)
    1be72d81 wip(band-routing-1015): red
PREFLIGHT OK
```
- THE RANGE, typed: `git log --stat --format=%h f2ca3e1a..c8c5ca90` → six commits: c8c5ca90 (CARD.md 2, CHECK-HUB.md 4, SHADOW-HUB.md 6, desk-launch.sh 1, test_band_routing_1015.py 5, test_check_hub_shadow.py 3; 10+/11−) · 01b10bdd (test_band_routing_1015.py +92) · ee21824d (test_band_routing_1015.py +11) · 115e1f37 (band-routing-build-2026-10-15.md +201, .result +15) · bd9c24ac (BUILD-HUB.md +2, CARD.md +3, SHADOW-HUB.md 11, bare-guard.py +5, desk-launch.sh 71, preflight.sh 26; 111+/7−) · 1be72d81 (test_band_routing_1015.py +567). Commit count 6.
- DB: none: `git diff --name-only --no-renames f2ca3e1a..c8c5ca90` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`. Every path is under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (exit 0), lines whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
- Seats: no `HOUSE A: OpenAI` header line; Grok UP → **house A: Grok · house B: none (not needed)** (`HOUSE B: as needed`). Gemini OUT is HARNESS (the model id is not recognized), not METER; no return time named.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check`), output whole:
```
44996 <S>/diff.md
22754 <S>/files/638-band-routing-fr-check-card.md
20584 <S>/files/band-routing-build-fr1-2026-10-16.md
34998 <S>/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
20258 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
43727 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
17252 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
25728 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md
220 <S>/files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result
56410 <S>/files/wt/ops/desk/bare-guard.py
136385 <S>/files/wt/ops/desk/desk-launch.sh
11676 <S>/files/wt/ops/desk/preflight.sh
29539 <S>/files/wt/tests/ops/test_band_routing_1015.py
4899 <S>/files/wt/tests/ops/test_check_hub_shadow.py
363 <S>/rulings.md
STAGED 15 files · 469789 bytes · commits 5
```
(the script printed absolute paths; `<S>` abbreviates them here.) `commits 5` against PREFLIGHT's 6: the diff is `git log -p f2ca3e1a..c8c5ca90 -- . ":(exclude)docs"`, and `git log --oneline f2ca3e1a..c8c5ca90 -- . ":(exclude)docs"` → five commits (c8c5ca90, 01b10bdd, ee21824d, bd9c24ac, 1be72d81); the sixth, `115e1f37`, is docs-only (`git log --stat`: the two build-report files). `grep -c "^commit "` over `diff.md` → `5`. The diff is complete for its own range; see `## DECISIONS` (ASK DESK 1).
`stage-copy.sh`, one call each (bytes = `wc -c` of the original, one call):
- `583-band-routing-card.md` → `COPIED 55079` · original 55079
- `band-routing-check-2026-10-16.md` → `COPIED 35110` · original 35110
- `band-routing-check-decisions-2026-10-16.md` → `COPIED 5193` · original 5193
- `band-routing-answer-2026-10-16.md` → `COPIED 4651` · original 4651
- `cto-2026-10-15.md` → `COPIED 28538` · original 28538
- `files/wt/ops/desk/desk-done.sh` → `COPIED 7293` · original 7293 (X5)
- `files/wt/ops/desk/deploy-card.sh` → `COPIED 37206` · original 37206 (X2, X5)
- `files/wt/ops/desk/desk-watch.sh` → `COPIED 12054` · original 12054 (X2)
- `files/wt/src/cobalt/jobs/restarts.py` → `COPIED 12098` · original 12098 (R3)
`<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the `Files:` paragraph.
House A Grok started 11:52 EDT (`date` 11:51:58, gates R17 / R19 re-run: one row each, `5055151d…` non-empty; `ls -la <S>` → `diff.md`, `files`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`), `run_in_background`, timeout 2700000. House B: none (not needed). After the return: `git status --short --branch` → `## ops/band-routing-1015`.

## OWN FINDINGS
Written 11:54 EDT, before any house list was opened. Read: the card, the build report (`## E2 RED` to `## RECORDS`), the first check's `## RUNS`, `## OPEN`, `## DECISIONS`, the brain's direction, `desk-launch.sh` `:956-1019`, `:1636-1685`, `:2354`, `desk-watch.sh` `:40-79`, `desk-done.sh` `:1-69`, `test_band_routing_1015.py` whole, `cobalt.md` from `## What Cobalt is` and from `## Build rules` down.

FINDING O1
ROW: X5 (FR-5)
CLAIM: A LOW or MID `build` re-enters as `shadow … --routed` (`ops/desk/desk-launch.sh:1667`), so the WATCH line it prints is `watch_line "$kind" "$card"` with `kind=shadow` (`:2354`, `:288`); `desk-watch.sh shadow` waits on `^(SHADOW BUILT|SHADOW ROLE|FAILED)` (`ops/desk/desk-watch.sh:64`), while FR-5's `SHADOW-HUB.md:70` clause makes the routed seat write `BUILT ·`. The watcher the launcher hands the desk never sees a routed build's DONE line.
RUN: TEST — `tests/ops/test_band_routing_1015.py`
```python
def test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line(desk):
    done = desk.run("build", str(desk.card_for("LOW")))
    assert done.returncode == 0, done.stderr
    printed = done.stdout + done.stderr
    assert "desk-watch.sh shadow " not in printed, printed
```
EXPECT: `1 failed`, the assertion fails with the printed `WATCH: sh …/desk-watch.sh shadow "…/01-x-band-card.md"`.

FINDING O2
ROW: X4 (FR-4)
CLAIM: `SHADOW-HUB.md:28` cites "2026-10-14 item 7: a 429 is retried, never a backup", but the one 2026-10-14 ruling with numbered items, R1471 (`reports/cto-2026-10-14-words.md:9`), has item (7) = "Grok cap of 3 removed"; no 2026-10-14 file under `reports/` holds a 429 rule.
RUN: COMMAND — `grep -n -F "(7)" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14-words.md"`
EXPECT: `9:Relayed by the brain (quoted): … (7) Grok cap of 3 removed; …` and no line naming 429.

FINDING O3
ROW: B3 (O2 class, X1)
CLAIM: The BAND date is the first folder under `$PROMPTS` (`ops/desk/desk-launch.sh:1645-1650`), and the path gate admits any `"$PROMPTS"/*-card.md` (`:991`); a card placed outside a dated folder (`$PROMPTS/01-x-band-card.md`) has no date, so a card with no `BAND` builds on the Opus line with no refusal — the same bypass O2 closed for `/./`, by another path shape.
RUN: TEST — `tests/ops/test_band_routing_1015.py`
```python
def test_o3_a_card_outside_a_date_folder_still_needs_its_band(desk):
    card = desk.card_for(None)
    flat = desk.prompts / card.name
    flat.write_text(card.read_text())
    desk.commit("flat card")
    done = desk.run("build", str(flat))
    assert done.returncode == 1, done.stdout + done.stderr
```
EXPECT: `1 failed`, `assert 0 == 1` with stdout the Opus `claude --bg … --model claude-opus-5-5` line.

## Findings
Grok finished 12:01 EDT (`date` 12:01:07; task exit 0). `ls -la <S>` → `house-a.md` 2572 bytes, 12:01. Grok wrote `house-a.md` itself; its stdout was progress text and the path. Its last line: `FINDINGS: 2`. THE DROP: `grep` of each block's `RUN:` line → both carry one (a `def test_` and a `grep` command).
- G1 · grok · X5 · a routed `build` prints `WATCH: … desk-watch.sh shadow`, which waits on `SHADOW BUILT`; the routed seat ends on `BUILT ·` (`SHADOW-HUB.md:70`), so neither watcher nor `desk-done shadow` admits it · TEST
- G2 · grok · X4 · `SHADOW-HUB.md:28` cites item 7 as "never a backup", the direction says "never a stop", card 583 "fallback"; the probe-OUT clause is not in R1532 · COMMAND

## Dropped
none

## RUNS
Each test was put in `tests/ops/test_band_routing_1015.py` with Edit and run (`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short <file>::<the three tests>`, one call, 12:0x EDT): `3 failed, 15 warnings in 1.67s`. No test's form or assertion was changed.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `::test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line` | `:407: AssertionError` · printed `WATCH: sh …/ops/desk-watch.sh shadow "…/prompts/2026-10-16/01-x-band-card.md"` after `BAND: LOW → grok-4.7 (backup gpt-5.6-terra)` and `ROUTED: a real build — BRANCH ops/x-band · REPORT …/x-band-build.md` | HELD, NOT FIXED — `ops/desk/desk-launch.sh` (`:2354`; the card's `## NOT IN THIS JOB` fences every edit of it). `desk-watch.sh shadow` waits on `^(SHADOW BUILT\|SHADOW ROLE\|FAILED)` (`desk-watch.sh:64`); `desk-watch.sh build` would wait on `<job>-build` (`:71`), not the seat's `<job>-gate` name |
| O2 | opus | `grep -n -F "(7)" ".../reports/cto-2026-10-14-words.md"` | `9:Relayed by the brain (quoted): "I want all, including 5, and I want to remove Grok's limit of 3." Items: (5) brain relays marked "Dejan said" count as his confirmation; (7) Grok cap of 3 removed; K5 cards (1) …, (6) card template.` | REJECTED — card 583 FR-4 (`583-band-routing-card.md:47`) gives the clause byte for byte, and the brain's direction row 4 (`band-routing-check-decisions-2026-10-16.md:14`) rules it. R1471's item (7) is the Grok cap, not a 429 rule. OPEN |
| O3 | opus | `::test_o3_a_card_outside_a_date_folder_still_needs_its_band` | `:416: assert 0 == 1`; stdout is `claude --bg "Read '…/BUILD-HUB.md' … CARD: '…/prompts/01-x-band-card.md'" --model claude-opus-5-5 …` and `WATCH: … desk-watch.sh build …` | HELD, NOT FIXED — `ops/desk/desk-launch.sh` (`:991` admits any `$PROMPTS/*-card.md`; `:1645-1650` reads the date only from the first folder). The failure goes to the safe band (Opus), as O2 of the first check did |
| G1 | grok | `::test_x5_routed_build_watch_does_not_wait_on_built` | `:423: AssertionError: ['WATCH: sh …/ops/desk-watch.sh shadow "…/2026-10-16/01-x-band-card.md"']` · `assert [...] == []` | HELD, NOT FIXED — `ops/desk/desk-launch.sh` (the same defect as O1, by another assertion) |
| G2 | grok | `grep -n -F -e "probe is OUT" -e "a 429 is retried, never a stop" -e "a 429 is retried, never a backup" -e "fallback on a 429" -e "LOW/MID Grok 4.7 + Terra backup" <SHADOW-HUB.md> <decisions> <cto-2026-10-15.md> <583 card>` | `SHADOW-HUB.md:28` (`probe is OUT` … `never a backup`); `band-routing-check-decisions-2026-10-16.md:3` (`2026-10-14 item 7 (a 429 is retried, never a stop)`) and `:14`; `cto-2026-10-15.md:102` (`LOW/MID Grok 4.7 + Terra backup`, no `probe is OUT`); `583-band-routing-card.md:38`, `:39`, `:47`, `:61` (`a fallback on a 429 (retried, R1471 item 7)`) | REJECTED — card 583 FR-4 gives the text byte for byte; the brain's direction row 4: "The backup causes (probe OUT, harness FAILED) are what 'backup' means under R1532". The three wordings of item 7 differ ("never a stop", "never a backup", "never a fallback"). OPEN |

The held tests carry `@pytest.mark.xfail(strict=True, reason="check r2 <id>: HELD, NOT FIXED — ops/desk/desk-launch.sh (fenced)")` (the first check's form, its ASK DESK [09:57]); the assertions are as written above. `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `48 passed, 3 xfailed, 15 warnings in 9.81s` (the three XFAIL lines name O1, O3, G1). Commit `7bf43c2b wip(band-routing-1015): check red — O1 O3 G1 (strict xfail: HELD, NOT FIXED, desk-launch.sh fenced)`.

THE CARD'S RUN ROWS, on the tip `c8c5ca90` (the check's one commit adds only the three xfail tests):
- S0: `git diff --name-only --no-renames ee21824d c8c5ca90` → `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py` (exactly the six). `git diff --stat c8c5ca90 3ac61a2f -- . ":(exclude)docs"` → nothing. `git diff --name-only --no-renames f2ca3e1a..c8c5ca90` → 11 paths (PREFLIGHT): nine code/hub/test paths plus the two build-report files; no `src/`, `configs/`, `.claude/`. `git diff --stat ee21824d c8c5ca90 -- tests/ops` → `test_band_routing_1015.py | 97 ++++…--` · `test_check_hub_shadow.py | 3 +-` · `2 files changed, 95 insertions(+), 5 deletions(-)`; the second is `L6_LINE` only (2+, 1−). `git diff ee21824d c8c5ca90 -- ops/desk/desk-launch.sh` → ONE hunk `@@ -994,6 +994,7 @@`, the one added line `+    */./*|*//*) refuse "the card path holds '/./' or '//': $card" ;;`.
- FR-1: `:990-998` read on the tip: the first `case "$card"` (`:990-993`) pins `"$PROMPTS"/*-card.md`; the second (`:994-998`) holds the character class, `*..*` and the new arm. Both sit after `case "$kind"` (`:971-979`: build, check, deploy, recut, devfix, shadow, prodwrite) and before any `field` read (`:1005`), so every one of those seven kinds crosses it; desk, prompt, brain, close and install-ops leave earlier. `grep -n -F xfail` of the test file on the tip → no hit (now three, the check's own markers). RED: the arm deleted with Edit → `-k "test_o2_ or test_fr1_"` → `2 failed, 1 passed`: `test_o2_…` `:381: … assert 0 == 1` (stdout the Opus line, `CARD: '…/prompts/./2026-10-16/01-x-band-card.md'`), `test_fr1_a_double_slash…` `:392: … assert 0 == 1` (`…/prompts//2026-10-16/…`); `test_fr1_control…` passed. Undone: `git diff --stat c8c5ca90 -- ops/desk/desk-launch.sh` → nothing. EXTRA RUN (a probe test, removed again; `git diff --stat HEAD -- tests/ops/test_band_routing_1015.py` → nothing): `build` and `shadow --model grok-4.7 --routed` NOT dry in the `desk` tmp desk, and `check` dry in the `cdesk` tmp desk (the `desk` helper has no CHECK-HUB.md: its first run of `check` gave `REFUSED: the fixed file is not installed: …/CHECK-HUB.md`, six cases, a harness gap, re-run on `cdesk`), each for `/./` and `//` and for BAND none, LOW, HIGH → `18 passed`: each exit 1, stderr `REFUSED: the card path holds '/./' or '//': <the path>`, and for build/shadow the fake `claude` call log absent.
- FR-2: `git diff ee21824d c8c5ca90 -- CHECK-HUB.md` → two one-line hunks `@@ -61,7 +61,7 @@` and `@@ -114,7 +114,7 @@` (quoted in `## Files copied` context; both lines `+CHECK-HUB §7(v) and \`## PREFLIGHT\`: on a shadow card or a routed card (BAND LOW or MID, dated on or after BAND_FROM), \`?? SHADOW-INSTRUCTIONS.md\` at the worktree root is expected and recorded, not a finding.`). The `## 7.` (v) step reads `ls <WT>/.env` → "No such file"; `git status --short --branch` → `## <BRANCH>` alone`, and the line under it now excepts a routed card. RED: both lines back to `on a shadow card,` (Edit, replace all) → `-k "fr2 or l6"` over both test files → `2 failed, 1 passed`: `test_fr2_check_hub_…` `:438: assert 0 == 2` (the card's `:415` is the control, which passed), `test_check_hub_shadow.py::test_l6_…` `:77: AssertionError: [] assert 0 == 2`. Undone: `git diff --stat c8c5ca90 -- CHECK-HUB.md` → nothing.
- FR-3: `git diff ee21824d c8c5ca90 -- CARD.md` → one hunk, one line (the check cell). RED: the cell back to `optional` → `-k fr3` → `1 failed, 2 passed`: `:456: AssertionError:  optional` / `assert 'required' in ' optional '`; the control `test_fr3_control_…[2026-10-16]` and `[2026-01-02]` PASSED (a check card with no `BAND`, a clean tree: `check` exits 0, no `REFUSED`). Undone: `git diff --stat c8c5ca90 -- CARD.md` → nothing. FR-3 is drafter text: no code reads the cell (the launcher's check arm reads `BAND` only for `routed_tree`, `desk-launch.sh:1791-1794`); the control is the launcher's `optional otherwise`.
- FR-4: `git diff ee21824d c8c5ca90 -- SHADOW-HUB.md` → three hunks `:28`, `:53`, `:70`. X4 citations read: R1532 (`cto-2026-10-15.md:102`) → `LOW/MID Grok 4.7 + Terra backup`; 2026-10-14 R1471 item (7) (`cto-2026-10-14-words.md:9`) → `Grok cap of 3 removed`. RED: `:28` back to the ee21824d clauses → `-k fr4` → `1 failed, 1 passed`: `:467: AssertionError: its own fresh job card with BAND: HIGH`; control passed. Undone: `git diff --stat` → nothing.
- FR-5: RED: both notes removed (Edit, replace all; the tool also joined `:53`/`:54` and `:70`/`:71`, the red is the same) → `-k fr5` → `1 failed, 1 passed`: `:485: assert [0, 0] == [1, 1]`; control passed. Undone (both notes and both line breaks back): `git diff --stat c8c5ca90 -- SHADOW-HUB.md` → nothing. X5: see O1 / G1 — the stop line the clause names is the one `desk-done.sh build` (`:47` `^BUILT`), `check` and `deploy-card.sh` read, but the WATCH line the launcher prints for the routed seat is `desk-watch.sh shadow`, and `desk-done.sh shadow` waits on `^SHADOW (BUILT|ROLE)` (`:54`).
- D1 / X1: `git diff ee21824d c8c5ca90 -- tests/ops/test_band_routing_1015.py`, the `test_o2_…` hunk: the three marker/comment lines removed; ONE assertion changed `-    assert BAND_REFUSAL in done.stderr, done.stderr` → `+    assert "REFUSED: the card path holds '/./' or '//'" in done.stderr, done.stderr`; `card = desk.card_for(None)`, the `"/./"` path build, `desk.run("build", odd)` and `assert done.returncode == 1` are unchanged context. Intent kept: the probe above shows exit 1 and no `claude` call under build and shadow, for every BAND, and exit 1 with no stdout under check.
- H1: the first check's `## OPEN` rows (`band-routing-check-2026-10-16.md:245-246`): `- O2 HELD, NOT FIXED — ops/desk/desk-launch.sh. Settled by the builder's fix round: the card path gates (:990-997) refuse /./ and //, or the day is read from the path's real folder. Then remove the strict xfail and test_o2_… passes.` · `- O4 HELD, NOT FIXED — docs/40 - DevDocs/prompts/CHECK-HUB.md. Settled by one hub line: :64 / :117 read "on a shadow card or a routed card (BAND LOW or MID, dated 2026-10-16 or later)". …`. O2 CLOSED (FR-1 above; on the tip the marker is gone and `test_o2_…` PASSED without `--runxfail`). O4 CLOSED (FR-2). O1 CLOSED by FR-3 (text; the drafter copies `BAND`). O3/G3: the fix-round clause CLOSED by FR-4; the backup citation stays OPEN (O2, G2 of this check). G2 CLOSED by FR-5's text, but its watch path is OPEN (O1, G1). G1 (PASS-2) OUT OF SCOPE (brain row 6).
- B*: B1 `grep -c -F "BAND" CARD.md` → `2`, the check cell `required when …` (FR-3 above). B2/B4/B6 and the test file: the whole-file run above (`48 passed, 3 xfailed`; every `test_b*` and every control PASSED, listed in `-rA`). B3 `grep -n -F -e "BAND_FROM=20261016" -e "band_row()" -e "--routed)"` → `393:            --routed)`, `1643:BAND_FROM=20261016`, `1652:band_row() {`. B4 `grep -n -F "BAND (his 2026-10-15 R1532):" BUILD-HUB.md` → `12:` (one line). `git diff -U0 f2ca3e1a c8c5ca90 -- desk-launch.sh preflight.sh bare-guard.py`: `desk-launch.sh` hunks at `:379`, `:392-395`, `:997`, `:1636-1686`, `:1715-1716`, `:1721`, `:1738`, `:1789-1794`, `:1815` (the last, in the check arm; no hunk in the launch tail or install-ops); `preflight.sh` `:118-133`, `:159`, `:165-171`; `bare-guard.py` `:1277-1281`. Mutations: see `## Suites` order below.
- R3: `uv run cobalt jobs restarts f2ca3e1a..c8c5ca90` → the four hubs and the two build-report files `DOCS -`; `bare-guard.py`, `desk-launch.sh`, `preflight.sh` `M operator script; no Cobalt reader -`; `test_band_routing_1015.py` `A test/documentation; no resident -`, `test_check_hub_shadow.py` `M test/documentation; no resident -`; `RESTARTS: none` = the header.
- T1: `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → `18: import subprocess`, `195`, `272`, `274`, `285`, `554`, `556`, `559`, `561`, `605`, `651`, `657` (the tmp-repo git helper and the runs of the launcher, preflight.sh and bare-guard.py): no `git show`, no 8-hex hash. `git diff --stat f2ca3e1a c8c5ca90 -- <the eleven files>` → ` tests/ops/test_check_hub_shadow.py | 3 ++-` only. The test file: `48 passed, 3 xfailed` (the three xfails are this check's held tests; the card's "no xfailed" held at `c8c5ca90`).

B* MUTATIONS (one per row, the first check's, each made with Edit, run, undone with Edit, the undo proved by `git diff --stat c8c5ca90 -- <file>` printing nothing):
- B1 `| \`BAND\` |` → `| \`BANDX\` |`: `-k b1` → `1 failed, 1 passed` · `:70: assert 0 == 1`.
- B2 the `| LOW |` band row deleted: `-k b2` → `1 failed, 2 passed` · `:95: AssertionError: ('LOW', [])`.
- B4 `BAND (his R1532):`: `-k b4` → `1 failed, 1 passed` · `:126: assert 0 == 1`.
- B3 the `exec sh "$0" shadow` line removed: `-k b3` → `4 failed, 12 passed` (`[LOW]`, `[MID]` `:299: assert 'MODEL: grok-4.7' in …` with the Opus line; `…keeps_the_signed_row…` `:286: assert 0 == 1`; `…real_build_not_a_shadow` `:353`), as the first check's 4.
- B5 `1LOW|1MID) routed_tree=1` → `1LOWX|1MIDX`: `-k b5` → `2 failed, 8 passed` · `:576: … is not clean (the check session commits there)` for `[LOW]`, `[MID]`.
- B6 G5 compares `report + ".result"`: `-k b6` → `2 failed, 1 passed` · `:665: … assert 2 == 0` · `:680: (…/x-band-build.md.result, '') assert 0 == 2`.
After the last undo: `git status --short --branch` → `## ops/band-routing-1015`.
- T1 neighbours, no edit: `uv run pytest -q -p no:cacheprovider --color=no <the eleven files of row T1>` → `550 passed, 16 warnings in 157.78s (0:02:37)`.

## FIXES
- O1: HELD, NOT FIXED — `ops/desk/desk-launch.sh`
- O3: HELD, NOT FIXED — `ops/desk/desk-launch.sh`
- G1: HELD, NOT FIXED — `ops/desk/desk-launch.sh`
No fix commit: the card's `## NOT IN THIS JOB` fences "any edit of `ops/desk/desk-launch.sh` … beyond a mutation that is undone in the same row", and its rows name no file this check may change. No DevDocs line (no module changed).

## Suites
On the tip now, `7bf43c2b` (the build's `c8c5ca90`, its report `3ac61a2f`, and the check's three strict-xfail tests). DB: none card, so W is (a0), (a), (e).
- RESTARTS: `uv run cobalt jobs restarts f2ca3e1a..HEAD` → the R3 table plus the fix-round report `.md` and `.result` (`A DOCS -`) → `RESTARTS: none`.
- (a0): `git diff --name-only --no-renames f2ca3e1a` → the 11 paths of PREFLIGHT plus `docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md` and `.result` (13). Every path is under `ops/`, `tests/ops/` or `docs/`. `cobalt_dev: not taken (DB: none — 13 paths)`.
- (a): `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline --deploy-gate` (exit 0), whole output: `tests/ops: run (deploy gate)` · `offline 8421/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261016-120704.log`. Log `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 689.84s (0:11:29)` · `:959` `3853 passed, 4 xfailed, 16 warnings in 839.93s (0:13:59)` (three xfails are this check's O1, O3, G1; one is the tree's own, as in the build's `1 xfailed`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3853 passed, 4 xfailed, 16 warnings in 853.21s (0:14:13)`.
- (e): `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` (exit 0) → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261016-123250.log`. The only skip, `:56` `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, does not name `COBALT_LIVE_VAULT_ROOT`.
- With-DB: not run (DB: none). `.env`: never present. `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory` (12:47); `git status --short --branch` → `## ops/band-routing-1015` alone.
- Every held finding's test is a strict xfail, not a pass: the held items are not fixed (`## FIXES`), so `ready: NO`.

## Scope
PREFLIGHT's path union (11 paths of `f2ca3e1a..c8c5ca90`: four hubs, two build-report files, three `ops/desk` scripts, two test files) matches S0. My one commit, `7bf43c2b`, touches only `tests/ops/test_band_routing_1015.py` (26 insertions: three strict-xfail tests). No `src/`, `configs/` or `.claude/` path; no fenced file was edited (every mutation undone; `git status` clean).

## Checked against the branch
- (i) `git log --oneline c8c5ca90..HEAD -- . ":(exclude)docs"` → `7bf43c2b wip(band-routing-1015): check red — O1 O3 G1 (strict xfail: HELD, NOT FIXED, desk-launch.sh fenced)`; `<tip now>` = `7bf43c2b`.
- (ii) `git log --stat --format=%h c8c5ca90..HEAD` → `7bf43c2b` `tests/ops/test_band_routing_1015.py | 26 +` · `3ac61a2f` the fix-round report `.md` and `.result` (docs). No other path.
- (iii) `git log --oneline f2ca3e1a..HEAD -- .claude/settings.json .claude/settings.json.bak src configs LAWS.md` → nothing. `git log --oneline c8c5ca90..HEAD -- ops/desk "docs/40 - DevDocs/prompts" tests/ops/test_check_hub_shadow.py` → nothing (the fenced scripts, hubs and `CARD.md` carry only the build's own commits).
- (iv) `grep -n -F` of the three `def` lines → `404:` O1, `412:` O3, `422:` G1 (one line each). All three are HELD, NOT FIXED: no `fix(` commit; their `wip(…): check red` commit is `7bf43c2b`.
- (v) see `## Suites`.
- (vi) `git log --stat --format=%h f2ca3e1a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no migration and no with-DB test; gate lists not owed.
- (vii) Card records: `git log --oneline -5 ops/band-routing-1015` → `7bf43c2b` (this check), `3ac61a2f`, `c8c5ca90`, `01b10bdd`, `ee21824d` (the record's five, shifted by mine; `115e1f37` sits below). `git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015` → `7bf43c2b`. `grep -n -F "*/./*" ops/desk/desk-launch.sh` → `997:` only. `grep -c -F "is expected and recorded, not a finding" CHECK-HUB.md` → `2`. `git diff --stat c8c5ca90 3ac61a2f -- . ":(exclude)docs"` → nothing (S0).
- (viii) L32: this report quotes no ticker, price or date of his; the dates are card folder days, ruling dates and constructed test days.

## OPEN
- O1 / G1 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. A routed build's WATCH line is `desk-watch.sh shadow …`, which waits on `SHADOW BUILT`, while the routed seat writes `BUILT ·`. Settled when the launcher prints a watch whose regex admits `^BUILT` and whose session is `<job>-gate` (a `desk-watch.sh` kind for a routed seat, or the build kind with the gate's session name), then the two strict xfails go.
- O3 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. A card outside a dated folder builds Opus with no BAND. Settled when `:991` pins `"$PROMPTS"/<8 digits with dashes>/*-card.md`, or an undated card is refused; then the strict xfail goes.
- O2 / G2 REJECTED (card 583 FR-4 text, brain direction row 4). Settled by the desk naming the ruling the 429 clause rests on: R1471's item (7) is "Grok cap of 3 removed", and the three wordings of "item 7" differ (`never a stop`, `never a backup`, `never a fallback`).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. O1 / G1 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. A LOW or MID `build` re-enters as `shadow … --routed` (`:1667`), and the WATCH line it prints comes from `watch_line "$kind" "$card"` (`:2354`), with `kind=shadow`: `WATCH: sh …/desk-watch.sh shadow "<card>"`. That watcher waits on `^(SHADOW BUILT|SHADOW ROLE|FAILED)` (`desk-watch.sh:64`). FR-5's `SHADOW-HUB.md:70` clause makes the routed seat end on `BUILT ·`, so the watcher never sees a routed build finish; only a FAILED line or its IDLE/GONE exits reach the desk. `desk-watch.sh build` is no answer either: it watches session `<job>-build` (`:71`), and the routed seat is `<job>-gate`. RUNS rows O1, G1; tests `tests/ops/test_band_routing_1015.py::test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line` and `::test_x5_routed_build_watch_does_not_wait_on_built` (strict xfail, `7bf43c2b`). Safe default taken: not fixed (the card fences every edit of `desk-launch.sh`), and the desk closes a routed seat with `desk-done.sh <id> <report> build` (`:47` `^BUILT`) until a fix lands. It goes to the builder's one fix round on this card.
2. O3 HELD, NOT FIXED — `ops/desk/desk-launch.sh`. `:991` admits any `"$PROMPTS"/*-card.md`, and the BAND date is the first folder under `$PROMPTS` (`:1645-1650`). A card with no `BAND` placed at `$PROMPTS/01-x-band-card.md` (no dated folder) launches the Opus line with no refusal: the same bypass the first check's O2 found for `/./`, by another path shape. RUNS row O3; test `::test_o3_a_card_outside_a_date_folder_still_needs_its_band` (strict xfail, `7bf43c2b`). The failure goes to the safe band (Opus); no LOW/MID launch comes from it. Safe default taken: not fixed (fenced). It goes to the builder's fix round, or the desk rules that an undated card is an older card (then this test is removed).
3. ASK DESK [11:50]: `stage-set.sh` printed `STAGED 15 files · 469789 bytes · commits 5`; PREFLIGHT's range has 6 commits. The staged diff is `git log -p f2ca3e1a..c8c5ca90 -- . ":(exclude)docs"`; that range has 5 commits (the sixth, `115e1f37`, is docs only), and `grep -c "^commit "` over `diff.md` → `5`. Safe default taken: the diff was taken as complete and the house was started; the hub files were staged whole under `files/wt/`. The hub's count rule could name the docs-excluded count.
4. ASK DESK [12:05]: the held tests of HELD, NOT FIXED findings would turn every suite red. I committed them as `@pytest.mark.xfail(strict=True, reason="check r2 <id>: HELD, NOT FIXED — ops/desk/desk-launch.sh (fenced)")`, assertions unchanged (the first check's form). Safe default taken: that form; the fix round's pass then shows as a strict-xfail red until each marker goes.
5. O2 / G2 (REJECTED, open): `SHADOW-HUB.md:28` cites "2026-10-14 item 7: a 429 is retried, never a backup". The only 2026-10-14 ruling with numbered items, R1471 (`cto-2026-10-14-words.md:9`), has item (7) "Grok cap of 3 removed". The brain's direction says "never a stop" (`:3`) and card 583 says "never a fallback" (`:39`, `:61`). The "probe is OUT / harness FAILED" causes are not in R1532's row; the brain's direction row 4 reads them into "backup". Safe default taken: the hub text stands, as card FR-4 gave it. The desk names the source of item 7, or a card row re-cites it.
House B: none (not needed; `HOUSE B: as needed`). Gemini OUT at the probe. No item touches his notes, money or sizing: for Dejan 0.

## RECORDS
- Gemini probe OUT: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (a HARNESS line; the card fences the probe's model id as a K5 card of its own). Not launched; no house B needed.
- Grok's stdout was progress text plus the path; it wrote `house-a.md` itself (2572 bytes, 12:01). I read it only after `## OWN FINDINGS` was written (11:54).
- Dropped findings: none. No REFUSED call, no CONTINUE, no lock take, no `.env`.
- The FR-1 extra run used a probe test, added and removed with Edit; its first form ran `check` in the `desk` helper, which carries no CHECK-HUB.md (`REFUSED: the fixed file is not installed`, six cases); re-run on `cdesk`. `git diff --stat HEAD -- tests/ops/test_band_routing_1015.py` → nothing after removal.
- The FR-5 mutation (Edit, replace all of the note with its leading blank) also joined `:53`/`:54` and `:70`/`:71`; the restore put both notes and both line breaks back (`git diff --stat c8c5ca90 -- SHADOW-HUB.md` → nothing).
- CHECK ASKS: X1 / D1 — intent kept: exit 1 and no `claude` call for `/./` and `//` under build, shadow and check, for BAND none, LOW, HIGH (18 probe cases). Recommendation: keep the changed assertion; the path arm refuses before any field is read, so a BAND text in that refusal would claim a read that never happened. X2 — `grep -n -F "desk-launch.sh"` over `deploy-card.sh`, `desk-watch.sh`, `desk-done.sh`, `desk-wake.sh`, `desk-handover.sh` → comments and `desk-watch.sh:175`, `:182` (`install-ops` only); no caller builds a card path. `PROMPTS="$REPO/docs/40 - DevDocs/prompts"` (`:219`) with `REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}` (`:217`); `Grep` of `ops/` for `COBALT_REPO_ROOT=` → no hit. None named. X3 — the FR-3 control passed on both dates; B5's controls (no BAND, HIGH, older LOW) still refused "not clean" (PASSED in the whole-file run). FR-3 is text only: the drafter's rule is the only gate for a routed build's check card. X4 — O2, G2. X5 — O1, G1. X6 — the 429 clause (O2/G2) is the one added sentence whose cited ruling does not say it; the fix-round clause cites note 7 (`band-routing-answer-2026-10-16.md`), the CHECK-HUB and CARD lines restate R1532's routing. X7 — Grok wrote one test and one `grep` command; no keyed call was run by this check.
- files opened: 27 — CHECK-HUB.md; the card 638; BUILD-HUB.md (`:33-94`); the fix-round build report; `band-routing-check-2026-10-16.md` (`:178-267`); `cobalt.md` (`:20-24`, `:33-64`); `desk-launch.sh` (`:940-1019`, `:1636-1685`, `:2340-2369`); `desk-watch.sh` (`:40-79`); `desk-done.sh` (`:1-69`); `test_band_routing_1015.py`; `house-a.md`; the house-probe, grok and T1-suite task outputs (3); and, by grep, `583-band-routing-card.md`, `band-routing-check-decisions-2026-10-16.md`, `band-routing-answer-2026-10-16.md`, `band-routing-fr-check-card-preflight-2026-10-16.md`, `band-routing-fixround-preflight-2026-10-16.md`, `589-draft-583-amend.md`, `cto-2026-10-14-words.md`, `cto-2026-10-15.md`, `cto-2026-09-24.md`, `rulings.md`, `diff.md` (count), `deploy-card.sh`, `CARD.md`, `SHADOW-HUB.md`.
- Check of `band-routing-1015`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 7bf43c2b · house A: Grok FINDINGS: 2 · findings: 5 · dropped: 0 · held: 3 · fixed: 0 · held unfixed: 3 · open: 5 · house B: none available · suites: offline 8421/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 27 · ready: NO · decisions: 5 · for Dejan: 0 · tokens: 311395
