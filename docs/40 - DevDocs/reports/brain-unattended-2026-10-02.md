# BRAIN — one standard for unattended work, 2026-10-02 (prompt `prompts/2026-10-02/03-brain-unattended.md`, seat `brain` `776c834d`, Fable 5.1, read-only)

`D` = `docs/40 - DevDocs` · `M` = `Vault/Think/6 - Permanent/Memory` · a row is `<mm-dd> R<n>` of `D/reports/cto-2026-<mm-dd>.md` · `CL` = `M/topics/cto-desk-checklist.md` · `CT` = `M/topics/cto-desk-contract.md` · `WU` = `D/prompts/CTO-DESK-WAKEUP.md` · `UL` = `D/prompts/UNATTENDED-LAUNCH.md` · `B 3`, `D 6`, `E 11` = a row of that section's table · times ET · written 07:12.

## §0 Headline
1. His question F: both. The process misses routes (dev DB repair, a settings change, failed-gate cleanup, house file staging, a fixed-file line change), and at each gap the desk built the route by hand: a script, a fixed-file line, a write-path prompt, law text. Today's rebuild script was written by a worker (`cf75cbe2`), not by the desk.
2. This morning's four returns have three causes: no dev DB repair route (10-02 R11, R14, R16, R18), an A/B that offered a ruled side (R11's B), and two asks that did not block the order (R26, R27). L78 covers the last two. Only a route removes the first.
3. The big losses of 10-01 and 10-02 were waits, not work: 7 h 19 min on three A/Bs asked at night, all answered A (10-01 R50, R58, R59 → 10-02 R7–R9); 7 h 12 min between `04` BUILT and its check (10-01 R27, R28); 4 h 09 min with `cobalt_dev` unusable (10-02 R5 → R24); 4 h 06 min staging one file for a house (10-01 R29 → R49).
4. One standard below: his order is the approval; the desk fills cards; a shell runner chains build → check → ready; a worker calls one script per step; every known failure has a scripted next step; a rule lives in a script, not on the read path. 24 script rows in six cards (cards `11`–`13` merged in), 26 strike-or-merge rows, 13 items for him.
5. LIVE RISK, the 09:30 order: `DEPLOY-HUB.md` P1 (iv) takes a window override only from a row that names the deploy card's `JOB`; R10 and R14 name `04` and a deadline, no job. Keep `04` in the card's `JOB` and put the desk's reading (R10 + R14 = this deploy) in its `## RECORDS`. A P1 failure there would be a fifth return.

## THE STANDARD
1. ORDER. His order is one §4 row. It approves every step below for every card filed under it (L78). A card cites that row in `RULINGS`; no card needs its own launch word.
2. ONE LIST. Before the first launch the desk runs `order-open.sh`: meters, lock, dev DB health, strings outside the approved classes, the window, a mandatory house B. What is his goes to him as ONE list. Nothing else reaches him until DONE, except a step that failed twice by approved commands and has no scripted route.
3. ASK CLASSES, the only things that reach him: scope · dates · money · a new permission class or production string · a carried held defect · a schema rollback · the failed-twice step. An ask names its class; an ask with no class is not sent.
4. CARD. The desk fills cards and nothing else. A build card also carries `## DEPLOY PROOF` (markers, smoke reads), so a script assembles the deploy card.
5. RUN. `job-run.sh <card>` chains build → verify → card fill → check → pass 2 → `READY`. It is a shell runner, not a model. It wakes the desk only on `FAILED`, `for Dejan > 0` or `READY`.
6. STEPS ARE SCRIPTS. A worker calls one script per step (`authorize`, `preflight`, `gate`, `stage-set`, `deploy-step0`, `deploy-outage`, `deploy-smoke`). Each prints a short verdict and a log path. A fixed file holds judgment, not command text.
7. FAIL FORWARD. Every known failure has a scripted next step the desk runs without asking: lock held → wait · dev DB dirty, off level or out of slots → self-heal or `devfix` · gate red on the environment → `gate-clean`, one re-cut · house out → next house · compound command → the guard, resend bare.
8. DECIDE. A worker takes the safe default. The judge seat answers decisions, held findings and fence questions inside the ordered feature. The desk decides what a ruled law covers and records it.
9. DEPLOY. `deploy-card.sh` builds the card from every READY job. The deploy launches itself in the window, or at once under a dated order (L73).
10. DONE. One message to him: what shipped, what was decided for him to veto, what waits. Cleanup by `job-clean.sh`.
11. THE DESK IS CLERICAL. It writes rows, cards and messages. It never writes a script, a fixed file, a write-path prompt, an allow line, code, config or law text. Work with no route = a route card, built and checked like any feature; if the order is blocked he is told once.
12. RULES LIVE IN SCRIPTS. A lesson becomes a script refusal. A rule a script enforces leaves the read path. Law changes fold at the nightly close, which a timer starts.
13. KINDS. `build`, `check`, `deploy`, `devfix`, `judge`, `close`: fixed files. `brain`, drafter, survey: read-only prompts. No other kind exists.

## A EFFICIENT
Today one feature passes about 15 desk touch points and 6–8 sessions: card → launch word → build → verify → judge → card fill → check → pass 2 → report commit → deploy-card drafter → deploy → verify → judge → cleanup → push. The standard keeps build, check and deploy and cuts what sits between them: three desk touch points (the one list, the run, DONE).

