# BRAIN — desk review 2026-09-30 (startup, worker reads, design / development / deployment)

Seat `brain`, Opus 5.5, read-only. Written 09:1x ET from the files named in `prompts/2026-09-30/46-brain-desk-review.md`. `M` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory` · `D` = `/Users/cobalt/cobalt/docs/40 - DevDocs` · `cto-<dd>` = `D/reports/cto-2026-09-<dd>.md` · `words-<dd>` = its words appendix · `44` = `D/prompts/2026-09-30/44-deploy-1-drc-0930.md` · `dep` = `D/reports/deploy-2026-09-30-1.md` · `att<n>` = `D/reports/deploy-2026-09-30-1-attempt<n>.md`. A cite is `file:line` or a row.

## §0 Headline
- He asked for both deploys before 09:30 (`words-30:9`). Deploy 1 merged on the eighth launch of `44` (residents up 09:11:56, smoke in flight at 09:14; `dep` `## CONTINUE`); deploy 2 is not launched. Attempt 5 left aset, radar and the agent down ≈11 min (`cto-30` R22). Every failure was a check or command nobody ran before launch, or a rule the desk already held (checklist K19, C2; `UNATTENDED-LAUNCH.md:19`).
- On 09-30 the desk broke its own contract five ways: commits on main while a deploy ran, three hand commits into the gate tree, the L67 deploy read dropped with no override row, his words not recorded, a standing ruling not marked for fold.
- Startup is no longer the cost: the desk's start files are 32,979 B of a 53,100-token wake-up. The cost is 34 wake-ups in 54 hours (2.26M tokens) and what workers are sent to read (a one-row fix build: over 100 KB of prompts and law).
- Five contradictions need his ruling (dialog rule, short rows vs gate literals, refresh cap vs refresh line, standing override vs L73, packets).
- Ten recommendations, ranked, at the end.

## HIS DIRECTIONS
Start point: the last ruling in `words-29` is `## R171`, 21:55 ET (`words-29:103-105`). Forward through 09-30, then back.

