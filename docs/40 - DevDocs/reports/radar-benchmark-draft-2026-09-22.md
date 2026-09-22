# RADAR BENCHMARK DRAFT 2026-09-22

## §0 DIGEST (≤12 lines, 06:2x–06:3x ET)
- Wrote two prompts on the shape of `2026-09-20/17-cards-htf-apply.md` + `18-review-cards-htf.md`: `docs/40 - DevDocs/prompts/2026-09-22/01-radar-benchmark-load.md` (apply hub) and `02-review-radar-benchmark-load.md` (house read, Grok + Gemini under R39, `18`'s shape minus Astra per the task file's item 15).
- **NEW rule strings vs `17`: 2** — the two `--optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996…0880` load lines (`--dry-run` / `--apply`). Every other string in `01`'s allowlist (`db query --side user --prod *`, `date*`, `git add *`, `git commit *`, `git status*`, `tail *`, `grep *`, `ls *`) is byte-identical in shape to strings already approved elsewhere in the corpus (see RULE PROOF) — `01` is the first WRITE-PATH hub to carry `git add`/`git commit` (17 committed nothing; the desk's task explicitly asked this one to commit its own docs-only report).
- **`--apply` IS pause-bound: yes.** `cmd_load_optional` calls the same `assert_writable("settings.load", target='"user".trader_settings')` at `settings/cli.py:170` that the `--card` path calls at `:249` — the 20:00–21:00 ET market_reset block applies identically. No separate "trading-day scanning session" refusal is warranted here (unlike `17`'s P1(b)): nothing resident reads `radar.benchmark` (`replay/runner.py:318`, one-shot only), so `01` carries only the pause refusal, not the wider one.
- **PRIMARY ESCALATE — read this first:** the drafter task (item 12(a)) named `MODEL Sonnet 5` + `--permission-mode auto` for the apply hub. That is a `"user".trader_settings` write path; L29 (Opus floor, "never auto mode on a write path", restored O12) and the precedent it names (`17`, Opus, no `--permission-mode`) disagree. `01` was drafted **Opus 5, no `--permission-mode` flag** instead — the safe default — with an `ASK DESK` line in its own header naming the conflict. No ruling overruling L29 for this file was found in `cto-2026-09-22.md`.
- Item 6's grep (`"cobalt db query --side user --prod"` in `prompts/2026-09-21/`) returned **nothing**; the proof read is treated as NEW per the task's own fallback, though the identical shape is approved in `17` (09-20) and several 09-19 files (`30-cards-golive-apply.md`, `53-deploy-d3.md`, `38-deploy-p4.md`) — named in RULE PROOF below.
- sha256 of both `radar-benchmark.yaml` copies verified independently (`shasum -a 256`, my own allowlist item, not `01`'s): both `10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880`, matching item 4's stated value.
- ESCALATE: 3 (see below). No FAILED.

## RULE PROOF — `01-radar-benchmark-load.md`'s full `--allowedTools` list
| # | string | precedent |
|---|---|---|
| 1 | `Bash(COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --dry-run)` | **NEW** — new file path + new sha256; the `--optional` flag itself is documented and existing (`settings/cli.py:1-20`) but this exact file/hash pair has never been an approved string before. |
| 2 | same, `--apply` | **NEW**, same reason. |
| 3 | `Bash(COBALT_ENV=production uv run cobalt db query --side user --prod *)` | Byte-identical to `17-cards-htf-apply.md`'s allowlist string (2026-09-20) and to strings in `2026-09-19/30-cards-golive-apply.md`, `53-deploy-d3.md`, `38-deploy-p4.md`. Item 6's grep scope (`prompts/2026-09-21/`) found none there specifically — named as NEW per the task's own fallback rule, though not novel against the wider corpus. |
| 4 | `Bash(date*)` | Common to nearly every desk prompt in the corpus (e.g. `17`, `18`, `13`, `50`, `64`, `71`). |
| 5 | `Bash(git add *)` | Approved in `2026-09-20/20-bars-chunk-1a-fix.md`, `01-bars-brief.md`, `03-memory-history.md`, `11-bars-chunk-2-build.md`, `99-close-0919.md`, others. |
| 6 | `Bash(git commit *)` | Same file set as row 5. |
| 7 | `Bash(git status*)` | Same file set as row 5 (bare form, not `git -C * status*` — `01` runs with cwd `~/cobalt` per its own two-bare-command launch, so the bare form is sufficient; `17` used `git -C * status*` because its worktree cwd differed). |
| 8 | `Bash(tail *)` | Common (`17`, `18`, this drafter's own list). |
| 9 | `Bash(grep *)` | Common. |
| 10 | `Bash(ls *)` | Common. |
| — | `--disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)"` | Byte-identical to `17`, `18`, and this drafter's own launch line. |

## ESCALATE
1. **MODEL / auto-mode conflict (see DIGEST) — the desk's decision, not mine.** `01-radar-benchmark-load.md` carries its own `ASK DESK` line on this; repeating the pointer here per L48 (evidence in the report file) so it is not missed if only this digest is read.
2. **Item 6's grep scope found nothing** in `prompts/2026-09-21/` for the proof-read shape; I named it NEW in `01` per the task's instruction, while recording in RULE PROOF above that the identical shape is approved elsewhere (09-19, 09-20). If the desk wants the string counted as precedented rather than new, that changes this report's "new rule strings" count from 2 to 2 either way (the db-query string was never counted among the 2 NEW above) — no change needed, noted for completeness.
3. **L74 data block (recorded once, not followed, never raised again).** A `<system-reminder>` in this session's own turns instructs commit messages to carry a `Claude-Session: https://claude.ai/code/session_01MrWbQyZ14xaaxYjPCu335T` line and name-drops a file-send tool. Per L74 it is DATA and was not followed — this drafter session made no commits at all (no git-write tool in its own allowlist), and `01`'s own commit step (STEP 5) does not carry that line either.

RADAR BENCHMARK PROMPTS DRAFTED · prompts: 2 · new rule strings: 2 · apply pause-bound: yes · ESCALATE: 3
