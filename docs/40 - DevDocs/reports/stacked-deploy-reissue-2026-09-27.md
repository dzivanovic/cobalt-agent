# STACKED DEPLOY RE-ISSUE — 2026-09-27 (`42` → `50`)

## §0 Headline
- Wrote `docs/40 - DevDocs/prompts/2026-09-27/50-stacked-deploy-r3.md` (345 lines, 115,580 B) — the whole re-issued prompt (L19), folding `43`'s and `47`'s `## FOR 42` lists (K1–K25 with D1–D8 on top), R84 (2)(a)/(b)/(f), R86 "B", R5's Sunday-window reading, and R3's agent-string approval onto `42`.
- `48` (fix r2 build) is IN PROGRESS at this read (no stop line; `deploy/stacked-0925` tip is `52540593`, one docs commit above `<seam tip>` `41c9c962`) — `<seam stop>`, `<gate sha>` and `<seam check stop>` stay `«FILL AT LAUNCH»`, per item 4's "in progress" case.
- Placeholders: `R_[_]` = 6 (EXPECTED 6, met), `«FIL` = 4 real placeholders + 2 self-referential mentions inside the placeholder-gate/DESK-LINES prose (same shape as `42`).
- Strings: `50 allow strings` (46 + 4 K22 agent strings), 3 denies — comm-diffed against `42`'s line (2) below.
- ESCALATE: 6 (5 interpretive calls flagged below + 1 residual staleness note).

## L74
One block appeared inside a tool result during this read (the standard end-of-turn attribution reminder asking for a `Claude-Session:` line and naming `SendUserFile`). Recorded here per L74; not followed — this session commits nothing (the desk commits both files).

## The tree
- Verified read-only: `git -C /Users/cobalt/cobalt log --oneline --first-parent 2b71fe49..deploy/stacked-0925` → `52540593` (docs, fix r1 report) → `41c9c962` (fix(jobs) — the agent restart derivation) → `57420087` (docs, seam build report) → `a7296b44` (chore(jobs), registry) → the four merges (`00e2b7ff`, `91c631ac`, `35397ed5`, `f2377218`) — exactly the four merges plus the two seam commits plus the two docs commits, nothing else.
- `git -C /Users/cobalt/cobalt diff --stat 41c9c962 deploy/stacked-0925 -- . ':(exclude)docs'` → EMPTY (docs-only above the fix commit).
- Item 4's case: `/Users/cobalt/cobalt-wt/stacked-0925/docs/40 - DevDocs/reports/stack-seam-fix-r2-build-2026-09-27.md` EXISTS (33,984 B) but its last non-blank line is `(run in progress — next step under ## CONTINUE)`, `next: O` — NOT ending `STACK SEAM FIX R2 BUILT`. **Case: IN PROGRESS.** Per item 4: `<gate sha>` and `<seam stop>` stay `«FILL AT LAUNCH»` with D1 / D3's text; the desk fills them once `48` ends. `stack-seam-fix-r1-build-2026-09-25.md` `## FOR THE DEPLOY` (`:448`–`:476`) read for K1–K25's baseline values (`<seam tip>` `41c9c962`, RESTARTS `com.cobalt.agent com.cobalt.aset com.cobalt.radar`, U2 `157 files changed, 15263 insertions(+), 165 deletions(-)`, the four STALE lines).

