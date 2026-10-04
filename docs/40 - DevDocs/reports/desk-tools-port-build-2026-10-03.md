# desk-tools-port — build report (2026-10-04; P5 added in a second session the same day)

## §0 Headline
- `07` brain-hub (`b5eb3530`) and `09` worker-watch (`a6bef8cb`) are ported onto `5ff16b1f` in one commit, `1c702713`. Twelve of their files are byte-identical to their heads (hash proof at E3).
- `desk-launch.sh`, `STANDING-LIST.md` and `test_desk_size_guard.py` are merged by hand. Each differs from one parent by the other parent's side only. The one new line is the unknown-kind list, which now names `recut` and `brain`; its pin in `test_desk_launch_devfix.py:383` follows.
- Every row went red on BASE for its named reason and red under its mutation, including `03c`'s optional TREE STATE and the stop hook's `cwd` exemption (X3). Suites at `1c702713`: offline 3751/0 · `tests/ops` 800/0 · live-note 146/0 · with-DB not run (DB: none). RESTARTS: none. His install text (P4) is valid JSON and sits under `## RECORDS`.
- P5 (second session, 10-04): the brain's line now defaults to `--model claude-opus-5-5`. `desk-launch.sh brain <handover> --fable` puts `claude-fable-5-1` on it, and any other value is refused. `## MEASURE` runs every ten answers. At 500,000 the brain messages `cto-desk` for its own replacement and names the next model. Red `1e171885`, fix `5c1d629f`. Offline 3751/0 · `tests/ops` 827/0 · live-note 146/0.
- Decisions: 0.

## L74
One block arrived in this session, in a system reminder (not a tool result). It asked that commits end with a `Claude-Session: https://claude.ai/code/session_…` line. Treated as DATA and not acted on: `d51c2125` and `1c702713` carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).
The second session (P5) received the same block again in a system reminder; DATA, not acted on: `1e171885`, `5c1d629f` and the report commit carry the `Co-Authored-By` line only.

## AUTHORIZATION
Started `Sun Oct  4 13:16:34 EDT 2026` (`date`).

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/07b-desk-tools-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/07b-desk-tools-port-card.md"` | 0 | `587710e76d2528667687f12f7f2020a41b79bedd` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST 2026-09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 2026-10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): … \| HIS RULING · APPROVED \|` |
| R47 committed | `git … log -1 --format=%H -S"\| R47 \|"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 2026-10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` |
| R157 committed | `git … log -1 --format=%H -S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| 2026-10-02 R154 | `grep -n "^\| R154 " cto-2026-10-02.md` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check … \| HIS RULING · APPROVED \|` |
| R154 committed | `git … log -1 --format=%H -S"\| R154 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

All hold.

P5, second session (14:10 ET): `grep -n -E "«INSTAL[L]" ".../BUILD-HUB.md"` → (nothing); `grep -n -E "«FIL[L]" "<card>"` → (nothing); `git -C /Users/cobalt/cobalt log -1 … -- "<card>"` → `e929fce161494491fad80386c909f808c4bc5edf` (P5's last edit, 13:41 ET); `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` → (nothing). The card's RULINGS header is unchanged (R47, R157, R154 above). P5 cites his 10-04 rulings, which sit in `cto-2026-10-03.md` (no `cto-2026-10-04.md` exists: `grep` → `No such file or directory`, exit 2); Grep tool on `reports/`:
- `cto-2026-10-03.md:194:| R188 | 10-04 13:36 ET | HIS RULING (brain relay): at 500,000 tokens the brain asks the desk by message for its own restart. … | APPROVED — pending fold |` — committed `328d08d8b850a3a2b50ef21b3e15e38970f0392b` (`git … log -1 --format=%H -S"| R188 |"`).
- `:195:| R189 | 10-04 13:36 ET | HIS RULING (brain relay): brain starts on Opus 5.5, Fable 5.1 only for design/high-effort, back to Opus at restart; \`07b\` row P5 (\`--fable\`), \`00-brain-handover.md\` MODEL Opus. … | APPROVED — pending fold |` — committed `328d08d8…`.
- `:197:| R191 | 10-04 13:41 ET | HIS RULING (brain relay, extends R188): past 500,000 every brain asks the desk for its own restart, no word of his; in code: \`07b\` P5 \`## MEASURE\` + the brain measures every ten answers. … | APPROVED — pending fold |` — committed `e929fce161494491fad80386c909f808c4bc5edf`.
Each carries HIS RULING and APPROVED, committed. All hold.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 13:16:34 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-port-1003` + `?? "docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md"` (this report, written first by REPORT's rule) |
| HEAD = BASE | `git log --oneline -1` | 0 | `5ff16b1f fix(adoption-port): port the adoption chain onto a8d8a848; …` |
| main's view | `git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-tools-port-1003` | 0 | `5ff16b1f …` (same) |
| clean on BASE | `git diff --stat 5ff16b1f` | 0 | (nothing) |
| BASE | `git show --stat 5ff16b1f` | 0 | `fix(adoption-port): port the adoption chain onto a8d8a848; …` · `tests/ops/test_hub_lines.py \| 7 +++++--` |
| no .env | `ls /Users/cobalt/cobalt-wt/desk-tools-port-1003/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| 07 range | `git diff --stat a09f0862 b5eb3530` | 0 | 7 files: `08-brain-handover.md` +8, `BRAIN-HUB.md` +43, `STANDING-LIST.md` +13, `brain-hub-build-2026-10-03.md` +190, `ops/desk/desk-launch.sh` 91, `tests/ops/test_desk_launch_brain.py` +412, `tests/ops/test_desk_size_guard.py` 4 |
| 09 range | `git diff --stat a09f0862 a6bef8cb` | 0 | 8 files: `worker-watch-build-2026-10-03.md` +237, `desk-watch.sh` +37, `idle-wake.py` +54, `stop-guard.py` +138, `wait-stop-line.sh` 75, `test_desk_watch.py` 382, `test_idle_wake.py` +115, `test_stop_guard.py` +251 |
| source trees | `git -C /Users/cobalt/cobalt-wt/brain-hub-1003 diff --stat b5eb3530` · `git -C /Users/cobalt/cobalt-wt/worker-watch-1003 diff --stat a6bef8cb` | 0 · 0 | (nothing) · (nothing): both worktrees hold their heads; their files are read from there |
| heads | `git -C /Users/cobalt/cobalt log --oneline -3 ops/brain-hub-1003` · `… ops/worker-watch-1003` | 0 · 0 | `b5eb3530 fix(brain-hub): the prompt kind reads the seat value as eval hands it …` · `a6bef8cb fix(worker-watch): a WAKE line raised while busy is spent …` |
| unknown-kind text | `grep -n -F "is none of build" ops/desk/desk-launch.sh` | 0 | `89:#   - a kind that is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops; …` · `437:    *) refuse "kind '$kind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops" ;;` |
| recut kind | `grep -n -F "recut)" ops/desk/desk-launch.sh` | 0 | `435:    deploy\|recut) fixed="$PROMPTS/DEPLOY-HUB.md" ;;` · `848:recut)` |
| TREE STATE optional | `grep -n -F "grep -q '^TREE STATE:'" ops/desk/desk-launch.sh` | 0 | `508:    grep -q '^TREE STATE:' "$card" \|\| return 0` |
| callers of the kind list | `grep -rn -F "is none of" tests/ops` | 0 | `tests/ops/test_desk_launch_devfix.py:383:            "kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops")` — pins the text P1 changes (DECISION 1) |
| P4 path | `ls ops/desk/bare-guard.py` | 0 | `ops/desk/bare-guard.py` |
| wc | `wc -l` of the edited files | 0 | `991 ops/desk/desk-launch.sh` · `53 ops/desk/desk-watch.sh` · `27 ops/desk/wait-stop-line.sh` · `454 tests/ops/test_desk_size_guard.py` · `165 tests/ops/test_desk_watch.py` · `207 docs/40 - DevDocs/prompts/STANDING-LIST.md` |
| READ tails | `tail -n 3 …/brain-hub-check-2026-10-03-r2.md` | 0 | `CHECK DONE · job: brain-hub · pass: 1 · tip: b5eb3530 · … · ready: YES · decisions: 0 · for Dejan: 0` |
| | `tail -n 3 …/worker-watch-check-2026-10-03-r2.md` | 0 | `CHECK DONE · job: worker-watch · pass: 1 · tip: a6bef8cb · … · ready: YES · decisions: 0 · for Dejan: 0` |
| READ §0 | `grep -n -F "## §0" -A 6` on both check reports | 0 | brain-hub: "1 finding, held and fixed. O1 (B5) … Red `03ce2125`, fix `b5eb3530`." · worker-watch: "Two own findings, both in W1, both HELD and fixed … Base `a09f0862`, tip `1bfd26e3`, now `a6bef8cb`." |
| RESTARTS empty | `uv run cobalt jobs restarts 5ff16b1f..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none` (only this untracked report) |