| # | cut | today | standard | saves |
|---|---|---|---|---|
| 1 | launch word per card | CL L7a wants his row per job; build `02` launched before it and failed AUTHORIZATION (10-01 R9, R10) | the card cites the order's row | one ask per card |
| 2 | desk steps between stages | verify, fill, commit, launch, watch, tab: about 7 calls per stage, each a full desk turn | `job-run.sh` | about 25 desk turns per job and the silent gaps (D 14) |
| 3 | deploy-card drafter | one session per deploy (09-30: 6 min, 185,176 tokens, 4 decisions; 10-02 R2) | `deploy-card.sh`; the build card carries `## DEPLOY PROOF` | one session per deploy |
| 4 | commands typed by workers | AUTHORIZATION 6–8 calls, PREFLIGHT 15–25, W about 30, deploy STEP-0 about 45 (`deploy-2026-10-01-1.md`), each a full worker turn | one script per step | most worker turns (C 4) |
| 5 | E0 baseline suite | `BUILD-HUB.md` E0 runs the offline suite on `BASE` (about 10 min), then W runs it again | skip E0 when `BASE` is code-identical to the last deploy tag; keep it for a stacked base | about 10 min per build |
| 6 | gate on a tree already checked | the deploy re-runs three suites (10-02: 9:39 offline + 11:42 with-DB pass 1) even for one branch whose code equals its checked tip | prove the trees equal, take the check's suite lines (FOR DEJAN 9) | about 25 min per single-branch deploy |
| 7 | TREE STATE | the pass-1 and pass-2 commands are 1.5 KB of prose each in two hub files; a build row edits both; the check re-proves it (`CHECK-HUB.md` `## 7` (vi)) | the pass lists live in one file `gate.sh` reads; the card key and the row go | a row per with-DB build and its failure class |
| 8 | folds inside an order | three rule-file edits 06:43–06:46 inside the deadline order (10-02 R27–R29) | a row binds at once; the close folds (FOR DEJAN 7) | desk turns, classifier refusals |
| 9 | serial checks | one outside house up until 10-04 (Sol, Astra out; Gemini HARNESS on `07`) and one Grok hub at a time (CL L15): three builds done by the morning of 10-01, their checks ran 17:22–23:56 | probe once whether two Grok runs can sit together (the rule dates from 09-24 R17; UNPROVEN) | hours per day while one house is up |

Not cut: build, check pass 1, pass 2 when open or mandatory, the gate for a stacked set, the judge seat. They are the floor (L67, L68) and none caused a stop.

## B STRIKE OR MERGE
Targets: desk start read about 33 KB → about 12 KB · checklist 127 lines → about 25 · NOW 5,968 characters → its 1,500 cap (L58). His 09-30 R45 already rules that rules contradicting the new process change as a set.

