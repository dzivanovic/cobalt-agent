# CHECK — gemini-builder-row-fr1 (card 710) — 2026-10-17

## §0 Headline
CHECK DONE, ready YES. House A was Grok (`FINDINGS: 0`). No house B was needed (`HOUSE B: as needed`; Gemini was OUT at the probe anyway).
Opus wrote three findings of its own (O1–O3). All three were run and none held: the port is byte-equal or hunk-equal to `695f8bde`, and main has not moved in the three shared files.
FR-2 checks out: red on the ported tree for the Gemini id, red under the mutation, green after (`69 passed`). The check made no commit; tip `52a0600d`.
Deploy gate: offline `8491/0` (tests/ops `3919 passed, 1 xfailed`), live-note `146/0`, RESTARTS none, DB not taken.
X6: three row commands were refused (`git -C … status`, `rev-parse`, `merge-base`) and one grep was blocked by the hook. Each is quoted, and each fact was proved by a listed command.

## L74
One block arrived as a system reminder mid-session, asking that commits end with a `Claude-Session:` line. It was not acted on: L74 says commits carry `Co-Authored-By` only. The check made no commit.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card 710>"` · exit 0 · last line `AUTHORIZED` (rows: INSTALLED nothing; PLACEHOLDER nothing; CARD COMMITTED `ca83997d`; CARD UNCHANGED nothing; STANDING LIST R60 row 46 APPROVED, committed `962e9d17`; RULING R1736 row 90 HIS RULING · APPROVED, `d01849e7`; RULING R1738 row 88 HIS RULING · APPROVED, `b57cbf8e`).
House gates: R17 row line 35 (one row); R19 row line 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh …/preflight.sh check "<card 710>"` · exit 0 · output:
```
clock · date · 0 · Sat Oct 17 18:22:23 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-builder-row-fr1
head · git log --oneline -1; git log --stat --format=%h 52a0600d..HEAD · 0 · (6 lines)
    5fea0cc4 docs(gemini-builder-row-fr1): build report — 52a0600d
    5fea0cc4
     .../gemini-builder-row-fr1-build-2026-10-17.md     | 156 +++++++++++++++++++++
     .../gemini-builder-row-fr1-build-2026-10-17.result |  15 ++
     2 files changed, 171 insertions(+)
env here · ls …/gemini-builder-row-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "<build report>" · 0 · BUILT · job: gemini-builder-row-fr1 · tip: 52a0600d | on 13bcd579 | migration: none | offline 8491/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 (PORT: 6 proofs of 6; FR-2) | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 161412
range · git log --oneline 13bcd579..52a0600d · 0 · (2 lines)
    52a0600d fix(gemini-builder-row-fr1): band-routing control pins the four builder rows (PORT, FR-2; L3, L72, R1738)
    395a9e77 wip(gemini-builder-row-fr1): red — PORT of 7f415a4f..695f8bde applied by Edit; FR-2 control red