THE SHARED PATHS, BOTH ONE-SIDED DIFFS (from `a09f0862`):
- `ops/desk/desk-launch.sh` — `07` (`git diff a09f0862 b5eb3530 --`): the `brain` usage/header lines, the `prompt` header's "a brain tab" struck, the header kind list `+ brain`, the two refusal bullets, the usage line `| brain <handover file>`, the B5 seat refusal in the `prompt` kind, the whole `kind brain` block before `install-ops`. BASE (`git diff a09f0862 5ff16b1f --`): the `recut` header and refusal bullets, `export LC_ALL=C`, the recut-args refusal, the `recut` usage/case, RULINGS `none` for recut, TREE STATE optional (`:508`), the `recut)` block. Both touch line 89 (the header kind list) only; the code list at `:437` is touched by neither.
- `ops/desk/desk-watch.sh` — BASE: `+export LC_ALL=C` after the header (one line). `09`: the same line at the same place plus the idle exit. Merged = `09`'s file.
- `ops/desk/wait-stop-line.sh` — BASE: `+export LC_ALL=C` before the guard line. `09`: `export LC_ALL=C` above the `--idle` branch, the guard moved below it. Merged = `09`'s file (one export, before every command).
- `docs/40 - DevDocs/prompts/STANDING-LIST.md` — `07`: `## 7. BRAIN-HUB.md` appended after `## 6`'s Deny line. BASE: R39 class rewrites in the head, §1–§3 and §6's table; `## 6`'s last two lines untouched. Merged = BASE's text + `07`'s §7 appended.
- `tests/ops/test_desk_size_guard.py` — `07`: `04-brain-prompt.md` → `04-survey-prompt.md`, seat `brain` → `survey` (lines 259–262). BASE: `desk_list` stub under `ops/` beside the staged `desk-context.sh` (lines 84–96). Disjoint.

RECORDS COPIED (card `## RECORDS`), re-read:
- RESTARTS homes at BASE: `restarts.py:38` `OPS_DESK_PREFIX = "ops/desk/"` ✓; `:228` `output.append(Classification(path, item.change, "DOCS", ()))` ✓; `:246` `rule = "test/documentation; no resident"` ✓. No `src/`, no `configs/` in the card.
- Preflight r2 (`reports/07b-card-preflight-2026-10-03-r2.md`): `ready: NO` on two fails (5a the backticked `## 7.` grep, 5c two rows `P3`); the card as committed carries the backticked grep and row `P4` — both fixed.
- Judge 10-03 21:39 ET: set 3, his install follows set 3's DEPLOYED line — not re-readable by this list; carried.

