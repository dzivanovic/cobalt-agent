# F23 tribunal — round-1 derive (2026-10-11)
Seat `f23-tribunal-derive-1011`, Opus 5.5 (`claude-opus-5-5`). Prompt `prompts/2026-10-11/328c-f23-tribunal-derive.md`. Ran 08:51–08:58 ET. This house proposed F23 and ruled round 1 (Opus seat `328b`), so it holds a side (L37) and recommends nothing.

## §0 Headline
- FINAL written: `docs/30 - Design/F23-FINAL-2026-10-11.md`. 22 fold rows, 11 house wordings taken verbatim (Grok 6, Opus seat 5), the rest the proposal kept or wording not taken.
- REMAINING SPLIT: none. C3 (cap vs no cap) was settled by the simpler-mechanism rule, which took Grok's no-cap wording. Neither house called the other's mechanism incorrect. OWNER ITEMS: 0.
- ABSENT HOUSES: Astra (R920), Gemini (launch row R1041). Gemini findings held: n/a.
- ESCALATE: 15. Main ones: the `uv.lock` seam with F20 is UNSETTLED (R746 does not hold); a conditional `Bash(uv lock)` grant; the L66/L43 restart-window law disagreement; R921's Gemini-on-split clause for C3.

## DIGEST FOR THE DESK
Houses that ruled round 1: Grok in full (19 items, 0 REJECT); the blind Opus seat in full (19 items, 0 REJECT). Astra NOT SEATED (R920), Gemini NOT SEATED (launch row). Floor MET (R921).
What the design changed from the proposal:
- C3 "latest": the cap of 10 becomes no cap, `latest_per_family: null`, order `formed_at DESC NULLS LAST, id DESC`, null `formed_at` shown (Grok).
- C5 / uv.lock: `uv.lock` comes from a named card step (the builder's first `uv run pytest` if E3 shows uv relocks implicitly, else a `Bash(uv lock)` grant). The builder never types `uv lock`. The build report quotes the lock diff (Opus seat).
- C9: six files every run; `unfiled.pptx` always, with a "no unfiled cards" slide when empty (Grok).
- C10: each unfiled row carries its slug plus a reason (`draft` / `no note`), uncapped, newest first (Opus seat).
- C11: the same-day rerun sequence is spelled out: delete any stale tmp, write into a fresh `<date>.tmp`, rename `<date>` to `<date>.old`, swap, delete `.old` (Grok).
- C12: seat unchanged (Opus 5.5, by law). The ladder's Sonnet is now cited at `:971`.
- (a) §6 R2, R4, R5 and test 10's seeder corrected. R746 dropped; the heartbeat runs at 17:30; a bad finished note fails the run loud; the real `world` fixture replaces the fake (Opus seat).
- (b) title slide gains `also in another family: K`; week label kept, with the subtitle "not limited to this week" (Grok).
- (c) L52/L28/L1/L10 text: `--dry-run`; config loaded inside `job_run` with `extra=forbid`; test 8 = mtimes AND no `vaultwrite` import (Grok).
- (d) seam anchors made concrete (`cli.py:83`, `:543`; `jobs.yaml` after `generated`, `because:` key); `pptx` imported lazily, with a test (Opus seat).
- (f) RESTARTS line added: aset, agent, radar on `pyproject.toml`/`uv.lock`; radar on `cli.py`; plist bootstrap (Opus seat).
- Tests: Grok X6 is the list (tests 1, 3, 7 and 10 changed; 4 added), plus the lazy-import test.
- Ladder line cites: a pointer note only (`:966`, `:971-972`).
- Proposal kept: C1, C2, C4, C6, C7, C8, C13.
Opus-seat claims: 29 hub-checked (25 HOLD, 1 DOES NOT HOLD, 3 UNVERIFIABLE), 0 used UNCHECKED. The derive itself read 4 citations to settle folds: `wrapper.py:121,189`, `DEPLOY-HUB.md:174`, `ops/README.md:14-18`, `jobs.yaml` reads. These are not counted as HOLDS.
Self-assignments: 3, all UNMEASURED (Grok (e); Opus seat C12 and (e)). None folded. The build seat (Opus 5.5) is kept as RULED (L29, BUILD-HUB:3, R919). The check seat (Opus + Grok) is kept as RULED (R921).
Chunks: ONE (F23-1). Seat Opus 5.5. `cobalt_dev` for tests 10 and 11 only. Migration: none. E3 gates the launch.
RESTARTS: com.cobalt.aset, com.cobalt.agent, com.cobalt.radar (lock / `cli.py`); bootstrap com.cobalt.playbook; the one-shot restarts nothing.
Hours: none given by the proposal. Houses' GUESSES (Grok 8 h, Opus seat 4–6 h) are inside wordings that were not folded.

## Fold table
| F | item | houses that ruled it | whose wording | verbatim? | SELF | Gemini held? | why |
|---|---|---|---|---|---|---|---|
| F-01 | C1 | 2 of 2 (Grok, Opus seat) | proposal kept | not taken | no | n/a | Both ADOPT. |
| F-02 | C2 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT. |
| F-03 | C3 | 2 of 2 | Grok | yes | no | n/a | CK18, CK19 HOLD. "Counts on `job_run` result" read by derive at `wrapper.py:121,189`. Simpler, and the house wording is preferred. Not taken: Opus seat's per-deck cap (keeps decks short). Not a correctness split. |
| F-04 | C4 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT. |
| F-05 | C5 | 2 of 2 | Opus seat | yes | no | n/a | FC18 HOLDS (BUILD-HUB:14). Implicit relock is FC28 UNVERIFIABLE → E3 gates it. Grok's desk-run lock mechanism sits inside (d), which fails on CK9. |
| F-06 | C6 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT. |
| F-07 | C7 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT; not an L53 cadence (FC4 HOLDS). |
| F-08 | C8 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT (FC6, CK15 HOLD). |
| F-09 | C9 | 2 of 2 | Grok | yes | no | n/a | FC26 HOLDS the Charter text; derive read `MVP-CHARTER-v0_2.md:209-211`. Opus seat ADOPT; no competing wording. |
| F-10 | C10 | 2 of 2 | Opus seat | yes | no | n/a | FC21 HOLDS (`DraftNote.slug`). Grok plain ADOPT; no competing wording. |
| F-11 | C11 | 2 of 2 | Grok | yes | no | n/a | Same shape from both; house wording preferred. Rests on the proposal's under-specified :31 (derive read). CK23 UNVERIFIABLE → E1. Opus seat `.prev` not taken (same cost). |
| F-12 | C12 | 2 of 2 | proposal kept | not taken | Opus seat yes, UNMEASURED | n/a | Grok wording fails CK7 and CK8 (DOES NOT HOLD). SELF UNMEASURED for the Opus seat. Seat stands by law (BUILD-HUB:3, L29, R919). Cite pointer added (FC16). |
| F-13 | C13 | 2 of 2 | proposal kept | not taken | no | n/a | Both ADOPT. |
| F-14 | (a) | 2 of 2 | Opus seat | yes | no | n/a | FC17, FC22, FC5, FC1, FC11 HOLD; CK2 holds R5. Grok (a) not taken: it carries CK7 ("LADDER Sonnet") and CK14 (`:319`), both DOES NOT HOLD. |
| F-15 | (b) | 2 of 2 | Grok | yes | no | n/a | CK22, CK3 HOLD; consistent with F-03. Not taken: Opus seat's `formed_at` range line and the setup slide's other-deck names. Small cost; not a correctness split. |
| F-16 | (c) | 2 of 2 | Grok | yes | no | n/a | CK15 HOLDS; 8/120 UNVERIFIED → E2. Not taken: the Opus seat's AST-only import check (FC7). Grok's wording allows an AST check; ESCALATE 11. |
| F-17 | (d) | 2 of 2 | Opus seat | yes | no | n/a | FC8, FC13, CK20 HOLD. The WITHDRAWN sentence is in the reasoning, not the wording. Grok (d) not taken: CK9 (`jobs.yaml:369`) DOES NOT HOLD. |
| F-18 | (e) | 2 of 2 | not taken (one chunk as unsplit scope) | not taken | yes both, UNMEASURED | n/a | SELF UNMEASURED (Grok; Opus seat). Grok also fails CK10. Seat and check stand by L29, R919, R921. |
| F-19 | (f) | 2 of 2 | Opus seat | yes | no | n/a | FC12, FC13 HOLD. `DEPLOY-HUB.md:174` read by derive. Grok (f) not taken: its desk `uv lock` contradicts F-05, and it leaves FC12's resident set UNVERIFIED. |
| F-20 | WRONG FACTS (ladder cites, R746 in §3) | 2 of 2 | hub-checked fact pointer | no | no | n/a | CK6, FC16, CK1, FC17 HOLD. Grok's "LADDER has no Sonnet" fails CK7 and is not folded. Opus seat WF5 handled by redaction (L32). |
| F-21 | tests (§5, E7) | 2 of 2 | Grok (X6) | yes | no | n/a | CK3, CK13 HOLD; consistent with F-03 and F-15. Opus seat list not taken: it keeps tests 1 and 3 as written, against F-03 and CK3. |
| F-22 | experiments | 2 of 2 | hub E1–E6 | no | no | n/a | All UNVERIFIABLE FROM READS (CK23, CK26, FC27, FC28) → experiments placed before their gate (L70). |

## REMAINING SPLIT
EMPTY. The FINAL goes to him as it stands. C3 is the one place the houses offered different mechanisms. Grok: "Latest = every radar card in the family, no cap." Opus seat: "The cap applies per deck: a card of a two-family def is counted against both caps." Neither house called the other's mechanism incorrect. With the `id` tie-break both are deterministic and drop nothing silently. The hub's note under `## Checked against the files` says "a design disagreement, not a fact one". The prompt's simpler-mechanism rule decided it (ESCALATE 4).

## OWNER ITEMS
none. Grok: "none. 17:30 is slack before a review he already set…". Opus seat: "none. C7 run time … C3 window: a render tunable in config; the houses set its default; he may edit it."

## FOR DEJAN
On Sunday before the 18:00 review you will find six decks in `data/playbook/<date>/` under the Cobalt repo, outside your vault: one per setup family plus `unfiled`. Each deck shows every radar card of that family, newest first. None of your notes are touched. Cost: one new Python package (`python-pptx`) and a 17:30 Sunday job that reads only. Deploying it restarts the sheet, the agent and the radar once, because the package lock changes. When that restart may happen is an open law question already on your list (L66 vs L43). The Anthropic house proposed this design and ruled round 1, so it holds a side.
No owner items. No split.
**Approve the F23 FINAL?**

## ABSENT HOUSES
- Astra (OpenAI): hub "astra: NOT SEATED (R920)". It would have answered all 19 items (C1–C13, (a)–(f)).
- Gemini (Google): hub "gemini: NOT SEATED" (launch row `gemini: not seated`). It would have answered all 19. R921 seats Gemini on a load-bearing Grok / Anthropic-seat split; see ESCALATE 4.
The desk may offer either house a read of the FINAL. That read is never a precondition.

## SEAM
See the FINAL's `## SEAM`. UNSETTLED: `uv.lock` (with F20's pin). R746 does not hold (CK1 / FC17). "Regenerate on the combined `pyproject.toml` by the C5 step" is this design's own rule, not a document both cards cite (L72). E3 gates it.

