## §0 Headline
- Card written: `prompts/2026-10-10/317-held-closed-card.md`, rows H1 (`deploy-card.sh`), H2 (`desk-launch.sh`), H3 (`deploy-step0.sh`), H4 (`DEPLOY-HUB.md:59`, `CARD.md:48`); tests in the existing suites.
- One rule read the same way by three scripts; n = 0 pinned unchanged in each row.
- `desk-launch.sh` is a symlink into the repo file: the builder edits `ops/desk/desk-launch.sh`; the edit reaches the installed path when main carries it.
- H3 widens the brain's file list: `deploy-step0.sh:340` would refuse the row H1 writes.

## DECISIONS
1. DECISION 1 — H3 added (`deploy-step0.sh`, `test_deploy_step0.py`), beyond R993's list. Default: in. Without it the deploy hub's P2 fails every held row. The brain may drop it only by also dropping H1's deploy path.
2. DECISION 2 — a held row's `its stop line must carry` cell holds the check line's own literals, `held unfixed: <n>` and `ready: NO`, not the clean pair. Default: own literals. A cell saying `held unfixed: 0` over a check line `held unfixed: 1` stays refused as today.
3. DECISION 3 — held ids = the `## RUNS` rows `- <id> · … HELD, NOT FIXED`; their count must equal n. Default: this extraction. D2 of the 298 check (same defect, under `## DECISIONS`) is no id.
4. DECISION 4 — test checks are static at the code tip: file and `def <name>(` exist, no `xfail` in the decorators directly above or in a `pytestmark` line. Default: static; the check and the gate run the test.
5. DECISION 5 — the held path also requires `open: <n>` equal to n and `ready: NO`, so a `ready: NO` caused by a red suite or a WIDENED path is not read as satisfied. Default: in; beyond R993's text, tightening only.
6. DECISION 6 — two FIXED lines for one id, or one for an unlisted id, are refused. Default: refused ("one line" in R993).

## RECORDS
- `ls -la /Users/cobalt/.claude/ops/desk-launch.sh` → symlink to `/Users/cobalt/cobalt/ops/desk/desk-launch.sh` (21:36 ET); `~/.claude/ops/` also links `deploy-card.sh`, `deploy-step0.sh`.
- `git -C /Users/cobalt/cobalt log --oneline -1` → `26327808` (BASE). `git diff --stat HEAD -- ops tests CARD.md DEPLOY-HUB.md <298 check>` → nothing, so every line cite in the card is HEAD's.
- Cites proven: `deploy-card.sh:172-173,179-195,201`; `desk-launch.sh:907-987,947-954,959-972,973-974`; `deploy-step0.sh:337-340,368-376,389-405`; `DEPLOY-HUB.md:59`; `CARD.md:48`; check report 298 `## RUNS` line 69, last line `held unfixed: 1 · open: 1 · ready: NO`.
- Test suites: `tests/ops/test_deploy_card.py` (grep `deploy-card`), `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py` (grep `desk-launch`); no test pins the two hub sentences' lines (`test_hub_lines.py` holds no P2 pin).
- Precedent: `244-launcher-card.md` (the launcher card of the day; 243 is its draft prompt) changed `deploy-card.sh` only; `231-ops-hand-card.md` is the card that edits `desk-launch.sh` in a `files` cell. No other route exists or was invented.
- No line cite into `cto-2026-10-10.md`; rows by id (R993). Nothing launched, committed or run.

HELD CLOSED CARD DRAFTED · decisions: 6
