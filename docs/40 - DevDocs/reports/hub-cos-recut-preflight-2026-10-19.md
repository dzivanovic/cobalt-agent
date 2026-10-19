# Preflight — card 869 `hub-cos-restart-1019` re-cut (rows 1-2), 2026-10-19, read-only

Card at `29250739`; `main` = `29250739`; BASE `bcbf08f9`.

## CHECKS
| # | command · output | OK/FAIL |
|---|---|---|
| 1 | `grep -n -o -E "launchctl bootout\|launchctl bootstrap\|kickstart\|allowedTools"` on the card → `allowedTools`: 0 hits. `kickstart`/`bootout`/`bootstrap` hits at lines 19 (STANDING-LIST `kickstart -k` row, stated unchanged), 24 (R2 test: line holds no `launchctl bootout/bootstrap/kickstart`), 25 (R3: "names no …", cos strings not added), 46 (X2 question on 4.6's `kickstart -k`), 53 (DEPLOY PROOF: `launchctl kickstart -k gui/501/com.cobalt.cos` before 0 · after 0), 64 (RECORDS, STANDING-LIST:148). No hit adds a string. | OK |
| 2a | loaded cos stops at STEP-R: R3 (line 25) replaces the `Exit 0 …` sentence with `FAILED: RESTARTS — com.cobalt.cos is loaded; … · rollback: not used`; pinned by `test_c3_a_loaded_cos_still_refuses`; DEPLOY PROOF line 52 counts it 0→1 | OK |
| 2b | not loaded: R2 (a) writes `com.cobalt.cos: not loaded — skipped`; `test_r1_…` and `test_r2_…` pin it; DEPLOY PROOF line 51 0→1 | OK |
| 2c | unknown label still refused: R1 keeps `Anything else (…)` byte for byte; `test_c1_a_label_outside_the_four_is_refused` (green on BASE) | OK |
| 2d | RED today: `git grep -n "^- GATE: exit 0" main -- DEPLOY-HUB.md` → `:93 … within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\` (one, two, all three, or none)`; `git grep -c com.cobalt.cos main -- DEPLOY-HUB.md` → 0; so the F16 set aset+cos+radar is refused at `:93` | OK |
| 3 | R1-R3 `files` cells: hub, `test_hub_cos_restart_1019.py`, `test_hub_deferred_1018.py` only. `test_deploy_smoke_string_1014.py`, `STANDING-LIST.md`, `ops/desk/desk-launch.sh` appear only in prose/NOT IN THIS JOB | OK |
| 4 | `git log -p -2 -- <card>`: `29250739` (re-cut) touches Scope, R3, NOT IN THIS JOB, READ, CHECK ASKS, DEPLOY PROOF, RECORDS only; header lines 1-15 not in its diff. `1c304215` changed only `RULINGS` to `2026-10-18 R1863`. Header now: BASE `bcbf08f9`, BRANCH `ops/hub-cos-restart-1019`, RULINGS `2026-10-18 R1863` | OK |
| 5 | `git show --stat 7d05ffe0`: parent `bcbf08f9`; 3 files (`test_desk_launch_launchd.py` 8, `test_hub_cos_restart_1019.py` +119, `test_hub_deferred_1018.py` 6) — the old R3 pins. `grep -c -E "7d05ffe0\|resum\|drop"` on the card → 2: line 28 (THE ONE RESUME, unrelated) and RECORDS line 64 (names the wip). The card does NOT say the build resumes from BASE `bcbf08f9` and drops the old R3 parts; only the drafter report (decision 4) does | FAIL |
| 6a | `main:DEPLOY-HUB.md:93` GATE span = three labels; `Anything else (…)` sentence present | OK |
| 6b | `:94` `THE SET DRIVES THE REST`; `:122` `<radar pid>` (D1); `:139` 4.2; `:149` (a); `:153` (e); `:154` (f) `RESTARTS:` minus `<deferred set>` (as `## RESTARTS` records it) | OK |
| 6c | `main:tests/ops/test_deploy_smoke_string_1014.py` → `:18 BASE = "7aa5d470"`, `:73` test name, `:76` allow-list assert, `:78` | OK |
| 6d | `main:tests/ops/test_hub_deferred_1018.py` → `:17 THREE`, `:57`, `:61 admits`, `:69`, `:74` (cos control), `:75`, `:96 == 5`, `:105 assert COS not in launch` | OK |
| 6e | `main:configs/cobalt/jobs.yaml` → `:206 label: com.cobalt.cos`, `:214 enabled: false` | OK |
| 6f | `main:src/cobalt/heartbeat/probes.py` → `:143 unknown — NOT PROBED`, `:164 loop stamping` | OK |
| 6g | `main:ops/desk/desk-launch.sh:1865 agent\|aset\|radar) refuse …`; `main:…/STANDING-LIST.md:148` aset/radar `kickstart -k` only | OK |
| 6h | `git diff --stat bcbf08f9 main -- DEPLOY-HUB.md tests/ops ops/desk` → empty (cites stable since BASE; BASE is an ancestor of `main`) | OK |
| 7 | CHECK ASKS X3 carries `test_deploy_smoke_string_1014.py:76` and the `FAILED: E3` stop; X4 carries `jobs.yaml:214` / `probes.py:143` `unknown — NOT PROBED` | OK |
| 8 | `git log -1 -- <card>` → `29250739 docs(desk): card 869 re-cut to rows 1-2, preflight 874 R2076`; `git diff HEAD --stat -- <card>` → empty | OK |

## ISSUES
- FAIL (5): the card does not state that the build resumes from BASE `bcbf08f9` and drops the old R3 parts of wip `7d05ffe0` (`test_desk_launch_launchd.py` edits, `test_hub_deferred_1018.py:105` change, old R3 tests). Only `draft-hub-cos-recut-2026-10-19.md` decision 4 says so. A builder reading the card alone could keep the wip. Fix: one line in the card (Scope or RECORDS).
- NOTE: R2 (b) adds a D1 `<cos pid>` clause that a loaded cos can never reach (R3 stops at STEP-R); harmless, drafter decision 3 keeps it.
- NOTE: MODEL `:3` still says no `launchctl` on any label but aset/radar/agent, while R2's line types `launchctl print gui/501/com.cobalt.cos` (allowed by `launchctl print gui/501/*`); drafter decision 1 leaves `:3` as is.
- NOTE: the working tree holds other uncommitted files; the card itself is clean.
- BLOCKS THE LAUNCH: the FAIL at check 5 only (a card edit, no code).

PREFLIGHT DONE · card: hub-cos-restart-1019 · checks: 17 · fails: 1 · ready: NO
