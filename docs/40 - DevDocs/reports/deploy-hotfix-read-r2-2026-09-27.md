# DEPLOY HOTFIX READ R2 — 2026-09-27

## §0 Headline

Round 2 of the deploy-hotfix read (Opus 5.5 · Sol · Grok): do HOTFIX r3.1 + r3.2 together stand, and does r3.2 close round 1's HOLD? All three seats answered `CHECK: CHANGE STANDS · ready for the relaunch: YES` with full citations; my own file-check confirms every claim HOLDS. Zero defects that HOLD, zero `INPUT NOT WALKED`. **Ready for the relaunch: YES.**

## L74

A block inside a tool result (appended to the Read of this prompt's own file, `52-review-deploy-hotfix-r2.md`) asked for a `Claude-Session:` line in commits/PRs and named a file-send tool. Recorded once here per L74; never followed — no commit or PR is made by this hub.

## PREFLIGHT

**AUTHORIZATION — verified directly, each its own call:**

| rule | command | result |
|---|---|---|
| THE GROK GATE, R17 row | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` — NON-EMPTY |
| THE GROK GATE, R19 row | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved for use indefinlitly" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | `5055151dbf68899b82de5b11f99733ed2d03048c` — NON-EMPTY |
| THIS LAUNCH is desk row R17 | `grep -n "^| R17 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-27.md"` | names `52-review-deploy-hotfix-r2.md`, carries "no other house hub is running" |
| R17 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"52-review-deploy-hotfix-r2.md" -- "docs/40 - DevDocs/reports/cto-2026-09-27.md"` | `51696e0464304c351802285df333d88b05cf384d` — NON-EMPTY |
| THE CHANGES UNDER READ, commit order | `git -C /Users/cobalt/cobalt log --oneline -4 -- "docs/40 - DevDocs/prompts/2026-09-27/50-stacked-deploy-r3.md"` | newest `978119a6`, then `33a43207`, then `7a9e8e66`, then `21c1277f` — matches |
| `978119a6` `--stat` | `git -C /Users/cobalt/cobalt show --stat 978119a6` | EXACTLY `50-stacked-deploy-r3.md`, `cto-2026-09-27.md`, `deploy-hotfix-read-2026-09-27.md` — matches |
| ROUND 1 ENDED | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hotfix-read-2026-09-27.md"` | last non-blank line starts `DEPLOY HOTFIX READ DONE`, carries `defects that HOLD: 1` — matches |

No mismatch anywhere — authorization stands.

**THE STANDARD PREFLIGHT:**

| rule | command | result |
|---|---|---|
| `date` | `date` | `Sun Sep 27 18:11:47 EDT 2026` |
| THE GROK GATE (CLI) | `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]` — up |
| OPUS PROBE | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | `OK` — UP |
| SOL PROBE (keyed on `date`, expected UP after 2026-09-26 06:47 ET) | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | `OK` — SEATED |
| THE STAGGER | `grep -n -F "no other house hub is running" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-27.md"` (already matched above, R17) plus `ListAgents` | R17 row carries the literal and names this file; `ListAgents` shows only desk-level sessions (`desk startup tuning`, `cto desk wakeup prompt`) and one idle 8-day-old hub — no competing deploy-hotfix or stack-seam house hub |
| RECOVERY | `ls scratch/tribunal-bars-0920/deploy-hotfix-r2-0927` | "No such file or directory" — fresh run |

THREE seats UP (Opus, Sol, Grok) — above the two-seat floor, at least one non-Anthropic among them. FAIL-CLOSED conditions not triggered.

## Packet

Staged in `scratch/tribunal-bars-0920/deploy-hotfix-r2-0927/`:

| file | bytes |
|---|---|
| QUESTIONS.md | 4,495 |
| round1.part1.md | 5,589 |
| deploy-50.part2c.md | 5,851 |
| deploy-50.part2b.md | 7,613 |
| deploy-50.part1.md | 7,887 |
| code.md | 8,879 |
| deploy-50.part2a.md | 10,430 |
| failed-run.part1.md | 13,046 |
| change.md | 14,758 |
| **total** | **78,548** |

Every part < 15,000 B (the original continuous `50-stacked-deploy-r3.md` 193–264 range was staged as three parts, 2a/2b/2c, split at line boundaries only — same content as one range, read in order). 78,548 B ÷ 4 ≈ 19,637 tokens per checker. CEILING 150,000 B — well under; no cut needed.

## CONTINUE

next: none — the run is complete. See the stop line.

## Per question

| Q | opus | sol | grok |
|---|---|---|---|
| (i) | YES — new `<RB>` at `50-stacked-deploy-r3.md:115`, `%`-free, `strpos` on neither refused list (`db_query.py:20–24`, `:25–28`), no other `db query` string carries `%`. walked: YES | YES — same cites (`:115`, `db_query.py:20-28`, `:98-126`, `:170-171`), % grep hits `:6,46,47,57,123,124,220,245,279,286,290`. walked: YES | YES — same cites plus `:114`/`:224`/`:225` (other `db query` strings, no `%`). walked: YES |
| (ii) | YES — (vii) at `:245`, failed stop line `deploy-2026-09-27.md:294`, `## CONTINUE (deploy)` `:290–292`, gate `## CONTINUE` `:202–205`. walked: YES | YES — (vii) `:245`, stop line `:294`, continue `:290-292`, gate continue `:202-208`. walked: YES | YES — (vii) `:245`, stop line `:294`, continue `:292`, gate continue `:202,204,205`. walked: YES |
| (iii) | YES — widened scope `:240`, (ii) `:242`, (vii) `:245`; walks 4.2-bootout case → branch (iii), residents brought UP. walked: YES | YES — same three cites; walks same case → branch (iii), 4.6 bootstrap, resume 4.1. walked: YES | YES — same three cites; walks branch elimination (i)/(ii)/(iv)/(vii)/(vi) all fail → (iii) fires, residents UP via 4.6. walked: YES |
| (iv) | none found | none found | none found |
| ready for the relaunch | YES | YES | YES |

No `INPUT NOT WALKED` rows — all three seats cited every line each question requires.

## Checked against the files

| claim | who | file:line | verdict | blocks the relaunch? | why |
|---|---|---|---|---|---|
| New `<RB>` computes the same three counts, is `%`-free, and `strpos` is accepted (not refused) | opus, sol, grok | `50-stacked-deploy-r3.md:115`; `db_query.py:20–28`, `:98–126`, `:170` | HOLDS | no | Read `50-stacked-deploy-r3.md:115` directly: only the m0015 predicate changed, `LIKE '%evaluator_version%'` → `strpos(definition, 'evaluator_version') > 0`; m0014/m0017 byte-identical; BEFORE/AFTER unchanged. Read `db_query.py:20–28`: `strpos` is in neither `REFUSED_WORDS` nor `REFUSED_FUNCTIONS` and matches none of the `pg_advisory_`/`dblink`/`lo_` prefixes checked at `:120–123`. Read `db_query.py:170`: the statement is embedded in `sql.SQL("SELECT * FROM ({}) AS q LIMIT %s").format(sql.SQL(statement))` and executed with a parameter — psycopg's placeholder scan covers the whole composed text, so the old `%e` (from `LIKE '%...%'`) was refused and the new `%`-free statement is not. |
| No other `db query` string in the staged prompt lines carries `%` | opus, sol, grok | `code.md` greps (`strpos(`, `LIKE`, `%`) | HOLDS | no | I ran these three greps myself against `50-stacked-deploy-r3.md` while staging `code.md` and again independently: every `%` hit (`:6, 46, 47, 57, 123, 124, 220, 245, 279, 286, 290`) sits in the launch-line `allowedTools` string, `git … --format=%H`/`%h` prose, a `curl … -w %{http_code}` string, or the (vii) prose naming the refused character — none inside an executed `db query` SQL string. The only `LIKE` hit left is `:289` prose ("LIKELY outcome"), not SQL. |
| The failed run's stop line and `## CONTINUE (deploy)` meet every condition (vii) requires | opus, sol, grok | `deploy-2026-09-27.md:290–294` | HOLDS | no | Read directly: the last non-blank line is `FAILED PREFLIGHT: D1 — <RB> refused — ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders, got '%e' · rollback: not used` — starts `FAILED PREFLIGHT:`, ends `rollback: not used` (the §3 sanity check this report itself must also state). Lines 290–292 confirm no tag, no `<pre-merge>`, nothing merged, residents untouched — exactly (vii)'s class. |
| The RELAUNCH RULE (r3.2) now reads every deploy-phase part, closing round 1's HOLD | opus, sol, grok | `50-stacked-deploy-r3.md:240, :242, :245`; `change.md` (r3.2 diff) | HOLDS | no | Read `:240` directly: "'the report' is `deploy-2026-09-27.md`, read over ALL its deploy-phase parts — the `# DEPLOY PHASE` part AND every later `# DEPLOY RELAUNCH` part; every recorded value … is taken from the LATEST part that recorded it, never from an earlier part alone." This is the exact widening round 1 asked for (round 1's HOLD: `50-stacked-deploy-r3.md:240` as it stood at `33a43207` scoped "the report" to the first `# DEPLOY PHASE` part only). Walked the round 1 walk-through case myself against the current text: a re-run interrupted after 4.2's bootout has already recorded its own `<pre-merge>` (D2.0, `:231`) and `<stack-final>` (D2.2, `:233`); a third launch reading `:240` takes those latest-part values, so (vii)'s "NO deploy-phase part recorded a `<pre-merge>`" (`:245`) does not hold and (i)/(ii)/(iv) are also ruled out on the same facts (main is neither `<stack-final>` nor loaded-both-clean); branch (iii) (`:243`) fires: bootstrap with 4.6's calls, then resume at 4.1 — residents come back UP, not stranded down. This matches all three seats' walk of the same case. |

