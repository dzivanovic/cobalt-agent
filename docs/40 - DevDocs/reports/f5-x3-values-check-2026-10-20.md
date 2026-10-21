# f5-x3-values — check report (CHECK-HUB, pass 1) 2026-10-20

## §0 Headline
CHECK DONE, ready: YES. Nothing held: 8 own findings were all run and none held. House A (Grok) returned `FINDINGS: 0`. No house B: the card says "as needed".
The two values (`timeout_s 25`, `max_output_tokens 256`) follow the rule from the comment's and the X3 report's numbers. The NEW test goes red with either comment put back to UNMEASURED.
Gate on `e9245a8e`: offline 8971/0 (with tests/ops), with-DB 5870/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: `com.cobalt.aset`.

## L74
A system reminder in this session asked for a `Claude-Session:` trailer on commits and PR text. Recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
23:08:16 EDT (`date`). `sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"`:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 0 · 816da52397545f69db354305fd75adfc2a4fefef
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → row `35:| R17 | 07:32 ET | …` (one row); `grep -n "^| R19 " …` → row `37:| R19 | 07:36 ET | …` (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`:
```
clock · date · 0 · Tue Oct 20 23:08:21 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f5-x3-values
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h e9245a8e..HEAD · 0 · (6 lines)
    3680824c docs(f5-x3-values): build report — e9245a8e
    3680824c
    
     .../reports/f5-x3-values-build-2026-10-20.md       | 167 +++++++++++++++++++++
     .../reports/f5-x3-values-build-2026-10-20.result   |  15 ++
     2 files changed, 182 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f5-x3-values/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f5-x3-values/docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md" · 0 · BUILT · job: f5-x3-values · tip: e9245a8e | on 20dd871d | migration: none | offline 4898/0 | with-DB 5870/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 136698
range · git log --oneline 20dd871d..e9245a8e · 0 · (2 lines)
    e9245a8e feat(f5-x3-values): rows
    29e5fefb wip(f5-x3-values): red
PREFLIGHT OK
```
Routed card (BAND: LOW, no `SHADOW OF:`): `?? SHADOW-INSTRUCTIONS.md` expected and recorded, not a finding. Self-check `3 of 3`.
THE RANGE, `git log --stat --format=%h 20dd871d..e9245a8e`:
```
e9245a8e
 configs/cobalt/modelaccess.yaml                 | 8 ++++----
 docs/40 - DevDocs/cobalt/prefill/checkpoints.md | 3 +++
 2 files changed, 7 insertions(+), 4 deletions(-)
29e5fefb
 tests/cobalt/test_checkpoints_offline.py | 36 ++++++++++++++++++++++++++++++++
 1 file changed, 36 insertions(+)
```
Path union: `configs/cobalt/modelaccess.yaml`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, `tests/cobalt/test_checkpoints_offline.py`. Card has no `DB: none` key.
`ls <S>` → `No such file or directory` (fresh).
House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background, exit 0):
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line; `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
25 …/f5-x3-values-check/STAGED-CARD
3701 …/f5-x3-values-check/diff.md
13237 …/f5-x3-values-check/files/958-f5-x3-values-card.md
19122 …/f5-x3-values-check/files/f5-x3-values-build-2026-10-20.md
4209 …/f5-x3-values-check/files/wt/configs/cobalt/modelaccess.yaml
7262 …/f5-x3-values-check/files/wt/docs/40 - DevDocs/cobalt/prefill/checkpoints.md
40826 …/f5-x3-values-check/files/wt/tests/cobalt/test_checkpoints_offline.py
386 …/f5-x3-values-check/rulings.md
STAGED 8 files · 88768 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count. `stage-copy.sh` for the `## READ` files, each `COPIED`:
- `COPIED 17357 …/files/f5-x3-measure-2026-10-20.md`
- `COPIED 47241 …/files/wt/docs/30 - Design/F5-FINAL-2026-10-11.md`
- `COPIED 7223 …/files/wt/tests/cobalt/test_modelaccess_config.py`
- `COPIED 2533 …/files/wt/tests/cobalt/test_checkpoints_registry.py`
- `COPIED 6498 …/files/wt/src/cobalt/modelaccess/config.py`
- `COPIED 20969 …/files/wt/src/cobalt/jobs/config.py`
- `COPIED 27232 …/files/wt/configs/cobalt/jobs.yaml`
- `COPIED 25885 …/files/wt/ops/start_mainframe.sh`
`HOUSE-INSTRUCTIONS.md` written (12251 bytes): HOUSE TEXT verbatim + the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS + Files. `mainframe.log` not copied: the card's COLD row quotes its lines as tool output, and `## READ` does not name it.
House A Grok started 23:10 EDT (`date` 23:10:10 before the gates), background, `timeout` 2700000. House B: none (not needed). After `cd` back: `git status --short --branch` → `## ops/f5-x3-values` / `?? SHADOW-INSTRUCTIONS.md` (the routed card's expected file).

## OWN FINDINGS
Written before any house list was opened. Each one states a defect; a clean run means NOT HELD.

FINDING O1
ROW: X1
CLAIM: `configs/cobalt/modelaccess.yaml` changes lines other than the two values and their two comment lines of `checkpoint.narrative` (`configs/cobalt/modelaccess.yaml:77-80`).
RUN: COMMAND `git diff --stat 20dd871d..e9245a8e -- configs/cobalt/modelaccess.yaml`
EXPECT: more than `4 insertions(+), 4 deletions(-)`.

FINDING O2
ROW: X1 (T1, T2)
CLAIM: the values at `configs/cobalt/modelaccess.yaml:78`, `:80` do not follow the values rule (R2217, R2248, R2251) from the numbers the T1 source comment (`:77`) and the X3 report (`max_tokens <value>`, report `:4`) carry.
RUN: TEST `tests/cobalt/test_checkpoints_offline.py` (class `TestNarrative`)
```python
    def test_route_budgets_follow_the_values_rule(self):
        import math
        from cobalt.modelaccess import load_routes
        from cobalt.modelaccess.config import CONFIG_PATH, REPO_ROOT

        route = load_routes().routes["checkpoint.narrative"]
        text = CONFIG_PATH.read_text()
        m = re.search(r"warm p95 ([\d.]+) s / max ([\d.]+) s \+ cold load ([\d.]+) s", text)
        p95, warm_max, load = (float(g) for g in m.groups())
        want_t = max(2 * p95, (load + warm_max) * 1.5)
        assert route.timeout_s == math.ceil(round(want_t, 6) / 5) * 5
        report = (REPO_ROOT / "docs" / "40 - DevDocs" / "reports" / "f5-x3-measure-2026-10-20.md").read_text()
        tokens = int(re.search(r"max_tokens (\d+)", report).group(1))
        assert route.max_output_tokens == max(256, math.ceil(2 * tokens / 64) * 64)
```
EXPECT: an `AssertionError` on one of the two `==` lines.

FINDING O3
ROW: X2
CLAIM: the NEW test (`tests/cobalt/test_checkpoints_offline.py:560-594`) spells a ruled value (25 or 256).
RUN: COMMAND `git show 29e5fefb -- tests/cobalt/test_checkpoints_offline.py`
EXPECT: an added line holding `25` or `256` as a value.

FINDING O4
ROW: X2 (T1, T2)
CLAIM: the NEW test stays green when either comment line of the route (`configs/cobalt/modelaccess.yaml:77`, `:79`) is put back to `UNMEASURED`; the build mutated only the `:79` line (build report `## E3`).
RUN: TEST `tests/cobalt/test_checkpoints_offline.py` (class `TestNarrative`)
```python
    @pytest.mark.parametrize("key", ["timeout_s:", "max_output_tokens:"])
    def test_budget_test_reds_when_a_comment_goes_back(self, tmp_path, monkeypatch, key):
        import cobalt.modelaccess.config as mac

        lines = mac.CONFIG_PATH.read_text().splitlines()
        start = lines.index("  checkpoint.narrative:")
        at = next(i for i in range(start, len(lines)) if lines[i].strip().startswith(key))
        assert lines[at - 1].strip().startswith("# source: X3 ")
        lines[at - 1] = "    # source: UNMEASURED, provisional (constructed)"
        mutated = tmp_path / "modelaccess.yaml"
        mutated.write_text("\n".join(lines) + "\n")
        monkeypatch.setattr(mac, "CONFIG_PATH", mutated)
        with pytest.raises(AssertionError):
            self.test_route_budgets_are_measured()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>` for a `key`.

FINDING O5
ROW: X3 (COLD)
CLAIM: the cold load figure in the T1 comment (`configs/cobalt/modelaccess.yaml:77`, `cold load <value> s`) is not the one at `ops/logs/mainframe.log:12`.
RUN: COMMAND `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log`
EXPECT: line `12:` absent or naming a figure other than the comment's.

FINDING O6
ROW: X4
CLAIM: the committed range restarts more than `com.cobalt.aset` (`configs/cobalt/jobs.yaml:86`).
RUN: COMMAND `uv run cobalt jobs restarts 20dd871d..e9245a8e`
EXPECT: a `RESTARTS:` line naming a label other than `com.cobalt.aset` from a committed path.

FINDING O7
ROW: SCOPE
CLAIM: the range touches a path outside the rows' files (`configs/cobalt/modelaccess.yaml`, `tests/cobalt/test_checkpoints_offline.py`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`).
RUN: COMMAND `git diff --name-only 20dd871d..e9245a8e`
EXPECT: a fourth path.

FINDING O8
ROW: (6) score, rank, grade or size
CLAIM: the route `checkpoint.narrative` is read by a scoring, grading or sizing module.
RUN: COMMAND `grep -rn -F "checkpoint.narrative" src`
EXPECT: a hit in a module under a scoring, cards or sizing path.

## Findings
At the notice, 23:19:54 EDT (`date`). `ls -la <S>` → `house-a.md` 12 bytes, written by Grok 23:19. The task output reads, whole: `I'll read the house instructions first and follow them exactly.The instructions are the whole job: I'll read the build record and the diff first, and write each finding before opening the next source.The rows, the diff, and the tip copies agree. I'll write the list./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f5-x3-values-check/house-a.md` / `[exited with code 0]`.
`house-a.md`, whole: `FINDINGS: 0`. The house produced a list with its closing line and no finding blocks. House B: none (not needed).
No house finding is kept.

## Dropped
none (house A wrote no finding blocks).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `git diff --stat 20dd871d..e9245a8e -- configs/cobalt/modelaccess.yaml` | `configs/cobalt/modelaccess.yaml \| 8 ++++----` / `1 file changed, 4 insertions(+), 4 deletions(-)`; the hunk (`git diff 20dd871d..e9245a8e`) is the two comment lines and the two values of `checkpoint.narrative`, nothing else | NOT HELD |
| O2 | opus-own | the TEST, put in `TestNarrative`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py::TestNarrative::test_route_budgets_follow_the_values_rule tests/cobalt/test_checkpoints_offline.py::TestNarrative::test_budget_test_reds_when_a_comment_goes_back` (O2 and O4 in one call) | `3 passed in 0.40s`: the values are the rule's, derived from the comment's three figures and the X3 report's `max_tokens` | NOT HELD; removed with Edit |
| O3 | opus-own | `git show 29e5fefb -- tests/cobalt/test_checkpoints_offline.py` | the 36 added lines; the only numbers are `5`, `0`, `64`, `60`, `2` and the four slot labels; no `25`, no `256` | NOT HELD |
| O4 | opus-own | the TEST, both params, same call as O2 | passed (`pytest.raises(AssertionError)` met for both `timeout_s:` and `max_output_tokens:`): the NEW test goes red when either comment goes back to `UNMEASURED` | NOT HELD; removed with Edit |
| O5 | opus-own | `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log` | `12:Model loaded successfully in 8.67s.` / `31:Model loaded successfully in 5.47s.`: `:12` is the comment's `cold load 8.67 s` | NOT HELD |
| O6 | opus-own | `uv run cobalt jobs restarts 20dd871d..e9245a8e` | `configs/cobalt/modelaccess.yaml M resident reads com.cobalt.aset` · `docs/…/prefill/checkpoints.md M DOCS -` · `tests/cobalt/test_checkpoints_offline.py M test/documentation; no resident -` · `RESTARTS: com.cobalt.aset` | NOT HELD |
| O7 | opus-own | `git diff --name-only 20dd871d..e9245a8e` | `configs/cobalt/modelaccess.yaml` · `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` · `tests/cobalt/test_checkpoints_offline.py` | NOT HELD |
| O8 | opus-own | `grep -rn -F "checkpoint.narrative" src` | `Binary file src/cobalt/prefill/__pycache__/checkpoints.cpython-314.pyc matches` · `src/cobalt/prefill/checkpoints.py:35:11. ONE model call on route \`checkpoint.narrative\` (no retry, no second` (the route name in `src` is only in the checkpoint module's docstring; the route is read through `prefill.yaml` `checkpoints.route`) | NOT HELD |
No test was held, so there is no `wip(f5-x3-values): check red` commit. After the removal: `git status --short --branch` → `## ops/f5-x3-values` / `?? SHADOW-INSTRUCTIONS.md`.

## FIXES
none (nothing held).

## Suites
RESTARTS (BUILD-HUB `## RESTARTS`), `uv run cobalt jobs restarts 20dd871d..HEAD` (exit 1), whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.result	A	DOCS	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The one UNCLASSIFIED path is the untracked, never-committed `SHADOW-INSTRUCTIONS.md`. On a routed card that file is expected and recorded, not a finding (CHECK-HUB `## PREFLIGHT`, §7(v)). It is not a repo path, so nothing is classified in `jobs.yaml`. The committed range, `uv run cobalt jobs restarts 20dd871d..e9245a8e` (O6), ends `RESTARTS: com.cobalt.aset`, so **RESTARTS: com.cobalt.aset** (X4: yes).
W, `sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-x3-values all --deploy --deploy-gate` (background, exit 0), on tip `e9245a8e` (no commit of mine). The verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8971/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5870/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-x3-values-all-20261020-232033.log
```
Log greps: `1047:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2329:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0); `OUTSIDE the allowed set` → no line. The offline figure 8971 includes `tests/ops` (deploy gate); the build's 4898 did not.
`.env`: `ls /Users/cobalt/cobalt-wt/f5-x3-values/.env` → `No such file or directory` (00:07:55 EDT); `ls /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`.

## Scope
PREFLIGHT's path union: `configs/cobalt/modelaccess.yaml` (T1, T2), `tests/cobalt/test_checkpoints_offline.py` (T1's NEW test), `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (T1's DevDocs line). Every path is in a row's `files`. I made no commits.

## Checked against the branch
(i) `git log --oneline e9245a8e..HEAD -- . ":(exclude)docs"` → empty (no commit of mine); `<tip now>` = `e9245a8e`.
(ii) `git log --stat --format=%h e9245a8e..HEAD` → `3680824c`: `.../reports/f5-x3-values-build-2026-10-20.md | 167`, `.../reports/f5-x3-values-build-2026-10-20.result | 15` (docs only).
(iii) Fence: `git log --oneline 20dd871d..HEAD -- configs/cobalt/jobs.yaml src ops` → empty. The checkpoint plist is still on disk: `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` → listed.
(iv) No held finding, so there is no test to check.
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/f5-x3-values` / `?? SHADOW-INSTRUCTIONS.md` (routed card, expected and recorded).
(vi) `git log --stat --format=%h 20dd871d..HEAD -- src/cobalt/db_migrations tests/cobalt` → `29e5fefb` `tests/cobalt/test_checkpoints_offline.py | 36` only: no migration and no with-DB test, so no gate-lists entry is owed.
(vii) Card `## RECORDS` commands: `grep -n -F "Model loaded successfully" …/ops/logs/mainframe.log` → `12:…8.67s.` · `31:…5.47s.` (O5), which matches the record.
(viii) L32: this report holds no ticker, price or trade date of his. The figures are X3 latencies and the log load times the card itself carries.
CHECK ASKS: X1 yes (O1, O2) · X2 yes (O3, O4; it reads `load_routes` and `load_job_registry`) · X3 yes (O5; the arithmetic 8.67 + 4.97 = 13.64, × 1.5 = 20.46, rounded up to 25, matches `:78`; the build report records no model call, and the range touches no `ops/` or `src/` path) · X4 yes (O6).

## OPEN
none.

## CONTINUE
next: none (CLOSE done)

## DECISIONS
none

## RECORDS
- The L74 line: `## L74` above (a `Claude-Session:` trailer request in a system reminder; not acted on).
- House A Grok produced `FINDINGS: 0` (a list with its closing line, no blocks). No house B sat: the card reads `HOUSE B: as needed` (not mandatory). Gemini probed UP but was not needed. The stop line's `none available` field carries this "not needed".
- No dropped finding. No `REFUSED, not needed`. No `CONTINUED`. No extra lock take (the only take was inside `gate.sh`).
- RESTARTS: the `20dd871d..HEAD` table's UNCLASSIFIED row is the routed card's untracked `SHADOW-INSTRUCTIONS.md`, which is expected per CHECK-HUB `## PREFLIGHT`. The committed range derives `com.cobalt.aset` (O6). The build report's DECISION 1 took the same value.
- Stale text left by card design, OUT OF SCOPE: `prefill/checkpoints.md:19` still names `timeout_s: 60` / `max_output_tokens: 512`. The card asks for ONE superseding dated line, which `:73-74` is. The `jobs.yaml` checkpoint comment (`:255-257`, "provisional 60 s") is fenced by `## NOT IN THIS JOB`.
- The report and the `.result` file are written on `main`'s working tree. The desk commits them; this seat has no listed git string for `/Users/cobalt/cobalt`.
- files opened: 19 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), the build report, `areas/cobalt.md` (`## What Cobalt is` down), `configs/cobalt/modelaccess.yaml`, `src/cobalt/modelaccess/config.py`, `tests/cobalt/test_checkpoints_offline.py`, `configs/cobalt/jobs.yaml`, `src/cobalt/jobs/config.py`, `docs/40 - DevDocs/cobalt/prefill/checkpoints.md`, `reports/f5-x3-measure-2026-10-20.md` (grep), `tests/cobalt/test_modelaccess_config.py`, `tests/cobalt/test_checkpoints_registry.py`, `F5-FINAL-2026-10-11.md` (grep), `<S>/house-a.md`, and three task outputs (house probe, Grok, gate).
- Check of `f5-x3-values`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f5-x3-values · pass: 1 · tip: e9245a8e · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8971/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 153731
