# D3 BUILD CHECK — `archiver/append-0919` @ `7117fc3` (code tip `85b6d7c`), review hub `review-d3-build-0919`

## §0 Headline
- **Two houses read it (Grok, Gemini); Astra METER.** Grok: A `SAFE TO DEPLOY`, B `FIX FIRST 1`. Gemini: A and B both `SAFE TO DEPLOY`.
- Hub read the real tree in `archiver-append`: all nine conflict resolutions, the registry, the six pins, the fold and R34 "B" match the report. `radar.finviz_max_rpm` = **50** (`tunables.yaml:494-495`). **No BLOCKER, no MAJOR.**
- Grok B's one MAJOR (weakened pins) is **NOT REAL**: the assertions it says are missing are in the tree.
- 4 REAL findings, all MINOR, **none blocks deploy 3**. Nothing changes what the archiver WRITES.
- ESCALATE 0. Suites, RESTARTS and live-DB behaviour are `UNVERIFIABLE FROM READS` (5 items, named below).

## PREFLIGHT
Authorization: `git -C /Users/cobalt/cobalt log --oneline -16 -- "docs/40 - DevDocs/reports/cto-2026-09-19.md"` lists `96163c2` (R34), `fde57c2` (R33), `5204535` (R32); the R1, R25, R26, R32, R33 and R34 rows are present in `cto-2026-09-19.md` §4 and match the prompt. R9 and L67 are named in the prompt and were not re-proven (same standing law as the earlier rounds).

| step | command | exit | result |
|---|---|---|---|
| Grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| Gemini | `agy --version` | 0 | allowed — `1.2.7` |
| clock | `date` | 0 | allowed — `Sat Sep 19 16:11:46 EDT 2026` |
| Astra | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background, one probe) | 1 | allowed, **METER** — verbatim: `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:54 PM.` The prompt expected the reset to have passed; at the probe (16:1x ET) it had not. Not re-probed (one probe only). **The desk runs Astra separately after 4:54 PM.** |

## Packet
Staged in `scratch/review-d3-build-0919/` by Read → Write from `docs/40 - DevDocs/prompts/2026-09-19/51-packet/`.

| file | bytes staged | bytes source | equal? |
|---|---|---|---|
| `fixes.diff` | 43,562 | 43,622 | **60 bytes short = the 60 blank-context lines (`^ $` in the source, 60 counted) that lose their single space on Read→Write; staged file has 60 empty lines. Stated once, not chased.** |
| `commits.txt` | 463 | 463 | yes |
| `registry-after.py` | 5,122 | 5,122 | yes |
| `rebase-report.md` | 59,396 | 59,396 | yes |
| `QUESTIONS.md` | 3,744 | 3,744 | yes |

