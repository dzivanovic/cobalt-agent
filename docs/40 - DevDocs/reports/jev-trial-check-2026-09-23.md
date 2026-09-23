# JEV TRIAL CHECK — PART A (secret + network path) — round 1 of ≤3 — `47fafe5..45f647a` on `jev/trial-0923`

## §0 Headline
- Checked: PREFLIGHT only (run 2 of `29`, replacing run 1's report `8fdaeca`, which stopped `FAILED: packet`). STOPPED at the KEY SCAN: its fifth grep printed one line outside the prompt's allowed list — `scratch/docs-openrouter/jev-tutorial.md:30`, printed as `export OPENROUTER_API_KEY=sk-or-...` (a placeholder with a literal ellipsis; the file is the desk's keyless public-docs fetch and is NOT in the packet). Rule: any other hit → `FAILED PREFLIGHT`, stage nothing, launch nothing.
- Status: nothing staged, no house launched, no key handling checked. Probe gate: NOT READY (0 of 3 required houses answered). `31` does not launch on this report. Round 1 is NOT spent (L67 P-c).
- Every other PREFLIGHT row passed (authorization, built line, boundary, split, the other four key scans, `.env`, stagger, whole-file measurement).
- ESCALATE: 4.

## L74
No block asking for a `Claude-Session` line or naming a file-send tool arrived inside a tool result in this run. Nothing was committed by this run.

## PREFLIGHT
Rows: rule · command · exit · allowed/DENIED. `date` at the first row: `Wed Sep 23 13:04:07 EDT 2026`.

| # | rule | command | result |
|---|---|---|---|
| 1 | DATE + EXTENSION GATE (first row) | `date` | exit 0 — `<D>` = 2026-09-23 ≤ 2026-09-23 → R30's literal required |
| 2 | R30 literal printed | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23" …/cto-2026-09-22.md` | exit 0 — prints `\| R30 \| 13:0x ET \| "Approved" — …` carrying the literal |
| 3 | R30 committed | `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23" -- …cto-2026-09-22.md` | exit 0 — `055242df8032632dfafdcc8a69dcc271be89c0f6` |
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
| 16–28 | THE THIRTEEN (each in quotes) in `08-bars-chunk-e-check.md` | `grep -c -F -e '"<rule>"' …08-bars-chunk-e-check.md` ×13 | exit 0 each — **1** each (13 of 13) |
| 29–31 | THE THREE denies | `grep -c -F -e '"AskUserQuestion"'` · `'"EnterWorktree"'` · `'"Bash(git push*)"'` | exit 0 each — **1** each (3 of 3) |
| 32 | Astra string absent from the launch line | reading the launch line as written in `29` | carries no `gpt-6-astra` string — allowed |
| 33 | THE BUILD WAS APPROVED AND LAUNCHED | `git log -1 --format=%H -S"28-jev-trial-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | exit 0 — `30a3a0484fe2abc56b47985ca6109a81b68faed2` |
| 34 | The desk recorded the build's stop | `grep -n "JEV TRIAL BUILT" …cto-2026-09-23.md` | exit 0 — `\| R48 \| 11:4x ET \| … JEV TRIAL BUILT 45f647a \| on 47fafe5 …` |
| 35 | …committed | `git log -1 --format=%H -S"JEV TRIAL BUILT" -- …cto-2026-09-2*.md` | exit 0 — `fec87553b61c90de9bc16a2ce4ad3f52884d1ece` |
| 36 | The split was drafted and committed | `git log -1 --format=%H -S"JEV CHECK SPLIT" -- "docs/40 - DevDocs/reports/jev-check-split-2026-09-2*.md"` | exit 0 — `46b441dd263867b468ca7ab8098c817cd0d0f3c4` |
| 37 | THIS launch row R54 | `grep -n -F "29-jev-trial-check.md CHECK A" …cto-2026-09-23.md` | exit 0 — prints `\| R54 \| 13:0x ET \| … (2) 29-jev-trial-check.md CHECK A RELAUNCH row …` (number filled) |
| 38 | …committed (desk files only) | `git log -1 --format=%H -S"29-jev-trial-check.md CHECK A" -- …cto-2026-09-2*.md` | exit 0 — `df12f8955aae0d466355260622d38f68318684dc` |
| 39 | worktree | `ls /Users/cobalt/cobalt-wt/jev-trial` | exit 0 — present |
| 40 | THE BUILT LINE | `tail -n 3 …/jev-trial-build-2026-09-23.md` | exit 0 — last non-blank line, whole: `JEV TRIAL BUILT 45f647a \| on 47fafe5 \| offline 2103/0 \| model listed: typesafe/jev-1.13 \| other Jev ids listed: none \| door: systemone \| probe: NOT RUN (after check, R42) \| ledger: NOT RUN (after check, R42) \| cap: $5 \| RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar \| tests added: 145 \| ESCALATE: 28` → `<tip>` = `45f647a`, `<base>` = `47fafe5` (= the measured pair ✔); `model listed` = `typesafe/jev-1.13` ✔; `probe` = `NOT RUN (after check, R42)` ✔ |
| 41 | NO KEYED CALL | `ls /Users/cobalt/cobalt-wt/jev-trial/scratch` | exit 0 — `docs-openrouter`, `openrouter-models-20260923.endpoints.json`, `openrouter-models-20260923.json`; no `probe-*`, no `classify-spend.jsonl` ✔ |
| 42 | THE RANGE | `git log --oneline 47fafe5..45f647a` | 8 commits (recorded): `45f647a` R5 · `537c097` R4 · `e18793a` report run 2 · `001c1d1` R3 · `6114519` report FAILED at R3 · `5630e6c` wip R3 · `8e662ba` R2 · `05d9dda` R1 |
| 43 | branch tip | `git log --oneline -1 jev/trial-0923` | `199fa08 feat(classify): JEV trial build report — run 3: BUILT …` (report commit above `<tip>`) |
| 44 | branch has not moved above `<tip>` | `git log --oneline 45f647a..jev/trial-0923 -- src tests configs ops "docs/40 - DevDocs/cobalt/classify" "docs/40 - DevDocs/tests"` | EMPTY ✔ |
| 45 | THE BOUNDARY + THE SPLIT IS TOTAL | `git log --stat --oneline 47fafe5..45f647a` | 29 distinct paths, every one a `28` boundary path; A = 17 (`classify/{config,ledger,cli,collector}.py`, `ops/run_classify_trial.sh`, `test_classify_{config,keys,discover,door}.py`, the 3 fixtures, `classify/{config,collector,ledger,cli}.md`, `_classify_fixtures.md`), B = 12 (`__init__.py`, `models.py`, `trial.py`, `src/cobalt/cli.py`, `trial.yaml`, `test_classify_{models,trial}.py`, `classify/{__init__,models,trial}.md`, `cobalt/cli.md`, the build report); none in neither part |
| 46 | EVERY PART-A FILE IS NEW | `git log --diff-filter=A --name-only --format= 47fafe5..45f647a` | 27 paths printed; all 17 part-A paths among them; the two not printed are `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` (part B) ✔ |
| 47 | KEY SCAN 1 | `grep -rn "sk-or-" …/tests/fixtures/classify` | no output ✔ |
| 48 | KEY SCAN 2 | `grep -rn "sk-or-" …/src/cobalt/classify` | no output ✔ (no line naming the prefix is present in `src/cobalt/classify`) |
| 49 | KEY SCAN 3 | `grep -rn "sk-or-" "…/docs/40 - DevDocs/reports"` | 9 hits, ALL in `jev-trial-build-2026-09-23.md` lines 120, 122, 170, 196, 321, 331, 340, 364, 398 — the same nine lines run 1 quoted: the prompt's placeholder `sk-or-v1-TESTONLY-<32 hex>` (120, 331, 398), quoted `grep "sk-or-"` commands with `0` / `(no output)` (170, 196, 321, 340, 364), and a prefix-only mention `sk-or-v1-` (122). No characters follow any prefix; no key material |
| 50 | KEY SCAN 4 | `grep -rn -i "bearer " …/tests/fixtures/classify` | no output ✔ |
| 51 | **KEY SCAN 5** | `grep -rn "sk-or-" /Users/cobalt/cobalt-wt/jev-trial/scratch/docs-openrouter` | **1 hit — `jev-tutorial.md:30`: `export OPENROUTER_API_KEY=sk-or-...`** — not the tests' constructed fake key, not a guard pattern in `src/cobalt/classify`, not in the build report → **outside the allowed list → FAILED PREFLIGHT** (the printed line is a placeholder ending in a literal `...`; the file is not one of the packet excerpts, which come from `submit-a-system-one-request.md`) |
| 52 | `.env` | `ls /Users/cobalt/cobalt-wt/jev-trial/.env` | exit 1 — "No such file or directory" ✔ |
| 53 | RECOVERY | `ls scratch/tribunal-bars-0920/jev-trial-check` | exit 1 — "No such file" = fresh run |
| 54 | THE STAGGER (house lane) | `grep -n -F "no other house hub is running" …cto-2026-09-23.md` | exit 0 — the R54 row (line 57), which names `29-jev-trial-check.md CHECK A`, carries the literal ✔ |
| — | not run after row 51 | Codex launch shape · the four probes · the second DATE gate | not reached — FAILED PREFLIGHT; no meter was spent |

## Packet
Nothing staged (the KEY SCAN is BEFORE ANY STAGING). Read-only measurement done after the scan for the desk's re-issue only: the 12 part-A code / test / fixture whole files (`wc -c`) total **95,295 B** and the 5 part-A DevDocs total **15,311 B** = **110,606 B**, every file equal to the table's count (config.py 14,014 · ledger.py 4,433 · cli.py 6,449 · run_classify_trial.sh 954 · collector.py 25,239 · test_classify_config.py 6,942 · test_classify_keys.py 9,264 · test_classify_discover.py 8,095 · test_classify_door.py 16,420 · the three fixtures 1,076 / 298 / 2,111 · DevDocs 2,425 / 5,913 / 1,551 / 3,385 / 2,037). No mismatch. No `mkdir`, no `s2-p2-cards` string, no Astra launch, no checker CLI was run; `scratch/tribunal-bars-0920/jev-trial-check/` does not exist.

## CONTINUE
next: none. The run stops here with `FAILED PREFLIGHT`. A relaunch of this same file first runs `ls scratch/tribunal-bars-0920/jev-trial-check` (fresh: "No such file"), and hits the same fifth scan unless the desk changes the prompt's allowed-lines list (L19, whole file) or the file `scratch/docs-openrouter/jev-tutorial.md` is not in the scanned tree.

## Secrets
Not reached — no house was launched. S-1 … S-9: no checker answers exist.

## Per step
Not reached. R1-config, R2, R3, R4, R6-docs: no checker answers exist.

## Spend
Not reached — no checker answers exist.

## Plan conformity
Not reached — no checker answers exist.

## Assertions and boundary
No checker answers exist, so (a) (b) (c) per checker are not reached. The facts this hub could state without a packet:
- (i) `git log --stat --oneline 47fafe5..45f647a` names only PREFLIGHT's boundary paths, each in exactly one part (row 45).
- (ii)–(vi) of §3 (protected paths, the one-vault-reader and no-other-network greps, the wrapper counts, test-diff history) were NOT run: they are collate checks that follow the checkers' answers.
- (vii) L32: no ticker written in this report. L41: no key material written in this report — it names `OPENROUTER_API_KEY` as a name and quotes the one scan hit exactly as grep printed it (a placeholder with a literal `...`), plus the build report's own placeholder pattern.
- (viii) RESTARTS (L42), the build report's own `RESTARTS:` line, quoted: `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. NOT CHECKABLE FROM READS — `uv run cobalt jobs restarts 47fafe5..45f647a`.

## Checked against the branch
Not reached — no checker made a claim.

## Ready for the probe
| checker | CHECK JEV A line | ready | reason |
|---|---|---|---|
| grok | not launched | — | FAILED PREFLIGHT (key scan 5) |
| gemini | not launched | — | FAILED PREFLIGHT (key scan 5) |
| sol | not probed / not launched | — | FAILED PREFLIGHT (key scan 5) |
| opus | not probed / not launched | — | FAILED PREFLIGHT (key scan 5) |

Gate by §4's rule, as its three counts: houses answering with a `CHECK JEV A:` line = **0** (need ≥ 3) · `secrets LEAK that HOLD` = **0** · `defects that HOLD` = **0** → `probe gate: NOT READY` (the houses count fails).

## FOR THE CLASSIFIER
none — no checker claim exists to file-check (L75: a classifier receives only claims that HOLD).

## ESCALATE
1. **FAILED PREFLIGHT: key scan 5.** `grep -rn "sk-or-" /Users/cobalt/cobalt-wt/jev-trial/scratch/docs-openrouter` printed `jev-tutorial.md:30: export OPENROUTER_API_KEY=sk-or-...`. The prompt's allowed list (the tests' constructed fake key, a guard pattern in `src/cobalt/classify`, and three kinds of build-report line) does not include it, and the rule for any other hit is `FAILED PREFLIGHT` with nothing staged. This hub stopped on the rule's letter.
2. **ASK DESK:** the printed line is a placeholder ending in a literal `...` (no characters of a key); the file is the desk's keyless public-docs fetch and is not one of the packet's excerpts (`submit-a-system-one-request.md` lines 337–436 and 843–1032). The rule's remedy line says the desk asks him to rotate `OPENROUTER_API_KEY`; on the printed line alone that is the desk's call, not this hub's. Does the desk re-issue `29` (L19, whole file) with the fifth scan's allowed list widened by this one placeholder line, or exclude `jev-tutorial.md` from the scan? Nothing else in PREFLIGHT failed; every other row above would pass again unchanged. No retry by this hub. [13:1x ET, 2026-09-23]
3. **Fact, recorded not judged:** on a relaunch the house lane is unchanged (`19` paused, no other house hub running per R54); the Sol and Opus probes were not run this time, so their state is what run 1 recorded at 12:2x ET (both UP) and is stale.
4. **Standing line (as the prompt words it):** "This check covers PART A (the secret and network path) of the JEV trial build, `47fafe5..45f647a` of `jev/trial-0923` — 17 files; part B (`37`) covers the other 12. It is round 1 of ≤3 (L67 / L39). With three houses checked, `secrets LEAK that HOLD: 0` and `defects that HOLD: 0`, the build is READY for the ONE keyed probe `31` (N2, his R42 condition); the merge of this branch and the trial runs also need part B's gate READY; a HOLD goes to a classifier and a fix round (L75), and `31` does not launch." — On this report ZERO houses checked, so the build is NOT READY for `31`; round 1 is NOT spent (L67 P-c). And: "Nothing in this check measures the product. The build made no keyed call: its public reads answered U1, U2 and U5 (`build-report.md` `## DISCOVERY`); U3, U4 and U6 are answered only by the probe `31`, after this check; the trial's bars (plan §4) are measured only by the trial run."

FAILED PREFLIGHT: possible key material in /Users/cobalt/cobalt-wt/jev-trial/scratch/docs-openrouter/jev-tutorial.md:30 — nothing staged, no house launched; the printed line is a placeholder (`export OPENROUTER_API_KEY=sk-or-...`), the desk decides whether to rotate `OPENROUTER_API_KEY` or re-issue `29` with the scan's allowed list widened