| time | his words | the desk must | followed? | evidence |
|---|---|---|---|---|
| 09-29 21:55 R171 | "record that next CTO desk starts as Sonnet 5.5. I will ask it to start Fable or Opus tab as Brain if it needs higher level reasoning" | next desk on Sonnet 5.5; a brain tab only on his ask | YES. One gap: `cto-30` R23 says "his ask, words below"; `words-30` has no `## R23` (it ends at `## R13`, `:20`) | `D/reports/desk-wakeup-log.md:43`; `D/prompts/CTO-DESK-WAKEUP.md:12`; `cto-30:30` |
| 09-30 06:09 R4 | "I want both deployed this morning before 9:30 and fix started for the issue right after both deployed" | both deploys by 09:30; E1 fix next | NOT MET for both: at 09:14 deploy 1 is merged with its smoke in flight; deploy 2 is "not launched" and its gate takes ≈26 min. E1 fix "not drafted" though a draft blocks nothing (L72) | `words-30:9`; `dep` `## CONTINUE` (read 09:14); `cto-30:41-42`; `att3:174` |
| 09-30 06:40 R9 | "You will follow this protocol as stated. That is what we wanted." + how to cancel the 9:30 block | AMBIGUOUS RECORD. The block does not say which protocol or what the desk had asked. Row R9 records "two deploys one by one, existing generic list, no new strings" — none of it his words — and every gate of `42` and `44` greps that row | not verifiable from the record. §5 still lists R8's two strings as OPEN TO HIM after R9 closed them | `words-30:11-14`; `cto-30:17`, `:44`; `44:29` |
| 09-30 06:43 R10 | "I don't want 9:30 L66/L43 to stop any deployments in the future until I say production is usable for trading" | a standing override, folded | PARTLY. In `44:1`. Status is `APPROVED`, not `APPROVED — pending fold`, so the wake-up reconcile grep never finds it. NOW still says "before 09:30" and "hard stop `FAILED: window` at 09:15", and every worker reads NOW. CONTRADICTS L73: "A standing or blanket permission to skip steps does not exist" | `cto-30:18`; `CTO-DESK-WAKEUP.md:33`; `M/areas/cobalt.md:26-27`; `M/LAWS.md:363` |
| 09-30 06:55 R13 | "Both are accepted and not risk just run like these were not a problem" | run the two gates in series, restart in a scan session | YES | `cto-30:21-22` |
| 09-29 05:43 R9 | "close a tab as soon as it's done working its job. And you have checked that it's done." | stop + rm + tab close, same turn | 09-29 YES (rows cite W8). 09-30: §5 says drafter `01` "stop + rm + close `w2:tE7` pending"; the TABS row says `w2:tE7` closed. One row is false | `cto-30:37`, `:46` |
| 09-29 05:57 R16 | "I don't want ever to hear I could not read and I stopped" | a second try another way before he hears of it | BROKEN three times after it: R125 "classifier refused the checklist … read … — to Dejan" (no second try named); R157 "not retried → to him"; wake-up 14:59 "refused … and not retried" | `cto-29:134`, `:166`; `desk-wakeup-log.md:36` |
| 09-29 06:0x R17 | "first check the list of commands and then devise a plan" | plan from the allow list | BROKEN 09-30: `44`'s listed `rm /Users/cobalt/Library/LaunchAgents/…` sat outside `--add-dir` (R21). Same class 09-29 R19, R108. The rule existed (checklist K19, last clause) | `cto-30:29`; `cto-29:27`, `:116`; `M/topics/cto-desk-checklist.md:106` |
| 09-29 12:08 R68 | "never restart below 220,000 tokens … if you're above 250 you need to restart on a first … quiet moment" | refresh floor 220K | YES: 226K, 226K, 228,573, 228,894, 237,581, 221,759, 232,909; 09-30 243,475 | `cto-29` R78, R89, R102, R114, R123, R138, R156; `cto-30:14` |
| 09-29 18:34 R127 | "And A" (he rules only scope, dates, deploys, money; refresh at most twice a day) | no A/B on a ruled law; ≤2 refreshes | refresh YES. A/B BROKEN once (R157 → his R160). CONTRADICTS R68's "above 250 … restart": the desk grew "≈170K in 22–48 min" (R161), so two refreshes cover about two hours of a day; the contract marks its merge of the two "(desk reading)" | `cto-29:136`, `:170`; `M/topics/cto-desk-contract.md:20` |
| 09-29 19:21 R129 | "tribunal can finish in one to 2 rounds … you pick tools and commands that work and save tokens and wasted rounds" | first builds that pass; no wasted launches | NOT MET: C4 took three rounds and ended HOLD 1; deploy 1 took eight launches | `cto-30:9`; `cto-30` R15–R23 |
| 09-29 20:50 R160 | "you shouldn't be running compound commands … I don't see you telling me anymore how many tokens was the startup" | bare commands; startup tokens on the plate | rule folded (`M/preferences.md:11`; wake-up `:22`, `:38`). Plate text is not on file: UNPROVEN | — |
| 09-29 21:0x, 21:3x | (row R165 "his 21:0x question"; row R167 "his 21:3x message — the process burns credits, three features undeployed") | his words verbatim, the same turn | BROKEN: `words-29` goes from `## R160` to `## R169`; neither message is there | `cto-29:174`, `:176`; checklist `:22` |
| 09-29 21:49 R169 | "let's see if we can do this check and deploy tonight. Without any more delays." | check `38`, then deploy, that night | NOT MET: `38` FAILED at AUTHORIZATION 21:42 — row R168 "lacked three literals"; relaunch row at 23:41; no deploy that night | `cto-29:183`, `:182` |
| 09-28 11:23–11:26 R54 / R55 | "whatever it's being written, it's very easy to understand … but much, much smaller" | short rows, detail in the linked report | PARTLY. 09-28 cut by a hub (142 rows). 09-29 R1–R131 never cut: "09-29 is cut after its close", and the close was not run; the file is 75,829 B. 09-30: three "row trimmed" commits after the row was committed (`6a5e4287`, `faad5ed6`, `4fd3fc24`) | `cto-29:146`; `cto-30:45` |
| 09-28 11:00 R49 | "ask me in a very short five sentences max" | replies ≤5 sentences | replies are not on file: UNPROVEN. Contrary text still live: "≤10 lines", "under ten sentences", "replies ≤10 lines" | `M/topics/working-contract.md:9`, `:45`; `M/topics/cto-desk.md:16` |
| 09-27 22:17 R42 | "why is this not a set of files and a tribunal instructions as another file" | no staged packet, no pre-measured ceiling | BROKEN in the window: three check launches died on a packet byte ceiling, and K17 still prescribes one | `cto-28:162`; `cto-29:50`, `:58`; checklist `:104`; `cto-desk.md:160` |

## STARTUP
What the wake-up orders at start (`CTO-DESK-WAKEUP.md:29`), measured with `wc -c` and `grep -b`:

| file | bytes | note |
|---|---|---|
| `CTO-DESK-WAKEUP.md` | 10,146 | 7,430 B when applied 09-28 (`cto-28:27`); +37% in two days of incident patches |
| `M/areas/cobalt.md` to `## Build rules` | 5,617 | NOW alone is 3,760 B; L58 caps it at "at most 1,500 characters" (`LAWS.md:305`) |
| `M/preferences.md` + `M/profile.md` | 1,817 | profile (age, town, family) drives nothing in the first turn |
| `M/LAWS.md` to `## Reading` | 9,396 | the Index is 8,848 B, one line for each of 77 laws |
| `M/topics/cto-desk-contract.md` | 6,003 | |
| TOTAL | 32,979 | ≈9K tokens (estimate); plus checklist `## handover` 3,196 B at every handover |

- Measured wake-up: 53,100 tokens on 09-30 (`desk-wakeup-log.md:43`). The harness's own first turn was 31,806–35,863 tokens before any desk read (`:37`, `:38`). The desk's files are under a fifth of a wake-up; the harness is about three fifths; the rest is handover work.
- What the desk used on 09-30: its §4 rows cite eight laws (L11, L35, L39, L43, L62, L66, L68, L73) of the 77 Index lines it read.
- Not read at start: `cto-desk.md` 135,242 B (175 lines; "never cut", contract `:19`), `working-contract.md` 11,517 B, `memory-system.md` 5,315 B, `INDEX.md` 2,128 B.
- 34 wake-ups from 09-28 00:03 to 09-30 06:16: 18 + 15 + 1 rows in the log, 2,255,513 tokens summed. R127's cap ended that on 09-29 18:34.