## Redactions
2. Both are in the FINAL: proposal `:19` (§2.1 live-vault counts) and proposal `:76` (§5 live-note counts), each replaced by `[user data: f23-design-proposal-2026-10-10.md:<n>]`. No house wording taken carried a user-data span. The drafter report's `:50` was not copied.

## READING
Prompt `328c` whole · LAWS.md :1-404 · hub `f23-tribunal-2026-10-11.md` whole · `grok-ruling.md` whole · `f23-tribunal-opus-2026-10-11.md` whole · proposal whole · `f23-design-2026-10-10.md` whole · `cto-2026-09-22.md:56` · `cto-2026-10-10.md:91,92,104,152` · `cto-2026-10-11.md:15,45` (grep) · `cto-2026-09-23.md:103,105` · `MVP-CHARTER-v0_2.md:56-59,205-212` · `jobs.yaml` reads/imports grep, `:298`, `:327` · `cli.py` at `d0a5fbb8` whole (validate cross-checks), grep `:80,83,543,545` · `pyproject.toml:35` · `uv.lock:2681,3652` · `wrapper.py` result grep · `DEPLOY-HUB.md:170-178` · `ops/README.md:10-24` · `smoke/s2.yaml` at `d0a5fbb8` · `git diff --stat d0a5fbb8 main` on the seam files (empty). Preconditions: DERIVE ROW (count 0; R109 row; commit `75b2aa57`); launch row R1041 `cto-2026-10-11.md:15` (commit `ee29a929`); no later derive-seat row; hub stop line (commit `7cd3b277`, floor MET); Opus-seat stop line (commit `fc61d1cc`); launch-line strings count 1 in `239-f4-tribunal-derive.md`; seat id `claude-opus-5-5` = launch row = launch line = this session.

