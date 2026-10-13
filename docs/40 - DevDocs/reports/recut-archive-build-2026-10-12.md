# Build report — recut-archive-1012 (card 434) — 2026-10-12

## §0 Headline
- A1 built at `9c2020e8`. `desk-launch.sh recut` now archives a FAILED prior deploy's leftovers when a `pre-<job>` tag exists. The tag, branch and gate tree move under `archive/` and nothing is deleted; then the recut goes on. A DEPLOYED prior, or a ref that does not match its report, is still refused.
- Seven new tests (RA1-RA7, 15 items): each was red on BASE and red again under its mutation. Offline `4309/0`, live-note `146/0`, `tests/ops` `3462 passed`. DB: none. RESTARTS: none.
- One ASK DESK: RA3 (a)'s `main~1` points at P itself, so the test uses `main` instead.

## L74
- A system reminder at session start asked commits to carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md"` (19:33 EDT), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 0 · 5dc6e7b7be8445def20a4506d86d24aa316f9418
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 151:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Mon Oct 12 19:34:07 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/recut-archive-1012
    ?? "docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 0990393f docs(desk): R1279 brain direction on 256 recut, drafter prompt 433
diff · git diff --stat 0990393f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/recut-archive-1012 · 0 · 0990393f docs(desk): R1279 brain direction on 256 recut, drafter prompt 433
env here · ls /Users/cobalt/cobalt-wt/recut-archive-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 0990393f` | 0 | `docs(desk): R1279 brain direction on 256 recut, drafter prompt 433` — 2 files (`433-draft-recut-archive.md` +11, `cto-2026-10-12.md` +1) |
| symbol | `grep -n -F "recut)" ops/desk/desk-launch.sh` | 0 | `955:    deploy\|recut) fixed="$PROMPTS/DEPLOY-HUB.md" ;;` · `1847:recut)` |
| symbol | `grep -n -F "gate-clean.sh" ops/desk/desk-launch.sh` | 0 | `66:` (header) · `1917:` (comment) · `1918:` printf RUN · `1919:    sh "$here/gate-clean.sh" "$card" \|\| exit 1` |
| symbol | `grep -n -F "exists: the deploy got that far" ops/desk/gate-clean.sh` | 0 | `87:    refuse "tag $tag exists: the deploy got that far"` · `90:    refuse "tag pre-$job exists: the deploy got that far"` |
| callers | `grep -rn -F "job-clean.sh" ops/desk` | 0 | only `job-clean.sh` itself (`:2`, `:3`, `:134`, `:178`) and a comment in `scratch-clean.sh:45`; no script calls salvage today |
| READ | Read `desk-launch.sh` `:1-260`, `:340-351`, `:1000-1019`, `:1840-2023` | — | `refuse` `:208-211`, `here` `:250`, `:346-348` the recut argument guard, fields `:1007-1013`, the recut arm `:1847-1935` (`bt=` `:1874`, `br=` `:1875`, nested `;;` `:1853`, `:1861`, own `    ;;` `:1935`), deploy worktree add `:1993-2020` — as the card cites |
| READ | Read `gate-clean.sh` whole, `job-clean.sh` whole | — | as the card cites (`gate-clean.sh:60-71`, `:74-83`, `:86-91`, `:92-96`, `:99-102`, `:105-109`; `job-clean.sh:51-173`) |
| READ | `grep -n -F "<pre-merge>"` / `"<stack-final>"` on `deploy-aset-orphan-1010.md` | 0 | `<pre-merge>` lines `:130`, `:132`, `:146`; `<stack-final>` line `:132` only |
| READ | `tail -n 3 deploy-aset-orphan-1010.md` | 0 | last line `FAILED PREFLIGHT: main moved outside docs since the cut — 55 paths (…); the desk re-cuts the gate · rollback: not used · aset: UP · radar: not in the set · decisions: 4 · for Dejan: 0 · tokens: 100737` |
| READ | Read `DEPLOY-HUB.md:125-134` | — | D2.0 `<pre-merge>`, D2.1 merge, D2.2 `<stack-final>` and `^2`, D2.6 `tag pre-<JOB>` at `<pre-merge>` |
| READ | Read `test_gate_clean.py:160-179` | — | `:173 test_the_pre_tag_existing_is_refused` |
| READ | `grep -n -F "R1279" cto-2026-10-12.md` | 0 | `7:\| R1279 \| 19:18 ET \| DESK RECORD brain L79, 256 recut: a K5 card, one row: recut ARCHIVES a FAILED prior deploy's tag, branch and gate tree under archive/ (renamed, never deleted), then proceeds; a DEPLOYED prior still refused. …` |
| wc | `wc -l desk-launch.sh test_desk_launch_recut.py` | 0 | `2023` · `338` |
| RESTARTS | `uv run cobalt jobs restarts 0990393f..HEAD` | 0 | only the untracked report (`DOCS -`); `RESTARTS: none` |

