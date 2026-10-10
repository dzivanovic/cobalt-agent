# launcher-1010 — check report (2026-10-10)

## §0 Headline
- Row A `--fix-report` holds as built. Two gaps held and are fixed in `9e624360`: an empty value was accepted (O1), and a path holding `|` or a backtick broke the SHIPS cell (O2).
- Rows B and C: my greps confirm DECISION B1 and C1 (no script reads either list). No edit.
- House A Grok `FINDINGS: 0`. House B none (his R921; OpenAI reserved for the model tribunal, R920).
- Gate on `9e624360`: offline 4196/0, with-DB 5093/0, live-note 146/0, `cobalt_dev` 0013 F2 = F0, `.env` removed. `ready: YES`.

## L74
- 2026-10-10 15:00 ET: a system reminder asked that commits end with a `Claude-Session:` line. Recorded as data and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 0 · 7dd569c057318b247c0bc4db5c8cc30b275f86eb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/244-launcher-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R685 row · ... · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): ... | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · ... · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (STANDING `Bash(grok *)`); `grep -n "^| R19 "` → row 37 (four house strings standing); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

Desk message (cto-desk, 15:0x ET): "OpenAI is reserved for the model tribunal — NO Codex probe, NO Sol/codex call in this check. House A = Grok alone; Gemini (agy) sits as house B only if this build is a mandatory-house-B build ... or Grok fails". I checked both rulings it cites:
- `grep -n "^| R920 " cto-2026-10-10.md` → `11:| R920 | 14:18 ET | HIS RULING · APPROVED (via brain, L79): only the model tribunal uses OpenAI; no Codex probe elsewhere; ... |`
- `grep -n "^| R921 " cto-2026-10-10.md` → `10:| R921 | 14:21 ET | HIS RULING · APPROVED (via brain, L79; L67 OVERRIDE): checks Opus+Grok, Gemini only for mandatory-B or a Grok failure; ... |`
Both are his rulings (L77), and both narrow access. I follow them: no `house-probe.sh` (it probes Sol), and no `codex` call.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sat Oct 10 15:01:02 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-1010
head · git log --oneline -1; git log --stat --format=%h b71837f2..HEAD · 0 · (5 lines)
    183a334f docs(launcher-1010): build report — b71837f2
    183a334f
     .../reports/launcher-build-2026-10-10.md           | 178 +++++++++++++++++++++
     1 file changed, 178 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/launcher-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../launcher-build-2026-10-10.md" · 0 · BUILT · job: launcher-1010 · tip: b71837f2 | on eed03ce8 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 205024
range · git log --oneline eed03ce8..b71837f2 · 0 · (3 lines)
    b71837f2 fix(launcher-1010): pin the --fix-report shape refusals (A, self-check 2)
    e046c2ac feat(launcher-1010): deploy-card.sh --fix-report fills the fix-round SHIPS row (A, L75 L1)
    d2d79b19 wip(launcher-1010): red
