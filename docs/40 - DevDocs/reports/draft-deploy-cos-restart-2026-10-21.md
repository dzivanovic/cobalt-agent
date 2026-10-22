# draft-deploy-cos-restart · 2026-10-21

## §0 Headline
- Card written: `prompts/2026-10-21/1008-deploy-cos-restart-card.md` (K5 serving K4, BAND HIGH, BASE `9e83bf2c`). Uncommitted.
- F1 adds S1-S3 (cos bootout, bootstrap `ops/com.cobalt.cos.plist`, kickstart -k) to `DEPLOY-HUB.md:11`, each after its aset twin, and to `STANDING-LIST.md` `:23`, `:146-148`.
- F2: STEP-R is hub text, not a script (`DEPLOY-HUB.md:94`). The strings alone admit nothing; F2 rewrites `:94` and names cos at `:3`, `:78`, 4.2 `:140`, 4.6 `:144`, smoke (a) `:150`.
- P1 changes four existing pins that hold the old refusal. Decisions: 3.

## DECISIONS
1. FOR DESK — scope. The ruling names one change: three strings on the line. `:94` refuses any loaded cos whatever the line holds, and 4.2 / 4.6 / smoke (a) / the MODEL fence name aset and radar only. The card also edits those hub lines, using card 869's own R2 text for `:94`, and `STANDING-LIST.md`, the approved list R60 cites. Without them a loaded cos is still refused (F2 stays red). Default taken: include them. If the brain rules the line only, cut F2 and P1 (a)/(b); 994 then still fails at STEP-R.
2. FOR DESK — the line's home. The prompt places the line in `ops/desk/desk-launch.sh`. It lives at `DEPLOY-HUB.md:11`; `desk-launch.sh` copies it and holds no resident string (`:207-211`, `:2652-2667`). The card leaves `desk-launch.sh` unchanged. RESTARTS class: docs and tests only, so `RESTARTS: none`; the class of `desk-launch.sh` (operator script, `restarts.py:230-233`) is recorded but not touched.
3. FOR DESK — RULINGS. Set to `2026-10-18 R1863` per the prompt. The strings rest on `2026-10-20 R2240` (`cto-2026-10-20.md:43`, HIS RULING · APPROVED). Add R2240 if `authorize.sh` must prove the approval of the changed list (CHECK ASK X5).

## RECORDS
- 20:46 EDT start (`date`); 20:51 EDT end (`date`). `main` `9e83bf2c`.
- Read: prompt 1007; `prompts/CARD.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` to end; card 1000; `reports/deploy-x15-hitl-probe-port.md` whole; `git show main:` of `DEPLOY-HUB.md` (lines 1-30, 60-174), `STANDING-LIST.md` (grep `launchctl`, headings), `ops/desk/desk-launch.sh` (`:200-229`, `:1895-1929`, `:2640-2689`), card 929, card 869, `tests/ops/test_hub_cos_restart_1019.py`, `test_hub_deferred_1018.py`, `test_desk_launch_launchd.py`, `test_deploy_smoke_string_1014.py`; `git grep` over `test_hub_agent_retired_1020.py`, `deploy-outage.sh`, `deploy-step0.sh`, `src/cobalt/jobs/restarts.py`, `configs/cobalt/jobs.yaml`; `cto-2026-10-20.md:43`, `cto-2026-10-21.md:14-15`, `cto-2026-10-20-words.md` `## R2240`; `topics/cto-desk-checklist.md` K4/K5/K10, L7a; `topics/writing-rules.md`.
- Proven at `main`: `git grep -c -F` of S1, S2, S3 over `DEPLOY-HUB.md` and `STANDING-LIST.md` → 0 each; the refusal sentence → 1 (`DEPLOY-HUB.md`); `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → listed. Six cites corrected after a `git grep -n` re-read (test line numbers).
- `git log --oneline -i --grep="launch line"` / `--grep="allow"`: no earlier card added a resident string to `:11`; nearest precedent card 869 (fix `d59fac71`, 4 files).
- Tools beyond the standing allow line: `cat` (prompt 1007, `CARD.md`, card 1000, the 994 report) and `sed -n` (`areas/cobalt.md`) at the start, before the allow line was read; reads only. One call blocked by the bare-command hook (a pipe) and resent as `git grep`.
- Nothing run beyond reads; no test executed; no git write; nothing committed; no `.env` touched.

DRAFTED · decisions: 3
