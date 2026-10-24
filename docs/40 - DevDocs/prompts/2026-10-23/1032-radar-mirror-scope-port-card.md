JOB: radar-mirror-scope-port
LADDER: OFF-LADDER — reports/survey-settings-writer-2026-10-23.md R2389
BRANCH: ops/radar-mirror-scope-port
WORKTREE: radar-mirror-scope-port
BASE: 148b03ef
TIP:
REPORT: /Users/cobalt/cobalt-wt/radar-mirror-scope-port/docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port-check-2026-10-24.md
HOUSE B: as needed
BAND: HIGH
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
MIGRATIONS: none
RULINGS: 2026-10-18 R1863

## ROWS

WHY: card 1020 (job `radar-mirror-scope`, check `reports/radar-mirror-scope-check-2026-10-23.md` ready YES, held unfixed 0, code tip `25994142`, branch `ops/radar-mirror-scope`, BASE `11ed17b8`) was merged to main (`4f35be8f`) and reverted (`41bb2402`) after deploy 1027 failed smoke (h) on the radar panel's `CardSettingsError` (`radar.cards_enabled`), a fault that predates the set (`reports/deploy-deploy-radar-mirror-scope.md` `## DECISIONS` 2). `25994142` is now an ancestor of main, so a recut or a revert of the revert is wrong. THE FIX (brain, L79, DESK RECORD R2410; precedent card 994): a fresh port from current main re-applies the checked diff. THE SPEC is `git diff 11ed17b8 25994142` over the seven files below (312+, 16−), nothing else; card 1020's rows M1, M2, M3, M4, F1, D0, the check's A1 fix and their tests are not re-opened. HOW: Edit / Write ONLY (`BUILD-HUB.md:14` admits `git show*` and `git diff *`, no `git apply`, `cherry-pick`, `git mv`, `revert`; `:16` never types `rm`, `git checkout`, `git merge`). For each file: `git show 25994142:<path>` read whole, then the worktree file is brought to those bytes (Write for the new file, Edit hunk by hunk for an existing one, quoting the spec's lines). No line is improved, reflowed or renamed. MAIN SINCE BASE: all seven files (and the two report files) are unchanged on main since `11ed17b8` (`git diff --stat 11ed17b8 HEAD --` the nine paths prints nothing: the revert `41bb2402` returned them to BASE content; `## RECORDS`). The builder re-proves it first, per file, with `git diff 11ed17b8..main -- <path>`; a line main changed since BASE is KEPT and named in `## DECISIONS`, and row E1 then admits exactly those lines. On the drafter's read: a pure re-application. No migration, no plist, no database row, no production command.