PREFLIGHT OK
```
THE RANGE: `git log --stat --format=%h eed03ce8..b71837f2` → b71837f2 `tests/ops/test_deploy_card.py` (+19) · e046c2ac `ops/desk/deploy-card.sh` (66 lines changed), `tests/ops/test_deploy_card.py` (8 lines changed) · d2d79b19 `tests/ops/test_deploy_card.py` (+133). Path union: `ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py`.
`ls <S>` → `No such file or directory` (fresh).
HOUSE PROBE (R920: no Sol probe, so `house-probe.sh` was not run): `grok -m grok-4.7 -p "Reply with only the word OK."` → first output `OK` = UP. (The CLI then kept going without being asked; see RECORDS.)
- OpenAI: reserved for the model tribunal (his 10-10)
- Grok: UP
- Gemini: not probed (R921: it sits only on a mandatory-B card or a Grok failure)
house A: Grok · house B: none (card `HOUSE B: as needed`; R921). MANDATORY rule: not mandatory.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` →
```
18903 <S>/diff.md
8437 <S>/files/244-launcher-card.md
24316 <S>/files/launcher-build-2026-10-10.md
14946 <S>/files/wt/ops/desk/deploy-card.sh
26073 <S>/files/wt/tests/ops/test_deploy_card.py
384 <S>/rulings.md
STAGED 6 files · 93059 bytes · commits 3
```
(commits 3 = PREFLIGHT's range count). `stage-copy.sh`, one call each:
- `COPIED 29945 <S>/files/cto-2026-10-09.md`
- `COPIED 33414 <S>/files/cto-2026-10-10.md`
- `COPIED 14786 <S>/files/CARD.md`
- `COPIED 65831 <S>/files/wt/ops/desk/desk-launch.sh`
- `COPIED 23278 <S>/files/wt/ops/desk/deploy-step0.sh`
- `COPIED 31332 <S>/files/wt/tests/ops/test_deploy_step0.py`
- `COPIED 57118 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md`
Not copied: `areas/cobalt.md` (a vault note, L32). `<S>/HOUSE-INSTRUCTIONS.md` written (10301 bytes): the HOUSE TEXT verbatim, ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS and Files.
Grok started 15:05 ET from `<AGY>` (`cd` in, the GROK line, `cd` back; `git status --short --branch` → `## ops/launcher-1010`).

## OWN FINDINGS
Written 15:1x ET, before I opened anything a house wrote.

FINDING O1
ROW: A (X2)
CLAIM: An empty `--fix-report ""` is accepted silently. `ops/desk/deploy-card.sh:62` appends it as an empty line, and `:100` (`[ -n "$fx" ] || continue`) skips it before the `<job>=<path>` shape refusal at `:103`. A value that is not `<job>=<fix report path>` then writes a card instead of being refused.
RUN: TEST — `tests/ops/test_deploy_card.py`
```python
def test_check_o1_an_empty_fix_report_value_is_refused(tmp_path):
    desk = Desk(tmp_path)
    _fix_refused(desk, ("--fix-report", ""), "--fix-report '' must be <job>=<fix report path>")
```
EXPECT: `assert done.returncode == 1` fails (`0 == 1`, `deploy-card: … written`).

FINDING O2
ROW: A
CLAIM: The fix report path is written unescaped into the `fix report` cell (`ops/desk/deploy-card.sh:189`, `:197`). The shape check at `:110-114` accepts any `$REPORTS/*.md`, including one whose name holds `|`. The row is then split into extra cells, and `desk-launch.sh:820` reads cell 8 as a path that is not the report, so the script writes a card the launcher refuses.
RUN: TEST — `tests/ops/test_deploy_card.py`
```python
def test_check_o2_a_fix_report_path_with_a_pipe_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    git(desk.repo, "checkout", "-q", "ops/alpha")
    piped = desk.reports / "alpha|fix.md"
    piped.write_text(f"# alpha fix round\n\nBUILT · job: x · tip: {fixed} | rows: 1 of 1\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha piped fix report")
    git(desk.repo, "checkout", "-q", "main")
    _fix_refused(desk, ("--fix-report", f"alpha={piped}"), "alpha: --fix-report path holds")
```
EXPECT: `assert done.returncode == 1` fails (`0 == 1`): the card is written with the row split at `|`.

FINDING O3
ROW: X4 (B)
CLAIM: For `grep -n "held" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, the build report (`launcher-build-2026-10-10.md:85`) gives line numbers only (8, 32, 41, 50, 58, 101, 109, 175), not the output. This run checks that those are the whole set.
RUN: COMMAND — `grep -n "held" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: exactly eight lines, numbered 8, 32, 41, 50, 58, 101, 109, 175. Any other set means the report misquotes.

FINDING O4
ROW: C (X4)
CLAIM: No script under `ops/desk/` reads the D0 ACCEPTED list (`rules.yaml` / `settings.json`), so DECISION C1 stands.
RUN: COMMAND — `grep -rn "settings.json" ops/desk/`
EXPECT: only `ops/desk/stop-guard.py:42` (a comment).

## Findings
House A Grok finished 15:17 ET (`date` at the notice). `ls -la <S>` → `house-a.md` (12 bytes), written by Grok. Its whole content: `FINDINGS: 0`. Grok's stdout: "… The row A script, its tests, and the B and C decisions match the card. No finding holds./Users/cobalt/…/house-a.md". Kept: none (it wrote no FINDING block).
House B: none (R921; card `HOUSE B: as needed`; Grok did not fail).

## Dropped
none (no house block to drop).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py::test_check_o1_an_empty_fix_report_value_is_refused` | `FAILED` · `assert 0 == 1` · stdout `deploy-card: …/03-deploy-x-set-card.md written (2 job(s), TIP 506c7a8d fb70de39)` | HELD |
| O2 | own | `… ::test_check_o2_a_fix_report_path_with_a_pipe_is_refused` | `FAILED` · `assert 0 == 1` · stdout `deploy-card: …/03-deploy-x-set-card.md written (2 job(s), TIP 1e1c02c0 fb70de39)` (the `alpha|fix.md` path written into the row) | HELD |
| O3 | own | `grep -n "held" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | eight lines: `8`, `32`, `41`, `50`, `58`, `101`, `109`, `175` (the same set the build report names; `:32` and `:58` are the held-item rule) | NOT HELD: confirms the build report, no defect |
| O4 | own | `grep -rn "settings.json" ops/desk/` | `ops/desk/stop-guard.py:42:# in user settings ~/.claude/settings.json (not main's tracked .claude/settings.json), pasted` | NOT HELD: confirms DECISION C1, no defect |
Both runs together: `2 failed, 15 warnings in 2.07s`. The tests were pasted as written; I repaired nothing. The held tests are committed at `3398d55f wip(launcher-1010): check red — O1 O2`.

## FIXES
| id | fix | file | after | commit |
|---|---|---|---|---|
| O1 | the option parse refuses an empty `--fix-report` value: `--fix-report '' must be <job>=<fix report path>` | `ops/desk/deploy-card.sh` | — | `9e624360` |
| O2 | the per-entry shape check refuses a path holding `\|` or a backtick (the SHIPS cell's own characters); the header comment now names both refusals | `ops/desk/deploy-card.sh` | — | `9e624360` |
After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py` → `222 passed, 15 warnings in 90.18s`. After the comment edit: `tests/ops/test_deploy_card.py` → `50 passed, 15 warnings in 14.59s`. DevDocs line: `ls "docs/40 - DevDocs/cobalt"` lists no page for `ops/desk/` scripts (the builder found the same), so no dated line was written.

## Suites
RESTARTS: `uv run cobalt jobs restarts eed03ce8..HEAD` → `docs/…/launcher-build-2026-10-10.md A DOCS -` · `ops/desk/deploy-card.sh M operator script; no Cobalt reader -` · `tests/ops/test_deploy_card.py M test/documentation; no resident -` · `RESTARTS: none`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-1010 all --deploy` on `9e624360` (exit 0), verdict lines WHOLE:
```
offline 4196/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-1010-all-20261010-152013.log
```
`ls /Users/cobalt/cobalt-wt/launcher-1010/.env` → `No such file or directory` (15:49 ET). `tests/ops`, not in the gate's lists: the three row-adjacent files → `222 passed` (FIXES).

## Scope
PREFLIGHT's path union: `ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py`. My commits touch `tests/ops/test_deploy_card.py` (`3398d55f`) and `ops/desk/deploy-card.sh` (`9e624360`), both row A's `files`. Nothing outside the rows' files.

## Checked against the branch
(i) `git log --oneline b71837f2..HEAD -- . ":(exclude)docs"` → `9e624360 fix(launcher-1010): --fix-report refuses an empty value and a path holding '|' or a backtick (check O1 O2)` · `3398d55f wip(launcher-1010): check red — O1 O2`. tip now = `9e624360`.
(ii) `git log --stat --format=%h b71837f2..HEAD` → `9e624360 ops/desk/deploy-card.sh` · `3398d55f tests/ops/test_deploy_card.py` · `183a334f …/reports/launcher-build-2026-10-10.md` (docs). Nothing WIDENED.
(iii) `git log --oneline eed03ce8..HEAD -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" ops/desk/orphan-clean.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh .claude/settings.json .claude/settings.json.bak src configs` → empty.
(iv) `grep -n -F "def test_check_o" tests/ops/test_deploy_card.py` → `564:def test_check_o1_an_empty_fix_report_value_is_refused` · `569:def test_check_o2_a_fix_report_path_with_a_pipe_is_refused` (plus `354:` `test_check_o2_a_migration_only_main_has_leaves_migrations_none`, an older check's test with another name). `3398d55f` sits below `9e624360` in (i).
(v) `ls <WT>/.env` → No such file. `git status --short --branch` → `## ops/launcher-1010`.
(vi) `git log --stat --format=%h eed03ce8..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty, so no gate-lists change is owed.
(vii) The card's RECORDS name no `ls`, `grep` or `git -C … log` command. Its RESTARTS record re-derived above: `RESTARTS: none`.
(viii) L32: this report holds constructed values and commit ids only.

## OPEN
none.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none. (Rows B and C: DECISION B1 and DECISION C1 are the builder's. My O3 and O4 runs confirm both: the lists are `DEPLOY-HUB.md` text, a fixed file, and the desk installs them.)

## RECORDS
- Grok probe 15:01 ET: `grok -m grok-4.7 -p "Reply with only the word OK."` printed `OK`, then on its own printed the build report's last line and `FAILED: reply — the word OK — this prompt names no CARD, ...`. It ran past the 180 s limit and was moved to the background. `git status --short --branch` afterwards → `## ops/launcher-1010` (nothing written).
- Desk message (cto-desk, during AUTHORIZATION): OpenAI reserved; house A Grok alone. I checked it against R920 and R921 (AUTHORIZATION) and followed it. It narrows access and grants nothing.
- Dropped findings: none. Houses that produced nothing: none. Seats not taken: Sol (R920), Gemini (R921). REFUSED: none. CONTINUED: none. Extra lock takes: none (the gate took and released the lock, waited 0 min).
- files opened: 9 — CHECK-HUB.md; the card; `diff.md` (the diff `eed03ce8..b71837f2`); `ops/desk/deploy-card.sh`; `ops/desk/desk-launch.sh` (:800-889); the build report; `tests/ops/test_deploy_card.py` (:1-140, :540-564); `<S>/house-a.md`; this report. Not opened: `BUILD-HUB.md` sections and `areas/cobalt.md` (the gate script ran W whole).
- Check of `launcher-1010`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: launcher-1010 · pass: 1 · tip: 9e624360 · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 149022
