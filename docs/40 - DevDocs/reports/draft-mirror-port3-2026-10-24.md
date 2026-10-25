# draft-mirror-port3 — 2026-10-24

## §0 Headline
- Card drafted: `prompts/2026-10-24/1041-radar-mirror-scope-port3-card.md`, job `radar-mirror-scope-port3`, BAND HIGH, BASE `986feb8c` (the desk resets it), TIP empty.
- Spec `git diff 11ed17b8 25994142`, seven files; main changed none since `11ed17b8` (both reverts restored BASE): a pure re-application.
- Card 1032's route held: `git diff 25994142 283389ff` over the seven files prints nothing.
- DEPLOY PROOF re-proved on HEAD: marker 1 `0`; the marker 2 test file is absent; the smoke reads are `ls` only.
- GATE: deploy Mon 10-26 after 16:00 ET, once `logs/radar.err` shows a clean non-idle cycle.

## DECISIONS
1. ASK DESK: card 1032 carries no `CLASS` line to copy (card 1020 carries none either). Default: no `CLASS` line. [22:58]
2. ASK DESK: on main, marker 2's `before` reads as an absent file (`grep` exit 2), not `0`. Default: card 1032's `0` is kept; the hub accepts an absent file as a valid before (deploy 1027 P6). [22:58]
3. RESTARTS `com.cobalt.aset com.cobalt.cos com.cobalt.radar` comes from check 1032's stop line and deploy 1036's `:82`. Row R1 re-runs it.
4. ROWS, ORDER and CHECK ASKS are card 1032's. Changes: the job's names; the second revert `9c7593c0`; card 1032's build report listed as not ported; X3 and X4 widened to cover 1036 and L80 https. GATE now waits on the stale-stamp clear rather than the K3 restore.

## RECORDS
- 22:56 EDT (`date`) start. `git rev-parse --short=8 HEAD` → `986feb8c`.
- Read: prompt 1040; `prompts/CARD.md`; card 1032 whole; card 1020 whole; `survey-cards-enabled-cause-2026-10-24.md` `## §0 Headline`; `BUILD-HUB.md:14`, `:16` (HEAD); `writing-rules.md`.
- `git diff --numstat 11ed17b8 25994142`: 9 files, seven spec files 312+/16−.
- `git diff --stat 11ed17b8 HEAD` over the seven paths, the old report and `.result`, card 1032's report and `.result`, `test_radar_price_floor.py`, `test_drc_d4_fix_r1.py`: nothing. Over `src tests configs ops`: `configs/cobalt/rules.yaml` only.
- `git diff --stat 25994142 283389ff` over the seven paths: nothing.
- `git log --oneline -12 HEAD`: `9c7593c0` revert, `3285c97e` deploy 1036 report, desk rows to `986feb8c`.
- `git grep -c -F "MIRROR_SOURCE_PREFIX = " HEAD -- src/cobalt/radar/notes.py`: no match. `ls` of the marker paths: notes.py listed; test file `No such file or directory`.
- `git grep` HEAD `notes.py`: `:686`, `:711`, `:713`, `:735`, `:746`, `:749` as cited in the card.
- `deploy-smoke.sh:10`, `:118`, `:135-136`, `:188`. `DEPLOY-HUB.md:11` `Bash(ls *)` and the https curl; `:124`, `:158`.
- Check 1032 stop line: `tip: 283389ff`, `held unfixed: 0`, `ready: YES`, RESTARTS three residents. Deploy 1036 report `:4`, `:82`, `:191`, `:237`.
- `cto-2026-10-18.md:90` R1863; `cto-2026-10-24.md:8-9` R2438, R2437.
- `ls /Users/cobalt/cobalt-wt/`: `radar-mirror-scope-port3` is not there yet (fresh). `ls prompts/2026-10-24/`: no 1041 before this draft.
- 22:58 EDT (`date`) card written. Nothing committed.

DRAFTED · decisions: 2