Redundant (one fact, several homes; `M/topics/writing-rules.md:7` allows one):
- Refresh limits: wake-up `:40`, contract `:20`, checklist `:9`, `cobalt.md:15`, `cto-desk.md:172`.
- Bare `claude stop` / `claude rm`: wake-up `:16`, `:22`; checklist `:15`, `:16`; `preferences.md:11`; `cobalt.md:17`; `cto-desk.md:174`.
- OWED is circular: `cto-30:45` "as 09-29 §5 OWED" → `cto-29:199` "as NOW's OWED line" → `cobalt.md:29`.

Contradictory:
- Contract `:16` "A denied git command → refresh; never ask him." against `:17` (try once another way) and `:20` (never refresh below 220,000).
- `preferences.md:10` "Up to ten rulings per message" against `working-contract.md:16` "he cannot rule on a batch" and his R129.
- `CLAUDE.md` → `cobalt.md:8` "read … INDEX.md once and obey its `## start`" against wake-up `:29` "do not open INDEX".
- `R<n>` means three things: a desk row, checklist `## rulings` R1–R2, checklist `## reads` R2–R7. `LAWS.md:93` requires `<date> R<n>`; NOW cites bare "(R16, R17, R134)", two rows of 09-29 and one of 09-28 (`cobalt.md:17`).

Too terse to apply: the checklist holds 25 K-rules and 17 L-rules, most under fifteen words ("K12 Web agents: budget, data, re-verified", `:98`); their meaning sits in the 135 KB file. The three rules that would have stopped 09-30's failures were on the page (K19 `:106`, C2 `:61`, L7 `:34`) and were not applied.

The three biggest cuts:
1. LAWS Index at start (8,848 B) → a desk card of the laws the desk acts on, about 1.5 KB. Needs L59 amended.
2. Wake-up file 10,146 → about 5 KB: VIEW, WAIT-DESK and STEP 0.2–0.5 move into checklist `## handover`, which every handover already opens; row cites and dated incidents come out.
3. NOW 3,760 → 1,500 B as L58 says: OWED (`cobalt.md:29`) and NEXT (`:27`, stale since 06:40) live in §5 only.
Together ≈14 KB, about 4K tokens, 7% of a wake-up. The larger lever is growth per turn: one launch turn cost +33K (`cto-29:173`).

## WORKERS
Before its own prompt, every Claude worker follows `CLAUDE.md` (126 B) → `cobalt.md` `## Start here` (`:8-9`): NOW, INDEX, preferences, profile, LAWS to `## Reading`, then `## Build rules` down. That is 8,566 + 2,128 + 1,111 + 706 + 9,396 = 21,907 B. Proof they do it: `att1:12` and the seam report `:11` both record a block "appended to the read of `areas/cobalt.md`". NOW is desk state; on 09-30 it told a deploy hub "before 09:30" while `44:1` told it any hour is lawful.

| kind | prompt (bytes) | told to read first | used, by its report |
|---|---|---|---|
| build | `2026-09-29/37` (32,138) — "ONE FIX ROW" (`:9`) | LAWS Preamble + Index, 22 law entries, `writing-rules.md` (2,748), checklist K24–K25; then "`24` whole; `26` whole" (27,158 + 27,656), four sections of `20` (file 31,610), five report sections (`:38-39`). Over 100 KB before any code | the one row (`:27`) and `trade_note.py`. The card already gives each law in one line (`:38`) |
| check | `2026-09-29/38` (19,091) | its procedure is not in it: "`21-s3-exits-c1-check.md`'s blocks of those names bind UNCHANGED with these substitutions" (`:13`), plus `30` §2 (`:14`) and `27`'s copy strings — 19,010 + 19,628 + 14,686 B of older prompts, read with about twelve substitutions held in mind | the three launch-row literals sit inside that sentence (`:13`); row R168 missed them and the launch failed (`cto-29:183`) |
| drafter | `2026-09-30/43` (8,189) | `41` whole (54,761), three sections of the re-issue report, rows R3–R11, LAWS Preamble + Index, 11 entries, `writing-rules.md` (`:18`) | `41`. A mechanical split acts on no law entry |
| deploy | `44` (47,720) | LAWS Preamble + Index, 11 entries; `50` STEP-4→7 (file 116,864); two sections of `deploy-2026-09-27.md` (file 78,682); sections of two build reports; re-issue ESCALATE (`:39-43`) | L42, L62, L66, L68, L70, L74, L76 in its reports. `44:45` is one paragraph of about 2.9 KB, patched after attempts 4, 5, 6 and 7 |
| seam build | `2026-09-30/42` (10,237) | LAWS Preamble + Index, 12 entries, `writing-rules.md`, one report section (`:37`, `:18`) | the right size. It still met nine conflicts the prompt called clean merges (seam report `:42`) |

- L19 is broken by `37` and `38`: "Every Code prompt delivered complete in one block" (`LAWS.md:165`).
- What a worker needs: its prompt, whole; the law lines on its card; an entry opened when it acts on that law. Not the Index (8,848 B), not NOW, not preferences or profile.

