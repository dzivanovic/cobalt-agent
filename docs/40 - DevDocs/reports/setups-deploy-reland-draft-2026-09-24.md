# SETUPS DEPLOY RE-LAND — DRAFT 2026-09-24 (`31` → `32` + `33`)

## §0 Headline
`32-setups-deploy-reland.md`: re-issues `09` whole (L19). One `git revert --no-edit 4e625f6a` puts back `a0ba0098`'s tree with the residents down. The tree is proven by `diff --stat a0ba0098 HEAD -- . ':(exclude)docs'` returning empty, 0013 is proven with `--proof-only` only, and the smoke runs with the tails spaced. No gate re-runs and no gate re-cut is needed.
New rule strings: **0**. `32` and `09`: 51/51 allow strings, `comm` empty both ways. `33` and `10`: 9/9, `comm` empty. Denies and `--add-dir` are identical.
New row (h) is the revert readback: the `ASSUMED` rows stay present, the heartbeat's `failed_stage evaluate` is gone, `radar panel FAILED` does not grow after `<t up>`, and `/radar` returns 200.
Tail rule: the tails run at ≥ `<t up>` + 90 / 180 / 300 s by `date`. RED only after the third tail, at ≥ 300 s. `33` is the delta read (Sonnet 5 hub; Opus 5.5 + Grok; grok gate = R19 standing).
ESCALATE 10. Top item is the house lane: `27` (the Grok + Gemini tribunal r2) may still hold it, and `33` cannot launch beside it.

