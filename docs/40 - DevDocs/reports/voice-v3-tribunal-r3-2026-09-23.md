# VOICE V3 TRIBUNAL — ROUND 3 (the last) — hub `voice-v3-tribunal-r3-0923` (Sonnet 5, `claude-sonnet-5`)

## §0 Headline

- **Who ruled:** grok and gemini (2 of 3 houses; both `TRIBUNAL R3: BUILD`); astra SKIPPED — R13 (probe UP, recorded); the Anthropic seat ran blind and is not counted here.
- **Items:** R2-1 **CONVERGED** (2-0 ADOPT N1) · R2-2 **SPLIT** (grok NEITHER, gemini ADOPT N2) · R2-3 **CONVERGED** (2-0 ADOPT A-V5). Converged: 2 of 3.
- **ESCALATE: 11** · redactions by me: 0 · packet 165,691 B (over 160 KB after the full drop order).
- **Anthropic-seat R2 claims checked: 14 HOLD of 14** (C9–C22; none DOES NOT HOLD). Raw rulings staged only under `scratch/` (gitignored); this report carries no user data.

## AUTHORIZATION

Verified 2026-09-23 11:43 ET (each its own Bash call; `date` = `Wed Sep 23 11:43:20 EDT 2026`).

| Check | Result |
|---|---|
| `cto-2026-09-20.md` R13 (13:33 ET, the rule list) | row printed (:86) — "Push and approved everything … the one new rule `Bash(mkdir -p scratch/tribunal-bars-0920)`" |
| `cto-2026-09-20.md` R23 (17:47 ET) | row printed (:206) — `grok`/`agy` through 09-21 |
| `cto-2026-09-21.md` R46 | row printed (:57) — carries `For the designs and creations we need the higher level models` ✓ |
| `cto-2026-09-22.md` R13 | row printed (:150) — carries `without Astra` ✓ |
| `cto-2026-09-22.md` R109 | row printed (:56) — carries `Make all Opus 5.5 for now` ✓ |
| `cto-2026-09-23.md` R18 | row printed (:21) — carries `VOICE v3 DIRECTIVE` ✓ and `Solve this` ✓ |
| `cto-2026-09-23.md` R39 | row printed (:42) — carries `write to everywhere with my confirmation` ✓ |
| `cto-2026-09-23.md` R43 | row printed (:46) — carries `round 3: 3` ✓, `32-draft-voice-v3-r3.md` ✓, `houses rule mechanics only` ✓ |
| second derive's stop line committed | `git log -S"VOICE V3 FINAL DERIVED"` → `82bd946ce6fa2042d75caff1d916e24353c5ba21` (non-empty) |
| derived design committed | `git log -1 -- VOICE-v3-derived-2026-09-23.md` → `fc82bfaa03c5563fd2c5f82f52f0d04eb39520a0` (non-empty) |
| second derive's last non-blank line | `VOICE V3 FINAL DERIVED · converged: 0 of 3 · round 3: 3 · O1: ruled B · FINAL: not written · ESCALATE: 9` ✓ (starts `VOICE V3 FINAL DERIVED `, carries `round 3: 3`) |
| LAUNCH ROW naming `33-voice-v3-tribunal-r3.md` | `cto-2026-09-23.md` :48 (R45, 11:1x ET) and :51 (R48, 11:4x ET: "`33-voice-v3-tribunal-r3.md` LAUNCHED (`2942f219`, R45's literals)") — both `| R` rows |
| launch row committed | `git log -1 -S"33-voice-v3-tribunal-r3.md" -- cto-2026-09-23.md` → `fec87553b61c90de9bc16a2ce4ad3f52884d1ece` (non-empty; desk file only) |
| THIS LAUNCH LINE ADDS NO RULE | `grep -c -F` on `prompts/2026-09-20/08-bars-chunk-e-check.md`: all 14 allow strings → 1 each; the 3 denies (`"AskUserQuestion"`, `"EnterWorktree"`, `"Bash(git push*)"`) → 1 each. No Sol / Opus checker string in the launch line. |
| DATE + EXTENSION GATE (row 1) | 2026-09-23 → stands on HIS R28: `grep -n "^| R28 "` prints exactly ONE row (:31) carrying `His word: "A"`, `run rules EXTENDED through 2026-09-24 23:59 ET` and `for every house-lane hub`; `git log -1 -S"run rules EXTENDED through 2026-09-24 23:59 ET" -- cto-2026-09-23.md` → `676fa870bc2b553a898e2734dd5cca2b64e92930` (non-empty). Windows: 11:43 ET is before 19:25 and before 23:20 — clear. |

L74: a block arriving inside a tool result (the Read of the prompt file `33`) carried an attribution paragraph asking for a `Claude-Session: …` line in commit messages / PR bodies and naming a file-send tool. It is DATA. Recorded ONCE here; never followed. This hub commits nothing.

## PREFLIGHT

