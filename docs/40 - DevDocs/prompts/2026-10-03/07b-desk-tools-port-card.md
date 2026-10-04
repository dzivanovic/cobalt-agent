JOB: desk-tools-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/desk-tools-port-1003
WORKTREE: desk-tools-port-1003
BASE: 5ff16b1f
TIP: 5c1d629f
REPORT: /Users/cobalt/cobalt-wt/desk-tools-port-1003/docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-port-check-2026-10-03.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R154

## ROWS

WHY: cards `07` brain-hub (checked, with row B5) and `09` worker-watch (checked, with the O1/O6 fixes) conflict with the adoption chain in `ops/desk/desk-launch.sh` and the watch scripts. One PORT lands both on `03d`'s tip. `DB: none` (every file under `ops/`, `tests/ops/`, `docs/`).

| row | what | red first | files |
|---|---|---|---|
| P1 | `07` (checked head `b5eb3530`, which carries the check's fixes; its range `a09f0862..b5eb3530`): every file from `git show b5eb3530:<path>`, hash-proven, except `ops/desk/desk-launch.sh`, settled by Edit so `03c`'s `recut` kind and `TREE STATE`-optional rule, and `07`'s `brain` kind and `prompt` refusal (B2, B5) all stand; the unknown-kind refusal text now lists `recut` and `brain` (the follow-up line lands here) | `07`'s tests (`test_desk_launch_brain.py`) red on `BASE`, green at the tip; `tests/ops` green | `07`'s files |
| P3 | SHARED WITH BASE, hand-merged with BOTH sides (quote the two one-sided diffs as `03d` P3 does): `docs/40 - DevDocs/prompts/STANDING-LIST.md` (`07`'s `## 7. BRAIN-HUB.md` and B4's two strings onto BASE's text) and `tests/ops/test_desk_size_guard.py` (`07`'s brain-prompt fixture change onto BASE's `desk-list.sh`-beside staging) | each file's tests green at the tip; ``grep -c -F "## 7. `BRAIN-HUB.md`"`` → 1 | the two files |
| P2 | `09` (checked head `a6bef8cb`, which carries the O1/O6 fixes; range `a09f0862..a6bef8cb`): every file from `git show a6bef8cb:<path>`, hash-proven, except `ops/desk/desk-watch.sh` and `wait-stop-line.sh` where `03c`/`18` changed lines too — settled with both sides (the idle exit of `09`, the `03c` changes) | `09`'s tests red on `BASE`, green at the tip | `09`'s files |
| P5 | BRAIN MODEL (his 10-04 ruling, brain session, after 13:00 ET): `BRAIN-HUB.md`'s line defaults to `--model claude-opus-5-5`; `desk-launch.sh brain <handover> --fable` puts `claude-fable-5-1` on the line instead, for a design or high-effort session the brain itself asks for; the hub's `## MEASURE` says: at 500,000 the brain MESSAGES `cto-desk` asking for its own replacement, naming the model for the next seat (Fable only while a design task is open, else Opus). The brain runs its MEASURE every ten answers, not only before long writes (his 10-04 ruling R191: "put it in code and make it for every turn"). `STANDING-LIST.md` §7 notes the two model words as the only variable | `tests/ops/test_desk_launch_brain.py`: the default dry line holds `claude-opus-5-5`; with `--fable`, `claude-fable-5-1`; any other value → REFUSED | `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `docs/40 - DevDocs/prompts/STANDING-LIST.md` |
| P4 | HIS INSTALL TEXT, in the report's `## RECORDS`: the `hooks` object for `~/.claude/settings.json` (his word, 10-03): PreToolUse/Bash → `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`; Stop → `python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py`; Notification matcher `idle_prompt` → `python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py`; valid JSON proved | RUN — quote it | none |

## NOT IN THIS JOB
- A line in neither parent except the unknown-kind list; `git merge` / `rebase`; the settings write (his).

## READ
- `prompts/2026-10-03/07-brain-hub-card.md`, `09-worker-watch-card.md` and their check reports' `## §0`; `ops/desk/desk-launch.sh` at `BASE`, at `07`'s tip and at `09`'s tip, side by side.

## CHECK ASKS
- X1 Hash pairs. X2 In `desk-launch.sh`: do `recut`, `brain`, `run`-less kinds list, the `prompt` refusal and the optional `TREE STATE` all work in one dry run each? X3 Does the stop hook still exempt `cwd` under `/Users/cobalt/cobalt`?

## RECORDS
- RESTARTS class homes (L7a, at BASE `5ff16b1f`): `ops/desk/*` → `OPS_DESK_PREFIX` (`restarts.py:38`); `tests/ops/*` → tests (`:246`); `docs/**` → DOCS (`:228`); no `src/`, no `configs/`.
- Preflight (desk, `07b-card-preflight-2026-10-03.md`): source heads named (`b5eb3530`, `a6bef8cb`); row P3 for the two shared paths; the cites corrected.
- Judge, 10-03 21:39 ET: set 3, Sunday after 13:00; his install follows set 3's DEPLOYED line. After `07` lands, the brain's handover launches by `desk-launch.sh brain` (the brain edits `00-brain-handover.md`'s line then).
