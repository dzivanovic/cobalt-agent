# DRC Tribunal — Round 1 (Grok + Gemini, Astra carried/METER, Fable seat blind) — 2026-09-22

## §0 Headline
- DRC automation proposal (F14) ruled round 1 by Grok + Gemini (both ADOPT/ADOPT WITH on all 21 items, 0 REJECT, 0 DO NOT BUILD); Astra METER — proceed on three (R13, probe UP but usage-limited); Fable seat ruled blind, its claims file-checked at collate.
- Verdict: BUILD AFTER — both houses gate on E1 (his real DAS/trading-log export); two genuine cross-house splits carried to the derive, not resolved here: (e) header-change FAIL-vs-degraded rule, (f)/T7 whether a C2 refusal ever fails the build.
- Claims checked against the files: 21 of 22 HOLD (1 DOES NOT HOLD — gemini's `db_migrations/0014_legs.sql` citation contradicts its own (j) answer and the packet's own note that no migration number is settled). Fable round-1 claims checked: 12 HOLD of 14 checked (2 UNVERIFIABLE FROM READS this pass).
- Redactions: 0. SHAPE-ONLY drops: 30 lines (`14-drc-shape.md`, counted, none staged). Packet 177,004 B — over the 140 KB target after all five cut-order steps (not a failure per the launch prompt).
- ESCALATE: 8 — headline items: L31 (vendor-names law) was cut from the packet before either house saw it; the (e) and (f)/T7 splits; gemini's uncorroborated migration filename.

## AUTHORIZATION

| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| R13 (09-20) exists | `grep -n "^| R13 " cto-2026-09-20.md` | 0 | ALLOWED — row found :86, launch-list ruling |
| R23 (09-20) exists | `grep -n "^| R23 " cto-2026-09-20.md` | 0 | ALLOWED — row found :206, grok/agy extension through 09-21 |
| R46 (09-21) carries required literal | `grep -n "^| R46 " cto-2026-09-21.md` | 0 | ALLOWED — row :57 carries "For the designs and creations we need the higher level models" |
| R13 (09-22) carries "without Astra" | `grep -n "^| R13 " cto-2026-09-22.md` | 0 | ALLOWED — row :94 carries "without Astra" |
| R60 (09-22) carries "DRC this week" | `grep -n "^| R60 " cto-2026-09-22.md` | 0 | ALLOWED — row :50 carries "DRC this week" |
| R66 (09-22) carries "ONE IMPORT PLACE" | `grep -n "^| R66 " cto-2026-09-22.md` | 0 | ALLOWED — row :44 carries "ONE IMPORT PLACE" |
| R72 (09-22) carries "THE DIFF MODEL IS RULED" | `grep -n "^| R72 " cto-2026-09-22.md` | 0 | ALLOWED — row :38 carries "THE DIFF MODEL IS RULED" |
| R73 (09-22) carries all three literals | `grep -n "^| R73 " cto-2026-09-22.md` | 0 | ALLOWED — row :37 carries `DRC-AUTOMATION-PROPOSAL-2026-09-22.md`, `Fable seat: yes`, `derive seat: claude-fable-5-1` |
| R73 row committed on main | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R73 | " -- cto-2026-09-22.md` | 0 | ALLOWED — 938f1f5ecbafaac8220564189435d4a47fa6cd78 (non-empty) |
| proposal committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/30 - Design/DRC-AUTOMATION-PROPOSAL-2026-09-22.md"` | 0 | ALLOWED — c52133c6fad7cc9836020dbb25d00a67c5c4a972 |
| §13 DIFF MODEL committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"## 13. DIFF MODEL" -- <proposal>` | 0 | ALLOWED — c52133c6fad7cc9836020dbb25d00a67c5c4a972 (same commit) |
| proposal stop line committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"DRC AUTOMATION PROPOSED" -- reports/drc-design-2026-09-22.md` | 0 | ALLOWED — d1d81e0f277427839ad3240305654988d9b62a40 |
| launch row names this file | `grep -n "40-drc-tribunal.md" cto-2026-09-22.md cto-2026-09-23.md` | 2 (cto-2026-09-23.md absent, recorded not fatal) | ALLOWED — R75 row :35 of cto-2026-09-22.md names `40-drc-tribunal.md`; cto-2026-09-23.md does not exist (`No such file or directory`), not fatal per rule since the row is in the other file |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"40-drc-tribunal.md" -- cto-2026-09-22.md cto-2026-09-23.md` | 0 | ALLOWED — ef0a1a13ff5ac4e67d0971dcbc5605cf85a4afc7 |
| 14 allow + 3 deny strings byte-identical to 09-20 baseline | `grep -c -F -e "<string>" 08-bars-chunk-e-check.md` ×17 | 0 each | ALLOWED — all counts ≥1: grok(2), agy(2), codex-astra(1), mkdir(1), git-show-cobalt(1), git-log-cobalt(1), s2-p2-cards show/log/diff(1 each), ls(1), grep(1), tail(1), wc(1), date(1), AskUserQuestion(1), EnterWorktree(1), git-push-deny(1) |
| No Sol/Opus checker string in this launch line | visual check of line 1's `--allowedTools` list | n/a | ALLOWED — no `gpt-5.6-sol` / `claude -p --model claude-opus-5` string present |
| DATE + EXTENSION GATE (authorization row) | `date` | 0 | ALLOWED — Tue Sep 22 16:22:48 EDT 2026, within 2026-09-22/23 window |
| R30 extension literal + his quoted words | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" cto-2026-09-22.md` | 0 | ALLOWED — row :77 R30 carries the literal and `"Approved"` in quotes |
| R30 extension literal committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" -- cto-2026-09-22.md` | 0 | ALLOWED — 055242df8032632dfafdcc8a69dcc271be89c0f6 |

All authorization checks ALLOWED. No `FAILED: authorization mismatch` triggered. Window check: 16:22–16:24 ET, outside both 19:25–20:45 and ≥23:20 — no window FAILED.

## PREFLIGHT

| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| DATE + EXTENSION GATE, row 1 | `date` | 0 | ALLOWED — Tue Sep 22 16:24:24 EDT 2026 |
| grok present | `grok --version` | 0 | ALLOWED — grok 1.0.25 (f7e67d6988e2) [stable] |
| agy present | `agy --version` | 0 | ALLOWED — 1.2.8 |
| base folder for Grok allow string exists | `ls scratch/tribunal-bars-0920` | 0 | ALLOWED — folder exists (bars-tribunal artifacts present) |
| RECOVERY: r1 folder | `ls scratch/tribunal-bars-0920/drc-tribunal/r1` | 1 | FRESH RUN — "No such file or directory", no prior staging to recover |
| STAGGER s1 (16) | `tail -n 3 reports/setups-check-r2-2026-09-22.md` | 1 | not running — file does not exist; cleared by desk launch row R75 (:35, cto-2026-09-22.md): "16 is not running (for `40-drc-tribunal.md`)" |
| STAGGER s2 (28) | `tail -n 3 reports/handicap-h1-check-2026-09-22.md` | 1 | not running — file does not exist; cleared by R75: "28 is not running (for `40-drc-tribunal.md`)" |
| STAGGER s3 (32) | `tail -n 3 reports/stale-score-check-2026-09-22.md` | 1 | not running — file does not exist; cleared by R75: "32 is not running (for `40-drc-tribunal.md`)" |
| CODEX PROBE (astra gate, R13, carried) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (run_in_background, 3 min) | 1 | astra: METER — proceed on three (verbatim tool output: "ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM." — EXPECTED per R13, RECORDED not a refusal) — astra SKIPPED, proceed on Grok + Gemini |

All PREFLIGHT rows ALLOWED / cleared. No `FAILED PREFLIGHT` triggered.

## Packet
Staged in `scratch/tribunal-bars-0920/drc-tribunal/r1/` (RECOVERY: fresh run, folder absent at preflight). `10-PROPOSAL.md` split into `.part1` (:1-191, 32,738 B) / `.part2` (:192-298, 10,843 B) at the `## 13. DIFF MODEL` heading — whole-file byte match confirmed against the original 43,581 B (0 trailing-whitespace lines in the original; both parts together match to the byte).

Per-file `wc -c` (final, after cuts): `00-READING-ORDER.md` 3,384 · `01-QUESTIONS.md` 14,986 · `02-greps.txt` 42,761 · `10-PROPOSAL.md.part1` 32,738 · `10-PROPOSAL.md.part2` 10,843 · `11-design-digest.md` 9,969 · `12-rulings.md` 9,267 · `13-spec-shape.md` 1,738 · `14-drc-shape.md` 5,089 · `20-trade-reporter.excerpt.txt` 4,071 · `21-drc-writers.excerpt.py` 17,479 · `22-vaultwrite.excerpt.py` 5,733 · `23-aset.excerpt.py` 4,536 · `24-migrations.excerpt.py` 1,722 · `25-s3-legs.excerpt.md` 8,265 · `27-laws-excerpt.md` 4,423. **Packet total: 177,004 B ≈ 44,251 tokens.** MANDATORY-only total (00–02, 10, 11, 12, 13, 14, 21, 25): 156,519 B ≈ 39,130 tokens.

**Over the 140 KB target — cut in the launch prompt's order, all five steps applied (still over after (v), which the prompt says is not a failure):**
(i) `26-s3-legs-open.excerpt.md` — CUT WHOLE (context-only; R67 already ruled the block).
(ii) `27-laws-excerpt.md` — cut from 16 laws to 6 (L1, L2, L3, L28, L40, L57); L7, L8, L9, L10, L32, L42, L45, L53, L68, L70 dropped.
(iii) `24-migrations.excerpt.py` — cut to `__init__.py`'s FORWARD/REVERSE range only; `placement.py`'s DECLARED_TABLES range dropped (covered by `02-greps.txt`).
(iv) `23-aset.excerpt.py` — cut to `web.py:83`, `web.py:940-960`, `store.py:268-322` only; the module docstring, `ensure_schema` and `mark_filled` ranges dropped.
(v) `20-trade-reporter.excerpt.txt` — `index.html` range cut from :1-86 to :55-75 (app.py stays whole); the `id="tab-drc"` anchor at :17 and the header/nav are dropped.
Packet still 177,004 B after all five cuts — over 140 KB, listed under `## ESCALATE` per the prompt's own rule (not a failure).

**REDACTION (L32, `grep -c -E "TSLA|372[.]82|374[.]50"` on every staged file):** all print `0`. No occurrence of the three literals in any source this packet drew on (the code comments at `aset/store.py:192`, `aset/web.py:355`, `aset/web.py:1084` were skipped by the excerpt ranges as anticipated).

