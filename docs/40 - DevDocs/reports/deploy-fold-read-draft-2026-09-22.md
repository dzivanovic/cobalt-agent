# DEPLOY FOLD READ — DRAFT REPORT 2026-09-22 (seat `deploy-fold-read-draft-0922`, 11:22–11:25 ET)

## DIGEST
- Wrote `prompts/2026-09-22/25-review-stacked-deploy-r2.md`: round-2 (L67) Grok + Gemini read of `05`'s two `[fold, desk 11:2x]` sentences ONLY, on `06`'s shape. NOT launched (L36).
- Launch line = `06`'s byte for byte except the prompt path and `--remote-control stacked-deploy-review-r2-0922`; cwd `~/cobalt-wt/agy-trial`; Sonnet 5; auto. New rule strings: 0.
- Staging `scratch/tribunal-bars-0920/stacked-deploy-0922/r2/` (inside `06`'s grok Write root). Packet: `fold.md` (P12 paragraph whole, STEP-4.5 whole, the 2 fold lines ±6), `evidence.md`, `rulings.md`, `greps.txt`, `QUESTIONS.md`.
- PREFLIGHT: date gate · `grok --version` · `agy --version` · fold committed (`git log -S"fold, desk 11:2x"`) · exactly 2 fold lines · the `19` stagger (at 11:22 the tribunal-r2 report does not exist) · RECOVERY `ls`.
- Q1 (P12 exception safe?), Q2 (smoke (e) still real?), Q3 (no string / order / L66 change); plus the other radar/heartbeat sentences' consistency. Stop line `STACKED DEPLOY REVIEW R2 DONE · houses: <n> of 2 · blockers: <n> · folds: <n>`.
- `05` untouched. My own reading (ESCALATE 2) finds a likely REPEAT of the 11:06 stop: the fold does not cover the probe's own per-record `poll <ticker> … since …` finding.

## RULE PROOF
`grep -c -F -e "<string>"` against `25` and `06` (`prompts/2026-09-22/`), 11:24 ET:

| string | 25 | 06 |
|---|---|---|
| `"Bash(grok *)"` | 1 | 1 |
| `"Bash(agy *)"` | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 |
| `"Bash(ls *)"` | 1 | 1 |
| `"Bash(grep *)"` | 1 | 1 |
| `"Bash(tail *)"` | 1 | 1 |
| `"Bash(wc *)"` | 1 | 1 |
| `"Bash(date*)"` | 1 | 1 |
| `"AskUserQuestion"` | 1 | 1 |
| `"EnterWorktree"` | 1 | 1 |
| `"Bash(git push*)"` | 1 | 1 |
| `--model claude-sonnet-5 --permission-mode auto` | 1 | 1 |
| `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt` | 1 | 1 |

Everything after `--remote-control <name> ` compared as one string: IDENTICAL. `"Bash(` strings on `25`'s line: 10 (9 allow + 1 deny), the same as `06`'s. New: **0**. Every command in `25` fits one of those shapes (`grep -n`, `tail -n`, `ls`, `wc -c`, `date`, `git -C … log`, `grok`, `agy`).

## ESCALATE
1. **Q1, MY READING — lifecycle refusal.** `runner.py:300-306` does share the stamp: `stamp_failure(pool_key, failed_stage="bars", failed_detail=lifecycle_refusal, …)`. The detail text is `lifecycle card read failed: …` (`runner.py:257`) or `lifecycle polling refused for …: …` (`runner.py:269`). The probe prints it as `failed_stage bars: <that text>` (`probes.py:107-108`), NOT `poll failures: <n>`. So the fold's wording "ONLY finding is `failed_stage bars: poll failures: <n>`" DOES exclude a persisted refusal when read literally. RESIDUAL, UNVERIFIED: the refusal is written AFTER `stamp_poll` in the cycle. `stamp_poll` sets `failed_detail` to `poll failures: <n>` whenever records are carried (`store.py:266-272`), and the S2 row does the same (`runner.py:375-376`). So a beat that samples between S2/S4 and the lifecycle stamp sees only `poll failures: <n>` while a refusal is live. That timing gap already exists without the fold: with no records carried, the row is clean in the same gap. The fold turns a RED sample into a baseline one only when records ARE carried. Not a blocker as I read it. Settle with `grep -n "def stamp_failure" -A25 src/cobalt/radar/store.py`.
2. **LIKELY REPEAT STOP (my reading, file-backed): the fold misses the probe's per-record finding.** For every carried record older than `heartbeat.radar_scan_max_age_s` = **320 s** (`tunables.yaml:504-505`), `probes.py:110-117` also appends `poll <ticker> <reason> since <since>`. At 11:04:48 ILAG's record (since 15:02:06Z) was 162 s old, so the line read only `failed_stage bars: poll failures: 1`. Any record carried longer than 5 m 20 s adds a second finding. That breaks the fold's "ONLY finding" at P12, so the relaunch FAILS PREFLIGHT again on the same design. In (e), the "ANOTHER kind" list (`last_scan_at stale`, `degraded …`, `mirror …`) does not say whether `poll …` counts, so a record that ages past 320 s during the run may turn (e) RED. I assume `since` is kept across polls (`poller.py:66` keys existing items by `(ticker, reason)`), but have not run it. Fold, verbatim-ready, for the desk if the houses confirm it: P12 "whose ONLY finding is `failed_stage bars: poll failures: <n>`" → "whose ONLY findings are `failed_stage bars: poll failures: <n>` and zero or more `poll <ticker> <reason> since <since>`". Mirror it in (e): "a finding of ANOTHER kind (`last_scan_at stale`, `degraded …`, `mirror …`, `failed_stage` with any detail but `poll failures: <n>`, `poll failure … invalid since`)". `25`'s Q1 sends the houses to this finding explicitly.
3. **Packet deviation, disclosed.** Index card item 4 lists four source excerpts. `25` adds two more: `runner.py:290-315`, which THE JOB's Q1 names ("walk `runner.py:300-315`"), and `tunables.yaml:504-510`, without which ESCALATE 2 cannot be judged from reads (L33). Nothing else of `05` is added. The desk strikes them if unwanted.

DEPLOY FOLD READ PROMPT DRAFTED · questions: 3 · new rule strings: 0 · ESCALATE: 3
