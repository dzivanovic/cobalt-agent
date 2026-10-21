JOB: x15-hitl-probe-port
LADDER: OFF-LADDER — reports/cto-2026-10-21.md R2285
CLASS: K2 serving K4
INSTALL: none
BRANCH: ops/x15-hitl-probe-port
WORKTREE: x15-hitl-probe-port
BASE: fb9c8963
TIP: 304d5f3b
REPORT: /Users/cobalt/cobalt-wt/x15-hitl-probe-port/docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md
HOUSE B: as needed
BAND: HIGH
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
RULINGS: 2026-10-18 R1863

## ROWS

WHY: card 977 (job `x15-hitl-probe`, check `reports/x15-hitl-probe-check-2026-10-21.md` ready YES, code tip `c1b4b785`, branch `ops/x15-hitl-probe`, BASE `41804777`) cannot deploy: `deploy-card.sh` refused it with `CONFLICT docs/40 - DevDocs/cobalt/cli.md`, because the deployed f5-probe (`c2565a9f`) appended its own dated section to the same file end. THE FIX (brain, L79, precedent card 965): a fresh port from current main re-applies the checked diff; never a merge, a cherry-pick or `recut`. THE SPEC is `git diff 41804777 c1b4b785` over the seven files below (344+, 6−), nothing else; the rows S1, P1, P2, P3, D0 and their tests are card 977's and are not re-opened. HOW: Edit / Write ONLY (`BUILD-HUB.md:14` admits `git show*` and `git diff *`, no `git apply`, `cherry-pick`, `git mv`; `:16` never types `rm`, `git checkout`, `git merge`). For each file: `git show c1b4b785:<path>` read whole, then the worktree file is brought to those bytes (Write for a new file, Edit hunk by hunk for an existing one, quoting the spec's lines). No line is improved, reflowed or renamed. Six of the seven files are unchanged on main since `41804777` (`## RECORDS`): a pure re-application. ONE is not: `docs/40 - DevDocs/cobalt/cli.md` gained main's 3-line section `## 2026-10-21 — f5-probe` (`c2565a9f`) at the same place the spec adds its own; the port KEEPS BOTH (row D2). No migration, no plist, no database row, no live send.

