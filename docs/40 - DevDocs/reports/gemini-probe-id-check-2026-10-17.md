# gemini-probe-id — check 2026-10-17

## §0 Headline
The check of `gemini-probe-id` found nothing to fix. The id swap to `gemini-4-argon-high` is the one token at `house-probe.sh:24`, `:104`, `CHECK-HUB.md:95`, `STANDING-LIST.md:13` and `test_house_probe.py:253`. The new pin was red under every mutation (a)–(d), each undone and proved.
House A Grok: `FINDINGS: 0`. House B: none (not needed; Gemini is OUT on `main`'s old id). Own findings: 2, both REJECTED by card 670 G1 and left open as follow-ups (STANDING-LIST not pinned; the pin's own old-id literal).
Gate on tip `744128d7`: `tests/ops: run (deploy gate)`, offline 8389/0 (tests/ops 3817 passed), live-note 146/0. RESTARTS: none. DB not taken. ready: YES.
The report sits in `main`'s checkout; the desk commits it with its `.result`.

## L74
A system reminder at the start of this session asked commits to end with a `Claude-Session:` line too. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/677-gemini-probe-id-check-card.md"` (Sat Oct 17 08:57:49 EDT 2026), exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/677-gemini-probe-id-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/677-gemini-probe-id-check-card.md" · 0 · 78bf481cd59486642b90b800258ecc7191bb0880
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/677-gemini-probe-id-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-17 R1736 row · grep -n "^| R1736 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 33:| R1736 | 06:32 ET | HIS RULING (brain, L79), 2026-10-17: Gemini top model = gemini-4-argon-high (medium, low recorded only). K5 card: CHECK-HUB :95 and house-probe.sh use it, was gemini-3.1-pro-high. Behind 641 and 583. | HIS RULING · APPROVED |
RULING 2026-10-17 R1736 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1736 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · d01849e7a6ef4a9de57d6de11856c866919737d2
RULING 2026-10-17 R1736 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
RULING 2026-10-17 R1738 row · grep -n "^| R1738 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · 31:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; answer: reports/gemini-bakeoff-answer-2026-10-17.md. Probe-id and builder cards drafted now; three builds after both deploy; routing B unchanged. | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1738 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-17.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, exit 0, output whole:

```
clock · date · 0 · Sat Oct 17 08:57:53 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-probe-id-1017
head · git log --oneline -1; git log --stat --format=%h 744128d7..HEAD · 0 · (6 lines)
    9f281a6a docs(gemini-probe-id): build report — 744128d7
    9f281a6a
    
     .../reports/gemini-probe-id-build-2026-10-17.md    | 147 +++++++++++++++++++++
     .../gemini-probe-id-build-2026-10-17.result        |  15 +++
     2 files changed, 162 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gemini-probe-id-1017/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gemini-probe-id-1017/docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md" · 0 · BUILT · job: gemini-probe-id · tip: 744128d7 | on f2140694 | migration: none | offline 8389/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 113826
range · git log --oneline f2140694..744128d7 · 0 · (2 lines)
    744128d7 fix(gemini-probe-id): Gemini house id gemini-4-argon-high in the probe, CHECK-HUB and STANDING-LIST (G1, R1736, L1, L72)
    5bce12c9 wip(gemini-probe-id): red — test_k5_gemini_id_is_gemini_4_argon_high (G1)
PREFLIGHT OK
```