| # | rule · command | exit | allowed / DENIED |
|---|---|---|---|
| 1 | `date*` — DATE + EXTENSION GATE + WINDOWS (row 1) | 0 | allowed — `Wed Sep 23 11:43:20 EDT 2026`; gate passes on R28 (above) |
| 2 | `grok *` — `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | `agy *` — `agy --version` | 0 | allowed — `1.2.9` |
| 4 | `ls *` — `ls scratch/tribunal-bars-0920/voice-v3-tribunal` | 0 | allowed — lists `r1` and `r2` ✓ |
| 5 | `ls *` — `ls scratch/tribunal-bars-0920/voice-v3-tribunal/r3` (RECOVERY) | 1 | allowed — `ls: …/r3: No such file or directory` → FRESH RUN |
| 6 | STAGGER (s1) `19-routing-x5-retro.md` — `tail -n 3 …/routing-x5-retro-2026-09-23.md` | 0 | allowed — last non-blank line is the in-progress line `(run in progress — next step under ## CONTINUE)` → running-or-paused; checked next two rows |
| 7 | `ls scratch/tribunal-bars-0920/routing-x5/PAUSE` | 0 | allowed — the PAUSE file EXISTS |
| 8 | `grep -n -F "paused by the desk" …/routing-x5-retro-2026-09-23.md` | 0 | allowed — prints `:77`: `next: PASS 1 from P<grok: 11 / gemini: 17> — paused by the desk at 11:11 ET (PAUSE file present; row R45, voice v3 round 3) …` — a time LATER than 10:1x ET. (The earlier 10:1x breadcrumb line is no longer in the file; only this one line prints.) → **`19: PAUSED by the desk (the :77 line above)`** — continue. The PAUSE file is never touched by me; the desk deletes it after my stop line. |
| 9 | (s2) `20-routing-x1-sonnet-shadow.md` — `reports/routing-x1-shadow-check-2026-09-23.md` | — | not in `ls reports` → report does not exist; `grep -n -F "20 is not running"` prints R40 (:43) and R45 (:48); R45 ALSO names `33-voice-v3-tribunal-r3.md` → **`20: no report — not running (launch row R45)`** |
| 10 | (s2) `29-jev-trial-check.md` — `jev-trial-check-2026-09-<dd>.md` | — | none in `ls reports`; `grep -n -F "29 is not running"` prints R45 (:48), which names `33-voice-v3-tribunal-r3.md` → **`29: no report — not running (launch row R45)`** |
| 11 | (s2) DRC checks `53`–`57` — `drc-d<k>-check-2026-09-<dd>.md` | — | none of the five printed in `ls reports`; `grep -n -F "<nn> is not running"` for 53, 54, 55, 56, 57 each prints R45 (:48), which names `33-voice-v3-tribunal-r3.md` → **`53 … 57: no report — not running (launch row R45)`** |
| 12 | (s3) `28-jev-trial-build.md` — `grep -c -F "Bash(grok *)"` | 0 | prints `0` → `28: not a house hub — does not block` |
| 13 | (s3) `31-jev-trial-probe.md` — `grep -c -F "Bash(grok *)"` | 0 | prints `0` → `31: not a house hub — does not block` |
| 14 | THE CODEX PROBE (run_in_background, 3 min) — `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | allowed — answered `OK`, `tokens used 2,265`, `[exited with code 0]` (11:44 ET) → **`astra: SKIPPED — R13 (probe UP, recorded)`**. Astra is NOT launched. |

No house denied at preflight. No `mkdir` run. The `s2-p2-cards` strings are carried and never used. The Anthropic seat `34` is not a house hub and does not block; a file `voice-v3-tribunal-fable-r3-2026-09-23.md` appears by NAME in `ls reports` — I never open it (blind).

## Packet

Folder `scratch/tribunal-bars-0920/voice-v3-tribunal/r3/` in `~/cobalt-wt/agy-trial` (gitignored; the first Write created it, no `mkdir`). Rounds 1 and 2 are NOT restaged (`../r1/`, `../r2/`); QUESTIONS-R3 says "open only if a ruling turns on it, by a line range". Every staged non-blank body line was verified verbatim against its source by `grep -n -v -x -F -f <source> <staged>` (only the range headers and blank lines print; the corrupted lines found on the way were fixed: one dropped `(`[F-08]`)` in the L37 line, one `R2-2`→`R2-1` slip in the O1 paragraph, and a mangled tail of the design grep block in `greps.txt`). The source files carry 0 trailing-whitespace lines (`grep -c -E "[[:space:]]$"` = 0 on all 15 sources), so the Write tool's stripping changed nothing. Whitespace-only lines are not distinguishable by this check; no other loss is known.

| file | bytes | what | RAW RULING? |
|---|---|---|---|
| `QUESTIONS-R3.md` | 15,859 | the prompt's questions verbatim + "Files in this folder" (mine; it also says which ranges were dropped) | — |
| `greps.txt` | 20,682 | 12 pre-computed searches, full output; top line says this shell's `grep` honours `.gitignore`; none over 400 lines | — |
| `NEEDS-ROUND-3.md` | 18,318 | derive-2 `## NEEDS ROUND 3` :72-129; `## Fold table` :55-70 (R2F-01…10); `## ESCALATE` items 1, 4, 5, 6 :158-170; `cto-2026-09-23.md` rows R39 and R43 | — |
| `hub-checks-r2.md` | 18,153 | round-2 hub rows: C1–C8 :238-252, G1–G13 + K1–K20 :253-298, experiments :299-301, per-item summary rows :148-150 | — |
| `seat-r2.excerpt.md` | 24,271 | the Anthropic seat's round-2 ruling :15-99 (minus `## Withdrawn from round 1`, dropped), ESCALATE item 2 :117, closing line :124 | — |
| `grok-r2-own.excerpt.md` | 10,117 | hub r2 committed copy `### GROK (` :155-211 | **[RAW RULING — Grok's own, for Grok only]** |
| `gemini-r2-own.excerpt.md` | 3,546 | hub r2 committed copy `### GEMINI (` :212-237 | **[RAW RULING — Gemini's own, for Gemini only]** |
| `derived-sections.excerpt.md` | 20,292 | derived design :1-11, :65-72, :76-79, :104-111, :113-127, :152-164, :254-262, :293-303 (ranges :210-241 and :269-290 DROPPED) | — |
| `writer.excerpt.py` | 13,258 | `writer.py` :457-479, :481-554, :596-606, :807-892, :895-989 | — |
| `merge.excerpt.py` | 4,702 | `merge.py` :1-25, :100-135; `store.py` :1-15, :88-110 | — |
| `ops.excerpt.txt` | 7,715 | `com.cobalt.aset.plist` :1-49; `com.cobalt.heartbeat.plist` :1-30, :55-73; `start_aset.sh` :15-35; `heartbeat/runner.py` :126-167 | — |
| `owner-gates.excerpt.py` | 8,778 | `settings/card.py` :1-25; `settings/cli.py` :1-15, :84-110, :182-212; `radar/propose.py` :422-445; `notify/mattermost.py` :1-15, :130-168; `.gitignore` :1-10 | — |
| **TOTAL** | **165,691** | | |

Anchors: every anchor named in the prompt sat on its expected line (`grep -n`): derive-2 :55 / :72 / :131 / :158; hub-r2 :238 / :253 / :299 / :302 / :148-150 / :155 / :212; fable-r2 :15 / :100 / :117 / :124; derived :65 / :76 / :104 / :113 / :152 / :210 / :254 / :269 / :293; `writer.py` :457 / :481 / :530 / :603 / :807 / :817 / :895; `merge.py` :18 / :100; `store.py` :10 / :91; plists :6 / :40 / :42 / :20 / :60; `start_aset.sh` :32; `runner.py` :126 / :133; `card.py` :15; `cli.py` :7 / :84 / :182; `propose.py` :433; `mattermost.py` :130; `.gitignore` :6. **No boundary moved.** Code read from the working tree of `/Users/cobalt/cobalt` (main head `fec8755`, a docs commit).

**Size: 165,691 B — over the 160 KB line.** Drop order applied in full: (i) `derived-sections.excerpt.md` `:210-241` dropped; (ii) `:269-290` dropped; (iii) `seat-r2.excerpt.md`'s `## Withdrawn from round 1` dropped (the same sentences stand under each ruling's own `WITHDRAWN` line). The packet is STILL over 160 KB after the drop order: not a failure, staged as is; listed under `## ESCALATE`. Consequence, stated to the houses in `QUESTIONS-R3.md`: the first-gate experiments' text (E1–E11, X1–X5, X12, X13) is cited by id only.

REDACTION (L32): the `grep -c -E` of `prompts/2026-09-21/73-s3-exits-tribunal.md` §1 (its three literals; not repeated here) printed `0` for every one of the 12 staged files. No other ticker, price, share count or P&L of his found. Redactions made by me: **0**. (The committed round-2 hub copies staged in `grok-r2-own.excerpt.md` already carry the hub's two `[user data]` placeholders, unchanged.) NOT STAGED: any audio, transcript or note of his; the proposal and the derived design whole; the raw `../r2/*-ruling-r2.md` files; any production row.

## CONTINUE

next: none — the run is complete; the last line is the stop line (§4). (Recovery, if this file is relaunched: both `r3/*-ruling-r3.md` files exist and are NEVER re-asked; re-check `wc -c` of the staged files against `## Packet`; go straight to a re-read of this report.)
DONE so far: preflight, authorization, packet (165,691 B), launch, `## Anthropic-seat round-2 claims, file-checked` (C9–C22, 14 HOLD of 14), GEMINI's ruling filed at `r3/gemini-ruling-r3.md` (closing line `TRIBUNAL R3: BUILD`), Gemini independence greps (0, 0) and SCOPE-R39 count (1).
Houses launched together at ≈12:00 ET (`date` read 12:00:31 right after both launch calls; date gate at 11:58:46): GROK task `bieshb7cm` (wrote `r3/grok-ruling-r3.md` itself; FINISHED, notice 12:16:17, ≈16 min; deadline was ≈12:20 ET), GEMINI task `bzs68my8k` (FINISHED 12:02:42).

## Clock

| time (`date`) | trigger | grok min | gemini min | action |
|---|---|---|---|---|
| 11:43:20 | preflight row 1 | — | — | DATE + EXTENSION GATE passes (R28) |
| 11:44:34 | Codex probe completion notice | — | — | probe `OK` → astra SKIPPED (R13, probe UP, recorded) |
| 11:58:46 | DATE + EXTENSION GATE, second row + STAGGER (s1) recheck | none launched | none launched | 09-23 → R28 row present; windows clear; `19` still PAUSED (last line in-progress, PAUSE file present); no new house-hub report in `ls reports` |
| 12:00:31 | launch (`date`, right after both launch calls) | 0 | 0 | GROK `bieshb7cm` and GEMINI `bzs68my8k` launched together, ONE attempt each, deadline ≈12:20 |
| 12:01:52 | claims file-check, after the code reads for C9–C22 (`date`) | ≈1.5 | ≈1.5 | no ruling files yet; writing C9 … |
| 12:02:42 | GEMINI completion notice (task `bzs68my8k`, exit 0) | ≈2 (running) | ≈2 (finished) | Gemini printed a ruling ending `TRIBUNAL R3: BUILD`; I wrote `r3/gemini-ruling-r3.md` byte for byte without the trailing `[exited with code 0]` (checked: `grep -v -x -F -f <task output>` prints only blank lines). No TIMEOUT. |
| 12:03:43 · 12:03:49 · 12:03:54 · 12:04:01 · 12:04:06 · 12:04:12 · 12:04:17 · 12:04:23 · 12:04:28 · 12:04:32 · 12:04:39 · 12:04:44 · 12:04:49 · 12:04:58 | between the claim rows C9→C10, C10→C11, … C21→C22, and after C22 (14 `date` reads, one per gap) | ≈3.5 → ≈4.5 | finished | claims table C9–C22 written row by row; at 12:04:58 `ls r3/` shows no `grok-ruling-r3.md` yet |
| 12:16:17 | GROK completion notice (task `bieshb7cm`, exit 0) | ≈16 (finished) | finished | `r3/grok-ruling-r3.md` present (Grok wrote it itself, closing line `TRIBUNAL R3: BUILD`); no TIMEOUT (deadline ≈12:20) |
| 12:17:57 | before §3 collate (`date`, after Grok/Gemini greps and the `_unified` / old-tree greps) | none running | none running | writing Rulings table, Wording offered |
| 12:20:55 | before `## Checked against the files` … `## ESCALATE` (`date`) | none running | none running | wrote the checks, experiments, OWNER, independence, ESCALATE |
| 12:22:47 | close (`date`) | none running | none running | §0 written; last line replaced with the stop line |
<!--CLOCK-ROWS-END-->

## Rulings table

Two houses ruled (grok, gemini). Astra: `SKIPPED — R13 (probe UP, recorded)`. The Anthropic seat is not counted here (blind; its round-3 report was never read). Agreement rule as the prompt states it: CONVERGED = every house that ruled gave the same answer (same `ADOPT` label, or NEITHER texts shown to be the same mechanism) AND no supporting claim of that answer DOES NOT HOLD in the file-check; otherwise SPLIT.

| item | grok | gemini | agreement across the houses that ruled | NEITHER gist (≤25 words per house) |
|---|---|---|---|---|
| R2-1 | **ADOPT N1** (changed from its round-2 ADOPT B) | **ADOPT N1** | **2-0 ADOPT N1 — CONVERGED** (no supporting claim DOES NOT HOLD) | none |
| R2-2 | **NEITHER** (changed from ADOPT S) | **ADOPT N2** | **SPLIT** (1 NEITHER / 1 ADOPT N2) | grok: N2's span mechanics kept; "takes no retry" out of the law; N2's "no merge baseline … every later write treats it as his" replaced by a `last_after` rule. |
| R2-3 | **ADOPT A-V5** (changed from its round-2 ADOPT B) | **ADOPT A-V5** | **2-0 ADOPT A-V5 — CONVERGED** (no supporting claim DOES NOT HOLD) | none |

**R2-1 lines checked against each house's answer** (`grep -c -F` of the seat's §5 bullet on each ruling file = 1 and 1):
- `§5:` — grok: N1's bullet VERBATIM (count 1). gemini: N1's bullet VERBATIM (count 1).
- `V4:` — under `ADOPT N1` the row is N1's text verbatim (N1's V4 text: "`voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; …" · Depends on: "V1" · RESTARTS: "`com.cobalt.heartbeat` reload (plist in the diff, L42) — it is a 900 s one-shot job (`heartbeat.plist:60-61`), not a resident" · h: 2). DIFFERENCES, quoted:
  - grok: `| **V4 — ops** | … the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |` — the seat's "…" is replaced by the derived §9 V4 row's own remaining words; the seat's "— it is a 900 s one-shot job (`heartbeat.plist:60-61`), not a resident" clause is omitted from the RESTARTS cell; the Write-path and Migration cells ("no (probes read)", "—") come from the derived row, not from N1.
  - gemini: `| **V4 — ops** | … the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; … | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |` — keeps the seat's "…"; omits the same "one-shot job … not a resident" clause; the Write-path and Migration cells come from the derived row.
  - Both rows state count-only ("COUNTS files older than … never deletes").

**R2-2 sub-table (a)–(d):**

| sub-point | grok (NEITHER) | gemini (ADOPT N2) |
|---|---|---|
| (a) span or note | span. 16:40:07 he types in the risk paragraph → a span check still writes the lesson; 16:40:08 he edits the lesson span itself → refused. P's "that one diff" fails once a line typed above the target moves the diff. | span. Note-level binding rejects the edit when he types elsewhere; span-bound sha256 allows it and refuses an edit of the span itself. |
| (b) "takes no retry" | only in §2.6 `[F-09]`, not in the law: with the span check inside `build`, attempt 2 writes only the confirmed span; "the checker verifies the check is inside `build`". | not law: an implementation mechanic; the retry re-reads the snapshot, verifies the span and writes the same span. |
| (c) "remains his" | made operational, but N2's last clause is "the wrong operation": a missing baseline is not "his" — when `last_after` is None the next write takes Cobalt's text (`writer.py:857-859`); its own text: "records no `unit_after` that `last_after` would return … A later write merges against the baseline already on record". | made operational as N2 has it ("records no merge baseline"); the 10:00 / 12:00 / 16:00 walk through `merge3`; a 30-day purge changes `merge3`'s behaviour. |
| (d) Cobalt-owned unit | "the same span-replace as any other field": no `merge3`, no returnable `unit_after`; Cobalt's next write merges against the baseline already on record → his bytes win, override logged; if `last_after` is None → Cobalt's text. Not `append_to_unit`, not today's `upsert_region`. | written by `upsert_region` with no merge baseline; Cobalt's next write "sees a mismatch against its last baseline, triggers `merge3` (human wins), and logs an override … preserving them". |

`FOLD:` lines: **gemini** — `FOLD B:` + N2's text with ONLY the scope clause replaced by SCOPE-R39: the staged suffix "— only when he orders … Nothing else in this law changes." from N2 is present in gemini's file (count 1) and in the seat's report (count 2: FOLD A and FOLD B); SCOPE-R39 present (count 1). **grok** — NEITHER: SCOPE-R39 present VERBATIM (count 1); its text differs from N2's in one clause. N2: "…and records no merge baseline: the replaced text remains his, and every later write treats it as his." grok: "…and records no `unit_after` that `last_after` would return for that unit: the replaced text remains his. A later write merges against the baseline already on record, so on-disk bytes that differ from it are his and win, logged as an override; when `last_after` is None the writer's existing `baseline_missing` path applies Cobalt's new text, the same as a hand edit with no baseline." No `SCOPE ≠ R39` finding for either.

`§6:` lines, quoted: **grok** — `| A Cobalt-owned unit | the one confirmed span-replace: `build` refuses unless the span equals the confirmed before bytes, then writes the confirmed after bytes, no `merge3`, no `unit_after` that `last_after` would return | a Cobalt line he changed is his against the baseline already on record — the next write human-wins and logs an override (L28). `last_after` None stays the existing `baseline_missing` path |`. **gemini** — `| A Cobalt-owned unit | voice edit via `upsert_region` recording no merge baseline | numbers are code; human-wins untouched |`.

**R2-3:** grok slice **V5** (`ADOPT A-V5`, changed from B); gemini slice **V5** (`ADOPT A-V5`, changed from A-V1). `§9:` — both = the seat's V5 row VERBATIM (`grep -c -F` of the full row: grok 1, gemini 1, seat's report 1). `F-07:` — both = "Built in V5 (§9); before V5, `unsupported` with the owner's command named." VERBATIM (counts 1, 1, 1). G10: no house adopts A-V1; gemini itself says "V1 fails on G10", grok says "A-V1 cannot be adopted … G10 is false as worded".