Card records copied (desk's facts): reads 19:10-19:30 EDT at `0990393f`; the 256 state (tag `pre-aset-orphan-1010` → `8199fa13`, branch → `a617c402`, not landed, gate clean, no `.env`, no lock); the 256 report holds A1 (a)-(f); INSTALL none (symlinks); RESTARTS none; the new git verbs inside the script appear on no seat line; AMEND line numbers at `75c39896`; line counts. Re-read here: line numbers `:1847`, `:1853`, `:1861`, `:1874`, `:1875`, `:1917`, `:1935` (Read), `wc -l` 2023 / 338 (as the card), the 256 report's `:132`, `:146`, `:248` (grep, tail). The 256 refs on the live repo were not re-read (no listed string reads them; L35: the card's record stands as the desk's).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `0990393f` → `4309 passed, 806 skipped, 1 xfailed, 36 warnings in 650.61s (0:10:50)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.03s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` names no `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Seven tests (RA1-RA7, 15 items with the parametrized cases) appended to `tests/ops/test_desk_launch_recut.py`, with the helper `stale_256(desk)` in the 256 shape. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_recut.py` on BASE → `15 failed, 13 passed, 15 warnings in 14.52s`. Each red's first line, by its row's named reason:
- RA1: `assert 1 == 0` — stderr `REFUSED: tag pre-x-deploy exists: the deploy got that far`.
- RA2 (i): `assert 'REFUSED: tag pre-x-deploy exists: the deploy got that far — not archived: ' in '…REFUSED: tag x-tag exists: the deploy got that far\n'` (gate-clean's own refusal). RA2 (ii): the same assertion against `REFUSED: tag pre-x-deploy exists: the deploy got that far`.
- RA3 (a)-(g), all seven: the same `— not archived:` assertion against gate-clean's `REFUSED: tag pre-x-deploy exists: the deploy got that far`.
- RA4: `assert 'INSPECT: locked: yes' in ['RUN: sh …/gate-clean.sh "…"']` (gate-clean's refusal).
- RA5: `assert 1 == 0`, refused at the pre tag.
- RA6: `AssertionError: no \`tag "$at"\` in the recut arm`.
- RA7 (i), (ii): the `— not archived:` assertion against gate-clean's refusal.
- The 13 existing tests passed (among them `test_a_failed_deploy_is_recut_and_its_launch_printed_in_order` and `test_main_holding_the_gate_branch_is_refused_by_gate_clean`).
Commit `4c4ba2b9 wip(recut-archive-1012): red` (test file only).

## E3 THE ROWS
**A1** — `ops/desk/desk-launch.sh`, the recut arm and the header only. Step 1 is now `if ! git rev-parse --verify --quiet refs/tags/pre-$job` → gate-clean.sh exactly as before; else THE ARCHIVE: `nogo()` refuses with the prefix `tag pre-$job exists: the deploy got that far — not archived: `; tests (a)-(g) in order, as the card states (a: deploy tags `$tag`, `$bt`, `$bt-attempt*`, and `^DEPLOYED` in `$report`, `$br.md` and `$br-attempt*.md`; b: P against the last `<pre-merge>` line; c: S against the last `<stack-final>` line, and `S^2` = P; d: gate-clean's tree tests; e: `merge-base --is-ancestor S main` must exit 1; f: `.env` and lock owner; g: `stamp=$(date +%Y%m%d-%H%M)`, `check-ref-format`, `show-ref` absent). Then `RUN: sh <here>/job-clean.sh salvage <wt>` and the salvage call; `branch -m` and its read-back of S → `ARCHIVE: branch …`; `tag "$at" <P full>` and its read-back of P, and only then `tag -d pre-$job` → `ARCHIVE: tag …`; `ARCHIVE: <job> done; recut proceeds`; then step 2 unchanged. Header `:22-24` and `:65-80` state the rule.
- Green: `uv run pytest … tests/ops/test_desk_launch_recut.py` → `28 passed, 15 warnings in 15.79s`; with `tests/ops/test_gate_clean.py` → `96 passed, 15 warnings in 27.29s`; all of `tests/ops` → `3462 passed, 1 xfailed, 16 warnings in 673.18s`.
- MUTATIONS (Edit, run, undo with Edit):
  - M1, the fix off (`if true || ! git … pre-$job`) → `-k "ra1 or ra2 or ra3 or ra4 or ra5 or ra7 or a_failed_deploy or main_holding"`: `14 failed, 4 passed, 10 deselected`; first failing line `AssertionError: RUN: sh …/gate-clean.sh "…" … REFUSED: tag pre-x-deploy exists: the deploy got that far` (RA1); every RA2/RA3/RA7 case on the `— not archived:` assertion, RA4 on `INSPECT: locked: yes`, RA5 `assert 1 == 0`.
  - M2, a `tag -d "pre-$job"` added before `tag "$at"` → `-k "ra6 or ra1"`: `2 failed, 1 passed`; RA6 `AssertionError: ([126], [125, 130])` (two `tag -d`, one before the copy); RA1 `error: tag 'pre-x-deploy' not found.` … `REFUSED: recut: the archive stopped at (3) the old name: …`.
  - M3, the (a) report test blinded (`'^DEPLOYEDX'`) → `-k ra2`: `1 failed, 2 passed`; RA2 (ii) `assert (… 'not archived: ' + 'DEPLOYED') in "… not archived: tag pre-x-deploy at c00d1c86 is not the report's <pre-merge>: no <pre-merge> line\n"`.
  - M4, the (g) absent tests blinded (`"$at-x"`, `"$ab-x"`) → `-k ra7`: `2 failed`; (i) `fatal: tag 'archive/pre-x-deploy-20261012-1930' already exists` · `REFUSED: recut: the archive stopped at (3) tag: …`; (ii) `fatal: a branch named 'archive/deploy/x-deploy-20261012-1930' already exists` · `REFUSED: recut: the archive stopped at (2) branch -m: …`.
  - M5, test (e) removed (`0) ;;`) → `-k ra3`: `1 failed, 6 passed`; RA3 (d) `Deleted branch deploy/x-deploy (was a94e579).` · `fatal: no branch named 'deploy/x-deploy'` — without (e), salvage deletes a merged gate branch (CHECK ASK X2).
  - After each undo `git diff --stat` → ` ops/desk/desk-launch.sh | 102 +++++++++++++++++++++++++++++++++++++++++++++---` (the fix alone); the two files → `96 passed`.
- No DevDocs line: `docs/40 - DevDocs/cobalt/` holds pages per `src/cobalt` module; Grep `desk-launch` there finds only `jobs/restarts.md` (a mention), no page of this script (RECORDS).
Commit `9c2020e8 feat(recut-archive-1012): recut archives a FAILED prior deploy's pre tag, gate branch and tree, then proceeds (A1, L1 L72)`.

**R2** (RUN, asserts nothing): see `## RESTARTS`.

## RESTARTS
`uv run cobalt jobs restarts 0990393f..HEAD` at `9c2020e8`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_recut.py	M	test/documentation; no resident	-
RESTARTS: none
```
As the card expected. No UNCLASSIFIED row.

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 0990393f` → `ops/desk/desk-launch.sh` · `tests/ops/test_desk_launch_recut.py`: every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh recut-archive-1012 offline` → `offline 4309/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/recut-archive-1012-offline-20261012-200342.log`. This build adds no test there; its tests are under `tests/ops`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh recut-archive-1012 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/recut-archive-1012-livenote-20261012-201421.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` at `9c2020e8` → `3462 passed, 1 xfailed, 16 warnings in 669.06s (0:11:09)`. Added: `test_ra1_the_256_state_is_archived_then_recut`, `test_ra2_a_deployed_prior_is_refused_before_and_after` [2], `test_ra3_a_ref_off_its_report_is_refused_before_and_after` [7], `test_ra4_a_salvage_refusal_archives_nothing`, `test_ra5_a_dirty_gate_is_kept_on_a_wip_branch`, `test_ra6_the_recut_arm_deletes_no_ref_it_did_not_copy`, `test_ra7_an_archive_name_already_present_is_refused` [2].
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/recut-archive-1012/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test shown RED for its named reason: E2 lists each red on BASE (RA1-RA7, 15 items), and E3's M1-M5 turn them red again against the fix (RA6 under M2, RA2 (ii)'s `DEPLOYED` under M3, RA7 under M4, RA3 (d) under M5). No test stayed green under its mutation.
(2) Every entry path pinned: the arm's one caller is `desk-launch.sh recut` (grep `recut)` → `:955`, `:1847`). Pre tag absent → `test_a_failed_deploy_is_recut_and_its_launch_printed_in_order` and `test_main_holding_the_gate_branch_is_refused_by_gate_clean` (green). Pre tag present: archived (RA1, RA5 dirty), DEPLOYED by tag (RA2 i) or by an earlier attempt's report (RA2 ii), each test (b)-(f) (RA3 a-g), salvage refusing (RA4), (g) names taken (RA7), the source order (RA6). `job-clean.sh` had no caller before (grep `job-clean.sh` in `ops/desk`); its one call is at `:1997`.
(3) Re-read at the tip: `git log --oneline 0990393f..HEAD`, `grep -n -F "tag -d"` → `:78` (header), `:2007`; `grep -n -F "job-clean.sh"` → `:76`, `:1994`, `:1996`, `:1997`; `ls …/.env` → none; `restarts` table at the tip.

## FOR THE CHECK
- `0990393f..9c2020e8`: `4c4ba2b9 wip(recut-archive-1012): red` · `9c2020e8 feat(recut-archive-1012): recut archives a FAILED prior deploy's pre tag, gate branch and tree, then proceeds (A1, L1 L72)`.
- A1: reds in `## E2 RED`; mutations M1-M5 and greens in `## E3 THE ROWS`.
- Caller greps: `## PREFLIGHT` and self-check (2).
- R2 output whole: `## RESTARTS`.
- Suites: offline `4309/0` (gate.sh offline), live-note `146/0` (gate.sh livenote), `tests/ops` `3462 passed, 1 xfailed`; with-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- Records copied at PREFLIGHT: `## PREFLIGHT`, last paragraph.
- For X1-X4: every test (a)-(g) runs before `job-clean.sh` (`desk-launch.sh` the `else` branch, then `:1996`). A refusal from (a)-(g) or salvage changes nothing (`nothing_archived` compares `for-each-ref`, `worktree list --porcelain`, the card and today's desk report). `tag -d` appears once in code, after `tag "$at"` and its read-back of P. (e) keeps a merged gate branch from being deleted by salvage (M5). No line moved outside the arm and the header; no allow string touched.

## CONTINUE
next: none (built; the desk verifies and launches the check)

## DECISIONS
1. ASK DESK: RA3 (a) as the card writes it (`git tag -f pre-x-deploy main~1`) does not move the tag. In `stale_256`, `main~1` is P: the D2.0 report commit, which is followed by the one FAILED-report commit. The tag would stay at P, the archive would proceed, and the case would test nothing. Safe default taken: `git tag -f pre-x-deploy main` (one commit past P), with an assert in the test that the tag no longer reads P. The refusal is (b): `is not the report's <pre-merge>`. Not his; the desk confirms or amends the card [20:26 EDT].

## RECORDS
- L74: a system reminder at session start asked commits to carry a `Claude-Session:` line. Recorded under `## L74`; not followed.
- No DevDocs dated line: no page for `ops/desk/desk-launch.sh` exists under `docs/40 - DevDocs/cobalt/`, and the card's `files` list none.
- RA2 (ii) shape: the hand recut to attempt 2 also moves REPORT to `deploy-2026-01-02-1-attempt2.md`, which ends on the 256 line. The `DEPLOYED x-tag <P> | set: x-job · constructed` line is appended to `deploy-2026-01-02-1.md` (`$br.md`).
- RA7's `date` stub prints `20261012-1930` only for `+%Y%m%d-%H%M` and passes every other call to `/bin/date`, so desk-row's clock and salvage's date still work.
- No extra lock take, no REFUSED, not needed line, no CONTINUED line.
- The card's records, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: recut-archive-1012 · tip: 9c2020e8 | on 0990393f | migration: none | offline 4309/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 179661