| # | item | action | why |
|---|---|---|---|
| 1 | L78 · L77 · L73 ¶1 · CT "never re-ask" · CT R127 line · CT Replies "grep before an A/B" · CL L17 last clause · CL K19a "never ask for a go" · preferences R160 line · NOW "he rules only" | MERGE into L78: one ask law with the seven classes; the rest link to it | ten homes of one rule; 10-02 R11 broke all ten |
| 2 | L61 "a classifier refusal of the bare launch is retried once citing that row, then reported, never worked around" · the same sentence in CL K19a | STRIKE | desk-added 10-01 06:07 against 09-30 R76; it restates the R110 / R112 rule he struck (10-02 R13) |
| 3 | L61 "Interim approval: L7." | STRIKE | dead pointer: L7 is shadow-mode promotion |
| 4 | L60 · L61 · L62 · L63 · L71 | MERGE into one law, Unattended launch | five laws, one mechanism; the launcher and the fixed files enforce all five |
| 5 | L51 three deploy pre-approvals | STRIKE | the standing list names every production string (L62) |
| 6 | L43 · L66 | MERGE into one deploy-window law | one window; `DEPLOY-HUB.md` P1 and STEP-4 enforce it |
| 7 | L58 "applied by the desk at the ruling" | AMEND: folds at the close (FOR DEJAN 7) | six classifier refusals on fold edits (09-29 R16, R17; 09-30 R64, R65; 10-01 R38; 10-02 R12) |
| 8 | L59 "the desk reads Preamble and Index at start" | AMEND: a desk card, the process laws one line each | the Index is 78 lines; on 09-30 the desk's rows cited eight |
| 9 | L67 | SLIM to the floor, the seat order, the override | the procedure has one home, `CHECK-HUB.md` |
| 10 | L13 "rule, paste, glance" | STRIKE "paste" | CT: he pastes nothing |
| 11 | CL `## launch` ids L1–L17 | RENAME or strike | they collide with LAWS, where `L<n>` always means a law: desk rows cite L11, L12, L15 meaning the checklist (10-02 §0; 10-01 §5); LAWS L12 is retired, L15 is external code |
| 12 | "one bare command": CT R16 line · CT R17 line · NOW allow-list line · CL H6 · CL C1, C5 · CL L1 · WU STEP 0.6 · preferences R160 · UL §2 · UNATTENDED RULES of four hub files | MERGE into the guard (E 1) plus one line | a dozen homes; broken daily (10-01 R44); a hook enforces it at no read cost |
| 13 | refresh limits: CT · CL H1, H1a · NOW (twice) · WU | ONE home, WU; guard `02` enforces | five copies |
| 14 | CT "growth over 10% … explained and tuned" · WU READ 7 | STRIKE the analysis; a script appends the number | each log row is 500–1,500 characters; it produced two asks (09-29 R117, 10-02 R27) |
| 15 | CT line 1 "plans, rules, writes prompts and memory … its own prompts too" | REWRITE to THE STANDARD 11 | it licenses the one-offs of F |
| 16 | CL `## handover` H2, H2a, H3–H7, REFRESH HOW, LAUNCH denied | STRIKE when `desk-handover.sh` lands (E 23) | nine rules run 4–5 times a day by hand; H7 already says DONE |
| 17 | CL L2, L4, L5, L11, L14, L16 now · L3, L7, L7a, L8, L10, L12, L13, L15 when E 7 lands | STRIKE | stale (L4's `acceptEdits` contradicts the `dontAsk` files; L5 is `BUILD-HUB.md`) or enforced by the launcher |
| 18 | CL W1, W2, W5, W6, W7, W9 · W8 | STRIKE when E 8 and E 18 land; W3 links to UL §3 | the watch script holds them |
| 19 | CL C1, C3, C5, C6 | STRIKE; keep C2 as one line | the hook does C6; `desk-commit.sh` the rest |
| 20 | CL P4, P6, P8, P9 | STRIKE | P4 is L78; P8 speaks of rounds a build check no longer has |
| 21 | CL K2, K6, K11, K13, K16, K18, K19, K19a, K23, K24, K25 and the four struck lines K4, K14, K17, K22 | STRIKE; K20, K21 move to `DEPLOY-HUB.md` P1 | each lives in a fixed file or becomes a launcher refusal |
| 22 | NOW: 20 of 25 lines (GOAL, he-rules, successor model, REFRESH twice, allow list, finished hub, cwd, K25, hook, low-water, fixed-file history, MORNING, stage-copy, TOMORROW, DAILY STOP, REFRESH lessons, R71, NEXT, voice, OWED) | STRIKE; OWED → `BACKLOG.md`. KEEP sprint, LIVE, meter, sittings, a pointer to today's §5 | each is in the contract, a fixed file, §5 or the backlog; NOW is four times its cap |
| 23 | WU STEP 0 and READ 1–8 | SHRINK to one `desk-wake.sh` call plus the plate; PROFILE leaves the start set | 15–25 calls per wake-up |
| 24 | UL §5 "an allow rule beats the classifier for a bare command" | AMEND with the interpreter caveat | `brain-install-help-2026-09-30.md` F2: a `python3` allow did not decide |
| 25 | the `COBALT_ENV=dev uv run python <script>` string of 10-02 R14 | RETIRE with card `11` | `uv run python` is in the standing list's NEVER block |
| 26 | `desk-launch.sh` line 2 "DRAFT — NOT INSTALLED" | FIX in the next card that edits it | it is the live launcher since 09-30 |

## C TOKENS
Context figures are a session's size at its end (`desk-context.sh`), not its spend. Every turn re-reads the session, so spend ≈ turns × size. The count of turns is the first-order cost, for the desk and for every worker; scripts cut turns.

| # | where | measured | cut |
|---|---|---|---|
| 1 | desk turns | about 60 desk commits on 10-01, 23 on 10-02 by 06:57 (`git log`); each event is 3–7 calls (row Edit, add, commit, launch, watch, tab, view), each a turn at 60–250K | one script call per event (E 7, E 17, E 18); `job-run.sh` removes the stage turns |
| 2 | desk wake-ups | 58,834–66,229 tokens each on 10-01 and 10-02, 4–5 a day (`desk-wakeup-log.md`); the harness first turn is 32–36K of it | `desk-wake.sh`; the desk card (−8.8 KB); NOW at its cap (−4.5 KB); WU 10.2 → about 5 KB. About 6K tokens per wake-up (estimate) |
| 3 | wake-up analysis rows | 500–1,500 characters each | the number only (B 14) |
| 4 | worker turns | build 134K–644K · check 145K–545K per pass · deploy 383K · deploy drafter 185K · judge 48–66K (`job-stats-2026-09-30.md`); a deploy is about 150 single-command turns (estimate from its report tables) | step scripts: AUTHORIZATION, PREFLIGHT, W and STEP-0 go from about 100 turns to 4, each returning about 10 lines |
| 5 | fixed files, read by every worker | BUILD 30.8 KB · CHECK 38.7 KB · DEPLOY 55.3 KB · CARD 12.6 KB | command text moves into scripts; about 8, 14 and 15 KB (estimate) |
| 6 | relaunches | `04` check: four sessions for one check (10-01 R28, R30, R49; 10-02 R25); the 10-02 deploy: 25 min of gate, then FAILED on the environment; 09-30: eight launches of one deploy | launcher pre-checks (E 7), slot guard (E 6), `stage-set.sh` (E 9) |
| 7 | drafter sessions | one per deploy card | `deploy-card.sh` |
| 8 | folds inside an order | 10-02 R27–R29 | the close |
| 9 | watches | one notice = one full desk turn; one per hub today | keep; `job-run.sh` cuts notices to FAILED and READY |

## D UNATTENDED
Rows 1–11 stop for him; rows 12–20 are a worker waiting for the desk.

| # | stop | cause, rows, cost | removal | L78 |
|---|---|---|---|---|
| 1 | launch word per card | CL L7a; 10-01 R9 → R10 | the order's row is the approval | sentence 1: the order approves every covered step |
| 2 | new permission string | L62 "asked for by itself": 10-01 R36 → R37 (cp) · R58 → 10-02 R9 (`--add-dir`, 6 h 10 min) · 10-02 R11 → R14 · R26 | approve by CLASS once (FOR DEJAN 3); a string inside a class is used and recorded | strings known at the start ride the one list; inside a class no ask exists |
| 3 | held finding or fence question | `04` A1 asked 22:40 (10-01 R50), `07` G1 (R57 → R59): answered 05:59; `04` and `07` missed the night deploy (10-02 R1) | the judge seat answers (FOR DEJAN 5); `CHECK-HUB.md` `## 7` (ii) exempts the L42 classification home as it does `jobs.yaml`; the ops glob rule ends the `OPS_TOOLS` lift | last sentence: the desk decides on the order's direction (10-01 R41) and records |
| 4 | an A/B that offers a ruled side | 10-02 R11's B (deploy at 20:00) against R10 | an ask names its class or is not sent | with L77: never sent |
| 5 | asks that do not block | 10-02 R26 (a later card's allow list), R27 (low-water) | held to DONE or the close | sentence 3 |
| 6 | work with no route | dev DB repair: 02:25 → 06:34, three asks (10-02 R11, R14, R16 / R18) · settings change: 10-01 R23, open over 22 h · card close: 10-01 R24, he ran the commands | `devfix` (E 4, E 5), self-heal (E 6), `settings` kind (FOR DEJAN 1) | a step with a route needs no ask; a gap reaches him once, its route card filed the same turn |
| 7 | classifier refusal of a desk action | compound commands (7 of 8 refusals on 09-30 / 10-01; 09-30 22:45 → 06:00, 7 h 15 min) and desk edits of rule files, prompts, settings (B 7's rows; 10-02 R13) | the guard and the resend line (E 1); the desk stops writing those files (F); folds at the close | "failed by the approved commands" = the BARE shape failed twice |
| 8 | mandatory house B, one house up | L67: waits unless he overrules per case; 10-01 R59 | `house-probe.sh` at the order's start; the overrule rides the one list | sentence 2 |
| 9 | window | 10-02 R6 → R10 | his dated order is the per-case override (L73 ¶3); the card cites it | no ask; today see §0 line 5 |
| 10 | push | L55: his word or the close; no close since 09-27 | the close by timer (FOR DEJAN 8) | no ask |
| 11 | night | open items drop jobs at the cutoff (10-02 R1) | rows 3 and 6 | — |
| 12 | `FAILED: W`, lock held | 09-30 R79 (16 min) · 10-01 R46 · builds not launched while the lock is held | card `07` (ready at `aeefb6df`, 10-02 R8, R9; not deployed) | — |
| 13 | FAILED AUTHORIZATION or PREFLIGHT on a desk omission | row not APPROVED (10-01 R9) · check reports uncommitted (10-01 R6) · docs-only head vs code tip (`deploy-2026-10-01-1.md` DECISIONS 1) · unclassified path (10-01 R11) | the launcher runs the same proofs before it starts a session and prints the fix (E 7) | — |
| 14 | silence between stages | `04` BUILT 10:10 → check 17:22 (7 h 12 min; no row gives the cause) · `02` pass 1 done by 17:22 (R28), PASS-2 22:38 (R51) · 09-30 watch regex, 71 min · a watch killed by the 30-min default (CL W9 (2)) | `desk-watch.sh` (E 8), `job-run.sh` (E 21) | — |
| 15 | house file staging | `04` check 17:32 → 21:38 (4 h 06 min, the last hour behind the one house lane); asks R29, R36 / R37, R39 | `stage-set.sh` (E 9) | — |
| 16 | house out or harness | 10-01 R36 (no house A), R59; six seats lost by launching on 09-28 / 09-29 | `house-probe.sh` with a real answer probe (E 14) | — |
| 17 | dev DB state | stray rows: 09-28 R182, 09-29 R52 (2 h 21 min) · level not 0013 · slots (10-02 R5, at minute 25 of a gate) | self-heal inside the lock take (E 5, E 6) | — |
| 18 | failed gate | a new card and new gate names per attempt (10-01, `44e676e8`); cleanup owed (L46) | `gate-clean.sh`, `RECUT` (E 7, E 19) | — |
| 19 | set conflict found at the deploy | `02` × `07` both edit `OPS_TOOLS` (10-01 R57, open); STEP-T resolves no conflict, so tonight's set fails there without a seam card | `deploy-card.sh` trial-merges at card time and names the seam card (E 16) | — |
| 20 | fixed-file line change, install | 09-30 R63 → R66 (58 min, a brain) · 10-01 R38 → R39 | `install-fixed.sh` (E 20) | — |

## E SCRIPTS
Priority 1 = this week first. Every script lives in `ops/desk/` and is called at the repo path, as `stage-copy.sh` is today: no symlink, no hand install, and a worker always runs the checked copy on `main`. One glob rule classifies `ops/desk/**` as operator scripts, so a new script changes no `src/` file and restarts nothing. Each card is built and checked like any feature (L67); scripts are tested with a dry-run flag and a stub `claude` (the shape of `tests/ops/`).

| # | script | what it does | stop removed | cost of that stop | pri |
|---|---|---|---|---|---|
| 1 | `bare-guard` (PreToolUse hook; his install) | blocks a Bash call that holds a chain operator, a pipe, a redirect, a newline or a command substitution OUTSIDE quotes; says NOT A REFUSAL, resend one per call (10-01 R45 part 1). Quote-aware: the `<FP>` query carries the SQL concat operator inside its string | D 7 | 7 h 15 min (09-30 22:45); the re-runs of 10-01 R44 | 1 |
| 2 | `take-devdb-lock.sh`, `release-devdb-lock.sh` (card `07`, checked) | atomic lock, waits, releases | D 12 | 16 min + queued builds | 1, tonight |
| 3 | desk-size guard (card `02`, checked) | launch refused at 300,000 | late refreshes (490,829 on 10-01) | tokens | 1, tonight |
| 4 | `cobalt db dev-rebuild` (card `11`, drafted) | rebuilds one dev table in one transaction, digest-proven | D 6, D 17 | 4 h 09 min (10-02) | 1 |
| 5 | `devfix` kind + `DEVFIX-HUB.md` (card `12`, drafted) — widen to a closed verb list: `dev-rebuild`, `dev-clean` (the constructed-ticker rows a suite left), `dev-level` (back to 0013) | a dev repair launches from a card | D 6, D 17 | 2 h 21 min (09-29 R52) | 1 |
| 6 | slot guard (card `13`, drafted) + SELF-HEAL: at the guard's exit the hub runs `dev-rebuild` inside its own lock take and goes on (needs class (b), FOR DEJAN 3) | no gate dies on slots; no devfix job for it | D 17 | 25 min of gate and the night deploy (10-02 R5) | 1 |
| 7 | `desk-launch.sh` pre-checks: every `RULINGS` row APPROVED and committed; check reports committed and clean; head vs code tip (docs-only accepted); RESTARTS class home of each card file; prints the fix. Plus `RECUT` for a failed gate, the row + commit + tab in the same call, the watch line printed, the header fixed | refuses before a session starts | D 13, D 18 | a relaunch each (10-01 R6, R9, R11) | 1 |
| 8 | `desk-watch.sh <kind> <card>` | derives the report path, the stop regex and the ceiling; explicit timeout; on timeout prints LIST and the last line | D 14 | 71 min (09-30); up to 7 h 12 min (10-01) | 1 |
| 9 | `stage-set.sh <card>` | stages the card, the report, the diff and every file the diff touches for a confined house in one call, from git at the tip, `cmp`-proven | D 15 | 4 h 06 min | 1 |
| 10 | close timer (launchd; his install) | starts `desk-launch.sh close <date>` at 21:05, hourly while a deploy hub is live | D 10 | four nights with no close (09-28 … 10-01); NOW at four times its cap | 1 |
| 11 | `gate.sh <worktree>` | W whole: lock, `<FP>`, level, pass 1, forward, pass 2, stray-row read, rollback, `<FP>`, release; a `trap` releases the lock at every exit; prints the three suite lines and a log path; the pass lists in one file | typed pass commands; TREE STATE (A 7) | about 30 worker turns per run, three runs per feature | 2 |
| 12 | `authorize.sh <kind> <card>` | the AUTHORIZATION block as one table | A 4 | 6–8 turns per session | 2 |
| 13 | `preflight.sh <kind> <card>` | the PREFLIGHT rows as one table | A 4 | 15–25 turns per session | 2 |
| 14 | `house-probe.sh` | a one-word answer probe per house; UP or OUT with its return time | D 8, D 16 | a failed check launch each (10-01 R36, R59) | 2 |
| 15 | `card-fill.sh <card>` | fills `TIP`, `CHECK REPORT`, `HOUSE B` from the build's stop line; commits | D 14 | cards filled 16:27 for builds done by 10:10 (10-01) | 2 |
| 16 | `deploy-card.sh <job> …` | assembles the deploy card; trial merge; migrations and RESTARTS from git | D 19; A 3 | a drafter session; a STEP-T failure | 2 |
| 17 | `desk-row.sh`, `desk-commit.sh` | next R number, time from `date`, the 300-character check, the day file; bare add and commit | wrong row times (10-01 R9, R16, R17); a ruling with no row (10-02 R13) | — | 2 |
| 18 | `desk-done.sh <id> <tab>` | verifies the stop line, stops, removes, closes the tab | orphan tabs (10-02 R17; 09-29 R7, 39 tabs) | his cleanup asks | 2 |
| 19 | `gate-clean.sh <job>`, `job-clean.sh <job>` | removes a failed gate's worktree and branch (refuses when `main` holds it or a deploy tag names it); after DEPLOYED removes the job worktree and its merged branch | D 18; the L46 debts (five worktrees, `deploy-1001-1`) | new gate names per attempt | 2 |
| 20 | `install-fixed.sh <file> <row>` | proves his row, replaces the `«INSTALL` token, proves none left, commits | D 20 | 58 min (09-30) | 2 |
| 21 | `job-run.sh <card>` | detached runner with a state file: build → verify → fill → check → PASS-2 → READY; launches through `desk-launch.sh`; wakes the desk on FAILED, `for Dejan > 0`, READY | D 14; A 2 | 7 h 12 min (10-01) | 3 |
| 22 | `deploy-step0.sh`, `deploy-outage.sh`, `deploy-smoke.sh` | STEP-0 as one table; the outage as one script whose `trap` brings residents up; the smoke rows. Needs the other-house read of `DEPLOY-HUB.md` (L67) | a session stopped inside the outage (09-30, 11 min down) | about 45 turns per deploy | 3 |
| 23 | `order-open.sh`, `desk-wake.sh`, `desk-handover.sh` | the one list's facts; the wake-up state in one output; the successor ends the predecessor | C 2; B 16, B 23 | 15–25 calls per wake-up | 3 |
| 24 | `settings` kind | a ruled production setting applied from a card | D 6 | open since 10-01 08:58 | on FOR DEJAN 1 |

Cards: tonight rows 2, 3 (after a seam card for `OPS_TOOLS`) · S2 dev DB = rows 4–6 (cards `11`–`13` as drafted, plus `dev-clean`, `dev-level`, self-heal) · S1 desk tools = rows 7, 8, 15, 17, 18, 20 · S3 worker steps = rows 9, 11–14 · S4 deploy = rows 16, 19, 22 · S5 runner and desk start = rows 21, 23 · row 24 on his word · his installs: rows 1, 10. Already standard and kept: `stage-copy.sh`, `wait-stop-line.sh`, `desk-context.sh`, the relaunch form `desk-launch.sh <kind> <card> <step>`.

## F CORNER CASES
His question: was the desk doing one-offs itself, or does the process miss a route? Class: `G` = no route existed · `D` = the desk did work that is a worker's, or broke a rule that existed · `OK` = a lawful one-off. Of 23: 2 lawful, 9 with a missing route (3 of them then built by the desk by hand), 11 desk work or slips, 1 record gap.

| # | when | what | who did the work | class, why | removed by |
|---|---|---|---|---|---|
| 1 | 10-01 06:03 (`12b7bc66`, `44e676e8`) | committed the two check reports late; re-cut the deploy card with new gate names | desk | D+G: K19a wants them committed first; no re-cut route | E 7 |
| 2 | 10-01 06:07 (R2) | wrote law text into L61 and K19a | desk | D: text he had not worded (09-30 R76) | B 2; FOR DEJAN 7 |
| 3 | 10-01 06:19 (R4) | wrote `JUDGE-HUB.md` and `JUDGE-CARD.md` | desk | D: a fixed file is a drafter's work, read by the judgment seat (CL L9) | THE STANDARD 11 |
| 4 | 10-01 07:33 (R9) | launched build `02` before his word | desk | D | D 1 |
| 5 | 10-01 08:00 (R12) | ASET sheet survey, a read-only prompt | worker (Sonnet) | OK | — |
| 6 | 10-01 08:16–08:50 (R16, R20, R22) | production reads of the daily-stop rows | desk | D, small: diagnosis is a survey's work | a survey prompt |
| 7 | 10-01 08:58 (R23) | a worker was to apply stops 420 / 210; the classifier refused the settings write; not applied | nobody | G: the standing list bans `settings load` on every line | FOR DEJAN 1 |
| 8 | 10-01 09:30 (R24, R25) | cards 498–500 closed: a brain wrote the commands, he ran them | he | G: no production data-fix route; the sheet refused pre-C1 cards | card `04`; he is never handed commands (09-29 R160) |
| 9 | 10-01 20:24 (R33) | `mkdir` into a check's scratch, refused; told to `cp` web.py itself (R31) | desk | D, on his order | E 9 |
| 10 | 10-01 20:32–20:35 (R38, R39; `01bfe67f`) | wrote `ops/desk/stage-copy.sh`, edited the `CHECK-HUB.md` launch line and `STANDING-LIST.md` §2, committed on `main` with no build and no check, the copy path untested | desk | D+G: no route for a worker script or a line change; the live desk line lacks the `Edit(ops/**)` deny that standing list §4 names | E 20; FOR DEJAN 4 |
| 11 | 10-01 20:40 (R40) | the design-gap report | desk | D, small | a drafter or the brain |
| 12 | 10-01 22:48 (R53) | typed attach text into a build's pane | desk | D, a slip | E 7 opens the tab |
| 13 | 10-01 23:48 (R57 → R59) | settled `07` G1 by a desk record sent as a message; PASS-2 rejected it | desk | G: `CHECK-HUB.md` has no exemption for the L42 classification home; a judge answer belongs in the card's `## RECORDS` | D 3 |
| 14 | 10-02 02:27 (R6) | no deploy; the dev rebuild named "first job" | desk | G: no route at night | E 4–E 6 |
| 15 | 10-02 06:06 (R11) | an A/B with a ruled side | desk | D | D 4 |
| 16 | 10-02 06:09–06:19 (R12, R14) | wrote prompt `01`, a write-path one-off: allow list, steps, a `uv run python` string | desk | G+D: UL §1.2 makes every write-path launch a fixed file; none existed for a dev repair | E 5 |
| 17 | 10-02 06:20–06:23 (R15, R16, R18, R19) | ran `01` in auto mode (L29 set aside), refused twice by the launcher, then hand-typed `claude --bg` | desk, on his R18 | G | E 5 |
| 18 | 10-02 06:26–06:34 | wrote and ran `rebuild_aset_sizings.py` (722 lines, outside git; three dry runs, two script errors fixed) | worker `cf75cbe2` (Opus 5.5) | G: R14 approved the command path before the file existed; nobody read the script before it wrote DDL | card `11` (a tested command; the script is its reference) |
| 19 | 10-02 06:21 (R17) | closed an orphan tab, stopped a build | desk, his ask | D: clerical, by hand | E 18 |
| 20 | 10-02 06:24 (R20) | the standard-scripts drafter | worker | OK | — |
| 21 | 10-02 06:43 (R26) | added `wc`, `git show`, `git diff` to the devfix line | desk | D, small: an allow line is his or a class's | FOR DEJAN 3 |
| 22 | 10-02 06:44–06:46 (R27–R29) | edited NOW; wrote L78 into LAWS twice | desk | D: lawful today (L58), inside the deadline order | FOR DEJAN 7 |
| 23 | 10-02 06:13 (R13; `f0b05232`) | struck the R110 / R112 line; the §4 row was classifier-refused, so R13 has words and no row | desk | record gap: no gate can prove R13 by row (K23) | E 17 |

The rule that ends class D: the desk writes rows, cards and messages. With no route it files the route card, tells him once if the order is blocked, and never builds the route by hand.

## MERGED
Fate: BUILT · RULED · DONE · IGNORED · OPEN. Then its place in the standard: kept, superseded or dropped.

| source | recommendation | fate | now |
|---|---|---|---|
| desk review 09-30, 1 | outage-proof deploy prompts | BUILT (`DEPLOY-HUB.md` rules A, C, E) | kept; steps become scripts (E 22) |
| 2 | never stop a deploy hub past its first bootout; a standing restore prompt | BUILT as rule F and K19; no restore prompt | superseded by `deploy-outage.sh` |
| 3 | no desk work in a gate or production tree | BUILT (C2, the pre-commit guard, K10) | kept; widened to `ops/` and the fixed files |
| 4 | one dialog rule | BUILT (UL §3, `dontAsk`) | kept, done |
| 5 | authorization by row + commit | BUILT (K23) | kept; the launcher runs it too (E 7) |
| 6 | his words, the fold, the owed closes | PARTLY: words files kept; no close since 09-27 | superseded: timer, folds at the close |
| 7 | §5 one row per live session | BUILT | kept; written by script (E 17) |
| 8 | cut the read paths | PARTLY: the workers' cut BUILT (L59); the desk's three cuts IGNORED (WU 10,228 B, NOW 5,968 characters, the Index still read) | kept (B 8, B 22, B 23) |
| 9 | whole prompts, one template per kind | BUILT (four fixed files, `CARD.md`) | kept; the files now shrink |
| 10 | refresh policy on numbers | RULED (09-30 R56, 10-01 R8); guard `02` checked, not deployed | kept |
| RULED PROCESS 1–9 | fixed files, launcher, hook, standing list, desk line | BUILT, installed 09-30; the live desk line lacks the `ops/` deny | kept; FOR DEJAN 4 |
| RULED close | the nightly close runs itself | BUILT (`CLOSE-HUB.md`), never run | kept; timer |
| RULED refresh | 250,000 / 400,000 | replaced by 10-01 R8 | superseded |
| install help 09-30 | the install route (git mv, checkout, one Edit) | DONE (09-30 R66) | superseded by E 20 |
| | commit his `settings.json` edits | RULED yes (R67); the file is modified again today and a `.bak` sits beside it (git status) | OPEN: one checkout would strip the desk's allows |
| | `rules.yaml` out of desk commits | still modified in the tree | OPEN, small |
| | two scratch proofs; the ≥196 B cut | DONE (R68) | done |
| | the prefix-matching line for him | NOT TOLD | superseded: the exact production strings leave the lines with E 22; told here: an allow with no `*` also admits trailing arguments to the same command |
| | launcher header, `desk-list.sh` untracked, UL caveat | OPEN | kept (B 24, B 26, E 7) |
| workflow review 10-01, 1 | bare launches only | RULED (R44), still broken | superseded by the guard (E 1) |
| 2 | refusal: one bare retry, then a brain, never an A/B | folded (K19a); R110 / R112 struck 10-02 R13 | kept, inside L78 (B 1) |
| 3 | MEASURE each turn, refresh | RULED (R8) | kept |
| 4 | watch the fixed file's stop line | folded (W9) | superseded by E 8 |
| 5 | commit check reports at CHECK DONE | folded (K19a) | superseded by E 7, E 21 |
| 6 | run the missed close | IGNORED | timer |
| 7 | tell him X5, file its fix card | NOT DONE | FOR DEJAN 11 |
| 8 | the prefix-widening line | NOT TOLD | as above |
| 9 | keep or strike the desk-added L61 sentence; the UL caveat | half ruled (10-02 R13) | B 2, B 24 |
| 10 | the auto-mode prose setting | UNRULED, unverified | dropped: the bare deploy launch ran unrefused (10-02 R4) |
| parallel builds 10-01, A | lock at the step, amended L76, two strings | RULED (R20); built and checked (`07`); not deployed | kept; tonight |
| A | a scratch DB per build | deferred to an ADR | kept deferred |
| B | L7a | RULED, folded | superseded by E 7 |
| B | re-arm after CONTINUE; `date` every time | folded (W9) | superseded by E 8, E 17 |
| B | stats `waits` column | OWED | kept: the `job-run.sh` state file gives the times |
| close cards 10-01 | commands for him to run | USED (R25) | dropped as a pattern (09-29 R160); the route is card `04` |
| design gap 10-01 | G1 worker step scripts | RULED A (R41); today's drafter made the dev DB cards instead | kept: cards S3, S4 |
| | G2, G3 | checked, not deployed | tonight |
| | G4 close · G5 standing `BRAIN-HUB.md` · G7 other-house desk verbs | never run · parked (R5); this is the fifth one-off brain prompt · later | timer · FOR DEJAN 13 · later |
| words 10-01 R45 | part 1 guard · part 2 resend line · part 3 `--append-system-prompt` | UNRULED | kept, all three: the guard quote-aware; the line's home is L78; the flag also on the fixed files' lines (FOR DEJAN 2) |
| scripts draft 10-02 | cards `11`–`13`; its DECISIONS 4, 5, 6 | drafted, uncommitted rows R23 | merged: E 4–E 6; 4 kept with self-heal; 5 → E 19; 6 → E 7 |

## FOR DEJAN
One list. Each is his: scope, dates, money or permission strings.

1. MONEY, open since 10-01 08:58. Production holds daily stop full 210 / half 420, swapped (10-01 R15, R22). He said yes to the fix (R23); no route may write a setting. A: approve a `settings` kind: one card with the keys, the values and his row; two production strings (the settings load, dry-run and real); it runs after 21:00 (L66). B: he enters 420 / 210 in the sheet's change line. Recommend A. A cannot land before tonight, so B is the only way to the right stop before today's open.
2. The bare-command fix (10-01 R45). A: all three parts: the hook in his settings, the system-prompt flag on the desk line and the fixed files' lines, the resend line in L78. B: practice only. Recommend A.
3. Permission by class, once. A: (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` in his settings and on every line, for scripts that landed through build, check and deploy; (b) `Bash(COBALT_ENV=dev uv run cobalt db *)` on the build, check, devfix and deploy lines, with `Bash(COBALT_ENV=production*)` denied on the first three; (c) each kind's own report glob. B: string by string, as today. Recommend A. What A trusts: the check of each script; any dev `cobalt db` verb, never production.
4. Desk deny strings (they only narrow). A: add `Edit(//Users/cobalt/cobalt/ops/**)` (in standing list §4, missing on the live line) and the fixed files (`prompts/*-HUB.md`, `CARD.md`, `STANDING-LIST.md`, `UNATTENDED-LAUNCH.md`). B: leave. Recommend A, once `install-fixed.sh` has landed.
5. What reaches him under an order. A: the judge seat answers a held finding or a fence question that stays inside the ordered feature; work goes on; he reads the list at DONE and may veto; notes, money, sizing and growth beyond the feature still wait for him. B: each comes to him (10-01: up to 7 h 19 min; he answered A to all three, and A was the desk's recommendation on D2 and G1). Recommend A.
6. The STRIKE OR MERGE table. A: one yes for the set, applied at the next close. B: row by row. Recommend A.
7. Folds. A: at the nightly close only; a row binds from the moment it is written; the day's standing rulings sit in §5, one line each. B: at the ruling, as today. Recommend A. It reverses my 09-30 line "applied at the ruling".
8. The close. A: a launchd timer starts it nightly (his install). B: the desk remembers. Recommend A: four nights missed.
9. The gate on a checked tree (L68). A: a single-branch set whose code equals its checked tip takes the check's suite lines; the deploy runs RESTARTS, validate and the outage. B: always re-run (about 25 min). Recommend A. What A gives up: the gate also caught the broken dev DB on 10-02; the slot guard covers that case.
10. Ops-only sets (L43, L66). A: a set with an empty restart set and no migration (scripts, tests, docs) deploys at any hour, no outage. B: one event per evening, as today. Recommend A: the script cards then land in days. It needs the `ops/desk/**` glob rule first.
11. X5, a fact owed since 09-30: a tap that commits while a refresh waits on the row lock is overwritten. It predates F15 P1 and is live (`f15-p1-decisions-2026-09-30.md`). A: a fix card now. B: backlog. Recommend A: it loses his input silently.
12. Dates. A: the script cards run in parallel lanes beside the ladder, priority 1 first; they share no `src/` with K3 (L72). B: scripts wait for S3 (stop 10-07, AT RISK). Recommend A.
13. A standing `BRAIN-HUB.md` (parked, 10-01 R5). A: drafted with card S1. B: one-off prompts, as today. Recommend A.

BRAIN DONE — report /Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-unattended-2026-10-02.md