| row | what | red first | files |
|---|---|---|---|
| P0 | RUN — asserts nothing. MAIN SINCE BASE, per spec file: `git diff 11ed17b8..main -- <path>` for each of the seven files, each output quoted whole (expected: nothing). Any output → its lines named in `## DECISIONS` and kept by the row that ports that file | — (tool output quoted in the report) | none (read only) |
| T1 | THE TESTS. `tests/cobalt/test_radar_mirror_scope.py` (NEW, spec 201+) is written byte-equal to `git show 25994142:tests/cobalt/test_radar_mirror_scope.py`; the four fakes are brought to the spec: `tests/cobalt/test_radar_notes.py` (7+: `MirrorStore.rows()`, the `rows()` of the `Store` in `test_mirror_replaces_old_block_with_parse_failed_status`), `tests/cobalt/test_radar_runner.py` (13+, 4−: `Settings.rows()`, `CrossingSettingsStore` `self.rows` → `self.stored`, `rows()`, `put(…, source, …)`), `tests/cobalt/test_radar_evaluate.py` (2+, 2−: `_Settings.rows()`, `return before_commit() or {}`), `tests/cobalt/test_radar_replay.py` (17+, 4−: `ReplaySettingsStore` as `CrossingSettingsStore`, and `test_f1_replay_settings_store_rows_is_callable`). Each hunk found by content. Ported FIRST, before C1 | RUN on BASE's `src/` with T1's tests: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py`, quoted whole. RED, by name, on card 1020's reasons: `::test_m1_unknown_source_is_left_alone_loudly` (`sent["radar.hand_typed"]["status"] == "removed"`), `::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` (`radar.cards_enabled` in `sent`, `status: removed`), `::test_m4_the_source_names_the_note_that_changed` (the label carries the Screens hash); `::test_m3_a_block_the_note_drops_is_still_tombstoned` GREEN. Quote each assertion | `tests/cobalt/test_radar_mirror_scope.py`, `tests/cobalt/test_radar_notes.py`, `tests/cobalt/test_radar_runner.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_replay.py` |
| C1 | THE SCOPE. `src/cobalt/radar/notes.py` becomes byte-equal to `git show 25994142:src/cobalt/radar/notes.py` (spec 40+, 6−: `from loguru import logger`; `MIRROR_SOURCE_PREFIX` and `FOREIGN_SOURCE_PREFIXES` after `FENCE_RE`; `_mirror_rows(parsed, before, owners)` and its owned-only tombstone loop with the unknown-source warning; `_changed_note_hash`; `mirror_sources` reading `target.rows()` once; the label `f"{MIRROR_SOURCE_PREFIX}{note_hash[:12]}"`) | T1's reds turn GREEN, M3 stays GREEN | `src/cobalt/radar/notes.py` |
| D1 | THE MODULE DOCS. `docs/40 - DevDocs/cobalt/radar/notes.md` becomes byte-equal to `git show 25994142:"docs/40 - DevDocs/cobalt/radar/notes.md"` (spec 32+: the section `## 2026-10-23 — radar-mirror-scope`, its 2026-10-23 check (A1) line included, kept as it is). No section of this job's own is added (the port is the record) | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/radar/notes.md` |
| E1 | RUN — asserts nothing. THE EQUALITY PROOF, on the committed port tip `<tip>`, each output quoted whole, ONE row per file: (a) `git diff 25994142 <tip> -- <path>` for each of `src/cobalt/radar/notes.py`, `tests/cobalt/test_radar_mirror_scope.py`, `tests/cobalt/test_radar_notes.py`, `tests/cobalt/test_radar_runner.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_replay.py`, `docs/40 - DevDocs/cobalt/radar/notes.md` prints NOTHING, or ONLY the lines P0 found main changed since BASE, each named against `git diff 11ed17b8 <BASE> -- <path>`; (b) `git diff --stat <BASE> <tip> --` the seven paths, beside `git diff --stat 11ed17b8 25994142 --` the same seven: equal file for file (`notes.py 46`, `test_radar_mirror_scope.py 201`, `test_radar_notes.py 7`, `test_radar_runner.py 17`, `test_radar_evaluate.py 4`, `test_radar_replay.py 21`, `radar/notes.md 32`); (c) `git diff --stat <BASE> <tip> -- src tests configs ops` names only `src/cobalt/radar/notes.py` and the five test files. Any line of (a) that is not one of P0's is a FAIL of this row, fixed by re-quoting from the spec commit, never by a `## DECISIONS` waiver | — (tool output quoted in the report) | none |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the header's `RESTARTS` is the drafter's reading (`## RECORDS`), the tool's last line is the record | — (tool output quoted in the report) | none |

THE DOCS OUTSIDE THE SPEC (excluded from E1, listed): the old job's build report `reports/radar-mirror-scope-build-2026-10-23.md` and its `.result` (in `25994142`, absent from main after the revert) are NOT ported; this job writes its own `REPORT` and `.result` instead.

ORDER: P0, T1 (then its RED run), C1 (then GREEN), D1, card 1020's offline suite with the check's A1 file `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py` (whole, quoted, `0 failed`), the commit, E1, R1, the `## DEPLOY PROOF` marker reads on the tree, the three suites (BUILD-HUB `## W`), the stop line.

