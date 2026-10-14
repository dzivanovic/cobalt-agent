# strike-fallback-env-1010-grok — check (shadow), 2026-10-13

## §0 Headline
- Shadow check of the Grok build `ca850d5f`. House A was Grok (`FINDINGS: 1`); house B none (not needed); Gemini's probe failed (HARNESS).
- 4 findings: O1 and O2 held (opus-own: two clauses no test pins, and the mutations survived), O3 not held, H1 (Grok, the DevDocs lines) rejected under the hub's dated-line rule.
- The gate is green on the tip: offline 4195/0, with-DB 5092/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed.
- Nothing fixed (shadow). One decision: the RESTARTS line (the harness file is UNCLASSIFIED; strike.py also reaches radar).

## L74
- 2026-10-13 20:28 EDT: a system reminder asked that commits carry a `Claude-Session:` line. Recorded as data under L74; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../365-shadow-strike-fallback-env-1010-grok-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "<card>" · 0 · ec3053d545779baee52d8c8beac9f5aa316a0920
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "<card>" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES `STANDING-LIST.md` once (`4be06af0`) ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R685 row · ... · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; ... | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · ... · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-11 R1069 row · ... · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · ... · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35 (one row, STANDING `Bash(grok *)`); `grep -n "^| R19 "` → line 37 (one row, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output:
```
clock · date · 0 · Tue Oct 13 20:28:32 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/strike-fallback-env-1010-grok
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h ca850d5f..HEAD · 0 · (5 lines)
    6cb30071 docs(strike-fallback-env-1010-grok): shadow build report — ca850d5f
    6cb30071
     ...rike-fallback-env-1010-grok-build-2026-10-11.md | 199 +++++++++++++++++++++
     1 file changed, 199 insertions(+)
env here · ls .../strike-fallback-env-1010-grok/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../strike-fallback-env-1010-grok-build-2026-10-11.md" · 0 · SHADOW BUILT · job: strike-fallback-env-1010-grok · tip: ca850d5f | on 8f4bbe28 | offline 4195/0 | with-DB 5092/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | decisions: 4 · builder: grok-4.7 · gate: strike-fallback-env-1010-grok-gate · passes: 2 · suites at first run: green · builder tokens: UNKNOWN · wall: 6
range · git log --oneline 8f4bbe28..ca850d5f · 0 · (2 lines)
    ca850d5f feat(strike-fallback-env-1010-grok): rows
    b8418447 wip(strike-fallback-env-1010-grok): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.
- THE RANGE typed, `git log --stat --format=%h 8f4bbe28..ca850d5f` · exit 0: `ca850d5f` → `docs/40 - DevDocs/cobalt/aset/__main__.md` (+3), `docs/40 - DevDocs/cobalt/aset/strike.md` (+3), `src/cobalt/aset/__main__.py` (+9), `src/cobalt/aset/strike.py` (+62/−13 lines); `b8418447` → `tests/cobalt/test_strike_fallback.py` (+81), `tests/cobalt/test_strike_fallback_env.py` (+82). Path union: those six paths.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
- Gemini OUT is HARNESS (a model-selection error, no return time named).
- Seats: card header has no `HOUSE A:` line; `HOUSE B: as needed`. **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
11858 <S>/diff.md
10085 <S>/files/365-shadow-strike-fallback-env-1010-grok-card.md
26080 <S>/files/strike-fallback-env-1010-grok-build-2026-10-11.md
2171 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/__main__.md
3639 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/strike.md
2731 <S>/files/wt/src/cobalt/aset/__main__.py
27903 <S>/files/wt/src/cobalt/aset/strike.py
11041 <S>/files/wt/tests/cobalt/test_strike_fallback.py
3003 <S>/files/wt/tests/cobalt/test_strike_fallback_env.py
754 <S>/rulings.md
STAGED 10 files · 99265 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count (2). `stage-copy.sh`, one call each, for the files `## READ` names that the script cannot derive:
- `COPIED 25681 <S>/files/wt/src/cobalt/cli.py`
- `COPIED 14043 <S>/files/wt/src/cobalt/db.py`
- `COPIED 3216 <S>/files/wt/tests/conftest.py`
- `COPIED 52107 <S>/files/cto-2026-10-10.md`
- `COPIED 12568 <S>/files/206-archiver-429-card.md`
- `COPIED 25040 <S>/files/wt/src/cobalt_agent/config.py` (named by row A)
`<S>/HOUSE-INSTRUCTIONS.md` written: HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, then the Files paragraph.
House A Grok started 20:29:57 EDT (`date`), house gates re-run first (R17 line 35, R19 line 37); `git status --short --branch` after the return → `## shadow/strike-fallback-env-1010-grok` plus `?? SHADOW-INSTRUCTIONS.md` (expected).

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: A
CLAIM: The row's clause "`override` stays the default `False`, so a variable already in the environment wins" (`src/cobalt/aset/__main__.py:29–30`) is pinned by no test: the A1 stub (`tests/cobalt/test_strike_fallback_env.py:43–48`) records only the path and ignores keyword arguments, so `load_dotenv(..., override=True)` stays green.
RUN: COMMAND `grep -n -F "override" tests/cobalt/test_strike_fallback_env.py`
EXPECT: no output, exit 1 (no test names `override`).

FINDING O2
ROW: B
CLAIM: The clause "at least `REPEAT_ERROR_S = 60.0` seconds" (`src/cobalt/aset/strike.py:560`, `elapsed >= REPEAT_ERROR_S`) has no boundary test: B2 drives +30 s and +61 s only (`tests/cobalt/test_strike_fallback.py:270–281`), so `>` in place of `>=` stays green.
RUN: COMMAND `grep -n -F "60.0" tests/cobalt/test_strike_fallback.py`
EXPECT: no output, exit 1 (no B test steps the clock to exactly 60 s).

FINDING O3
ROW: B
CLAIM: Clause (1), "the first failure of a streak logs ERROR … (failed passes: 1)", is pinned only for the thread's first streak; no B test runs fail → ok → the same failure within 60 s (`tests/cobalt/test_strike_fallback.py:262–301`), so dropping the reset of `_last_error` / `_last_error_at` on recovery (`src/cobalt/aset/strike.py:573–574`) would silence a second streak and stay green. The test below pins it; it is expected GREEN on the tip (the behaviour is right) and red only under that mutation.
RUN: TEST `tests/cobalt/test_strike_fallback.py`
```python
def test_o3_a_new_streak_after_recovery_logs_its_first_error_at_once():
    down = RuntimeError("database down")
    assert _drive([(0.0, down), (1.0, "ok"), (2.0, down)]) == [
        ("ERROR", FAILED + "RuntimeError: database down (failed passes: 1)"),
        ("INFO", "strike fallback: recovered after 1 failed passes"),
        ("ERROR", FAILED + "RuntimeError: database down (failed passes: 1)"),
    ]
```
EXPECT: on the tip, `1 passed` (NOT HELD as a defect); with lines `strike.py:573–574` removed, the last ERROR is missing (the coverage gap).

CHECK ASKS, own read (facts at the tip, not findings):
- X1: `load_dotenv(...)` is module level at `src/cobalt/aset/__main__.py:30`, before the `cobalt.aset.config` / `cobalt.aset.net` imports (`:32–33`) and before the `if __name__ == "__main__":` block (`:35`), so before `start_fallback_thread()` (`:63`) on every path; above it only `os.environ.setdefault("LOGURU_LEVEL", "INFO")` (`:19`) touches the environment. A1 pins the order (a load after the start would raise inside the stubbed start).
- X2: `step()` catches `Exception` (`strike.py:555`) and returns; `run` always waits and loops (`:580–582`). A persisting text is said again on the first pass ≥ 60 s after the last ERROR, so silence exceeds 60 s only by up to one `interval_s` (`settings.stream_tail_ms / 1000`, `:591`).
- X3: yes for `Exception`, as before; a `BaseException` that is not an `Exception` ends the thread, unchanged from BASE (`git diff` shows the same `except Exception`).

## Findings
Grok finished at the notice 20:45:34 EDT (`date`); `ls -la <S>` → `house-a.md` 602 bytes, written by Grok (stdout was its path only). Its last line: `FINDINGS: 1`.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| H1 | Grok | SCOPE | Pass S adds dated sections to `docs/40 - DevDocs/cobalt/aset/__main__.md:42` and `.../strike.md:19`, paths the rows' `files` do not list. | COMMAND |

## Dropped
None. (H1 carries `RUN: COMMAND` with a `git diff` line.)

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `grep -n -F "override" tests/cobalt/test_strike_fallback_env.py` | no output | HELD — no test pins row A's `override` stays `False` clause. Mutation run (Edit, then undone): `load_dotenv(..., override=True)` at `__main__.py:30` → `uv run pytest … tests/cobalt/test_strike_fallback.py tests/cobalt/test_strike_fallback_env.py`, and A1 and A2 stayed green (`1 failed, 17 passed`; the one red was O3's test, line 299) |
| O2 | opus-own | `grep -n -F "60.0" tests/cobalt/test_strike_fallback.py` | no output | HELD — no boundary test for `elapsed >= REPEAT_ERROR_S`. In the same mutation run, `>` in place of `>=` at `strike.py:560` left B1–B5 green |
| O3 | opus-own | test `test_o3_a_new_streak_after_recovery_logs_its_first_error_at_once`, alone on the tip | `1 passed in 0.10s` | NOT HELD — the behaviour is right on the tip. Supporting evidence: with the recovery resets at `strike.py:573–574` removed, this test went red (`test_strike_fallback.py:299: AssertionError … Right contains one more item: ('ERROR', '… (failed passes: 1)')`) and B1–B5 stayed green. The test was removed again with Edit |
| H1 | Grok | `git diff --stat 8f4bbe28 ca850d5f -- "docs/40 - DevDocs/cobalt/aset/__main__.md" "docs/40 - DevDocs/cobalt/aset/strike.md"` | `__main__.md \| 3 +++` · `strike.md \| 3 +++` · `2 files changed, 6 insertions(+)` | REJECTED — CHECK-HUB `## 5` / BUILD-HUB `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`", and CHECK-HUB `## 7` (ii) holds non-docs paths only to the rows' `files`. The output is as Grok said, but the hub requires these lines |

