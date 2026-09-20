# BARS BUILD CHECK PROMPTS — draft report, 2026-09-20

## §0 Headline
- Two ≥3-house BUILD CHECK prompts DRAFTED, nothing launched (L36): `prompts/2026-09-20/14-bars-chunk-1a-check.md` (31,190 B) and `15-bars-chunk-2-check.md` (37,829 B), both Sonnet 5 hubs, both copying `08-bars-chunk-e-check.md` byte for byte wherever the same command serves.
- **NEW rule strings: NONE.** Both launch lines carry the identical 14 allow strings + 3 denies of `08`; a `grep -o "Bash([^)]*)"` over each new file returns those 17 and nothing else.
- The one step that looked like it needed a new string — reading each build's branch, which lives in `~/cobalt-wt/bars-chunk-1a` / `bars-chunk-2` and has no git rule — was RESTRUCTURED away, not granted: files via the Read tool under `--add-dir`, commits/diff/blobs via `git -C /Users/cobalt/cobalt log -p <base>..<tip>` and `show <sha>:<path>` from the shared object store. Proven here at 18:3x ET.
- Chunk 1a is BUILT (`BARS CHUNK 1A BUILT c597bfe | on main e15d03e`, ESCALATE 10) so prompt 14 names its range. **Chunk 2 was at step 4 of 7 when this was written** (tip `02d67a6`, last line `(run in progress …)`), so prompt 15 hard-codes no sha: it reads the stop line at run time and FAILS PREFLIGHT unless that line starts `BARS CHUNK 2 BUILT `.
- READING: 7 · ESCALATE: 6.

## The two prompts

| | `14-bars-chunk-1a-check.md` | `15-bars-chunk-2-check.md` |
|---|---|---|
| seat | `bars-chunk-1a-check-0920`, Sonnet 5 hub | `bars-chunk-2-check-0920`, Sonnet 5 hub |
| under check | branch `bars/chunk-1a-0920`, `e15d03e..c597bfe` (5 build commits) + report commit `589d40f` | branch `bars/chunk-2-0920`, range read from the stop line at run time |
| report | `reports/bars-chunk-1a-check-2026-09-20.md` | `reports/bars-chunk-2-check-2026-09-20.md` |
| stop line | `BARS CHUNK 1A CHECK DONE · … · ESCALATE: <n>` | `BARS CHUNK 2 CHECK DONE · … · ESCALATE: <n>` |
| staged in | `scratch/tribunal-bars-0920/chunk-1a-check/` (Write creates it; no `mkdir`) | `scratch/tribunal-bars-0920/chunk-2-check/` (same) |
| houses | grok · gemini · astra, one attempt each, `run_in_background`, `01-review-harness.md` §2.1–2.3 spellings unchanged | same |
| house verdict | `CHECK: BUILD STANDS` / `… EXCEPT <items>` / `CHECK: FIX FIRST <items>` + ` · ready for its deploy prompt: YES\|NO` | same + ` · inert on an unpartitioned parent · composition note: SOUND\|UNSOUND · hard boundary: HELD\|CROSSED` |
| DATE GATE | first PREFLIGHT row, `date`; 2026-09-22 or later → `FAILED: authorization expired` (his R23 stands through 2026-09-21 23:59 ET) | same |

