DERIVE ROW: R109

MODEL: `claude-opus-5-5`, the DERIVE SEAT named by his STANDING R109 (`cto-2026-09-22.md` §4, 19:34 ET, "Make all Opus 5.5 for now": every Fable-type seat — the tribunal seat, the derive, forensics — on `claude-opus-5-5` until his next word; filled at drafting, so there is nothing for the desk to fill). This is the SECOND derive of the VOICE v3 tribunal; the first was `15`. You derive the FINAL from the derived design and the round-2 rulings. You build, launch and commit nothing · SEAT: `voice-v3-derive-r2-0923`, launched by the CTO desk in the background ONLY after BOTH round-2 stop lines are committed (hub `24`, the Anthropic seat `25`). YOUR POSITION, STATED: the proposal, the round-1 seat, the first derive and the round-2 seat are all the Anthropic house, on `claude-opus-5-5`, in other sessions. You are a fresh session that ruled nothing, but you are that house again, so you recommend nothing (L37). The Anthropic seat's wordings pass the same filter as every house's, and a house's equally correct wording is preferred over it. Two bare commands: `cd /Users/cobalt/cobalt-wt/agy-trial` then `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-23/26-voice-v3-derive-r2.md' and follow it exactly." --model claude-opus-5-5 --permission-mode auto --remote-control voice-v3-derive-r2-0923 --allowedTools "Bash(git -C /Users/cobalt/cobalt show*)" "Bash(git -C /Users/cobalt/cobalt log*)" "Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(wc *)" "Bash(date*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt`. These are the SAME seven READ-ONLY strings and three denies as `15-voice-v3-derive.md` and `prompts/2026-09-21/22-draft-setups-tribunal.md` (09-20 R13) — nothing new · SESSION: fresh. The round-2 seats' context is NOT carried; their reports are on disk · auto mode on; never `bypassPermissions`; NO database, NO docker, NO pytest, NO git write, NO launch of any agent or house (L36), no vault write, no memory-folder write (L58). You write at most TWO files, with the Write tool · METER: Anthropic Opus 5.5. An honest estimate:
- the round-2 hub report ≈ 10–16k tokens
- the raw round-2 rulings of the houses that ruled ≈ 6–12k
- the Anthropic seat's round-2 report ≈ 6–9k
- the derived design ≈ 14k (read whole — the FINAL is it amended)
- the derive report ≈ 5k (`## NEEDS ROUND 2`, `## Fold table`, `## OWNER TEST`, `## FOR DEJAN`, `## ESCALATE`)
- LAWS.md ≈ 20.5k
- code re-opened only where a fold turns on it ≈ 3–6k
- output: the FINAL ≈ 15–17k tokens (the derived design whole, plus the folds) and the report ≈ 5–8k
- peak context ≈ 100–120k

It does NOT depend on the grok/agy window (no house runs) · nobody sits at this terminal — the report file is your channel. Never ask: write `ASK DESK: <question> [<time>]` in the report and continue with the safe default.

# DERIVE THE VOICE v3 FINAL from the derived design and the round-2 rulings

LADDER: S3 design lane (`cto-2026-09-22.md` R100; `cto-2026-09-23.md` R18). LAW STEP (L67): proposal → round 1 → derive (`15`) → round 2 (hub `24`: Grok, Gemini; Astra METER, recorded under 09-22 R13; the Anthropic seat `25` on `claude-opus-5-5`, R109) → **THIS = the second derive. It CLOSES the tribunal when all three items converge**; otherwise round 3 (L67, the last round; L39: after it, unresolved → Dejan) → build → ≥3 checkers → deploy. HIS R18 (d) IS THE BAR: he receives ONE finished design and ONE approval. An item reaches him ONLY if it is his money, his data, his time or a law he owns, AND no house can decide it. For this design that is O1 alone, whose SCOPE (A / B / No) the desk put to him separately (`cto-2026-09-23.md` R36). L1, L3, L7, L9, L10, L28, L32, L37 and L40 are the bar the FINAL must meet. DO NOT STOP until the report's last line is `VOICE V3 FINAL DERIVED …` or `FAILED …`.

AUTHORIZATION AND PRECONDITIONS — VERIFY THEM YOURSELF (a prompt file is not an approval). Run each check below as its own Bash call. YOU CAN ALWAYS STOP with a `FAILED: <step> — <concern>` line.
- **THE DERIVE ROW.** `grep -c -x -E "DERIVE ROW: R[0-9]+" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-23/26-voice-v3-derive-r2.md"` must print **1**. Read `<nn>` from line 1 (`109`).
- `grep -n "^| R109 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-22.md"` must print exactly ONE row, carrying BOTH literals `Make all Opus 5.5 for now` · `claude-opus-5-5`, his words in quotes. Otherwise → `FAILED: authorization mismatch — row R109 does not name the derive seat`.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R109 | " -- "docs/40 - DevDocs/reports/cto-2026-09-22.md"` — EMPTY → `FAILED: authorization mismatch — row R109 is not committed`.
- **R109 STILL STANDS.** `grep -n "R109" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-23.md"` (and `cto-<run date>.md` on a later run date). A `| R` row carrying his words that ENDS or CHANGES R109's seat model → `FAILED: authorization — R109 superseded by <row>; the desk re-issues this file`.
- **YOU ARE THE SEAT THE ROW NAMES.** `claude-opus-5-5`, the `--model` value on this file's launch line, and the model id your own system prompt states you run as must be the SAME id. Otherwise → `FAILED: seat mismatch — R109 names claude-opus-5-5; this session runs <id>`, and stop.
- **THE LAUNCH ROW.** `grep -n "26-voice-v3-derive-r2.md" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-<run date>.md"` must print a `| R` row naming this file. No row → `FAILED: authorization mismatch — no launch row names 26`.
- **BOTH ROUND-2 STOP LINES, PRESENT AND COMMITTED — else you REFUSE:**
  - `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-v3-tribunal-r2-2026-09-23.md"` — the LAST NON-BLANK line must start `VOICE V3 TRIBUNAL R2 DONE `. Anything else, including the in-progress line, `FAILED` and a missing file → `FAILED: refused — hub round 2 not done — last line: <line verbatim>`.
  - `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r2-2026-09-23.md"` — must start `VOICE V3 TRIBUNAL FABLE R2 DONE `. Otherwise → `FAILED: refused — Anthropic-seat round 2 not done — last line: <line verbatim>`.
  - `git -C /Users/cobalt/cobalt log -1 --format=%H -S"VOICE V3 TRIBUNAL R2 DONE" -- "docs/40 - DevDocs/reports/voice-v3-tribunal-r2-2026-09-23.md"` and `git -C /Users/cobalt/cobalt log -1 --format=%H -S"VOICE V3 TRIBUNAL FABLE R2 DONE" -- "docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r2-2026-09-23.md"` — either EMPTY → `FAILED: refused — <report> stop line is not committed on main`.
- **A HOUSE MUST HAVE RULED.** If the hub's stop line shows `houses that ruled: 0 of 3`, or its `## Rulings table` shows no house (Grok or Gemini) answering ANY of R2-1, R2-2, R2-3 with `ADOPT` / `NEITHER` → `FAILED: no house ruled round 2 — the desk relaunches 24`. The Anthropic seat alone never settles an item: it holds one side of every item, and its house proposed the design.
- **ASTRA (09-22 R13).** The hub's `astra:` field is `METER — proceed on three` or `SKIPPED — R13 (probe UP, recorded)`. This is RECORDED, not a refusal: derive from the seats that ruled, mark the FINAL's header `ASTRA PENDING (R13)`, and name in §0 that Astra reads the FINAL on Sat 09-26.
- **THIS LAUNCH LINE ADDS NO RULE.** Run `grep -c -F -e "<rule>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-21/22-draft-setups-tribunal.md"` for each of the seven allow strings and the three deny strings, quotes included. Each must count **≥1**.
- **HIS O1 ANSWER, IF GIVEN.** Run `grep -n "O1" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-23.md"`, and the same on each later desk file through `cto-<run date>.md`, one call each. His ANSWER is a `| R` row that carries HIS WORDS in quotes and answers the desk's O1 A / B / No on the VOICE L28 scope. A DESK row marked "NO WORDS OF HIS" / "DESK RECORD" never counts. Record the row and his words VERBATIM in the report. He answered twice → the LATER row stands, and both are quoted. He has not answered → `O1: open`. A row whose words you cannot read as A, B or No → quote it, `O1: open`, and `ASK DESK: <row> — read as A / B / No? [<time>]`. You never infer his answer.

INDEX CARD — read in this order:
1. `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` in full (L59). Binding here:
   - **L1**, **L3**, **L7**, **L9**, **L10**, **L19**
   - **L28** — his law; O1 amends it ONLY by his ruling, and the desk applies the fold under L58, never you
   - **L32** — the FINAL and your report are COMMITTED: no audio, transcript, note line, ticker, price or P&L of his
   - **L35**
   - **L36**
   - **L37** — you derive; a SPLIT is carried, never settled by count; a seat that holds a side recommends nothing to him
   - **L38 / L40**
   - **L39** — ≤3 rounds; round 3 is the last; unresolved after it → Dejan; a law file is never voted
   - **L42**
   - **L48**
   - **L52**
   - **L58** — you write no memory or law file
   - **L67**
   - **L68** — migration NUMBERS are the gate's
   - **L70**, **L71**, **L72**, **L73**, **L74**
   - CLAUDE.md's absolute boundary: nothing in the FINAL reads, writes or infers from his trading platform, and no order is ever placed.
2. THE ROUND-2 RULINGS:
   - The hub report, `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-v3-tribunal-r2-2026-09-23.md`, whole: `## Rulings table`, `## Wording offered, verbatim`, `## Anthropic-seat round-1 claims, file-checked` (C1–C8), `## Checked against the files`, `## Experiments named (L70)`, `## OWNER answers`, `## Independence`, `## ESCALATE`. Its HOLDS / DOES NOT HOLD tables are your filter.
   - The raw round-2 rulings of every house that ruled, in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-v3-tribunal/r2/` (`grok-ruling-r2.md`, `gemini-ruling-r2.md`). The raw file is what "verbatim" means, but you never copy a user-data span out of it.
   - The Anthropic seat's round-2 report, `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r2-2026-09-23.md`. Its SELF-ATTACK and WITHDRAWN lines bind you: a sentence that seat withdrew is never folded. The hub checked the seat's ROUND-1 claims only (C1–C8), so a round-2 seat claim the hub did not check is UNCHECKED. You may rest on it only after opening the file it cites yourself, and the fold row then says `UNCHECKED by a hub — read by the derive at <file:line>`, as `15` did.
3. The derived design, `/Users/cobalt/cobalt/docs/30 - Design/VOICE-v3-derived-2026-09-23.md`, whole. Also the derive report `reports/voice-v3-derive-2026-09-23.md` (`## NEEDS ROUND 2`, `## Fold table`, `## OWNER TEST`, `## FOR DEJAN`, `## ESCALATE`).
4. Only where a fold turns on it: the real file a file-check cites — read it to check, never to copy.

THE RULES OF THIS DERIVE — `15`'s rules, UNCHANGED, plus the closing rule of `prompts/2026-09-22/37-s3-exits-tribunal-derive-r2.md`, adapted to R18 (d):
- **Take a wording VERBATIM.** Take a house's `NEITHER` replacement, the position text an `ADOPT <letter>` names (quoted in the derive report's `## NEEDS ROUND 2` and in `24`'s QUESTIONS-R2), or — for R2-2 — the `FOLD A:` / `FOLD B:` lines of a seat whose answer converged, the hub having checked them as that position's mechanics verbatim. Take it word for word, or not at all: you choose, and you never blend, edit or improve. A wording whose supporting claim DOES NOT HOLD in the round-2 hub's file-check, or that the Anthropic seat WITHDREW in round 2, is NOT taken.
- **When an item is CONVERGED.** Count the SEATS that ruled it: the houses (Grok, Gemini) plus the Anthropic seat. An item is CONVERGED when:
  - (i) every seat that ruled it gave the same answer — `ADOPT` the same letter (for R2-3 `ADOPT A`, also the same slice), or `NEITHER` texts the hub's file-check shows are the same mechanism — **with at least one HOUSE among them**; or
  - (ii) every HOUSE that ruled it gave the same answer, and the Anthropic seat's contrary answer rests on a claim that DOES NOT HOLD in the hub's C1–C8 or file-check table, or that the seat itself WITHDREW.

  The Anthropic seat's answer alone never settles an item. Everything else is STILL SPLIT.
- **Prefer the smaller mechanism** only BETWEEN texts the seats agree are correct. A disagreement about correctness is a split.
- **NOT CONVERGED → `## NEEDS ROUND 3`, never settled by you and never sent to him (R18 (d): design questions are the houses'; L67: round 3 is each house's last; L39: only what round 3 leaves unresolved reaches him).** Write ONE block per item: the positions VERBATIM, each seat's reason in ONE sentence with its `file:line`, the file-check rows that decide nothing yet, and the question round 3 must answer. A house's closing `TRIBUNAL R2: DO NOT BUILD …` whose defect HOLDS in the hub's file-check also goes to `## NEEDS ROUND 3`, with its text verbatim.
- **THE FINAL IS WRITTEN ONLY WHEN ALL THREE ITEMS CONVERGED.** With any item in `## NEEDS ROUND 3`, you write the report ONLY. The derived design stays the round-3 input, and no file named FINAL exists before the tribunal closes.
- **His R18, R92, R93, R99, R100 are NEVER re-opened.** A round-2 wording that refuses trading-logic requests as a class, keeps audio, adds a second widget, or narrows 'any command' is NOT folded. It is carried in `## Dissents, verbatim` and named in `## ESCALATE` as `RE-OPENS A RULING (<R-row>)`.
- **O1's SCOPE is his; its MECHANICS are R2-2's.** The FINAL's `## OWNER ITEMS` carries O1 with the converged `FOLD A:` and `FOLD B:` texts, verbatim, beside each other. When he has ANSWERED (the check above), mark the text of his scope `RULED <A|B> — <row>, his words: "<verbatim>"`, the other `not ruled — record`. His "No" → both are marked record, and the V3 his-text class stays off (§6, §9 — his answer quoted where the design says "only if O1 is ruled"). The FOLD into LAWS.md is the desk's under L58, at his approval — never yours; the FINAL states that as a fact.
- **Invent nothing.** Add no mechanism, number, key, slice, file or hour that no round-2 wording or earlier text contains. **Engine tunables are the houses'**: a proposed VALUE is recorded as `<key>: value proposed by <seat> — <file>:<line>`, and taken only with its measurement. **Every "not checkable from reads" claim becomes a first-gate experiment** in the FINAL's list, placed before the slice it gates (L70). A round-2 experiment that repeats a derived E / X row is merged into that row and attributed, never duplicated. **Dissents carried VERBATIM**: `## Dissents, verbatim` gains every round-2 answer the FINAL does not follow, with seat and item. **No user data** (L32): each span is replaced by `[user data: <file:line>]` and counted.

WRITE (Write tool):
- **ONLY WHEN `converged: 3 of 3`:** `/Users/cobalt/cobalt/docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`. Use this name WHATEVER the date of the run. It is the derived design, whole, with each round-2 point REPLACED in place by the converged wording, verbatim, and tagged `[R2F-nn]` (a row of your fold table). The round-2 points are:
  - the header's "Open after round 1" line;
  - §2.4's `[F-22]` note ("who else may delete them is R2-1") and its `[F-07 — OPEN, R2-3 …]` marker;
  - §5's `[F-12 — OPEN, R2-1 …]` marker and the crash-leftover bullet;
  - §9's V4 row ("R2-1 for the `voice_scratch` probe's delete-or-count"), and the slice that R2-3 names (its row, hours, dependencies and RESTARTS exactly as the converged wording states them — a new V5 row only if that wording adds one);
  - the total hours line — recomputed ONLY from the rows' own numbers, with the arithmetic shown in the report; the words "GUESS / UNVERIFIED" are kept;
  - `## L52 and the bar`'s L7, L28 and L40 lines;
  - `## OWNER ITEMS` (O1: the round-2 fold texts, and his answer if given);
  - `## Dissents, verbatim` (extended).

  The FINAL also carries:
  - a header naming the derived design, the round-2 hub report, the raw rulings of every house that ruled round 2, the Anthropic seat's round-2 report, the fold table's path, R18 / R92 / R93 / R99 / R100 / R109, and `ASTRA PENDING (R13)`;
  - a `## Status after round 2` section: per item, converged and whose text, and the slice each gates;
  - `## First-gate experiments (L70)` = the derived list plus every round-2 experiment the fold takes;
  - `## L52 and the bar`, re-answered for the FINAL;
  - `## FOR DEJAN` as the LAST section, holding EXACTLY two entries:
    - (1) **O1**, in HIS terms. If open: what he would say to the widget, what he would hear back, what changes in which note, and the ONE question — **A** (his text outside the units that hold his dictated answers) / **B** (there AND inside those units) / **No** — naming that it is a law he owns (L28) and why no house can decide it, ≤4 lines, NO recommendation (L37). If answered: one line, `O1 — ruled <A|B|No>, <row>: "<his words verbatim>"`, and nothing asked.
    - (2) the ONE approval R18 (d) promises: `APPROVE: the VOICE v3 FINAL design (docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md, sha256 taken by the desk at commit) for build — yes / no`.

  Nothing else goes in it. Committable: no user data.
- **ALWAYS:** `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-v3-derive-r2-2026-09-23.md`. Layout, in this order:
  - §0 Headline ≤5 lines: converged / round 3, whose text, FINAL written or not, O1 open or ruled, Astra pending.
  - `## DIGEST FOR THE DESK` (≤30 lines): per item, converged or NEEDS ROUND 3, and whose text; the slice R2-3 names and its hours; V4's probe under R2-1; the O1 fold texts' mechanics under R2-2; the seats that ruled round 2; what the build prompts wait on (the S1 seam; DRC D2 + D3; the first-gate experiments).
  - `## Fold table` — `R2F-nn · item (R2-1, R2-2, R2-3; a sub-point where a fold turns on one) · seats that ruled it (<n>, named) · answers (per seat) · whose wording · adopted verbatim? yes / no / not taken · why (≤25 words, citing the round-2 hub's file-check row or C<n>, or UNCHECKED by a hub — read by the derive at <file:line>, or RE-OPENS A RULING (<R-row>))`.
  - `## NEEDS ROUND 3` (the blocks; `none` when empty).
  - `## OWNER TEST` — every item any round-2 seat sent him · PASSES / FAILS · where it went.
  - `## FOR DEJAN` — the FINAL's section, copied, or, with no FINAL, O1 alone and `APPROVE: not yet — round 3 owed on <items>`.
  - `## Redactions` (count, and where)
  - `## READING`
  - `## ESCALATE` — every `RE-OPENS A RULING`, every DOES-NOT-HOLD wording a seat still presses, every owner item a seat wrote as a precondition, every `ASK DESK`, and the hours recomputation if it changed the total.
  - `## CONTINUE`
  - the last line.

  Write it in the same turn as the work (L48). While you work, the last non-blank line is EXACTLY `(run in progress — next step under ## CONTINUE)`. The breadcrumb lives inside `## CONTINUE` only. No other line may START with `VOICE V3 FINAL DERIVED`, `FAILED` or `CONTINUE`. RECOVERY (L60): a relaunch first runs `ls` on both file paths, reads its own report first, and continues from `## CONTINUE`. A FINAL already written is re-read, never re-derived from scratch. One command per Bash call, bare shape, no pipe, no redirect. Use `date` for every time you write.

STOP LINE (the last non-blank line of the report, L71): `VOICE V3 FINAL DERIVED · converged: <n> of 3 · round 3: <n> · O1: <open|ruled A|ruled B|ruled No> · FINAL: <written|not written> · ESCALATE: <n>` — or `FAILED: <step> — <reason>`. Here `converged` counts ITEMS marked converged and `round 3` counts `## NEEDS ROUND 3` blocks. Then stop.

NEXT STEP, not yours:
- `FINAL: written` → the desk commits both files and brings him `## FOR DEJAN`: O1 if open, then the ONE approval, one per message. On his approval of the FINAL (and his O1 scope), the desk folds the L28 amendment under L58 and drafts the build prompts: the first-gate experiments first, then V1, ordered against the S1 seam and the DRC build at the L68 gate.
- `round 3: n` → a round-3 hub, seat and derive are drafted for the listed items only (L67: the last round).
- In every case, Astra reads the FINAL on Sat 09-26 (09-22 R13).
