# Draft report — K5 card 869 re-cut, `hub-cos-restart-1019` (2026-10-19)

## §0 Headline
Card 869 is re-cut in place to rows R1-R2 plus a stop. R3 now stops the run at STEP-R when cos is loaded: `FAILED: RESTARTS — com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60), they are asked of Dejan · rollback: not used`.
The card adds no cos `launchctl` allow string. `:11`, `desk-launch.sh`, `STANDING-LIST.md`, `test_deploy_smoke_string_1014.py` and `test_desk_launch_launchd.py` stay untouched.
CHECK ASKS X3 asks for the allow strings to be unchanged and records the wrong RECORDS line (`test_deploy_smoke_string_1014.py:76`). X4 carries smoke (e) (`probes.py:143`).
The header, BASE, JOB, BRANCH, RULINGS and BAND are unchanged. Nothing is committed.

## DECISIONS
- ASK DESK: MODEL `DEPLOY-HUB.md:3` says `NO launchctl on any label but com.cobalt.aset / com.cobalt.radar / com.cobalt.agent and the labels of <launchd set>`. R2's NOT LOADED line types `launchctl print gui/501/com.cobalt.cos`, which `"Bash(launchctl print gui/501/*)"` on `:11` allows but `:3`'s prose forbids. Default: `:3` stands, because the prompt bars any change beyond its own list. If the desk wants the conflict gone, it adds a print-only clause to `:3`. [15:55 EDT]
- ASK DESK: R3's one edit replaces the `Exit 0 → …` sentence of the line R2 inserts, so R2's cell stays byte for byte. The plist path stays in the new sentence, so R2's test assert still holds. Default: as drafted. [15:55 EDT]
- ASK DESK: R2 (b)'s D1 clause (`com.cobalt.cos` in `<restart set>` → `<cos pid>`) can no longer be reached, because a loaded cos stops at STEP-R. Default: it is kept, since R2 stays as is. [15:55 EDT]
- ASK DESK: the kept wip `7d05ffe0` holds the old R3 edits, including `test_desk_launch_launchd.py` and `test_hub_deferred_1018.py:105`. Default: the relaunched build works to the re-cut card from BASE `bcbf08f9` and drops those parts. [15:55 EDT]

## RECORDS
- 15:53 EDT from `date`. `main` = `5a182e4b`. Before the edit, `git diff --stat main --` showed the hub, `STANDING-LIST.md`, `test_deploy_smoke_string_1014.py`, `test_hub_deferred_1018.py`, `desk-launch.sh`, `probes.py`, `jobs.yaml` and the card unchanged from `main`. Line numbers were then read by content on those files.
- `git show main:docs/40 - DevDocs/prompts/DEPLOY-HUB.md` matched the card's cites by content: `:11` launch line, `:78`, `:93` GATE, `:94`, `:122` `<radar pid>`, `:139` 4.2, `:143` 4.6, `:144-145`, `:153` (e), `:154` (f).
- `git show main:tests/ops/test_deploy_smoke_string_1014.py`: `:18` `BASE = "7aa5d470"`, `:73` `test_s1_no_other_allow_or_deny_string_changes`, `:76` the allow-list assert, `:78`.
- Other cites: `STANDING-LIST.md:148` (aset / radar `kickstart -k` only); `test_hub_deferred_1018.py:17` `THREE`, `:105` `assert COS not in launch`; `desk-launch.sh:1918`; `configs/cobalt/jobs.yaml:206` label, `:214` `enabled: false`; `probes.py:143` `unknown — NOT PROBED, registry enabled: false`, `:164` `loop stamping`.
- Read the build stop `/Users/cobalt/cobalt-wt/hub-cos-restart-1019/docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md` (DECISION 1, `FAILED: E3`) and `reports/hub-cos-restart-preflight-2026-10-19.md:36` (smoke (e) NOTE).
- Card edits:
  - Scope: one existing test file, plus the allow-list sentence.
  - R3: the row is replaced. The new test is `test_c3_a_loaded_cos_still_refuses`. BASE now reads `3 failed, 1 passed`. The old R3 CONTROL `test_c2` and the pin changes are dropped.
  - NOT IN THIS JOB: the line list is narrowed, and the asked strings get their own line.
  - READ: `test_deploy_smoke_string_1014.py` replaces `test_desk_launch_launchd.py`.
  - CHECK ASKS: X2 widened, X3 and X4 replaced, X5 dropped.
  - DEPLOY PROOF: one line added, and the `kickstart -k` cos count reads `0` after.
  - RECORDS: the wrong line is corrected, and the re-cut and smoke (e) lines are added.
- Card size, `wc -c`: 17259 → 16643. `git diff --stat`: `14 insertions(+), 11 deletions(-)`.
- 15:55 EDT from `date`: report written. No commit, no launch.

DRAFTED · decisions: 4