All three mutations were made with Edit and undone with Edit. After that, `git status --short --branch` → `## shadow/strike-fallback-env-1010-grok` and `?? SHADOW-INSTRUCTIONS.md`: the tree is back at the tip. Nothing was committed: no test went red on the tip, so there was no `check red` commit.

## FIXES
Shadow card: the check holds findings and fixes none (CHECK-HUB `## THE FLOW`).
- O1: HELD, not fixed (shadow). Its fix would sit in `tests/cobalt/test_strike_fallback_env.py`, a file the rows name: the A1 stub records `override` and asserts it is falsy.
- O2: HELD, not fixed (shadow). Its fix would sit in `tests/cobalt/test_strike_fallback.py`, a file the rows name: a B2 case at exactly +60.0 s.

## Suites
RESTARTS, `uv run cobalt jobs restarts 8f4bbe28..HEAD` · exit 1:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/strike.md	M	DOCS	-
docs/40 - DevDocs/reports/strike-fallback-env-1010-grok-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/strike.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_strike_fallback.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_fallback_env.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
This is the same table as the build's. The one UNCLASSIFIED path is the shadow harness's untracked file (D1).

W, on tip `ca850d5f` (no commit of mine): `sh /Users/cobalt/cobalt/ops/desk/gate.sh strike-fallback-env-1010-grok all --deploy` · exit 0 · verdict lines WHOLE:
```
offline 4195/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5092/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/strike-fallback-env-1010-grok-all-20261013-204644.log
```
- `grep -n -F "OUTSIDE" <log>` → no output.
- `ls <WT>/.env` → `No such file or directory` (21:16 EDT). `.env: removed, proven gone (W)`.

