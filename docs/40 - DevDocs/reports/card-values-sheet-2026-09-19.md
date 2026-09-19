# Card values sheet — 09-19 values session (`card.proposed_key` / `card.curves`)

Read-only research for the desk. Every claim below is file:line-sourced; `facts.md` in
`docs/40 - DevDocs/prompts/2026-09-19/23-packet/` is treated as a claim to verify, not settled
fact, per its own instruction. No trading value is invented — where nothing is found, it says so.

## 1. Schema (`src/cobalt/settings/card.py`)

- **`ProposedKeyBands`** (card.py:85–100): `a_plus_min`, `a_min`, `b_min`, `c_min` — each `Decimal`,
  `ge=0, le=1`. `model_validator` `_descending` (card.py:94–100) refuses unless
  `a_plus_min > a_min > b_min > c_min` strictly. These are thresholds on **conviction**
  (`mean(tapped trader grades)/10`, `cards/scoring.py:238-244`), not on any single dot.
- **`CurveAnchor`** (card.py:103–105): `x: Decimal` (unbounded), `grade: Decimal, ge=1, le=10`.
- **`Curve`** (card.py:108–133): `anchors: tuple[CurveAnchor,...]`, `min_length=2`. A before-validator
  (card.py:113–123) accepts the file's `[[x, grade], ...]` list shorthand. After-validator
  `_increasing` (card.py:125–130) refuses unless `x` is strictly increasing.
- **`card.curves`** = `dict[str, Curve]` keyed by factor name (card.py:153) — one curve per
  `quality_factors[]` name that needs one.
- **`AlignmentDefault`** (card.py:136–140): `with_grade`/`flat_grade`/`against_grade` (`int, ge=1,
  le=10`), `flat_pct` (`Decimal, ge=0`) — all four required together (no partial object).
  **Dark-only-optional; NOT checked by the `cards_enabled=true` gate at all** (no validator
  references it, card.py:157–169) **and NOT read by the running evaluator at all**:
  `src/cobalt/radar/evaluate.py` `desk_shadow()` hardcodes `DEFAULT_UNRULED` for both alignment
  dots regardless of what (or whether) this setting holds any value (packet excerpt
  `src-radar-evaluate-desk_shadow.py`, matching `facts.md` §2). Null is fully acceptable live —
  the code path that would consume it does not exist yet.
- **`ShadowPromotionBar`** (card.py:143–147): `sessions`/`pairs` (`int, gt=0`), `median_max`
  (`Decimal, ge=0`), `within2_min` (`Decimal, ge=0, le=1`). Dark-only-optional for the
  `cards_enabled` gate, but **required** by `cobalt cards shadow-report`
  (`src/cobalt/cards/shadow_report.py:147-152`, refuses loud if `None`) — needed for the L7
  agreement gate later, not for Monday's switch.
- **The actual enable-gate** — `CardSettings._enabled_needs_bands_and_curves` (card.py:157–169):
  when `cards_enabled=True`, both `proposed_key` and `curves` must be non-`None` or it raises
  `ValueError(f"radar.cards_enabled=true requires {missing}: an enabled radar with no bands or
  curves would publish keys and grades nobody set")`. Confirmed live against the module by the
  packet's own run (`facts.md` §0): the drafted `23-packet/p2-live-settings.yaml`
  (`cards_enabled: true` + `shadow_promotion_bar` only) is **refused** with exactly that message.
- Also refused: unknown top-level keys, `card.dot.*`/`card.health.*` tunables, and the 7
  sheet/day-mode `SETTING_KEYS` (card.py:259-273); any extra field inside a sub-object
  (`ConfigDict(extra="forbid")`, card.py:81-82).

**Minimal valid shapes — SYNTHETIC-SHAPE-ONLY, not proposed values:**
```yaml
card.proposed_key: {a_plus_min: 0.90, a_min: 0.80, b_min: 0.60, c_min: 0.40}
card.curves:
  rvol: [[1, 1], [10, 10]]
```
(A `curves` dict with even one factor satisfies the enable-gate; per-factor sparse coverage is a
separate, non-blocking degrade — see §2.)

## 2. Meaning (from `src/cobalt/cards/scoring.py`)

- **`proposed_key`** (scoring.py:273–286, `proposed_key()`): given the card's current conviction
  (tap-derived, 0–1, no taps → `None`), find the **highest** `card.proposed_key` band the
  conviction meets (A+ → A → B → C), then snap that grade down to an enabled key via
  `aset.engine.snap_down` — **the same function the key-tap sizing path uses**, so the highlighted
  proposal can never suggest a key the tap would refuse. No conviction → "tap to propose". It is a
  per-card, per-scan **display hint** next to the tap strip, computed once per card, never a gate
  on any action.
- **`card.curves`** (scoring.py:118–135 `grade_from_curve`, 144–198 `compute_dots`): for each
  **computed** `quality_factors[]` entry (`source: cobalt`/`cobalt-degraded`, `tier: deterministic`
  — everything else is a human/judgment dot, hollow, curve-irrelevant), the raw measured value
  (RVOL, ATRs-from-open, etc.) is passed through that factor's named curve — piecewise-linear
  between anchors, flat beyond the ends, clipped 1–10, rounded half-up once — to a 1–10 shadow
  grade. **Per factor, per trade_def** (keyed by name, not global).
