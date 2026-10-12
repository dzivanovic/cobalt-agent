# CHECK — strike-fallback-env-1010-terra (shadow) · 2026-10-12

## §0 Headline
- Shadow check of `d02370df` (built by Terra). House A Grok produced `FINDINGS: 2`; house B none (`as needed`). Opus wrote 2 findings of its own first.
- Held 3 (opus-own 2 · house 1): O1, an exception whose `__str__` raises escapes `FallbackThread.step()` (`strike.py:549`) and kills the thread; O2 = G1, the B2 +30 s half asserts only the last record. Rejected 1: G2, the DevDocs pages are required by the hub.
- Shadow: nothing fixed and no commit. The gate on `d02370df` is green: offline 4195/0 · with-DB 5092/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`.

## L74
- The session's harness attribution reminder asked for a `Claude-Session:` line in commits. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · last line `AUTHORIZED`. The rows: INSTALLED nothing; PLACEHOLDER nothing; CARD COMMITTED a7167077; CARD UNCHANGED nothing; STANDING LIST R60 row 46 APPROVED, committed 962e9d17; RULING 2026-10-08 R685 row 38 APPROVED · HIS RULING, committed e1edc838; RULING 2026-10-11 R1069 row 74 HIS RULING · APPROVED, committed 2322ed1e; RULING 2026-10-11 R1107 row 36 HIS RULING … APPROVED, committed e501ad3a; `AUTHORIZED`.
House gates: R17 row at line 35 · R19 row at line 37 · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → 5055151dbf68899b82de5b11f99733ed2d03048c.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 12 11:06:28 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/strike-fallback-env-1010-terra
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h d02370df..HEAD · 0 · (5 lines)
    36be230f docs(strike-fallback-env-1010-terra): build report — d02370df
    36be230f
     ...ike-fallback-env-1010-terra-build-2026-10-11.md | 188 +++++++++++++++++++++
     1 file changed, 188 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/strike-fallback-env-1010-terra/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/radar-display-fix-1008-sonnet/.env
report · tail -n 3 "<REPORT>" · 0 · SHADOW BUILT · job: strike-fallback-env-1010-terra · tip: d02370df | on 8f4bbe28 | offline 4195/0 | with-DB 5092/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | decisions: 6 · builder: gpt-5.6-terra · gate: strike-fallback-env-1010-terra-gate · passes: 4 · suites at first run: green · builder tokens: 148582 · wall: 67
range · git log --oneline 8f4bbe28..d02370df · 0 · (3 lines)
    d02370df fix(strike-fallback-env-1010-terra): pass S2 1
    7a6c8955 feat(strike-fallback-env-1010-terra): rows
    154b6bc5 wip(strike-fallback-env-1010-terra): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.
- Another job's worktree holds `.env` (radar-display-fix-1008-sonnet): its lock, not this check's failure; waited for at the with-DB step.
- THE RANGE `git log --stat --format=%h 8f4bbe28..d02370df`: d02370df `tests/cobalt/test_strike_fallback.py` (1+/1-); 7a6c8955 `docs/40 - DevDocs/cobalt/aset/__main__.md`, `docs/40 - DevDocs/cobalt/aset/strike.md`, `src/cobalt/aset/__main__.py` (+9), `src/cobalt/aset/strike.py` (+41/-12); 154b6bc5 `tests/cobalt/test_strike_fallback.py` (+111), `tests/cobalt/test_strike_fallback_env.py` (+78). Path union: the two src files, the two test files, the two docs pages.
- `ls <S>` → No such file or directory (fresh).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → `STAGED 10 files · 99511 bytes · commits 3` (k = 3 = PREFLIGHT's range count). Per file:
```
12397 <S>/diff.md
10468 <S>/files/367-shadow-strike-fallback-env-1010-terra-card.md
25827 <S>/files/strike-fallback-env-1010-terra-build-2026-10-11.md
2079 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/__main__.md
3429 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/strike.md
2584 <S>/files/wt/src/cobalt/aset/__main__.py
27410 <S>/files/wt/src/cobalt/aset/strike.py
11770 <S>/files/wt/tests/cobalt/test_strike_fallback.py
2454 <S>/files/wt/tests/cobalt/test_strike_fallback_env.py
1093 <S>/rulings.md
```
`stage-copy.sh`, the `## READ` files not in the diff: `COPIED 25681 <S>/files/wt/src/cobalt/cli.py` · `COPIED 14043 <S>/files/wt/src/cobalt/db.py` · `COPIED 3216 <S>/files/wt/tests/conftest.py` · `COPIED 52107 <S>/files/cto-2026-10-10.md` · `COPIED 12568 <S>/files/206-archiver-429-card.md`.
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS whole, and the Files paragraph.
House probe (`house-probe.sh --card`): `grok: UP` · `gemini: UP`. Seats: house A Grok · house B none (not needed; card `HOUSE B: as needed`, no `HOUSE A:` header line).
House A started at 11:07:42 EDT (`date` before the gates), Grok `grok-4.7`, background, timeout 2700000.

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: X2 / X3 (row B)
CLAIM: `step()` catches the pass's exception at `src/cobalt/aset/strike.py:546` but builds the text at `:549` (`f"{type(e).__name__}: {e}"`) inside the `except` block with no guard, so an exception whose `__str__` raises escapes `step()`, and `run` (`:572–575`) ends and the fallback thread dies with no strike-fallback ERROR line.
RUN: TEST — `tests/cobalt/test_strike_fallback.py`:
```python
def test_check_o1_an_unprintable_failure_does_not_escape_step():
    class Unprintable(Exception):
        def __str__(self):
            raise RuntimeError("constructed: no text")

    clock = [0.0]
    with _thread_records([Unprintable(), "ok"], clock) as (thread, records):
        thread.step()
        clock[0] += 1
        thread.step()

    assert [r.split("|", 1)[0] for r in records][:1] == ["ERROR"]
```
EXPECT: on the tip the test errors with `RuntimeError: constructed: no text` raised out of `thread.step()` (from `strike.py:549`).

