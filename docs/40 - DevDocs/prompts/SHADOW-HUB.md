INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED

MODEL: Opus 5.5 (`claude-opus-5-5`; L29: the with-DB gate is a DB write path) · PERMISSION MODE `dontAsk`, never `auto`, never a bypass · SEAT: the gate seat `<job>-gate`, a FRESH session launched by the CTO desk with `sh /Users/cobalt/.claude/ops/desk-launch.sh shadow "<card>" --model <id>`. You are never the builder (the model of `MODEL:` in your launch message) and never the check (a separate fresh Opus under `CHECK-HUB.md`) · nobody sits at this terminal: the report is your channel, as in BUILD-HUB.

This file is the same for every shadow build. Your values are in the shadow card (`CARD:` in your launch message, a copy of an original card with `SHADOW OF: <original card>`, FINAL §2.2 step 1, `[F-18]`) and in the one row of `## BUILDERS` that `MODEL:` names. You run every command; the model only writes files.

## THE LINE (the launcher fills `<card>`, `<job>`, `<worktree>`, `<model>` and `<builder allow>`; nobody types it by hand)
It is BUILD-HUB's line (`BUILD-HUB.md:12`) with this file read in BUILD-HUB's place, `MODEL: <model>` after the card, the seat `<job>-gate`, BUILD-HUB's 26 allow and 4 deny strings unchanged, and ONE more token, `<builder allow>`: the `builder allow` string of `--model`'s row, quoted.

claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md' and follow it exactly. CARD: '<card>' MODEL: <model>" --model claude-opus-5-5 --permission-mode dontAsk --remote-control <job>-gate --name <job>-gate --append-system-prompt "ONE bare command per Bash call: no &&, ;, |, redirect, newline or \$(…) outside quotes. A call the hook blocks is NOT A REFUSAL: resend it as single calls." --allowedTools "Read" "Grep" "Glob" "Edit(//Users/cobalt/cobalt-wt/**)" "Bash(uv run pytest *)" "Bash(uv run cobalt jobs restarts *)" "Bash(git add *)" "Bash(git commit *)" "Bash(git diff *)" "Bash(git status*)" "Bash(git log*)" "Bash(git show*)" "Bash(git -C /Users/cobalt/cobalt log*)" "Bash(git -C * diff*)" "Bash(cd *)" "Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(wc *)" "Bash(date*)" "Bash(COBALT_ENV=dev uv run pytest *)" "Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/<worktree>/.env)" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)" "Bash(sh /Users/cobalt/cobalt/ops/desk/*)" "Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)" "Bash(COBALT_ENV=dev uv run cobalt db *)" <builder allow> --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" "Bash(COBALT_ENV=production*)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt --add-dir /Users/cobalt/.claude/ops

The launcher refuses (`REFUSED:`, exit 1, nothing launched) an unsigned row, an id that is no row, a Gemini id, this file uncommitted or still carrying its install token, a card without `SHADOW OF:`, a `BRANCH` outside `shadow/`, a `JOB` that does not end in `-<slug>` of the model, and a line in any mode but `dontAsk` (once). The guard (`ops/desk/bare-guard.py`, kind `shadow`) lets ONE builder call through G7: the whole command, `--model`'s `builder command` below with `<worktree>` the card's WORKTREE and one plain double-quoted `<pass prompt>`, and only while `<worktree>/.env` does not exist. Every other launch stays G7.

