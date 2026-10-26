# Draft: F23 gate-run prompt — 2026-10-26

## §0 Headline
- Drafted `prompts/2026-10-26/1046-f23-gate-run.md`, seat `f23-gate-run`, CLASS K2, LADDER `S5-P2 · F23`, RULINGS `2026-10-18 R1863`, in 970's shape.
- Four pytest strings plus `date`, `grep`, `ls` and the `git` reads. No database command, no `launchctl`, no render.
- No item can read a plain `OK` today. E1 and E2 each have an offline leg plus a [HIS HAND] leg. E4 has no allowed command. E5 gated the code deploy, which is done. E6 is `OK (offline …)`.
- Risk for the bootstrap deploy: on the first sweep after load, the label has no production `jobs` row, so it reads `unregistered` RED (`watchdog.py:451-456`). See DECISIONS 4.

## DECISIONS
1. `ASK DESK: E1 and E2's [HIS HAND] legs need a real .pptx he can open. No allowed string writes one: `cobalt playbook render` writes a `jobs` row, and pytest decks live in `tmp_path` and are deleted. Which seat renders a test deck (for example, a dev render under the L76 lock with `--out` to a scratch folder)? [07:53]` Default: E1 and E2 stay `NOT RUN`.
2. `ASK DESK: E4 calls for a dev-labelled copy of the plist loaded on this Mac. That is a launchd install, and no hub may run one (deploy-step-c.sh FAILTEXT). Should the desk run it as its own job, or should the brain rule E4 settled by the offline parity tests plus `date +%Z`? [07:53]` Default: E4 `NOT RUN`.
3. `ASK DESK: E5 gated the code deploy's resident downtime. That deploy finished 2026-10-18 (7398d4a7, `uv sync` at row 4.5, RESTARTS done), and the bootstrap-only deploy restarts nothing. May the brain rule E5 moot? [07:53]` Default: E5 `NOT RUN`, so the line does not count until the brain rules it.
4. `ASK DESK: on load, the sweep's first pass finds no `com.cobalt.playbook` row in cobalt_brain. Nothing registers it before load, because the watchdog's `row is None` branch sits after the loaded check (`watchdog.py:451-456`). That pass reads `unregistered` RED for one beat. After it, `registered_at` = load time, and the row stays green until the first Sunday (`:336`). Should the bootstrap-only deploy run `COBALT_ENV=production uv run cobalt jobs register` right after the bootstrap? E6's own consequence is "the deploy card runs one manual render". [07:53]` Default: the bootstrap card states one expected `unregistered` beat.
5. `ASK DESK: E6's offline leg proves the registration rule on a Mon–Fri spec. It does not cover a live sweep of the weekly row on a weekday, which can only run after load. Should the brain accept `OK (offline …)`, or should a post-load `cobalt jobs check` on a weekday be the proof? [07:53]` Default: the line does not count until the brain rules it.

## RECORDS
- 07:50 `date`. 07:52 and 07:53 `date` before each write.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `73cca43b`.
- Read `prompts/2026-10-21/970-f5-gate-run.md` (whole), `prompts/2026-10-19/873-cos-gate-run.md` (whole), `prompts/2026-10-18/779-deploy-f23-playbook-card.md` (`## LAUNCHD` `:21`: `com.cobalt.playbook · deferred · … · gate: E1, E2, E4, E5, E6`), `data/deploy/bootstrap-owed.json` (`:3`).
- `F23-FINAL-2026-10-11.md`: gate table found with Grep; `## First-gate experiments` `:151`, rows E1–E6 `:157-161` (E3 `:156`, pre-build, not owed), RESTARTS/`RunAtLoad false` `:178-179`.
- `ops/desk/deploy-step-c.sh`: `:39-41` (bootstrap-only rule), `:185-186` (the GATE RESULT awk).
- `git show main:tests/cobalt/test_playbook_offline.py`: nodes `:273`, `:291`, `:373`, `:392`, `:412`; offline seam docstring `:1-13`.
- `git show main:tests/cobalt/test_playbook_registry.py`: `:16` `test_the_row_is_a_sunday_1730_one_shot`.
- `git show main:tests/cobalt/test_jobs.py` (saved tool output): `TestTheShippedRegistry` `:69` (`:88`, `:107`), `TestRealPrefillDailySchedule` `:584` (`:658`), `TestMissedStartsWhenWatchingStarts` `:794` (`:797`). None needs a DB.
- `git show main:ops/com.cobalt.playbook.plist`: Weekday 0 Hour 17 Minute 30, `RunAtLoad false`, `COBALT_ENV production`, comment `system TZ = ET`.
- `git show main:src/cobalt/jobs/watchdog.py`: `:336` registration exemption, `:441` OWED, `:451-456` unregistered RED. `git grep register_all|.register(` → no deploy-time registrar outside `cobalt jobs register`, the watchdog and the wrapper.
- `git show main:src/cobalt/jobs/cli.py`, `main:src/cobalt/heartbeat/cli.py`: `jobs check` and `heartbeat beat` write cobalt rows, so they stay off the hub line.
- `git grep add_parser|add_argument main -- src/cobalt/playbook/` → `render --date --out --dry-run` only.
- `reports/deploy-f23-playbook.md`: `grep -n "uv sync"` → `:185`, `:197`; last line `DEPLOYED deploy-2026-10-18-f23-playbook 7398d4a7 …`.
- `ls` → deploy report, `ops/com.cobalt.playbook.plist`, `tests/cobalt/test_jobs.py` all present.
- `topics/writing-rules.md` read.
- Wrote `prompts/2026-10-26/1046-f23-gate-run.md` and this report. Commit: none.

