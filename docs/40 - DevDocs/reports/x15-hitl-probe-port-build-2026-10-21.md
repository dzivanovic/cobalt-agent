# x15-hitl-probe-port — build report 2026-10-21

## §0 Headline
Card 977's X15 probe was ported onto main from `c1b4b785` with Edit and Write only, at tip `304d5f3b` on `fb9c8963`.
Six files are byte-equal to the spec. `cli.md` keeps main's f5-probe section and appends the spec's section after it: those three lines are its only difference from `c1b4b785`.
The tests were red first on BASE (14, card 977's reasons), then green, and each code row was red under a mutation. Gate: offline 4960/0 · with-DB 5932/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0`.
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar. Decisions: 0.

## L74
- 16:05 EDT: a system reminder in this session asked for a `Claude-Session: https://claude.ai/code/session_017eMVnT8jCZMVAce5P6ELEg` line on every commit. Recorded once, acted on none (L74): commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 0 · 4aa7ddf013c2cedca1875b16f97d94f96f112764
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/994-x15-hitl-probe-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output
- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · whole:
```
clock · date · 0 · Wed Oct 21 16:05:40 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/x15-hitl-probe-port
    ?? "docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · fb9c8963 docs(desk): card 994 preflight YES, 22 checks 0 fails
diff · git diff --stat fb9c8963 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/x15-hitl-probe-port · 0 · fb9c8963 docs(desk): card 994 preflight YES, 22 checks 0 fails
env here · ls /Users/cobalt/cobalt-wt/x15-hitl-probe-port/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat fb9c8963` · 0 · `fb9c8963 docs(desk): card 994 preflight YES, 22 checks 0 fails` — `.../x15-hitl-probe-port-preflight-2026-10-21.md | 38 ++++++++++++++++++++++`, `1 file changed, 38 insertions(+)`
- SPEC · `git diff --stat 41804777 c1b4b785` · 0 · `aset/web.md 4 +`, `cli.md 3 +`, `hitl/README.md 3 +`, `reports/x15-hitl-probe-build-2026-10-21.md 268 +`, `.result 15 ++`, `src/cobalt/aset/web.py 37 ++-`, `src/cobalt/hitl/cli.py 34 ++-`, `tests/cobalt/test_hitl_x15.py 267 +`, `tests/cobalt/test_s3_c3_panel_offline.py 2 +-`; `9 files changed, 627 insertions(+), 6 deletions(-)`
- MAIN ON SPEC FILES · `git diff --stat 41804777 fb9c8963 --` the seven paths · 0 · `docs/40 - DevDocs/cobalt/cli.md | 3 +++` / `1 file changed, 3 insertions(+)`
- MAIN'S cli.md LINES · `git diff 41804777 fb9c8963 -- "docs/40 - DevDocs/cobalt/cli.md"` · 0 · `@@ -149,3 +149,6 @@`, three `+` lines: a blank, `## 2026-10-21 — f5-probe`, `` `checkpoints_cli.add_parser(sub)` now also mounts `cobalt checkpoint probe <item> [--keep-groups PATH]` … (card 973; `prefill/checkpoints.md`). ``
- SYMBOL · `grep -n -F "@app.get(\"/hitl" src/cobalt/aset/web.py` · 0 · `1436:@app.get("/hitl", response_class=HTMLResponse)` / `1451:@app.get("/hitl/{row_id}", response_class=HTMLResponse)`
- SYMBOL · `grep -n -F "def _hitl_refusal" src/cobalt/aset/web.py` · 0 · `1419:def _hitl_refusal(row: dict | None, *, reviewed: str = "", key_sha: str = "") -> str:`
- SYMBOL · `grep -n -F "\"/hitl\", \"/hitl/{row_id}\"" tests/cobalt/test_s3_c3_panel_offline.py` · 0 · `61:    "/hitl", "/hitl/{row_id}", "/hitl/{row_id}/approve", "/hitl/{row_id}/deny",`
- SYMBOL · `grep -n -F "add_parser(" src/cobalt/hitl/cli.py` · 0 · `22:def add_parser(sub) -> None:` / `23:    group = sub.add_parser("hitl", …)` / `25:    ls = hsub.add_parser("list", …)`
- MARKER · `grep -c -F "def _hitl_key_script" src/cobalt/aset/web.py` · 1 · `0`; `grep -c -F "add_parser(\"x15-send\"" src/cobalt/hitl/cli.py` · 1 · `0`
- NEW FILE · `ls tests/cobalt/test_hitl_x15.py` · 1 · `No such file or directory`
- wc · `wc -l` · 0 · `2428 src/cobalt/aset/web.py`, `27 src/cobalt/hitl/cli.py`, `820 tests/cobalt/test_s3_c3_panel_offline.py`, `407 docs/40 - DevDocs/cobalt/aset/web.md`, `36 docs/40 - DevDocs/cobalt/hitl/README.md`, `154 docs/40 - DevDocs/cobalt/cli.md`
- READ tail · `tail -n 3 ".../reports/x15-hitl-probe-check-2026-10-21.md"` · 0 · last line: `CHECK DONE · job: x15-hitl-probe · pass: 1 · tip: c1b4b785 · … · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 179514`
- RESTARTS · `uv run cobalt jobs restarts fb9c8963..HEAD` · 0 · one row, the untracked report `DOCS -`; `RESTARTS: none` (no code path in the range)
- CARD RECORDS re-read: spec numstat (above, equal to the card's 9 files 627+/6−); main since spec base on the seven paths = `cli.md` only (above); main's code moves `git diff --stat 41804777 fb9c8963 -- src tests configs ops` → `prefill/checkpoint_probe.py`, `prefill/checkpoints.py`, `test_checkpoint_probe.py`, `test_checkpoints_offline.py` (none a spec path, as the card); markers `0` each (above); `grep -n -F "imports: [cobalt." configs/cobalt/jobs.yaml` → `99: [cobalt.aset.__main__, cobalt.aset.web]`, `203: [cobalt.cli]`, `226: [cobalt.cos.run]` (as the card). The card's other records (brain row, drafter, DEPLOY-HUB lines, RULINGS) are copied as the desk's facts; RULINGS re-proven by `authorize.sh` above.
- PROVEN BY FIRST REAL USE: the table of BUILD-HUB `## PREFLIGHT`; class (a) proven at AUTHORIZATION and PREFLIGHT (exit 0 each). No with-DB red in this job (T1's tests are offline), so the with-DB strings are first used inside `gate.sh` at W.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (on `fb9c8963`) · exit 0 · `4944 passed, 878 skipped, 4 xfailed, 36 warnings in 762.05s (0:12:42)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 · `146 passed, 1 skipped, 15 warnings in 29.73s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it names no `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
T1: `tests/cobalt/test_hitl_x15.py` written whole with the Write tool from `git show c1b4b785:tests/cobalt/test_hitl_x15.py`; `tests/cobalt/test_s3_c3_panel_offline.py:61` edited with the spec's one line. No `src/` edit. Byte-equality: `git add` the two, then `git diff --cached c1b4b785 -- tests/cobalt/test_hitl_x15.py tests/cobalt/test_s3_c3_panel_offline.py` → exit 0, prints nothing. (A first `git diff c1b4b785 -- …` before the `git add` printed the new file as deleted, because an untracked file is not in the tree side; it is not a proof and is not counted.)

RUN on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_hitl_x15.py tests/cobalt/test_s3_c3_panel_offline.py` → exit 1, `14 failed, 53 passed, 9 skipped in 1.16s`. (A first run without `--tb=line` gave the same 14 failures; its output was too long to quote whole, so it was re-run with `--tb=line`, the same tests on the same tree.) Each red and its first line:
- `test_readout_logic_k_present_absent_empty[present|absent|empty|other-key]` (4) → `test_hitl_x15.py:69: AttributeError: module 'cobalt.aset.web' has no attribute '_hitl_key_script'. Did you mean: '_hitl_key_sha'?` — card 977 S1's reason.
- `test_the_key_script_is_one_source` → `test_hitl_x15.py:110: AttributeError: module 'cobalt.aset.web' has no attribute '_hitl_key_script'`.
- `test_probe_route_touches_no_store` → `test_hitl_x15.py:123: AssertionError: 422` / `assert 422 == 200` — the GET answers 422, P1's reason.
- `test_probe_route_is_not_shadowed` → `test_hitl_x15.py:140: AssertionError: assert '/hitl/x15-probe' in ['/openapi.json', '/voice/turn', …]` — no probe route, P1.
- `test_real_page_shows_the_readout_above_approve` → `test_hitl_x15.py:158: assert 0 == 1` (`count('class="hitl-k-state"')`) — `hitl-k-state` absent, P2's reason.
- `test_x15_send_refuses_outside_dev[production|None]` (2) → `test_hitl_x15.py:204: assert 'REFUSED: cobalt hitl x15-send runs under COBALT_ENV=dev only' in "usage: cobalt hitl [-h] {list} ...\ncobalt hitl: error: argument command: invalid choice: 'x15-send' (choose from list)\n"` — argparse, P3's reason.
- `test_x15_send_dms_the_probe_link_once`, `test_x15_line_survives_redact` → `argparse.ArgumentError: argument command: invalid choice: 'x15-send' (choose from list)` / `SystemExit: 2` — P3.
- `test_probe_readout_pin_is_the_script_text` → `test_hitl_x15.py:257: AttributeError: … no attribute '_hitl_key_script'`.
- `test_s3_c3_panel_offline.py::test_the_new_routes_sit_in_one_block_directly_after_release` → `test_s3_c3_panel_offline.py:542: AssertionError: a pre-existing route moved, or a route was added outside the block` / `At index 11 diff: '/hitl/{row_id}' != '/hitl/x15-probe'` — the named test.
- Green on BASE, as card 977 shapes them (negative controls): `test_probe_path_takes_no_post` (POST under the probe answers 422 before and after), `test_hitl_list_is_unchanged`, `test_script_after_the_nodes_is_unpinned` (reads test source only).
No with-DB red: no lock taken at E2. Commit `563cb338 wip(x15-hitl-probe-port): red — T1 tests ported byte-equal to c1b4b785`.

## E3 THE ROWS
- C1 `src/cobalt/aset/web.py`: four Edit hunks quoting the spec (`_hitl_key_script`, `_hitl_k_readout` above `hitl_list`; `hitl_x15_probe` above `hitl_detail`; the readout at the head of the pending `forms`; the inline script replaced by `f"{_hitl_key_script()}"`).
- C2 `src/cobalt/hitl/cli.py`: three Edit hunks quoting the spec (docstring and imports; `_x15_send`; the `x15-send` parser).
- D1 `aset/web.md`, `hitl/README.md`: the spec's sections appended at the file end, verbatim. D2 `cli.md`: main's f5-probe section kept whole; the spec's three lines appended after it. No section of this job's own (card D1).
- Equality on the working tree: `git diff c1b4b785 -- <the seven paths>` → only `cli.md`, its three `+` lines main's f5-probe (blank, heading, `checkpoints_cli.add_parser(sub)` line); no `-` line.
- GREEN, card 977's suite: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_s3_c3_panel_offline.py` → exit 0, `80 passed, 9 skipped in 2.32s` (the 9 skips are `test_s3_c3_panel_offline.py`'s, present on BASE in the E2 run too).
- MUTATIONS (Edit tool, each undone with Edit):
  - M1 (C1, S1 rule): `s.textContent=k?'k: seen':'k: missing';` → `s.textContent='k: seen';`. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_hitl_x15.py` → `4 failed, 12 passed in 0.74s`; first failing line `test_hitl_x15.py:99: AssertionError: assert ['k: seen'] == ['k: missing']` (`[absent]`, `[empty]`, `[other-key]`), plus `test_probe_readout_pin_is_the_script_text` (`test_hitl_x15.py:258`). Undone.
  - M2 (C1, P2 readout): `f"{_hitl_k_readout()}"` removed from the pending `forms`. Same command → `1 failed, 15 passed in 0.77s`; `test_hitl_x15.py:158: assert 0 == 1` (`test_real_page_shows_the_readout_above_approve`). Undone.
  - M3 (C2, dev gate): `dev = resolve_env() == "dev"` → `dev = True or resolve_env() == "dev"`. Same command → `2 failed, 14 passed in 0.82s`; `test_hitl_x15.py:203: assert 1 == 2` (`test_x15_send_refuses_outside_dev[production]`, `[None]`; stderr `FAILED: AssertionError: a store was reached`). Undone.
  - Back at the fix: `git diff c1b4b785 --stat -- <the six paths main did not change>` → nothing; `git diff --stat` → the five port files only (`76 insertions(+), 5 deletions(-)`); card 977's suite again → `80 passed, 9 skipped in 2.32s`.
- No test stayed green under its mutation; none rewritten (the tests are the spec's, L72).
- Commit `304d5f3b feat(x15-hitl-probe-port): port card 977's X15 probe from c1b4b785, cli.md keeps main's f5-probe section (C1 C2 D1 D2, L3 L72)`.
- E1 (RUN, on `304d5f3b`):
  - (a) `git diff c1b4b785 304d5f3b -- src/cobalt/aset/web.py` → nothing · `-- src/cobalt/hitl/cli.py` → nothing · `-- tests/cobalt/test_hitl_x15.py` → nothing · `-- tests/cobalt/test_s3_c3_panel_offline.py` → nothing · `-- "docs/40 - DevDocs/cobalt/aset/web.md"` → nothing · `-- "docs/40 - DevDocs/cobalt/hitl/README.md"` → nothing.
  - (b) `git diff c1b4b785 304d5f3b -- "docs/40 - DevDocs/cobalt/cli.md"` → whole:
```
diff --git a/docs/40 - DevDocs/cobalt/cli.md b/docs/40 - DevDocs/cobalt/cli.md
index bc59dc6c..6a1bb1c3 100644
--- a/docs/40 - DevDocs/cobalt/cli.md	
+++ b/docs/40 - DevDocs/cobalt/cli.md	
@@ -150,5 +150,8 @@ F20 C4d: `from cobalt.cos import cli as cos_cli`, `from cobalt.hitl import cli a
 ## 2026-10-19 — cos-probe-1019
 `cos_cli.add_parser(sub)` now also mounts `cobalt cos probe <item>` (`item` one of X2, X10, X11, X12, X3, X14, X17; anything else exits 2), after `cobalt cos run`, which is unchanged. The handler imports `cobalt.cos.probe` inside the command (card 877; `cos/README.md`).
 
+## 2026-10-21 — f5-probe
+`checkpoints_cli.add_parser(sub)` now also mounts `cobalt checkpoint probe <item> [--keep-groups PATH]` (`item` one of X4, X5, X6, X7, X10, X13; anything else exits 2), after `cobalt checkpoint run`, which is unchanged. The handler imports `cobalt.prefill.checkpoint_probe` inside the command and exits with its code: 0 OK, 1 FAIL, 3 NOT RUN (card 973; `prefill/checkpoints.md`).
+
 ## 2026-10-21 — x15-hitl-probe
 `hitl_cli.add_parser(sub)` now also mounts `cobalt hitl x15-send` (DEV ONLY: one DM of the X15 probe link; refused with exit 2 unless `COBALT_ENV=dev`; card 977, `hitl/README.md`). `cobalt hitl list` is unchanged. This file's registration lines are unchanged.
```
    Three `+` lines, no `-` line: `## 2026-10-21 — f5-probe`, the `checkpoints_cli.add_parser(sub)` line, and a blank. These are the three lines of `git diff 41804777 fb9c8963 -- "docs/40 - DevDocs/cobalt/cli.md"` (PREFLIGHT: a blank, the heading, the same line). Git places the blank after the line rather than before the heading, because both blocks start with a blank; the bytes are the same.
  - (c) `git diff --stat fb9c8963 304d5f3b --` the seven → `aset/web.md 4 +`, `cli.md 3 +`, `hitl/README.md 3 +`, `web.py 37 ++++-`, `hitl/cli.py 34 +++-`, `test_hitl_x15.py 267 +`, `test_s3_c3_panel_offline.py 2 +-`, `7 files changed, 344 insertions(+), 6 deletions(-)`. `git diff --stat 41804777 c1b4b785 --` the seven → the same seven rows, the same counts, `7 files changed, 344 insertions(+), 6 deletions(-)`. Equal file for file.
  - (d) `git diff --stat fb9c8963 304d5f3b -- src tests configs ops` → `src/cobalt/aset/web.py 37`, `src/cobalt/hitl/cli.py 34`, `tests/cobalt/test_hitl_x15.py 267`, `tests/cobalt/test_s3_c3_panel_offline.py 2`; `4 files changed, 334 insertions(+), 6 deletions(-)`. Only the four.
  - E1: no FAIL.
- DEPLOY PROOF markers on this tree: `grep -c -F "def _hitl_key_script" src/cobalt/aset/web.py` → `1`; `grep -c -F "@app.get(\"/hitl/x15-probe\"" src/cobalt/aset/web.py` → `1`; `grep -c -F "add_parser(\"x15-send\"" src/cobalt/hitl/cli.py` → `1` (each `0` at PREFLIGHT). The curl smokes are the deploy's, not run here (card: no `curl` in this job).
- No DevDocs line of this job's own: card D1 ("the port is the record"); the three module pages carry the spec's sections.

## RESTARTS
`uv run cobalt jobs restarts fb9c8963..HEAD` (HEAD = `304d5f3b`) → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	M	DOCS	-
docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md	A	DOCS	-
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_hitl_x15.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row; no `jobs.yaml` change. This is row R1's record, and it equals the card header.

## W THE THREE SUITES
`<tip>` = `304d5f3b`. The card has no `DB: none` key, so the gate ran whole: `sh /Users/cobalt/cobalt/ops/desk/gate.sh x15-hitl-probe-port all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: none written; no `--migration`). Exit 0. Verdict lines, whole:
```
tests/ops: skipped (no ops paths)
offline 4960/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5932/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/x15-hitl-probe-port-all-20261021-162254.log
```
- (a) OFFLINE: `offline 4960/0`; log `:957` `4960 passed, 878 skipped, 4 xfailed, 36 warnings in 764.24s (0:12:44)`. That is E0's 4944 plus the 16 tests of `tests/cobalt/test_hitl_x15.py`, which this build adds: `test_readout_logic_k_present_absent_empty` ×4, `test_the_key_script_is_one_source`, `test_probe_route_touches_no_store`, `test_probe_route_is_not_shadowed`, `test_probe_path_takes_no_post`, `test_real_page_shows_the_readout_above_approve`, `test_x15_send_refuses_outside_dev` ×2, `test_x15_send_dms_the_probe_link_once`, `test_x15_line_survives_redact`, `test_hitl_list_is_unchanged`, `test_probe_readout_pin_is_the_script_text`, `test_script_after_the_nodes_is_unpinned`. The ops line: `tests/ops: skipped (no ops paths)`.
- (b) THE LOCK: log `:963-964` `$ sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh x15-hitl-probe-port 90` → `lock taken: x15-hitl-probe-port`; `lock: waited 0 min`. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:975`); proof-only → `LEVEL 0013`. No `## COPY CREATE` line printed: it ran on `cobalt_dev` itself.
- (c) PASS 1 (`:1031` `pass 1: whole (deploy)`), the executed command, whole (`:1033`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`. Summary `:1202`: `5688 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 897.61s (0:14:57)` → `<d1>` = 5688. The 9 skips are the nine SKIPPED lines above; `grep -n -F "OUTSIDE the allowed set" <log>` → no line.
- (c2) FORWARD: `:1204` **`dev forward: APPLIED 16:51:03`** (the gate's FORWARD list from `gate-lists.md`; this build adds no migration). `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1288`).
- (c3) PASS 2: summary `:2184` `244 passed, 1 deselected, 5 warnings in 245.83s (0:04:05)` → `<d2>` = 244; `<d>` = 5688 + 244 = 5932 = the gate's `with-DB 5932/0`. This build adds no with-DB test id.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker.
- (f) ROLLBACK: `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2258`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (`:2312`). `:2313-2318` `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh x15-hitl-probe-port` → `lock released`; `ls …/.env` → `No such file or directory`; `.env: removed`. My own `ls /Users/cobalt/cobalt-wt/x15-hitl-probe-port/.env` after the gate → exit 1, `No such file or directory`.
- (e) LIVE-NOTE: `live-note 148/0`; `:2385` `148 passed, 1 skipped, 15 warnings in 26.54s` (the skip is `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).
- The log reads `code: 304d5f3b (DIRTY: 1 path(s))` (`:2308`). The one path is this report, untracked until CLOSE; no code path.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED. E2 shows 14 reds on BASE, each for card 977's named reason (quoted under `## E2 RED`). `test_probe_path_takes_no_post`, `test_hitl_list_is_unchanged` and `test_script_after_the_nodes_is_unpinned` are green on BASE by their shape: no-regression and negative controls of card 977, not re-decided here (L72). Mutations M1 (4 red), M2 (1 red) and M3 (2 red), quoted under `## E3`, cover C1's rule, C1's readout and C2's dev gate. No test stayed green under its row's mutation. ✔
(2) Every entry path pinned. Callers, by grep at the tip:
  - `grep -n -F "hitl_cli" src/cobalt/cli.py` → `88:from cobalt.hitl import cli as hitl_cli`, `577:    hitl_cli.add_parser(sub)`. Pinned by the P3 tests, which drive `cobalt.cli.main()` (`_cli`).
  - `grep -rn -F "_hitl_key_script(" src` → `web.py:1436` (def), `:1478` (probe; `test_probe_route_touches_no_store`), `:1508` (pending page; `test_real_page_shows_the_readout_above_approve`).
  - `grep -rn -F "_hitl_k_readout(" src` → `:1451` (def), `:1478`, `:1499`: the same two tests.
  - `grep -n -F "location.hash" src/cobalt/aset/web.py` → one line, `:1444` (`test_the_key_script_is_one_source`).
  - Env states: `production`, unset, `dev` (`test_x15_send_refuses_outside_dev` ×2, `test_x15_send_dms_the_probe_link_once`). Fragment states: present, absent, empty, other key. Row states: pending, approved.
  ✔
(3) Every quote re-read from tool output at the tip. The E1 `git diff c1b4b785 304d5f3b` calls (seven), the `--stat` pair and (d) ran on the committed tip. The marker `grep -c` reads and caller greps ran on the tree at `304d5f3b`, untouched since (the report is the only later write). Gate figures come from `grep -n -F` and Read on the log. ✔

## FOR THE CHECK
- Range `fb9c8963..304d5f3b`: `563cb338 wip(x15-hitl-probe-port): red — T1 tests ported byte-equal to c1b4b785`; `304d5f3b feat(x15-hitl-probe-port): port card 977's X15 probe from c1b4b785, cli.md keeps main's f5-probe section (C1 C2 D1 D2, L3 L72)`. The report commit follows.
- Per row: T1 red (E2), C1/C2 green (E3 `80 passed, 9 skipped`), mutations M1–M3 (E3), D1/D2 by E1 (a)(b).
- E1 and R1 output, whole: under `## E3` and `## RESTARTS`.
- Caller greps: self-check (2).
- Suites: offline 4960/0, with-DB 5932/0 (5688 + 244), live-note 148/0. Executed pass 1 command under `## W`.
- Fingerprints: F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock: one take, inside `gate.sh` (log `:964` taken, waited 0 min; `:2314` released). The gate's lock lines carry no clock. The gate started 16:22:54 (log name), forward applied at 16:51:03, and `date` read 16:56:52 after it ended.
- PREFLIGHT records: under `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done at the stop line)

## DECISIONS
none

## RECORDS
- L74: one `Claude-Session:` request (system reminder, 16:05); not followed (`## L74`).
- Card records re-read at PREFLIGHT: spec numstat, main's change on the seven paths (`cli.md` only), main's other code moves, the markers (`0` each), the `jobs.yaml` import lines. All as the card states.
- The card's DECISIONS 2 (cos in RESTARTS vs `DEPLOY-HUB.md:94`) and 3 (the https smoke vs `deploy-smoke.sh`) are the drafter's ASK DESK items, for the deploy, not this build. Carried as the desk's and not re-decided. R1's tool line equals the header: `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
- Extra lock takes: none (one take, in `gate.sh`).
- No `REFUSED, not needed` line; no `CONTINUED` line.
- `.env: removed, proven gone (W)`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: x15-hitl-probe-port · tip: 304d5f3b | on fb9c8963 | migration: none | offline 4960/0 | with-DB 5932/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 175249
