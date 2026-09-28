# Voice V1 check — RE-CUT (L19 re-issue of `44`) · 2026-09-24

## §0 Headline

- Re-cut `44` (two packets of ≈417 KB) into **FOUR parts**, each ≤ 230,000 B measured: A ≈222,531 · B ≈222,826 · C ≈213,549 · D ≈212,534 (projected packet totals including header and file-list allowances).
- **Three parts cannot fit under `44`'s shape.** The shared context alone is 96,187 B per part, and the non-context bytes total ≈458.8 KB. Written: `prompts/2026-09-24/16-voice-v1-check-a.md` … `19-voice-v1-check-d.md`. `19` is past the 16–18 the desk reserved (ESCALATE 1).
- Of the range's 84 paths, every one is in exactly one part. Unassigned: 0. Excluded: 1 (`uv.lock` whole diff, generated; a 1,708 B excerpt is staged instead). Rule strings: `44`'s line minus `"Bash(agy *)"`, **0 new**, verified by `grep -c -F` (the whole allowed/deny/add-dir run = 1 in each of the four files; `44`'s run with `agy` = 1 in `44`).
- Checkers: Opus 5.5 + Grok seated. Sol probed; Astra is NOT SEATED (shared Codex meter, back 09-26 06:47 ET). Grok gate = `cto-2026-09-24.md` R17 (committed `1758fd78`). Part A (the ordered act) runs FIRST, then B → C → D in the house lane. All four gate the MERGE of `voice/v1-0923`; none gates any other deploy.
- ESCALATE: 8.

## L74

After this session's first tool result, one block asked that commits end with a `Claude-Session:` line and named a file-send tool (`SendUserFile`). Recorded once, as data. Not followed: this seat commits nothing and sent no file.

## Method (every number is `wc -c` or a saved-output size, `date` 07:56 ET)

- Range `04b05cd4..28b6b0c6` (15 commits). `voice/v1-0923` tip = `28b6b0c6`. There are 67 NEW paths (`--diff-filter=A`) and 17 CHANGED paths, 84 in all. `git log --stat` shows 100 file-touches.
- **Staging method (precedent `36`/`37`):** NEW files are staged WHOLE at the tip. CHANGED files are staged as their `git log -p <base>..<tip>` diff. Two later in-range edits of NEW *test* files are staged as `git show` diffs, so an assertion weakened inside the range stays visible. `44` staged both the diff and the whole tip copy of each new file. That duplication (136,601 B across the two packets, per `44`'s report) is removed.
- **Shared context per part** is 96,187 B, copied byte-identical from `44` run 1's staged, fidelity-checked `scratch/tribunal-bars-0920/voice-v1-check/A/`: `final-v1.part1` 15,586 · `final-v1.part2` 21,457 · `seam-s1` 14,433 · `rows.part1` 13,946 · `rows.part2` 21,984 · `rulings` 4,080 · `l28` 4,701. Also reused byte-identical: `stop-route-before-after` 5,870 and `store-stop` 4,986 (→ A), `build-report-A.part2` 8,519 (ESCALATE → B), `build-report-B.part1` 24,761 (EXPERIMENTS → C), `build-report-B.part2` 8,754 (WITH-DB/DEMO/CLOSE → D).
- **Build-report sections** were measured as `tail -n +N` differences: C1 3,378 · C2 3,084 · C3 1,697 · C4 1,876 · C5 1,035 · C6 1,249 · C7–C10 8,059 · C11–C13 6,740. The `## RULE BREACH` section (lines 462–464) is ≈700 B, measured on the staged copy. Not staged by any part: §0, `## L74`, `## AUTHORIZATION`, `## PREFLIGHT`, `## CONTINUE` (process sections; `44` did not stage them either).
- Every saved diff's `grep -c "^diff --git"` equals its touch count: web.py 2 · db_migrations py 2 · pins 6 · radar_panel_cards 1 · cli.py 1 · start_aset 1 · pyproject 1 · uv.lock 1 · aset/web.md 2 · db_migrations md 2 · cli.md 1 · the two `git show` diffs 1 each.
- **Why not three parts:** a part can hold at most 230,000 − 96,187 − QUESTIONS (≈3.6–5.0 K) − file list (≈2.5 K) ≈ 126–128 K of non-context. Non-context incl. headers ≈ 458.8 K ≥ 3 × 128 K = 384 K. Three parts would need the shared context cut to ≈69–70 K per part (−26 K). That changes `44`'s context, and this seat was not given that change.

## Split

`N` = staged whole (NEW) · `Δ` = diff (CHANGED) · `X` = EXCLUDED. Bytes are `wc -c` at `28b6b0c6`. Saved outputs include the harness's footer line.

| part | path | how | bytes |
|---|---|---|---|
| A | `src/cobalt/voice/tools.py` | N | 10,240 |
| A | `src/cobalt/aset/card_stop.py` | N | 2,027 |
| A | `src/cobalt/voice/store.py` | N | 9,189 |
| A | `src/cobalt/voice/confirm.py` | N | 5,427 |
| A | `src/cobalt/db_migrations/0017_voice_turns.sql` | N | 3,569 |
| A | `src/cobalt/db_migrations/0017_voice_turns.rollback.sql` | N | 297 |
| A | `tests/cobalt/test_voice_tools.py` | N | 8,985 |
| A | `tests/cobalt/test_voice_card_stop.py` | N | 7,715 |
| A | `tests/cobalt/test_voice_confirm.py` | N | 8,508 |
| A | `tests/cobalt/test_voice_store.py` | N | 12,317 |
| A | `src/cobalt/aset/web.py` (read-only copy to D) | Δ | 4,529 |
| A | `src/cobalt/db_migrations/__init__.py` + `placement.py` | Δ | 2,804 |
| A | `tests/cobalt/test_archiver_migrations.py` + `test_p4_migrations.py` + `test_radar_migration.py` + `test_radar_score_migration.py` + `test_tenancy.py` | Δ | 9,126 |
| A | `docs/40 - DevDocs/cobalt/voice/tools.md` · `aset/card_stop.md` · `voice/store.md` · `voice/confirm.md` | N | 2,160 · 1,169 · 1,616 · 1,446 |
| A | `docs/40 - DevDocs/cobalt/aset/web.md` | Δ | 3,053 |
| A | `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` + `placement.md` | Δ | 2,797 |
| A | + `stop-route-before-after` 5,870 · `store-stop` 4,986 · report C7–C10 8,059 | — | — |
| B | `src/cobalt/modelaccess/__init__.py` · `adapters.py` · `client.py` · `config.py` · `guard.py` · `models.py` | N | 769 · 5,031 · 7,449 · 5,064 · 1,800 · 3,201 |
| B | `configs/cobalt/modelaccess.yaml` | N | 2,190 |
| B | `src/cobalt/voice/agent.py` · `models.py` · `resolve.py` | N | 7,696 · 4,692 · 8,064 |
| B | `tests/cobalt/test_modelaccess_client.py` · `_config.py` · `_silence.py` | N | 13,513 · 4,541 · 3,672 |
| B | `tests/cobalt/test_voice_plan.py` (+ `git show 8bed61d3` diff 1,391) · `test_voice_resolve.py` | N | 7,525 · 5,842 |
| B | `tests/fixtures/voice/plan-replies.constructed.yaml` | N | 4,971 |
| B | DevDocs `modelaccess/{__init__,adapters,client,config,guard,models}.md` · `voice/agent.md` · `voice/models.md` · `tests/fixtures/voice/_voice_fixtures.md` · `voice/resolve.md` | N | 863 · 1,302 · 1,206 · 1,180 · 1,125 · 991 · 1,609 · 1,036 · 523 · 1,357 |
| B | + report C1 3,378 · C3 1,697 · C6 1,249 · RULE BREACH ≈700 · ESCALATE copy 8,519 | — | — |
| C | `src/cobalt/voice/__init__.py` · `config.py` · `registry.py` · `scratch.py` · `transcribe.py` | N | 579 · 6,517 · 3,924 · 9,487 · 6,851 |
| C | `configs/cobalt/agents/voice.yaml` · `configs/cobalt/voice.yaml` | N | 2,227 · 2,728 |
| C | `tests/fixtures/voice/plan-utterances.constructed.yaml` | N | 8,142 |
| C | `tests/cobalt/test_voice_config.py` · `test_voice_scratch.py` · `test_voice_transcribe.py` | N | 11,403 · 8,373 · 5,442 |
| C | `ops/start_aset.sh` · `pyproject.toml` | Δ | 1,147 · 615 |
| C | `uv.lock` — whole diff **EXCLUDED** (26,366 B, generated wheel URL/hash lines); staged instead: `grep -n -v` excerpt of every added package, version, source and dependency edge | X / Δ-excerpt | 1,708 |
| C | DevDocs `voice/__init__.md` · `config.md` · `registry.md` · `scratch.md` · `transcribe.md` | N | 620 · 1,993 · 871 · 1,636 · 1,372 |
| C | + report C2 3,084 · C4 1,876 · C5 1,035 · EXPERIMENTS copy 24,761 | — | — |
| D | `src/cobalt/voice/turn.py` · `web.py` · `cli.py` | N | 19,606 · 14,802 · 4,186 |
| D | `src/cobalt/cli.py` | Δ | 1,236 |
| D | `tests/cobalt/test_voice_turn.py` · `test_voice_web.py` · `test_voice_cli.py` · `test_voice_lifecycle.py` (+ `git show 28b6b0c6` diff 1,574) | N | 16,615 · 10,076 · 3,817 · 7,765 |
| D | `tests/cobalt/test_radar_panel_cards.py` | Δ | 1,561 |
| D | DevDocs `voice/turn.md` · `voice/web.md` · `voice/cli.md` | N | 2,104 · 2,150 · 948 |
| D | `docs/40 - DevDocs/cobalt/cli.md` | Δ | 1,189 |
| D | + report C11–C13 6,740 · WITH-DB/DEMO/CLOSE copy 8,754 · CONTEXT `aset/web.py` diff 4,529 | — | — |
| A–D | `docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md` (NEW) — by sections, as above | N-excerpts | 75,781 whole |

Path counts: A 25 · B 26 · C 19 · D 13, plus the build report = **84**. Unassigned: **0**.

| part | seam | checked (measured) | context | QUESTIONS | headers ≤ | list ≈ | packet ≈ | spare ≈ |
|---|---|---|---|---|---|---|---|---|
| A (`16`, FIRST) | the ordered act: C7–C10 | 115,889 | 96,187 | 4,755 | 3,200 | 2,500 | **222,531** | 7,400 |
| B (`17`) | the model path: C1, C3, C6 + build ESCALATE | 114,146 | 96,187 | 5,033 | 4,960 | 2,500 | **222,826** | 7,100 |
| C (`18`) | audio / model files / config / experiments: C2, C4, C5, X-* | 106,391 | 96,187 | 4,951 | 3,520 | 2,500 | **213,549** | 16,400 |
| D (`19`) | widget / route / turn / CLI: C11–C13 + CLOSE | 103,123 + 4,529 ctx | 96,187 | 3,635 | 2,560 | 2,500 | **212,534** | 17,400 |

Every staged file is ≤ 38,000 B; the largest is `d-code-1.md` at ≈34,408 B. Each part runs a MEASUREMENT gate before staging. A whole file off by any byte, or a saved output off by more than 64 B, stops the part (`FAILED: packet … re-measure the split`).

## What changed from `44`, per part file

- **Launch line:** `44`'s line, byte for byte, minus `"Bash(agy *)"`. Only the prompt path and the `--remote-control` names change (`voice-v1-check-{a,b,c,d}-0924`).
- **Grok gate:** the R17 row + `git log -S"Grok approved with no asking going forward"`. No dated row.
- **Checkers:** Opus 5.5 + Grok. Sol is probed and launched if UP. Astra is NOT SEATED. There is no Gemini seat. The part fails closed if Opus or Grok is down.
- **Stop line:** `44`'s DONE shape + `part: <X> (<seam>)`. The gemini field is removed and `astra:` added. Report paths: `reports/voice-v1-check-{a,b,c,d}-2026-09-24.md`.
- **Added gates:** the re-cut report must be committed. Parts B, C and D each require the previous part's report to have stopped (`DONE · part: <prev>` or `FAILED`); that part's verdict does not hold them (L72). The split must be total, and NEW vs CHANGED is checked against the staging method.
- **Questions:** `44`'s A and B texts, cut to each part's chunks, word for word otherwise. The build-ESCALATE SECOND question moves to B, the EXPERIMENTS SECOND to C. Checks (i)–(ix) are distributed: A (i)(ii)(iii)(v-bytes)(viii) · B (ii)(iii)(iv)(viii)(ix) · C (ii)(iii)(v-audio)(vii)(viii) · D (ii)(iii)(vi)(viii).

## ESCALATE

1. **FOUR parts, not ≤ 3, and a 4th file number.** The arithmetic is under `## Method`: three parts are impossible without cutting `44`'s shared context by ≈26 K per part. `19-voice-v1-check-d.md` is beyond the 16–18 range the desk reserved (`ls prompts/2026-09-24/` at 07:5x showed no `19`).
   `ASK DESK: accept four parts (16–19), or re-issue with a per-part trimmed context (e.g. seam-s1 only in B, rows' C-sections per part) for three? Safe default taken: four parts, 44's context whole in each. [07:56 ET]`
2. **Staging method differs from `44` §1 (1)–(2).** NEW files are staged whole at the tip instead of diff + tip copy; CHANGED files as diffs (precedent `37`). The in-range history of NEW non-test files is not staged: `agent.py`/`store.py` (`8bed61d3`) and `modelaccess.yaml`/`voice.yaml` (`b0acd0ed`) are read as the tip. The two later edits of NEW test files are staged as `git show` diffs (`test_voice_plan.py` @ `8bed61d3`, `test_voice_lifecycle.py` @ `28b6b0c6`).
3. **EXCLUDED: `uv.lock`.** Its whole diff is 26,366 B of generated wheel URLs and hashes. The part-C checkers get a 1,708 B `grep -n -v` excerpt instead: the added packages `av` 18.1.0, `ctranslate2` 4.8.2, `faster-whisper` 1.2.1, `flatbuffers` 25.12.19 and `onnxruntime` 1.30.0, plus their edges. A claim about the unstaged lines is checked by the hub against the full saved diff.
4. **Seam reading.** V1 writes NO vault byte (L28), so the "vault-write + versioning" part is V1's one confirmed act. A = tools + `set_card_stop` + confirm (the `diff_sha256`/`target_sha256` binding) + `voice_turns`, run FIRST. The desk's "widget + confirm" pairing was read the other way: confirm sits in A because its sha256 binding is the ordered edit's core, and the widget is in D. The desk's "secret / audio / model-file" group is split for size: the secret path (the modelaccess outbound guard) is in B, audio and model files in C. B and C together would be ≈220 K non-context.
5. **Checker count.** L67 (as amended 2026-09-24) seats Fable · Astra · Grok for a new build's check. With Astra on METER, two houses are seated (Opus 5.5 + Grok), per `13`'s "floor met". Each part fails closed below those two. Sol is carried and probed; Astra has no string on these lines, so it cannot be seated from 09-26 06:47 without a line change. Its string is standing under R19, but adding it would be a new string on this line. The desk decides.
6. **L68 GATE EARLY (2026-09-24).** V1's BUILT line (09-23) quotes offline `2422/0` and with-DB `2774/0` and no live-note result. Carried as a standing ESCALATE line in every part. The desk rules whether it is owed before the merge.
7. **Stop-line shape.** This report's last line adds a `D:` field that `13`'s shape did not have. The part reports use the fixed date `-2026-09-24` in their names whatever the launch day (`13`'s literal; the part gates depend on it).
8. **Reused staged files carry `44`'s old header lines.** They say "packet A" / "packet B". Kept byte-identical (they are fidelity-checked), and each part's QUESTIONS tells the checkers so. If they are gone at launch, the part stops `FAILED PREFLIGHT … must re-stage`.

VOICE V1 CHECK RECUT · parts: 4 · A: 222531 B · B: 222826 B · C: 213549 B · D: 212534 B · files unassigned: 0 · excluded: 1 · new rule strings: 0 · ESCALATE: 8
