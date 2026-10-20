# cos-probe-fr1 — check report — 2026-10-20

## §0 Headline
- CHECK DONE on `da47500a`, ready YES. The port matches the old checked tip `f8b2887b`; cli.md differs only by main's f16 and f5 sections.
- 9 findings (2 mine, 7 Grok's), none dropped. Two held and were fixed in `probe.py`: the auth check and `ps` now run in the scratch cwd (G2), and X14 FAILs past `cos.max_turns` (G5).
- 6 open: the source-tip question (O1/G1), the resident's `pgrep` (G3, fenced), the X2 file scope (G4), cli.md drift (G6), and merge-base (G7, the desk's).
- Gate: offline 8959/0, with-DB 5858/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. House B was not needed (Gemini was up). Decisions: 4, none for Dejan.
- The `open:` count in the stop line counts O1 and G1 as two items.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/877-cos-probe-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/877-cos-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/877-cos-probe-card.md" · 0 · 3da7d25ccd7acbbe4a07cee52ab7e88d47af3b16
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/877-cos-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, whole:
```
clock · date · 0 · Tue Oct 20 10:46:52 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-probe-fr1
head · git log --oneline -1; git log --stat --format=%h 78b93da3..HEAD · 0 · (6 lines)
    a2e562d2 docs(cos-probe-fr1): build report — 78b93da3
    a2e562d2
    
     .../reports/cos-probe-fr1-build-2026-10-20.md      | 151 +++++++++++++++++++++
     .../reports/cos-probe-fr1-build-2026-10-20.result  |  15 ++
     2 files changed, 166 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-probe-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-probe-fr1/docs/40 - DevDocs/reports/cos-probe-fr1-build-2026-10-20.md" · 0 · BUILT · job: cos-probe-fr1 · tip: 78b93da3 | on 0f3c3e01 | migration: none | offline 4884/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 (PORT · PROOF 6 of 6) | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 218983
range · git log --oneline 0f3c3e01..78b93da3 · 0 · 78b93da3 feat(cos-probe-fr1): port cos-probe-1019 at its checked tip f8b2887b onto main, cli.md seam appended after f5-checkpoints-1018 (PORT; L79, R1485)
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h 0f3c3e01..78b93da3` · 0 · `78b93da3` · `docs/40 - DevDocs/cobalt/cli.md | 3 +` · `docs/40 - DevDocs/cobalt/cos/README.md | 6 +` · `src/cobalt/cos/cli.py | 19 +-` · `src/cobalt/cos/probe.py | 470 +++` · `tests/cobalt/test_cos_probe.py | 473 +++` · `tests/cobalt/test_hitl_offline.py | 18 ++` · `6 files changed, 988 insertions(+), 1 deletion(-)`. Path union = the PORT row's six files.
- The card carries no "DB: none" header.
- `ls <S>` · 1 · `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · `grok: UP` · `gemini: UP`.
- No `HOUSE A:` header line; `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · whole:
```
22 <S>/STAGED-CARD
42553 <S>/diff.md
21804 <S>/files/877-cos-probe-card.md
20478 <S>/files/cos-probe-fr1-build-2026-10-20.md
8503 <S>/files/wt/docs/40 - DevDocs/cobalt/cli.md
6230 <S>/files/wt/docs/40 - DevDocs/cobalt/cos/README.md
1643 <S>/files/wt/src/cobalt/cos/cli.py
18577 <S>/files/wt/src/cobalt/cos/probe.py
18753 <S>/files/wt/tests/cobalt/test_cos_probe.py
8424 <S>/files/wt/tests/cobalt/test_hitl_offline.py
386 <S>/rulings.md
STAGED 11 files · 147373 bytes · commits 1
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-probe-fr1-check`.) `## READ` files, each `stage-copy.sh` → `COPIED`: `F20-FINAL-2026-10-11.md` 36631 · `cos/session.py` 14955 · `cos/tools.py` 5085 · `agents/cos.yaml` 1438 · `hitl/card.py` 2645 · `redact/guard.py` 8273 · `redact.yaml` 10238 · `test_cos_offline.py` 23205 · `draft-cos-gate-amend-2026-10-19.md` 5487. `HOUSE-INSTRUCTIONS.md` written (23103 bytes).
House A Grok started 10:49 EDT (`date` 10:49:02), background task `bv8rrs6aj`; no house B.