PREFLIGHT OK
```
THE RANGE typed `git log --stat --format=%h 13bcd579..52a0600d`: `52a0600d` → `tests/ops/test_band_routing_1015.py | 4 ++--`; `395a9e77` → `SHADOW-HUB.md | 12`, `ops/desk/bare-guard.py | 15`, `ops/desk/desk-launch.sh | 4`, `tests/ops/test_bare_guard.py | 97`, `tests/ops/test_desk_launch_shadow.py | 30`, `tests/ops/test_shadow_hub_file.py | 47` (6 files, 187+/18-). Path union: the seven paths below.
DB: none — `git diff --name-only --no-renames 13bcd579 52a0600d` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py` — every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` → No such file or directory (fresh).
House probes: `sh …/house-probe.sh --card "<card 710>"` (background) · exit 0 · output whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
(Gemini's line is HARNESS: the probe still names the retired id; `house-probe.sh` is card 670's file — recorded, not a finding. No OpenAI header line: Sol not probed.)
**house A: grok · house B: none (not needed)** — card `HOUSE B: as needed`; the MANDATORY rule does not apply. (X5: Gemini would be the only candidate and is out; N/A.)
PROVEN BY FIRST REAL USE: `uv run pytest *` at row F2's green run; `git add` / `git commit` only if a finding holds; no with-DB string (DB: none).

## Files copied
`sh …/stage-set.sh "<card 710>" "<S>"` → output whole:
```
42 <S>/STAGED-CARD
18816 <S>/diff.md
20068 <S>/files/710-gemini-builder-row-port-check-card.md
22664 <S>/files/gemini-builder-row-fr1-build-2026-10-17.md
19740 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
56882 <S>/files/wt/ops/desk/bare-guard.py
136832 <S>/files/wt/ops/desk/desk-launch.sh
42290 <S>/files/wt/tests/ops/test_band_routing_1015.py
103195 <S>/files/wt/tests/ops/test_bare_guard.py
14782 <S>/files/wt/tests/ops/test_desk_launch_shadow.py
14088 <S>/files/wt/tests/ops/test_shadow_hub_file.py
701 <S>/rulings.md
STAGED 12 files · 450100 bytes · commits 2
```
(commits 2 = PREFLIGHT's range count.) `stage-copy.sh`, each its own call:
- `COPIED 36226 <S>/files/671-gemini-builder-row-card.md`
- `COPIED 29891 <S>/files/gemini-builder-row-check-2026-10-17.md`
- `COPIED 31831 <S>/files/cto-2026-10-17.md`
- `COPIED 16484 <S>/files/deploy-gemini-builder-row.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (21271 bytes): HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
Launch 18:24:03 EDT (`date`); house gates re-run: R17 line 35, R19 line 37, `5055151d…`; `cd <AGY>`; grok started (background, timeout 2700000); `cd <WT>`; `git status --short --branch` → `## ops/gemini-builder-row-fr1`.

## OWN FINDINGS
Written before any house list was opened. Read: the card, the diff `13bcd579..52a0600d` (`<S>/diff.md`), `bare-guard.py:1140-1299`, `desk-launch.sh:368-412`, `:1652-1671`, `SHADOW-HUB.md:1-110`, `test_band_routing_1015.py:1-125`, `:170-199`, `:460-479`, `:636-660`, the build report `:67-157`, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down. Nothing in the diff reaches a score, rank, grade or size (ops/desk scripts, one hub and tests only; no `src/`). No person or vendor name in a new identifier beyond the model ids the rulings name.

FINDING O1
ROW: P2
CLAIM: The deploy is a plain merge only if main has not moved in the three shared files since BASE; the drafter's read (18:19 EDT, main `7ae1ba99`) predates this check, and `ops/desk/desk-launch.sh:380` / `bare-guard.py:1284` sit beside this card's hunks, so a main commit since then could touch an adjacent line.
RUN: COMMAND `git -C /Users/cobalt/cobalt diff --stat 13bcd579 main -- ops/desk/bare-guard.py ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts/SHADOW-HUB.md"`
EXPECT: a non-empty stat line for one of the three files (the claim true); empty = no overlap.

FINDING O2
ROW: P1
CLAIM: The three main-untouched test files are byte-equal to the checked tip `695f8bde` only if the port missed nothing; `tests/ops/test_bare_guard.py:2454-2553` (the 97-line add) is the largest hand-applied block.
RUN: COMMAND `git -C /Users/cobalt/cobalt diff --stat 695f8bde ops/gemini-builder-row-fr1 -- tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py`
EXPECT: a non-empty stat line (the claim true); empty = byte-equal.

FINDING O3
ROW: F2
CLAIM: `tests/ops/test_band_routing_1015.py:112-117` is the only assertion of that file that counts `## BUILDERS` builder rows; the other `section(…, "BUILDERS")` readers (`:91`, `:469`, `:644`) count band rows only, so a fifth stale count elsewhere would have failed the deploy gate again.
RUN: COMMAND `grep -n -F "startswith(\"| \`\")" tests/ops/test_band_routing_1015.py`
EXPECT: more than one line (the claim of a second builder-row counter true); one line (`:114`) = FR-2 is the one edit needed.

