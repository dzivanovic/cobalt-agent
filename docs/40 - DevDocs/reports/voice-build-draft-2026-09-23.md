# VOICE BUILD DRAFT — 2026-09-23 (seat `voice-build-draft-0923`, Opus 5.5; prompt `prompts/2026-09-23/42-draft-voice-build.md`)

## §0 Headline
- Wrote 3 files, none committed (no git write, per the prompt): seam S1 `docs/30 - Design/VOICE-v3-SEAM-S1-2026-09-23.md` (14,433 B), build `prompts/2026-09-23/43-voice-v1-build.md` (59,118 B), check `prompts/2026-09-23/44-voice-v1-check.md` (41,788 B). Sizes from `wc -c` at 13:28 EDT.
- V1 = the FINAL §9 slice, R2-1 **side B only** (R56). 12 of the 17 "Before V1" experiments run on this Mac inside the build; 5 of them run FIRST, before any code. The other 5 (E1, E3, E5, E8, X3) need his phone, the trading PC and `tailscale serve`: they are a DEVICE SESSION, OWED before ship.
- His ONE approval list: 9 NEW rule strings (N1–N7 plus the re-pointed `.env` pair), 1 desk command (NEW USE), 1 conditional date extension. The check (`44`) adds no string.
- Status: DRAFTED. ESCALATE: 11.

## NEW strings — his ONE approval list (for `43`'s launch line; `44` is `06`'s line byte for byte)
| # | String | What for · can touch · can never touch |
|---|---|---|
| E-1 | `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env)"` | with-DB suite + `cobalt_dev` migrate. It is the 09-21 R41 / 09-22 R30 pair re-pointed to this worktree: copied by name, never printed, removed at every stop · touches this worktree only · never production |
| E-2 | `"Bash(rm /Users/cobalt/cobalt-wt/voice-v1/.env)"` | the pair's removal. It matches one path only |
| N1 | `"Bash(uv add faster-whisper*)"` | E10: adds ONE dependency (network to PyPI; changes `pyproject.toml` and `uv.lock` in the worktree) · never another package |
| N2 | `"Bash(uv tree*)"` | E10: read-only lock inspection |
| N3 | `"Bash(uv pip show *)"` | E10: read-only licence lines |
| N4 | `"Bash(uv run python scratch/voice-x/*)"` | the builder's experiment scripts (gitignored `scratch/`): synthetic speech via `say`, STT timing, the Plan call to `127.0.0.1:1234`, and ONE model download from `huggingface.co` into `/Users/cobalt/.cobalt-dev/voice-models/`. Same code-execution class as the already-approved `uv run pytest *` · no DB |
| N5 | `"Bash(COBALT_ENV=dev uv run python scratch/voice-x/*)"` | the same, for E6 / X13 on `cobalt_dev`. It never runs under production |
| N6 | `"Bash(bash /Users/cobalt/cobalt-wt/voice-v1/scratch/voice-x/x22-launchd.sh)"` | X22 only: a THROWAWAY launchd job `com.cobalt.x22-probe` on port 5099. The script text is fixed in `43` and grep-verified before its one run. It never names a production job, and it bootouts itself |
| N7 | `"Bash(COBALT_ENV=dev uv run cobalt voice turn *)"` | the new CLI, dev only, `--dry-run` demos. `--confirm` is refused in production by code |
| desk | `git -C /Users/cobalt/cobalt worktree add -b voice/v1-0923 /Users/cobalt/cobalt-wt/voice-v1 main` | the desk's worktree add (NEW USE of the precedented shape; the hub never runs it) |
| cond. | `Bash(grok *)` and `Bash(agy *)` extended through the day `44` launches, if that day is after 2026-09-24 (R28 ends 2026-09-24 23:59 ET) | no new string. His date extension only |

Precedented and carried unchanged: `33`'s seventeen shared strings, its three denies and the `--add-dir` triplet; `"Bash(COBALT_ENV=dev uv run cobalt db migrate)"` (`27-handicap-h1-build.md`, `53-deploy-d3.md`); `"Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)"` (09-2x deploy prompts); `44` = `06`'s 15 strings + 3 denies + triplet.