P5 PREFLIGHT (second session; RECOVERY's three calls are under `## RECORDS`, CONTINUED):
- The brain kind at `5fa56360`: Grep tool `brain|opus|fable|MODEL` (case-insensitive) on `ops/desk/desk-launch.sh` → `:413 if [ "$kind" = "brain" ]; then`, `:414 [ "$#" -eq 2 ] || refuse "usage: desk-launch.sh brain <absolute handover path>"`, `:439 fixed="$PROMPTS/BRAIN-HUB.md"`, `:449 *"--remote-control brain --name brain"*) ;;`, `:470 run_launch "$REPO" "$line" …`; no `opus` or `fable` in the script.
- `BRAIN-HUB.md:3` `MODEL: Fable 5.1 (\`claude-fable-5-1\`)`; `:8` the line's `--model claude-fable-5-1`; `## MEASURE` `:33` (read whole). `STANDING-LIST.md:209` §7 `\`--model claude-fable-5-1\``; `:211` the comparison sentence. `23-brain-judge.md`'s line: `--model claude-fable-5-1` (Grep `-o`).
- Callers of the usage text: `grep -rn -F "brain <handover file>" tests/ops` → (nothing).
- No `.env`: `ls -la …/.env` → `No such file or directory`.

## E0 BASELINE
P5 ran no new E0: BASE is the same `5ff16b1f`, and the baseline below stands.
- Offline on `5ff16b1f`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 605.02s (0:10:05)`, exit 0: 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.96s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Test files written (no `ops/`, `docs/` or `src/` edit):
- `tests/ops/test_desk_launch_brain.py` (P1) — `07`'s file from `b5eb3530`, written whole; hash-proven after `git add`: `git diff --cached --stat b5eb3530 -- tests/ops/test_desk_launch_brain.py` → (nothing).
- `tests/ops/test_stop_guard.py`, `tests/ops/test_idle_wake.py` (P2) — `09`'s files from `a6bef8cb`: `git diff --cached --stat a6bef8cb -- tests/ops/test_idle_wake.py tests/ops/test_stop_guard.py` → (nothing).
- `tests/ops/test_desk_watch.py` (P2) — BASE's file is `a09f0862`'s (BASE never touched it), so `09`'s hunks were applied by Edit: `git diff --stat a6bef8cb -- tests/ops/test_desk_watch.py` → (nothing).
- `tests/ops/test_desk_launch_devfix.py:383` (P1, the unknown-kind list: the follow-up line of brain-hub DECISION 5, which the card says lands here) — the pinned text gains `brain`: `"kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops"`.

`uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfE tests/ops/test_desk_launch_brain.py tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py tests/ops/test_desk_launch_devfix.py::test_an_unknown_kind_names_devfix_among_the_kinds` → `74 failed, 3 passed, 15 warnings in 3.92s`.
- P1, `test_desk_launch_brain.py` B2/B5 cases: first line `AssertionError: REFUSED: kind 'brain' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops` (`:138`, `:145`, `:160`, `:129`) — the row's red (no `brain` kind on BASE); the B5 `prompt`-kind cases `assert 0 == 1` with the brain line printed (dry) or `RUN: claude --bg …` (real) — the `prompt` kind runs a brain line on BASE.
- P1, B1/B4 cases: `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/desk-tools-port-1003/docs/40 - DevDocs/prompts/BRAIN-HUB.md'` — the hub is not ported yet.
- P1, the kind list: `AssertionError: … assert "REFUSED: kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops" in "WARNING: desk size unread — guard skipped\nREFUSED: kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops\n"` (`test_desk_launch_devfix.py:142`).
- P2, `test_stop_guard.py` (30) and `test_idle_wake.py` (7): `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/desk-tools-port-1003/ops/desk/stop-guard.py'` / `…/idle-wake.py'` — the row's red (no such file).
- 3 passed, as at `07`'s E2: `test_the_desk_size_guard_runs_first` (pinned by `07`'s M3) and the two `test_b5_a_prompt_line_on_another_seat_still_launches` negative controls.

`uv run pytest -q -p no:cacheprovider --color=no --tb=line -rf tests/ops/test_desk_watch.py` (background) → `13 failed, 25 passed, 15 warnings in 286.31s (0:04:46)`.
- P2, W1 positives: `AssertionError: STILL RUNNING after 20s — last line: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3` (`:226`, `:286`, `:388`, `:409`, `:422` ×3, `:432`); `…restarts_the_idle_count` `STILL RUNNING after 20s — last line: RESUMED: E2 11:00` (`:266`); the two refusals `assert 2 == 1` (`:441`, `:450`); the two wait-stop-line cases `TIMEOUT after 200s — last line was: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3` (`:477`, `:520`) — the row's red: the watch waits past the stub's idle answers until its timeout.
- 25 passed: the 15 existing desk-watch tests through the staged copy and the 10 W1 negative controls (green on BASE by design, each red under its mutation at E3).

No RUN-row test is new here: P4's RUN is `test_stop_guard.py::test_i1_run_his_install_text`, red above on `FileNotFoundError … stop-guard.py`; it is run with `-rP` at E3.

