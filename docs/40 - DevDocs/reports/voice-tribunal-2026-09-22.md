# VOICE TRIBUNAL — ROUND 1 (2026-09-22)

## §0 Headline
- Both houses ruled `BUILD AFTER`: grok on a missing seam document (L72 P-b), gemini on making `append_to_unit` idempotent — this hub's file-check confirms both underlying claims HOLD, so both are real blockers, not in conflict with each other. Two items SPLIT between the houses (T-V5 binding, T-V9 surface) and one CONTRADICTION ((f) whether a seam document already exists) — grok's side holds the file-check in all three; the blind Fable seat independently converged with grok on the seam-document question.
- Status: DONE. Packet staged, 16 files, 141,739 B (over the 100 KB target even after the full cut order — disclosed, not a failure per the instruction's own clause). REDACTION: 0 hits, all 16 files. Fable R1 claims checked: **6 HOLD of 6** (one with a trivial line-number imprecision).
- Houses that ruled: 2 of 3 (astra: `METER — proceed on three`, not launched, per R13). ESCALATE: 9.

## AUTHORIZATION
All checks run, each its own Bash call, before any staging or launch:
- `grep -n "^| R13 " cto-2026-09-20.md` → :86, carries the rule list this line takes.
- `grep -n "^| R23 " cto-2026-09-20.md` → :206, the grok/agy extension.
- `grep -n "^| R46 " cto-2026-09-21.md` → :57, carries "For the designs and creations we need the higher level models."
- `grep -n "^| R13 " cto-2026-09-22.md` → :135, carries "without Astra".
- `grep -n "^| R92 " cto-2026-09-22.md` → :58, carries "_imports should be a subdirectory of 1 - Trading/5 - Review".
- `grep -n "^| R93 " cto-2026-09-22.md` → :57, carries "DRC every market trading day".
- `grep -n "^| R99 " cto-2026-09-22.md` → :51, carries "his per-trade answer lines sit in their own unit".
- `grep -n "^| R100 " cto-2026-09-22.md` → :50, carries "A, B as soon as possible".
- `grep -n "^| R106 " cto-2026-09-22.md` → :44, carries all three required literals: `DRC-VOICE-PROPOSAL-2026-09-22.md` · `Fable seat: yes` · `seat model: claude-opus-5-5`.
- `git log -1 --format=%H -S"| R106 | " -- cto-2026-09-22.md` → `01b63ffb0a24af061294768ee5d857a2e4fccf00` (non-empty, committed).
- `git log -1 --format=%H -- docs/30 - Design/DRC-VOICE-PROPOSAL-2026-09-22.md` → `1bcc1a899d148031c4f82cad7cbd6a95bffeb397` (non-empty, committed).
- `git log -1 --format=%H -S"DRC VOICE PROPOSED" -- reports/drc-voice-propose-2026-09-22.md` → `1bcc1a899d148031c4f82cad7cbd6a95bffeb397` (non-empty, committed).
- `grep -n "59-voice-tribunal.md" cto-2026-09-22.md cto-2026-09-23.md` → `cto-2026-09-23.md` does not exist (recorded, not fatal); `cto-2026-09-22.md:35` (R115) names it: "`59-voice-tribunal.md` launched in the free house lane (R107 authorizes; window 20:45–23:20 holds)." A `| R` row names the file — gate satisfied.
- `git log -1 --format=%H -S"59-voice-tribunal.md" -- cto-2026-09-22.md cto-2026-09-23.md` → `dbfe49f95dde048b791af53af58fa382c3ebb072` (non-empty, committed).
- **No new rule check**: each of the 14 allow strings and 3 deny strings counted (`grep -c -F -e "<string>"`) against `prompts/2026-09-20/08-bars-chunk-e-check.md` — every count ≥1 (`Bash(grok *)` and `Bash(agy *)` counted 2, as expected); no Sol/Opus checker string (`gpt-5.6-sol`, `claude -p --model claude-opus-5`) present in this launch line.
- **DATE + EXTENSION GATE + WINDOWS**: `date` → Tue Sep 22 21:05:00 EDT 2026 (first row), re-checked Tue Sep 22 21:21:35 EDT 2026 immediately before launch. Both inside 2026-09-22/23, both outside the 19:25–20:45 and ≥23:20 refusal windows.
- `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" cto-2026-09-22.md` → :118, R30 "Approved", his words in quotes, on the desk file (not the drafter's report).
- `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" -- cto-2026-09-22.md` → `055242df8032632dfafdcc8a69dcc271be89c0f6` (non-empty, committed).

Result: every gate ALLOWED. No FAILED condition triggered.

## PREFLIGHT
| Rule | Command | Exit | Allowed / DENIED + reason |
|---|---|---|---|
| Host CLI | `grok --version` | 0 | ALLOWED — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| Host CLI | `agy --version` | 0 | ALLOWED — `1.2.8` |
| Base folder | `ls scratch/tribunal-bars-0920` | 0 | ALLOWED — folder exists, many sibling tribunal dirs present |
| Recovery check | `ls scratch/tribunal-bars-0920/voice-tribunal/r1` | 1 "No such file or directory" | Fresh run confirmed, not a resume |
| Stagger 28 | (no report file; R115 names "28 is not running") | — | ALLOWED — launch-row exception (`cto-2026-09-22.md:35`) |
| Stagger 32 | (no report file; R115 names "32 is not running") | — | ALLOWED — same row |
| Stagger 53–57 | `ls "docs/40 - DevDocs/reports"` — no `drc-d<k>-check-*` name for k=1..5; R115 names all five "not running" | — | ALLOWED — same row |
| Astra probe (gate for astra only, R13) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (run_in_background, 3 min) | 1 | Usage-limit text: "You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM." — matches R13's expected meter-out state exactly. RECORDED: `astra: METER — proceed on three`. Astra NOT launched. |

No house denied at preflight. Grok and Gemini both available.

## Packet
Staged at `scratch/tribunal-bars-0920/voice-tribunal/r1/`. Sizes (`wc -c`, byte-identical where copied, verified against originals):

| File | Bytes | Mark | Note |
|---|---|---|---|
| `00-READING-ORDER.md` | 4,336 | MANDATORY | authored this run |
| `01-QUESTIONS.md` | 12,542 | MANDATORY | verbatim charge + file list |
| `02-greps.txt.part1` | 17,531 | MANDATORY (search) | split — over 38,000 B whole (56,043 B); cut at a heading boundary |
| `02-greps.txt.part2` | 36,254 | MANDATORY (search) | second half |
| `02-greps.txt` | 393 | superseded stub | left in place (cannot delete under this session's own governed Bash patterns); redirects to the two parts, marked "not data" |
| `10-PROPOSAL.md` | 19,980 | MANDATORY | byte-identical to committed original (verified `wc -c` both sides: 19,980 = 19,980); 0 trailing-whitespace lines in the original, 0 disclosed gap |
| `11-propose-digest.md` | 3,907 | MANDATORY | anchors §0 Headline :5, Findings :24, Chunks :35, ESCALATE :44 all verified unmoved by `grep -n` before excerpting |
| `12-rulings.md` | 2,264 | MANDATORY | table header + R92/R93/R99/R100 verbatim, re-found by `grep -n` (lines moved since drafting — R92:60, R93:59, R99:53, R100:52 — real boundaries used, disclosed inside the file) |
| `13-rulings-cited.md` | 3,180 | OPEN-AS-NEEDED | R66/R90/R101 verbatim, re-found |
| `14-devices.excerpt.md` | 3,661 | MANDATORY | devices.md :8,:11,:12,:17,:31 + R27 row |
| `15-drc-v2.excerpt.md` | 10,930 | MANDATORY | all 12 anchors checked with `grep -n`, none moved |
| `20-drc-build-seam.excerpt.md` | 8,478 | MANDATORY | all 5 anchors checked, none moved |
| `21-vaultwrite.excerpt.py` | 5,073 | OPEN-AS-NEEDED | **CUT (v)** applied at staging — reduced from 4 ranges to 2 (`_commit` :457-480 and `create_if_absent` :559-600 dropped; their gist already quoted elsewhere, named inside the file) |
| `22-aset.excerpt.py` | 1,658 | OPEN-AS-NEEDED | **CUT (iv)** applied — reduced from 4 ranges to 2 (docstring, viewport, `/size` route dropped) |
| `23-cited-docs.excerpt.md` | 2,278 | OPEN-AS-NEEDED | **CUT (iii)** applied — reduced from 5 ranges to 2 (assessment audit, MVP Charter, probes.py dropped) |
| `24-migrations.excerpt.py` | 2,112 | OPEN-AS-NEEDED | **CUT (ii)** applied — `placement.py` DECLARED_TABLES range dropped, `__init__.py` kept |
| `27-laws-excerpt.md` | 7,555 | OPEN-AS-NEEDED | **CUT (i)** applied — reduced from 12 laws (L1,L3,L9,L15,L18,L23,L25,L28,L31,L40,L45,L57) to 5 (L1,L3,L23,L25,L28); the 7 dropped laws' gist named as already-quoted-elsewhere inside the file |

**Total (all 16 files, including the stub): 141,739 B ≈ 35,435 tokens (÷4). Total without the stub (the real 15-file reading order): 141,346 B.**

CUT DISCLOSURE: the MANDATORY core alone (00, 01, 02.part1+2, 10, 11, 12, 14, 15, 20 — the files the instruction forbids cutting) already totals 119,883 B, over the 100 KB target before any OPEN-AS-NEEDED file is added. The drafter's own estimate (§ MANDATORY ≈ 75–80 KB) undershot this — chiefly because `02-greps.txt`'s two parts (53,785 B combined) ran far larger than guessed, since several of the pre-computed searches (the DRC build-prompt search, the DRC v2 design search) returned long table-row and quoted-verbatim matches. The full cut order (i)–(v) was applied to all five OPEN-AS-NEEDED files regardless, since doing so still reduces the overage (by roughly 24 KB versus their originally specified ranges) even though it cannot bring the whole packet under 100 KB. Per the instruction's own clause, this is disclosed here and under `## ESCALATE`, not treated as a failure.

REDACTION: `grep -c -E "TSLA|372[.]82|374[.]50"` run on all 16 staged files → `0` on every file. No other ticker symbol, price, share count or P&L of his was found in any staged file during construction (every source file staged was committed code, committed config, a committed design doc, a committed report, or a committed ruling row — never a note, the coach spec, `Rules.md`, or any audio/transcript). No audio, transcript or note-of-his content is staged (per the packet's own NOT-STAGED list). REDACTION count: **0**.

NOT STAGED (per the instruction's own list): any audio, transcript or note of his; the coach spec (cited by `SPEC §n` and keys only inside `10-PROPOSAL.md`, never opened here); his DRC note and his template; `Rules.md`; `configs/dev/aset.local.yaml` (untracked — `git log` prints nothing for it; the proposal's V8 claim about it is staged as a claim, not verified against its content); the DRC v2 design whole, `aset/web.py` whole, `vaultwrite/writer.py` whole, the DRC build prompts `48`–`57` whole (only their cited ranges are staged); any production row.

## Rulings table

| item | grok | gemini | agreement | wording / reason (≤25 words each) |
|---|---|---|---|---|
| T-V1 landing | ADOPT WITH | ADOPT WITH | 2-0 ADOPT WITH, convergent | Both independently require idempotency added to `append_to_unit` — grok: skip if row already landed; gemini: skip if block already at end of unit. |
| T-V2 sync vs job | ADOPT WITH | ADOPT | 2-0 ADOPT (grok narrower) | Grok adds a reap rule for a dead `running` row; gemini defers entirely to V-E5. Not a conflict. |
| T-V3 engine | ADOPT WITH | ADOPT | 2-0 ADOPT | Both: faster-whisper first, Metal engine only if V-E2/V-E3 win it; grok is more explicit that L15 is not yet met. |
| T-V4 fallback | ADOPT | ADOPT | 2-0 ADOPT | One engine, loud pending, retry; no second engine for a rare case. |
| T-V5 binding | ADOPT WITH | ADOPT WITH | **SPLIT** — same item, opposite resolution | Grok: on >1 trade matching a card, capture stays UNBOUND, listed on A31, never guessed. Gemini: binds to the EARLIEST matched trade. Grok's reading is the one the staged D3-2 text supports (see Checked against the files). |
| T-V6 pre-DRC holding | ADOPT WITH | ADOPT | 2-0 ADOPT | Hold in `drc_voice` + imports dir until the note exists; grok adds the date-source rule (never the clock date). |
| T-V7 field mapping | ADOPT | ADOPT | 2-0 ADOPT | Verbatim only; no cue-word split, no shadow mapping this build. |
| T-V8 model provisioning | ADOPT WITH | ADOPT | 2-0 ADOPT | Pinned revision, offline load, model swap = config change + `com.cobalt.aset` restart (L42). |
| T-V9 surface | ADOPT WITH | ADOPT WITH | **SPLIT** — opposite resolution | Grok: NO new tailnet-only gate — `/voice` inherits the existing bind, already covered by the standing backlog access-token item (file-verified). Gemini: ADD a tailnet-only restriction. Grok's position is the one the real backlog item supports (see Checked against the files). |
| T-V10 vocabulary bias | ADOPT | ADOPT | 2-0 ADOPT | Lawful decoding hint stored in `params`; not inference; X6 settles whether it leaks words he didn't say. |
| (a) fact base | ADOPT WITH (many V-rows UNVERIFIED/DOES NOT HOLD from the packet alone) | ADOPT WITH (all V1–V18 HOLD) | disagreement on rigor, not on the underlying facts | Grok's tighter packet-only reading flags V3–V5, V13, V15, V16 as UNVERIFIED FROM THE PACKET (their source docs were cut); this hub's direct file-check (below) found the underlying claims true in every case checked. |
| (b) L3 one path | ADOPT (no second path) | ADOPT WITH (append_to_unit is technically a "second operation" but no second writer) | 2-0, same conclusion | Both agree: one bytes writer, one transcribe function, one unit; audio path and unit path are distinct legs of the same `VaultWriter`. |
| (c) local-first | ADOPT WITH (not yet past L15, pending V-E2/V-E3) | ADOPT WITH (meets L15 if V-E2/V-E3 prove it) | 2-0, same conclusion, different tense | Substantively identical: local engine correct in principle, L15's "proven"/"reviewed-clean" gates still open pending experiments. |
| (d) append-only unit | ADOPT WITH (not idempotent as written; fixed by T-V1; walks market_reset, sync-revert, vanished-trade cases) | ADOPT WITH (not idempotent; fixed by T-V1) | 2-0 ADOPT WITH | Both find the same defect and the same fix; grok's answer is more complete on the sync-revert and market_reset paths. |
| (e) capture surfaces | ADOPT WITH (flags the `str(v)` form-stringify bug risk; NONE for trading-PC install) | ADOPT WITH (NONE for trading-PC install; less detail on the form-parsing risk) | 2-0, grok adds a finding | Neither disputes the other; grok's form-parser risk is a genuine addition gemini did not raise. |
| (f) the seam | ADOPT WITH (NO seam document exists yet; one is owed before D2/V2 launch, 5 "carried not folded" items named) | ADOPT WITH (names `DRC-AUTOMATION-v2-2026-09-22.md` itself as "the ONE seam document") | **CONTRADICTION** | Checked against the files: gemini's claim does not hold against L72 P-b's actual text (a seam document is something "the desk settles… BEFORE either launches" — v2 predates this design and never names `append_to_unit`, the `voice/` question, or A31's home). Grok's reading matches L72 P-b; the Fable seat (blind, independent) reached the same conclusion. |
| (g) the chunks | ADOPT WITH (re-derives migration numbering, confirms 0012/0013 claimed elsewhere) | ADOPT WITH (same, less detail) | 2-0, same conclusion | Both: no assumed migration number, 19h/27h estimate held as the proposal's own (UNVERIFIED), Opus 5 floor for write-path chunks. |
| closing line | `TRIBUNAL R1: BUILD AFTER seam note before D2 or V2` | `TRIBUNAL R1: BUILD AFTER idempotent append_to_unit replaces the byte-prefix check` | both BUILD AFTER, different single condition named | Both closing conditions HOLD in this hub's file-check (below) and are not mutually exclusive — the Fable seat's closing line names both plus the experiments. |

## Wording offered, verbatim
Grok's and Gemini's `ADOPT WITH` replacement wordings and the one `WRONG FACTS` text from each, copied unedited from their ruling files (no user data present, no redaction needed):

**T-V1** — Grok: "the same resolution that made the allow/refuse decision" mechanism is described narratively, not as pasteable wording (grok's T-V1 section is reasoning, not a single replacement sentence — see `grok-ruling.md:7-13` in full). Gemini: `ADOPT WITH a NEW VaultWriter operation append_to_unit(unit_id, block) that is idempotent: if the block is already exactly at the end of the unit (e.g. from a prior crash), it returns success instead of failing.`

**T-V5** — Grok: (narrative, see `grok-ruling.md:40-47`: bind only by the recording control's own key; on ambiguity, stays unbound and listed on A31, never guessed). Gemini: `ADOPT WITH card id during the day → trade through the DRC's card match; if a card matches multiple trades, the capture binds to the earliest trade, unmatched to A31.`

**T-V9** — Grok: (narrative, see `grok-ruling.md:73-80`: no new gate, inherits existing bind and backlog token item). Gemini: `ADOPT WITH the /voice route is restricted to the tailnet only.`

**Grok's WRONG FACTS** (verbatim, `grok-ruling.md:230-236`):
1. `10-PROPOSAL.md:9` says the voice grep hit `generate_constitution.py:291`, covered `dev_utils`, and was a whole-tree read. `02-greps.txt.part1:3-6` searches `src/cobalt`, `configs`, `ops`, and `pyproject.toml`, and the hits are `cards/models.py:240`, `ops/pg_role.py:15`, and `ops/pg_role.py:19`.
2. `10-PROPOSAL.md:15` and `11-propose-digest.md:17` say there is no inbound DM path. `notify/mattermost.py` inside the `:6-11` range they cite (`23-cited-docs.excerpt.md`) says the old module is an 800-line websocket listener. The new module is outbound; the absolute claim is not.

**Gemini's WRONG FACTS** (verbatim, `gemini-ruling.md`, closing paragraph): `10-PROPOSAL.md:55` - "asserts the new body = old body + one separator + the block (a byte-prefix check... deterministic)". Contradicted by vault write idempotency requirements; a byte-prefix check fails upon retry after a crash, meaning it's not truly deterministic/idempotent.

## Checked against the files
Every claim below was checked by this hub directly against the real files under `/Users/cobalt/cobalt/` (Read tool, plus `git log`/`git show` where a committed-vs-branch question arose) — never taken on a house's or the Fable seat's word (L35).

| claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| `dev_utils/generate_constitution.py:291` has a voice-adjacent TODO | grok (WRONG FACTS 1), proposal V1 | `dev_utils/generate_constitution.py:291` | HOLDS | Read directly: line 291 is `* [ ] Build "Ion Voice" for audio alerts.` — real, matches the proposal's own citation exactly. |
| The packet's `02-greps.txt` voice search did not cover `dev_utils` | grok | `02-greps.txt.part1` header command | HOLDS | This hub's own staged search command lists only `src/cobalt configs ops pyproject.toml` — `dev_utils` was omitted, a real packet-construction gap, disclosed here. |
| `notify/mattermost.py` is outbound-only; the OLD tree (`src/cobalt_agent/interfaces/mattermost.py`) is an 800-line websocket listener | grok (WRONG FACTS 2) | `src/cobalt_agent/interfaces/mattermost.py` | HOLDS | File exists, 854 lines (`wc -l`), matches the "800 lines" description already quoted in `23-cited-docs.excerpt.md`'s docstring range. |
| `/voice` is already covered by the standing backlog access-token item (grok, T-V9) vs a new tailnet-only gate is needed (gemini, T-V9) | grok / gemini | `docs/00 - Project/BACKLOG.md:150-151` | grok's claim HOLDS | Read directly: "Access token for the LAN-bound sheet (currently unauthenticated by design/acceptance, see server.bind config comments)." A real, pre-existing, accepted-scope item — supports grok's "inherits the existing bind, no private carve-out" over gemini's new asymmetric gate. |
| D3-2's card match direction is TRADE → nearest prior CARD (so >1 trade can claim one card; a card does not "match multiple trades" the other way) | grok (T-V5) vs gemini (T-V5, inverted direction) | `20-drc-build-seam.excerpt.md` (D3-2, "Card match: `AsetStore.for_date`, nearest prior card, same ticker + direction, within `limits.card_match_window_minutes`") | grok's reading HOLDS | The staged D3-2 text is unambiguous about the match direction; gemini's "a card matches multiple trades" framing is not supported by this text. |
| L72 P-b requires the DESK to settle a shared seam in "a document both prompts cite BEFORE either launches" — this is a document not yet written, not `DRC-AUTOMATION-v2-2026-09-22.md` itself | grok (f) vs gemini (f, names v2 as the seam doc) | `LAWS.md:401-404` (L72, amendment `[amended 2026-09-22, cto-2026-09-22.md R87 P-b]`) | grok's claim HOLDS, gemini's DOES NOT HOLD | Read L72 directly: the seam is settled by the desk "in a document both prompts cite BEFORE either launches" — v2 predates the voice design and cites none of `append_to_unit`, the `voice/` subdirectory question, or A31's home. The Fable seat (blind) reached the identical conclusion independently. |
| A31 ("open items carried forward") is a v2 §13 row the DRC build as drafted (D3) does NOT build | grok (carried-not-folded item 4) | `20-drc-build-seam.excerpt.md` (D3's own "NOT IN D3: … A26–A39 sections other than the ones listed") | HOLDS | This hub's own staged excerpt already carries this line verbatim — grok's finding is file-supported; the same gap was independently re-derived by the blind Fable seat, checked separately below. |
| No STT model exists in `~/.lmstudio/models` (V15) | proposal, all three seats | `~/.lmstudio/models/{mlx-community,lmstudio-community}/*` | HOLDS | This hub ran `ls` directly (not just trusting the packet's frozen-at-drafting claim): only Qwen3.5/3.8 text-model directories present, no speech model. |
| No `ffmpeg`, `whisper*`, or `sox` in `/opt/homebrew/bin` (V16) | proposal, all three seats | `/opt/homebrew/bin` | HOLDS | This hub ran `ls \| grep -iE "ffmpeg\|whisper\|sox"` directly: zero matches, independent of the packet. |
| The lock has no STT/av engine package; `python-multipart`, `huggingface-hub`, `tokenizers` are already locked transitively (V17) | proposal, all three seats | `uv.lock:1983, 2879, 4460, 5310` | HOLDS | This hub's own `02-greps.txt` search (constructed from a direct `grep` on `uv.lock`) already carries this verbatim; re-checked, matches. |

## Fable round-1 claims, file-checked
Checked only after both houses' tables above were written (nothing of this section could reach a house). `tail -n 3` on `voice-tribunal-fable-r1-2026-09-22.md` → last non-blank line starts `VOICE TRIBUNAL FABLE R1 DONE` (verdict `BUILD AFTER the seam document, one landing path, and V-E1–V-E5 plus X1–X9 · adopt: 3 · adopt with wording: 14 · reject: 0`). Its `## Rulings`, `## Self-attack` and `## WRONG FACTS` were read in full. For each `file:line` claim it rests an `ADOPT WITH`, a `REJECT`, or a WRONG FACT on, this hub opened the real file itself:

| FC# | claim (Fable report, its line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| FC1 | T-V1: `_write_with_retry` retries exactly once, re-invoking `build(snapshot)` fresh each attempt, so the idempotency check must sit inside the closure (`voice-tribunal-fable-r1-2026-09-22.md:35`) | `vaultwrite/writer.py:530-549` | HOLDS | Read directly: `for attempt in (1, 2):`, fresh `_snapshot(path)` + `build(snapshot)` each attempt, `NoteChangedOnDisk` caught and retried once — exact match. |
| FC2 | (a) V25: `VaultWriter` has three write ops today — `create_if_absent :559`, `upsert_unit :644`, `upsert_region :918` (`:74`, `:79`) | `vaultwrite/writer.py:559,644,895` | HOLDS (minor line imprecision) | All three defs confirmed by `grep -n "def "`. `upsert_region`'s `def` is at :895, not :918 — Fable's :918 is a line inside the function body, not a wrong fact. |
| FC3 | WRONG FACTS 2: "D2 and D3 land in ONE deploy … D2 alone never deploys", contradicting the proposal's V2/V3 ordering (`:180`) | `docs/40 - DevDocs/prompts/2026-09-22/49-drc-d2-build.md:3` | HOLDS | Read directly: "D2 and D3 land in ONE deploy (v2 §9, grok (b)); D2 alone never deploys." — word-for-word. |
| FC4 | WRONG FACTS 1: A31 is a v2 §13 row the DRC build as drafted (D3) does not build (`:179`) | `20-drc-build-seam.excerpt.md` (D3's "NOT IN D3: … A26–A39 sections other than the ones listed") | HOLDS | Matches this hub's own staged excerpt verbatim; independently converges with grok's carried-not-folded item 4 — a genuine cross-house finding. |
| FC5 | (a) V22: the old tree carries a websocket Mattermost listener, `src/cobalt_agent/interfaces/mattermost.py`, which new-core must not import (`:74`) | `src/cobalt_agent/interfaces/mattermost.py` | HOLDS | File exists, 854 lines (`wc -l`) — matches "800 lines" in the new module's own docstring (`23-cited-docs.excerpt.md`), independently converges with grok's WRONG FACTS 2. |
| FC6 | (f): a seam document is owed before any V2/V3 prompt launches (L72 P-b), naming 8 entries none of which v2 itself settles (`:111`) | `LAWS.md:401-404` (L72) | HOLDS | Same file-check as grok's (f) row above: L72 P-b requires the desk to settle the seam "in a document both prompts cite BEFORE either launches" — a document that does not yet exist. Fable reached this blind, independent of grok's identical conclusion — the strongest convergence in this round. |

Fable R1 claims checked: **6 HOLD of 6 checked** (one, FC2, with a trivial line-number imprecision that does not change the verdict).

## Clock
| time | trigger | running houses since launch | action |
|---|---|---|---|
| 21:21:35 ET | launch | grok 0 min · gemini 0 min | both launched together, `run_in_background` |
| 21:25:14 ET | gemini completion notice | grok ~4 min · gemini DONE | wrote `gemini-ruling.md` byte-identical from stdout |
| 21:38:11 ET | grok completion notice | grok DONE · gemini DONE | confirmed `grok-ruling.md` exists (grok wrote it itself), read its harness output for denial text (none, exit 0) |
| 21:52:40 ET | collate | grok DONE · gemini DONE | file-checked grok/gemini claims (10 rows), read the Fable seat's report, file-checked its claims (6 FC rows) |

## Experiments named (L70)

| experiment | named by | = proposal V-E<n> or NEW | gates which chunk | result that would change the design |
|---|---|---|---|---|
| V-E1 | proposal, grok, gemini, Fable | = V-E1 | V2, W6 | Phone/desk browser mic secure-context test, file-input hand-off, trading-PC mic presence — decides W6 and the recorder markup. |
| V-E2 | proposal, grok, gemini, Fable | = V-E2 | V1 (T-V3) | Engine × model on his real clips: accuracy, latency, RSS, determinism — picks the transcription engine. |
| V-E3 | proposal, grok, gemini, Fable | = V-E3 | V1 (T-V3) | Decode phone's actual audio formats with the chosen engine, no system ffmpeg — a failure makes ffmpeg a named host dependency. |
| V-E4 | proposal, grok, gemini; WIDENED by Fable (X3/X4) | = V-E4, widened | V3 (T-V1, (d)) | His edits above/below/inside a block, a concurrent edit mid-append, an Obsidian Sync revert, a crash between vault commit and row update, a call during `market_reset` — settles idempotency and the refuse-not-merge rule. |
| V-E5 | proposal, grok, gemini; WIDENED by Fable | = V-E5, widened | V2 (T-V2) | `com.cobalt.aset` RSS + first-clip latency with the model loaded and LM Studio serving, plus a concurrent `/fill` request's latency — settles sync-in-request vs one-shot job. |
| X1 | Fable | NEW | T-V2 | Kill the resident mid-transcribe on `cobalt_dev`; separately fault the engine. Settles whether the reap rule alone suffices or the caller must move to a child process. |
| X2 | Fable | NEW | T-V2 | A `/size` POST issued while a transcribe runs in the same process — settles whether the off-event-loop wording is mandatory. |
| X3 | Fable | NEW (V-E4 split) | T-V1, (d) | `land_pending` called twice, a crash injected between the vault write and the row update, two concurrent calls — proves or disproves the idempotency check. |
| X4 | Fable | NEW (V-E4 split) | (d) | An Obsidian Sync revert AFTER a block has landed — does the block vanish silently, and is that detectable. |
| X5 | Fable | NEW | (f), seam entry 1 | A bytes-method write when `<date>/` does not exist, and a `voice/` sub-path write — settles whether D2-2 must create a missing parent and whether a subdirectory is legal. |
| X6 | grok, Fable | NEW (both named it independently) | T-V10 | On his clips, the vocabulary hint on vs off — count hint words appearing in the transcript that he did not say. Any count > 0 turns the bias off. |
| X7 | Fable | NEW | T-V8 | Model load with network disabled (`local_files_only`) succeeds; one model file removed → `FAILED` naming the path. |
| X8 | Fable | NEW | (c), L15 | `uv add faster-whisper` in a scratch worktree, full lock diff — every new transitive package, version and license named against L15's four gates. |
| X9 | grok (named `trade_id` stability question inline, (f) seam entry 4), Fable (X9) | NEW (both named it independently) | (f), seam entry 4 | Re-import a superseding trading log that leaves one trade unchanged — is its `trade_id` identical? If not, every re-import orphans that trade's voice unit. |
| X10 (this hub) | this hub, from the packet-construction gap itself | NEW | (a) | Re-run the voice/whisper/speech/transcri grep including `dev_utils` and `cobalt_agent` — the packet's own pre-staged search omitted both; grok's WRONG FACTS 1 and this hub's direct check (above) already show `dev_utils/generate_constitution.py:291` holds a real hit the packet missed. |

Beside the proposal's own V-E1…V-E5: none were dropped by any seat; V-E4 and V-E5 were widened (Fable), not replaced. UNPROVEN rows V19–V21 (proposal §1) are unanimously confirmed as correctly-framed experiments (V-E1 for V19/V20, V-E2/V-E3 for V21) by all three seats.

## OWNER ITEMS (after the tribunal)

- **W1** capture points (card + `/drc` row, vs `/drc` only) — grok: "as framed", not a precondition. Gemini: "Rec A", no objection. Fable: "framed correctly."
- **W2** audio retention — grok: not raised beyond the proposal's own framing. Gemini: "Rec A." Fable: option B ("deleted once the transcript lands") **conflicts with L57** as the proposal's own §6 argues — flagging a house-adjacent inconsistency inside the proposal's own owner-item framing, not proposing a number.
- **W3** audio home — grok: the "~1 MB per spoken minute" figure is UNCITED, X9(grok's numbering)/V-E3 settles it. Fable: same UNCITED flag, ties it to its own X9(Fable's numbering) real-file measurement. Gemini: "Rec A", no flag.
- **W4** cloud STT fallback — all three: framed correctly, no objection.
- **W5** scope (per-trade only vs also per-day/next-day) — grok: R100 already sets per-trade for this build; the per-day block is a later binding key, not an open choice. Fable: same, and names the target unit R93 already creates (`drc-day/voice-no-trades`) that a later per-day slice should reuse — **new item W9** (below).
- **W6** phone microphone (tailnet HTTPS vs file-input hand-off) — all three: framed correctly, V-E1 decides.
- **Missing / mis-framed, named by grok**: a max upload size and a max clip length are HIS keys (L53), not "engine tunables" as the proposal's §5 frames them — until he sets them, an unbounded upload should FAIL loud rather than pick a default.
- **Missing, named by Fable — W7**: the clip length, transcribe time limit, and upload size limit are his keys (L53), not committed config as the proposal frames them (same substance as grok's item above, independently reached).
- **Missing, named by Fable — W8**: the vocabulary hint on/off switch and the home of his structure list (ties to T-V10 / X6).
- **Missing, named by Fable — W9**: per-day / no-trade voice, via the `drc-day/voice-no-trades` unit R93 already creates — a sub-case of W5 the proposal's own W5 framing did not name.

No owner item was written by any seat as a precondition to BUILD. No claim re-opens R92, R93, R99 or R100.

## WRONG FACTS claimed

| # | claimed by | statement | file:line | this hub's verdict |
|---|---|---|---|---|
| 1 | grok | Proposal V1's grep claim (whole-tree, hit `generate_constitution.py:291`, covered `dev_utils`) does not match what the STAGED packet search (`02-greps.txt.part1`) actually covers (`src/cobalt configs ops pyproject.toml` only, no `dev_utils` hit shown) | `10-PROPOSAL.md:9` vs `02-greps.txt.part1:3-6` | HOLDS as a packet-completeness gap; the UNDERLYING claim in the proposal is independently verified TRUE by this hub (`dev_utils/generate_constitution.py:291` really does read `* [ ] Build "Ion Voice" for audio alerts.`) — the proposal is not factually wrong, the packet's pre-computed search under-covered relative to what the proposal author actually ran. |
| 2 | grok | Proposal's "no inbound DM path" (V6) is stated as an absolute; the OLD tree (not new-core) does carry an 800-line websocket listener | `10-PROPOSAL.md:15`, `11-propose-digest.md:17` vs `src/cobalt_agent/interfaces/mattermost.py` | HOLDS as a precision nuance — the design conclusion (new-core has no inbound path) is unaffected; the absolute phrasing overreaches. Independently confirmed by Fable's V22. |
| 3 | gemini | The proposal's `append_to_unit` byte-prefix check (`10-PROPOSAL.md:55`) is not truly idempotent — a retry after a crash between the vault commit and the row update fails the prefix check | `10-PROPOSAL.md:55` | HOLDS — confirmed by this hub's own read of `_write_with_retry` (FC1 above): the retry re-snapshots and re-builds, so a prefix check computed only from "old body" without checking whether the block is already present will indeed double-count or refuse incorrectly on retry. Independently reached by grok (T-V1) and Fable (T-V1) with the same fix. |
| 4 | Fable | A31 is not built by D3 as drafted, so the proposal's "the DRC lists it under A31" (`:46`, `:60`) needs a home | `DRC-VOICE-PROPOSAL-2026-09-22.md:46,60` vs `20-drc-build-seam.excerpt.md` (D3's NOT-IN-D3 list) | HOLDS — see FC4 above; independently converges with grok's carried-not-folded item 4. |
| 5 | Fable | "D2 and D3 land in ONE deploy … D2 alone never deploys" contradicts the proposal's chunk ordering ("V2 after v2 D2 is merged … V3 after v2 D3") | `DRC-VOICE-PROPOSAL-2026-09-22.md:83` vs `49-drc-d2-build.md:3` | HOLDS — see FC3 above. |
| 6 | Fable | The proposal's own ESCALATE 2 (v2 F17 "not on the tailnet" is stale) is incomplete: the same stale wording also sits in `configs/dev/aset.yaml:33-35` and `src/cobalt/aset/__main__.py:4-6` | `drc-voice-propose-2026-09-22.md:47` vs `aset.yaml:33-35`, `aset/__main__.py:4-6` | UNVERIFIABLE FROM THIS HUB'S STAGED READS this round — `aset/__main__.py`'s comment text beyond what `22-aset.excerpt.py` carries (only `:80-84`) was not staged; this hub did not independently open `__main__.py`'s docstring lines this round to confirm the "NOT Tailscale" wording verbatim. Recorded as a claim to verify at derive/round 2, not dismissed. |

## Independence
`grep -c -F -e "-ruling"` run on each ruling file, one Bash call each:
- `gemini-ruling.md` → **0** hits.
- `grok-ruling.md` → **7** hits — all seven are grok citing the packet's own `12-rulings.md` / `13-rulings-cited.md` files (his already-ruled inputs, staged as part of the packet grok was told to read), never `grok-ruling.md`, `gemini-ruling.md`, or any `*-ruling.partial.md`. Not a breach — grok never opened another house's ruling file. Both houses independent.

## ESCALATE
1. **Packet over 100 KB even after the full cut order (i)–(v)** — 141,739 B total (00's own bytes + the 15-file reading order), against the ≤100 KB target. The MANDATORY core alone (which the instruction forbids cutting) already totals ~119,883 B before any OPEN-AS-NEEDED file, chiefly because `02-greps.txt`'s two parts ran to 53,785 B combined versus the drafter's ≈ 75–80 KB estimate for the WHOLE mandatory core. Disclosed per the instruction's own "not a failure" clause; `ASK DESK: the drafter's size estimate for future voice/DRC-adjacent tribunals should assume the pre-computed search output alone can exceed 50 KB when a design touches several already-ruled, heavily-cross-referenced documents — widen the estimate or narrow the search list next time. [21:52 ET]`
2. **T-V5 SPLIT** — grok (unbound + listed on A31 when a card matches >1 trade, never guessed) vs gemini (binds to the earliest matched trade). This hub's file-check found grok's reading is the one the staged D3-2 match-direction text supports; carried to the derive, not resolved here (L37).
3. **T-V9 SPLIT/CONTRADICTION** — grok (no new gate, `/voice` inherits the existing bind + standing backlog access-token item) vs gemini (add a tailnet-only restriction). This hub's file-check found the backlog item is real and grok's reading is the one it supports; carried to the derive, not resolved here (L37).
4. **(f) CONTRADICTION** — gemini names `DRC-AUTOMATION-v2-2026-09-22.md` itself as "the ONE seam document"; grok and the blind Fable seat both independently conclude no such document exists yet and one is owed before D2/V2 launch (L72 P-b). This hub's file-check of L72 P-b's actual text supports grok/Fable over gemini. Strongest cross-house convergence of the round — carried to the derive.
5. **WRONG FACTS 6 (Fable)** — UNVERIFIABLE FROM THIS ROUND'S STAGED READS (the claim about `aset/__main__.py:4-6`'s exact wording); not dismissed, needs a direct open at derive or round 2.
6. **Owner item convergence, not a precondition**: grok and Fable (W7) independently and separately named the same gap — clip length, transcribe time limit, and upload size are HIS keys (L53), not "engine tunables" as the proposal's §5 frames them. Worth folding into the design's wording even though neither seat made it a precondition to build.
7. Every REDACTION count: **0** (no redaction needed on any of the 16 staged files).
8. Astra's probe row: `METER — proceed on three` (the expected/recorded state, not a refusal) — listed per instruction, not a concern.
9. No `DO NOT BUILD`, no plain `REJECT`, no path to the trading platform, no claim that the design reaches scoring/ranking/grading/sizing that HOLDS, no claim of a second writer or second transcribe path that HOLDS (both houses and Fable confirm one path after the T-V1 fix), no Fable-seat claim that DOES NOT HOLD, no number proposed by a house for one of his keys, no owner item written as a precondition, no `RE-OPENS A RULING`, independence clean, no house failed to rule.

You add no recommendation (L37) — this ESCALATE list and the Rulings table above are what the derive step (`61-voice-tribunal-derive.md`) takes forward.

## CONTINUE
next: none — round 1 complete, both houses ruled, Fable's round-1 claims file-checked, report closed. NEXT STEP, not this hub's: the desk commits this report; when the Fable seat's line is committed too and the derive-seat row is written (R76), the desk fills `61-voice-tribunal-derive.md`'s two placeholders and launches it; Astra reads the derived FINAL on Sat 09-26 (R13).

## Clock (close)
| 21:44:34 ET | close | grok DONE · gemini DONE · astra METER | writing the final stop line |

VOICE TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER seam note before D2 or V2 · gemini: TRIBUNAL R1: BUILD AFTER idempotent append_to_unit replaces the byte-prefix check · astra: METER — proceed on three · houses that ruled: 2 of 3 · claims that HOLD: 10 · blockers to build: 2 · owner items: 10 · ESCALATE: 9
