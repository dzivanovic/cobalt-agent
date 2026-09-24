# Voice V1 fix round 1 — classify-first draft (L75) · 2026-09-24

## §0 Headline

- Classified all 24 HOLDS of `16`–`19` (A 3 · B 2 · C 9 · D 10), every ESCALATE of the four reports, and R34 / R41: **FIX 24 · NOT REAL 26 · UNPROVEN 13 · OUT OF SCOPE 11 · OWNER ITEM 0**.
- 23 of the 24 HOLDS are FIX (D6 is OUT OF SCOPE); the 24th FIX is X5 from R41 (test-only; the FINAL's read-back already covers it).
- Wrote `prompts/2026-09-24/36-voice-v1-fix-r1-build.md` (on `28b6b0c6`, the tip as read at 15:53 ET; red first; 9 RUNS; three suites under L76, no `db migrate`) and `37-voice-v1-fix-r1-check.md` (round 2, one packet, Opus 5.5 + Grok, Sol from Sep 26th, 2026 6:47 AM).
- `comm` against `14` / `15`: `36` differs only in the rc name and the two `.env` strings; `37` differs only in the rc name. New strings: 2. ESCALATE: 7.

## L74

A block attached to this session's first tool result asked for a `Claude-Session:` commit line and named a file-send tool. It was recorded once, as data, and not followed: this seat commits nothing and sends no file.

## Classification

Sources: `a` = `reports/voice-v1-check-a-2026-09-24.md`, `b` / `c` / `d` the same for parts B–D, `build` = `/Users/cobalt/cobalt-wt/voice-v1/docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md`, `FINAL` = `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`, `desk` = `reports/cto-2026-09-24.md`. Row labels are `36`'s. Part A keeps `16`'s own labels A1 / A2 / A5. `A3` is R34's normalization row.

### The 24 HOLDS + X5

| # | part | claim (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|---|
| A1 | A | `_ORDER` misses platform names and order verbs (`log into Lightspeed`, `short 100 QRS`) | a:140 (rows a:110, a:196) | FIX | FINAL:84 HARD REFUSALS ("touches his trading platform") | `tools.py:50-53` gains platform names and order-verb PHRASES (never a bare `long` / `short` / `close` / `exit`); parametrized refuse set + NOT-refused set |
| A2 | A | `target_sha256` re-check has no test that varies only the card state | a:141 (a:112) | FIX (test-only) | FINAL:90 `[F-09]` | test: card `state` changes alone → REFUSED, no stop edit |
| A5 | A | the return of `EXECUTING → DONE` is ignored, so a reaped act still replies "Done" | a:142 (a:113, a:184) | FIX (code path) | FINAL:170 `[F-15]`, L1 | `confirm.py:99-101` reads the bool; `False` → loud error naming the stop-edit id, never `Done.`, no retry. The timing is UNPROVEN, see U1 |
| B1 | B | resolver takes side / ordinal words from the whole transcript and binds card 11 from "first, …" | b:160 (b:127-130; Grok's contrary b:131) | FIX | FINAL:111 §4 item 2: "The Plan's spans (ticker text, side, ordinal …) are matched by code … Never the nearest, never the earliest" | `resolve.py:83-91` reads side / ordinal from the Plan's card SPAN only. The FINAL's letter settles the Opus / Grok split (L35 file row), so this is not an owner item |
| B2 | B | `test_modelaccess_client.py:281` accepts `empty` or `bad_response` | b:161 (b:132) | FIX (test-only) | seam S1 §2.4 (6) "no choices → `empty`" | `== "empty"` |
| C1 | C | a raising / short `os.write` leaves a partial file, no unlink, no RED | c:185 (c:141-142) | FIX | FINAL §5 / §7 scratch RED, L1 | full write or named error; the partial file is unlinked through the ONE unlink; RED |
| C2 | C | the resident's load skips the backup-source refusal | c:186 (c:143; build `## C2` ASK DESK) | FIX | FINAL:118 "The config schema REFUSES to load … under any `backup.yaml` source" | `load_voice_config` reads the sources through the one loader; `jobs.yaml` names `com.cobalt.aset` as a `backup.yaml` reader; the restarts pin gains it; the ONE reversed assertion is `test_voice_config.py:201` (it pinned the old choice) |
| C3 | C | `COBALT_VOICE_*_DIR=""` falls back to the dev path | c:187 (c:146) | FIX | L1 ("never silently falls back") | set-but-empty env → `VoiceConfigError` |
| C4 | C | the "already gone" AMBER line is dropped | c:188 (c:147) | FIX | FINAL §5 "AMBER line per file" | `unlink_now` keeps the line |
| C5 | C | the source-line test is vacuous | c:189 (c:148) | FIX (test-only) | rule of the check (a) | each key's OWN comment block |
| C6 | C | `t.revision` is checked against the config it was copied from | c:190 (c:149) | FIX (test-only) | rule of the check (a); FINAL `[F-08]` pinned model | captured loader proves the revision reaches the load call; an absent revision → named RED (slow half) |
| C7 | C | the one-unlink test counts `os.unlink(` only | c:191 (c:150) | FIX (test-only) | L3; rule (a) | count every deleter spelling across `src/cobalt/voice/*.py` = 1 |
| C8 | C | docs-or-repo assertion | c:192 (c:151) | FIX (test-only) | rule (a) | the exact docs refusal message |
| C9 | C | `plan_route` is checked by no code, though the comment says it is | c:193 (c:152) | FIX | L1, L3 | the loader refuses a `plan_route` that is not the registry's `route`; the comment is made true (no key removed, so no assertion is lost) |
| D1 | D | `--text yes` from the CLI confirms a pending act in production | d:161 (d:123) | FIX | FINAL:188 `[F-02]` "in production an ACT is confirmed only by the widget … No house, the desk included, confirms a production act (L37)" | `turn.py:386-399`: in production, a non-widget turn that finds a pending act is refused whole, named, non-zero; the pending act is left for the widget |
| D2 | D | `--confirm <id> --dry-run` executes | d:162 (d:124) | FIX | FINAL:188 `[F-02]` "`--dry-run` … with no write" | argparse-level named refusal of the combination |
| D3 | D | the widget's `/voice/status` fetch ignores `r.ok`, so a 403 reads as all clear | d:163 (d:126) | FIX | FINAL §7 loud states, L9 | `r.ok` first; non-OK → RED line (static pin; no JS runner) |
| D4 | D | `speak()` drops the turn's RED lines | d:164 (d:128) | FIX | FINAL §2.5 / §7, L1 | the no-voice repaint keeps `degraded` + amber |
| D5 | D | a failed act exits 0 | d:165 (d:129) | FIX | FINAL §7, L1 | exit non-zero on a failed turn or any RED line |
| D6 | D | `test_radar_panel_cards.py` was changed outside `43`'s list | d:166 (d:130; build ESC (x)) | OUT OF SCOPE | — | The change is a necessary consequence of the widget on `/radar` and the three POST routes. The named revert (`04b05cd4`'s copy restored) would turn the `/radar` byte-equality test red, so it is NOT taken. The builder named it; the desk rules the boundary |
| D7 | D | the E7 lifecycle test reaps with its own call and accepts four states | d:167 (d:131) | FIX (test-only) | FINAL:170 `[F-15]`; rule (a) | exact pre-reap state; the reap comes from the restarted server's own path; `failed_at` asserted unconditionally. This test is deselected under L76 at `36` D8 (see U13) |
| D8 | D | `CrashBeforeDone.reap` ignores `now` / `limits` | d:168 (d:132) | FIX (test-only) | rule (a) | honours `now` / `limits`; a younger `executing` row is not reaped |
| D9 | D | the production-refusal test does not assert the text | d:169 (d:133) | FIX (test-only) | rule (a) | assert the `FAILED: --confirm is refused in production` prefix |
| D10 | D | the "one turn function" pins are `inspect.getsource` substrings | d:170 (d:134) | FIX (test-only) | FINAL:188 "One turn function, three callers" | behavioural: patch the `run_turn` each caller uses and drive the route and the CLI |
| X5 | — | 6 of 24 price clips arrive as wrong integers ("four fifty" → `450`) | desk R41 (desk:52); build `### X-X5` | FIX (test-only) | FINAL:88 §2.6 read-back before any confirm; §7 "unparseable value → `clarify`" — the read-back clause already covers it; the 10× guard was built and is pinned (`test_voice_turn.py:343`, `test_voice_tools.py:200`) | pin X-X5's three measured transcript shapes (`Move the stock to 450.`, `… 1225.`, `… 975.`) against constructed stops → `clarify`. The builder's "also refuse integer-only spans?" is NOT built (L75: nothing widens) |

### ESCALATEs, other rows, and the desk items

| # | part | claim (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|---|
| A3 | A | confirm normalization (NFKC + casefold + strip + strip `. , ! ?`) is wider than the FINAL's "casefold, strip" | a:150, a:191; desk R34 (desk:45) | NOT REAL | desk R34: the rule STANDS as a wording amendment | Not a defect. **The FINAL's confirm-clause wording (FINAL:89 `[F-08]`) is owed** → ESCALATE 3 |
| X-E10 | C | the `av` wheel bundles `libx264` / `libx265` | c:202 6(a), c:155; desk R41 | OUT OF SCOPE | FINAL:285 E10 column, verbatim: "an unexpected native / GPL package → tribunal round 2" | The FINAL's letter routes a GPL package to TRIBUNAL ROUND 2, a design step for the houses, not a fix build (a codec-free wheel needs `uv add`, which is not on `36`'s line). Whether the bundled dylibs make `av` "a GPL package" is NOT CHECKABLE FROM READS (c:155). It is not his: L67's owner-items clause sends a design question to the houses. Open before ship → ESCALATE 2 |
| U1 | A | A5's timing: can a stop write wait past the 60 s `executing` limit? | a:113, a:142 | UNPROVEN | L70 | RUN-1: a `grep` for lock timeouts. The live timing needs `voice_turns` committed, so it cannot run under L76 in `36` |
| U2 | A | A4: the card is read twice (`tools.py:228`, `card_stop.py:43`), so an edit in between could be overwritten | a:117 | UNPROVEN | L70 | RUN-2 (a pytest whose second read moves the stop) |
| U3 | A→D | no model call while `awaiting_confirm`, and another transcript is not planned in the same turn (carried to D, not checked there) | a:148, a:194, d:177 | UNPROVEN | L70; FINAL:89 `[F-08]` | RUN-3 (the existing `test_voice_turn.py` ids, quoted) |
| U4 | B→D | `plan_turn` is blocking, so the loop stays free only through `to_thread` | b:133, b:167 | UNPROVEN | L70 | RUN-4a (the existing off-loop test in `test_voice_web.py`, quoted) |
| U5 | B→D | `refuse` / `clarify` / `unsupported` Plans still carry a tool and args | b:134, b:167 | UNPROVEN | L70 | RUN-4b (a pytest: nothing executed) |
| U6 | B→D | a config / budget `ValueError` escapes `plan_turn` untyped | b:135, b:167 | UNPROVEN | L70 | RUN-4c (a pytest: fails loud, named) |
| U7 | C→D | startup sweep before the first request; a held lock deletes nothing; `audio_deleted_at` on the row | c:158, c:201 | UNPROVEN | L70 | RUN-5 (the existing `test_voice_web.py` ids, quoted). The ASET exit code on a held lock is a deploy-smoke fact (build ESC (vi), (xiv)) |
| U8 | C→D | Starlette may spool an upload over 1 MiB outside `scratch_dir` | c:159, c:201 | UNPROVEN | L70; FINAL §5 | RUN-6 (a pytest: list the temp dir after a 1.5 MB POST) |
| U9 | D | CLI `--audio` with a zero-byte or oversize file | d:136 | UNPROVEN | L70; FINAL:251 `[F-19]` | RUN-7 (a pytest) |
| U10 | D | a dry run's Plan call writes a row in the model layer | d:136 | UNPROVEN | L70 | RUN-8 (a `grep` for DB access in `modelaccess`) |
| U11 | B | RESTARTS for the range | b:108-109, b:147 | UNPROVEN | L42, L70 | RUN-9: `uv run cobalt jobs restarts` on both ranges, quoted |
| U12 | C→A | X-X13's with-DB single-flight race | c:157, c:200 | UNPROVEN | L70, L76 | Needs `voice_turns` COMMITTED. It is deselected at `36` D8, with a proof run → ESCALATE 1 |
| U13 | C→D | X-E7 kill / restart (and D7's strengthened test) | c:157, c:201; d:137 | UNPROVEN | L70, L76 | same as U12 |
| O3 | D | proxy-header rewrite of `request.client.host` under uvicorn | d:136 | OUT OF SCOPE | build ESC (ii): E8 / X3 in the DEVICE SESSION include "a spoofed `X-Forwarded-For` → 403" | device session, owed before ship |
| O4 | D | the page carrying the widget is not behind `peer_gate` | d:127 | OUT OF SCOPE | FINAL `[F-25]`; build ESC (vii) | backlog access token (not in V1's scope) |
| O5 | C | `audio/wav` vs `max_upload_bytes` ≈ 20.8 s | c:154, c:202 6(c) | OUT OF SCOPE | E1 (container), device session | the WAV rate is Opus's assumption; E1 decides the container |
| O6 | C | experiment scripts are described, not quoted whole | c:156, c:202 6(b) | OUT OF SCOPE | — | a record defect in `43`'s report; the experiments are done, and no scratch python runs this round |
| O7 | B | JEV re-point; `src/cobalt/classify` absent | b:104-105, b:138; build ESC (iv) | OUT OF SCOPE | seam S1 §3 | owed by `jev/trial-0923`'s merge |
| O8 | A–D | standing: DEVICE SESSION owed | a:155, b:174, c:207, d:182 | OUT OF SCOPE | build ESC (ii) | before any ship; not this round |
| O9 | A–D | standing: V1's production prerequisites | a:156, b:175, c:208, d:183 | OUT OF SCOPE | build ESC (vi) | the deploy prompt carries them |
| O10 | C | the `uv.lock` whole diff was not staged | c:203 | OUT OF SCOPE (for the build) | desk R41 | `37` §1 (3) stages it |
| O11 | B | 6 UNCLASSIFIED restart paths "must be ruled before the deploy" | b:109, b:147; build ESC (viii) | OUT OF SCOPE | L42 | `jobs.yaml` declarations for the three voice configs are the deploy's / the desk's. C2 adds only `backup.yaml`'s reader |
| N2 | A | `open DAS and flatten nothing` gets no refusal | a:111 | NOT REAL | — | refused through `flatten`; the class is A1 |
| N3 | A | vacuous `test_voice_store.py:143-144`; DevDoc says "four registry pins" | a:114-115 | NOT REAL | — | "recorded, not counted" by the hub; not on the classifier list (L75: only HOLD rows are built) |
| N4 | A | C8 pins captured on base = the builder's claim | a:118 | NOT REAL | — | C8 CLOSED 2 of 2 (a:174); a provenance note, not a defect claim |
| N5 | A | Grok did not check (HARNESS) | a:149 | NOT REAL | desk R34 | answered: rerun done (a:159-167) |
| N6 | A | hub cwd `~/cobalt`, not `agy-trial` | a:152 | NOT REAL | desk R34 | cause settled; `37` makes the `cd` its own call |
| N7 | A–D | Sol METER / Astra NOT SEATED | a:151, b:171, c:205, d:180 | NOT REAL | L62 R19 | a record; `37` seats Sol from Sep 26th, 2026 6:47 AM |
| N8 | A, B | L74 block | a:153, b:172 | NOT REAL | L74 | recorded once, not followed |
| N10 | B | the substring span check accepts a truncated span | b:136 | NOT REAL | — | Opus files it "not a defect"; not counted by the hub; the read-back speaks the parsed value before any confirm (FINAL:88) |
| N11 | B | the build report says `PLAN_SCHEMA`; the tip says `plan_schema` | b:137 | NOT REAL | — | stale record |
| N12 | B | R56 reading (card stop keeps `[F-09]`) | b:106-107 | NOT REAL | — | both checkers AGREE |
| N13 | B | packet copy `extends` / `EXTENDS` | b:168 | NOT REAL | — | packet typo; no finding rests on it |
| N14 | C | a URL-shaped `route` is accepted once registered | c:144 | NOT REAL | — | no failing input without editing the registry; not counted |
| N15 | C | C5 "empty transcript ungated" (Grok) | c:145, d:138 | NOT REAL | — | DOES NOT HOLD: `turn.py:383-384` |
| N16 | C | `REPO_ROOT` from a worktree | c:153, c:202 6(d) | NOT REAL | — | dev only; not counted |
| N17 | C | Grok: subdirectory RED-logged; `AgentConfigError` / `startswith` | c:160-161 | NOT REAL | — | logged, not silent; no regression named |
| N18 | C | experiments file header says "packet B" | c:202 6(f) | NOT REAL | — | copied as the re-cut ruled |
| N19 | C | packet notes; part B's verdict read as a stop | c:204, c:210 | NOT REAL | — | records |
| N20 | D | the CLI dry-run test fakes `run_turn` | d:135 | NOT REAL | — | the hub: "not a gap"; D2 covers the two-flag case |
| N21 | D | the builder's WITH-DB / DEMO / CLOSE claims | d:137 | NOT REAL | L68 | superseded: `36` executes all three suites itself |
| N22 | D | launch row R41 uncommitted | d:178 | NOT REAL | — | a desk-process record |
| N23 | D | Grok's narration says it read beyond the packet | d:179 | NOT REAL | L44 | it cites nothing outside the packet |
| N24 | A–D | standing: live-note result owed for V1 | a:157, b:176, c:209, d:184 | NOT REAL | desk R34 ESC 12 | MET BY `36` (D1 / D6) |
| N25 | A→D | CLI `--confirm` refused in production | a:148 | NOT REAL | — | d:125 HOLDS: the narrow asks close. The `--text yes` path is D1 |
| N26 | A–D | standing "this check covers part X" lines; the checker lines | a:146, a:154, b:165, b:173, c:197, c:206, d:174-175, d:181 | NOT REAL | — | records; their defects are the rows above |
| N27 | C | build ASK DESKs X-X22 (keep the lock) / X-E4 (15 s loud timeout) | c:109, c:122; build ESC (ix) | NOT REAL | — | both checkers: "RUN — follows"; the safe defaults stand; not a check finding |

Counts: FIX 24 (A1 A2 A5 B1 B2 C1–C9 D1–D5 D7–D10 X5) · NOT REAL 26 (A3, N2–N8, N10–N27) · UNPROVEN 13 (U1–U13) · OUT OF SCOPE 11 (D6, X-E10, O3–O11) · OWNER ITEM 0. Contradictions settled by the hub's file-check column, never smoothed: B1 (Opus vs Grok; FINAL:111 decides), A5 (Opus (c) vs Grok (c), a:184), C4 / C5 (c:170).

## OWNER ITEMS

none. Every open question here is a design question the FINAL's letter settles, or the houses settle (X-E10 → tribunal round 2). L67's owner-items clause keeps them off his list.

## FOR DEJAN

ONE list, two new strings, for `36` only (they sat on `43`'s line, approved for `43` alone):
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env)`
- `Bash(rm /Users/cobalt/cobalt-wt/voice-v1/.env)`

`37` carries no new string (15's fourteen, byte for byte; R17 / R19 standing).

## ESCALATE

1. **L76 leaves five V1 with-DB tests UNRUN in `36`**: `test_voice_store.py`'s suite round-trip and reaper, the two real-connection X-X13 races (store + confirm), and X-E7 (with D7's strengthened version of it), plus RUN-1's timing. `dev_db_tx` (`tests/cobalt/conftest.py:133-183`) applies no migration, and these tests reach `"user".voice_turns` without applying `0017` in their own transaction. `43` ran them only because it left `0017` COMMITTED (09-23 R71). `36` D8 (c) proves the reason before deselecting. Where they run before the merge is the desk's ruling: the stacked L68 gate with `0017` applied and rolled back before its stop (L76's second clause), or a later round that makes them transaction-scoped.
2. **X-E10 → tribunal round 2 (FINAL:285, by its letter)** before ship. The desk opens it; the drafter did not assume it away.
3. **FINAL wording owed (R34):** `[F-08]` (FINAL:89) still reads "Unicode casefold, strip". The code and the desk's reading are NFKC + casefold + strip + strip `. , ! ?`.
4. **D6 boundary:** `test_radar_panel_cards.py` is kept as built (reverting it turns `/radar` red). The desk rules it.
5. **C2 changes L42 derivation:** `jobs.yaml` names `com.cobalt.aset` as a `configs/cobalt/backup.yaml` reader, so a `backup.yaml` change will derive an ASET restart. One pinned assertion is reversed (`test_voice_config.py:201`) and the restarts pin gains one reader. Both are named in `36`.
6. **`37`'s stop line** follows `35`'s shape (opus · grok only). Sol's line (SEATED or METER) is written in `37`'s §0 and `## ESCALATE`, not in the stop line.
7. **L74:** recorded once above, not followed.

VOICE V1 FIX R1 DRAFTED · FIX: 24 · NOT REAL: 26 · UNPROVEN: 13 · OUT OF SCOPE: 11 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 2 · ESCALATE: 7