| closing line | grok | gemini |
|---|---|---|
| `TRIBUNAL R3:` | `TRIBUNAL R3: BUILD` | `TRIBUNAL R3: BUILD` |

**Per-item summary rows:**

| item | outcome | why (facts only) |
|---|---|---|
| R2-1 | **CONVERGED — ADOPT N1, 2-0** | same label; no supporting claim DOES NOT HOLD (`## Checked against the files`); the two V4 rows differ from N1's text as quoted above, and the respawn delay is UNVERIFIABLE FROM READS (E7 sharpened) |
| R2-2 | **SPLIT** — grok NEITHER, gemini ADOPT N2 | different answers; the two houses contradict each other on what an absent baseline does (`## Checked against the files` GM9 vs GK9) |
| R2-3 | **CONVERGED — ADOPT A-V5, 2-0** | same label; §9 row and F-07 line verbatim in both; no supporting claim DOES NOT HOLD |

## Wording offered, verbatim

House by house, item by item, UNEDITED. The only change: heading levels of grok's own headings lowered by me so they do not read as report sections (no word changed). No user-data span found in either ruling (the `73` §1 redaction grep = 0 on both); the one `[user data]` in grok's R2-3 is the placeholder it copied from the staged packet, not a redaction of mine.

### GROK (`r3/grok-ruling-r3.md`, whole file)

##### GROK — VOICE v3 tribunal, round 3

##### R2-1 — who deletes crash-leftover scratch audio (L40)

ADOPT N1

I change my round-2 ADOPT B. The age gate is the predicate for a clip still transcribing inside a live process. At a fresh `com.cobalt.aset` start that predicate is false.

Walk, 14:02:00 turn `t-A` writes `t-A.webm`; 14:02:10 `kill -9` mid-transcribe, before the turn's `finally:`; `KeepAlive` relaunches the job. How soon is not in the plist (no `ThrottleInterval` on `com.cobalt.aset`) — the E7 sharpening, not a premise here.

Under B: the start sweep deletes only files older than `scratch_max_age_s`, and the settled refusal keeps that key above `stt_timeout_s`. If `t-A.webm` is still younger than `scratch_max_age_s` when the sweep runs, it is left, and nothing sweeps again until a turn. He does not press until the next morning, so the voice module's per-turn sweep deletes it then and logs one AMBER line. If that press never comes, B never deletes it (the probe only counts). If the relaunch is so late that the file is already older than `scratch_max_age_s`, B deletes it at start and logs AMBER — that branch is E7.

Under N1: the respawned process, before the first request is served, deletes every file in `scratch_dir`, including `t-A.webm`, age unused. One AMBER line names the file (a turn died mid-way). A failed unlink is RED. If the job stays down, the file sits and `voice_scratch` counts it AMBER once it is older than `scratch_max_age_s`.

At a fresh start, no file in `scratch_dir` can belong to a live turn of the new process. Launchd is starting this job because the previous one exited. The only writer is this process's upload handler, and it has served no request. A delete-ALL start sweep is safe.

A per-turn sweep deletes nothing the `finally:` plus that start sweep do not. `finally:` unlinks this turn's file on commit or on any in-process failure. A file whose process died is already gone at the next start. The only residue is an unlink that already failed RED; a later sweep hits that same failure unless the error was transient. That retry is the larger mechanism.