| rule | command | exit | output verbatim |
|---|---|---|---|
| THE RANGE | `git log --stat --format=%h f2140694..744128d7` | 0 | `744128d7`: `docs/40 - DevDocs/prompts/CHECK-HUB.md \| 2 +-`, `docs/40 - DevDocs/prompts/STANDING-LIST.md \| 2 +-`, `ops/desk/house-probe.sh \| 4 ++--`, `tests/ops/test_house_probe.py \| 2 +-`, `4 files changed, 5 insertions(+), 5 deletions(-)` · `5bce12c9`: `tests/ops/test_house_probe.py \| 14 ++++++++++++++`, `1 file changed, 14 insertions(+)` |
| DB: none | `git diff --name-only --no-renames f2140694..744128d7` | 0 | `docs/40 - DevDocs/prompts/CHECK-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `ops/desk/house-probe.sh` · `tests/ops/test_house_probe.py` — every path under `ops/`, `tests/ops/` or `docs/` |
| scratch | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-probe-id-check` | 1 | `No such file or directory` (fresh) |
| HOUSE PROBES | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` · `[exited with code 0]` |

Seats: no `HOUSE A: OpenAI` header line → Sol not probed. **house A: Grok · house B: none (not needed)** — the card's line is `HOUSE B: as needed`. Gemini OUT (HARNESS: `main`'s probe still carries the old id, the very change under check; X5 also says Gemini cannot sit on its own probe change). Self-check count `3 of 3`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`, output whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gemini-probe-id-check`):
```
4117 <S>/diff.md
14787 <S>/files/677-gemini-probe-id-check-card.md
19984 <S>/files/gemini-probe-id-build-2026-10-17.md
43599 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
46754 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
5712 <S>/files/wt/ops/desk/house-probe.sh
11738 <S>/files/wt/tests/ops/test_house_probe.py
701 <S>/rulings.md
STAGED 8 files · 147392 bytes · commits 2
```
(paths shortened to `<S>`; commits 2 = PREFLIGHT's range count.) `stage-copy.sh`, each its own call:
- `COPIED 8725 <S>/files/670-gemini-probe-id-card.md`
- `COPIED 48643 <S>/files/check-scratch-fr-check-2026-10-16.md`
- `COPIED 3572 <S>/files/gemini-bakeoff-answer-2026-10-17.md`
- `COPIED 11500 <S>/files/cto-2026-10-17.md`
- `COPIED 133124 <S>/files/wt/ops/desk/desk-launch.sh`
- `COPIED 13261 <S>/files/wt/tests/ops/test_desk_launch_shadow.py`
- `COPIED 15934 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md`
- `COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (16189 bytes, `ls -la <S>`): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
House A Grok started Sat Oct 17 08:59:46 EDT 2026 (`date`; gates re-run: R17 1 row, R19 1 row), background id `bat7lkx5k`. House B: none (not needed). `cd` back; `git status --short --branch` → `## ops/gemini-probe-id-1017`.

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: G1
CLAIM: `docs/40 - DevDocs/prompts/STANDING-LIST.md:13` carries the new id but no test reads that line: putting the old id back there leaves every test green (`tests/ops/test_house_probe.py:283-294` reads only `PROBE` and `CHECK_HUB`).
RUN: COMMAND `grep -n -F "STANDING" tests/ops/test_house_probe.py`
EXPECT: no output (exit 1).

FINDING O2
ROW: D1 (DECISION P1)
CLAIM: the pin's negative assertion at `tests/ops/test_house_probe.py:294` holds the old id as a literal, so the card 670 P1 grep (`grep -rn -F "gemini-3.1-pro-high" ops … tests/ops/test_house_probe.py`) can never print nothing.
RUN: COMMAND `grep -n -F "gemini-3.1-pro-high" tests/ops/test_house_probe.py`
EXPECT: `294:        assert not any("gemini-3.1-pro-high" in ln for ln in path.read_text().splitlines()), path`

FINDINGS: 2 (own)

## Findings
House A Grok finished at Sat Oct 17 09:07:13 EDT 2026 (`date` at the notice), exit 0. `ls -la <S>` → `house-a.md` 12 bytes. Grok wrote the file itself; its stdout was the path. `house-a.md` whole: `FINDINGS: 0`. House B: none (not needed).

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | Opus | G1 | `STANDING-LIST.md:13` holds the new id but no test reads it | COMMAND |
| O2 | Opus | D1 | the pin's `:294` holds the old id as a literal, so card 670's P1 grep can never print nothing | COMMAND |

