# DRC OVERNIGHT TRIBUNAL — ROUND 2 (hub `drc-overnight-tribunal-r2-0924`, Sonnet 5)

## §0 Headline
- Ruled: Grok `TRIBUNAL R2: BUILD AFTER fold this paste before the K1 migration` · Gemini `TRIBUNAL R2: BUILD` · Astra `METER` (back Sep 26th, 2026 6:47 AM). 2 of 3 houses ruled; neither timed out.
- R2-1: (i) and (ii) 2-0 `ADOPT seat`; (iii) SPLIT — Grok ADOPT WITH (fills from the newest un-superseded import, stored `stats_row` rows re-matched) vs Gemini ADOPT seat. R2-2: (b), (c) 2-0 same mechanism; (a) SPLIT on the literal — Grok `state_book_cli` vs Gemini `cli`. **Items converged: 0 of 2.** Owner items: 0.
- The Anthropic seat's round-2 report is DONE and file-checked AFTER the houses: it WITHDREW the text both houses adopted for (ii) and the `day`-row import ids Gemini adopted for (iii) (quoted under ESCALATE 3).
- Checked: Anthropic-seat R1 Q3 claims 8 HOLD of 8 · seat R2 claims 20 HOLD of 22 (2 UNVERIFIABLE FROM READS, 0 DO NOT HOLD) · house claims 25 HOLD of 29 (4 UNVERIFIABLE, 0 DO NOT HOLD). Redactions: 0 (packet 120,865 B, no cut). ESCALATE: 5. No write path; nothing committed by me.

## AUTHORIZATION
Verified by me, each its own Bash call, 2026-09-24 (first `date` 12:13:02 EDT):

| Proof | Result |
|---|---|
| `^\| R13 ` `cto-2026-09-20.md` | line 86 present (his 13:33 ET "Push and approved everything…", the rule list) |
| `^\| R109 ` `cto-2026-09-22.md` | line 56, carries `Make all Opus 5.5 for now` |
| `^\| R67 ` `cto-2026-09-22.md` | line 99, carries `continuing position` |
| `^\| R19 ` `cto-2026-09-24.md` (THE GROK / AGY GATE, row 2) | line 29, carries `All 4 house models approved for use indefinlitly` |
| `^\| R22 ` `cto-2026-09-24.md` | line 32, carries `We need to design the lane` |
| `git log -1 -S"All 4 house models approved"` (cto-2026-09-24.md) | `5055151dbf68899b82de5b11f99733ed2d03048c` — R19 committed |
| `git log -1 -S"DRC OVERNIGHT DERIVED v2"` (derive report) | `e9652bdbcecfeebe988e8887fea5a08317ac84ba` — committed |
| `git log -1 -- DRC-OVERNIGHT-POSITION-v2-2026-09-24.md` | `e9652bdbcecfeebe988e8887fea5a08317ac84ba` — v2 committed |
| `tail -n 3` derive report | last non-blank line `DRC OVERNIGHT DERIVED v2 · folds: 26 · verbatim: 19 · needs round 2: 1 · owner items: 0 · ESCALATE: 9` — starts `DRC OVERNIGHT DERIVED v2 `, carries `needs round 2: 1` |
| launch row naming `27-drc-overnight-tribunal-r2.md` | `cto-2026-09-24.md` line 54, **R44** (12:12 ET): carries `Fable seat: yes` and `derive seat: claude-opus-5-5`. (Lines 48 = R38 and 50 = R40 also name the file — drafting records, not the launch row.) `cto-2026-09-25.md` does not exist — recorded, not fatal (the row is in the other file) |
| `git log -1 -S"27-drc-overnight-tribunal-r2.md"` (the two desk files only) | `c14217ba2384be6532b90d7f0771b7952063bcb2` — launch row committed |
| 17 rule strings, `grep -c -F -e "<rule>"` on `08-bars-chunk-e-check.md`, quotes included | each of the 14 allow strings and 3 denies printed **1** (line count; ≥1 required; 0 failures). `Bash(grok *)` and `Bash(agy *)` printed 1 here, not the 2 the prompt recorded — ≥1 is the test, so it passes; disclosed |
| Sol / Opus checker string in my launch line | none (`gpt-5.6-sol`, `claude -p --model claude-opus-5` absent; the astra string is `gpt-6-astra`, the carried one) |