## BUILDERS
One row per proven id (the card's `## RECORDS`). Three rows (R1019: no Opus and no Sol arm; Gemini N/A — id not found). Each command's write target is `/Users/cobalt/cobalt-wt/<worktree>/**` and nothing wider. Each builder allow string is a NEW COMMAND CLASS (R411): the desk replaces a row's sign mark with his row; the launcher refuses a row that still holds it.

| id | slug | builder allow | builder command | SIGN |
|---|---|---|---|---|
| `grok-4.7` | `grok` | `Bash(grok -m grok-4.7 --sandbox cobalt-job *)` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/<worktree>/**)" -p "<pass prompt>"` | 2026-10-11 R1069 · HIS RULING · APPROVED |
| `claude-sonnet-5-5` | `sonnet` | `Bash(claude -p --model claude-sonnet-5-5 *)` | `claude -p --model claude-sonnet-5-5 "<pass prompt>" --permission-mode dontAsk --output-format json --allowedTools "Read(//Users/cobalt/cobalt-wt/<worktree>/**)" "Edit(//Users/cobalt/cobalt-wt/<worktree>/**)" "Write(//Users/cobalt/cobalt-wt/<worktree>/**)" --disallowedTools "Bash" "AskUserQuestion" "EnterWorktree" "Agent" "WebFetch" "mcp__*"` | 2026-10-11 R1069 · HIS RULING · APPROVED |
| `gpt-5.6-terra` | `terra` | `Bash(codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write *)` | `codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write -C /Users/cobalt/cobalt-wt/<worktree> "<pass prompt>" < /dev/null` | 2026-10-11 R1069 · HIS RULING · APPROVED · network: off (workspace-write default; X1 proves it) |

Notes on the rows:
- Grok is FINAL §2.6's line: `--sandbox cobalt-job` (`ops/grok-sandbox.toml`: the workspace profile; `.env`, `~/.cobalt` and the agent homes denied) and ONE `--allow "Write(…)"` glob; it never carries Grok's approve-everything flag, so Grok runs no shell command (the guard denies a Grok call that carries it).
- Sonnet: `Edit(//…)` and `Write(//…)` are the absolute-path spelling of Claude Code's permission rules (`//` = from the filesystem root), the spelling of BUILD-HUB's own `Edit` string; the write target is `/Users/cobalt/cobalt-wt/<worktree>/**`. `Bash` is denied; `--output-format json` prints its token use.
- Terra: `-s workspace-write` confines writes to `-C <worktree>`; its sandbox network stays off (codex's default; no `network_access` override on the command). X1 proves both before the Terra arm runs. Whether `workspace-write` lets codex run a shell command inside its sandbox is X3's question: "writes only" for Terra rests on the sign-off and X1.

`<pass prompt>`, one double-quoted string with no `"`, `\`, `$` or backtick in it (the guard passes nothing else):
`You are <GROK (xAI) | SONNET 5.5 (Anthropic) | TERRA (OpenAI)>, building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass <T | S | S2>: <tests only under tests/ | the rows | fix the failing lines quoted under PASS S2>. Write only the rows' files. Run no command. Reply with the list of files you wrote.`

## RULES OF THE SEAT
- You run every command: BUILD-HUB's steps by their own scripts, RED FIRST, the three suites of BUILD-HUB `## RESTARTS` and `## W`, the with-DB gate under THE LOCK (L76). BUILD-HUB's UNATTENDED RULES, RECOVERY, THE LOCK and REPORT bind you as they bind a builder; where BUILD-HUB says "build the rows", the builder pass does it and you never do.
- You never edit `src/` or `tests/`. You write ONLY `/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md` and your report (the guard's G5 for kind `shadow`). A builder's red is fed back to the builder; you never repair it.
- Builder passes and gate passes never overlap: a builder runs only while no suite, no lock take and no `.env` exists; a suite starts only after the builder's call has returned.
- THE `.env` PRECONDITION (S7; L76): `.env` exists only inside your with-DB step, under the lock. Before EVERY builder pass of ANY model, `ls -la /Users/cobalt/cobalt-wt/<worktree>/.env` prints `No such file`, quoted in the report. The guard denies a builder call while `.env` (a file or a link) is in the worktree: `route: no builder pass while .env is in the worktree (the gate's with-DB step holds it)`.
- A builder call is ONE bare command, the row's command filled: `cd /Users/cobalt/cobalt-wt/<worktree>` its own call first; the builder call `run_in_background`, `timeout` 2700000 (45 minutes); its wall time from `date` before and after; its tokens from its own output where it prints them (Sonnet's JSON), else `UNKNOWN` (L70).
- Re-pass cap: 2 (pass S2, at most twice). After the second, the build stops `suites at first run: red` and is scored, not repaired (FINAL §2.2 step 6, S6).
- A red caused by the lock, the dev DB level or a missing `.env` is the harness, not the model: INCOMPLETE (`[F-31]`), never scored BELOW; the card is rerun once on a clean harness or reported INCOMPLETE.
- `git diff --stat` is quoted before EVERY commit, so the check can match each commit to a pass. A path outside the rows' files (and the original's admitted exceptions, `[F-32]`) is recorded `SCOPE` and not reverted.
- Never merged, never deployed (FINAL §2.2 step 9): no deploy card names a `shadow/` branch.

## THE PROCEDURE (BUILD-HUB's steps; only the differences are written here)
1. AUTHORIZATION: `sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "<card>"` → quoted whole; last line `AUTHORIZED`.
2. PREFLIGHT: `sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"` → quoted whole; last line `PREFLIGHT OK`. Then BUILD-HUB's other PREFLIGHT rows. The card's `SHADOW OF:` original, its RULINGS and the original build report's admitted docs and test exceptions are read here.
3. E0 BASELINE on BASE, as BUILD-HUB `## E0`.
4. THE INSTRUCTIONS (`[F-32]`): write `/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md`, never committed (X9 settles its ignored path; until then it is named in the report as the one untracked file): the WHOLE shadow card, its RULINGS rows quoted, the original build's exceptions, BUILD-HUB `## E2` and `## E3` verbatim, and the fence: the rows' files (every path a row's `files` names) plus those exceptions, nothing else. The builder's sandbox reads only its workspace, so everything it needs is copied in.

ENV CHECK before pass T: `ls -la /Users/cobalt/cobalt-wt/<worktree>/.env` → `No such file`, quoted.
pass T — the row's command with `Pass T: tests only under tests/`. Then `git diff --stat` quoted; `git add <the test paths>`; `git commit -m "wip(<job>): red" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- <paths>`; the new tests run, each red quoted with its first line. A test green before the fix is recorded, not repaired.

ENV CHECK before pass S: `ls -la /Users/cobalt/cobalt-wt/<worktree>/.env` → `No such file`, quoted.
pass S — the row's command with `Pass S: the rows`. Then `git diff --stat` quoted; `git add <paths>`; `git commit -m "feat(<job>): rows" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- <paths>`; the rows' tests → quoted.

5. RESTARTS and W: BUILD-HUB `## RESTARTS` and `## W` as they stand (`gate.sh <worktree> all --deploy …`, the lock taken and released by the gate). A red: one re-pass.

ENV CHECK before pass S2: `ls -la /Users/cobalt/cobalt-wt/<worktree>/.env` → `No such file`, quoted (the gate's (f) has removed it; `.env` present → W (f) first, never a pass).
pass S2 — the row's command with `Pass S2: fix the failing lines quoted under PASS S2`; the failing lines are written verbatim under `## PASS S2` in SHADOW-INSTRUCTIONS.md first. Then `git diff --stat` quoted; commit `fix(<job>): pass S2 <n>`; RESTARTS and W again. At most 2.

6. THE SCORED BUILD: the last commit before the check is frozen as the scored build (`[F-18]`): its hash is the report's `tip:`; any later Opus fix is the check's and is kept apart.
7. REPORT: `<WT>/docs/40 - DevDocs/reports/<job>-build-<date>.md` (the card's REPORT) in BUILD-HUB's REPORT shape, plus `## PASSES` (per pass: the env check, the command as run, wall, tokens, the diff stat, the commit). Stop line, the last non-blank line:
`SHADOW BUILT · job: <JOB> · tip: <tip> | on <BASE> | offline <p>/0 | with-DB <d>/0 | live-note <l>/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: <as derived> | decisions: <n> · builder: <id> · gate: <seat> · passes: <n> · suites at first run: <green|red> · builder tokens: <n|UNKNOWN> · wall: <minutes>`
or `FAILED: <step> — <reason>` (a harness stop: INCOMPLETE named in it).
A shadow of a "DB: none" card runs W as BUILD-HUB gives it for that card ((a0), (a), (e); no lock) and writes `with-DB 0/0` and `cobalt_dev: not taken` in those two fields.

## ROLE TRIALS (Grok only, R1016)
A shadow card whose header carries `ROLE: drafter|preflight|judge` runs ONE Grok pass with the same Grok command, its write target that card's worktree, and no gate: no suite, no lock, no commit of the model's file.
- drafter: Grok writes one card from the FINAL the card names into the worktree.
- preflight: Grok reads two preflighted cards the card names, one with a planted mismatch, and writes its verdict there.
- judge: Grok answers one past build report's `## DECISIONS` there.
You run AUTHORIZATION and PREFLIGHT, write SHADOW-INSTRUCTIONS.md (the task and the inputs copied in), the env check, the one pass, and a report quoting the file Grok wrote. Stop line: `SHADOW ROLE · <role> · builder: grok-4.7 · wall: <minutes>`.

## RESULTS TABLE
The desk copies this shape into `reports/complexity-shadow-results-2026-10-<dd>.md` and fills it from the stop lines and the shadow checks. It is a routing table by band (R1008, R1014): per band, the models that build it, so a card of that band can go to a model other than Opus 5.5. Routing takes effect only on his word on the result (L29).

- Bands, frozen (`[F-13]`): LOW 0-2 · MID 3-6 · HIGH ≥7.
- Baseline: each card's original Opus build and its check (FINAL §2.1); Opus-own held 1 / 2 / 2, distinct defects 1 / 2 / 2 (`[F-04]`).
- Harness, printed once: the originals ran their own commands; the arms write only, under an Opus gate seat
- Grades per cell, counted on Opus-own held findings over the original's (`[F-04]`, `[F-30]`, `[F-31]`): AT LEVEL (no extra held) · CLOSE BELOW (exactly one extra) · BELOW (two or more, or the model's own red after 2 re-passes) · INCOMPLETE (a harness red, not scored).
- Readings per model: CAN BUILD <band> (the highest band AT LEVEL, every lower band AT LEVEL or CLOSE BELOW) · CAN BUILD WITH A REVIEW <band> (a band CLOSE BELOW) · NOT YET <band> (a band BELOW). `NOT YET` = `not this band, on this evidence`.

| model | LOW | MID | HIGH | reading |
|---|---|---|---|---|
| Grok 4.7 (`grok-4.7`) | <cards> · <grade> · builder tokens <n or UNKNOWN> · wall <min> per build · insufficient data (n=2 per band) | same | same | <reading> |
| Sonnet 5.5 (`claude-sonnet-5-5`) | <card> · <grade> · builder tokens <n> · wall <min> · insufficient data (n=1 per band) | same | same | <reading> |
| Terra (`gpt-5.6-terra`) | <card> · <grade> · builder tokens <n or UNKNOWN> · wall <min> · insufficient data (n=1 per band), or `N/A — <where read>` | same | same | <reading> |
| Opus 5.5 | can build every band — his word, 2026-10-11 R1019, not measured | | | NOT MEASURED |
| Sol | can build every band — his word, 2026-10-11 R1019, not measured | | | NOT MEASURED |
| Gemini | N/A — id not found (`CHECK-HUB.md:92` names `gemini-3.1-pro-high`; no `gemini-4` id in `prompts/`, `ops/`, `LAWS.md`; card 324 `## RECORDS`) | | | N/A |

Per band, below the rows:
- LOW — builds it: <models AT LEVEL>; with a review: <models CLOSE BELOW>.
- MID — builds it: <models AT LEVEL>; with a review: <models CLOSE BELOW>.
- HIGH — builds it: <models AT LEVEL>; with a review: <models CLOSE BELOW>.

Grok's role rows, apart (each against the seat that did the same job):

| role | Grok's result | the seat that did the job | its result | wall |
|---|---|---|---|---|
| drafter | <its card's preflight result> | <the drafter seat> | <the real card's preflight result> | <min> |
| preflight | <caught the plant: yes or no> | <the preflight seat> | <its result> | <min> |
| judge | <its answers> | <the brain> | <the recorded answers> | <min> |

Each house's ruling on its own vendor's models is recorded apart, on its own line below the tables, and counts on no cell: Grok on Grok, Astra on Sol and Terra, the Anthropic seat on Opus and Sonnet.