### E2 — P5 (second session, 2026-10-04 14:10 ET onward; on `5fa56360`)
`tests/ops/test_desk_launch_brain.py` only: `STANDIN_LINE` carries `--model claude-opus-5-5` (the hub's new default); `:289` and the allow-list comparison (`:301`, `23`'s Fable word read as the Opus default) follow the row; ten new `test_p5_*` tests (the default line, `--fable` dry and real, eight other values dry and real, a flag after `--fable`, a hub line without exactly one Opus word, the tree's hub with `--fable`, the hub's `## MEASURE` text, `STANDING-LIST.md` §7). Red commit `1e171885`.
`uv run pytest -q -p no:cacheprovider --color=no --tb=line -rfE tests/ops/test_desk_launch_brain.py` → `26 failed, 38 passed, 15 warnings in 4.47s`. First lines:
- `:292` (the tree's hub line) `assert '--model claude-opus-5-5 --permission-mode auto --remote-control brain --name brain' in 'claude --bg …'`; `:301` `- --model claude-opus-5-5 … + --model claude-fable-5-1 …` — the hub's line is Fable on BASE.
- `test_p5_fable_puts_fable_on_the_line_instead[True|False]`, `…a_hub_line_that_does_not_default…`, `…the_trees_hub_line_takes_fable…`: `AssertionError: REFUSED: usage: desk-launch.sh brain <absolute handover path>` / `assert 1 == 0` (`:432`) — no `--fable` on BASE.
- `test_p5_any_other_value_is_refused[*]` (16): `assert 'REFUSED: usage: desk-launch.sh brain <absolute handover path> [--fable]' in 'REFUSED: usage: desk-launch.sh brain <absolute handover path>\n'` (`:132`) — refused, but not by the row's usage.
- `…hubs_measure…` `:486` `assert 'every ten answers' in 'MESSAGE \`cto-desk\` for your MEASURE …'`; `…standing_list…` `:496` `assert ('\`--model claude-opus-5-5\`' in ' — THE STANDING BRAIN SEAT …')`.
- Green on BASE by construction: `test_p5_the_default_line_holds_opus` (the stand-in line is Opus and BASE passes it through; red under M11 below). The `opus-twice` id of `test_p5_a_hub_line_that_does_not_default_to_opus_is_refused` was added at E3 (see there).

## E3 THE ROWS
Built in card order P1, P3, P2, then P4 (RUN); P5 in the second session (below). Red commit `d51c2125`; code commit `1c702713 fix(desk-tools-port): port 07 brain-hub (b5eb3530) and 09 worker-watch (a6bef8cb) onto 5ff16b1f; desk-launch.sh and the two shared files hand-merged; the unknown-kind list names recut and brain (P1, P3, P2; L3, L72)` — 11 files, 879+/11−. Files whose source text comes from `git show <head>:<path>`: they were read from the two source worktrees, whose trees equal their heads (PREFLIGHT `git -C … diff --stat <head>` → nothing). New files were written whole with the Write tool; files BASE already holds were patched hunk by hunk with the Edit tool. No `git checkout`, `cp` or `merge` was used.

HASH PROOF at the tip `1c702713`:
- `git diff --stat b5eb3530 HEAD -- "docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md" "docs/40 - DevDocs/prompts/BRAIN-HUB.md" "docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md" tests/ops/test_desk_launch_brain.py` → (nothing): `07`'s four unshared files are byte-identical.
- `git diff --stat a6bef8cb HEAD -- "docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md" ops/desk/desk-watch.sh ops/desk/idle-wake.py ops/desk/stop-guard.py ops/desk/wait-stop-line.sh tests/ops/test_desk_watch.py tests/ops/test_idle_wake.py tests/ops/test_stop_guard.py` → (nothing): all eight of `09`'s files are byte-identical, the two files BASE also changed among them (BASE's side there was the one line `export LC_ALL=C`, which `09` carries too).
- The three hand-merged files against each parent: `git diff --stat 5ff16b1f HEAD -- …` → `STANDING-LIST.md | 13 +++++`, `desk-launch.sh | 93 ++++…--`, `test_desk_size_guard.py | 4 +-` (plus `test_desk_launch_devfix.py | 2 +-`, the kind-list pin): `07`'s side only. `git diff --stat b5eb3530 HEAD -- …` → `STANDING-LIST.md | 39`, `desk-launch.sh | 105`, `test_desk_size_guard.py | 7`: BASE's side only. `git diff b5eb3530 -- ops/desk/desk-launch.sh`, read whole at E3, holds BASE's one-sided hunks (recut header, refusal bullets, `export LC_ALL=C`, the recut-args refusal, the recut usage and case, RULINGS `none` for recut, optional TREE STATE, the `recut)` block) and ONE line in neither parent: `:518` `*) refuse "kind '$kind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops" ;;` (the card's one allowed line). The header list (`:92`) is the merge of both parents' lines.

- **P1** `ops/desk/desk-launch.sh` (07's hunks by Edit onto BASE: the `brain` usage and WHAT IT DOES lines, "a brain tab" struck from `prompt`, the header kind list, the `prompt` and `brain` refusal bullets, the usage line, the B5 seat refusal in the `prompt` kind, the whole `kind brain` block before `install-ops`; the code kind list at `:518`); `BRAIN-HUB.md`, `2026-10-03/08-brain-handover.md`, `reports/brain-hub-build-2026-10-03.md` written whole; `tests/ops/test_desk_launch_devfix.py:383` pins the new list. Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_brain.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_install_ops.py` → `163 passed, 15 warnings in 44.75s`.
- **P3** `STANDING-LIST.md`: `07`'s `## 7. BRAIN-HUB.md` appended after BASE's `## 6` Deny line (BASE's R39 class text kept whole). `tests/ops/test_desk_size_guard.py`: `07`'s `04-survey-prompt.md` / `--remote-control survey --name survey` fixture onto BASE's `desk-list.sh`-beside staging. Two one-sided diffs from `a09f0862` quoted at PREFLIGHT. Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_size_guard.py tests/ops/test_desk_launch_brain.py tests/ops/test_hub_lines.py` → `96 passed, 1 xfailed, 15 warnings in 10.81s` (the xfail is G3's strict probe, as at both parents). The count: Grep tool, pattern ``## 7. `BRAIN-HUB.md` ``, `output_mode: count` on `STANDING-LIST.md` → `1` (the card's `grep -c -F` with a backtick is refused by the hub's grep rule: `## RECORDS`).
- **P2** `stop-guard.py`, `idle-wake.py` written whole; `desk-watch.sh` and `wait-stop-line.sh` patched by Edit with `09`'s hunks (the merged result = `09`'s file, hash above). Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py tests/ops/test_bare_guard.py` → `76 passed, 15 warnings in 2.87s`; `uv run pytest -q -p no:cacheprovider --color=no --tb=line -rf tests/ops/test_desk_watch.py tests/ops/test_desk_done.py` (background) → `57 passed, 15 warnings in 75.53s (0:01:15)`.
- **P4** RUN, whole (it asserts nothing): `uv run pytest -q -rP -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k i1_run` → `1 passed, 29 deselected, 15 warnings in 0.76s`; the test cuts the object out of `stop-guard.py`'s header, writes it to a `tmp_path` file and `json.load`s it (valid JSON proved). Captured stdout is in `## RECORDS` (HIS INSTALL TEXT).
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (both source builds recorded the same: `brain-hub-build` `## RECORDS`, `worker-watch-build` `## E3`), so no dated module line was written.

