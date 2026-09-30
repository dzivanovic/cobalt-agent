# SPLIT — the proof nothing is lost (DRAFT 2026-09-30)

Every line of three prompts as run, assigned to a home: `37` = `prompts/2026-09-29/37-s3-exits-c4-fix-r2-build.md` (100 lines), `38` = `prompts/2026-09-29/38-s3-exits-c4-fix-r2-check.md` (33 lines), `45` = `prompts/2026-09-30/45-deploy-2-s3-seam-0930.md` (192 lines). Line numbers are `grep -n`'s.

HOW TO READ A ROW: `<file>:<line><segment>` · what the text says · where it lives now · the HOME. A long line is cut into segments `a`, `b`, `c` …: a segment is one sentence, or consecutive sentences that share one home. HOMES: `CARD` (a value of the job, in the card's named field) · `BUILD` / `CHECK` / `DEPLOY` (the fixed hub file, with its section) · `LIST` (`STANDING-LIST.md`) · `LAUNCH-SH` (`desk-launch.sh`) · `GUARD` (`pre-commit-deploy-guard.sh`) · `DROPPED` (with the reason) · `BLANK`. A segment with no home would be `UNHOMED` and an ESCALATE; there is none. A home marked CHANGED keeps the rule and alters it, and says how.

DROP REASONS, by letter: **H** history or a value of one date (a prompt carries no history; `writing-rules.md`) · **W** written whole in the fixed file instead of pointed at (L19) · **K** a gate literal or a quoted word: approval is proved by row number and commit only (K23; the brain's recommendation 5) · **P** packet, byte ceiling or staging by `cp`: his 2026-09-27 R42 (`cto-2026-09-27.md` R42, 22:17: no packets — one instructions file plus the files, each house reads; a copy only where access requires it) · **N** a count or expectation copied from an earlier run: the gate is `0 failed`, the table, the read itself · **S** one standing list: nothing is compared string by string per job · **G** the launch-row field and its gate, dropped by his 2026-09-30 R38 (the brain's gap 5): the hub proves the card is committed and unchanged; the desk's §4 row stays the desk's record (L34) · **R** (fourth pass) applied at the ruling, not at the close: RULED — THE NIGHTLY CLOSE point 2 keeps, reduces and adds steps and names no areas/topics step (L58 as amended, `RULE-CHANGES.md` row 50).

LOOP 4 (2026-09-30, the brain's READ OF THE SCRATCH TEST and RULED — THE NIGHTLY CLOSE). Three rows CHANGED in place, marked `L4`: the permission mode of the three launch lines (`37:1c`, `38:1j`, `45:1d`: `dontAsk`, the file tools listed). A fourth source is split: `SESSION-CLOSE.md` (15 lines), whose table `CLOSE-HUB.md` replaces; two new homes: `CLOSE` (`CLOSE-HUB.md`, with its section) and `RULE` (a row of `RULE-CHANGES.md`).

LOOP 2 (2026-09-30, his R38 and the brain's RULED CHECK FLOW, READ OF THE DRAFT and RULED WORKER ENDINGS). Rows whose home MOVED or whose rule CHANGED are marked `L2`: the launch-row gate (`37:45a`, `38:13d`, `45:29`, `45:37a`); the read of LAWS `## Preamble` + `## Index` (`37:38a`, `45:45`); every `38` row that lived in the old check file, now homed in the rewritten `CHECK-HUB.md` (sections `## THE FLOW AND THE SEATS`, `## 1` stage, `## 2` house A, `## 3` the fresh Opus seat, `## 4` house B and the second pass, `## THE OPUS SEAT`, `## 5` collate, `## 6` close); the launch steps the script now runs (`37:4`, `38:1g`, `45:4`); the window (`45:72`); the ending sections (`37:97a`, `38:24c`, `45:63`, `45:177a` and the three stop lines).

LOOP 3 (2026-09-30, his R45 and the brain's THIRD PASS). `CHECK-HUB.md` was rebuilt: the check IS one fresh Opus session, so every `38` row homed in the loop-2 check file is re-homed to the rebuilt file's sections and marked `L3`: header; `## LAUNCH`; `## THE FLOW AND THE SEATS`; `## WHAT YOU READ`; `## AUTHORIZATION`; `## UNATTENDED RULES`; `## REPORT`; `## PREFLIGHT`; `## 1` (stage, the HOUSE TEXT, (5) start the house); `## 2` (the own read); `## 3` (the house's list, THE DROP); `## 4` (judge by running); `## 5` (fix); `## 6` (the finish); `## 7` (checked against the branch, COUNTING); `## 8` (close); `## PASS 2`; `## STOP LINE`. Two rows changed HOME: `38:1e` (the card's `ROUND` field is gone: CARD → CHECK) and `45:1f` (his R10 override ended the same day, `cto-2026-09-30.md` R44: CARD → DROPPED, H). The ESCALATE wording of the three ending rows and of `37:33b` was already `## DECISIONS` / `## RECORDS` in loop 2; the hub files' "a denied call ends the run" is now CONTINUE, DO NOT RESTART (`37:1c`, `45:62`).

## `37` — the fix build (100 lines)

| ref | what it says | where it lives now | home |
|---|---|---|---|
| 37:1a | MODEL Opus 5.5, Opus floor, never auto mode | header, MODEL | BUILD |
| 37:1b | why THIS job is a write path (the trade-note writer, the lock) | H: every build is a write path in the fixed file | DROPPED |
| 37:1c | `acceptEdits`; only exact listed prefixes; a dialog = FAILED | header, PERMISSION MODE (L3 CHANGED: a refused call is `## UNATTENDED RULES`, CONTINUE, DO NOT RESTART (a)–(c); a dialog is still never pressed. L4 CHANGED: the mode is `dontAsk` — an off-list call is refused with no dialog, scratch item 9 — and the file tools are allow strings) | BUILD |
| 37:1d | SEAT name, launched by the desk in the background | header (`<JOB>-build`); `JOB` | BUILD |
| 37:1e | fresh session; relaunch = the same line + ONE `CONTINUE:` line | header, SESSION | BUILD |
| 37:1f | never `bypassPermissions`; push denied | header | BUILD |
| 37:1g | METER medium, minutes per step | header ("sized by the card's rows"); the minutes are N | BUILD |
| 37:1h | test vault writes in `tmp_path`; his vault and the dev vault read only | header | BUILD |
| 37:1i | nobody at the terminal; `ASK DESK`; never end a turn between steps | header | BUILD |
| 37:1j | grep patterns: plain fixed strings, one per call | `## UNATTENDED RULES` | BUILD |
| 37:3a | launch only while no `.env` under any worktree and no with-DB run (L76) | `## LAUNCH`; refused by the script too | BUILD |
| 37:3b | launch only when the classification's OWNER ITEMS are empty or ruled | WHO FILLS IT (a fix-round card is written only then) | CARD |
| 37:3c | the worktree is clean and on its branch | build branch of the script (branch and clean-tree refusals) | LAUNCH-SH |
| 37:3d | the branch stands at `<base>`; the worktree exists and is not re-cut | `## PREFLIGHT` (HEAD = `BASE`); `## LAUNCH` (0) | BUILD |
| 37:4 | (1) `cd` into the worktree | `## LAUNCH` (1); L2: RUN by the script, not typed by the desk | BUILD |
| 37:5 | (2) the launch line: 24 allow, 3 deny, three `--add-dir` | `## LAUNCH`, the one `claude --bg` line (`mkdir -p *` left out; L2: 24 allow, `git -C * diff*` added for the card-committed proof) | BUILD |
| 37:7a | RULE STRINGS: no new string, byte for byte as two earlier prompts; the `comm -3` proof | S; the list's provenance is §1 of the list | LIST |
| 37:7b | the `.env` pair is his approved pair | THE `.env` PATTERN | LIST |
| 37:7c | `mkdir -p *` carried unused | §1, "dropped from the proven line" | LIST |
| 37:7d | never typed: `uv run python` … `COBALT_ENV=production` | `## LAUNCH`, Never typed (the job's own CLI verb is `NOT IN THIS JOB`) | BUILD |
| 37:7e | a mutation is made and undone with Edit only, never committed | `## LAUNCH`; `## E3` | BUILD |
| 37:9 | title: what is built, on which commit, the ladder tag, "the last fix round" | `JOB`, `LADDER`, `BASE`, `## ROWS` (L3: "the last fix round" has no field — a build check has no rounds) | CARD |
| 37:11a | LADDER line | `LADDER` | CARD |
| 37:11b | LAW STEP: the chain of earlier builds, rounds and records | H | DROPPED |
| 37:11c | what comes next: the check, the last round, the deploy set | `## CLOSE`, the standing ESCALATE line (generic) | BUILD |
| 37:11d | DO NOT STOP until the last line is BUILT or FAILED | header paragraph | BUILD |
| 37:13 | LAUNCH-TIME VALUES; a token left standing = `FAILED: placeholder` | `«FILL` tokens; proved by `## AUTHORIZATION` of the hub file | CARD |
| 37:14 | `<base>` with the desk's read and time | `BASE` | CARD |
| 37:15 | `<code base>`, the last code commit below a docs-only head | `## RECORDS` (the reds run on `BASE`'s tree) | CARD |
| 37:16 | the dev-vault listing the desk read | `## RECORDS` | CARD |
| 37:18 | heading: his rulings and the desk's calls | `RULINGS`, `## NOT IN THIS JOB` | CARD |
| 37:19 | earlier rulings and seams hold unchanged; nothing re-decided or re-opened | `RULINGS` (row numbers), `## NOT IN THIS JOB`; L72 / L77 lines in `## LAWS` of the hub | CARD |
| 37:20 | ONE `src/` file, one branch of one function; nothing under `vaultwrite/` | `## ROWS` files; `## NOT IN THIS JOB` | CARD |
| 37:21 | X3 out of scope again; no X3 test changed | `## NOT IN THIS JOB` | CARD |
| 37:22 | the `tmp_path` guard stands; a guard trip is fixed in the test, never in the guard | `## NOT IN THIS JOB` (the rule itself: header, 37:1h) | CARD |
| 37:24 | heading: THE ROWS, in this order, nothing else | `## ROWS`; "nothing else" is `## E3` of the hub | CARD |
| 37:25 | table header | `## ROWS` header | CARD |
| 37:26 | table rule | `## ROWS` | CARD |
| 37:27 | row B1: the rule, the mechanism, the fix, tests B1-1 … B1-7 and N with each red | `## ROWS` (what · red first · files), whole | CARD |
| 37:29 | one dated DevDocs line for the changed module | `## E3` (every changed module gets one dated line) | BUILD |
| 37:31 | the dev vault is a record; no command on it; nothing removed in any vault | `## RECORDS`; the hub copies records at `## PREFLIGHT` | CARD |
| 37:33a | RUN U3: what it runs, the test to add, the command, what to print | `## ROWS`, a RUN row | CARD |
| 37:33b | a RUN asserts nothing, is quoted whole, its finding is an ESCALATE line, not fixed here | `## E2` (L2: the line is a `## DECISIONS` item, `DECISION <row>`) | BUILD |
| 37:35 | NOT IN THIS FIX | `## NOT IN THIS JOB` | CARD |
| 37:37 | heading: INDEX CARD, read in this order | `## LAWS`; the card's `## READ` | BUILD |
| 37:38a | LAWS Preamble + Index, then each entry, one line per law | `## LAWS` (L2 CHANGED by R38, gap 9: the read of Preamble + Index is STRUCK; the worker reads the fixed file, the card and `areas/cobalt.md` from `## What Cobalt is` and `## Build rules` down; one line per law stays, an entry opened only when acted on) | BUILD |
| 37:38b | the job's own gloss on a law (what L1, L39, L72, L77 mean here) | `## ROWS`, `## NOT IN THIS JOB` | CARD |
| 37:38c | `writing-rules.md` for §0, CONTINUE, ESCALATE | `## LAWS`, last line | BUILD |
| 37:38d | read checklist K24–K25 | W: the three self-check lines are in `## PRE-STOP SELF-CHECK` | DROPPED |
| 37:39a | the classification, the round-2 check sections, the fix r1 build report sections | `## READ` | CARD |
| 37:39b | "`24` whole; `26` whole" | W: an earlier prompt of the chain is not read; what binds is in the hub file and the card | DROPPED |
| 37:39c | `20`'s UNATTENDED RULES, RECOVERY, THE LOCK, W | W: `## UNATTENDED RULES`, `## RECOVERY`, `## THE LOCK`, `## W` written whole | BUILD |
| 37:39d | the defect survey's TOP 3 | W: it is K25, in `## PRE-STOP SELF-CHECK` | DROPPED |
| 37:40 | code to read, by symbol | `## READ` | CARD |
| 37:42 | AUTHORIZATION: the desk wrote it, not Dejan; `<D>` from `date` | `## AUTHORIZATION` | BUILD |
| 37:43 | PLACEHOLDER GATES, two greps on the prompt file | `## AUTHORIZATION`: the `«INSTAL[L]` grep on the hub file, the `«FIL[L]` grep on the card | BUILD |
| 37:44 | the classification's stop line carries `OWNER ITEM: 0` | K as a gate literal; the report is in `## READ` and its last line is quoted at `## PREFLIGHT`; the condition itself is 37:3b | DROPPED |
| 37:45a | THIS LAUNCH is the desk's row; the row names this file; the commit proves it | L2 CHANGED (G): no launch row is read; `## AUTHORIZATION` proves THE CARD IS COMMITTED (`log -1` non-empty, `diff --stat` empty) | BUILD |
| 37:45b | the row must carry `<base>`, the dev-vault listing, the literal `no with-DB run in flight` | K; the lock is proved by `ls` (`## PREFLIGHT`), the values are in the card | DROPPED |
| 37:46 | YOU CAN ALWAYS STOP; with `.env` present or a migration applied, stop = W (f) first | `## AUTHORIZATION`, last lines | BUILD |
| 37:48 | heading: UNATTENDED RULES, RECOVERY, THE LOCK | the three sections | BUILD |
| 37:49a | `20`'s blocks bind unchanged, with four substitutions | W: written whole; the substitutions are `JOB`, `BRANCH`, `WORKTREE` | BUILD |
| 37:49b | you write only the row's files, the RUN test, the DevDocs line, the report | `## UNATTENDED RULES` | BUILD |
| 37:49c | the lock is taken twice; a third take is an ESCALATE line | `## THE LOCK` (CHANGED: the PREFLIGHT probe is one more, read-only take) | BUILD |
| 37:49d | never run two named with-DB files at `0013` outside W (c) | `## W` (c): never a deselected with-DB file outside that command | BUILD |
| 37:51 | heading: REPORT | `## REPORT` | BUILD |
| 37:52a | the report path | `REPORT` | CARD |
| 37:52b | sections, clock from `date`, first Write, pinned last line | `## REPORT` (CHANGED: `## RESTARTS` before `## W`) | BUILD |
| 37:54 | heading: PREFLIGHT, one row each | `## PREFLIGHT` | BUILD |
| 37:55a | `date`; status = the branch alone; HEAD = `<base>` | `## PREFLIGHT` | BUILD |
| 37:55b | no `src` / `tests` / `configs` commit between `<code base>` and the head | N: the reds run on `BASE`'s own tree; the code commit below it is a record (37:15) | DROPPED |
| 37:56 | `.env` absent here; no `.env` under any worktree | `## PREFLIGHT` | BUILD |
| 37:57a | each symbol and each caller grep, quoted; a missing symbol = FAILED | `## PREFLIGHT`, THE CARD'S SYMBOLS | BUILD |
| 37:57b | which symbols, which callers are expected at which lines | `## READ`, `## ROWS` | CARD |
| 37:58 | copy the desk's dev-vault listing into PREFLIGHT | `## PREFLIGHT`, `## RECORDS` | BUILD |
| 37:59 | `jobs restarts <base>..HEAD` → an empty range | `## PREFLIGHT` | BUILD |
| 37:60 | write the report; `next: E0` | `## PREFLIGHT` | BUILD |
| 37:62 | heading: E0 baseline | `## E0` | BUILD |
| 37:63a | the offline and live-note commands; a red base = FAILED; no test file written meanwhile | `## E0` | BUILD |
| 37:63b | EXPECTED `3320 passed`; `146 passed, 1 skipped` | N | DROPPED |
| 37:65 | heading: E2 red first; a `wip … red` commit before any `src/` edit | `## E2` | BUILD |
| 37:66a | write the tests; the offline run; each red for its named reason; rewrite a wrong red | `## E2` | BUILD |
| 37:66b | which tests fail, which pass, on which line | `## ROWS`, red first | CARD |
| 37:66c | the with-DB reds: lock take, `<FP>`, proof-only, no forward, the `-rA` run, the lock's (d), commit | `## E2` | BUILD |
| 37:68 | heading: E3 the row | `## E3` | BUILD |
| 37:69a | what to write and where it is called | `## ROWS` | CARD |
| 37:69b | the row's tests green after the edit | `## E3` | BUILD |
| 37:69c | the mutations: made with Edit, the named tests run alone, quoted, undone, `git diff --stat` | `## E3`, THE MUTATIONS | BUILD |
| 37:69d | which mutation (M1, M2) must turn which test red | `## ROWS`, red first (the fix undone; the negative control broken) | CARD |
| 37:69e | the commit message; `next: W` | `## E3` (shape `<fix|feat>(<JOB>): …`; next is RESTARTS) | BUILD |
| 37:71 | heading: W, the three suites, "as your fix r1 report executed it" | `## W` (W: every command typed whole) | BUILD |
| 37:72 | `<tip>`; `<FP>` copied from the earlier report | `## THE LOCK` (`<FP>` typed whole); `## W` | BUILD |
| 37:73 | (a) offline, `0 failed`, `0 errors` (the expected count is N) | `## W` (a) | BUILD |
| 37:74 | (b) the lock, `<F0>`, proof-only at `0013`, else FAILED | `## W` (b) | BUILD |
| 37:75 | (c) pass 1: the earlier report's command byte for byte | `## W` (c), THE PASS-1 COMMAND typed whole | BUILD |
| 37:76 | (c2) forward in the foreground; `dev forward: APPLIED`; `<F1>` (the four numbers are H) | `## W` (c2) | BUILD |
| 37:77 | (c3) pass 2 byte for byte; the job's ids PASSED | `## W` (c3), THE PASS-2 COMMAND typed whole | BUILD |
| 37:78 | (c3r) nothing left behind: the earlier report's query → no rows | `## W` (c3r), the query typed whole with the build's own tickers | BUILD |
| 37:79 | (e) live-note | `## W` (e) | BUILD |
| 37:80 | (f) rollback to `0013`, `F2 = F0`, the lock's (d), no `.env` | `## W` (f) | BUILD |
| 37:81 | X22 is not repeated (no migration) | `## W` (c4): only a build that adds a migration | BUILD |
| 37:82 | a red at W: fix inside the row's files, a second commit, W again, an ESCALATE line | `## W`, last paragraph | BUILD |
| 37:83 | `next: RESTARTS` | CHANGED: `## RESTARTS` runs before `## W` (rule C) | BUILD |
| 37:85 | heading: RESTARTS | `## RESTARTS` | BUILD |
| 37:86 | the table whole; UNCLASSIFIED = FAILED; the stop line carries the table's last line, never predicted | `## RESTARTS` (CHANGED: an UNCLASSIFIED path is classified in this build first, L42; FAILED only if it stays) | BUILD |
| 37:88 | heading: PRE-STOP SELF-CHECK (K25) | `## PRE-STOP SELF-CHECK` | BUILD |
| 37:89 | (1) every test shown red against a mutation or negative control | (1) | BUILD |
| 37:90a | (2) every entry path pinned by a test | (2) | BUILD |
| 37:90b | the six callers and the test that pins each | `## ROWS` | CARD |
| 37:91 | (3) every `file:line`, count and quote re-read at the tip | (3) | BUILD |
| 37:92 | a line you cannot back: fix it, or `self-check: <k> of 3` | last line of the section | BUILD |
| 37:94 | heading: CLOSE | `## CLOSE` | BUILD |
| 37:95 | the dev vault: nothing to run; the desk lists it again | `## RECORDS` (the desk's re-read is the desk's) | CARD |
| 37:96 | `## FOR THE CHECK`: what it holds | `## CLOSE` | BUILD |
| 37:97a | `## ESCALATE`: every ASK DESK, every ESCALATE line, the L74 line | `## CLOSE` (L2 CHANGED, RULED WORKER ENDINGS: questions under `## DECISIONS`, facts and the L74 line under `## RECORDS`; the stop line's `decisions: <n> · for Dejan: <n>`) | BUILD |
| 37:97b | the standing sentence: checked by which prompt, which seats, X3 owed, the deploy set | `## CLOSE` (generic: checked on the same card by `CHECK-HUB.md`); X3 is `## NOT IN THIS JOB` | BUILD |
| 37:98 | §0; the report commit by explicit path; clean status; no `.env` | `## CLOSE` | BUILD |
| 37:99 | the stop line | `## STOP LINE` (CHANGED: one shape for every build, `BUILT · job: <JOB> · tip: …`; `FIX` / `RUNS` become `rows`; L2: ends `decisions: <n> · for Dejan: <n>`) | BUILD |
| 37:100 | next step, not yours: the desk verifies and launches the check | `## STOP LINE`, last line | BUILD |
| 37:2, 6, 8, 10, 12, 17, 23, 28, 30, 32, 34, 36, 41, 47, 50, 53, 61, 64, 67, 70, 84, 87, 93 | 23 blank lines | — | BLANK |

## `38` — the fix check (33 lines)

| ref | what it says | where it lives now | home |
|---|---|---|---|
| 38:1a | MODEL Sonnet; you copy, point three checkers at ONE instructions file, file-check, tabulate; no verdict | header (L3 CHANGED: no Sonnet hub — the check is ONE fresh Opus session that stages, starts one house, reads first, judges every finding by running it and fixes what holds) | CHECK |
| 38:1b | SEAT name, launched by the desk in the background | header (`<JOB>-check`) | CHECK |
| 38:1c | LADDER | `LADDER` | CARD |
| 38:1d | LAW STEP: the chain of builds, rounds and records | H | DROPPED |
| 38:1e | this is round 3 of ≤3, the last; after it nothing loops | `## THE FLOW AND THE SEATS`, PASS 2 (L3 CHANGED: no `ROUND` field; a check is one pass or two and nothing loops after the second — NO FURTHER HOUSE AND NO THIRD PASS) | CHECK |
| 38:1f | SEATS Opus · Sol · Grok; no Astra, no Gemini; the floor | `## THE FLOW AND THE SEATS` (L2 CHANGED by R38: house A and house B by the meter order OpenAI · Grok · Gemini, a fresh Opus between and after; Gemini may sit; no outside house up = FAILED) | CHECK |
| 38:1g | two bare commands: `cd` into `agy-trial`, the launch line | `## LAUNCH`, the one `claude --bg` line (L3 CHANGED: the script enters the JOB'S WORKTREE, not `agy-trial`; the session `cd`s to `agy-trial` only to start a house, `## UNATTENDED RULES` CWD) | CHECK |
| 38:1h | the four `cp` strings on that line | P | DROPPED |
| 38:1i | RULE STRINGS: 14 allow, byte for byte as an earlier prompt; the `comm -3` check; the house strings standing | S; §2 of the list | LIST |
| 38:1j | fresh; auto mode; no database, pytest, uv, git write, vault or memory write, mkdir | header (L3 CHANGED: the rule is reversed — the check is a write-path session on the build list (L4: in `dontAsk`, no longer `acceptEdits`); what stays: no vault or memory write, no `mkdir`) | CHECK |
| 38:1k | METER small; nobody at the terminal; ASK DESK with the safe default | header (L3: METER medium per pass) | CHECK |
| 38:1l | grep patterns | `## UNATTENDED RULES` | CHECK |
| 38:1m | DESK: launch only while no other Grok hub and no other house hub runs; the watch regex | `## LAUNCH` (the script prints the reminder; L2: and refuses while the `cobalt_dev` lock is held) | CHECK |
| 38:3 | LAUNCH-TIME VALUES, filled from the build's stop line and `git log` | `«FILL` tokens | CARD |
| 38:4 | `<build stop>`, the build's stop line copied in | K: the hub reads the build's last line itself, `## PREFLIGHT` THE BUILD IS BUILT | DROPPED |
| 38:5 | `<base>` / `<tip>`, the report commit on top, the commit list | `BASE`, `TIP`, `## RECORDS` | CARD |
| 38:6 | `<packet ceiling>` = 300,000 B and how it was measured | P | DROPPED |
| 38:7 | `<report>` | `REPORT` | CARD |
| 38:8 | `<class>`, `<r2>`, `<r1>`, `<c4>`: the reports the check reads | `## READ` | CARD |
| 38:10 | title: which round, which range, which rule | `JOB`, `BASE`, `TIP`, `## ROWS` (L3: no `ROUND`) | CARD |
| 38:12 | heading: AUTHORIZATION, PREFLIGHT, REPORT, §2, §3, §4 | L3: `## AUTHORIZATION`, `## PREFLIGHT`, `## REPORT`; the old §2 (launch the seats) is `## 1` (5), `## 3` and `## PASS 2`, §3 (collate) is `## 7`, §4 (close) is `## 8` | CHECK |
| 38:13a | "`21`'s blocks of those names bind UNCHANGED with these substitutions" | W: every section written whole (L3: `## 1`–`## 8` and `## PASS 2`) | CHECK |
| 38:13b | the substitutions: worktree, scratch folder, report path, the build prompt's name | `WORKTREE`, `CHECK REPORT`, `JOB` (the scratch folder `<S>` is derived in the hub file) | CARD |
| 38:13c | the built-line start, the closing line, the `ready for …` literal, the table columns | fixed once for every check: `BUILT · job:`, `ready:` (L3 CHANGED: a house closes with `FINDINGS: <n>`, the check with `CHECK DONE · job: <JOB> · pass: <1|2>`; the per-question table is the `## OWN FINDINGS`, `## Findings` and `## RUNS` sections) | CHECK |
| 38:13d | THIS LAUNCH is the desk's row, found by the same greps | L2 CHANGED (G): no launch row is read; `## AUTHORIZATION` proves the card is committed and unchanged | CHECK |
| 38:13e | the row carries `<build stop>`, the dev-vault listing, the literal `no other house hub is running` | K (the three literals a launch row missed on 2026-09-29) | DROPPED |
| 38:13f | his ruling R35, proved by its row and by two quoted phrases | `## AUTHORIZATION`, every row of `RULINGS` by number + commit; the quoted phrases are K | CHECK |
| 38:13g | THE COPY STRINGS: his R85 / R88, the four `Bash(cp` lines proved | P | DROPPED |
| 38:13h | the classification's stop line with `OWNER ITEM: 0` | K as a literal; the condition is the card's (WHO FILLS IT) | DROPPED |
| 38:13i | not copied or staged: his vault notes, his template, the dev vault's notes | `## 1` (3), last sentence (L2: LAWS.md is no longer copied either) | CHECK |
| 38:14a | THE SOL SWAP: the Sol probe; Astra never probed; the floor's wording | `## PREFLIGHT` THE SOL PROBE; `## THE FLOW AND THE SEATS`, SEAT ORDER (L3: the probe decides who is house A; no Opus probe — the session is the Opus seat) | CHECK |
| 38:14b | the Sol seat line, taken from a third prompt with substitutions | W: `## 1` (5), SOL, typed whole (L3; the sentence asks for findings in runnable form) | CHECK |
| 38:14c | OPUS and GROK as `21` §2, with the folder | W: GROK `## 1` (5), typed whole; OPUS: L3 CHANGED — there is no Opus seat line: the check session itself is the fresh Opus (`## LAUNCH`, `## 2`, `## 4`–`## 6`) | CHECK |
| 38:14d | OPUS gets an extra `--add-dir` for round 1's `cp` folder; GROK is told where the four `cp` documents are | P: every file Grok needs is under `<S>/files/` (`## 1` (3)); Opus reads originals | DROPPED |
| 38:16 | heading: STAGING THIS RUN (R85 / R88) | P; what is still copied is `## 1` | DROPPED |
| 38:17 | THE FOUR COPIES by `cp`, each its own call, into round 1's folder, with the `wc -c` proof | P; the four documents reach Grok by Read → Write (`## 1` (3)); which documents is the card's `## READ` | DROPPED |
| 38:18 | every other copy: Read → Write byte-identical, parts ≤ 38,000 B cut at a heading | `## 1` (3) (CHANGED: whole files; ordered parts only after a whole Write failed — R42) | CHECK |
| 38:19 | a copy refused or failing → `FAILED: copy`; never a question, a wait or a skipped file | `## 1` (3); `## UNATTENDED RULES` | CHECK |
| 38:21a | (1) the diff of the range, whole, `src/` and `tests/` | `## 1` (1) | CHECK |
| 38:21b | (2) `rulings.md`: the grep of each ruling row | `## 1` (2); which rows is `RULINGS` and `## RECORDS` | CHECK |
| 38:21c | (2b) `packet.md`: seven report sections copied under a ceiling | P: the seats read the build report whole | DROPPED |
| 38:21d | the files copied for Grok: the reports, the build prompt, the touched files, four read-only files | `## 1` (3); the job's own list is `## READ` | CHECK |
| 38:21e | the "Files:" paragraph of the instructions file | `## 1` (4) | CHECK |
| 38:22a | §3, the hub's own checks (i), (ii): the commits and the path union | L3: `## 7` (i), (ii) (over the check's own commits as well) | CHECK |
| 38:22b | (iii) no commit under `vaultwrite/`; (iv) the helper's definition and one call | `## NOT IN THIS JOB` and `## ROWS`; run by `## 7` (iii), (iv) | CARD |
| 38:22c | (v) the dev-vault notes' sizes and times equal the listing | `## RECORDS`; run by `## 7` (vii) | CARD |
| 38:22d | (vi) L32 | L3: `## 7` (viii) | CHECK |
| 38:23 | COUNTING (K24): a finding counts only on a failing test, a command, or a diff line; X3 never counted | L3: a finding counts only when the check RAN it and it held (`## 4`; `## 7`, COUNTING); a diff line alone no longer counts; a claim with nothing runnable is dropped (`## 3`, THE DROP) | CHECK |
| 38:24a | X3 as classified: out of scope, owed as its own item | `## NOT IN THIS JOB`, `## CHECK ASKS` | CARD |
| 38:24b | for each NO, record whether it is "X3 alone" | L3: no house answers YES or NO; `## 7`, COUNTING, last sentence lists an out-of-scope item `OUT OF SCOPE`, never open | CHECK |
| 38:24c | the standing ESCALATE line: the round, the seats, what loops, the deploy set | L3: `## 8`, the standing line, under `## RECORDS` (the pass, its house; nothing loops after the second pass) | CHECK |
| 38:25 | the stop line; when `ready` is YES; the in-progress last line | `## STOP LINE` (L3 CHANGED: one line per pass — `CHECK DONE · job · pass · tip · house A (pass 2: house B) · findings · dropped · held · fixed · held unfixed · open · house B: needed / not needed / none available · suites · files opened · ready · decisions`; the token total is the desk's measurement); `## RECOVERY`, `## REPORT` | CHECK |
| 38:27 | QUESTIONS: you are one of three houses, round 3; read whole; cite real lines; mask real values | L2: `## 1`, HOUSE TEXT, first paragraph and the CLAIM / `<value>` lines | CHECK |
| 38:28a | THE FIX: what round 2 found, what the build built, what is out of scope | `## ROWS`, `## NOT IN THIS JOB`, `## RECORDS`, copied whole into the instructions file | CARD |
| 38:28b | the rows are the rules; the claims are the report and `packet.md`; what counts as a finding | L2: HOUSE TEXT, THE JOB and the FINDING form (the packet is P: the report itself) | CHECK |
| 38:29 | FOR EACH: HOLDS / DOES NOT HOLD / NOT CHECKABLE FROM READS | L2 CHANGED: a house gives no verdict word; it hands over a TEST or a COMMAND with what to EXPECT; the verdict per finding is the check session's, from its run: `HELD` / `NOT HELD` / `REJECTED` / `UNSETTLED` (L3: `## 4`) | CHECK |
| 38:30 | (i) RED FIRST, with this job's reds and mutations named | L2: HOUSE TEXT, WHAT TO LOOK FOR (1); the named reds are `## ROWS` | CHECK |
| 38:31 | (ii) B1: every byte, every caller path, the refusal, `vaultwrite/` untouched | L2: HOUSE TEXT, WHAT TO LOOK FOR (2), (4); the clauses are `## ROWS` and `## NOT IN THIS JOB` | CHECK |
| 38:32a | (iii) the run, the suites, `.env` gone, the self-check, nothing widened | L2: HOUSE TEXT, WHAT TO LOOK FOR (3), (4); the suites and `.env` are also the check's own reads (L3: `## 6`, `## 7` (v)) | CHECK |
| 38:32b | `ready for the deploy set: YES|NO`; `NO — X3 alone` | `## CHECK ASKS` (the out-of-scope ask) | CARD |
| 38:33 | THEN (a) weak assertions, (b) a path to a score; "differently" is not a finding; the closing line | L2: HOUSE TEXT, WHAT TO LOOK FOR (5), (6), and its last lines (the closing line is `FINDINGS: <n>`) | CHECK |
| 38:2, 9, 11, 15, 20, 26 | 6 blank lines | — | BLANK |

## `45` — the deploy (192 lines), lines 1–88

| ref | what it says | where it lives now | home |
|---|---|---|---|
| 45:1a | MODEL Opus; L29 write path: a production migration, a `cobalt_dev` forward and rollback | header (which migration is `MIGRATIONS`) | DEPLOY |
| 45:1b | SEAT name; launched ONCE by the desk in the background | header (`deploy-hub-<JOB>`) | DEPLOY |
| 45:1c | launched only after the day's first deploy landed | `## MARKERS` (the `before` reads prove what production carries) | CARD |
| 45:1d | fresh; `acceptEdits`; never `bypassPermissions`; push denied; an unlisted command opens a dialog | header (L4 CHANGED: `dontAsk`; an unlisted command is refused with no dialog, scratch item 9; the file tools are allow strings) | DEPLOY |
| 45:1e | the NO list: settings load … `launchctl` on any other label | header | DEPLOY |
| 45:1f | STANDING (his R10): the pause and the restart window bind nothing until he says so | H (L3): the override ended 2026-09-30 (`cto-2026-09-30.md` R44); L66 and L43 bind again; STEP-0 P1 (iv) admits only his per-case override for one deploy (L73) | DROPPED |
| 45:1g | METER; nobody at the terminal; a written `FAILED:` stops the run safely | header | DEPLOY |
| 45:3 | heading: the desk's bare commands | `## LAUNCH` | DEPLOY |
| 45:4 | (0) `worktree add` of the gate branch on `main`, after the launch row is committed | `## LAUNCH` (0) (L2: RUN by the script, after the CARD is committed; no launch row is read) | DEPLOY |
| 45:5 | (1) `cd /Users/cobalt/cobalt` | `## LAUNCH` (1) | DEPLOY |
| 45:6 | (2) the launch line: 50 allow, 3 deny, three `--add-dir` | `## LAUNCH`, the one `claude --bg` line (CHANGED: `--name` added; `--add-dir /Users/cobalt/cobalt` added; the head merge and the three production-DB strings filled by the script) | DEPLOY |
| 45:8a | THE LIST against two earlier prompts: 50 allow, no new string | S; §3 of the list | LIST |
| 45:8b | his approval is two rows; nothing in this file is an approval | `## AUTHORIZATION`, first sentence | DEPLOY |
| 45:10 | title: which set, which migration, gated on `main`'s tip | `JOB`, `SET`, `MIGRATIONS` | CARD |
| 45:12a | LADDER; his word, three rows | `LADDER`, `RULINGS` (L2: a deploy with nothing carried says `RULINGS: none`; its approval is the standing rule, DEPLOY `## AUTHORIZATION`) | CARD |
| 45:12b | an open defect ships as it stands by his ruling; its fix is the next build | `## RECORDS`; the ruling row is in `RULINGS` (STEP-0 P2) | CARD |
| 45:12c | the seam was resolved before this run; this run resolves nothing; a conflict is a stop | rule B; STEP-T | DEPLOY |
| 45:14 | WHAT SHIPS; every value re-read at run time | `## SHIPS`; the re-read is STEP-0 P3 | CARD |
| 45:15 | table header | `## SHIPS` | CARD |
| 45:16 | table rule | `## SHIPS` | CARD |
| 45:17 | row: branch C1, tip, base, check stop, report | `## SHIPS` | CARD |
| 45:18 | row: branch C2 | `## SHIPS` | CARD |
| 45:19 | row: branch C3 | `## SHIPS` | CARD |
| 45:20 | row: branch C4, its head one report commit above the tip | `## SHIPS` (code tip and branch head are two columns) | CARD |
| 45:21 | row: the seam branch | `## SHIPS`, `TIP` | CARD |
| 45:22 | the C4 check's stop line, whole; its held defect ships by his ruling | `## SHIPS` last column (the literals), `RULINGS` | CARD |
| 45:23a | the set's code is one stack; an earlier deploy is an ancestor of `main` | `## RECORDS` | CARD |
| 45:23b | `Already up to date.` is a result, never a failure | STEP-T | DEPLOY |
| 45:24 | MIGRATIONS in `FORWARD` order; production's level | `MIGRATIONS` | CARD |
| 45:25 | LIVE = `main` at the earlier deploy's stop line | `## MARKERS`, `before` | CARD |
| 45:27 | heading: the launch-time values | `«FILL` tokens | CARD |
| 45:28 | `<main base>`, read by the desk at (0) | STEP-0 P5: the hub records `<m0>` itself (`BASE: main`) | DEPLOY |
| 45:29 | the launch row | L2 (G): the card field is dropped; the desk's §4 row is the desk's own record (L34) | DROPPED |
| 45:30 | `<built tip>` | `## SHIPS`, code tip | CARD |
| 45:31 | `<seam tip>`, also written into the merge string | `TIP`; the script writes it into the line | CARD |
| 45:32 | `<set>` | `SET` | CARD |
| 45:34 | AUTHORIZATION: the desk wrote it from a drafter seat; each check its own call | `## AUTHORIZATION` | DEPLOY |
| 45:35 | his ruling R9: ONE row carrying `HIS RULING` and `APPROVED`, committed | `## AUTHORIZATION`, every row of `RULINGS` (L2 CHANGED, gap 4: no row of his per deploy; the standing rule — clean checks and a green gate — proved by his 2026-09-30 R38; a row only for a carried held defect) | DEPLOY |
| 45:36 | his ruling R10, the same, also carrying `STANDING` | `## AUTHORIZATION` (the third literal is K) | DEPLOY |
| 45:37a | THIS LAUNCH is the desk's row; it names this file; the commit proves it | L2 CHANGED (G): no launch row is read; `## AUTHORIZATION` proves the card is committed and unchanged | DEPLOY |
| 45:37b | the row carries the literal `LOCK: no with-DB run in flight` | K; the lock is proved by `ls` (STEP-0 P4) and refused by the script | DROPPED |
| 45:38 | YOU CAN ALWAYS STOP; the three asymmetries | `## AUTHORIZATION`, last lines | DEPLOY |
| 45:40 | PLACEHOLDER GATE, the first thing you do | `## AUTHORIZATION`: INSTALLED, THE CARD | DEPLOY |
| 45:41 | the two greps | `## AUTHORIZATION` (the `«INSTAL[L]` grep on the hub file, the `«FIL[L]` grep on the card) | DEPLOY |
| 45:42 | each prints nothing, exit 1; a hit = `FAILED: placeholder`, nothing touched | `## AUTHORIZATION` | DEPLOY |
| 45:44 | INDEX CARD: read in this order, nothing more until a step needs it | `## LAWS` | DEPLOY |
| 45:45 | (1) LAWS Preamble, Index, eleven entries | `## LAWS` (L2 CHANGED by R38, gap 9: the read of Preamble + Index is STRUCK; one line per law stays, an entry opened only when acted on) | DEPLOY |
| 45:46 | (2) an earlier deploy prompt, STEP-4 → STEP-7, "the shape this file copies" | W | DROPPED |
| 45:47 | (3) two earlier deploy reports' Smoke, ESCALATE and Deploy table | W: what they taught is rules A–F, the carried baseline, the one resume | DROPPED |
| 45:48 | (4) a build report's W section, "the gate's commands" | W: STEP-G types every command | DROPPED |
| 45:49 | (5) the seam build's report: headline, file list, stop line | `## SHIPS`, the row's report; carried by `## RECORDS` | CARD |
| 45:51a | the report path and title | `REPORT` | CARD |
| 45:51b | the report must not exist at start; if it does, `FAILED: relaunch` | `## REPORT`, A FIRST LAUNCH | DEPLOY |
| 45:51c | EXCEPT `CONTINUE: STEP-D0`: checks (a)–(d); what is re-run and what is not; never STEP-4 or later | `## REPORT`, THE ONE RESUME (CHANGED: check (e) reads the residents and restores them first; an earlier main-into-gate merge above `<m1>` is accepted with a docs-only proof; L2, gap 7: (e) is read FIRST, and a hub the desk stopped hung after its bootout is resumable from the in-progress line) | DEPLOY |
| 45:51d | the attempt's own values in that rule (a gate commit, two row numbers) | H: the rule reads `<m1>` from the report | DROPPED |
| 45:52 | the report's sections; the writing rules | `## REPORT` (CHANGED: `## RESTARTS` before `## L68 GATE`; L2: `## DECISIONS` and `## RECORDS` in place of the ESCALATE section); `## LAWS` | DEPLOY |
| 45:53 | the in-progress last line; where `next:` lives; no other line starts DEPLOYED / FAILED / CONTINUE | `## REPORT` | DEPLOY |
| 45:54a | commits on `main`: a FAILED ending, D2.0, STEP-7, each by explicit path; no other | `## REPORT` | DEPLOY |
| 45:54b | the desk holds its commits and stages nothing from launch to stop line | enforced, not asked: the guard refuses the commit; `DEPLOY-HUB.md` `## LAUNCH` states it | GUARD |
| 45:56 | heading: UNATTENDED RULES | `## UNATTENDED RULES` | DEPLOY |
| 45:57 | one command per call; no pipe, redirect, `&&`; only the three listed `VAR=` prefixes | `## UNATTENDED RULES` | DEPLOY |
| 45:58 | git is always `git -C <absolute path>`; grep patterns | `## UNATTENDED RULES` | DEPLOY |
| 45:59 | the report by Write / Edit; no sleep: background runs, `date` + heartbeat pairs | `## UNATTENDED RULES` | DEPLOY |
| 45:60 | the four long commands in the foreground with `timeout` 600000 | `## UNATTENDED RULES` | DEPLOY |
| 45:61 | CWD rules; `ls -la` of `.env` before every pytest or dev call; never print `.env` | `## UNATTENDED RULES` | DEPLOY |
| 45:62 | a mid-run denial = the run failed; abort, release or restore first | `## UNATTENDED RULES`; rule D (L3: a deploy never continues by message; outside the outage a refused command the hub added itself is a record; inside the outage the strict rule stays) | DEPLOY |
| 45:63 | `ASK DESK` under ESCALATE, safe default, continue | `## UNATTENDED RULES` (L2: under `## DECISIONS`) | DEPLOY |
| 45:65 | THE FIXED SQL READS, typed exactly, no `%` | `## UNATTENDED RULES` (no `%`); the script refuses a `%` in a card's query | DEPLOY |
| 45:66 | `<FP>`, the `cobalt_dev` fingerprint | after `## UNATTENDED RULES`, typed whole | DEPLOY |
| 45:67 | `<RB>`, the production read-back, with its before and after answers | `## READ-BACK` | CARD |
| 45:68 | a refused read = FAILED, never re-typed | `## UNATTENDED RULES` | DEPLOY |
| 45:70 | STEP-0 PREFLIGHT, one row per rule | `## STEP-0` | DEPLOY |
| 45:71 | P0: the placeholder gate, the authorization proofs | P0 | DEPLOY |
| 45:72 | P1 DATE: any hour is lawful (his R10) | P1 (CHANGED: the window is L66's; L2, gap 3: also L43's overnight idle before 04:00 ET and a non-trading day, re-read at D2.6; L3: any other hour only on his per-case override for that one deploy, L73 — the standing R10 ended) | DEPLOY |
| 45:73a | P1b: the earlier deploy landed — its tip is an ancestor of `main` | `## MARKERS`, `before` (STEP-0 P6) | CARD |
| 45:73b | P1b: that deploy's report last line, its tag, its report commit | H: a proof for the second deploy of one day; the markers read production itself | DROPPED |
| 45:74a | P2: each check report's last line, committed, clean | STEP-0 P2 | DEPLOY |
| 45:74b | P2: the seam BUILD's stop line (built, suite `/0`) | STEP-0 P2 (CHANGED: every `## SHIPS` row needs a CHECK report, L67; a build's stop line alone does not pass) | DEPLOY |
| 45:75a | P3: every tip re-read; the head equals its value; docs-only above the code tip | STEP-0 P3 | DEPLOY |
| 45:75b | P3: this set's own ancestry facts (which tip is under which) | `## SHIPS`, `## RECORDS` | CARD |
| 45:76 | P4: the lock | STEP-0 P4 | DEPLOY |
| 45:77 | P5: `.clinerules` absent from `rules.yaml` and from the diff | H: an owed item of 2026-09-28; STEP-R's table is the gate for every unclassified path | DROPPED |
| 45:78 | P6: the gate worktree is clean, on its branch, at the cut (or at an earlier attempt's merge) | STEP-0 P5; the resume case is `## REPORT` check (c) | DEPLOY |
| 45:79 | P7: production is at the earlier deploy and does not carry the set | STEP-0 P6; the reads are `## MARKERS` | DEPLOY |
| 45:80 | `next: STEP-T` | STEP-0 | DEPLOY |
| 45:82 | STEP-T: one merge of the tip into the gate; no conflict resolution | `## STEP-T` | DEPLOY |
| 45:83 | the merge command and its two lawful answers; `<m1>` | STEP-T | DEPLOY |
| 45:84 | a conflict: quote the paths, `merge --abort`, FAILED | STEP-T | DEPLOY |
| 45:85a | after the merge: `--merges --first-parent`; each tip an ancestor; the migration diff; the registry grep | STEP-T | DEPLOY |
| 45:85b | which code commits stand under which checked tips; the docs-only proofs | `## SHIPS` (code tip / head); proved at STEP-0 P3 | CARD |
| 45:85c | the `ops` diff prints nothing | `## STEP-C` (CHANGED: read before the suites; a plist change stops or is owed) | DEPLOY |
| 45:85d | the migration list: which commit carries the migration | STEP-0 P7 | DEPLOY |
| 45:86 | THE SEAM AS BUILT: `show --stat`, quoted beside the seam report's list | `## RECORDS` (carried into the deploy report's ESCALATE) | CARD |
| 45:87 | `next: STEP-G` | STEP-T (CHANGED: next is STEP-C, then STEP-R, then STEP-G) | DEPLOY |
| 45:2, 7, 9, 11, 13, 26, 33, 39, 43, 50, 55, 64, 69, 81, 88 | 15 blank lines | — | BLANK |

## `45` — the deploy, lines 89–192

| ref | what it says | where it lives now | home |
|---|---|---|---|
| 45:89 | STEP-G: the three suites "exactly as" a build report's W executed them | `## STEP-G` (W: every command typed whole) | DEPLOY |
| 45:90 | (a0) the early offline read of sixteen files | G (a0) | DEPLOY |
| 45:91 | (a) offline, background, `0 failed`, `0 errors` (the context counts are N) | G (a) | DEPLOY |
| 45:92 | (b) the lock; `<F0>` (its expected value is N); proof-only at `0013` | G (b) and the line after (d2) | DEPLOY |
| 45:93 | (c) pass 1 at `0013`, byte for byte, background | G (c) | DEPLOY |
| 45:94 | the pass-1 command, fourteen `--deselect` | G (c), typed whole | DEPLOY |
| 45:95a | gate: `0 failed`, `0 errors`; the allowed skip set; any other skip is red | G (c) (CHANGED: the set is named by test and reason; a moved line is inside it) | DEPLOY |
| 45:95b | no SKIPPED or FAILED line names a `test_drc_` file | N: covered by "any other skip = red" and `0 failed` | DROPPED |
| 45:96 | (c2) forward: every migration in `FORWARD` order, no `CHANGED`; record APPLIED; `<F1>` | G (c2); the created objects are `MIGRATIONS` | DEPLOY |
| 45:97 | (c3) pass 2, byte for byte | G (c3) | DEPLOY |
| 45:98 | the pass-2 command | G (c3), typed whole | DEPLOY |
| 45:99 | gate; `<d>`; the named-cursor count is information | G (c3) | DEPLOY |
| 45:100 | (d2) validate with `.env` in; any violation → (f) first, FAILED | G (d2) (CHANGED: first thing inside the lock) | DEPLOY |
| 45:101 | (f) the L76 release: rollback, `F2 = F0`, `rm`, the two `ls` | G (f) | DEPLOY |
| 45:102 | (e) live-note, no `.env`; the known skip | G (e) | DEPLOY |
| 45:103 | a red anywhere: name it, (f), `cd` back, FAILED; never "known"; no fix commit | G, last bullets; rule B | DEPLOY |
| 45:105 | STEP-R RESTARTS | `## STEP-R` (CHANGED: before STEP-G, rule C) | DEPLOY |
| 45:106 | the command, the table whole | STEP-R | DEPLOY |
| 45:107 | the gate: exit 0, no UNCLASSIFIED row, the set within three labels; else FAILED | STEP-R | DEPLOY |
| 45:108 | EXPECTED: aset and radar (the table overrules) | N: "never copy an expectation from an earlier deploy" (STEP-R) | DROPPED |
| 45:109 | `cd` back; `ls` of `.env`; write the two sections; `next: STEP-D0` | STEP-R and STEP-G, last lines | DEPLOY |
| 45:111 | STEP-D0: nothing in production changes | `## STEP-D0` | DEPLOY |
| 45:112 | MAIN: the branch, the accepted dirt, the refused dirt, docs-only since the cut | D0 | DEPLOY |
| 45:113 | ALLOWLIST PROBE: a tag and its delete, an empty commit and its reset | D0 (the tag is named from `JOB`) | DEPLOY |
| 45:114 | TAG NAMES: both free | D0 (CHANGED: on a resume the hub deletes the earlier attempt's rollback tag itself) | DEPLOY |
| 45:116 | STEP-D1: the production baseline | `## STEP-D1` | DEPLOY |
| 45:117a | the heartbeat; an aset or radar RED stops; THE CARRIED KIND is a baseline | D1, THE CARRIED-BASELINE RULE (the family with its stale clauses) | DEPLOY |
| 45:117b | what earlier attempts read, quoted | H | DROPPED |
| 45:118 | validate; backup status | D1 | DEPLOY |
| 45:119 | the residents' state and pids; the agent ONLINE; not running = FAILED | D1; the loaded `path =` proof is STEP-0 P8 | DEPLOY |
| 45:120 | the radar tail; the eight log baselines | D1 | DEPLOY |
| 45:121 | the `/radar` curl; the markers again | D1 | DEPLOY |
| 45:122 | `<RB>` exactly its before answer | D1 (with a migration); the answer is `## READ-BACK` | DEPLOY |
| 45:123 | the census before: two counts | `## SMOKE READS`, the `census` lines; read at D1 | CARD |
| 45:124 | D1-M: the production proof-only | D1 (with a migration) | DEPLOY |
| 45:126 | STEP-D2: `main` into the gate, docs-only proof, snapshot, rollback tag | `## STEP-D2` | DEPLOY |
| 45:127 | D2.0 commit the report; `<pre-merge>` | D2.0 | DEPLOY |
| 45:128 | D2.1 merge `main`; a conflict = FAILED | D2.1 | DEPLOY |
| 45:129 | D2.2 `<stack-final>`, its two parents | D2.2 (CHANGED: `^1` may be an earlier attempt's merge; `<m1>` must be an ancestor) | DEPLOY |
| 45:130 | D2.3 docs-only proof | D2.3 | DEPLOY |
| 45:131 | D2.4 snapshot | D2.4 | DEPLOY |
| 45:132 | D2.5 second heartbeat, ≥100 s later; the carried family is not new | D2.5 (≥110 s) | DEPLOY |
| 45:133a | D2.6 the rollback tag; `next: STEP-4` | D2.6 (the resume point never is STEP-4) | DEPLOY |
| 45:133b | "No report prose until STEP-4 ends" | CHANGED: the outage line is written BEFORE the outage (rule F, L48), the outage rows right after 4.6 | DEPLOY |
| 45:135 | STEP-4: the outage, exactly these calls in this order | `## STEP-4` (on the labels of the restart set only) | DEPLOY |
| 45:136 | 4.1 `date` | 4.1 | DEPLOY |
| 45:137 | 4.2 the two bootouts, proved gone; the agent stopped | 4.2 | DEPLOY |
| 45:138 | 4.3 HEAD = `<pre-merge>`; the fast-forward; a refusal → 4.6 | 4.3 | DEPLOY |
| 45:139 | 4.4 the production migration; the proof table; `<RB>` after; any fault → STEP-5 | 4.4 (the objects and answers are the card's) | DEPLOY |
| 45:140 | 4.5 validate | 4.5 | DEPLOY |
| 45:141 | 4.6 bootstrap, kickstart, one retry each; `<t up>`; downtime over 300 s escalated | 4.6 | DEPLOY |
| 45:143 | STEP-4.7 SMOKE: `date` before each row; a red row → STEP-5 | `## STEP-4.7` | DEPLOY |
| 45:144 | first calls: the four failure counts | 4.7, first calls | DEPLOY |
| 45:145 | (a) residents running with new pids; the agent ONLINE | (a) | DEPLOY |
| 45:146 | (b) the server-start count, the tail, the traceback counts, the three spaced radar tails | (b) | DEPLOY |
| 45:147 | (c) the three `200` reads | (c) | DEPLOY |
| 45:148 | (d) MARKERS: the migration file listed, the helper present | (d); the reads are `## MARKERS`, `after` | CARD |
| 45:149 | (e) two heartbeats; no new RED; the carried family is not new | (e) | DEPLOY |
| 45:150 | (f) validate; `jobs restarts` on the landed range | (f) | DEPLOY |
| 45:151 | (g) `<RB>` its after answer | (g); the answer is `## READ-BACK` | DEPLOY |
| 45:152 | (s) the set's four smoke reads | (s) | DEPLOY |
| 45:153 | the C1 read | `## SMOKE READS` | CARD |
| 45:154 | the C2 read | `## SMOKE READS` | CARD |
| 45:155 | the C3 read | `## SMOKE READS` | CARD |
| 45:156 | the C4 read | `## SMOKE READS` | CARD |
| 45:157 | (h) REVERT-READBACK: the counts did not grow; the curl; the census again | (h) | DEPLOY |
| 45:158 | THE CHAIN, written in `## Smoke`; the card surface is the desk's with him | 4.7, THE CHAIN | DEPLOY |
| 45:159 | RED = the list of red conditions → STEP-5 | 4.7, RED | DEPLOY |
| 45:161 | STEP-5: ONE `revert -m 2`; no schema rollback, no DB write, no vault edit | `## STEP-5` | DEPLOY |
| 45:162 | (0), (1): residents down; the four counts | STEP-5 (0), (1) | DEPLOY |
| 45:163 | (2) the one revert, proved; a conflict → abort, new code kept | STEP-5 (2) | DEPLOY |
| 45:164 | (2b) the migration stays; why the old code runs on it | STEP-5 (2b); the why is `MIGRATIONS` ("old code on the new schema") | CARD |
| 45:165 | (3) bootstrap each resident booted out; the agent | STEP-5 (3), THE RESTORE | DEPLOY |
| 45:166 | (4) re-run the smoke rows; the revert-readback; a growing count is terminal | STEP-5 (4) | DEPLOY |
| 45:167 | (5) the last line; STEP-5 is never entered twice | STEP-5 (5) | DEPLOY |
| 45:169 | THE ROLLBACK STRING: written into the deploy table; the desk's | THE ROLLBACK STRING | DEPLOY |
| 45:170 | 1 CODE: one revert; residents down first (the earlier deploy stays: H) | string 1 | DEPLOY |
| 45:171 | 2 SCHEMA: a separate desk job on his word, down to production's earlier level | string 2 (the level is `MIGRATIONS`) | DEPLOY |
| 45:172 | 3 RE-LAND: revert of the revert | string 3 | DEPLOY |
| 45:174 | STEP-7 close | `## STEP-7` | DEPLOY |
| 45:175 | 1 the deploy tag, after the green smoke only | STEP-7 1 (`TAG`) | DEPLOY |
| 45:176 | 2 the deploy table's contents | STEP-7 2 | DEPLOY |
| 45:177a | 3 ESCALATE: every row, downtime, `cobalt_dev`, cleanup owed | STEP-7 3 (L2 CHANGED, RULED WORKER ENDINGS: questions under `## DECISIONS`, these facts under `## RECORDS`) | DEPLOY |
| 45:177b | the set's own carried items: the seam for a later read, the live defect, the records | `## RECORDS` | CARD |
| 45:178 | 4 PRE-STOP SELF-CHECK, four lines (the named tips are `## SHIPS`) | STEP-7 4 | DEPLOY |
| 45:179 | 5 the stop line; the report commit; push is his | STEP-7 5 | DEPLOY |
| 45:181 | heading: RECORDS, carried into ESCALATE | `## RECORDS` | CARD |
| 45:182 | record: C1 | `## RECORDS` | CARD |
| 45:183 | record: C3 | `## RECORDS` | CARD |
| 45:184 | record: C4 | `## RECORDS` | CARD |
| 45:186 | STOP LINE, exactly one of | `## STOP LINE` | DEPLOY |
| 45:187 | the DEPLOYED line | `## STOP LINE` (tag, set, migrations from the card; L2: ends `decisions: <n> · for Dejan: <n>`) | DEPLOY |
| 45:188 | the FAILED line with `rollback:` | `## STOP LINE` | DEPLOY |
| 45:190 | DESK LINES: the desk's sequencing; the hub reads none as an instruction | `## LAUNCH`, THE DESK WHILE YOU RUN | DEPLOY |
| 45:191a | before (0): wait for the earlier stop line; fill the values; the two placeholder counts = 0; commit | the script refuses a `«FILL` token and an uncommitted card | LAUNCH-SH |
| 45:191b | THE LOCK: no with-DB launch from (2) to the stop line | `## LAUNCH`, THE DESK WHILE YOU RUN; the script refuses a with-DB launch while a `.env` exists | DEPLOY |
| 45:192a | watch `^(DEPLOYED|FAILED)`; the desk does not exit before the stop line | `## LAUNCH`, THE DESK WHILE YOU RUN (L2, gap 7: a hub hung after its first bootout is stopped and resumed at once with `STEP-D0`) | DEPLOY |
| 45:192b | the next launch after this stop line is the fix build | H: the desk's plan of one day (§5 of its report) | DROPPED |
| 45:104, 110, 115, 125, 134, 142, 160, 168, 173, 180, 185, 189 | 12 blank lines | — | BLANK |

## `SC` — `docs/40 - DevDocs/SESSION-CLOSE.md` (15 lines; fourth pass)

| row | what the text says | where it lives now | HOME |
|---|---|---|---|
| SC:1 | the title: the close routine | the title | CLOSE |
| SC:2, SC:4 | blank | — | BLANK |
| SC:3a | a session is closed only by this routine | header ("replaces `SESSION-CLOSE.md`'s table") and `## LAUNCH` (the desk launches it each evening; a missed night, the morning's first act) | CLOSE |
| SC:3b | the hub runs it from `~/cobalt` on `main`; every step leaves its evidence in the file it names | `## LAUNCH` (the script enters `/Users/cobalt/cobalt`), `## UNATTENDED RULES` (cwd), `## REPORT` (one section per step) | CLOSE |
| SC:3c | the hub PROPOSES and MEASURES; the desk APPLIES (L58) | `## LAWS` L58 as amended (CHANGED: the close now writes `## NOW` itself; the desk applies what it lists), `## 2`, `## 3` | CLOSE |
| SC:3d | memory rules: INDEX `rules:` and [[writing-rules]] | `## LAWS`, "Report prose: … `writing-rules.md`" (CHANGED: INDEX `rules:` is not named — the close writes no tagged memory line; NOW is a snapshot, L58) | CLOSE |
| SC:5–6 | the table's header and rule line | — (W: the steps are written whole as sections) | DROPPED |
| SC:7 | step 1, ledger appendix | `## 1 LEDGER APPENDIX` | CLOSE |
| SC:8 | step 2, laws fold: every candidate, his words, the fold text; the desk folds | `## 2` (CHANGED, reduced: only a ruling still `APPROVED — pending fold`); the desk's fold procedure stays in LAWS `## Fold at session close` (row 51) | CLOSE |
| SC:9 | step 2a, lessons gate: audit, OWED list, the boundary | `## 3` (CHANGED, reduced: only a lesson no fixed file or checklist rule carries; no audit boundary) | CLOSE |
| SC:10 | step 4a, ladder and backlog status | `## 5 SPRINT STATUS BLOCK` | CLOSE |
| SC:11 | step 3, `## NOW` rewritten whole from live evidence, by the desk, measured | `## 6` (CHANGED: the runner is the close, L58 as amended; ≤1,500 characters measured on the written text) | CLOSE |
| SC:12 | step 4, areas/topics: the day's rulings and facts to their homes, by the desk | — (R: applied at the ruling) | DROPPED |
| SC:13 | step 5, the always-loaded block under 4,000; over = FAIL and a proposed move | `## 7` (CHANGED: over = a `## DECISIONS` item with the move, not a FAIL) | CLOSE |
| SC:14 | step 6, one commit on `main`; L51; validate exit 0 first | `## 8` (a)–(c) (CHANGED: validate ≠ 0 is a DECISION and the docs commit goes on, as `prompts/2026-09-27/99-close.md` ran it) | CLOSE |
| SC:15a | step 7, push on his word (L55) | `## 8` (d) (CHANGED: the standing nightly push, L55 as amended, `RULE-CHANGES.md` row 49) | CLOSE |
| SC:15b | the report ends `CLOSE COMMITTED <hash> · PUSH: on his word · ESCALATE: <n>` | `## STOP LINE` (CHANGED: `CLOSE PUSHED <hash> · … · decisions: <n> · for Dejan: <n>`) | CLOSE |
| SC:15c | the next opener goes in the same message | checklist `## close` `:123` as amended ("The last reply carries the next opener"), `RULE-CHANGES.md` row 53 | RULE |

## COUNTS
FOURTH PASS: the `SC` table adds 18 rows for its 15 lines (14 CLOSE, 1 RULE, 2 DROPPED, 1 BLANK row for its 2 blank lines); the three `L4` rows keep their homes. 394 rows cover 340 lines. The earlier counts below stand for the three prompts; the table under them is the whole.
Counted by `grep -c -F "| <HOME> |"` on this file, one call per home, at 11:1x ET; the draft report's check (f) quotes the calls. RECOUNTED after loop 2 (the draft-2 report's check (g)): one row moved, `45:29` from the card to DROPPED (G); the three launch-row gate rows (`37:45a`, `38:13d`, `45:37a`) keep their hub file as home, because the gate's place is taken there by the card-committed proof; every other loop-2 change alters a rule inside the same home. RECOUNTED after the third pass (the third-pass report's check (h)): two rows moved — `38:1e` from the card to `CHECK-HUB.md` (no `ROUND` field) and `45:1f` from the card to DROPPED (H: the override ended); every other third-pass change re-homes a row inside `CHECK-HUB.md`. A row is a segment. 376 rows cover the 325 lines: 372 segment rows for the 269 lines that hold text (77 + 27 + 165), and 4 BLANK rows for the 56 blank lines (23 + 6 + 15 + 12).

| home | rows |
|---|---|
| the card (`CARD.md`'s fields) | 80 |
| `BUILD-HUB.md` | 77 |
| `CHECK-HUB.md` | 37 |
| `DEPLOY-HUB.md` | 137 |
| `STANDING-LIST.md` | 5 |
| `desk-launch.sh` | 2 |
| `pre-commit-deploy-guard.sh` | 1 |
| `CLOSE-HUB.md` (fourth pass) | 14 |
| a row of `RULE-CHANGES.md` (fourth pass) | 1 |
| dropped with a reason (H, W, K, P, N, S, G or R) | 35 |
| blank | 5 |
| unhomed | 0 |
| total | 394 |

DROPPED FOR "PACKET" (reason P, his 2026-09-27 R42): `38:1h`, `38:6`, `38:13g`, `38:14d`, `38:16`, `38:17`, `38:21c` — seven rows, all in `38`.

UNHOMED: 0.

WEAK HOMES — homed, but the brain should read them: `37:55b` (the second base is dropped); `45:73b` (the earlier deploy's stop line and tag are no longer read: markers only); `45:74b` (a branch that was built and never checked can no longer ship); `38:1f` (the floor now needs the Anthropic seat); `37:83` / `45:105` (RESTARTS moved before the suites); `45:133b` (the report is written just before the outage).

WEAK HOMES ADDED BY LOOP 2 — homed, and each is a rule the old check had that the ruled flow no longer has in that form: `38:29` (the houses' three verdict words are gone; a house hands over something runnable, and only the Opus seat's run gives a verdict); `38:23` (a diff line alone no longer counts as a finding; nothing counts without a run); `38:1e` (three rounds with a classified fix round between them become one run with two Opus passes: L39's round cap and L75's classifier have no step in the fixed check); `38:24b` (no house says YES or NO, so "NO on the out-of-scope item alone" has nothing to attach to; the out-of-scope item is listed, never open); `38:14c` (the Anthropic seat is no longer a reader beside the houses: it is the session that runs and fixes).

WEAK HOMES ADDED BY THE THIRD PASS: `38:1j` (the check's "no pytest, no git write" is reversed: the check session is the write path); `38:1a` (the hub that "gives no verdict" is gone: the session that judges a finding is the one that ran it, and the one that fixes it); `38:1g` (the check no longer starts in `agy-trial`; it `cd`s there only to start a house); `45:1f` (a standing window override has no home: L73 allows none).
