JOB: next-flow
LADDER: OFF-LADDER — cto-2026-10-05.md R438
BRANCH: ops/next-flow-1006
WORKTREE: next-flow-1006
BASE: 1f4a8598
TIP:
REPORT: /Users/cobalt/cobalt-wt/next-flow-1006/docs/40 - DevDocs/reports/next-flow-build-2026-10-06.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-05 R438, 2026-10-05 R412

## ROWS

Each edit below is one exact replacement. OLD is quoted byte for byte from the file at BASE with its `file:line` (every OLD was read from the file and proven by `grep -n -F`, see `## RECORDS`); NEW is the text that replaces it. Quote marks « » are this card's delimiters, not file text. KEYS: where OLD or NEW holds a backtick (a bare `grep -n -F` argument may not), the edit names a backtick-free OLDKEY or NEWKEY taken from it; otherwise the key is the OLD or NEW text itself. A line marked DELETE is removed whole (its key is its start). Edits on one line are made in the order listed; line numbers are at BASE.

| row | what | red first | files |
|---|---|---|---|
| F1 | Both outside vendors run inside the check, at once, one report (R438 change 1; L67 stays: two different houses, never fewer than one other house). Edits F1.01 to F1.37 below: CHECK-HUB runs house A and house B at the same time from one staging, reads both lists after its own, writes one report; the second pass (`## PASS 2`, `PASS-2.`, `house B: needed`, `opus-1.md`, `diff-b.md`) is removed. The stop line keeps `pass: 1` and every field name; only the `house B:` value changes. | for each edit: `grep -n -F` of NEW (or NEWKEY) → exactly one hit; `grep -n -F` of OLD (or OLDKEY) → no hit; then `uv run pytest -q tests/ops/test_hub_lines.py` → `0 failed` (no pinned line moves: the launch lines, the `- **GROK:** ` line and DEPLOY-HUB G (f) are untouched, so the test file is NOT changed) | `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/BUILD-HUB.md` (F1.37 only) |
| F2 | ONE fix round for all findings, by the original builder on the same card, no re-check, no third vendor pass (R438 change 2; L75 extended; the round reruns the touched tests, then the deploy gate's pass). Edits F2.01 to F2.03: the sentence that lived in the deleted `## PASS 2` (CHECK-HUB line 124) and in BUILD-HUB line 109 is rewritten for one round. The check still fixes what holds inside the card's rows (`## 5` stands); the round takes what it leaves (see DECISION 3 of the drafter's report). | as F1: NEW one hit, OLD no hit, then the pytest line, no test-file change | `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/BUILD-HUB.md` |
| F3 | Every build W step and every check runs the deploy gate's pass: `gate.sh <WORKTREE> all --deploy …` (R438 change 3). Spelling read from `ops/desk/gate.sh:2` and `:72` (`[--deploy]`, accepted by `withdb` and `all` only, `:112`), and from `DEPLOY-HUB.md:101` (`gate.sh <WORKTREE> all --deploy`). Edits F3.01 to F3.10. The flag is not carried by a "DB: none" card's `offline` and `livenote` calls (gate.sh refuses it there): F3.03 and F3.10 say so. | as F1: NEW one hit, OLD no hit, then the pytest line, no test-file change | `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/BUILD-HUB.md` |

F4 (drafters prove every `file:line` and count against BASE and record each read in `## RECORDS`) has NO row: no hub holds the drafter shape (the four fixed hubs and CARD.md name no drafter `HOW` or `REPORT` line); it lives in the desk's contract (R438 change 4) and in each drafter prompt. The drafter's report records this.

### F1 edits — CHECK-HUB.md

F1.01 · CHECK-HUB.md:3 · OLD «you start ONE outside house, you judge» · NEW «you start TWO outside houses at once, you judge»
F1.02 · CHECK-HUB.md:3 · OLD «SESSION: fresh. PASS 1, unless your launch message starts `PASS-2.` — then `## PASS 2` binds and replaces `## 1`–`## 3` ·» · NEW «SESSION: fresh, ONE pass (there is no `PASS-2`) ·» · OLDKEY «PASS 1, unless your launch message starts» · NEWKEY «ONE pass (there is no»
F1.03 · CHECK-HUB.md:3 · OLD «but the ONE outside house of your pass (L36)» · NEW «but the TWO outside houses of this check, started at once (L36)»
F1.04 · CHECK-HUB.md:3 · OLD «METER: Anthropic medium per pass» · NEW «METER: Anthropic medium for the check»
F1.05 · CHECK-HUB.md:5 · OLD «(the scratch folder of both passes;» · NEW «(the scratch folder of the check;»
F1.06 · CHECK-HUB.md:8 · OLD «THE SECOND PASS is a second launch, `desk-launch.sh check <card> PASS-2`, of the same line with `PASS-2. ` put before `Read`, after the pass-1 session is verified, stopped and removed; there is no third.» · NEW «THERE IS NO SECOND PASS: both outside houses run in this one session and this file never asks for `desk-launch.sh check <card> PASS-2` (his 2026-10-05 R438).» · OLDKEY «THE SECOND PASS is a second launch» · NEWKEY «THERE IS NO SECOND PASS: both outside houses»
F1.07 · CHECK-HUB.md:8 · OLD «commits the report after each pass.» · NEW «commits the report after the check.»
F1.08 · CHECK-HUB.md:14 · OLD «the brain's RULED CHECK FLOW and THIRD PASS; L67 as amended)» · NEW «the brain's RULED CHECK FLOW and THIRD PASS; L67 as amended; his 2026-10-05 R438, the next flow)»
F1.09 · CHECK-HUB.md:15 · OLD «PASS 1 — this session:» · NEW «THE ONE PASS — this session:»
F1.10 · CHECK-HUB.md:16 · OLD «START HOUSE A, one house outside Anthropic, in the background. It reads the card, the diff» · NEW «START HOUSE A AND HOUSE B AT ONCE, two different houses outside Anthropic, in the background. Each reads the card, the diff»
F1.11 · CHECK-HUB.md:16 · OLD «touches. It cannot run a command» · NEW «touches, and neither reads the other's list. Neither can run a command»
F1.12 · CHECK-HUB.md:17 · OLD «2. WHILE HOUSE A RUNS you read the same set yourself» · NEW «2. WHILE BOTH HOUSES RUN you read the same set yourself»
F1.13 · CHECK-HUB.md:17 · OLD «You do not open house A's list before your own is written.» · NEW «You open neither house's list before your own is written.»
F1.14 · CHECK-HUB.md:18 · OLD «3. ONLY THEN house A's list. A block that carries nothing runnable is dropped (a form rule).» · NEW «3. ONLY THEN both lists, house A's and house B's. A block that carries nothing runnable is dropped (a form rule). Every finding of yours and of both houses goes into the ONE check report.»
F1.15 · CHECK-HUB.md:19 · OLD «yours and the house's, BY RUNNING IT» · NEW «yours and both houses', BY RUNNING IT»
F1.16 · CHECK-HUB.md:20 · OLD «5. Nothing open and the card not `mandatory` → `house B: not needed`: DONE. Something open (a finding you could not settle, or one you reject although its test runs red for its stated reason), or a `mandatory` card → `house B: needed`.» · NEW «5. DONE when every held finding is fixed (`## 5`) and the suites are green (`## 6`). A finding you could not settle, or one you reject although its test runs red for its stated reason, goes under `## OPEN` as FOLLOW-UP: there is no second pass.» · OLDKEY «5. Nothing open and the card not» · NEWKEY «5. DONE when every held finding is fixed»
F1.17 · CHECK-HUB.md:21 · DELETE the line that begins «PASS 2 — a NEW Opus session, only when pass 1 says» and put in its place the line · NEW «NO SECOND PASS, NO FURTHER HOUSE: what no test can catch ships and goes on the follow-up list. L67 stays: two different houses, never fewer than one other house.» · OLDKEY «PASS 2 — a NEW Opus session, only when pass 1 says» · NEWKEY «NO SECOND PASS, NO FURTHER HOUSE: what no test can catch ships»
F1.18 · CHECK-HUB.md:22 · OLD «changes sizing runs pass 2 even when nothing is open.» · NEW «changes sizing needs BOTH houses up.»
F1.19 · CHECK-HUB.md:23 · OLD «house B = the next one UP after it.» · NEW «house B = the next one UP after it; both start at once.»
F1.20 · CHECK-HUB.md:36 · OLD «house A's list (pass 2: house B's list and pass 1's sections of the report).» · NEW «house A's list and house B's list.» · OLDKEY «(pass 2: house B's list and pass 1's sections of the report)» · NEWKEY «house A's list and house B's list.»
F1.21 · CHECK-HUB.md:58 · OLD «Pass 2 appends the same sections under one `# PASS 2` heading in the same file and writes the new last line.» · NEW «One pass, one report: both houses' findings sit under `## Findings` and `## Dropped`, each row naming its house.» · OLDKEY «Pass 2 appends the same sections under one» · NEWKEY «One pass, one report: both houses' findings sit under»
F1.22 · CHECK-HUB.md:65 · OLD «house B, if needed: <name|none>» · NEW «house B: <name|none>» · NEWKEY «house A: <name> · house B: <name|none>» (the full recorded line, which reads «Record `house A: <name> · house B: <name|none>` from the SEAT ORDER»)
F1.23 · CHECK-HUB.md:69 · OLD «## 1. STAGE AND START HOUSE A — one instructions file» · NEW «## 1. STAGE AND START HOUSE A AND HOUSE B — one instructions file»
F1.24 · CHECK-HUB.md:87 · REPLACE the whole line · OLD «HOUSE B gets the same text with this paragraph added before "EVERY FINDING": "You are the SECOND house. Read also `house-a.md` (the first house's findings) and `opus-1.md` (what the Opus session found itself, what it ran, what held, what it fixed, what is OPEN). The diff you read is `diff-b.md`, which includes its fixes. Add findings the two lists miss, and for each OPEN item write the test or command that would settle it."» · NEW «HOUSE B gets exactly the same HOUSE TEXT as house A, in the same `<S>/HOUSE-INSTRUCTIONS.md`: the two houses run at once and read neither list.» · OLDKEY «HOUSE B gets the same text with this paragraph added» · NEWKEY «HOUSE B gets exactly the same HOUSE TEXT as house A»
F1.25 · CHECK-HUB.md:89 · OLD «(5) START THE HOUSE. » · NEW «(5) START BOTH HOUSES AT ONCE. »
F1.26 · CHECK-HUB.md:89 · OLD «; ONE attempt, » · NEW «; for each of house A and house B ONE attempt, started in two calls, one after the other, with no wait between, »
F1.27 · CHECK-HUB.md:89 · OLD «The spelling of the house that sits:» · NEW «House B's spelling is house A's with house-b.md for house-a.md. The spelling of each house that sits:»
F1.28 · CHECK-HUB.md:93 · OLD «next: 2 (house A <name> started <time>)» · NEW «next: 2 (house A <name> and house B <name> started <time>)»
F1.29 · CHECK-HUB.md:95 · OLD «## 2. YOUR OWN READ, FIRST — while house A runs» · NEW «## 2. YOUR OWN READ, FIRST — while both houses run»
F1.30 · CHECK-HUB.md:96 · OLD «A completion notice of the house that arrives» · NEW «A completion notice of either house that arrives»
F1.31 · CHECK-HUB.md:98 · OLD «## 3. HOUSE A'S LIST — only now» · NEW «## 3. BOTH HOUSES' LISTS — only now»
F1.32 · CHECK-HUB.md:99 · OLD «House A still running → this is the ONE place a turn may end: the in-progress last line stands and its completion notice (or its 45-minute stop) resumes you.» · NEW «A house still running → this is the ONE place a turn may end: the in-progress last line stands and each completion notice (or 45-minute stop) resumes you; you go on only when BOTH houses have finished or stopped.»
F1.33 · CHECK-HUB.md:99 · OLD «Its list is `<S>/house-a.md` (written by Grok,» · NEW «House A's list is `<S>/house-a.md` and house B's is `<S>/house-b.md`, each (written by Grok,» · OLDKEY «Its list is» · NEWKEY «and house B's is»
F1.34 · CHECK-HUB.md:100 · OLD «NOTHING PRODUCED (METER, HARNESS, TIMEOUT, no `FINDINGS:` line): recorded verbatim; the next house in the order takes seat A — `## 1` (5) again, its one attempt — and house B moves down the order with it. No house left → `FAILED: 3 — no house A produced a list (<each house and its line>)`.» · NEW «NOTHING PRODUCED by a house (METER, HARNESS, TIMEOUT, no `FINDINGS:` line): recorded verbatim; the next house UP in the order that has not sat takes its seat, started on its own, ONE attempt — `## 1` (5) again. No such house → that seat is `none produced`; no house produced a list → `FAILED: 3 — no house produced a list (<each house and its line>)`; a `mandatory` card with a seat `none produced` → `FAILED: 3 — house B mandatory and none produced (<each house and its line>)`.» · OLDKEY «NOTHING PRODUCED (METER, HARNESS, TIMEOUT, no» · NEWKEY «NOTHING PRODUCED by a house (METER»
F1.35 · CHECK-HUB.md:103 · OLD «## 4. JUDGE EVERY FINDING BY RUNNING IT — yours, then the house's» · NEW «## 4. JUDGE EVERY FINDING BY RUNNING IT — yours, then both houses'»
F1.36 · CHECK-HUB.md:117 · OLD «`house B:` = `needed` when `open` is above 0 or the card says `HOUSE B: mandatory` (and is not overruled); `none available` when it is needed, the card is not `mandatory` and PREFLIGHT found no second house up (the open items are then listed once more under `## DECISIONS`: they ship to the follow-up list unless the judgment seat orders PASS-2 when a meter is back); otherwise `not needed`. Write `<S>/opus-1.md` = your `## OWN FINDINGS`, `## RUNS`, `## FIXES` and `## OPEN` sections, copied whole (house B reads it).» · NEW «`house B:` = `<name> <its FINDINGS line|METER|HARNESS|TIMEOUT|NO FINDINGS LINE>`, or `none available` when PREFLIGHT found no second house up and the card is not `mandatory` (the open items are then listed once more under `## DECISIONS`: they ship to the follow-up list).» · OLDKEYS «PASS-2 when a meter is back» and «(house B reads it)» · NEWKEY «found no second house up and the card is not»
F1.36b · CHECK-HUB.md:117 · OLD «Check of `<JOB>`, pass <k>: house <A|B> `<name>` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass.» · NEW «Check of `<JOB>`: house A `<name>`, house B `<name|none>` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round.» · OLDKEY «Nothing loops after the second pass.» · NEWKEY «Nothing loops: one pass, one fix round.»
F1.37 · CHECK-HUB.md:119 to :124 · DELETE the section: the heading line that begins «## PASS 2 — a launch whose message starts» and the five lines under it that begin «- PREFLIGHT, added: », «- P2.1 STAGE: », «- P2.2 START HOUSE B: », «- P2.3 WAIT for it», «- THEN » (the last sentence of the last line, "After a check, a small fix …", is carried by F2.02). No new text; OLDKEYS are those six line starts (each: no hit). The stop line `CHECK DONE · job: <JOB> · pass: 2 …` (line 129) is deleted in F1.40.
F1.38 · CHECK-HUB.md:127 · OLD « · house B: needed|not needed|none available · » · NEW « · house B: <name> <its FINDINGS line|METER|HARNESS|TIMEOUT|NO FINDINGS LINE>|none available · » · OLDKEY «house B: needed|not needed|none available» · NEWKEY «NO FINDINGS LINE>|none available ·»
F1.39 · CHECK-HUB.md:129 · DELETE the whole line that begins «`CHECK DONE · job: <JOB> · pass: 2 · tip:» (OLDKEY «job: <JOB> · pass: 2 · tip:»)
F1.40 · CHECK-HUB.md:131 · OLD «only when the suites are green (or stand as built), » · NEW «only when the suites are green, » · OLDKEY «(or stand as built), » · NEWKEY «only when the suites are green, »
F1.41 · CHECK-HUB.md:131 · OLD «, and — pass 1 — `house B:` is `not needed` or `none available`. A pass-1 line with `house B: needed` is `ready: NO`: the desk launches PASS-2.» · NEW «, and the card's HOUSE B rule held (a `mandatory` card whose house B is `none produced` or `none available` is `ready: NO`).» · OLDKEY «A pass-1 line with» · NEWKEY «the card's HOUSE B rule held»

### F1 edit — BUILD-HUB.md

F1.42 · BUILD-HUB.md:17 · OLD «its own and an outside house's — and fixes what holds» · NEW «its own and both outside houses' — and fixes what holds»

### F2 edits

F2.01 · CHECK-HUB.md:107 · OLD «(it needs a build: a card row backed by its» · NEW «(it goes to the original builder's ONE fix round on this card, his R438: a card row backed by its»
F2.02 · CHECK-HUB.md:131 · OLD «launches the next step. Then stop.» · NEW «launches the next step. AFTER A CHECK there is ONE fix round for every finding left (open, or held and not fixed), by the original builder on the same card: only the tests that touch the fixed part rerun, then the deploy gate's pass (gate.sh with --deploy); no re-check, no second check and no third vendor pass (his R438; L75, his R376). Then stop.»
F2.03 · BUILD-HUB.md:109 · OLD «a small fix to this feature is yours, on this same card: only the tests that touch the fixed part rerun, then the deploy gate; no re-check and no outside review (L75, his R376).» · NEW «ONE fix round is yours, on this same card, for every finding the check and its two outside houses left (his R438, L75 extended): only the tests that touch the fixed part rerun, then the deploy gate's pass (gate.sh with --deploy); no re-check, no second check and no third vendor pass (L75, his R376).»

### F3 edits

F3.01 · CHECK-HUB.md:110 · OLD «No commit of yours → the build's three suite lines stand: quote them and the RESTARTS line from its report; `suites: as built (no commit)`. One commit or more → » · NEW «EVERY check runs the deploy gate's pass (his R438), with a commit of yours or none (with none, the tip is the build's `TIP`): » · OLDKEY «No commit of yours → the build's three suite lines stand» · NEWKEY «EVERY check runs the deploy gate's pass (his R438)»
F3.01b · CHECK-HUB.md:110 · OLD «on your new tip, as ONE call:» · NEW «on the tip named above, as ONE call:»
F3.02 · CHECK-HUB.md:110 · OLD «<WORKTREE> all [--deselect <id>]…» · NEW «<WORKTREE> all --deploy [--deselect <id>]…»
F3.03 · CHECK-HUB.md:110 · OLD «A "DB: none" card: after a commit of yours, RESTARTS» · NEW «A "DB: none" card (gate.sh accepts --deploy with withdb and all only, so none is typed here): after a commit of yours or none, RESTARTS» · OLDKEY «after a commit of yours, RESTARTS» · NEWKEY «gate.sh accepts --deploy with withdb and all only, so none is typed here»
F3.04 · CHECK-HUB.md:127 · OLD « | suites: as built (no commit) ·» · NEW « ·» · OLDKEY «| suites: as built (no commit)» · NEWKEY «live-note <l>/0 · cobalt_dev: 0013»
F3.05 · BUILD-HUB.md:78 · OLD «and nothing of (b) to (d) or (f).» · NEW «and nothing of (b) to (d) or (f); --deploy is not typed here, gate.sh accepts it with withdb and all only (his R438 reaches every card with a with-DB suite).»
F3.06 · BUILD-HUB.md:79 · OLD «<WORKTREE> all [--deselect <id>]…» · NEW «<WORKTREE> all --deploy [--deselect <id>]…»
F3.07 · BUILD-HUB.md:79 · OLD «for a build that adds a migration.» · NEW «for a build that adds a migration; --deploy is on EVERY call (his R438: the deploy gate's whole pass 1, so a deploy-only red is caught at build, not at deploy).»
F3.08 · BUILD-HUB.md:82 · OLD «the with-DB tests only (--db-only; the rest ran in (a)):» · NEW «the deploy gate's WHOLE pass 1 (--deploy: the one --db-only token removed, printing pass 1: whole (deploy); the offline tests run again here, on purpose; his R438):»
F3.09 · BUILD-HUB.md:82 · OLD «grep -n -F "tests/cobalt tests/taxonomy --db-only" <log>» · NEW «grep -n -F "pass 1: whole (deploy)" <log>» · OLDKEY «tests/taxonomy --db-only» · NEWKEY «"pass 1: whole (deploy)" <log>»
F3.10 · BUILD-HUB.md:83 · OLD «stays a quoted mark here, never a red: only the deploy gate judges skips» · NEW «is a RED here, judged as DEPLOY-HUB.md STEP-G (c) judges it: any skip outside the allowed set = red (his R438)»
F3.11 · BUILD-HUB.md:83 · OLD «runs without --db-only, on purpose.» · NEW «runs without --db-only, on purpose; so does this pass (his R438).»

## NOT IN THIS JOB
- `ops/desk/*` scripts: `desk-launch.sh` (its `PASS-2` branch, lines 881–886) and `preflight.sh` (lines 147–155) stay as they are; with F1 no pass-1 line says `house B: needed`, so neither branch fires.
- `DEPLOY-HUB.md` (its STEP-G stays the one place the deploy gate is spelled), `DEVFIX-HUB.md`, `CARD.md`, and any other hub rule: the launch lines, allow strings, the `- **GROK:** ` line, SEAT ORDER, the house spellings, `## 1` staging scripts, the stop-line field names and the `pass: 1` literal.
- `tests/ops/test_hub_lines.py`: not changed; no new test.
- The desk's own MEASURE rows (R438 change 5, the contract), the drafter `Order:` text in the contract, and changes 6 to 8 of `next-flow-answer-2026-10-05.md` (the launcher card, the deploy-card tickers): not hub text, not this card.
- `HOUSE A: none — overruled`: left to the desk; no overrule is written here.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/next-flow-answer-2026-10-05.md`, whole (changes 1 to 4).
- `prompts/CHECK-HUB.md` lines 3 to 131 and `prompts/BUILD-HUB.md` lines 17, 76 to 83, 109 (the lines the edits name).
- `ops/desk/gate.sh` lines 1 to 50 (usage, `--deploy`), 72, 106, 112, 176 to 195, 429 to 431; `prompts/DEPLOY-HUB.md` lines 101 and 103 (the deploy pass and its skip judgment).
- `tests/ops/test_hub_lines.py` lines 76 to 122 (what pins the hubs).
- LAWS `L67`, `L68`, `L71`, `L75`.

## CHECK ASKS
- X1 Does any hub still describe two checks, a re-check after a fix, or a third vendor pass? Run `grep -n -F` over CHECK-HUB.md, BUILD-HUB.md and DEPLOY-HUB.md for «PASS-2», «PASS 2», «house B: needed», «opus-1», «diff-b», «second pass», «re-check», «outside review»; every hit must be a statement that none exists (the fence lines F1.06, F1.17, F1.02, F2.03), or DEPLOY-HUB.md text outside this job (list it, do not fix it).
- X2 Does `--deploy` appear in exactly the steps F3 names? `grep -n -F -- "--deploy"` on BUILD-HUB.md must hit lines 78 (F3.05), 79 (F3.06, F3.07), 82 (F3.08) and the stop-line paragraph at 109 (F2.03, the fix round), nothing else; on CHECK-HUB.md the hits are the `## 6` line (F3.02, F3.03) and the stop-line paragraph (F2.02), nothing else.
- X3 Is the `gate.sh` spelling exact? The only new spelling is `<WORKTREE> all --deploy` before the existing options; confirm against `ops/desk/gate.sh:2` and `:106`, and that no edit invents a flag.
- X4 Does any edit move a line `tests/ops/test_hub_lines.py` pins (the one `claude --bg ` line of each hub, the `- **GROK:** ` line, DEPLOY-HUB G (f))? Expected: none.
- X5 After F1 does CHECK-HUB still read as one consistent flow: every mention of «house A» alone in `## 1` to `## 8` either names both houses or a house-specific spelling, and `## 8`'s stop line names `house B:` with a house name or `none available`?

## RECORDS
- Every OLD key above was run as `grep -n -o -F -f <keys> <hub>` against CHECK-HUB.md and BUILD-HUB.md at head `e71a5fa1`: each key hit once, on the line the edit names (the drafter, 00:51 ET).
- BASE fill: head of main at launch; at drafting time `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` printed `e71a5fa1`, and `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` printed nothing (the drafter, 00:49 ET), so the line numbers above hold at that head; the desk re-proves each OLD against the real BASE before it launches.
- His R438: `grep -n "^| R438 " reports/cto-2026-10-05.md` → line 173, a row that carries `HIS RULING` and ends `APPLIED: contract, NOW 15:42`; it does NOT carry `APPROVED` (see the drafter's DECISION 1). His R412: line 109, carries `HIS RULING` and `APPROVED`. Both rows are committed (`git log --oneline -3 -- reports/cto-2026-10-05.md` → `59981ca7`).
- `reports/next-flow-answer-2026-10-05.md` has 6 uncommitted lines in the working tree (`git diff --stat` → 6 insertions); the card reads the working-tree copy as the prompt ordered.
- The hubs' pinned lines (`tests/ops/test_hub_lines.py`): launch lines at CHECK-HUB.md:10 and BUILD-HUB.md:12, the GROK line at CHECK-HUB.md:91 and DEPLOY-HUB G (f); no edit above touches them.