## Findings
House A grok finished 18:34:17 EDT (`date` at the notice); `ls -la <S>` → `house-a.md` 12 bytes. `<S>/house-a.md` whole: `FINDINGS: 0`. Grok's stdout (the task output) ends with the path, as asked; no finding block. House B: none (not needed).
Kept: none.

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `git -C /Users/cobalt/cobalt diff --stat 13bcd579 main -- ops/desk/bare-guard.py ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` | (nothing printed) — main now `600c2b72` (`git -C /Users/cobalt/cobalt log --oneline -1 main` → `600c2b72 docs(desk): R1820 port-job check 9ead9383 launched`) | NOT HELD — no overlap |
| O2 | opus | `git -C /Users/cobalt/cobalt diff --stat 695f8bde ops/gemini-builder-row-fr1 -- tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` | (nothing printed) | NOT HELD — byte-equal |
| O3 | opus | Grep tool, the fixed string `startswith("| \`")` on `tests/ops/test_band_routing_1015.py` (the backtick pattern is barred from a Bash grep by UNATTENDED RULES; the first Grep spelling, unescaped, matched nothing and was re-spelled) | `114:    rows = [ln for ln in sect if ln.startswith("| \`")]` — one line | NOT HELD — FR-2 is the one builder-row counter |

### The card's rows (RUN rows, asserting nothing)
**S0.** `git diff --name-only --no-renames 13bcd579 52a0600d` → the seven paths of the card, exactly (PREFLIGHT). `git diff --stat 13bcd579 52a0600d` →
```
 docs/40 - DevDocs/prompts/SHADOW-HUB.md | 12 ++--
 ops/desk/bare-guard.py                  | 15 +++--
 ops/desk/desk-launch.sh                 |  4 +-
 tests/ops/test_band_routing_1015.py     |  4 +-
 tests/ops/test_bare_guard.py            | 97 +++++++++++++++++++++++++++++++++
 tests/ops/test_desk_launch_shadow.py    | 30 +++++++++-
 tests/ops/test_shadow_hub_file.py       | 47 ++++++++++++++--
 7 files changed, 189 insertions(+), 20 deletions(-)
```
`git diff --stat 52a0600d 5fea0cc4 -- . ":(exclude)docs"` → nothing. `git diff --stat 52a0600d 5fea0cc4` → `.../gemini-builder-row-fr1-build-2026-10-17.md | 156 +++`, `.../gemini-builder-row-fr1-build-2026-10-17.result | 15 ++`, `2 files changed, 171 insertions(+)`. No `src/`, `configs/`, `.claude/` path; none of card 670's four files. `git -C /Users/cobalt/cobalt-wt/gemini-builder-row-fr1 status --short --branch` → **REFUSED** (X6, quoted): `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` — the allow line carries `git status*`, not `git -C * status`; the same fact by the listed spelling, cwd `<WT>`: `git status --short --branch` → `## ops/gemini-builder-row-fr1`; `ls …/gemini-builder-row-fr1/.env` → `No such file or directory`.
**P1.** `git -C /Users/cobalt/cobalt diff --stat 7f415a4f main -- <the three test files>` → nothing. `git -C /Users/cobalt/cobalt diff 695f8bde ops/gemini-builder-row-fr1 -- <the three test files>` → nothing (byte-equal). Hub: `git diff -U0 13bcd579 52a0600d` six hunks `@@ -12 +12 @@`, `@@ -15 +15 @@`, `@@ -21,0 +22 @@`, `@@ -26,0 +28,3 @@`, `@@ -38 +42 @@`, `@@ -97 +101 @@`; `git diff -U0 7f415a4f 695f8bde` six hunks `@@ -12 +12 @@`, `@@ -15 +15 @@`, `@@ -21,0 +22 @@`, `@@ -26,0 +28,3 @@`, `@@ -29 +33 @@`, `@@ -88 +92 @@` — every `+`/`-` line identical (read side by side: the launcher sentence, `Three rows`→`Four rows`, the Gemini row, the Gemini note + blank + `X1 for Gemini`, the `<pass prompt>` template, the RESULTS TABLE Gemini row); only (v) and (vi) moved, by 583's 9-line insert. Launcher: port `@@ -376,0 +377 @@` + `@@ -403 +404,2 @@`; checked tip `@@ -376,0 +377 @@` + `@@ -398 +399,2 @@`; lines identical (`# card 671 L1: …`; `-        gemini-*) refuse "…(N/A — id not found)" ;;` → `+        gemini-4-argon-high) ;;`, `+        gemini-*) refuse "shadow: model '$model' is a Gemini id not admitted; gemini-4-argon-high is the one Gemini builder (R1738)" ;;`). Guard: both diffs print the same four hunks with the same headers `@@ -1184,2 +1184,2 @@`, `@@ -1201,2 +1200,0 @@`, `@@ -1203,0 +1202,6 @@`, `@@ -1208,0 +1213,3 @@` and identical lines. `git -C /Users/cobalt/cobalt rev-parse --short=8 695f8bde` → **REFUSED** (X6): `Permission to use Bash has been denied because Claude Code is running in don't ask mode.`; `git -C /Users/cobalt/cobalt merge-base --is-ancestor 695f8bde ops/gemini-builder-row-1017` → **REFUSED** (X6), same text (the card's own RECORDS name `git rev-parse` / `git merge-base` as row commands; neither is on the allow line). The same facts by `git -C /Users/cobalt/cobalt log`: `log --oneline -1 695f8bde` → `695f8bde fix(gemini-builder-row): guard reads --add-dir=D for agy as --add-dir D (FR-1, check O1; L1, L3)`; `log --oneline 695f8bde^..ops/gemini-builder-row-1017` → `06d31180 …SETTLED: O2 — R1804`, `8ba22eaf …fix round FR-1 report — 695f8bde`, `695f8bde …` (695f8bde is on that branch). The build's `## E3` holds six PROOF lines (1–6) and the stop line `rows: 2 of 2 (PORT: 6 proofs of 6; FR-2)`. `git diff --name-only 13bcd579 52a0600d -- "docs/40 - DevDocs/reports"` → nothing: no old report ported.
**P2.** `grep -c -F "BAND ROUTING (his 2026-10-15 R1532"` → `1`. `grep -n -F "| LOW |"` → `36:| LOW | \`grok-4.7\` | \`gpt-5.6-terra\` |`, `94:| model | LOW | MID | HIGH | reading |`; `| MID |` → `37:…`, `94:…`; `| HIGH |` → `38:| HIGH | Opus 5.5 …`, `94:…`. `grep -n -F "## BUILDERS"` → `14:## BUILDERS` (plus prose at `:5`, `:86`). The section `:14-42` holds four `| \`` rows at `:19-22` (`grok-4.7`, `claude-sonnet-5-5`, `gpt-5.6-terra`, `gemini-4-argon-high`). Row readers at the tip: launcher `desk-launch.sh:1727` `awk '/^## /{insec = ($0 ~ /^## BUILDERS/)} insec && /^\| \`/'` (a builder row needs `| \``; `| LOW |` has none); `band_row` `:1657-1658` matches cell 2 with backticks and spaces cut equal to the band word — a builder row's cell 2 is a model id, never `LOW`/`MID`/`HIGH`; guard `bare-guard.py:1149` `line.startswith("| \`")`. Order: Gemini row `:22`, Gemini note `:28`, `X1 for Gemini` `:30`, `BAND ROUTING (` `:32` — all three before. `grep -n -F "routed" ops/desk/desk-launch.sh` → `380`, `393-395`, `1643`, `1644`, `1665`, `1671`, `1676`, `1687`, `1719`, `1720`, `1725`, `1742`, `1793`, `1795`, `1797`, `1819`, `2358` (as the build listed). `git -C /Users/cobalt/cobalt diff --stat 13bcd579 main -- ops tests "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → nothing. `git diff -U0 main ops/gemini-builder-row-fr1 -- ops/desk/desk-launch.sh` → the two hunks only (`@@ -376,0 +377 @@`, `@@ -403 +404,2 @@`). `grep -n -F "card 583" ops/desk/bare-guard.py` → `1284:        # card 583 B6: …` ; the guard diff's hunks sit at `1184-1215` (`builder_call`), none inside `g5` (`:1264-1299`). The three-file `diff --stat 13bcd579 main` → nothing: no overlap.
**F2.** `git diff 13bcd579 52a0600d -- tests/ops/test_band_routing_1015.py` → ONE hunk `@@ -109,11 +109,11 @@`, two changed lines (the def rename; the ids list gaining `"gemini-4-argon-high"`), quoted in `<S>/diff.md:14-25`. `:117` `assert "claude-opus-5-5" not in "\n".join(sect)` stands. Other `BUILDERS` readers (`:91`, `:469`, `:644`) count band rows only (O3). GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `69 passed, 15 warnings in 23.73s`. RED (old test put back by Edit): `-k b2_control_the_three` → `1 failed, 68 deselected, 15 warnings in 0.92s`, `E         At index 1 diff: 'gemini-4-argon-high' != 'gpt-5.6-terra'` at `tests/ops/test_band_routing_1015.py:116`; undone by Edit, `git diff --stat 52a0600d -- tests/ops/test_band_routing_1015.py` → nothing. MUTATION (Gemini id cut): `--tb=line -k b2_control_the_four` → `1 failed, 68 deselected, 15 warnings in 0.86s`, first line `…/test_band_routing_1015.py:116: AssertionError: assert ['claude-sonn...', 'grok-4.7'] == ['claude-sonn...', 'grok-4.7']`; undone, `git diff --stat 52a0600d -- …` → nothing. CONTROL: `tests/ops/test_shadow_hub_file.py -k four_ids` → `1 passed, 50 deselected`.
**R3.** `uv run cobalt jobs restarts 13bcd579..52a0600d`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	M	test/documentation; no resident	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
= the header `RESTARTS: none`.
**A1.** (suite: below) X1: `grep -n -F "gemini-4-argon-high) ;;" ops/desk/desk-launch.sh` → `404:        gemini-4-argon-high) ;;`; `grep -n -F "gemini-*) refuse"` → `405:` — before it in the one `case` (`:402-406`). X2: `grep -n -F "card 671 G2/FR-1" ops/desk/bare-guard.py` → `1204:` one line; the guard diff holds no `.env` line (P1, the four hunks read whole; `:1216-1217` unchanged). X3: `grep -c -F "x1-canary/.env" <hub>` by Bash → **blocked by the hook** (quoted: `route: .env is never read; \`ls -la <path>/.env\` shows it is there, and the lock scripts copy and remove it`); the Grep tool, `x1-canary/\.env` count on the hub → `0`. `ls -la /Users/cobalt/cobalt-wt/x1-canary` → `A.txt` 25, `B.txt` 25, `C.txt` 25, `CANARY.txt` 23, `probe/`; no `.env`. `ls -la …/x1-canary/probe` → `.env` 23. Neither decoy read. R1 grep, whole: `tests/ops/test_desk_launch_shadow.py:218`, `:219`, `tests/ops/test_shadow_hub_file.py:129`, `:178` — four lines, none in hub, launcher or guard. Build `## DECISIONS`: `none` (report `:144-145`).

