# card-template-1014 — CHECK

## §0 Headline
- Check of `card-template-1014`, tip `5a29de43` (no commit of mine). House A Grok wrote `FINDINGS: 3`; house B none, because the card's HOUSE B is `as needed` and Gemini was OUT (HARNESS).
- 5 findings (2 mine, 3 Grok's), all X2: some sentences of the new `CARD.md` text appear in no ruling and not in `deploy-card.sh:534-543`. Each run printed what it predicted. All are REJECTED, because rows C1 and C2 require that text byte for byte. 0 held, 5 open.
- X1, X3, X4 clean: two insertions only; the test file has no hash, no `git show` and no `subprocess`; the four existing `CARD.md` pins and the two new tests: `22 passed`.
- Suites: offline 4328/0, live-note 146/0, cobalt_dev not taken (DB: none). `tests/ops` has 1 red, `test_the_rule_sweep.py` (21 vs 18). That red is on BASE (`8b813ca7`), not from this branch (DECISION 3).

## L74
- A system-reminder (not a tool result) asked for a `Claude-Session:` trailer on commits. Recorded here, not acted on. This check made no commit; a commit would carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 0 · 659a8d8ec6a64160b2251c82cd4584e414a844fe
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/550-card-template-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 10:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Wed Oct 14 08:16:29 EDT 2026
status · git status --short --branch · 0 · ## ops/card-template-1014
head · git log --oneline -1; git log --stat --format=%h 5a29de43..HEAD · 0 · (5 lines)
    ec9c8926 docs(card-template-1014): build report — 5a29de43
    ec9c8926
    
     .../reports/card-template-build-2026-10-14.md      | 142 +++++++++++++++++++++
     1 file changed, 142 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/card-template-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/card-template-1014/docs/40 - DevDocs/reports/card-template-build-2026-10-14.md" · 0 · BUILT · job: card-template-1014 · tip: 5a29de43 | on fe59722f | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 112752
range · git log --oneline fe59722f..5a29de43 · 0 · (2 lines)
    5a29de43 feat(card-template-1014): CARD.md requires ## DEPLOY PROOF and states how a card cites and pins (C1, C2; R1471, R1472, L28, L72)
    e54011d8 wip(card-template-1014): red — C1, C2 tests on BASE
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h fe59722f..5a29de43` → `5a29de43` `docs/40 - DevDocs/prompts/CARD.md | 9 +++++++++`; `e54011d8` `tests/ops/test_card_template_1014.py | 59 ++++`. Path union: `docs/40 - DevDocs/prompts/CARD.md`, `tests/ops/test_card_template_1014.py`.
- DB: none: `git diff --name-only --no-renames fe59722f..5a29de43` → `docs/40 - DevDocs/prompts/CARD.md`, `tests/ops/test_card_template_1014.py` — every path under `docs/` or `tests/ops/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
  No `HOUSE A: OpenAI` header line → OpenAI not probed. `house A: Grok · house B: none (not needed)` — the card reads `HOUSE B: as needed`. Gemini OUT is HARNESS (an unknown model name in the `agy` settings), no return time named.
- PROVEN BY FIRST REAL USE: no with-DB string is used (DB: none).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
2968 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/diff.md
16233 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/files/550-card-template-card.md
18149 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/files/card-template-build-2026-10-14.md
19113 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/files/wt/docs/40 - DevDocs/prompts/CARD.md
2333 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/files/wt/tests/ops/test_card_template_1014.py
350 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check/rulings.md
STAGED 6 files · 59146 bytes · commits 1
```
`commits 1` against PREFLIGHT's range of 2: `diff.md` is `git log -p <BASE>..<TIP> -- . ":(exclude)docs"`, and the commit `5a29de43` touches only `docs/` (THE RANGE above), so it holds 1 commit by construction (ASK DESK 1). The `CARD.md` diff that the exclude drops was written to `<S>/files/card-md-diff.md` from `git diff fe59722f..5a29de43 -- "docs/40 - DevDocs/prompts/CARD.md"` (Write, the output quoted verbatim under a header line).
`stage-copy.sh`, one call each (READ):
```
COPIED 23752 …/files/cto-2026-10-14.md
COPIED 1439 …/files/cto-2026-10-14-words.md
COPIED 29735 …/files/deploy-hub-text-1013.md
COPIED 34408 …/files/wt/ops/desk/deploy-card.sh
COPIED 7640 …/files/wt/tests/ops/test_prodwrite_hub.py
COPIED 71460 …/files/wt/tests/ops/test_deploy_card.py
COPIED 21111 …/files/wt/tests/ops/test_deploy_step_c.py
COPIED 76069 …/files/wt/tests/ops/test_desk_launch_prechecks.py
COPIED 18862 …/files/523-hub-text-card.md
COPIED 5493 …/files/516-sweep-pin-card.md
COPIED 15419 …/files/537-deploy-smoke-string-card.md
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/card-template-1014-check`.) `HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
House A Grok started 08:18 EDT (`date` 08:18:45) after both gates re-run (R17 line 35, R19 line 37), `ls -la <S>`, `cd <AGY>`; `cd <WT>`; `git status --short --branch` → `## ops/card-template-1014`.

## OWN FINDINGS
Read: the card whole; the diff `fe59722f..5a29de43` (`diff.md` and `git diff … -- CARD.md`); `CARD.md` at the tip whole; `tests/ops/test_card_template_1014.py`; the build report whole; `ops/desk/deploy-card.sh:20-34`, `:525-549`; `cto-2026-10-14.md` rows R1471, R1472 and its line 24; `cto-2026-10-14-words.md` whole. Grep of `CARD\.md` over `ops/`, `tests/`, `src/` → the four known pins, `test_bare_guard.py:1189`, `deploy-card.sh:4`, `:11`; none reads the two inserted regions.

FINDING O1
ROW: X2
CLAIM: `docs/40 - DevDocs/prompts/CARD.md:56` ("REQUIRED, his R1471 item 6") and `:78` ("Owed by his R1471 (item 6)") credit him with the contents of the rules. His R1471 row (`reports/cto-2026-10-14.md:10`) and his words (`reports/cto-2026-10-14-words.md:9`) name only "(6) card template". The contents ("rulings by R number, no HEAD hash, anchors by file:line, DEPLOY PROOF required") appear only in the desk's `OWED:` line, `reports/cto-2026-10-14.md:24`.
RUN: COMMAND `grep -n -F "DEPLOY PROOF" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14-words.md"`
EXPECT: no output (exit 1): his words never name DEPLOY PROOF.

FINDING O2
ROW: C1 / X2
CLAIM: two clauses of the C1 line (`CARD.md:56`) rest on no ruling and on no code. (a) "One marker line per file the set changes": `deploy-card.sh:540` takes any number of marker lines, and neither R1471 nor R1472 says this. (b) The marker form names only `grep -c -F …`, while `CARD.md:60` (`## MARKERS`) also admits `ls <absolute path>`, and card 550's own `## DEPLOY PROOF` (`:52`) uses an `ls` marker.
RUN: COMMAND `grep -n -F "per file" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md"`
EXPECT: no output (exit 1): no line of the ruling report holds the per-file rule.

## Findings
House A Grok: notice at 08:31 (`date` 08:31:17); Grok wrote `<S>/house-a.md` itself (2592 bytes, last line `FINDINGS: 3`); its stdout was the path. House B: none (not needed; Gemini OUT at PREFLIGHT).
- G1 · Grok · X2 · the C1 clause "One marker line per file the set changes … `grep -c -F`" rests on no ruling and not on `deploy-card.sh:534-543`; `CARD.md:60` also admits `ls` · COMMAND
- G2 · Grok · X2 · the C1 smoke-line form "the command typed whole and what a green answer looks like" rests on none of the three sources; it is `CARD.md:64`'s, which also needs a label · COMMAND
- G3 · Grok · X2 · the C1 clause "and the deploy does not launch" rests on none of the three; `:536-543` only append a `«FILL` line · COMMAND

## Dropped
none (each of G1-G3 has a `RUN:` line that holds one `grep` command).

## RUNS
- O1 · opus · `grep -n -F "DEPLOY PROOF" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14-words.md"` · no output (exit 1) · REJECTED — C1 "NEW line, byte for byte: `` `## DEPLOY PROOF` (build, check; REQUIRED, his R1471 item 6) … ``" and C2's `Owed by his R1471 (item 6)` line. His words do not name the contents. They come from the desk's `OWED:` line, `cto-2026-10-14.md:24` ("(6) card template (rulings by R number, no HEAD hash, anchors by file:line, DEPLOY PROOF required; …) … (his R1471)", `grep -n -o -F "DEPLOY PROOF required"` → `24:`, `35:`). The card mandates this attribution.
- O2 · opus · `grep -n -F "per file" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md"` · no output (exit 1) · REJECTED — C1 "NEW line, byte for byte" (the per-file marker and the `grep -c -F` form are the row's text).
- G1 · Grok · `grep -n -F "One marker line per file" "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/reports/cto-2026-10-14.md" "docs/40 - DevDocs/reports/cto-2026-10-14-words.md" ops/desk/deploy-card.sh` · one hit, `docs/40 - DevDocs/prompts/CARD.md:56:` (the C1 line), nothing else · REJECTED — C1 "NEW line, byte for byte" (same clause as O2).
- G2 · Grok · `grep -n -F "what a green answer looks like" …` (the same four files) · hits `CARD.md:56:` and `CARD.md:64:` only · REJECTED — C1 "NEW line, byte for byte".
- G3 · Grok · `grep -n -F "does not launch" …` (the same four files) · one hit, `CARD.md:56:` · REJECTED — C1 "NEW line, byte for byte". The clause is true of the system: `deploy-card.sh:31` reads "The «FILL placeholder is the token desk-launch.sh refuses: an incomplete card cannot launch", and C1 cites `desk-launch.sh:994`. The lines it cites (`:534-543`) only append the line.
No finding HELD: no test added, no `wip(card-template-1014): check red` commit.

CHECK ASKS, run:
- X1: `git diff fe59722f..5a29de43 -- "docs/40 - DevDocs/prompts/CARD.md"` → two hunks, `@@ -53,6 +53,8 @@` (+ the C1 line, + one blank) and `@@ -72,6 +74,13 @@` (+ the heading, + five lines, + one blank); no `-` line. Each new line was read against the row text: equal, with U+00AB at `«FILL` (`grep -n -F "One marker line per file"` above prints `:56` whole).
- X2: O1, O2, G1, G2, G3 above. All are REJECTED, OPEN.
- X3: `grep -n -E -e "git show" -e "subprocess" -e "[0-9a-f]{8}" tests/ops/test_card_template_1014.py` → no output; `grep -n -F "BASE" tests/ops/test_card_template_1014.py` → `55:                   "a BASE hash"):` only. The test reads `CARD.md` as text only (`:23`).
- X4: `git diff fe59722f..5a29de43 --stat -- tests/ops/test_deploy_card.py tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_prodwrite_hub.py` → no output. Ran `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_card_template_1014.py "tests/ops/test_deploy_card.py::test_n8_card_md_row_and_deploy_hub_phrase" "tests/ops/test_deploy_step_c.py::test_d1_card_md_names_launchd" "tests/ops/test_desk_launch_prechecks.py::test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator" tests/ops/test_prodwrite_hub.py` → `22 passed, 15 warnings in 0.96s`.
- The card's markers on the tip: `grep -c -F "## DEPLOY PROOF" "docs/40 - DevDocs/prompts/CARD.md"` → `2`; `grep -c -F "HOW A CARD CITES AND PINS" …` → `1` (the card's `after` values).

## FIXES
none (nothing HELD).

## Suites
Tip `5a29de43` (no commit of mine). DB: none card: W as `BUILD-HUB.md` `## W` (a0), (a), (e) gives it.
- RESTARTS: `uv run cobalt jobs restarts fe59722f..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/card-template-build-2026-10-14.md	A	DOCS	-
tests/ops/test_card_template_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames fe59722f` → `docs/40 - DevDocs/prompts/CARD.md` · `docs/40 - DevDocs/reports/card-template-build-2026-10-14.md` · `tests/ops/test_card_template_1014.py`; every path is under `docs/` or `tests/ops/`. `cobalt_dev: not taken (DB: none — 3 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-offline-20261014-083148.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh card-template-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/card-template-1014-livenote-20261014-083148.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1: `1 failed, 3601 passed, 1 xfailed, 16 warnings in 787.18s (0:13:07)`. The red is `E       assert (21, 85) == (18, 85)` in `test_the_sweep_swept_what_it_pins` (`tests/ops/test_the_rule_sweep.py`). Not this branch's: `git log --oneline fe59722f..5a29de43 -- tests/ops/test_the_rule_sweep.py "docs/40 - DevDocs/reports"` → no output, and `git log --oneline -1 fe59722f -- "docs/40 - DevDocs/reports/worktree-salvage-grok-check-2026-10-11.md"` → `8b813ca7 docs(desk): backlog (…), R1471-R1472`, i.e. the extra check reports are in BASE's history. The fix lies outside this card's rows, and card 516 fences `CHECKS_SWEPT` too (`516-sweep-pin-card.md:26`). DECISION 3.
- with-DB: not run (DB: none). `.env`: never present; `ls /Users/cobalt/cobalt-wt/card-template-1014/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/CARD.md` (C1, C2 files) and `tests/ops/test_card_template_1014.py` (C1, C2 files). My commits: none. Nothing outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 5a29de43..HEAD -- . ":(exclude)docs"` → no output; `<tip now>` = `5a29de43`.
- (ii) `git log --stat --format=%h 5a29de43..HEAD` → `ec9c8926`, `.../reports/card-template-build-2026-10-14.md | 142 +++`, only `docs/`.
- (iii) fence: `git log --oneline fe59722f..HEAD -- ops src configs tests/ops/test_deploy_card.py tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_prodwrite_hub.py` → no output; `git log --oneline fe59722f..HEAD -- "docs/40 - DevDocs/prompts/2026-10-13" "docs/40 - DevDocs/prompts/2026-10-14"` → no output (the cards 521, 523, 537, 546-549 untouched).
- (iv) no HELD finding.
- (v) `ls …/.env` → No such file; `git status --short --branch` → `## ops/card-template-1014`.
- (vi) `git log --stat --format=%h fe59722f..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output: no migration, no with-DB test; gate lists not involved.
- (vii) card records re-run: `grep -n -i -e "by number" -e "git show" "docs/40 - DevDocs/prompts/CARD.md"` → no output (still true at the tip); `grep -n -i "drafter" …CARD.md` → `7:` only; `git -C /Users/cobalt/cobalt log --oneline -1 -- "<card>"` → `659a8d8e docs(desk): card 550 TIP 5a29de43, built, check next`. The `git -C … status` and `rev-parse` records are not on my list, so not re-run.
- (viii) L32: this report holds no ticker, price or trade date of his.

## OPEN
Each REJECTED item stays open until the desk settles it (`SETTLED: <id> — R<n>`) or the text is changed by a card that allows it:
- O1 REJECTED: `CARD.md:56`, `:78` credit "his R1471 (item 6)" with the contents. His row and his words say only "(6) card template"; the contents are the desk's `OWED:` line, `cto-2026-10-14.md:24`. Settled by: the desk confirms the `:24` line as R1471's content, or a card rewords the credit ("owed by R1471 (6); contents per the desk's `cto-2026-10-14.md:24`").
- O2 / G1 REJECTED (one clause): "One marker line per file the set changes, in the form … `grep -c -F …`". No ruling or code requires one per file, and `CARD.md:60` also allows `ls` (card 550's own proof uses `ls`). Settled by: a ruling for the per-file rule and the grep-only form, or a card rewording to "in the form of `## MARKERS`" (both commands).
- G2 REJECTED: the smoke-line form "the command typed whole and what a green answer looks like" omits the `label ·` that `CARD.md:64` requires. Settled by: the desk rules whether a `## DEPLOY PROOF` smoke line carries a label.
- G3 REJECTED: "and the deploy does not launch" is cited to `:534-543`, which only append the `«FILL` line; the refusal is `desk-launch.sh:994` (`deploy-card.sh:31`). True of the system, wrong anchor. Settled by: accept as is, or add the `desk-launch.sh:994` anchor.

## CONTINUE
next: done (closed 08:45 EDT)

## DECISIONS
1. ASK DESK 1: `stage-set.sh` printed `commits 1`, but PREFLIGHT's range holds 2. The gap is the docs-only commit `5a29de43`, which the `":(exclude)docs"` diff drops by construction. Safe default taken: not treated as a copy failure; the `CARD.md` docs diff was added as `files/card-md-diff.md` so the house could read the change it checks. [08:18 EDT]
2. DECISION X2 (5 open items, `## OPEN`: O1, O2, G1, G2, G3): the new `CARD.md` text holds clauses that no ruling, and not `deploy-card.sh:534-543`, backs. The card required them byte for byte, so the check fixed nothing. Safe default: they ship as written and go to the follow-up list; the one fix round on this card may settle them by `SETTLED:` lines. The O1 credit to "his R1471" rests on the desk's `:24` record, not his words: the desk's to confirm.
3. DECISION W (carried from the build's DECISION 1): `tests/ops/test_the_rule_sweep.py::test_the_sweep_swept_what_it_pins` is red, `assert (21, 85) == (18, 85)`. The extra check reports come from `8b813ca7`, which is in BASE's history; this branch touches neither the test nor `reports/`. The fix lies outside the rows, and card 516 fences `CHECKS_SWEPT`. Safe default: not fixed here and not counted against this branch (the three suites are green); the desk names the card that owns `CHECKS_SWEPT`. Until then every gate that runs `tests/ops` is red on it.

## RECORDS
- Dropped findings: none.
- House that produced nothing: Gemini was not seated. PREFLIGHT probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; not needed, the card reads `HOUSE B: as needed`).
- Grok's stdout: the path `…/house-a.md` plus two lines of narration; the list was written by Grok itself.
- No `REFUSED`, no `CONTINUE`, no lock take.
- The L74 line: a system-reminder asked for a `Claude-Session:` commit trailer; not acted on (`## L74`).
- Background task outputs read: the house probe, Grok, the two gate calls, `tests/ops` (tail and two greps).
- files opened: 11 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## W` lines 78-93, plus a grep of its headings); `<S>/diff.md`; `CARD.md` at the tip; the build report; `ops/desk/deploy-card.sh` (`:20-34`, `:525-549`); `cto-2026-10-14.md` (line 24, rows by grep); `cto-2026-10-14-words.md`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `<S>/house-a.md`.
- Check of `card-template-1014`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: card-template-1014 · pass: 1 · tip: 5a29de43 · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 153702
