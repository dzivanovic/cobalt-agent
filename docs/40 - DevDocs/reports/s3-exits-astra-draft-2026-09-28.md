# S3 exits — Astra read, drafter report — 2026-09-28

## §0
- Drafted `prompts/2026-09-28/13-s3-exits-astra-read.md` (16,819 B): Sonnet 5 hub `s3-exits-astra-0928`, seats Astra only, cwd `/Users/cobalt/cobalt`.
- 19 items: every `[R2F-nn]` tag of the FINAL (the header mark, line 3, rules nothing). The launch line drops 6 of 02's 14 allow strings; the 3 denies stay.
- Authorization: `cto-2026-09-28.md` line 37 (R29) carries this launch, `APPROVED — launching`, checked 08:46 ET.
- ESCALATE: 3. Nothing committed.

## ITEMS
FINAL = `docs/30 - Design/S3-EXITS-v3-2026-09-22.md` (371 lines). Order = the order in the hub's question list.

| # | id | FINAL line(s) | subject |
|---|---|---|---|
| 1 | R2F-01 | 21, 100 | R2-1 converged, DO NOT BUILD withdrawn |
| 2 | R2F-03 | 102, 280, 295, 365 | C1 build note: `autocommit = False` |
| 3 | R2F-09 | 23, 139 | R2-3 converged: M1 = one `db_migrations` file + `.rollback.sql` |
| 4 | R2F-10 | 192 | `card_stop_edits.kind` in M1 |
| 5 | R2F-11 | 253 | C1 migration cell |
| 6 | R2F-07 | 50, 193 | FILLED stop-edit reads planned `shares` / `entry` |
| 7 | R2F-14 | 282 | X20, second half of that defect |
| 8 | R2F-12 | 288 | X4 merged |
| 9 | R2F-13 | 288 | X7 merged |
| 10 | R2F-15 | 288 | X21 |
| 11 | R2F-16 | 288 | X22 |
| 12 | R2F-04 | 22, 89, 119, 128, 131, 137, 141, 170, 254 | R2-2 OPEN FOR DEJAN block |
| 13 | R2F-20 | 280 | tests that follow R2-2 |
| 14 | R2F-21 | 319 | Q3 / Q4 dispositions |
| 15 | R2F-17 | 337 | O16 |
| 16 | R2F-18 | 342 | O21 |
| 17 | R2F-19 | 343 | O22 |
| 18 | R2F-02 | 349 | gemini round-1 dissent, spent |
| 19 | R2F-22 | 353 | round-2 answers not followed |

Not items: `R2F-05`, `R2F-06`, `R2F-08` are rows of the derive's `## Fold table` only (`s3-exits-tribunal-derive-r2-2026-09-22.md` lines 41, 42, 44); `grep -n -F` finds none in the FINAL.

## RULE PROOF
Launch line of `13` vs `02`'s (`grep -c -F -e` on `02`, quotes included, one call each, 08:49 ET):

| string | in `02` | in `13` |
|---|---|---|
| `Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)` | 1 | kept |
| `Bash(git -C /Users/cobalt/cobalt show*)` | 1 | kept |
| `Bash(git -C /Users/cobalt/cobalt log*)` | 1 | kept |
| `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)` | 1 each | kept |
| `"AskUserQuestion" "EnterWorktree" "Bash(git push*)"` | 1 | kept |
| `Bash(grok *)` | 1 | removed — no Grok seat |
| `Bash(agy *)` | 1 | removed — no Gemini seat |
| `Bash(mkdir -p scratch/tribunal-bars-0920)` | 1 | removed — the Write tool creates the folder |
| `Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)` · `… log*` · `… diff*` | 1 each | removed — no copy step |

Strings removed: 6. The launch line's other parts: `--model claude-sonnet-5 --permission-mode auto`, the three `--add-dir` are `02`'s; `--remote-control` and `--name` carry `s3-exits-astra-0928` (H6). `claude --bg "Read '…' and follow it exactly."` differs in the path only.

`NEW strings:` none. `--name <job>` is a launch flag under checklist H6, on `12`'s own line, not a permission string.

Placeholder count: the launch-row placeholder appears once in `13`, in its AUTHORIZATION block (line 5), nowhere else (K18).

## ESCALATE
1. ASK DESK: `13` captures to `scratch/tribunal-bars-0920/s3-exits/astra/` under cwd `/Users/cobalt/cobalt` (as `12` orders). `~/cobalt/.gitignore` carries no `scratch` entry (`grep -n -F "scratch"` on it printed nothing) and `~/cobalt/scratch/` holds only `review-p4-folds-0919`; `02`'s hub ran in `agy-trial`, where the folder is ignored. The capture files will show as untracked in production. Safe default taken: as ordered. Fix, if wanted: run `13` from `/Users/cobalt/cobalt-wt/agy-trial` (then Astra's original-path reads still work; the report path stays under `~/cobalt`). [08:49 ET]
2. ASK DESK: `cto-2026-09-22.md` R67 (line 99) already gives his R2-2 answer as a desk reading (B + three additions), while the FINAL header still says "NOT FINAL until he rules R2-2". `13` treats R67 as an input Astra never reopens and rules R2-2 items on their cited facts only. Whether the FINAL needs a re-issue that folds R67 is the desk's; `07`'s chunks that rest on `R2F-04` / `R2F-07` are the ones affected. Safe default taken: no change. [08:49 ET]
3. ASK DESK: the launch row must carry both literals `s3-exits-astra-0928` and `Astra only`, and name `13-s3-exits-astra-read.md`, or the hub stops `FAILED: authorization mismatch`. The desk writes the row number into the placeholder before launch. [08:49 ET]

## CONTINUE
Done. Both files written; nothing committed. Next is the desk's: read `13` end to end, fill the launch-row placeholder, commit, launch with the two bare commands on `13`'s first line.

S3 EXITS ASTRA READ DRAFTED · items: 19 · strings removed: 6 · new rule strings: 0 · ESCALATE: 3
