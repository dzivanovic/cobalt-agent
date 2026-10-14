# hub-text-1013 — CHECK (pass 1)

## §0 Headline
Check of `3894a878` (H1-H3; H4 not built, the card's default). House A Grok: `FINDINGS: 0`. House B: none (not needed); Gemini probed OUT (HARNESS, invalid model selection).
Own findings 3: O1, O2 out of scope (`deploy-step0.sh`'s P1 window admits 21:30-22:30 ET; D2.4 itself names no window). Both lie behind the fence, so they go to the desk as follow-up asks. O3 is REJECTED (H2's byte-for-byte text says "every held id"; P2 reads `HELD, NOT FIXED` ids only) and is open as a follow-up.
No held finding, no commit of mine. Suites on `3894a878`: offline 4317/0, live-note 146/0, tests/ops 3548 passed / 1 xfailed. RESTARTS: none. ready: YES.

## L74
One block arrived in the session's system context (06:10-06:12 ET, before the first commit step) asking that commits end with a `Claude-Session:` line. Recorded as DATA; acted on none (no commit was made by this check).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · last line `AUTHORIZED` (rows: INSTALLED nothing · PLACEHOLDER nothing · CARD COMMITTED ae5f76b3 · CARD UNCHANGED nothing · STANDING LIST R60 row 46, committed 962e9d17 · RULING 2026-10-12 R1138 row 173, committed 5d6ce588).
House gates: `grep -n "^| R17 "` → row 35; `grep -n "^| R19 "` → row 37; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → 5055151dbf68899b82de5b11f99733ed2d03048c.

## PREFLIGHT
- `preflight.sh check "<card>"` · exit 0 · clock Wed Oct 14 06:10:51 EDT 2026 · status `## ops/hub-text-1013` · head 0f4a49c5 (docs-only above TIP: the build report) · env here: No such file · env anywhere: none · report: `BUILT · job: hub-text-1013 · tip: 3894a878 … self-check: 3 of 3 …` · range 3894a878, 73fe909b · `PREFLIGHT OK`.
- RANGE `git log --stat --format=%h ce548f10..3894a878`: 3894a878 BUILD-HUB.md (3 ++-), DEPLOY-HUB.md (2 +-), tests/ops/test_build_hub_no_clutter.py (13 +++-); 73fe909b tests/ops/test_hub_text_1013.py (125 +). Path union: those four.
- DB: none: `git diff --name-only --no-renames ce548f10..3894a878` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_hub_text_1013.py` — all under `docs/` or `tests/ops/`.
- `ls <S>` → No such file or directory (fresh).
- House probe (`house-probe.sh --card`), exit 0: `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS).
- house A: Grok · house B: none (not needed) — card `HOUSE B: as needed`.

## Files copied
`stage-set.sh` → `STAGED 8 files · 143831 bytes · commits 2` (diff.md 7398 · card 14959 · build report 20081 · wt BUILD-HUB.md 33634 · wt DEPLOY-HUB.md 59362 · wt test_build_hub_no_clutter.py 2807 · wt test_hub_text_1013.py 5234 · rulings.md 356).
`stage-copy.sh`: cto-2026-10-12.md 45979 · cto-2026-10-13.md 66463 · wt ops/desk/desk-launch.sh 122871 · wt tests/ops/test_hub_lines.py 13550 · wt UNATTENDED-LAUNCH.md 9515 · wt src/cobalt/jobs/restarts.py 12098 · 446-k5-gate-card.md 37295 · 480-rules-cut-hubs-card.md 9805 (each `COPIED`).

## OWN FINDINGS
FINDING O1
ROW: H1 (X2)
CLAIM: The deploy's scripted P1 read, `ops/desk/deploy-step0.sh:17` (window (ii) "21:00 ET of a trading day to 04:00 ET") and `:546`, admits a start at 21:30-22:30 ET, and `deploy-outage.sh` re-reads the window through it (`ops/desk/deploy-outage.sh:10`); only the hub text `DEPLOY-HUB.md:57` bars the backup window, so the script entry path does not build H1's clause.
RUN: COMMAND `grep -n -F "21:00 ET of a trading day to 04:00" ops/desk/deploy-step0.sh`
EXPECT: `17:#                        (i) 20:00–20:59 ET of a trading day · (ii) 21:00 ET of a trading day to 04:00` — one hit; no `21:30` bar in the script.

