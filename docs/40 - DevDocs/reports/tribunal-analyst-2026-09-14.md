# Trading-desk analyst design tribunal — 2026-09-14

Hub: Sonnet 5 (launches, collects, verifies files; never judges the
design). Workspace:
`Vault/Think/0 - Inbox/tribunal-analyst-2026-09-14/{inputs,fable,astra,grok,rounds}/`
— each seat wrote only its own folder. Nothing under `~/cobalt` was
written by any seat; only this report.

## STEP 0 — inputs (read-only; byte sizes at copy time)

| path | bytes |
|---|---|
| `inputs/LAWS.md` (whole, canonical current law) | 40102 |
| `inputs/prior-final/fable-FINAL.md` | 11360 |
| `inputs/prior-final/astra-FINAL.md` | 6970 |
| `inputs/prior-final/grok-FINAL.md` | 8128 |
| `inputs/prior-final/tribunal-grok-2026-09-14-hub-report.md` | 14789 |
| `inputs/GROKBOT_CHIEF_OF_STAFF_INSTRUCTIONS.md` | 4910 |
| `inputs/PEER_REVIEW_DESK_SPEC.md` | 6715 |
| `inputs/COS_VISUAL_AND_TWOWAY.md` | 1238 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/card-spec.md` | 6908 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/decisions.md` | 3880 |
| `inputs/MVP-CHARTER-v0_2.md` | 29164 |
| `inputs/radar-schema.md` | 2763 |
| `inputs/grok-launcher-diag-2026-09-14.md` | 6088 |
| `inputs/entry-variables.md` (hub-written, cited facts) | ~5900 |
| `inputs/rulings-2026-09-14.md` (hub-written, verbatim rulings) | ~2100 |

All fourteen source inputs verified present before copy; both hub-authored
files (`entry-variables.md`, `rulings-2026-09-14.md`) built only from
cited file:line reads, listed in full in the workspace.

## Codex meter probe (L47, before R1)

```
cd .../astra && codex exec --skip-git-repo-check \
  "Run: wc -l LAWS.md -- reply with only the number." < /dev/null
```
Exit 0. Model `gpt-6-astra`, sandbox `read-only` (probe only — R1 itself
ran `-s workspace-write`). Ran `wc -l` itself, replied `310`, matching the
known-answer (`inputs/LAWS.md` copy in astra/, 310 lines, consistent with
the canonical file). No usage-limit text anywhere in the output. **Astra
cleared to launch on time; no wait-exception triggered.**

## STEP 1 — R1 launches