## WORKFLOWS
DESIGN — F15, 09-29, one day: proposer `10` 11:37 (R58) → tribunal `12` + seat `13` 12:03 (R64) → derive `14` DRAFT 13:33 (R77) → round-2 hub `17` → derive `19` FINAL 19:57 (R140) → his two rulings 20:14 (R145) → fold → approved 20:24 (R151). Lost: 17:06–19:43 on hub `17`, five launches (R107; R110 a classifier stopped a Write; R112; R113 Astra stdin timeout; R118 Astra METER; R130). Astra was lost twice, to stdin and then to its meter after 32,000 tokens (`cto-29:126`); the stdin fix was on record since 09-21 (`cto-29:121`).

DEVELOPMENT — every chain is drafter → build → check hub → classifier-drafter → fix build → check. 09-29 has 40 prompt files, 15 of them drafters; 09-28 has 61.

| item | check rounds | launches lost, with the row |
|---|---|---|
| S3 C1 (09-28) | 3 (R57 HOLD 2, R72 HOLD 1, R88 YES) | — |
| F14 merge (09-28) | 3 | build FAILED (R46); fix r1 FAILED (R66); round 1 held on hand-off text and one weak assertion (R80), round 2 on report text only (R100 "both HOLDs report text"); R120 authorization: a report never committed |
| DRC D3 (09-29) | 3 (R51 HOLD 10, R94 HOLD 2, R125 YES) | build: a dialog 05:55–06:18 (R19), lock (R26), red (R32); check `11`: two packet ceilings (R42, R50); drafter `15`: wrong cwd (R72), classifier (R76) |
| S3 C4 (09-29) | 3, ends HOLD 1 (`cto-30` R1) | stray dev cards, waited on him 09:47 → 12:08 (R52, R65) for the "A" he gave to the same question at R1; check `27` stalled 13:46 → 14:40 (R84); dialog (R108); authorization 21:42 → 23:41 (R174) |

The same six causes repeat across the three days:
- a path outside `--add-dir` → a dialog: 4 (`cto-29` R19, R108; `cto-30` R19, R21).
- a launch-row literal or an uncommitted report → FAILED at authorization or preflight: 3 (`cto-28` R120, R174; `cto-29` R168 → R174).
- a packet byte ceiling: 3 (`cto-28` R154; `cto-29` R42, R50).
- a hub's Write or Edit refused or stopped by the classifier: 4 (`cto-29` R20, R76, R84, R110).
- a build leaves rows on `cobalt_dev` → an A/B to him: 2 (`cto-28` R182; `cto-29` R52).
- a seat lost to a meter or a timeout, found by launching: 6 (`cto-28` R31, R72, R151; `cto-29` R73, R99, R118).
Two of his directions collide in the second cause: short rows (09-28 R55; the 300-character hook, `cto-29:141`) and rows that carry "every gate literal its prompt greps" (checklist `:22`). The lean launch read (L6, 21:02, `cto-29:174`) was 39 minutes old when R168 went out without the literals.

Commit trail: 361 commits since 09-28, 348 of them `docs(desk)` (96%); two per launch (the row, then "running, tab, watched"); main is "ahead 327" of origin (`dep` STEP-D0, attempt 8).

Day rhythm (contract `:11`): no `close-2026-09-28.md`, no `close-2026-09-29.md`, no `day-open-2026-09-30.md` exist (`ls`); `cto-30:45` "09-29 close not run". The fold-at-close path has not run since 09-27.

DEPLOYMENT — 09-29 21:49 his "tonight" → drafter `39` → `40` (44,125 B; DRC × C1 conflict found 22:05, R172) → his set ruling OPEN overnight (R173) → 09-30 06:11 drafter `01` → `41` (54,761 B, never launched) → R9 → seam build `42` + split drafter `43` → `44` + `45` (47,720 + 47,442 B). Three generations of deploy prompt, about 194 KB, for one deploy; the seam known at 22:05 was built at 06:45.

## THE 09-30 DEPLOY
Launch row R14, 06:56. Eight launches of `44`:

| # | session · time | stopped at | cause | what was known before launch |
|---|---|---|---|---|
| 1 | `14887881` 06:57–06:59 | STEP-T | `--merges` also prints DRC's own merge `5bb1f4b5` (`att1:52`) | nobody ran the command. Drafter `43` had `git -C /Users/cobalt/cobalt log*` on its line (`43:1`) |
| 2 | `db724e9b` 07:02–07:12 | gate (a), offline red | the desk's own commit `ad805ca4` wrote the retired job label into `jobs.yaml`; `44` STEP-S ordered that wording; DRC's test refuses it (`att2:146`) | the desk made a production config commit by hand (`44:5-6`), with no suite run on it |
| 3 | `74f74d5f` 07:16–07:42 | STEP-R | `daily.md.j2` UNCLASSIFIED (`att3:173`), after 26 minutes of green suites | the seam report ESCALATE 4 (`:138`, written 07:02) lists it; the desk ruled on that report at 07:10 (R16) and launched at 07:14. `att3:173` says `deploy-2026-09-27.md` ESCALATE 14 had named it |
| 4 | `27d21872` 07:44–08:14 | D1, gate GREEN 08:11 | the hub ran an unlisted `ls` outside `--add-dir` → dialog; the desk pressed Escape and told it to go on (R19); the hub counted a denial and ended (`dep` ESCALATE 1, 3) | checklist W3 (`:51` "Dialog: `send-keys Escape`, MESSAGE") contradicts `UNATTENDED-LAUNCH.md:19` ("Never press another session's dialog") |
| 5 | `c6301631` 08:38–≈08:45 | 4.2b, residents DOWN | the listed plist `rm` is outside `--add-dir` → a dialog inside the outage; the desk stopped the hub, and no one ran STEP-5 (R21, R22). Down ≈08:44 → 08:55 | attempt 4's ESCALATE 2 (08:14) named this step as the one that fails with residents down; the same directory had just raised a dialog. `44:131` "No report prose until STEP-4 ends" left the outage unrecorded (L48) |
| 6 | `0c1f2c08` 08:53–08:58 | resume check (d) | the desk's resume rule assumed residents up; the hub restored them, then stopped | the desk wrote the rule without reading production |
| 7 | `30bed372` ≈08:59 | UNPROVEN | no §4 row and no report section. Commit `0a2bdde7` 09:00 "44 resume check uses git show (listed), attempt 8" and `44:45` "`show` is on your list, `ls-files` is not" point to an unlisted command in the desk's new resume check | — |
| 8 | `457cb535` 09:01– | running | MERGED `ef623fc7` → `9f92747e`, four migrations applied, residents up 09:11:56; `next: STEP-4.7 smoke, in flight` (read 09:14) | — |