**(5') GROK / AGY GATE:** R19 row printed at PREFLIGHT row 2; it is re-run immediately before the house launches (`## Clock`).

## PREFLIGHT
| # | Rule | Command | Exit | Result |
|---|---|---|---|---|
| 1 | `Bash(date*)` | `date` | 0 | allowed — `Thu Sep 24 12:13:02 EDT 2026` |
| 2 | `Bash(grep *)` (5') | R19 grep | 0 | allowed — row 29 printed, carries `All 4 house models approved` |
| 3 | `Bash(grok *)` | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 4 | `Bash(agy *)` | `agy --version` | 0 | allowed — `1.2.10` |
| 5 | `Bash(ls *)` | `ls scratch/tribunal-bars-0920/drc-overnight` | 0 | allowed — lists `r1` |
| 6 | `Bash(ls *)` | `ls scratch/tribunal-bars-0920/drc-overnight/r2` | 1 | allowed — `No such file or directory` = fresh run |
| s1 | `Bash(tail *)` | `tail -n 3` `drc-d1-fix-r1-check-2026-09-24.md` (15) | 0 | last non-blank starts `DRC D1 FIX R1 CHECK DONE ` |
| s2 | `Bash(tail *)` | `voice-v1-check-a-2026-09-24.md` (16) | 0 | last non-blank starts `VOICE V1 CHECK DONE ` (part A) |
| s3 | `Bash(tail *)` | `voice-v1-check-b-2026-09-24.md` (17) | 0 | `VOICE V1 CHECK DONE ` (part B) |
| s4 | `Bash(tail *)` | `voice-v1-check-c-2026-09-24.md` (18) | 0 | `VOICE V1 CHECK DONE ` (part C) |
| s5 | `Bash(tail *)` | `voice-v1-check-d-2026-09-24.md` (19) | 0 | `VOICE V1 CHECK DONE ` (part D) |
| s6 | `Bash(tail *)` | `jev-check-final-2026-09-23.md` (74) | 1 | `No such file` → `grep -n -F "74 is not running"` printed `cto-2026-09-24.md:54` (R44), which ALSO names `27-drc-overnight-tribunal-r2.md` → `74: no report — not running (launch row)` |
| s7 | `Bash(tail *)` | `drc-overnight-tribunal-2026-09-24.md` (23) | 0 | last non-blank starts `DRC OVERNIGHT TRIBUNAL R1 DONE ` |
| 7 | `Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)` (3') | astra probe, `run_in_background`, `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 1 | allowed, answered with the usage-limit text verbatim: `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM.` → **`astra: METER — proceed on Grok + Gemini`**; return time **Sep 26th, 2026 6:47 AM** (the desk seats Astra from then, L62 / R19). Not a refusal; astra is not launched. |

No other Grok / Gemini hub named by the launch row (R44: `15`–`19`, `74`, `23` not running). The Anthropic seat `28` running beside me is not a house hub and does not block.

## Packet
Folder `scratch/tribunal-bars-0920/drc-overnight/r2/` (gitignored in `~/cobalt-wt/agy-trial`; created by the first Write, no `mkdir`). **THE BUILT CODE IS THE D1 BRANCH:** `git -C /Users/cobalt/cobalt log -1 --format=%H drc/d1-trading-log` → `38a709472d428f1fda77fac93c75d0f5b9a2c6d6` (= expected `38a70947…`, no new tip); `git show --stat 38a70947` → docs only (`reports/drc-d1-fix-r1-build-2026-09-24.md`, 234 insertions, 1 file); worktree `git status --short` empty; sizes at drafting all match: `pairing.py` 12,901 B · `store.py` 10,568 B · `models.py` 8,844 B · `test_drc_pairing.py` 13,959 B · `0016_drc.sql` 4,945 B. Trailing-whitespace lines (`grep -c -E "[[:space:]]$"`): `pairing.py` 0, `store.py` 0, v2 0 — so the whole-file copies are byte-identical after the one header line (`20-` = 12,901 + 86 B header line; `21-` = 10,568 + 84 B header line; line counts 349 / 254 = original + 1).

| File | Bytes | Status |
|---|---|---|
| `00-READING-ORDER.md` | 2,958 | MANDATORY reading order (written last) |
| `01-QUESTIONS-R2.md` | 9,694 | verbatim questions + "Files in this folder" + the `../r1/` sentence |
| `02-greps.txt` | 15,610 | OPEN-AS-NEEDED; S1–S7 (the seven commands, full output) |
| `10-NEEDS-ROUND-2.md` | 3,850 | MANDATORY — derive `:90-100` + ESCALATE 5 (`:144`) and 9 (`:148`) |
| `11-v2-sections.excerpt.md` | 36,837 | MANDATORY — v2 `:1-11`, `:73-94`, `:95-110`, `:111-165`, `:166-190`, `:201-216`, `:261-268`, `:276-285`, `:295-306`, `:308-315` |
| `12-hub-checks.md` | 6,655 | MANDATORY — R1 hub rows Q3, Q10, (b), (e), GK7/13/21/26/32, GM3/8/12, FC3/13/19/22, ESCALATE 1–2 |
| `13-seat-r1.excerpt.md` | 5,763 | MANDATORY — seat R1 `:41-52`, `:75-77`, `:98-107`, `:114-120` |
| `14-grok-r1-own.excerpt.md` | 6,872 | **[RAW RULING — Grok's own, for Grok only]** — `grok-ruling.md` `:21-28`, `:77-86`, `:133-147`, `:171-178` |
| `15-gemini-r1-own.excerpt.md` | 2,170 | **[RAW RULING — Gemini's own, for Gemini only]** — `gemini-ruling.md` `:9-12`, `:37-40`, `:48-50`, `:57-59` |
| `20-pairing-whole.py` | 12,987 | MANDATORY — `pairing.py` WHOLE (code tip `d1342595`) |
| `21-store-whole.py` | 10,652 | MANDATORY — `store.py` WHOLE |
| `22-cited.excerpt.py` | 6,817 | MANDATORY — `models.py` `:94-113`, `:254-263`; test `:340-351`; `0016_drc.sql` `:17-95`; `propose.py` `:300-307` |
| **Total** | **120,865** | under 140 KB — NO cut applied (cut order (i) `11-` to markers, (ii) `02-greps` whole: not needed) |

Anchors checked with `grep -n`: v2 `R2-1 OPEN` printed `:9 :93 :109 :142 :190 :206 :224` (= drafting); v2 headings at `:1 :73 :95 :111 :166 :201 :261 :276 :295 :308`; derive `:90 :102 :144 :148`; seat R1 `:41/:53`, `:75/:78`, `:98/:108`, `:114/:121`; Grok R1 `:21/:29`, `:77/:87`, `:133/:148`, `:171/:179`; Gemini R1 `:9/:13`, `:37/:41`, `:48/:51`, `:57/:60`; code anchors `models.py:94/:102/:254`, `test:350`, `0016_drc.sql:20/:34/:52/:80/:86/:95`, `propose.py:300` — **no boundary moved**. One boundary note: v2's last line is `:315` (the prompt's `:308-316` runs one past the end); staged `:308-315`. The R1 report's `## Rulings table` is at `:95-115` and `## Checked against the files` at `:140`, so the row lines used are `Q3 :102 · Q10 :109 · (b) :112 · (e) :115 · GM3 :147 · GM8 :152 · GM12 :156 · GK7 :164 · GK13 :170 · GK21 :178 · GK26 :183 · GK32 :189 · FC3 :208 · FC13 :218 · FC19 :224 · FC22 :227`, ESCALATE items at `:279-280`.

NOT STAGED: the proposal, his DRC note and template, any real export or fixture, `DRC-AUTOMATION-v2`, S3 v3, the voice FINAL, any trade or production row, the seat's ROUND-2 report (blind both ways). The round-1 packet stays at `../r1/`.

**REDACTION (L32):** `grep -c -E "TSLA|372[.]82|374[.]50"` (the three literals of `73` §1) on each of the 12 staged files → `0` on every one. Replacements: **0** (no `[TICKER]` / `[PRICE]` / `[user data]` was needed; no other ticker, price, share count of his or P&L found — the only share figures are the Anthropic seat's constructed `40` in its Mon / Tue / Wed scenario and the tests' constructed fixtures). SHAPE-ONLY drops: 0 (no vault note of his is staged).
Wrong-path write: one stray Write (a malformed `/Users/cobalt-wt-placeholder` path in my own turn) was REFUSED by the harness with `EACCES`; nothing was created; recorded for honesty.

## CONTINUE
next: none — the run is finished (12:42:21 ET). The desk commits this report; when the Anthropic seat's `DRC OVERNIGHT FABLE R2 DONE` line is committed too, it launches `29-drc-overnight-tribunal-derive-r2.md`. No house is running. (History of this section: launch 12:22, deadline 12:42, Gemini done 12:24, Grok done 12:36.) Launched: Grok (background task `ba3gs8d5t`) and Gemini (background task `bjxd0ej70`), both launched together in one message between 12:22:32 (gate row) and 12:23:08 (`date` after) — launch taken as **12:22**; 20-minute deadline **12:42 ET** for both (stop by task-stop, record TIMEOUT). Astra: METER (return Sep 26th, 2026 6:47 AM), not launched.

## Clock
| time | trigger | minutes since launch | action |
|---|---|---|---|
| 12:13:02 | preflight row 1 | — | — |
| 12:22:32 | packet staged; pre-launch gate row (R19 grep re-run, printed, carries `All 4 house models approved`) | — | about to launch both houses |
| 12:23:08 | both houses launched together in one message (Grok `ba3gs8d5t`, Gemini `bjxd0ej70`), `run_in_background` | Grok 0–1 · Gemini 0–1 | launch taken as 12:22; deadline 12:42; starting the round-1 Q3 file-check C1–C8 |
| 12:23:37 · 12:23:48 · 12:23:52 | between C rows (C1 → C2–C6 → C7 → C8) | 1–2 | both running; no ruling file yet (`ls` of `r2/` shows the 12 staged files only) |
| 12:36:33 | completion notice: Grok `ba3gs8d5t` exit 0 (≈ 14 min) | Grok ≈ 14 · Gemini done | `grok-ruling-r2.md` present (written by Grok itself); closing line `TRIBUNAL R2: BUILD AFTER fold this paste before the K1 migration` |
| 12:37:23 | collate step (independence greps; reading models.py) | — | both houses finished |
| 12:38:41 | before `## Checked against the files` | — | — |
| 12:39:29 | before the seat's round-2 check (tail printed `DRC OVERNIGHT FABLE R2 DONE …`) | — | read its `## Rulings`, `## Self-attack`, `## Withdrawn` after the tables were written |
| 12:40:24 | between FR rows | — | verifying greps |
| 12:42:21 | close | — | last non-blank line replaced; no house still running |
| 12:24:18 | C1–C8 written; before ending the turn | Grok ≈ 2 · Gemini ≈ 2 | both running; deadline 12:42 |
| 12:24:37 | completion notice: Gemini `bjxd0ej70` exit 0 (≈ 2 min) | Grok ≈ 2 · Gemini done | read its printed answer; `gemini-ruling-r2.md` written byte for byte (harness's trailing `[exited with code 0]` dropped); Gemini closing line `TRIBUNAL R2: BUILD` |
| 12:25:03 | after writing the Gemini file | Grok ≈ 3 | Grok's interim output shows it is reading the packet, no ruling file yet; waiting |

## Rulings table
Houses: Grok (`grok-ruling-r2.md`, background `ba3gs8d5t`, finished 12:36 ET, ≈ 14 min) · Gemini (`gemini-ruling-r2.md`, printed, `bjxd0ej70`, finished 12:24 ET, ≈ 2 min) · Astra: METER (probe row in `## PREFLIGHT`, back Sep 26th, 2026 6:47 AM), did not rule. The Anthropic seat is not counted here (I read its round-2 report only after this table was written); the second derive counts it.

| sub-item | grok | gemini | agreement (houses that ruled) | gist ≤25 words per house |
|---|---|---|---|---|
| R2-1(i) first record of P is a re-pair trigger | ADOPT seat (changes its round-1 mind) | ADOPT seat | 2-0 ADOPT seat | grok: trigger fires on P's first record; N's stated seed is not lawful once P's close exists. gemini: Mon's first file triggers nothing under "superseding only"; Tue stays flat, violating L1. |
| R2-1(ii) P's carried book replaces N's stated seed; history; `/drc` | ADOPT seat | ADOPT seat | 2-0 ADOPT seat | both: carried book replaces the stated seed (R67 DAS is the truth); the stated row stays append-only; `/drc` shows `stated book for <N> differed from <P>'s close: <trade_ids>`. |
| R2-1(iii) re-paired day's stats input | ADOPT WITH (current-import fills; stored `stats_row` read before the delete; re-run `match_stats`; NOT the `day` row's import ids) | ADOPT seat | SPLIT | grok: fills from the newest un-superseded import; stats from stored rows, re-matched; objects to the seat's `day`-row import ids. gemini: stats rows read before the delete, seat's text whole. |
| R2-2(a) `via` of the CLI caller | ADOPT WITH third literal `state_book_cli` | ADOPT WITH third literal `'cli'` | SPLIT (both: a third literal; different literal) | grok: `CHECK IN (drc_page, voice_widget, state_book_cli)`; reusing either existing literal misreplays. gemini: `'cli'`, distinct caller. |
| R2-2(b) migration consequence | ADOPT WITH: the one K1 migration only | ADOPT WITH: the one K1 migration only | 2-0 same consequence (literal names differ, see (a)) | both: `drc_stated_books` exists on no branch (S1, S6, S7); nothing built changes; `0016` not edited. |
| R2-2(c) CLI is the landing set's caller when K3 is not checked | ADOPT WITH: yes; only the `via` literal differs from the form; `turn_id` / `readback_sha256` NULL; no vault note | ADOPT WITH: yes; `via` differs, `turn_id` / `readback_sha256` NULL | 2-0 same mechanism (literal names differ, see (a)) | both: the CLI stands in per `[F-10]` so D2 + D3 never deploy without a caller; it writes the same columns as the page form. |
| closing line | `TRIBUNAL R2: BUILD AFTER fold this paste before the K1 migration` | `TRIBUNAL R2: BUILD` | — | — |

| item | outcome | why |
|---|---|---|
| R2-1 (i)(ii)(iii) | **SPLIT** | (i) and (ii) agree 2-0; (iii) differs: Grok's ADOPT WITH (executions from the newest un-superseded import, not the `day` row's ids) against Gemini's ADOPT seat (whole text, which carries the `day` row's import ids). No supporting claim of either DOES NOT HOLD in my file-check. |
| R2-2 (a)(b)(c) | **SPLIT** | (b) and (c) agree; (a) names two different literals — `state_book_cli` (Grok) vs `'cli'` (Gemini). The rule counts the same literal only. |

Items converged: **0 of 2** (houses only; the Anthropic seat is counted by the second derive).

## Wording offered, verbatim
Unedited; no user-data span found in either text (the days Mon / Tue / Wed, the `40` and the import ids `10` / `12` are constructed examples). Grok's file is copied whole below; Gemini's answer is `gemini-ruling-r2.md`, copied whole.

### GROK — `scratch/tribunal-bars-0920/drc-overnight/r2/grok-ruling-r2.md` (verbatim)

> # Grok — DRC overnight lane, tribunal round 2
>
> House: Grok. Code tip `d1342595`. Round-1 own wording read: `14-grok-r1-own.excerpt.md`. I change my mind on the trigger scope (below). I do not reopen a folded rule. Line numbers are the D1 files (`S2`: `record_import` commit `store.py:145`, `record_day` `store.py:153`, DELETE `store.py:202`, `seed_for` `store.py:220`).
>
> ## R2-1(i) — first record of P is a forward re-pair trigger
>
> ADOPT seat.
>
> I change my round-1 mind. My Q3 trigger was only a superseding import of P. That leaves the seat's first-record case uncorrected. My (b) sentence is true of how a pairing starts and false as a licence to keep N's stated seed after P's close exists. Not lawful under L1 once P is recorded (R67 DAS reconciles; R22 last night informs the next day).
>
> Walk (constructed; 40 is the seat's figure). N is Tue. (1) Tue first, he states flat, file `B 40`: `record_import` writes the import and fills (`store.py:88-117`, commit `store.py:145`); no stated-book table today (`store.py:42`); under v2 the statement is `drc_stated_books` kind `opening`, positions `[]`, supersedes NULL. Empty seed: `B` opens a long (`pairing.py:190-191`); `record_day` writes that long (`store.py:153-212`). (2) Wed: `seed_for` reads only earlier days (`store.py:227-235`) and Tue's `open_position` (`store.py:245-250`); contiguity passes (`pairing.py:249-250`); Wed stores the long. (3) Mon's first file: `check_contiguity` passes because `earlier` is empty (`pairing.py:249-250`; `test_drc_pairing.py:350-351`); nothing to supersede (`store.py:88-97`). My R1 trigger does not fire. Tue stays the stated-flat long; `/drc` does not say Mon's short 40 contradicts it. (4) The seat's trigger is the fix: Mon's `record_day` re-pairs Tue (the `B 40` covers, `pairing.py:203-213`) and Wed from Tue's new close.
>
> No objection that survives. A non-adjacent later day (Wed recorded, Tue missing, Mon recorded later) fails loud on contiguity (`pairing.py:250-254`) under the folded all-or-nothing rule. He states or imports Tue, then Mon. That is the smaller mechanism, not a second path.
>
> ## R2-1(ii) — P's carried book replaces N's stated seed
>
> ADOPT seat.
>
> After the trigger commits, Tue's `drc_rows` are replaced (DELETE `store.py:202`, then insert): `seed` source `carried`, `from_day` Mon; the `B 40` is a cover, not a new long; the open book is flat if that was the only position. Wed's rows are replaced from Tue's new close: the long is gone. The Tue `drc_stated_books` opening row is not deleted and not superseded — the DELETE names `drc_rows` only (`store.py:202`); v2 §3 is append-only. It stays the audit of what he said. It is not the seed once Mon is recorded: `seed_for` reads the prior day's `open_position` rows (`store.py:245-250`). `/drc` shows `stated book for Tue differed from Mon's close: <Mon's short trade_id>`.
>
> R67's "his held-count statement wins mid-trade" lasts until the export reconciles. The opening statement is not a permanent override of P's stored close. Not OWNER: the reconcile direction is already his ruling.
>
> No objection. Writing the carry back as a new `opening` row would record a statement he did not make. The seat does not do that.
>
> ## R2-1(iii) — stats input of a re-paired day
>
> ADOPT WITH: "Inputs of each re-paired day: executions from `drc_fills` of the current import only — the `drc_imports` row of that day and kind that no other row supersedes (`store.py:88-97`). Not the import ids on its `day` row (`store.py:190`): `record_import` commits the new file first (`store.py:145`) and that row still names the predecessor until `record_day` replaces it. Stats are not in `drc_fills` (`0016_drc.sql:52-71`); the file bytes are not kept (`store.py:109` stores sha256 only). Before the delete (`store.py:202`), read that day's `stats_row` rows (`derived.row`, `store.py:170-186`) and its `day.derived.not_computed` (`store.py:195`). Re-run `match_stats` (`pairing.py:260-316`) from those stored rows against the new pairing. If `not_computed.match` is set, keep it and do not invent a match. An unchanged later day yields the same `derived` and `inputs`."
>
> I keep my round-1 executions sentence and drop it as a complete answer: it never named the stats rows. The seat is right that stats survive only in `drc_rows`, and wrong that the executions source is the `day` row's import ids. Price: K2, `store.py` only, inside the one re-pair transaction already folded; no migration, no new table, no second chunk. The seat's +1 h already covers the read-before-delete; this wording adds no measured hour (UNVERIFIED, as that estimate was).
>
> Objection to the seat's executions clause. Tue's `day` row names trading_log import 10 (`B 40`). He re-imports Tue: `record_import` commits import 12, supersedes 10 (`store.py:116`, `:145`); the `day` row still says 10. A re-pair that loads import 10 pairs the superseded fills and ignores 12. `/drc` shows the old book. X9 names that result. The current-import predicate is the smaller rule and covers both the superseded day and an unchanged later day.
>
> Objection to stopping at my executions sentence. The same re-pair then deletes Tue's `stats_row` rows (`store.py:202`). Nothing in `drc_fills` can rebuild them. `/drc` shows the trades with the stats match gone. Copying the old match verdict is also wrong: after Mon's short, the phantom long's `trade_id` is gone (`pairing.py:211-213`), and a stored link to it would be a lie. Re-run `match_stats` on the stored rows. X9 is the run; I do not restate it.
>
> ## R2-2(a) — `via` for the CLI statement caller
>
> ADOPT WITH: "`drc_stated_books.via` is `text CHECK IN (drc_page, voice_widget, state_book_cli)`. `state_book_cli` is the `cobalt drc state-book` caller. `record_stated_book` stays the one writer (L3); the caller passes `via` and does not insert. A replay can tell which of the three callers wrote the row (L57)."
>
> S5: the CHECK names only `drc_page` and `voice_widget` (v2 `:125`); the CLI is unnamed (v2 `:134`). S1: neither literal, nor the table, nor `record_stated_book`, exists in D1 `src/cobalt` or main `src/cobalt`. Reusing `drc_page` fails L57. He states Tue flat by CLI while K3 is not deployed; the row stored as `drc_page` replays as a page write on a day the page had no route. Reusing `voice_widget` is worse: the CLI has no turn and no read-back (v2 `:126-127`), so `via=voice_widget` with `turn_id` NULL looks like a widget confirm that never happened (09-23 R39). The third literal is snake_case like the other two and names this command, not `cobalt drc build`. Price: one token in the K1 CREATE CHECK. No second migration, no edit of `0016`. The CLI's +0.5 h (`[F-10]`) already includes passing the literal.
>
> ## R2-2(b) — migration consequence
>
> ADOPT WITH: "The literal `state_book_cli` is written only in the one K1 migration that creates `drc_stated_books`. Nothing already built changes. `0016_drc.sql` is not edited. `0017_voice_turns.sql` is not edited."
>
> S1: no match in either tree. S6: the D1 worktree's migrations are `0001`–`0011` and `0016_drc.sql` / `.rollback.sql`. No file creates `drc_stated_books`. S7: `0016` is `d583f6fd` (`drc_imports`, `drc_fills`, `drc_rows`); `0017` is `69c376bd` (`voice_turns`). No commit on any branch creates this table or this CHECK. The literal is therefore not an ALTER of an applied constraint. It changes the one K1 migration only. Objection to putting it in `0016`: that file's CHECKs are the three D1 tables (`0016_drc.sql:52-71` fills, `:86` `drc_rows.kind`), and `[F-02]` already keeps a new file. X5 is the run for whether `0016` is applied; it does not create this table, so I do not restate it.
>
> ## R2-2(c) — CLI is the statement caller when K3 is absent
>
> ADOPT WITH: "When K3 is not checked, `cobalt drc state-book` is the landing set's statement caller. D2 and D3 do not deploy without K1, K2, and that caller (`[F-10]`, `[F-17]`). It calls `record_stated_book` only (L3, the same function as the form and the widget). It writes the same columns the `/drc` form writes, except `via = state_book_cli` where the form writes `drc_page`. It does not write `turn_id` or `readback_sha256` (both NULL; voice caller only, v2 `:126-127`) and it writes no vault note."
>
> I do not change my round-1 landing shape. The column delta is new: round 1 had no `via` gap. What the CLI writes that the form would not: only the `via` literal. No other column. ESCALATE 5 stands — the deploy set and the migration number stay the desk's at the L43 / L68 gate. Not re-ruled here.
>
> Objection to leaving no statement caller when K3 is absent. D2 + D3 + K1 + K2 deploy, no CLI. The first import stores the file and shows `not computed — opening book not stated`, and nothing can call `record_stated_book` (S1: no caller exists today; S3: `record_day` / `seed_for` have no caller outside their definitions). He cannot state the book. That is the stuck first import `[F-10]` forbids. It is not a flat path: pairing still does not run on an empty seed until the statement (B8 is `pairing.py:189-193` only when a seed is empty and pairing runs).
>
> Objection to the CLI writing `turn_id` or `readback_sha256`. The row would replay as a confirmed widget read-back. He typed a command. 09-23 R39's confirm did not happen.
>
> ## OWNER
>
> none. The `via` literal, the re-pair trigger, and the stats source are design. The opening-book reconcile is already R67. The deploy set and the migration number are the existing L43 / L68 gate (ESCALATE 5), not a new owner item and not a precondition this round adds.
>
> ## EXPERIMENTS
>
> X7: cited, not restated — the one-transaction shape R2-1(i) uses when a later day fails contiguity.
> X9: cited, not restated — R2-1(iii); superseded fills, and whether stored `stats_row` rows rebuild an unchanged day.
> X10: cited, not restated — R2-1(i)'s stated-later-then-earlier-file sequence. The code walk is already HOLDS (`FC3`, `FC22`); this ruling is the design that run was left open to show.
> No new X. R2-2 is a CHECK literal on a table S1, S6 and S7 show does not exist.
>
> TRIBUNAL R2: BUILD AFTER fold this paste before the K1 migration

### GEMINI — `scratch/tribunal-bars-0920/drc-overnight/r2/gemini-ruling-r2.md` (verbatim)

> **R2-1(i)**
> ADOPT seat
> - Tue imported first, states `flat`. `drc_rows` stores Tue's `day`, `seed`, and `open_position`.
> - Wed imported. `store.py:227` finds Tue. `check_contiguity` (`pairing.py:249-250`) passes. Wed seeds from Tue's flat.
> - Mon imported for the first time. `check_contiguity` passes (`earlier` is empty). Mon's `drc_rows` stored with an open short.
> - Under Grok's trigger ("superseding import" only), Mon's first file triggers nothing.
> - Tue stays paired from flat, hiding Mon's open short, violating L1 (no assumed book). It must be a trigger.
>
> **R2-1(ii)**
> ADOPT seat
> - P's carried book replaces N's stated seed because R67 rules "DAS is the truth" (exports override statements).
> - N's stated row stays in `drc_stated_books` as history since it is append-only.
> - N's `drc_rows` for `seed` will reflect `source: carried` from P's `book_close`.
> - `/drc` shows: `stated book for <N> differed from <P>'s close: <trade_ids>`.
>
> **R2-1(iii)**
> ADOPT seat
> - `drc_fills` holds trading-log columns only (`0016_drc.sql:52-71`).
> - `match_stats` requires a `ParsedStatsLog` which contains `StatsRow`s (`pairing.py:261-263`).
> - These stats rows are stored only in `drc_rows` with `kind = 'stats_row'` (`store.py:173-186`).
> - Because `record_day` runs `DELETE FROM drc_rows` first (`store.py:202-203`), the stats rows must be read before the delete to reconstruct the stats input.
>
> **R2-2(a)**
> ADOPT WITH a third CHECK literal: 'cli'
> - L57 requires a replay to tell exactly which caller wrote the row.
> - The `cobalt drc state-book` CLI is a distinct caller from `drc_page` and `voice_widget`.
> - L3 dictates one store function behind every caller, so `record_stated_book` handles all three `via` values.
>
> **R2-2(b)**
> ADOPT WITH it changes the one K1 migration only
> - `02-greps.txt` S1 confirms `drc_stated_books` and `via` values do not exist in the D1 worktree or main branch.
> - No existing migration or built code needs to be altered.
> - The third literal `'cli'` is simply added to the new K1 migration.
>
> **R2-2(c)**
> ADOPT WITH yes, the CLI is the landing set's statement caller when K3 is not checked
> - Per `[F-10]`, if K3 is not deployed in time, the CLI stands in so K1 + K2 can safely deploy with D2 + D3.
> - The CLI writes `via = 'cli'` instead of `via = 'drc_page'`.
> - Like the page form, it writes `NULL` for `turn_id` and `readback_sha256`, as those are exclusively voice-widget columns.
>
> OWNER: none
> EXPERIMENTS: none
> TRIBUNAL R2: BUILD

## Anthropic-seat round-1 Q3 claims, file-checked
Seat report `reports/drc-overnight-tribunal-fable-r1-2026-09-24.md` (Q3 claims at `:41` (1)–(4) and `:49`; C8 at `:73` and `:116-117`). Files opened by me: the D1 worktree at `d1342595` (`store.py`, `pairing.py`, `test_drc_pairing.py`, the migrations dir) and `02-greps.txt` S1 (my own greps). `date` between rows: 12:23:37 · 12:23:48 · 12:23:52 (Clock).

| C | claim (seat report line) | file:line | verdict | note ≤30 words |
|---|---|---|---|---|
| C1 | a later day recorded first is lawful today (`:41`) | `test_drc_pairing.py:350-351` (`D = 2001-01-02` `:146`, `D_NEXT = 2001-01-03` `:147`) | HOLDS | `check_contiguity(D, 2000-12-29, [D_NEXT])` raises nothing: `earlier` (days before `D`) is empty, so a later recorded day is not history. |
| C2 | a re-paired day's executions can be found through the import ids its own `day` row names (`:41`) | `store.py:190` | HOLDS | the `day` row's `inputs` is `{"import_ids": {kind: id}}`; a no-trade day writes `{}`; an id names the import current when the day was recorded, not necessarily the newest. |
| C3 | stats rows are stored as `stats_row` rows carrying `derived.row` (`:41`, `:49`) | `store.py:170-186` | HOLDS | matched rows `:171-176`, unmatched `:181-186`; each `derived = {match, trade_id, row: <StatsRow dump>}`; `drc_fills` has no stats columns (`0016_drc.sql:52-71`). |
| C4 | the day row stores `not_computed` (`:41`) | `store.py:195` | HOLDS | `derived.not_computed = dict(pairing.not_computed)`; the `match` key is set by `match_stats` (`pairing.py:271`) and `build_day` (`:333`). |
| C5 | `record_day` commits per call (`:41`) | `store.py:198-212` | HOLDS | `autocommit = False` `:199`, DELETE `:201-203`, INSERTs, one `conn.commit()` `:212` per call; rollback on error. Days are separate transactions today. |
| C6 | `record_import` commits the `drc_imports` / `drc_fills` rows before any pairing (`:41`) | `store.py:85-150` | HOLDS | one transaction, `conn.commit()` at `:145`; `store.py` calls no pairing function at all — pairing is the caller's separate step. |
| C7 | `seed_for(day)` reads recorded days strictly before `day` only, so a first record of an earlier day passes `check_contiguity` (`:41`, `:45`) | `store.py:227-235`, `pairing.py:249-250` | HOLDS | SQL `day < %s` `:231`; `earlier = {d … if d < day}` `:249`; `check_contiguity` is called only from `seed_for` (`store.py:235`) — `record_day` does not call it. |
| C8 | nothing in `src/cobalt` of the D1 worktree or main writes or reads `drc_stated_books` or a `via` column today (`:73`, `:116-117`; S1) | `02-greps.txt` S1; my extra `grep -rn -w -e via` on both migration dirs and `drc/` | HOLDS | S1: no output for `drc_stated_books`, `record_stated_book`, `state-book`, `voice_widget`, `drc_page` in either `src/cobalt`; `via` appears only in a `0001_schemas.sql:112` comment. |

Anthropic-seat R1 Q3 claims checked: 8 HOLD of 8 checked.

## Checked against the files
Legend: `claim · who · file:line · verdict · ≤30 words`. Files opened by me at 12:37–12:39 ET: the D1 worktree (`store.py`, `pairing.py` whole; `models.py:196-253`; `0016_drc.sql`; test constants), main's `LAWS.md` (L57, L3), `cto-2026-09-22.md` R67, v2 (`:125-134`, `:152-154`, `:214`), `02-greps.txt`. `G` = Grok, `M` = Gemini. Design statements about rows / pages that are not built (`seed`, `book_close`, `drc_stated_books`, the `/drc` line) are checked against v2's text and marked "v2 design, not built".

| # | claim · who | file:line | verdict | note ≤30 words |
|---|---|---|---|---|
| G1 | R2-1(i) `record_import` writes the import and fills, committed at `:145`; no stated-book table today · grok | `store.py:88-117`, `:145`, `:42` | HOLDS | = C6; `TABLES = ("drc_imports", "drc_fills", "drc_rows")` at `:42`; `S1` finds no `drc_stated_books` anywhere. |
| G2 | R2-1(i) an empty seed lets a leading `B` open a long; `record_day` writes it · grok | `pairing.py:190-191`, `store.py:153-212` | HOLDS | `book is None` and `BUY` → `_open(e, LONG)`; the position is still open at file end → an `open_position` row. |
| G3 | R2-1(i) Wed's `seed_for` reads only earlier days and Tue's `open_position`; contiguity passes · grok, gemini (M1) | `store.py:227-235`, `:245-250`, `pairing.py:249-250` | HOLDS | = C7; `day < %s` `:231`; open positions read at `:245-249`; `check_contiguity` is fed `recorded` from the same query. |
| G4 | R2-1(i) Mon's first file: `check_contiguity` passes (`earlier` empty), nothing to supersede, so a "superseding import" trigger does not fire · grok, gemini (M2) | `pairing.py:249-250`, `test_drc_pairing.py:350-351`, `store.py:88-97` | HOLDS | = C1 / C7, FC3, FC22; `prior` query returns none for a day with no earlier import of that kind (`:88-97`). |
| G5 | R2-1(i) Tue stays the stated-flat long; nothing compares Mon's close with Tue's seed · grok, gemini | `store.py:153-250`, `pairing.py:239-254` | HOLDS | mechanism only (= FC22); no line of `store.py` / `pairing.py` compares an earlier day's book with a later day's seed. The label "L1 violation" is theirs. |
| G6 | R2-1(i) a non-adjacent later day (Wed recorded, Tue missing, Mon recorded later) fails loud on contiguity when re-paired · grok | `pairing.py:250-254` | HOLDS | as mechanism: re-pairing Wed via `seed_for` has `earlier = {Mon}`, `prior = Tue` absent → `PairingError`. It presumes the re-pair goes through `seed_for` (v2 design, not built). |
| G7 | R2-1(ii) the DELETE names `drc_rows` only; the stated row is not deleted; `seed_for` reads `open_position` rows · grok | `store.py:202`, `:245-250`; v2 `:129`, `:132` | HOLDS | = GK7; v2 §3 makes `drc_stated_books` append-only (`refuse_row_update`); the table is not built (S1). |
| G8 | R2-1(ii) R67: his held-count statement wins mid-trade; the DAS import RECONCILES — DAS is the truth · grok, gemini (M3) | `cto-2026-09-22.md` R67 (row 99) | HOLDS | R67 (1) "held-count statement … wins over the recomputed count", (3) "DAS trading-log import RECONCILES — DAS is the truth". That an opening statement yields to P's close is their reading. |
| M4 | R2-1(i) `drc_rows` stores Tue's `day`, `seed` and `open_position` · gemini | `0016_drc.sql:86`; v2 `:79` | HOLDS | v2 design, not built: `kind` CHECK today has `trade`, `open_position`, `stats_row`, `day` only; `seed` is v2 §2b(3) (K1). |
| M5 | R2-1(ii) N's `seed` row will read `source: carried` from P's `book_close` · gemini | v2 `:79` | HOLDS | v2 design, not built (`book_close` and `seed` kinds are K1). |
| G9 | R2-1(iii) `drc_fills` holds no stats rows; `store.py:109` stores sha256 only, not the file bytes · grok | `0016_drc.sql:52-71`, `:26-42`, `store.py:109` | HOLDS | = FC5 / FC19; `drc_imports` has `sha256`, no bytes column; `drc_fills` columns are trading-log only. |
| M6 | R2-1(iii) `match_stats` requires a `ParsedStatsLog` containing `StatsRow`s · gemini | `pairing.py:260-263` | HOLDS | = FC6; `models.py:241-243`: `ParsedStatsLog{result: ImportResult, rows: list[StatsRow]}` — it also needs a `result`. |
| M7 | R2-1(iii) stats rows are stored only in `drc_rows` `stats_row` rows · gemini | `store.py:173-186` | HOLDS | = C3 / FC5; matched rows `:170-176`, unmatched `:180-186` (its range starts at `:173`, inside the first append; substance holds). |
| G10 | R2-1(iii) the `day` row still names the predecessor import until `record_day` replaces it · grok | `store.py:145`, `:187-197`, `:190` | HOLDS | `record_import` commits at `:145`; the `day` row (`import_ids`) is written only by `record_day`. It bites a day whose newer file is stored but not applied (`[F-25]`); the seat's text does not address it. |
| G11 | R2-1(iii) the current import is the row of that day and kind that no other row supersedes · grok | `store.py:88-97`, `:116`, `:145` | HOLDS | the same predicate `record_import` uses to set `supersedes`; nothing else in `store.py` reads it back. |
| G12 | R2-1(iii) re-run `match_stats` from the stored `stats_row` rows against the new pairing; keep `not_computed.match` if set · grok | `pairing.py:260-316`, `store.py:170-195`, `models.py:241-243` | UNVERIFIABLE FROM READS | stored `StatsRow` dumps can fill `.rows`, but `match_stats` reads `stats.result.missing` (`pairing.py:265`) and `missing` is no stored column (`0016_drc.sql:26-42`) → run X9 (no new X). |
| G13 | R2-1(iii) after Mon's short the phantom long's `trade_id` is gone, so a stored match link to it is stale · grok | `pairing.py:67-69`, `:210-213`, `:295` | HOLDS | `trade_id` carries direction and entry time (`:69`); a covered trade closes and is deleted from `books` (`:210-213`); the stats match is by symbol + direction + entry time (`:295`). |
| G14 | R2-2(a) the CHECK names only `drc_page` and `voice_widget`; the CLI is unnamed · grok | v2 `:125`, `:134`; `02-greps` S5 | HOLDS | = the derive's ESCALATE 9; S5 prints v2 `:125` and `:134`. |
| G15 | R2-2(a) neither literal, the table, nor `record_stated_book` exists in D1 or main `src/cobalt` · grok, gemini (M8) | `02-greps` S1 | HOLDS | = C8; S1 prints nothing for all five names in both trees; `via` appears only in a `0001_schemas.sql:112` comment. |
| G16 | R2-2(a) the CLI has no turn and no read-back; `turn_id` / `readback_sha256` are voice-only · grok, gemini (M9) | v2 `:126-127` | HOLDS | v2 §3 table: `turn_id` "the widget turn (voice caller only)", `readback_sha256` "the confirmed read-back's binding (voice caller only)". |
| G17 | R2-2(a) reusing `drc_page` / `voice_widget` "fails L57" (a replay could not tell the caller); L57 requires a replay to tell which caller wrote the row · grok, gemini (M10) | `LAWS.md:317` (L57) | UNVERIFIABLE FROM READS | L57 says "No derived value ships without its stored inputs; every number must be replayable." — silent on caller identity. `01-QUESTIONS-R2.md` itself framed "can a replay tell which caller". A reading, not a file fact. |
| G18 | R2-2(a) one store function behind every caller (L3) · grok, gemini (M11) | `LAWS.md` L3; v2 `:160`, `:312` | HOLDS | v2 §3 "Who writes what": one `DrcStore` writer, callers include page, `cobalt drc build`, the CLI and the widget; v2 "The bar" L3 says the same. |
| G19 | R2-2(a) the CLI's `+0.5 h` already includes passing the literal · grok | v2 `:210` | UNVERIFIABLE FROM READS | v2 says the `+0.5 h` is "the proposal's own Q10 estimate, UNVERIFIED"; no measurement exists. |
| G20 | R2-2(b) D1's migrations are `0001`–`0011` and `0016`; `0016` = `d583f6fd`, `0017` = `69c376bd`; no commit creates `drc_stated_books` · grok, gemini (M12) | `02-greps` S6, S7 | HOLDS | = FC2, GK5; S6 lists `0001`–`0011`, `0016_drc(.rollback).sql`; S7 shows `d583f6fd` and `69c376bd`; no line names the table. |
| G21 | R2-2(b) `[F-02]` already keeps a new file, so the literal is not an ALTER of an applied constraint · grok | v2 `:152`, `:154` | HOLDS | v2 `:152` creates `drc_stated_books` in one NEW file; `[F-02]` (`:154`) allows folding only the `drc_rows.kind` widening into `0016`, conditionally. The `via` CHECK lives on the new table. |
| G22 | R2-2(c) `record_day` / `seed_for` have no caller outside their definitions; nothing can call `record_stated_book` today · grok | `02-greps` S3, S1 | HOLDS | = GK13, FC13; S3 lists only definitions, docstring lines and `store.py:235`; S1 empty. |
| G23 | R2-2(c) without a CLI a first import in a K1 + K2 + D2 + D3 deploy cannot be stated · grok | v2 `:214`, `:205-207` | HOLDS | as v2 design: K3 (the form) is the other caller; with K3 unchecked, v2 `[F-10]` names the CLI as the stand-in. |
| M13 | R2-2(c) per `[F-10]` the CLI stands in when K3 is not deployed in time · gemini | v2 `:214` | HOLDS | v2 `[F-10]`: "Otherwise the CLI stands in." |
| G24 | R2-2(c) the CLI writes the same columns as the `/drc` form except `via` · grok, gemini (M14) | v2 `:117-130` | UNVERIFIABLE FROM READS | v2 does not spell the form's column set: the table is `via`, `turn_id`, `readback_sha256` (voice-only), `reason`, `supersedes`, …; neither the form nor the CLI is built. A design statement. |

Two houses contradicting each other (quoted, not smoothed):
- **R2-1(iii)** — Grok: "Not the import ids on its `day` row (`store.py:190`) … the current-import predicate is the smaller rule". Gemini (ADOPT seat): the seat's text, whose executions clause reads "its executions from `drc_fills` of the import ids its own `day` row names (`store.py:190`)". Both mechanisms are named in the files (G10, G11, C2).
- **R2-2(a)** — Grok: "`CHECK IN (drc_page, voice_widget, state_book_cli)`"; Gemini: "ADOPT WITH a third CHECK literal: 'cli'".

Counts (29 rows): claims HOLD 25 · DOES NOT HOLD 0 · UNVERIFIABLE FROM READS 4 (G12, G17, G19, G24) — the runs that settle them: G12 → v2's X9; G17 is a reading of L57's scope, not a run; G19 is an estimate; G24 waits for K1 / K3 to exist.

## Anthropic-seat round-2 claims, file-checked
`date` 12:39:29 (Clock). `tail -n 3` of `reports/drc-overnight-tribunal-fable-r2-2026-09-24.md` printed, as its last non-blank line: `DRC OVERNIGHT FABLE R2 DONE · R2-1: ADOPT WITH/ADOPT WITH/ADOPT WITH · R2-2: ADOPT WITH/ADOPT WITH/ADOPT WITH · owner: 0 · ESCALATE: 2` — starts `DRC OVERNIGHT FABLE R2 DONE `. I read its `## Rulings`, `## Self-attack` and `## Withdrawn from round 1` only after the two houses had finished and the tables above were written; nothing of it reached a house. Closing line `TRIBUNAL R2: BUILD AFTER the R2-1 (i)–(iii) and R2-2 wordings are folded`. Its `## Withdrawn from round 1` lists **3** withdrawn sentences (recorded `WITHDRAWN`, not checked): (1) "The later day N … is re-paired from P's carried book" as an unconditional rule · (2) "If N's seed was STATED, the carried book replaces it (DAS is the truth, R67) …" · (3) "(2) Inputs of each re-paired day: its executions from `drc_fills` of the import ids its own `day` row names (`store.py:190`)". Its `## READING` says it ran blind (its line 1 and `RUN DATE` 12:12:57).

| FR | claim (seat report line) | file:line | verdict | note ≤30 words |
|---|---|---|---|---|
| FR1 | `seed_for` reads only `day < %s` (`:28`) | `store.py:230-231` | HOLDS | = C7; the predicate is `:231`, the SELECT that carries it starts `:230`. |
| FR2 | `seed_for` / `record_day` / `record_import` have no caller on D1 or main; `check_contiguity` only at `store.py:235`; `prior_trading_day` readers `store.py:225`, `daymode/drc.py:152`, `propose.py:380`; `pair_day` only `pairing.py:337` (`:28`, `:104`, `:117-125`) | `02-greps` S3; my `grep -rn -e prior_trading_day -e "record_import("` on the D1 tree; main has no `drc/store.py` | HOLDS | every hit is a definition or the listed reader; = GK13, FC13. |
| FR3 | P recorded with pairing `not computed` (`build_day`, `pairing.py:327-328`); `seed_for(N)` then raises at `store.py:236-244`, so `[F-03]` would refuse P (`:30`, `:139`) | `pairing.py:327-336`, `store.py:236-244` | HOLDS | mechanism: `derived->'not_computed' ? 'pairing'` on the prior day's `day` row raises `PairingError`. The refusal of P is v2 design, not built. |
| FR4 | a leading `B` with no seed opens a long (`:29`, `:46`) | `pairing.py:189-191` | HOLDS | = G2. |
| FR5 | L1 "one contradicted by a stored close, is a loud FAILED" (`:29`) | prompt `27-…:7` INDEX CARD; `LAWS.md:30` | HOLDS | HOLDS as the index card's wording (prompt `27` line 7, also in `23`); the phrase is not in `LAWS.md` L1's text (`:30`, "No plausible-empty artifacts, ever …") — grep of `LAWS.md` and `CLAUDE.md`: none. |
| FR6 | P's carried book is itself rooted in a statement because `earlier` was empty when P was first recorded (`pairing.py:249`) (`:37`, `:140`) | `pairing.py:249-250`, `store.py:227-235` | HOLDS | mechanism only: a first record has no earlier day, so its seed is empty / stated. |
| FR7 | R67's "DAS is the truth" settles DAS against Cobalt's recompute, not a statement for N against a statement for P (`:37`) | `cto-2026-09-22.md` R67 (row 99) | UNVERIFIABLE FROM READS | R67 (1) and (3) are quoted in the row; whether (3) reaches an opening-book statement is a reading of his ruling, not a file fact. |
| FR8 | every parsed stats row is stored exactly once, matched or unmatched (`:67`) | `store.py:170-186`, `pairing.py:266-307` | HOLDS | matched → `stats_row` under its trade (`:170-176`), unmatched → `:180-186`; `match_stats` puts every row in `claims` or `unmatched`, including the early-return branch. |
| FR9 | `StatsRow` rebuilt from `derived.row` at `store.py:175`, `:185` (`:59`) | `store.py:175`, `:185` | HOLDS | both `derived` dicts carry `"row": …model_dump(mode="json")`. |
| FR10 | `match_stats` reads only `MATCH_INPUTS ∩ missing` (`pairing.py:265`); with `not_computed.match` absent the set was empty, so `missing = []` is exact (`:60`, `:142`) | `pairing.py:265`, `:271`, `:333` | HOLDS | `absent = [c for c in MATCH_INPUTS if c in stats.result.missing]`; `not_computed["match"]` is set only when `absent` is non-empty (`:271`) or pairing did not run (`:333`). |
| FR11 | `missing` is stored as no list; it exists only as text in `drc_imports.reason` and `derived.not_computed.match` (`:142`) | `0016_drc.sql:26-42`, `detect.py:116`, `models.py:205`, `:231` | HOLDS | `drc_imports` has no `missing` column; `reason` is `PARTIAL — missing: <cols>` (`detect.py:116`); the seat's `models.py:205` / `:231` are the same string in `partial_flag`. |
| FR12 | a superseding file is committed as current at `record_import` while a failed pairing leaves the `day` row naming file 1 (`:64-65`, `:141`) | `store.py:88-97`, `:116`, `:145`, `:187-197`, `pairing.py:203-218` | HOLDS | = G10; `pairing.py:203-218` is the "contradicts the seed" raise. |
| FR13 | a `failed` newest file is stored with zero fills and becomes current; "current import only" then pairs an empty day and the seed passes through (`:66`, `:143`) | `store.py:83-84`, `:88-97`, `:116`, `:119`, `pairing.py:220-234` | HOLDS | a failed file inserts its `drc_imports` row with `supersedes` = the prior (`:98-118`), no fills (`:119`); `pair_day` with no executions returns the seed as open positions. |
| FR14 | a `partial` import re-pairs to `not computed` exactly as its first record did (`pairing.py:327-336`) (`:58`) | `pairing.py:178-182`, `:327-336`, `store.py:195` | UNVERIFIABLE FROM READS | the first record took `build_day`'s `not_computed` key; a re-pair from `drc_fills` calls `pair_day`, which raises on a `None` column (`:178-182`); `not_computed` survives only on the day row (`store.py:195`). Settled by a K2 test / X9. |
| FR15 | precedent for a caller / source CHECK: `0007_radar_cards.sql:124` `source IN ('cobalt', 'cobalt-degraded', 'human')` (`:78`) | `db_migrations/0007_radar_cards.sql:124` | HOLDS | the line prints verbatim. |
| FR16 | `drc_stated_books`, `record_stated_book`, `via` exist nowhere; `git log --all -S"drc_stated_books" -- src/` is empty (`:78`, `:84`, `:127-129`) | `02-greps` S1; my `git log --all --oneline -S"drc_stated_books" -- src/`; my `grep -rn -w -e via` | HOLDS | = C8; my `git log` printed nothing; `via` only in a `0001_schemas.sql:112` comment. |
| FR17 | `0016_drc.sql` CHECKs are on `drc_imports.kind`, `parse_status`, `event_state`, `drc_fills.side`, `drc_rows.kind` at `:26`, `:30`, `:35`, `:61`, `:86` — none on `via` (`:88`) | `0016_drc.sql:26`, `:30`, `:35`, `:61`, `:86` | HOLDS | each line opened in `22-cited.excerpt.py`. |
| FR18 | `cobalt settings load` has the `--apply` / `--sha256` shape at `settings/cli.py:313-319` (`:100`) | main `settings/cli.py:314`, `:316`, `:319` | HOLDS | `--sha256` `:314` ("required with --apply", `:316`), `--apply` `:319`; the hash verifies a `--card` / `--optional` FILE's bytes (`:101-110`, `:201-204`), not a computed row hash — the seat calls it "the shape". |
| FR19 | `[F-05]`'s `no_trade` row is written by `record_stated_book` on `/drc`; without K3 nothing writes it, so a no-trade Tue makes Wed FAIL contiguity (`:94-95`) | v2 `:88`, `pairing.py:250-254` | HOLDS | v2 `:88` quoted; `check_contiguity` raises when the prior day has no import and no record while an earlier day exists. |
| FR20 | K1 alone is inert: no caller of `seed_for`, `record_day`, `record_import` (`:104`) | = FR2 | HOLDS | = FR2, GK13, FC13. |
| FR21 | L7's interim clause: the desk-relayed chat "approve" is the HITL approval; `--sha256` is its mechanical half (`:100`, `:204`) | `LAWS.md` L7 `[amended 2026-09-16, L61]` | HOLDS | L7 text: "The mechanical half of the approval is `--sha256`: what is applied is byte-identical to what was reviewed." |
| FR22 | `record_stated_book` refuses inside `market_reset` for every caller (`[F-01]`) (`:99`) | v2 `:115` | HOLDS | v2 design text (`[F-01]`, gated by X6); not built (S1). |

Anthropic-seat R2 claims checked: 20 HOLD of 22 checked (FR7 and FR14 are UNVERIFIABLE FROM READS; 0 DO NOT HOLD; 3 WITHDRAWN sentences not checked).

**Facts the second derive needs from the seat file (quoted, not judged — L37):** (a) the seat WITHDREW the round-1 sentence on which both houses' R2-1(ii) `ADOPT seat` rests — "If N's seed was STATED, the carried book replaces it (DAS is the truth, R67) …" — and its ruling is instead: compare N's stated `opening` with P's close, EQUAL → carried, DIFFERENT → FAIL naming N, nothing replaced (`seat report :39-42`); (b) it WITHDREW the executions source ("the import ids its own `day` row names"), which is the sentence Grok objected to in R2-1(iii) and Gemini adopted; (c) it adds a carve-out to (i): P recorded with pairing `not computed` keeps N's stated seed; (d) for R2-2 it names the literal `cli` (as Gemini) and widens the CLI to `--opening` / `--no-trade` / `--resolve` with dry-run and `--apply --sha256`. The houses were blind to all of this.

## Experiments named (L70)
Deduplicated by what they run, against v2's X7, X9, X10.

| experiment | named by | = v2 X<n> or NEW | gates | the result that would change the design |
|---|---|---|---|---|
| X7 — record P with a later day failing its re-pair; then all days pair and a note upsert fails | grok (cited, not restated) | = v2 X7 | K2 | any day half-replaced, or the page showing the old note, or the database rolling back with the note → `[F-03]`'s one-transaction / stale-mark shape changes |
| X9 — supersede day 1's import, re-pair day 2; re-pair an unchanged later day from its fills and stored `stats_row` rows → identical `derived` and `inputs` | grok (cited; adds "whether stored `stats_row` rows rebuild an unchanged day"); seat R2 (cited; adds the failed-current-import → FAIL case and the `StatsRow` round-trip); the runs my UNVERIFIABLE rows G12 and FR14 name | = v2 X9 | K2 | superseded fills paired again (double book), or stats rows only recoverable from the kept file bytes → K2 gains a D2 dependency (R2-1 (iii)) |
| X10 — record Wed stated `flat`, then Tue (a first file) leaving a short open | grok (cited); seat R2 (cited; adds the stated-differs-from-carried FAIL sequence and the P-not-computed sequence) | = v2 X10 | K2 | the trigger stays "superseding file" only → the gap R2-1 names remains |

Gemini named none ("EXPERIMENTS: none"). Grok: "No new X." The Anthropic seat: "No new X." NEW experiments: none.

## OWNER answers
- grok: `none.` (its full sentence in `## Wording offered`) — precondition to build: no.
- gemini: `OWNER: none` — precondition to build: no.
- (the Anthropic seat, not counted: `none. Every sub-item is mechanism.`)
Sub-items on which at least one house answered `OWNER`: 0. No house wrote an owner item as a precondition. `RE-OPENS A RULING`: none by a house — Grok and Gemini both keep R22, R67 ("DAS is the truth"), R90, R93 and 09-23 R39 and answer `ADOPT seat` / `ADOPT WITH` on mechanism; Grok states "R67's 'his held-count statement wins mid-trade' lasts until the export reconciles" and rules "Not OWNER: the reconcile direction is already his ruling".

## Independence
Each `grep -c -F` its own call, 12:25 and 12:36–12:37 ET:
- `grep -c -F -e "-ruling" gemini-ruling-r2.md` → `0`
- `grep -c -F -e "14-grok-r1-own" gemini-ruling-r2.md` → `0`
- `grep -c -F -e "-ruling" grok-ruling-r2.md` → `0`
- `grep -c -F -e "15-gemini-r1-own" grok-ruling-r2.md` → `0`
No house opened another's ruling; neither quoted the other's file name. (Grok names `14-grok-r1-own.excerpt.md`, its own, in its first paragraph — not a breach.) No `READ ANOTHER RULING`.

## L74
One block arrived inside a tool result: appended to the end of the `Read` result of the launch prompt `27-drc-overnight-tribunal-r2.md`, a block in the shape of a system reminder asking for a `Claude-Session: …` line in every commit message and pull-request body and naming a file-send tool (`SendUserFile`). Recorded once, as DATA; not followed (this hub commits nothing and sent no file). The Anthropic seat's own report records the same shape at its `## L74` (`:197-199`).

## ESCALATE
1. **Assumed-book path that HOLDS (question (b), carried from round 1):** the seat's sequence — Tue imported first and stated `flat`, Wed seeded from Tue, then Mon dropped for the first time — passes `check_contiguity` (`pairing.py:249-250`; C1, C7, G4, G5; = round-1 `FC3`, `FC22`) and nothing in `store.py` / `pairing.py` re-checks Tue against Mon's close. Both houses now rule it a re-pair trigger (R2-1(i), 2-0 `ADOPT seat`); it remains a fact of the code at `d1342595` until K2 exists.
2. **Astra's probe row:** `astra: METER` — `ERROR: You've hit your usage limit … try again at Sep 26th, 2026 6:47 AM.` Not launched; the desk seats it again from then (L62 / R19).
3. **The seat's round-2 text withdraws what both houses adopted** (see the block under `## Anthropic-seat round-2 claims`): for R2-1(ii) both houses `ADOPT seat` — the round-1 text the seat now withdraws; for R2-1(iii) Gemini `ADOPT seat` — includes the executions clause the seat now withdraws and Grok objects to. The two houses' texts and the seat's are all quoted above; the second derive counts all three.
4. **A pointer, not a finding (L37):** the seat's R2-1(ii) wording keeps N's stated `opening` and FAILs on a difference instead of replacing it; the houses' wording replaces it with P's carried book. R67 (3) reads "the DAS trading-log import RECONCILES — DAS is the truth; Cobalt's legs are adjusted to DAS (as correction rows, append-only, with the DAS source named, L57)". I take no side on which mechanism that fits; no house's text is marked `RE-OPENS A RULING`.
5. **Disclosures:** (a) rule-string test printed `1` (a line count) for `Bash(grok *)` and `Bash(agy *)`, not the `2` the prompt recorded — ≥1 is the test; (b) `cto-2026-09-25.md` does not exist (recorded, not fatal); (c) one stray Write of mine to a malformed path was refused with `EACCES`, nothing created; (d) I corrected two transcription slips in `02-greps.txt` (one garbled line in S4, four abridged lines in S5) before launching the houses, so the staged file is the verbatim tool output; (e) Grok took ≈ 14 of its 20 minutes; Gemini ≈ 2; neither timed out; (f) `wc -c` of the packet: 120,865 B, no cut; (g) the prompt's `## Rulings table` asked for the Anthropic seat not to be counted — it is not.

No `DO NOT BUILD` from any house (Grok `BUILD AFTER`, Gemini `BUILD`, the seat `BUILD AFTER`). No answer whose supporting claim DOES NOT HOLD (0 of 29 house rows, 0 of 22 seat rows, 0 of 8 round-1 Q3 rows). No owner item written as a precondition. No REDACTION (0 replacements, 0 SHAPE-ONLY drops). No independence breach. No `ASK DESK`.

DRC OVERNIGHT TRIBUNAL R2 DONE · grok: TRIBUNAL R2: BUILD AFTER fold this paste before the K1 migration · gemini: TRIBUNAL R2: BUILD · astra: METER · houses that ruled: 2 of 3 · items converged: 0 of 2 · owner: 0 · ESCALATE: 5