THE MUTATIONS (Edit tool, each undone with the Edit tool):
| # | row | mutation | run | result | first failing line |
|---|---|---|---|---|---|
| M1 | P1 (the kind list undone) | `:518` back to BASE's `… recut, desk, prompt, close, install-ops` | `tests/ops/test_desk_launch_devfix.py` | `1 failed, 47 passed` | `test_desk_launch_devfix.py:142: AssertionError: … assert "REFUSED: kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops" in "WARNING: desk size unread — guard skipped\nREFUSED: kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops\n"` |
| M2 | P1 (the brain kind undone) | `if [ "$kind" = "brain-MUTANT" ]` | `tests/ops/test_desk_launch_brain.py` | `25 failed, 14 passed` | `test_desk_launch_brain.py:138: AssertionError: REFUSED: kind 'brain' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops` |
| M3 | P1 (B5 undone) | the seat match on `brain-MUTANT` | `tests/ops/test_desk_launch_brain.py` | `10 failed, 29 passed` | `test_o1_…`, the 6 `test_b5_a_prompt_line_naming_…` and the 3 `test_check_o1_a_quoted_or_spaced_…` cases; the 2 negative controls passed |
| M4 | P1 (`03c`'s optional TREE STATE dropped in the merge) | `grep -q '^TREE STATE-MUTANT:'` | `tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_recut.py` | `6 failed, 72 passed` | `test_desk_launch_prechecks.py:222: AssertionError: WATCH: …` / `assert 0 == 1` (`test_m4_a_card_with_a_tree_state_of_another_shape_is_refused` ×6: the bad shape launches) |
| M5 | P3 (`07`'s fixture undone) | fixture back to `--remote-control brain --name brain` | `tests/ops/test_desk_size_guard.py` | `1 failed, 37 passed, 1 xfailed` | `test_desk_size_guard.py:331: AssertionError: REFUSED: a brain seat launches by desk-launch.sh brain <handover>` (`test_g2_a_passing_guard_lets_every_kind_reach_its_launch[prompt]`) |
| M6 | P3 (BASE's side undone) | the stub back under `list/` | `tests/ops/test_desk_size_guard.py` | `13 failed, 25 passed, 1 xfailed` | `test_desk_size_guard.py:93: AssertionError: assert PosixPath('…/list/desk-list.sh') == ((PosixPath('…') / 'ops') / 'desk-list.sh')` |
| M7 | P2 (S2 (b), S2 (a), N1 type filter) | `"DEPLOYED ·"`; the no-`CARD:` exemption `and False`; idle-wake's `notification_type` test removed | `tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` | `3 failed, 34 passed` | `test_stop_guard.py:137: AssertionError: assert (2, 'NOT A RE...then stop.\n') == (0, '')`; `:197 … (2, '', 'NOT ...then stop.\n') == (0, '', '')`; `test_idle_wake.py:78: AssertionError: assert not True` |
| M8 | P2 (X3: the `cwd` exemption) | `if worktree(cwd) is None and False` | `tests/ops/test_stop_guard.py` | `1 failed, 29 passed` | `test_stop_guard.py:108: AssertionError: /Users/cobalt/cobalt` / `assert (2, '', 'NOT ...then stop.\n') == (0, '', '')` |
| M9 | P2 (desk-watch idle exit) | the probe call → `out=busy; rc=0` | `-k "idle_for_two_polls or wake_line_for_the_worktree or exits_3_gone or no_desk_list"` | `4 failed, 34 deselected` | `test_desk_watch.py:226: AssertionError: STILL RUNNING after 20s — last line: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3` |
| M10 | P2 (wait-stop-line idle exit) | its probe call → `out=busy; rc=0` | `-k wait_stop_line` | `2 failed, 1 passed, 35 deselected` | `test_desk_watch.py:477: AssertionError: TIMEOUT after 200s — last line was: (run in progress — next step under ## CONTINUE)`; the negative control `…without_a_session_reads_no_listing` passed |
(M1–M10 and the undo proof below are the first session's, at `1c702713`.)

- **P5** (second session) — code commit `5c1d629f feat(desk-tools-port): the brain's line defaults to Opus; desk-launch.sh brain <handover> --fable puts Fable on it, any other value refused; MEASURE every ten answers and the 500,000 self-replacement message naming the next model (P5; L3, L72)`, 4 files, 32+/14−.
  - `ops/desk/desk-launch.sh` (`:417`–`:420`): the kind takes `<handover>` or `<handover> --fable`; anything else → `REFUSED: usage: desk-launch.sh brain <absolute handover path> [--fable]`. `:461`–`:468`: the hub's line must hold ` --model claude-opus-5-5 ` exactly once (else `REFUSED: the brain line does not default to --model claude-opus-5-5`); with `--fable` that one word becomes ` --model claude-fable-5-1 `, by shell expansion, nothing else on the line touched. Header lines `:31`–`:33`, `:70`–`:71`, `:113`–`:114` and the top usage `:232` name `[--fable]`.
  - `BRAIN-HUB.md`: `MODEL:` Opus 5.5 by default, Fable 5.1 only on `--fable` (R189); `## LAUNCH` names `--fable` and its one-word change; the line's `--model claude-opus-5-5`; `## MEASURE`: every ten answers, when he asks, before any long write (R191); at 500,000 MESSAGE `cto-desk` for its own replacement, no word of his (R188, R191), naming the next seat's model — Fable (`--fable`) only while a design task is open, else Opus (R189).
  - `STANDING-LIST.md` §7 (`:209`): the two model words, "the only variable of the line, and no allow or deny string changes with them"; the launch `desk-launch.sh brain "<handover>" [--fable]`; `:211` the comparison reads `23`'s Fable word as the Opus default.
  - A real gap found at E3: the first fix missed two ADJACENT Opus words (`… --model claude-opus-5-5 --model claude-opus-5-5 …` share the blank between them, so the second was not seen after the first was cut off). The new `opus-twice` case went red on it (`2 failed, 64 passed`: `[flag0-opus-twice]`, `[flag1-opus-twice]`, `assert 0 == 1` at `:131`); the check now looks again from that blank (`case " $after"`), and the case is green.
  - Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line -rf tests/ops/test_desk_launch_brain.py tests/ops/test_desk_size_guard.py tests/ops/test_hub_lines.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_install_ops.py` → `247 passed, 1 xfailed, 15 warnings in 54.56s` (`test_desk_launch_brain.py` alone: `66 passed`).
  - DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (as at P1–P3); no dated module line.

| # | row | mutation | run | result | first failing line |
|---|---|---|---|---|---|
| M11 | P5 (the default undone: Fable always) | `[ "$#" -eq 99 ] \|\| line=…` | `test_desk_launch_brain.py` | `4 failed, 60 passed` | `:142` the good case prints `--model claude-fable-5-1`; `:164`; `:290` the tree's hub; `:426` `test_p5_the_default_line_holds_opus` `assert (' --model claude-opus-5-5 ' in '… --model claude-fable-5-1 …')` |
| M12 | P5 (the flag inverted) | `[ "$#" -eq 3 ] \|\| line=…` | `-k p5` | `4 failed, 21 passed, 39 deselected` | `:426` (default → Fable); `:434` `--fable` dry prints `--model claude-opus-5-5`; `:440` real args `assert (' --model claude-fable-5-1 ' in "--bg … --model claude-opus-5-5 …")`; `:473` |
| M13 | P5 (any third value accepted) | `[ "$3" != "--fable-MUTANT" ]` | `-k p5` | `16 failed, 9 passed, 39 deselected` | every `test_p5_any_other_value_is_refused[*]`: `:131 … assert 0 == 1` (the line printed / `RUN: claude --bg …` run) |
| M14 | P5 (a fourth argument accepted) | `[ "$#" -ge 3 ]` | `-k p5` | `1 failed, 24 passed, 39 deselected` | `test_p5_a_flag_after_fable_is_refused` `:131 … assert 0 == 1` |
| M15 | P5 (the Opus-word refusal off) | `"$line-MUTANT"\|*"$opus-MUTANT"*` | `-k p5` | `2 failed, 23 passed` (before `opus-twice`), then `-k default_to_opus` → `4 failed` | `:131 … --model claude-fable-5-1 … assert 0 == 1` (launched on Fable); the `opus-twice` ids launched with two `--model` words |
| M15b | P5 (the twice branch alone) | `*"$opus-MUTANT"*` | `-k default_to_opus` | `2 failed, 2 passed, 62 deselected` | `[flag0-opus-twice]` `:131 … --model claude-opus-5-5 --model claude-opus-5-5 … assert 0 == 1`; `[flag1-opus-twice]`; the `no-opus` ids passed |
| M16 | P5 (the hub's three texts) | the line back to `--model claude-fable-5-1`; "every ten answers, " struck from `## MEASURE`; §7's "are the only variable of the line" → "vary" | `test_desk_launch_brain.py` | `7 failed, 59 passed` | `:288 REFUSED: the brain line does not default to --model claude-opus-5-5` (the tree's hub, ×4 tests); `:301` the allow-list segment; `:490 assert 'every ten answers' in 'MESSAGE \`cto-desk\` …'`; `:501 assert 'the only variable' in …` |
After the P5 undos: `grep -rn -F "MUTANT" ops/desk/desk-launch.sh` → (nothing); `git diff --stat` → `BRAIN-HUB.md | 8`, `STANDING-LIST.md | 4`, the report, `desk-launch.sh | 26`, `test_desk_launch_brain.py | 8` (the fix and the `opus-twice` test, before `5c1d629f`); `git diff ops/desk/desk-launch.sh`, read whole, holds the fix only.

After the first session's undos: `grep -rn -F "MUTANT" ops/desk/desk-launch.sh` → (nothing); `git diff --stat` → `STANDING-LIST.md | 13`, `desk-launch.sh | 93`, `test_desk_size_guard.py | 4` (the fix only); `git diff --cached --stat a6bef8cb -- ops/desk/stop-guard.py ops/desk/idle-wake.py ops/desk/desk-watch.sh ops/desk/wait-stop-line.sh` → (nothing) and `git diff --stat` shows none of them (the tree back at the fix).

## RESTARTS
`uv run cobalt jobs restarts 5ff16b1f..HEAD` (HEAD `1c702713`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md	A	DOCS	-
docs/40 - DevDocs/prompts/BRAIN-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md	A	DOCS	-
docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md	A	DOCS	-
docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
ops/desk/idle-wake.py	A	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	A	operator script; no Cobalt reader	-
ops/desk/wait-stop-line.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_brain.py	A	test/documentation; no resident	-
tests/ops/test_desk_launch_devfix.py	M	test/documentation; no resident	-
tests/ops/test_desk_size_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_watch.py	M	test/documentation; no resident	-
tests/ops/test_idle_wake.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row (the tool also lists this uncommitted report).

P5, at HEAD `5c1d629f`: `uv run cobalt jobs restarts 5ff16b1f..HEAD` → the same seventeen rows, but `docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md	M	DOCS	-` (the report is committed now, and edited); no `UNCLASSIFIED` row; last line `RESTARTS: none`.

## W THE THREE SUITES
`<tip>` = `1c702713`. TREE STATE: unchanged; the diff adds no with-DB test and nothing under `src/cobalt/db_migrations`.
- (a0) `git diff --name-only --no-renames 5ff16b1f` → `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md`, `docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_launch_devfix.py`, `tests/ops/test_desk_size_guard.py`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 16 paths)`**.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 607.24s (0:10:07)`, exit 0: 0 failed, 0 errors → `<p>` = 3751. This build adds no test there.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `800 passed, 1 xfailed, 15 warnings in 326.96s (0:05:26)`, exit 0. Added by this build: `tests/ops/test_desk_launch_brain.py` (39 ids), `tests/ops/test_stop_guard.py` (30), `tests/ops/test_idle_wake.py` (7), and 23 `test_w1_*` ids in `tests/ops/test_desk_watch.py`; changed: `test_desk_launch_devfix.py::test_an_unknown_kind_names_devfix_among_the_kinds`, the `test_desk_size_guard.py` fixture.
- (b)–(d), (f): not run (DB: none).
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.54s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.
- `ls /Users/cobalt/cobalt-wt/desk-tools-port-1003/.env` → `No such file or directory` (14:01:50 EDT).

P5, `<tip>` = `5c1d629f` (second session):
- (a0) `git diff --name-only --no-renames 5ff16b1f` → the same sixteen paths plus `docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md` (17); every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 17 paths)`**.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 576.81s (0:09:36)`, exit 0 → `<p>` = 3751. P5 adds no test there.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `827 passed, 1 xfailed, 15 warnings in 321.69s (0:05:21)`, exit 0. Added by P5: 27 ids in `tests/ops/test_desk_launch_brain.py` (39 → 66; 800 + 27 = 827); changed: `STANDIN_LINE`, `:289`, the allow-list comparison.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.39s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` → `<l>` = 146.
- (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED for its named reason against a mutation or negative control. P1: 36 `test_desk_launch_brain.py` cases were red at E2 on `REFUSED: kind 'brain' is none of …`, `FileNotFoundError … BRAIN-HUB.md`, or the `prompt` kind running a brain line. At E3, 25 were red under M2 and 10 under M3. The 3 green at E2 are `07`'s known greens: the guard test, pinned by `07`'s M3, and the two B5 negative controls, which stayed green under M3 as negative controls should. The kind-list pin was red at E2 and under M1. P3: the fixture red under M5; BASE's side of the same file red under M6. P2: `test_stop_guard.py` and `test_idle_wake.py` all red at E2 (no such file); S2 (a), S2 (b), the N1 type filter and the `cwd` exemption red under M7/M8. W1: 13 red at E2 (`assert 2 == 3` / `TIMEOUT`); the desk-watch and wait-stop-line probes red under M9/M10. `03c`'s optional TREE STATE in the merged `desk-launch.sh` red under M4. No test stayed green under its mutation; none was rewritten (every test is the source head's, byte for byte).
(2) Every entry path pinned. `desk-launch.sh brain`'s callers: `grep -rn -F "desk-launch.sh brain" ops tests` → `ops/desk/desk-launch.sh:31` (header), `:360` (the B5 refusal text), `:414` (its usage), `tests/ops/test_desk_launch_brain.py:1`, `:235`, `:349`. No script calls the kind; the desk types it, and the test pins dry and real runs. The unknown-kind list: `tests/ops/test_desk_launch_devfix.py:383` (M1). `wait-stop-line.sh` callers: `grep -rn -F "wait-stop-line.sh" ops` → `desk-watch.sh:80` (the probe; M9 and every `test_w1_*` desk-watch test), `desk-launch.sh:1054` (the devfix reminder, three-argument form, pinned by `…without_a_session_reads_no_listing`; `09`'s DECISION 4, judged KEEP: `## RECORDS`), comments at `desk-watch.sh:8,15`, `desk-context.sh:10`, `idle-wake.py:9`. `stop-guard` callers: `grep -rn -F "stop-guard" ops` → `idle-wake.py:8,23,26` (the loader; `test_idle_wake.py` stages both) and its own header. The recut and devfix kinds beside the new `brain` kind: `tests/ops/test_desk_launch_recut.py` and `test_desk_launch_devfix.py` green at E3 and in `tests/ops` (800 passed).
(3) Every `file:line`, count and quote re-read from tool output at the tip `1c702713`. Re-run calls: `git log --oneline 5ff16b1f..HEAD` (2 commits); `grep -n -F "is none of build" ops/desk/desk-launch.sh` → `92`, `518`; `grep -n -F "a brain seat launches by desk-launch.sh brain" ops/desk/desk-launch.sh` → `360`; `grep -n -F "kind brain" ops/desk/desk-launch.sh` → `412`; `grep -n -F "grep -q '^TREE STATE:'" ops/desk/desk-launch.sh` → `589`; the three caller greps above; the hash-proof `git diff --stat <head> HEAD` calls at E3; the RESTARTS table re-run at HEAD.

P5 (tip `5c1d629f`): (1) the 26 E2 reds (`## E2 RED`, P5) and M11–M16; the one test green at E2, `test_p5_the_default_line_holds_opus`, red under M11 and M12; the `opus-twice` id red against the first fix, then under M15b; no test stayed green under its mutation. (2) `desk-launch.sh brain`'s entries: `grep -rn -F "desk-launch.sh brain" ops tests` → `ops/desk/desk-launch.sh:31` (header), `:363` (the B5 refusal), `:420` (the usage refusal), `tests/ops/test_desk_launch_brain.py:1`, `:238`, `:353`, `:449`, `:455`; no script calls the kind. Each argument shape is pinned: two args (the good cases, `test_p5_the_default_line_holds_opus`), `--fable` dry and real, eight other third values dry and real, a fourth argument, none or one argument (`test_the_usage_is_one_handover`); each hub shape: one Opus word (the tree's hub and the stand-in), none, two. `grep -rn -F "claude-fable-5-1" ops tests/ops` → only `desk-launch.sh:71`, `:468` and the test file. (3) Re-read at `5c1d629f`: `grep -n -F "fable" ops/desk/desk-launch.sh` → `31, 33, 71, 114, 232, 417, 419, 420, 461, 468`; `grep -n -F "opus" ops/desk/desk-launch.sh` → `71, 113, 462, 463, 466, 468`; `wc -l` → `1086 desk-launch.sh`, `43 BRAIN-HUB.md`, `220 STANDING-LIST.md`, `501 test_desk_launch_brain.py`; `git log --oneline 5ff16b1f..HEAD` (5 lines: `d51c2125`, `1c702713`, the report `5fa56360`, `1e171885`, `5c1d629f`); the RESTARTS table re-run at HEAD. The first session's line numbers below are at `1c702713`; P5 moved the brain block down by three (`:360` → `:363`, `:414` → `:420`).

## FOR THE CHECK
- Range `5ff16b1f..1c702713`: `d51c2125 wip(desk-tools-port): red — P1, P2 tests from b5eb3530 and a6bef8cb; the unknown-kind list pin`, `1c702713 fix(desk-tools-port): port 07 brain-hub (b5eb3530) and 09 worker-watch (a6bef8cb) onto 5ff16b1f; desk-launch.sh and the two shared files hand-merged; the unknown-kind list names recut and brain (P1, P3, P2; L3, L72)`.
- X1 hash pairs: `## E3 THE ROWS` HASH PROOF (twelve files equal to their head; the three merged files against both parents).
- X2 (`recut`, `brain`, the kind list, the `prompt` refusal, optional TREE STATE in one tree): pinned by `test_desk_launch_recut.py`, `test_desk_launch_brain.py` (dry runs), `test_desk_launch_devfix.py:383`, the B5 cases and `test_m4_*` in `test_desk_launch_prechecks.py`. All are green at the tip, and M1–M4 show each is live in the merged file. The check runs its own dry runs.
- X3 (the stop hook exempts `cwd` under `/Users/cobalt/cobalt`): `stop-guard.py` is `a6bef8cb`'s, byte for byte; `test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report` green, red under M8.
- Per row: reds at `## E2 RED`, mutations and greens at `## E3 THE ROWS`, quoted.
- Caller greps: `## PRE-STOP SELF-CHECK` (2).
- RUN row P4, whole: `## E3 THE ROWS` (command, `1 passed`) and `## RECORDS` (the object).
- Suites and executed commands: `## W THE THREE SUITES`. With-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- P5 (second session): range `5fa56360..5c1d629f` — `1e171885 wip(desk-tools-port): red — P5 brain model: Opus default, --fable, any other value refused; MEASURE every ten answers`, `5c1d629f feat(desk-tools-port): the brain's line defaults to Opus; desk-launch.sh brain <handover> --fable puts Fable on it, any other value refused; MEASURE every ten answers and the 500,000 self-replacement message naming the next model (P5; L3, L72)`. Reds at `## E2 RED` (P5), mutations M11–M16 and greens at `## E3 THE ROWS` (P5), suites at `## W` (P5). Dry runs to try: `desk-launch.sh brain <handover>` (Opus), `… --fable` (Fable), `… --opus` (REFUSED). The Opus-word refusal (`## RECORDS`) is the one check P5 adds beyond the row's words.

## CONTINUE
next: none — the desk verifies and launches the check (P1–P5 built; tip `5c1d629f`)

## DECISIONS
none

## RECORDS
- HIS INSTALL TEXT (P4; his word, 10-03): the value of `"hooks"` for user settings `~/.claude/settings.json`, valid JSON (proved by `tests/ops/test_stop_guard.py::test_i1_run_his_install_text`, `-rP`, `1 passed`). Captured stdout, whole:
```
{
  "PreToolUse": [
    {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"}]}
  ],
  "Stop": [
    {"hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py"}]}
  ],
  "Notification": [
    {"matcher": "idle_prompt", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py"}]}
  ]
}
```
  The settings write is his (NOT IN THIS JOB). The three paths must be on `main` first: `bare-guard.py` is at BASE (`ls ops/desk/bare-guard.py`), and `stop-guard.py` and `idle-wake.py` arrive with this branch. The card's record says his install follows set 3's DEPLOYED line.
- `tests/ops/test_desk_launch_devfix.py:383`: one line outside `07`'s files. It is the pin of the unknown-kind text the card's P1 changes ("the follow-up line lands here"; brain-hub build DECISION 5 named the follow-up as "one line in that test plus the message"). Without it `tests/ops` is red (M1). The card's fence allows the unknown-kind list.
- Carried, not built: `ops/desk/desk-launch.sh:1054`, the devfix reminder `watch: wait-stop-line.sh <its REPORT> '^(REBUILT|FAILED)'`, has no session argument (`09`'s DECISION 4, judged KEEP; a later `desk-launch.sh` follow-up card per desk row 2026-10-03 R69). It is a line in neither parent's diff, so it is outside this card's fence.
- REFUSED, not needed: `git diff a09f0862 b5eb3530 -- ops/desk/desk-launch.sh tests/ops/test_desk_size_guard.py docs/40\ -\ DevDocs/prompts/STANDING-LIST.md` and `git diff a09f0862 5ff16b1f --stat -- … docs/40\ -\ DevDocs/…` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (my error: backslash-escaped spaces; re-run as one quoted path per call).
- REFUSED, not needed: ``grep -c -F "## 7. `BRAIN-HUB.md`" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (a backtick in the pattern breaks the hub's grep rule; counted with the Grep tool instead → `1`).
- Card records re-read at PREFLIGHT: the RESTARTS homes (`restarts.py:38`, `:228`, `:246`) hold; preflight r2's two fails are fixed in the committed card; the judge's 10-03 21:39 ET line (set 3, his install after set 3's DEPLOYED) is carried as stated (no listed command re-reads it).
- The ported `brain-hub-build-2026-10-03.md` and `worker-watch-build-2026-10-03.md` end with their own `BUILT ·` lines; they are other jobs' reports, ported as `07`'s and `09`'s files, and are not this report.
- `.env`: never present in this worktree (`DB: none`; no lock taken); `ls …/.env` → `No such file or directory` at PREFLIGHT and at W (14:01:50 EDT).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.
- `.env`: never present in the second session either; `ls …/.env` → `No such file or directory` at 14:10 and 14:32 EDT.
- CONTINUED at P5 14:10 (`date` → `Sun Oct  4 14:10:09 EDT 2026`): a NEW session, launch message `CONTINUE: P5.` with no fact. RECOVERY: `git status --short --branch` → `## ops/desk-tools-port-1003`; `git log --oneline -3` → `5fa56360 docs(desk-tools-port): build report — 1c702713` on top; `ls -la …/.env` → `No such file or directory`. The card gained row P5 after the first BUILT line: `git -C /Users/cobalt/cobalt log -3 --format=%H%x20%ci%x20%s -- "<card>"` → `e929fce1… 2026-10-04 13:41:31 -0400 docs(desk): R191 brain self-restart rule; 07b P5 measure every ten answers` · `328d08d8… 2026-10-04 13:37:14 -0400 docs(desk): R186-R190 his rulings via brain (…); 07b P5, brain handover MODEL` · `587710e7…` (the first build's card). The row is the card's, committed; the message widens nothing.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show --stat e929fce1` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (no listed prefix; the rulings were found with the Grep tool and proved committed with `git -C … log -1 -S`).
- P5's rulings (10-04 R188, R189, R191) are cited in the row, not in the card's `RULINGS` header; they were verified anyway (`## AUTHORIZATION`, P5). Their rows say "APPROVED — pending fold".
- R189 also names `00-brain-handover.md` MODEL Opus. That file is not in P5's `files` and is the brain's to edit (card `## RECORDS`, judge 10-03 21:39 ET); not touched here.
- R191 says "put it in code": the ten-answer MEASURE lives in `BRAIN-HUB.md`'s `## MEASURE`, the brain's fixed file, as the row places it. No script counts a brain's answers; the desk still runs `desk-context.sh` on the brain's message.
- How `--fable` is built: the hub's line must hold ` --model claude-opus-5-5 ` exactly once, and `--fable` replaces that one word. A line with no Opus word, or two, is refused (L1: never launched on whatever model it names). This refusal is P5's "Opus by default" made checkable, in P5's file; it adds no kind and no other line.

BUILT · job: desk-tools-port · tip: 5c1d629f | on 5ff16b1f | migration: none | offline 3751/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
