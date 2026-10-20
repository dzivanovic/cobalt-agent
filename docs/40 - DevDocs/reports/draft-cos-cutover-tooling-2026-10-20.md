# draft-cos-cutover-tooling · 2026-10-20

## §0 Headline
- Card `prompts/2026-10-20/931-cos-cutover-tooling-card.md` drafted: K5, BAND HIGH, BASE `bd7bc0c9`, rows T2, T1a, T1b, T1c, R5; uncommitted.
- T1: one retirement record (form is the builder's: candidates (a) `data/deploy/retired.json`, (b) a tracked `ops/desk/` file, (c) `jobs.yaml` agent `enabled: false`). With no record, behavior is byte for byte BASE.
- T2: `desk-launch.sh deploy` admits card 929's form. Today it is refused at `:2161` (no `## SHIPS`), and the real 929 earlier at `:1286` (FILL tokens). Every other refusal is a parametrized control.
- Found: `deploy-outage.sh:429-437` reads the agent ONLINE on every outage, so after the retirement every outage would fail. The hub's restart set would also kickstart a retired agent on a `pyproject.toml` change (`jobs.yaml:157-158`).
- The launch blocks on ASK DESK 2: the RULINGS value the prompt gave is refused by `desk-launch.sh:1328-1331`.

## DECISIONS
1. ASK DESK: T1c goes beyond the brain's P8 `:65` and D1 `:123` into GATE `:93` (agent out of `<restart set>` when retired), smoke (a) `:150` and STEP-5 (3) `:169`. Without these, a retired agent is restarted or read red. [17:49] Default: in (ASK DESK 1 in the card).
2. ASK DESK: `RULINGS: 2026-10-20 brain 9b07db5a (L79)` is written as the prompt says. `desk-launch.sh:1328-1331` refuses any value not starting `<date> R<n>`, and `authorize.sh` proves R rows. Before the build launch, the desk replaces it with the R row that records the brain's ruling. [17:49] Default: written as given; the launch stays blocked until the desk replaces it.
3. ASK DESK: a retired agent found ONLINE (P8, D1, and the outage's pre-check and final read) fails loud, because it would mean two listeners. [17:49] Default: fail.
4. ASK DESK: on a bootstrap-only card the hub launch line fills `<worktree>`/`<branch>` with `none`, which produces the `.env` cp/rm strings under `cobalt-wt/none`, a `merge` there, and `merge --ff-only none`. The hub never types them, and under R60 the line is not changed. [17:49] Default: keep (check X5 names them).
5. ASK DESK: `prompts/CARD.md` still calls `TIP`, `BRANCH` and `WORKTREE` deploy values "required" with no bootstrap-only form. [17:49] Default: no CARD.md edit in this card.
6. ASK DESK: `DEPLOY-HUB.md` has no explicit skip of P2, P3, P5, STEP-T, STEP-R and STEP-G for a bootstrap-only card; only card 929's RECORDS lists them. [17:49] Default: out of this card; card 929's preflight confirms the hub reading.
7. ASK DESK: the marker `com.cobalt.agent recorded retired` after `5` assumes item 1. If the desk strikes item 1, it is `2`. [17:49] Default: `5`.

## RECORDS
- 2026-10-20 17:43 EDT (`date`), start; 17:49 EDT, report. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `bd7bc0c9`.
- `git diff --stat main` over `ops/desk`, `DEPLOY-HUB.md`, `CARD.md`, `F20-FINAL-2026-10-11.md` and `tests/ops` printed nothing, so the working files equal `main`. Card 929 has an uncommitted amend and was read with `git show main:`.
- Reads (`git show main:`): `prompts/CARD.md`, `prompts/BUILD-HUB.md` (`:14` launch/allow line, `:16` the list and never-typed commands), `prompts/2026-10-19/869-hub-cos-restart-card.md`, `prompts/2026-10-19/885-deploy-hub-cos-restart-fr1-card.md`, `prompts/2026-10-14/546-deploy-freeze-card.md`, `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md`, `configs/cobalt/jobs.yaml`.
- Reads (files equal to `main`): `reports/cos-bootstrap-decisions-2026-10-20.md` whole; `areas/cobalt.md` `## What Cobalt is` and from `## Build rules` down; `ops/desk/desk-launch.sh` `:96-109`, `:1250-1399`, `:1690-1729`, `:1840-1929`, `:2120-2229`, `:2600-2781`, `check_paths` `:403-424`; `ops/desk/deploy-step0.sh` `:1-130`, `:860-907`; `ops/desk/deploy-outage.sh` whole; `ops/desk/deploy-step-c.sh` `:30-59`; `DEPLOY-HUB.md` `:55-68`, `:119-126`; `tests/ops/test_desk_launch_launchd.py` `:1-135`; `tests/ops/test_deploy_step0.py` `:1-30`; `topics/writing-rules.md`.
- Greps and lists: `com.cobalt.agent` over configs, `src/cobalt/jobs`, `ops/desk`, DEPLOY-HUB and STANDING-LIST; F20-FINAL agent and SEAM lines (`:119`, `:123`, `:155`, `:157`); tests pinning agent, RESIDENTS and launcher refusals; `restarts.py` homes (`:38`, `:225-228`, `:230-232`, `:245-246`); `cobalt.sh` status strings (`:84`, `:89`, `:92`); `INSTALL:` headers; `ls -la` of the three installed links (into the repo); test names in `test_deploy_outage.py` and `test_deploy_step0.py`.
- `wc -l`: desk-launch 2782, deploy-step0 908, deploy-outage 443, DEPLOY-HUB 188, F20-FINAL 192.
- The prompt cites `deploy-outage.sh:428-435`; that block is `:429-437` at `main` (`:428` is the loop's `done`). Every other cited line was confirmed.
- The card holds no FILL token: `grep -n -F "«"` on the card printed nothing after the edit.
- Nothing was run but reads. No test was executed and nothing was committed.

DRAFTED · decisions: 7
