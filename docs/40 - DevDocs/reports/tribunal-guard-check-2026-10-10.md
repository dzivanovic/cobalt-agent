# tribunal-guard-1010 — CHECK (pass 1)

## §0 Headline
- Check of row T on tip `2e680273`: Sol `FINDINGS: 0`, Grok `FINDINGS: 0`; own O1-O4 run: none held, no fix, no commit.
- The three real 237 launch lines and the probe pass the guard from a tribunal seat (O1); the name pattern sorts 22 real names correctly (O2); wrapped and chained launches stay denied (O4).
- OPEN, follow-up: O3, bypass flags after a `HOUSE` prefix pass the guard (fenced by the card; X6).
- Offline 4196/0, `tests/ops` 2743 passed, live-note 146/0; DB: none; RESTARTS: none; ready: YES.

## L74
- ~09:00 ET: a system reminder after the launch message asked commits to end with a `Claude-Session: https://claude.ai/code/session_…` line. DATA (L74): recorded once, not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../prompts/2026-10-10/251-tribunal-guard-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../251-tribunal-guard-card.md" · 0 · 11fe4043eef00d6bed16958fc5b04a6b2ee6d3a5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- ".../251-tribunal-guard-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES `STANDING-LIST.md` once (`4be06af0`) ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " ".../reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing) ... | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · ... · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(paths shortened with `...` to `/Users/cobalt/cobalt/docs/40 - DevDocs`; row texts shortened here, the full rows were printed.)

House gates: `grep -n "^| R17 " ".../reports/cto-2026-09-24.md"` → `35:| R17 | 07:32 ET | ... STANDING: \`Bash(grok *)\` is a PRE-APPROVED string ...` (one row) · `grep -n "^| R19 " ...` → `37:| R19 | 07:36 ET | ... the four house strings are pre-approved ...` (one row) · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sat Oct 10 09:00:39 EDT 2026
status · git status --short --branch · 0 · ## ops/tribunal-guard-1010
head · git log --oneline -1; git log --stat --format=%h 2e680273..HEAD · 0 · (5 lines)
    8a7a938f docs(tribunal-guard-1010): build report — 2e680273
    8a7a938f

     .../reports/tribunal-guard-build-2026-10-10.md     | 146 +++++++++++++++++++++
     1 file changed, 146 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/tribunal-guard-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/aset-orphan-1010/.env
report · tail -n 3 ".../tribunal-guard-build-2026-10-10.md" · 0 · BUILT · job: tribunal-guard-1010 · tip: 2e680273 | on fccbb258 | migration: none | offline 4196/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 150795
range · git log --oneline fccbb258..2e680273 · 0 · (2 lines)
    2e680273 fix(tribunal-guard-1010): G9 lets a design-tribunal hub type the house strings (T, L67, L79)
    593e4a8e wip(tribunal-guard-1010): red — G9 tribunal hub tests (T)
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h fccbb258..2e680273` · 0 · `2e680273` `ops/desk/bare-guard.py | 12 ++++++++----` (8+, 4−) · `593e4a8e` `tests/ops/test_bare_guard.py | 62 +++…` (62+). Path union: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`.
- DB: none · `git diff --name-only --no-renames fccbb258..2e680273` · 0 · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py` — both under `ops/` / `tests/ops/`.
- `ls <S>` · 1 · `No such file or directory` → fresh.
- House probes · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · 0 · `sol: UP` · `grok: UP` · `gemini: UP`.
- house A: Sol (OpenAI, `gpt-5.6-sol`) · house B: Grok (xAI, `grok-4.7`). HOUSE B: as needed.
- Lock: a sibling (`aset-orphan-1010`) holds `.env`; this card is DB: none, the lock is not taken.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · output whole:
```
5875 <S>/diff.md
8593 <S>/files/251-tribunal-guard-card.md
17238 <S>/files/tribunal-guard-build-2026-10-10.md
45471 <S>/files/wt/ops/desk/bare-guard.py
75620 <S>/files/wt/tests/ops/test_bare_guard.py
384 <S>/rulings.md
STAGED 6 files · 153181 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/tribunal-guard-1010-check`; commits 2 = PREFLIGHT's range count.)
`stage-copy.sh` for the files `## READ` names: `COPIED 67322 <S>/files/237-f4-tribunal.md` · `COPIED 40252 <S>/files/CHECK-HUB.md` · `COPIED 21650 <S>/files/cto-2026-10-10.md` · `COPIED 4328 <S>/files/f4-tribunal-2026-10-10.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (10608 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
Houses started 09:02 (date 09:02:30 before the gates): house A Sol (task `bp6bktg2f`), house B Grok (task `b05j7vrfd`); `cd` back, `git status --short --branch` → `## ops/tribunal-guard-1010`.

