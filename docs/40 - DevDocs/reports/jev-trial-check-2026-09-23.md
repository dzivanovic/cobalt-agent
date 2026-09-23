# JEV TRIAL CHECK — round 1 of ≤3 — `47fafe5..45f647a` on `jev/trial-0923`

## §0 Headline
- Checked: the Jev trial collector build `47fafe5..45f647a` (8 commits) — PREFLIGHT and the key scan only. STOPPED at staging: `FAILED: packet` — the measured originals alone are 316,683 B against the 230,000 B whole-packet ceiling (≥ 86,683 B over). No packet staged, no house launched, no key handling checked.
- Probe gate: NOT READY (0 of 3 required houses answered). `31` does not launch on this report.
- PREFLIGHT: every authorization gate, the built line, the boundary and all four key scans passed; four houses probed UP (Grok · Gemini · Sol · Opus 5.5).
- ESCALATE: 6 (one FAILED, one ASK DESK, two recorded facts, two standing lines).

## L74
No block asking for a `Claude-Session` line or naming a file-send tool arrived inside a tool result in this run. Nothing was committed by this run.

## PREFLIGHT
Rows: rule · command · exit · allowed/DENIED. Clock times are from `date` (12:24:36 EDT at the first row; 12:28:32 EDT at the write of this report).