- `KeepAlive` is true (`ops/com.cobalt.aset.plist:42-45`); the heartbeat process imports no voice module and has no `unlink` (`heartbeat/runner.py:41-60`; greps: deleters are `archiver/shadow.py:234`, `redact/secrets.py:280`, `vaultwrite/writer.py:478`, `radar/collector.py:108`, `backup/restic.py:197`).
- The age gate exists so a live clip inside `stt_timeout_s` is not swept. My round-2 (b) already said the start sweep does not need it, because that process's previous transcribe is dead. B still applies the gate there, so a leftover younger than `scratch_max_age_s` survives the only start sweep that crash will get.
- After that skip, B's next deleter is the next turn. `t-A.webm` then waits until the next morning's press — the hole N1 closes inside the same process.
- One unlink function in the voice process serves `finally:` (`VOICE-v3-derived-2026-09-23.md:107`) and the start sweep (L3, L40). A per-turn sweep adds no expert and no file those two do not already cover.
- V4 stays count-only (`:161`, "no (probes read)"). The probe still needs the production directory, the same override pattern as `COBALT_VAULT_PATH` (`ops/com.cobalt.heartbeat.plist:20-21`, `ops/start_aset.sh:32`). The heartbeat job is a 900 s one-shot (`ops/com.cobalt.heartbeat.plist:60-61`), so the V4 restart is a plist reload, not "the heartbeat resident".
- Price against B: V1 drops the age test and the per-turn sweep (same lines, ±0 h); V4 stays 2 h plus the one plist key either position needs.

§5: **Crash leftovers:** the voice module is the ONLY deleter of scratch files (L40): the turn's `finally:` unlink above, and on every `com.cobalt.aset` start, before the first request is served, a sweep that deletes EVERY file in `scratch_dir` — the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover; one AMBER line per file deleted (a turn died mid-way), an unlink that fails is RED (L9). One unlink function serves the turn and the sweep (L3). The heartbeat's `voice_scratch` probe (V4) only COUNTS: files older than `scratch_max_age_s` → AMBER with the count and the oldest age; none → OK; `scratch_dir` unreadable → RED unknown; it never deletes. The probe resolves `scratch_dir` through the voice config's one loader; the production override is carried in `ops/com.cobalt.heartbeat.plist` exactly as `COBALT_VAULT_PATH` is (`:20-21`) and in `ops/start_aset.sh` (`:32`), and the probe's detail line names the directory it read. The config schema refuses `scratch_max_age_s ≤ stt_timeout_s` (L10).

V4: | **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |

##### R2-2 — O1's fold mechanics under SCOPE-R39

NEITHER — the FOLD line below. I change my round-2 ADOPT S. S's span binding stays. "Takes no retry" does not belong in the law. "Remains his" left bare does not stop Attack 2, and N2's "every later write treats it as his" is not what a missing baseline does.

(a) Span, not the note. 16:40:05 the widget reads back the lesson span in that note. 16:40:07 he types a line in the risk paragraph and Obsidian saves. 16:40:12 he says yes. P refuses, because the note changed, and re-reads a span he did not touch. A span check writes the lesson and leaves the risk line. 16:40:08 he edits the lesson span itself: the span no longer equals the confirmed before bytes, the write is refused, and the new before → after is read back. S and N2 both refuse that case. P's "that one diff" does not, once a line typed above the target moves the diff.

(b) Only in §2.6 `[F-09]`, not in the law. 16:40:12 "yes". `_write_with_retry` snapshots and runs `build` (`writer.py:530-553`). The span check sits inside `build`. Before `_commit` (`:464`) Obsidian saves the risk paragraph; attempt 1 raises `NoteChangedOnDisk`. Attempt 2 snapshots again and runs `build` again. The lesson span still equals the confirmed before bytes, so the retry writes those after bytes into the new snapshot and keeps the risk line. It cannot write a span he did not hear. "Takes no retry" refuses that confirm. `[F-09]` still disables the retry; that text stays. The checker verifies the check is inside `build` (the seat's escalate 2). My round-2 K10 stands only if the check runs once, outside `build` (X2).

(c) Made operational, and N2's last clause is the wrong operation. 10:00 a voice edit A→B goes through `upsert_region` and stores `unit_after` = B (`writer.py:963-972`). 12:00 he types C over that span. 16:00 he confirms C→D. `merge3(base=B, human=C, cobalt=D)` — both changed — keeps C and records an override (`merge.py:18-21`). He heard C→D. Nothing changed. The audit says he insisted on C. S's "no Cobalt ownership is created" does not forbid that row. N2's "never a three-way merge" stops this voice write. N2's "records no merge baseline: … every later write treats it as his" does not: when `last_after` is None, `_merge_base` returns missing (`writer.py:857-859`) and the next write takes Cobalt's text (G6). Past retention the same None happens (`store.py` purge of `vault_writes`, "older than 30 days"; `last_after` at `:91-108`).

(d) One op writes a confirmed voice edit into a Cobalt-owned unit: the same span-replace as any other field. `build` refuses unless the located span equals the confirmed before bytes, writes the confirmed after bytes, calls no `merge3`, and inserts no `unit_after` that `last_after` would return for that unit. Not `append_to_unit`. Not today's `upsert_region`. Cobalt's next write of that unit calls `_merge_base` (`:817`). If the pre-voice baseline is still on record, the on-disk bytes differ from it, so his confirmed bytes win and an override is logged (L28, K11) — the same as if he had typed them, including a heartbeat unit that then stays on his sentence. If `last_after` is None (never written, or purged), G6 applies Cobalt's new text. That is the writer's existing path for a hand edit with no baseline, not a second rule.

- P's note refusal fails the 16:40:07 risk-paragraph save. The span sha of before and after bytes is the binding (`[F-09]` already stores that shape). `_commit:464` is not that window (C2, K9).
- I drop "takes no retry" from the law. C1: attempt 2 re-runs `build`. Inside `build`, the retry is safe. `[F-09]` is not re-opened.
- Attack 2 is `writer.py:963-972` plus `merge.py:18-21`. The voice op must replace the span and must not store the after bytes as `unit_after`.
- "Every later write treats it as his" contradicts G6. The law states the real split: a live baseline, his bytes win; `last_after` None, `baseline_missing`, Cobalt's new text applies.
- Cobalt-owned units use that one op (L3). SCOPE-R39 forbids leaving them on "never edited by voice". The next Cobalt write is the merge already in `_merge_base`, not a new owner.
- Price: about 25 lines and 3 tests in `vaultwrite/writer.py` (refuse in `build` unless the span equals the confirmed before; write the after bytes; versioning row with no unit key, as `create_if_absent` does at `:603-604`). Slice V3, +1 h. No new writer. X21's "returns None" passes the G6 bug when a pre-voice row exists; the pass is below.

§6: | A Cobalt-owned unit | the one confirmed span-replace: `build` refuses unless the span equals the confirmed before bytes, then writes the confirmed after bytes, no `merge3`, no `unit_after` that `last_after` would return | a Cobalt line he changed is his against the baseline already on record — the next write human-wins and logs an override (L28). `last_after` None stays the existing `baseline_missing` path |

FOLD: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no `unit_after` that `last_after` would return for that unit: the replaced text remains his. A later write merges against the baseline already on record, so on-disk bytes that differ from it are his and win, logged as an override; when `last_after` is None the writer's existing `baseline_missing` path applies Cobalt's new text, the same as a hand edit with no baseline. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.

##### R2-3 — which slice builds the trading-logic draft-and-send tool

ADOPT A-V5

I change my round-2 ADOPT B. All of the seat's V5 text stands: the targets, the two asks, before-V5 `unsupported`, other targets left to a registry entry, the row, and the `[F-07]` sentence. The two lines below are that row and that sentence.

B names no slice. At 10:41, after V4 has shipped, "set my max risk to [user data]" still gets Plan kind `unsupported`. §2.4 says the change is drafted and sent. §9 never builds a drafter. The kind string is not `refuse`, and the spoken line can name `cobalt settings load --card <file> --sha256 <hash> --apply`, but nothing in the plan ever does it. That is a class non-execution. R18 (a) is "any command". A permanent `unsupported` with no committed slice is that refusal.

A-V1 cannot be adopted. Its apply step is G10: after his "approve", "the existing chat bot executes the trader-run settings apply". `send_dm` posts and returns (`notify/mattermost.py:130-168`); the module has no inbound reader (C8). The token exemption is a trader-run CLI (`settings/card.py:15-16`), not a bot. The only inbound approve handler is the old tree, and it does not call `cobalt settings` (G10). Separately, a radar-style JSON artifact is the wrong file: `--card` / `--optional` hash the file's own bytes before parsing (`settings/cli.py:84-106`). That is G11.

A-V5: V5 is committed, so `unsupported` before it is the same kind a DRC request gets in V1 (`VOICE-v3-derived-2026-09-23.md:159`), and it ends when the slice ships. It is not a ban, and it does not name L7 as one. Orders and the trading platform stay `refuse` (`:72`).

After his "approve": voice has already stopped. He runs `cobalt settings load --card|--optional <file> --sha256 <hash> --apply` himself — trader-run, token-exempt (`settings/card.py:10-16`) — or he says "approve" in the desk chat for that file and that sha256 and the desk runs that same command (L7 as this packet states it). Voice runs neither. No new gate.

- No V1–V4 row builds a drafter (`:158-161`, C5). Leaving §2.4 with no row makes the drafter permanent prose. I drop B on that ground.
- G10 is false as worded, so A-V1's text is not adoptable. What applies the change is the existing CLI, under the gate it already has.
- `data/` is gitignored (`.gitignore:6`). `write_artifact` (`radar/propose.py:433-438`) is the directory precedent only; the draft is the owner's card or optional file, not that JSON.
- `send_dm` not-sent returns `SendResult(False, …)` (`mattermost.py:147-152`, the disabled channel). The turn says so, AMBER. Nothing is applied.
- Other trading-logic targets (radar notes, a config in git) stay `unsupported` and the reply names the owner command (`radar/propose.py` apply, C7; a build and a deploy). A later target is a registry entry plus that owner's draft function, not a voice change and not `refuse`.
- Price is the seat's, labeled GUESS: about 40 lines in `src/cobalt/settings/`, about 60 in the voice tool, 4 h, depends on V1, not on O1. Totals become 26 h, ≈36 h at ×1.4, still UNVERIFIED. RESTARTS `com.cobalt.aset` plus every resident whose entrypoint imports `cobalt.settings`; the grep lists more than `aset/config.py` and `radar/evaluate.py` (`heartbeat/probes.py`, `radar/runner.py`, `aset/web.py`). The AST walk is the list (L42), not the two examples.

§9: | **V5 — trading-logic drafts** | `trading_logic: true` registry tools for the `--card` / `--optional` settings keys; owner-drafted file in `data/voice-drafts/` + sha256 + per-key diff; `send_dm` card with the owner's exact apply command; applied only by `cobalt settings load … --sha256 … --apply` (his hand, or the desk on his L7 approve) | no (a gitignored draft file; the owner's own apply is unchanged) | — | V1 | `com.cobalt.aset` (+ residents importing `cobalt.settings`, AST walk) | 4 |