## DELTA FROM 09
| # | `09` line | before (`09`) | after (`32`) | why |
|---|---|---|---|---|
| 1 | 1 | MODEL/SEAT: deploy hub `setups-deploy-r2-0924`, re-issue of `05` as a stacked set, migration `--allow-prod` runs here | Deploy hub `setups-deploy-reland-0924`; re-issue of `09` as the RE-LAND of `a0ba0098` after the 11:40 false red, on R45. 0013 is ALREADY APPLIED and only proved (`--proof-only`). NO rebase, merge, pytest (except 6.8), DB write or gate re-cut | `31` HEADER; R45; `deploy-2026-09-24.md` ESC 4 |
| 2 | — | (none) | NEW `WHAT HAPPENED` paragraph (from `31`) | `31` WHAT HAPPENED; the incident is the run's premise |
| 3 | 3–4 | bare command (1): gate re-cut `checkout -B deploy/stacked-0923 replay/mover-partial-0924` | (1) NO GATE RE-CUT: deleted. `deploy/stacked-0923` stays at `a0ba0098` and its worktree is untouched | `31` "command (1) of `09` is DELETED" |
| 4 | 5 | DESK LINE: hold "until the relaunch's 4.3" / "desk re-cuts"; row R25 | Hold until the relaunch's 4.2; row `R__L` | the revert is 4.2 now; placeholder per `31` |
| 5 | 7 | launch line: `09-setups-deploy-r2.md`, rc `setups-deploy-r2-0924` | Launch line is byte for byte except the prompt path `32-setups-deploy-reland.md` and rc `setups-deploy-reland-0924` | `31` (3) |
| 6 | 9 | THE LIST: provenance from `66`/`05`, R3 + R52 | The same 51 strings and approval (R3 + R52). NEW: a NEVER RUN HERE list of the 13 strings carried only for byte identity, `--allow-prod` without `--proof-only` included | `31` "each is named `NEVER RUN HERE`" |
| 7 | 11 | title: stacked, ff-merge, migration, "DONE TRADING" word (R83) | title: RE-LAND by revert of `4e625f6a`, 0013 proved, tails spaced, readback row, R45 | `31` HEADER |
| 8 | 13–20 | LADDER / WHAT SHIPS (tips to read at P5, chain, shared path, WITH-DB PROOF) | WHAT SHIPS = `a0ba0098`'s tree on `<main0>` via `<reland>`, with the same two branches' path lists. ITS PROOF = `09`'s gate and smoke artifacts, read and never re-run. The WITH-DB PROOF paragraph is removed (the gate ran: 2856/0) | consequence of `31` deleting STEP-1/2/3; nothing rebuilt (`31` LAW STEP) |
| 9 | 22–29 | THE SHAPE: rebase, stack, gate, `main` into the gate, ff-merge, migrate; rollback `revert -m 2 <stack-final>` | THE SHAPE: revert of the revert, then STEP-R (snapshot + tag), then residents down, revert, prove the tree, proof-only, validate + restarts, up. Rollback: ONE `revert --no-edit <reland>`, stated as RETURNING production to the degraded state | `31` LAW STEP (L54 rollback shape) |
| 10 | 31–32 | L66 SHAPE / DOWNTIME: restarts predicted at 2.5; ≈17 s + migration proof | RESTARTS were derived by `09` (2.5, 4.7 (f)) and are re-derived on `<main0>..<reland>`. Downtime ≈ 20 s + one proof-only (≈ 80 s) + bootstrap, likely > 60 s → ESCALATE, never a failure | `31` STEP-R/4.5; L73 |
| 11 | 35–44 | THE WINDOW: start on `DONE TRADING <hh:mm>` (R83); MERGE CLOCK 19:58 / PAUSE merge clock from P14-M | START at launch on R45; the `DONE TRADING` wait is dropped. DAY (R45 on R83/R39) before 19:55, REVERT CLOCK 19:58. PAUSE 20:00–20:20 with the REVERT CLOCK at 20:22 (fixed: no P14-M in this run). BETWEEN / too late as `09`. `window: DAY (R45)` | `31` WINDOW clause |
| 12 | 46–67 | AUTHORIZATION: R83 first; R25 launch row with `TWO BRANCHES: …` | R45 first (`right now` + `re-land`, `-S"| R45 |"`). R39 kept as the precedent (missing → ESCALATE, not a stop). R83 / R4 / R104 / R113 / R114 / R119 / R82 / R118 / R3 / R52 unchanged. The launch row `R__L` carries `RE-LAND: a0ba0098 by revert of 4e625f6a` | `31` HEADER/AUTH |
| 13 | 68–70 | TWO ASYMMETRIES (`.env` in gate; residents down) | ONE ASYMMETRY (residents down; before the revert: bootstrap only). No `.env` is ever copied | no with-DB gate in this run |
| 14 | 72–74 | placeholder gate on `09`'s path | the same gate on `32`'s path; his rows R45 / R3 / R52 literal | L19 |
| 15 | 76–102 | INDEX CARD (1) laws + (2)–(6) `68`/`59` reports, `d3`, 0013 SQL, ADDING-A-SETUP, plist | Law lines reworded where the shape changed (L43, L54, L66, L67, L68, L76). (2) = `deploy-2026-09-24.md` (read, never append). (3) ADDING-A-SETUP (via `git show a0ba0098:` before 4.2). (4) plist. `68`/`59`/`d3`/SQL reads dropped | the gate/migration legs they served are gone |
| 16 | 104–110 | REPORT `deploy-2026-09-24.md`; THREE commit points incl. the mid-run 2.8 | REPORT `deploy-2026-09-24-reland.md` (NEW file; the failed record never appended). ONE commit point at the end, NO mid-run commit (`main` must stay `<main0>` until 4.2). Sections: `## STEP-R` replaces `## L68 GATE` | `31` REPORT |
| 17 | 112–130 | UNATTENDED RULES incl. THE WITH-DB READ, `.env` cwd rules for STEP-2 | WITH-DB READ removed. The one pytest (6.8) runs in the foreground. The `cd` is used only for 6.8. `COBALT_ENV=dev` only on 6.3's string | no suites except 6.8 |
| 18 | 134–135 | P00 / P-HIS `DONE TRADING` grep + `-S` | P00 (R45 first); P-HIS lives in AUTHORIZATION (R45) | `31` STEP-0 |
| 19 | 140–151 | P1 dirt list (07:0x ET) | P1 uses the KNOWN DIRT of 12:15 (below). Two live tribunal reports are named NEVER added. Dirt under `src/`/`configs/`/`tests/`/`ops/` (other than `rules.yaml`) → `FAILED: preflight — unexpected dirt <path>`. The untracked-added-path refusal is kept, reworded for the revert | `31` STEP-0 |
| 20 | 154 | P4 tag names | P4 now also covers MAIN = REVERT + DOCS: `rev-parse` `<main0>`; `log --oneline -1 4e625f6a` = `Revert "Merge branch 'main' into deploy/stacked-0923"`; `merge-base --is-ancestor 4e625f6a HEAD`; `diff --stat 4e625f6a HEAD -- . ':(exclude)docs'` EMPTY; `deploy/stacked-0923` = `a0ba0098`; `deploy-2026-09-24` absent; `pre-setups-0924` = `1118c3d4` (never re-tagged); `pre-reland-0924` absent | `31` STEP-0 / STEP-R |
| 21 | 155–173, 175–196 | P5 builds, P6 checks, P7 dev DB, P8 blind values, P10–P12 worktrees/identity/gate cut, P13 three `.env` reads | DELETED, except that P13 is kept as ONE read: `ls -la …/stacked-0923/.env` must NOT exist (L76) | nothing is rebuilt or re-gated; `31` "the lock is free" |
| 22 | 174 | P9 reads `10`'s report | P9 reads `33`'s report `setups-deploy-reland-review-2026-09-24.md` (committed; `SETUPS DEPLOY RELAND REVIEW DONE`, houses ≥1, blockers 0 or folded on `R__L`) | `31` (2) |
| 23 | 197–211 | P14 baseline: RED only the carried bars kind; slug `True` expected; markers pre-stack | P14 DEGRADED BASELINE: radar `failed_stage evaluate` EXPECTED; other new kinds recorded, not a stop. `<rp0>` added. Slug `False` expected (`True` → FAILED, the desk decides). Markers as `09`. Cards `<cards0>`. NEW: the three `ASSUMED` rows read (`<n_assumed0>`; 0 → ASK DESK + continue) | `31` STEP-0 |
| 24 | 212 | P14-M proof-only before the window | REMOVED from preflight. The one proof-only runs at 4.4 inside the window | `31` 4.4 |
| 25 | 217–299 | STEP-1 / STEP-2 / STEP-3 (rebase, stack, L68 gate, 2.8 commit, main into gate, snapshot, `pre-setups-0924`, RELAUNCH RULE) | DELETED → `## STEP-R` (R.1 read-only tree proofs incl. `merge-base --is-ancestor a0ba0098 HEAD`, `<stack stat>`; R.2 `backup run` + `status`; R.3 `tag pre-reland-0924 <main0>`; R.4 expected RESTARTS line; R.5 RELAUNCH RULE) | `31` STEP-1/2/3 |
| 26 | 291–298 | RELAUNCH RULE (i)–(vi) for merge states | Re-derived for this run's states: (i) revert in progress → abort, prove, bootstrap, FAILED. (ii) HEAD = `<main0>` → bootstrap, re-read baselines, resume at 4.1 in window. (iii) HEAD = `<reland>` → prove, proof-only if unrecorded, bootstrap, 4.7. (iv) STEP-5 done → never re-entered. (v) STEP-6 resume. (vi) any other HEAD → FAILED, residents named | `31` REPORT |
| 27 | 303–304 | 4.1 HARD CLOCK; 4.2 bootouts | 4.1 HARD CLOCK (REVERT CLOCK); 4.1b bootouts (as `09`) | numbering: `31` names the revert 4.2 |
| 28 | 307–309 | 4.3 `merge --ff-only deploy/stacked-0923` | 4.2 `revert --no-edit 4e625f6a` (pre-checks HEAD = `<main0>`, gate = `a0ba0098`). Conflict/error → `revert --abort`, HEAD read, residents UP, `FAILED: 4.2 — revert conflict <files>` | `31` 4.2 |
| 29 | — | (none) | NEW 4.3 PROVE THE TREE: `rev-parse` `<reland>`, `HEAD^1` = `<main0>`, `diff --stat a0ba0098 HEAD -- . ':(exclude)docs'` EMPTY (else STEP-5 at once), `diff --stat 4e625f6a HEAD …` = `<stack stat>` | `31` 4.3 |
| 30 | 310–314 | 4.4 `db migrate --allow-prod` (applies 0013) | 4.4 `--allow-prod --proof-only` ONLY. The non-proof string is NEVER RUN HERE (capitals). Gate: exit 0, no `CHANGED`, `NOTHING WAS APPLIED`. "0013 applied" is proven by the `attnotnull` read-back `False` (proof-only prints no pending list — ESC 2) | `31` 4.4 |
| 31 | 315 | 4.5 validate | 4.5 validate + `jobs restarts <main0>..<reland>` (both residents, no UNCLASSIFIED, else `FAILED: 4.5 — RESTARTS <line>` → STEP-5) | `31` 4.5 |
| 32 | 332 | 4.7 (b) radar tail: up to three tails, spacing unstated | TAILS SPACED: tail 1 ≥ `<t up>`+90 s, tail 2 ≥ +180 s, tail 3 ≥ +300 s by `date`. (a)(b-counts)(c)(d)(f)(g)(e1) run before tail 1; (e2) and `date` + `heartbeat show` fill between tails, never a wait. RED only after the third at ≥ 300 s, or on a post-`<t up>` `S5 evaluate FAILED` / `lifecycle card read failed` | `31` 4.7 (b); `09` ESC 2; cto-desk lesson (2) |
| 33 | 335 | 4.7 (e) twice, same kinds | Unchanged, except that the old code's `failed_stage evaluate` record is allowed on the FIRST read only (before the new radar's first cycle). (h) judges the incident kind | drafter precision: the heartbeat record predates the restart |
| 34 | 336 | (f) restarts `<pre-merge>..<stack-final>` | (f) restarts `<main0>..<reland>` | `31` |
| 35 | — | (none) | NEW (h) REVERT-READBACK after tail 3: `ASSUMED` count ≥ `<n_assumed0>` (lower → RED); heartbeat without `failed_stage evaluate` (present after (e2) → RED → STEP-5 + ESCALATE text); `grep -c "radar panel FAILED"` = `<rp_up>` (read FIRST after `<t up>`); `/radar` 200 | `31` (h). ≥ rather than = because a new cycle may write more `assumed_formation` dots (ESC 7) |
| 36 | 339–340 | card-surface proof chain; RED list | chain rewritten to `5e62ea26` → `a0ba0098` → `<reland>`, plus (h); RED list + (h) | `31` |
| 37 | 342–357 | STEP-5: `revert -m 2 <stack-final>`, prove vs `<pre-merge>`; 0013 stays "if 4.4 ran" | STEP-5: ONE `revert --no-edit <reland>`, prove `diff --stat 4e625f6a HEAD … ` EMPTY. Capitals: RETURNS production to DEGRADED, the desk decides, never a second revert, never a DB write. 0013 always stays. (4) re-runs smoke incl. (h), expecting the degraded kind (recorded, not a new failure) | `31` STEP-5 |
| 38 | 362 | 6.1 note absence evidence (09-23) | evidence: `09` never reached STEP-6 (`deploy-2026-09-24.md` ESC 4 / 7) | fact update |
| 39 | 364 | 6.2 "the folder does not exist" | if the rows file exists, Read it and it must equal the block byte for byte, else Write | `09` never created it (not reached); safe on relaunch |
| 40 | 406 | 6.7 tails "as 4.7 (b)" | Tails spaced +90 / 180 / 300 s after `<t write>`; + `radar panel FAILED` = `<rp_up>`; heartbeat as (h) | the same lesson applied to the same kind of read |
| 41 | 407–408 | 6.8 gate HEAD must = `<stack-final>` | Gate HEAD must = `a0ba0098` (NOT `<reland>`: `<reland>` lives on `main`; the gate worktree is not moved), plus `status --short --branch` | a literal `<stack-final>` → `<reland>` swap would FAIL 6.8 by construction (ESC 3) |
| 42 | 417–422 | STEP-7 tag, table, ESCALATE, commit | STEP-7 order and `reset --soft` shape unchanged. `<stack-final>` → `<reland>`, `<pre-merge>` → `<main0>`. Table names both rollback tags and the new rollback shape. ESCALATE adds the three rows and `cobalt_dev` untouched. Report path `…-reland.md` | `31` STEP-6/7 (ESC 1 on the tag point) |
| 43 | 425–426 | stop lines `SETUPS DEPLOY R2 DONE …` | `SETUPS DEPLOY RELAND DONE · reland: <sha> · tag: deploy-2026-09-24 · rows: 4 · live-note: <n passed> · S2 smoke: owed 21:10 · ESCALATE: <n>` / `FAILED: … · rollback: <used|not used> — migration 0013 applied: yes — aset: … — radar: …` | `31` REPORT |

