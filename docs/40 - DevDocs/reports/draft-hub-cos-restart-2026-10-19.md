# draft-hub-cos-restart — card 869 (hub-cos-restart-1019), 2026-10-19

## §0 Headline
- Card written: `prompts/2026-10-19/869-hub-cos-restart-card.md`, BASE `bcbf08f9`, BAND HIGH, rows R1-R3 RED-first, uncommitted.
- R1 `DEPLOY-HUB.md:93` admits agent / aset / cos / radar. R2 a new `- NOT LOADED` line after `:93`, plus `:122` (D1) and `:154` (smoke f). R3 cos after radar at `:3`, `:11`, `:78`, `:94`, `:139`, `:143`, `:149`, `:153`.
- Allow list: `desk-launch.sh` copies the hub's launch line `:11` verbatim (`desk-launch.sh:2614-2629`). Cos's three strings go into `:11`. `desk-launch.sh` stays as it is.
- Two existing tests pin changed lines and are edited in R1/R3: `test_hub_deferred_1018.py:17,:74,:105` and `test_desk_launch_launchd.py:143` (8 → 11 strings).

## DECISIONS
1. ASK DESK: orphan-clean for cos [15:15]. Prompt R(3) asks for it "as aset does today". `ops/desk/orphan-clean.sh:76-82` admits `aset` only and verifies by voice lock and port 5010, which cos does not hold. Default: the card makes no orphan-clean call for cos (`:139` reads `radar and cos: no call, the script REFUSES them`). Adding cos to the script is its own card.
2. ASK DESK: smoke (b) for cos [15:15]. `:150` reads aset's `Started server process` and radar's cycle tails, and no start line for cos is known. Default: (b) gets no cos read. Smoke (a) checks running with a new pid, and (e) checks the heartbeat `cos` probe `loop stamping` (`probes.py:164`).
3. ASK DESK: THE ONE RESUME `:53` (e) reads aset and radar only [15:15]. Default: `:53` is not changed (it is outside the prompt's rows). STEP-5 (3) still brings a downed cos back up from 4.6's strings. Carried as CHECK ASK X3.
4. ASK DESK: F-14 [15:15]. A loaded cos refuses to start while the agent's pidfile is alive (`jobs.yaml:210-211`). The hub's P8, D1 and smoke (a) require the agent ONLINE. Default: out of this card. This belongs to K4 / the F20 handover. Carried as X5.
5. ASK DESK: card header [15:15]. LADDER is `OFF-LADDER — reports/deploy-f16-close-fr2.md 2026-10-19 R2067`, and RULINGS is the prompt's literal `2026-10-19 brain L79 (R2067 and the F16 STEP-R directions)`. Default: kept as given. The desk confirms that `desk-launch.sh build` accepts the parentheses.

## RECORDS
- 15:10 EDT `date`. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `bcbf08f9`.
- Read: `prompts/CARD.md` (whole), `prompts/2026-10-18/787-hub-deferred-card.md` (whole), `git show main:docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (whole, 188 lines; card 787 merged).
- Read: `reports/deploy-f16-close-fr2.md:61-91`, `git show main:ops/com.cobalt.cos.plist`, `configs/cobalt/jobs.yaml:203-227`.
- Read: `ops/desk/desk-launch.sh:1843-1920`, `:2170-2209`, `:2590-2649`. `/Users/cobalt/.claude/ops/desk-launch.sh` is a link to it. No duplicate-string refusal exists there.
- Read: `ops/desk/deploy-outage.sh:1-160` (cos restorable, card 784), `ops/desk/deploy-step0.sh:73` (cos in RESIDENTS), `ops/desk/deploy-step-c.sh` (`:274` refuses agent / aset / radar only), `ops/desk/orphan-clean.sh` header. The hub calls none of deploy-step0 / deploy-outage (grep count 0).
- Read: `tests/ops/test_hub_deferred_1018.py` (whole), `tests/ops/test_desk_launch_launchd.py:140-181`, `src/cobalt/heartbeat/probes.py` (cos probe).
- Grep of `tests/` and `ops/` for the changed hub texts: only the two test files above pin them.
- 15:15 EDT `date`: card and report written. No commit.

DRAFTED · decisions: 5
