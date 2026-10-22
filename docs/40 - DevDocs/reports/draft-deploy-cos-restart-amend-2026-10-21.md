# draft-deploy-cos-restart-amend · 2026-10-21

## §0 Headline
- Card 1008 amended in place: new rows F3 (THE ONE RESUME (e) `:53` reads cos when it is in `<restart set>`) and F4 (STEP-5 stop line `:171` and rule F `:23` carry a cos field). Uncommitted.
- A cos outside the set reads and prints exactly as today, and a new CONTROL test pins that. No allow string is added; `## 3.` counts and `RESTARTS: none` are unchanged.
- `## DEPLOY PROOF` +3 `grep -c -F` reads (0 → 1). CHECK ASK X6 added. Decisions: 3.

## DECISIONS
1. FOR DESK: stop-line shape. `:171` keeps its backticked template byte for byte and adds a clause after it: `com.cobalt.cos` in `<restart set>` adds `— cos: <UP|DOWN>` after the aset field. Rule F `:23` keeps `aset: DOWN · radar: DOWN` and adds `, and \`cos: DOWN\` when \`com.cobalt.cos\` is in \`<restart set>\``. This is the only way to get "a cos-not-in-set run prints as today": a fixed `cos: not in the set` field would change every run. Field order follows the strings: aset, cos, radar.
2. FOR DESK: the resume's read order. (e) runs FIRST, before (b) reads `## RESTARTS`. F3 makes (e) take the set from the report's `## RESTARTS` with the Read tool (no new call). A hub that hung before STEP-R wrote the set took nothing down, so it does not read cos. X6 asks the checker to confirm this order.
3. FOR DESK: a new CONTROL. `test_c_a_cos_outside_the_set_reads_and_prints_as_today` is green on BASE and after. It pins today's (e) span, the `:171` template and the `:23` phrase, which is bound (4) as a test. ORDER now expects it to pass on BASE. Cut it if the desk wants F pins only.

## RECORDS
- 22:54 EDT start (`date`); 22:56 EDT end (`date`). `main` `6a23d651`; `git diff --stat 9e83bf2c main --` of the hub, list, `tests/ops`, `ops/desk` → empty.
- Read: prompt 1011; card 1008 whole; `reports/deploy-cos-restart-preflight-2026-10-21.md` (NOTE 3, NOTE 4); `reports/draft-deploy-cos-restart-2026-10-21.md`; `topics/writing-rules.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` to end; `git show main:` of `DEPLOY-HUB.md` (grep `aset|radar`, `:23`, `:53`, `:171`), `tests/ops/test_hub_agent_retired_1020.py` whole.
- `git grep` over `main` for pins on the three lines: `test_hub_agent_retired_1020.py:30` (kept), `test_desk_launch_recut.py:231`, `:345` (constructed lines, unaffected), `desk-launch.sh:2493` (matches `rollback: used` only). Older cards 40, 44, 45, 51, 787, 869, 931 name `:53` / `:171` as history only.
- `git grep -c -F` of the three new markers over `DEPLOY-HUB.md` at `main` → 0 each.
- Card edits: rows F3, F4; ORDER; `## NOT IN THIS JOB` hub line list; `## READ` (+23, 53); X6; `## DEPLOY PROOF` +3; `## RECORDS` +2 (the brain line verbatim and this read).
- Tools beyond the standing allow line: `cat` of prompt 1011 (first read). Nothing run beyond reads; no test executed; no git write; no `.env` touched.

DRAFTED · decisions: 3