## OWN FINDINGS
Written before either house list was opened. Read: the diff `0f3c3e01..78b93da3` and its six files at the tip, `git diff` of the port against `8f47d85b` and `f8b2887b`, main's `src/cobalt/cli.py` and `configs/cobalt/jobs.yaml` drift since `07eb89a3`, `session.py` `_client` / `_transport` lines.

FINDING O1
ROW: PORT (CHECK ASK P1)
CLAIM: The card's PROOF says five files are byte-equal to `8f47d85b`; three of them are not — `src/cobalt/cos/probe.py` (+12), `tests/cobalt/test_cos_probe.py` (+54, `:422-473`) and `cos/README.md` (+3) carry `f8b2887b`, the old check's fix commit (build DECISIONS 1).
RUN: COMMAND `git diff --stat 8f47d85b 78b93da3 -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"`
EXPECT: three files changed, 69 insertions.

FINDING O2
ROW: P1 (THE BOUNDARY (a)) · CHECK ASK X1
CLAIM: The repo half of the scratch refusal (`src/cobalt/cos/probe.py:169-171`, "the repo") is pinned by no test (`test_cos_probe.py:313-319` pins only the real-HOME half); a scratch under the repo must be refused with nothing spawned and nothing left.
RUN: TEST `tests/cobalt/test_cos_probe.py`
```python
def test_a_scratch_dir_under_the_repo_is_refused(rig, monkeypatch, capsys, tmp_path):
    from cobalt.cos import probe

    repo = (tmp_path / "repo").resolve()
    (repo / "tmp").mkdir(parents=True)
    monkeypatch.setattr(probe, "REPO_ROOT", repo)
    monkeypatch.setattr(tempfile, "tempdir", str(repo / "tmp"))
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert code == 1 and out.startswith("PROBE X11 FAIL refused: the scratch dir is under the repo"), out
    assert rig.fakes == [] and rig.calls == []
    assert list((repo / "tmp").iterdir()) == []
```
EXPECT: if the clause is not built, the assertion on the `refused:` line fails; green means the clause holds (NOT HELD).

## Findings
House A Grok finished 11:05 (`date` 11:05:56; task exit 0, its reply the path of `<S>/house-a.md`, 4513 bytes, last line `FINDINGS: 7`). Every block carries a `RUN:` with a test function or an allowed command: none dropped.
- G1 · Grok · P1/PORT · the port carries `8f47d85b`'s later check fixes (`probe.py:332`, `:465`), against the PORT row's letter · COMMAND
- G2 · Grok · X1 · `claude auth status` (`probe.py:133`) and `ps` (`:141`) run with no `cwd`, so they inherit the repo cwd, not the scratch · TEST
- G3 · Grok · P1 (e) · a killed turn makes the resident's `_kill_tree` start `pgrep` (`session.py:146`), a process (e) does not name · TEST
- G4 · Grok · X4 · X2/X10 "no written file" lists only `home/work` (`probe.py:316`); a file written elsewhere in the scratch HOME passes · TEST
- G5 · Grok · X4 · X14 OK from the ok count alone (`probe.py:417`); measured `num_turns` never compared with `cfg.max_turns` · TEST
- G6 · Grok · P1/PORT · cli.md vs `8f47d85b` holds main's f5 section too, not only f16-close · COMMAND
- G7 · Grok · P3 · merge-base is `0f3c3e01` while main moved · COMMAND

## Dropped
none