F-07: Built in V5 (§9); before V5, `unsupported` with the owner's command named.

OWNER: none. R2-1 is which process unlinks scratch. R2-2 is fold mechanics; R39 already ruled the scope. R2-3 is which slice builds the drafter. None is his money, his data, his time, or a law no house can decide, and none is a precondition for a slice that does not need it.

EXPERIMENTS: E7 (sharpened), X20, X21, and the G2 / K5 run stand as already named. No new run.
- X21 (sharpened, R2-2): the named pass "`_baseline` returns None" is the G6 bug when a pre-voice row exists — `last_after` None makes the next upsert apply Cobalt's text (`writer.py:857-859`). Pass: the voice row is not what `last_after` returns for that unit; disk is the confirmed after bytes; a following upsert against a live baseline keeps those bytes and writes one `vault_overrides` row. Fail: the confirm itself leaves the span unchanged and logs an override (merge kept the hand edit), or the voice row's `unit_after` equals the after bytes.

TRIBUNAL R3: BUILD

### GEMINI (`r3/gemini-ruling-r3.md`, whole file; printed by the house, filed by me byte for byte; no redaction needed)

**R2-1**
ADOPT N1
Under B, the start sweep (shortly after 14:02:10) is age-gated (`older than scratch_max_age_s`). At 14:02:10, `t-A.webm` is 10s old, so it survives the start sweep. It waits until the next morning, when he presses the widget and the next turn's sweep deletes it, logging AMBER.
Under N1, the start sweep runs unconditionally before serving requests. So it deletes `t-A.webm` immediately at respawn (shortly after 14:02:10), logging AMBER.
At a fresh `com.cobalt.aset` start, no turn of a new process is live (it hasn't accepted requests yet), so any file present is a leftover. A delete-ALL start sweep is safe.
The `finally:` block unlinks files for normal turn completions and normal exceptions. A per-turn sweep deletes nothing else: any crash leftover was already deleted by the start sweep when launchd respawned the process. Thus N1 is correct.
`§5:` **Crash leftovers:** the voice module is the ONLY deleter of scratch files (L40): the turn's `finally:` unlink above, and on every `com.cobalt.aset` start, before the first request is served, a sweep that deletes EVERY file in `scratch_dir` — the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover; one AMBER line per file deleted (a turn died mid-way), an unlink that fails is RED (L9). One unlink function serves the turn and the sweep (L3). The heartbeat's `voice_scratch` probe (V4) only COUNTS: files older than `scratch_max_age_s` → AMBER with the count and the oldest age; none → OK; `scratch_dir` unreadable → RED unknown; it never deletes. The probe resolves `scratch_dir` through the voice config's one loader; the production override is carried in `ops/com.cobalt.heartbeat.plist` exactly as `COBALT_VAULT_PATH` is (`:20-21`) and in `ops/start_aset.sh` (`:32`), and the probe's detail line names the directory it read. The config schema refuses `scratch_max_age_s ≤ stt_timeout_s` (L10).
`V4:` | **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; … | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |

**R2-2**
ADOPT N2
(a) If binding is note-level, his typing elsewhere while a confirm is pending rejects the voice edit. Span-bound sha256 allows him to type elsewhere (the span is unchanged) but correctly refuses if he edits the target span itself.
(b) `_write_with_retry` (writer.py:530) runs `build()`. If the span check is inside `build()`, a retry just reads the new snapshot, verifies the span, and writes the *same* span he confirmed. A retry is safe design; "takes no retry" is not law.
(c) If "remains his" is left bare, a 10:00 voice edit is recorded as a `unit_after` baseline. At 12:00 he hand-edits it. At 16:00 Cobalt writes. `merge3` uses the 10:00 baseline, sees his 12:00 edit beat Cobalt's, logs a `vault_overrides` row, and applies his 12:00 edit. If the 30-day purge drops the 10:00 baseline, `merge3` behaves differently. N2 correctly makes it operational: "records no merge baseline" so it remains his text functionally, leaving no `unit_after`.
(d) SCOPE-R39 means his confirmed voice edit into a Cobalt-owned unit is written by `upsert_region`. If it records no merge baseline (no `unit_after`), Cobalt's NEXT write of that unit sees a mismatch against *its* last baseline, triggers `merge3` (human wins), and logs an override for his voice-edited bytes, preserving them. This perfectly obeys L28.
`§6:` | A Cobalt-owned unit | voice edit via `upsert_region` recording no merge baseline | numbers are code; human-wins untouched |
`FOLD:` FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no merge baseline: the replaced text remains his, and every later write treats it as his. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.

**R2-3**
ADOPT A-V5
R18 (a) says "ANY command he asks". If a valid domain command gets `unsupported` and there is NO committed slice to ever build it, that is functionally a permanent class refusal, violating R18 (a). A slice MUST be committed.
V1 (gemini): claims the existing chat bot executes the settings apply. But `hub-checks-r2.md` and greps (`notify/mattermost.py`) show `send_dm` is outbound only. There is no inbound approve handler in the new core, and L7 says the desk relays approvals to the owner's apply command. V1 fails on G10.
V5 (Anthropic seat): names a 4h slice explicitly. It uses owner-drafted file + sha256 + per-key diff, and a `send_dm` card. The owner applies it manually with `cobalt settings load ... --apply`, perfectly matching the L7 hand gate.
`§9:` | **V5 — trading-logic drafts** | `trading_logic: true` registry tools for the `--card` / `--optional` settings keys; owner-drafted file in `data/voice-drafts/` + sha256 + per-key diff; `send_dm` card with the owner's exact apply command; applied only by `cobalt settings load … --sha256 … --apply` (his hand, or the desk on his L7 approve) | no (a gitignored draft file; the owner's own apply is unchanged) | — | V1 | `com.cobalt.aset` (+ residents importing `cobalt.settings`, AST walk) | 4 |
`F-07:` Built in V5 (§9); before V5, `unsupported` with the owner's command named.

TRIBUNAL R3: BUILD

