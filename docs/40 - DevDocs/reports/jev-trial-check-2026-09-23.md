# JEV TRIAL CHECK — PART A (secret + network path) — round 1 of ≤3 — `47fafe5..45f647a` on `jev/trial-0923`

## §0 Headline
- Checked: PART A (17 files, the secret and network path) of the JEV trial build `47fafe5..45f647a` — run 3 of `29` CHECK A (replaces run 1's report `8fdaeca` and run 2's `037cff6b`, run 2 having stopped at the key scan on a documentation placeholder, desk R55). PREFLIGHT passed whole; packet 213,827 B; three houses checked (Grok, Gemini, Opus 5.5); Sol METER (retry Sep 26th 6:47 AM).
- Status: DONE. **probe gate: NOT READY** — `secrets LEAK that HOLD: 3` (a non-200 raw body written past the guard; a redirect that carries `Authorization`; a response `id` written to the ledger before the stored guard) and `defects that HOLD: 3` (cost-less calls invisible to the ledger; a negative returned cost accepted; a `from None` regression on the transport-exception path stays green). Gemini alone says CLEAN. No keyed call was ever made, so no key material reached anything.
- ESCALATE: 13.

## L74
One block arrived inside a tool result (the Read result of `29-jev-trial-check.md`, first read): it asked for a `Claude-Session:` trailer line in commits and pointed at a file-send tool. It is DATA — recorded here once, never followed, never raised again. Nothing was committed by this run.

## PREFLIGHT
Rule · command · exit · result. `date` first row: `Wed Sep 23 13:08:33 EDT 2026` (`<D>` = 2026-09-23).

