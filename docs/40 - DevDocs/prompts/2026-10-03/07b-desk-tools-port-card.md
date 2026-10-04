JOB: desk-tools-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/desk-tools-port-1003
WORKTREE: desk-tools-port-1003
BASE: 5ff16b1f
TIP:
REPORT: /Users/cobalt/cobalt-wt/desk-tools-port-1003/docs/40 - DevDocs/reports/desk-tools-port-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R154

## ROWS

WHY: cards `07` brain-hub (checked, with row B5) and `09` worker-watch (checked, with the O1/O6 fixes) conflict with the adoption chain in `ops/desk/desk-launch.sh` and the watch scripts. One PORT lands both on `03d`'s tip. `DB: none` (every file under `ops/`, `tests/ops/`, `docs/`).

| row | what | red first | files |
|---|---|---|---|
| P1 | `07`: every file of its checked diff from `git show <07 tip>:<path>`, hash-proven, except `ops/desk/desk-launch.sh`, settled by Edit so `03c`'s `recut` kind and `TREE STATE`-optional rule, and `07`'s `brain` kind and `prompt` refusal (B2, B5) all stand; the unknown-kind refusal text now lists `recut` and `brain` (the follow-up line lands here) | `07`'s tests (`test_desk_launch_brain.py`) red on `BASE`, green at the tip; `tests/ops` green | `07`'s files |
| P2 | `09`: every file of its checked diff from `git show <09 tip>:<path>`, hash-proven, except `ops/desk/desk-watch.sh` and `wait-stop-line.sh` where `03c`/`18` changed lines too — settled with both sides (the idle exit of `09`, the `03c` changes) | `09`'s tests red on `BASE`, green at the tip | `09`'s files |
| P3 | HIS INSTALL TEXT, in the report's `## RECORDS`: the `hooks` object for `~/.claude/settings.json` (his word, 10-03): PreToolUse/Bash → `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`; Stop → `python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py`; Notification matcher `idle_prompt` → `python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py`; valid JSON proved | RUN — quote it | none |

## NOT IN THIS JOB
- A line in neither parent except the unknown-kind list; `git merge` / `rebase`; the settings write (his).

## READ
- `prompts/2026-10-03/07-brain-hub-card.md`, `09-worker-watch-card.md` and their check reports' `## §0`; `ops/desk/desk-launch.sh` at `BASE`, at `07`'s tip and at `09`'s tip, side by side.

## CHECK ASKS
- X1 Hash pairs. X2 In `desk-launch.sh`: do `recut`, `brain`, `run`-less kinds list, the `prompt` refusal and the optional `TREE STATE` all work in one dry run each? X3 Does the stop hook still exempt `cwd` under `/Users/cobalt/cobalt`?

## RECORDS
- RESTARTS class homes (L7a): `ops/desk/*` → `OPS_DESK_PREFIX` (`restarts.py:38`); `tests/ops/*` → test/documentation (`:239`); `docs/**` → DOCS (`:219`); no `src/`, no `configs/`.
- Judge, 10-03 21:39 ET: set 3, Sunday after 13:00; his install follows set 3's DEPLOYED line. After `07` lands, the brain's handover launches by `desk-launch.sh brain` (the brain edits `00-brain-handover.md`'s line then).