## Anthropic-seat round-2 claims, file-checked
Done WHILE the houses ran. Each row: the REAL file opened with the Read tool on main's working tree `/Users/cobalt/cobalt` (head `fec8755`, a docs commit) plus `grep -n`; the seat's line numbers are those of `reports/voice-v3-tribunal-fable-r2-2026-09-23.md`. The Anthropic seat's ROUND-3 report is NEVER read here (blind); its round-2 report is the file under check. Numbering continues round 2's C1–C8.
| # | claim (seat r2 line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| C9 | (R2-1; seat r2 `:20`, `:30`) `ops/com.cobalt.aset.plist` sets `RunAtLoad` true and `KeepAlive` true (`:40-43`); `com.cobalt.heartbeat` is a one-shot job every 900 s (`heartbeat.plist:60-61`), not a resident | `ops/com.cobalt.aset.plist:40-43`; `ops/com.cobalt.heartbeat.plist:23-44,60-61,66-67` | **HOLDS** (static keys) · respawn DELAY after `kill -9` **UNVERIFIABLE FROM READS** | aset: `RunAtLoad` `<true/>` :40-41, `KeepAlive` `<true/>` :42-43. heartbeat: no `KeepAlive` key; `StartInterval` 900 (:60-61), `RunAtLoad` true (:66-67), runs `cobalt jobs run … heartbeat beat`. Run = derived E7 sharpened. |
| C10 | (R2-1; seat r2 `:22`) derived §5 `:107` names the upload handler "the voice module's one file writer" and unlinks in a `finally:` on every in-process exit | `docs/30 - Design/VOICE-v3-derived-2026-09-23.md:107` (staged `derived-sections.excerpt.md`) | **HOLDS as design text** (no voice code exists yet) | Quote: "written by the upload handler (the voice module's one file writer — not a vault write, not the DRC bytes method) → read by the Transcriber → **UNLINKED in a `finally:` right after the transcript row commits, or on any failure of the turn**". A `kill -9` runs no `finally:` — that is the crash case. |
| C11 | (R2-1; seat r2 `:26`) `ops/com.cobalt.heartbeat.plist:20-21` carries `COBALT_VAULT_PATH` as an env override, and `ops/start_aset.sh:32` exports it | `ops/com.cobalt.heartbeat.plist:20-21`; `ops/start_aset.sh:32` | **HOLDS** | heartbeat.plist :20 `<key>COBALT_VAULT_PATH</key>`, :21 `<string>/Users/cobalt/Vault/Think</string>`; start_aset.sh :32 `export COBALT_VAULT_PATH="/Users/cobalt/Vault/Think"`. (The aset plist itself carries only `COBALT_ENV`; the export is in the launcher.) |
| C12 | (R2-1; seat r2 `:30`) `heartbeat/runner.py:133` runs `sheet_http`, the probe that goes RED when `com.cobalt.aset` is down | `src/cobalt/heartbeat/runner.py:131-133`; `src/cobalt/heartbeat/probes.py:128-144` | **HOLDS** | `sheet_http` does `urlopen("http://127.0.0.1:5010/")` with a timeout; 200 → `Probe(…, True, …)`, any other code or an exception ("unreachable") → `Probe(…, False, …)`. It samples once per beat (900 s). |
| C13 | (R2-2 Attack 1; seat r2 `:40`) `_write_with_retry` (`writer.py:530-554`) re-snapshots and re-runs the SAME `build` callable on attempt 2 (`:535-537`), so a check placed inside `build` runs again on the retry | `src/cobalt/vaultwrite/writer.py:530-554` | **HOLDS** | `for attempt in (1, 2): snapshot = _snapshot(path)` (:535-536); `built = build(snapshot)` (:537) on each pass; `NoteChangedOnDisk` on attempt 1 → `continue` (:547-552). A check inside `build` re-runs against the fresh snapshot. = C1. |
| C14 | (R2-2 Attack 2; seat r2 `:41`, `:49`) `upsert_region` writes a `unit_after` row keyed (note, section, unit) (`writer.py:963-972`); `store.last_after` reads it (`store.py:91-103`); `_baseline` returns it (`writer.py:807-810`) | `writer.py:963-972`, `:807-810`; `store.py:91-109` | **HOLDS** · = C6 in part | Same lines as C6. What C14 adds: the key is `section=section_label`, `unit=region_id` (:964-965) and `last_after` takes the NEWEST row with `unit_after IS NOT NULL` (`store.py:102-105`). `upsert_unit` does the same at `writer.py:766`. Nothing else is new. |
| C15 | (R2-2 Attack 2; seat r2 `:41`) `merge.py:14-19` and `:100-121`: when only the human changed a region against the base, the human's text is kept, and an override row is recorded | `vaultwrite/merge.py:14-26`, `:100-135`, `:141-159`; `store.py:214`; `writer.py:498-506`; `greps.txt` `vault_overrides` | **HOLDS** | :16-17 "region only the human changed → the human's version is kept"; :23-26 an override is recorded when `human != base` and base non-empty; `emit_group` appends the `Override` (:109-123, conflict False when Cobalt left the lines alone). The row is INSERTed at `store.py:214`. The seat's scenario base=B, human=C, cobalt=D takes the "replace" branch (:141-155): human wins, override (conflict True). |
| C16 | (R2-2 Attack 2; seat r2 `:41`) `vault_writes` rows are purged after 30 days (`store.py:10-11`, the purge at `:245-256`), so `last_after` returns nothing past retention (`store.py:96-97`) | `store.py:10-11`, `:33`, `:96-98`, `:247-256`; `writer.py:444`, `:566`, `:667`, `:923`, `:1134` | **HOLDS** | `RETENTION_DAYS = 30` (:33); `DELETE FROM vault_writes WHERE ts < now() - make_interval(days => %s)` (:253); the writer calls `_purge_once` itself. `last_after` → None when no row exists (:96-98) — but only if no NEWER `unit_after` row for the key survives. `vault_overrides` is never purged. |
| C17 | (R2-2 (d); seat r2 `:49`) `create_if_absent`'s versioning row carries `section=None` and `unit=None` (`writer.py:596-606`), a row `last_after` never matches | `writer.py:598-608`; `store.py:102-105` | **HOLDS** | The call passes `section=None, unit=None, before_section=None, after_section=text, overrides=[]` (:603-607); no `unit_after` is passed (default None). `last_after` requires `note = %s AND section = %s AND unit = %s AND unit_after IS NOT NULL`, so a NULL-section, NULL-`unit_after` row never matches. |
| C18 | (R2-3; seat r2 `:69`) `.gitignore:6` ignores `data/`, and `radar/propose.py:433` `write_artifact` writes to `data/radar-proposals` by default | `/Users/cobalt/cobalt/.gitignore:6`; `src/cobalt/radar/propose.py:433-438` | **HOLDS** | `.gitignore:6` is `data/`. `write_artifact(artifact, *, directory: Path = Path("data/radar-proposals"))` (:433) does `directory.mkdir(parents=True, exist_ok=True)` and writes `<kind>-<digest>.json` (:435-437). |
| C19 | (R2-3; seat r2 `:62`, `:69`) `settings/cli.py:6-7` documents `load --card\|--optional <file> [--sha256 <hash>] --dry-run \| --apply`; `:84` `load_optional_file`; `:182-209` `cmd_load`; `:304-316` the flags; `settings/card.py:281-290` refuses `--apply` without `--sha256` | `src/cobalt/settings/cli.py:6-7`, `:84`, `:182-212`, `:303-319`; `src/cobalt/settings/card.py:281-290` | **HOLDS** (flag range off by one) | cli.py :6 `--card <file> [--sha256 <hash>] --dry-run \| --apply`, :7 the same for `--optional`; :84 `def load_optional_file`; :182 `def cmd_load`; the flags are :303-317 (`--card` :303, `--sha256` :313-317), not :304-316. card.py :285-288: `--apply` without `--sha256` → `SystemExit("… requires --sha256 <hash of the reviewed file>")`. |
| C20 | (R2-3; seat r2 `:64`) `settings/card.py:4-8` names the card keys the seat calls "the five card keys", and `:10-16` the token exemption | `src/cobalt/settings/card.py:1-16` | **HOLDS** | Key names at :4-8: `radar.cards_enabled`, `card.proposed_key`, `card.curves`, `card.alignment_default`, `card.shadow_promotion_bar` (five). :10-16: `THE WRITE PATH IS HIS HAND` … "A trader-run apply is exempt from the HITL token (L28, amended 2026-09-15)". |
| C21 | (R2-3; seat r2 `:69`) `notify/mattermost.py:147-152` returns a not-sent `SendResult` when the channel is disabled | `src/cobalt/notify/mattermost.py:147-152` | **HOLDS** | `if not cfg.enabled:` (:147) logs a WARNING "message NOT sent" (:148-151) and `return SendResult(False, "channel disabled in configs/cobalt/notify.yaml", safe.hits)` (:152). |
| C22 | (R2-3, V5 RESTARTS; seat r2 `:72`) `aset/config.py` and `radar/evaluate.py` import `cobalt.settings`; name every other importer the grep prints | `greps.txt` (`grep -rln -e "cobalt.settings" -e "from cobalt import settings"`) | **HOLDS** as far as it names them · completeness **UNVERIFIABLE FROM READS** (needs the L42 AST walk) | Both named files print. The grep prints 22 files. Others: `cli.py`, `settings/{card,models,__init__,cli}.py`, `cards/{scoring,shadow_report}.py`, `daymode/config.py`, `heartbeat/probes.py`, `dayopen/checks.py`, `replay/{runner,movers,line,cli}.py`, `radar/{runner,evaluate_cli,audit_export,notes}.py`, `aset/{web,radar_panel}.py`. A grep hit is a string match, not an entrypoint import; the seat's list omits `heartbeat/probes.py`, `aset/web.py`. |