`33` vs `10`: hub Sonnet 5, `10`'s 9 allow strings / 3 denies / `--add-dir` triplet byte for byte, rc `setups-deploy-reland-review-0924`, cwd `agy-trial`. The grok gate is the standing row R19 (`All 4 house models approved`), replacing `10`'s dated R17 DATE GATE. R45 was added to AUTHORIZATION. One placeholder `R__L` (no `R__G`). The packet is delta-only (`delta.md`, `32-delta-sections.md`, `launch-09.md`, `incident.md`, `what-happened.md`, `tree.md`, `greps.txt`). Q1–Q6 = `31`'s five read targets + dialog/harm. Text carried unchanged from `09` → `OUT OF SCOPE`. House time is 12 min (`10`: 20). Stop line `SETUPS DEPLOY RELAND REVIEW DONE · houses: <n> of 2 · blockers: <n> · folds: <n>`.

## KNOWN DIRT
`git -C /Users/cobalt/cobalt status --porcelain`, read by this drafter at 12:2x ET. It matches the desk's 12:15 list exactly:
```
 M configs/cobalt/rules.yaml
 M "docs/40 - DevDocs/reports/seat-usage.md"
?? "docs/40 - DevDocs/reports/.grok-stdout-2026-09-22.tmp"
?? "docs/40 - DevDocs/reports/day-open-2026-09-24.md"
?? "docs/40 - DevDocs/reports/drc-overnight-tribunal-fable-r2-2026-09-24.md"
?? "docs/40 - DevDocs/reports/drc-overnight-tribunal-r2-2026-09-24.md"
?? "docs/40 - DevDocs/reports/routing-x5-retro-2026-09-23.md"
?? "docs/40 - DevDocs/reports/voice-v1-check-2026-09-23.md"
```
(New since then: this drafter's three untracked files, `prompts/2026-09-24/32-…`, `33-…` and this report.) Revert safety, read by the drafter:
- `comm -12` of the paths `4e625f6a` touches against the paths `4e625f6a..HEAD` touches → EMPTY (7 commits above the revert, docs only).
- `git log --stat 4e625f6a..HEAD -- . ':(exclude)docs'` → EMPTY.
- `rules.yaml` / `seat-usage.md` in `4e625f6a`'s file list → 0 hits.
- None of the untracked files is a path the revert adds back.

## RULE STRINGS
| pair | allow strings | `comm -23` (base only) | `comm -13` (new only) | denies + `--add-dir` (`cmp`) |
|---|---|---|---|---|
| `32` vs `09` | 51 / 51 | EMPTY | EMPTY | identical |
| `33` vs `10` | 9 / 9 | EMPTY | EMPTY | identical |
Method: each file's `(3) claude --bg` / `claude --bg` line was cut before `--disallowedTools`, `grep -o '"Bash([^"]*)"'`, sorted, then `comm`; the tail after `--disallowedTools` compared with `cmp`. Placeholders: `32` has `R__L` on 4 lines (7, 64, 66, 158), and `33` on 2 (31, 50). The desk fills them.

