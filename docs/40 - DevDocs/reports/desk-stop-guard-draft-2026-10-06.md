# Desk stop-guard draft 2026-10-06

## §0 Headline
- Card `prompts/2026-10-06/66-desk-stop-guard-card.md` written: six rows G1-G6 on `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` and one wake-up line; `DB: none`; RESTARTS expected none.
- Seat = cwd under `/Users/cobalt/cobalt` and first message `Read '…/CTO-DESK-WAKEUP.md'` (bare-guard's own rule); every other repo seat stays unguarded, pinned by negative controls.
- Count across stops in `<transcript_path>.desk-stop`, reset by `stop_hook_active` false; 3 blocks, the 4th stop ends the turn and logs `GAVE UP` to `.job-state/DESK-STOP`.
- No settings change; the contract line is already at `cto-desk-contract.md:25`; the checklist line L20 and today's OWED block are the desk's.
- 8 decisions, each with a default the card already follows.

## CARD
- JOB: desk-stop-guard · LADDER: OFF-LADDER — reports/cto-2026-10-06-words.md 2026-10-06 R590 · BRANCH: ops/desk-stop-guard-1006 · WORKTREE: desk-stop-guard-1006
- BASE: the one fill token (main HEAD at launch, 8 hex) · TIP, CHECK REPORT, HOUSE B empty · DB: none · RULINGS: 2026-10-06 R590
- REPORT: /Users/cobalt/cobalt-wt/desk-stop-guard-1006/docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md
- Rows: G1 seat · G2 OWED block and report path · G3 live check (`desk-list.sh` beside the hook; `pgrep -l -f`) · G4 block sentence and count · G5 fail open · G6 header comment and the wake-up line.

## DECISIONS
1. ASK DESK: the order says both "an unreadable report blocks" and "an unreadable file fails open". Default: an ABSENT report (or no block in it) blocks; a report that exists but cannot be read fails open. Alternative: both block. [19:39]
2. ASK DESK: where the count lives. Default: `<transcript_path>.desk-stop` (the path is in every Stop event, proven by `stop-guard.py:125`). Alternative: `$CLAUDE_JOB_DIR/tmp`, not proven to reach the hook's environment. [19:39]
3. ASK DESK: where the give-up line goes, so the desk can read it. Default: append to `/Users/cobalt/cobalt-wt/.job-state/DESK-STOP` (beside WAKE; the watches read only `IDLE` lines of WAKE, `wait-stop-line.sh:51`). Alternative: a WAKE line, or stderr only (not seen by the model). [19:39]
4. ASK DESK: which `desk-list.sh`. Default: the tracked `ops/desk/desk-list.sh` beside the hook (stageable in tests; skips id-less rows). Alternative: `/Users/cobalt/.claude/ops/desk-list.sh`, the untracked older copy the prompt names (not a symlink; same row shape). [19:39]
5. ASK DESK: a `desk-watch.sh` process carries the card, not the report, in its arguments (`desk-watch.sh:2`). Default: `live: watch <path>` names the path the watch was given (report for `wait-stop-line.sh`, card for `desk-watch.sh`). Alternative: the hook reads each card to derive its report (more code; a path with spaces cannot be cut from `pgrep` output reliably). [19:39]
6. ASK DESK: is `pgrep` a new command under R411/R412? Default: no — it runs inside the hook, on no seat's allow line, and is already the desk's VIEW liveness verb (`CTO-DESK-WAKEUP.md:14`). Alternative: no watch check; `live: watch` items then block. [19:39]
7. ASK DESK: the sentence for a missing or misplaced block. Default: `start it: the OWED block under ## §5 CURRENT of <report path>`. Alternative: a different fixed text. [19:39]
8. ASK DESK: who writes the wake-up line. Default: the build (row G6 b), landing on `main` with the deploy. Alternative: the desk writes it on `main` at the deploy; G6 b dropped. [19:39]

## RECORDS
All at main HEAD `d2f651ce` (`git -C /Users/cobalt/cobalt rev-parse HEAD`, 19:39 EDT `date`), by Read unless named.
- `reports/cto-2026-10-06-words.md:21-22` R590 his order.
- `ops/desk/stop-guard.py` whole (138 lines): `:2-13` header, `:19-31` INSTALL, `:37` WT_ROOT, `:40-53` STOP / SENTENCE, `:57-62` worktree, `:65-83` first_user_text, `:100-109` report_last_line, `:113-118` JSON, `:119-120` stop_hook_active, `:121-123` cwd exit, `:124-134` worker path.
- `ops/desk/idle-wake.py` whole: `:22-29` loads stop-guard, `:39-42` uses worktree / report_last_line.
- `tests/ops/test_stop_guard.py` whole: `:23-30` stage, `:33-76` World, `:101-108` repo-cwd exemption, `:233-242` I1, `:245-251` writes nothing. `tests/ops/test_idle_wake.py` whole: `:25-27` stages stop-guard. Found by `grep -rln` on `tests/ops`.
- `ops/desk/bare-guard.py:656-657` under, `:667-695` first_message, `:723-745` seat (desk rule `:736`); constants `:47-48`, HUBS `:73` (`grep -n`).
- `ops/desk/desk-list.sh` whole (`:2-3`, `:16` row shape); `/Users/cobalt/.claude/ops/desk-list.sh` whole (untracked copy; `ls -la /Users/cobalt/.claude/ops` shows it is not a symlink, the others are).
- `ops/desk/wait-stop-line.sh` whole (`:2` args, `:22-23` desk-list beside, `:51` WAKE IDLE filter); `ops/desk/desk-watch.sh` whole (`grep -n ""`; `:2` card argument).
- `prompts/CARD.md` whole; `prompts/CTO-DESK-WAKEUP.md` whole (`:14` pgrep, `:15` LIST, `:40` EVERY TURN, `:42` ON TRIGGER); `grep -rn CTO-DESK-WAKEUP ops/desk`.
- `reports/cto-2026-10-06.md` `## §5 CURRENT` `:124-129` (session table, no OWED block; `grep -n "^## "`).
- `src/cobalt/jobs/restarts.py:222-247` (`:225-228` DOCS, `:230-232` operator script, `:245-246` tests); `:38` prefix (`grep -n`).
- `Memory/topics/cto-desk-checklist.md` whole (`:40` L11 after midnight, `:27-48` `## launch`); `Memory/topics/cto-desk-contract.md` (`grep -n`; `:25` R590 rule already present); `Memory/topics/writing-rules.md` whole.
- `prompts/2026-10-06/62-draft-launcher-next-flow.md` and `63-launcher-next-flow-card.md` whole (card shape precedent).
- Card check: `grep -n "FILL\|^## "` on the card shows the one fill token at `:5` and headings ROWS, NOT IN THIS JOB, READ, CHECK ASKS, RECORDS.

DESK STOP GUARD CARD DRAFTED · decisions: 8