| row | what | red first | files |
|---|---|---|---|
| T1 | THE TESTS. `tests/cobalt/test_hitl_x15.py` (NEW, spec 267+) is written byte-equal to `git show c1b4b785:tests/cobalt/test_hitl_x15.py`; `tests/cobalt/test_s3_c3_panel_offline.py` `BASE_ROUTES` (`:61`, found by content) gets the spec's one-line change (`"/hitl", "/hitl/{row_id}", …` → `"/hitl", "/hitl/x15-probe", "/hitl/{row_id}", …`). Ported FIRST, before C1 and C2 | RUN on BASE's `src/` with T1's tests: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_s3_c3_panel_offline.py`, quoted whole. RED, by name, on card 977's reasons: `test_readout_logic_k_present_absent_empty` (`AttributeError: … no attribute '_hitl_key_script'`), the probe tests (GET `/hitl/x15-probe` answers 422), the readout test (`hitl-k-state` absent), the `x15-send` tests (argparse `invalid choice: 'x15-send'`), `test_the_new_routes_sit_in_one_block_directly_after_release`; quote each assertion | `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py` |
| C1 | THE PAGE. `src/cobalt/aset/web.py` becomes byte-equal to `git show c1b4b785:src/cobalt/aset/web.py` (spec 33+, 4−: `_hitl_key_script`, `_hitl_k_readout` above `hitl_list` (`:1436`); `hitl_x15_probe` on `@app.get("/hitl/x15-probe")` above `hitl_detail` (`:1451`); the readout and the shared script in `hitl_detail`'s pending branch, the inline script gone) | T1's web reds turn GREEN | `src/cobalt/aset/web.py` |
| C2 | THE DEV SEND. `src/cobalt/hitl/cli.py` becomes byte-equal to `git show c1b4b785:src/cobalt/hitl/cli.py` (spec 33+, 1−: `hsub.add_parser("x15-send", …)`, `_x15_send`, the docstring `Read only, but the dev X15 send.`) | T1's `x15-send` reds turn GREEN | `src/cobalt/hitl/cli.py` |
| D1 | THE MODULE DOCS, UNCHANGED ON MAIN. `docs/40 - DevDocs/cobalt/aset/web.md` (spec 4+) and `docs/40 - DevDocs/cobalt/hitl/README.md` (spec 3+) each become byte-equal to `git show c1b4b785:<path>` (the sections `## 2026-10-21 — x15-hitl-probe`, kept as they are, `Card 977` and all). No section of this job's own is added (the port is the record) | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/aset/web.md`, `docs/40 - DevDocs/cobalt/hitl/README.md` |
| D2 | THE CONFLICT FILE, CHANGED ON MAIN. `docs/40 - DevDocs/cobalt/cli.md`: main's content is KEPT whole (its last section `## 2026-10-21 — f5-probe`, 3 lines: a blank, the heading, the `checkpoints_cli.add_parser(sub)` line); the spec's 3 lines (a blank, `## 2026-10-21 — x15-hitl-probe`, the `hitl_cli.add_parser(sub)` line, quoted from `git show c1b4b785:"docs/40 - DevDocs/cobalt/cli.md"`) are appended AFTER it, at the file end. Neither block is edited | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/cli.md` |
| E1 | RUN — asserts nothing. THE EQUALITY PROOF, on the committed port tip `<tip>`, each output quoted whole, ONE row per file (the seven spec files): (a) `git diff c1b4b785 <tip> -- <path>` for each of `src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`, `docs/40 - DevDocs/cobalt/aset/web.md`, `docs/40 - DevDocs/cobalt/hitl/README.md` prints NOTHING; (b) `git diff c1b4b785 <tip> -- "docs/40 - DevDocs/cobalt/cli.md"` prints ONLY main's three f5-probe lines as `+` (no `-` line), each named against `git diff 41804777 <BASE> -- "docs/40 - DevDocs/cobalt/cli.md"`; (c) `git diff --stat <BASE> <tip> --` the seven paths, beside `git diff --stat 41804777 c1b4b785 --` the same seven: equal file for file (`web.py 37`, `hitl/cli.py 34`, `test_hitl_x15.py 267`, `test_s3_c3_panel_offline.py 2`, `aset/web.md 4`, `hitl/README.md 3`, `cli.md 3`); (d) `git diff --stat <BASE> <tip> -- src tests configs ops` names only `src/cobalt/aset/web.py`, `src/cobalt/hitl/cli.py`, `tests/cobalt/test_hitl_x15.py`, `tests/cobalt/test_s3_c3_panel_offline.py`. Any line of (a), or any (b) line that is not one of main's three, is a FAIL of this row, fixed by re-quoting from the spec commit, never by a `## DECISIONS` waiver | — (tool output quoted in the report) | none |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the header's `RESTARTS` is the drafter's reading (`## RECORDS`), the tool's last line is the record | — (tool output quoted in the report) | none |

THE DOCS OUTSIDE THE SPEC (excluded from E1, listed): the old job's build report `reports/x15-hitl-probe-build-2026-10-21.md` and its `.result` (on `c1b4b785`'s branch only, never on main) are NOT ported; this job writes its own `REPORT` and `.result` instead.

ORDER: T1 (then its RED run), C1, C2 (then GREEN), D1, D2, card 977's suite `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_hitl_x15.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_s3_c3_panel_offline.py` (whole, quoted, `0 failed`), the commit, E1, R1, the `## DEPLOY PROOF` marker reads on the tree, the three suites (BUILD-HUB `## W`), the stop line. No live send, no DM, no `curl` in this job.

## NOT IN THIS JOB
- Any change to the spec's content: a line of a spec file that differs from `c1b4b785`, but main's three f5-probe lines of `cli.md`, is a defect of this port. A flaw found in the spec is a `## DECISIONS` item, UNPROVEN (L70), never fixed here (card 977 and its check stand).
- Editing, moving or reordering main's `## 2026-10-21 — f5-probe` section of `cli.md`, or any other line main holds.
- Any file outside the seven spec files, but this job's own build report and `.result`.
- `git apply`, `git cherry-pick`, `git merge`, `git revert`, `git checkout <ref> -- <path>`, `git mv`, `rm`, `mv` (`BUILD-HUB.md:14`, `:16`); `desk-launch.sh recut`; a merge of `ops/x15-hitl-probe`.
- Card 977's own fence stands: running `cobalt hitl x15-send` outside a test; any DM; `hitl_approve`, `hitl_deny`, `_hitl_key_sha`, `_hitl_refusal`, `hitl_list`; `src/cobalt/hitl/card.py`, `store.py`, `actions.py`, `executor.py`; `src/cobalt/notify/*`; `src/cobalt/redact/*`; `configs/cobalt/redact.yaml`, `tunables.yaml`, `notify.yaml`; a HITL row or test row in `cobalt_dev` or production.
- Loading, bootstrapping or kickstarting `com.cobalt.cos`; any `launchctl`; any migration; any production command.