Cost to the merge: 2 h 16 min from the launch row; two full gate runs and one ten-minute partial; ≈11 minutes of production down in a premarket scan session; `com.cobalt.prefill-drc` left unloaded on the old tree (`dep` ESCALATE 12).

Rules that would have stopped each before the first launch:
- A (1, 7): the drafter runs every read-only check of a deploy prompt and quotes the output in its report.
- B (2): the desk commits nothing into a gate tree. A config classification is a build, with the offline suite on it (contract `:7` already says the desk "never does the work itself").
- C (3): `cobalt jobs restarts` runs before the suites, not after; an UNCLASSIFIED path is fixed in the build that adds it (L42), never "OWED to the DRC deploy" (`cto-28:82`).
- D (4): one dialog rule. STOP, fix, rerun.
- E (5): no command runs for the first time inside the outage, and every absolute path on the allow list is under `--add-dir`. `UNATTENDED-LAUNCH.md:29` allows the opposite today: "a rule with no harmless variant is probed by its first real use".
- F (5, 6): a deploy hub past its first bootout is never stopped by the desk; residents come up first.

The desk's conduct during the run:
- Commits on main while a deploy hub ran: `423da40d` 06:57, `27f4a86a` 07:05, `48167e84` 07:16, `9a18db0a` 08:14, `b6e88f23` 08:15 and more (`git log`). Checklist C2 (`:61`), K19 and `44:48` forbid it. After D2 a desk commit makes 4.3 refuse the fast-forward with residents down (`44:137`).
- Relaunches 2–8 ran on launch row R14 (`dep` ESCALATE 4). R14 was edited after launch: `att1:24` quotes it "06:58 ET"; the file reads "06:56 ET" (`cto-30:22`). Attempt 6's prompt cited a row R21 that did not exist yet (`dep` ESCALATE 15).
- The desk's gate commit carried a `Claude-Session:` line (`att1:136`): the L74 block was followed.
- The L67 deploy read was dropped silently. Both drafters flagged it "for the desk's one-line override note" (`deploy-split-2026-09-30.md:104`, `deploy-reissue-2026-09-30.md:112`); no 09-30 row names L67 as set aside (R4 names L66 only). The 09-27 deploy had that read (`50-stacked-deploy-r3.md:77`).
- §5 CURRENT, the crash state, shows three different states at once: attempt 7 with its watches (`cto-30:39`), tab `w2:tEF` (`:46`), watch `brk3zk9tu` (`:47`). R23 sits above R22 and is stamped 09:12; `date` read 09:09 after it was written.

## RECOMMENDATIONS
Ranked. Each: the change · the file · the law · the risk. He rules.

