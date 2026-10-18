# draft-751-fix-round — 2026-10-18

## §0 Headline
- Row `F1` added to card 751 (`prompts/2026-10-18/751-checkin-install-card.md`, after R1) plus one `## RECORDS` bullet; nothing else on the card changed (BASE, TIP, CHECK REPORT, HOUSE B untouched).
- Option (a): `checkin-timer.sh` step 4 judges by age, never by state. Every `checkin-ping` row older than 30 min is closed with `desk-done.sh <id> --replaced`, then the launch. Only a row under 30 min defers, naming its id.
- Both strict xfails settled by name: O1 passes and loses its mark; A1 is restated at the timer (close recorded before launch) and loses its mark.
- Snag: `desk-list.sh` prints no start time, so the row reads `claude agents --json` `startedAt`. The builder first checks the key exists (3 decisions below).
- Nothing committed, nothing launched.

## DECISIONS
- ASK DESK: the row cites the ruling as "L79 (a)" because the brain's R-number for it is not in my files. Which `R<n>` goes on O1/A1's SETTLED? Default: `L79` stays. [09:11 ET]
- ASK DESK: a ping row with no numeric `startedAt`, or an unreadable `claude agents --json`, counts as stale (closed, then replaced), so a bad read can never defer forever. The cost is closing a live ping under 30 min old, which is harmless (one turn). Default: stale. [09:11 ET]
- ASK DESK: A1's test asserts a cleanup on the launcher's kind `prompt`, which (a) leaves unchanged, so it cannot pass as written. The row restates it, same name, at the timer (`<id> --replaced` before `prompt <PING>`). Default: restated and the mark removed; the other path is CARRIED with the xfail kept for a launcher fix. [09:11 ET]

## RECORDS
- Clock: `date` → Sun Oct 18 09:08:20 EDT 2026 (start); 09:09:48 EDT (reads done); 09:11 EDT (report).
- Read: prompt 773; `areas/cobalt.md`; the card 751 whole; check report whole; precedent `771-draft-503-fix-round.md`.
- Branch tip `3108359f`: `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/checkin-install-1018` → `3108359f`; `git -C /Users/cobalt/cobalt-wt/checkin-install-1018 rev-parse --short=8 HEAD` → `3108359f`; `git status --short ops/desk tests/ops` there → nothing. Lines proved from that worktree plus `git show ops/checkin-install-1018:<file>` for `checkin-timer.sh`, `desk-launch.sh`, `desk-done.sh`, `test_checkin_install_1018.py`:
  - `ops/desk/checkin-timer.sh:44-48` (roots, `LAUNCH`, `PING`), `:111-127` (step 4: loop `:113-123`, `break` `:120`, DEFERRED `:124-127`), `:23-24` (header text of steps 4, 5, as listed at the tip).
  - `ops/desk/desk-launch.sh:749` (`run_launch` for kind `prompt`), `:2364-2397` (replacement block), `:2385` (busy test: `idle` and not `working`), `:2388` (`desk-done.sh "$rid" --replaced`), `:2393-2395` (KEPT or non-zero → refuse).
  - `ops/desk/desk-done.sh:3` (usage `--replaced`), `:16-17` (no-report form text); refuses `brain*` and `cto-desk` only, so `checkin-ping` closes.
  - `ops/cto-desk.sh:189` (row fields incl. `startedAt`), `:226-229` (epoch milliseconds, CLI 2.1.276, 2026-09-18).
  - `tests/ops/test_checkin_install_1018.py:183-191`, `:193-203`, `:205-227`.
  - `/Users/cobalt/.claude/ops/desk-list.sh:16` (installed copy: prints id, name, cwd, status, state; no start time).
- UNPROVEN today: that the installed CLI's `claude agents --json` still carries `startedAt` (last seen 2026-09-18, 2.1.276). I ran no `claude` command (not allowed here). The row makes the builder quote the key list first and stop with `ASK DESK: startedAt absent` if it is gone.
- Not changed: T1 to S1 rows, NOT IN THIS JOB, DEPLOY PROOF, the header lines. The row says it replaces T1 (4)'s text; T1's own cell is left as built.

DRAFTED · decisions: 3
