# Grok / Chief-of-Staff design tribunal — 2026-09-14

Hub: Sonnet 5 (launches, collects, verifies file existence; never judges the
designs). Workspace: `~/tmp/tribunal-grok/{inputs,fable,astra,grok,rounds}/`
— each seat wrote only its own folder. Nothing under `~/cobalt` was written
by any seat; only this report.

## STEP 0 — inputs (all read-only; byte sizes at copy time)

| path | bytes |
|---|---|
| `inputs/LAWS.md` (whole, canonical current law) | 40102 |
| `inputs/ledger-grok-excerpt.md` (PROJECT-LEDGER.md:1327-1328) | 2516 |
| `inputs/GROKBOT_CHIEF_OF_STAFF_INSTRUCTIONS.md` | 4910 |
| `inputs/PEER_REVIEW_DESK_SPEC.md` | 6715 |
| `inputs/COS_VISUAL_AND_TWOWAY.md` | 1238 |
| `inputs/MVP-CHARTER-v0_2.md` | 29164 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/README.md` | 1722 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/card-spec.md` | 6908 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/decisions.md` | 3880 |
| `inputs/TRADE-RADAR-CARD-MOCK-v0_1/open-questions.md` | 2812 |
| `inputs/radar-schema.md` (real Postgres seam + vault rank rule) | 2763 |

Reference docs found at `docs/90 - References/` (moved off the tree
09-13, as the ledger excerpt states — absolute paths:
`/Users/cobalt/cobalt/docs/90 - References/GROKBOT_CHIEF_OF_STAFF_INSTRUCTIONS.md`,
`.../PEER_REVIEW_DESK_SPEC.md`, `.../COS_VISUAL_AND_TWOWAY.md`).

**Radar seam — DB permission note.** `cobalt db query --side system --prod`
is a real command but requires `uv run` + `COBALT_ENV=production` (not on
PATH bare) — the hub's first attempt (bare `cobalt`, then an equivalent
`docker exec cobalt_memory psql`) was wrong and the second was correctly
DENIED by the auto-mode classifier ("Production Reads"); the hub stopped
and asked Dejan rather than working around the denial (per policy). Dejan
supplied the exact command; it ran clean (read-only `information_schema`
metadata query, no row data). Result: `system.radar_pool` and
`system.radar_membership` columns are real (see `inputs/radar-schema.md`
for the full list); **no `system.scans` table exists anywhere** —
`radar_membership.opened_scan_id`/`last_scan_id`/`closed_scan_id` and
`radar_pool.last_scan_id` are FK-shaped bigint columns with nothing to
reference. This is a live instance of the exact failure class L45/the
ledger excerpt warns against (spec built against an imagined artifact),
now handed to the seats as a real, verified gap rather than an invented
one.

Pool rank rule read directly from the vault (not queried): Radar
Screens.md:225-243, unit `radar-pool` — `cap: 50`, `priority: [screens,
lists]`, `rank_metric` by session (premarket/rth/aftermarket =
volume/rvol/volume), overrides for `morning_low_float` and `day_scan`,
`stickiness_scans: 3`.

## Codex meter probe (L47, before R1)

```
cd ~/tmp/tribunal-grok/astra && codex exec --skip-git-repo-check \
  "Run: wc -l LAWS.md -- reply with only the number." < /dev/null
