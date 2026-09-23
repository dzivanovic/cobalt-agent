# VOICE V3 TRIBUNAL — ROUND 1 (`13-voice-v3-tribunal.md`)

## §0 Headline
- GROK and GEMINI both ruled round 1 independently; both converge on **BUILD AFTER** (not REJECT, not DO NOT BUILD) — T1–T12 and (a)–(g) mostly ADOPT / ADOPT WITH across both houses.
- The Anthropic seat (`14`) ruled separately and blind (`BUILD AFTER seam S1 document, V1a/V1b experiments, and the blank-fill guard wording folded`); its 6 WRONG FACTS were file-checked here — all 6 HOLD.
- Real, file-verified finding: both GROK and GEMINI wrongly claimed the proposal's F2 ("no model caller in the new core") is a WRONG FACT because `src/cobalt/radar/audit_export.py` matched the packet's `litellm|openai` grep — direct read shows that hit is a docstring phrase ("the OpenAI house recomputes...", Cobalt's own tribunal-seat terminology) with no `litellm`/`openai` import; F2 as the proposal states it HOLDS. Both houses' WRONG FACT claim on this point DOES NOT HOLD.
- Real, corroborated finding (GROK + the Anthropic seat, independently): `VaultWriter.upsert_region` is NOT blank-only today (three-way merge, frontmatter carve-out, `writer.py:895`) — the proposal's clause-2a table row treats it as blank-only. GROK's `ADOPT WITH` (`blank_only` flag) fixes this; unfixed, it risks overwriting his bytes without O1.
- Claims that HOLD: 6 of 10 checked · Anthropic-seat R1 claims checked: 6 HOLD of 6 · blockers to build: 1 (the S1 seam-document precondition) · owner items: 1 (O1) · ESCALATE: 6

## AUTHORIZATION
- `date` (row 1, DATE + EXTENSION GATE): 2026-09-23 09:16:14 ET — before 19:25, before 23:20 → no window block.
- `cto-2026-09-20.md` R13 :86 — present, matches launch-list ruling.
- `cto-2026-09-20.md` R23 :206 — present, grok/agy standing through 2026-09-21.
- `cto-2026-09-21.md` R46 :57 — present, carries "For the designs and creations we need the higher level models."
- `cto-2026-09-22.md` R13 :150 — present, carries "without Astra".
- `cto-2026-09-22.md` R100 :65 — present, carries "A, B as soon as possible."
- `cto-2026-09-22.md` R109 :56 — present, carries "Make all Opus 5.5 for now."
- `cto-2026-09-23.md` R18 :21 — present, carries all three literals: `VOICE v3 DIRECTIVE`, `Solve this`, `All houses have same permission`.
- `git log -S"VOICE v3 DIRECTIVE" -- cto-2026-09-23.md` → `08f2e161c579c5ce0122319a593266fa46b5f0a` — non-empty.
- `git log -1 -- VOICE-v3-proposal-2026-09-23.md` → `153c4b805363d749e2a4b4b491c64e6aaab9cf4d` — non-empty, committed.
- `git log -S"VOICE V3 DRAFTED" -- voice-v3-draft-2026-09-23.md` → `153c4b805363d749e2a4b4b491c64e6aaab9cf4d` — non-empty.
- Launch row: `cto-2026-09-23.md` R33 :36 — names `13-voice-v3-tribunal.md`, gives full stagger literals; committed at `c97b0cd3c135d2896f007d781b69376a3c2f7ed4`.
- NO NEW RULE check: all 14 allow strings + 3 deny strings counted ≥1 in `08-bars-chunk-e-check.md` (all returned 1 or 2). No Sol/Opus checker string in this launch line.
- Result: AUTHORIZATION HOLDS — proceed.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| DATE + EXTENSION GATE (row 1) | `date` | 0 | ALLOWED — 09:16 ET, before both windows |
| grok present | `grok --version` | 0 | ALLOWED — grok 1.0.25 (f7e67d6988e2) [stable] |
| agy present | `agy --version` | 0 | ALLOWED — 1.2.9 |
| base folder exists | `ls scratch/tribunal-bars-0920` | 0 | ALLOWED — folder exists, populated by prior tribunals |
| recovery check | `ls scratch/tribunal-bars-0920/voice-v3-tribunal/r1` | 1 "No such file or directory" | FRESH RUN — no prior stage |
| stagger 53-57 (DRC checks) | `ls reports | grep drc-d<k>-check-2026-09-` | 0, no matches | ALLOWED — absent; covered by launch row R33 "53/54/55/56/57 is not running" |
| stagger 03 | `tail -3 devdb-repair-review-2026-09-23.md` | 0 | ALLOWED — last line `DEVDB REPAIR RE-ISSUE REVIEWED …` (done prefix) |
| stagger 05 | `tail -3 setups-blind-code-2026-09-23.md` | 0 | ALLOWED — last line `SETUPS BLIND CODE SEAT DONE …` (done prefix) |
| stagger 06 | `tail -3 s2-smoke-fix-check-2026-09-23.md` | 0 | ALLOWED — last line `S2 SMOKE FIX CHECK DONE …` (done prefix) |
| stagger 08 | `tail -3 stacked-deploy-review-2026-09-23.md` | 0 | ALLOWED — last line `STACKED DEPLOY REVIEW DONE …` (done prefix) |
| astra probe (gate for astra only, carried) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | exit 1 | USAGE-LIMIT — "You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM." → `astra: METER — proceed on three` verbatim (EXPECTED until Sat 09-26 06:47 ET). RECORDED, not a refusal. Proceed on Grok + Gemini. |

PREFLIGHT RESULT: all rows ALLOWED; no house denied; astra METER (expected) — proceed to stage the packet.

Note: `cto-2026-09-23.md` changed on disk mid-run (desk appended new rows after R18/R33, which remain intact and unchanged) — taken as current state, not reverted.

## Packet
Staged at `scratch/tribunal-bars-0920/voice-v3-tribunal/r1/` (worktree `/Users/cobalt/cobalt-wt/agy-trial`). 16 files, total **166,901 B ≈ 41,725 tokens** — OVER the 100 KB target both before and after all six cuts.

| file | bytes | status |
|---|---|---|
| 00-READING-ORDER.md | 2,024 | MANDATORY, written last |
| 01-QUESTIONS.md | 12,544 | MANDATORY, verbatim + file list appended |
| 02-greps.txt.part1 | 30,963 | MANDATORY, split (part2 continues) |
| 02-greps.txt.part2 | 37,998 | MANDATORY |
| 10-PROPOSAL.md | 31,958 | MANDATORY, whole — matches committed file exactly (31,958 B / 207 lines, drafter's stated size) |
| 11-draft-digest.md | 6,111 | MANDATORY, 4 headed ranges |
| 12-rulings.md | 5,153 | MANDATORY, verbatim ruling rows |
| 13-v2.excerpt.md | 4,299 | OPEN-AS-NEEDED, CUT (ii) applied |
| 14-devices.excerpt.md | 4,286 | MANDATORY |
| 15-drc-v2.excerpt.md | 3,735 | OPEN-AS-NEEDED |
| 20-drc-build-seam.excerpt.md | 6,630 | MANDATORY |
| 21-vaultwrite.excerpt.py | 4,505 | OPEN-AS-NEEDED, CUT (vi) applied |
| 22-aset.excerpt.py | 3,536 | OPEN-AS-NEEDED, CUT (v) applied |
| 23-cited-docs.excerpt.md | 2,413 | OPEN-AS-NEEDED, CUT (iv) applied |
| 24-migrations.excerpt.py | 2,349 | OPEN-AS-NEEDED, CUT (iii) applied |
| 27-laws-excerpt.md | 6,397 | OPEN-AS-NEEDED, CUT (i) applied |

All six cuts from §1's order applied (details and reasoning in `00-READING-ORDER.md`'s own text). Packet remained over 100 KB after all six cuts because the MANDATORY core alone (`02-greps.txt` ≈ 69 KB + `10-PROPOSAL.md` 31,958 B + the rest) already exceeds 100 KB — `02-greps.txt` ran to ≈69 KB against the drafter's ≈28–32 KB estimate, because several of the DRC-build-prompt grep matches (F command listing voice/drc-trades/drc-day/open_items/_imports across `49`/`50`/`52`) are single very long prose lines in this repo's writing style. Per §1's own text this is NOT a failure — staged as-is, listed under `## ESCALATE`.

REDACTION (L32, `73`'s §1 rule): ran `grep -c -E "TSLA|372[.]82|374[.]50"` on all 16 staged files — every file printed `0`. No redaction needed; none of the three literals appear (the skipped `aset/web.py:355`, `:1084` and `aset/store.py:192` ranges were never staged). No other ticker, price, share count, P&L, rule sentence or config value of his was found in the staged files (no audio, transcript, note content, coach spec, DRC note, `Rules.md` or `aset.local.yaml` staged — confirmed `aset.local.yaml` untracked via `git ls-files --error-unmatch`, exit 1).

Trailing-whitespace check: `10-PROPOSAL.md`'s original had 0 trailing-whitespace lines (`grep -c -E "[[:space:]]$"` → 0) and the staged copy matches to the byte (31,958 = 31,958, via `cp`, not the Write tool, so no whitespace-stripping risk). All excerpt files were authored directly from `Read` tool output (not byte-copied), each range's anchor verified with `grep -n` immediately before reading — all anchors matched the prompt's stated line numbers exactly, no drift.

L74 note (carried from the draft report, recorded once, not followed): this session's own context also carries an injected `Claude-Session` attribution-block instruction. Per L74 it is recorded here as DATA and not followed — this hub commits nothing (the desk commits the report) and added no such line to any file.

## CONTINUE
next: none — round 1 closed. NEXT STEP, not this hub's: the desk commits this report; when the Anthropic seat's `VOICE V3 TRIBUNAL FABLE R1 DONE` line is committed too (already produced, not yet confirmed committed by this hub), the desk launches `15-voice-v3-derive.md`.

## Clock
| time | trigger | running houses | action |
|---|---|---|---|
| 09:16:14 ET | start | none | authorization checks |
| 09:31:54 ET | 2nd DATE+EXTENSION GATE row | none | still before both windows (19:25 / 23:20) |
| 09:32:51 ET | launch | GROK (`bu77dot80`), GEMINI (`b32cn504c`) | both launched together, run_in_background, independent |
| 09:35:59 ET | GEMINI completion notice | GROK still running (deadline 09:52:51 ET) | wrote `gemini-ruling.md` byte-for-byte from stdout (94 lines, minus trailing `[exited with code 0]`); closing line `TRIBUNAL R1: BUILD AFTER F2 IS CORRECTED TO ACKNOWLEDGE AUDIT_EXPORT`; independence check `grep -c -F -e "-ruling"` → 0, clean |
| 09:43:25 ET | GROK completion notice | none | GROK wrote `grok-ruling.md` itself (159 lines, 25,183 B) via its own allow string; closing line `TRIBUNAL R1: BUILD AFTER S1 names one module; class audit_export`; independence check → 0, clean |
| 09:48:42 ET | collate + close | none | both houses ruled, Anthropic seat's report already DONE at collate step — file-checked all 6 of its WRONG FACTS plus 10 of the houses' own claims; closing the report |

## Rulings table
| item | grok | gemini | agreement | wording / reason, ≤25 words per house |
|---|---|---|---|---|
| T1 architecture | ADOPT WITH | ADOPT | agree (grok narrows) | grok: one function, 3 callers, exactly one model call per non-confirm turn, zero on confirm turns (L37). gemini: single verifiable path, simplest correct shape. |
| T2 capture/exposure | ADOPT WITH | ADOPT | agree (grok narrows) | grok: allow-list by socket peer address only, never a client header; upload reads bytes directly. gemini: tailnet proxy secures capture, respects "private/isolated" ruling. |
| T3 local STT | ADOPT | ADOPT | agree | Both: faster-whisper pinned, CPU first, Metal only after E2 + deploy step, no cloud. |
| T4 agent/tool boundary | ADOPT WITH | ADOPT | agree (grok narrows) | grok: token-level figures check (no per-digit compare); read tools never call a write route. gemini: closed lists + code-rendered figures block hallucination into trading logic. |
| T5 device TTS | ADOPT | ADOPT | agree | Both: no reply audio on server; local voice absent = text + AMBER, not a defect (E5). |
| T6 confirmation | ADOPT WITH | ADOPT | agree (grok narrows) | grok: single-flight token, exact "yes"/"no" match, sha256 re-check before execution, TTL. gemini: sha256 diff-check + code-matched word guarantees exact-heard execution. |
| T7 field/candidate resolution | ADOPT WITH | ADOPT | agree (grok narrows) | grok: floating widget carries NO card/trade id — nearest-card binding is BANNED outright (concrete wrong-card scenario given). gemini: 0/2+ candidates clarify, never nearest. |
| T8 ephemeral-audio lifecycle | ADOPT | ADOPT | agree | Both: scratch path, config refusals, unlink-in-finally, no bytes column, synthetic test audio all stand. |
| T9 vault-write path | ADOPT WITH | ADOPT | disagree on `upsert_region` | grok: `upsert_region` is NOT blank-only today — needs new `blank_only` flag (~15 lines) or it can overwrite his bytes via its existing sync-revert win. gemini: asserts `append_to_unit` "safely idempotent," does not flag the blank-cell gap. **grok's finding file-checked HOLDS** (see Checked against the files). |
| T10 failure modes/state machine | ADOPT WITH | ADOPT | agree (grok narrows) | grok: reap `planned`→`failed` on limit; never auto-retry a reaped `executing` row (crash-after-commit scenario given). gemini: degraded states map to heartbeat probes, no silent failure. |
| T11 slice plan/experiments | ADOPT WITH | ADOPT | agree (grok narrows) | grok: V1 migration number must NOT be 0012/0013 (already claimed off-main); hours are GUESS. gemini: V1 minimal, complex vault writes correctly deferred to V2. |
| T12 v2 owner items/seam | ADOPT WITH | ADOPT | agree (grok narrows) | grok: seam entry 1 resolved by `land_pending`, not "initial body"; entries 2/4/5 kept, entry 3 void. gemini: the 12 items are correctly implementation mechanics, not his. |
| (a) fact base | see F-table | see F-table | disagree on F2 | Both flag F2 as a WRONG FACT (`audit_export.py`). **File-checked: DOES NOT HOLD** — see Checked against the files. |
| (b) L3 one path | HOLDS | (not separately addressed) | grok only, detailed | grok walks the 11:00/16:30/re-import/vanished-trade sequence: one writer (`land_pending`→`append_to_unit`) for his bytes throughout. |
| (c) routing/local-first | S1 lawful, UNVERIFIED on deps | S1 lawful | agree | Both: one model-access module is the lawful shape; grok adds L15's four gates are not yet run (E10 owed). |
| (d) his bytes | mostly holds, ONE gap (T9) | holds | disagree on T9 gap | See T9 row — grok's gap is the substantive disagreement; both agree `market_reset`/`_session_gate` correctly refuses. |
| (e) the boundary | NONE | NONE | agree | Both: no order/platform path; L7 HITL unchanged; no secret reaches the model; confirm is code-matched, never model-judged. |
| (f) the card | L52 does not bind | nothing computes a score | agree (but premise imprecise) | Both assert no score/rank/grade/size is computed. **File-checked: DOES NOT HOLD as literally stated** — `record_stop_edit` recomputes `shares` (store.py:668-674), inherited unmodified from the page's own human-fed path. See Checked against the files. |
| (g) owner test | O1 passes, sole item | O1 passes, sole item | agree | Both: O1 is the only item that is his money/data/time/law; neither house sends him anything else. |
| closing line | `TRIBUNAL R1: BUILD AFTER S1 names one module; class audit_export` | `TRIBUNAL R1: BUILD AFTER F2 IS CORRECTED TO ACKNOWLEDGE AUDIT_EXPORT` | both BUILD AFTER, different conditions | Grok's S1-seam-document condition file-checks as the real blocker; the audit_export "class it" condition (both houses) is resolved by this hub's file-check — it is not a model caller. |

## Wording offered, verbatim
**GROK — T2, ADOPT WITH:** "`/voice/*` allows a request only from the socket peer address. Loopback is allowed. The peer address E8 records for `tailscale serve` is allowed. Any other peer, including a LAN address, is a named 403. A header the client can set is never the allow key."
**GROK — T6, ADOPT WITH:** "While a row is `awaiting_confirm` and younger than `confirm_ttl_s`, the turn function makes no model call. The whole normalized transcript (Unicode casefold, strip) must equal the single confirm word `yes`, or he taps Confirm. The single cancel word is `no`. ... One single-flight token: the first confirm or cancel commits; a second in-flight request finds no pending action. Execution re-computes the owning expert's diff and requires the same sha256."
**GROK — T7, ADOPT WITH:** "The floating widget sends no card id and no trade id. UI context narrows only when the control he pressed belongs to one card or one trade row, or the page is showing exactly one. Geometric nearest is never a candidate."
**GROK — T9, ADOPT WITH:** "Blank cells outside markers are filled only by `upsert_region` with `blank_only=true` (new flag, default false, about 15 lines in `vaultwrite/writer.py` plus tests, slice V2/V3, no second writer). `blank_only` writes only when the located span is empty or whitespace, and it does not take the sync-revert win; a non-empty span is refused as the O1 class and is not merged."
**GROK — T11, ADOPT WITH:** "The one migration is `\"user\".voice_turns`, number assigned by the desk at L68, and it is not 0012 or 0013: those numbers are already claimed off main ... while FORWARD's last file on this tree is 0011."
**GROK — closing:** "TRIBUNAL R1: BUILD AFTER S1 names one module; class audit_export"
**GEMINI — closing:** "TRIBUNAL R1: BUILD AFTER F2 IS CORRECTED TO ACKNOWLEDGE AUDIT_EXPORT"
No REJECT text was issued by either house (this section carries only ADOPT WITH replacement wordings and the closing lines, per §1's instruction to reproduce them unedited).

## Wording offered, verbatim
(pending)

## Checked against the files
| # | claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|---|
| C1 | WRONG FACT: proposal's F2 "no model caller under src/cobalt" — `audit_export.py` hits the litellm/openai grep | grok | `src/cobalt/radar/audit_export.py:7` | **DOES NOT HOLD** | Line reads "The OpenAI house recomputes `card_score`" — Cobalt's own tribunal-seat term, not an API call; no litellm/openai import in the file. |
| C2 | Same WRONG FACT claim | gemini | `src/cobalt/radar/audit_export.py:7` | **DOES NOT HOLD** | Same file-check as C1. |
| C3 | F2 itself: "grep -rln -i litellm src/cobalt → none" | proposal (`10-PROPOSAL.md:17`) | `src/cobalt/radar/audit_export.py` imports (`:43-61`) | **HOLDS** | Imports are pydantic/stdlib/cobalt-internal only; no litellm, openai SDK, or httpx call anywhere in the file. |
| C4 | `upsert_region` today is a three-way-merge frontmatter carve-out, not blank-only; takes the sync-revert win | grok | `src/cobalt/vaultwrite/writer.py:895-919` | **HOLDS** | Docstring literally: "the same three-way merge... this is the frontmatter carve-out," no blank-only guard in signature or body. |
| C5 | Proposal's clause-2a row: "A BLANK template cell/bullet ... `upsert_region` (F9), blank → value only" | proposal (`10-PROPOSAL.md`, §6 table) | `src/cobalt/vaultwrite/writer.py:895` | **DOES NOT HOLD as written** | Same code as C4; "blank only" is enforced today only by a CALLER (`seatusage/runner.py:141-147`), not by `upsert_region` itself — corroborated independently by the Anthropic seat's WRONG FACT #3. |
| C6 | Migration number for `voice_turns` must not be 0012 or 0013 — already claimed off main | grok | `02-greps.txt.part2` git-log (`--diff-filter=A`): `0012_bars_partitioned_parent.sql` (`02d67a6`), `0013_tunables_slug_nullable.sql` (`61a283f`) | **HOLDS** | Both numbers exist on other branches; `db_migrations/__init__.py` FORWARD on main still ends at 0011. |
| C7 | WRONG FACT: proposal cites `52-drc-d5-build.md:18` for A31/D5-3, packet's current anchor is `:21` | grok | `docs/40 - DevDocs/prompts/2026-09-22/52-drc-d5-build.md:21` (grepped fresh) | **HOLDS** (as citation drift) | Confirmed current line is 21. Proposal's own F10 row already flags "line numbers move on re-issue — grep the anchors" — expected drift, not treated as a defect. |
| C8 | "Nothing here computes or changes a score, rank, grade, or size" / "the card stop edit acts identically to the manual page edit" | grok + gemini, item (f) | `src/cobalt/cards/store.py:659-674` | **DOES NOT HOLD as literally stated** | `record_stop_edit` calls `engine.recompute_for_stop` and updates `shares` in the same transaction ("Decision 11: stop edits recompute shares/risk/targets/room live," comment at :668-671) — a sizing figure IS recomputed. This is pre-existing behavior shared with the page's own edit, not new to voice, but the houses' stated premise is imprecise. |
| C9 | Card-stop route: `_check_entry_allowed()` then `CardStore.record_stop_edit`, gated by `assert_writable("cards.stop_edit", ...)` | grok (F5) | `src/cobalt/aset/web.py:1239-1257`; `src/cobalt/cards/store.py:659` | **HOLDS** | Verbatim match at both sites. |
| C10 | `market_reset` / `_session_gate` correctly refuses every vault write; `record_stop_edit`'s own gate is separate and also refuses | grok + gemini, item (d)/(e) | `src/cobalt/vaultwrite/writer.py:387-416`; `src/cobalt/cards/store.py:659` | **HOLDS** | Both gates confirmed live; `assert_writable` raises `SessionBlocked` in the window for both paths. |

## Anthropic-seat round-1 claims, file-checked
Anthropic seat report `voice-v3-tribunal-fable-r1-2026-09-23.md` last non-blank line starts `VOICE V3 TRIBUNAL FABLE R1 DONE` — read its `## Rulings`, `## Self-attack` and `## WRONG FACTS` sections; file-checked every `file:line` claim its `## WRONG FACTS` rests on (its `## Rulings`/`## Self-attack` ADOPT WITHs were not separately re-derived beyond what overlaps the WRONG FACTS below — the same file reads cover both).

| # | claim (seat report line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| FC1 | "only the old tree `src/cobalt_agent/llm.py` imports LiteLLM" is incomplete — `extractor.py:22`, `memory/postgres.py:31` also import it | `:211` | `src/cobalt_agent/tools/extractor.py:22`, `src/cobalt_agent/memory/postgres.py:31` | **HOLDS** | Both files confirmed present in this hub's own `02-greps.txt.part1:12-15` (`cobalt_agent/tools/extractor.py`, `cobalt_agent/memory/postgres.py` both listed on the litellm/openai grep). Old tree only, no design effect, as the seat itself notes. |
| FC2 | F9 "every op passes `_session_gate`" is wrong — `restore` is ungated by the 09-04 ruling | `:212` | `src/cobalt/session/guard.py:80-91` | **HOLDS** | Docstring: "RULED 2026-09-04 ... `VaultWriter.restore` and `CardStore.backfill` already carried that carve-out ... migration and repair tooling stays UNGATED in `market_reset`." |
| FC3 | §6 blank-cell row: `upsert_region` is not blank-only; "blank only" is a caller-side check today (`seatusage/runner.py:141-147`) | `:213` | `src/cobalt/vaultwrite/writer.py:895-919` | **HOLDS** | Same finding as C4/C5 above — three independent reads (grok, Anthropic seat, this hub) converge. |
| FC4 | "nothing computes a score, rank, grade or size" is wrong — `cards/store.py:668-674`/`:730` recomputes `shares` | `:214` | `src/cobalt/cards/store.py:668-674` | **HOLDS** | Same finding as C8 above — confirms this hub's independent read. |
| FC5 | Proposal self-contradicts: §5 "on every heartbeat, a sweep deletes" vs §9 V4 row "no (probes read)" | `:215` | `docs/30 - Design/VOICE-v3-proposal-2026-09-23.md` §5 and §9 V1/V4 rows | **HOLDS** | §5 (scratch lifecycle) reads "on every heartbeat, a sweep deletes any scratch file older than `scratch_max_age_s`"; the V1 row (not V4) is the one that lists "scratch lifecycle + sweep" under `com.cobalt.aset`, while V4's row adds only `voice_stt`/`voice_plan`/`voice_scratch` PROBES under the heartbeat resident — the two sections describe the sweep as belonging to different components; a genuine internal ambiguity, not resolved here (L37 — a house's/derive's call). |
| FC6 | §3 "or his day voice unit" — no such unit exists in the DRC build; only `drc-day/voice-no-trades` on no-trade days | `:216` | `docs/40 - DevDocs/prompts/2026-09-22/50-drc-d3-build.md:10`, `:27` | **HOLDS** | Matches this hub's own `20-drc-build-seam.excerpt.md` staged text verbatim — `drc-day/voice-no-trades` is scoped to no-trade days only; no general "day voice unit" is built. |

Anthropic-seat R1 claims checked: **6 HOLD of 6** (counted in §0).

## Anthropic-seat round-1 claims, file-checked
(pending)

## Experiments named (L70)
| experiment | named by | = proposal E<n> or NEW | gates which slice | result that would change the design |
|---|---|---|---|---|
| E1 | grok (KEEP) | E1 | V1 (T2) | which container/format each device produces over `tailscale serve` HTTPS — a device that fails decodes needs a fallback path |
| E2 | grok (KEEP, CHANGE — adds RSS-beside-88GB measurement) | E2 | V1 (T3, T11) | faster-whisper RSS beside the mainframe's 88 GB wired limit — over budget keeps CPU faster-whisper, never silently adds a second resident |
| E3 | grok (KEEP) | E3 | V1 (T3) | whether phone containers decode with no system ffmpeg — fail makes ffmpeg a named host dependency (L15 gate) |
| E4 | grok (KEEP, CHANGE — adds a think-wrapped-reply case) | E4 | V1 (T4, T6) | parse-valid rate and whether a think-wrapped reply is correctly FAILed, not executed |
| E5 | grok (KEEP) | E5 | V1 (T5) | whether phone/trading-PC browsers have `localService` speech synthesis — none means text-only on that device |
| E6 | grok (KEEP) | E6 | V1 (T3) | whether `/fill`/`/size` latency stalls during a transcribe — stall moves the call to a one-shot job, not a second transcriber |
| E7 | grok (KEEP, CHANGE — adds crash-after-commit case) | E7 | V1 (T8, T10) | scratch sweep behavior on `kill -9`; also whether a crash after `record_stop_edit` commits but before `done` double-applies on restart |
| E8 | grok (CHANGE — reframed from "recorder presence" to "peer identity") | E8 | V1 (T2) | recording the actual socket peer for loopback/tailnet/LAN cases, to prove the peer-address allow key can't be spoofed by a client header |
| E9 | grok (KEEP) | E9 | V2 (T9, item d) | dev-vault proof that `append_to_unit`/`land_pending` are crash-idempotent and never touch his bytes without O1 — any double block or changed byte blocks V2 |
| E10 | grok (KEEP) | E10 | V1 (item c, L15) | full lock diff + licenses for the faster-whisper dependency — an unexpected native/GPL package sends it to tribunal round 2 |
| E11 | grok (KEEP) | E11 | V2 (T12) | whether `trade_id` stays stable across a superseding re-import log |
| X12 | grok (ADD, before V1) | NEW | V1 (T4) | deterministic price-parser test on synthetic dictated numbers ("four fifty" / "4.50") — no model in the loop |
| X13 | grok (ADD, before V1) | NEW | V1 (T6) | race test: tap Confirm + spoken "no" in flight — stop must change at most once, never both `done` and `cancelled` |
| gemini's E1–E11 | gemini (KEEP all, no changes proposed) | = proposal's own | — | gemini kept the proposal's set unmodified; no new experiment or gate change offered |
| Anthropic seat's 16 experiments | fable seat (per its own report, not separately re-derived here — L36 binds this hub to the two houses only) | mixed | — | not re-walked in this collation; its report is the record (`voice-v3-tribunal-fable-r1-2026-09-23.md` `## Experiments (L70)`) |
Proposal's own UNPROVEN rows: F12 (`MediaRecorder`/secure-context/`speechSynthesis` behavior — both houses correctly call it an experiment, not a defect) and F13 (faster-whisper phone-container decoding without ffmpeg — same).

## OWNER ITEMS (after the tribunal)
| # | house | line, verbatim | NAMED/NOT NAMED against the test |
|---|---|---|---|
| 1 | grok | "O1 — a law he owns. Amend L28 so Cobalt may replace his non-blank text outside markers only for the exact voice/text-widget edit he confirms, fold text as in `10-PROPOSAL.md` `## OWNER ITEMS`. No house can change L28. Not a precondition for V1, V2, or V4; only the V3 overwrite class waits." | **NAMED** — "a law he owns," explicit "no house can change L28" |
| 2 | gemini | "O1 — A law he owns: amending L28 to allow voice-ordered overwriting of his non-blank text requires his ruling (no house can decide it)." | **NAMED** — same, word-for-word same reasoning |

Deduplicated: both lines are the same item (O1, the proposal's own owner item), worded independently but substantively identical — one row after dedup. Beside the proposal's own O1 text (`10-PROPOSAL.md` `## OWNER ITEMS`): unchanged by either house. **owner items: 1.**
Neither house named O1 as a precondition to build any slice that does not need it (both explicitly: "Not a precondition for V1, V2, or V4" / not stated as blocking V1/V2). No `RE-OPENS A RULING` text from either house — R18, R92, R93, R99, R100 are all cited as inputs, never re-argued.

## WRONG FACTS claimed
| # | house | claim | file-check verdict |
|---|---|---|---|
| 1 | grok | `10-PROPOSAL.md:17` F2 "no LiteLLM/model-endpoint caller under `src/cobalt`" vs `audit_export.py` litellm/openai grep hit | **DOES NOT HOLD** (C1) — the hit is prose ("the OpenAI house"), not a caller; F2 itself HOLDS |
| 2 | gemini | Same claim | **DOES NOT HOLD** (C2) |
| 3 | grok | `10-PROPOSAL.md:24`/`:102` treat `upsert_region` as the clause-2a blank-only fill; `writer.py:895` is a three-way-merge frontmatter carve-out with no blank-only guard | **HOLDS** (C4/C5) — corroborated independently by the Anthropic seat's WRONG FACT #3 (FC3) |
| 4 | grok | `10-PROPOSAL.md:25` cites `52-drc-d5-build.md:18` for A31; the packet's current anchor is `:21` | **HOLDS** as citation drift (C7) — proposal's own F10 row already flags line numbers move; not a design defect |
| 5 | grok | `10-PROPOSAL.md:201` "the voice module owns only its rows" vs `:89` the voice module is the scratch file writer | Not independently re-derived by this hub (outside the file-check budget of this round); flagged here for the derive to check directly against those two proposal lines |
| 6 | grok | `10-PROPOSAL.md:136` V1 depends on E1–E4, E6, E7, E10 vs `:148-154` E5 and E8 also listed "Before V1" | Not independently re-derived; flagged for the derive |
| 7 | grok | `10-PROPOSAL.md:191` seam entries 1,2,4,5 KEPT vs `:107`/`:186` settling R2-V1 on `land_pending`, and vs `13-v2.excerpt.md:15` where entry 1's first-body alternative is still open | Consistent with this hub's own T12 read — grok's ruling itself resolves entry 1 via `land_pending`, so the "still open" tension is real but already closed by grok's own T9/T12 rulings, not left hanging |
| 8 | grok | `11-draft-digest.md:48`-equivalent packet-size estimate (≈100–110 KB) vs this hub's actual staged total (≈166 KB after all six cuts) | **HOLDS** — see `## Packet`; already listed under ESCALATE |
| 9 | fable seat (FC1–FC6) | see `## Anthropic-seat round-1 claims, file-checked` | **All 6 HOLD** |

## Independence
`grep -c -F -e "-ruling" gemini-ruling.md` → 0. `grep -c -F -e "-ruling" grok-ruling.md` → 0. Neither house opened the other's ruling file (and could not have — GEMINI finished at 09:35:59 ET while GROK was still running, and GROK writes its own file directly via its allow string, never reading GEMINI's). No independence breach.

## ESCALATE
1. **Packet over 100 KB after the cut order.** 166,901 B staged (target ≤100 KB) — see `## Packet` for the full breakdown and why (the MANDATORY core alone, chiefly `02-greps.txt` at ≈69 KB against the drafter's ≈28–32 KB estimate, already exceeds 100 KB). Not a failure per §1's own text; named here as required.
2. **REDACTION count: 0.** `grep -c -E "TSLA|372[.]82|374[.]50"` printed 0 on all 16 staged files; no other ticker/price/share-count/P&L/rule-sentence/config-value of his was found. Named as required even though the count is zero.
3. **DRC FINAL changes both houses ask for, carried not folded (item d).** Seam S2: D3 must call `land_pending(date)` right after create-once of `drc-trades/voice-<trade_id>`/`drc-day/voice-no-trades`; D5-3's `drc-day/open_items` must also render `voice not bound` from `voice_turns` rows. Neither is in the current `50-drc-d3-build.md`/`52-drc-d5-build.md` text (both explicitly say "voice is not in D3/D5," per R100) — this is a change to the DRC FINAL that the desk must place, not a silent edit made here.
4. **The S1 seam-document precondition (blocker to build).** Grok's BUILD AFTER and the Anthropic seat's ESCALATE #2 (independently) both name the same precondition: before V1's build prompt, a seam document must name the ONE model-access module the routing lane extends (L72 P-b, L3) — this is the one item this hub counts as a real blocker to build (see stop line).
5. **Item (d) — a real gap in the proposal-as-written.** `VaultWriter.upsert_region` is not blank-only today (`writer.py:895`, three-way merge + sync-revert win, no `blank_only` guard) — file-checked HOLDS (C4/C5/FC3, three independent reads: grok, the Anthropic seat, this hub). As the proposal currently specifies clause-2a blank-cell fills through unmodified `upsert_region`, a blank-cell voice fill risks landing on the existing sync-revert win and overwriting his bytes with no O1 ruling. Grok's `ADOPT WITH` (`blank_only` flag, ~15 lines) fixes this in the ruling, but the code does not exist yet — must reach the desk before any blank-cell fill (V2/V3) ships, not folded silently.
6. **File-check finding beyond any house's own claim, safety-adjacent (item f premise).** Both houses stated "nothing computes a score, rank, grade, or size" for the one card act voice would trigger. File-checked DOES NOT HOLD as literally stated: `CardStore.record_stop_edit` (`cards/store.py:659-674`) recomputes `shares` via `engine.recompute_for_stop` — a sizing figure. This is pre-existing behavior identical to the page's own human-fed stop edit, not something new the voice design adds, and neither house actually claimed "the design DOES reach the card" (so the strict L52 escalate trigger does not fire) — but their stated premise for item (f) is imprecise, and this bears on how the derive frames whether L52 truly does not bind. Surfaced for the desk/derive to judge (L37 — this hub takes no side).

No `DO NOT BUILD`, no `REJECT` whose claim HOLDS, no path to the trading platform/order/PC-install that HOLDS, no trading-logic/secret/model-judged-approval path that HOLDS, no `RE-OPENS A RULING`, no un-NAMED owner item, no number proposed without its measurement, no owner item written as a precondition, no independence breach, no house that failed to rule, and astra's row is exactly `METER — proceed on three` (no separate listing needed). No `ASK DESK` was raised this round — both houses ruled inside the window with no recovery or retry needed.

VOICE V3 TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER S1 names one module; class audit_export · gemini: TRIBUNAL R1: BUILD AFTER F2 IS CORRECTED TO ACKNOWLEDGE AUDIT_EXPORT · astra: METER — proceed on three · houses that ruled: 2 of 3 · claims that HOLD: 6 · blockers to build: 1 · owner items: 1 · ESCALATE: 6
