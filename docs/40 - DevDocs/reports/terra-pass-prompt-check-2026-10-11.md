# terra-pass-prompt-1011 — CHECK (pass 1) · 2026-10-11

## §0 Headline
Row T1 holds at `a790e54d`. `SHADOW-HUB.md` changes at `:26` and `:29` only (2/2, 103 lines). Filled, the template gives Terra's read sentence and leaves Grok and Sonnet at `Run no command.`
X5 is settled by a run: the guard keeps a `;` inside the quoted prompt and passes the Terra builder call.
Findings: 8 (7 mine, 1 Grok's), none held. Two are REJECTED: the card's after-grep 2 cannot hit the text the card prescribes. That is a card defect; the build is right.
Suites: offline 4199/0, live-note 146/0, `tests/ops` 3135 passed. DB: none. No commit by the check. One decision, an ASK DESK on the stage-set commit count.

## L74
A system reminder at 16:04 EDT asked commits to end with a `Claude-Session:` line. Data under L74; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 0 · c7785d1a9d7f209d3ec300096725752f9d9941ab
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/382-install-terra-pass-prompt-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1107 row · grep -n "^| R1107 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 14:| R1107 | 15:29 ET | HIS RULING: "Approved grok and I approve terra read" (mid-turn). Grok 365 X1 re-run approved, but my CONTINUE to `5b7147c4` was classifier-denied again: he types it there. Terra read: brain asked how (decoy .env). | APPROVED |
RULING 2026-10-11 R1107 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1107 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · e501ad3a2f473d05e732b8e03b9350c49cfd5459
RULING 2026-10-11 R1107 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sun Oct 11 16:04:37 EDT 2026
status · git status --short --branch · 0 · ## ops/terra-pass-prompt-1011
head · git log --oneline -1; git log --stat --format=%h a790e54d..HEAD · 0 · (5 lines)
    7e0cc8a2 docs(terra-pass-prompt-1011): build report — a790e54d
    7e0cc8a2
    
     .../reports/terra-pass-prompt-build-2026-10-11.md  | 129 +++++++++++++++++++++
     1 file changed, 129 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/terra-pass-prompt-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/radar-display-fix-1008-grok/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/terra-pass-prompt-1011/docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md" · 0 · BUILT · job: terra-pass-prompt-1011 · tip: a790e54d | on ffc704da | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 100980
range · git log --oneline ffc704da..a790e54d · 0 · a790e54d feat(terra-pass-prompt-1011): Terra pass prompt may run read commands (T1, R1107, L72)
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h ffc704da..a790e54d` → `a790e54d` · `docs/40 - DevDocs/prompts/SHADOW-HUB.md | 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)`. Path union: `docs/40 - DevDocs/prompts/SHADOW-HUB.md`.
- DB: none: `git diff --name-only --no-renames ffc704da..a790e54d` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (under `docs/`).
- `ls <S>` → `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · `grok: UP` · `gemini: UP`. No `HOUSE A: OpenAI` header line → Sol not probed.
- **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.
- PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION / PREFLIGHT (above). No with-DB string is used (DB: none).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · output whole:
```
112 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/terra-pass-prompt-1011-check/diff.md
7320 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/terra-pass-prompt-1011-check/files/382-install-terra-pass-prompt-card.md
13044 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/terra-pass-prompt-1011-check/files/terra-pass-prompt-build-2026-10-11.md
15934 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/terra-pass-prompt-1011-check/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
339 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/terra-pass-prompt-1011-check/rulings.md
STAGED 5 files · 36749 bytes · commits 0
```
`commits 0` against PREFLIGHT's range of 1 commit: the diff's `git log -p … -- . ":(exclude)docs"` excludes `docs/`, and the one commit `a790e54d` touches only `docs/` (PREFLIGHT, THE RANGE). The non-docs commit count is 0, so the staged diff is complete for what it covers; recorded under `## DECISIONS` (ASK DESK). So the house sees the change, I wrote `git diff ffc704da..a790e54d -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` (tool output, quoted whole) to `<S>/files/shadow-hub-docs-diff.md`.
`stage-copy.sh`, each `COPIED`:
- `COPIED 15739 …/files/SHADOW-HUB-main-at-base.md` (from `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `## READ`; main's last commit on it is `d4ec4fe3`, the hub at BASE)
- `COPIED 53420 …/files/wt/ops/desk/bare-guard.py` (`## READ` by symbol)
- `COPIED 33304 …/files/cto-2026-10-11.md` (`## READ`)
- `COPIED 13306 …/files/355-install-shadow-hub-card.md` (`## READ`, precedent)
- `COPIED 92953 …/files/wt/tests/ops/test_bare_guard.py` (the row's suite; X5 needs a test there)
- `COPIED 12470 …/files/wt/tests/ops/test_shadow_hub_file.py` (the row's suite)
`<S>/HOUSE-INSTRUCTIONS.md` written (9601 bytes): HOUSE TEXT verbatim, then the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, then Files.
House gates re-run at 16:06:33: R17 count 1, R19 count 1. Grok started 16:06 EDT (`cd <AGY>`, the GROK line, `cd <WT>`, `git status --short --branch` → `## ops/terra-pass-prompt-1011`).

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: X5 (T1)
CLAIM: `scan()` (`ops/desk/bare-guard.py:165-244`) may cut the Terra builder call at the `;` the new `SHADOW-HUB.md:29` puts inside the double-quoted prompt, so G1 or G7 would deny the one builder call `builder_call` (`bare-guard.py:1148`) should pass; no test pins a prompt with `;`, `,` or `'` (the constructed `PASS_PROMPT` at `tests/ops/test_bare_guard.py:2116` has none).
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
TERRA_PROMPT = (
    "You are TERRA (OpenAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first "
    "and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run only commands "
    "that read files; no command that writes, deletes or uses the network. Reply with the list of files you wrote."
)


def test_x5_the_terra_prompt_with_a_semicolon_inside_its_quotes_is_its_builder_call(roots):
    """Check of terra-pass-prompt-1011 X5: `;`, `,` and `'` inside the one double-quoted prompt are
    quoted for scan(), so the Terra builder call passes; the same `;` outside the quotes is denied."""
    seat = shadow_seat(roots, "gpt-5.6-terra")
    cmd = builder(roots, "gpt-5.6-terra").replace(PASS_PROMPT, TERRA_PROMPT)
    assert '"' + TERRA_PROMPT + '"' in cmd
    assert_allowed(run(cmd, seat))
    done = run(cmd + " ; ls", seat)
    assert done.returncode == 2, done.stderr
```
EXPECT (claim true): `assert_allowed` fails with a `G1` `` `;` `` block or the G7 route in stderr.

FINDING O2
ROW: X1 (T1)
CLAIM: the diff of `docs/40 - DevDocs/prompts/SHADOW-HUB.md` is more than 2/2 or touches a line other than `:26` and `:29`.
RUN: COMMAND — `git diff -U0 ffc704da..a790e54d -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` (with `git diff --numstat ffc704da..a790e54d` and `grep -c "" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` beside it)
EXPECT (claim true): a hunk header other than `@@ -26 +26 @@` / `@@ -29 +29 @@`, numstat other than `2	2`, or a count other than 103.

FINDING O3
ROW: X2 (T1)
CLAIM: the new `:29` carries a `"`, `\` or `$` that `PLAIN_PROMPT` (`bare-guard.py:108`) refuses.
RUN: COMMAND — `grep -n -F '"' "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` (then the same for `\` and `$`, each its own call)
EXPECT (claim true): a line starting `29:` in any of the three outputs.

FINDING O4
ROW: X3 (T1)
CLAIM: filling the tip's `:29` template does not give `Run only commands that read files; no command that writes, deletes or uses the network.` for Terra and `Run no command.` for Grok and Sonnet.
RUN: TEST — `tests/ops/test_shadow_hub_file.py`:
```python
@pytest.mark.parametrize("model,want", [
    ("GROK", "Run no command."),
    ("SONNET", "Run no command."),
    ("TERRA", "Run only commands that read files; no command that writes, deletes or uses the network."),
])
def test_x3_the_run_sentence_filled_for_each_model(model, want):
    """Check of terra-pass-prompt-1011 X3: the <pass prompt> template's Run sentence, filled."""
    lines = [x for x in text().splitlines() if x.startswith("`You are <GROK (xAI)")]
    assert len(lines) == 1
    m = re.search(r"Run <no command \((GROK, SONNET)\) or (only [^(]*) \((TERRA)\)>\.", lines[0])
    assert m, lines[0]
    filled = "Run no command." if model in m.group(1) else f"Run {m.group(2)}."
    assert filled == want
    assert lines[0].endswith("Reply with the list of files you wrote.`")
```
EXPECT (claim true): `AssertionError` on `filled == want` or on `m`.

FINDING O5
ROW: T1 (the card's red-first grep 2)
CLAIM: the card's after-grep `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network"` → 1 does not hold at the tip, because the row's own template text puts `<no command (GROK, SONNET) or ` between `Run` and `only` (`SHADOW-HUB.md:29`); the build records it as DECISION T1.
RUN: COMMAND — `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"`
EXPECT (claim true): `0`.

FINDING O6
ROW: X4
CLAIM: a test or script reads the text of `SHADOW-HUB.md:26` or `:29`.
RUN: COMMAND — `grep -rn -F "Run no command" tests ops` (and `grep -rn -F "Reads are not confined" tests ops`, its own call)
EXPECT (claim true): any hit.

FINDING O7
ROW: SCOPE
CLAIM: the range touches a path other than `docs/40 - DevDocs/prompts/SHADOW-HUB.md`.
RUN: COMMAND — `git diff --name-only --no-renames ffc704da..a790e54d`
EXPECT (claim true): a second path.

No path to a score, rank, grade or size: the change is one prompt template line and one note in a desk hub; `src/` is untouched (O7).

## Findings
House A Grok finished 16:17 (notice; `date` 16:17:29). `ls -la <S>` → `house-a.md` 520 bytes, written by Grok; its stdout ended with that path and `[exited with code 0]`. Last line `FINDINGS: 1`. House B: none (not needed).
THE DROP: `grep` of `RUN:` → FINDING 1 has `RUN: COMMAND` followed by a line beginning `grep`. Kept.
- G1 · Grok · T1 · the card's after-count of the filled Terra sentence is 0, not 1: `Run` and `only` are not adjacent at `SHADOW-HUB.md:29` · COMMAND

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | TEST `tests/ops/test_bare_guard.py::test_x5_the_terra_prompt_with_a_semicolon_inside_its_quotes_is_its_builder_call` | `1 passed, 15 warnings in 1.07s` | NOT HELD: the Terra builder call with `;`, `,` and `'` inside its quotes is allowed, and the same `;` outside the quotes is denied. X5 is settled: `scan()` keeps a `;` inside `"…"` (its `quote == '"'` branch, `bare-guard.py:190-199`, cuts nothing). Test removed |
| O2 | own | `git diff -U0 ffc704da..a790e54d -- "…SHADOW-HUB.md"` · `git diff --numstat ffc704da..a790e54d` · `grep -c ""` | hunks `@@ -26 +26 @@` and `@@ -29 +29 @@` only · `2	2	docs/40 - DevDocs/prompts/SHADOW-HUB.md` · `103` | NOT HELD: X1 answered yes |
| O3 | own | `grep -n -F '"'` · `grep -n -F '\'` · `grep -n -F '$'` on the hub | `"` on lines 3, 10, 19, 20, 21, 24, 26, 28, 32, 43, 44, 49, 52, 63 · `\` on 10, 28 · `$` on 10, 28; no `29:` in any | NOT HELD: X2 — `:29` holds none of the three; its only backticks are the two markdown code marks around the template. O1's run shows the filled Terra prompt passes `PLAIN_PROMPT` |
| O4 | own | TEST `tests/ops/test_shadow_hub_file.py::test_x3_the_run_sentence_filled_for_each_model` (3 params) | `3 passed, 15 warnings in 0.91s` | NOT HELD: X3 — the tip's `:29`, filled, gives `Run no command.` for GROK and SONNET and `Run only commands that read files; no command that writes, deletes or uses the network.` for TERRA, and still ends `Reply with the list of files you wrote.` Test removed |
| O5 | own | `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network" "…SHADOW-HUB.md"` | `0` | REJECTED — card T1 prescribes the template text `Run <no command (GROK, SONNET) or only commands …>`, which the tip carries character for character (O2). The card's own after-grep 2 cannot hit that text. The filled sentence is right (O4). This is a card defect, not a build defect (the build's DECISION T1). OPEN |
| G1 | Grok | the same command as O5 | `0` | REJECTED — the same card line as O5. OPEN |
| O6 | own | `grep -rn -F "Run no command" tests ops` · `grep -rn -F "Reads are not confined" tests ops` | empty · empty | NOT HELD: X4 — nothing reads `:26` or `:29`'s text. (`test_shadow_hub_file.py` reads the file, but not these lines' text) |
| O7 | own | `git diff --name-only --no-renames ffc704da..a790e54d` | `docs/40 - DevDocs/prompts/SHADOW-HUB.md` | NOT HELD |
X6: no finding rests on Terra being allowed to read files.
No test was HELD, so there is no `wip(terra-pass-prompt-1011): check red` commit. Both temporary tests were removed with the Edit tool; `git status --short --branch` → `## ops/terra-pass-prompt-1011` (clean).

## FIXES
none (held: 0)

## Suites
With no commit by the check, the tip is the build's `a790e54d` (the HEAD `7e0cc8a2` above it is docs only).
- RESTARTS: `uv run cobalt jobs restarts ffc704da..HEAD` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-` · `docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md	A	DOCS	-` · `RESTARTS: none`
- (a0) `git diff --name-only --no-renames ffc704da` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md` · `docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md`. Every path is under `docs/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh terra-pass-prompt-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/terra-pass-prompt-1011-offline-20261011-161826.log` (exit 0)
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh terra-pass-prompt-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/terra-pass-prompt-1011-livenote-20261011-161832.log` (exit 0)
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3135 passed, 1 xfailed, 15 warnings in 630.00s (0:10:30)`
- with-DB: not run (DB: none; `--deploy` is not typed for a DB: none card). `ls /Users/cobalt/cobalt-wt/terra-pass-prompt-1011/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, which is row T1's `files`. The check made no commit.

## Checked against the branch
- (i) `git log --oneline a790e54d..HEAD -- . ":(exclude)docs"` → empty (no commit by the check); `<tip now>` = `a790e54d`.
- (ii) `git log --stat --format=%h a790e54d..HEAD` → `7e0cc8a2` · `.../reports/terra-pass-prompt-build-2026-10-11.md | 129 +++` (docs only).
- (iii) `git log --oneline ffc704da..HEAD -- ops/desk/bare-guard.py ops/desk/desk-launch.sh ops/desk/authorize.sh "…/SPIKE-HUB.md" "…/STANDING-LIST.md" .claude tests` → empty. The other lines of `SHADOW-HUB.md` are untouched (O2: hunks `-26 +26` and `-29 +29` only).
- (iv) no held finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/terra-pass-prompt-1011`.
- (vi) `git log --stat --format=%h ffc704da..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No gate lists are owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -1 -- "…/SHADOW-HUB.md"` → `d4ec4fe3 fix(install-shadow-hub-1011): …` (holds). `grep -n -F "Run no command." "…/SHADOW-HUB.md"` → empty at the tip (was `29:` at BASE per the record, as T1 intends). `grep -rn -F "Run no command" tests ops` → empty (holds).
- (viii) L32: this report holds no ticker, price or date of his.

## OPEN
- O5 / G1 · REJECTED — the card's T1 after-grep `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network"` → 1 cannot hold with the template text the same row prescribes. It counts 0 at the tip. The build is right. To settle it, the desk corrects the card's grep (for example, grep `or only commands that read files; no command that writes, deletes or uses the network (TERRA)>`) on its follow-up list. Nothing in the branch changes.

## CONTINUE
next: done

## DECISIONS
- ASK DESK: `stage-set.sh` ended `STAGED 5 files · 36749 bytes · commits 0`, while PREFLIGHT's range holds 1 commit. `## 1` reads a different `<k>` as `FAILED: copy`. Its diff is `git log -p … -- . ":(exclude)docs"`, and this build's one commit `a790e54d` touches only `docs/`, so 0 is the true non-docs count. That rule cannot be met by any docs-only card. Safe default taken: continue. Grok was given the whole docs diff as `files/shadow-hub-docs-diff.md` (tool output) and both hub versions (BASE and TIP). No access was widened and no house was started twice. [16:05 EDT]
- OPEN, for the follow-up list (house B: none — the card says `as needed`; Gemini was UP and not seated): O5 / G1. The card's T1 after-grep 2 counts 0 at the tip by the card's own text. Default taken: the build stands unchanged; the desk corrects the card's grep. Not his notes, money or sizing.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. Gemini was UP and not seated (house B not needed).
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none).
- L74: one system reminder asked for a `Claude-Session:` line; it is recorded under `## L74`.
- The three suites ran at the same time (offline gate, live-note gate, `tests/ops`), all green.
- Temporary tests O1 and O4 were added, run green (NOT HELD) and removed with the Edit tool. Nothing was committed.
- files opened: 11 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `SHADOW-HUB.md` (worktree), the build report, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_shadow_hub_file.py`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `<S>/diff.md`, `<S>/house-a.md`.
- Check of `terra-pass-prompt-1011`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: terra-pass-prompt-1011 · pass: 1 · tip: a790e54d · house A: Grok FINDINGS: 1 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 157961