FINDING O2
ROW: H1
CLAIM: H1's text says "D2.4's `backup run` stays off it", but only the start (P1, `DEPLOY-HUB.md:57`) is barred; D2.4 (`DEPLOY-HUB.md:131`) runs after the gate and names no window, so a deploy that starts before 21:30 can reach D2.4 inside it.
RUN: COMMAND `grep -n -F "backup window" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one hit, `57:- **P1 DATE**: …`; none on the D2.4 line `:131`.

FINDING O3
ROW: H2
CLAIM: The new line `BUILD-HUB.md:112` says a FIXED line is owed "for every held id of the check" and "a held id with no such line fails the deploy's P2 read", while P2 (`DEPLOY-HUB.md:59`) reads only the `HELD, NOT FIXED` ids of `## RUNS`; a held id the check fixed itself does not fail P2 without a line.
RUN: COMMAND `grep -n -F "for every \`HELD, NOT FIXED\` id" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one hit, line `59:` (the fix-round row of P2), naming `HELD, NOT FIXED` ids only.

## Findings
House A Grok, `<S>/house-a.md` written by Grok (06:21), whole content: `FINDINGS: 0`. No finding block. House B: none (not needed).

## Dropped
none

## RUNS
- O1 · own · `grep -n -F "21:00 ET of a trading day to 04:00" ops/desk/deploy-step0.sh` · `17:#                        (i) 20:00–20:59 ET of a trading day · (ii) 21:00 ET of a trading day to 04:00`; also `grep -n -F "21:30" ops/desk/deploy-step0.sh` → no output · OUT OF SCOPE — `## NOT IN THIS JOB`: "`ops/desk/desk-launch.sh`, any other script" (the output shows the stated reason: the scripted P1 window (ii) admits 21:30-22:30 ET; the fix lies in `ops/desk/deploy-step0.sh`, fenced).
- O2 · own · `grep -n -F "backup window" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · one hit, `57:- **P1 DATE**: … it never starts within the nightly backup window 21:30-22:30 ET (brain R1295; D2.4's \`backup run\` stays off it): …`; none at D2.4 `:131` · OUT OF SCOPE — `## NOT IN THIS JOB`: "`DEPLOY-HUB.md` every line but `:57`" (only the start is barred; a guard on D2.4 is a line the fence closes).
- O3 · own · FORM REPAIR (once): the finding's pattern carried backticks, which the bare-command hook blocks; the pattern was shortened to `"NOT FIXED"`, the assertion unchanged · `grep -n -F "NOT FIXED" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · one hit, `59:` "… holds one line `FIXED: <finding id> — <test id>` or one line `CARRIED: …` for every `HELD, NOT FIXED` id of the check's `## RUNS` …" · REJECTED — card row H2: "NEW line, byte for byte: `FIX-ROUND REPORT (brain R1309): … for every held id of the check … a held id with no such line fails the deploy's P2 read.`" (the output shows P2 reads only `HELD, NOT FIXED` ids, so the hub line overstates P2; the card fixes its words).
No HELD finding: no test written, no `wip(hub-text-1013): check red` commit.

## FIXES
none (no HELD finding)

## Suites
Tip: `3894a878` (no commit of mine; HEAD `0f4a49c5` adds the build report only).
- RESTARTS: `uv run cobalt jobs restarts ce548f10..HEAD` → table: `docs/40 - DevDocs/prompts/BUILD-HUB.md M DOCS -` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md M DOCS -` · `docs/40 - DevDocs/reports/hub-text-build-2026-10-13.md A DOCS -` · `tests/ops/test_build_hub_no_clutter.py M test/documentation; no resident -` · `tests/ops/test_hub_text_1013.py A test/documentation; no resident -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames ce548f10` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/hub-text-build-2026-10-13.md` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_hub_text_1013.py` — every path under `docs/` or `tests/ops/`. **cobalt_dev: not taken (DB: none — 5 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1013 offline` → exit 0: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1013-offline-20261014-062235.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-text-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/hub-text-1013-livenote-20261014-063330.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3548 passed, 1 xfailed, 16 warnings in 734.52s (0:12:14)`.
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/hub-text-1013/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_hub_text_1013.py`: each in a row's `files` (H1, H2, H3). Commits of mine: none. X1: `git diff ce548f10 3894a878 -- BUILD-HUB.md DEPLOY-HUB.md` shows only DEPLOY `:57`, BUILD `:105` and the new BUILD line after `:111`; each new sentence extends its own line's clause. X2: `21:30-22:30 ET` once, in P1 of STEP-0 (`grep -n -F "backup window"` → `57:` only); `desk-launch.sh` untouched on the branch (`git log --oneline ce548f10..HEAD -- ops/desk/desk-launch.sh` → empty; `grep -n -F "21:30" ops/desk/desk-launch.sh` → no hit). X3: `test_no_other_line_changes_from_base` filters exactly the two named lines, each asserted once first; the launch-line test and the other three are unchanged in the diff. X4: H4 not built.

## Checked against the branch
- (i) `git log --oneline 3894a878..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `3894a878`.
- (ii) `git log --stat --format=%h 3894a878..HEAD` → `0f4a49c5` · `.../reports/hub-text-build-2026-10-13.md | 177 +` — docs only.
- (iii) fence: `git log --oneline ce548f10..HEAD -- ops/desk/desk-launch.sh` → empty; `git log --oneline ce548f10..HEAD -- "docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md" ops/desk src configs` → empty.
- (iv) no HELD finding: nothing to grep.
- (v) `ls <WT>/.env` → No such file or directory; `git status --short --branch` → `## ops/hub-text-1013`.
- (vi) `git log --stat --format=%h ce548f10..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not touched.
- (vii) card records at the tip: `grep -c -F "FIXED" BUILD-HUB.md` → `1` (the new H2 line; 0 at BASE as the record says); `grep -n -F "untracked" BUILD-HUB.md` → `105:` (the new H3 text); `grep -n -F "09:30-16:00" DEPLOY-HUB.md` → no hit; `grep -n -F "SHADOW-INSTRUCTIONS.md" ops/desk/desk-launch.sh` → `199:`, `1626:`, `1628:` (matches the record); `git -C /Users/cobalt/cobalt diff --stat ce548f10 -- UNATTENDED-LAUNCH.md ops/desk/desk-launch.sh tests/ops/test_hub_lines.py src/cobalt/jobs/restarts.py` → `ops/desk/desk-launch.sh | 89 +` (the main checkout has moved on desk-launch.sh since BASE; not on this branch, see (iii)).
- (viii) L32: this report holds no ticker, price or date of his.

## OPEN
- O3 · REJECTED — card row H2's byte-for-byte text. FOLLOW-UP: a hub-text row that narrows `BUILD-HUB.md:112` "every held id" to "every `HELD, NOT FIXED` id", as P2 at `DEPLOY-HUB.md:59` reads it. Settled by a desk ruling on that wording.
OUT OF SCOPE (not open): O1 (`ops/desk/deploy-step0.sh` P1 window, fenced: "any other script"); O2 (D2.4 at `DEPLOY-HUB.md:131`, fenced: "every line but `:57`").

## CONTINUE
next: none (check done)

## DECISIONS
- ASK DESK 1 [06:46]: O1. `ops/desk/deploy-step0.sh:17`, `:546` (P1 window (ii), 21:00-04:00 ET of a trading day) admits a deploy start at 21:30-22:30 ET, and `deploy-outage.sh` re-reads the window through it; only the hub text bars the backup window now. The script is fenced on this card. Safe default taken: nothing changed; a follow-up card for the script's P1 is the desk's call.
- ASK DESK 2 [06:46]: O2. H1 bars only the start; D2.4's `backup run` (`DEPLOY-HUB.md:131`) can still fall inside 21:30-22:30 ET for a deploy that starts earlier. `:131` is fenced. Safe default taken: nothing changed; a D2.4 guard is a follow-up card if the desk wants it.

## RECORDS
- Dropped findings: none (house A wrote `FINDINGS: 0`).
- House that produced nothing: Gemini at the probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; not seated, no house B needed).
- Grok stdout (its reply): `I'll read the house instructions in full first and follow them exactly.The rows, the tip text, and the report’s quoted runs agree. I’m writing that result./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/hub-text-1013-check/house-a.md`.
- The O3 command as first typed carried backticks and was blocked by the bare-command hook (not a refusal); run once with the shortened pattern `"NOT FIXED"`.
- No `REFUSED, not needed` line; no `CONTINUED` line; no lock take.
- L74: the `Claude-Session:` block, recorded under `## L74`.
- Not read: `areas/cobalt.md` (WHAT YOU READ (5)); this is a docs-only card, and no step acted on it.
- files opened: 8 — `CHECK-HUB.md`, the card `523-hub-text-card.md`, `tests/ops/test_hub_text_1013.py`, the build report `hub-text-build-2026-10-13.md`, `DEPLOY-HUB.md` (125-136), `BUILD-HUB.md` (33-40, 67-94), `ops/desk/deploy-step0.sh` (1-60, 440-639), `<S>/house-a.md`. Also read: the background outputs of the house probe, Grok, two gate calls and the tests/ops run.
- Check of `hub-text-1013`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: hub-text-1013 · pass: 1 · tip: 3894a878 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 138522