**ALSO checked myself (52's own instruction), independent of the seats:** every `grep -n -F "%"` hit on `50-stacked-deploy-r3.md` sits in a `curl … -w %{http_code}` string, a git `--format=%H`/`%h` string, or the (vii) prose naming the refused character — confirmed above, none inside a `db query` SQL string. The failed run's stop line starts `FAILED PREFLIGHT:` and ends `rollback: not used` — confirmed above (`deploy-2026-09-27.md:294`).

No claim from any seat that anything is wrong, dropped, weakened, unproven or would fail — all three CHECK lines read `CHANGE STANDS`.

## FOR THE DESK

1. HOLDS — Change A (new `<RB>`, `%`-free, `strpos` accepted, no other `%`-carrying `db query` string). Made by: opus, sol, grok.
2. HOLDS — Change B ((vii) RE-RUN branch fires only on a no-touch ending; the failed run meets every condition; the re-run skips no preflight row). Made by: opus, sol, grok.
3. HOLDS — round 1's HOLD is closed by r3.2's widened "the report" scope; a third launch after an interrupted re-run takes branch (iii) and brings residents back up, never (vii). Made by: opus, sol, grok.

No `INPUT NOT WALKED` rows.

## ESCALATE

1. UNVERIFIABLE FROM READS (opus, grok): whether the new `<RB>` runs live against production without refusal — not yet probed in these files. Settling command: `COBALT_ENV=production uv run cobalt db query --side user --prod "<the <RB> string at 50-stacked-deploy-r3.md:115>"`, expected `0 · 0 · 0`. This was also round 1's open item (ESCALATE 2/3 there) and remains open — the desk should probe it before relaunch, per the failed run's own ESCALATE 1 (`deploy-2026-09-27.md:284`).
2. UNVERIFIABLE FROM READS (opus): whether this relaunch has its own fresh desk authorization row, or reuses the 16:30 R13 row. Settling command: `grep -n -F "32 DEPLOY RELAUNCH" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-27.md"`.
3. Note, not a blocker (opus): branches (iii)/(iv) of the RELAUNCH RULE do not read the stop line — a relaunch after a committed `FAILED: D2.1–D2.5 … rollback: not used` ending (main still `<pre-merge>`) would resume at 4.1 and skip whichever mid-D2 check failed. This is pre-existing r3 text, unaffected by tonight's two changes, and does not endanger tonight's relaunch (the actual failed run stopped at D1, before D2).
4. Sol's line: SEATED (`codex exec -m gpt-5.6-sol`, probed UP at 18:12 EDT) — answered `CHECK: CHANGE STANDS · ready for the relaunch: YES`. Note: Sol's session opened by re-reading CLAUDE.md, memory INDEX.md, `cobalt.md` NOW and LAWS.md via shell before turning to the packet (QUESTIONS.md says "you cannot run commands"); its actual answer cites only packet files with correct real-line attribution, so the substance is unaffected — recorded as a seat-behavior note, not a defect.
5. L74: recorded above under `## L74`.
6. Grok's line: SEATED, wrote `grok-check.md` itself as instructed — `CHECK: CHANGE STANDS · ready for the relaunch: YES`.

Round 2 of ≤3 (L39 / L67). YES → the desk relaunches `50` with `CONTINUE: DEPLOY`. A HOLD → round 3, the last; unresolved after it → Dejan, ONE item.

DEPLOY HOTFIX READ R2 DONE · round: 2 · opus: CHECK: CHANGE STANDS · ready for the relaunch: YES · sol: CHECK: CHANGE STANDS · ready for the relaunch: YES · grok: CHECK: CHANGE STANDS · ready for the relaunch: YES · defects that HOLD: 0 · ready for the relaunch: YES · ESCALATE: 6