Identical prompt to all three seats (`prompt-r1-common.md`, copied into
each seat's own workspace with the Grok-only addendum appended for Grok),
citing every STEP 0 input by path.

| seat | launch line | exit | start | end | wall-clock |
|---|---|---|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 --permission-mode acceptEdits --permission-prompts none --allowedTools "Read" "Edit(.../fable/*)" "Write(.../fable/*)" --disallowedTools "Bash" --add-dir /Users/cobalt/Vault --add-dir .../tribunal-analyst-2026-09-14 < prompt-r1-fable.md` | 0 | 10:37:59 | 10:48:29 | 10m30s |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r1-astra.md)" < /dev/null` (cwd astra/) | 0 | 10:38:00 | 10:43:49 | 5m49s |
| Grok | `grok -p "$(cat prompt-r1-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto --output-format json` | 0 | 10:38:02 | 10:46:28 | 8m26s |

Non-fatal note: Fable's launch again printed the same advisory as the
prior tribunal — its `Write(path)` allow-rule isn't matched by file
permission checks (only `Edit(path)` rules are). It proceeded and wrote
both files via the Edit path regardless; both artifacts exist and are
non-empty.

### R1 file verification (L35 — hub verified existence + non-empty size directly, never took a seat's own claim)

| seat | DESIGN.md | OPEN.md |
|---|---|---|
| Fable | 28802 bytes | 3749 bytes |
| Astra | 34029 bytes | 2852 bytes |
| Grok | 21301 bytes | 3098 bytes |

All six files exist and are non-empty. **R1 COMPLETE.**

### R1 substance, one line per seat (from each seat's own recap, not re-litigated by the hub)

- **Fable:** ruled dot question **B** — new `catalyst` standard factor
  (`source: cobalt, tier: judgment`) plus desk-graded fill of the two
  existing hollow `market_alignment`/`sector_alignment` dots (L7 shadow
  run required before they go solid); structure (float/SI/dilution/
  offerings/halts) is not a fourth dot — it only ever subtracts, so it
  enters as deterministic caps on `catalyst` plus named warnings; math:
  documents set a ceiling, analyst score moves the grade under that
  ceiling at an 0.8 haircut, an offering-only story caps at 3, inference
  never scores 0 (floor keeps it counted, never zero-weighted per ruling
  4); WHY line shows the pair `desk 8→6`; flags two tensions for the hub
  — no seat has a proven network fetch today (design reads
  workspace-only, defers live fetch to an S2 proof step), and putting a
  cross-house seat in the grading chain sits against L25 ("not
  load-bearing in Phase 1") — raised as an explicit OPEN item, not
  resolved unilaterally.
- **Astra / Grok:** DESIGN.md + OPEN.md delivered per spec — substance not
  yet compared here; reconciliation is R2's job, not the hub's.

### Hub fact-check (L35, factual verification not design judgment)

Grok's R1 `DESIGN.md` claimed proven live fetches this round (EDGAR Atom,
PR Newswire RSS, GlobeNewswire RSS, NASDAQ halt RSS, X). The hub grepped
`grok/r1-stdout.log` (12964 bytes, Grok's own `--output-format json`
capture) for any URL, domain, or tool-call record: none found — the file
contains only the model's narrated "thought"/"text" claims, no structured
tool invocation or fetch evidence. Flagged, not adjudicated, in R1's hub
entry. Grok's own R2 `MERGED.md` independently recanted the claim after
reading the other two seats ("Recanted R1's 'this session fetched, so the
job may fetch.' Production is hub collectors → workspace bundle → analyst
reads CWD") — self-corrected before the hub needed to intervene. Treated
as converged, not escalated.

---

## STEP 2 — R2

Codex meter probe before R2: exit 0, matched known-answer 310, no
usage-limit text — Astra cleared on time.

Each seat received the other two's `DESIGN.md`/`OPEN.md` (already
readable at their default/granted paths — Fable via its `--add-dir`
workspace-root grant, Astra/Grok via default unrestricted read) plus its
own, and wrote `MERGED.md` (one merged A–I design, verbatim dissent
quoted in place, no vote).

| seat | launch line | exit | start | end | wall-clock |
|---|---|---|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 --permission-mode acceptEdits --permission-prompts none --allowedTools "Read" "Edit(.../fable/*)" --disallowedTools "Bash" --add-dir /Users/cobalt/Vault --add-dir .../tribunal-analyst-2026-09-14 < prompt-r2-fable.md` | 0 | 10:49:32 | 10:58:36 | 9m04s |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r2-astra.md)" < /dev/null` | 0 | 10:49:34 | 10:56:07 | 6m33s |
| Grok | `grok -p "$(cat prompt-r2-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto --output-format json` | 0 | 10:49:35 | 10:56:36 | 7m01s |

### R2 file verification (L35)

| seat | MERGED.md |
|---|---|
| Fable | 50134 bytes |
| Astra | 50652 bytes |
| Grok | 57470 bytes |

All three exist and are non-empty. **R2 COMPLETE.**

### R2 substance, one line per seat (self-reported, not re-litigated by the hub)

- **Fable:** withdrew three R1 positions on read of the other two —
  missing computed dot now suppresses card score (not silent mean-drop,
  matching the prior tribunal's own settled rule), `catalyst` shadows in
  S2 alongside the two alignment dots (all three flip to live together at
  one S3 HITL, since a new dot in the conviction mean is itself an L7
  trading-logic change), an uncited analyst score is N/A not floored at 1,
  one name per spawn (not five), ten-session/thirty-pair shadow (not
  five), checker at every release (not nightly only). Held its ceiling +
  0.8-haircut math and its `cobalt-degraded` = dead-feed (not
  inference-contributed) reading against both other seats, dissent quoted
  inline.
- **Astra:** wrote `MERGED.md` with A–I order and 29 machine-verified
  verbatim dissent quotations (script cross-checked each quote against
  the source file:line before writing); explicit "no unverified fetch is
  claimed as proven."
- **Grok:** held rule B and the Tesla-surface standard across all three
  seats unanimously; recanted its own R1 fetch claim (see hub fact-check
  above); adopted Astra's baseline+haircut math over its own R1
  product-of-haircuts and over Fable's 0.8-ceiling form, dissenting from
  both on that point; held out against Fable on live-`catalyst`-in-S2 vs.
  shadow-only, and against Astra on the n≥30 gate and full-pool-pass
  envelope.

---

## STEP 3 — R3 (final round, no R4)

Codex meter probe before R3: exit 0, matched known-answer 310, no
usage-limit text — Astra cleared on time.

Each seat received all three `MERGED.md`, picked a base (own or
another's), stated required edits, and quoted remaining dissent verbatim
in `FINAL.md`.

| seat | launch line | exit | start | end | wall-clock |
|---|---|---|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 --permission-mode acceptEdits --permission-prompts none --allowedTools "Read" "Edit(.../fable/*)" --disallowedTools "Bash" --add-dir /Users/cobalt/Vault --add-dir .../tribunal-analyst-2026-09-14 < prompt-r3-fable.md` | 0 | 11:00:04 | 11:04:30 | 4m26s |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r3-astra.md)" < /dev/null` | 0 | 11:00:05 | 11:02:58 | 2m53s |
| Grok | `grok -p "$(cat prompt-r3-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto --output-format json` | 0 | 11:00:06 | 11:16:16 | 16m10s |

### R3 file verification (L35)

| seat | FINAL.md |
|---|---|
| Fable | 16182 bytes |
| Astra | 11455 bytes |
| Grok | 14225 bytes |

All three exist and are non-empty. **R3 COMPLETE. Tribunal closed — no R4.**

### Base adoption

| seat | base adopted |
|---|---|
| Fable | `grok/MERGED.md` |
| Astra | `astra/MERGED.md` (own) |
| Grok | `grok/MERGED.md` (own) |

`grok/MERGED.md` is adopted by two seats (Fable, Grok). **Design of
record: `grok/MERGED.md`, as amended by both seats' R3 edits (the two
edit sets converge almost completely — see below).** Astra held its own
base alone; its R3 dissents are recorded unchanged, not resolved by the
hub.

### Hub fact-check on a safety-relevant OPEN item (L35, factual not design)

Grok's FINAL item 17 (credential-path reads) cites the launcher
diagnostic's side-by-side table, which the hub re-verified directly:
Grok's `workspace` sandbox profile defaults to **unscoped filesystem
read** (`inputs/grok-launcher-diag-2026-09-14.md` §5 table — "whole
filesystem (default)"), scoping only *write* to CWD. No test in the
diagnostic specifically exercises whether the analyst job can be denied
read access to a credential path (e.g. `.env`, VaultManager's own store)
— the diagnostic proves unscoped read exists, not that it was probed
against a secret. This is a genuine open safety question tied to L4
(`inputs/LAWS.md:36-38`, secrets discipline), correctly surfaced, loosely
cited — the hub is not resolving it, only confirming the underlying fact
is real and not fabricated.

## FINAL — design of record, plain language (≤1 page)

**The dot ruling (all three seats, unanimous, R1 through R3): rulings
item 10, option B.** One new standard factor `catalyst` (the story behind
the move, source quality, structural risk) joins the validator-enforced
trio on every trade_def. The desk also grades the two already-existing
hollow standard dots, `market_alignment` and `sector_alignment`, from its
own regime/sector read. Trader override is kept on all three. Structure
(float, short interest, dilution, offerings, halts) is **not** a fourth
dot — it only ever subtracts, so it enters as deterministic caps on
`catalyst`'s grade plus named warning flags, not more semaphore. All
three desk dots carry `source: cobalt` / `cobalt-degraded`, `tier:
judgment` — shadow (hollow, human-visible but not counted) through S2,
one HITL flip into conviction together in S3, per L7.

**B — the analyst's job.** The Grok CLI seat fetches nothing itself in
production: it is a workspace-in / `packet.json`-out Cobalt job, reading
a bundle a hub collector already fetched and proved (EDGAR, PR wires,
official halt feed, X as context-only, never a grading input). No seat's
R1 claim of a live fetch this tribunal round survived scrutiny — see the
hub fact-check above; Grok's own R2/R3 recanted it. Regime/sector read
draws on several sources beyond Vital Dawn (which the seats confirm does
not give the full picture) and renders in the card's existing detail/
reasons slot — no new widget. The analyst never proposes a trade, a
price target, or an invented filing.

**C — the packet.** Closed schema. Every fact needs a locator, a bytes
hash, and a verbatim quote, or it's labelled inference, not fact. Cobalt
derives the evidence class (filing/PR/wire/none) from the evidence kind,
not the model's say-so. Freshness is tracked per-dependency (filing age,
halt age, coverage age), not one blanket packet TTL. A required computed
dot that's missing renders N/A, never a guessed mid-value; an unsupported
score is null, never a ceremonial 5.

**D — the math, Cobalt-owned.** `raw = (3×class_baseline +
analyst_judgment)/4 − 0.5`, one rounding after caps. Class sets the
baseline (confirmed filing 8, PR 7, wire 6); an empty completed search
prints a flat 1 ("no catalyst in scope"); a *failed* search (couldn't
search) stays N/A, never conflated with "no catalyst". Inferred linkage
is labelled in the WHY line but does not collapse the baseline — the
design-of-record base reversed its own earlier R2 haircut after Fable
showed it would print a fresh, confirmed 8-K down to amber. Caps: offering/
dilution story 3, source conflict 4, halt-with-no-facts 2. Inference is
never worth zero, per ruling 4. Colour bands 1–3 red / 4–6 amber / 7–10
green; WHY line ≤90 chars, template `desk {a}→{b}`.

**E — warnings.** Named condition codes (dilution explains the tape, halt
with no facts, offering as the only story, stale news, X-only rumour, and
more) render in the card's existing warning space — no new chip UI.
Dilution/offering warnings require the analyst's own *supported causal*
inference, not just the presence of an offering. DM fires once, on
transition only (enter/clear), never on every grade tick; Grokbot never
sends one.

**F — the event model.** Three triggers, one deterministic evaluator, no
LLM in the watch loop: a scheduled full-pool pass (07:20/08:20 ET, after
the market-open checkpoints; noon meter-conditional), on-admission, and
news-first — a cheap, zero-token Cobalt listener (EDGAR, PR wires, the
halt feed, Grok's X lane) that on a hit runs the analyst on that name now,
recomputes its dots and conviction, re-ranks, and can admit a
not-yet-in-pool name with `source: news:` on `radar_membership`. Every
hit produces the full artifact set: a Postgres row, a board unit update,
a Grokbot outbox entry, and (if warnings changed) a DM. 15-second event
coalescing; a halt is never held back.

**G — the job.** Grok CLI as a Cobalt job: one issuer per spawn, two
concurrent workers, a bounded retry then fallback to a `claude -p`
seat, 180s timeout, credential isolation proven *before* the first live
packet, credentials held by the hub not the model (L41). New tables
`system.desk_packet` / `desk_grade` / `desk_regime` sit beside the
already-settled seam (`radar_score_run` / `radar_score` / `radar_board_v`
— no `candidates.json`, no invented `system.scans`). Per-run meter cost
is genuinely unmeasured — a ten-name probe is the first S2 step, no
top-ups assumed. Grokbot reads the outbox view-only, on a second Grok
meter, answering "why" cheaply — it never scores, never sends. Outbox
transport is a pasted file until an L24 dead-drop is proven.

**H — audit.** Every release gets an independent, deterministic,
zero-token recompute of every dot from its packet by a different house
than the one that wrote it — mismatch blocks. A daily spot review of the
*inference* (not just the arithmetic) covers ten packets or all of them
if fewer, plus every newly raised severe warning (halt-no-facts,
dilution-explains-tape), auditor house rotating weekly. Promotion out of
shadow needs ten sessions, thirty graded pairs per dot, median |Δ| ≤ 1,
≥90% of pairs within 2 — then an L7 HITL token, not an automatic flip.

**I — MVP slice.** S2 (→ 09-23): packets, warnings, shadow grades (not
yet in conviction), the listener logging hits, on-admission trigger, a
scoped Grokbot outbox. S3 (→ 10-07): live news-first admission, the L7
HITL promotion that puts all three dots into conviction together, DMs on
warning transitions. Nothing in this design touches the card except
these three dots' grades, WHY lines, and warnings — ranking, sizing, and
the card layout are untouched (ruling 1, out of scope, not reopened).

### OPEN FOR DEJAN (hub-compiled from all three FINAL.md, deduplicated, simple first; recommendation named where the design-of-record base and/or majority favors one side)

1. Accept the B ruling above as written? **A** accept (unanimous
   recommendation) / B send back with a named objection.
2. Alignment grading before any trade_def authors expectations: **A**
   default direction map — dot reads "with/flat/against" the checkpoint's
   sign vs. the card's own long/short direction, so the shadow run starts
   day one (Fable+Grok, design of record) / B N/A until you author
   per-trade expectations, whether or not the shadow clock has started
   (Astra dissents).
3. `source` label on an inferred desk dot: **A** `cobalt-degraded` only
   when a needed feed is down or stale, `tier: judgment` alone carries
   the inference label (Fable+Grok) / B `cobalt-degraded` any time
   inference contributes to the number, even with all feeds live (Astra
   — "deterministic arithmetic does not make its inputs deterministic").
4. Catalyst/alignment formula: **A** `raw=(3×class_baseline+judgment)/4
   −0.5`, class sets the baseline, inferred linkage is labelled but never
   collapses the baseline (Fable+Grok, design of record, reversing an
   earlier draft) / B haircut inferred linkage toward the no-story
   baseline before the blend (Astra, and Grok's own R1/R2 draft before it
   reversed).
5. L8 (n≥30) on these three desk dots specifically: **A** L8 governs EV/
   auto-grade in the expectancy sense only — dots display 1–10 with WHY
   regardless of sample size (Fable+Grok) / B literal gate — the numeric
   display itself is blanked ("insufficient data") until n≥30 (Astra,
   citing L8's plain text).
6. Shadow/promotion bar before HITL: **A** ten sessions, thirty graded
   pairs per dot, median |Δ|≤1, ≥90% within 2 (all three propose this
   number, unresolved whether it's final) / B a different bar — name it.
7. Scheduled-pass cadence: **A** two checkpoint-triggered full-pool
   passes (07:20 + 08:20 ET), noon meter-conditional (Fable+Grok) / B
   three fixed full-pool passes, 07:15 / 08:45 / 12:00, as a binding
   envelope regardless of meter (Astra).
8. Daily inference spot-review volume and auditor rotation: **A** ten
   packets/day or all if fewer, plus every newly-raised severe warning,
   weekly rotation (Fable+Grok converged in R3) / B five/day,
   risk-directed sample, monthly rotation (Fable's own earlier R2
   position, not fully withdrawn by all seats).
9. Packet staleness handling: **A** per-dependency freshness — a stale
   grade stands, marked "stale", until `PACKET_STALE_MIN` (Fable+Grok) /
   B any expired *required* dependency suppresses the fresh grade
   outright; the prior value survives only as clearly-labelled history
   (Astra).
10. Where does a `news:`-admitted name sit in the pool's existing
    `priority: [screens, lists]` order (`inputs/radar-schema.md`)? A
    ahead of screens / B after lists — not addressed by rulings-2026-09-14.
11. New desk-only tables (`system.desk_packet`/`desk_grade`/
    `desk_regime`) now, or hold: **A** add them now, beside the settled
    seam, so the lane is auditable before the card table itself is
    inspected (Fable+Grok) / B hold until the physical card `dots[]`
    column/table is actually inspected in the schema — building ahead of
    that inspection risks a second, competing shape (Astra).
12. Grokbot outbox transport: **A** pasted `desk-outbox.json` until an
    L24 dead-drop is proven / B build the L24 dead-drop now, before first
    live use.
13. Second Grok meter for Grokbot: **A** a separate account with its own
    allowance / B the same login as the analyst job, budget-shared.
14. **Safety item, hub-verified real (see fact-check above):** the Grok
    CLI's `workspace` sandbox profile defaults to *unscoped filesystem
    read* — proven in the launcher diagnostic, not merely claimed. No
    test yet confirms whether a credential path (`.env`, VaultManager's
    store) can be read by an analyst-job spawn. A do not launch the first
    live packet job until this is tested and, if needed, scoped down
    (ties to L4) / B launch on the current `workspace` profile as-is and
    record the exposure as accepted risk.
15. Is the desk lane load-bearing under L25, or advisory: **A** stays
    advisory — a required-but-N/A desk dot nulls `card_score` post-
    promotion (not a halt on every WATCH card pre-promotion), outage is
    loud and bounded with a fallback house / B declare it load-bearing
    now.
16. Who authors the `catalyst` line inside each trade_def note: **A** you
    author it / B Cobalt drafts it for your approval.
17. Empty-search ("NONE") grading: **A** always prints a flat 1 on every
    trade_def / B allow a specific trade_def to invert that (e.g. "no
    news is itself bullish" setups).
18. DM firing rule: **A** on both entering and clearing a warning / B on
    entering only.
19. Tunable numeric defaults for S2 (haircut/freshness windows,
    `PACKET_TTL`, `PACKET_STALE_MIN`, `NEWS_RUNS_PER_HOUR`,
    `JOB_TIMEOUT_S` 180, colour cutoffs 1-3/4-6/7-10,
    `OFFERING_WINDOW_D` 5, `SHELF_WINDOW_D` 90, `FLAT_PCT` 0.15) — under
    L53, Dejan's to set: **A** accept the proposed defaults as S2 starting
    values / B set your own before S2 starts.

**Caution for the fold:** items 2–9 are the substantive design fights —
Astra held a materially different, tighter-gated position alone through
all three rounds (never picked up by either other seat as a 2-vs-1), so
"design of record" here means the base two seats converged on, not a
settled cross-house agreement the way the prior ranking tribunal reached
one on every gate clause. Dejan is ruling a real, live disagreement on
items 2–9, not rubber-stamping consensus.

TRIBUNAL: R3 COMPLETE | WAITING none · DESIGN OF RECORD: grok/MERGED.md
(adopted by Fable + Grok, as amended by both seats' R3 edits) · OPEN
ITEMS: 19 · ESCALATE: none