## READ
- `prompts/2026-10-21/977-x15-hitl-probe-card.md` whole (rows S1, P1, P2, P3, D0; its `## CHECK ASKS` X1–X6; `## GATE`).
- `git diff 41804777 c1b4b785` (the spec); `git show c1b4b785:<path>` for each of the seven files (the bytes to write).
- `git diff 41804777 <BASE> -- "docs/40 - DevDocs/cobalt/cli.md"` (main's f5-probe lines, kept).
- `reports/x15-hitl-probe-check-2026-10-21.md` (its stop line: `ready: YES`, `held unfixed: 0`, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`; `## DECISIONS` 2).

## CHECK ASKS
- X1 THE DIFF EQUALITY, per file: re-run row E1 on the check's own read of the tip. Is `git diff c1b4b785 <tip> --` empty for each of the six files main did not change? For `cli.md`, does it print only main's three f5-probe lines (from `c2565a9f`), each `+`, no `-`? Is `git diff --stat <BASE> <tip>` over the seven paths equal, file for file, to `git diff --stat 41804777 c1b4b785` over them?
- X2 THE CONTENT: for each file but `cli.md`, does `git show <tip>:<path>` equal `git show c1b4b785:<path>` byte for byte? Does `cli.md` hold BOTH dated sections, f5-probe then x15-hitl-probe, each byte-equal to its source? Did the port touch any file but those seven, the build report and its `.result`?
- X3 RESTARTS re-derived: does `uv run cobalt jobs restarts <BASE>..<tip>` end `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`web.py` → aset and, by static import reach, cos; `hitl/cli.py` → radar via `cobalt.cli`)?
- X4 THE SMOKE READS: is each `## DEPLOY PROOF` smoke command exactly the admitted form of `DEPLOY-HUB.md:11` (`curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/…`), with no `http://127.0.0.1:5010/` read and no `uv run` line in the section?
- X5 SCOPE: the check is diff equality plus card 977's offline suite and the three suites. Card 977's rows, its tests and its check stand: write no finding that rests on re-deciding them.

## DEPLOY PROOF
- `grep -c -F "def _hitl_key_script" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F '@app.get("/hitl/x15-probe"' /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F 'add_parser("x15-send"' /Users/cobalt/cobalt/src/cobalt/hitl/cli.py` · before `0` · after `1`
- the probe page answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl/x15-probe` · exit 0, `200` (before the deploy it answers `422`, by reading `web.py:1451-1452`)
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` · exit 0, `200`

## GATE
- Card 977's `## GATE` stands, unchanged: after the deploy, a gate seat runs `COBALT_ENV=dev uv run cobalt hitl x15-send` once and quotes the `X15 SENT …` line; he taps the DM link; `k: seen` → `GATE RESULT: com.cobalt.cos · X15 · OK`, `k: missing` → X15 fails (`F20-FINAL-2026-10-11.md:81`).
- The port deploys after card 929, outside his trading hours (brain, `## RECORDS`).

## DECISIONS
1. MAIN CHANGED ONE SPEC FILE: `docs/40 - DevDocs/cobalt/cli.md` (`c2565a9f`, f5-probe, 3 lines). Row D2 keeps main's section and appends the spec's after it (date order, main's first); E1 (b) names those 3 lines as the only allowed difference from `c1b4b785`. The other six spec files are unchanged on main: pure re-application.
2. ASK DESK: `RESTARTS` holds `com.cobalt.cos` (brain's set, the check's tool line). `DEPLOY-HUB.md:94` skips cos when not loaded, and FAILS the deploy at STEP-R when cos is loaded (its strings are not on the deploy list, R60). If card 929 loads cos before this deploy, the desk adds cos's bootout and bootstrap strings via R60 first. Default: header as written; the hub's NOT LOADED read decides.
3. ASK DESK: the smoke reads are the admitted https form (`DEPLOY-HUB.md:11`); `ops/desk/deploy-smoke.sh` does NOT map them (it maps `http://127.0.0.1:5010/*` only, `:136`), as card 965 decision 2. Default: kept; the hub runs them at (s) on the launch line's own `curl` entry, the precedent of the 965 deploy.
4. CLASS, LADDER, BAND HIGH, RULINGS: copied from card 977. The builder's `cobalt jobs restarts` line (R1) overrides the header if it differs.
5. BASE `e88edfef` = main's HEAD at the drafter's read; the desk resets it at launch.

## RECORDS
- 977 refused on a cli.md trial-merge conflict → fresh PORT (HIGH, PROOF vs c1b4b785); cos cutover no longer waits on it; the port deploys after 929 with RESTARTS aset cos radar via R60 — brain 9b07db5a 2026-10-21
- Drafter `draft-x15-port` (prompt 993), 2026-10-21 16:00 EDT (`date`). Reads only; nothing run, no git write, nothing committed. `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `e88edfef` (BASE; the desk resets it at launch). `ls /Users/cobalt/cobalt-wt/` → no `x15-hitl-probe-port` (fresh); `x15-hitl-probe` present.
- THE SPEC: `git diff --numstat 41804777 c1b4b785` → `aset/web.md 4/0`, `cli.md 3/0`, `hitl/README.md 3/0`, build report `268/0`, its `.result` `15/0`, `web.py 33/4`, `hitl/cli.py 33/1`, `test_hitl_x15.py 267/0`, `test_s3_c3_panel_offline.py 1/1` (9 files, 627+, 6−; the seven spec files 344+, 6−).
- MAIN SINCE BASE, per spec file: `git diff --stat 41804777 HEAD --` the nine paths → `docs/40 - DevDocs/cobalt/cli.md | 3 +++` only; the other eight unchanged. `git log --oneline 41804777..HEAD -- "docs/40 - DevDocs/cobalt/cli.md"` → `c2565a9f feat(f5-probe): …`. `git diff 41804777 HEAD -- cli.md` → after the `## 2026-10-19 — cos-probe-1019` section (`:150-151`): a blank, `## 2026-10-21 — f5-probe`, the `checkpoints_cli.add_parser(sub)` line; the spec appends its x15 block at the same end (`@@ -149,3 +149,6 @@` both) — the conflict.
- Main's code moved elsewhere since BASE: `git diff --stat 41804777 HEAD -- src tests configs ops` → `src/cobalt/prefill/checkpoint_probe.py`, `src/cobalt/prefill/checkpoints.py`, `tests/cobalt/test_checkpoint_probe.py`, `tests/cobalt/test_checkpoints_offline.py` (none a spec path).
- MARKERS on HEAD (16:0x): `git grep -c -F` of `def _hitl_key_script`, `@app.get("/hitl/x15-probe"` over `src/cobalt/aset/web.py` and `add_parser("x15-send"` over `src/cobalt/hitl/cli.py` → no match each (`0`). `git grep -n -F '@app.get("/hitl'` → `web.py:1436` (`/hitl`), `:1451` (`/hitl/{row_id}`): the probe path today falls to `hitl_detail(row_id: int)` → 422.
- SMOKE: `DEPLOY-HUB.md:11` (HEAD) admits `"Bash(curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*)"`; `:152` (c) reads `https://cobalt.taild24291.ts.net/` already. `ops/desk/deploy-smoke.sh:12`, `:136` (HEAD): curl shape `http://127.0.0.1:5010/<path>` only (`curl reads http://127.0.0.1:5010/ only`).
- RESTARTS (K10), by reading `jobs.yaml` (HEAD): `:99` aset `imports: [cobalt.aset.__main__, cobalt.aset.web]`; `:203` radar `imports: [cobalt.cli]`; `:226` cos `imports: [cobalt.cos.run]`. The check's run of the tool on the spec (`x15-hitl-probe-check-2026-10-21.md:253`, `:264`) → `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`web.py` in cos's static import reach); the brain's set is the same. Not run by the drafter; row R1 is the record.
- `DEPLOY-HUB.md:93-94` (HEAD): a `RESTARTS` set holding `com.cobalt.cos` runs ONE `launchctl print gui/501/com.cobalt.cos`; not loaded → `com.cobalt.cos: not loaded — skipped`; loaded → `FAILED: RESTARTS — com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60), they are asked of Dejan`.
- `BUILD-HUB.md:14` (HEAD): `"Edit(//Users/cobalt/cobalt-wt/**)"` (governs Write too, `:16`), `git show*`, `git diff *`; no `git apply`, `cherry-pick`, `git mv`. `:16`: `Never typed: … rm of anything but the .env string, git checkout, … git merge`.
- `git diff --stat HEAD --` over `BUILD-HUB.md`, `DEPLOY-HUB.md`, `CARD.md`, `deploy-smoke.sh`, card 977, `jobs.yaml`, `src`, `tests` → nothing: the on-disk lines are main's.
- RULINGS: `cto-2026-10-18.md:90` R1863 `HIS RULING · APPROVED` (as card 977). The route: brain 2026-10-21 (L79), desk rows R2321, R2322 (`cto-2026-10-21.md:13-14`).