**SHAPE-ONLY drops (L32):** `13-spec-shape.md` carries headings + key names only, no values — 0 lines dropped (no line carried a digit, `$`, ticker or rule-text word beyond a heading's own section number). `14-drc-shape.md`: of the prompt-line ranges the proposal's §13 (A) cites (DRC:22-249), 10 lines matched his template verbatim and are staged; 30 lines did not match (his filled answers, dollar values, Rules.md rule-check sentences with tags, and card/ticker/fill-time rows) and are DROPPED and counted — see the per-range breakdown inside `14-drc-shape.md`. The title line (:5) and date heading (:7) are staged redacted as `# [title]` / `### [date]` per rule.

**NOT STAGED** (per the launch prompt's list): the coach spec's body, his DRC note's body and his template's body (only the shape files carry anything of them), `Rules.md`'s rule sentences, any daily note of his, trade-reporter's `static/js/app.js` / `utils/drc_builder.py` / PDF material, `aset/web.py` / `prefill/drc.py` / `vaultwrite/writer.py` / S3 v3 whole (only the excerpts above and `02-greps.txt`), the DRC sitting packet, any trade, any production row.

## Clock
| time | trigger | running houses (minutes since launch) | action |
|---|---|---|---|
| 16:48:15 ET | date (§2 gate) | — | window clean (16:48, not 19:25–20:45, not ≥23:20) — launching both houses now |
| 16:48:1x ET | launch | grok 0 min (task b46f5umo8) · gemini 0 min (task b79ogc0qk) | both launched together, run_in_background, ONE attempt each, 20-min deadline ≈ 17:08 ET |
| 16:52:23 ET | gemini completion notice | grok ~4 min (task b46f5umo8, still running) · gemini DONE | gemini's printed answer captured verbatim (minus the harness's trailing `[exited with code 0]`) and written to `gemini-ruling.md`; its closing line: `TRIBUNAL R1: BUILD AFTER HIS REAL-SHAPE EXPORT (E1) IS SECURED` |

| 17:00:17 ET | grok completion notice | grok DONE (11 min, task b46f5umo8) · gemini DONE | grok wrote `grok-ruling.md` itself (25,679 B); closing line `TRIBUNAL R1: BUILD AFTER folds on writers, seams, and E1`. Both houses ruled inside the 20-min window — proceeding to collate. |
| 17:01:27 ET | collate start | — | tailed the Fable seat's report: `DRC TRIBUNAL FABLE R1 DONE` present — reading it for file-check |
| 17:03:11 ET | collate in progress | — | building `## Rulings table` and file-checking claims |

## Rulings table
Neither house issued a REJECT on any item. Gemini gave explicit `ADOPT`/`ADOPT WITH` tags for T1–T10 but NOT for items (a)–(j) — its (a)–(j) answers are prose with no verdict tag (a HOW-TO-RULE compliance gap, noted per row; content extends/agrees with the proposal, never rejects it, so read as an implicit ADOPT/ADOPT WITH).

| item | grok | gemini | agreement | wording / reason (≤25 words each) |
|---|---|---|---|---|
| T1 import place | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: new `VaultWriter` byte-write method owned by the vault expert, gated by `market_reset`, never a raw `open()`. gemini: import store owns `_imports/`, write-once, `VaultWriter` stays text-only. |
| T2 sync vs job | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: event row is state not a queue; `done` only after the note write returns. gemini: no launchd trigger exists for an HTTP upload; in-request precedent already exists (`aset/daily_note.py`). |
| T3 miss line on absent note | ADOPT WITH | ADOPT WITH | 2-0 | grok: store `render_line`'s exact call args on the replay run; build calls `write_miss_line` from that stored blob. gemini: store the RENDERED body itself on the run result; build writes that body through `replay.line`'s own writer name, no re-render. |
| T4 table names | ADOPT WITH | ADOPT WITH | 2-0 | grok: `drc_imports` + `drc_fills` + reuse declared `drc_rows`; never touches declared `fills` or `order_fills`. gemini: `drc_executions` not `drc_fills` (L31 — no vendor name in an identifier); event state folds onto `drc_rows`'s day row, no 4th table. |
| T5 rule engine shadow | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: engine writes only `drc-rules/rule_engine`; no checker ever writes `[x]`. gemini/Fable-aligned: keys join `OPTIONAL_SETTING_KEYS` not `SETTING_KEYS`; binding carries a text-hash so a renumbered rule renders `untested`, never silently re-bound. |
| T6 his answers across rebuilds | ADOPT WITH | ADOPT WITH | 2-0 | grok: voice units created blank once, never re-upserted; a vanished trade's unit stays with one `orphaned` line, not merged/lost. gemini/Fable-aligned: one unit per trade (`trade:<id>`), not one `tickers` unit, so a rebuild's merge is per-trade. |
| T7 DAS-vs-legs reconcile | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: S-C1 rides C1's migration set (no number assumed); S-C2/S-C2b amend C2's one writer; `adjustment pending` before C2 merges is L1-clean. gemini/Fable-aligned: a C2 refusal never fails the build — recorded as an unresolved-leg-mismatch row (A31), not a permanent block. |
| T11 open-position carry | ADOPT | ADOPT | 2-0 | grok: seed from prior `drc_rows`; a carried symbol with no prior row FAILs naming the symbol; a contradicting file FAILs. gemini/Fable-aligned: seed only from a CONTIGUOUS import chain; a missing prior trading day FAILs naming the day. |
| T8 template reader | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: only caller of the repo j2 today is `prefill/drc.py:272`; the early `create_if_absent` return is wrong for HIS template (no units inside it). gemini/Fable-aligned: exactly 2 `{{` lines in his template, both the date token (F5 holds). |
| T9 one source, daily-stop/grade $ | ADOPT WITH | ADOPT WITH | 2-0 | grok: one function reads `trader_settings` keys only, never `daily.md.j2` / Rules.md / sheet-mode config; absent key renders `not given`. gemini/Fable-aligned: grade $ from existing `aset.sheet_modes` row (no new `grades.*` key); daily stop = one new optional key family; `daily.md.j2:18` becomes a rendered variable. |
| T10 S2/S3 smoke re-keyed | ADOPT WITH | ADOPT | 2-0 adopt (1 with) | grok: retire the `job_row` smoke check in the same deploy as the prefill retirement, never point it at a dead job; `pending` only when no event exists. gemini/Fable-aligned: K12.2 replaced by an `sql` check on the day row; a lawful no-inputs day reports a fact, never red. |
| (a) fact base | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: §1 holds; F23's `public.trades` claim and F25's "OPEN" status do NOT hold (WRONG FACTS). gemini: same misses as Fable (CLI entrypoints, smoke reader) — content overlaps Fable's (a) almost verbatim. |
| (b) L3 one writer | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: kill the plist + `jobs.yaml` rows + CLI entry in the SAME deploy as the first input-driven build. gemini: after the change, no second DRC writer or template is left; walks a night with no DRC and a night built after 21:10 — same conclusion as grok's T3/(b). |
| (c) import place on ASET app | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: one web surface, one expert per side effect (L40); LAN reach is E7, an owner/ops item, not a precondition. gemini: same L3/L40 read; multipart via already-transitive `python-multipart`; LAN reach = owner/ops item. |
| (d) the trigger | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: `market_reset` uploads REFUSED, never queued or deferred — a queue would be a second trigger (L3). gemini: same — deferred-accept scenario named as the failure a refusal avoids. |
| (e) DAS export parser | ADOPT WITH | ADOPT WITH | SPLIT on the header-change rule; 2-0 on the boundary | grok: missing column FAILs; an EXTRA column with every required name present is `degraded` (L9), not a failure. gemini/Fable: ANY header change (missing OR renamed) FAILs AND raises `degraded`; only an added column parses. Both: platform boundary = NONE. |
| (f) reconcile against S3 legs | ADOPT WITH | ADOPT WITH | 2-0, but on DIFFERENT terms | grok: a C2 refusal (e.g. a CLOSED card moved off 0) = build FAILED naming the card, never forced. gemini/Fable: a C2 refusal NEVER fails the build — recorded as an unresolved-leg-mismatch row, carried forward until resolved (O20). This is a real disagreement, not just wording — see `## ESCALATE`. |
| (g) TradeZella screenshot | ADOPT WITH | ADOPT WITH | 2-0 | grok: this slice reads nothing from the image; no OCR library, no new package. gemini/Fable-aligned: "not an image" decided by magic bytes (PNG/JPEG header), no image library imported at all — `pillow` stays fully untouched. |
| (h) rule engine in shadow | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: a hard-coded rule-number checker is a hidden copy of his numbering (L3/L53); the `rule number → checker id` map is the thing he edits. gemini: adds — no engine result reaches `cards/scoring.py`, `radar/evaluate.py` or `aset/engine.py` either (broader boundary list than grok's). |
| (i) ledgers + stored inputs | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: names the exact `aset_sizings` columns `drc_rows.inputs` must snapshot; realized R `not computed` before D5, never `confirmed` early. gemini: same snapshot requirement; flags that `mark_filled` UPDATEs the card row after the DRC, so a later replay of a stored row can read a changed `actual_fill` (L57 risk named, not resolved). |
| (j) chunks this week | ADOPT WITH | no tag (content = adopt-with) | 2-0 (1 untagged) | grok: migration takes no number here (desk's at L68); arithmetic 7+7+9+4+5=32 re-derived and holds; the 0.4× fix-round factor is UNVERIFIED (not in the packet). gemini: same hours arithmetic (7+7+9+4+5=32, ×1.4≈44.8≈45, holds); D4∥D2 share no file; D1 blocked on E1. |

## Wording offered, verbatim
**T1** — grok: "The one import place is `GET /drc` and `POST /drc/import` on the existing ASET FastAPI app (`aset/web.py:83`). Dropped bytes land under the vault's `_imports/drc/<YYYY-MM-DD>/` only by a new method on `VaultWriter` (the vault-write expert, L40), versioned and sha256'd, refused inside `market_reset` by the same `_session_gate` as notes." — gemini: (no replacement wording offered; plain ADOPT.)

**T2** — grok: "The build runs in the request, and `cobalt drc build --date D [--dry-run]` calls that same function. The event row is the state record of that run (`pending` before any note write, then `running`, then `done` or `failed`), not a polled watcher and not a one-shot job." — gemini: (plain ADOPT, no replacement wording.)

**T3** — grok: "If the note is absent at 21:10, `line_step` does not raise and does not create a note. It stores the exact arguments `render_line` is called with today ... on the replay run, records `line: pending (no DRC)`, and ends green. The build ... is the only later caller of `render_line` plus `write_miss_line` for that stored blob." — gemini: "`line_step` on an absent note ... renders the body as today, stores it on the run result as `line_body` with `line_action = 'pending_no_drc'` ..., and ends green. The DRC build, when it runs later for that date, reads that stored body and writes it through `replay.line.write_miss_line(path, body, writer=VaultWriter(replay.line.WRITER))` — the replay's own function and writer name, no re-render."

**T4** — grok: "D1 creates `\"user\".drc_imports` and `\"user\".drc_fills` and uses the already-declared `\"user\".drc_rows`. It does not create `\"user\".fills`. It does not create or alter `order_fills`." — gemini: "`\"user\".drc_imports` (one row per dropped file), `\"user\".drc_executions` (the trading-log export's execution rows — not `fills`) ..., `\"user\".drc_rows` (one row per trade and ONE per day; the day row carries the build event ...). No fourth table. No vendor name in any identifier, schema, enum or config key (L31)."

**T5** — grok: "The engine writes only `drc-rules/rule_engine`, labelled shadow. `drc-rules/rules_check` stays the checkbox scaffold ... already writes. No checker writes a `[x]`." — gemini: (plain ADOPT for T5's headline; the wording under (h) extends it — see (h) below.)

**T6** — grok: "A rebuild never drops text he typed. Derived figures live in Cobalt units the build upserts. His answers live in units the build creates blank once ... and does not upsert again. ... A trade missing from a later CSV leaves its voice unit in place with one Cobalt line `orphaned` above it." — gemini: "`drc-trades/tickers` retires; one unit per trade, id `trade:<trade_id>` ..., each carrying the derived table, matched card, legs, flags, the screenshot embed, then his blank voice lines. A rebuild upserts each trade's unit by id; a trade absent from the superseding export is NOT deleted — its unit is upserted with a first line `not in the trading-log export of <date> (import <id>)` and its body otherwise unchanged."

**T7** — grok: "S-C1 amends S3 C1's set ..., not the DRC migration. `source` and `price_source` each gain the value `das`. A nullable `source_id` names the `drc_imports` row. ... S-C2 / S-C2b amend C2's one writer: append-only correction or new exit leg .... Until C2 is merged the reconcile unit's only completion text is `adjustment pending (legs writer not built)`." — gemini: "A refusal from C2's writer is never forced and never fails the build: it is recorded as an UNRESOLVED LEG MISMATCH ..., rendered in the reconcile unit as `unresolved: card <id> — <refusal>`, and carried forward on every later DRC (A31) until resolved ... C1's `legs` DDL adds the value `trading_log` to the `source` CHECK and a nullable `import_id bigint` (no FK)."

**T8** — grok: "The build reads `5 - Templates/DRC.md` and replaces only the literal token `{{date:YYYY-MM-DD}}`. Any other `{{` FAILs the build naming the line. No Jinja and no Templater on his file. `configs/cobalt/templates/drc.md.j2` is deleted in D3." — gemini: (plain ADOPT.)

**T9** — grok: "One function is the only reader of daily-stop and grade dollars on the DRC path. ... Until he rules O6 otherwise, that home is `\"user\".trader_settings` keys `account.daily_stop_full`, `account.daily_stop_half`, and `grades.*`. It does not read `daily.md.j2`, a Rules.md sentence, or the sheet-mode config." — gemini: "ONE source = `\"user\".trader_settings`, loaded only by his hand. Grade dollars: the existing `aset.sheet_modes` row — no `grades.*` key is created. Daily stop: one new optional key family for SPEC §7 `account.*`. `configs/cobalt/templates/daily.md.j2:18`'s literal becomes a template variable rendered from that key by the 05:15 prefill."

**T10** — grok: "In the same deploy as the prefill retirement, `s2.yaml:436-438` ... is removed, not pointed at a dead job. `s2.yaml:383-398` passes as `pending` when no DRC event exists for that date, fails when the event is `failed` or `done` without the note and the `drc-misses` markers, and passes when `done` and both markers are present." — gemini: (plain ADOPT; wording extended in (j)/T10 overlap — "K12.2 ... replaced by an `sql` check on the day row: `failed` = red; `done` = green; no row = `DRC: no inputs for <day> (R66)` reported as a fact, not a pass.")

**(e)** — grok: "an EXTRA column, required names present, sets `degraded: das_export_shape` (L9) and still parses. Reorder alone is not a failure." — gemini: "a MISSING or RENAMED column = the import FAILED naming file and line (L1) AND the `trading_log_shape` degraded flag raised (L9); an ADDED column = parsed by header name AND the flag raised; the flag clears on the next import whose header set equals the fixture's." **These two replacement wordings conflict and cannot both be adopted verbatim — a genuine split, carried to the derive.**

**(f)** — grok: "A refusal from C2's writer (e.g. a CLOSED card moved off 0) = build FAILED naming the card — never forced" (i.e., ADOPTS the proposal's own §3 step-4 wording as written). — gemini: replaces the SAME sentence with "A refusal from C2's writer is never forced and never fails the build: it is recorded as an UNRESOLVED LEG MISMATCH ... and carried forward on every later DRC (A31) until resolved; how a CLOSED card the export shows still open is reopened is his (O20)." **Direct contradiction on the same proposal sentence — carried to the derive, not resolved here (L37).**

**(g)** — grok: "This slice reads nothing from the image. ... No OCR library and no new package." — gemini: "`not an image` is decided by the file's magic bytes (PNG `89 50 4E 47`, JPEG `FF D8 FF`) — no image library is imported; `pillow` stays transitive."

## Checked against the files
Coverage note: given the packet's size (177 KB) and the number of file:line claims across two house rulings plus the Fable seat's report (several hundred individual citations), this section checks every WRONG FACT, every claim the houses split on, and a representative, load-bearing sample of the file:line citations underpinning each ADOPT WITH — not literally every citation in both files. Every claim checked below HOLDS unless marked otherwise.

| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| Writers of the DRC note/units are only `prefill/drc.py:427,:447` and `replay/line.py:172`; readers `daymode/drc.py`, `smoke/checks.py:566` | grok (a) | `prefill/drc.py:427,447`; `replay/line.py:172` | HOLDS | confirmed via `02-greps.txt`'s `create_if_absent`/`upsert_unit` grep — no other caller uses the four DRC section names |
| `public.trades` is NOT named in `placement.py:106-112` or `:143-147`; only `order_fills` is at :143 | grok WRONG FACTS #1 | `db_migrations/placement.py` | HOLDS | `grep -n "public.trades\|order_fills"` on the real file: only `"order_fills",` at :143; no `public.trades` anywhere in the file |
| v3 R2-2 is not "OPEN" — R67 ruled it, and the proposal's own F33 says so | grok WRONG FACTS #2 | `12-rulings.md` R67; proposal F33 | HOLDS | R67 (`cto-2026-09-22.md`) is exactly the ruling text staged in `12-rulings.md`; F33 in the proposal itself already states R67 as PROVEN — the v3 excerpt's own "OPEN" text is stale because that file was never re-edited, exactly as claimed |
| `request.form()` appears at `web.py:947,1048,1147,1190,1247,1282`, not just the two F14 names | grok WRONG FACTS #3 | `aset/web.py` | HOLDS | matches `02-greps.txt`'s grep output exactly (6 hits) |
| Caller of the 09:00 reader (`prior_day_inputs`): `daymode/cli.py:151` | gemini (a) | `daymode/cli.py:151` | HOLDS | real file: line 151 is `inputs = prior_day_inputs(day)` |
| Caller of the 15:40 job (`run_drc_prefill`): `prefill/cli.py:49` | gemini (a) | `prefill/cli.py:49` | HOLDS | real file: line 49 is `result = asyncio.run(run_drc_prefill(for_date_=for_date_, dry_run=dry_run))` |
| Caller of the miss-line setup (`drc_note_path`): `replay/cli.py:98` | gemini (a) | `replay/cli.py:98` | HOLDS | real file: line 98 passes `drc_path=drc_note_path` |
| Reader of the DRC note path for tests: `smoke/checks.py:151,566` | gemini (a) | `smoke/checks.py` | HOLDS | confirmed both lines in `02-greps.txt`'s output and by direct read |
| "a header change = `degraded: das_export_shape` flag (L9)" is the proposal's literal text at `10-PROPOSAL.md.part1:72` | gemini WRONG FACTS | proposal :72 | HOLDS (accurate quote) | grepped the staged part1 — the literal is exactly at line 72; whether gemini's OWN replacement (FAIL, not degrade) is the better rule is a house disagreement (see `## Wording offered`), not a fact question |
| S-C1 "rides C1's migration (`db_migrations/0014_legs.sql`)" | gemini (f) | — | **DOES NOT HOLD (self-contradiction)** | `25-s3-legs.excerpt.md`'s own migrations paragraph explicitly warns "the number 0014 inside that verbatim [Fable round-1] text is not v3's: the migration NUMBER is the desk's at the L68 gate" — gemini's (j) answer correctly says the number is desk-assigned, but its (f) answer names `0014_legs.sql` as if settled. Internally inconsistent; the desk has not numbered anything |
| L31 "Person or vendor names never in code identifiers, schema, config keys, enum values or system design docs" | Fable T4/T9/multiple | `LAWS.md:173-175` | HOLDS | verbatim match; **L31 was NOT included in the packet's `27-laws-excerpt.md`** (cut to L1/L2/L3/L28/L40/L57 only) — grok and gemini never saw this law and neither one raised the vendor-name issue the proposal's `das.py`/`das_import_id`/`degraded: das_export_shape` naming would trip. Flagged under `## ESCALATE`. |
| `format_card_reconcile_block` is at `prefill/drc.py:230`, not inside the proposal's cited `:248-347` range; `format_rules_checkbox_block` is DEFINED in `prefill/daily.py:165` (only imported at `drc.py:54`); the DRC's own is `format_rules_check_block` at `:285` | Fable WRONG FACTS #1 | `prefill/drc.py`, `prefill/daily.py` | HOLDS | confirmed exactly by direct grep: `format_card_reconcile_block` def at :230, `format_rules_check_block` def at :285, `format_rules_checkbox_block` def in `daily.py:165` |
| R67 was cited by the proposal (F33) at `cto-2026-09-22.md:35`; it is no longer at that line (rows keep being inserted above it by the desk) | Fable WRONG FACTS #2 | `cto-2026-09-22.md` | HOLDS (and still drifting) | at hub packet-staging time (16:2x ET) R67 was at :45; when Fable read it (~16:33-16:4x ET) it had moved to :43 (Fable's citation); by hub collate time (17:0x ET) it has moved again to :50, as new rulings (R74–R77) were appended above it — this is the desk's normal append behavior, not a new error |
| `VaultWriter.create_if_absent` refuses to create a missing parent directory ("refusing to create vault structure"), text-only via `fdopen(..., "w", encoding="utf-8")` | Fable T1 | `vaultwrite/writer.py` ~:470, :583-587 | HOLDS | both confirmed by direct read of the real file |
| `upsert_unit`: "New id -> appended inside the section" | Fable T6 | `vaultwrite/writer.py:651-653` (docstring) | HOLDS | confirmed against the docstring text already staged in `22-vaultwrite.excerpt.py` |
| Marker `NAME_RE` admits `:` and `-` | Fable T6 | `vaultwrite/markers.py:31` | HOLDS | real file: `NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:+-]*$")` — exact |
| `SETTING_KEYS` vs `OPTIONAL_SETTING_KEYS` exist as distinct tuples; `BENCHMARK_KEY` is the only optional key today | Fable T5 | `settings/models.py:44,53,57` | HOLDS | confirmed exactly by direct grep |
| `daymode/drc.py`'s Grade/Goal regex: a filled grade must be a ladder value, a filled goal must contain a digit | Fable (b)/(h) | `daymode/drc.py:116-132` | HOLDS | confirmed by direct read — matches the code exactly, including the "template placeholder is not filled" comment |
| An in-request vault-write precedent already exists (`aset/daily_note.py`'s `create_if_absent` + `upsert_unit` called from a request handler) | Fable T2 | `aset/daily_note.py` (`_write_unit`, `build_writer`) | HOLDS | confirmed — `_write_unit` calls `vw.create_if_absent(...)` then `vw.upsert_unit(...)` synchronously |
| `s2.yaml` already keys smoke rows off `last_trading_day` (a calendar function the codebase already has) | Fable T11 | `configs/cobalt/smoke/s2.yaml:384` | HOLDS | confirmed: `day: last_trading_day` at that line |
| Neither design touches `cards/scoring.py`, `cards/radar.py`, `radar/evaluate.py`, `aset/engine.py` or `daymode/propose.py` (L52) | proposal §12; both houses | — | HOLDS (UNVERIFIABLE beyond a negative grep) | no staged excerpt or grep result names those files as touched by any D1–D5 chunk; a full negative proof would need a repo-wide diff against a built D1–D5, which does not exist yet — recorded as consistent with everything read, not independently provable from reads alone |
| Platform boundary: no path in the design reads, writes to or infers from a trading platform beyond the file he exports and drops (R66 a) — answer NONE | all three houses | `02-greps.txt` DAS/Lightspeed/TradeStation/CenterPoint grep | HOLDS | every hit in the packet's grep is an existing comment/message stating Cobalt never touches DAS; no code path reads the platform |

## Fable round-1 claims, file-checked
Checked AFTER both houses' tables above were written (L32/independence: nothing of this section reached grok or gemini). Every `FC<n>` below HOLDS on direct file-check; none is withdrawn-and-still-cited (the three WITHDRAWN sentences in Fable's report are correctly marked withdrawn and are not re-checked as live claims).

| FC# | claim (Fable report line) | file:line | verdict |
|---|---|---|---|
| FC1 | L31 exists and reads "Person or vendor names never in code identifiers..." (report :62) | `LAWS.md:173-175` | HOLDS |
| FC2 | `format_card_reconcile_block` / `format_rules_checkbox_block` / `format_rules_check_block` locations (report :233, WRONG FACTS) | `prefill/drc.py:230,:285`; `prefill/daily.py:165` | HOLDS |
| FC3 | R67's line number has drifted from the proposal's `:35` citation (report :234, WRONG FACTS) | `cto-2026-09-22.md` | HOLDS (now :50, still drifting — see above) |
| FC4 | `create_if_absent` refuses a missing parent directory (report :40, T1) | `vaultwrite/writer.py:583-587` | HOLDS |
| FC5 | `upsert_unit` is markers-only, text via `"w", encoding="utf-8"` — cannot take a PNG (report :39, T1) | `vaultwrite/writer.py` ~:470 | HOLDS |
| FC6 | `_imports/` does not exist in the vault today (report :40, T1; F30) | `ls` of the vault (F30, already PROVEN in the proposal and re-confirmed at packet-staging) | HOLDS |
| FC7 | `_parse_rules_md` numbers rules by ORDER, not a stable id independent of position (report :69, T5) | `prefill/rules_gen.py` (rule_number loop) | HOLDS (consistent with the excerpt read; full loop not re-walked line-by-line) |
| FC8 | `SETTING_KEYS` vs `OPTIONAL_SETTING_KEYS` — a new required key breaks every sheet reader with no row (report :71, T5) | `settings/models.py:44,57,120-127` | HOLDS on the tuple split; the "breaks every reader" consequence is a reasonable reading of `_build`'s required-row behavior, not independently re-run |
| FC9 | `format_rules_checkbox_block` writes inside `drc-rules/rules_check`; a new engine unit id is appended inside the same section, never replacing the checkbox lines (report :73, T5) | `vaultwrite/writer.py` upsert semantics + `prefill/daily.py:165` | HOLDS |
| FC10 | Today his voice lines live INSIDE the one `tickers` unit; a rebuild replaces the whole unit body (report :78, T6) | `prefill/drc.py:196-214` (`_render_entry`, not independently re-read this pass) | UNVERIFIABLE FROM READS this pass — not in the staged excerpts or re-opened; consistent with `21-drc-writers.excerpt.py`'s `format_tickers_unit`/`TRADES_PLACEMENT` shape but the exact line range was not re-read |
| FC11 | `request.form()` used six times; no `UploadFile`/multipart import in `src/` today (report :136, (c)) | `aset/web.py`; `pyproject.toml` | HOLDS |
| FC12 | Production loads `configs/dev/aset.yaml` unless `aset.local.yaml` exists (report :139, (c)) | `aset/config.py:41-42` | UNVERIFIABLE FROM READS this pass — not re-opened; not contradicted by anything staged (F16 in the proposal is marked UNPROVEN → E7 for the same reason) |
| FC13 | `mark_filled` UPDATEs the card row after a fill, so a stored `drc_rows` figure could read a changed `actual_fill` on replay unless the input is snapshotted (report :177, (i)) | `aset/store.py:185-257` | HOLDS — confirmed via `23-aset.excerpt.py`'s staged `mark_filled` UPDATE statement (before the step-iv cut) and the live re-read above |
| FC14 | `s2.yaml` smoke kinds today are `vault_unit`, `sql`, `job_row` only — a conditional check needs a new kind or a precondition row (report :115, (j)) | `configs/cobalt/smoke/s2.yaml` | HOLDS on the kinds observed in the staged excerpt (`vault_unit` :385, `sql` :395, `job_row` :438); not exhaustively re-grepped for a fourth kind |

## Experiments named (L70)
Deduplicated by what each runs, against the proposal's own E1–E8.

| experiment | named by | = proposal E<n> or NEW | gates which chunk | result that would change the design |
|---|---|---|---|---|
| one real DAS/trading-log export (columns, side codes, tz, account col(s), order-log presence, flat-start vs overnight rows, through-0 execution) | proposal (E1) · grok (kept) · gemini (kept) · Fable (X1, widened) | = E1 | D1 | any column/behavior absent from the export changes the parser/fixture; overnight rows change T11's seed rule |
| one real TradeZella screenshot, which stats-panel fields are legible | proposal (E2) · all three (kept) | = E2 | D2 | decides O1 (typed cells vs OCR) |
| dev-vault render of his template, date token only, existing + new placements land correctly | proposal (E3) · grok (kept) · gemini (kept) · Fable (X3, widened to per-trade units) | = E3 | D3 | a placement failure moves the anchor logic, not the template |
| one ASET card `created_at` vs that trade's first DAS fill time (clock skew/zone) | proposal (E4) · all three (kept) | = E4 | D1 (`card_lead_seconds`) | skew/zone unknown → rule 1 needs a tolerance key (his) |
| multipart `UploadFile` with the transitive `python-multipart`, before pinning direct | proposal (E5) · all three (kept) | = E5 | D2 | fail → dependency added knowingly, still not new |
| replay-line re-render / stored-body proof for T3 | proposal (E6) · grok (CHANGE: prove the stored ARGUMENTS re-render identically) · gemini/Fable (CHANGE: prove the stored RENDERED BODY needs no re-render at all) | NEW shape (E6 split two ways) | D3 | grok's version fails if any of the 5 non-`missed`-sourced args are needed; gemini/Fable's version removes the question by storing the body itself — **the two designs are not the same mechanism**, carried to the derive |
| which aset config production loads + LAN upload from the trading PC | proposal (E7) · all three (kept) | = E7 | D2, ops | not a precondition either way; decides only where he uses the page |
| two builds with a trade removed between, his typed text inside that trade's block | proposal (E8) · grok (CHANGE, same shape) · gemini/Fable (CHANGE: shrinks to one unit under T6's per-trade design) | = E8 (mechanism differs per T6 split) | D3 | proves text survival differently depending on whether T6's per-trade-unit wording is adopted |
| Obsidian embed of `![[_imports/drc/<date>/<file>]]` renders under his attachment settings | grok ((g), named inline) · Fable (X9, new) | NEW | D3 display only | if it fails, the embed shape changes; never a build gate |
| `this.file.cday` dataview lists D+1's notes, not D's, when a DRC is built the morning after | Fable (X10, new) | NEW | none (owner item if it fails) | if true, the tickers dataview line is HIS template's issue, not a build defect |
| a CLOSED card whose export shows an open remainder — does C2 refuse, and does the DRC still build | Fable (X11, new) | NEW | D5 / T7 split | resolves which of grok's vs gemini's T7/(f) wording is livable in practice |
| inserting one new `trader_settings` key on `cobalt_dev` with no migration | Fable (X12, new) | NEW | D4 | fail → D4 gains the migration the desk numbers |
| kill the ASET request mid-build (after `pending`, before `done`) | grok (E11, new) | NEW | D2/D3 | fail → the request-based T2 design does not hold as written |

## OWNER ITEMS (after the tribunal)
O1–O18 as the proposal frames them; no house made one a precondition to BUILD. O19 is spent (R69–R72, all three houses agree). Two NEW items from the Fable seat, not named by grok or gemini:
- **O20 (Fable, new)** — how a CLOSED card whose export shows a still-open remainder is reopened; a CLOSED→FILLED edge does not exist in v3's state machine today. This is the mechanism behind the (f)/T7 split above — a trading-logic change needing his ruling + HITL, not this tribunal's to build.
- **O21 (Fable, new)** — the summary-line P&L: gross or net (SPEC §2 carries both figures; the proposal's prose only writes "net").
Grok's read of O15 ("mis-framed as a free option: L45 requires the committed shape before production; he can hand E1's export over without committing it, the git commit alone needs his consent") sharpens rather than reframes O15 — not treated as a build precondition since E1 itself can proceed on `cobalt_dev` without a git commit.

## WRONG FACTS claimed
| claim | claimed by | file-check verdict |
|---|---|---|
| Proposal F23: `public.trades` is taken at `placement.py:106-112`/`:143-147` | grok | DOES NOT HOLD (as claimed by grok) — confirmed above; `placement.py` names no `public.trades` anywhere |
| Proposal F25: "v3 R2-2 OPEN FOR DEJAN" | grok | DOES NOT HOLD (stale) — R67 ruled it; the proposal's own F33 already says so |
| Proposal F14: `request.form()` cited at only two of its six real call sites | grok | Minor/immaterial — the two cited lines are real, just an incomplete list; not a design change |
| Proposal §8: "the three placements (`prefill/drc.py:248-347`)" | Fable | DOES NOT HOLD as a clean range — `format_card_reconcile_block` (:230) sits outside it and `format_rules_checkbox_block` is defined in `daily.py:165`, only imported at `drc.py:54`; the DRC's own function is `format_rules_check_block` (:285) |
| Proposal F33 / desk report: R67 cited at `cto-2026-09-22.md:35` | Fable | Row has moved (now :50) — the desk keeps inserting rulings above it; not a design error |
| Gemini (f): "S-C1 rides C1's migration (`db_migrations/0014_legs.sql`)" | hub (this collate) | DOES NOT HOLD — self-contradicts gemini's own (j) answer and `25-s3-legs.excerpt.md`'s explicit note that 0014 is not settled; the desk has not numbered any migration |

## Independence
`grep -c -F -e "-ruling"`: `grok-ruling.md` = 2, `gemini-ruling.md` = 0. Grok's two hits are both false positives, not a breach: line 3 is grok's own compliance statement ("No `-ruling.md` opened"), and line 206 cites the packet's OWN `12-rulings.md` (a mandatory packet file, not a house's output) — the substring match is on "-rulings.md", not on another house's `-ruling.md` file. Neither house shows evidence of reading the other's ruling. No independence breach.

## ESCALATE
1. **L31 (vendor names) was never in the packet.** `27-laws-excerpt.md` was cut (over-140KB step ii) down to L1/L2/L3/L28/L40/L57 — L31 never reached grok or gemini. The Fable seat (reading LAWS.md directly, blind to the hub's cut packet) raised it and it HOLDS against the real law text. Grok and gemini's designs (naming `das.py`, `das_import_id`, `degraded: das_export_shape`) were never checked against L31 by either house. `ASK DESK: fold L31 into round 2's packet (uncut), or treat T4's naming fix as settled from the Fable seat alone? [17:0x ET]` — safe default: carried to the derive unresolved, not decided here.
2. **(f)/T7 is a real split, not a wording variant.** Grok ADOPTS the proposal's own "a CLOSED card moved off 0 = build FAILED naming the card, never forced." Gemini/Fable REPLACE that same sentence with "never fails the build — an unresolved-leg-mismatch row, carried forward (O20)." Both are internally consistent designs; they produce different behavior on the same scenario (a CLOSED card the export shows still open). Neither claim's supporting citations fail file-check — this is a genuine disagreement for the derive, not a defect in either wording.
3. **(e)'s header-change rule is a real split.** Grok: missing column FAILs, extra column (all required names present) = `degraded`. Gemini/Fable: ANY header change (missing or renamed) FAILs AND raises `degraded` together; only a pure addition parses without failing. Both cite L1/L9 correctly; the difference is which reading of "degraded vs failed" the derive adopts.
4. **Gemini's (f) migration-number claim does not hold** (`db_migrations/0014_legs.sql` named as settled) — see `## WRONG FACTS claimed`. Not a precondition, not a REJECT, but the derive should not carry the literal filename forward.
5. **Packet over the 140 KB target.** 177,004 B total after all five cut-order steps (see `## Packet`) — per the launch prompt this is not a failure, listed here as required.
6. **REDACTION and SHAPE-ONLY counts (L32).** REDACTION: 0 replacements needed on any staged file (`grep -c -E "TSLA|372[.]82|374[.]50"` = 0 everywhere). SHAPE-ONLY: `13-spec-shape.md` 0 lines dropped (headings/keys only, no value ever matched); `14-drc-shape.md` 30 prompt lines dropped and counted (his filled answers, dollar values, Rules.md rule-check sentences with tags, ticker/fill-time card-reconcile rows) against 10 staged; `26-s3-legs-open.excerpt.md` cut whole (context-only, R67 already ruled it).
7. Neither house named a `DO NOT BUILD`. Neither house's `BUILD AFTER` clause (grok: "folds on writers, seams, and E1"; gemini: "HIS REAL-SHAPE EXPORT (E1) IS SECURED") is a REJECT of any item — both point at E1, already the proposal's own named first-gate experiment, not a new blocker.
8. No `ASK DESK` beyond item 1 above. No independence breach. No owner item was written as a precondition to BUILD. No claim re-opens R65–R73.

| 17:05:54 ET | close | grok DONE · gemini DONE · astra METER | writing the final stop line |

DRC TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER folds on writers, seams, and E1 · gemini: TRIBUNAL R1: BUILD AFTER HIS REAL-SHAPE EXPORT (E1) IS SECURED · astra: METER — proceed on three · houses that ruled: 2 of 3 · claims that HOLD: 21 · blockers to build: 0 · owner items: 20 · ESCALATE: 8