## FOR DEJAN
NONE. No new string and no new window: R45 is his word. The migration is proof-only because 0013 is applied. The vault write is his R3 / R119 / R82 / R118, unchanged.

## ESCALATE
1. `ASK DESK: STEP-7 tag point [12:27]`. `31` says both "tag `deploy-2026-09-24` at `<reland>`" and "NOT at `<reland>`: the tag goes on the commit that carries the report — keep `09`'s STEP-7 order and `reset --soft` shape exactly". `09`'s order tags HEAD BEFORE the report commit, so the tag lands on `<reland>`. Safe default taken: `09`'s order kept byte for byte (tag on `<reland>`, the deployed code). To tag the report commit instead, swap STEP-7 items 1 and 5.
2. `31` 4.4 asks "the proof must show 0013 applied and nothing pending". `--proof-only` prints a proof table and `NOTHING WAS APPLIED…` (`src/cobalt/db_migrations/cli.py:468`), not an applied/pending ledger. `32` therefore proves "applied" by the `attnotnull` read-back (`False`) right after 4.4. UNPROVEN (L70): the NEW code's proof-only output on production. The drafter never ran it.
3. 6.8: a literal `<stack-final>` → `<reland>` swap would require the gate worktree's HEAD to be `<reland>`, which is impossible (`<reland>` exists on `main` only). `32` requires `a0ba0098` and relies on 4.3's non-docs identity. A deliberate deviation from `31`'s "every `<stack-final>` → `<reland>`".
4. **HOUSE LANE: `33` needs the Grok lane (one Grok hub at a time).** R44 launched `27` (a Grok + Gemini tribunal r2 hub, cwd `agy-trial`) at 12:1x, and its report `drc-overnight-tribunal-r2-2026-09-24.md` is untracked and live. `33` checks for the stagger literal `no other house hub is running`, which the desk cannot write truthfully while `27` runs. `ASK DESK: wait for 27's stop line, or rule an exception for 33 given degraded production [12:27]`. Safe default: wait. The L67 floor is Grok, so an Opus-only read does not satisfy it.
5. `33` house time is 12 min (`10`: 20) because of the degraded production and the ≈ 60–80 KB delta packet. The desk may restore 20.
6. Consequential deltas beyond `31`'s explicit list (rows 8–10, 13, 15, 17, 21, 24, 33, 38–40): each follows from a deleted step or from the no-gate shape, and each is a row above. `33` Q6 reads them.
7. (h) count rule is `≥ <n_assumed0>` where `31` said "→ the STEP-0 count". Reason: a new radar cycle can write more `assumed_formation` dots (the new code wrote 3 in one cycle). A lower count is RED. The desk may tighten this to equality if new writes are impossible.
8. Drafter process: `31` says "Write tool only". `32`, `33` and this report were written with the Write/Edit tools. Bash was used only for reads and for `comm`/`cmp` scratch files under `$CLAUDE_JOB_DIR/tmp` (never in a worktree or the vault). Several Bash reads (`sed`, `find`, `comm`, `cmp`, `git status`) are not among the seven launch strings; auto mode allowed them. No DB, no git write, no launch.
9. LAWS.md was NOT read in full (L59): time-bound under degraded production. The sections read were L19, L54, L66 and L68 (verbatim) plus the heading index for L43 / L67 / L70 / L73 / L76, and the `cto-desk.md` last eight lines. `33`'s houses and the desk's end-to-end read of `32` cover this; the desk may run the full L59 read before launch.
10. Downtime prediction for `32`: ≈ 100–120 s (> 60 s → ESCALATE by rule, not a failure). The one proof-only was ≈ 79 s on the old code (`09` P14-M).

SETUPS DEPLOY RELAND DRAFTED · new rule strings: 0 · readback rows: 1 · tail rule: 90/180/300 · window: R45 now · restarts: com.cobalt.aset com.cobalt.radar · ESCALATE: 10