## Dropped
none (Grok wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "STANDING" tests/ops/test_house_probe.py`; then `STANDING-LIST.md:13` put back to `gemini-3.1-pro-high` by Edit and `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_house_probe.py` | grep: no output, exit 1 · under the mutation: `27 passed, 15 warnings in 26.76s` · undone by Edit (proved below) | REJECTED — card 670 G1 `red first`: the pin "reads `PROBE` and `CHECK_HUB`", and its fence keeps the probe test to those files; the build report's self-check (2) says the same ("`STANDING-LIST.md:13` is a record line no code reads"). Open, follow-up |
| O2 | Opus | `grep -n -F "gemini-3.1-pro-high" tests/ops/test_house_probe.py` | `294:        assert not any("gemini-3.1-pro-high" in ln for ln in path.read_text().splitlines()), path` | REJECTED — card 670 G1 asks for this assertion ("no line of either file holds `gemini-3.1-pro-high`"); it is the builder's DECISION P1, and card 677 fences any test edit. Open, follow-up (D1 below) |

THE CARD'S ROWS (each RUN, asserts nothing):
- **S0** · `git diff --name-only --no-renames f2140694..744128d7` → `docs/40 - DevDocs/prompts/CHECK-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `ops/desk/house-probe.sh` · `tests/ops/test_house_probe.py`. `git diff --stat f2140694 744128d7` → `CHECK-HUB.md | 2 +-`, `STANDING-LIST.md | 2 +-`, `house-probe.sh | 4 ++--`, `test_house_probe.py | 16 +++++++++++++++-`, `4 files changed, 19 insertions(+), 5 deletions(-)`. `git diff --stat 744128d7 9f281a6a -- . ":(exclude)docs"` → nothing. No `src/`, `configs/`, `.claude/` path. `git -C <WT> status --short --branch` was refused (not a listed string; `## RECORDS`); `git status --short --branch` from `<WT>` → `## ops/gemini-probe-id-1017`.
- **G1 / X1** · `git diff f2140694 744128d7` read whole: one `-`/`+` pair at `house-probe.sh:24`, `:104`, `CHECK-HUB.md:95`, `STANDING-LIST.md:13` and `test_house_probe.py:253`. With the token swapped back, each `+` line is its `-` line byte for byte; the only other hunk is the appended pin (`:281-294`). `git show 744128d7:ops/desk/house-probe.sh` → `:24` `#           agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 3m …`, `:104` `(cd "$WT/agy-trial" && exec agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 3m --add-dir "$WT/agy-trial" --print="$PROMPT") \`. `grep -n -F "gemini-4-argon-high"` → `CHECK-HUB.md` `95:- **GEMINI:** \`agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 20m …`; `STANDING-LIST.md` `13:- THE HOUSE SPELLINGS: … Gemini's (\`agy --model gemini-4-argon-high --mode accept-edits …`. `wc -l CHECK-HUB.md` → `127`. `grep -n -E "[0-9a-f]{8}" tests/ops/test_house_probe.py` → no output (no hash anywhere in the file).
- **G1 green** · `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_house_probe.py` → `27 passed, 15 warnings in 27.05s`.
- **G1 (b)** · `:104` back to the old id by Edit → whole file: `2 failed, 25 passed`; `FAILED …::test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout` (`:252`, `At index 1 diff: 'gemini-3.1-pro-high' != 'gemini-4-argon-high'`) and `FAILED …::test_k5_gemini_id_is_gemini_4_argon_high` (`:289`, `AssertionError:             (cd "$WT/agy-trial" && exec agy --model gemini-3.1-pro-high …`).
- **G1 (a)** · `:24` and `CHECK-HUB.md:95` also put back (so the probe and the hub are BASE's text: `git diff f2140694 -- ops/desk/house-probe.sh "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → nothing); the pin alone → `1 failed, 15 warnings in 0.92s`; first line `E   AssertionError: #           agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir $WT/agy-trial --print="Reply with only the word OK."` at `:289`, the first `gemini-4-argon-high` assertion. (Done by undoing the hunks by hand, as the card allows, not by a checkout of `5bce12c9`.) Control in the same state: `-k "grok or sol"` → `9 passed, 18 deselected`.
- **G1 (c)** · the probe restored (`git diff --stat 744128d7 -- ops/desk/house-probe.sh` → nothing), `CHECK-HUB.md:95` alone at the old id → whole file `1 failed, 26 passed`: only `test_k5_gemini_id_is_gemini_4_argon_high`, at `:292` (`assert 'agy --model gemini-4-argon-high ' in "- **GEMINI:** \`agy --model gemini-3.1-pro-high …`). The argv test stays green. Undone: `git diff --stat 744128d7 -- "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → nothing.
- **G1 (d)** · a line `# agy --model gemini-4-argon-high` appended before `exit 0` → the pin `1 failed`: `assert 3 == 2` at `:287`. Undone: `git diff --stat 744128d7 -- ops/desk/house-probe.sh` → nothing.
- **Undo proved** · after O1's mutation was undone: `git diff --stat 744128d7` → only the head's docs commit (`gemini-probe-id-build-2026-10-17.md | 147 +`, `.result | 15 +`); `git status --short --branch` → `## ops/gemini-probe-id-1017`.
- **G2 / X4** · `grep -rn -F "gemini-3.1-pro-high" ops tests` → `tests/ops/test_desk_launch_shadow.py:216` and `:217` (card 671), `tests/ops/test_house_probe.py:294` (the pin), and two `__pycache__` `.pyc` "Binary file … matches" (not a source). `grep -n -F "gemini-3.1-pro-high"` on `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `CARD.md`, `STANDING-LIST.md`, `SHADOW-HUB.md` → `SHADOW-HUB.md:88` only (card 671). No hit in `ops/`. `ops/desk/desk-launch.sh:398` read: `gemini-*) refuse "shadow: model '$model' is a Gemini id; …"`, the glob, no old id. Every other hit under `docs/` sits in a dated prompt (`prompts/2026-*`), a dated plan (`plans/fixed-files-2026-09-30/`), a report or the design record: history. No hit is neither card 671, history nor the pin.
- **P1 / X3** · the desk's records, whole: `THE CLI LIST (the desk, before the build launched): \`agy models\` → \`gemini-4-argon-high	Gemini 4 Argon (High)\` (listed with \`gemini-4-argon-medium\` and \`gemini-4-argon-low\`), Sat Oct 17 08:03:45 EDT 2026.` · `THE WORKTREE PROBE (the desk, not on the build line): \`sh /Users/cobalt/cobalt-wt/gemini-probe-id-1017/ops/desk/house-probe.sh gemini\` → \`gemini: UP\`, Sat Oct 17 08:52 EDT 2026.` Both are present and read as the card quotes them; the first names `gemini-4-argon-high`, the second answers `gemini: UP`. Not re-run (`agy` is not on the check line). `git diff --stat 744128d7 -- ops/desk/house-probe.sh` → nothing: the worktree's script is the tip's.
- **D1** · (1) `agy models`: the desk's 08:03:45 record answers it. (2) the worktree probe: the desk's 08:52 record answers it. (3) DECISION P1: yes, `:294` is the form card 670 G1 asks for. A smaller form that keeps the assertion and leaves the P1 grep empty exists: build the string, e.g. `old = "gemini-3.1" + "-pro-high"`. RECOMMENDATION: keep `:294` as it is. Card 670's P1 expectation ("→ nothing") was what was wrong, because the pin it asked for has to name the id it forbids; splitting the literal only hides the id from a grep. If the desk wants the grep empty, that is a one-line follow-up, not this card's.
- **R3** · `uv run cobalt jobs restarts f2140694..744128d7`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
ops/desk/house-probe.sh	M	operator script; no Cobalt reader	-
tests/ops/test_house_probe.py	M	test/documentation; no resident	-
RESTARTS: none
```
Equals the header `RESTARTS: none`; the rules are the three the card names.

## FIXES
none. No finding held. No commit of mine.

## Suites
"DB: none" card. Tip `744128d7`, no commit of mine. RESTARTS first (R3 above: `RESTARTS: none`). (a0) `git diff --name-only --no-renames f2140694` → `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.md`, `docs/40 - DevDocs/reports/gemini-probe-id-build-2026-10-17.result`, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py`: every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- **G3**, (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-probe-id-1017 offline --deploy-gate` (background, exit 0), output whole: `tests/ops: run (deploy gate)` · `offline 8389/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-probe-id-1017-offline-20261017-091023.log`. In the log (`grep -n -F "passed"`): `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 741.84s (0:12:21)`; `959:3817 passed, 1 xfailed, 16 warnings in 873.57s (0:14:33)` (the `tests/ops` run).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-probe-id-1017 livenote` (exit 0), output whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-probe-id-1017-livenote-20261017-093735.log`.
- with-DB: not run (DB: none).
- `ls /Users/cobalt/cobalt-wt/gemini-probe-id-1017/.env` → `No such file or directory`. `.env` was never present; no lock was taken.

## Scope
PREFLIGHT's path union `f2140694..744128d7`: `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py`. All four are card 670 G1's `files`. Above the tip: `9f281a6a`, which holds only the build report and its `.result` under `docs/`. Commits of mine: none.

## Checked against the branch
- (i) `git log --oneline 744128d7..HEAD -- . ":(exclude)docs"` → nothing; `<tip now>` = `744128d7`.
- (ii) `git log --stat --format=%h 744128d7..HEAD` → `9f281a6a`: `.../reports/gemini-probe-id-build-2026-10-17.md | 147 +`, `.../gemini-probe-id-build-2026-10-17.result | 15 +`: docs only.
- (iii) `git log --oneline f2140694..HEAD -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md" ops/desk/desk-launch.sh tests/ops/test_desk_launch_shadow.py LAWS.md .claude` → nothing.
- (iv) no held finding.
- (v) `ls /Users/cobalt/cobalt-wt/gemini-probe-id-1017/.env` → `No such file or directory`; `git status --short --branch` → `## ops/gemini-probe-id-1017` alone.
- (vi) `git log --stat --format=%h f2140694..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate lists owed.
- (vii) the card's records: `git log --oneline -5 ops/gemini-probe-id-1017` → `9f281a6a`, `744128d7`, `5bce12c9`, `f2140694`, `5b933294`, as recorded. The tip-lines and occurrence records were re-run above (G1, G2) and match. The record's `git -C /Users/cobalt/cobalt rev-parse` is not a listed string. `git -C /Users/cobalt/cobalt log --oneline -1` → `390d923f docs(desk): OWED 583 build line keeps live ea4e2cfc`: `main` has moved past the drafter's `03da61af`, as expected.
- (viii) L32: this report holds no ticker, price or date of his. The dates and times are the session's own clock and the records' times.

## OPEN
- O1 · REJECTED (card 670 G1). FOLLOW-UP: no test pins `STANDING-LIST.md:13`. A test that reads that line for `agy --model gemini-4-argon-high` and no old id would settle it.
- O2 · REJECTED (card 670 G1, DECISION P1). FOLLOW-UP only if the desk wants the P1 grep empty: split the literal at `tests/ops/test_house_probe.py:294`. Recommended: no change (D1).

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none.

## RECORDS
- The `main` probe's Gemini line answers OUT with the old id (PREFLIGHT): expected before deploy (card `## DEPLOY PROOF`). Gemini did not sit (X5: not needed, and it cannot sit on its own probe change).
- Dropped findings: none. Houses that produced nothing: none (Grok produced `FINDINGS: 0`).
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/gemini-probe-id-1017 status --short --branch` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." I ran the same read as the listed `git status --short --branch` from `<WT>`.
- Mutations of G1 (a)–(d) and O1 were made with Edit and undone with Edit; each undo was proved by `git diff --stat 744128d7 -- <file>` printing nothing; at the end the tree equals HEAD (`git status` clean).
- No lock taken; `.env` never present. No CONTINUE message arrived.
- The `.result` file is written beside this report. This session has no listed string to commit in `/Users/cobalt/cobalt`, so the desk commits both (CHECK-HUB `## LAUNCH`).
- files opened: 14. Files: `CHECK-HUB.md`; card 677; the build report; `tests/ops/test_house_probe.py`; `ops/desk/house-probe.sh`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`); card 670; `ops/desk/desk-launch.sh` (`:390-404`); `<S>/house-a.md`; four tool-output files (the probe, Grok's stdout, the offline gate, one saved grep result). The READ reports `check-scratch-fr-check-2026-10-16.md`, `gemini-bakeoff-answer-2026-10-17.md` and `cto-2026-10-17.md` were not opened. Their rows came through `authorize.sh`, and the build report's quotes were not needed for any judgement.
- Check of `gemini-probe-id`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gemini-probe-id · pass: 1 · tip: 744128d7 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8389/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179030