| # | rule | command | result |
|---|---|---|---|
| 1 | DATE + EXTENSION GATE (first row) | `date` | exit 0 — `Wed Sep 23 12:24:36 EDT 2026` → `<D>` = 2026-09-23 ≤ 2026-09-23 → R30's literal required |
| 2 | R30 literal printed | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23" …/cto-2026-09-22.md` | exit 0 — prints `\| R30 \| 13:0x ET \| "Approved" — …` carrying the literal |
| 3 | R30 committed | `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23" -- …cto-2026-09-22.md` | exit 0 — `055242df8032632dfafdcc8a69dcc271be89c0f6` NON-EMPTY |
| 4 | grok present | `grok --version` | exit 0 — `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| 5 | agy present | `agy --version` | exit 0 — `1.2.9` — allowed |
| 6 | 66 gate: R13 of 09-20 | `grep -n "^\| R13 " …cto-2026-09-20.md` | exit 0 — row printed |
| 7 | 66 gate: R40 | `grep -n "^\| R40 " …cto-2026-09-21.md` | exit 0 — carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| 8 | 66 gate: R44 | `grep -n "^\| R44 " …cto-2026-09-21.md` | exit 0 — carries `ONE BUILD of the whole FINAL` |
| 9 | 66 gate: R46 | `grep -n "^\| R46 " …cto-2026-09-21.md` | exit 0 — carries `instead of Astra you can use Sol` |
| 10 | R46 committed | `git log -1 --format=%H -S"instead of Astra you can use Sol" -- …cto-2026-09-21.md` | exit 0 — `53e059456750c0c9efcf50222a7a647630dc4b04` |
| 11 | R49 (Sol string) | `grep -n "^\| R49 " …cto-2026-09-21.md` | exit 0 — carries `"Approved"` |
| 12 | R49 Sol string present | `grep -c -F "Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)" …cto-2026-09-21.md` | exit 0 — `1` (≥1) |
| 13 | R49 Sol string committed | `git log -1 --format=%H -S"Bash(codex exec … gpt-5.6-sol …)" -- …cto-2026-09-21.md` | exit 0 — `60147d400b009db5a2518e02b8ab1fe5765db405` |
| 14 | Opus seat string, R32 of 09-22 | `grep -n "^\| R32 " …cto-2026-09-22.md` | exit 0 — carries `claude -p --model claude-opus-5-5` |
| 15 | R32 committed | `git log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- …cto-2026-09-22.md` | exit 0 — `b8a72b5300370e248cd6c7a8a732258fec03e6a0` |
| 16–28 | THE THIRTEEN (each in quotes) in `08-bars-chunk-e-check.md` | `grep -c -F -e '"<rule>"' …08-bars-chunk-e-check.md` ×13 (`Bash(grok *)`, `Bash(agy *)`, `Bash(mkdir -p scratch/tribunal-bars-0920)`, `git -C …/cobalt show*`, `…/cobalt log*`, `…/s2-p2-cards show*`, `…log*`, `…diff*`, `ls *`, `grep *`, `tail *`, `wc *`, `date*`) | exit 0 each — **1** each (13 of 13) |
| 29–31 | THE THREE denies | `grep -c -F -e '"AskUserQuestion"'` · `'"EnterWorktree"'` · `'"Bash(git push*)"'` | exit 0 each — **1** each (3 of 3) |
| 32 | Astra string absent from the launch line | reading the launch line as written in `29-jev-trial-check.md` | carries no `gpt-6-astra` string — allowed |
| 33 | THE BUILD WAS APPROVED AND LAUNCHED | `git log -1 --format=%H -S"28-jev-trial-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | exit 0 — `30a3a0484fe2abc56b47985ca6109a81b68faed2` NON-EMPTY |
| 34 | The desk recorded the build's stop | `grep -n "JEV TRIAL BUILT" …cto-2026-09-23.md` | exit 0 — `\| R48 \| 11:4x ET \| … JEV TRIAL BUILT 45f647a \| on 47fafe5 …` |
| 35 | …committed | `git log -1 --format=%H -S"JEV TRIAL BUILT" -- …cto-2026-09-2*.md` | exit 0 — `fec87553b61c90de9bc16a2ce4ad3f52884d1ece` |
| 36 | THIS launch row R49 | `grep -n "29-jev-trial-check.md" …cto-2026-09-23.md` | exit 0 — `\| R49 \| 12:2x ET \| … LAUNCH 29-jev-trial-check.md …` (number filled) |
| 37 | …committed (desk files only) | `git log -1 --format=%H -S"29-jev-trial-check.md" -- …cto-2026-09-2*.md` | exit 0 — `15a725331d8f6f46c6a2fd35fe02a281670e52a5` |
| 38 | worktree | `ls /Users/cobalt/cobalt-wt/jev-trial` | exit 0 — present |
| 39 | THE BUILT LINE | `tail -n 3 …/jev-trial-build-2026-09-23.md` | exit 0 — last non-blank line, whole: `JEV TRIAL BUILT 45f647a \| on 47fafe5 \| offline 2103/0 \| model listed: typesafe/jev-1.13 \| other Jev ids listed: none \| door: systemone \| probe: NOT RUN (after check, R42) \| ledger: NOT RUN (after check, R42) \| cap: $5 \| RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar \| tests added: 145 \| ESCALATE: 28` → `<tip>` = `45f647a`, `<base>` = `47fafe5`; `model listed` = `typesafe/jev-1.13` ✔; `probe` = `NOT RUN (after check, R42)` ✔ |
| 40 | NO KEYED CALL | `ls /Users/cobalt/cobalt-wt/jev-trial/scratch` | exit 0 — `docs-openrouter`, `openrouter-models-20260923.endpoints.json`, `openrouter-models-20260923.json`; no `probe-*`, no `classify-spend.jsonl` ✔ |
| 41 | THE RANGE | `git log --oneline 47fafe5..45f647a` | 8 commits (recorded): `45f647a` R5 · `537c097` R4 · `e18793a` report run 2 · `001c1d1` R3 · `6114519` report FAILED at R3 · `5630e6c` wip R3 · `8e662ba` R2 · `05d9dda` R1 |
| 42 | branch tip | `git log --oneline -1 jev/trial-0923` | `199fa08 feat(classify): JEV trial build report — run 3: BUILT …` (report commit above `<tip>`) |
| 43 | branch has not moved above `<tip>` | `git log --oneline 45f647a..jev/trial-0923 -- src tests configs ops` | EMPTY ✔ |
| 44 | THE BOUNDARY | `git log --stat --oneline 47fafe5..45f647a` | see `## Assertions and boundary` (i) |
| 45 | KEY SCAN 1 | `grep -rn "sk-or-" …/tests/fixtures/classify` | no output ✔ |
| 46 | KEY SCAN 2 | `grep -rn "sk-or-" …/src/cobalt/classify` | no output ✔ (no guard pattern naming the prefix is present in `src/cobalt/classify` either) |
| 47 | KEY SCAN 3 | `grep -rn "sk-or-" "…/docs/40 - DevDocs/reports"` | 9 hits, ALL in `jev-trial-build-2026-09-23.md` lines 120, 122, 170, 196, 321, 331, 340, 364, 398: each is the prompt's placeholder `sk-or-v1-TESTONLY-<32 hex>`, a quoted `grep "sk-or-"` command whose result is `(no output)` / `0`, or the words "the prefix" — no key material ✔ |
| 48 | KEY SCAN 4 | `grep -rn -i "bearer " …/tests/fixtures/classify` | no output ✔ |
| 49 | `.env` | `ls /Users/cobalt/cobalt-wt/jev-trial/.env` | exit 1 — "No such file or directory" ✔ |
| 50 | RECOVERY | `ls scratch/tribunal-bars-0920/jev-trial-check` | exit 1 — "No such file" = fresh run |
| 51 | THE STAGGER (house lane) | `grep -n -F "no other house hub is running" …cto-2026-09-23.md` | exit 0 — the R49 row (line 52) that names `29-jev-trial-check.md` carries the literal ✔ |
| 52 | THE CODEX LAUNCH SHAPE | `grep -c -F "Experiment field: **reads started**" …setups-tribunal-r2-2026-09-21.md` | `1` → a Sol launch would append ` < /dev/null` (not reached) |
| 53 | PROBE Sol | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` (run_in_background) | exit 0 — `OK`, no usage-limit text → **sol: UP** (the METER expected by 09-22 R13 did not appear) |
| 54 | PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (run_in_background) | exit 0 — `OK` → **opus: UP** |
| 55 | PROBE Grok / Gemini | by rows 4 / 5 | **grok: UP · gemini: UP** |
| 56 | COUNT | four UP (fail-closed floor is three) | would have launched Grok · Gemini · Sol · Opus 5.5 — **NOT launched: §1 stopped first (below)** |
| 57 | DATE + EXTENSION GATE (second row, before the launch) | — | not reached (no launch) |

## Packet
STOPPED under §1's `HONEST SIZE` rule before anything was staged. The originals the packet is made of were measured with `wc -c`; a byte-identical copy has the same size, so the ceiling is decided by the originals.

| packet item (`§1`) | source | bytes (`wc -c`) |
|---|---|---|
| (1) `build-diff.md` — `git log -p 47fafe5..45f647a -- . ":(exclude)docs"` | saved stdout (4,067 lines) | **174,464** |
| (2) `devdoc-diff.md` | saved stdout | **32,867** |
| (3) `classify-at-tip.md` — the seven `src/cobalt/classify/*.py` | `models` 8,508 · `config` 14,014 · `collector` 25,239 · `ledger` 4,433 · `trial` 8,055 · `cli` 6,449 · `__init__` 936 | **67,634** |
| (3) `wrapper-at-tip.md` | `ops/run_classify_trial.sh` | **954** |
| (3) `config-at-tip.md` | `configs/cobalt/classify/trial.yaml` | **20,356** |
| (3) `fixtures-at-tip.md` — the three files at the tip (`openrouter-model-entry.real-shape.json` 1,076 · `openrouter-systemone-response.openapi-example.json` 298 · `systemone-openapi-example.json` 2,111) | `tests/fixtures/classify/` | **3,485** |
| (6) `plan.md` | `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md` | **16,923** |
| **measured subtotal — six items of (1)–(3) plus the plan** | | **316,683** |
| not measured (only add to the total): (4) `contract.md` (`secrets.py` is 11,801 B whole, `mattermost.py` 6,740 B, `run_backup.sh` 1,467 B, plus the prompt's wrapper block, each taken by excerpt); (5) `build-report.md` (sections of a 55,226 B file, lines 100–399); (6) `rows.md`; (7) `QUESTIONS-JEV.md` and its file list; headers | | > 0 |

- **CEILING 230,000 B** → measured subtotal 316,683 B is **86,683 B over it**, before the unmeasured items. The two largest items alone — the build diff and the code at the tip — are 242,098 B, already above the ceiling; no item on §1's list can be shortened without dropping a staged item (L73), and §1 gives no shorter form.
- Per-checker token estimate at the measured subtotal: 316,683 ÷ 4 ≈ 79,000 tokens (the drafter's estimate was 120–180 KB ≈ 30–45k tokens).
- Diff completeness check on the saved build diff (measured, kept because it is cheap): `grep -c "^commit "` = **6** = the range's 8 commits minus its 2 docs-only report commits (`e18793a`, `6114519`); `grep -c "^diff --git"` = **30** = the non-docs file-touches of the `--stat` list (R5 5 · R4 10 · R3 4 · wip 2 · R2 3 · R1 6). No mismatch.
- The key scan AFTER staging: not run — nothing was staged. (The key scan BEFORE staging is PREFLIGHT rows 45–48, all clean.)
- Nothing was written under `scratch/tribunal-bars-0920/jev-trial-check/`: a partial folder would make a relaunch's RECOVERY rule treat a stale part as staged. No `mkdir`, no `s2-p2-cards` string and no Astra launch was run.
- The four probes (rows 53–55) wrote nothing but their own stdout; no checker CLI was launched, so the written-nothing proof (the `ls -la` pairs) has nothing to compare.

## CONTINUE
next: none. The run stops here with `FAILED: packet`. A relaunch of this same file first runs `ls scratch/tribunal-bars-0920/jev-trial-check` (fresh: "No such file") and hits the same ceiling unless the desk changes the prompt's ceiling or its packet list (L19, whole file).

## Secrets
Not reached — no house was launched. S-1 … S-9: no checker answers exist.

## Per step
Not reached. R1 … R6: no checker answers exist.

## Spend
Not reached — no checker answers exist.

## Plan conformity
Not reached — no checker answers exist.

## Assertions and boundary
No checker answers exist, so (a) (b) (c) per checker are not reached. The facts this hub could state without a packet:
- (i) `git log --stat --oneline 47fafe5..45f647a` names only: `src/cobalt/classify/{__init__,models,config,collector,ledger,trial,cli}.py`; `src/cobalt/cli.py` (commit `5630e6c`, two lines); `configs/cobalt/classify/trial.yaml`; `ops/run_classify_trial.sh`; `tests/cobalt/test_classify_{config,models,keys,discover,door,trial}.py`; `tests/fixtures/classify/{openrouter-model-entry.real-shape.json,openrouter-systemone-response.openapi-example.json,systemone-openapi-example.json}`; `docs/40 - DevDocs/cobalt/classify/{__init__,cli,collector,config,ledger,models,trial}.md`; `docs/40 - DevDocs/cobalt/cli.md`; `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md`; the build report. Every path is one of PREFLIGHT's allowed boundary paths; no other path.
- (ii)–(viii) of §3 (protected paths, the one-vault-reader and no-other-network greps, the wrapper counts, test-diff assertions, RESTARTS) were NOT run: they are collate checks that follow the checkers' answers, and no answers exist.
- (vii) L32: no ticker written in this report. L41: no key material written in this report (it names `OPENROUTER_API_KEY` and `COBALT_MASTER_KEY` only as names; PREFLIGHT row 47 names the build report's own placeholder pattern).
- (viii) RESTARTS (L42), the build report's own `RESTARTS:` line, quoted: `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. NOT CHECKABLE FROM READS — `uv run cobalt jobs restarts 47fafe5..45f647a`.

## Checked against the branch
Not reached — no checker made a claim.

## Ready for the probe
| checker | CHECK JEV line | ready | reason |
|---|---|---|---|
| grok | not launched | — | packet over the ceiling |
| gemini | not launched | — | packet over the ceiling |
| sol | not launched (probe UP) | — | packet over the ceiling |
| opus | not launched (probe UP) | — | packet over the ceiling |

Gate by §4's rule, as its three counts: houses answering with a `CHECK JEV:` line = **0** (need ≥ 3) · `secrets LEAK that HOLD` = **0** · `defects that HOLD` = **0** → `probe gate: NOT READY` (the houses count fails; a gate of READY needs all three).

## FOR THE CLASSIFIER
none — no checker claim exists to file-check (L75: a classifier receives only claims that HOLD).

## ESCALATE
1. **FAILED: packet.** The measured originals of §1's packet are 316,683 B against the 230,000 B ceiling — ≥ 86,683 B over, before the unmeasured items (`Packet` above). The rule says launch nothing; nothing was launched.
2. **ASK DESK:** the packet cannot be staged under the prompt's 230,000 B ceiling: the build diff (174,464 B) and the code at the tip (67,634 B) alone are 242,098 B. Does the desk want a new ceiling, or a re-issued `29` (L19, whole file) with a different packet list? No retry by this hub. [12:28 ET, 2026-09-23]
3. **Fact, recorded not judged:** `tests/fixtures/classify/` at the tip holds three files — `openrouter-model-entry.real-shape.json`, `openrouter-systemone-response.openapi-example.json`, `systemone-openapi-example.json`. `28` R4 and `QUESTIONS-JEV.md` (S-7) name a fourth, `openrouter-chat-response.published-schema.json`; it is not in the folder (the build report's door is `systemone`, from the desk's R47 correction). A re-issued `29` would need its S-7 and R4 wording checked against this list.
4. **Fact, recorded:** the Sol probe answered `OK` (exit 0) — Sol is not on METER today, contrary to the 09-22 R13 expectation the prompt carries. On a relaunch four houses are available, not three.
5. **Standing line (as the prompt words it):** "This check covers the JEV trial build only, `47fafe5..45f647a` of `jev/trial-0923`. It is round 1 of ≤3 (L67 / L39). With three houses checked, `secrets LEAK that HOLD: 0` and `defects that HOLD: 0`, the build is READY for the ONE keyed probe `31` (N2, his R42 condition), then the local-lane build and the trial-run hub under his approved cap; a HOLD goes to a classifier and a fix round (L75), and `31` does not launch." — On this report ZERO houses checked, so the build is NOT READY for `31`; round 1 is NOT spent (L67 P-c: a run that produced no ruling does not spend a round).
6. **Standing line (as the prompt words it):** "Nothing in this check measures the product. The build made no keyed call: its public listing read answered U1, U2 and U5 (`build-report.md` `## DISCOVERY`); U3, U4 and U6 are answered only by the probe `31`, after this check; the trial's bars (plan §4) are measured only by the trial run."

FAILED: packet — 316,683 B measured (build diff + devdoc diff + code at tip + wrapper + config + fixtures + plan, before contract / build report / rows / questions) is ≥ 86,683 B over the 230,000 B ceiling — nothing staged, no house launched, probe gate NOT READY