## V2–V5 queue (not drafted today; FINAL §9 hours are GUESS)
| Slice | What | h | Gate |
|---|---|---|---|
| V1-D device session | E1, E3 (his phone's real file, no system ffmpeg), E5, E8 / X3 behind `tailscale serve` on a dev port. Attended: his phone + the trading PC; the desk runs it | ≈0.5 (his time ≈10 min) | V1 BUILT; NEW `tailscale serve` on / off strings (his approval); before `44` if possible, before ship always |
| V2 | DRC by voice: per-trade answer (`append_to_unit` + `land_pending`), no-trade reason, per-day blank cells, `drc.build` / `drc.status`, `drc.voice.bind`, `upsert_region blank_only` | 7 | DRC D2 + D3 merged; the S2 seam items placed in the DRC FINAL re-issue (D3 calls `land_pending`, D3 persists the matched card id, D5-3 renders `voice not bound`); E9, E11, X2, X4 first; V1 merged. First VAULT write → `acceptEdits` + full allowlist (L29 / L62 / L63 interim) |
| V3 | any note field + the voice-ordered edit class under L28 as amended 2026-09-23 (item 3 side B + his clause: written even if the span changed, before / after versioned, no merge baseline) | 5 | V2; X21, X23 first; the FINAL's item-3 text still says "refused if changed" and the LAW governs. The desk's R56 FINAL fold should land before V3's prompt. Vault write → `acceptEdits` |
| V4 | ops: `voice_stt` / `voice_plan` / `voice_scratch` probes (count only, side B's row), the `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`, the model-fetch step, the `tailscale serve` production step, DevDocs | 2 | V1 merged. RESTARTS `com.cobalt.heartbeat`. The `tailscale serve` production step needs his word (outward-facing) |
| V5 | trading-logic drafts: `trading_logic: true` tools for the `--card` / `--optional` settings keys, owner-drafted file in `data/voice-drafts/` + sha256 + per-key diff, `send_dm` card with his apply command | 4 | V1 merged; L7 unchanged (applied only by his `cobalt settings load … --sha256 … --apply`, or the desk on his approve) |

## ESCALATE
1. **MODE.** `43` launches `--permission-mode auto` under the desk's DEV-LANE READING (`27`, `28` precedents). V1 writes NO vault byte. Its writes are `cobalt_dev` + worktree only. The prompt `42` triggers `acceptEdits` for "a vault write in V1", and V1 has none; V2 / V3 are the first `acceptEdits` launches. ASK DESK: confirm auto for V1 [13:28].
2. **DEVICE EXPERIMENTS AFTER THE BUILD.** The FINAL says V1 "depends on" E1–E8, but E1 / E3 / E5 / E8 / X3 need his devices and a `tailscale serve` string. The builder therefore builds container-agnostic code (the `isTypeSupported` chain; the allow list lives in config) and synthesizes fixtures in the EXPECTED Android container (`audio/webm;codecs=opus`). A different container found on device = a fixture / map fix round. The alternative is a static probe page served by `tailscale serve` BEFORE the build (E1 / E5 on screen, ≈10 min of his time). That is not drafted. Desk's call.
3. **X22 + THE LOCK.** `43` C4 adds an exclusive `flock` in front of side B's delete-ALL start sweep. It is a mechanics guard that makes side B's premise ("no turn of a new process is live") a CHECK: it never adds an age test, and it never reopens his letter. It exists because uvicorn's lifespan startup likely runs BEFORE the port bind (a reading, UNVERIFIED — X22 measures the orphan half). The builder carries it as an ASK DESK with keep as the safe default. The desk may strike it.
4. **R56 SCOPE READING.** His "it doesn't matter what was in the box in the interim" is folded into L28, and L28 governs VAULT edits (V3). V1's card-stop act keeps FINAL `[F-09]`'s refuse-and-re-confirm on a changed target. The desk should confirm the reading, or tell him if he meant it for card acts too.
5. **PRODUCTION PREREQUISITES V1 NEEDS AT ITS DEPLOY.** The FINAL puts "model-fetch deploy step" in V4, but V1 cannot transcribe in production without the model in `/Users/cobalt/.cobalt/voice-models/`. The V1 deploy prompt must carry the model fetch plus the migration (`--allow-prod`), the `COBALT_VOICE_*` exports and the `com.cobalt.aset` restart inside the pause. Until `tailscale serve` (V4 / V1-D) lands, the widget is reachable only from the Mac browser on loopback.
6. **MIGRATION NUMBER (L68).** 0012 (`bars/chunk-2-0920`), 0013 (`deploy/stacked-0923`) and 0014 (`27-handicap-h1-build.md`, not yet built) are claimed. `43` carries `<NNNN>` for the desk to fill. Suggest 0015.
7. **FINAL FOLD OWED (R56).** `43`'s AUTHORIZATION pins the FINAL at `43a11a1`. If the desk commits the item-3 fold before V1 launches, that gate must be re-issued (L19). I left the FINAL untouched.
8. **CHECK DATE.** grok / agy stand through 2026-09-24 23:59 ET (R28). `44` will most likely launch later than that, and its DATE + EXTENSION GATE then needs a committed row of his.
9. **ONE GUARD (L3).** `classify/collector.py::_guard_outbound` (unmerged `jev/trial-0923`) duplicates S1's `refuse_if_secret_shaped`. Seam §3 rules that whichever branch merges second re-points to S1. JEV's check B / merge prompt must carry it if V1 lands first.
10. **S1 DECISIONS NO HOUSE HAS RULED.** The seam is the FINAL's precondition, not a tribunal item. The drafter set four mechanics: the literal guard being inactive does not refuse a LOCAL route; `litellm` must be silent at import, else the pinned `openai` client is the adapter; V1 has no module call ledger; the module name is `modelaccess`. None of them touches frozen routing law. The L67 check of V1 reads them, and the routing tribunal may rule otherwise later.
11. **CHECK PACKET SIZE.** V1 will exceed `70`'s 230,000 B ceiling as one packet (`29` failed that way today). `44` pre-splits into A (model / agent / act / DB) and B (audio / route / widget / CLI / experiments). Each packet has its own ceiling and a rule-based one-time halving. That means ≥3 houses PER packet and up to 2–4 calls per house. The per-packet reading of the ceiling is the drafter's; the desk should confirm it.

No `ASK DESK` beyond items 1 and 3. L74: no block arrived inside a tool result. No `MEMORY:` / `RULING:` lines. L32: no ticker, price or spoken word of his written. L48: the only clock time used (13:28) was read from `date` in the turn.

VOICE BUILD DRAFTED · slice: V1 · experiments first: 5 · new rule strings: 9 · ESCALATE: 11