## REVISION (brain R2465)
- F4 reservation card drafted in parallel, launched only on the X15 FAIL; F23 E1/E2 dev render by a K2 seat plus his open legs; E4 settled offline (+ first-Sunday watch); E5 moot; register only if already on the line; E6 post-load weekday check — brain 9b07db5a 2026-10-26
- 1046 revised. E1 and E2 point to render seat 1050 and his session. E4 → `OK — settled offline` (parity tests, `date +%Z`, `/etc/localtime`). E5 → `RULED MOOT`. E6 → `RULED post-load watch`. The stop line counts `ruled`.
- New `prompts/2026-10-26/1050-f23-render-seat.md`, K2, seat `f23-render`. Under the L76 lock (`f23-playbook-1013`), it runs a dev render with `--out /Users/cobalt/cobalt-wt/.f23-render/data`, builds the kill state, renders again, and keeps E2's synthetic decks with `--basetemp`. Its SECOND PASS reruns the swap while he has the decks open. The scratch folder is K1, owed to the desk.
- New `prompts/2026-10-26/1051-deploy-playbook-bootstrap-card.md`. It is the bootstrap-only load card, in 1048's shape. Its pre-written lines: E5 RULED MOOT, E6 RULED post-load. It carries E6 WATCH and E4 WATCH. The `unregistered` beat is recorded as expected in RECORDS and CHECK ASKS X3. Item 4: `DEPLOY-HUB.md:3` bars `jobs register` ("NO `jobs register`"), so no string was added.
- `ASK DESK: 1050 step 3 does not land a real kill -9 between the two renames, which are microseconds apart. Instead it builds the on-disk state such a kill leaves (`mv <day> <day>.old`, no `<day>`), then proves the next render recovers it. Is the constructed state accepted as E1's kill leg? [08:08]` Default: yes; 1050's line names it `constructed kill state`.
- `ASK DESK: the dev render reads cobalt_dev's cards, and the drafter can't confirm they include an 8-plus-row family or a why over 120 characters. 1050 therefore also keeps the synthetic test decks (exact E2 shape) via `pytest --basetemp`, and those are his E2 decks. The dev decks serve E1. Accept the split? [08:08]` Default: both are offered; E2 is read on the synthetic decks.
- `ASK DESK: 1050 takes the lock in the name of worktree `f23-playbook-1013`, which exists; `take-devdb-lock.sh` copies `.env` into it until the release. Keep that worktree? [08:08]` Default: yes.
- Revision reads: `cto-2026-10-26.md:13` (R2465), `ls prompts/2026-10-26/` at 08:06 (1049 taken by `f4-strike-reserve`) and again before 1051, `DEPLOY-HUB.md:3`, `git show main:src/cobalt/playbook/cli.py` (`publish()`, the `.old` recovery), `git show main:ops/desk/take-devdb-lock.sh` and `release-devdb-lock.sh`, `git show main:configs/cobalt/playbook.yaml`, `data.py:156-173` (dev DB and vault), `vault_loader.py:91`, `ls` of the dev vault strategies folder (exists; contents not quoted), `ls -l /etc/localtime` → `America/New_York`, plist `:6`, `:20`, `:44-49`, `gate-lists.md:56` (`## LEVEL 0013`), card 1048 (shape), `ls /Users/cobalt/cobalt-wt/` (`f23-playbook-1013` present, no `.f23-render`).
- Times: 08:06 (revision start), 08:08 (report). Commit: none.

## REVISION (brain R2467)
- F23 render seat — E1 kill leg = constructed kill state; E2 = synthetic decks, E1 = dev decks; lock via f23-playbook-1013 with .env removed at release — brain 9b07db5a 2026-10-26
- 1050: RULINGS adds R2467. Step 3's OK line names `constructed kill state`, accepted. Step 4 records `ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env` → "No such file" after the release, and a file still found there is `FAILED: lock release`. The SECOND PASS records the same. `## FOR HIS SESSION` offers two labelled groups: `E2 — synthetic decks (clip read)` and `E1 — dev decks (viewer-open swap)`. `## RECORDS` carries the R2467 line verbatim.
- 1046: RULINGS adds R2467, and `## RECORDS` carries the R2467 line verbatim.
- NUMBER CLASH: `prompts/2026-10-26/` holds both `1050-f23-render-seat.md` and `1050-f4-gate-run-preflight.md`. Per the desk, the render seat is renumbered at launch, and its launch line names its own file path.
- Reads: `cto-2026-10-26.md:13` (R2467), `ls prompts/2026-10-26/` at 08:10. Time 08:10. Commit: none.

DRAFTED R2467 · decisions: 8
