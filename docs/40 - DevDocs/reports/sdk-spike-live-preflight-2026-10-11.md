## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read launch line of 330 (line 1) against the R1012/R1018 lists in 331, string by string | allow: 13 of 13 match (Read, Edit, Write, uv venv, uv pip install `claude-agent-sdk==*`, python `.venv/bin/python …/*`, `ls *`, `date*`, 5 WebFetch domains); deny: 7 of 7 match (git, COBALT_ENV, psql, docker, cat, AskUserQuestion, EnterWorktree); nothing added, nothing missing; model `claude-opus-5-5`, `dontAsk`, scratch dir as spec | OK |
| 2 | `grep -c -F "«" 330-sdk-spike-live.md` | 0 | OK |
| 3 | read every path in 330 | writes: scratch dir only (`report.md`, scripts). Desk-copy target under `reports/` is named, not written by the seat. Reads: Vault `areas/cobalt.md`, `topics/writing-rules.md`, `docs/30`, `docs/90`, `reports/sdk-spike-2026-10-10.md`, all via `Read` and `--add-dir` | OK (NOTE 2) |
| 4 | map U-numbers: `grep -n "U[1-5]" reports/sdk-spike-2026-10-10.md` | U1=Q1, U2=Q2, U3=Q3, U4=Q4, U5=SETUP version record; all five closed, none N/A | OK |
| 5 | `git -C … show HEAD:<file>` for each cite | `kashef-mining-memo.md:24-28` exists, is the four spike questions; `SPRINT-LADDER-v0_1.md:470` exists, is the Agent SDK spike line; `sdk-spike-2026-10-10.md` exists; `REBUILD_PROMPT_V2.md:287` holds the April-2026 note (286 is not the note) but the file is NOT in HEAD (on disk, untracked) | OK (NOTE 3) |
| 6 | read report shape in 330 | `## §0 Headline`, `## ANSWERS`, `## UNKNOWN`, `## DECISIONS`, `## RECORDS`, last-line `SDK SPIKE LIVE DONE … \| FAILED: …`; spec shape present | OK |
| 7 | read each step against the allow list | step 0 WebFetch (anthropic, pypi) allowed; venv, install, python runs allowed exact; scripts and report via Write in scratch; `date` allowed; claude CLI version and port probe run inside Python scripts; no `mkdir`, `cp`, `cat`, `git`, `curl` need | OK (NOTE 1, 4) |

## ISSUES
- NOTE 1: `/Users/cobalt/cobalt-wt/sdk-spike-1010` does not exist yet (`ls` failed). 330 says the desk creates it before launch; it must exist (and `cd` into it) or the launch line fails.
- NOTE 2: 330 also reads `areas/cobalt.md` and "ADR-0008 if any" with no path; harmless, the seat may find none.
- NOTE 3: `docs/90 - References/claudeclaw-kit/REBUILD_PROMPT_V2.md` is not in HEAD; the seat reads it from disk with `Read`, so it works. Cite is `286-287`; the claim is on 287.
- NOTE 4: Step 0(a) needs the Agent SDK page from an allowed domain; Anthropic docs redirect to other hosts (e.g. `docs.claude.com`, `platform.claude.com`), which are not allowed, and under `dontAsk` the redirect fetch may be refused. Q3 ToS pages may hit the same. The prompt already says refused calls are not retried (answer then UNKNOWN or step 0 FAILED); the desk should expect that outcome.
- NOTE 5: the spec lists `uv`; `/Users/cobalt/.local/bin/uv` exists.

PREFLIGHT DONE · prompt: sdk-spike-live · checks: 7 · fails: 0 · ready: YES