Count: **Anthropic-seat R2 claims checked: 14 HOLD of 14 checked** (C9–C22; two carry a stated limit: C9's respawn DELAY and C22's entrypoint-import completeness are UNVERIFIABLE FROM READS, not contradicted; C19's flag range is off by one line). None DOES NOT HOLD.
## Checked against the files

Real files opened by me (Read / `grep -n`) on main's working tree (`/Users/cobalt/cobalt`, head `fec8755`). `= C<n>` / `= G<n>` / `= K<n>` = the same as a row above or in `hub-checks-r2.md`; the file was still opened. A claim about how the unbuilt voice code, launchd, Obsidian or a speech engine BEHAVES = UNVERIFIABLE FROM READS + the run (L70). Arguments that are readings of a law (L40, R18) and carry no file claim are not rows.

**Gemini**
| # | claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| GM1 | R2-1 under B `t-A.webm` (10 s old at 14:02:10) survives the age-gated start sweep · gemini | `NEEDS-ROUND-3.md` B text; the config refusal `scratch_max_age_s ≤ stt_timeout_s` | **HOLDS as B's logic** · the ages are UNVERIFIABLE FROM READS | Follows only if `scratch_max_age_s` exceeds the file's age at respawn (10 s + respawn delay). Both are tunables with no value staged; respawn delay = E7 sharpened. |
| GM2 | R2-1 under B the next turn's sweep deletes it and logs AMBER · gemini | B text: "at the start of every turn it deletes … (AMBER line per file …)" | **HOLDS** (as B's own wording) | Design text; no voice code exists. |
| GM3 | R2-1 under N1 the start sweep deletes `t-A.webm` immediately at respawn, AMBER · gemini | N1 §5 bullet (`seat-r2.excerpt.md`); `ops/com.cobalt.aset.plist:40-43` (= C9) | **HOLDS as N1's text** · "immediately" UNVERIFIABLE FROM READS | `KeepAlive` true holds; the respawn delay is behaviour (E7 sharpened). |
| GM4 | R2-1 at a fresh start no turn of a new process is live, so any file is a leftover · gemini | derived `:107`; N1 text; `ops/com.cobalt.aset.plist:29-30`; `ops/start_aset.sh:69` | **HOLDS as design text** · one adjacent behaviour UNVERIFIABLE FROM READS | The plist carries `AbandonProcessGroup` true and the launcher ends `exec uv run python -m cobalt.aset`. Whether a killed job can leave a python child alive is not read → hub-noted run H1. |
| GM5 | R2-1 `finally:` covers normal completions and exceptions; a per-turn sweep deletes nothing else · gemini | derived `:107` (= C10) | **HOLDS as design text** | Grok's wording differs: "The only residue is an unlink that already failed RED" (`grok-ruling-r3.md:17`). Both quoted, neither smoothed. |
| GM6 | R2-2 (b) `_write_with_retry` (`writer.py:530`) runs `build()`; a retry re-reads the snapshot and can write the same confirmed span · gemini | `writer.py:530-554` (= C1, C13) | **HOLDS** | `for attempt in (1, 2)`: fresh `_snapshot`, `build(snapshot)` each pass. Holds only when the span check sits inside `build`. |
| GM7 | R2-2 (c) a 10:00 voice edit stored as `unit_after`; at 16:00 `merge3` uses it, sees the 12:00 hand edit beat Cobalt's, logs a `vault_overrides` row, applies the 12:00 edit · gemini | `writer.py:963-972`; `store.py:91-109`, `:214`; `merge.py:141-155` (= C14, C15) | **HOLDS on read** for an op that stores a keyed `unit_after` | The op is unbuilt; the walk follows the read code. |
| GM8 | R2-2 (c) a 30-day purge that drops the 10:00 baseline makes `merge3` behave differently · gemini | `store.py:33`, `:247-256`; `writer.py:857-859`, `:947-948` (= C16) | **HOLDS** | `last_after` None → `_merge_base` returns `missing`; `upsert_region` then takes base = the human's text, so `merge3` lets Cobalt's text apply. |
| GM9 | R2-2 (c) N2's "records no merge baseline" means the text "remains his text functionally, leaving no `unit_after`" · gemini | `writer.py:857-859`, `:947-948`, `:725-729`; `merge.py:141-159` | **PARTLY HOLDS** | For text no Cobalt op writes, nothing overwrites it. For a unit or region a Cobalt write covers, `last_after` None ⇒ base = human ⇒ Cobalt's next text applies. Contradicts GK9's reading of N2; quoted both, smoothed by neither. |
| GM10 | R2-2 (d) his confirmed edit into a Cobalt-owned unit "is written by `upsert_region`" · gemini | `writer.py:895-918`; `writer.py:644-661`; seat r2 `:51` (price assumes an `expect_before` mode on `upsert_region`) | **PARTLY HOLDS** | `upsert_region`'s docstring: "Do NOT reach for this anywhere a marker would work — `upsert_unit` is the write path; this is the frontmatter carve-out" (:917-918). Holds only as a NEW mode of it. |
| GM11 | R2-2 (d) with no baseline recorded, Cobalt's NEXT write "sees a mismatch against its last baseline, triggers `merge3` (human wins), and logs an override … preserving them" · gemini | `writer.py:724-733`, `:745-766`, `:771-773`; `merge.py:141-159`; `store.py:102-105` | **PARTLY HOLDS** · beyond the first next write UNVERIFIABLE FROM READS + run H2 | First next write: base = the older Cobalt `unit_after`, human = his bytes → human wins, override. That write stores `unit_after: merged_body` (= his bytes, :766; comment :771-772 "advances the baseline"). By the read, a second Cobalt write then has base = human and Cobalt's text applies (`merge.py:157-158`). |
| GM12 | R2-3 `send_dm` is outbound only; no inbound approve handler in the new core · gemini | `notify/mattermost.py:130-168` (= C8); old tree `cobalt_agent/interfaces/mattermost.py` | **HOLDS** | `grep -c -F "cobalt settings"` on the old-tree handler file = 0 (= G10). |
| GM13 | R2-3 L7 says the desk relays approvals to the owner's apply · gemini | `LAWS.md` L7 `:57` | **HOLDS** | "the hub executes on the desk's relay". |
| GM14 | R2-3 "V1 fails on G10" · gemini | hub row G10 (`hub-checks-r2.md`) | **HOLDS** (= G10) | G10 is DOES NOT HOLD as worded; gemini now agrees. |
| GM15 | R2-3 V5 = "4h", owner-drafted file + sha256 + per-key diff, `send_dm` card, owner applies with `cobalt settings load … --apply` · gemini | `seat-r2.excerpt.md` (`:67-75` of the seat report); `grep -c -F` on the row = 1 | **HOLDS** (as the seat's text) | Its §9 row and F-07 line are the seat's verbatim. |

**Grok**
| # | claim · who | file:line | verdict | note |
|---|---|---|---|---|
| GK1 | R2-1 `KeepAlive` true (`aset.plist:42-45`); no `ThrottleInterval` on `com.cobalt.aset` · grok | `ops/com.cobalt.aset.plist:40-45`; `greps.txt` (launchd keys) (= C9) | **HOLDS** (range +2) | `KeepAlive` `<true/>` is :42-43; :44-45 is `StandardOutPath`. The keys grep prints `RunAtLoad`, `KeepAlive` only: no `ThrottleInterval`, no `ExitTimeOut`. |
| GK2 | R2-1 the heartbeat imports no voice module and has no `unlink` (`runner.py:41-60`); the five deleters · grok | `heartbeat/runner.py:41-60`; `greps.txt` (= K2, K3) | **HOLDS** | Imports list has no voice module; the deleters grep prints exactly the five files named. |
| GK3 | R2-1 one unlink function serves `finally:` (derived `:107`) and the start sweep · grok | derived `:107` (= C10) | **HOLDS as design text** | — |
| GK4 | R2-1 V4 stays count-only (`:161`, "no (probes read)") · grok | derived `:161` | **HOLDS** | The V4 row reads "no (probes read)". |
| GK5 | R2-1 the heartbeat job is a 900 s one-shot (`heartbeat.plist:60-61`) so V4's restart is "a plist reload, not the heartbeat resident" · grok | `ops/com.cobalt.heartbeat.plist:60-61`; derived `:161` RESTARTS cell "the heartbeat resident" | **HOLDS** for the one-shot fact (= C9) · "plist reload" is N1's wording, no run | The derived V4 RESTARTS cell does read "the heartbeat resident". |
| GK6 | R2-2 (a) a line typed ABOVE the target changes "that one diff" · grok | `writer.py:311-319` (`_unified` = `difflib.unified_diff`) | **HOLDS on read** for a unified-diff hash | A unified diff carries hunk headers with line numbers; the pending action's hash is design (§2.6 `diff_sha256` vs `[F-09]` `target_sha256`). |
| GK7 | R2-2 (b) with the check inside `build`, attempt 2 re-runs `build` and writes the confirmed span, keeping the risk line · grok | `writer.py:530-553` (= C1, C13, K10) | **HOLDS** on read · "Obsidian saves the risk paragraph before `_commit`" UNVERIFIABLE FROM READS | What Obsidian writes while he types is behaviour (derived E9's "his edit during an append"). |
| GK8 | R2-2 (c) 10:00 A→B stores `unit_after` B; 12:00 C; 16:00 C→D: `merge3(B, C, D)` keeps C and records an override (`merge.py:18-21`) · grok | `writer.py:963-972`; `merge.py:18-21`, `:109-155` (= C14, C15) | **HOLDS** on read | Unedited-base `replace` opcode → `touched` → `emit_group` → override with `conflict=True`. |
| GK9 | R2-2 (c) when `last_after` is None `_merge_base` returns missing (`writer.py:857-859`) and the next write takes Cobalt's text (G6); the same past retention · grok | `writer.py:857-859`, `:947-948`, `:725-729`; `merge.py:157-158`; `store.py:96-98`, `:247-256` (= G6, C16) | **HOLDS** | `_MergeBase(text=None, missing=True)`; `upsert_region` :947 sets base = the human's lines; `merge3(human, human, cobalt)` writes Cobalt's text. |
| GK10 | R2-2 (d) X21's "`_baseline` returns None" passes the G6 bug when a pre-voice row exists · grok | `store.py:102-105`; `writer.py:807-810` | **HOLDS** | `last_after` = newest row with non-null `unit_after` for (note, section, unit): a voice op writing no keyed row leaves the older row current. |
| GK11 | R2-2 (d) his confirmed bytes win against the baseline on record and an override is logged, "including a heartbeat unit that then stays on his sentence" · grok | `writer.py:724-733`, `:745-766`, `:771-773`; `merge.py:141-159` | **PARTLY HOLDS** · "stays" UNVERIFIABLE FROM READS + run H2 | First write: yes (as GM11). By the read, that write advances the baseline to his bytes, so the following Cobalt write applies Cobalt's text with no new override. |
| GK12 | R2-2 `create_if_absent`'s versioning row carries no unit key (`:603-604`) · grok | `writer.py:598-608` (= C17) | **HOLDS** | `section=None, unit=None`. |
| GK13 | R2-2 price: about 25 lines + 3 tests in `writer.py`, slice V3 +1 h · grok | seat r2 `:51` (the seat's own price) | **UNVERIFIABLE FROM READS** | An estimate, copied from the seat; no file settles it. |
| GK14 | R2-3 a DRC request gets `unsupported` in V1 (derived `:159`) · grok | derived `:158-161` (= K14) | **HOLDS as a reading** | `:159` is the V2 row (DRC by voice); the V1 row (:158) has no DRC work. |
| GK15 | R2-3 `send_dm` posts and returns, no inbound reader; the only inbound approve handler is the old tree and it does not call `cobalt settings` (G10) · grok | `notify/mattermost.py:130-168`; old-tree handler (= C8, G10) | **HOLDS** | Old-tree file: 0 hits for "cobalt settings". |
| GK16 | R2-3 `--card` / `--optional` hash the file's own bytes before parsing (`settings/cli.py:84-106`) · grok | `settings/cli.py:84-110` | **HOLDS** | `read_bytes()` (:98) → `sha256` (:101) → mismatch refusal (:108-110) before parsing. |
| GK17 | R2-3 `.gitignore:6`; `write_artifact` at `radar/propose.py:433-438` · grok | `.gitignore:6`; `propose.py:433-438` (= C18) | **HOLDS** | — |
| GK18 | R2-3 `SendResult(False, …)` on a disabled channel (`mattermost.py:147-152`) · grok | `mattermost.py:147-152` (= C21) | **HOLDS** | — |
| GK19 | R2-3 RESTARTS: the grep lists more than `aset/config.py` and `radar/evaluate.py` (`heartbeat/probes.py`, `radar/runner.py`, `aset/web.py`) · grok | `greps.txt` (importers) (= C22) | **HOLDS** | All three print. Entrypoint imports = the L42 AST walk. |
| GK20 | R2-3 no V1–V4 row builds a drafter (`:158-161`, C5) · grok | derived `:158-161` (= C5, K14) | **HOLDS** | — |
| GK21 | R2-3 totals 26 h, ≈36 h at ×1.4 · grok | derived `:163` (22 h, ≈31 h) | **HOLDS** as arithmetic (22 + 4; 26 × 1.4 = 36.4) · the hours are GUESS | The derived text labels its hours GUESS / UNVERIFIED. |

## Experiments named (L70)

| experiment | named by | = | gates | the result that would change the design |
|---|---|---|---|---|
| E7 (sharpened): `kill -9` `com.cobalt.aset` LESS than `scratch_max_age_s` after the upload, no later turn | grok ("stand as already named") | = round-2 E7 sharpening (derived E7) | V1 | the file survives the start sweep → the sweep is age-gated, contrary to N1 |
| X20: unlink mid-transcribe (informational) | grok | = round-2 X20 | none (would set the cost of an out-of-process deleter) | transcript fails or completes; changes nothing under N1 |
| X21 (sharpened by grok): pass = the voice row is not what `last_after` returns for that unit, disk is the confirmed after bytes, a following upsert against a live baseline keeps those bytes and writes ONE `vault_overrides` row; fail = the confirm leaves the span unchanged and logs an override, or the voice row's `unit_after` equals the after bytes | grok | = round-2 X21, with a NEW pass/fail text (replaces "`_baseline` returns None", which grok says passes the G6 bug) | V3 overwrite class | a merged span or a returnable baseline → the op merges, contrary to the fold text |
| G2 / K5: a sweep firing while a long synthetic clip transcribes, age key ≤ STT-timeout key | grok ("stand as already named") | = round-2 G2/K5 (NEW at round 2) | V1 config check | the file is unlinked under the Transcriber |
| gemini | — | — | — | gemini named none and wrote no `EXPERIMENTS:` line |
| **H1** (hub-noted file fact, NOT house-named): `kill -9` the pid of `com.cobalt.aset` on the home server, then list processes for a surviving `python -m cobalt.aset` child (`aset.plist:29-30` `AbandonProcessGroup` true; `start_aset.sh:69` `exec uv run python -m cobalt.aset`) | none (hub) | NEW | V1's delete-ALL start sweep (N1's "no turn of a new process is live") | a surviving child that serves turns → a start sweep can delete a live turn's file |
| **H2** (hub-noted, NOT house-named): on the dev vault + `cobalt_dev`, a confirmed voice edit into a Cobalt-owned unit, then TWO Cobalt writes of that unit | none (hub) | NEW (X21-shaped; bears on GM11 / GK11) | V3 overwrite class into Cobalt-owned units | whether his confirmed bytes survive the second Cobalt write |

## OWNER answers

| house | line, verbatim (redacted) | NAMED / NOT NAMED | precondition to build |
|---|---|---|---|
| grok | "OWNER: none. R2-1 is which process unlinks scratch. R2-2 is fold mechanics; R39 already ruled the scope. R2-3 is which slice builds the drafter. None is his money, his data, his time, or a law no house can decide, and none is a precondition for a slice that does not need it." | NAMED (says none passes the owner test, per item) | no |
| gemini | no `OWNER:` line | NOT NAMED (absent) | no |

No line re-states or narrows O1's scope.

## Independence

One Bash call each: `grep -c -F -e "-ruling"` on `gemini-ruling-r3.md` → 0; `grep -c -F -e "grok-r2-own"` on `gemini-ruling-r3.md` → 0; `grep -c -F -e "-ruling"` on `grok-ruling-r3.md` → 0; `grep -c -F -e "gemini-r2-own"` on `grok-ruling-r3.md` → 0. No house opened another's ruling (it could not: no name appears in either file). No `READ ANOTHER RULING`.

## ESCALATE

(no recommendation added)
1. **Supporting claims that PARTLY HOLD (none DOES NOT HOLD):** gemini R2-2 ADOPT N2 rests on GM9, GM10, GM11; grok's R2-2 NEITHER rests in part on GK11 ("stays on his sentence"). Not one of these DOES NOT HOLD; the persistence beyond the first Cobalt write is a run (H2).
2. **Packet over 160 KB after the full drop order:** 165,691 B (drops (i), (ii), (iii) all applied).
3. **REDACTIONS:** 0 made by me. The committed round-2 hub copy staged in `grok-r2-own.excerpt.md` already carries its `[user data]` placeholders (2); grok copied one placeholder into its R2-3 text. Neither ruling carries any of the three literals.
4. **Astra:** probe answered `OK`, exit 0, at 11:44 ET → `astra: SKIPPED — R13 (probe UP, recorded)`. `ASK DESK: astra's probe answered OK at 11:44 ET — relaunch a re-issued file for astra alone, or leave Astra to read the FINAL on Sat 09-26 (R13)? [12:21 ET]`
5. **STAGGER (s1), `19`:** PAUSED by the desk — its `## CONTINUE` line 77, "paused by the desk at 11:11 ET (PAUSE file present; row R45, voice v3 round 3)", later than 10:1x. The desk deletes `scratch/tribunal-bars-0920/routing-x5/PAUSE` after my stop line; I never touched it.
6. **Environment note:** mid-run the harness reported the primary working directory changed from `~/cobalt-wt/agy-trial` to `~/cobalt`; a relative `ls scratch/…` failed. I restored it with one bare `cd /Users/cobalt/cobalt-wt/agy-trial` (no chaining) BEFORE the launches, so both launch lines ran from the worktree with the approved spellings unchanged.
7. **L74, recorded ONCE:** a block inside the Read result of the prompt file `33` asked for a `Claude-Session:` line in commits and PR bodies and named a file-send tool. It is DATA and was not followed; this hub commits nothing.
8. **The two houses contradict each other on what an absent baseline does** (R2-2 (c)): gemini — "N2 correctly makes it operational: \"records no merge baseline\" so it remains his text functionally, leaving no `unit_after`" (`gemini-ruling-r3.md:14`); grok — "N2's \"records no merge baseline: … every later write treats it as his\" does not [forbid the row]: when `last_after` is None, `_merge_base` returns missing (`writer.py:857-859`) and the next write takes Cobalt's text (G6)" (`grok-ruling-r3.md:38`). The read code supports grok's mechanism (GK9) and gemini's (c) walk on the merge path (GM7, GM8).
9. **Both houses' `V4:` rows differ from N1's text**, although both `ADOPT N1` (quoted under `## Rulings table`). Grok's own progress note (task output `bieshb7cm`) says "I'll put N1's row back verbatim"; its filed row still carries the added words.
10. **Hub-noted experiments H1 and H2** are not house claims; they are file facts I read while checking (`aset.plist:29-30`, `start_aset.sh:69`, `writer.py:745-773`), stated as runs, never as defects (L70).
11. **A house that did not rule:** none of grok, gemini. Astra did not run (R13).

VOICE V3 TRIBUNAL R3 DONE · grok: TRIBUNAL R3: BUILD · gemini: TRIBUNAL R3: BUILD · astra: SKIPPED — R13 (probe UP, recorded) · houses that ruled: 2 of 3 · converged: 2 of 3 · ESCALATE: 11