```
Exit 0. Model `gpt-6-astra`, sandbox `read-only` (probe only — R1 itself
ran `-s workspace-write`). Ran `wc -l` itself, replied `310`, matching the
known-answer. No usage-limit text anywhere in the output. **Astra cleared
to launch on time; no wait-exception triggered.**

## STEP 1 — R1 launches

Identical prompt to all three seats (`prompt-r1-common.md`, copied into
each seat's own workspace with the Grok-only addendum appended for Grok),
citing every STEP 0 input by path.

| seat | launch line | exit | start | end | wall-clock |
|---|---|---|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 --permission-mode acceptEdits --permission-prompts none --allowedTools "Read" "Edit(.../fable/*)" "Write(.../fable/*)" --disallowedTools "Bash" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/tmp/tribunal-grok < prompt-r1-fable.md` | 0 | 08:38:26 | 08:46:55 | 8m29s |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r1-astra.md)" < /dev/null` (cwd astra/) | 0 | 08:38:30 | 08:42:32 | 4m02s |
| Grok | `grok -p "$(cat prompt-r1-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto --output-format json` | 0 | 08:38:35 | 08:48:37 | 10m02s |

Non-fatal note: Fable's launch printed an advisory that its
`Write(path)` allow-rule isn't matched by file permission checks (only
`Edit(path)` rules are) — it proceeded and wrote both files via the Edit
path regardless; flagged here, not treated as a failure since both
artifacts exist and are non-empty.

### R1 file verification (L35 — hub verified existence + non-empty size directly, never took a seat's own claim)

| seat | DESIGN.md | OPEN.md |
|---|---|---|
| Fable | 22475 bytes | 6822 bytes |
| Astra | 21921 bytes | 3803 bytes |
| Grok | 21315 bytes | 3912 bytes |

All six files exist and are non-empty. **R1 COMPLETE.**

### R1 substance, one line per seat (from each seat's own recap, not re-litigated by the hub)

- **Fable:** sourced-only scoring (MODELLED fields weight-zero, shown under
  a badge, promoted only via L7 shadow run); one ranking authority
  `card_score` (conviction × proximity) fed by the existing volume/RVOL
  pool rank; new seam `system.radar_score_run` + `system.radar_score` +
  view `system.radar_board_v`, no `candidates.json`; audit = independent
  recompute + ablation test; Grokbot = Outbox reader only, never a writer.
- **Astra / Grok:** DESIGN.md + OPEN.md delivered per spec — substance not
  yet compared here; reconciliation is R2's job, not the hub's.

---

## STEP 2 — R2

Codex meter probe before R2: exit 0, matched known-answer 310, no
usage-limit text — Astra cleared on time.

Each seat received the other two's `DESIGN.md`/`OPEN.md` (already
readable at their default/granted paths, no copying needed) plus its own,
and wrote `RECONCILE.md` (AGREE/DISAGREE per gate clause + merged
proposal, no vote).

| seat | launch line | exit | start | end | wall-clock |
|---|---|---|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 --permission-mode acceptEdits --permission-prompts none --allowedTools "Read" "Edit(.../fable/*)" --disallowedTools "Bash" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/tmp/tribunal-grok < prompt-r2-fable.md` | 0 | 08:50:11 | 09:00:13 | 10m02s |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r2-astra.md)" < /dev/null` | 0 | 08:50:18 | 08:53:56 | 3m38s |
| Grok | `grok -p "$(cat prompt-r2-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto --output-format json` | 0 | 08:50:24 | 08:59:04 | 8m40s |

### R2 file verification (L35)

| seat | RECONCILE.md |
|---|---|
| Fable | 56903 bytes |
| Astra | 20556 bytes |
| Grok | 38961 bytes |

All three exist and are non-empty. **R2 COMPLETE.**

### R2 substance — hub's procedural (not design-judging) scan for 2-vs-1 splits

Grepped all three `RECONCILE.md` for DISAGREE clauses. Disagreement is
dense across nearly every gate clause, but three clusters show a clean
2-vs-1 pattern (two seats independently reject the same third-seat
position), which is what triggers R3 per the STEP 3 rule:

1. **Gate (b), ranking authority.** Astra: the pool's live volume/RVOL
   rank should be the sole authority reaching the card, retiring
   conviction×proximity (`astra/DESIGN.md:7`, `:59-62`). Fable
   (`fable/RECONCILE.md:49`) and Grok (`grok/RECONCILE.md:45`) both
   independently DISAGREE and keep conviction×proximity as the
   card-score formula, treating the pool rank as admission/membership
   authority only.
