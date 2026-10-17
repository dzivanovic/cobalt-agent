# Preflight: card 671 `gemini-builder-row-fr1` (port job, rows PORT and FR-2), 2026-10-17

Read-only. Nothing launched, run or committed. Card: `prompts/2026-10-16/671-gemini-builder-row-card.md`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main`; `git diff --name-only 13bcd579 main` | main = `eb01cc38`. Card BASE `13bcd579` is its ancestor. `13bcd579..main` touches five files, all under `docs/` (card 671, prompt 708, `cto-2026-10-17.md`, `desk-wakeup-log.md`, the draft report). Header: JOB `gemini-builder-row-fr1`, BRANCH `ops/gemini-builder-row-fr1`, WORKTREE `gemini-builder-row-fr1`. | OK |
| 2 | read the card | `## PORT JOB`, rows PORT and FR-2, ORDER, DEPLOY ORDER, the O2 gate (`## NOT IN THIS JOB`, R1804, and CHECK ASKS), CHECK ASKS P1-P3 all present. | OK |
| 3 | `git diff --name-only 7f415a4f 695f8bde` | 8 files. Less the two old report files, the six are `SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh` and the three `tests/ops/` files. This matches the PORT row's list, and it asks for one PROOF line per file. | OK |
| 4 | `git diff --stat 7f415a4f main -- tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` | Empty. The three test files are untouched on main, so they are byte-equal to `695f8bde` after the port. | OK |
| 5 | `git diff -U0 7f415a4f main` against `git diff -U0 7f415a4f 695f8bde` over the three main-touched files | Hub: 583 inserts after `:27` and edits `:44`, `:61`, `:73`. 671 edits `:12`, `:15`, adds after `:21`, adds after `:26`, edits `:29` and `:88`. Guard: 583 is in `g5` (main `:1277`), 671 is in `builder_call`. Launcher: 583 has `routed=""` at `:379`, `--routed` at `:392`, and further hunks from `:991` to `:2356`. 671 has one comment line after `:376` and the arm at `:398` (main `:403`). No hunk overlap in any file. The hub inserts are adjacent (see N2). | OK |
| 6 | `grep -n "def test_b2" tests/ops/test_band_routing_1015.py` | `:112` `test_b2_control_the_three_builder_rows_stand`, `:116` `assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"])`, `:117` the `claude-opus-5-5` line. FR-2 names this exact test and the change from three to four rows (add `gemini-4-argon-high`, rename to `…_four_…`). | OK |
| 7 | `file:line` sampled against main (7 samples) | `bare-guard.py`: `write_targets` `:1171`, `builder_call` `:1180`, the `startswith(prefix)` test `:1197`, the write-target test `:1201-1202`, `head = verb(...)` `:1203`, `g5` `:1257`. `desk-launch.sh`: `:403` holds the Gemini arm. The card's `:398` is the old line. `SHADOW-HUB.md`: Terra row `:21`, Terra note `:26`, `:12`, `:15` as written, results Gemini row `:97`. The card says `:88` is the old line. The rows' old `file:line`s are declared as context and found by content (BUILD-HUB E3); the PORT row cites main's lines. | OK |
| 8 | scan the card for commands | Only `uv run pytest`, `uv run cobalt jobs restarts`, `git diff`, `git diff --stat`, `git -C … diff --name-only`, `grep -n -F`. The card says "No new command beyond the standing allow line". | OK |
| 9 | `files` columns against `## NOT IN THIS JOB` | The edit set is the six files plus `tests/ops/test_band_routing_1015.py`. Excluded: `house-probe.sh`, `CHECK-HUB.md`, `STANDING-LIST.md`, `test_house_probe.py` (card 670), the old job's two reports, `BUILD-HUB`. None is in a `files` column. | OK |
| 10 | `git diff HEAD --stat -- <card>`; `git status --short -- <card>`; `git log -2 -- <card>` | Diff empty. Status empty. Last commit `eb01cc38`. Found committed and clean (the desk commits this prompt next). | OK |
| 11 | `^\| R(1736\|1738) \|` in `cto-2026-10-17.md`; `git diff -U0 HEAD` on it; `git log -S"\| R1738 \|"` | Both rows say `HIS RULING · APPROVED`. The only uncommitted change in that file is the `OWED` and `STATE` lines (`:91-92`), so the rows stand as committed (`b57cbf8e`). | OK |
| 12 | `rev-parse --verify refs/heads/ops/gemini-builder-row-fr1`; `ls cobalt-wt` | No such branch (exit 1) and no `gemini-builder-row-fr1` worktree. The old `gemini-builder-row-1017` and `deploy-gemini-builder-row` worktrees exist, with other names. | OK |
| 13 | `git diff --name-only 695f8bde 06d31180` | Only the old job's two report files. The tip `695f8bde` has the same code as `06d31180`. | OK |
| 14 | `grep` tests and ops for the old refusal sentence and the `:28` pin | The sentence `Gemini is not in ## BUILDERS` is in `test_desk_launch_shadow.py:217` only, the one test L1 edits. `test_band_routing_1015.py:476` pins `FR5_NOTE` as a literal string and not as a line number, so the move of the BAND ROUTING paragraph does not break it (N3). | OK |
| 15 | `tests/ops/test_shadow_hub_file.py` at `695f8bde`, `builders()` | It reads rows that start with ``| ` ``, so the band rows (`\| LOW \|` etc.) never match. The hub has three band rows on main and the card keeps each once. | OK |
| 16 | `desk-launch.sh` build gates (read, not run) | See ISSUES B1-B3. Nothing blocks. | OK |

## ISSUES

- N1 NOTE: brain R1808 names 671's checked tip as `06d31180`. The card says CHECKED code tip `695f8bde`, and the later head adds only reports (check 13). The code is the same, so no action.
- N2 NOTE: 671's hub inserts (Gemini note and X1 paragraph) land after `:26`. 583's BAND ROUTING block lands after `:27`. They are adjacent but not overlapping, and the port is by Edit/Write (not merge), so the order in the card is unambiguous: Terra note, Gemini note, blank, X1 paragraph, blank, BAND ROUTING.
- N3 NOTE: after the port, 583's `(a routed card: … stop line BUILT · as :28)` text cites a stale line number. Draft decision 2 leaves it byte for byte, and the 583 test pins the string only, so this is harmless.
- N4 NOTE: the port tip's three test files were written against the `7f415a4f` hub. They are not proven green on main's tree (that is the builder's run). The only red the card expects is `test_b2_control_the_three_builder_rows_stand`.
- B1 NOTE (blocks `desk-launch.sh build`): the launcher has no port-job concept. `## PORT JOB` is read by the builder only, so the header needs no new key. The L7a row is `RULINGS: 2026-10-17 R1736, R1738`: both rows are HIS RULING + APPROVED and committed (check 11), so it passes. R1807 and R1808 are DESK RECORD rows and are not in RULINGS, which `ruling_row` would refuse. That is by design and not a block.
- B2 NOTE: other `build` gates pass. The card is committed and unchanged. BASE is hex8 and a commit on main. REPORT sits under `cobalt-wt/gemini-builder-row-fr1/…/reports/`. The branch and the worktree are absent. The card is dated 2026-10-16, which is at or after `BAND_FROM` 20261016, and its BAND is HIGH, so it launches BUILD-HUB's Opus 5.5 line with no `--routed` re-entry.
- B3 NOTE: the O2 gate (no Gemini build before the X1 cwd result is a DESK RECORD row, R1804) is a card rule and the launcher does not check it. This job builds files and launches no Gemini build, so it does not trigger.
- N5 NOTE: `cto-2026-10-17.md` has uncommitted `OWED` and `STATE` edits (`:91-92`). They do not touch the ruling rows, so they do not block.

PREFLIGHT DONE · card: gemini-builder-row-fr1 · checks: 16 · fails: 0 · ready: YES
