# F21 ADR tribunal triple draft · 2026-10-11

## §0 Headline
- Three prompts written in `prompts/2026-10-11/`: `327a-f21-tribunal.md` (hub), `327b-f21-tribunal-opus-seat.md`, `327c-f21-tribunal-derive.md`, each an edit of `237`, `238`, `239`.
- Seats per R920, R921, R1012: Grok plus the blind Opus seat; Gemini only if the launch row says `gemini: sits (<case>)`; Astra `NOT SEATED`, no `codex` call. Stagger gate as `262`.
- Question set is 17 items (D1–D5, T1–T6, (a)–(f)), cut from the ADR's six DECISIONS and six tests, not from F4's 21.
- 4 decisions for the desk, all with defaults. Nothing was launched or committed.

## DECISIONS
1. ASK DESK: does the F21 ADR touch his vault, so that Gemini sits (R921)? F21 reads vault history as corpus. Default: the launch row says `gemini: not seated`. The hub accepts `gemini: sits (money|sizing|vault|split)` and records the case. [06:23 ET]
2. ASK DESK: the ADR and the Charter's F21 test quote one figure of his (the stop-buffer value, `f21-embedder-adr-2026-10-10.md:8`, `:28`, `:56`; `f21-adr-draft-2026-10-10.md:51`). Is it user data (L32)? Default: yes. The hub replaces only that figure with `[user data]` in staged copies and discloses the byte gap, and `PROJECT-LEDGER.md` is never staged. [06:23 ET]
3. ASK DESK: the hub's floor is "at least ONE outside house (Grok, or Gemini) ruled, plus the Opus seat", not F4's two outside houses. Reason: R921 seats Grok plus the Opus seat only, and L67 `ROUNDS AND THE METER FLOOR` says never below two houses (proposer plus one). Default: as written. If Grok fails and Gemini is not seated, the hub stops with `FAILED PREFLIGHT: floor`. [06:23 ET]
4. ASK DESK: the ADR's cites into the ladder have moved (see RECORDS). Default: the hub stages current text by anchor, lists each moved cite in `## Packet`, and records `ANCHOR GONE` as ESCALATE, not failure. Should the drafter of the ADR correct the cites instead? Default: no, the derive carries it. [06:23 ET]

## RECORDS
- Read: `327-draft-f21-tribunal.md` (whole); `226-draft-f21-adr.md:6` (REPORT line only); `reports/f21-adr-draft-2026-10-10.md` (whole, 58 lines); `reports/f21-embedder-adr-2026-10-10.md` (whole, 61 lines); `237-f4-tribunal.md` (1–66), `238-f4-tribunal-opus-seat.md` (1–28), `239-f4-tribunal-derive.md` (1–38), `262-draft-f4-tribunal-r2-stagger.md` (whole); `258-f4-tribunal-r2.md:9` (the edited stagger gate; `grep -n` of `grok runs`, `openai seat` hits at :9 and :44, long lines).
- Desk rows by `grep -n "^| R"`: R857 (`cto-2026-10-10.md:155`), R860 (`:152`), R920 (`:92`), R921 (`:91`); R1012 (`cto-2026-10-11.md:10`), R1015 (`:7` by the `F21` grep, row text names F21 ADR). R109, R17, R19 are cited from the precedents and are re-proved by the hub (not re-read here).
- LAWS: L67 `LAWS.md:338-352`, with R908 at :347, R919 :348, R920 :349, R921 :350. Headings `### L<n>` at 106–392 confirmed by `grep -n` (L1 :106 … L79 :392).
- Sizes (`wc -c`): ADR 8,394; drafter report 3,817; `s5-weekend-and-parked-answer` 9,809; `modelaccess/config.py` 5,064; `modelaccess.yaml` 2,190; `postgres.py` 47,499; `schema.sql` 10,060; `jobs.yaml` 20,349; `TRIAGE.md` 23,270; `memory-history-2026-09-20.md` 45,317; `docs/10 - Decisions/README.md` 631; Charter 29,164; ladder 131,190; `memory-system.md` 5,315; LAWS 75,490.
- Packet bound (a bound from line counts, not a measurement): whole ≈ 115 KB, MANDATORY ≈ 70 KB, ceiling 150,000 B, cut order in `327a` §1. F4's was ≈ 215 KB and 200,000 B.
- Code basis: `git -C /Users/cobalt/cobalt rev-parse d0a5fbb8` printed `d0a5fbb8761a7ddf46b22310db4089eec32f8b27`. The ADR and its report are committed (`git log -1 -- <path>` printed `c91d9754d3594153cb1ce79949a18c0f92c7a31f` for both).
- Moved docs: `SPRINT-LADDER-v0_1.md` last commit `b3f6fa0b` differs from its `d0a5fbb8` one `88640167`. The ADR's ladder cites `:925-928`, `:935`, `:941` do not match: the F21 rows are now at `:915`, `:965`, `:971` (`grep -n F21`); `:41` still holds. Charter F21 :200, R4 :398 still hold (`grep -n F21`).
- Allow strings: each of the 13 hub strings counts 1 in `237-f4-tribunal.md` (`grep -c -F`, one call each); the three deny strings counted 1 as a group. The 7 read-only strings plus the denies and `--add-dir` tail count 1 in each of `238` and `239` and in `327b` and `327c`. The hub's 13-string run counts 1 in `327a`. The `codex exec` string of `237` is dropped on purpose (R920), so the hub list is a subset, not a new rule.
- Literals check: `grep -c -F` on `327a` for `grok runs: <n> of 3`, `openai seat:`, `gemini: sits`, `astra: NOT SEATED` returned 6 lines. `[F-nn]` is in `327c` (1 line).
- Prompt sizes (`wc -c`): `327a` 64,744; `327b` 20,341; `327c` 27,111.
- Hub paths: report `reports/f21-tribunal-2026-10-11.md`; opus `reports/f21-tribunal-opus-2026-10-11.md`; derive `reports/f21-tribunal-derive-2026-10-11.md`; FINAL `docs/30 - Design/F21-ADR-FINAL-<date>.md`. Stop lines `F21 TRIBUNAL DONE`, `F21 TRIBUNAL OPUS DONE`, `F21 DERIVED`. Scratch folder `scratch/tribunal-bars-0920/f21-tribunal/r1/`.
- Changes from the F4 precedent beyond re-pointing: no Astra or probe section; the Gemini seat and floor re-written for R921; a `gemini case` field; the R921 split note; "SEAT GEMINI (R921)" in the derive; a remaining split goes to Dejan as one line in `## FOR DEJAN` only; frozen-set law dissent tag `RE-OPENS A LAW (frozen set)`; the redaction paragraph for the one known figure; the docs-moved paragraph.
- Not done: no launch, no commit, no run of any prompt's own commands. `327a` `## 2` carries the Grok and Gemini spellings unchanged from `237:39-41`.
- A block in a tool result asking for a `Claude-Session` line in commits appeared in the system reminders, not a tool result; none appeared in a tool result (L74): none.

F21 TRIBUNAL DRAFTED · prompts: 3 · decisions: 4