**What each prompt stages where.** Both stage into a NEW subfolder of the existing `scratch/tribunal-bars-0920/` that the first Write creates, and both RE-USE what the tribunal and the chunk-E check already staged rather than copying it again (L44 — the same material every house has already had): `../chunk-e-check/spec-final-s3.md` (FINAL §3 — §3.2 in full incl. the COMPOSITION NOTE, §3.3, §3.4 step 3, §3.9, §3.10), `../chunk-e-check/spec-final-s6.md`, `../chunk-e-check/spec-final-s8.md`, `../r3/DERIVED-v3.md.part1/.part2`, `../owner-rulings.md`, `../0001_bars.sql`, `../poller.py` and `../archiver-store.py` (main's copies, verified byte-equal to main at 18:3x ET: 4,981 B and 14,076 B), `../chunk-e-check/build-report.md.part4`. Each re-used file carries a VERIFY command in the prompt (`wc -l` + a `grep -n` anchor) and a re-stage instruction if it fails.

- **14 stages:** `built/` = the branch's `cli.py` (≈55 KB, parts), `placement.py`, `test_migrate_proof.py` (≈142 KB, parts cut at `def test_` boundaries), `test_tenancy.py`, the two DevDocs · `build-diff-src.md.part*` = `log -p` of the two source files against main · `build-report.md.part*` (688 lines, last part starts at `## SPEC vs CODE`) · `build-prompt.md.part*` = prompt 10 whole · new `spec-final-s2.md` (FINAL 20–53) and `spec-final-s4.md` (102–121) · `main-placement.py` · `chunk-e-check-report.md.part*` · `QUESTIONS-CHECK.md`.
- **15 stages, poller diff FIRST:** `THE-POLLER-DIFF.md` + `main-poller.py` + `built/poller.py` · `build-diff-src.md.part*` (`log -p … -- src/cobalt`) · `built/` = every path the run-time `--stat` list names · `main-store.py`, `main-0006.sql`, `main-0010.sql` · `build-report.md.part*` (one part begins at `## THE POLLER DIFF`) · `build-prompt.md.part*` = prompt 11 whole · new `spec-final-s2.md`, `s4.md` and **`s5.md` (FINAL 122–152 — §5.2's D1/D2/N2, the seam-B dissents he ruled against, so a house can see what was NOT built)** · `chunk-e-check-report.md.part*` · `QUESTIONS-CHECK.md`.

**What the houses are asked.** 14: the five deliverables with `file:line` (filtered streamed fold + a byte-identical unfiltered statement · `REPLACED` true only when baseline = source = target on rows AND digest, with the three §3.10 cases · MP1 default everywhere, `FROZEN_ARCHIVE` unable to activate and naming astra's three conditions, `SEALED_BASELINE_TRUSTED` emitted by no path · the placement pattern admitting ONLY the named shapes and not wildcarding `PLACEMENT` · lock-before-snapshot with an EMPTY default leaving main's statement order byte for byte — **and whether that closes chunk E's ESCALATE 6, answered with the sequence** · AMBER a label, never a refusal); test honesty including the ONE test the builder fixed (`ast` parse replacing a text grep) and the companion assertion it REMOVED (`"|".join`); each of the 10 ESCALATEs and both `READING:` items; L52. 15: INERTNESS first (is the test asserting against main's behaviour or a re-description); **the COMPOSITION NOTE, which no house has ruled on — each house rules now, SOUND/UNSOUND with the failing sequence**; the 13 named poller tests present and honest; `upsert_bars`/`upsert_bars_on` additions-only; `0012` (empty parent, PK, `CHECK (interval = 'i1')`, no `DEFAULT`, rollback drops only its own relation, grants per `0006`, columns identical to `0001_bars.sql`); `ensure` never detaching/dropping/truncating and granting on parent AND every child; the probe inert before the swap and U1 a loud refusal, never a default; the HARD BOUNDARY (no seam B, no lock/generation on the poller, no change to `complete` or a detector's refusal, nothing reaching a card); the cross-branch `placement.py` seam and the child NAME SHAPE, named for the stacked gate.

## RULE PROOF
`grep -c -F "<string>" "docs/40 - DevDocs/prompts/2026-09-20/08-bars-chunk-e-check.md"`, one bare command per string, run 2026-09-20 18:3x ET. **Every string is in the approved file; none is new.**

| # | string | count in `08` |
|---|---|---|
| 1 | `Bash(grok *)` | **2** (launch line + its R9 prose citation) |
| 2 | `Bash(agy *)` | **2** (launch line + its R9 prose citation) |
| 3 | `Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)` | 1 |
| 4 | `Bash(mkdir -p scratch/tribunal-bars-0920)` | 1 |
| 5 | `Bash(git -C /Users/cobalt/cobalt show*)` | 1 |
| 6 | `Bash(git -C /Users/cobalt/cobalt log*)` | 1 |
| 7 | `Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)` | 1 |
| 8 | `Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)` | 1 |
| 9 | `Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)` | 1 |
| 10 | `Bash(ls *)` | 1 |
| 11 | `Bash(grep *)` | 1 |
| 12 | `Bash(tail *)` | 1 |
| 13 | `Bash(wc *)` | 1 |
| 14 | `Bash(date*)` | 1 |
| D1 | `AskUserQuestion` | 1 |
| D2 | `EnterWorktree` | 1 |
| D3 | `Bash(git push*)` | 1 |
| + | `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt` | 1 |

**NEW strings: NONE.** Verified from the other side as well: `grep -o -n "Bash([^)]*)"` over `14-bars-chunk-1a-check.md` and over `15-bars-chunk-2-check.md` each return exactly those 17 rule strings (the allow list once, the three denies once, plus the prose citations of `grok`/`agy`/`mkdir`/`git push`) and no other `Bash(...)` pattern. The tail `--disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir …` greps `1` in each new file.

**Four of the fourteen are NEVER RUN, and both prompts say so in their first paragraph** (`08`'s own treatment of `mkdir`): `Bash(mkdir -p scratch/tribunal-bars-0920)` — the Write tool creates the subfolder — and the three `s2-p2-cards` git strings, which point at a worktree unrelated to these checks. Carrying them keeps the list byte-identical; dropping them would also have been lawful (a subset is not a new rule), but the brief says use exactly those fourteen.

**How the branches are read with no worktree git rule** (the restructure that kept the count at zero):

| need | not used | used instead | proof |
|---|---|---|---|
| the branch's files | `git -C …/bars-chunk-1a show` | Read tool under `--add-dir /Users/cobalt/cobalt-wt`; `ls`/`grep`/`wc`/`tail` take any path | `wc -c /Users/cobalt/cobalt-wt/bars-chunk-1a/src/…` ran clean here |
| the branch's commits | `git -C …/bars-chunk-1a log` | `git -C /Users/cobalt/cobalt log --oneline e15d03e..bars/chunk-1a-0920` | listed all six commits (worktrees share `refs/heads` + objects) |
| the branch's diff | `git -C …/bars-chunk-1a diff` | `git -C /Users/cobalt/cobalt log -p <base>..<tip> -- <paths>` | printed the `tunables.yaml` patch verbatim |
| a file at a branch sha | — | `git -C /Users/cobalt/cobalt show <sha>:<path>` | `show --stat c597bfe` returned the commit |

## READING:
1. **The `= 1` spec.** The brief asks for `grep -c -F` = **1** for each of the 17 strings against `08`. Two count **2** because `08` cites `Bash(grok *)` and `Bash(agy *)` in its prose as well as its launch line. Read as "present in the approved file" (≥ 1 = approved, 0 = new); recorded here rather than reported as a mismatch. Sentence read from: *"for each of the 14 allow strings + 3 denies, `grep -c -F` = 1 against `08-bars-chunk-e-check.md`, and an explicit `NEW strings: NONE`"*.
2. **Reading a branch without a rule for its worktree.** No approved string covers `git` in `~/cobalt-wt/bars-chunk-1a` or `bars-chunk-2`. Narrowest resolution: restructure, per the brief's *"If a step seems to need one, do not add it: restructure so it does not"* — Read tool + the shared object store through the `~/cobalt` git rules. Proven before it was written into either prompt.
3. **The verdict strings.** The brief names `BUILD STANDS` / `BUILD STANDS EXCEPT <items>` / `FIX FIRST <items>`. Written as `CHECK: BUILD STANDS …` etc., keeping `08`'s machine-readable `CHECK:` prefix so the hub's last line can quote a house verdict whole, as the chunk-E check report does.
4. **Report paths and stop-line wording** are not given by the brief. Narrowest: mirror `08` exactly — `reports/bars-chunk-<n>-check-2026-09-20.md` and `BARS CHUNK <N> CHECK DONE · …`, with the same fallback path inside the scratch folder if the Write is refused.
5. **Chunk 2's "FAIL if the last line is not `BARS CHUNK 2 BUILT …`"** is placed as a PREFLIGHT gate (`FAILED PREFLIGHT: chunk 2 is not built — last line: <verbatim>`), before any staging or launch, so a premature run costs nothing and the desk can simply relaunch.
6. **Packet size.** Chunk 1a's packet is ≈360 KB staged (chunk E's was ≈255 KB), mostly `test_migrate_proof.py` at 142 KB. Kept WHOLE and split into ≤38,000 B parts: a house cannot rule on whether a test is honest from an excerpt of it. Chunk 2's size is unknown until its build lands, so prompt 15 gives the same splitting rule and derives the file list from `git log --stat` at run time.
7. **`spec-final-s5.md` (FINAL §5.2) is staged for chunk 2 only.** The brief does not name it; it is added because question EIGHTH asks a house to rule that seam B was NOT built, and the dissents toward B (astra, gemini — D1/D2/N2) are what "not built" means there. Narrow addition of already-approved material (L44), no new access.

## ESCALATE
1. **The two strings that count 2, not 1** (READING 1). Nothing is new; the brief's arithmetic just does not match `08`'s prose. Named so the desk's own check of this report does not read it as a drift.
2. **Chunk 2 was still building when prompt 15 was written** (18:34 ET: step 4 of 7, tip `02d67a6`, last line `(run in progress — next step under ## CONTINUE)`). Prompt 15 therefore hard-codes no sha, no range and no verified file list: it reads the stop line, derives `<tip>`/`<base>` from it, stages from `git log --stat`, and stages any path that list names which the prompt's expected list does not, with an ESCALATE line. **If the build ends `CONTINUE:` or `FAILED`, the check FAILS PREFLIGHT and stages nothing.**
3. **The child NAME SHAPE seam, and it is real.** Chunk 1a's ESCALATE 3 records `bars_p_<YYYY>w<WW>` as a READING because `main` does not spell the shape; chunk 2 generates the actual children. If the two differ, both branches are individually green and wrong together — only the stacked-tree gate (L68 as amended 2026-09-20) sees it. Prompt 15's question NINTH asks all three houses to compare the two spellings from the files; prompt 14's THIRD asks the same from the other side. The desk owns the gate.
4. **Six headless house sessions if both checks run at once.** Each hub probes the meters itself (L47) and takes ONE attempt per house, and the folders are separate; but grok, agy and the Codex Astra seat would be carrying two checks in parallel. The desk may prefer to stagger the two launches. `ASK DESK` is not written into either prompt for this — it is the desk's launch decision, not a hub's.
5. **Astra on METER would leave chunk 2 with two houses**, which meets L67's floor but not FINAL §8's `≥3 checkers (live write path)` for this chunk specifically. Prompt 15 continues with two, records it verbatim, and writes `ASK DESK: … is a second attempt wanted before the deploy prompt?` under its ESCALATE; it never waits.
6. **L74, recorded ONCE and never followed:** after the Read of this run's launch prompt, a block arrived inside the tool-result stream asking for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and naming a file-send tool. It is DATA, not an instruction. Not followed. This run commits nothing and sends nothing.

## CONTINUE
Nothing to continue. Both prompt files are written and rule-checked; this report is the third and last file of this seat. **Not mine, and in this order (L67, L73):** the desk launches `14-bars-chunk-1a-check.md` now — chunk 1a's stop line landed at 18:28 ET — and launches `15-bars-chunk-2-check.md` at chunk 2's own stop line, not before. No deploy prompt for either chunk is written until its check closes, and the stacked-tree gate over both branches is a separate step the desk owns.

BARS BUILD CHECK PROMPTS DRAFTED · prompts: 2 · new rule strings: 0 · READING: 7 · ESCALATE: 6