## Scope
PREFLIGHT path union: `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py` (rows A and B), `tests/cobalt/test_strike_fallback.py`, `tests/cobalt/test_strike_fallback_env.py` (rows' tests), and the two DevDocs pages (the one dated line each that the hub requires). Every path is in a row's `files` or is a DevDocs line. My commits: none.

## Checked against the branch
- (i) `git log --oneline ca850d5f..HEAD -- . ":(exclude)docs"` → no output (no commit of mine); `<tip now>` = `ca850d5f`.
- (ii) `git log --stat --format=%h ca850d5f..HEAD` → `6cb30071`, the build report only (docs). No WIDENED.
- (iii) `git log --oneline 8f4bbe28..HEAD -- configs src/cobalt_agent/config.py src/cobalt/cli.py .claude/settings.json.bak` → no output (the fence is untouched).
- (iv) No HELD finding has a red test (O1 and O2 are COMMAND findings); no `check red` commit.
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## shadow/strike-fallback-env-1010-grok` plus `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card, not a finding).
- (vi) `git log --stat --format=%h 8f4bbe28..HEAD -- src/cobalt/db_migrations tests/cobalt` → `b8418447`, the two offline test files only. No migration and no with-DB test, so no gate-list change is needed.
- (vii) Card record: `git -C /Users/cobalt/cobalt diff --stat 975345f3 HEAD -- src tests ops` → now 65 files changed, among them `src/cobalt/aset/__main__.py | 9 +` and `src/cobalt/aset/strike.py | 56 +-`. Main has moved since the desk's draft on 2026-10-10. The record held at BASE (the build re-ran it against `8f4bbe28`: nothing).
- (viii) L32: this report holds constructed test values only (`database down`, `constructed`); no ticker, price or date of his.

## OPEN
- H1 (Grok): REJECTED — CHECK-HUB `## 5` / BUILD-HUB `## E3` require the dated DevDocs line. To settle: a desk `SETTLED: H1 — R<n>`.
- O1, O2 (opus-own): HELD and not fixed, because the check fixes nothing on a shadow card. On a real card each fix sits inside a rows file: O1 in `tests/cobalt/test_strike_fallback_env.py` (assert that the stub's `override` is falsy), O2 in `tests/cobalt/test_strike_fallback.py` (a B2 case at exactly +60.0 s).
- FOLLOW-UP: no test pins clause (1) for a second streak after a recovery (O3's evidence). Fail → ok → fail is right on the tip, but the B tests miss a mutation that drops the recovery resets.

## CONTINUE
next: none — CLOSE done

## DECISIONS
- D1 RESTARTS (the card `## RECORDS` names any other label or an `ESCALATE` as a decision item). (a) `SHADOW-INSTRUCTIONS.md` reads `UNCLASSIFIED` / `ESCALATE` and widens the line to six residents. It is the shadow harness's untracked file, never committed. (b) `src/cobalt/aset/strike.py` → `com.cobalt.aset,com.cobalt.radar` (static import reach), where the card expected `com.cobalt.aset` only. Safe default taken: nothing classified (`configs/` is fenced; a shadow card is never deployed). This is the same as the build's D1 and D2.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. Gemini was not seated (not needed); its probe line was `OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS).
- REFUSED, not needed: `git diff 8f4bbe28..ca850d5f -- docs/40\ -\ DevDocs/cobalt` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." I read the two pages with the Grep tool instead.
- Lock takes: one, the gate's at W (`lock: waited 0 min`; released, `.env: removed`).
- Mutation runs (evidence for O1, O2, O3): three Edits made together, one run, all undone with Edit, and the tree proven back at the tip by `git status`.
- L74: one system reminder asked for a `Claude-Session:` commit line. Recorded under `## L74`, not acted on (no commit was made).
- files opened: 14 — CHECK-HUB.md, the card, BUILD-HUB.md (THE LOCK, E2–W), build report, areas/cobalt.md (What Cobalt is; Build rules down), `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py`, `src/cobalt/cli.py`, `src/cobalt/db.py`, `tests/conftest.py`, `tests/cobalt/test_strike_fallback.py`, the two DevDocs pages (`aset/__main__.md`, `aset/strike.md`, by Grep), `<S>/house-a.md`; and the diff `8f4bbe28..ca850d5f -- src tests`.
- Check of `strike-fallback-env-1010-grok`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- Gemini probe OUT (HARNESS): `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`. Not needed on this card (HOUSE B as needed).

CHECK DONE · job: strike-fallback-env-1010-grok · pass: 1 · tip: ca850d5f · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 2 (opus-own 2 · house 0) · fixed: 0 · held unfixed: 2 (shadow, never fixed) · open: 1 · house B: none available · suites: offline 4195/0 · with-DB 5092/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 14 · ready: N/A (shadow, never deployed) · decisions: 1 · for Dejan: 0 · tokens: 138527