## FIXES
none — no finding held; no commit of the check.

## Suites
No commit of the check: the tip is the build's `52a0600d` (head `5fea0cc4`, docs only). DB: none card: RESTARTS (R3 above, `RESTARTS: none`), then W (a0), (a), (e).
- (a0) `git diff --name-only --no-renames 13bcd579 52a0600d` → the seven paths, every one under `ops/`, `tests/ops/` or `docs/` (PREFLIGHT). **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) G3: `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-fr1 offline --deploy-gate` (background) · exit 0 · whole:
```
tests/ops: run (deploy gate)
offline 8491/0
log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-fr1-offline-20261017-183626.log
```
  In the log: `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 661.05s (0:11:01)` (tests/cobalt + tests/taxonomy) and `960:3919 passed, 1 xfailed, 16 warnings in 856.99s (0:14:16)` (tests/ops); `grep -n -F " failed"` → nothing; `grep -c -F "OUTSIDE the allowed set"` → `0`. The (a0) `uv run pytest … tests/ops` line was not run apart: the `--deploy-gate` call ran `tests/ops` whole (`:960`).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-builder-row-fr1 livenote` · exit 0 · whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-builder-row-fr1-livenote-20261017-190202.log`. Its one SKIPPED line: `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. The one `COBALT_LIVE_VAULT_ROOT` hit is the command line (`:2`), not a skip.
- A1: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py` → `1948 passed, 15 warnings in 64.97s (0:01:04)`.
- with-DB: not run (DB: none). `.env`: never present; `ls /Users/cobalt/cobalt-wt/gemini-builder-row-fr1/.env` → `No such file or directory` (19:02 EDT).