## OWN FINDINGS
Written by 09:05 (date 09:05:25), before either house list was opened. Inputs read: the card, the diff `fccbb258..2e680273`, `ops/desk/bare-guard.py` (`:60-139`, `:700-759`, `:1000-1060`, the G10 lines) and `tests/ops/test_bare_guard.py` (`:1-280`, `:1180-1340`) at the tip, the build report whole, `237-f4-tribunal.md` lines 1, 9, 39-43, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down, and `ls -1 ".../prompts/"20*/*tribunal*` (87 names).

FINDING O1
ROW: T (clause "the launch shapes of 237 `## 2`")
CLAIM: The tests pin only short stand-ins (`tests/ops/test_bare_guard.py:1290-1294`); the three real 237 launch lines (`237-f4-tribunal.md:39`, `:41`, `:43`) carry long quoted sentences with an apostrophe (`houses' rulings`), `;`, `<id>`, `(1)`, an `--add-dir` path and ` < /dev/null`; if any guard rule trips on them, the relaunch of 237 still fails.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
_237_SAME = (
    "Read ONLY the packet files in that folder. Do NOT open any file whose name ends in "
    "-ruling.md or -ruling.partial.md: those are other houses' rulings and round 1 is independent. "
)
GROK_237 = (
    'grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p '
    '"You are GROK. The folder is scratch/tribunal-bars-0920/f4-tribunal/r1/. ' + _237_SAME +
    "Start with 00-READING-ORDER.md, then 01-QUESTIONS.md, and follow them exactly. Search 02-greps.txt whenever a ruling "
    "needs a search: every search this tribunal needs has already been run and its full output is in 02-greps.txt. "
    'Write your complete ruling to scratch/tribunal-bars-0920/f4-tribunal/r1/grok-ruling.md."'
)
GEMINI_237 = (
    "agy --model gemini-3.8-flash-high --mode accept-edits --sandbox --print-timeout 20m --add-dir "
    '/Users/cobalt/cobalt-wt/agy-trial --print="You are GEMINI. The folder is scratch/tribunal-bars-0920/f4-tribunal/r1/ '
    "(absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f4-tribunal/r1/). " + _237_SAME +
    "Start with 00-READING-ORDER.md, then 01-QUESTIONS.md, and follow them exactly. Open 02-greps.txt THIRD: every search "
    "this tribunal needs has already been run and its full output is in 02-greps.txt, including every writer of a "
    "daily-note unit, every reader of the three store methods, the loud-flag text search, the job label across code, "
    "config, plists and tests, the rules-config write, the slot-state and slot-spec uses, the new config keys search, the "
    "ET clock callers, the FAILED renders, the Market Context search, the forbid search, the shared-gate inventory, the "
    "prebell search, the plist and prefill directory listings and the branch state. Read every file with your file viewer "
    "only. Run NO shell command - not cat, grep, ls or any pipe: a shell command is denied in this headless run and a "
    "denial ends your answer with no output. A shell or command tool call ends this run with no output - open files with "
    "the file viewer only; a run of yours on another packet ended exactly that way, on a grep whose answer was already in "
    'greps.txt. Do NOT write any file: print your complete ruling as your answer."'
)
ASTRA_237 = (
    'codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "You are GPT-6 Astra, one of the houses on this design '
    "tribunal. The folder is /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f4-tribunal/r1/ . " + _237_SAME +
    "Do NOT run any command other than reading those files and do NOT write any file. YOUR USAGE METER IS SMALL: a run of "
    "yours on another tribunal packet read files for 135,471 tokens and was stopped by the usage limit before it ruled "
    "anything. Read in THIS ORDER and no further than a ruling needs: (1) 01-QUESTIONS.md whole; (2) 10-PROPOSAL.md whole; "
    "(3) 11-seam.md, 12-drafter-report.md and 13-rulings.md whole; (4) 20-prefill.excerpt.py whole, then "
    "21b-merge-store.excerpt.py whole; (5) 21a-writer.excerpt.py and 22-config.excerpt.md whole. Everything else - "
    "14-charter-ladder.md, 23-consumers.excerpt.py, 25-references.excerpt.md, 27-laws-excerpt.md - you open ONLY where a "
    "ruling turns on it, by a search inside the folder or a line range, never whole-file dumps; the searches the questions "
    "name are already run in 02-greps.txt - search 02-greps.txt, do not print it whole. RULE AS YOU GO: rule the items in "
    "the order C1, C2, ... C12, S1, S2, S3, (a), (b), (c), (d), (e), (f), then EXPERIMENTS, OWNER (after the tribunal), "
    "then WRONG FACTS; the moment you have ruled an item, PRINT that item's complete ruling as a message, headed ITEM <id>, "
    "before you read anything for the next item. If the meter stops you, what you printed is kept as a partial ruling. "
    "When all items are ruled, print your complete ruling once more as your final message, ending with exactly one "
    'TRIBUNAL R1: line as 01-QUESTIONS.md says." < /dev/null'
)