2. **Seam location/tenancy.** Astra proposes a new user-side evidence
   snapshot table and/or blocks the seam pending producer-transaction
   inspection (`astra/DESIGN.md:67-93`). Fable (`fable/RECONCILE.md:84,
   88`) and Grok (`grok/RECONCILE.md:69-73`) both independently hold the
   seam on the `system` side, against the real schema in
   `radar-schema.md`, with no new tenancy split.
3. **Second grading-letter vocabulary.** Fable cuts any letter beyond the
   card's own `proposedKey` entirely (`fable/DESIGN.md:179`). Astra and
   Grok each keep some form of a research letter (different formulas/
   gates) — a 2-vs-1 on whether one survives at all, even though the two
   "yes" positions don't fully agree with each other on its shape.

## STEP 3 — R3 (final round, in progress)

Codex meter probe before R3: exit 0, matched known-answer, no
usage-limit text — Astra cleared on time.

Each seat received all three `RECONCILE.md`, told the three 2-vs-1
clusters above, and asked for a final ≤2-page `FINAL.md`: final position
per cluster + any other remaining DISAGREE, verbatim dissent, no vote,
closing with SETTLED / OPEN FOR DEJAN lists. This is the last round — no
R4.

| seat | launch line | start |
|---|---|---|
| Fable | `claude -p --model claude-fable-5-1 ... < prompt-r3-fable.md` | (in progress) |
| Astra | `codex exec --skip-git-repo-check -s workspace-write "$(cat prompt-r3-astra.md)" < /dev/null` | (in progress) |
| Grok | `grok -p "$(cat prompt-r3-grok.md)" --cwd .../grok --sandbox workspace --permission-mode auto` | (in progress) |

### R3 launch/exit/wall-clock

| seat | exit | start | end | wall-clock |
|---|---|---|---|---|
| Fable | 0 | 09:01:39 | 09:04:57 | 3m18s |
| Astra | 0 | 09:01:44 | 09:04:06 | 2m22s |
| Grok | 0 | 09:01:49 | 09:06:59 | 5m10s |

### R3 file verification (L35)

| seat | FINAL.md |
|---|---|
| Fable | 11360 bytes |
| Astra | 6970 bytes |
| Grok | 8128 bytes |

All three exist and are non-empty. **R3 COMPLETE. Tribunal closed — no R4.**

### R3 outcome: the three flagged 2-vs-1 clusters all converged to full 3-way SETTLED

