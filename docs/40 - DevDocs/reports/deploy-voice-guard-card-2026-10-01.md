## §0 Headline
Deploy card for the set `voiceguard` written: `prompts/2026-10-01/10-deploy-voice-guard-card.md`.
Two ships: `ops/voice-peers-1001` (head `76f7f7d5`), then `ops/desk-size-guard-1001` (head `ee667f3c`). No migration. Restart set expected `com.cobalt.aset com.cobalt.radar`.
Both checks end `held unfixed: 0` and `ready: YES`; `RULINGS: none`. Window: overnight idle, 01:58 ET at the last `date`; the outage must begin before 04:00 ET.

## DECISIONS
1. `UNPROVEN — needs a commit of the card and of the two check reports.` Whether `voice-peers-check-2026-10-01.md` and `desk-size-guard-check-2026-10-01.md` are committed and clean (hub P2) was not read; the desk commits them with the card or the hub refuses with `FAILED PREFLIGHT P2` (as attempt 1 of the 09-30 deploy did). Default: none taken.
2. `UNPROVEN — needs the hub's STEP-R.` The restart set `com.cobalt.aset com.cobalt.radar` is the union of the two checks' stop lines, not a derivation. Default: the card records it as expected; the hub derives its own.
3. `UNPROVEN — needs the hub's STEP-T.` The two branches share no file by `git log`; a merge conflict is decided by the merge, not by this card. Default: none.
4. The open item of the desk-size-guard check (O1 / H1 / B1, the `OPS_TOOLS` edit outside the build fence) is not a held defect and carries no ruling. The check's own line says `held unfixed: 0`, `for Dejan: 0`. Default: ship under the desk's L42 and R127 answer. Not for Dejan.
5. The `07` build also edits `OPS_TOOLS`. It conflicts with `02` at its own merge, after this deploy. Default: owed to the `07` card, not this one.
6. `UNPROVEN — needs the hub's G (c)–(e).` The smoke reads are greps of the landed tree; the `--guard` count in `ops/desk/desk-context.sh` and the `desk-launch.sh` count were not read on the branch's file by this drafter (`desk-launch.sh` shows `3` occurrences in the branch copy; the card asks for 1 or more). Default: the card says "1 or more".

For Dejan: none.

## RECORDS
Read at 01:58 ET Friday 2026-10-02 unless noted.
- `Read` of `prompts/2026-10-01/09-draft-deploy-voice-guard.md`, `areas/cobalt.md`, `prompts/CARD.md`, `prompts/DEPLOY-HUB.md` (whole), `prompts/2026-09-30/67-deploy-f15-e1-card.md`, `topics/writing-rules.md`.
- `date` → `Fri Oct 2 01:58:00 EDT 2026`.
- `ls -d /Users/cobalt/cobalt-wt/deploy-1001-1` → No such file or directory.
- `git -C /Users/cobalt/cobalt log -1 --format=%h ops/voice-peers-1001` → `76f7f7d5`; `ops/desk-size-guard-1001` → `ee667f3c`.
- `tail -n 3` of each check report → stop lines carry `held unfixed: 0` and `ready: YES`, tips `76f7f7d5` and `ee667f3c`; `RESTARTS: com.cobalt.aset` and `RESTARTS: com.cobalt.radar`.
- `git log --oneline main..<branch> -- src/cobalt/db_migrations` → empty, both.
- `git log --oneline --stat main..<branch> -- . ":(exclude)docs"` → paths as the card's `## RECORDS`.
- `git log --oneline <branch>..main -- . ":(exclude)docs"` → `d13cc261`, `01bfe67f`, both.
- `git show --stat 76f7f7d5` → `docs/40 - DevDocs/cobalt/voice/web.md` alone.
- `git rev-parse --verify --quiet` of `refs/tags/deploy-2026-10-01-1`, `refs/tags/pre-voice-guard-1001`, `refs/heads/deploy/voice-guard-1001` → exit 1 each; `ls` of the report path → No such file.
- Markers on `main`: `grep -c -F "100.82.85.27" …/configs/cobalt/voice.yaml` → `0`; `grep -c -F -e "--guard" …/ops/desk/wait-stop-line.sh` → `0`; `grep -c -F "ops/desk/desk-launch.sh" …/src/cobalt/jobs/restarts.py` → `0`; `ls …/tests/ops/test_desk_size_guard.py` → No such file. After values: `1` and `2` counted by eye from `git show` of the branch files (`voice.yaml` one list line; `wait-stop-line.sh` a comment line and the `sh` line); `1` for `restarts.py` from its `OPS_TOOLS` literal.
- `grep -n -F "migrations applied" …/deploy-2026-09-30-4b.md` → `migrations applied: all (0022)`; stop line `migrations: 0022`.
- Files written: the card and this report. No commit, no launch.

DEPLOY CARD DRAFTED · set: voiceguard · ships: 2 · migrations: none · decisions: 6 · for Dejan: 0