## NOT IN THIS JOB
- Any change to the spec's content: a line of a spec file that differs from `25994142`, but a line P0 found main changed since BASE, is a defect of this port. A flaw found in the spec is a `## DECISIONS` item, UNPROVEN (L70), never fixed here (card 1020 and its check stand).
- Any file outside the seven spec files, but this job's own build report and `.result`.
- `git apply`, `git cherry-pick`, `git merge`, `git revert`, `git checkout <ref> -- <path>`, `git mv`, `rm`, `mv` (`BUILD-HUB.md:14`, `:16`); `desk-launch.sh recut`; a merge of `ops/radar-mirror-scope`; a revert of `41bb2402`.
- Card 1020's own fence stands: any `src/` file but `src/cobalt/radar/notes.py`; `src/cobalt/settings/*` and `src/cobalt/radar/runner.py` read only; the fixtures under `tests/fixtures/radar/`; the label format beyond M4.
- Restoring `radar.cards_enabled` or `radar.benchmark` (the K3 seat's, R2410), any `cobalt settings load`, any production command, any database.
- Editing `Radar Lists.md`, `Radar Screens.md` or any vault note (HOLD: no radar-note edit until this port is DEPLOYED).
- Any `launchctl`, bootstrap, bootout or kickstart; any migration.

## READ
- `prompts/2026-10-23/1020-radar-mirror-scope-card.md` whole (rows M1–M4, F1, D0; `## CHECK ASKS` X1–X6; `## DEPLOY PROOF`).
- `git diff 11ed17b8 25994142` (the spec); `git show 25994142:<path>` for each of the seven files (the bytes to write).
- `git diff 11ed17b8..main -- <path>` per spec file (row P0).
- `reports/radar-mirror-scope-check-2026-10-23.md` (its stop line: `ready: YES`, `held unfixed: 0`, `tip: 25994142`, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`; `## DECISIONS` none; `## RECORDS`, the A1 fix file `tests/cobalt/test_radar_replay.py`).

## CHECK ASKS
- X1 THE DIFF EQUALITY, per file: re-run row E1 on the check's own read of the tip. Is `git diff 25994142 <tip> --` empty for each of the seven files, or does it print only lines P0 named as main's since BASE? Is `git diff --stat <BASE> <tip>` over the seven paths equal, file for file, to `git diff --stat 11ed17b8 25994142` over them? Did the port touch any file but those seven, the build report and its `.result`?
- X2 THE SUITE: is card 1020's offline suite (ORDER, with `tests/cobalt/test_radar_replay.py`) `0 failed` on the tip, and were M1, M2, M4 red and M3 green on BASE's `src/` (T1)?
- X3 RESTARTS re-derived: does `uv run cobalt jobs restarts <BASE>..<tip>` end `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`src/cobalt/radar/notes.py` by static import reach, as the check's `## Suites` and deploy 1027's `## RESTARTS` read it)?
- X4 THE SMOKE READS: is each `## DEPLOY PROOF` smoke line in a shape `ops/desk/deploy-smoke.sh` maps (`ls <path>`, `:10`, `:118`) and the `DEPLOY-HUB.md:11` launch line admits (`Bash(ls *)`), with no `http://127.0.0.1:5010/` read and no `uv run` line in the section?
- X5 SCOPE: the check is diff equality plus card 1020's offline suite and the three suites. Card 1020's rows, its tests and its check stand: write no finding that rests on re-deciding them.

## DEPLOY PROOF
- `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · before `0` · after `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · before `0` · after `1`
- the radar notes module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · exit 0, listed
- the scope test is on the tree · `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · exit 0, listed

## GATE
- The deploy runs only after the K3 restore of `radar.cards_enabled` and `radar.benchmark` (R2410) and a clean radar cycle: smoke (h) (`DEPLOY-HUB.md:158`) counts the radar panel's `radar panel FAILED` lines, and each `/radar` curl of (c) (`:152`) adds one while `radar.cards_enabled` fails validation; that is how deploy 1027 failed (h) (`reports/deploy-deploy-radar-mirror-scope.md` `## DECISIONS` 2).

## DECISIONS
1. MAIN CHANGED NO SPEC FILE since `11ed17b8` (the revert `41bb2402` returned them to BASE): pure re-application. Row P0 re-proves it on the builder's BASE; any line it finds is kept and named, and E1 (a) admits exactly those.
2. ASK DESK: card 1020 carries no `CLASS` line, so none is copied (CARD.md's build header has no `CLASS` key; card 994 carried `CLASS: K2 serving K4` of its own). Default: no `CLASS` line. [19:55]
3. ASK DESK: `RESTARTS` is re-derived to `com.cobalt.aset com.cobalt.cos com.cobalt.radar` (the check's tool line and deploy 1027's), not card 1020's `com.cobalt.radar`. Deploy 1027 found cos loaded and kept it in the set (`DEPLOY-HUB.md:11` carries cos's bootout and bootstrap strings). Default: header as written; row R1's tool line is the record. [19:55]
4. ASK DESK: marker 2's `before` is `0` on the card, but on main the file is absent, so `grep -c -F` prints `No such file or directory` (exit 2), not `0`; deploy 1027's hub took absent as a valid before (its P6, `## DECISIONS` 1). Default: card 1020's line kept as written. [19:55]
5. ASK DESK: card 1020's suite gains `tests/cobalt/test_radar_replay.py`, the check's A1 fix file and a spec file. Default: included in ORDER. [19:55]
6. The smoke reads are `ls` lines, mapped by `deploy-smoke.sh:10`, `:118` and admitted by `DEPLOY-HUB.md:11` `Bash(ls *)`; no curl, so L80's https form is not touched. Copied unchanged from card 1020.
7. LADDER, BAND HIGH, MIGRATIONS none, RULINGS: copied from card 1020. BASE `148b03ef` = main's HEAD at the drafter's read; the desk resets it at launch.

## RECORDS
- 1020 FAILED (h) on the pre-existing radar CardSettingsError, rolled back clean; K3 restore runs before the re-ship on his "Restore yes"; 1020 re-ships as a fresh PORT — brain 9b07db5a 2026-10-24
- HOLD: no radar-note edit until the port is DEPLOYED (R2410, `cto-2026-10-24.md:8`).
- Drafter `draft-mirror-port` (prompt 1031), 2026-10-24 19:54 EDT (`date`). Reads only; nothing run, no git write, nothing committed. `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `148b03ef` (BASE; the desk resets it at launch). `ls /Users/cobalt/cobalt-wt/` → no `radar-mirror-scope-port` (fresh); `radar-mirror-scope`, `deploy-radar-mirror-scope` present.
- THE SPEC: `git diff --numstat 11ed17b8 25994142` → `radar/notes.md 32/0`, build report `234/0`, its `.result` `15/0`, `notes.py 40/6`, `test_radar_evaluate.py 2/2`, `test_radar_mirror_scope.py 201/0`, `test_radar_notes.py 7/0`, `test_radar_replay.py 17/4`, `test_radar_runner.py 13/4` (9 files; the seven spec files 312+, 16−). `git log --oneline 11ed17b8..25994142` → `de798203`, `3067e8b9`, `5bb80b36`, `c1a8cf46`, `96bb9aea`, `25994142` (the check's A1 fix).
- MAIN SINCE BASE, per spec file: `git diff --stat 11ed17b8 HEAD --` the nine paths → nothing. Main's code since BASE: `git diff --stat 11ed17b8 HEAD -- src tests configs ops` → `configs/cobalt/rules.yaml | 2 +-` only (`7001737f docs(close): 2026-10-23`), not a spec path.
- MAIN'S LAST COMMITS: `41bb2402 Revert "Merge branch 'main' into deploy/deploy-radar-mirror-scope"`, `4f35be8f` the merge, `2618a9ad` the deploy report, `baa08130` R2409-R2410, `148b03ef` HEAD.
- MARKERS on HEAD (19:5x): `git grep -c -F "MIRROR_SOURCE_PREFIX = " HEAD -- src/cobalt/radar/notes.py` → no match (`0`); `git ls-tree --name-only HEAD tests/cobalt/test_radar_mirror_scope.py src/cobalt/radar/notes.py` → `src/cobalt/radar/notes.py` only (the test file ABSENT on main: "absent = valid before", deploy 1027 P6). On `25994142`: each marker `1`.
- SMOKE: `deploy-smoke.sh:10` `ls <path> | ls "<path>"`, `:118` `"ls "*)`, `:188` runs `ls "$path"`; `:135-136` curl `http://127.0.0.1:5010/*` only. `DEPLOY-HUB.md:11` (HEAD) admits `"Bash(ls *)"` and `"Bash(curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*)"`; `:152` (c) the three radar curls; `:158` (h) the four failure counts, a growing count RED.
- DEPLOY 1027 (`reports/deploy-deploy-radar-mirror-scope.md`): `## RESTARTS` tool line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`src/cobalt/radar/notes.py` · static import reach), cos loaded and kept; (h) `radar panel FAILED` 21 → 23, the same `CardSettingsError … radar.cards_enabled` on the reverted tree 24 → 26; `## DECISIONS` 2.
- `BUILD-HUB.md:14` (HEAD): `"Edit(//Users/cobalt/cobalt-wt/**)"`, `git show*`, `git diff *`; no `git apply`, `cherry-pick`, `git mv`, `revert`. `:16`: `Never typed: … rm of anything but the .env string, git checkout, … git merge`.
- RULINGS: `cto-2026-10-18.md:90` R1863 `HIS RULING · APPROVED` (as card 1020). The route: brain 2026-10-24 (L79), desk rows R2409, R2410 (`cto-2026-10-24.md:8-9`).
