# Float-handicap tribunal R2 — draft report (2026-09-22)

Seat `handicap-r2-draft-0922` · Opus 5 · prompt `prompts/2026-09-22/18-draft-handicap-r2.md` · 11:10–11:18 ET (`date`) · three prompts written, nothing launched or committed.

## DIGEST
- **R2-1 (gates H1):** does R28's "competes on its LOWERED score for the pool's 50" mean a handicapped name competes across `priority` / `first_from` (B, pool-wide, Fable), or only inside its tier (A, tier-bound, grok)? Under A, does H2 change the position basis?
- **R2-2 (gates H2):** does `handicap_cap` get stored as an additive `ExcludedBy` value (two CHECKs and a migration, grok) or as a JSONB `handicap.decisive` flag with no migration (Fable)? And is the counterfactual a second full `decide()` or the O(1) `winners[-1]` comparison?
- **`19` (Sonnet hub, Grok + Gemini):** stages the fold only, about 95 KB: NEEDS-ROUND-2 verbatim, the v2 sections carrying the two items, 4 round-1 hub-check rows, the Fable seat's round-1 wording, each house's own round-1 excerpt (its own only), 7 code excerpts, `greps.txt`. It asks 4 questions (R2-1.1, R2-1.2, R2-2.1, R2-2.2), and the answers are `ADOPT A | ADOPT B | ADOPT WITH | OWNER (his — why)`. It file-checks the Fable claims C1–C9 while the houses run. The Astra probe is carried and its result recorded: METER → skipped (R13).
- **`20` (Fable seat, blind):** the same four questions. It attacks its own round-1 text first, and `OWNER` is allowed with the why plus the default H1 builds.
- **`21` (Fable derive):** writes v3 = `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md`. An item converges only with at least one house in the agreement. An `OWNER` answer from any house goes to OPEN FOR DEJAN (L53). A split gets one A/B per item, never a vote.
- **New rule strings: 0** (proof below).
- **Launch order:** `20` beside `19` → both stop lines committed → `21`. `19` gates itself: the date must be 2026-09-22, the time outside 19:25–20:45 and before 23:20 ET, and `17` must have stopped. `17` ended on its stop line (checked 11:17), so the stagger passes now.
- **Stop lines to watch:** `19` `^(FLOAT HANDICAP TRIBUNAL R2 DONE|FAILED)` · `20` `^(FLOAT HANDICAP TRIBUNAL FABLE R2 DONE|FAILED)` · `21` `^(FLOAT HANDICAP DERIVED v3|FAILED)`.

## RULE PROOF
Each string was counted with `grep -c -F -e` in the new file and in its precedent. Every count is new|precedent.

| new file | precedent | strings checked | counts |
|---|---|---|---|
| `19-handicap-tribunal-r2.md` | `38-float-handicap-tribunal.md` | 14 allow + 3 deny; `--model claude-sonnet-5`; `--permission-mode auto`; `` `cd /Users/cobalt/cobalt-wt/agy-trial` ``; `` `claude --bg "Read ``; `--remote-control`; the three `--add-dir`; grok `--sandbox cobalt-job --allow "Write(…/tribunal-bars-0920/**)"`; the agy `--print="` spelling; the codex probe | all 1|1 |
| `20-handicap-tribunal-fable-seat-r2.md` | `39-float-handicap-tribunal-fable-seat.md` | 7 allow + 3 deny; `--model claude-fable-5-1`; `--permission-mode auto`; cd; `claude --bg`; `--remote-control`; add-dirs | all 1|1 |
| `21-handicap-tribunal-derive-r2.md` | `40-float-handicap-tribunal-derive.md` | same as `20` | all 1|1 |
| whole span `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` | 38 / 19 · 39 / 20 · 40 / 21 | one span each | 1 in every file |
| approved sources | `08-bars-chunk-e-check.md` (the 17 strings) · `22-draft-setups-tribunal.md` (the 10 strings) | — | every count 1 |

**NEW strings: none.** Across the three launch lines, only the prompt path and the `--remote-control` name differ from the precedent (`float-handicap-tribunal-r2-0922` · `float-handicap-tribunal-fable-r2-0922` · `float-handicap-tribunal-derive-r2-0922`). `21` drops `40`'s "THE DESK replaces `--model`" clause because R30 has already fixed `claude-fable-5-1`. No value of his appears in any of the four files: `grep` for `500`, `million` and decimal factors across the three prompts found none. `19` also carries no Astra launch spelling, only the probe.

## EXPERIMENTS
v2's `## First-gate experiments (L70)` lists four experiments that gate the round-2 items:

| X | what it runs | runnable by a house from reads? | gates | H1 build prompt runs it first? |
|---|---|---|---|---|
| X2 | re-run `decide()` on the stored 09-18 RTH cache; the marginal seat's tier; `first_from` screen counts against `cap` | no (needs code run on the cache) | R2-1, then H1's dry-run wording | **yes** |
| X13 | time `decide()` plus one extra `decide()` per `config_cap` name, or the re-sort + `decisive` | no (a timed run) | R2-2, then H2 | no (H2's prompt) |
| X15 | dry-run: do not-equity rows distort `effective_position`? | no (a dry-run on the retained cache) | R2-1 position basis, then H2 | no (H2's prompt; only if R2-1 = A and R2-1.2 needs it) |
| X16 | on `cobalt_dev`, re-add the four-value CHECK with a `handicap_cap` row present | no (a database) | R2-2, only if the enum survives; H2 rollback | no (H2's prompt, conditional) |

None of the four can be run from reads, as expected. `19` and `20` tell the houses to cite these experiments, not restate them. **Experiments for H1: 1 (X2).** v2's other H1 gates (X1, X3–X11) sit outside round 2 and are the H1 prompt's to schedule. I launched nothing.

## ESCALATE
1. **`16` against `19`.** `19`'s stagger row gates only on `17`, as `18` specified. `16-setups-check-r2.md` also carries `Bash(grok *)`, and no report of it exists yet (11:17). Nothing in `19` stops the desk launching `16` and `19` together, so the desk has to keep one Grok/Gemini hub at a time by hand.
2. **Astra probe UP (not expected).** My safe default: record it and do NOT launch Astra, plus an `ASK DESK`. `19` carries no Astra spelling (R13 runs this week without Astra), and drafting one would be new. Desk: accept, or re-issue `19` (L19).
3. **R2-1 will be ruled without X2 / X15 facts** (the derive said they "inform it and run first"; no seat can run them today). Both round-1 seats already named the crossing as his, so an `OWNER` answer is likely. `21` then routes it to OPEN FOR DEJAN, and H1 waits on his A/B. `19` and `20` require any `OWNER` answer to name the default H1 builds.
4. **Question split.** The derive's R2-1 carries two questions (the crossing, and the position basis under A), and R2-2 carries two ((i) storage, (ii) predicate), so each prompt asks four questions under two items. `items converged: <n> of 2` counts items, not questions.

L74, recorded once: a block asking for a `Claude-Session` commit line and naming a file-send tool arrived as a system reminder, not inside a tool result. This seat commits nothing either way.

HANDICAP R2 PROMPTS DRAFTED · prompts: 3 · items: 2 · new rule strings: 0 · experiments for H1: 1 · ESCALATE: 4