Bucketing, identical for both houses (L44): **A** = `QUESTIONS.md` + `fixes.diff` + `commits.txt` + `registry-after.py` (≈52.9 KB, Q2–Q7); **B** = `QUESTIONS.md` + `rebase-report.md` (≈63.1 KB, Q1 and the report's claims). No file was dropped and nothing truncated. Each call was launched once, in the background, with no retry. `QUESTIONS.md` Q1 tells a reviewer to read `/Users/cobalt/cobalt-wt/archiver-append/`; the reviewers are sandboxed to the folder, so Q1 was `UNVERIFIABLE FROM PACKET` for both houses by design and is settled by the hub below.

## Grok
Launched as `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/review-d3-build-0919/**)" -p "<prompt>"`. Calls A and B both returned, exit 0. Files: `grok-findings-A.md`, `grok-findings-B.md`.

- **A** (Q2–Q7 from the diff): 0 BLOCKER / 0 MAJOR / 2 MINOR — F1 (window built from `hour:minute`), F2 (stale `--rollback` sentence in the registry docstring). `VERDICT: SAFE TO DEPLOY`. It marked disk existence, `_rollback_paths` and `radar.finviz_max_rpm` "everywhere" UNVERIFIABLE FROM PACKET (settled by the hub).
- **B** (Q1 and the report's claims): 0 BLOCKER / 1 MAJOR / 0 MINOR — B-F1 "the (c)/(d)/(e) merged tests dropped HEAD's complete enumerations to a `[:4]` prefix". All nine Q1 rows `UNVERIFIABLE FROM PACKET`. `VERDICT: FIX FIRST 1`.

## Gemini
`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 15m …`, "you have NO tools" opener with an explicit file list per call. Both calls printed answers (exit 0). I wrote each printed answer byte for byte to `gemini-findings-A.md` / `-B.md`, dropping only the harness's trailing `[exited with code 0]` line.

- **A**: 0/0/0, `VERDICT: SAFE TO DEPLOY`. Independently read the diff for Q2–Q6 and its statements check out. Q1 N/A THIS CALL. It marked disk existence and the global `finviz_max_rpm` UNVERIFIABLE FROM PACKET.
- **B**: 0/0/0, `VERDICT: SAFE TO DEPLOY`. This call was a **restatement of the report's claims** ("Report claims: …"). It read no tree and did not test the claims, so it adds no evidence beyond "the report says so". Q1 `UNVERIFIABLE FROM PACKET`.
- Aggregate: `SAFE TO DEPLOY`, 0/0/0, both buckets answered, none HARNESS.

## Astra
`astra: METER`, verbatim in PREFLIGHT above. No launch, no findings, no token count. Not counted as a house that read it.

## Hub verification (L35 — real tree `/Users/cobalt/cobalt-wt/archiver-append`, tip `7117fc3`, `git status` clean; only docs commits sit above the code tip `85b6d7c`)

**Q1 — the nine conflict resolutions.** "theirs" = the pre-rebase branch tip `953cf89` (from the branch reflog), "HEAD" = post-P4 `19bb1b2`. Every P4 hunk to `store.py`, `runner.py` and `cli.py` was read with `git log -p 8838dda..19bb1b2` and found in the result.

| # | file | what the tree contains | hunk dropped? |
|---|---|---|---|
| a | `db_migrations/__init__.py` | `FORWARD` 0001…0011 (`:67-79`), `REVERSE` 0011…0002 (`:82-93`); docstring lists every 0002–0011 file (`:3-37`), P4 paragraph `:39-41` verbatim, gap paragraph `:43-49` rewritten as disclosed | none |
| b | `db_migrations/placement.py` | `movers_daily`, `picks`, `missed` (`:79-82`) and `archive_progress`, `archive_incidents` (`:87-88`) all in `CREATED_TABLES`; `missed` absent from `DECLARED_TABLES` (`:106-116`, comment `:107-108`) | none |
| c | `test_radar_migration.py::test_rollback_selects_only_newer_files_newest_first` | `[:4]` head, `[-4:]` tail, `not any(startswith 0003/0002/0001)`, equality against the REVERSE prefix filter, **and HEAD's `selected == tuple(p for p in REVERSE if int(p.name[:4]) > 3)` (`:50`)** | none — every assertion of both sides is present |
| d | `test_radar_score_migration.py` | both adjacency forms kept (`:92-93`); `reverse_names[:4] == newest_four`, the 0006/0007 adjacency, `_rollback_paths("0005")[:4]` and `[-2:]`, `("0006")[:4]` and `[-1:]`, the negative filter | HEAD's two exact-list assertions became a head-slice plus a tail-slice (disclosed in the report; see NOT REAL below) |
| e | `test_tenancy.py::test_down_to_0004_…` | `[:4]`, `[-3:]`, `names[-1]`, `all(int(name[:4]) > 4)`, `not any(startswith 0004/0003/0002)`, docstring | same: HEAD's exact 5-list became head+tail slices |
| f | `archiver/store.py` | imports `Bar, Interval` + `values_from_row` (`:23-24`); methods `upsert_bars`, `upsert_bars_on`, `watermark`, `count_rows`, `run_lock`, `target_transaction`, `insert_new_bars`, `bars_in_range`; P4's `bars_between` body is folded into `bars_in_range` (`:283`), not lost | none |
| g | `archiver/runner.py` | `_check_demand` present (`:80`) and called first in `_run_targets` (`:209`), before settings, store, lock and token | none |
| h | `docs/…/archiver/runner.md` | sections `## 2026-09-17` (`:62`), `## 2026-09-19 — write_mode` (`:85`), the "both live" note (`:149`), `## … R34 "B"` (`:158`) | none |
| i | `cli.py` | `replay_cli` `:72`/`:487`, `smoke_cli` `:74`/`:488`, `archiver_cli` `:80`/`:493`, `QuietRefused`, `ArchiveLockError` `:81-82`, P4's docstring lines `:26-27` | none. The report's "`:485–:491`" is off by two lines, cosmetic |

**Q2 — registry.** 21 files on disk (0001 plus 0002–0011 in `.sql` and `.rollback.sql` pairs); `FORWARD` and `REVERSE` match `registry-after.py`. `_rollback_paths` is `version > target` over `REVERSE` (`db_migrations/cli.py:606-616`), so `--down-to 0009` selects 0011, 0010 and `--down-to 0007` selects 0011, 0010, 0009, 0008. `0010`/`0011` carry the R25 `REVOKE ALL … FROM cobalt_user` (`0010:98`, `0011:121-122`). The branch touches none of P4's four migration files (`git log main..archiver/append-0919 -- <the four>` empty).

**Q3 — pins.** All six read in the tree; none deleted, none passes on a broken registry (`range(1, 12)`, no duplicate, `REVERSE` = `FORWARD` reversed minus 0001, exact 0009/0007 lists in `test_archiver_migrations.py`).

**Q4 — fold.** No reference to `bars_between` or `_bars_in_range` remains in `src`, `tests`, `ops` or `configs` beyond comments. Callers of `bars_in_range`: archiver `runner.py:354`, `shadow.py:155`, `cli.py:351` (pass their own `conn`, defaults inclusive/dict); replay `runner.py:382`, `:409`, `movers.py:542` (pass `None, end_inclusive=False, as_bars=True`).

**Q5 — R34 "B".** `tunables.yaml:494` key, `:495` `value: 50`; `main`'s file carries the same value; the branch's only `configs` commit is `e824f36` (ArchiverSettings block), which does not touch that row. Refusal `runner.py:112-118` and `window=window` `:120` are both present; `full` returns `check_scheduled_demand("archiver")` (`:106-107`) with no bound. `git -C … log --stat main..archiver/append-0919 -- src/cobalt/radar src/cobalt/replay src/cobalt/session src/cobalt/taxonomy ops` shows only `0efe5a9` (two replay call sites): no radar, `notes.py`, replay-consumer or cadence change.

**Q6.** The only write-path files are unchanged in behaviour; no diff line touches `upsert_bars`, `_upsert_targets` or `write_mode`.

## Verdict table

| # | finding | houses | sev | hub verdict | evidence | blocks deploy 3? |
|---|---|---|---|---|---|---|
| G-A1 | Backfill window is built from `hour:minute` (seconds dropped) | Grok A F1 | MINOR | **REAL** | `notes.py:191-194` (`from_at` uses `_hhmm_minutes(at)`, `end = start + ceil(seconds/60)`); `runner.py:75-77`. Run started 03:59:50 with ≥9 targets (`round(9×1.2)=11 s` → 1 min) declares 03:59–04:00, no overlap, and ends ≈04:00:01. Overshoot is under 60 s | **no** — manual `--backfill` only; the nightly `full` path is untouched |
| G-A2 | Registry docstring still says `--rollback` "reverse 0003 then 0002" | Grok A F2 | MINOR | **REAL, pre-existing** | `__init__.py:57-58`; `git log -S"to reverse 0003 then 0002"` = `16847eb` (heartbeat commit, before this branch); `--rollback` needs `--down-to` (`cli.py:606-609`) | **no** — comment only |
| H1 | The declared window counts only the sleeps, not the fetches | hub (no house) | MINOR | **REAL** | `runner.py:76`: `seconds = len(targets) × 1.2`; `_upsert_targets` sleeps 1.2 s after each fetch (`:264-265`) and each fetch is up to 30 s (`collector.py:192`), so the real run is longer than the declared one. A backfill started 03:30 with 900 targets declares 03:30–03:48 and is allowed, but at ≈2.2 s per request it runs to ≈04:10, inside the window R34 closed. The comment `_backfill_window` "ACTUALLY hold the transport" is not exact. Also untested: the midnight clause (`:112`, no test mentions it) | **no** — operator-initiated, rare, and the ruling B is honoured for the scheduled path; fix = add a latency allowance per request or bound the run with a deadline |
| H2 | Registry docstring says "nothing asserts contiguity" while the new pin asserts it; the new pins are tail-anchored again | hub (no house) | MINOR | **REAL** | `__init__.py:46-47` vs `test_archiver_migrations.py` `test_the_registry_is_an_explicit_contiguous_list…` (`numbers == list(range(1, 12))`, `numbers[-2:] == [10, 11]`) and `FORWARD[-4:]`; the next migration (0012) will redden them, the failure class `test_tenancy.py`'s docstring warns about | **no** — tests and prose only |
| G-B1 | "(c)/(d)/(e) dropped HEAD's complete enumerations; `_rollback_paths("0005")`/`("0006")` could omit 0007/0006 and `[:4]` would still pass" | Grok B F1 | MAJOR | **NOT REAL** | Read in the tree: (d) asserts `_rollback_paths("0005")[-2:] == [0007, 0006]` and `("0006")[-1:] == [0007]` beside the `[:4]`, so its scenario fails those assertions; (c) keeps `selected == tuple(p for p in REVERSE if int(p.name[:4]) > 3)` (`:50`); exact `REVERSE` is pinned separately. Residual, not a defect: (d) and (e) no longer pin a selection's exact length, the archiver's own pins cover the registry itself | n/a |

**UNVERIFIABLE FROM READS (5)** — each names the missing command; the build's numbers are evidence only:
1. **U1** offline 2146/0 and db 2486/0: `uv run pytest -q tests/cobalt tests/taxonomy` and `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy` (neither rule is in this launch line).
2. **U2** `RESTARTS: com.cobalt.aset com.cobalt.radar`: `uv run cobalt jobs restarts 19bb1b2..HEAD`.
3. **U3** a real `--backfill` refused inside 04:00–09:30 ET end to end, and H1's timing on a real run: `uv run python -m cobalt.archiver.runner --backfill <TICKER>` with the clock at a premarket instant (production-adjacent, not run here).
4. **U4** the R25 `REVOKE` actually denying `cobalt_user` on a live database: `COBALT_ENV=dev uv run cobalt db migrate` then `SET ROLE cobalt_user; SELECT 1 FROM system.archive_progress;` on `cobalt_dev`.
5. **U5** `--rollback --down-to 0009` and `--down-to 0007` on a live dev database: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0009` (and `0007`) with `--proof-only` before and after.

Not findings (per `QUESTIONS.md`): `append`-mode switch, C the cadence stagger, §11 "follows 0006's pattern", a backfill being refused in most scheduled hours.

D3 BUILD CHECK · grok: FIX FIRST 1 · gemini: SAFE TO DEPLOY · astra: METER · houses that read it: 2 of 3 · hub-verified REAL: 4 (blocks deploy 3: 0) · NOT REAL: 1 · UNVERIFIABLE: 5
