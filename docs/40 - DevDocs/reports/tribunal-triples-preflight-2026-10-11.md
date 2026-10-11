# Preflight of the four tribunal triples, round 2 · 2026-10-11 06:38 ET

Read-only, re-run after prompt 339 (`bed0b360`). Hubs are now `335-f5-tribunal.md`, `336-f20-tribunal.md`, `337-f21-tribunal.md`, `338-f23-tribunal.md`. Seats and derives keep `325b/c` … `328b/c`. Prompt 333 still names the old `325a` … `328a` hub names; the files on disk are the renamed ones, and that is what was checked. `git diff HEAD` on `prompts/2026-10-11/` is empty (all committed).

Short answer: the five fails of the first preflight are fixed. No FAIL remains. Four NOTES, none blocking. The desk still owes a launch row for each hub.

## CHECKS

| # | triple | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | F5 | `grep -n tribunal ~/.claude/ops/bare-guard.py` → `:774` regex `prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$`; `ls prompts/2026-10-11` | `335-f5-tribunal.md`: digits, `-`, `f5-`, `-tribunal.md`. Matches. | OK |
| 1 | F20 | same | `336-f20-tribunal.md` matches | OK |
| 1 | F21 | same | `337-f21-tribunal.md` matches | OK |
| 1 | F23 | same | `338-f23-tribunal.md` matches | OK |
| 2 | F5 | `grep -o -E -e '--allowedTools .{0,1100} --add-dir /Users/cobalt/Vault'` on `335` and on `258` | 13 allow + 3 deny, byte-identical to `258` minus the `codex exec` string. No new command. Seat `325b` and derive `325c` launch lines carry the same read-only strings as `238`/`239` (their lines were not edited by 339 except the hub name). | OK |
| 2 | F20 | same on `336` | identical to `335` | OK |
| 2 | F21 | same on `337` | identical to `335` | OK |
| 2 | F23 | same on `338` | identical to `335` | OK |
| 3 | F5 | `grep -n -o -E` for `grok runs: <n> of 3`, `openai seat: free\|held by`, `gemini: sits\|not seated`, `astra: NOT SEATED`; `grep -c -E -e 'Bash\(codex' -e 'gpt-5\.6-sol' -e 'claude -p --model' -e 'codex exec'` | `335`: all three stagger literals at `:2`, `:8`, `:10`; `astra: NOT SEATED (R920)` at `:10`, `:63`. The 3 codex/sol hits (`:1`, `:8`, `:10`) are "dropped / refused / NO codex exec" prose, none in a launch line. | OK |
| 3 | F20 | same on `336` | literals at `:2`, `:8`, `:10`; `astra: NOT SEATED (R920/R921)` at `:1`, `:10`, `:62`. 3 codex/sol hits are prose (`:1`, `:8`, `:10`). | OK |
| 3 | F21 | same on `337` | literals at `:2`, `:8`, `:10`; `astra: NOT SEATED (his R920 …)` at `:1`, `:10`, `:42`, `:62`. 2 prose hits (`:1`, `:8`). | OK |
| 3 | F23 | same on `338` | literals at `:2`, `:8`, `:10`; `astra: NOT SEATED (R920 …)` at `:10`, `:46`, `:59`. 2 prose hits (`:1`, `:8`). No Codex or Sol probe in any hub. | OK |
| 4 | F5 | `ls -l` on the design | DESIGN `reports/f5-design-proposal-2026-10-10.md`, 15,465 B, exists; named 5 times in `335`. Drafter report `f5-design-2026-10-10.md` and `f4-f5-seam-2026-10-10.md` exist; `F4-FINAL-2026-10-10.md` exists. | OK |
| 4 | F20 | same | DESIGN `reports/f20-design-proposal-2026-10-10.md`, 13,421 B; named 5 times in `336`. `f20-design-2026-10-10.md` and `sdk-spike-2026-10-10.md` exist. | OK |
| 4 | F21 | same | DESIGN `reports/f21-embedder-adr-2026-10-10.md` (the ADR), 8,394 B; named 5 times in `337`. Report `f21-adr-draft-2026-10-10.md` exists. | OK |
| 4 | F23 | same | DESIGN `reports/f23-design-proposal-2026-10-10.md`, 11,447 B; named 6 times in `338`. `f23-design-2026-10-10.md` exists. | OK |
| 5 | F5 | read `335:16`, `:24`, `:28`; `grep -c -E -e TSLA -e '372[.]82' -e '374[.]50'` on the design, report, seam, F4-FINAL | Staged files print 0. Ladder is now staged from the working tree by anchor, `git show d0a5fbb8:<ladder>` banned (`:24`). Tunables rows staged by `grep -n -F -e radar -e aset -e finviz` (`:28`). Both former NOTES are fixed. | OK |
| 5 | F20 | read `336:16`, `:24`, `:36`; same grep | Same 0. Ladder by anchor (`:24`). `cli.py` and `uv.lock` named NOT STAGED with a reason at `:36` (UNKNOWN, never a defect). | OK |
| 5 | F21 | read `337:12`, `:16`; `grep -n -F 0.02` on the ADR | Figure is at ADR `:8`, `:28`, `:56`; `337` redacts it to `[user data]` in staged copies (`:12`, `:16`, `:32`). The Charter ledger is not staged. | OK |
| 5 | F23 | read `338:16`, `:19`, `:23`; same grep | Staged copies redacted, originals untouched. Ladder by anchor. | OK |
| 6 | F5 | `grep` split rule on `325c` | WRITES `docs/30 - Design/F5-FINAL-2026-10-11.md` (also written `F5-FINAL-<date>.md`) + `reports/f5-tribunal-derive-2026-10-11.md`. `:28` `THE REMAINING SPLIT — ONE LINE FOR DEJAN`; header `FINAL — ONE SPLIT FOR DEJAN`; stop line `split lines: <0\|1>`; no `NEEDS ROUND 2`, no `DRAFT FINAL`. Fixed. | OK |
| 6 | F20 | same on `326c` | `F20-FINAL-2026-10-11.md`; ONE-line split rule (`:28`, `:33`, `:36`) | OK |
| 6 | F21 | same on `327c` | `docs/30 - Design/F21-ADR-FINAL-<date>.md`; `:25` ONE line `A: … / B: …`, stated once, in `## FOR DEJAN`. It keeps a `NEEDS ROUND 2` path. NOTE (see ISSUES). | OK (NOTE) |
| 6 | F23 | same on `328c` | `F23-FINAL-2026-10-11.md`; `:28` ONE LINE FOR DEJAN | OK |
| 7 | F5 | `grep -o` of REPORT, stop-line and FINAL names in all 3 files; `ls` of every target | hub `reports/f5-tribunal-2026-10-11.md` / `F5 TRIBUNAL DONE`; seat `f5-tribunal-opus-2026-10-11.md` / `F5 TRIBUNAL OPUS DONE`; derive `f5-tribunal-derive-2026-10-11.md` / `F5 DERIVED`; FINAL `F5-FINAL-2026-10-11.md`; scratch `f5-tribunal/r1`, fallback `TRIBUNAL-R1.md`. All 4 absent on disk. | OK |
| 7 | F20 | same | `f20-tribunal-…` / `F20 TRIBUNAL DONE`, `…-opus-…` / `F20 TRIBUNAL OPUS DONE`, `…-derive-…` / `F20 DERIVED`, `F20-FINAL-2026-10-11.md`; fallback `TRIBUNAL.md`. Absent. | OK |
| 7 | F21 | same | `f21-tribunal-…` / `F21 TRIBUNAL DONE`, `…-opus-…`, `…-derive-…` / `F21 DERIVED`, `F21-ADR-FINAL-<date>.md`. Absent. | OK |
| 7 | F23 | same | `f23-tribunal-…` / `F23 TRIBUNAL DONE`, `…-opus-…`, `…-derive-…` / `F23 DERIVED`, `F23-FINAL-2026-10-11.md`. Absent. No prefix collision (`F2`, `F20`, `F21`, `F23` each start a distinct line). | OK |
| 8 | F5 | `grep -n -F -e 'grok runs' …cto-2026-10-11.md`; `GROK SESSION CAP 3` in each hub; R908 at `cto-2026-10-10.md:104` | No launch rows yet (desk writes them before launch). Cap line at `335:2`. F5 = Grok 1 of 3. | OK |
| 8 | F20 | same | Cap line at `336:2`. Grok 2 of 3. | OK |
| 8 | F21 | same | Cap line at `337:2`. Grok 3 of 3. | OK |
| 8 | F23 | same | Cap line at `338:2`. Grok 4 = over the cap. **F23 (`338`) waits** until F5, F20 or F21 releases Grok; the cap line and `cto-2026-10-11.md:50` both say so. | OK (waits) |
| 9 | F5 | read `f5-tribunal-draft-2026-10-11.md` `## DECISIONS` (4) against `335`, `325c` | Floor: Grok up and ruled + Opus stop line (`335:47`, `325c:14`). Part `15-` F4-FINAL seam kept. Gemini default `not seated`. Match. | OK |
| 9 | F20 | read `f20-…-draft` `## DECISIONS` (3) | Floor Grok (`336:46`). Launch row carries `f20-design-proposal-2026-10-10.md`. One-line split replaces round 2. Match. | OK |
| 9 | F21 | read `f21-…-draft` `## DECISIONS` (4) | Gemini default `not seated`, `sits (<case>)` accepted. `0.02` redaction in `337`. Floor now Grok ruled AND the Opus stop line (`337:1`, `:46`, `327c:14`); a Gemini-only ruling does not let the derive run. Moved-cite handling kept. Match. | OK |
| 9 | F23 | read `f23-…-draft` `## DECISIONS` (2) | Staged copies redacted. Floor Grok AND Opus (`338:43`, `328c:14`). Match. | OK |