| # | rule | command | result |
|---|---|---|---|
| 1 | DATE + EXTENSION GATE (first row) | `date` | exit 0 — `<D>` = 2026-09-23 ≤ 2026-09-23 → R30's literal required |
| 2 | R30 printed | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23" …/cto-2026-09-22.md` | exit 0 — prints `\| R30 \| 13:0x ET \| "Approved" — …` carrying the literal |
| 3 | R30 committed | `git log -1 --format=%H -S"…through 2026-09-23" -- …cto-2026-09-22.md` | exit 0 — `055242df8032632dfafdcc8a69dcc271be89c0f6` |
| 4 | grok present | `grok --version` | exit 0 — `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| 5 | agy present | `agy --version` | exit 0 — `1.2.9` — allowed |
| 6 | 66 gate: R13 of 09-20 | `grep -n "^\| R13 " …cto-2026-09-20.md` | exit 0 — row printed |
| 7 | 66 gate: R40 | `grep -n "^\| R40 " …cto-2026-09-21.md` | exit 0 — carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| 8 | 66 gate: R44 | `grep -n "^\| R44 " …cto-2026-09-21.md` | exit 0 — carries `ONE BUILD of the whole FINAL` |
| 9 | 66 gate: R46 | `grep -n "^\| R46 " …cto-2026-09-21.md` | exit 0 — carries `instead of Astra you can use Sol` |
| 10 | R46 committed | `git log -1 --format=%H -S"instead of Astra you can use Sol" -- …cto-2026-09-21.md` | exit 0 — `53e059456750c0c9efcf50222a7a647630dc4b04` |
| 11 | R49 (Sol string) | `grep -n "^\| R49 " …cto-2026-09-21.md` | exit 0 — carries `"Approved"` |
| 12 | R49 Sol string present | `grep -c -F "Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" …cto-2026-09-21.md` | exit 0 — `1` |
| 13 | R49 Sol string committed | `git log -1 --format=%H -S"Bash(codex exec … gpt-5.6-sol …)" -- …cto-2026-09-21.md` | exit 0 — `60147d400b009db5a2518e02b8ab1fe5765db405` |
| 14 | Opus seat string, R32 of 09-22 | `grep -n "^\| R32 " …cto-2026-09-22.md` | exit 0 — carries `claude -p --model claude-opus-5-5` |
| 15 | R32 committed | `git log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- …cto-2026-09-22.md` | exit 0 — `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| 16–28 | THE THIRTEEN (quotes included) in `08-bars-chunk-e-check.md` | `grep -c -F -e '"<rule>"' …08-bars-chunk-e-check.md` ×13 | exit 0 each — **1** each (13 of 13) |
| 29–31 | THE THREE denies | `'"AskUserQuestion"'` · `'"EnterWorktree"'` · `'"Bash(git push*)"'` | exit 0 each — **1** each (3 of 3) |
| 32 | Astra string absent from the launch line | the launch line as written in `29` | carries no `gpt-6-astra` string — allowed |
| 33 | The build was approved and launched | `git log -1 --format=%H -S"28-jev-trial-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | exit 0 — `30a3a0484fe2abc56b47985ca6109a81b68faed2` |
| 34 | The desk recorded the build's stop | `grep -n "JEV TRIAL BUILT" …cto-2026-09-23.md` | exit 0 — `\| R48 \| 11:4x ET \| … JEV TRIAL BUILT 45f647a \| on 47fafe5 …` |
| 35 | …committed | `git log -1 --format=%H -S"JEV TRIAL BUILT" -- …cto-2026-09-2*.md` | exit 0 — `fec87553b61c90de9bc16a2ce4ad3f52884d1ece` |
| 36 | The split was drafted and committed | `git log -1 --format=%H -S"JEV CHECK SPLIT" -- "docs/40 - DevDocs/reports/jev-check-split-2026-09-2*.md"` | exit 0 — `46b441dd263867b468ca7ab8098c817cd0d0f3c4` |
| 37 | THIS launch row R54 | `grep -n -F "29-jev-trial-check.md CHECK A" …cto-2026-09-23.md` | exit 0 — prints `\| R54 \| 13:0x ET \| … (2) 29-jev-trial-check.md CHECK A RELAUNCH row …` (number filled; R55 `\| R55 \|` records the relaunch after run 2's false stop) |
| 38 | …committed (desk files only) | `git log -1 --format=%H -S"29-jev-trial-check.md CHECK A" -- …cto-2026-09-2*.md` | exit 0 — `037cff6b4051ac7cb6c59d179473533eac15dbdf` |
| 39 | worktree exists | `ls /Users/cobalt/cobalt-wt/jev-trial` | exit 0 — listing (`src`, `tests`, `ops`, `configs`, `docs`, `scratch`, …) |
| 40 | THE BUILT LINE | `tail -n 3 …/jev-trial-build-2026-09-23.md`, last non-blank line | exit 0 — `JEV TRIAL BUILT 45f647a \| on 47fafe5 \| offline 2103/0 \| model listed: typesafe/jev-1.13 \| other Jev ids listed: none \| door: systemone \| probe: NOT RUN (after check, R42) \| ledger: NOT RUN (after check, R42) \| cap: $5 \| RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar \| tests added: 145 \| ESCALATE: 28`. `<tip>` = `45f647a`, `<base>` = `47fafe5` = the measured pair; `model listed` = `typesafe/jev-1.13`; `probe` = `NOT RUN (after check, R42)` → allowed |
| 41 | NO KEYED CALL WAS MADE | `ls /Users/cobalt/cobalt-wt/jev-trial/scratch` | exit 0 — `docs-openrouter`, `openrouter-models-20260923.endpoints.json`, `openrouter-models-20260923.json`; no `probe-*`, no `classify-spend.jsonl` → allowed |
| 42 | THE RANGE | `git log --oneline 47fafe5..45f647a` | exit 0 — 8 commits (`05d9ddae` R1 · `8e662bad` R2 · `5630e6c8` wip · `61145195` report · `001c1d1c` R3 · `e18793ad` report · `537c0978` R4 · `45f647a2` R5) — recorded |
| 43 | the branch tip | `git log --oneline -1 jev/trial-0923` | exit 0 — `199fa082 feat(classify): JEV trial build report — run 3: BUILT …` (the report commit above `<tip>`) |
| 44 | the branch did not move above `<tip>` | `git log --oneline 45f647a..jev/trial-0923 -- src tests configs ops "docs/40 - DevDocs/cobalt/classify" "docs/40 - DevDocs/tests"` | exit 0 — EMPTY → allowed |
| 45 | THE BOUNDARY | `git log --stat --oneline 47fafe5..45f647a` | exit 0 — 29 distinct paths, every one inside `28`'s `WHAT YOU BUILD` (`src/cobalt/classify/{__init__,models,config,collector,ledger,trial,cli}.py`, `src/cobalt/cli.py`, `configs/cobalt/classify/trial.yaml`, `ops/run_classify_trial.sh`, `tests/cobalt/test_classify_*.py`, `tests/fixtures/classify/*`, the classify DevDocs, `docs/40 - DevDocs/cobalt/cli.md`, the fixtures DevDoc, the report); no other path. THE SPLIT IS TOTAL: 29 = A 17 + B 12, each path in exactly one part |
| 46 | EVERY PART-A FILE IS NEW | `git log --diff-filter=A --name-only --format= 47fafe5..45f647a` | exit 0 — 27 paths printed, all 17 part-A paths among them; the two not printed are `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` (both part B) → allowed |
| 47 | KEY SCAN 1 | `grep -rn "sk-or-" …/tests/fixtures/classify` | exit 1 — no output |
| 48 | KEY SCAN 2 | `grep -rn "sk-or-" …/src/cobalt/classify` | exit 1 — no output (no guard pattern naming the prefix sits in `classify`; the guard is `cobalt.redact`) |
| 49 | KEY SCAN 3 | `grep -rn "sk-or-" "…/docs/40 - DevDocs/reports"` | exit 0 — 9 lines, all in `jev-trial-build-2026-09-23.md`: `:120` the prompt's placeholder `sk-or-v1-TESTONLY-<32 hex>` · `:122` the prefix in words (`any other sk-or-v1- string`) · `:170` a quoted `grep -c "sk-or-"` command · `:196` a quoted `grep -c "sk-or-"` command · `:321` a quoted `grep -rn "sk-or-"` command · `:331` the placeholder · `:340` a quoted grep command · `:364` a quoted grep command · `:398` the placeholder → every line in an allowed class |
| 50 | KEY SCAN 4 | `grep -rn -i "bearer " …/tests/fixtures/classify` | exit 1 — no output |
| 51 | KEY SCAN 5 | `grep -rn "sk-or-" …/scratch/docs-openrouter` | exit 1 — no output (the desk reworded the one placeholder line of `jev-tutorial.md`, R55) |
| 52 | `.env` in the worktree | `ls /Users/cobalt/cobalt-wt/jev-trial/.env` | exit 1 — `No such file or directory` → allowed |
| 53 | RECOVERY | `ls scratch/tribunal-bars-0920/jev-trial-check` | exit 1 — `No such file or directory` = fresh run |
| 54 | THE STAGGER | `grep -n -F "no other house hub is running" …cto-2026-09-23.md` | exit 0 — the R54 row that names `29-jev-trial-check.md CHECK A` carries `no other house hub is running` (`19` PAUSED by the desk; the Anthropic seats do not block) |
| 55 | THE CODEX LAUNCH SHAPE | `grep -c -F "Experiment field: **reads started**" …setups-tribunal-r2-2026-09-21.md` | exit 0 — `1` → a Sol launch appends ` < /dev/null` |
| 56 | PROBE — SOL | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` (`run_in_background`) | exit 0 — answered `OK`, no usage-limit text → **sol: UP** |
| 57 | PROBE — OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (`run_in_background`) | exit 0 — answered `OK` → **opus: UP** |
| 58 | PROBE — GROK / GEMINI | by rows 4 and 5 | **grok: UP · gemini: UP** |

Recorded fields of the built line: `model listed: typesafe/jev-1.13` · `other Jev ids listed: none` · `door: systemone` · `probe: NOT RUN (after check, R42)` · `ledger: NOT RUN (after check, R42)` · `cap: $5` · `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar` · `tests added: 145` · `ESCALATE: 28`.

FOUR of FOUR checkers UP → launch every UP house (row 58's count: 4 ≥ 3).

## Packet
Folder `scratch/tribunal-bars-0920/jev-trial-check/` (staged by Read → Write, no `mkdir`). THE MEASUREMENT BEFORE STAGING: `wc -c` of every whole-file original equals the drafter's table to the byte (12 code / test / fixture files 95,295 B; 5 DevDocs 15,311 B; 4 contract whole files 22,616 B). Trailing whitespace in every original: 0.

| staged file | pieces | bytes | check |
|---|---|---|---|
| `a-code-1.md` | `config.py` 14,014 · `ledger.py` 4,433 · `cli.py` 6,449 · `run_classify_trial.sh` 954 (whole) | 26,098 | `wc -c` = pieces 25,850 + 4 headers 245 + 3 blank separators = 26,098 |
| `a-code-2.md` | `collector.py` 25,239 (whole) | 25,306 | = 25,239 + header 67 |
| `a-tests-1.md` | `test_classify_config.py` 6,942 · `test_classify_keys.py` 9,264 · `test_classify_discover.py` 8,095 (whole) | 24,513 | = 24,301 + headers 210 + 2 |
| `a-tests-2.md` | `test_classify_door.py` 16,420 · the three fixtures 1,076 + 298 + 2,111 (whole) | 20,269 | = 19,905 + headers 360 + 4 (the endpoints-record fixture has no trailing newline, its line end is a separator) |
| `a-devdocs.md` | `config.md` 2,425 · `collector.md` 5,913 · `ledger.md` 1,551 · `cli.md` 3,385 · `_classify_fixtures.md` 2,037 (whole) | 15,720 | = 15,311 + headers 405 + 4 |
| `contract.md` | `secrets.py` 11,801 · `redact/__init__.py` 1,075 · `guard.py` 8,273 · `mattermost.py` lines 58–129 2,800 · `run_backup.sh` 1,467 · `28` lines 67–91 954 | 26,785 | = 26,370 + headers 410 + 5 |
| `context.md` | `models.py` 157–243 2,748 · `trial.yaml` 1–44 2,304 · OpenAPI 337–436 3,357 · OpenAPI 843–1032 5,040 | 13,865 | = 13,449 + headers 413 + 3 |
| `plan.md` | plan §1 lines 21–31 2,218 · §5–§7 lines 82–99 3,089 | 5,482 | = 5,307 + headers 174 + 1 |
| `rows.md` | `28` 33–37 1,728 · 39–42 2,899 · 44–48 2,268 · 50–56 5,826 · 58–96 8,368 · `31` 29–34 1,254 | 22,948 | = 22,343 + headers 600 + 5 |
| `build-report.md` | report lines 100–116 1,681 · 117–137 2,705 · 158–183 3,791 · 184–206 4,842 · 252–268 3,663 · 269–285 4,715 | 21,996 | = 21,397 + headers 594 + 5 |
| `QUESTIONS-JEV-A.md` | the verbatim questions 8,470 + the appended "Files in this folder:" paragraph 2,375 | 10,845 | the questions alone = 8,470 B (the drafter's measure); 6 of 6 question lines occur in `29` (`grep -c -F -f`) |

Fidelity beyond `wc -c`: for every whole file, the number of original lines absent from the staged copy (`grep -c -v -x -F -f <staged> <original>`) equals the original's blank-line count (empty patterns are ignored by `-f`), i.e. every non-blank line is present; for `rows.md` and `build-report.md` the same reverse search against the sources printed only headers and blank lines; for the `31` piece the reverse search shows lines 29–34 present. Piece line ranges start at the named headings (`## R1`, `## R2`, `## R3 (run 2, desk R46)`, `## R4 (run 3, desk R47)`, `## DISCOVERY`, `## ESCALATE`, `## WHAT YOU BUILD …`, `## R1 …` … `## R4 …`, `## THE PROBE`, `DecisionsRequest:`, `DecisionsChoiceQuestion:`, `class Answer(_Strict):`) — no shifted range. HEADER REFS: the shape `### <path> @ <tip>` carries the checked tip `45f647a` for worktree files, `8fdaeca` for the prompts and the plan (`git log 8fdaeca..HEAD` on the three files EMPTY — unchanged since), `199fa08` for the build report (branch tip; only the report commit sits above `<tip>`); the two OpenAPI excerpts are the worktree's gitignored scratch copy (not in git).

HONEST SIZE: whole packet **213,827 B** (11 files; largest 26,785 B ≤ 38,000 B; no file is split into parts); ÷ 4 ≈ **53,457 tokens per checker**. The ceiling is 230,000 B → **under by 16,173 B**. Drafter's estimate ≈ 215,200 B.

KEY SCAN OVER THE STAGED FOLDER (`grep -rn "sk-or-" scratch/tribunal-bars-0920/jev-trial-check`, 14 lines): `a-tests-2.md:45` the tests' CONSTRUCTED fake key · `a-tests-1.md:177` the docstring placeholder `sk-or-v1-TESTONLY-<32 hex>` · `a-tests-1.md:197` the constructed fake key · `a-tests-1.md:311` a constructed other-string test (`"sk-or-v1-" + "f" * 40` — the source text holds the prefix and a repeat, no key value) · `rows.md:19` the placeholder in the build prompt's R2 · `rows.md:27`, `:68` quoted `grep -c "sk-or-"` commands · `rows.md:75` the words "any `sk-or-` text" · `build-report.md:24` the placeholder · `:26` the prefix in words · `:56`, `:84` quoted grep commands. No other line; no real credential, no `Authorization` value, no bearer text. Allowed classes only.

## Launch
Second DATE + EXTENSION GATE row: `date` → `Wed Sep 23 13:29:09 EDT 2026` (`<D>` = 2026-09-23); R30's literal `grep -c -F` = `1`; committed `055242df8032632dfafdcc8a69dcc271be89c0f6` → allowed. Before-launch listings taken: `ls -la scratch/tribunal-bars-0920/jev-trial-check` (11 staged files, newest 13:26) and `ls -la /Users/cobalt/cobalt-wt/jev-trial` (27 entries, newest `ops` 11:34). All four launched `run_in_background` at `Wed Sep 23 13:29:30 EDT 2026`, independent, one attempt per house, 45-minute clock → deadline 14:14 ET. Launch lines as run (secret-free, no key, no write path beyond Grok's own `--allow`):
- GROK `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "…"` (never `--always-approve`) — task `blleu5dbu`
- GEMINI `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 45m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"` — task `bsdgqinm5`
- SOL `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "…" < /dev/null` — task `bc5c2005k` — **METER at `Wed Sep 23 13:30 ET`, exit 1**: after reading its own contract files (`CLAUDE.md` and memory, which sit outside the packet) it stopped with `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM.` — no answer to any question, no `CHECK JEV A:` line, nothing to keep (no `sol-check.md` is written). The 13:0x probe had answered `OK`; the limit hit on the run's first turn. Recorded verbatim, NOT relaunched (one attempt per house). `sol: METER — retry after Sep 26th, 2026 6:47 AM`. The check continues on three houses (Grok · Gemini · Opus 5.5 = L67's floor).
- OPUS `claude -p --model claude-opus-5-5 "…" --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/jev-trial-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"` — task `b3yny9qqo`
Every sentence: "You are <HOUSE>. The folder is scratch/tribunal-bars-0920/jev-trial-check/. Start with QUESTIONS-JEV-A.md and follow it exactly. Do not open any *-check.md file." (no file is split, so no parts sentence; GEMINI's carries the absolute path and the no-shell / no-write sentences; Grok's adds "print your complete check … and write the same text to …/grok-check.md; write no other file").

## Checkers (clock, output files, written-nothing proof)
| house | landed | exit | closing line | file |
|---|---|---|---|---|
| gemini | `13:32 ET` (`date` 13:32:28; 3 min) | 0 | `CHECK JEV A: SECRETS CLEAN · BUILD STANDS EXCEPT THIRD · ready for the probe: YES · key handling is clean, safe and isolated` | `jev-trial-check/gemini-check.md`, written by me from stdout, byte for byte |
| opus 5.5 | `13:33 ET` (`date` 13:33:52; 4 min) | 0 | `CHECK JEV A: SECRETS LEAK S-3 S-6 · DEFECT REMAINS R2-T R4-RAW SPEND · ready for the probe: NO · urllib forwards Bearer on cross-host redirect; non-200 raw tail unguarded` | `jev-trial-check/opus-check.md`, written by me from stdout, byte for byte |
| grok | `13:46 ET` (`date` 13:46:51; 17 min) | 0 | `CHECK JEV A: SECRETS LEAK S-3, S-9 · DEFECT REMAINS R2, R4, SPEND · ready for the probe: NO · raw error tail and ledger id can hold the key` | `jev-trial-check/grok-check.md`, written by Grok itself through its approved `--allow` (its stdout also carried the answer, with a few narration sentences before the first `S-1`) |
| sol | `13:30 ET` | 1 | METER — see `## Launch`; no answer, no file | none |

All three answering houses finished inside the 45-minute clock (no TIMEOUT). NO CHECK LINE: none. HARNESS: none.
WRITTEN-NOTHING PROOF: `ls -la scratch/tribunal-bars-0920/jev-trial-check` after the launches lists the 11 staged files unchanged (same sizes and times) plus exactly `gemini-check.md` and `opus-check.md` (mine) and `grok-check.md` (Grok's own permitted write); `ls -la /Users/cobalt/cobalt-wt/jev-trial` after equals the before listing (27 entries, same modification times; `ops` 11:34, `scratch` 11:27, `src` / `tests` 11:07). No checker is marked `WROTE:`. `grep -c -i "denied\|not allowed\|permission"` on the three check files: 0 / 0 / 0 (no tool-denial line).

## CONTINUE
next: none — the four houses are accounted for (three answered, Sol METER), every claim is file-checked and the report is closed; the desk reads the last line.

## Secrets
Verdicts as answered (`sol` = METER). Checkers cite the STAGED files' line numbers (`a-code-2.md:n` = `collector.py:n-1`; the wrapper block in `a-code-1.md` is the last piece); Grok cites the source lines; the file-check below is in source lines.
| item | grok | gemini | opus | checkers answering CLEAN |
|---|---|---|---|---|
| S-1 wrapper | CLEAN — `run_classify_trial.sh:1-25`, 954 B equal | CLEAN — `a-code-1.md:628` | CLEAN — `a-code-1.md:629-653` = `contract.md:680-704`, no `set -x`, only `COBALT_ENV` / `COBALT_VAULT_FILE` exported | 3 of 3 |
| S-2 `read_secret` path | CLEAN — `collector.py:401`, `:544`, `:406-414` | CLEAN — `a-code-2.md:402` | CLEAN — `:545`, header dict set to `None` in `finally` (`:554`) | 3 of 3 |
| S-3 leave the process | **LEAK** — `collector.py:387-388` (a response `id` with the key is ledgered before the guard) and `:349`, `:354-359` + `cli.py:91` (a non-200 non-JSON body's tail past byte 2000 reaches `.raw.json`) | CLEAN — `a-code-2.md:549` | **LEAK** — `collector.py:350,359` + `cli.py:573` (same raw-tail sequence; also a JSON body with a duplicate key); NOT CHECKABLE FROM READS: a `KeyboardInterrupt` traceback under the top-level handler | 1 of 3 |
| S-4 outbound guard | CLEAN — `:428-433`, `:421-427`, only keyed POST is `_send` `:533` | CLEAN — `a-code-2.md:419` | CLEAN — `_send` `:534` reached only via `_classify` `:340`; part-B runner not visible | 3 of 3 |
| S-5 discovery keyless | CLEAN — `:452-456`, `:494` | CLEAN — `a-code-2.md:453` | CLEAN — `:456`; `test_classify_discover.py:480-494` | 3 of 3 |
| S-6 hosts / network | CLEAN — `config.py:125-134`, urllib only | CLEAN — `a-code-1.md:126` | **LEAK** — `collector.py:254-256`: default opener follows a 301/302/303 to any host and re-sends `Authorization` (needs OpenRouter itself to redirect) | 2 of 3 |
| S-7 fixtures | CLEAN — no key, no `Authorization`; `SHAPE:` markers | CLEAN — `a-tests-2.md:403` | CLEAN — NOT CHECKABLE FROM READS: "no value changed" against the saved YAML (run a diff) | 3 of 3 |
| S-8 tests prove S-1…S-4 | CLEAN — for the 401 path, instance cache, zero-call refusals; the two S-3 sequences have no test | CLEAN — `a-tests-1.md:174` | Partial — dropped `from None` at `:552` and a module-global cache stay green; loguru-sink tests assume no log patcher (conftest not provided) | 2 of 3 |
| S-9 the one keyed command | **LEAK** — the raw file (`cli.py:91`) and the ledger `call_id` can carry the key (via S-3) | CLEAN — `a-code-1.md:546` | Not clean — S-3 applies to `.raw.json`; a redirect would make it two requests; a non-200 leaves no ledger line; a failed probe leaves no file so code does not refuse a re-run | 1 of 3 |

LEAK claims in the checkers' own words (≤40 words; my file-check under `## Checked against the branch`):
- grok S-3 (a): "collector.py:387-388. On HTTP 200, call_id is the response id and ledger.record runs before _guard_stored. A body whose id contains the key writes that key into scratch/classify-spend.jsonl."
- grok S-3 (b) / opus S-3: "a non-200 other than 401/403 whose body is not JSON stores only raw[:2000] on the record, guards that, and returns the full raw. cli.py:91 writes those bytes to .raw.json."
- opus S-6: "urlopen uses the default opener, which follows redirects. For a POST it follows 301/302/303 as a GET, copying every non-content header, Authorization included, to any Location host."
- grok S-9: "The raw file can [carry the key]: the S-3 tail sequence writes it at cli.py:91. The ledger line can carry it via call_id (S-3)."
Contradiction, both quoted, none smoothed: gemini "S-3: CLEAN — a-code-2.md:549 … S-6: CLEAN — a-code-1.md:126 … S-9 … CLEAN" against opus "S-6 LEAK — collector.py:254-256" and grok "S-3 LEAK — collector.py:387-388"; grok S-6 "CLEAN — config.py:125-134 allows only https and hostname openrouter.ai" against opus S-6.

## Per step
| step | grok | gemini | opus | checkers answering CLOSED |
|---|---|---|---|---|
| R1-config | CLOSED — `config.py:125-150`; tests `:115`…`:139` | CLOSED | CLOSED — `config.py:126-151` | 3 of 3 |
| R2 | NOT CLOSED — `collector.py:359` + `cli.py:91`; `:387-388` ledger `id` before the guard (`:393`) | CLOSED | NOT CLOSED [R2-T] — `test_classify_keys.py:274-280`: dropping `from None` at `collector.py:552` turns no test red; module-global cache untested | 1 of 3 |
| R3 | CLOSED — `:494-501`; `test_classify_discover.py:89`, `:98` | CLOSED | CLOSED — `collector.py:495`, `:505-516` | 3 of 3 |
| R4 | NOT CLOSED — the probe write, `cli.py:91` (same hole as R2) | CLOSED | NOT CLOSED [R4-RAW] — `collector.py:359` / `cli.py:573`; minor [R4-b] `door.py:198,219` raise `KeyError` if the live capture has no `usage.cost` | 1 of 3 |
| R6-docs | CLOSED — five DevDocs, `SHAPE:` markers | CLOSED | CLOSED — two DevDoc sentences become false while S-3 / S-6 stand (`collector.md:152`, `cli.md:224-226`) | 3 of 3 |

## Spend
Per checker, verbatim ≤40 words:
- gemini: "a-code-2.md:387 DOES — a cost of `None` skips `ledger.record`, counting as 0. (Additionally, `a-code-2.md:360` returns early on HTTP errors without writing a ledger line, allowing unlimited failed calls to bypass total demand tracking)."
- opus: "[SPEND] `collector.py:387-389` DOES. When a call has no cost, it gets no ledger line. That covers every non-200 and a 200 without `usage`. … The call ceiling cannot see these calls. If OpenRouter bills them, the cap cannot see them either." Also: "`_is_number` accepts a **negative** returned cost (`:367`), which would lower the ledger total."
- grok: "`collector.py:361-388` DOES — a 200 with no `usage` leaves `cost` `None` and skips `record` … `stop_if` is never called on the send path (`:395` is only the 10× `check_cost`), so a returned cost that crosses the cap but stays at or under 10× its projection is recorded and the call returns success over the cap."
- sol: METER, no answer.

## Plan conformity
R4 items (from the SECOND question), per checker:
- request field for field from the schema: grok "The request is `{model, state, questions}` only (`render_systemone`) … no undocumented field is added"; gemini R4 CLOSED (no detail given); opus "exactly `{model, state, questions}`, per the schema (`:152-174`). No field is added."
- probabilities / confidence only from the response: grok "taken only from the response, else `None` / `source: absent`; the Noul example fixture invents neither"; opus "come only from the response; absent means `None` (`:228-230`). The fixtures invent none."; gemini CLOSED.
- returned model id: grok "`model_returned` is the response's `model`"; opus "`model_returned` is the returned value."
- invalid answer counted `invalid`: grok "status: invalid, not a label"; opus "becomes `invalid` plus a log line."
- 429 / 5xx recorded, not retried: grok "429 and every other non-200 except 401/403 are recorded once, not retried"; opus "429 is recorded once, not retried."
- parse tests parametrized, zero fixtures fails: grok "zero files fails `test_there_is_at_least_one_response_fixture` rather than skipping"; opus "glob-parametrized, and zero fixtures FAIL (`door.py:173-180`)". Opus adds [R4-b]: `door.py:198,219` raise `KeyError` on a live capture without `usage.cost`.

## Assertions and boundary
| checker | (a) weaker / skipped / empty tests | (b) reaches outside the module | (c) silent failure |
|---|---|---|---|
| grok | NONE — "no part-A test uses skip or xfail, and none asserts a name it does not check" | NONE | `cli.py:91` DOES — the non-200 raw tail is written after the guard has seen only the prefix; discovery, price and answer paths are loud |
| gemini | NONE | NONE | NO PATH |
| opus | NONE — "No part-A test carries skip or xfail, and every test asserts." | NONE | two silent paths: `cli.py:573` (a partly unguarded raw body is written) and `collector.py:387` (a missing cost is left out of the ledger) |
| sol | METER | METER | METER |

## Checked against the branch
Originals under `/Users/cobalt/cobalt-wt/jev-trial/` (= `45f647a` for part A; PREFLIGHT proved it), source line numbers. Claim · who · file:line · verdict · note.
| # | claim | who | file:line | verdict | note |
|---|---|---|---|---|---|
| C1 | urllib re-sends `Authorization` on a redirect to any host (S-6) | opus | `collector.py:253-256` (`urlopen`, default opener; no `build_opener` anywhere — iv-2 lists only `:43`, `:253`, `:255`); header built `:544`; stdlib `urllib/request.py:631-654` of the venv's base Python 3.14.3 (`newheaders` = every header except `content-length` / `content-type`, no host check; 301/302/303 on POST → GET) | HOLDS | the line that hands the header to the default opener is `:255`. The trigger — OpenRouter answering the POST with a 3xx — is external and not settled by reads |
| C2 | a non-200 body is written to `.raw.json` after the guard saw only `rec` (S-3 / R4-RAW) | opus, grok | `collector.py:349` (`raw[:2000]` for a non-JSON body), `:354-359` (`_guard_stored(rec…)` only, `return rec, raw`); `cli.py:86-91` writes `raw` with no guard of its own | HOLDS | the 200 path guards the full raw (`:394`); 401/403 raise first. A key past byte 2000 (non-JSON), or an earlier duplicate JSON key, is never shown to the guard. It needs the server to echo the key |
| C3 | the response `id` is written to the ledger before the stored guard (S-3a / R2) | grok | `collector.py:386-388` (`call_id = _str_field(resp,"id")` → `ledger.record`), stored guard only at `:393`; `ledger.py:104`, `:109-110` write `call_id` as given | HOLDS | needs a 200 with `usage` and an `id` that holds the key |
| C4 | a call with no cost leaves no ledger line, so `spent()` and `calls()` do not see it | gemini, opus, grok | `collector.py:354-359` (non-200 returns before any ledger write), `:361-371` (cost `None` when `usage` absent), `:386-388` (`if cost is not None`); `ledger.py:55-59` (`spent` / `calls` read only recorded lines) | HOLDS | as code. Whether OpenRouter bills such calls: NOT CHECKABLE FROM READS — the probe `31` is the first evidence |
| C5 | `_is_number` accepts a negative returned cost, lowering the ledger total | opus | `collector.py:176-177` (finite int or float, not bool — no sign test), `:366-367`, `ledger.py:56` sums `cost_usd`, `:101-110` records any float | HOLDS | needs a response with a negative `usage.cost` |
| C6 | `stop_if` is never called on the send path | grok | `grep stop_if`: defined `ledger.py:80`, called only at `trial.py:187` | PART B — carried to 37 | the runner (part B) owns the running-total stop |
| C7 | a regression dropping `from None` on the transport-exception path turns no test red (R2-T) | opus | `test_classify_keys.py:100-106` asserts only `FAKE_KEY not in str(ei.value)`; the `__cause__ is None and __suppress_context__` assertion (`:97`) belongs to the 401 test; the raise is `collector.py:550-551` | HOLDS | the assertion that stays true after the regression is `:106` |
| C8 | a module-global key cache stays green | opus | `test_classify_keys.py:88` checks `vars(clf)`; `:108-113` (missing key → raise, zero calls) would fail if a cache survived, in file order | NOT CHECKABLE FROM READS — run `test_classify_keys.py` with the key cached in a module global | not stated as a defect here |
| C9 | [R4-b] `door.py:198,219` raise `KeyError` on a live capture with no `usage.cost` | opus | `test_classify_door.py:197` (`fx["usage"]["cost"]`), `:218` (`del fx["usage"]["cost"]`) | NOT CHECKABLE FROM READS — depends on `31`'s capture | the code lines exist as stated; the schema marks `cost` optional |
| C10 | loguru-sink tests assume no log patcher | opus | tests `keys.py:76-88`, `door.py:264-273` | NOT CHECKABLE FROM READS — run the keys tests with `install_log_guard` active | conftest not in the packet |
| C11 | a `KeyboardInterrupt` traceback could print the header | opus | top-level handler in `src/cobalt/cli.py` (a part-B file) | PART B — carried to 37 (NOT CHECKABLE FROM READS — Ctrl-C mid-POST under the real handler) | |
| C12 | S-7: the example fixture "no value changed" against the saved YAML | opus | `grep -c -F` of four distinctive values (`customer_tier`, the generation id, the cost, "Blocking revenue right now") on `scratch/docs-openrouter/submit-a-system-one-request.md` = 5 lines | NOT CHECKABLE FROM READS — a full diff | partial support only |
| C13 | a failed probe leaves no file, so the code does not refuse a re-run | opus | `cli.py:77-82` refuses only on an existing `probe-*.json`; the build prompt's R4 says exactly that | recorded, not a defect claim | `31` carries "never retried" |
| C14 | two DevDoc sentences become false while C1 / C2 stand | opus | `collector.md` "talks to any host but `openrouter.ai` (config-validated)"; `cli.md` "What it never does" | dependent on C1 / C2 — not counted separately | |
| C15 | S-4: `classify()` is the ONLY function that sends a keyed request | grok, opus, gemini | `grep "_send(\|\.transport("`: keyed POST only at `collector.py:548` inside `_send`, called only at `:339` in `_classify`; `_classify` called at `:325` (`classify`) and `cli.py:86` (`probe`); `trial.py` has no `_send`, `_classify` or `transport` call | HOLDS | the checkers' three CLEAN agree |

(i) `git log --stat --oneline 47fafe5..45f647a` names only PREFLIGHT's boundary paths (29), each in exactly one part (A 17 + B 12; PREFLIGHT row 45).
(ii) PROTECTED PATHS: `git log --oneline 47fafe5..45f647a -- src/cobalt_agent configs/config.yaml src/cobalt/radar src/cobalt/aset src/cobalt/cards src/cobalt/db_migrations src/cobalt/redact` → EMPTY.
(iii) `grep -rn "Fernet\|cobalt_agent\|\.cobalt_vault" src/cobalt/classify` → no output. `grep -rn "read_secret" src/cobalt/classify` → `collector.py:8` (the docstring) and `collector.py:404` (`value = vault_secrets.read_secret(KEY_NAME)`).
(iv) `grep -rln "import requests\|import httpx\|litellm\|typesafe_sdk\|subprocess\|os.system"` → no output. `grep -rn "urlopen\|urlrequest\|build_opener"` → `collector.py:43`, `:253`, `:255` — every hit in `collector.py`.
(v) wrapper: `grep -c -F -x -e 'source "$KEY_FILE"'` = 1 · `wc -l` = 25 · `grep -c -E "^[^#]*(COBALT_MASTER|OPENROUTER|set -x|printenv)|^env"` = 0.
(vi) `git log -p 47fafe5..45f647a -- <the four part-A test files>` (4 commits): ONE `-` line, `537c0978` on `test_classify_config.py`: `raw["classify"]["chat_url"] = "https://example.com/api/v1/chat/completions"` replaced by the `+` line `raw["classify"]["door_url"] = "https://example.com/api/v1/systemone"` (a re-point, no `assert` removed; the build report says the same, R4 (C)); `skip` / `xfail` on `+` lines: 1 text hit, the message string `never a skip` in `test_classify_door.py` (`assert RESPONSES, "no tests/fixtures/classify/openrouter-*response*.json — L1: never a skip"`) — not a marker.
(vii) L32: I read my own report once before the last line: no ticker written. L41: no key material written (the report names `OPENROUTER_API_KEY` and `COBALT_MASTER_KEY` as NAMES only; the quoted lines carry only the tests' constructed `sk-or-v1-TESTONLY-…` placeholder text and quoted grep commands).
(viii) RESTARTS (L42), the build report's line: `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`; its ESCALATE item 22 says `cobalt jobs restarts 47fafe5..HEAD` exits 1 with two unclassified paths (`configs/cobalt/classify/trial.yaml`, `ops/run_classify_trial.sh`), all six residents derived. NOT CHECKABLE FROM READS — `uv run cobalt jobs restarts 47fafe5..45f647a`; no checker's claim is settled by it.

## Ready for the probe
| checker | CHECK JEV A line | ready | reason verbatim |
|---|---|---|---|
| grok | `CHECK JEV A: SECRETS LEAK S-3, S-9 · DEFECT REMAINS R2, R4, SPEND · ready for the probe: NO · raw error tail and ledger id can hold the key` | NO | raw error tail and ledger id can hold the key |
| gemini | `CHECK JEV A: SECRETS CLEAN · BUILD STANDS EXCEPT THIRD · ready for the probe: YES · key handling is clean, safe and isolated` | YES | (none given; the text after YES reads "key handling is clean, safe and isolated") |
| opus | `CHECK JEV A: SECRETS LEAK S-3 S-6 · DEFECT REMAINS R2-T R4-RAW SPEND · ready for the probe: NO · urllib forwards Bearer on cross-host redirect; non-200 raw tail unguarded` | NO | urllib forwards Bearer on cross-host redirect; non-200 raw tail unguarded |
| sol | METER — retry after Sep 26th, 2026 6:47 AM | — | — |

The gate, by §4's rule (arithmetic, not a verdict): houses answering with a `CHECK JEV A:` line = **3** (≥ 3 ✓) · `secrets LEAK that HOLD` = **3** (must be 0 ✗) · `defects that HOLD` = **3** (must be 0 ✗) → **probe gate: NOT READY**. The checkers' own `ready` answers (NO, YES, NO) are shown, never counted.

## FOR THE CLASSIFIER
Round 1 of ≤3 (L67 / L39). One item per claim that HOLDS in my file-check; no class, no recommendation.
1. LEAK — "the raw body of a non-200 is written without a full guard" (opus S-3 `collector.py:350,359` + `cli.py:573` / R4-RAW; grok S-3 second sequence, S-9, R2, R4, (c)). Mine: `collector.py:349`, `:354-359`; `cli.py:86-91`. HOLDS.
2. LEAK — "`urlopen` uses the default opener, which follows redirects … copying every non-content header, `Authorization` included, to any `Location` host" (opus S-6, `collector.py:254-256`). Mine: `collector.py:253-256`, `:544`; stdlib `urllib/request.py:631-654`. HOLDS.
3. LEAK — "On HTTP 200, `call_id` is the response `id` and `ledger.record` runs before `_guard_stored`. A body whose `id` contains the key writes that key into `scratch/classify-spend.jsonl`" (grok S-3 first sequence, S-9, R2). Mine: `collector.py:386-388`, `:393`; `ledger.py:104`, `:109-110`. HOLDS.
4. SPEND — "When a call has no cost, it gets no ledger line. That covers every non-200 and a 200 without `usage`. Neither `spent()` nor `calls()` advances" (opus SPEND `collector.py:387-389`; gemini THIRD `a-code-2.md:387`, `:360`; grok SPEND `:361-388`). Mine: `collector.py:354-359`, `:361-371`, `:386-388`; `ledger.py:55-59`. HOLDS (as code; billing of such calls NOT CHECKABLE FROM READS).
5. SPEND — "`_is_number` accepts a negative returned cost (`:367`), which would lower the ledger total" (opus). Mine: `collector.py:176-177`, `:366-367`; `ledger.py:56`, `:101-110`. HOLDS.
6. TEST — "[R2-T] `test_classify_keys.py:274-280`: a regression dropping `from None` at `collector.py:552` turns no test red" (opus R2 NOT CLOSED, S-8). Mine: `test_classify_keys.py:100-106` (asserts `:106` only), raise at `collector.py:550-551`. HOLDS.

## ESCALATE
1. **LEAK that HOLDS — the non-200 raw body written past the guard** (FOR THE CLASSIFIER 1; opus S-3 / grok S-3, S-9). No key material reached any file: the build made no keyed call and nothing was captured.
2. **LEAK that HOLDS — a redirect re-sends `Authorization`** (FOR THE CLASSIFIER 2; opus S-6; grok and gemini answered S-6 CLEAN — both quoted above).
3. **LEAK that HOLDS — the response `id` reaches the ledger before the stored guard** (FOR THE CLASSIFIER 3; grok S-3). No `ASK DESK: rotate OPENROUTER_API_KEY` is raised: none of the held lines shows key material reaching a committed file, a report or captured stdout (no keyed call was made).
4. Checkers' `DEFECT REMAINS`: grok `R2, R4, SPEND`; opus `R2-T R4-RAW SPEND`; gemini `BUILD STANDS EXCEPT THIRD`.
5. Defect that HOLDS — cost-less and non-200 calls are invisible to the ledger (FOR THE CLASSIFIER 4).
6. Defect that HOLDS — a negative returned cost is accepted (FOR THE CLASSIFIER 5).
7. Defect that HOLDS — the `from None` regression on the transport-exception path stays green (FOR THE CLASSIFIER 6).
8. Output of the mechanical searches: (iv)'s second search prints `collector.py:43`, `:253`, `:255` (all in `collector.py`, allowed); (vi) prints one `-` line (the `chat_url` → `door_url` re-point) and one text hit for "skip". (ii), (iii)'s first search and (iv)'s first search are empty; (v) matches.
9. `PART B — carried to 37`: C6 (grok: `stop_if` is called only at `trial.py:187` — does the runner stop after every call, in parallel mode too?) and C11 (opus: a `KeyboardInterrupt` traceback under the top-level handler in `src/cobalt/cli.py`).
10. A checker that did not check: **sol — METER, retry after Sep 26th, 2026 6:47 AM** (`ERROR: You've hit your usage limit …`); three houses (Grok, Gemini, Opus 5.5) checked, L67's floor met. No `ASK DESK` (the count is three).
11. The L74 line: one block arrived (the Read result of `29-jev-trial-check.md`), recorded once under `## L74`, not followed.
12. This check covers PART A (the secret and network path) of the JEV trial build, `47fafe5..45f647a` of `jev/trial-0923` — 17 files; part B (`37`) covers the other 12. It is round 1 of ≤3 (L67 / L39). With three houses checked, `secrets LEAK that HOLD: 0` and `defects that HOLD: 0`, the build is READY for the ONE keyed probe `31` (N2, his R42 condition); the merge of this branch and the trial runs also need part B's gate READY; a HOLD goes to a classifier and a fix round (L75), and `31` does not launch.
13. Nothing in this check measures the product. The build made no keyed call: its public reads answered U1, U2 and U5 (`build-report.md` `## DISCOVERY`); U3, U4 and U6 are answered only by the probe `31`, after this check; the trial's bars (plan §4) are measured only by the trial run.

JEV TRIAL CHECK DONE · part: A (secret + network path) · grok: CHECK JEV A: SECRETS LEAK S-3, S-9 · DEFECT REMAINS R2, R4, SPEND · ready for the probe: NO · raw error tail and ledger id can hold the key · gemini: CHECK JEV A: SECRETS CLEAN · BUILD STANDS EXCEPT THIRD · ready for the probe: YES · key handling is clean, safe and isolated · opus: CHECK JEV A: SECRETS LEAK S-3 S-6 · DEFECT REMAINS R2-T R4-RAW SPEND · ready for the probe: NO · urllib forwards Bearer on cross-host redirect; non-200 raw tail unguarded · sol: METER — retry after Sep 26th, 2026 6:47 AM · secrets LEAK that HOLD: 3 · defects that HOLD: 3 · probe gate: NOT READY · ESCALATE: 13
