# aset orphan on bootout · brain brief for the drafter · 2026-10-10

Desk R771, R851/R853/R855. Defect class R685: survey done by the brain (code read below), so the card goes straight to fix, deploy, then "please check". Nothing is asked of him, except the one item marked HIS.

## §0 The cause (code read, re-proved by the drafter at BASE)
- `ops/com.cobalt.aset.plist:29-30`: `AbandonProcessGroup` = `true`.
- `ops/start_aset.sh:73`: `exec uv run python -m cobalt.aset`. launchd's pid is `uv`, and `python` is uv's child.
- On `launchctl bootout` (DEPLOY-HUB 4.2 and STEP-5), launchd signals the job's pid. Because the group is abandoned, it leaves the rest of the group alone, so `python` survives with ppid 1. It keeps the voice scratch lock (`COBALT_VOICE_SCRATCH_DIR`, `start_aset.sh:35`), and every KeepAlive restart fails on that lock. Seen 10-10: orphan pid 39280 after the https attempt-2 rollback, aset DOWN (https 502).
- DEPLOY-HUB 4.2 checks only `launchctl print … Could not find service`, never the process. The hub cannot see an orphan.

## ROWS (text for the drafter; the drafter proves every citation at BASE, next-flow change 4)
| Row | What | Proof | Files |
|---|---|---|---|
| A | aset stops as a whole group. Pick ONE and state why: (i) remove `AbandonProcessGroup` from `com.cobalt.aset.plist` (default false: launchd signals the whole group on bootout), or (ii) `start_aset.sh` execs the venv python directly (`exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset`), so launchd's pid IS python. (ii) keeps the plist's posture but drops `uv run`'s sync, so say how the venv stays current (the deploy's uv sync). Read the plist comment's reason for `AbandonProcessGroup` before removing it | A test reads the plist and the start script: under (i) no `AbandonProcessGroup` true, under (ii) the last line `exec …/.venv/bin/python -m cobalt.aset`. RED on BASE. Live proof is the next deploy's 4.2 (see C) | `ops/com.cobalt.aset.plist` or `ops/start_aset.sh`, plus a test under `tests/ops/` |
| B | AUDIT every `ops/com.cobalt.*.plist` and its start script for the same pair (`AbandonProcessGroup` true plus a `uv run` child, or any wrapper that does not exec the final process). Resident jobs (KeepAlive) get the row A fix. One-shot jobs are listed with a finding; fix them only when a lock or port makes an orphan harmful | The audit table in the build report, one line per plist; the same test parametrized over the residents (radar first) | the residents' plists or start scripts found |
| C | HIS, NOT IN THIS CARD until he says yes: DEPLOY-HUB 4.2 and STEP-5 would add `pgrep -f "python -m cobalt.<label>"` → no output after each bootout, else stop. That is a new string on the hub line (L9). The card RECORDS it as owed on his word and does not edit DEPLOY-HUB | — | — |

The card adds no new command for any seat (R411). RESTARTS: `com.cobalt.aset` (plus each resident row B changes). The plist change takes effect on the deploy's own bootout and bootstrap (the deploy hub bootstraps from `ops/com.cobalt.aset.plist`). Note: THAT deploy's own bootout still runs under the OLD plist, so the deploy hub must find no orphan after 4.2 before 4.3. Until C is approved, the card's DEPLOY PROOF carries a smoke read by the existing `ps -p <old aset pid>` (on the hub line) → header only.

## MODEL AND ORDER
- Drafter: Opus 5.5 (judgment: (i) or (ii), and the audit), not a precedent copy. Then the Sonnet preflight, an Opus 5.5 build, the check, and the deploy (L43, any hour).
- BEFORE it: aset must be UP. If the orphan is still alive, his plain-sentence kill order (brain message R851) comes first. This card does not fix a live outage.
- AFTER it, each only on his recorded one-line yes: `ops/desk/orphan-clean.sh` (a card; it widens R39's script class), then the `ops-hand` default-mode seat (a new permission class, an L63 exception), then row C. They do not wait on each other beyond his yes, but each is its own card.

FOR THE CHECK: aset-orphan brain 10-10 — AbandonProcessGroup true (plist:29) plus exec uv run (start_aset.sh:73) orphans python on bootout; fix one of (i)/(ii) with a RED file test; audit all resident plists; the pgrep hub row is his (L9), recorded not built; the deploy's own 4.2 proves no orphan via ps -p of the old pid.