@pytest.mark.parametrize("command", [GROK_237, GEMINI_237, ASTRA_237])
def test_check_o1_the_tribunal_hub_types_237s_launch_lines_verbatim(roots, command):
    assert_allowed(run(command, tribunal_seat(roots)))
```
EXPECT: if the claim holds, a case fails `assert done.returncode == 0` with a G1/G2/G3 line; if every rule passes the real lines, `3 passed` (NOT HELD, and the relaunch shapes are proven).

FINDING O2
ROW: X2 / T (clause "matches … `17-f15-tribunal-r2.md`")
CLAIM: No test pins the `(-r[0-9]+)?` arm of the pattern (`ops/desk/bare-guard.py:756`; test (1) uses only `237-f4-tribunal.md`, `tests/ops/test_bare_guard.py:1279`) nor any real hub or seat name beyond the card's nine; run over the 87 real `prompts/20*/*tribunal*` names, the pattern must pass every round hub (`-r2`, `-r3`) and deny every `-fable-seat`, `-anthropic-seat`, `-derive` and `draft` name.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
@pytest.mark.parametrize(
    "name",
    ["04-bars-tribunal.md", "06-bars-tribunal-r3.md", "44-setups-tribunal-r2.md", "19-handicap-tribunal-r2.md",
     "24-voice-v3-tribunal-r2.md", "27-drc-overnight-tribunal-r2.md", "16-voice-tts-tribunal.md",
     "02-shrink-tribunal.md", "12-f15-tribunal.md", "17-f15-tribunal-r2.md", "63-routing-tribunal.md"],
)
def test_check_o2_every_real_hub_name_types_a_house_string(roots, name):
    assert_allowed(run("grok --version", tribunal_seat(roots, name)))


@pytest.mark.parametrize(
    "name",
    ["24-setups-tribunal-fable-seat.md", "45-setups-tribunal-fable-seat-r2.md", "25-voice-v3-tribunal-r2-fable-seat.md",
     "17-voice-tts-tribunal-anthropic-seat.md", "18-f15-tribunal-anthropic-seat-r2.md", "46-setups-tribunal-derive-r2.md",
     "43-draft-setups-tribunal-r2.md", "22-draft-overnight-tribunal.md", "250-draft-tribunal-guard.md",
     "251-tribunal-guard-card.md", "254-tribunal-guard-preflight-r2.md"],
)
def test_check_o2_no_real_seat_derive_or_draft_name_types_a_house_string(roots, name):
    assert_denied(run("grok --version", tribunal_seat(roots, name)), G7_ROUTE)
```
EXPECT: a defect shows as a failing case naming the mis-classified name; `22 passed` = X2 answered yes for these names (NOT HELD).

FINDING O3
ROW: X6
CLAIM: G9 passes any option after the `HOUSE` prefix (`ops/desk/bare-guard.py:126`, `:1038`), so a tribunal hub may type `codex exec … -s read-only --dangerously-bypass-approvals-and-sandbox "x"` or `grok --always-approve -p "x"` (237 line 39 says "never `--always-approve`"); and 237 line 1 launches the hub `--permission-mode auto`, not `dontAsk`, so the launch line's `--allowedTools` is not a hard fence for it either.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
@pytest.mark.parametrize(
    "command",
    ['codex exec --skip-git-repo-check -m m -s read-only --dangerously-bypass-approvals-and-sandbox "x"',
     'grok --always-approve -p "x"'],
)
def test_check_o3_a_tribunal_hub_is_denied_a_sandbox_bypass_flag(roots, command):
    assert_denied(run(command, tribunal_seat(roots)), G7_ROUTE)
```
EXPECT: `assert done.returncode == 2` fails with `(0, '')` for both cases.

FINDING O4
ROW: X3
CLAIM: With the tribunal flag set, shapes that hide a second launcher or wrap the house string must still be denied (`ops/desk/bare-guard.py:1024`, `:1037-1041`): a wrapper (`command grok`, `timeout 5 agy x`), a `;`/`&&` second launcher, and `$(claude …)` inside the house call's argument.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
@pytest.mark.parametrize(
    "command",
    ['command grok -p "x"', "timeout 5 agy x", 'grok -p "x"; claude -p y', 'agy --version && claude -p y',
     'grok -p "$(claude -p y)"', "env grok --version"],
)
def test_check_o4_a_tribunal_hub_wrapped_or_chained_launch_is_denied(roots, command):
    done = run(command, tribunal_seat(roots))
    assert done.returncode == 2, (done.returncode, done.stderr)
```
EXPECT: a case that passes the guard fails `assert done.returncode == 2` with `(0, '')`; `6 passed` = X3 answered: no reach beyond the prefix (NOT HELD).

## Findings
Both houses finished before their lists were opened: Sol notice 09:07 (date 09:07:33; list left unread until Grok finished), Grok notice 09:16 (date 09:16:26). `ls -la <S>` at 09:16: `house-b.md` 12 bytes (written by Grok), no `house-a.md`.
- House A Sol: exit 0; its final message (task output lines 5853-5857, after `codex`) is exactly `FINDINGS: 0` (`tokens used 187,864`). Written by me to `<S>/house-a.md` = `FINDINGS: 0`.
- House B Grok: exit 0; stdout = the path of `house-b.md`; `<S>/house-b.md` = `FINDINGS: 0`.
No house finding to keep. Own findings O1-O4 above.

## Dropped
none (neither house wrote a `FINDING` block).

## RUNS
All four own tests pasted after `test_g9_a_tribunal_hub_is_denied_what_g1_to_g6_deny` and run together: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py -k test_check_o` → `2 failed, 34 passed, 1732 deselected, 15 warnings in 2.18s`; both failures `tests/ops/test_bare_guard.py:268: AssertionError: (0, '')` (`assert_denied`), the two O3 cases.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | TEST, 3 cases (237 line 39, 41, 43 verbatim) | 3 passed | NOT HELD — the three real launch lines pass every guard rule from a tribunal seat |
| O2 | own | TEST, 11 hub names + 11 seat/derive/draft/card/preflight names | 22 passed | NOT HELD — X2 answered for these names; the `-rN` arm allows `-r2`/`-r3` hubs |
| O3 | own | TEST, 2 cases | 2 failed, `(0, '')` at `:268` — the guard allows both bypass flags from a tribunal seat | REJECTED — the card's `## NOT IN THIS JOB`: "a change to `HOUSE` (`:125`) … a wider `codex` shape" and X6 ("confirm the fence is the launch line's `--allowedTools` and the sandbox, not this guard"); OPEN |
| O4 | own | TEST, 6 cases | 6 passed | NOT HELD — X3 answered: wrapper, `;`, `&&`, `$(…)` and `env` shapes all exit 2 |
All four tests removed again with the Edit tool (O3 is not held, so not committed); `git status --short --branch` → `## ops/tribunal-guard-1010` (clean). No `wip(tribunal-guard-1010): check red` commit: nothing held.

## FIXES
none — no finding held.

## Suites
No commit of mine: the tip is the build's `TIP` `2e680273` (HEAD `8a7a938f` adds only the build report under `docs/`). DB: none card → RESTARTS, then W (a0), (a), (e) and `tests/ops`.
- RESTARTS · `uv run cobalt jobs restarts fccbb258..HEAD` · 0 ·
  ```
  path	change	rule	restart
  docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md	A	DOCS	-
  ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
  tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
- (a0) · `git diff --name-only --no-renames fccbb258` · 0 · `docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py` — every path under `docs/`, `ops/` or `tests/ops/` → **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh tribunal-guard-1010 offline` · 0 · `offline 4196/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/tribunal-guard-1010-offline-20261010-091802.log`
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · 0 · `2743 passed, 1 xfailed, 15 warnings in 510.68s (0:08:30)`
- (e) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh tribunal-guard-1010 livenote` · 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/tribunal-guard-1010-livenote-20261010-091827.log`; its one skip (log `:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — not `COBALT_LIVE_VAULT_ROOT`.
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/tribunal-guard-1010/.env` → `No such file or directory` (never present in this check).

## Scope
PREFLIGHT's path union: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` — both in row T's `files`. My commits: none. Nothing outside the row's files; no fenced path touched.

## Checked against the branch
- (i) `git log --oneline 2e680273..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `2e680273`.
- (ii) `git log --stat --format=%h 2e680273..HEAD` → `8a7a938f` · `.../reports/tribunal-guard-build-2026-10-10.md | 146 +` only (docs).
- (iii) `git log --oneline fccbb258..HEAD -- ops/desk/stop-guard.py .claude` → empty. (`HOUSE`/`LAUNCHERS` unchanged: the diff of `bare-guard.py` has three hunks — header, `seat()`, `:1038` — quoted at PREFLIGHT's diff read.)
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/tribunal-guard-1010`.
- (vi) `git log --stat --format=%h fccbb258..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not involved.
- (vii) card `## RECORDS`: the `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py` record re-run → printed nothing (main HEAD now `518b4c57 docs(desk): R883 tribunal-guard check launched`): holds. The other records name `git show` / `uv` reads, not an `ls`, `grep` or `git -C … log`; the RESTARTS record is answered above (`RESTARTS: none`).
- (viii) L32: this report holds no ticker, price or date of his; the test strings were constructed or copied from 237's prompt text, and were removed.
- CHECK ASKS: X1 — the build matches the brain's direction (diff above; `claude` still G7: build test (2), my O4). X2 — `ls -1 ".../prompts/"20*/*tribunal*` (87 names) and O2: 11 real hub names allowed, 11 seat/derive/draft/card/preflight names denied. X3 — O4: no reach beyond the prefix. X4 — confirmed by reading the diff: test (3) adds `ASTRA_PROBE` and `claude --bg "Read x"` for build/devfix/deploy; `grok --version`/`agy --version` repeat `:1265-1268`. X5 — the listing shows the unmatched names `2026-09-19/08-tribunal-archiver.md`, `10-tribunal-archiver-r2.md`, `12-tribunal-archiver-r3.md`, `2026-09-21/27-setups-tribunal-r1b.md`, `41-reissue-handicap-tribunal-q17.md`; every name from `2026-09-22` on that ends `-tribunal` or `-tribunal-r<n>` follows the matched shape; whether any of the five is live is the desk's (no run settles it). X6 — O3: the guard is NOT a fence on options; and 237 line 1 launches the hub `--permission-mode auto`, so the allow list is not a hard fence either (OPEN).

## OPEN
- O3 · REJECTED — the card's fence (`HOUSE` unchanged; X6) · a tribunal hub (as the check already can) passes `codex exec --skip-git-repo-check -m m -s read-only --dangerously-bypass-approvals-and-sandbox "x"` and `grok --always-approve -p "x"` through the guard (`(0, '')`), and 237's hub runs `--permission-mode auto`. FOLLOW-UP: settled by a guard card that denies the bypass options after a `HOUSE` prefix, or by a desk ruling that the auto-mode classifier and the house sandboxes are the fence.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- Dropped findings: none. Houses that produced nothing: none (both wrote `FINDINGS: 0`).
- Sol's task output (653 KB) shows it printed text from outside the staged set (line 5851: the LAWS fold section); its instructions named only the staged files. A house claim is never accepted (L35); its list was empty.
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (DB: none). A sibling worktree (`aset-orphan-1010`) held `.env` at PREFLIGHT; not this check's.
- L74: one system reminder asking for a `Claude-Session:` commit line (~09:00); recorded under `## L74`, not followed. No commit was made.
- `tokens` read at 09:29 (date 09:29:37): `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 9d7aa0cb` → `context 168237 of 400000 — ok`.
- files opened: 11 — `CHECK-HUB.md`; the card; `ops/desk/bare-guard.py`; `tests/ops/test_bare_guard.py`; `237-f4-tribunal.md` (lines 1, 9, 39-43); the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `BUILD-HUB.md` (`## THE LOCK`, `## RESTARTS`, `## W`); house A's output (Sol task file, lines 5850-5859); house B's stdout (Grok task file); `<S>/house-b.md`.
- Check of `tribunal-guard-1010`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: tribunal-guard-1010 · pass: 1 · tip: 2e680273 · house A: Sol FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 168237