- **Ranking authority:** Astra explicitly withdrew its R1 pool-rank-as-authority
  position (`astra/FINAL.md`: "adopt the peers' argument, reaffirming R2... my
  R1 repeal is withdrawn"). All three: `card_score = round(conviction ×
  proximity × 100)` is the sole card authority; pool rank is
  admission/membership only.
- **Seam location:** Astra withdrew its user-side evidence-snapshot proposal
  (`astra/FINAL.md`: "withdraw the separate user-side radar snapshot and
  identity-FK prerequisite"). All three: new score tables sit on the
  `system` side beside `radar_pool`/`radar_membership`.
- **Second letter vocabulary:** Grok explicitly reversed
  (`grok/FINAL.md`: "I am persuaded by Fable R2 and Astra R2. Cut `Research
  A|B|C/Pass` / `size_label` entirely"). All three: one letter, the card's
  own `proposedKey` — no second research-grade vocabulary.
- **Bonus convergence not originally flagged:** all three also converged on
  missing-required-computed-dot handling (`card_score` suppressed/null, not
  0, not silently renormalized — with a trader-tap escape hatch), and Astra
  dropped its pool-rank-replay (`RANK_UNVERIFIED`) publication block.

**Caution for the fold:** each seat's own self-reported "OPEN FOR DEJAN"
list still names some of the above as open (stale relative to that same
seat's more careful body-text position a few paragraphs earlier in its own
`FINAL.md`). The hub is reporting the body-text convergence as the more
reliable signal, but is NOT overriding the seats' own list — flagging the
discrepancy for Dejan rather than resolving it.

## Consolidated OPEN items for Dejan (deduplicated across all three FINAL.md; hub compiled, did not adjudicate)

1. **n≥30 gate on F10 computable dot grades** — Astra: L8 applies, n<30
   suppresses any auto-grade including dots. Fable + Grok: L8 governs
   EV/auto-grade in the expectancy sense; F10 ratifies dots 1–10 with no n
   attached; genuinely still 2-vs-1, unresolved in R3.
2. **Do the three new formulas (activity/catalyst/room) ever enter
   conviction, or are they audit/WHY-only always?** Fable: they enter
   conviction when a `trade_def` lists that variable. Grok: audit/WHY only,
   never rank. Astra silent on this specific split. Unresolved.
3. **Per-release house review of research/evidence releases** — Astra wants
   every new research release reviewed by another house before publication;
   Fable holds a narrower gate (hub schema verification + review only on
   formula-version change or spot audit). Tied to whether Dejan puts the
   research/evidence lane in MVP or post-MVP at all (Fable's R2 finding:
   no primary-document collector exists in the MVP feed list today).
4. **`MODELLED` as a formal fourth card-face owner badge** — Fable wants it
   proposed as a v0.2 card-spec amendment; Grok says the existing detail/
   audit mark is enough, no new badge. Both explicitly defer this to
   Dejan's card-spec call, not a tribunal ruling.
5. **Producer-transaction-boundary / identity-PK proof at publication time**
   — Astra's residual ask (softened from a DDL blocker to a publication-time
   proof requirement: "publication must prove a coherent generation, scoped
   latest-run selection and complete card projection"); Fable/Grok treat it
   as a plain migration caution, not a gate. Narrower than R2's version but
   still open.
6. **Tunable numeric constants, Dejan's to set under L53** (not a house
   disagreement — inputs needed): gap/ATR thresholds, dot red/amber
   cutoffs, `FOCUS_N`, `proposedKey` score bands, `radar.input_max_age_s`,
   `radar.board_refresh`, `radar.score_retention_days`,
   `AUDIT_RUNS_PER_WEEK` + auditor rotation.
7. **Build-time unknowns no seat could settle from the given inputs** (facts
   to verify, not design disagreements): whether a card table exists in the
   DB and on which side; `system.bars` and `session_blocks` column lists;
   whether the Finviz export carries a news/catalyst field; the L28 writer
   entry point for a new `radar-board` unit; whether a Grok CLI job can
   reach `vaultwrite` per L41's interim (hub-runs-DB-stage) clause.
8. **Board unit home and Grokbot transport** — daily note vs a dedicated
   note for the `radar-board` unit; whether Grokbot receives data by paste
   or an L24 dead-drop path. Minor, flagged by Fable only.

## Where this leaves the design

All four L52 gate clauses have a converged, cross-house-agreed answer:
(a) sourced/MODELLED separation with weight-zero degradation for modelled
inputs (all three); (b) one ranking authority, `card_score` =
conviction × proximity, pool rank = admission only (all three, after R3);
(c) real seam = new `system.radar_score_run` / `system.radar_score` tables
beside the real `radar_pool`/`radar_membership`, no `candidates.json`, no
invented `scans` table (all three); (d) cross-house audit = frozen bundle,
independent other-house recompute, deterministic and zero-token, modelled
values excluded from the ablation-invariance check (all three). The eight
items above are what's left for Dejan to rule before a build ticket is
cut — this proposal now clears L52/the ledger's STANDING gate as a design,
not a stepping stone, modulo those eight rulings.

TRIBUNAL: R3 COMPLETE · OPEN ITEMS: 8 · ESCALATE: none