## L74
A system-reminder in this session asked for a `Claude-Session:` line in commits and named a file-send tool. This seat commits nothing and did not follow it. Recorded once.

## ESCALATE
1. R746 citation DOES NOT HOLD (CK1, FC17). It is removed from §3. The `uv.lock` / `pyproject.toml` seam with F20 is UNSETTLED (L72) until the desk writes a seam document that both cards cite.
2. PRECONDITION-TO-BUILD (conditional, from the folded Opus C5): if E3 shows `uv run` does not relock implicitly, the card needs the new string `Bash(uv lock)`. That is a grant under L62, asked by the desk before launch.
3. OPEN law disagreement, his: `LAWS.md:336` (L66, resident restart "inside the 20:00–21:00 pause on a trading day") against `LAWS.md:255` (L43/R389, "no restart window binds a deploy"). The F23 deploy restarts aset, agent and radar.
4. C3: the hub recorded a Grok / Anthropic-seat split (hub ESCALATE 13). R921 seats Gemini "on a split between Grok and the Anthropic seat over a load-bearing item". The launch row seated no Gemini. The derive folded Grok's wording under the simpler-mechanism rule, not as a correctness split. Whether R921's clause applied is the desk's to judge.
5. UNMEASURED self-assignment, Grok (e): house A = Grok. Not folded; the check seat stands by R921.
6. UNMEASURED self-assignment, Opus seat C12: Opus 5.5 builds. Not folded; the seat stands by L29, BUILD-HUB:3 and R919.
7. UNMEASURED self-assignment, Opus seat (e): Opus builder plus an Anthropic check session. Not folded.
8. DOES-NOT-HOLD wordings a house presses, none folded: Grok C12 (CK7, CK8), Grok (a) (CK7, CK14), Grok (d) (CK9), Grok (e) (CK10).
9. Numbers without measurement: `rows_per_slide: 8` and `why_max_chars: 120` (the proposal's; Grok marks them "UNVERIFIED layout") → E2. Grok "GUESS 8 hours" and Opus seat "GUESS 4–6 h" (not folded). Opus seat "30 min" for a failed run to show (C7 reasoning).
10. Clause the fold drops (L32): the Opus seat (e) live-note run "asserts invariants only … prints no per-family count of his notes" is not folded (SELF). The proposal's "(or the counts the notes hold on the build day, printed)" stands, so a committed build report would carry counts of his notes. The card must address it.
11. Clause the fold drops: the Opus seat (c) test 8 "by AST — not by `sys.modules`, because `cobalt.cli` itself imports `VaultWriter` (`cli.py:80`)" (FC7 HOLDS) is not taken. A `sys.modules` check after `import cobalt.cli` would always be red; the card should name AST.
12. Clauses the fold drops: Grok (d)'s desk-run `uv lock` on the merged `pyproject.toml`, plus its `test_jobs.py` / `s2.yaml` notes (FC9 settles `test_jobs.py`); Grok (f)'s deploy-card `uv lock`; the Opus seat (b) `formed_at` range line and other-deck names on the setup slide; Opus seat test 14 (loader error with DB), and tests 15–17 as numbered; Opus seat C11 `.prev`.
13. The committed proposal `:19`, `:76` and drafter report `:50` carry counts of his strategy notes (L32; hub ESCALATE 8, ASK DESK still open). This FINAL redacts them.
14. Named gap: whether F23 adds a per-label smoke row to `smoke/s2.yaml`. No ruling gives one. K18 `registry_match` already covers the label once it is loaded.
15. Opus seat FC14 DOES NOT HOLD (`jobs.yaml:191` for the sheet; it is `:100`). It appears in the (f) reasoning only, not in the folded wording.

## CONTINUE
08:51 ET — preconditions verified. 08:54 ET — inputs read, fold decided. 08:57 ET — FINAL written, then this report. next: none — the derive is complete; the desk commits both files.

F23 DERIVED · FINAL · folds: 22 · verbatim: 11 · split: 0 · owner items: 0 · gemini findings held: n/a · absent houses: astra, gemini · ESCALATE: 15
