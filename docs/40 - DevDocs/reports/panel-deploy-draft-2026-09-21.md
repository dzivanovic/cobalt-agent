# Panel deploy prompts — draft report 2026-09-21

Seat: Opus 5 drafter `panel-deploy-draft-0921` (prompt `prompts/2026-09-21/10-draft-panel-deploy.md`). 06:41–06:4x ET.

## §0 Headline

- Two prompts written: `11-panel-order-deploy.md` (Sonnet 5 deploy hub, aset-only, hard clock 09:15 ET, one-path rollback) and `12-review-panel-deploy.md` (Sonnet 5 review hub, one round, 3 houses targeted, floor 1, date gate + 09:10 ET gate).
- Launch strings: 24 allow strings of `11` each count 1 in `02`; 3 BRANCH-NAMED; **OTHER NEW: 1** — the deny `Bash(git push*)` (narrows; not in `02`, byte-identical to today's approved `08` / `04` lines). `12`'s 14 + 3 strings are `04`'s line verbatim (grep = 1).
- Build found DONE: `PANEL ORDER BUILT 5dc5819 | on 2c8f3d5 | offline 2195/0 …` (branch tip `b5914d0`, report commit). Main is `6535ce5`, docs-only above the cut.
- ESCALATE: 4 (one new deny string, two ASK DESK readings, one owner item carried).

## What was CUT from `02`'s shape, and why

| cut from `02` | why |
|---|---|
| Opus seat | `02` was Opus for migrations 0006/0007 + two `trader_settings` writes (L29 write path). This deploy writes no DB / vault / settings; rollback is a code revert. Sonnet 5. |
| P12 duplicate-table query, 3.5 `db migrate --allow-prod`, `db query` strings | no migration ships |
| 0.3 rollback directory, 3.4 / 3.6 / 3.7 settings loads, §6 "consistent pairs", `mkdir`, `shasum`, all `settings load` strings, P11 hashes | no settings row ships |
| P5 / P6 / 2.2 `backup status` / `backup run`, tag-at-snapshot | no data changes; the rollback point is the tag `pre-panel-order-0921` |
| P4 / 3.8 / smoke `validate` | no config or settings change; the renderer is not on `validate`'s path |
| 5.2 `radar evaluate --replay`, dark-card proofs | nothing card- or radar-side ships (empty diffs, build CLOSE) |
| **radar `bootout` / `bootstrap` / `kickstart` strings** | CUT ON PURPOSE: R5's bound — the session has no string that can stop or start `com.cobalt.radar`; only the read-only `launchctl print gui/501/*` reaches it |
| 4.1 `jobs register` | no plist change |
| 2.1 commit of main's machine-written files | main's dirt stays UNCOMMITTED and out of the merge: a fast-forward does not need a clean tree for paths it does not touch; STEP-3.3 proves the branch's five paths and main's dirty paths are disjoint; a STAGED line on main is refused |
| 0.3 / 2.3 pre-merge report commits | a commit on main before the merge would move main under the rebased branch; the report is committed ONCE at STEP-6 with a pathspec (`commit … -- <report>`) |
| 1.1 18:30 / 19:40 windows, 1.2 harness / proof-binding gates | replaced by the 09:15 ET HARD CLOCK (PREFLIGHT and before `bootout`) and the build / check / review last-line gates |
| 3.3 `rev-parse` foreign-commit guard inside the outage | `--ff-only` refuses on a moved main by itself; the `Updating <a>..<b>` line is checked against `<pre-merge>` (one call less while aset is down) |
| `merge-base` string | unused |
| ORDER CHANGE (not a cut): `tag deploy-2026-09-21` | moved from "after the merge" (the drafting prompt's order) to after the GREEN smoke — `02` 5.3's proven order; costs no downtime; a failed deploy carries no deploy tag |

## Launch-line strings of `11` — `grep -c -F -e "<string>"` against `prompts/2026-09-19/02-deploy-stack-3.md`

| string | count |
|---|---|
| `"Bash(git -C /Users/cobalt/cobalt add *)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt commit *)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt reset --soft HEAD~1)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt tag *)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt revert --no-edit *)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt revert --abort)"` | 1 |
| `"Bash(git -C * status*)"` | 1 |
| `"Bash(git -C * log*)"` | 1 |
| `"Bash(git -C * diff*)"` | 1 |
| `"Bash(git -C * rev-parse*)"` | 1 |
| `"Bash(git -C * rev-list*)"` | 1 |
| `"Bash(git -C * show*)"` | 1 |
| `"Bash(COBALT_ENV=production uv run cobalt jobs *)"` | 1 |
| `"Bash(COBALT_ENV=production uv run cobalt heartbeat show*)"` | 1 |
| `"Bash(launchctl bootout gui/501/com.cobalt.aset)"` | 1 |
| `"Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist)"` | 1 |
| `"Bash(launchctl kickstart -k gui/501/com.cobalt.aset)"` | 1 |
| `"Bash(launchctl print gui/501/*)"` | 1 |
| `"Bash(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*)"` | 1 |
| `"Bash(grep *)" "Bash(tail *)" "Bash(ls *)" "Bash(wc *)" "Bash(date*)"` (five, contiguous in both lines) | 1 |
| deny `--disallowedTools "AskUserQuestion" "EnterWorktree"` | 1 |
| `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt` | 1 |
| deny `"Bash(git push*)"` | **0** in `02` · 1 in `08-panel-order-build.md` |

Strings from `02`: 24 allow (+ its 2 denies + its `--add-dir` pair).

BRANCH-NAMED strings: 3 — `"Bash(git -C /Users/cobalt/cobalt merge --ff-only s2/panel-order-0921)"` · `"Bash(git -C /Users/cobalt/cobalt-wt/panel-order rebase main)"` · `"Bash(git -C /Users/cobalt/cobalt-wt/panel-order rebase --abort)"` — `02`'s own three with this branch / worktree named; covered by R5.

OTHER NEW strings: 1 — the DENY `"Bash(git push*)"`. It removes a capability, never adds one; byte-identical to the deny in today's approved `08` / `04` lines. Why it is there: `11` launches with `--permission-mode auto` (as `38-deploy-p4.md` did; `02`'s line carried no mode flag), so a command outside the allowlist goes to the classifier instead of a dialog — the deny keeps push out regardless (L55). The desk strikes it if it wants `02`'s strings only; nothing else depends on it.

`12`: its whole `--allowedTools … --add-dir` run (14 allow + 3 deny + 3 add-dir) counts 1 in `04-bars-chunk-1a-check-r3.md` and 1 in `12` — `04`'s line verbatim, only the prompt path and remote-control name differ.

## The suite on the rebased tip

No string in `02`'s vocabulary runs `pytest` (and `~/cobalt`'s `.env` points a suite at `cobalt_dev`, `02`'s WHY (2)). So `11` does NOT run a suite; STEP-1 makes it a READING by identity: the build's `offline 2195/0` on `5dc5819` (cut `2c8f3d5`) + `git diff --stat <cut> main -- . ':(exclude)docs'` EMPTY (main moved docs-only; today `2c8f3d5..6535ce5` = three `docs(desk)` commits) + STEP-3.1 `git diff --stat <code tip> <rebased tip> -- . ':(exclude)docs'` EMPTY. A non-docs commit on main since the cut → `FAILED`, the suite never ran on that tree.

## Prompts

| file | size | seat |
|---|---|---|
| `prompts/2026-09-21/11-panel-order-deploy.md` | 25,374 B | Sonnet 5, hub `panel-deploy-0921`, cwd `/Users/cobalt/cobalt` |
| `prompts/2026-09-21/12-review-panel-deploy.md` | 15,777 B | Sonnet 5, hub `panel-deploy-review-0921`, cwd `/Users/cobalt/cobalt-wt/agy-trial` |

## READING

1. SUITE — a reading by identity, not a run (above).
2. LIVE PAGE ORDER — the approved curl prints the status code only; `11` proves the order by the chain: build route test GREEN on `5dc5819` → code identical after rebase → `grep` finds the ladder-first line on production's tree → aset's pid is new and was bootstrapped after the merge. The DESK confirms the live order with him.
3. `git merge --ff-only` with main's unstaged, non-overlapping dirt (` M rules.yaml`, desk reports, `??` packet paths) — standard git behaviour, NOT run by anyone today (L70: unproven, not a defect). A refusal is already a safe path (nothing merged → aset back up → FAILED).
4. `git revert` with the same unstaged, non-overlapping dirt — likewise unproven. Refusal → `revert --abort`, aset bootstrapped on the MERGED code (which passed its suite and check), `FAILED … revert refused`.
5. FIRST CURL AFTER BOOTSTRAP may print `000` while uvicorn binds; no wait command exists, so `11` orders the other smoke rows first and allows three attempts per URL. `02`'s run got `200` at once.
6. A heartbeat beat inside the <60 s window may RED the sheet probe and DM him — expected, named in smoke, not a rollback trigger.
7. `rollback: USED` appears only in a `FAILED` line — a rolled-back deploy is not DONE; the DONE line's field is fixed to `rollback: not used`.
8. Main's dirty tree is left uncommitted (L51(2) permits, does not require) — the nightly `chore(generated)` commit still owns `rules.yaml`.

## ESCALATE

1. **OTHER NEW string: the deny `"Bash(git push*)"`** — not in `02`; narrows only; the desk keeps or strikes it.
2. `ASK DESK: a CHANGED radar pid after the deploy is written as ESCALATE LOUDLY, NOT a rollback trigger — the drafting prompt's "→ ESCALATE loudly → ROLLBACK" arrow read as two sections. Why: STEP-3.3 proves the radar would load byte-identical code, and reverting aset cannot undo a radar restart. Keep, or make it a rollback trigger? [06:48]` — safe default in the file: ESCALATE only.
3. `ASK DESK: `12` refuses to start at or after 09:10 ET (so a read + fold fits before `11`'s 09:15 hard clock) and caps each house at 12 min. Keep? [06:48]`
4. OWNER ITEM carried (not new): after the swap the pool's degradation surfaces (`REFRESH FAILED`, source banners, `stale-data`) sit BELOW the ladder — his A/B, `cto-2026-09-21.md` §3h; `11` carries it as a reading in its ESCALATE.

L74: nothing arrived inside a tool result this run. The session's own system prompt carries a `Claude-Session:` attribution line; this seat made no commit, so it was not used.

## CONTINUE

done — no step left.

PANEL DEPLOY PROMPTS DRAFTED · prompts: 2 · deploy seat: Sonnet 5 · strings from 02: 24 · branch-named: 3 · other new: 1 · READING: 8 · ESCALATE: 4