- **No curve for a factor** → `na_reason: "curve_unset"` (scoring.py:184-190): that one dot shows
  the raw engine value but no grade — a **per-dot degrade**, not a file-level refusal. It does not
  block `radar.cards_enabled=true` (only a wholly-`None` `curves` dict does that) and does not
  block the card from forming or scoring on its other dots.
- **Which variables need a curve, for real, on Monday:** only **one** of the six radar trade_defs
  is wired to form cards in S2 — Rubberband (the formation/detector code in
  `src/cobalt/radar/evaluate.py` matches Rubberband's anatomy exactly: `Extension.culminating`,
  `bar_break`, `snapback_candle`). The other five (Back$ide, Fashionably Late, Hitchhiker, Second
  Chance, Big Dog) are **S3-scoped detectors, not built yet**
  (`docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md` §7 Carried: "S3: detectors for Back$ide,
  Fashionably Late, Hitchhiker, Second Chance, Big Dog"), so they form no cards regardless of what
  `card.curves` holds. Rubberband's real Definition unit (`/Users/cobalt/Vault/Think/1 - Trading/4
  - Strategies/Rubberband.md:88-103`) marks exactly **four** `quality_factors[]` entries
  `source: cobalt, tier: deterministic`: `atrs_from_open` (:89), `rvol` (:90),
  `Extension.leg_count` (:94), `htf_level_proximity` (:95) — identical to the shipped test fixture
  `tests/cobalt/radar_p2_support.py:71-81`. A fifth, `trail_fit` (Rubberband.md:100), is also tagged
  `source: cobalt` but has no computer written yet — `compute_dots` (scoring.py:168-170) always
  renders it `na_reason: "MANUAL"` regardless of `card.curves` content (R5, draft-only in P2). So:
  **4 curves matter for Monday** — `atrs_from_open`, `rvol`, `Extension.leg_count`,
  `htf_level_proximity`. The remaining Rubberband factors (`last_leg_range_and_volume_expansion`,
  `snapback_bar_volume_rank`, `pause_bar_in_cleared_set`, `htf_level_significance`,
  `prior_session_rehearsal`, `short_interest_float`, `range_wick_ratio`) are plain human/judgment
  dots (bare strings → `source: human` by default, `configs/cobalt/taxonomy/examples/
  example_trade_def.md`'s own documented default) — hollow, tap-only, no curve applies.

## 3. What depends on them during the shadow — nothing that moves money

- **Sizing/dollars**: `POST /radar/card/{id}/key {grade}` sizes off the **tapped** grade through
  `snap_down(tapped, enabled)` and `dollars_for(sheet_mode_today, sized)`
  (`plan-s2-p2-excerpt-step5-10.md:20`) — not off `card.curves` or `card.proposed_key`. `ACCEPT`/
  `ARM` use the pre-existing `/card/{id}/move`, gated on a non-null **tapped** grade
  (`plan-s2-p2-excerpt-step5-10.md:26`).
- **Dots**: every judgment-role dot renders hollow regardless of any engine computation
  (`facts.md` §5); a computed dot's role is **`shadow`** always in S2 — its grade is stored and
  shown, but explicitly excluded from `conviction`, which is `mean(tapped grades)/10` only
  (`scoring.py:16-27,238-244`).
- **`card_score`** = `round(conviction × proximity × 100)` — `conviction` is tap-only, so a
  curve's number cannot move `card_score` unless/until a curve tribunal + L7 run promotes that dot
  out of shadow (owed, unscheduled — plan §8 ESCALATE item 1).
- **`proposed_key`** is a same-screen suggestion next to the tap strip; it never fires an action —
  the trader's own tap is what writes `grade`/`risk_budget`/`shares`.
- **What DOES change with these settings**: only the engine's own recorded number beside his tap —
  the `desk shadow: n` text mirrored into a dot's reason (`plan-s2-p2-2026-09-15.md:204`) and the
  `card_dot_taps.engine_grade_at_tap` value that `"user".shadow_agreement_v` aggregates
  (`facts.md` §5) — **which is exactly what the three shadow mornings exist to measure.** No alert,
  no page, no Mattermost DM is wired to card formation or scoring (`facts.md` §5, not exhaustively
  verified against every line of `notify/`, flagged not asserted).

## 4. Sources for starting values — already his

| Value needed | Existing source | Implied value | Verdict |
|---|---|---|---|
| `card.proposed_key` bands (a_plus/a/b/c on 0–1 conviction) | `0 - Inbox/tribunal-grok-2026-09-14/fable/RECONCILE.md:402` lists `proposedKey conviction bands` as an open ⚑ value in the 09-14 tribunal itself; never resolved since — `plan-s2-p2-2026-09-15.md` §7 Carried: "**Dejan:** … values for `card.proposed_key` and `card.curves`" | — | **NONE FOUND** |
| `card.curves` — `atrs_from_open` | `Rubberband.md:89` — `{name: atrs_from_open, source: cobalt, tier: deterministic}  # sheet >3 guide` | a "≥3 = strong" guide number, not a ruled curve anchor pair | GUIDE ONLY, not a ruling |
| `card.curves` — `rvol` | `Rubberband.md:90` — `{name: rvol, source: cobalt, tier: deterministic}  # sheet 5+ guide; factor not gate` | a "≥5 = strong" guide number; the comment itself says "factor not gate" | GUIDE ONLY, not a ruling |
| `card.curves` — `Extension.leg_count` | none found (Rubberband.md:94 carries no guide comment) | — | **NONE FOUND** |
| `card.curves` — `htf_level_proximity` | none found (Rubberband.md:95 carries no guide comment) | — | **NONE FOUND** |
| `card.dot.red_max`/`amber_max` (tunables, not this ask) | `plan-s2-p2-2026-09-15.md:206` "Colours: tunables `card.dot.red_max` 3 / `card.dot.amber_max` 6 (09-14 accepted defaults)" | 3 / 6 | RULED (context only — separate settings file, `tunables.yaml`, L53) |
| `card.shadow_promotion_bar` (not this ask, but the file's other open item) | `plan-s2-p2-2026-09-15.md:223`; `TAXONOMY-DRAFT-v0_8.md:69` — 09-14 group-2 ruling | `{sessions:10, pairs:30, median_max:1, within2_min:0.90}` | RULED (already in the drafted go-live file) |
| `card.alignment_default` | plan's own STEP-5 amendment (Astra R2-6, `plan-s2-p2-excerpt-step5-10.md:53`) rejects the only numeric source on record (10/6/4) and directs explicit N/A | — | **NONE FOUND / explicitly rejected** — leave absent (matches runtime: unread by `desk_shadow()` anyway) |

No other configs/dev/aset*.yaml, daymode.yaml, or `areas/cobalt-product-definition.md` hit
searched for RVOL/float/spread/ATR/A+/conviction thresholds produced a `card.proposed_key`- or
`card.curves`-shaped number; Finviz screener filters in `Radar Screens.md` (RVOL>3, RVOL>4,
ATR>0.5) are scan-population thresholds, a different purpose from a per-dot 1–10 grading curve,
and are not treated as a source here.

## 5. DESK PROPOSAL — not his until he says yes

The smallest complete shape the loader would accept, built only from §4's two guide numbers where
they exist; everything else is the schema's simplest legal linear form, obviously provisional.

```yaml
card.proposed_key:
  a_plus_min: 0.90   # PROVISIONAL — no ruled source (§4); matches card.py's own doc example, coincidence not authority
  a_min: 0.80        # PROVISIONAL
  b_min: 0.60        # PROVISIONAL
  c_min: 0.40        # PROVISIONAL
card.curves:
  atrs_from_open: [[0, 1], [3, 10]]        # "3" = SOURCED(Rubberband.md:89, "sheet >3 guide"); shape (0/1 low anchor, 10 at 3) PROVISIONAL
  rvol:           [[1, 1], [5, 10]]        # "5" = SOURCED(Rubberband.md:90, "sheet 5+ guide"); shape PROVISIONAL
  Extension.leg_count:   [[1, 1], [5, 10]] # fully PROVISIONAL — no guide found
  htf_level_proximity:   [[0, 1], [1, 10]] # fully PROVISIONAL — no guide found; direction (closer=higher grade?) unconfirmed
```

**Count: 2 numbers SOURCED-as-guide (the "3" and "5" thresholds); the rest — all 4 proposed_key
values and the remaining 10 curve numbers/shapes — are PROVISIONAL.** This is deliberately a
starting point, not a design: the three shadow mornings (Mon–Wed, L7) exist specifically to
compare the engine's numbers under exactly this file against his own taps and produce the
agreement stats that would justify changing it. Changing it later needs no deploy/restart — it is
the same `cobalt settings load --card <file> --sha256 <hash> --apply` path, re-read by
`CardSettingsReader.current()` on every call (card.py:232-239).

## 6. THE ASK (for the ear, ≤8 sentences)

> Two settings are blocking Monday's cards switch: `proposed_key`, which bands your tap-average
> conviction into a suggested A+/A/B/C key next to the tap strip, and `curves`, which turn four
> Rubberband numbers — ATRs from open, RVOL, leg count, and HTF-level proximity — into a 1-to-10
> shadow dot. Nothing about money, sizing, or what you have to do depends on either one during the
> shadow run: sizing comes only from your own tap, every dot stays hollow until you tap it, and
> these settings only shape the engine's own recorded number sitting beside your tap — which is
> exactly what the three shadow mornings are there to score. I have a starting proposal: two of the
> curve numbers come from guide thresholds already in your Rubberband note — ATRs greater than 3,
> RVOL 5-plus — and everything else, including all four conviction bands, is a provisional
> placeholder with no ruling behind it. Your choices: approve the proposal as the shadow's starting
> point, tell me which numbers to change, or sit a proper values session before Monday.

---
FINAL OUTPUT (digest) delivered separately to the CTO desk via SubagentHandback.
