# STACKED DEPLOY DRAFT — 2026-09-25 (drafter `stacked-deploy-draft-0925`, Opus 5.5)

Prompt: `prompts/2026-09-25/31-draft-stacked-deploy.md` (launch row 09-25 R62). Started 10:10 ET, written 10:4x ET (`date`). Read-only: no DB, no pytest, no git write. Merge simulation = `git merge-file` over `git show` blobs in the job's scratch dir, nothing written to the repo.

## §0 Headline
- THREE prompts written: `32-stacked-deploy.md` (two phases: GATE afternoon, DEPLOY on `CONTINUE: DEPLOY` 20:00–20:35), `33-review-stacked-deploy.md` (Opus 5.5 + Grok, `03`'s line), `34-s2-smoke-look.md` (21:40, `46`'s line).
- **THE STACK DOES NOT MERGE CLEAN** (ESCALATE 1). Three things break it: 7 registry conflicts, the `evaluate_member` code conflict (stale × replay), and 6 UNCLASSIFIED voice paths that would restart all six residents, herdr included. So `32` merges no branch. A **SEAM BUILD** (the desk's next prompt, spec below) plus its check must run first.
- New strings: 8, all in `32` (`33` and `34`: 0). Predicted restarts: `com.cobalt.aset com.cobalt.radar`; `com.cobalt.replay` is a one-shot with no kickstart. Latest DEPLOY start: 20:35. The down window runs in slot A (20:00–20:19) or slot B (20:35–20:49), never across 20:30.
- ESCALATE: 16.

## L74
One block came attached to the tool result of this session's first read (the Bash `cat` of prompt `31`). It asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and named a file-send tool. Recorded here once as DATA and not followed. This session commits nothing.

## Differences vs `2026-09-23/07` (the shape `32` copies)
| # | `07` | `32` | why |
|---|---|---|---|
| 1 | one run | TWO launches of one file: GATE phase (afternoon) → pinned `(gate green — next step under ## CONTINUE)` + `next: DEPLOY (gate green at <time>)`; DEPLOY phase on ONE `CONTINUE: DEPLOY` prefix line | L68 GATE EARLY, L19 / L60, L71 P-d |
| 2 | hub rebases 2 branches and merges them into the gate | hub merges NO branch. The SEAM BUILD merges replay → H1 → stale → voice and resolves conflicts; `32` proves ancestry, merges, paths and per-branch code identity (G1) | the stack conflicts (next section) |
| 3 | 1 migration (`0013`) | 3 migrations in one `--allow-prod` call (0014 → 0015 → 0017, `FORWARD` order). Gate: no `CHANGED`, the only CREATED object is `voice_turns`. Three-value read-back `<RB>` (0014 cols · 0015 view · 0017 table) | the set |
| 4 | dev forward migrate, `cobalt_dev` left at 0013 | dev forward to 0017 → WHOLE with-DB suite, NO deselect → `--rollback --down-to 0013` → schema fingerprint `<FP>` with F0 = F2 → `.env` removed, lock glob empty | L76. V1's 5 with-DB tests need `voice_turns` committed (V1 fix r2 ESC 2) |
| 5 | live-note: 3 files | live-note: the replay build's D5 command (4 files) | the widest leg of the four builds |
| 6 | R5 done-trading window, 19:55 hard clock | pause: DEPLOY start 20:00–20:35. First bootout in slot A 20:00–20:19 (merge < 20:22) or slot B 20:35–20:49 (merge < 20:52). 20:20–20:34 is read-only filler, no wait command. Everything done before 21:05 | L43 / L66, 20:30 archiver, 21:10 replay is the fix's proof |
| 7 | R4 / R5 / R119 / R52 / R53 gates | approval literal `STACKED DEPLOY 2026-09-25 APPROVED <time>` (R__A), launch row R__L, relaunch row `32 DEPLOY RELAUNCH`, P-V1 (device session or DROP), P-LOCK, seam build + seam check lines, `33`'s DONE line | brief 4 (i)–(vi) |
| 8 | three radar tails with no spacing | tails at +90 / +180 / +300 s, PAUSE provision (idle radar is not red if heartbeat is fresh twice), REVERT-READBACK (h) | 09-24 false red (`deploy-2026-09-24.md` ESC 2), K10 |
| 9 | — | (i) H1 production dry-run as the deploy's acceptance (`mismatches 0`); (j) voice rows (`/voice/status` 200; scratch lock line; model missing is expected) | 09-25 R3; V1 build ESC (vi) |
| 10 | STEP-5 revert, 0013 stays | the same ONE `revert -m 2`; all three migrations stay; H1 block check; REVERT-READBACK on the reverted tree (old code vs new rows: NULL-proximity cards, `s2p2.3` runs, `raw_rank`) → terminal ESCALATE 0, never a second revert | 09-24 `ASSUMED` lesson |
| 11 | STEP-6 vault write (R119) | none; the 4 taxonomy strings dropped | nothing to write tonight |
| 12 | restarts must equal aset + radar | the same, and G4 fails closed on any other resident or on UNCLASSIFIED. `com.cobalt.replay` is not kickstarted | L42; replay build `:52` |
| 13 | docs-only proofs exclude `docs` | also `configs/cobalt/rules.yaml` by name (05:15 `generated_at`, `no_resident_reads`; ddb41fbd committed it on main) | proven below |
| 14 | — | D06 compares the `cobalt_dev` fingerprint to gate F2 and re-runs with-DB only if it moved | brief 4 asks for `cobalt db status`, which does not exist (ESC 4) |
| 15 | — | 4.4 is the first `uv run` on the new `uv.lock`, so the five voice wheels sync inside the window. G2 proves they are in the uv cache | voice `pyproject.toml` / `uv.lock` |
| 16 | the RELAUNCH RULE | re-cut for the phases; `Reapply` named in THE ROLLBACK STRING (code → schema by the desk only → re-land) | K10; 09-24 lesson (3) |

## The merge order and the seams
PROOF OF THE FOUR (10:1x):
- replay `a6b99de0`: mb `a994a5dd`, 6 ahead, 14 non-docs paths.
- H1 `77aea166`: mb `f6643d41`, 18 ahead, 49 non-docs paths.
- stale `358f1f75`: mb `de48c19b`, 8 ahead, 50 non-docs paths.
- voice `d794e899`: mb `04b05cd4`, 24 ahead, 60 non-docs paths.
- Union: 156 non-docs paths. `main` = `46f77e5d`; since `fb6f86cd`: 6 commits, docs-only (`git diff --stat fb6f86cd main -- . ':(exclude)docs'` empty).

**THE BRIEF'S PREMISE "docs-only since every merge-base" IS FALSE** (ESC 3):
- Since `de48c19b` and `f6643d41`, main changed one non-docs path: `configs/cobalt/rules.yaml`, committed by desk commit `ddb41fbd`.
- Since `04b05cd4` (voice): 367 commits and 86 non-docs paths, the setups deploy.
- Since `a994a5dd`: nothing non-docs.
- Base ancestry: `04b05cd4` ≤ `de48c19b` ≤ `f6643d41` ≤ `a994a5dd`.

MERGE ORDER (fewest conflicts first, migrations in numeric order): **replay → H1 → stale → voice**. Simulated per file (`git merge-file` from main's blob, each branch's base and tip):
| step | merges | conflicts |
|---|---|---|
| 1 replay | clean | none |
| 2 H1 | clean | none (no shared path with replay; main moved only `rules.yaml`) |
| 3 stale | CONFLICT | `src/cobalt/db_migrations/__init__.py` (docstring + `FORWARD` + `REVERSE`: 0014 and 0015 inserted at the same lines) · `tests/cobalt/test_tenancy.py:515` · `test_p4_migrations.py:102,117,128` · `test_radar_migration.py:35` · `test_radar_score_migration.py` · `test_archiver_migrations.py` · `test_assumed_store.py:244` (positional `FORWARD[-2]` / `[-1]` pins) · **`src/cobalt/radar/evaluate.py` `evaluate_member`, two hunks (CODE)** |
| 4 voice | CONFLICT | `__init__.py` (voice's base has no 0013), the same five registry-pin tests. `test_radar_panel_cards.py` (THE KNOWN SEAM) merges CLEAN against main's moved version |

Any order gives the same conflicts: the evaluate hunk is intrinsic (tried 4 orders).

THE KNOWN SEAM `tests/cobalt/test_radar_panel_cards.py`:
- Of tonight's four, only voice touches it (POST allowlist + the `/radar` expectation gains the widget).
- Main moved it since voice's base (setups ladder SHA pin). The DRC D4 branch also touches it, but that is not tonight's.
- Simulated: clean. The offline suite proves it.
- If the seam build ever conflicts there, resolve "both sides, no line dropped". NEVER hand-edit an expectation to pass. A pin or SHA a merged render changes goes to the check as a named reading. A conflict that cannot be resolved that way → `FAILED: gate — conflict tests/cobalt/test_radar_panel_cards.py`.

**THE SEAM BUILD — the desk's next prompt** (L67 new development + L72 P-b; Opus 5.5 writer, `acceptEdits`, worktree `/Users/cobalt/cobalt-wt/stacked-0925` on `deploy/stacked-0925`, cut from main by `32`'s bare command (0)):
1. Four `git merge --no-edit <branch>` in the order above (voice only if the V1 row says DONE). Each conflict is resolved by the rules below and committed as the merge commit. Conflict resolution is the build.
   - `db_migrations/__init__.py`: keep every side in numeric order. `FORWARD` … 0011, 0013, 0014, 0015, 0017. `REVERSE` 0017, 0015, 0014, 0013, 0011 …. ONE "not a gap" paragraph true to `reports/devdb-builds-reissue-2026-09-23.md` `## MIGRATION SEAM`: 0012 bars chunk-2, 0015 stale-score, 0016 DRC D1, 0017 voice, 0018 DRC K1, 0019 DRC D2's proposed `drc_events`. Voice's paragraph says "0015 DRC D1, 0016 stale-score", which contradicts that doc (ESC 8).
   - The six registry-pin tests: re-point each pin to the combined registry, same objects, same strength. Stale's FOR THE DEPLOY names this ("the `[:6]`/`[-6:]` lists and `numbers == [*range(1, 12), 13, 15]` must be re-pointed together"), and so does H1's A1 table. `test_assumed_store.py`'s positional pins become 0013 / 0014 / 0015 / 0017 from the end. This is the builder's work under the check, never the deploy hub's.
   - `evaluate.py` `evaluate_member`: the replay build's own rule (`replay-deadline-fix-build-2026-09-24.md` `## FOR THE DEPLOY`): "The merge keeps stale-score's block at the top and its `intraday_stale=` in `base`, plus this branch's prep lines."
     - Hunk 1 = replay's `prep` / identity / `prep.*` lines, then stale's `if last_bar is None: intraday_stale = True / else: … .stale` block.
     - Hunk 2 = replay's `run = prep.run` … `frames = prep.frames(...)` WITHOUT its own `intraday_stale` block.
     - Proof: T1 / T2 (`tests/cobalt/test_radar_evaluate.py`) and stale's T (i) on every return path, in the offline suite.
2. ONE registry commit (FOUR only) classifying voice's six UNCLASSIFIED paths (ESC 2). Proposed lines, each proven by its loader `file:line`:
   - `com.cobalt.aset` `reads:` + `configs/cobalt/voice.yaml` (`voice/config.py:32`, cached `voice/web.py:49`), `configs/cobalt/agents/voice.yaml` (`voice/registry.py` `load_agent`), `configs/cobalt/modelaccess.yaml` (`modelaccess/config.py:28` `load_routes`), `ops/start_aset.sh` (the aset plist's program; its exports reach the process only at a restart), `pyproject.toml`, `uv.lock`.
   - `com.cobalt.radar` `reads:` + `pyproject.toml`, `uv.lock` (its plist runs `uv run cobalt radar run`).
   - `com.cobalt.agent`: it also runs `nohup uv run src/cobalt_agent/main.py`. L42's honest rule puts it in the dependency set too, which changes tonight's restart set. That is a house question for the seam check, not his. `32` G4 fails closed if the table names it; the desk then re-issues `32` with the agent restart.
3. The three suites on the tip (L68 GATE EARLY): offline · with-DB forward → whole suite → `--rollback --down-to 0013` → fingerprint · live-note. Then `cobalt jobs restarts <main-at-cut>..HEAD`.
4. Stop line, which `32` G03 checks: `STACK SEAM BUILT <tip> | branches: <4|3> | offline <p>/0 | with-DB <d>/0 | live-note <l>/0 | cobalt_dev: 0013 | .env: removed | UNCLASSIFIED: 0 | RESTARTS: com.cobalt.aset com.cobalt.radar | ESCALATE: <n>`. Report at `…/stacked-0925/docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md`, with a `## FOR THE DEPLOY` naming any path it added.
5. Its CHECK (L67 "other check", Opus 5.5 + Grok) reads each merge's resolution (`git show --remerge-diff <merge>` is the natural packet), the registry lines and the suites. Stop: `STACK SEAM CHECK DONE · … defects that HOLD: 0 · ready for the gate: YES` (`reports/stack-seam-check-2026-09-25.md`).

FALLBACK B, if the seam build or its check is not green by ~18:30 (L43: a branch that turns the combined gate red is dropped, named, and the rest lands):
- Ship `fix/replay-deadline-0924` + `radar/handicap-h1-0922` only. They merge clean (simulated) and restart aset + radar.
- The desk re-issues `32` (L19) with: two hub merges (`merge --no-edit fix/replay-deadline-0924`, `merge --no-edit radar/handicap-h1-0922` in `stacked-0925`: 2 more NEW strings); no seam gates; `<RB>` = 0014 only; no P-V1 and no voice rows; stop line `migrations: 0014`.
- Stale and V1 wait for their seam (named).

## NEW strings — for his ONE approval list (all in `32`; `33` = `03`'s line ± path/rc, `34` = `46`'s line ± path/rc, both proved with `diff` 10:38)
The four worktrees' strings: NONE (the hub rebases and merges no branch).
The gate's (five, `07`'s `stacked-0923` strings re-pointed):
1. `Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0925)`
2. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --no-edit main)`
3. `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --abort)`
4. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env)`
5. `Bash(rm /Users/cobalt/cobalt-wt/stacked-0925/.env)`
The migrations' (one; the two production migrate strings are carried byte for byte):
6. `Bash(COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013)` (shape: `2026-09-23/58`'s `--down-to 0011`)
No precedent shape (two):
7. `Bash(COBALT_ENV=dev uv run cobalt db query *)` (the read-only `cobalt_dev` fingerprint; SELECT/WITH only by the client's allowlist)
8. `Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar handicap-dry-run --day 2026-09-25)` (H1's acceptance; "writes nothing")
RULE PROOF: `comm` of `32`'s line (2) vs `07`'s line 6 and `2026-09-24/09-setups-deploy-r2.md`'s line 7 → 50 strings (47 allow + 3 deny); 39 allow + 3 deny in both; exactly the 8 above in neither. Dropped from `07`: 4 rebase, 2 branch merges, 4 taxonomy (and `07`'s five `stacked-0923` strings).
ALSO ON HIS LIST, drafted by the desk, not here: the SEAM BUILD's strings. It needs, for example, `merge --no-edit <each branch>` in `stacked-0925`, add/commit in that worktree, the three pytest prefixes, the `.env` pair, the dev migrate / rollback / query strings and `jobs restarts`. Its prompt pins them.

## The desk's launch order (with times; `date` 10:4x)
| when | what | notes |
|---|---|---|
| now | ONE message to him: (a) the V1 device session, A = do it this afternoon / B = V1 drops tonight (recommend A, steps below); (b) the approval list (8 strings + 3 migrations + the dev rollback); (c) the seam build (its prompt + strings) | L62 P4, one message |
| now, in parallel | `33` (read of `32`), on the house lane after the running Grok hub (STAGGER literal) | independent of the seam: it reads `32` only (L72). Any HOLD → re-issued `32` before the gate |
| after (a)'s answer and after `09` (DRC D3) releases the `cobalt_dev` lock | the seam build (≈ 60–90 min: 4 merges, resolutions, registry commit, three suites) | the lock: `09` → seam build → `32` gate. No other with-DB launch in between (L76) |
| after the seam build | the seam check (Opus 5.5 + Grok, ≈ 30 min) | house lane |
| after the seam check DONE + `33` DONE (folded) + lock free, target ≤ 18:30 | `32` GATE PHASE (≈ 30–40 min) | stop `(gate green — …)` |
| 20:00–20:05 (latest 20:35) | `32` DEPLOY relaunch (`CONTINUE: DEPLOY`) | desk holds commits and stages nothing; DO NOT EXIT (L60) |
| ≥ 21:40 | `34` | after the 21:10 replay and the 21:40 backup start |
| 18:30 not green | FALLBACK B | named drop, L43 |

## FOR DEJAN
**Voice V1 needs your phone before it ships tonight.** Your 09-25 R23 word: "still OWED before any ship". What the session must show comes from the voice FINAL rows E1 E3 E5 E8 X3. The desk sets it up and runs its own half; your part:
1. The desk starts a TEST copy of the sheet with voice on the Mac (from the voice build, not production). It shares it on your tailnet with `tailscale serve` and sends you one `https://…ts.net` link.
2. **Phone (Android):** open the link. Tap the mic and allow the microphone when asked. Say one short sentence, then tell the desk: did it ask for the mic, did it record, did words come back? (E1)
3. **Trading PC browser:** open the same link. Say whether the PC has a microphone at all; if yes, the same test. (E1)
4. **Both devices:** when a reply shows, does the device speak it out loud in a voice? (E5: a voice on the device). The desk may add a playback test and two voice samples for the coming read-aloud feature in the same sitting, if you want it asked once (09-25 R25).
5. Desk only, no action from you: it decodes your phone's real recording with no ffmpeg installed (E3). It records the network address the server sees for your phone, the Mac and a LAN device, and proves a faked header from the LAN is refused (E8 / X3).
6. You say "V1 device session done". The desk writes `V1 DEVICE SESSION DONE <time>` with the results. If the phone cannot record, records a format the code does not expect, or the recording will not decode, V1 does NOT ship tonight: the desk writes `V1 DROPPED` with your word and the other three land.
**What V1 is in production tonight, even after a good session:** text-only on the Mac (loopback). The speech model is not fetched and the phone link to production is not set up; both are V4 deploy steps. The widget will show "speech-to-text down (model missing)" and the text box works.
**The strings list (one approval):** the 8 NEW strings above, the three production migrations `0014` / `0015` / `0017`, and the dev rollback string, as `STACKED DEPLOY 2026-09-25 APPROVED <time>`. The seam build's strings come in the same message.

## RECORDS
- 09-25 R20 → `configs/cobalt/templates/daily.md.j2` → `jobs.yaml` `no_resident_reads`: **NOT TONIGHT'S — the DRC deploy's item.** None of the four touches it (checked in the four path lists).
- 09-25 R30 ESC 8 → his daily-stop VALUE by his hand before the FIRST DRC deploy: the DRC lane's, recorded, not tonight's. The DRC-deploy doc items stay with the DRC drafter.
- 09-25 R3 → `v3:75` (ESCALATE 1 of the deploy prompt, carried in `32` `## FOR THE DEPLOY — RECORDS`):
  - `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md:75` cites `12:28 ET 2026-09-22, cto-2026-09-22.md §4 R26`.
  - The R26 row (`reports/cto-2026-09-22.md:137`) prints `12:1x ET`. `12:28` is the desk record's minute (`:241`, which H1 fix r2 cites at v3:252).
  - Shipped unchanged as a KNOWN CARRIER. Not a deploy stop.
- 09-25 R3 → H1 RUN-3's two lines, the dry-run acceptance (`32` 4.7 (i)), the rollback order ("the block" = the `handicap:` block in `1 - Trading/Radar Screens.md`, `configs/cobalt/radar.yaml:16`; `handicap-h1-build-2026-09-24.md:736`), aset + radar restarts: all in `32`.
- 09-25 R47 → the timing proof is in `34`: `REPLAY FIX PROVEN | CUT | NOT PROVEN | NOT TESTED`. Opus's two readings are carried. T1 / T2 are named in `32` G2. `com.cobalt.replay` gets no kickstart.
- 09-24 R88 → X24 is information in `34` step 8; X9 = X25 = 0; the gate re-proves `358f1f75`'s code.

## ESCALATE
1. **THE STACK DOES NOT MERGE CLEAN** (details in the section above): 7 test / registry conflicts, 1 code conflict (`evaluate_member`), both certain in any order. `32` cannot gate until the SEAM BUILD and its check are green. That is a new development the desk drafts; the spec is above. Fallback B if not green by ~18:30.
2. **Six UNCLASSIFIED voice paths** (`voice.yaml`, `agents/voice.yaml`, `modelaccess.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `uv.lock`):
   - Today `cobalt jobs restarts` names ALL six residents for them: `com.cobalt.herdr`, which hosts every seat including the deploy hub, and `com.cobalt.mainframe` among them.
   - The registry lines (above) belong to the seam build, never the deploy hub (L42). The brief's R25 ESC 2 (`voice.yaml` not in aset's `reads:`) is PROVEN by the builds' own tables: UNCLASSIFIED CONFIG.
   - OPEN for the houses: does `com.cobalt.agent` (same uv env) restart for a dependency change?
3. **The brief's premise is false** (proven above): voice's base predates 86 non-docs paths, and `rules.yaml` rides desk commit `ddb41fbd`. `32`'s docs-only proofs exclude `rules.yaml` by name.
4. **No `cobalt db status` command exists** (`db_migrations/cli.py:787-836`: `migrate` only, with `--allow-prod`, `--rollback`, `--down-to`, `--proof-only`). The DEPLOY phase re-check uses the `pg_catalog` fingerprint `<FP>`, which needs NEW string 7.
5. **V1's eight with-DB deselects** (`voice-v1-fix-r2-build-2026-09-24.md` ESC 1): the gate runs the whole suite with `0017` committed and then rolled back. It is the FIRST run of the five V1 store / race / lifecycle tests on any DB; a red is real (L70).
6. **What V1 ships as tonight:** text-only on loopback (no model, no `tailscale serve`, both V4). A voice config error or a held scratch lock now FAILS the sheet's start (L1; V1 build ESC xiv). `32` 4.7 (a) / (b) / (j) catch it and roll back. Named for him in FOR DEJAN.
7. **uv sync inside the window:** the first `uv run` after the ff installs 5 wheels. G2 proves they are in the uv cache (the gate `.venv`); still unmeasured. Downtime claim ≤ 300 s; over that is ESCALATE, not failure.
8. **Migration-number text disagrees:** voice's `__init__.py` paragraph ("0015 DRC D1, 0016 stale-score") contradicts the settled seam doc and stale's own paragraph ("0015 stale, 0016 DRC D1"). Docstring only; the seam build writes one true paragraph.
9. **H1 `v3:75`** two-source wording ships as a known carrier (RECORDS).
10. **Rollback forward-data risk, UNPROVEN** (L70): the pre-deploy code on NULL-proximity cards written by stale-score (main's `RadarCardSpec.proximity: Decimal`, `src/cobalt/cards/radar.py:97`, is required; the panel reads `Decimal | None`). `32` STEP-5 (4)'s REVERT-READBACK detects a failure; it does not prevent it. The paused radar writes few rows before a rollback.
11. **Stale's version bump vs tonight's replay:** READING, not a stop. The nightly replay passes the CODE's `EVALUATOR_VERSION` (`replay/runner.py:221`, `formations.py:148`) = `s2p2.3` ∈ `{"s2p2.3"}`, so it is not refused. Receipt replay and audit-export refuse across the cut by design.
12. **H1 dry-run pinned to `--day 2026-09-25`:** if today is not in the radar cache, the row is `UNPROVEN` and ESCALATE, not red.
13. **`34`'s stop line** adds a fourth replay value, `NOT TESTED` (the fix not on production's tree: a rolled-back or dropped deploy). The brief listed three.
14. **`32` is ≈ 100 KB:** `33`'s packet stages it in about 7–8 parts under 15,000 B (R79).
15. **Lock sequencing with the DRC lane** (`09` D3 build, the D2 fix `35`, DRC's proposed `0019`): the seam build and `32`'s gate each take `cobalt_dev` alone. The desk holds DRC with-DB launches between them (L76).
16. **L74:** one block recorded under `## L74`, not followed.

STACKED DEPLOY DRAFTED · prompts: 3 · branches: 4 · migrations: 0014 0015 0017 · new rule strings: 8 · restarts predicted: com.cobalt.aset com.cobalt.radar (+ com.cobalt.replay one-shot, no kickstart) · latest start: 20:35 · ESCALATE: 16