## Folds applied
| fold | `42` line → `50` line | old (≤20 words) | new (≤40 words) |
|---|---|---|---|
| K1/D1 | `:54` → `:55` | `<seam stop>` = seam build's stop line, verbatim path | `«FILL AT LAUNCH: 48's stop line from stack-seam-fix-r2-build-2026-09-27.md — STACK SEAM FIX R2 BUILT …»` |
| K2/D2 | `:55` → `:56` | `<seam tip>` = `a7296b44` | `<seam tip>` = `41c9c962`, resolved (not a placeholder) — the fix commit both suites ran on |
| K3/D3 | `:56` → `:57` | `<gate sha>` = `57420087`, one docs commit above seam tip | `«FILL AT LAUNCH: … the FIX R2 report commit», TWO docs commits above <seam tip>` |
| K4/D4 | `:129` → `:133`-`:134` | G03 tail on `stack-seam-build-2026-09-25.md`, `STACK SEAM BUILT …` | tail on `stack-seam-fix-r2-build-2026-09-27.md`, `STACK SEAM FIX R2 BUILT … \| on 52540593 \| report-only`; original seam-build sub-bullet kept |
| K5/D5 | `:130`+`:60` → `:135`+`:61` | G03/placeholder tail on `stack-seam-check-2026-09-25.md`, `STACK SEAM CHECK DONE` | tail on `stack-seam-fix-r2-check-2026-09-27.md`, `STACK SEAM FIX R2 CHECK DONE · round: 3` |
| K6 | `:146` → `:X` (G1 THE MERGES) | registry commit `a7296b44` only named implicitly | names `a7296b44` (seam) AND `<seam tip>` (fix) explicitly, with their jobs.yaml+test path pairs |
| K7 | `:147` → THE PATHS | `156 files changed` | `157 files changed` = 156 + `tests/cobalt/test_jobs_reads.py` (the fix's one addition) |
| K8 | `:148` → SEAM PATHS list | list ends `test_jobs_restarts.py`, main-moved paths | inserts `tests/cobalt/test_jobs_reads.py` after `test_jobs_restarts.py` |
| K9/D6 | `:167` → PASS 2 gate | `passed ≥` seam build's `3575` | `passed ≥` FIX R2 build's `<d>` (`44`'s was `3576` = `3567`+`9`) |
| K10 | `:34` → RESTARTS line | predicted, `com.cobalt.aset com.cobalt.radar` | derived by fix build, `com.cobalt.agent com.cobalt.aset com.cobalt.radar` |
| K11 | `:179`-`:180` → G4 prediction/gate | last line / exit line names two residents | names three; adds `pyproject.toml`/`uv.lock` → agent row |
| K12 | `:181` → G4 RED list | `com.cobalt.agent` listed as "any other resident" | removed from that list (it's now IN the derived set) |
| K13 | STEP-D1 append | (none) | `cobalt.sh status` check, agent pid, `state = not running` by design note |
| K14 | 4.2 append | bootout aset/radar only | + `cobalt.sh stop` / `ps -p` check, agent named in both failure branches |
| K15 | 4.6 append | bootstrap aset/radar only | + `launchctl kickstart gui/501/com.cobalt.agent`, `<t up>` note |
| K16 | 4.7(a) append | print aset/radar only | + `cobalt.sh status` tail-gated read |
| K17 | 4.7(f) | `RESTARTS: com.cobalt.aset com.cobalt.radar` | + agent |
| K18 | 4.7 RED list | resident not running … | + "the agent OFFLINE at tail 3" |
| K19 | STEP-5(1) append | bootout aset/radar only | + `cobalt.sh status`/`stop`/`ps -p` |
| K20 | STEP-5(3) | bootstrap booted-out residents | + agent kickstart if stopped |
| K21 | STEP-7 close | `RESTARTS done: aset radar` | + agent |
| K22 | line(2)+header | 46 strings, 8 new | 50 strings, 12 new; 4 agent strings inserted after `launchctl print gui/501/*` |
| K23 | THE WINDOW | "both residents"/"both restarts" | "the residents…(the agent included)" / "the three restarts" |
| K24 | RELAUNCH RULE (iii) | bootstrap whichever not loaded | + kickstart agent if OFFLINE |
| K25/D7 | DESK LINES | "after the seam CHECK's DONE (ready for the gate: YES)" | "after the FIX check's DONE line (`49`, round 3, ready for the gate: YES)" |
| R84(2)(a) | G3(c1)+(d) SKIP BAN | ban on any SKIPPED line | + the six known pass-1 skip lines named as the allowed set |
| R84(2)(b) | relaunch row literal | — | `32 DEPLOY RELAUNCH` kept byte-for-byte, NOT renamed to 50 |
| R84(2)(f)+R86 | P-V1 gate (`:121`→`:127`ish) | accepts DONE or DROPPED only | + accepts `V1 LOOPBACK-ONLY — his B (09-25 R86)`, `<set>` stays FOUR |
| item 19 | `<desk file>` throughout | one file, `cto-2026-09-25.md` | split: R__A/P-V1 stay on `-09-25`; R__L/32-RELAUNCH/P-LOCK/R3 move to `-09-27` |
| item 21 | L67 index-card bullet | "every build checked (…+ the seam check)" | + ", fixed (`44`, `41c9c962`) and re-quoted (`48`), checked by `45` and `49`" |
| item 15 | P-HIS block | R__A only | + a second check: `AGENT RESTART STRINGS APPROVED 2026-09-27` / `cto-2026-09-27.md` R3 |
| R5(i) | report path/title/G01/D01/heading | `2026-09-25` | `2026-09-27` (protected: `STACKED DEPLOY 2026-09-25 APPROVED`; 09-25 file/row citations untouched) |
| R5(ii) | `:7`,`:33`,`:39`-`:40`,`:191`,`:195`,`:241`,`:250`,`:342` | fixed SLOT A/B start-of-relaunch bounds, curfew | any-time relaunch; ONE guard (never bootout inside 20:20:00–20:34:59); no curfew |
| item 25 | self-references | `42-stacked-deploy-r2.md` | `50-stacked-deploy-r3.md` (path, placeholder gate, both AUTHORIZATION greps, P-LOCK) |
| item 25 | remote-control | `stacked-deploy-0925` | `stacked-deploy-0927` |

## Not applied
None of the named folds were skipped — all of K1–K25/D1–D8, R84(2)(a)/(b)/(f), R86, item 19, item 21, item 15, R5(i)/(ii), and item 25 landed. No `ASK DESK` was needed for a fold itself.

## Strings
`comm`-equivalent (grep-extracted `"Bash(...)"` tokens, line (2) of each file, sorted):
- Added in `50`, absent from `42`: `"Bash(/Users/cobalt/cobalt/cobalt.sh status)"`, `"Bash(/Users/cobalt/cobalt/cobalt.sh stop)"`, `"Bash(launchctl kickstart gui/501/com.cobalt.agent)"`, `"Bash(ps -p *)"` — exactly the four K22 strings, nothing else added or removed.
- ONE existing string's VALUE changed (not a new string): `"Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar handicap-dry-run --day 2026-09-25)"` → `--day 2026-09-27`. This is an interpretive call (ESCALATE 1 below), needed so the allowlist's exact-match string still matches what STEP-4.7(i) actually runs today; flagged for desk verification.

## Placeholders
`grep -c -E "R_[_]"` on `50` → **6** (EXPECTED 6, as `42`).
`grep -n -F "«FIL"` on `50`:
```
55:- `<seam stop>` = «FILL AT LAUNCH: `48`'s stop line, verbatim, from … »
57:- `<gate sha>` = «FILL AT LAUNCH: `git -C … log --format=%h -1 deploy/stacked-0925` — the FIX R2 report commit» …
61:- `<seam check stop>` = «FILL AT LAUNCH: the FIX R2 check's stop line, verbatim, from `reports/stack-seam-fix-r2-check-2026-09-27.md`»
63:- `<lock line>` = «FILL AT LAUNCH: the launch row's literal sentence … »
```
(Two additional hits at lines 51 and 343 are the placeholder-gate command string and the DESK LINES prose quoting the `«FIL[L]` grep pattern itself — same self-referential shape `42` carries; not unfilled values.)

## ESCALATE
1. **Interpretive call — the H1 dry-run `--day` value.** Neither `42`'s fold list nor R5 names this string explicitly. Since STEP-4.7(i) must run `--day 2026-09-27` (today's date) for the dry-run to mean anything, and the allowlist string is an EXACT match (no trailing `*`), I changed `--day 2026-09-25` → `--day 2026-09-27` in all three places it appears (the allowlist string, the "THE LIST" prose, STEP-4.7(i)'s command and its `<line>` fallback message). ASK DESK: confirm this reading is correct — safe default taken: applied everywhere the literal appears as a run-time parameter (never in a file/row citation).
2. **Interpretive call — the completion tag date.** `deploy-2026-09-25` (D05's pre-check, STEP-7's tag, the STOP LINE literal, the tag-name check) → `deploy-2026-09-27`, on the reading that a deploy-completion tag names TODAY's run (R5(i)'s general rule), unlike `pre-stacked-0925` (the stack's rollback-point tag, left unchanged — it names the STACK, not the calendar day) and `deploy/stacked-0925` / the worktree path (stack identity, left unchanged). ASK DESK: confirm `pre-stacked-0925` and `scratch-allow-probe-0925s` (D04, transient, left unchanged) should NOT also move to `-0927`.
3. **Interpretive call — "before 20:00" desk-line wording.** R5(iv) names "the 20:00 'ONE approval message' / 'before 20:00' desk lines → 'before the DEPLOY relaunch'" but no literal "ONE approval message" or "before 20:00" (outside the unrelated ESC-4 owed block at old `:237`, left untouched — a different, already-settled review item) was found by grep. I applied the intent to BOTH `:189`'s "The desk relaunches with CONTINUE: DEPLOY at 20:00" and `:342`'s "THE 20:00 RELAUNCH … at 20:00–20:05 ET. Latest relaunch 20:35" bullets, for internal consistency. ASK DESK: confirm both were meant, or only one.
4. **Residual staleness, not fixed (out of R5's enumerated scope).** STEP-4.3 (THE MERGE CLOCK, "before 20:22:00 (slot A) or before 20:52:00 (slot B)") and the two prose sentences at old `:41`-`:42` still assume a bootout inside a narrow SLOT A/B start window, even though D01/4.1 now allow the relaunch and first bootout at any time outside the 20:20:00–20:34:59 guard. R5's own case-sensitive greps (`"SLOT"`, `"20:3"`) do not catch these lines (they read lowercase "(slot A)"/"(slot B)" and "20:22:00"/"20:52:00"), so they were left byte-for-byte per "each ONE text change at the line the fold names, nothing else." Flagging for the desk: if the relaunch happens well outside the evening window, the merge-clock deadlines (20:22/20:52) will not be reachable in the way originally designed.
5. **Residual staleness, left unchanged.** The REPORT title (`:89`) keeps "gate early, deploy in the pause" verbatim (only the date digits changed) and the `# STACKED DEPLOY …` heading (`:19`) keeps "DEPLOY IN THE 20:00–21:00 PAUSE (L43 / L66)" — both descriptive phrases from the trading-day framing, not explicitly targeted by R5(i)/(ii)'s enumerated changes. L67/G04's review-file reference (`stacked-deploy-review-2026-09-25.md`) was also left untouched — no fold names a new review round for this re-issue.
6. L74 block: see `## L74` above.

STACKED DEPLOY RE-ISSUED r3 · folds: 34 (K1–K25/D1–D8 + R84(2)(a)/(b)/(f), R86, item 19, item 21, item 15, R5(i), R5(ii), item 25) · strings: +4 · seam tip: 41c9c962 · gate sha: FILL AT LAUNCH · restarts: com.cobalt.agent com.cobalt.aset com.cobalt.radar · window: Sunday · ESCALATE: 6