1. OUTAGE-PROOF DEPLOY PROMPTS (rules A, C, E). Cheap checks first: preflight → tree → configs → RESTARTS → suites. The drafter runs every read-only check and quotes it. Nothing is first used inside the outage; every absolute path on the allow list sits under `--add-dir`; the retired-plist cleanup moves to after the residents are up. · `UNATTENDED-LAUNCH.md` §2 PREFLIGHT and `:29`; checklist K19 (`:106`); the deploy template. · L62, L63, L66. · Risk: a few more minutes of preflight per deploy.
2. NEVER STOP A DEPLOY HUB AFTER ITS FIRST BOOTOUT (rule F). One standing restore prompt (bootstrap aset and radar, kickstart the agent, smoke), approved by him once; the desk launches it when a deploy hub hangs with residents down, and reads the hub's pane and the heartbeat before it writes any resume rule. · `UNATTENDED-LAUNCH.md` §3; checklist `## watch`. · L66, L62 (the restore's strings are his to approve). · Risk: two sessions near production; the hung one is stopped first.
3. NO DESK WORK IN A GATE OR PRODUCTION TREE (rules B, C). A config classification belongs to the build that adds the path, proven by `cobalt jobs restarts` at that build's stop line and by its suite. · checklist K10 (`:97`), which today sends the classification to the deploy; the build template. · L42, L67, L68; contract `:7`. · Risk: one more step per build.
4. ONE DIALOG RULE (rule D). Delete checklist W3's "Escape, MESSAGE"; keep `UNATTENDED-LAUNCH.md:19`. Test once, on a scratch hub, a launch mode in which an unlisted command is refused with no dialog. · checklist `:51`. · L63. · Risk: none found; the mode is unproven.
5. AUTHORIZATION BY ROW NUMBER + COMMIT ONLY (K23, already his). Launch facts (build stop line, dev-vault listing, "no other house hub") stay in the prompt's LAUNCH-TIME VALUES, not in the §4 row. Ends the literal failures (3 in the window) and the clash between short rows and gate literals. · the check and build AUTHORIZATION blocks; checklist `:22`, `:34`. · L62; `UNATTENDED-LAUNCH.md:11`. · Risk: the row and the prompt no longer cross-check each other.
6. HIS WORDS AND THE FOLD. Every words block states what he was answering. A standing ruling stays `APPROVED — pending fold` until it is in LAWS or NOW. Owed now: `words-30` R9 (the protocol he meant), R23 (no block), `words-29` 21:0x and 21:3x; R10 needs his wording against L73. Run the two owed closes or rule them dropped. · checklist `:22`; `SESSION-CLOSE.md`. · L58, L73. · Risk: none.
7. §5 CURRENT: ONE ROW PER LIVE SESSION, OVERWRITTEN IN PLACE. Delete its TABS and WATCHES rows (second homes; they are the rows that went stale). One §4 row per relaunch, written before the launch. · checklist `:17` (3), `:23`. · L34. · Risk: none.
8. CUT THE READ PATHS. Workers: `CLAUDE.md` points at `## Build rules` down only; NOW, INDEX's start set, preferences and profile are the desk's. Prompt cards drop "Preamble + Index" and keep one line per binding law. Desk: the three cuts in `## STARTUP`. · `CLAUDE.md`; `cobalt.md:8-9`; `INDEX.md:8-12`; every template. · L59 (amend), L44, L58. · Risk: a worker misses a law its card omits; L59 already lets it open any entry.
9. WHOLE PROMPTS, ONE TEMPLATE PER KIND. A fix or check prompt carries its own steps; no "`24` whole; `26` whole", no "`21`'s blocks bind with substitutions". Stable `CHECK-HUB.md` and `BUILD-HUB.md` beside `UNATTENDED-LAUNCH.md` hold the unattended rules, the lock and the recovery. Packet ceilings (K6, K17) go, as he ruled on 09-27. · `D/prompts/`; checklist `:93`, `:104`. · L19, L67. · Risk: a one-time drafting cost; templates must be kept current.
10. HIS RULING: THE REFRESH POLICY AND THE SONNET TRIAL, ON NUMBERS. R127 (twice a day) and R68 (refresh above 250,000) cannot both hold at ≈170K of growth per 22–48 minutes. The per-turn MEASURE in §5 promised at `cto-29:173` is absent on 09-30; with it he can see the desk's size and rule. · wake-up `:40`; contract `:20`. · no law. · Risk: each extra refresh is one wake-up of 53–63K tokens.

## RULED PROCESS — the drafter's spec
His ruling in the brain tab, 09-30 ≈09:4x ET: "I want all this". The desk records it as a §4 row with his words. The drafter builds exactly the items below and nothing else.

DRAFT, all under `D/plans/fixed-files-2026-09-30/` (nothing installed, nothing launched on it):
1. `BUILD-HUB.md` — the fixed build file: launch line, allow list, `--add-dir` set, unattended rules, lock (L76), recovery (L60), the three suites (L68), `cobalt jobs restarts` with no UNCLASSIFIED row before the stop line (L42), pre-stop self-check (K25), report sections, stop line.
2. `CHECK-HUB.md` — the fixed check file: seats per L67, probes, one instructions file plus the files themselves, no packet and no byte ceiling, collate, stop line.
3. `CARD.md` — the job card format, one for both kinds: ladder line, branch, base, tip, the rows with the test that goes red first, his rulings that bind the job, report path. No launch line, no procedure, no authorization block, no words-file read.
4. `desk-launch.sh <kind> <card>` — the one way the desk launches: refuses an incomplete card, a kind that is not a fixed file, a worktree outside the approved pattern, a with-DB launch while a lock is held.
5. A pre-commit addition: refuse a desk commit on main while a deploy hub is live.
6. `STANDING-LIST.md` — for his ONE approval: each fixed file's allow list, and the `.env` copy / remove as a pattern for any `~/cobalt-wt/<branch>`.
7. `DESK-LINE.md` — the proposed narrower desk launch line (git add / commit on its own report, card and memory files; log, show; no Edit of `src/`, `configs/`, a gate tree) and the fold texts the desk applies: deploys leave his four; a deploy launches itself when every check closed with nothing held and the gate is green; he is asked only for a carried held defect and for a schema rollback; his words are appended to the words file and read by no start routine and no worker.
8. `SPLIT.md` — the proof nothing is lost: every line of `prompts/2026-09-29/37-…build.md` and `38-…check.md` assigned to card, fixed file, or dropped-with-reason. A line with no home is an ESCALATE.

9. `DEPLOY-HUB.md` — the fixed deploy file (in scope since deploy 2 landed 10:20, `cto-30` R30), carrying rules A–F above: cheap checks before the suites, every command and path proven before the first bootout, residents restored before any stop, a carried-baseline rule for a probe already RED at D1 (`cto-30` R28, R29), one resume point. Its card: the tips, the migrations, the smoke reads of the set. `SPLIT.md` also assigns every line of `prompts/2026-09-30/45-deploy-2-s3-seam-0930.md`.