## Scope
PREFLIGHT's path union: the seven paths of row S0, every one in a row's files (P1's six, F2's test file). The check's commits: none. The F2 red and mutation were made by Edit and undone, each undo proved (`git diff --stat 52a0600d -- tests/ops/test_band_routing_1015.py` → nothing, twice).

## Checked against the branch
(i) `git log --oneline 52a0600d..HEAD -- . ":(exclude)docs"` → nothing; `<tip now>` = `52a0600d`.
(ii) `git log --stat --format=%h 52a0600d..HEAD` → `5fea0cc4`: the build report `.md` (156+) and `.result` (15+), docs only.
(iii) `git log --oneline 13bcd579..HEAD -- ops/desk/house-probe.sh "…/CHECK-HUB.md" "…/STANDING-LIST.md" tests/ops/test_house_probe.py .claude/settings.json .claude/settings.json.bak` → nothing; `… -- "docs/40 - DevDocs/prompts/2026-10-16" "docs/40 - DevDocs/prompts/2026-10-17"` → nothing.
(iv) No held finding.
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/gemini-builder-row-fr1` alone.
(vi) `git log --stat --format=%h 13bcd579..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no migration, no with-DB test; gate lists not touched (not needed).
(vii) Card RECORDS: `git -C /Users/cobalt/cobalt log --oneline ops/gemini-builder-row-fr1 -5` → `5fea0cc4`, `52a0600d`, `395a9e77`, `13bcd579`, `9569ac1b` (as recorded). `git diff --stat 7f415a4f main -- <three tests>` → nothing (as recorded). `git diff --stat 13bcd579 main -- ops tests <hub>` → nothing, now at main `600c2b72` (recorded at `7ae1ba99`). The decoys `ls -la` → as recorded (A1). The `rev-parse` / `merge-base` records: refused here, proved by `git log` (P1).
(viii) L32: this report holds no ticker, price or date of his; the values are commit ids, model ids, paths and test counts.

