JOB: cos-probe-fr2b
LADDER: S5-P2 · F20
CLASS: K2
INSTALL: none
BRANCH: ops/cos-probe-fr2b
WORKTREE: cos-probe-fr2b
BASE: be5fc23d
TIP:
REPORT: /Users/cobalt/cobalt-wt/cos-probe-fr2b/docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2b-check-2026-10-20.md
HOUSE B: as needed
BAND: HIGH
RESTARTS: com.cobalt.radar
RULINGS: 2026-10-18 R1863

## ROWS

WHY: card 918 (job `cos-probe-fr2`, check `reports/cos-probe-fr2-check-2026-10-20.md` ready YES, tip `dfea631a`) deployed and was rolled back at smoke (d): marker 4's `after` was `1`, but the README carries two matching headings, build and check (`reports/deploy-cos-probe-fr2.md` `## DECISIONS` 1). The code is correct and stays as checked. Main holds the merge and its revert, so `dfea631a` is an ancestor of main and `deploy-card.sh` refuses it. THE FIX (brain, L79, option C): a fresh port from current main re-applies the same diff. THE SPEC is `git diff 27c35e37..dfea631a` for the three files below, nothing else; the fix itself is card 918's and is not re-opened. HOW: Edit and Write ONLY (`BUILD-HUB.md:14` lists no `git apply`, `cherry-pick` or `git mv`; `:16` never types `rm`, `git checkout`, `git restore`, `git merge`). For each file: `git show dfea631a:<path>` read whole, then the worktree file is written to those bytes (Write of the whole file, or Edit hunk by hunk, quoting the spec's lines). No line is improved, reflowed or renamed. Every spec file is unchanged on main since `27c35e37` (`## RECORDS`), so each port is a pure re-application. Constructed values only (L32). Migrations: none.

| row | what | red first | files |
|---|---|---|---|
| P1 | THE TESTS. `tests/cobalt/test_cos_probe.py` becomes byte-equal to `git show dfea631a:tests/cobalt/test_cos_probe.py` (spec: 147+, 14−; card 918 rows H1–H4 and the check's O1, O2 tests). Ported FIRST, before P2 | RUN on BASE's `probe.py` with P1's tests: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py`, quoted whole. RED, by name, at least: `test_auth_runs_under_the_real_home_and_a_login_there_passes` (the line ends `under the scratch HOME`), `test_a_missing_home_is_refused` (the auth stub is reached), `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home` (env `HOME` is the scratch home), `test_auth_quotes_logged_in_and_method_only`. The H4 control `test_the_probe_opens_no_file_under_the_real_home` may be green here (card 918 H4) | `tests/cobalt/test_cos_probe.py` |
| P2 | THE CODE. `src/cobalt/cos/probe.py` becomes byte-equal to `git show dfea631a:src/cobalt/cos/probe.py` (spec: 81+, 30−; card 918 H1–H4 plus check O1, O2, O3) | P1's reds turn GREEN; the same command, quoted whole, `0 failed` | `src/cobalt/cos/probe.py` |
| D0 | THE MODULE DOC. `docs/40 - DevDocs/cobalt/cos/README.md` becomes byte-equal to `git show dfea631a:"docs/40 - DevDocs/cobalt/cos/README.md"` (spec: 6+): the two sections `## 2026-10-20 — cos-probe-fr2` and `## 2026-10-20 — cos-probe-fr2 (check)` appended, unchanged, both headings kept as they are. No section of this job's own is added (the port is the record; ASK DESK 2 of the drafter) | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/cos/README.md` |
| E1 | RUN — asserts nothing. THE EQUALITY PROOF, on the committed port tip `<tip>`, each output quoted whole: (a) `git diff --stat 27c35e37 <tip> -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"` and `git diff --stat 27c35e37 dfea631a --` the same three paths: the two tables are equal line for line (README `6`, `probe.py` `111`, `test_cos_probe.py` `161`; 234 insertions, 44 deletions); (b) `git diff dfea631a <tip> -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"` prints NOTHING; (c) `git diff --stat dfea631a <tip> -- src tests configs ops` prints nothing (no code outside the spec moved). Any line of (b) is a FAIL of this row, fixed by re-quoting from `dfea631a`, never by a `## DECISIONS` waiver | — (tool output quoted in the report) | none |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the header's `RESTARTS` is the drafter's reading (`## RECORDS`), the tool's last line is the record | — (tool output quoted in the report) | none |

THE DOCS LINES OUTSIDE THE SPEC (excluded from E1, listed): the spec's two files `docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md` and `.result` are the old job's build report; they are NOT ported (they sit in main's history at `dfea631a`; the revert took them off main's tree). This job writes its own `REPORT` and its `.result` instead. ASK DESK 1 of the drafter.

ORDER: P1 (then its RED run), P2 (then GREEN), D0, the card's offline suite `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` (whole, quoted, 0 failed), the commit, E1, R1, the `## DEPLOY PROOF` reads on the tree, the three suites, the stop line. No live run in this job.

## NOT IN THIS JOB
- Any change to the spec's content: a line of `probe.py`, `test_cos_probe.py` or the README that differs from `dfea631a` is a defect of this port. A flaw found in the spec is a `## DECISIONS` item, UNPROVEN (L70), never fixed here (card 918, its check and the gate stand).
- Any file outside the three spec files, but this job's own build report and `.result`.
- `git apply`, `git cherry-pick`, `git merge`, `git revert`, `git checkout <ref> -- <path>`, `git mv`, `rm`, `mv` (`BUILD-HUB.md:14`, `:16`); the re-land string `git revert ebb5020c` (the desk's, not taken: brain option C).
- Running `cobalt cos probe <item>` or `python -m cobalt.cos.probe` outside a test; any `claude` command; every live gate run (the DONE test after the deploy is a gate seat's).
- Any edit to `src/cobalt/cos/session.py`, `run.py`, `listener.py`, `tools.py`, `cli.py`, `src/cobalt/redact/*`, `configs/cobalt/agents/cos.yaml`, `configs/cobalt/taxonomy/tunables.yaml`.
- His `~/.claude.json`, `~/.claude/`, his login's files or keychain items read, written, copied or listed by the probe or a test; any DM; any production resident; `launchctl`; `com.cobalt.cos` loaded.

## READ
- `prompts/2026-10-20/918-cos-probe-realhome-card.md` whole (the spec's rows H1–H4, D0, its `## CHECK ASKS` X1–X6).
- `git diff 27c35e37..dfea631a -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"` (the spec); `git show dfea631a:<path>` for each of the three (the bytes to write).
- `reports/cos-probe-fr2-check-2026-10-20.md` (findings O1, O2, O3, fixed at `dfea631a`; the stop line).
- `reports/deploy-cos-probe-fr2.md` `## Smoke` (d) and `## DECISIONS` 1 (why this port exists).

## CHECK ASKS
- X1 THE DIFF EQUALITY: re-run row E1 on the check's own read of the tip: is `git diff dfea631a <tip> --` the three spec paths empty, and is `git diff --stat 27c35e37 <tip>` over them equal, file for file, to `git diff --stat 27c35e37 dfea631a` over them? Is `git diff --stat dfea631a <tip> -- src tests configs ops` empty?
- X2 THE CONTENT: for each of the three files, does `git show <tip>:<path>` equal `git show dfea631a:<path>` byte for byte? Did the port touch any file but those three, the build report and its `.result`?
- X3 THE REAL-HOME WRITE BOUND (card 918 X1, carried): does any path of `probe.py` write outside its `cos-probe-` scratch dir? Is the CLI's own state under the real HOME stated in the docstring and the README, and bounded as card 918 row H4 says (one scratch cwd per run, at most 67 sessions at the gate, the probe cleaning none of it)?
- X4 NO CREDENTIAL READ (card 918 X2, carried): does `probe.py` open, read or name any credential file (`~/.claude.json`, `~/.claude/`, a keychain item, `security`), and is `grep -c -F ".claude.json" src/cobalt/cos/probe.py` `0`? Is the H4 control's mutation red?
- X5 SCOPE: the check is diff equality plus the card's offline suite and the three suites. The fix's design (R2177 option A) and card 918's check findings are settled: write no finding that rests on re-deciding them.

## DEPLOY PROOF
- `grep -c -F "under the scratch HOME" /Users/cobalt/cobalt/src/cobalt/cos/probe.py` · before `1` · after `0`
- `grep -c -F ".claude.json" /Users/cobalt/cobalt/src/cobalt/cos/probe.py` · before `2` · after `0`
- `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" /Users/cobalt/cobalt/tests/cobalt/test_cos_probe.py` · before `0` · after `1`
- `grep -c -F "## 2026-10-20 — cos-probe-fr2" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/cos/README.md"` · before `0` · after `2`
- cos probe module doc · `grep -n -F "## 2026-10-20 — cos-probe-fr2" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/cos/README.md"` · green: two lines, `## 2026-10-20 — cos-probe-fr2` and `## 2026-10-20 — cos-probe-fr2 (check)`

## RECORDS
- Drafter `draft-cos-probe-fr2b` (prompt 922), 2026-10-20 14:58-15:00 EDT (`date`). `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `9c21facd` at 14:58, `be5fc23d` at 14:59 (`be5fc23d docs(desk): handoff 759331db, drafter 8ef18696 live`); BASE = `be5fc23d` (the desk resets it at launch). `ls /Users/cobalt/cobalt-wt/` → no `cos-probe-fr2b` (fresh).
- THE SPEC: `git diff --numstat 27c35e37..dfea631a` → `6 0 docs/40 - DevDocs/cobalt/cos/README.md` · `193 0 …/reports/cos-probe-fr2-build-2026-10-20.md` · `15 0 …/reports/cos-probe-fr2-build-2026-10-20.result` · `81 30 src/cobalt/cos/probe.py` · `147 14 tests/cobalt/test_cos_probe.py` (5 files, 442+, 44−). `git log --oneline 27c35e37..dfea631a` → `7b1427af` (red), `74169800` (fix H1-H4, D0), `220eaa70` (build report), `3e406f66` (check red O1, O2), `dfea631a` (fix O1, O2, O3).
- PURE RE-APPLICATION: `git diff --stat 27c35e37 be5fc23d -- src/cobalt/cos/probe.py tests/cobalt/test_cos_probe.py "docs/40 - DevDocs/cobalt/cos/README.md"` → nothing; `git diff --stat 27c35e37 be5fc23d -- src tests configs ops` → nothing. So main's three files equal the spec's base, and `git diff dfea631a <tip>` over them is empty when the port is exact.
- `git merge-base --is-ancestor dfea631a HEAD` → exit 0 (why `deploy-card.sh` refuses the old tip). `ls …/reports/cos-probe-fr2-build-2026-10-20.md` → No such file (off main since the revert `ebb5020c`); `…/cos-probe-fr2-check-2026-10-20.md` → listed.
- MARKERS on main's tree (14:58-14:59): `under the scratch HOME` in `probe.py` → `1`; `.claude.json` in `probe.py` → `2`; the H1 test name in `test_cos_probe.py` → `0`; `## 2026-10-20 — cos-probe-fr2` in the README → `0` (the revert restored each `before`). `git grep -c -F "## 2026-10-20 — cos-probe-fr2" dfea631a -- "docs/40 - DevDocs/cobalt/cos/README.md"` → `2` (marker 4's `after`); the spec's README hunk adds `## 2026-10-20 — cos-probe-fr2` and `## 2026-10-20 — cos-probe-fr2 (check)`. Markers 1-3's `after` values read green at the failed deploy's smoke (d) on the same code (`deploy-cos-probe-fr2.md` `## Smoke` (d)).
- No `uv run pytest` line in `## DEPLOY PROOF`: unmapped by `deploy-smoke.sh` (prompt 922).
- `BUILD-HUB.md:14` (HEAD): the build line's allow list (`Edit(//Users/cobalt/cobalt-wt/**)`, `git show*`, `git diff *`; no `git apply`, `cherry-pick`, `git mv`); `:16`: never typed `rm` (but the `.env`), `git checkout`, `git restore`, `git merge`, `claude`, `launchctl`.
- RESTARTS, carried from card 918 `## RECORDS` and confirmed by the failed deploy's run of the tool on the same diff (`deploy-cos-probe-fr2.md` `## RESTARTS`): `src/cobalt/cos/probe.py M static import reach com.cobalt.radar`, `tests/cobalt/test_cos_probe.py M test/documentation; no resident`, README `DOCS` → `RESTARTS: com.cobalt.radar`. Row R1 is the record.
- RULINGS: `cto-2026-10-18.md:90` R1863 `HIS RULING · APPROVED` (as card 918). The route: brain 2026-10-20 15:10 (L79), option C, a fresh port (prompt 922; desk rows R2185-R2186).