NOT in this draft: any edit to LAWS, memory, the wake-up, settings or hooks in place; the read-path cuts (rec 8); §5 (rec 7); the refresh policy (rec 10); any change to a prompt already queued.

DONE means: the brain reads the nine files against this section and reports each gap; he approves `STANDING-LIST.md` once; the desk installs; the first job is the next build the desk launches after the install, on a card (E1 was built the old way at 10:25, `cto-30` R31). Work already queued or running (`50`, `51`) finishes as written.

## RULED CHECK FLOW — second loop (after the brain has read the drafter's nine files)
His ruling in the brain tab, 09-30 ≈11:0x ET; the desk records it with his words. It replaces item 2's "seats per L67" in `CHECK-HUB.md` and amends L67's build-check clauses (three checkers; Gemini reads no code check). Design tribunals are unchanged.

THE FLOW, one build:
1. HOUSE A, one house outside Anthropic (Grok; Sol or Astra when their meter is back): reads the card, the diff `<base>..<tip>` and the files it touches. Every finding = a failing test or a command it ran, with the output. A claim with no run is dropped by the hub.
2. FRESH OPUS, a new session, never the builder: FIRST its own read of the same set, its own findings in the same form; THEN house A's findings, each judged by running it; THEN it fixes what holds. Done when every held finding's test passes, the three suites are green and each new test was shown red first.
3. Nothing open → DONE. Something open (a finding Opus could not settle, or one it rejects and house A's run supports) → HOUSE B, a different house from A (Gemini is available), reads the diff plus both findings lists and adds its own, same form.
4. FRESH OPUS applies them; the same finish as step 2. No further house. What no test can catch ships and goes on the follow-up list.
MANDATORY HOUSE B: a build that writes his vault notes or changes sizing runs step 3 even when nothing is open.
SEAT ORDER (his ruling, same sitting), by the meter probe at launch:
- OpenAI up → house A = OpenAI, house B = Grok.
- OpenAI out → house A = Grok, house B = Gemini.
- OpenAI and Grok both out → house A = Gemini, no house B. A mandatory-B build then WAITS for a meter (his "Agreed", same sitting); he may overrule it per case.
START-SET RULE: nothing in this section or in RULED PROCESS is added to a file the desk reads at start. The flow lives in the fixed files and the launch script. Any edit to the wake-up, the contract or NOW replaces lines; `wc -c` after is smaller than before (`writing-rules.md:23`).
Gemini never sits ahead of a house that is up. This replaces step 1's and step 3's house names above.

WHAT THE OPUS SEAT READS — the card is the whole list:
- the job card (rows, his rulings that bind it, the one-line laws);
- the diff and the files it touches, at the tip;
- the build report's gate section (the three suite lines, RESTARTS);
- house A's findings, after its own read.
NOT: the LAWS Index, NOW, preferences, profile, earlier prompts, earlier rounds, the design document beyond the sections the card names.
Its stop line carries the count of files it opened and its token total, so a seat that read beyond the list shows in one line.

## READ OF THE DRAFT (`D/plans/fixed-files-2026-09-30/`, the drafter's report `D/reports/fixed-files-draft-2026-09-30.md`)
Read whole: the drafter's report, `CARD.md`, `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `desk-launch.sh`, `pre-commit-deploy-guard.sh`, `STANDING-LIST.md`, `DESK-LINE.md`. `SPLIT.md` (44,326 B): its head, its counts, all 31 DROPPED rows and the six WEAK HOMES; the other 345 rows not read one by one.

VERDICT: the nine files are the spec's nine and nothing more; nothing is installed (each hub file refuses to run on its `«INSTALL` token). The three hub lists carry no new string. Each dropped row has a reason that holds (history, a pointer replaced by the text itself, a gate literal, a packet, a copied count). The drafter named its own departures (Edit, two Writes over 15 KB, two `cd`); none touched a file that existed before.

GAPS, for the second loop (each: the file · the fix):
1. `CHECK-HUB.md` is the old check (Sonnet hub, Opus · Sol · Grok read-only, rounds 1–3, a classifier). RULED CHECK FLOW replaces it whole, not by a revision: the fresh Opus seat runs tests and fixes, so it is a write-path session on the build list. CORRECTION to RULED CHECK FLOW step 1: the outside seats cannot run commands (`CHECK-HUB.md:51` "you cannot run commands"; Sol `-s read-only`; Grok's sandbox). House A's finding = a test it WROTE or an exact command, which the fresh Opus runs. A claim with nothing runnable is dropped.
2. `desk-launch.sh` prints the commands; the desk still types them, so nothing stops a launch outside the script. Fix: the script runs the launch itself and the desk's own `claude --bg` allow goes. Then the NEW `worktree add` string on the desk line is not needed.
3. `DEPLOY-HUB.md:59` P1 admits only the 20:00–21:00 pause or a ruling that sets the window aside. His night deploys fail there. Fix: P1 also admits L43's overnight idle (after the pause, before 04:00) and a non-trading day.
4. `DEPLOY-HUB.md:33` still needs a row of his for each deploy. Fix: the standing rule (clean checks + green gate); his row only for a carried held defect.
5. `LAUNCH ROW` in the card (`CARD.md:23`) and its gate in all three hub files: every relaunch needs a new row, a card edit and a commit before it may start. It proves only that the desk wrote a row. Fix: drop the field and the gate; the hub proves the card is committed; the desk still writes its row (L34).
6. Tree state sits in two fixed files: the pass-1 and pass-2 commands, the allowed-skip list, the level `0013` (`BUILD-HUB.md:79`, `:83`; `DEPLOY-HUB.md:103`–`:107`). No owner is named for keeping them current. Fix: a build that adds a with-DB test or a migration carries a row that edits those lines; its check reads it.
7. Rule F says the desk never stops a deploy hub after its first bootout, and the draft has no action for a hub hung there (the drafter's ESCALATE 6). The resume already restores residents found down (`DEPLOY-HUB.md:55` (e)). Fix: one line — hung after the bootout → stop it and at once `desk-launch.sh deploy <card> STEP-D0`.
8. A set that adds, changes or retires a launchd job cannot deploy on the fixed file (`DEPLOY-HUB.md:88`); the retire is the desk's, on strings he would approve each time. Rare; named so it is not a surprise.
9. The hub files still order LAWS `## Preamble` + `## Index` (`BUILD-HUB.md:16`): the worker read-path cut, waiting on his word.
10. `DESK-LINE.md:13` makes the wake-up's launch line longer (13 allow strings for 4). START-SET RULE: measured at install; the checklist's launch and prompt sections must shrink by more.
11. UNTESTED, before any install, on a scratch session: both scripts; whether a deny on Edit also stops Write; whether the desk can still Write a new card once the bare Write is gone (`DESK-LINE.md:26-29`); whether the hook finds `claude` and `python3`.

RULED by him on gaps 5 and 9 (brain tab, 09-30, after the read):
- Gap 5: the launch-row field and its gate are DROPPED.
- Gap 9: a worker reads its fixed file, its card, and `M/areas/cobalt.md` from `## What Cobalt is` (the absolute boundaries, `:32-35`) and `## Build rules` down. It does not read NOW, INDEX's start set, preferences, profile, or LAWS `## Preamble` + `## Index`. The laws that bind stay as the one-line list already in each fixed file (`BUILD-HUB.md:17`); a worker opens a full entry when it acts on that law. The second loop strikes the "Preamble and Index first" line from the three hub files and writes the fold texts for `CLAUDE.md`, `cobalt.md:8-9` and L59 into `DESK-LINE.md`, PROPOSED.

`STANDING-LIST.md`: the build and deploy lists are as run today and read correctly. The check list changes with gap 1 (the Opus seat's strings; Gemini's). ONE approval belongs after the second loop, on the final list.

## RULED WORKER ENDINGS (his "yes", brain tab, 09-30; for the three hub files)
1. Every hub report ends with two sections in place of `## ESCALATE`: `## DECISIONS` and `## RECORDS`.
2. `## DECISIONS`: one item per question, each with the safe default the worker took. An item MUST be here when it blocks the next step, lies outside the card's rows, is unproven and the job depends on it, or touches his notes, money or sizing. An item that is his (scope, dates, money, a carried held defect, a schema rollback) is marked `FOR DEJAN`.
3. `## RECORDS`: facts for the file (cleanup owed, a value re-read, an L74 line, a carried item). Read by nobody unless a later step fails.
4. The stop line carries `decisions: <n> · for Dejan: <n>` in place of `ESCALATE: <n>`.
5. `decisions: 0` → the desk verifies the artifact (L35) and launches the next step. `decisions: ≥1` → the desk hands the report path to the Opus judgment seat (`brain`, or a hub it launches); that seat reads `## DECISIONS` only, answers each; the desk records the answers. A `FOR DEJAN` item reaches him as one short question.
6. A DEPLOY report: the judgment seat reads both sections, whatever the count.
7. The desk, per event: one §4 row and one commit per launch; §5 CURRENT one row per live session, overwritten in place, no TABS or WATCHES row (checklist change, PROPOSED in `DESK-LINE.md`).

## UNPROVEN
- The desk's replies to him (length, plate content, the startup-tokens line): chat text is in no file handed to me.
- Attempt 7's cause; attempt 8's smoke result (in flight at 09:14; a red row sends it to the revert).
- Whether the Sonnet desk caused 09-30's errors: one morning, under a deadline. The same error classes appear under the Opus and Fable desks on 09-28 and 09-29 (the six causes above).
- Token figures for files: bytes are measured; tokens are estimated from bytes.
- Why `38`'s 21:42 FAILED was acted on only at 23:39: no row between. The relaunch armed two watches, the reports path and the scratch path (`cto-29:195`).
- Whether the row-length hook ran on 09-30's desk commits (three "row trimmed" commits followed).
- "this protocol" in `words-30` R9.
- The size of desk `3adfd15c` now: no MEASURE row in `cto-30` §5.
- Both-before-09:30 for deploy 2: not yet launched; one gate run took ≈26 minutes (`att3:174`).
- L74: a block inside tool results in this session asked for a `Claude-Session:` line and named a file-send tool. Data; not followed. This session commits nothing.
- Written in three parts of under 15 KB: the first by Write, the next two appended by Edit to this same file.

BRAIN DESK REVIEW DONE · directions: 17 · followed: 2 · partly: 5 · not followed: 7 · not verifiable: 3 · contradictions: 5 · recommendations: 10