## OPEN
none.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none.

## RECORDS
- Findings: O1, O2, O3 (opus), each NOT HELD by its run; house A grok `FINDINGS: 0`; house B none (not needed).
- X6, the refusals, quoted under `## RUNS`, each fact proved by a listed spelling: `git -C <WT> status --short --branch` (S0), `git -C /Users/cobalt/cobalt rev-parse --short=8 695f8bde` and `git -C /Users/cobalt/cobalt merge-base --is-ancestor 695f8bde ops/gemini-builder-row-1017` (P1), each `Permission to use Bash has been denied because Claude Code is running in don't ask mode.`; and the hook's block of `grep -c -F "x1-canary/.env" <hub>` (A1 X3): `route: .env is never read; …`. For the drafter: card 710 names three row commands that the CHECK-HUB allow line does not carry, and one grep that the guard blocks.
- House-probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" …)` — the probe still names the retired id; `house-probe.sh` is card 670's (recorded, not a finding; X5: house B N/A).
- Gemini produced nothing because it never sat (not needed); no house was relaunched.
- Lock: never taken (DB: none). No extra take.
- The F2 red and mutation ran while the A1 suite (other files) ran in the background; `test_band_routing_1015.py` is not in A1's set.
- files opened: 15 — `CHECK-HUB.md`; card 710; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `<S>/diff.md`; `ops/desk/bare-guard.py`; `ops/desk/desk-launch.sh`; `SHADOW-HUB.md`; `tests/ops/test_band_routing_1015.py`; the build report; `areas/cobalt.md` (the two named parts); `<S>/house-a.md`; four task outputs (house probe, grok, gate offline, gate livenote). The A1 suite's output was read by `tail -n 3` and the gate logs by `grep`; neither is counted.
- Check of `gemini-builder-row-fr1`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gemini-builder-row-fr1 · pass: 1 · tip: 52a0600d · house A: grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8491/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 190470
