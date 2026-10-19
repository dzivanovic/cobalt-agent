# Draft amend 2 — gemini-read-grant-1019 (prompt 832)

## §0 Headline
- Card 827 amended in place and retitled "Gemini build: X1 split, cwd pin, builder text". Rows dropped: P0, R1, R2, R3, R4 (the read twin and its settings proofs), H1 (hub text for the twin only) and the ViewFile proof. Kept: H2, H3, D1. Added: C1, C2, T1. Not committed.
- C1: `builder_call` admits agy only when the seat's cwd is exactly `<WT>/<wt>`. RED: `x1-canary/`, the repo root, `<WT>`, a subdirectory and another worktree are all admitted today.
- C2: the launcher already cds the Gemini seat into its worktree (`desk-launch.sh:2575`, `:440`). The row adds a pin test and no code change.
- T1: new `ops/desk/x1-transcript.sh` copies the leg's `transcript.jsonl` (found from `cli.log`) and the log's `soft-denying` lines into the worktree. H2 now has legs 0a-0f, and leg 0f is the guard-refusal proof. BASE `6f2a4651` → `0c79bbae`.

## DECISIONS
1. ASK DESK: `authorize.sh` proves each RULINGS row by a line holding `HIS RULING` … `APPROVED` (`:115`). R2005, R2007 and R2011 are DESK RECORD rows, so AUTHORIZATION fails on the first of them. Card 800's RULINGS hold his rows only. Default taken: R2011 added as directed. Before the build, the desk either removes the three DESK RECORDs from RULINGS (they are quoted in `## RECORDS`) or accepts `FAILED: authorization mismatch`. [2026-10-19 08:41 EDT]
2. ASK DESK: it is UNPROVEN that the hook event's `cwd` follows the seat's `cd`. No guard ledger line has `cwd` x1-canary, and the tests use constructed events. Default taken: leg 0f is the live proof. Verdict (1) stops on an admitted call, and leg 0f's prompt is leg 0e's write step, which names no decoy. [2026-10-19 08:41 EDT]
3. ASK DESK: the "launcher script" cannot copy the transcript, because `desk-launch.sh` exits once the gate seat starts. Default taken: a new `ops/desk/x1-transcript.sh <worktree> <leg>`. The seat runs it after each agy leg under its existing `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`, with no new `--add-dir`. `scratch-clean.sh` removes each copy on `X1 RESULT: clean`. [2026-10-19 08:41 EDT]
4. ASK DESK: a fetch denial leaves no trace in the transcript (717 leg 0b: 0 `permission check failed`, every step `DONE`); it appears only as `soft-denying` in `cli.log`. Default taken: the script also writes `x1-<leg>.log`, holding `conversation <id>` and only the `soft-denying` lines. The rest of `cli.log` (76 lines match key/token/auth words) is never copied. The script refuses a stale `cli.log` whose conversation is already copied for an earlier leg. [2026-10-19 08:41 EDT]
5. ASK DESK: the old leg 0e combined the outside-cwd launch with the write outside. Default taken: leg 0e is now the write outside, run from the worktree. Leg 0f is the outside-cwd guard proof, which runs no agy. The legs are now 0a-0f, so the hub test parts and D1 say `0a to 0f`. [2026-10-19 08:41 EDT]
6. ASK DESK: a card has no heading line. Default taken: the title is line 1, `# Gemini build: X1 split, cwd pin, builder text`, with `JOB:` right below it. The header parsers grep `^KEY:` and stop at the first blank line, so they are not affected. [2026-10-19 08:41 EDT]

## RECORDS
- 08:30 EDT `date` at start; 08:40:43 card RECORDS; 08:41:46 report. The desk's rows R2010-R2011 (08:56, 09:00 ET) are stamped ahead of this machine's `date`.
- Read: prompt 832; `areas/cobalt.md`; `writing-rules.md`; card 827 (working tree, which holds amend 829 uncommitted: `git diff --stat main` 19+/5−); my reports `draft-gemini-read-grant-2026-10-19.md` and `…-amend-2026-10-19.md`; `cto-2026-10-19.md` R2005-R2011; `grep -n "671" cto-2026-10-17.md` → `:31` R1804, quoted in the card.
- `rev-parse main` → `0c79bbae`. `git diff --stat 6f2a4651 main` on `ops/`, `tests/`, `SHADOW-HUB.md`, `CHECK-HUB.md`, `prompts/2026-10-18/` → only card 790. `git diff --stat main` on those code files → nothing.
- `git show main:` `ops/desk/bare-guard.py` (`:60-61`, `:87-88`, `:119-122`, `:713-722`, `:788-824`, `:1085-1135`, `:1180-1218`), `ops/desk/desk-launch.sh` (`:431-444`, `:2573-2589`, `:2665-2695`), `ops/desk/scratch-clean.sh`, `ops/desk/authorize.sh`, `SHADOW-HUB.md` (`:10`, `:12`, `:28`, `:30`, `:42`, `:49`, `:59`), `tests/ops/test_bare_guard.py` (fixtures, `:2215-2553`, 2553 lines), `tests/ops/test_desk_launch_shadow.py` (690 lines), `tests/ops/test_shadow_hub_file.py` (429 lines), the test list of `tests/ops/test_scratch_clean.py`.
- `~/.claude/settings.json:22`: the hook runs `/Users/cobalt/cobalt/ops/desk/bare-guard.py`.
- agy, read with `ls`/`grep -c`/`grep -o` only: `cli.log -> log/cli-20261019_080949.log`; `:165` is its one `Created conversation`; `brain/9209175d…/logs/transcript.jsonl` is 13,935 bytes; `X1_CANARY` there is `X1_CANARY=not-a-secret` ×2; `permission check failed` count 0; `cli.log` `soft-denying` count 1. Neither the settings file nor any decoy was read. No secret was printed.
- Card `wc -c` 38,369 → 32,720 (smaller).
- Nothing committed or launched. Only card 827 and this report were written.

DRAFTED · decisions: 6