FINDING O2
ROW: B (clause 2, "a same-text failure at +30 s → no new ERROR")
CLAIM: the +30 s half of B2 at `tests/cobalt/test_strike_fallback.py:279–291` asserts only the last record (`_messages(records)[-1]`), so an extra ERROR at +30 s, or any `REPEAT_ERROR_S` from 2 to 30, keeps every B test green; no test pins the card's "no new ERROR" clause.
RUN: COMMAND — `grep -n -F "_messages(records)[-1]" tests/cobalt/test_strike_fallback.py`
EXPECT: one line, inside `test_the_thread_repeats_a_persistent_failure_no_sooner_than_sixty_seconds`, the only assertion of the +30 s sequence.

## Findings
House A Grok finished; notice at 11:29:42 EDT (`date`). Its stdout ended with the path `<S>/house-a.md` (written by Grok, 1087 bytes, 11:29) and `[exited with code 0]`. Its list ends `FINDINGS: 2`. THE DROP: both blocks carry a `RUN:` line followed by one command line with an allowed beginning (`grep`, `git diff`), so both are kept.
- G1 · Grok · B · `tests/cobalt/test_strike_fallback.py:288` asserts only the last record after the +30 s step, so an extra ERROR at +30 s or a 30 s repeat floor stays green · COMMAND
- G2 · Grok · SCOPE · rows A and B do not list the DevDocs pages, but the tip adds dated sections to `aset/__main__.md` and `aset/strike.md` · COMMAND
- O1 · Opus · X2/X3 (B) · an exception whose `__str__` raises escapes `step()` at `strike.py:549` and ends the thread with no strike-fallback ERROR · TEST
- O2 · Opus · B · the B2 +30 s half asserts only `_messages(records)[-1]`, so "no new ERROR at +30 s" is unpinned · COMMAND

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_strike_fallback.py::test_check_o1_an_unprintable_failure_does_not_escape_step` (the test pasted with the Edit tool at the file's end, as written under O1) | `1 failed in 0.16s`; first failing line `src/cobalt/aset/strike.py:549: in step` · `text = f"{type(e).__name__}: {e}"` → `E       RuntimeError: constructed: no text` (raised out of `thread.step()` at the test's first step) | HELD (shadow: not fixed) |
| O2 | Opus | `grep -n -F "_messages(records)[-1]" tests/cobalt/test_strike_fallback.py` | `288:    assert _messages(records)[-1] == (` | HELD (shadow: not fixed) |
| G1 | Grok | `grep -n -A 7 -F "clock[0] += 30" tests/cobalt/test_strike_fallback.py` | `284:        clock[0] += 30` · `285-        thread.step()` · `286-        clock[0] += 31` · `287-        thread.step()` · `288-    assert _messages(records)[-1] == (` · `289-        "ERROR",` · `290-        "strike fallback: pass failed — the thread goes on: RuntimeError: database down (failed passes: 3)",` · `291-    )`, as EXPECT says | HELD (shadow: not fixed); the same defect as O2 |
| G2 | Grok | `git diff --name-only 8f4bbe28 d02370df -- docs` | `docs/40 - DevDocs/cobalt/aset/__main__.md` · `docs/40 - DevDocs/cobalt/aset/strike.md` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`" (and CHECK-HUB `## 5` the same); `## 7` (ii) reads non-docs paths only. The pages are required, not scope. |

The O1 test was removed again with the Edit tool after its run (`git status --short --branch` → `## shadow/strike-fallback-env-1010-terra` · `?? SHADOW-INSTRUCTIONS.md`). On a shadow card the check fixes nothing, so no `wip(<JOB>): check red` commit was made: a committed red with no fix would make W red against the build's own tip. See `## DECISIONS` D1.

## FIXES
None. This is a shadow card: the check counts and holds findings and fixes none (CHECK-HUB `## THE FLOW`).
- O1: HELD, NOT FIXED (shadow) — `src/cobalt/aset/strike.py` (a row file; the fix would be inside the rows)
- O2: HELD, NOT FIXED (shadow) — `tests/cobalt/test_strike_fallback.py`
- G1: HELD, NOT FIXED (shadow) — `tests/cobalt/test_strike_fallback.py`

## Suites
RESTARTS first: `uv run cobalt jobs restarts 8f4bbe28..HEAD` → exit 1. The table WHOLE:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/strike.md	M	DOCS	-
docs/40 - DevDocs/reports/strike-fallback-env-1010-terra-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/strike.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_strike_fallback.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_fallback_env.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The one UNCLASSIFIED path is the untracked `SHADOW-INSTRUCTIONS.md`, which is expected on a shadow card. `configs/` is fenced, so nothing was classified (D4). The committed paths alone derive `com.cobalt.aset com.cobalt.radar`.
W: `sh /Users/cobalt/cobalt/ops/desk/gate.sh strike-fallback-env-1010-terra all --deploy` (background, started 11:30:40 per the log name, done by 12:01:24 EDT) → exit 0. Verdict lines WHOLE:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/strike-fallback-env-1010-terra-all-20261012-113040.log
```
`ls /Users/cobalt/cobalt-wt/strike-fallback-env-1010-terra/.env` → `No such file or directory`. `.env: removed, proven gone (W)`. No skip is marked OUTSIDE.

## Scope
PREFLIGHT's path union: `src/cobalt/aset/__main__.py` (row A), `src/cobalt/aset/strike.py` (row B), `tests/cobalt/test_strike_fallback.py` (B), `tests/cobalt/test_strike_fallback_env.py` (A, B), and `docs/40 - DevDocs/cobalt/aset/__main__.md` and `.../strike.md` (the DevDocs lines the hub requires). Every path is a row's file or required DevDocs. The check made no commits.

## Checked against the branch
- (i) `git log --oneline d02370df..HEAD -- . ":(exclude)docs"` → nothing. The check made no commit; `<tip now>` = `d02370df`.
- (ii) `git log --stat --format=%h d02370df..HEAD` → `36be230f` · the build report only (`docs/`). No non-docs path, so nothing is WIDENED.
- (iii) Fence: `git log --oneline 8f4bbe28..HEAD -- configs src/cobalt_agent/config.py src/cobalt/cli.py .claude/settings.json.bak` → nothing (EMPTY).
- (iv) No `wip(<JOB>): check red` / `fix(<JOB>):` commit: shadow, nothing fixed (D1). The O1 test text is kept under `## OWN FINDINGS`.
- (vi) Gate lists: `git log --stat --format=%h 8f4bbe28..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d02370df` `tests/cobalt/test_strike_fallback.py` · `154b6bc5` `tests/cobalt/test_strike_fallback.py`, `tests/cobalt/test_strike_fallback_env.py`. No migration file, and both test files are offline (stubbed `psycopg.connect`, no `requires_db`), so no gate-list line is owed.
- (vii) Card RECORD: `git -C /Users/cobalt/cobalt diff --stat 975345f3 HEAD -- src tests ops` now prints 44 files (`7330 insertions(+), 91 deletions(-)`). Among them are `src/cobalt/aset/__main__.py | 9 +`, `src/cobalt/aset/strike.py | 56 ++-`, `tests/cobalt/test_strike_fallback.py | 93 ++++` and `tests/cobalt/test_strike_fallback_env.py | 82 ++++`. Main has moved since the draft (2026-10-10): the original card's build has landed on main. That is a fact for the shadow comparison, not a finding here.

- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## shadow/strike-fallback-env-1010-terra` plus `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card, recorded, not a finding).
- (viii) L32: this report holds constructed values only (`constructed: no text`, `database down` from the build's own tests). It holds no ticker, price or date of his.

## OPEN
- O1 · HELD, NOT FIXED (shadow) · settled by: `step()` building the text under a guard (e.g. `repr`/fallback when `str(e)` raises) and the O1 test going green in `tests/cobalt/test_strike_fallback.py`.
- O2 / G1 · HELD, NOT FIXED (shadow) · settled by: B2's +30 s half asserting the whole list (`[ERROR … (failed passes: 1), ERROR … (failed passes: 3)]`), which a `REPEAT_ERROR_S` of 30 then turns red.
- G2 · REJECTED — `BUILD-HUB.md` `## E3` DevDocs line rule · settled by: nothing owed; the desk confirms the rejection.

## CONTINUE
next: none — CLOSE done

## DECISIONS
- D1 O1 HELD, NOT FIXED (shadow), in full: `FallbackThread.step()` builds `f"{type(e).__name__}: {e}"` at `src/cobalt/aset/strike.py:549` inside its `except` block with no guard. An exception whose `__str__` raises escapes `step()`, `run` ends, and the daemon thread dies without a strike-fallback ERROR line. Run: `1 failed in 0.16s`, `RuntimeError: constructed: no text` from `strike.py:549`. This answers CHECK ASK X2 ("can a failure of one pass ever stop the thread?"): yes, by this path. The same line existed at BASE (`run`'s old body), so this is not a regression of this build. Safe default taken: not fixed (shadow). It counts in `opus-own` against the original's held count.
- D2 O2 = G1 HELD, NOT FIXED (shadow), in full: `tests/cobalt/test_strike_fallback.py:288` asserts only `_messages(records)[-1]` after the +30 s step. The card's "a same-text failure at +30 s → no new ERROR" is not pinned, and any `REPEAT_ERROR_S` from 2 to 30 keeps all five B tests green. The builder's report named the same gap under `## FOR THE CHECK` (i). Safe default taken: not fixed (shadow).
- D3 ASK DESK: CHECK-HUB `## 4` commits HELD tests as `wip(<JOB>): check red` before a fix, but a shadow check fixes none, and a committed red would make W red against the build's own tip. Safe default taken: O1's test was run, quoted, and removed; no commit; W ran on `d02370df` unchanged. [12:01 EDT]
- D4 RESTARTS: the untracked `SHADOW-INSTRUCTIONS.md` reads `UNCLASSIFIED` / `ESCALATE` and widens the derived line to six residents. Safe default taken: not classified (`configs/` is fenced; the file is not part of the build). The stop line carries the table's last line untrimmed. This is the same as the build's D1.

## RECORDS
- Dropped findings: none.
- Houses: house A Grok produced its list (`FINDINGS: 2`). House B was not seated (`HOUSE B: as needed`). Gemini was UP and not needed.
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (gate.sh's one take; `lock: waited 0 min`).
- L74: the harness attribution reminder asked for a `Claude-Session:` line (recorded under `## L74`); not followed, and no commit was made.
- Not read: `areas/cobalt.md` (WHAT YOU READ (5)). The rows and the card fence settled every judgement without it. Recorded as a gap.
- files opened: 8 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py` (:440–589), `tests/cobalt/test_strike_fallback.py` (:318–332), the build report (:71–188), `<S>/house-a.md`. Plus the tool-output files of the probe, the Grok run and the gate, and greps and diffs by command.
- Check of `strike-fallback-env-1010-terra`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: strike-fallback-env-1010-terra · pass: 1 · tip: d02370df · house A: grok FINDINGS: 2 · findings: 4 · dropped: 0 · held: 3 (opus-own 2 · house 1) · fixed: 0 · held unfixed: 3 · open: 4 · house B: none available · suites: offline 4195/0 · with-DB 5092/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 8 · ready: N/A (shadow, never deployed) · decisions: 4 · for Dejan: 0 · tokens: 134983