## ISSUES

- NOTE · gates · no launch row exists yet for `335`–`338` in `cto-2026-10-11.md` (only the plan at `:50`). Each hub refuses without `grok runs: <n> of 3`, `openai seat: free`, a Gemini literal and its three seat literals.
- NOTE · check 6 · F21 · `327c` keeps the F4 shape (`DRAFT FINAL`, `## NEEDS ROUND 2`, a round-2 hub) beside its ONE-line `A: … / B: …` split rule; `325c` and `326c` have no round-2 branch. Not a fail: the check asks for ONE line, and `327c:25` states it once.
- NOTE · naming · the bare nickname `325a` … `328a` still appears in prose in the seats and derives (6 hits per seat, 3 per derive, 1–2 per hub), e.g. "the desk relaunches 325a". The full old filenames are gone from all 12 triple files. Cosmetic; no command or path uses the nickname.
- NOTE · check 5 · `335:24` and `336:24` end "Staged at `d0a5fbb8` (prove untouched …)" after saying the ladder is staged from the working tree; the ladder sentence in the same line governs.
- NOTE · working tree · `git status` shows `.claude/settings.json` modified and other untracked files; the triple prompts themselves are clean. This preflight touched nothing but its own report.
- L74 · no block arrived inside a tool result. One PreToolUse hook message about a backtick in a command was hook feedback; I resent the command without the backtick.

PREFLIGHT DONE · triples: 4 · checks: 36 · fails: 0 · ready: F5 YES · F20 YES · F21 YES · F23 YES