## RUNS
- O1 · opus · `git diff --stat 8f47d85b 78b93da3 -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"` · `cos/README.md | 3 ++` · `probe.py | 12 ++++++++` · `test_cos_probe.py | 54 +++` · `3 files changed, 69 insertions(+)` · UNSETTLED — the card's letter (port `8f47d85b`) and its own record ("code tip 8f47d85b, check ready YES") disagree: the old check's YES stands on `f8b2887b`; porting the letter brings back four held defects. The desk settles (DECISIONS 1).
- O2 · opus · test `test_a_scratch_dir_under_the_repo_is_refused` · `1 passed in 0.55s` · NOT HELD (the repo refusal is built); removed again.
- G1 · Grok · `git diff -U0 8f47d85b -- src/cobalt/cos/probe.py` · hunks `@@ -331,0 +332,3 @@` (`if _init_tools(turn.messages) is None:` … `return False, f"the session never ran …"`), `@@ -436,0 +440,5 @@` (`logger.disable("cobalt.cos.session")`), `@@ -449,0 +458,2 @@`, `@@ -453,0 +464,2 @@` (`clause = " ".join(clause.split())`) · UNSETTLED — the same fact as O1; the desk settles (DECISIONS 1).
- G2 · Grok · test `test_auth_and_ps_are_spawned_with_cwd_inside_scratch` · `1 failed in 0.56s` · `AssertionError: (['claude', 'auth', 'status'], None)` · HELD (CHECK ASK X1: the auth child ran in the caller's cwd, the repo when run from it).
- G3 · Grok · test `test_the_killed_turn_does_not_start_pgrep` · `1 failed in 0.55s` · `AssertionError: PROBE X3 FAIL error AssertionError` (the rig's `subprocess.run` refuses the resident kill's `pgrep`) · REJECTED — P1 (c) "THE SESSION is the resident's" and (e) "the only subprocesses the probe ITSELF starts"; the `pgrep` is `session.py`'s `_kill_tree`, inside the fence (`## NOT IN THIS JOB`: no edit to `session.py`). The old check carried the same item open (its A1). Test removed again (its text is above in house-a.md).
- G4 · Grok · test `test_x2_a_file_outside_cwd_but_inside_scratch_is_a_fail` · `1 failed in 0.55s` · `AssertionError: PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)` · UNSETTLED — a write outside cwd needs a tool call, which the allowlist check (`probe.py:326-329`) already FAILs; a scratch-wide file check would also count the CLI's own state under its HOME, which no run has measured (a live run is `## NOT IN THIS JOB`). Settles on the gate seat's first live X2. Test removed again.
- G5 · Grok · test `test_x14_fails_when_measured_turns_exceed_the_cap` · `1 failed in 0.56s` · `AssertionError: PROBE X14 OK ok 20/20 · max num_turns 50 · max seconds 0.0 (caps: max_turns 5, timeout 0.2s)` · HELD (the card's X14 default: "OK iff all 20 end ok within `cos.max_turns`").
- G6 · Grok · `git diff -U0 8f47d85b -- "docs/40 - DevDocs/cobalt/cli.md"` · `+## 2026-10-19 — f16-close-1018` … `+## 2026-10-19 — f5-checkpoints-1018` (6 lines at `@@ -143,0 +144,6 @@`) · REJECTED — PORT row: "Any other drift the builder finds … is folded into this row"; the build's PROOF line 6 names both sections.
- G7 · Grok · `git log --oneline HEAD..main` · `3da7d25c docs(desk): cos-probe-fr1 BUILT 78b93da3, card TIP set` · `7ef040af docs(desk): F5 fr2 deployed 25c51ca0, cos-probe card BASE reset to 0f3c3e01` · REJECTED — CHECK ASK P3: "Before the deploy card the desk proves `git merge-base main <tip>`": the desk's step; both commits are docs only.
`wip(cos-probe-fr1): check red — G2, G5` → `727efa05` (`1 file changed, 29 insertions(+)`).

## FIXES
- G2 + G5 · `src/cobalt/cos/probe.py`: `_auth_exit(cwd)` and `_child_env_names(pid, cwd)` pass `cwd` = scratch `home/work`; `_x14` returns OK only when `max_turns <= cfg.max_turns` too. Doc line `## 2026-10-20 — cos-probe-fr1 (check)` in `docs/40 - DevDocs/cobalt/cos/README.md`. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` → `63 passed in 4.53s`. Commit `da47500a fix(cos-probe-fr1): auth check and ps in the scratch cwd; X14 FAIL past cos.max_turns (check G2, G5)` (`2 files changed, 14 insertions(+), 9 deletions(-)`).

## Suites
RESTARTS (`BUILD-HUB.md` `## RESTARTS`), `uv run cobalt jobs restarts 0f3c3e01..HEAD` · 0 · whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr1-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr1-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cos/probe.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
W on `da47500a`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr1 all --deploy --deploy-gate` · exit 0 · whole:
```
tests/ops: run (deploy gate)
offline 8959/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5858/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr1-all-20261020-110757.log
```
No skip line marked `OUTSIDE the allowed set`. `ls /Users/cobalt/cobalt-wt/cos-probe-fr1/.env` → `No such file or directory`.
New tests, each shown red first (`## RUNS`): `test_auth_and_ps_are_spawned_with_cwd_inside_scratch`, `test_x14_fails_when_measured_turns_exceed_the_cap`.

CHECK ASK X5 (X20 mutation, Edit on `configs/cobalt/redact.yaml:131`, undone, never committed): `[?&]` → `[?&#]`, `key` → `k|key` → `uv run pytest … test_hitl_offline.py::test_x20_redact_keeps_the_card_fragment_key` → `1 failed in 0.06s`, `assert ('#k=' + '0123456789abcdef0123456789abcdef') in 'Review, then approve or deny: https://sheet.example.invalid/hitl/7#k=[REDACTED:url_query_secret]'`. Undone: `git status --short --branch` → `## ops/cos-probe-fr1` alone; the same test → `1 passed in 0.03s`. The test runs the real `redact()` on the real `redact.yaml`, and its mutation is red.
CHECK ASK X3: `git log --oneline 0f3c3e01..HEAD -- src/cobalt/cos/session.py src/cobalt/cos/run.py …` → empty; `test_cos_run_is_unchanged` and `test_the_probe_is_mounted_and_lists_the_seven_items` green in the targeted run (63 passed).

## Scope
PREFLIGHT path union (the PORT row's six files) plus my commits: `tests/cobalt/test_cos_probe.py` (727efa05), `src/cobalt/cos/probe.py` and `docs/40 - DevDocs/cobalt/cos/README.md` (da47500a). Every path is in the PORT row's `files`.

## Checked against the branch
(i) `git log --oneline 78b93da3..HEAD -- . ":(exclude)docs"` → `da47500a fix(cos-probe-fr1): auth check and ps in the scratch cwd; X14 FAIL past cos.max_turns (check G2, G5)` · `727efa05 wip(cos-probe-fr1): check red — G2, G5`. `<tip now>` = `da47500a`.
(ii) `git log --stat --format=%h 78b93da3..HEAD` → `da47500a`: `cos/README.md | 3`, `src/cobalt/cos/probe.py | 20`; `727efa05`: `tests/cobalt/test_cos_probe.py | 29`; `a2e562d2`: the build report and its `.result`. Every non-docs path is a row file or a test file.
(iii) `git log --oneline 0f3c3e01..HEAD -- src/cobalt/cos/session.py src/cobalt/cos/run.py src/cobalt/cos/listener.py src/cobalt/cos/tools.py src/cobalt/redact configs/cobalt/redact.yaml configs/cobalt/agents/cos.yaml configs/cobalt/taxonomy/tunables.yaml src/cobalt_agent` → empty.
(iv) `grep -n -F "def test_auth_and_ps_are_spawned_with_cwd_inside_scratch" tests/cobalt/test_cos_probe.py` → `481:`; `grep -n -F "def test_x14_fails_when_measured_turns_exceed_the_cap" …` → `499:`; red `727efa05` sits below fix `da47500a` in (i).
(v) `ls <WT>/.env` → "No such file or directory"; `git status --short --branch` → `## ops/cos-probe-fr1` alone.
(vi) `git log --stat --format=%h 0f3c3e01..HEAD -- src/cobalt/db_migrations tests/cobalt` → `727efa05` (`test_cos_probe.py`), `78b93da3` (`test_cos_probe.py`, `test_hitl_offline.py`): no migration, no with-DB test file. No gate-lists change needed.
(vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: nothing to run. Its seam facts were re-read by content: `git diff f8b2887b 78b93da3 -- "docs/40 - DevDocs/cobalt/cli.md"` → only main's f16-close-1018 and f5-checkpoints-1018 sections, inserted between f21-genesis-1013 and cos-probe-1019 (CHECK ASK P2: the F5 section is already on main, no open seam); `git diff --stat f8b2887b 78b93da3` over the six files → `cli.md | 6` only (CHECK ASK P1, against the checked tip).
(viii) L32: this report holds constructed values only (the test key `0123456789abcdef`×2 and the `.invalid` host are the test's own).

## OPEN
- O1 / G1 · UNSETTLED · the port's source is `f8b2887b` (the checked tip), not the card's `8f47d85b`. Settled by the desk naming the source tip (DECISIONS 1).
- G3 · REJECTED · `pgrep` started by the resident's `_kill_tree` on a killed turn; the fix would be in `session.py` (fence). Settled by a session.py card, or by the desk accepting it as the SDK side of (e) (DECISIONS 2).
- G4 · UNSETTLED · X2/X10 "no written file" covers `home/work` only; a write elsewhere needs a tool call, which already FAILs. Settled by the gate seat's first live X2 listing what the CLI itself writes under the scratch HOME (DECISIONS 3).
- G6 · REJECTED · cli.md carries main's f5 section too: drift the PORT row folds in. Nothing to settle.
- G7 · REJECTED · merge-base `0f3c3e01`, main ahead by two docs commits: the desk's P3 before the deploy card (DECISIONS 4).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK (PORT source tip; O1, G1) [11:55]: the card ports `8f47d85b`; the build ported `f8b2887b`, the tip the old check marked ready YES (build DECISIONS 1). Verified: `git diff --stat f8b2887b 78b93da3` over the six files → `cli.md` only. Default taken: keep `f8b2887b`; the check's two new fixes sit on top of it.
2. ASK DESK (G3, the resident kill's `pgrep`) [11:55]: a killed turn runs `pgrep` from `session.py`'s `_kill_tree`, not from the probe. A change would be in `session.py`, inside the fence. Default taken: not fixed, carried open (the old check's A1 too).
3. ASK DESK (G4, X2/X10 file scope) [11:55]: the written-file check covers the session cwd only. Default taken: unchanged; the gate seat's first live X2 records what the CLI writes under the scratch HOME, then a follow-up decides whether to widen.
4. ASK DESK (G7 / CHECK ASK P3) [11:55]: `git log --oneline HEAD..main` → `3da7d25c`, `7ef040af` (docs only). Default taken: none here; the desk proves merge-base = main HEAD before the deploy card.

## RECORDS
- Clock (`date`): 10:46 PREFLIGHT · 10:49 Grok started · own findings written before 11:05 · 11:05 Grok's list read · 11:07 gate started · 11:55 close.
- Dropped findings: none. Houses that produced nothing: none. House B: not seated (`HOUSE B: as needed`; Gemini was UP).
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (the gate took and released its own).
- L74: one `Claude-Session:` reminder, recorded under `## L74`, not acted on.
- Tests removed again after their run: O2 (NOT HELD), G3 (REJECTED), G4 (UNSETTLED). Their text is in `## OWN FINDINGS` and `<S>/house-a.md`.
- The report sits on `main` in `/Users/cobalt/cobalt`; my git strings run in `<WT>`. The report and its `.result` are left for the desk to commit (CHECK-HUB `## LAUNCH`: "commits the report after the check").
- files opened: 13 — CHECK-HUB.md, the card, the build report, BUILD-HUB.md, areas/cobalt.md, `src/cobalt/cos/probe.py`, `src/cobalt/cos/cli.py`, `tests/cobalt/test_cos_probe.py`, `configs/cobalt/redact.yaml`, `<S>/house-a.md`, and the three background task outputs (house probe, Grok, gate).
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh fb625806` → `context 181890 of 400000 — ok`.
- Check of `cos-probe-fr1`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: cos-probe-fr1 · pass: 1 · tip: da47500a · house A: Grok FINDINGS: 7 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 6 · house B: none available · suites: offline 8959/0 · with-DB 5858/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 181890
