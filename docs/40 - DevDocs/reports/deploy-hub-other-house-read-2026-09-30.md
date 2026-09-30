# DEPLOY-HUB.md — other-house read (Grok), 2026-09-30

Reader: Grok (`grok --sandbox cobalt-job -p`), a house other than the author (Opus drafter). Read-only. Files: `plans/fixed-files-2026-09-30/DEPLOY-HUB.md` (commit `4be06af0`), `STANDING-LIST.md` §3, `prompts/2026-09-30/51-deploy-3-e1-0930.md`. Output verbatim below; the desk ran none of its greps yet (K24: a finding counts only with a failing test or command the checker ran; none of these carries one).

---

The resume path stalls, a failed revert can leave residents down or bring them back on the unrestored tree, and several allow-list strings can write past the steps.

1. **Line 63** (against line 55). Quoted: `git -C /Users/cobalt/cobalt log --oneline main..<BRANCH>` → EMPTY. Line 55 says a `CONTINUE: STEP-D0` resume re-runs STEP-0 and does not re-run STEP-T, and check (c) allows HEAD to be a merge above `<m1>`. That merge is a commit `main..<BRANCH>` lists, so P5 fails and the only resume stops.  
   `grep -n "log --oneline main..<BRANCH>" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/DEPLOY-HUB.md"`

2. **Line 162** (against line 23). Quoted: `else residents stay DOWN, FAILED: STEP-5 (2)`. Rule F says every ending after the first bootout passes through 4.6 or STEP-5 (3) so residents are up before the stop. A revert that does not restore `<pre-merge>` leaves aset and radar down.  
   `grep -n "residents stay DOWN" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/DEPLOY-HUB.md"`

3. **Line 55** (against prompt 51 line 43). Quoted: `(e) false = an earlier attempt left residents down: run STEP-5 (3) NOW, whatever (a)–(d) say`. Prompt 51, on any failed resume check, ends `FAILED: resume` and `nothing touched`. It does not bootstrap. This file starts residents before it knows whether the revert restored the tree, including after finding 2 left them down on purpose. Line 15 makes that STEP-D0 session the continuation of a FAILED deploy.  
   `grep -n "nothing touched" "docs/40 - DevDocs/prompts/2026-09-30/51-deploy-3-e1-0930.md"`

4. **Line 8** (against lines 62, 55, and 35). Quoted: `a STEP-D0 resume is launched with the gate's OWN <GATE>/.env left`. P4 then requires `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`, or the run fails. The resume says do not re-run STEP-G. Asymmetry (a) says a stop while `.env` is present means G (f) first. One reading leaves the `cobalt_dev` lock held.  
   `grep -n "\.env" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/desk-launch.sh"` (the script's `lock_free` skips the job's own `.env` on a resume step)

5. **Line 11.** Quoted: `Bash(git -C /Users/cobalt/cobalt add *)` and `Bash(git -C /Users/cobalt/cobalt commit *)`. STANDING-LIST §3 says `add *` never touches `src/`, `configs/`, or `ops/`, and commits only the report. The same `*` matches `git -C /Users/cobalt/cobalt add src/cobalt/prefill/trade_note.py` and `git -C /Users/cobalt/cobalt add -f .env` (`.gitignore` line 1 is `.env`), then `commit` without a pathspec. That lands code or the secret file on `main`. The steps only add the report path (line 130).  
   `grep -n "Bash(git -C /Users/cobalt/cobalt add" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/STANDING-LIST.md"`

6. **Line 11** (against line 162). Quoted: `Bash(git -C /Users/cobalt/cobalt revert --no-edit *)`. The step allows only `revert --no-edit -m 2 <stack-final>`. D2.2 says `<stack-final>^1` is `<m1>` (the new tree) and `^2` is `<pre-merge>`. The same string matches `git -C /Users/cobalt/cobalt revert --no-edit -m 1 <stack-final>`, which keeps the new tree. Line 78 calls this an exact string with no wildcard while the string contains `*`.  
   `grep -n "revert --no-edit" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/DEPLOY-HUB.md"`

7. **Line 11** (against lines 117, 118, 136, and 174). Quoted: `Bash(git -C /Users/cobalt/cobalt tag *)`. The steps only create or delete `scratch-allow-probe-<JOB>`, `pre-<JOB>`, and `<TAG>`. The same string matches `git -C /Users/cobalt/cobalt tag -d deploy-2026-09-30-2`, which removes the previous deploy's tag. Prompt 51 P1b requires that tag to exist.  
   `grep -n "tag \*" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/DEPLOY-HUB.md"`

8. **Line 11** (against line 40). Quoted: `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)`. Line 40 says nothing is written except the one report. Line 33 reads approval from `docs/40 - DevDocs/reports/cto-<date>.md`, which is under that glob, so the same session can edit the ruling file it treats as approval. `add *` and `commit *` can then put that edit on `main`.  
   `grep -n "cto-<date>.md" "docs/40 - DevDocs/plans/fixed-files-2026-09-30/DEPLOY-HUB.md"`

9. **Line 142** (against line 93 and STANDING-LIST line 129). Quoted: `COBALT_ENV=production uv run cobalt db migrate --allow-prod`. An empty `<restart set>` takes no resident down (line 93), and 4.4 still runs. STANDING-LIST §3 says that string runs with residents down. A `.sql` path adds no label: `_module_for` returns None unless the suffix is `.py` (`src/cobalt/jobs/restarts.py` lines 94–95 and 215–216). Prompt 51 line 128: `NO migration: no db migrate runs against production`.  
   `grep -n "non-Python src asset" src/cobalt/jobs/restarts.py`

10. **Line 163** (against prompt 51 lines 145 and 150). Quoted: `A MIGRATION THAT RAN STAYS`. STEP-5 then runs (3) and starts residents. A 4.4 fault can leave `migrations applied: partial` (line 142) and still bring residents up on that schema. Prompt 51's rollback ends at the old code with `migrations applied: none`, because that prompt never migrates production. The schema command in line 170 (`--allow-prod --rollback --down-to`) is forbidden for this session (line 3).  
   `grep -n "migrations applied: none" "docs/40 - DevDocs/prompts/2026-09-30/51-deploy-3-e1-0930.md"`

## UNPROVEN

**Line 11 / STANDING-LIST line 129.** Quoted: `Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod)` and `never --rollback, never --down-to`. If an unstarred allow rule matches by prefix, that string also runs `… --allow-prod --rollback --down-to <level>` against production. No file shows the host result. `docs/40 - DevDocs/prompts/2026-09-19/45-packet/round1-verdicts.md` marks it UNVERIFIABLE FROM READS (the named experiment is `Bash(echo hi)` then `echo hi there`).

GROK READ DONE · findings: 10 · unproven: 1

[exited with code 0]
